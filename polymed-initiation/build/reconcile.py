"""Merge ledger shards into one fact table, standardize units, render house-style display strings,
compute derived facts and flag conflicts.

Inputs : ledger/shards/*.jsonl, ledger/derived.py (DERIVED list), registry/*.csv
Outputs: ledger/facts.jsonl (used by the build), ledger/facts.csv (for humans),
         ledger/conflicts.csv, ledger/reconcile_report.txt
"""
import csv, glob, json, math, os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

REQUIRED = ["fact_id", "metric", "entity", "segment", "geography", "period", "value", "unit",
            "basis", "doc_id", "page", "snippet"]


# ---------------------------------------------------------------- registry
def load_registry():
    docs = {}
    for f in sorted(glob.glob("registry/*.csv")):
        if os.path.basename(f) in ("wp_pdf_inventory.csv", "text_stats.csv"):
            continue
        with open(f, newline="") as fh:
            for r in csv.DictReader(fh):
                did = (r.get("doc_id") or "").strip()
                if not did:
                    continue
                docs[did] = {
                    "title": r.get("title", "").strip(),
                    "date": r.get("date", "").strip(),
                    "tier": (r.get("tier") or "").strip(),
                    "type": (r.get("type") or "").strip(),
                    "publisher": (r.get("publisher") or "Poly Medicure").strip(),
                    "url": (r.get("url") or r.get("path") or "").strip(),
                }
    docs["DERIVED"] = {"title": "Our calculation from cited figures", "date": "", "tier": "D",
                       "type": "derived", "publisher": "Our calculation", "url": ""}
    return docs


# ---------------------------------------------------------------- numbers
def to_float(v):
    """Parse a printed value to float; return None for text/ranges."""
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip()
    s = s.replace("\u2019", "").replace("'", "")  # Swiss thousands separators 13'509'871.08
    if re.fullmatch(r"-?\d{1,3}(\.\d{3}){2,}", s):  # European grouping 10.514.702
        s = s.replace(".", "")
    s2 = s.replace(",", "").replace("~", "").replace("+", "").replace("%", "").strip()
    neg = s2.startswith("(") and s2.endswith(")")
    s2 = s2.strip("()")
    try:
        x = float(s2)
        return -x if neg else x
    except ValueError:
        return None


def fmt_num(x, dec=None):
    """Format with thousands separators; dec=None keeps up to 1 decimal if not integer."""
    if dec is None:
        dec = 0 if abs(x - round(x)) < 1e-9 else 1
    return f"{x:,.{dec}f}"


UNIT_ALIASES = {
    "rs cr": "Rs cr", "rs. cr": "Rs cr", "inr cr": "Rs cr", "₹ cr": "Rs cr", "cr": "Rs cr", "rs crore": "Rs cr", "crore": "Rs cr",
    "rs lakh": "Rs lakh", "rs lakhs": "Rs lakh", "lakh": "Rs lakh", "₹ lakh": "Rs lakh",
    "rs mn": "Rs mn", "rs million": "Rs mn", "inr mn": "Rs mn", "rs bn": "Rs bn", "inr bn": "Rs bn",
    "rs": "Rs", "inr": "Rs", "₹": "Rs",
    "inr cr": "Rs cr", "inr crore": "Rs cr", "inr crores": "Rs cr", "rs crores": "Rs cr", "₹ crore": "Rs cr",
    "inr lakh": "Rs lakh", "inr lakhs": "Rs lakh", "rs lac": "Rs lakh", "inr mn": "Rs mn", "inr million": "Rs mn",
    "inr bn": "Rs bn", "inr billion": "Rs bn", "rs billion": "Rs bn", "₹ bn": "Rs bn", "₹ mn": "Rs mn",
    "usd million": "USD mn", "usd billion": "USD bn", "us$ million": "USD mn", "us$ billion": "USD bn",
    "eur million": "EUR mn", "eur billion": "EUR bn", "€ million": "EUR mn", "€m": "EUR mn", "eur thousand": "EUR k",
    "eur mn": "EUR mn", "€ mn": "EUR mn", "eur m": "EUR mn", "eur million": "EUR mn", "eur k": "EUR k",
    "eur": "EUR", "€": "EUR", "eur bn": "EUR bn",
    "usd mn": "USD mn", "$ mn": "USD mn", "us$ mn": "USD mn", "usd million": "USD mn", "usd bn": "USD bn",
    "$ bn": "USD bn", "us$ bn": "USD bn", "usd": "USD", "$": "USD", "usd k": "USD k",
    "jpy bn": "JPY bn", "jpy tn": "JPY tn", "rmb mn": "RMB mn", "cny mn": "RMB mn",
    "%": "%", "percent": "%", "pp": "pp", "bps": "bps",
    "x": "x", "days": "days", "count": "count", "units": "units", "pcs": "units", "pieces": "units",
    "mn units": "mn units", "mn pcs": "mn units", "million units": "mn units", "bn units": "bn units",
    "mn pieces": "mn units", "million pieces": "mn units", "bn pieces": "bn units", "billion units": "bn units",
    "cr units": "cr units", "crore units": "cr units", "cr pieces": "cr units", "lakh units": "lakh units",
    "text": "text",
}


def norm_unit(u):
    u0 = (u or "").strip()
    return UNIT_ALIASES.get(u0.lower(), u0)


def standardize(value, unit):
    """Return (value_std, unit_std). Money in rupees -> Rs mn."""
    u = norm_unit(unit)
    x = to_float(value)
    if x is None:
        return None, u
    if u == "Rs cr":
        return x * 10.0, "Rs mn"
    if u == "Rs lakh":
        return x * 0.1, "Rs mn"
    if u == "Rs bn":
        return x * 1000.0, "Rs mn"
    if u == "cr units":
        return x * 10.0, "mn units"
    if u == "lakh units":
        return x * 0.1, "mn units"
    return x, u


def display_money_rs_mn(x, approx=False):
    t = "~" if approx else ""
    sign = "-" if x < 0 else ""
    a = abs(x)
    if a >= 1000:
        return f"{t}{sign}Rs. {a / 1000:,.1f}bn"
    if a >= 10:
        return f"{t}{sign}Rs. {a:,.0f}mn"
    return f"{t}{sign}Rs. {a:,.1f}mn"


CCY_SYM = {"EUR": "€", "USD": "$", "GBP": "£", "CHF": "CHF ", "RMB": "RMB ", "CNY": "RMB ", "BRL": "BRL ", "JPY": "JPY "}
CCY_MULT = {"": 1.0, "k": 1e3, "thousand": 1e3, "'000": 1e3, "000": 1e3, "mn": 1e6, "m": 1e6, "million": 1e6,
            "100 mn": 1e8, "100m": 1e8, "bn": 1e9, "billion": 1e9, "tn": 1e12, "trillion": 1e12}


def parse_ccy_unit(u):
    """'EUR mn' -> ('EUR', 1e6, ''); 'USD/ton' -> ('USD', 1, '/ton'); '100M JPY' -> ('JPY', 1e8, '')."""
    u0 = (u or "").strip()
    m = re.fullmatch(r"100M\s+([A-Z]{3})", u0)
    if m:
        return m.group(1), 1e8, ""
    m = re.fullmatch(r"(EUR|USD|GBP|CHF|RMB|CNY|BRL|JPY)\s*(k|thousand|'000|000|mn|m|million|100 mn|bn|billion|tn|trillion)?\s*(/.*|per .*)?", u0, re.I)
    if not m:
        return None
    ccy = m.group(1).upper()
    mult = CCY_MULT.get((m.group(2) or "").lower(), 1.0)
    per = (m.group(3) or "").strip()
    if per.startswith("per "):
        per = " " + per
    return ccy, mult, per


def display_ccy(x, ccy, mult, per="", printed=None):
    sym = CCY_SYM.get(ccy, ccy + " ")
    amt = x * mult
    sign = "-" if amt < 0 else ""
    a = abs(amt)
    if per:  # a price per unit: keep the printed precision
        return f"{sign}{sym}{fmt_num(a)}{per}"
    printed_ok = printed is not None and re.fullmatch(r"-?[\d,]+(\.\d{1,2})?", str(printed).strip())
    if a >= 1e12:
        body = f"{a / 1e12:,.1f}tn"
    elif a >= 1e9:
        if mult == 1e9 and printed_ok:
            dp = len(str(printed).strip().split(".")[1]) if "." in str(printed) else 0
            body = f"{a / 1e9:,.{dp}f}bn"
        else:
            body = f"{a / 1e9:,.1f}bn"
    elif a >= 1e6:
        if mult == 1e6 and printed is not None and re.fullmatch(r"-?[\d,]+(\.\d{1,2})?", str(printed).strip()):
            # a figure already printed in mn keeps its printed precision (EUR 11mn, EUR 3.2mn, EUR 14.58mn)
            dp = len(str(printed).strip().split(".")[1]) if "." in str(printed) else 0
            body = f"{a / 1e6:,.{dp}f}mn"
        else:
            body = f"{a / 1e6:,.2f}mn" if a < 1e7 else f"{a / 1e6:,.1f}mn"
    elif a >= 1e3:
        body = f"{a / 1e3:,.0f}k" if a >= 1e5 else f"{fmt_num(round(a / 1e3, 1))}k"
    else:
        body = fmt_num(a)
    return f"{sign}{sym}{body}"


def display_ccy_text(v, ccy, mult, per=""):
    """Printed text values in a currency unit: '<100', 'approximately 180', '81-85'."""
    sym = CCY_SYM.get(ccy, ccy + " ")
    suffix = {1.0: "", 1e3: "k", 1e6: "mn", 1e8: "00mn", 1e9: "bn", 1e12: "tn"}.get(mult, "")
    s = str(v).strip()
    m = re.fullmatch(r"(?i)(approximately|approx\.?|around|about|nearly|close to|~)?\s*(<|>|less than|more than|over|above|under)?\s*([\d.,]+)\s*(?:-|to)?\s*([\d.,]+)?\s*(\+)?", s)
    if not m:
        return f"{s} ({ccy}{(' ' + suffix) if suffix else ''}{per})"
    approx = "~" if m.group(1) else ""
    rel = {"less than": "<", "under": "<", "more than": ">", "over": ">", "above": ">"}.get((m.group(2) or "").lower(), m.group(2) or "")
    lo, hi, plus = m.group(3), m.group(4), m.group(5) or ""
    rng = f"{lo}-{hi}" if hi else lo
    return f"{approx}{rel}{sym}{rng}{suffix}{plus}{per}"


def display(row):
    """House-style display string for a fact."""
    v, u = row["value"], norm_unit(row["unit"])
    x = to_float(v)
    approx = str(v).strip().startswith("~") or "[vendor estimate]" in (row.get("note") or "") and False
    if re.fullmatch(r"Rs per (EUR|USD)", u) and x is not None:
        return f"Rs. {fmt_num(x)}/{CCY_SYM[u[-3:]].strip()}"
    pc = parse_ccy_unit(row["unit"]) if u not in ("Rs cr", "Rs lakh", "Rs mn", "Rs bn", "Rs") else None
    if pc and u != "text" and x is None:
        return display_ccy_text(v, *pc)
    if u == "text" or x is None:
        # text or a printed range such as "25-27" -> keep as printed with unit
        s = str(v).strip()
        if u in ("%",) and not s.endswith("%"):
            s += "%"
        elif u in ("Rs cr", "Rs mn", "Rs bn", "Rs lakh") and u != "text":
            s = f"{s} ({u})"  # ranges in money are rendered explicitly by the writer
        return s
    plus = "+" if str(v).strip().endswith("+") else ""
    if u in ("Rs cr", "Rs lakh", "Rs mn", "Rs bn"):
        vs, _ = standardize(v, u)
        return display_money_rs_mn(vs, approx) + plus
    if u == "Rs":
        if abs(x) >= 1e6:  # rupee amounts printed in full (e.g. Rs 2,50,25,820) -> Rs. mn / bn
            return display_money_rs_mn(x / 1e6, approx) + plus
        return ("~" if approx else "") + f"Rs. {fmt_num(x)}" + plus
    if u == "%":
        if row.get("dec") is not None:
            return f"{x:,.{row['dec']}f}%"
        return f"{str(v).strip().rstrip('%')}%" if not isinstance(v, (int, float)) else f"{fmt_num(x, None if abs(x) < 100 else 0)}%"
    if pc:
        return display_ccy(x, pc[0], pc[1], pc[2], printed=v) + plus
    if u == "EUR mn":
        return f"€{fmt_num(x)}mn{plus}"
    if u == "EUR bn":
        return f"€{fmt_num(x)}bn{plus}"
    if u == "EUR k":
        return f"€{fmt_num(x)}k{plus}"
    if u == "EUR":
        return f"€{fmt_num(x)}{plus}"
    if u == "USD mn":
        return f"${fmt_num(x)}mn{plus}"
    if u == "USD bn":
        return f"${fmt_num(x)}bn{plus}"
    if u == "USD k":
        return f"${fmt_num(x)}k{plus}"
    if u == "USD":
        return f"${fmt_num(x)}{plus}"
    if u in ("cr units", "lakh units"):
        vs, _ = standardize(v, u)
        return (f"{fmt_num(vs / 1000)}bn units{plus}" if vs >= 1000 else f"{fmt_num(vs)}mn units{plus}")
    if u == "mn units":
        return f"{fmt_num(x)}mn units{plus}"
    if u == "bn units":
        return f"{fmt_num(x)}bn units{plus}"
    if u == "units":
        return f"{fmt_num(x)} units{plus}"
    if u == "count":
        return f"{fmt_num(x)}{plus}"
    if u == "days":
        return f"{fmt_num(x)} days"
    if u == "x":
        return f"{fmt_num(x)}x"
    if u == "bps":
        return f"{fmt_num(x)}bps"
    if u == "pp":
        return f"{fmt_num(x)}pp"
    return f"{fmt_num(x)}{plus} {u}".strip()


# ---------------------------------------------------------------- main
def main():
    docs = load_registry()
    rows, problems = [], []
    seen = set()
    for f in sorted(glob.glob("ledger/shards/*.jsonl")):
        shard = os.path.basename(f)[:-6]
        with open(f) as fh:
            for ln, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError as e:
                    problems.append(f"{shard}:{ln} bad JSON: {e}")
                    continue
                miss = [k for k in REQUIRED if k not in r]
                if miss:
                    problems.append(f"{shard}:{ln} {r.get('fact_id')} missing {miss}")
                    continue
                fid = r["fact_id"]
                if fid in seen:
                    problems.append(f"{shard}:{ln} duplicate fact_id {fid}")
                    continue
                seen.add(fid)
                r["shard"] = shard
                if r["doc_id"] not in docs:
                    problems.append(f"{fid} unknown doc_id {r['doc_id']}")
                rows.append(r)

    # derived facts
    derived_defs = []
    for dp in sorted(glob.glob("ledger/derived*.py")):
        ns = {"DERIVED": []}
        try:
            exec(open(dp).read(), ns)
        except Exception as e:  # one broken file must not stop the others
            problems.append(f"{dp} failed to load: {e}")
            continue
        derived_defs += ns.get("DERIVED", [])
    byid = {r["fact_id"]: r for r in rows}
    for d in derived_defs:
        if d.get("id") in seen:
            problems.append(f"duplicate derived id {d.get('id')}")
            continue
        seen.add(d.get("id"))
        refs = re.findall(r"\b[A-Z]{1,3}-\d{4}\b", d["formula"])
        env, ok = {}, True
        for ref in refs:
            if ref not in byid:
                problems.append(f"derived {d['id']} references missing {ref}")
                ok = False
                break
            vs, us = standardize(byid[ref]["value"], byid[ref]["unit"])
            if vs is None:
                problems.append(f"derived {d['id']} ref {ref} not numeric")
                ok = False
                break
            env[ref.replace("-", "_")] = vs
        if not ok:
            continue
        expr = re.sub(r"([A-Z]{1,3})-(\d{4})", r"\1_\2", d["formula"])
        try:
            val = eval(expr, {"__builtins__": {}}, env)
        except Exception as e:
            problems.append(f"derived {d['id']} eval error {e}")
            continue
        dec = d.get("dec", 1)
        unit = d.get("unit", "%")
        rows.append({
            "fact_id": d["id"], "metric": d.get("metric", "derived"), "entity": d.get("entity", ""),
            "segment": d.get("segment", ""), "geography": d.get("geography", ""), "period": d.get("period", ""),
            "value": round(val, dec), "unit": unit, "basis": "derived_ours", "doc_id": "DERIVED", "page": 0,
            "snippet": d["formula"], "speaker": "", "section": d.get("section", ""),
            "note": d.get("note", ""), "inputs": refs, "shard": "DERIVED", "dec": dec,
        })

    # standardize + display
    for r in rows:
        vs, us = standardize(r["value"], r["unit"])
        r["value_std"] = vs
        r["unit_std"] = us
        r["display"] = display(r)
        meta = docs.get(r["doc_id"], {})
        r["doc_title"] = meta.get("title", "")
        r["doc_date"] = meta.get("date", "")
        r["tier"] = meta.get("tier", "")
        r["doc_url"] = meta.get("url", "")

    # conflicts: same metric/entity/segment/geography/period/unit_std, numeric values differ >1.5%
    groups = defaultdict(list)
    for r in rows:
        if r["value_std"] is None or r["basis"] in ("guidance",):
            continue
        key = (r["metric"].lower(), r["entity"].lower(), str(r["segment"]).lower(), str(r["geography"]).lower(),
               str(r["period"]).lower(), r["unit_std"])
        groups[key].append(r)
    conflicts = []
    for key, g in groups.items():
        vals = [x["value_std"] for x in g]
        lo, hi = min(vals), max(vals)
        if len(g) > 1 and hi != 0 and (hi - lo) / max(abs(hi), 1e-9) > 0.015:
            for x in g:
                conflicts.append([*key, x["fact_id"], x["value"], x["unit"], x["doc_id"], x["page"], x["basis"], x.get("note", "")])

    with open("ledger/facts.jsonl.tmp", "w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    cols = ["fact_id", "metric", "entity", "segment", "geography", "period", "value", "unit", "value_std", "unit_std",
            "display", "basis", "doc_id", "page", "tier", "section", "speaker", "snippet", "note", "shard"]
    with open("ledger/facts.csv.tmp", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in cols])
    with open("ledger/conflicts.csv.tmp", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["metric", "entity", "segment", "geography", "period", "unit_std", "fact_id", "value", "unit",
                    "doc_id", "page", "basis", "note"])
        w.writerows(conflicts)
    # atomic swap so concurrent readers (the build, other agents) never see a half-written file
    for f in ("ledger/facts.jsonl", "ledger/facts.csv", "ledger/conflicts.csv"):
        os.replace(f + ".tmp", f)
    by_shard = defaultdict(int)
    for r in rows:
        by_shard[r["shard"]] += 1
    rep = [f"facts: {len(rows)}", "by shard: " + ", ".join(f"{k}={v}" for k, v in sorted(by_shard.items())),
           f"conflict rows: {len(conflicts)}", f"problems: {len(problems)}"] + problems[:200]
    open("ledger/reconcile_report.txt", "w").write("\n".join(rep) + "\n")
    print("\n".join(rep[:12]))


if __name__ == "__main__":
    import fcntl
    with open("ledger/.reconcile.lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        main()
