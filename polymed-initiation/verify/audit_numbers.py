"""Numeric traceability audit for the built report.

1. Every fact used in the report is re-found on its cited page (value or snippet) in sources/text/<doc>.txt.
   [visual read] facts are listed for manual spot-check instead.
2. Derived facts are recomputed from their inputs.
3. The rendered HTML has no untraced number: after removing number tokens (<span class="n">), any digit left
   in visible text must match a whitelist (years, fiscal labels, exhibit/section numbers, dates, identifiers).
Usage: python3 verify/audit_numbers.py [report.html]
"""
import json, os, re, sys
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

facts = {}
for line in open("ledger/facts.jsonl"):
    r = json.loads(line)
    facts[r["fact_id"]] = r
used = json.load(open("report/used_facts.json"))
page_cache = {}


def page_text(doc, page):
    key = (doc, page)
    if key in page_cache:
        return page_cache[key]
    p = f"sources/text/{doc}.txt"
    if not os.path.exists(p):
        page_cache[key] = None
        return None
    t = open(p, errors="ignore").read()
    m = re.search(rf"=== \[{re.escape(doc)} p\.{page}\] ===\n(.*?)(?=\n=== \[|\Z)", t, re.S)
    page_cache[key] = m.group(1) if m else None
    return page_cache[key]


def norm(s):
    s = str(s).lower()
    s = re.sub(r"(\d)\s+(\d)", r"\1\2", s)   # CRISIL split digits
    s = re.sub(r"(\d)['\u2019](\d{3})", r"\1\2", s)   # Swiss/Italian thousands 17'237
    return re.sub(r"[\s,₹]+", "", s)


def value_forms(v):
    forms = {norm(v)}
    try:
        x = float(str(v).replace(",", "").replace("+", "").replace("~", "").replace("%", ""))
        forms |= {norm(f"{x:.1f}"), norm(f"{x:.2f}"), norm(f"{x:,.0f}") if abs(x - round(x)) < 1e-9 else norm(f"{x}"),
                  norm(f"{x:,.1f}"), norm(f"{x:,.2f}")}
        if x < 0:  # accounts print negatives in brackets
            forms |= {norm(f"({abs(x):,.0f})"), norm(f"{abs(x):,.0f}"), norm(str(int(round(abs(x))))) if abs(x - round(x)) < 1e-9 else norm(f"{abs(x)}")}
        if abs(x - round(x)) < 1e-9:
            forms.add(norm(str(int(round(x)))))
            if abs(x) >= 1000:  # European grouping 17.237
                forms.add(norm(f"{int(round(x)):,}".replace(",", ".")))
    except ValueError:
        pass
    return {f for f in forms if f}


def main():
    html_path = sys.argv[1] if len(sys.argv) > 1 else "report/Poly_Medicure_Initiating_Coverage.html"
    fail, visual, ok, nosrc = [], [], 0, []
    for fid in used:
        r = facts.get(fid)
        if r is None:
            fail.append((fid, "unknown fact"))
            continue
        if r["doc_id"] == "DERIVED":
            continue
        if "[visual read]" in (r.get("note") or ""):
            visual.append(fid)
            continue
        pt = page_text(r["doc_id"], r["page"])
        if pt is None:
            nosrc.append(fid)
            continue
        npt = norm(pt)
        if any(f in npt for f in value_forms(r["value"])):
            ok += 1
            continue
        sn = norm(r.get("snippet", ""))
        if sn and sn[:60] in npt:
            ok += 1
            continue
        fail.append((fid, f"value '{r['value']}' not found on {r['doc_id']} p.{r['page']}"))
    # derived recompute
    dfail = []
    for fid in used:
        r = facts.get(fid)
        if r and r["doc_id"] == "DERIVED":
            env = {}
            for ref in r.get("inputs", []):
                env[ref.replace("-", "_")] = facts[ref]["value_std"]
            expr = re.sub(r"([A-Z]{1,3})-(\d{4})", r"\1_\2", r["snippet"])
            try:
                v = eval(expr, {"__builtins__": {}}, env)
                if abs(round(v, 1) - float(r["value"])) > 0.051 * max(1, abs(v)) and abs(v - float(r["value"])) > 0.06:
                    dfail.append((fid, v, r["value"]))
            except Exception as e:
                dfail.append((fid, str(e), r["value"]))
    # untraced numbers in HTML
    soup = BeautifulSoup(open(html_path).read(), "html.parser")
    MON = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*"
    WL = [
        r"\b[A-C]\d{1,2}(\.\d{1,2})?\b",                       # section ids A4.1 (first)
        r"\b\d{1,2}-\d{1,2} " + MON + r" \d{4}\b",              # 7-10 Aug 2026
        r"\b\d{1,2}[- ]" + MON + r"[- ]\d{4}\b",              # 23 Sep 2025, 1-Apr-2026 (before years)
        r"\b\d{1,2}[- ]" + MON + r"\b",                        # 23 Sep
        r"\b(19|20)\d{2}-\d{2}\b",                             # 2025-26
        r"\bExhibit \d+:?|\bExhibits? \d+(-\d+)?\b",
        r"\bFY\d{2}-(FY)?\d{2}\b|\bCY\d{2}-(CY)?\d{2}\b|\b[1-4]?[QH]?FY\d{2}(E)?\b|\b9MFY\d{2}\b|\bFY\d{2}/FY\d{2}\b|\bCY\d{2}\b|\b[1-4]QCY\d{2}\b|\b[12]H\b",
        r"\b\d{3}\(k\)s?",                                    # 510(k)
        r"\b[A-Za-z]+\d+[A-Za-z][\w']*|\bPlan1\b|\bQ\d{2}\b|\bPolyMed \d\.0\b",   # identifiers
        r"\b[A-Z][A-Z_]*\d+[A-Z0-9_]*\b|\bpp?\.\s?\d+(-\d+)?\b",   # document ids and page refs in citations
        r"\bForm \d+s?\b|\bHS( code)? ?\d{4,8}\b|\b\d+(\.\d+)?\s?(mL|ml|mm|cm|Fr|kV)\b|\bPhase[- ]\d\b",
        r"\b1Lattice\b|\b[Tt]op-?10\b|\bany 12 months\b|\b\d{1,2}-month\b|\bin 10 points\b|\bmore than \d+ days overdue\b|\bThe \d+ must-ask\b|\bAll \d+ questions\b|\bthe 10% disclosure\b",
        r"\b(19|20)\d{2}\b",                                   # years
    ]

    def strip_wl(t):
        for p in WL:
            t = re.sub(p, " ", t)
        return t

    def nums_in(t):
        return [float(x.replace(",", "")) for x in re.findall(r"\d[\d,]*\.?\d*", t)]

    # 1) exhibit captions: a number is traced if it matches (after rounding) a sourced value shown in the exhibit
    for fig in soup.select("figure.exh"):
        cap = fig.find("figcaption")
        if not cap:
            continue
        pool = []
        for sp in fig.select("span.n, [data-tip]"):
            pool += nums_in(sp.get_text(" ") + " " + (sp.get("data-tip") or ""))
        for td in fig.select("details.tv td"):
            pool += nums_in(td.get_text(" "))
        def ok_num(x):
            return any(abs(x - v) <= max(0.51, 0.02 * abs(v)) or abs(x - round(v)) < 0.51 for v in pool)
        txt = strip_wl(cap.get_text(" "))
        for m in re.finditer(r"~?\d[\d,]*\.?\d*", txt):
            try:
                x = float(m.group(0).lstrip("~").replace(",", ""))
            except ValueError:
                continue
            if ok_num(x) or (1990 <= x <= 2035):
                txt = txt.replace(m.group(0), " ", 1)
        cap.string = txt
    # 2) rank / row-number cells (a lone small integer in the first column of a data table)
    for tr in soup.select("table.data tr"):
        cells = tr.find_all(["td", "th"])
        if cells and re.fullmatch(r"\s*\d{1,2}\s*", cells[0].get_text()):
            cells[0].string = " "
    for s in soup.select(".qindex td.num, .qindex h4"):
        s.decompose()
    for s in soup.select("span.n, script, style, .src, table.bib, svg, details.tv, nav, .qid"):
        s.decompose()
    for h in soup.find_all(["h1", "h2"]):
        h.insert(0, f" §§{h.get('id', '?')}§§ ")
    text = soup.get_text(" ")
    WL = WL + [
        r"\b[A-C]\d{1,2}(\.\d{1,2})?\b",                       # section ids A4.1
        r"\bK\d{6}\b|\bHS ?\d{4,8}\b|\b\d{4,8}\b(?= \(HS)|\bISO ?\d+(:\d{4})?\b|\bEN ?\d+\b",
        r"\b(Reg\.|Regulation|Directive|Notification|G\.S\.R\.|Section|s\.|Para|Rule|No\.)\s?[\d/().A-Za-z-]+",
        r"\b\d{4}/\d{2,4}(/EU)?\b|\b\d{2,4}/\d{4}\b",
        r"\bPart [A-C]\b|\bPhase [0-9]\b|\bClass [A-D]\b|\bClass (I|II|III)\b|\bTarget Segment \d\b",
        r"\b\d+(st|nd|rd|th)\b",
        r"\b[1-9]\)\s", r"^\s*\d+\.\s",
        r"\b\d+G\b|\b\d+F\b|\b\d{1,2}G x\b",                    # gauges, French sizes
        r"\bCOVID-19\b|\bIEEPA\b|\b\d+@\d+\b",
    ]
    rest = text
    for p in WL:
        rest = re.sub(p, " ", rest)
    leftovers = []
    marks = [(m.start(), m.group(1)) for m in re.finditer(r"§§([^§]*)§§", rest)]
    for m in re.finditer(r"[^\s]*\d[^\s]*", rest):
        s = m.group(0)
        if "§§" in s:
            continue
        sec = "?"
        for pos, sid in marks:
            if pos < m.start():
                sec = sid
            else:
                break
        ctx = rest[max(0, m.start() - 50): m.end() + 30].replace("\n", " ")
        ctx = re.sub(r"§§[^§]*§§", " ", ctx)
        leftovers.append((s, f"[{sec}] {ctx}"))
    print(f"facts used: {len(used)} | re-found: {ok} | visual-read (manual check): {len(visual)} | "
          f"no source text: {len(nosrc)} | FAILED: {len(fail)} | derived mismatches: {len(dfail)} | "
          f"untraced numbers in HTML: {len(leftovers)}")
    for f in fail[:80]:
        print("FAIL", *f)
    for f in dfail[:40]:
        print("DERIVED", *f)
    for s, ctx in leftovers[:120]:
        print("UNTRACED", repr(s), "…", ctx.strip(), "…")
    json.dump({"visual": visual, "fail": fail, "nosrc": nosrc, "untraced": leftovers},
              open("verify/audit_result.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
