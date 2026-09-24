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


def display(row):
    """House-style display string for a fact."""
    v, u = row["value"], norm_unit(row["unit"])
    x = to_float(v)
    approx = str(v).strip().startswith("~") or "[vendor estimate]" in (row.get("note") or "") and False
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
        return ("~" if approx else "") + f"Rs. {fmt_num(x)}" + plus
    if u == "%":
        return f"{str(v).strip().rstrip('%')}%" if not isinstance(v, (int, float)) else f"{fmt_num(x, None if abs(x) < 100 else 0)}%"
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
        exec(open(dp).read(), ns)
        derived_defs += ns.get("DERIVED", [])
    byid = {r["fact_id"]: r for r in rows}
    for d in derived_defs:
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
            "note": d.get("note", ""), "inputs": refs, "shard": "DERIVED",
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

    with open("ledger/facts.jsonl", "w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    cols = ["fact_id", "metric", "entity", "segment", "geography", "period", "value", "unit", "value_std", "unit_std",
            "display", "basis", "doc_id", "page", "tier", "section", "speaker", "snippet", "note", "shard"]
    with open("ledger/facts.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in cols])
    with open("ledger/conflicts.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["metric", "entity", "segment", "geography", "period", "unit_std", "fact_id", "value", "unit",
                    "doc_id", "page", "basis", "note"])
        w.writerows(conflicts)
    by_shard = defaultdict(int)
    for r in rows:
        by_shard[r["shard"]] += 1
    rep = [f"facts: {len(rows)}", "by shard: " + ", ".join(f"{k}={v}" for k, v in sorted(by_shard.items())),
           f"conflict rows: {len(conflicts)}", f"problems: {len(problems)}"] + problems[:200]
    open("ledger/reconcile_report.txt", "w").write("\n".join(rep) + "\n")
    print("\n".join(rep[:12]))


if __name__ == "__main__":
    main()
