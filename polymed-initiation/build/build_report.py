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
RISKS = []                    # (risk no., short name, likelihood, impact) parsed from the risk register table


DOCS = {}


def load_facts():
    with open("ledger/facts.jsonl") as fh:
        for line in fh:
            r = json.loads(line)
            FACTS[r["fact_id"]] = r
    import csv, glob as _glob
    for f in sorted(_glob.glob("registry/*.csv")):
        if os.path.basename(f) in ("wp_pdf_inventory.csv", "text_stats.csv"):
            continue
        with open(f, newline="") as fh:
            for row in csv.DictReader(fh):
                did = (row.get("doc_id") or "").strip()
                if did:
                    DOCS[did] = (row.get("title") or did).strip()


def docs_in_comment(c):
    """Doc ids cited in an HTML comment such as '<!-- AR26 p.88; PD24 pp.1-3 -->'."""
    return [d for d in re.findall(r"\b([A-Z][A-Z0-9_]*[A-Z0-9])\b", c) if d in DOCS]


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
    cls = "n nl" if len(disp) > 24 else "n"
    return f'<span class="{cls}" title="{tip}">{html.escape(disp)}</span>'


def fmt_range(r):
    """Render a printed range/approximate text value in house style: '30-32%', 'Rs. 10.8-10.9bn', '5-10%'."""
    txt = str(r["value"])
    nums = [float(x.replace(",", "")) for x in re.findall(r"\d[\d,]*\.?\d*", txt)]
    if not nums:
        return r["display"]
    unit = r.get("unit", "")
    low = txt.lower()
    is_pct = "%" in txt or unit == "%"
    is_bps = "bps" in low or unit == "bps"
    def f(x, dec=None):
        if dec is None:
            dec = 0 if abs(x - round(x)) < 1e-9 else 1
        return f"{x:,.{dec}f}"
    ul = unit.lower()
    mult = None
    if "crore" in low or ul in ("rs cr", "inr cr"):
        mult = 10.0
    elif "lakh" in low or ul in ("rs lakh", "inr lakh"):
        mult = 0.1
    elif ul in ("rs mn", "inr mn"):
        mult = 1.0
    elif ul in ("rs bn", "inr bn"):
        mult = 1000.0
    if mult is not None:
        mn = [x * mult for x in nums]
        approx = "~" if re.search(r"approx|around|about|close to|nearly|almost|roughly", low) else ""
        plus = "+" if len(nums) == 1 and re.search(r"\bover\b|more than|above|north of|\bplus\b|upwards|\+", low) else ""
        if max(abs(x) for x in mn) >= 1000:
            vals = [x / 1000 for x in mn]
            if len(vals) > 1 and all(abs(v - round(v)) < 1e-9 for v in vals):
                parts = [f"{v:,.0f}" for v in vals]  # Rs. 23-24bn
            else:
                parts = [f"{v:,.1f}" if abs(v * 10 - round(v * 10)) < 1e-6 else f"{v:,.2f}" for v in vals]
            return f"{approx}Rs. {'-'.join(dict.fromkeys(parts))}bn{plus}"
        return f"{approx}Rs. {'-'.join(dict.fromkeys(f(x, 0) for x in mn))}mn{plus}"
    joined = "-".join(dict.fromkeys(f(x) for x in nums))
    plus = "+" if re.search(r"\bplus\b|\+|upwards|over |north of|above|more than", low) and len(nums) == 1 else ""
    if is_pct:
        return joined + "%" + plus
    if is_bps:
        return joined + "bps"
    scale = "bn" if ("billion" in low or " bn" in low) else ("mn" if ("million" in low or " mn" in low or "mn" in unit.lower()) else "")
    if unit.upper().startswith("USD") or "usd" in low or "$" in txt:
        return "$" + joined + (scale or "mn") + plus
    if unit.upper().startswith("EUR") or "eur" in low or "€" in txt:
        return "€" + joined + (scale or "mn") + plus
    return joined + plus


TOKEN = re.compile(r"\{\{([A-Z]{1,3}(?:-[0-9A-Za-z_]+)+)(?:\|([a-z,]+))?\}\}")


def sub_tokens(text):
    return TOKEN.sub(lambda m: fmt_fact(m.group(1), m.group(2) or ""), text)


def sources_line(fids, extra="", cited=()):
    docs = OrderedDict()
    for d in cited:
        docs[DOCS.get(d, d)] = True
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
    parts = [html.escape(n) for n in docs.keys()] + ([html.escape(extra)] if extra else []) + ["Avendus Spark Research"]
    return f'<p class="src">Source: {"; ".join(parts)}</p>'


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
            f'{sources_line(all_fids, spec.get("src_extra", ""), spec.get("_cited", []))}{table}</figure>')


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


def parse_risk_register(body):
    """Collect (no., risk, likelihood, impact) from the register's markdown table; grades read 'H / M'."""
    rows = [r for r in body.strip().splitlines() if r.strip().startswith("|")]
    def cells_of(r):  # split on table pipes, not on the pipes inside {{FACT|fmt}} tokens
        return [c.strip() for c in re.split(r"\|(?![^{]*\}\})", r.strip().strip("|"))]
    head = [c.lower() for c in cells_of(rows[0])]
    gi = next(i for i, c in enumerate(head) if c.startswith("likelihood"))
    RISKS.clear()
    for r in rows[2:]:
        cells = cells_of(r)
        m = re.match(r"^([HML])\s*/\s*([HML])$", cells[gi])
        if m:
            RISKS.append((cells[0], cells[1], m.group(1), m.group(2)))


def render_riskgrid(attrs):
    """Likelihood x impact heat grid built from the parsed risk register, so the two cannot diverge."""
    eid = attrs.get("id", "risk_heat")
    n = exh_number(eid)
    lv = {"H": 3, "M": 2, "L": 1}
    names = {"H": "High", "M": "Medium", "L": "Low"}
    tiers = {1: ("t1", "Low"), 2: ("t1", "Low"), 3: ("t2", "Moderate"), 4: ("t2", "Moderate"), 6: ("t3", "Elevated"), 9: ("t4", "High")}
    rows = []
    for li in "HML":
        cells = [f'<th scope="row">{names[li]}</th>']
        for im in "LMH":
            cls, word = tiers[lv[li] * lv[im]]
            items = [f'<li><b>{html.escape(no)}</b> {html.escape(name)}</li>' for no, name, l, i in RISKS if l == li and i == im]
            body = f'<ul>{"".join(items)}</ul>' if items else '<p class="none">–</p>'
            cells.append(f'<td class="{cls}"><span class="tier">{word}</span>{body}</td>')
        rows.append(f'<tr>{"".join(cells)}</tr>')
    table = ('<div class="tw"><table class="riskgrid"><thead><tr><th scope="col">Likelihood ↓ / impact →</th>'
             + "".join(f'<th scope="col">{names[im]}</th>' for im in "LMH") + '</tr></thead><tbody>'
             + "".join(rows) + '</tbody></table></div>')
    legend = ('<p class="rglegend" aria-hidden="true">' + "".join(
        f'<span><i class="{c}"></i>{w}</span>' for c, w in (("t1", "Low"), ("t2", "Moderate"), ("t3", "Elevated"), ("t4", "High")))
        + '</p>')
    note = f'<p class="note">{sub_tokens(html.escape(attrs["note"], quote=False))}</p>' if attrs.get("note") else ""
    return (f'<figure class="exh" id="exh-{eid}"><figcaption><span class="exn">Exhibit {n}:</span> '
            f'{html.escape(attrs.get("title", ""))}</figcaption>{legend}{table}{note}'
            f'{sources_line([], "", attrs.get("_cited", []))}</figure>')


def render_table_block(attrs, body):
    eid = attrs.get("id") or f"t{len(EXH) + 1}"
    if eid == "risk_register":
        parse_risk_register(body)
    n = exh_number(eid)
    fids = TOKEN.findall(body)
    inner = md(sub_tokens(body))
    inner = inner.replace("<table>", '<div class="tw"><table class="data">').replace("</table>", "</table></div>")
    note = f'<p class="note">{sub_tokens(html.escape(attrs["note"], quote=False))}</p>' if attrs.get("note") else ""
    return (f'<figure class="exh" id="exh-{eid}"><figcaption><span class="exn">Exhibit {n}:</span> '
            f'{html.escape(attrs.get("title", ""))}</figcaption>{inner}{note}'
            f'{sources_line([f for f, _ in fids], attrs.get("src_extra", ""), attrs.get("_cited", []))}</figure>')


def parse_attrs(s):
    return dict(re.findall(r'(\w+)="([^"]*)"', s))


BLOCK = re.compile(r"^:::\s*(chart|table|callout|snapshot|q|riskgrid)([^\n]*)\n(.*?)^:::\s*$", re.S | re.M)
QS = []  # question-bank entries collected during a build: (num, id, theme, priority, text)
QFIELDS = [("why", "Why it matters"), ("context", "Our context"), ("listen", "Listen for"), ("follow-up", "Follow-up")]


def render_question(attrs, body):
    """A question-bank card: 'Q:', 'Why:', 'Context:', 'Listen:', 'Follow-up:' lines."""
    fields, cur = {}, None
    for line in body.strip().splitlines():
        m = re.match(r"^(Q|Why|Context|Listen|Follow-up):\s*(.*)$", line.strip(), re.I)
        if m:
            cur = m.group(1).lower()
            fields[cur] = m.group(2)
        elif cur and line.strip():
            fields[cur] += " " + line.strip()
    num = len(QS) + 1
    qid = f"Q{num:02d}"
    pri = attrs.get("priority", "")
    theme = attrs.get("theme", "")
    QS.append((num, qid, theme, pri, fields.get("q", "")))
    tags = (f'<span class="tag must">Must-ask</span>' if pri == "must" else '<span class="tag">If time permits</span>')
    tags += f'<span class="tag">{html.escape(theme)}</span>' if theme else ""
    dl = "".join(f"<dt>{lab}</dt><dd>{md(sub_tokens(fields[k]))[3:-4]}</dd>" for k, lab in QFIELDS if fields.get(k))
    return (f'<div class="qblock{" must" if pri == "must" else ""}" id="q-{qid}"><p class="qh"><span class="qid">{qid}</span>{tags}</p>'
            f'<p class="q">{md(sub_tokens(fields.get("q", "")))[3:-4]}</p><dl class="qd">{dl}</dl>'
            f'<div class="qnotes" aria-hidden="true"></div></div>')


def question_index():
    """Must-ask list and theme index, generated from the cards in this build."""
    must = [q for q in QS if q[3] == "must"]
    rows = "".join(f'<tr><td><a href="#q-{qid}">{qid}</a></td><td>{html.escape(th)}</td><td>{md(sub_tokens(t))[3:-4]}</td></tr>'
                   for _, qid, th, _, t in must)
    themes = OrderedDict()
    for _, qid, th, pri, _ in QS:
        themes.setdefault(th, []).append((qid, pri))
    def links(v):
        return ", ".join('<a href="#q-%s">%s</a>' % (q, q) for q, _ in v)
    trows = "".join(
        f'<tr><td>{html.escape(th)}</td><td class="num">{len(v)}</td><td class="num">{sum(1 for _, p in v if p == "must")}</td>'
        f'<td>{links(v)}</td></tr>' for th, v in themes.items())
    return (f'<div class="qindex"><h4>The {len(must)} must-ask questions for a short meeting</h4>'
            f'<div class="tw"><table class="data"><thead><tr><th>No.</th><th>Theme</th><th>Question</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<h4>All {len(QS)} questions by theme</h4><div class="tw"><table class="data"><thead><tr><th>Theme</th><th class="num">Questions</th>'
            f'<th class="num">Must-ask</th><th>Numbers</th></tr></thead><tbody>{trows}</tbody></table></div></div>')


def process_blocks(text):
    def rep(m):
        kind, attrs_s, body = m.group(1), m.group(2), m.group(3)
        attrs = parse_attrs(attrs_s)
        nxt = re.match(r"[ \t]*\n?[ \t]*<!--(.*?)-->", m.string[m.end():], re.S)
        cited = docs_in_comment(nxt.group(1)) if nxt else []
        if kind == "chart":
            spec = json.loads(body)
            spec["_cited"] = cited
            return "\n\n" + render_chart(spec) + "\n\n"
        if kind == "table":
            attrs["_cited"] = cited
            return "\n\n" + render_table_block(attrs, body) + "\n\n"
        if kind == "callout":
            k = attrs.get("kind", "note")
            t = attrs.get("title", "")
            return (f'\n\n<aside class="callout {k}">' + (f"<p class=\"ct\">{html.escape(t)}</p>" if t else "")
                    + md(sub_tokens(body)) + "</aside>\n\n")
        if kind == "q":
            return "\n\n" + render_question(attrs, body) + "\n\n"
        if kind == "riskgrid":
            attrs["_cited"] = cited
            return "\n\n" + render_riskgrid(attrs) + "\n\n"
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


def add_heading_ids(h, toc_levels=("1", "2")):
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
        if lvl in toc_levels:
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


def render_body(draft_files, companion=False):
    """Render the drafts to one HTML body; returns (body, toc). Resets exhibit, fact and question state."""
    USED.clear()
    EXH.clear()
    QS.clear()
    parts = []
    for f in draft_files:
        t = open(f).read()
        if companion:  # the bank reads as a standalone document in the companion
            t = t.replace("## C3 Plant-visit question bank {#c3}", "## The question bank {#c3}")
            t = t.replace("This chapter turns the open issues in this report", "This bank turns the open issues in the initiation report")
        t = process_blocks(t)
        t = sub_tokens(t)
        parts.append(t)
    body_md = "\n\n".join(parts)
    body = md(body_md)
    # exhibit cross references
    body = re.sub(r"\[\[EXREF:([\w-]+)\]\]",
                  lambda m: f'<a href="#exh-{m.group(1)}">Exhibit {EXH.get(m.group(1), "?")}</a>', body)
    if "[[QINDEX]]" in body:
        body = body.replace("<p>[[QINDEX]]</p>", question_index()).replace("[[QINDEX]]", question_index())
    if "[[BIBLIOGRAPHY]]" in body or "<p>[[BIBLIOGRAPHY]]</p>" in body:
        body = body.replace("<p>[[BIBLIOGRAPHY]]</p>", bibliography()).replace("[[BIBLIOGRAPHY]]", bibliography())
    body = re.sub(r'<td>(\s*(?:[~+\-–]?\s*)?<span class="n"[^>]*>[^<]*</span>\s*)</td>', r'<td class="num">\1</td>', body)
    body = re.sub(r'<td>(\s*[~+\-]?[0-9][0-9,.]*%?\s*)</td>', r'<td class="num">\1</td>', body)
    body = align_numeric_columns(body)
    body, toc = add_heading_ids(body, ("2", "3") if companion else ("1", "2"))
    return body, toc


def wrap_page(body, toc_html, title, pagetitle=None, companion=False, brand=None, sitelinks="", nav_top="", nav_bottom=""):
    tpl = open("build/template.html").read()
    return (tpl.replace("{{PAGETITLE}}", html.escape(pagetitle or title))
               .replace("{{BRAND}}", brand or html.escape(title))
               .replace("{{SITELINKS}}", sitelinks)
               .replace("{{TOC}}", toc_html)
               .replace("{{PAGENAV_TOP}}", nav_top)
               .replace("{{PAGENAV_BOTTOM}}", nav_bottom)
               .replace("{{BODY}}", body)
               .replace("{{AS_OF}}", AS_OF)
               .replace("{{BODYCLASS}}", "companion" if companion else "report"))


def toc_list(toc):
    return "".join(f'<li class="l{lvl}"><a href="#{hid}">{html.escape(html.unescape(txt))}</a></li>' for lvl, hid, txt in toc)


def build(out_path, draft_files, companion=False):
    body, toc = render_body(draft_files, companion)
    title = "Polymed Plant Visit Questions" if companion else "Poly Medicure Initiating Coverage"
    page = wrap_page(body, toc_list(toc), title, companion=companion)
    open(out_path, "w").write(page)
    unknown = re.findall(r"\{\{[^}]+\}\}", body)
    print(f"built {out_path}: {len(page)/1e6:.2f}MB, exhibits={len(EXH)}, facts used={len(USED)}, "
          f"unresolved tokens={len(unknown)}")
    return page


# ---------------------------------------------------------------- multipage site
REPORT_TITLE = "Poly Medicure Initiating Coverage"
HEAD_RE = re.compile(r'<h([123]) id="([^"]+)"[^>]*>(.*?)</h\1>', re.S)
SUBPAGED = {"c3"}  # chapters split further at h3 (the question bank)


def strip_tags(x):
    return html.unescape(re.sub(r"<[^>]+>", "", x)).strip()


def split_pages(body):
    """Cut the rendered body into pages: home (before the first part), one page per h2 chapter (a part's h1
    opens its first chapter), and one page per h3 inside the chapters in SUBPAGED."""
    heads = [(m.start(), int(m.group(1)), m.group(2), strip_tags(m.group(3))) for m in HEAD_RE.finditer(body)]
    pages = [{"file": "index.html", "id": "home", "title": "Summary, key facts and debates", "part": None,
              "parent": None, "start": 0}]
    part, pending, chapter = None, None, None
    for pos, lvl, hid, txt in heads:
        if lvl == 1:
            part, pending = txt, pos
        elif lvl == 2 and part is None:
            continue  # the front section's headings stay on the home page
        elif lvl == 2:
            pages.append({"file": f"{hid}.html", "id": hid, "title": txt, "part": part, "parent": None,
                          "start": pending if pending is not None else pos})
            pending, chapter = None, hid
        elif lvl == 3 and chapter in SUBPAGED:
            base = f"{chapter}-{slug(txt)}"  # named from the title, so no heading-id de-duplication suffix
            name, k = base, 2
            while any(p["file"] == f"{name}.html" for p in pages):
                name, k = f"{base}-{k}", k + 1
            pages.append({"file": f"{name}.html", "id": hid, "title": txt, "part": part,
                          "parent": chapter, "start": pos})
    for i, p in enumerate(pages):
        p["html"] = body[p["start"]: pages[i + 1]["start"] if i + 1 < len(pages) else len(body)]
    return pages


def site_toc(pages, cur):
    cur_group = cur["parent"] or cur["id"]
    def sections(p):  # in-page section links for the current page (home: its h2s; chapters: their h3s)
        lvl = "2" if p["file"] == "index.html" else "3"
        if p["id"] in SUBPAGED or p["parent"]:
            return []
        return [f'<li class="l3"><a href="#{hid}">{html.escape(strip_tags(t))}</a></li>'
                for l, hid, t in re.findall(r'<h([23]) id="([^"]+)"[^>]*>(.*?)</h\1>', p["html"], re.S) if l == lvl]
    home_act = ' class="active"' if cur["file"] == "index.html" else ""
    out = [f'<li class="l2"><a href="index.html"{home_act}>{html.escape(pages[0]["title"])}</a></li>']
    if cur["file"] == "index.html":
        out += sections(cur)
    seen_parts = set()
    for p in pages[1:]:
        if p["part"] and p["part"] not in seen_parts:
            seen_parts.add(p["part"])
            out.append(f'<li class="l1"><a href="{p["file"]}">{html.escape(p["part"])}</a></li>')
        if p["parent"]:
            if p["parent"] != cur_group:
                continue
            lvl = "l3"
        else:
            lvl = "l2"
        act = ' class="active"' if p["file"] == cur["file"] else ""
        out.append(f'<li class="{lvl}"><a href="{p["file"]}"{act}>{html.escape(p["title"])}</a></li>')
        if p["file"] == cur["file"]:
            out += sections(p)
    return "".join(out)


def page_label(p):
    return f'Question bank: {p["title"]}' if p["parent"] == "c3" else p["title"]


def page_nav(pages, i, where):
    prev = pages[i - 1] if i > 0 else None
    nxt = pages[i + 1] if i + 1 < len(pages) else None
    a = (f'<a class="prev" href="{prev["file"]}"><span>Previous</span>{html.escape(page_label(prev))}</a>' if prev
         else '<span></span>')
    b = (f'<a class="next" href="{nxt["file"]}"><span>Next</span>{html.escape(page_label(nxt))}</a>' if nxt
         else '<span></span>')
    return f'<nav class="pagenav {where}" aria-label="Chapter navigation">{a}{b}</nav>'


def directory(pages):
    """The home page's chapter directory: every page, grouped by part, with links."""
    groups = OrderedDict()
    for p in pages[1:]:
        if p["parent"]:
            continue
        groups.setdefault(p["part"] or "", []).append(p)
    out = ['<section class="dirx" id="chapters"><h2>Chapters</h2>',
           '<p class="lead">Each chapter is its own page. Use the contents list or the Previous and Next links to move '
           'between them. <a href="full-report.html">The full report on one page</a> is best for printing or searching '
           'the whole text; <a href="Polymed_Plant_Visit_Question_Bank.html">the plant-visit question bank</a> is laid '
           'out for printing and taking to the meeting.</p><div class="dirgrid">']
    for part, ps in groups.items():
        items = "".join(f'<li><a href="{p["file"]}">{html.escape(p["title"])}</a></li>' for p in ps)
        out.append(f'<div class="dircol"><p class="dirpart">{html.escape(part)}</p><ol>{items}</ol></div>')
    out.append("</div></section>")
    return "".join(out)


def build_site(out_dir, body):
    """Write one self-contained page per chapter into out_dir, with cross-page links rewritten."""
    os.makedirs(out_dir, exist_ok=True)
    pages = split_pages(body)
    id_map = {}
    for p in pages:
        for hid in re.findall(r'\bid="([^"]+)"', p["html"]):
            id_map.setdefault(hid, p["file"])
    for p in pages:
        f = p["file"]

        def rep(m, f=f):
            target = m.group(1)
            dest = id_map.get(target)
            if dest is None or dest == f:
                return m.group(0)
            return f'href="{dest}#{target}"'
        p["html"] = re.sub(r'href="#([^"]+)"', rep, p["html"])
    pages[0]["html"] += directory(pages)
    brand = f'<a href="index.html">{html.escape(REPORT_TITLE)}</a>'
    links = ('<ul class="sitelinks"><li><a href="full-report.html">Full report on one page</a></li>'
             '<li><a href="Polymed_Plant_Visit_Question_Bank.html">Question bank for printing</a></li></ul>')
    for i, p in enumerate(pages):
        page = wrap_page(p["html"], site_toc(pages, p), REPORT_TITLE,
                         pagetitle=f'{page_label(p)} · {REPORT_TITLE}' if i else REPORT_TITLE,
                         brand=brand, sitelinks=links,
                         nav_top=page_nav(pages, i, "top") if i else "", nav_bottom=page_nav(pages, i, "bottom"))
        open(os.path.join(out_dir, p["file"]), "w").write(page)
    print(f"built site {out_dir}: {len(pages)} pages")
    return pages


def zip_site(out_dir, zip_path, folder="Poly_Medicure_Initiating_Coverage"):
    import zipfile
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(os.listdir(out_dir)):
            z.write(os.path.join(out_dir, name), f"{folder}/{name}")
    print(f"zipped {zip_path}: {os.path.getsize(zip_path)/1e6:.2f}MB")


def main():
    import shutil
    load_facts()
    drafts = sorted(glob.glob("draft/*.md"))
    os.makedirs("report", exist_ok=True)
    full = "report/Poly_Medicure_Initiating_Coverage.html"
    body, toc = render_body(drafts)
    page = wrap_page(body, toc_list(toc), REPORT_TITLE)
    open(full, "w").write(page)
    unknown = re.findall(r"\{\{[^}]+\}\}", body)
    print(f"built {full}: {len(page)/1e6:.2f}MB, exhibits={len(EXH)}, facts used={len(USED)}, "
          f"unresolved tokens={len(unknown)}")
    json.dump(list(USED.keys()), open("report/used_facts.json", "w"))
    json.dump(dict(EXH), open("report/exhibits.json", "w"))
    site = "report/site"
    if os.path.isdir(site):
        shutil.rmtree(site)
    build_site(site, body)
    shutil.copy(full, os.path.join(site, "full-report.html"))
    qb = sorted(glob.glob("draft/companion/*.md")) + sorted(glob.glob("draft/52_*.md"))
    if qb:
        build("report/Polymed_Plant_Visit_Question_Bank.html", qb, companion=True)
        shutil.copy("report/Polymed_Plant_Visit_Question_Bank.html", os.path.join(site, "Polymed_Plant_Visit_Question_Bank.html"))
    zip_site(site, "report/Poly_Medicure_Initiating_Coverage_site.zip")


if __name__ == "__main__":
    main()
