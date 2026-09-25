"""Check the multipage site: every link resolves, every exhibit and heading appears on exactly one page,
and no page carries an unresolved token."""
import glob, os, re, sys
from collections import Counter

site = sys.argv[1] if len(sys.argv) > 1 else "report/site"
full = open(os.path.join(site, "full-report.html")).read()
pages = {os.path.basename(f): open(f).read() for f in glob.glob(os.path.join(site, "*.html"))
         if os.path.basename(f) not in ("full-report.html", "Polymed_Plant_Visit_Question_Bank.html")}
ids = {f: set(re.findall(r'\bid="([^"]+)"', h)) for f, h in pages.items()}
bad, n_links = [], 0
for f, h in pages.items():
    for href in re.findall(r'href="([^"]+)"', h):
        if re.match(r"^(https?:|mailto:|tel:)", href):
            continue
        n_links += 1
        target, _, frag = href.partition("#")
        target = target or f
        if target in ("full-report.html", "Polymed_Plant_Visit_Question_Bank.html"):
            if not os.path.exists(os.path.join(site, target)):
                bad.append((f, href, "missing file"))
            continue
        if target not in pages:
            bad.append((f, href, "missing page"))
        elif frag and frag not in ids[target]:
            bad.append((f, href, "missing anchor"))
exh_site = Counter(i for f in pages for i in ids[f] if i.startswith("exh-"))
exh_full = set(re.findall(r'\bid="(exh-[^"]+)"', full))
dup = [e for e, c in exh_site.items() if c > 1]
lost = sorted(exh_full - set(exh_site))
head_full = set(re.findall(r'<h[1-3] id="([^"]+)"', full))
head_site = Counter(i for h in pages.values() for i in re.findall(r'<h[1-3] id="([^"]+)"', h))
lost_h = sorted(head_full - set(head_site))
unres = [f for f, h in pages.items() if re.search(r"\{\{[A-Z]", h)]
print(f"pages {len(pages)} | links checked {n_links} | broken {len(bad)} | exhibits {len(exh_site)} of {len(exh_full)} "
      f"| duplicated exhibits {len(dup)} | lost exhibits {len(lost)} | lost headings {len(lost_h)} | pages with tokens {len(unres)}")
for b in bad[:20]:
    print("BROKEN", b)
for e in (dup + lost)[:20]:
    print("EXHIBIT", e)
for h in lost_h[:20]:
    print("HEADING", h)
sys.exit(1 if (bad or dup or lost or lost_h or unres) else 0)
