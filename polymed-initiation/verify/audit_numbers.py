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
    return re.sub(r"[\s,₹]+", "", s)


def value_forms(v):
    forms = {norm(v)}
    try:
        x = float(str(v).replace(",", "").replace("+", "").replace("~", "").replace("%", ""))
        forms |= {norm(f"{x:.1f}"), norm(f"{x:.2f}"), norm(f"{x:,.0f}") if abs(x - round(x)) < 1e-9 else norm(f"{x}"),
                  norm(f"{x:,.1f}"), norm(f"{x:,.2f}")}
        if abs(x - round(x)) < 1e-9:
            forms.add(norm(str(int(round(x)))))
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
    for s in soup.select("span.n, script, style, .src, table.bib, svg, details.tv, nav"):
        s.decompose()
    text = soup.get_text(" ")
    WL = [
        r"\b(19|20)\d{2}\b",                                   # years
        r"\b[1-4]?[QH]?FY\d{2}(E)?\b|\b9MFY\d{2}\b|\bFY\d{2}-\d{2}\b|\bFY\d{2}/FY\d{2}\b|\bCY\d{2}\b|\b[1-4]QCY\d{2}\b",
        r"\bExhibit \d+\b|\bExhibits? \d+(-\d+)?\b",
        r"\b[A-C]\d{1,2}(\.\d{1,2})?\b",                       # section ids A4.1
        r"\b\d{1,2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b",
        r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[- ]\d{4}\b",
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
    for m in re.finditer(r"[^\s]*\d[^\s]*", rest):
        s = m.group(0)
        ctx = rest[max(0, m.start() - 50): m.end() + 30].replace("\n", " ")
        leftovers.append((s, ctx))
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
