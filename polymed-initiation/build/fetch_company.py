"""Download company PDFs listed in registry/company_docs.csv into sources/pdf/<doc_id>.pdf."""
import csv, subprocess, os, hashlib
from concurrent.futures import ThreadPoolExecutor
BASE = "https://www.polymedicure.com/wp-content/uploads/"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
rows = list(csv.DictReader(open("registry/company_docs.csv")))
os.makedirs("sources/pdf", exist_ok=True)

def get(r):
    out = f"sources/pdf/{r['doc_id']}.pdf"
    if os.path.exists(out) and os.path.getsize(out) > 5000:
        return r['doc_id'], 'cached', os.path.getsize(out)
    url = BASE + r['path']
    p = subprocess.run(["curl", "-sS", "-L", "-m", "300", "-A", UA, "-o", out, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    code = p.stdout.strip()
    size = os.path.getsize(out) if os.path.exists(out) else 0
    return r['doc_id'], code, size

with ThreadPoolExecutor(6) as ex:
    for doc, code, size in ex.map(get, rows):
        flag = "" if size > 5000 else "  <-- CHECK"
        print(f"{doc:10s} {code:6s} {size/1e6:7.2f}MB{flag}")
