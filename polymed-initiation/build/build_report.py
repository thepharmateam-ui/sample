"""Build the self-contained HTML report (and the plant-visit question-bank companion).

Drafts: draft/*.md in filename order. Markdown with these extensions:
  {{FACT_ID}} or {{FACT_ID|fmt}}   -> house-style number with a source tooltip (fmt: bn, mn, approx, signed,
                                      num, pct, raw, plain)
  ::: chart {json} :::              -> numbered exhibit with inline SVG, legend, table view, source line
  ::: table title="..." [note="..."] <markdown table> :::   -> numbered exhibit (table)
  ::: callout title="..." [kind=...] <markdown> :::         -> aside box
  ::: snapshot title="..." <key | value lines> :::          -> business-line snapshot box
  [[EXREF:id]]                      -> "Exhibit N" cross-reference
No number may be typed into prose; the audit enforces it.
"""
import glob, html, json, os, re, sys
from collections import OrderedDict
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "build"))
import svgcharts as sc  # noqa: E402

AS_OF = "24 Sep 2026"
FACTS = {}
USED = OrderedDict()          # fact_id -> True (order of first use)
EXH = OrderedDict()           # exhibit id -> number
PENDING_EXREF = []


def load_facts():
    with open("ledger/facts.jsonl") as fh:
        for line in fh:
            r = json.loads(line)
            FACTS[r["fact_id"]] = r


def doc_label(r):
    t = r.get("doc_title") or r["doc_id"]
    return t


def tooltip(r):
    if r["doc_id"] == "DERIVED":
        parts = []
        for ref in r.get("inputs", []):
            x = FACTS.get(ref)
            if x:
                parts.append(f"{x['display']} ({doc_label(x)}, p.{x['page']})")
        return "Our calculation: " + r.get("snippet", "") + ("; inputs: " + "; ".join(parts) if parts else "")
    pg = r.get("page")
    loc = f"slide/page {pg}" if str(pg) not in ("", "0", "1") or r["doc_id"].startswith(("DK", "RS", "AR", "PD")) else ""
    base = f"{doc_label(r)}" + (f" ({r['doc_date']})" if r.get("doc_date") else "") + (f", {loc}" if loc else "")
    extra = []
    if r.get("basis") == "guidance":
        extra.append("management guidance")
    if r.get("basis") == "third_party" and r.get("tier") in ("5", "6"):
        extra.append("third-party estimate")
    if r.get("speaker"):
        extra.append(r["speaker"])
    return "Source: " + base + (" · " + "; ".join(extra) if extra else "")


def fmt_fact(fid, fmt=""):
    r = FACTS.get(fid)
    if r is None:
        raise KeyError(f"unknown fact {fid}")
    USED[fid] = True
    disp = r["display"]
    vs, us = r.get("value_std"), r.get("unit_std")
    for f in [x for x in fmt.split(",") if x]:
        if f == "bn" and us == "Rs mn" and vs is not None:
            disp = f"Rs. {vs / 1000:,.1f}bn"
        elif f == "mn" and us == "Rs mn" and vs is not None:
            disp = f"Rs. {vs:,.0f}mn"
        elif f == "approx":
            disp = "~" + disp.lstrip("~")
        elif f == "signed" and vs is not None:
            disp = ("+" if vs > 0 else "") + disp if not disp.startswith(("+", "-")) else disp
        elif f == "num" and vs is not None:
            dec = 0 if abs(vs - round(vs)) < 1e-9 else 1
            disp = f"{vs:,.{dec}f}"
        elif f == "abs":
            disp = disp.lstrip("-+")
        elif f == "raw":
            disp = f"{r['value']} {r['unit']}".strip()
        elif f == "plain":
            disp = str(r["value"])
        elif f == "range":
            disp = fmt_range(r)
    tip = html.escape(tooltip(r)).replace("|", "&#124;")
    return f'<span class="n" title="{tip}">{html.escape(disp)}</span>'


def fmt_range(r):
    """Render a printed range/approximate text value in house style: '30-32%', 'Rs. 10.8-10.9bn', '5-10%'."""
    txt = str(r["value"])
    nums = [float(x.replace(",", "")) for x in re.findall(r"\d[\d,]*\.?\d*", txt)]
    if not nums:
        return r["display"]
    unit = r.get("unit", "")
    is_cr = "crore" in txt.lower() or unit.lower() in ("rs cr", "inr cr")
    is_pct = "%" in txt or unit == "%"
    is_bps = "bps" in txt.lower() or unit == "bps"
    def f(x, dec=None):
        if dec is None:
            dec = 0 if abs(x - round(x)) < 1e-9 else 1
        return f"{x:,.{dec}f}"
    if is_cr:
        mn = [x * 10 for x in nums]
        if max(mn) >= 1000:
            def fb(x):
                v = x / 1000
                return f"{v:,.1f}" if abs(v * 10 - round(v * 10)) < 1e-6 else f"{v:,.2f}"
            parts = [fb(x) for x in mn]
            return f"Rs. {'-'.join(dict.fromkeys(parts))}bn"
        return f"Rs. {'-'.join(dict.fromkeys(f(x, 0) for x in mn))}mn"
    joined = "-".join(dict.fromkeys(f(x) for x in nums))
    plus = "+" if re.search(r"\bplus\b|\+|upwards|over |north of|above|more than", low if (low := txt.lower()) else "") and len(nums) == 1 else ""
    if is_pct:
        return joined + "%" + plus
    if is_bps:
        return joined + "bps"
    low = txt.lower()
    scale = "bn" if ("billion" in low or " bn" in low) else ("mn" if ("million" in low or " mn" in low or "mn" in unit.lower()) else "")
    if unit.upper().startswith("USD") or "usd" in low or "$" in txt:
        return "$" + joined + (scale or "mn")
    if unit.upper().startswith("EUR") or "eur" in low or "€" in txt:
        return "€" + joined + (scale or "mn")
    return joined


TOKEN = re.compile(r"\{\{([A-Z]{1,3}(?:-[0-9A-Za-z_]+)+)(?:\|([a-z,]+))?\}\}")


def sub_tokens(text):
    return TOKEN.sub(lambda m: fmt_fact(m.group(1), m.group(2) or ""), text)


def sources_line(fids, extra=""):
    docs = OrderedDict()
    for f in fids:
        r = FACTS.get(f)
        if not r:
            continue
        if r["doc_id"] == "DERIVED":
            for ref in r.get("inputs", []):
                x = FACTS.get(ref)
                if x:
                    docs[doc_label(x)] = True
            docs["our calculation"] = True
        else:
            docs[doc_label(r)] = True
    names = "; ".join(docs.keys())
    return f'<p class="src">Source: {html.escape(names)}{("; " + html.escape(extra)) if extra else ""}; Avendus Spark Research</p>'


def exh_number(eid):
    if eid not in EXH:
        EXH[eid] = len(EXH) + 1
    return EXH[eid]


def val_of(fid, scale=None):
    r = FACTS[fid]
    USED[fid] = True
    v = r.get("value_std")
    if v is None:
        raise ValueError(f"fact {fid} not numeric: {r['value']}")
    if scale == "bn" and r.get("unit_std") == "Rs mn":
        return v / 1000
    if scale == "mn" and r.get("unit_std") == "Rs mn":
        return v
    return v


def render_chart(spec):
    eid = spec["id"]
    n = exh_number(eid)
    cats = spec["cats"]
    scale = spec.get("scale")
    series, all_fids = [], []
    for s in spec["series"]:
        vals, tips = [], []
        for j, f in enumerate(s["facts"]):
            if f in (None, "", "-"):
                vals.append(None)
                tips.append(None)
                continue
            v = val_of(f, scale)
            if spec.get("negate"):
                v = -v
            vals.append(v)
            all_fids.append(f)
            r = FACTS[f]
            tips.append(f"{cats[j]} · {s['name']}: {r['display']}")
        series.append({"name": s["name"], "values": vals, "tips": tips})
    kind = spec["type"]
    unit = spec.get("unit", "")
    dec = spec.get("dec", 1)
    if kind in ("column", "stacked_column"):
        svg = sc.column_chart(cats, series, unit=unit, stacked=kind == "stacked_column", dec=dec,
                              height=spec.get("height", 300), label_last=spec.get("label_last", True),
                              label_all=spec.get("label_all", False), totals=spec.get("totals", False))
    elif kind in ("hbar", "stacked_hbar", "share_hbar"):
        svg = sc.hbar_chart(cats, series, unit=unit, stacked=kind == "stacked_hbar", share=kind == "share_hbar",
                            dec=dec, label_w=spec.get("label_w", 190))
    elif kind == "line":
        svg = sc.line_chart(cats, series, unit=unit, dec=dec, height=spec.get("height", 280), ymin=spec.get("ymin"))
    else:
        raise ValueError(kind)
    # table view
    th = "".join(f"<th>{html.escape(str(c))}</th>" for c in cats)
    rows = []
    for s, sd in zip(spec["series"], series):
        cells = []
        for j, f in enumerate(s["facts"]):
            cells.append(f"<td>{fmt_fact(f) if f not in (None, '', '-') else '–'}</td>")
        rows.append(f"<tr><th scope=\"row\">{html.escape(s['name'])}</th>{''.join(cells)}</tr>")
    table = (f'<details class="tv"><summary>Data table</summary><div class="tw"><table class="data">'
             f'<thead><tr><th></th>{th}</tr></thead><tbody>{"".join(rows)}</tbody></table></div></details>')
    note = f'<p class="note">{sub_tokens(html.escape(spec["note"], quote=False))}</p>' if spec.get("note") else ""
    return (f'<figure class="exh" id="exh-{eid}"><figcaption><span class="exn">Exhibit {n}:</span> '
            f'{html.escape(spec["title"])}</figcaption><div class="plot">{svg}</div>{note}'
            f'{sources_line(all_fids, spec.get("src_extra", ""))}{table}</figure>')


LIST_RE = re.compile(r"^(\s*)([-*]|\d+[.)])\s+")


def fix_lists(text):
    """Insert the blank line Python-Markdown needs before a list, and normalise nested indents to 4 spaces."""
    out, prev = [], ""
    for line in text.split("\n"):
        m = LIST_RE.match(line)
        if m:
            ind = len(m.group(1).expandtabs(4))
            if 0 < ind < 4:
                line = "    " + line.lstrip()
            elif 4 < ind < 8:
                line = "        " + line.lstrip()
            pm = LIST_RE.match(prev)
            if prev.strip() and not pm and not prev.lstrip().startswith(("|", "<", ":::")) and not prev.startswith("    "):
                out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def md(text):
    return markdown.markdown(fix_lists(text), extensions=["tables", "attr_list", "sane_lists", "md_in_html"])


def render_table_block(attrs, body):
    eid = attrs.get("id") or f"t{len(EXH) + 1}"
    n = exh_number(eid)
    fids = TOKEN.findall(body)
    inner = md(sub_tokens(body))
    inner = inner.replace("<table>", '<div class="tw"><table class="data">').replace("</table>", "</table></div>")
    note = f'<p class="note">{sub_tokens(html.escape(attrs["note"], quote=False))}</p>' if attrs.get("note") else ""
    return (f'<figure class="exh" id="exh-{eid}"><figcaption><span class="exn">Exhibit {n}:</span> '
            f'{html.escape(attrs.get("title", ""))}</figcaption>{inner}{note}'
            f'{sources_line([f for f, _ in fids], attrs.get("src_extra", ""))}</figure>')


def parse_attrs(s):
    return dict(re.findall(r'(\w+)="([^"]*)"', s))


BLOCK = re.compile(r"^:::\s*(chart|table|callout|snapshot)([^\n]*)\n(.*?)^:::\s*$", re.S | re.M)


def process_blocks(text):
    def rep(m):
        kind, attrs_s, body = m.group(1), m.group(2), m.group(3)
        attrs = parse_attrs(attrs_s)
        if kind == "chart":
            spec = json.loads(body)
            return "\n\n" + render_chart(spec) + "\n\n"
        if kind == "table":
            return "\n\n" + render_table_block(attrs, body) + "\n\n"
        if kind == "callout":
            k = attrs.get("kind", "note")
            t = attrs.get("title", "")
            return (f'\n\n<aside class="callout {k}">' + (f"<p class=\"ct\">{html.escape(t)}</p>" if t else "")
                    + md(sub_tokens(body)) + "</aside>\n\n")
        if kind == "snapshot":
            items = []
            for line in body.strip().splitlines():
                if "|" in line:
                    k, v = line.split("|", 1)
                    items.append(f"<div><dt>{html.escape(k.strip())}</dt><dd>{md(sub_tokens(v.strip()))[3:-4]}</dd></div>")
            t = attrs.get("title", "Snapshot")
            return f'\n\n<section class="snapshot"><p class="ct">{html.escape(t)}</p><dl>{"".join(items)}</dl></section>\n\n'
        return m.group(0)
    return BLOCK.sub(rep, text)


def slug(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:60] or "s"


def add_heading_ids(h):
    seen = {}
    toc = []

    def rep(m):
        lvl, attrs, inner = m.group(1), m.group(2) or "", m.group(3)
        idm = re.search(r'id="([^"]+)"', attrs)
        hid = idm.group(1) if idm else slug(inner)
        if hid in seen:
            seen[hid] += 1
            hid = f"{hid}-{seen[hid]}"
        else:
            seen[hid] = 1
        if lvl in ("1", "2"):
            toc.append((int(lvl), hid, re.sub(r"<[^>]+>", "", inner)))
        attrs = re.sub(r'\s*id="[^"]+"', "", attrs)
        return f'<h{lvl} id="{hid}"{attrs}>{inner}</h{lvl}>'
    h = re.sub(r"<h([1-3])([^>]*)>(.*?)</h\1>", rep, h, flags=re.S)
    return h, toc


def align_numeric_columns(body):
    """Right-align header cells of columns whose body cells are mostly numeric."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(body, "html.parser")
    for t in soup.select("table.data"):
        head = t.find("thead")
        if not head:
            continue
        ths = head.find_all("th")
        rows = t.find("tbody").find_all("tr") if t.find("tbody") else []
        for ci, th in enumerate(ths):
            cells = []
            for tr in rows:
                tds = tr.find_all(["td", "th"])
                if ci < len(tds):
                    cells.append(tds[ci])
            if cells and sum(1 for c in cells if "num" in (c.get("class") or [])) >= 0.6 * len(cells):
                th["class"] = (th.get("class") or []) + ["num"]
                for c in cells:
                    if c.name == "td" and c.get_text(strip=True) in ("–", "-", "n.a.", "nd"):
                        c["class"] = (c.get("class") or []) + ["num"]
    return str(soup)


def bibliography():
    docs = OrderedDict()
    for fid in USED:
        r = FACTS[fid]
        ids = [r["doc_id"]] if r["doc_id"] != "DERIVED" else [FACTS[x]["doc_id"] for x in r.get("inputs", []) if x in FACTS]
        for d in ids:
            x = next((FACTS[k] for k in USED if FACTS[k]["doc_id"] == d), None)
            docs[d] = x
    rows = []
    for d, x in sorted(docs.items(), key=lambda kv: (kv[1].get("doc_date", "") if kv[1] else ""), reverse=True):
        if not x:
            continue
        url = x.get("doc_url", "")
        if url and not url.startswith("http"):
            if url.startswith("BSEMIRROR:"):
                url = "https://bsmedia.business-standard.com/_media/bs/data/announcements/bse/" + url.split(":", 1)[1]
            else:
                url = "https://www.polymedicure.com/wp-content/uploads/" + url
        link = f'<a href="{html.escape(url)}">{html.escape(url[:90])}{"…" if len(url) > 90 else ""}</a>' if url else ""
        rows.append(f"<tr><td class=\"mono\">{html.escape(d)}</td><td>{html.escape(x.get('doc_title') or d)}</td>"
                    f"<td>{html.escape(x.get('doc_date') or '')}</td><td class=\"url\">{link}</td></tr>")
    return ('<div class="tw"><table class="data bib"><thead><tr><th>ID</th><th>Document</th><th>Date</th><th>Location</th>'
            '</tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")


def build(out_path, draft_files, companion=False):
    USED.clear()
    EXH.clear()
    parts = []
    for f in draft_files:
        t = open(f).read()
        t = process_blocks(t)
        t = sub_tokens(t)
        parts.append(t)
    body_md = "\n\n".join(parts)
    body = md(body_md)
    # exhibit cross references
    body = re.sub(r"\[\[EXREF:([\w-]+)\]\]",
                  lambda m: f'<a href="#exh-{m.group(1)}">Exhibit {EXH.get(m.group(1), "?")}</a>', body)
    if "[[BIBLIOGRAPHY]]" in body or "<p>[[BIBLIOGRAPHY]]</p>" in body:
        body = body.replace("<p>[[BIBLIOGRAPHY]]</p>", bibliography()).replace("[[BIBLIOGRAPHY]]", bibliography())
    body = re.sub(r'<td>(\s*(?:[~+\-–]?\s*)?<span class="n"[^>]*>[^<]*</span>\s*)</td>', r'<td class="num">\1</td>', body)
    body = re.sub(r'<td>(\s*[~+\-]?[0-9][0-9,.]*%?\s*)</td>', r'<td class="num">\1</td>', body)
    body = align_numeric_columns(body)
    body, toc = add_heading_ids(body)
    toc_html = []
    for lvl, hid, txt in toc:
        toc_html.append(f'<li class="l{lvl}"><a href="#{hid}">{html.escape(txt)}</a></li>')
    tpl = open("build/template.html").read()
    title = "Polymed Plant Visit Questions" if companion else "Poly Medicure Initiating Coverage"
    page = (tpl.replace("{{TITLE}}", title)
               .replace("{{TOC}}", "".join(toc_html))
               .replace("{{BODY}}", body)
               .replace("{{AS_OF}}", AS_OF)
               .replace("{{BODYCLASS}}", "companion" if companion else "report"))
    open(out_path, "w").write(page)
    unknown = re.findall(r"\{\{[^}]+\}\}", body)
    print(f"built {out_path}: {len(page)/1e6:.2f}MB, exhibits={len(EXH)}, facts used={len(USED)}, "
          f"unresolved tokens={len(unknown)}")
    return page


def main():
    load_facts()
    drafts = sorted(glob.glob("draft/*.md"))
    os.makedirs("report", exist_ok=True)
    build("report/Poly_Medicure_Initiating_Coverage.html", drafts)
    json.dump(list(USED.keys()), open("report/used_facts.json", "w"))
    json.dump(dict(EXH), open("report/exhibits.json", "w"))
    qb = sorted(glob.glob("draft/companion/*.md"))
    if qb:
        build("report/Polymed_Plant_Visit_Question_Bank.html", qb, companion=True)


if __name__ == "__main__":
    main()
