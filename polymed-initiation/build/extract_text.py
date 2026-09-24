"""Extract per-page text from sources/pdf/*.pdf into sources/text/<doc_id>.txt with page markers.
Writes registry/text_stats.csv (doc_id, pages, chars, low_text_pages)."""
import pymupdf, glob, os, csv, sys
os.makedirs("sources/text", exist_ok=True)
stats = []
files = sorted(glob.glob("sources/pdf/*.pdf"))
only = set(sys.argv[1:])
for f in files:
    doc_id = os.path.basename(f)[:-4]
    if only and doc_id not in only:
        continue
    out = f"sources/text/{doc_id}.txt"
    try:
        d = pymupdf.open(f)
    except Exception as e:
        print("FAIL", doc_id, e); continue
    low = []; total = 0
    with open(out, "w") as fh:
        for i, page in enumerate(d, start=1):
            t = page.get_text("text")
            total += len(t)
            if len(t.strip()) < 200:
                low.append(i)
            fh.write(f"\n=== [{doc_id} p.{i}] ===\n")
            fh.write(t)
    stats.append((doc_id, d.page_count, total, len(low), " ".join(map(str, low[:40]))))
    print(f"{doc_id:10s} pages={d.page_count:4d} chars={total:8d} low_text_pages={len(low)}")
mode = "a" if only else "w"
with open("registry/text_stats.csv", mode, newline="") as fh:
    w = csv.writer(fh)
    if mode == "w": w.writerow(["doc_id", "pages", "chars", "n_low_text", "low_text_pages"])
    w.writerows(stats)
