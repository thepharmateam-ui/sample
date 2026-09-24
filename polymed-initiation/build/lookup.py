"""Print ledger facts: python3 build/lookup.py CA-0107 CA-0512 ...  or  --grep <regex> [--shard CA]"""
import json, re, sys
rows = [json.loads(l) for l in open("ledger/facts.jsonl")]
by = {r["fact_id"]: r for r in rows}
args = sys.argv[1:]
if args and args[0] == "--grep":
    pat = re.compile(args[1], re.I)
    shard = args[args.index("--shard") + 1] if "--shard" in args else None
    for r in rows:
        if shard and r["shard"] != shard:
            continue
        blob = " ".join(str(r.get(k, "")) for k in ("metric", "entity", "segment", "geography", "period", "snippet", "note"))
        if pat.search(blob):
            print(f"{r['fact_id']:9s} {r['period'][:12]:12s} {str(r['value'])[:14]:14s} {r['unit'][:7]:7s} -> {r['display'][:22]:22s} | {r['metric'][:26]:26s} | {r['entity'][:22]:22s} | {str(r['segment'])[:10]:10s} | {str(r['geography'])[:9]:9s} | {r['doc_id']} p.{r['page']} | {r['snippet'][:90]}")
else:
    for a in args:
        r = by.get(a)
        if not r:
            print(a, "MISSING"); continue
        print(f"{a:9s} {r['period'][:12]:12s} {str(r['value'])[:14]:14s} {r['unit'][:7]:7s} -> {r['display'][:22]:22s} | {r['metric'][:26]:26s} | {r['entity'][:22]:22s} | {str(r['segment'])[:10]:10s} | {str(r['geography'])[:9]:9s} | {r['basis'][:10]} | {r['doc_id']} p.{r['page']} | {r['snippet'][:100]}")
