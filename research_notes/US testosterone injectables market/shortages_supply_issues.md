# US Testosterone Injection (Cypionate / Enanthate Vials): Shortages, Supply Disruptions and Low-Share Player Supply Issues, 2019–Oct 2026

Research date: 2026-10-21. Scope: US market only. Brand = Pfizer (Pharmacia & Upjohn) Depo-Testosterone. "Pfizer generic" = Hospira-labeled (NDC 0409-xxxx) testosterone cypionate sold under the same ANDA 085635.

Method note: ASHP pages block direct fetches (HTTP 403), so the live ASHP bulletins were read through a reader proxy (r.jina.ai). The Wayback Machine was blocked, so **no historical ASHP snapshots could be retrieved**. The history below is rebuilt from FDA openFDA datasets (enforcement/recalls, NDC directory, Drugs@FDA, drug shortages), the current ASHP bulletins, and secondary sources. Secondary consumer and telehealth blogs (medfinder, trtcatalog, healthrx) are flagged as weak where they are cited.

---

## Q1. FDA Drug Shortages Database: has testosterone cypionate or enanthate injection been listed?

### Takeaway
No. Neither testosterone cypionate nor testosterone enanthate injection appears in the FDA Drug Shortages Database: not on the current/resolved list, not on the discontinuations list, and not in the openFDA drug-shortages dataset, as of October 2026. The "shortage" exists only in ASHP/University of Utah tracking. This matters for regulation: 503B outsourcing facilities cannot use the FDA-shortage-list route to compound copies (see Q6).

### Cited Findings
- The FDA Drug Shortages Database index (current/resolved list and discontinuations list, both alphabetical) has no testosterone entry between "Technetium" and "Triamcinolone" (current/resolved) or between "Tazemetostat" and "Tiagabine" (discontinuations). The Reproductive/Urology category lists only cetrorelix, medroxyprogesterone tablets and progesterone vaginal gel. Read 2026-10-21. — [FDA Drug Shortages Database](https://www.accessdata.fda.gov/scripts/drugshortages/default.cfm)
- An openFDA drug-shortages API query for generic_name "testosterone" (and a free-text "testosterone" query) returns "No matches found". The same API works for other drugs: medroxyprogesterone acetate tablets show "To Be Discontinued 08/31/2026". — [openFDA drug shortages API, testosterone query](https://api.fda.gov/drug/shortages.json?search=generic_name:testosterone&limit=100)
- Conflicting/weak claim: a consumer pharmacy-information site says "FDA shortage database entries listed testosterone cypionate injection as in shortage at multiple points" in 2023 and that it first appeared on the FDA list "around 2010". The page cites no specific entries and contains several factual errors (see Q5), so this is likely unreliable. — [HealthRx (low reliability)](https://healthrx.com/testosterone-cypionate/manufacturing-supply)
- A consumer blog (Feb 2026) cites the "FDA Drug Shortage Database" in general terms but gives no FDA entry. — [Medfinder (weak)](https://www.medfinder.com/blog/testosterone-shortage-what-providers-prescribers-need-to-know-2026)

### Inferences
- FDA lists a shortage only when total market supply cannot meet national demand, while ASHP lists any presentation-level backorder. Testosterone injection being absent from FDA's list but present on ASHP's since 2019 points to presentation- and manufacturer-specific gaps (mainly Pfizer brand, plus intermittent generic backorders), not a market-wide failure that FDA judged a national shortage.
- Because FDA never declared a shortage, FDA tools such as expedited ANDA review via shortage prioritization, temporary importation and 503B "shortage list" compounding were presumably not triggered. Generic entrants since 2022 (Alvogen/American Regent, Xiromed, Eugia, BPI Labs/Ajenat) came in through normal ANDA timelines.

### Gaps
- Could not retrieve FDA's historical shortage entries before the openFDA dataset began. It is possible, though unverified, that testosterone cypionate was listed around 2010–2013, as HealthRx claims; no primary evidence was found.

---

## Q2. ASHP Drug Shortages: per-manufacturer products, backorders, reasons, recovery dates and history

### Takeaway
ASHP has carried a testosterone cypionate injection shortage bulletin continuously since **11 Sep 2019** (latest update **3 Sep 2026**, still current). As of Sept 2026 the only presentations "affected" are **Pfizer's brand Depo-Testosterone** (100 mg/mL 10 mL; 200 mg/mL 1 mL and 10 mL), on backorder for "manufacturing delays" with no release date. All listed generics (Cipla, Eugia, Hikma, Padagis, Pfizer/Hospira generic) are "available". The enanthate bulletin (created Dec 2018, last updated Jun 2021) covers only Teva's long-unavailable 5 mL vial; Hikma's is available. No ASHP evidence was found for a distinct "2022–2023 enanthate shortage".

### Cited Findings
**ASHP testosterone cypionate injection bulletin (id=592), updated 3 Sep 2026, created 11 Sep 2019**
- Products affected: Depo-Testosterone, Pfizer, 100 mg/mL 10 mL vial (NDC 00009-0347-02); 200 mg/mL 1 mL vial (00009-0417-01); 200 mg/mL 10 mL vial (00009-0417-02). — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- Reasons, verbatim in substance:
  - Cipla: "did not provide a reason for the shortage. The 200 mg/mL 10 mL vials were discontinued in 2022."
  - Eugia, Hikma, Padagis: "has testosterone cypionate injection available."
  - Pfizer: "has Depo-Testosterone on shortage due to manufacturing delays."
  - Sun Pharma: "discontinued testosterone cypionate in late-2023."
  - — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- Available products, Sept 2026:
  - Cipla USA: 200 mg/mL 1 mL (69097-0802-32)
  - Eugia US: 100 mg/mL 10 mL (55150-0276-01); 200 mg/mL 1 mL (55150-0277-01); 200 mg/mL 10 mL (55150-0278-01)
  - Hikma: 200 mg/mL 1 mL (00143-9659-01); 200 mg/mL 10 mL (00143-9726-01)
  - Padagis: 200 mg/mL 1 mL (00574-0820-01); 200 mg/mL 10 mL (00574-0820-10)
  - Pfizer generic (Hospira labeler): 100 mg/mL 10 mL (00409-6557-01); 200 mg/mL 1 mL (00409-6562-01); 200 mg/mL 10 mL (00409-6562-20)
  - — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- Estimated resupply: "Pfizer has Depo-Testosterone 100 mg/mL 10 mL vials and 200 mg/mL 1 mL and 10 mL vials on back order and the company cannot estimate a release date." — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- The bulletin cites a Lexicomp reference "Accessed September 1, 2025", which suggests a substantive revision around Sept 2025. It suggests transdermal patch or gel as alternatives. — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- Earlier (undated) version of the same ASHP page, seen only in a search-engine snippet: Eugia's 100 mg/mL and 200 mg/mL 10 mL vials were then listed as affected, and "Cipla and Eugia did not give a reason." This indicates Eugia was on backorder at some point between its Oct 2023 launch and 2026. Unverified, because the snapshot date is unknown. — [Search snippet of ASHP id=592](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)

**ASHP testosterone enanthate IM injection bulletin (id=498), updated 4 Jun 2021, created 7 Dec 2018**
- Affected: Teva 200 mg/mL 5 mL vial (NDC 00591-3221-21). "Teva did not provide a reason for the shortage. They have had their presentation temporarily unavailable for several years." Available: Hikma 200 mg/mL 5 mL vial (00143-9750-01). — [ASHP enanthate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=498)

**2019 shortage, the origin of the current ASHP cypionate bulletin**
- Vice (25 Sep 2019) reported that ASHP declared a shortage of some forms of testosterone cypionate on Sept 11 [2019] and of some forms of testosterone enanthate on Sept 23 [2019]. Hikma spokesperson Steven Weiss said a key API was unavailable due to "production issues" and that "Most manufacturers were impacted, not just us." Hikma expected to supply the market from Oct 2019, with full supply schedules by early 2020. — [Vice, 25 Sep 2019](https://www.vice.com/en/article/8xwm84/testosterone-shortage-trans-impact)

**Secondary sources on 2023–2026 history (weak; telehealth/consumer blogs)**
- Trtcatalog (16 Apr 2026), citing ASHP accessed April 2026:
  - Hikma 200 mg/mL 10 mL vials were on backorder and had missed a late-January 2026 release estimate.
  - Pfizer Depo-Testosterone 100 mg/mL 10 mL and 200 mg/mL 10 mL were on backorder with no date; the 200 mg/mL 1 mL had "limited weekly allocations".
  - Pfizer's generic 100 mg/mL 10 mL was in limited supply with weekly releases.
  - Outlook: "intermittent availability through at least late 2026."
  - — [Trtcatalog (weak)](https://trtcatalog.com/treatment/testosterone-cypionate-shortage-alternatives)
- Medfinder (updated 15 Feb 2026):
  - Claims ASHP "first reported" the injectable shortage in early 2023 and that in mid-2023 Pfizer cited "increased demand and manufacturing delays".
  - Says Cipla, Hikma and Sun "reported supply constraints in early 2023".
  - Describes 2025 as Pfizer 1 mL vials in limited weekly batches and 10 mL on backorder, and early 2026 as "improving but not normalized".
  - — [Medfinder (weak)](https://www.medfinder.com/blog/testosterone-shortage-what-providers-prescribers-need-to-know-2026)
  - The "began in early 2023" claim is contradicted by ASHP's own bulletin creation date of 11 Sep 2019. [ASHP](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- Trtcatalog says enanthate "has had intermittent shortages during 2023–2025" but that its supply was more reliable than cypionate's as of Q2 2026. No ASHP enanthate update after June 2021 was found to corroborate this. — [Trtcatalog (weak)](https://trtcatalog.com/treatment/testosterone-cypionate-shortage-alternatives)

**Non-US context (Pfizer brand constraints appear global)**
- Canada: Pfizer attributed a Depo-Testosterone shortage starting March 2021 to its focus on COVID-19 vaccine manufacturing and expected it to last into early 2022. — [Xtra Magazine](https://xtramagazine.com/health/testosterone-shortage-2-212490)
- New Zealand: Pharmac said Pfizer informed it that Depo-Testosterone would be in short supply from late October to mid-December 2025. — [NZNO](https://www.nurse.org.nz/posts/supply-issue-testosterone-cipionate-inj-100-mg-per-ml-10-ml-vial-depo-testosterone)
- Canada: Health Canada reports show a Hikma testosterone enanthate 200 mg/mL shortage with reason "demand increase", resolved (updated 25 Mar 2025), and a new "actual shortage" updated 21 Apr 2026. This is Canadian data and only a weak signal for Hikma's global enanthate capacity. — [Health Product Shortages Canada](https://healthproductshortages.ca/ingredient/310)

### Inferences
- The dated pattern is:
  - 2019: an API-driven, multi-manufacturer shortage (Hikma API "production issues").
  - 2020–2022: generic quality and recall events (Cipla 2019; Sun 2020–2022; Wilshire 2019/2023).
  - Late 2023: Sun exited.
  - 2023–2026: persistent backorder of Pfizer's brand Depo-Testosterone ("manufacturing delays"), with intermittent backorders at Eugia (undated) and Hikma (early 2026).
  - By Sept 2026: all ASHP-tracked generics show as available, and only the brand remains short.
- The brand being the long-running constrained product, while Pfizer's own Hospira-labeled generic stays available, suggests Pfizer is prioritizing generic/unbranded volume or has brand-specific line or packaging constraints. This is inference only; Pfizer gives no detail beyond "manufacturing delays".
- ASHP's manufacturer list in 2026 omits several marketed labelers: Xiromed, NorthStar (Xiromed ANDA), Alvogen (American Regent ANDA), Wilshire/Azurity, Azurity Azmiro, and BPI Labs/Ajenat. ASHP's "available/affected" picture therefore does not cover all small labelers. Their supply reliability is unobserved, not shown to be reliable.

### Gaps
- No dated ASHP snapshots for 2020–2025 could be retrieved (ASHP returns 403 and archive.org is blocked). The exact dates when each manufacturer went on or off backorder in 2021–2025 (Pfizer brand onset, Eugia backorder, Cipla, Hikma 2026) could not be confirmed from primary data.
- No ASHP bulletin was found for a 2022–2023 enanthate shortage. The only enanthate bulletin is the Teva-only 2018–2021 one, so the premise in the brief is unverified.
- Pfizer's own product-availability page was not retrieved.

---

## Q3. Discontinuations and exits from US testosterone injection vials

### Takeaway
Confirmed exits:
- **Sun Pharma** exited testosterone cypionate in late 2023, after its Halol site's 2022 recalls, OAI status, import alert and warning letter. ANDA 201720 is now "Discontinued".
- **Cipla** discontinued its 200 mg/mL 10 mL presentation in 2022.
- **Teva** enanthate (5 mL) has been unavailable since around 2018 and has no current US listing.
- **Pfizer** discontinued Depo-Testosterone 50 mg/mL long ago.
- **Azurity's Azmiro** (prefilled syringe/vial, launched Dec 2024) is now shown as "Discontinued" in Drugs@FDA.

No evidence was found of Sandoz, Mylan/Viatris or Teva marketing testosterone cypionate vials in the US in 2020–2026. Perrigo's ANDA now sits with Padagis, which is still active.

### Cited Findings
- Sun Pharma "discontinued testosterone cypionate in late-2023." — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- Drugs@FDA lists Sun Pharm Inds Ltd ANDA 201720 (approved 3 Jun 2013), with both 100 mg/mL and 200 mg/mL products marked "Discontinued". — [openFDA Drugs@FDA, testosterone cypionate](https://api.fda.gov/drug/drugsfda.json?search=openfda.generic_name:%22testosterone+cypionate%22&limit=100)
  - Sun's three NDCs (62756-015/-016/-017) still carry NDC directory listings through 2026-12-31, apparently stale listings. [openFDA NDC directory](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)
- Cipla: "The 200 mg/mL 10 mL vials were discontinued in 2022." — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- Teva enanthate 5 mL (NDC 00591-3221-21) has been "temporarily unavailable for several years" (as of Jun 2021). — [ASHP enanthate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=498)
  - The current NDC directory lists only three enanthate injection products: Hikma ANDA 091120 (since 18 Sep 2012), Eugia ANDA 212659 (since 28 Feb 2024) and Antares Xyosted NDA 209863 (since 15 Nov 2018). Teva is absent. [openFDA NDC directory, enanthate](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+enanthate%22&limit=1000)
- Pfizer Depo-Testosterone (ANDA 085635, approved 25 Jul 1979): 50 mg/mL is "Discontinued"; 100 and 200 mg/mL are "Prescription" (active). — [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=openfda.generic_name:%22testosterone+cypionate%22&limit=100)
- Azurity Azmiro (NDA 216318; 200 mg/mL prefilled glass syringe and 1 mL vial):
  - Announced as available 11 Dec 2024, billed as "the first and only FDA-approved prefilled testosterone cypionate injection". — [Azurity press release, 11 Dec 2024](https://azurity.com/azurity-pharmaceuticals-inc-announces-availability-of-azmiro-testosterone-cypionate-injection-for-intramuscular-use-ciii/)
  - Drugs@FDA shows product 001 as "Discontinued". [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=openfda.generic_name:%22testosterone+cypionate%22&limit=100)
  - The NDC directory still lists Azmiro NDCs (marketing start 4 Oct 2024, listing expiry 2026-12-31). [openFDA NDC directory](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)
  - Conflicting signals; no discontinuation announcement was found.
- Padagis (formerly Perrigo's Rx business) still holds ANDA 040530 (approved 31 Jan 2005), marketed since 2007. It also markets product under Hikma's ANDA 091244 (NDC 0574-0827, since 1 May 2014). — [openFDA NDC directory](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)

### Inferences
- The exits are concentrated among **small, India-manufactured or quality-challenged labelers (Sun, partly Cipla, Azurity)** and a legacy enanthate player (Teva). None of the larger, established suppliers (Pfizer, Hikma, Padagis) exited. Pfizer's brand has been constrained but not discontinued.
- Sun's late-2023 exit was followed within weeks by Eugia's ANDA approval (20 Oct 2023). Xiromed (Apr 2023) and Alvogen/American Regent (Nov 2022) had launched shortly before. Small-player churn in this market is high, with low barriers to ANDA entry; see the Feb 2026 FDA product-specific guidance in Q7.

### Gaps
- No primary source dates the Perrigo-to-Padagis transfer or confirms any Sandoz, Mylan or Teva cypionate history in 2020–2026. Their absence from the current NDC directory is the only evidence.
- Reason for the Azmiro discontinuation and its date: not found.

---

## Q4. Quality and regulatory events affecting testosterone injection manufacturers (recalls, warning letters, OAIs, import alerts)

### Takeaway
Every manufacturer-level (non-compounder) testosterone cypionate vial recall in 2019–2026 came from a **lower-share, India-made or contract-made generic**: Cipla (Verna, Goa), Sun (Halol), Wilshire/Azurity, Eugia (Telangana) and an unapproved product (Advanced Pharmaceutical Technology). There were no recalls of Pfizer (brand or Hospira generic), Hikma or Padagis vials in openFDA for 2019–2026. Recurring failure modes:
- particulates (Cipla 2019)
- sterility/microbial excursions and API impurity (Sun 2022)
- **crystallization that does not redissolve** (Wilshire 2023, Eugia 2025)
- label mix-ups

Sun Halol's Aug 2022 OAI, Dec 2022 import alert and warning letter, and Sept 2025 OAI align with Sun's exit.

### Cited Findings
**Manufacturer recalls of testosterone cypionate vials (openFDA enforcement reports; report date / initiation date)** — all from [openFDA enforcement API](https://api.fda.gov/drug/enforcement.json?search=product_description:testosterone+AND+report_date:%5B20190101+TO+20261231%5D&limit=100) unless noted.

Cipla (recalls filed by InvaGen, Cipla's US subsidiary)
- D-1123/1124/1125-2019, Class II, report 24 Apr 2019, initiated 22 Mar 2019: "Presence of Particulate Matter".
- Product made by Cipla Ltd., Verna, Goa, India.
- Quantities: 200 mg/mL 1 mL, 692,538 vials; 200 mg/mL 10 mL, 12,234 vials; 100 mg/mL 10 mL, 75,968 vials.
- Terminated 16 Aug 2022.

Wilshire Pharmaceuticals (Arbor, later Azurity)
- D-0167-2020, Class III, report 6 Nov 2019: label mix-up. A shipper carton for 1 mL vials contained 10 mL cartons; 67,934 units. Terminated 2 Feb 2021.
- D-0489-2023, Class II, report 12 Apr 2023, initiated 15 Feb 2023 (Azurity): "complaints of crystals not redissolving into solution after warming and shaking the vials". 10 mL, 16,471 vials; 1 mL, 43,096 vials. Terminated 4 Dec 2023.

Sun Pharma (made at Halol, Gujarat)
- D-0787/0788-2020, Class II, report 22 Jan 2020, initiated 14 Jan 2020: released lots "manufactured under similar manufacturing conditions to a previously rejected OOS lot". Covers 100 mg/mL 10 mL and 200 mg/mL 1 mL/10 mL.
- D-0242-2021, Class III, report 3 Feb 2021: incorrect lot number on secondary packaging; 36,275 cartons.
- D-1153-2022, Class II, initiated 3 Jun 2022: lots made with API from lots rejected for impurity-related manufacturing issues; 97,450 vials (200 mg/mL 1 mL).
- D-1154-2022, initiated 10 Jun 2022: "Lack of Assurance of Sterility: … microbial excursion"; 47,500 vials.
- D-1176-2022, initiated 3 Jun 2022: abnormal appearance on parts of machinery; 27 vials.
- D-1190-2022, initiated 21 Jun 2022: "cGMP – Water leakage"; 50,860 vials.
- Total for the four 2022 recalls: about 195,800 vials of the 200 mg/mL 1 mL presentation, all made at Halol. Terminated May 2023.

Eugia (made by Eugia Specialties Ltd., Telangana)
- D-0363-2025, Class II, report 23 Apr 2025, initiated 10 Apr 2025: "complaints of crystals not redissolving into solution after warming and shaking"; 36,816 vials of 200 mg/mL 1 mL (NDC 55150-277-01). Ongoing.

Advanced Pharmaceutical Technology (Elmsford, NY)
- D-0531-2025, Class II, report 2 Jul 2025: "TESTO-200" testosterone cypionate 200 mg/mL 10 mL, "Marketed Without an Approved NDA/ANDA"; 26 vials, distributed in NY and NJ.
- See also [HMP Global](https://www.hmpgloballearningnetwork.com/site/pln/news/recall-issued-testo-200-testosterone-injection-due-cgmp-violations).

Pfizer, Hikma, Padagis, Xiromed, Alvogen
- No testosterone injection recalls in the openFDA enforcement dataset for 2019–2026. Searches were by product description and by recalling firm. — [openFDA enforcement API](https://api.fda.gov/drug/enforcement.json?search=product_description:testosterone+AND+report_date:%5B20190101+TO+20261231%5D&limit=100)

**Site-level FDA actions**

Sun Pharma, Halol
- OAI in Aug 2022, after an Apr–May 2022 inspection.
- Import alert listed 8 Dec 2022. FDA letter dated 7 Dec 2022 said all drugs from the facility "are subject to refusal of admission".
- Warning letter disclosed Dec 2022.
- — [Business Today, 19 Dec 2022](https://www.businesstoday.in/amp/markets/stocks/story/sun-pharma-shares-slip-2-after-usfda-issues-warning-letter-for-halol-facility-356855-2022-12-19); [Medical Dialogues](https://medicaldialogues.in/sun-pharma-gets-usfda-warning-letter-on-halol-facility)
- Re-inspected Jun 2025 and classified OAI again (disclosed Sept 2025). Repeat observations include poor aseptic practice, inadequate environmental monitoring and inadequate media fills; the site remains under import alert. — [Business Today, Sept 2025](https://www.businesstoday.in/amp/markets/stocks/story/sun-pharma-what-jm-financial-says-as-halol-plant-gets-oai-tag-check-key-stock-drivers-493339-2025-09-10); [Moneylife](https://moneylife.in/article/us-fda-flags-sun-pharmas-halol-plant-with-official-action-indicated-status-amid-repeat-safety-breaches/78234.html)

Cipla, Verna (Goa), the site that made Cipla's testosterone cypionate per the 2019 recall
- Warning letter (dated around 25 Feb 2020, published Mar 2020) after a 16–27 Sep 2019 inspection with 12 observations, including cross-contamination. Sterile production was suspended in several units.
- Jun 10–21 2024 inspection: Form 483 with six observations.
- — [Fierce Pharma](https://www.fiercepharma.com/manufacturing/cipla-knocked-fda-warning-letter-for-sterile-injectables-plant); [Business Standard, Mar 2020](https://www.business-standard.com/article/pti-stories/usfda-issues-warning-letter-to-cipla-for-goa-plant-120031801598_1.html); [The Goan](https://www.thegoan.net/goa-news/%EF%BB%BFus-fda-inspects-cipla%E2%80%99s-plant-in-goa-makes-six-%E2%80%98observations%E2%80%99/115023.html)

Eugia Pharma Specialities, Unit III (Pashamylaram, Telangana; terminally sterilized products)
- Inspected 22 Jan–2 Feb 2024, then OAI.
- Warning letter 320-24-55 dated 15 Aug 2024. Aurobindo said there was "no impact on the existing supplies to the US".
- Eugia's Jadcherla injectable unit: VAI in Jun 2024.
- — [FDA warning letter, Eugia, 15 Aug 2024](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/eugia-pharma-specialities-limited-681905-08152024); [Business Standard](https://www.business-standard.com/companies/news/aurobindo-pharma-arm-gets-warning-letter-from-usfda-for-telangana-unit-124081600751_1.html); [Fierce Pharma](https://www.fiercepharma.com/manufacturing/fda-rebukes-another-troubled-eugia-production-site-warning-letter)

**Compounded testosterone injection recalls (503A/503B), showing how widespread compounding is** — [openFDA enforcement API](https://api.fda.gov/drug/enforcement.json?search=product_description:testosterone+AND+report_date:%5B20190101+TO+20261231%5D&limit=100)
- Talon Compounding (Nov 2021)
- APS Pharmacy (Apr 2022)
- Olympia Pharmacy (May–Jun 2022; e.g., 7,161 and 3,962 vials of 200 mg/mL in grapeseed or sesame oil, for unaddressed EM/personnel-monitoring excursions)
- Tailor Made Compounding (Jul 2022)
- New Vitalis (2021, 2023)
- Empower Pharmacy (initiated 2 May 2025; 8,230 vials of 200 mg/mL 5 mL, lack of sterility assurance) — [Houston Chronicle](https://www.houstonchronicle.com/news/houston-texas/health/article/empower-pharmacy-testosterone-recall-20340925.php)
- Testosterone pellet recalls in 2025–2026 (FarmaKeio Outsourcing, Asteria Health), for metal particulates

### Inferences
- The quality-failure risk in US testosterone vials sits with Indian-made generics and small labelers, not with the leaders. For an entrant, "reliability plus quality track record" is a real differentiator. The specific technical risk to design out is **crystallization in oil-based 200 mg/mL vials**: two separate labelers (Wilshire 2023, Eugia 2025) had complaints of crystals not redissolving. That points to formulation (benzyl benzoate/cottonseed oil ratio), API particle and polymorph control, and cold-chain or storage robustness, all of which an API-integrated maker like Symbiotec could address.
- Sun's sequence shows how quickly a small player can be pushed out of this market by site-level compliance problems: recalls (2020–2022), then OAI (Aug 2022), import alert and warning letter (Dec 2022), then discontinuation (late 2023). This is a cautionary template for an Indian fill-finish entrant.

### Gaps
- Could not confirm which Eugia unit makes testosterone cypionate. The recall label says only "Eugia Specialties Limited, Telangana", so a link to the Unit III warning letter is not established.
- Pfizer's manufacturing site for Depo-Testosterone (presumably Kalamazoo) and for the Hospira-labeled generic, and any 483s or warning letters at those sites in 2020–2026: not researched or confirmed.
- Hikma's testosterone sites: Drugs@FDA lists the ANDA holder as "Hikma Farmaceutica" (Portugal). No 483s or warning letters tied to testosterone were found.
- Xiromed's manufacturing site (Chemo/Insud group) and Gland Pharma involvement: not found.
- No import alerts specific to testosterone API were found.

---

## Q5. DEA aggregate production quota (APQ): has it constrained testosterone supply?

### Takeaway
**No. DEA aggregate production quotas do not apply to testosterone.** By statute (21 USC 826(a)), APQs are set only for Schedule I and II substances (plus ephedrine, pseudoephedrine and PPA). Testosterone is Schedule III. DEA's 2026 APQ Federal Register notices cover only Schedule I/II. Blog claims that "DEA quotas haven't kept pace" with testosterone demand are legally incorrect, and no DEA quota notice for testosterone exists. DEA controls on testosterone are registration, recordkeeping/ARCOS and import/export rules, not production caps.

### Cited Findings
- 21 USC 826(a)(1): the Attorney General "shall determine the total quantity and establish production quotas for each basic class of controlled substance in schedules I and II and for ephedrine, pseudoephedrine, and phenylpropanolamine…" — [21 U.S.C. § 826, Cornell LII](https://www.law.cornell.edu/uscode/text/21/826)
- Testosterone cypionate injection "is a schedule III controlled substance." — [ASHP cypionate bulletin](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=592)
- DEA's established 2026 APQs (91 FR 287, published 5 Jan 2026, Docket DEA-1568E) and proposed 2026 APQs (28 Nov 2025, DEA-1568P) cover "Schedule I and II Controlled Substances" and List I chemicals only. — [Federal Register, 5 Jan 2026](https://www.federalregister.gov/documents/2026/01/05/2025-24277/established-aggregate-production-quotas-for-schedule-i-and-ii-controlled-substances-and-assessment); [Federal Register, 28 Nov 2025](https://www.federalregister.gov/documents/2025/11/28/2025-21509/proposed-aggregate-production-quotas-for-schedule-i-and-ii-controlled-substances-and-assessment-of)
- Contradicting (incorrect) claims:
  - Trtcatalog says "DEA production quotas for Schedule III testosterone … haven't kept pace with real demand". — [Trtcatalog](https://trtcatalog.com/treatment/testosterone-cypionate-shortage-alternatives)
  - Medfinder says "DEA production quotas may not fully account for demand increases" (unsourced). — [Medfinder](https://www.medfinder.com/blog/testosterone-shortage-what-providers-prescribers-need-to-know-2026)
  - HealthRx says DEA "sets an aggregate production quota for Schedule III anabolic steroids under 21 U.S.C. § 826". This contradicts the statute. The same page also wrongly calls Paddock "a Pfizer subsidiary" and misattributes citations, which undermines its reliability. — [HealthRx](https://healthrx.com/testosterone-cypionate/manufacturing-supply)
- A December 2025 FDA expert panel recommended that DEA remove testosterone from Schedule III. As of around Aug 2026 it remains Schedule III, with no DEA descheduling rulemaking found. — [NBC News](https://www.nbcnews.com/health/mens-health/fda-panel-testosterone-replacement-therapy-rcna248053) (search-snippet level; article not fully read)

### Inferences
- DEA quota is not a supply bottleneck for testosterone injection, and Federal Register APQ notices for 2022–2026 contain no testosterone entries because the statute does not cover Schedule III. The real DEA-related frictions for an entrant are DEA manufacturer, distributor and importer registrations for a Schedule III substance, and import paperwork for the API. These are compliance and timing costs, not volume caps.
- If testosterone is descheduled (recommended Dec 2025; not enacted), these frictions would ease further and distribution and telehealth demand could expand.

### Gaps
- The exact DEA import procedure for Schedule III non-narcotic API (import declaration rather than permit) was not verified from 21 CFR Part 1312 in this session.
- No DEA ARCOS volume data was retrieved to quantify US testosterone distribution trends.

---

## Q6. Demand drivers: telehealth / men's-health clinics, label changes, and compounding (503A/503B)

### Takeaway
Demand has clearly re-accelerated. Epic Research shows the share of US men with an active testosterone prescription rose from a 2021 trough of 0.64% to **0.93% in 2025 and 0.95% in H1 2026**, above the 2013 peak of 0.83%. This rise coincides with telehealth and direct-to-consumer men's-health growth and with FDA's 2025–2026 label liberalization. Compounders (503A/503B such as Empower and Olympia) produce large volumes of testosterone cypionate in alternative oils. Because FDA never listed testosterone on its shortage list, 503B "copies" of the approved drug lack the shortage-list pathway; the compounded market rests largely on 503A patient-specific and variant formulations.

### Cited Findings
- Epic Research (published 29 Jul 2026), covering 109 million men aged 18+ from Jan 2012 to Jun 2026:
  - Active testosterone prescription share peaked at 0.83% in 2013, fell to 0.64% in 2021, rose to 0.93% in 2025 and reached 0.95% in mid-2026.
  - In 2025, the 50–64 group was at 1.57% (prior peak 1.30% in 2013) and the 40–49 group at 1.35%.
  - Every group aged 30+ exceeded its early-2010s peak by 2025.
  - The article mentions telehealth/DTC growth but gives no telehealth-specific data and no injection-versus-gel split.
  - — [Epic Research, 29 Jul 2026](https://www.epicresearch.org/articles/after-nearly-a-decade-long-decrease-testosterone-prescribing-rates-rising-again/)
- Per Epic Research, FDA in February 2025 removed the boxed cardiovascular warning from testosterone products following the 2023 TRAVERSE trial. — [Epic Research](https://www.epicresearch.org/articles/after-nearly-a-decade-long-decrease-testosterone-prescribing-rates-rising-again/)
- Trade press reports that in June 2026 FDA asked sponsors to drop the age-related hypogonadism limitation and narrow prostate cancer warnings. Testosterone labeling was described as a priority of Commissioner Makary. — [Pink Sheet](https://insights.citeline.com/pink-sheet/drug-safety/testosterone-product-labeling-a-makary-priority-to-be-updated-ZHMMXF2NTJEFZC6SJKZM37UAG4/) (search-snippet level)
- A December 2025 FDA expert panel called for loosening TRT restrictions. — [NBC News](https://www.nbcnews.com/health/mens-health/fda-panel-testosterone-replacement-therapy-rcna248053) (search-snippet level)
- Blogs attribute the shortage to telehealth TRT growth (Hims, Ro, Hone, and others) and cite "325+ new men's health clinics" since 2024 without a source. — [Medfinder (weak)](https://www.medfinder.com/blog/testosterone-shortage-what-providers-prescribers-need-to-know-2026); [Trtcatalog (weak)](https://trtcatalog.com/treatment/testosterone-cypionate-shortage-alternatives)
- Empower Pharmacy describes itself as a 503A compounding pharmacy and 503B outsourcing facility, lists testosterone cypionate injection among its popular products, and offers both 503A patient-specific and 503B office-use supply. — [Empower Pharmacy](https://www.empowerpharmacy.com/mens-health)
- Compounded testosterone cypionate is made in grapeseed oil, sesame oil and ethyl oleate, and in combinations (with anastrozole or propionate), per FDA recall records for Olympia, Talon, APS, Tailor Made and others, 2021–2025. — [openFDA enforcement API](https://api.fda.gov/drug/enforcement.json?search=product_description:testosterone+AND+report_date:%5B20190101+TO+20261231%5D&limit=100)
- Testosterone cypionate does not appear on the FDA shortage list (Q1). — [openFDA shortages API](https://api.fda.gov/drug/shortages.json?search=generic_name:testosterone&limit=100)

### Inferences
- Under FD&C Act §503B, compounding drugs that are "essentially copies" of approved drugs is restricted unless the drug is on FDA's shortage list. Since testosterone cypionate was never FDA-listed, compounders have relied on 503A patient-specific prescriptions and differentiated formulations (alternative oils, combinations). This statutory point comes from general regulatory knowledge, not a source fetched in this session. The practical result is a large parallel "telehealth plus compounder" channel competing with FDA-approved vials on price and convenience.
- Rising prescriptions (up about 45% relative to the 2021 trough by 2025, from Epic's 0.64% to 0.93%) plus label liberalization point to sustained volume growth for FDA-approved vials. The telehealth channel is exposed to compounder quality recalls (Empower 2025, Olympia 2022), which could favor reliable, approved generic vials sold direct to telehealth pharmacies.

### Gaps
- No quantitative split of injection versus gel demand, or of telehealth share of TRT scripts, was found from a primary source.
- No source quantified compounded testosterone volume versus FDA-approved vial volume.
- The FDA February 2025 labeling change was not verified against FDA's own announcement in this session (taken from Epic Research's summary).

---

## Q7. Who is supply-constrained vs. reliable? Did leaders gain share? Implications for an entrant (Symbiotec)

### Takeaway
Supply problems in 2019–2026 fall into two groups:
1. **Persistent constraint at the brand leader's branded SKU** (Pfizer Depo-Testosterone, "manufacturing delays", no release date as of Sept 2026). Pfizer's unbranded Hospira-labeled generic and Hikma/Padagis remain broadly available, apart from Hikma's early-2026 10 mL backorder.
2. **Episodic quality-driven disruption and exits among small, India-made labelers**: Sun (exited 2023), Cipla (10 mL discontinued 2022; shortage with no reason given), Wilshire/Azurity (recalls; Azmiro now discontinued) and Eugia (2025 crystal recall; earlier intermittent backorder).

The market keeps attracting small entrants: Alvogen/American Regent in Nov 2022, Xiromed in Apr 2023, Eugia in Oct 2023 (enanthate Feb 2024), NorthStar in Nov 2024, Azurity in Oct 2024, and BPI Labs/Ajenat on **14 Sep 2026**. No primary market-share data was found to prove leaders captured share during shortages.

### Cited Findings
**Current US labeler map (FDA NDC directory, excluding repackagers)** — [openFDA NDC directory, cypionate](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000); [Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=openfda.generic_name:%22testosterone+cypionate%22&limit=100)

| Labeler | Application (holder; approval) | Presentations | US marketing start | Supply status / events |
|---|---|---|---|---|
| Pfizer: Depo-Testosterone (brand), Pharmacia & Upjohn | ANDA 085635 (Pfizer; 1979) | 100 mg/mL 10 mL; 200 mg/mL 1 mL and 10 mL | 1979 | On ASHP backorder, "manufacturing delays", no ETA (Sept 2026) |
| Pfizer generic (Hospira labeler) | ANDA 085635 | 100 mg/mL 10 mL; 200 mg/mL 1 mL and 10 mL | 1 Aug 2016 | ASHP "available" (Sept 2026); limited weekly releases of 100 mg/mL per Apr 2026 blog |
| Hikma | ANDA 091244 (Hikma Farmacêutica; 1 May 2012) | 200 mg/mL 1 mL and 10 mL | 2012 (new 10 mL NDC 0143-9005 on 22 Nov 2021) | 2019 API "production issues"; 10 mL backorder, missed Jan 2026 ETA (Apr 2026 blog); "available" Sept 2026 |
| Padagis (ex-Perrigo) | Own ANDA 040530 (2005), plus product under Hikma ANDA 091244 | 200 mg/mL 1 mL and 10 mL | 2007; Hikma-ANDA NDC since 2014 | "Available"; no recalls found |
| Cipla USA | Own ANDA 210362 (19 Jun 2018), plus product under Hikma ANDA 091244 (since 26 Mar 2019) | Own: 100 mg/mL 10 mL, 200 mg/mL 1 mL and 10 mL; Hikma-ANDA: 200 mg/mL 1 mL and 10 mL | Own-ANDA NDCs re-listed 15 Sep 2023 | 2019 particulate recall (about 780k vials, Goa); Goa warning letter 2020; 200 mg/mL 10 mL discontinued 2022; ASHP lists only the 1 mL as available |
| Sun Pharma | ANDA 201720 (2013) | 100 and 200 mg/mL | 2013 | Recalls 2020, 2021 and 2022 (Halol); discontinued late 2023 |
| Wilshire (Azurity) | ANDA 206368 (24 Apr 2019) | 200 mg/mL 1 mL and 10 mL | 31 May 2019 | Label mix-up recall 2019; crystal recall 2023; not tracked by ASHP |
| Alvogen | American Regent ANDA 207742 (16 Jun 2017) | 200 mg/mL 1 mL and 10 mL | 2 Nov 2022 | Not tracked by ASHP; no recalls found |
| Xiromed / NorthStar Rx | ANDA 215351 (Xiromed; 13 Apr 2023) | 100 mg/mL 10 mL; 200 mg/mL 1 mL and 10 mL | Xiromed 28 Apr 2023; NorthStar 1 Nov 2024 | Not tracked by ASHP; no recalls found |
| Eugia US (Aurobindo) | ANDA 211817 (20 Oct 2023) | 100 mg/mL 10 mL; 200 mg/mL 1 mL and 10 mL | 20 Oct 2023 | Earlier ASHP version showed 10 mL vials affected (undated); crystal recall Apr 2025; "available" Sept 2026 |
| Azurity: Azmiro (505(b)(2)) | NDA 216318 (2022) | 200 mg/mL prefilled syringe and 1 mL vial | 4 Oct 2024 (launch PR 11 Dec 2024) | Drugs@FDA "Discontinued" |
| BPI Labs / Ajenat | ANDA 219478 | 200 mg/mL 1 mL and 10 mL (incl. 10-vial pack) | **14 Sep 2026** | New entrant |

- Enanthate injection labelers: Hikma ANDA 091120 (5 mL, since 2012), Eugia ANDA 212659 (5 mL, since 28 Feb 2024) and Antares Xyosted SC autoinjector NDA 209863 (since Nov 2018). Teva has effectively exited (Q3). — [openFDA NDC directory, enanthate](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+enanthate%22&limit=1000)
- An Orange Book aggregator counts 16 generic testosterone cypionate ANDAs against one brand listing (third-party tool, unverified). — [Assyro Orange Book tool](https://www.assyro.com/tools/fda-orange-book/testosterone-cypionate)
- A February 2026 FDA product-specific guidance for testosterone cypionate says a generic IM solution can seek a waiver of in vivo bioequivalence if it is qualitatively and quantitatively the same as the reference product. — [FDA PSG 216318](https://www.accessdata.fda.gov/drugsatfda_docs/psg/PSG_216318.pdf) (search-snippet level)

### Inferences
- **Concentration of supply issues:**
  - Disruptions are not concentrated only among low-share players. The single most persistent constraint (2023–2026) is the leader's brand SKU, Depo-Testosterone.
  - Quality-driven disruptions and exits are, however, concentrated among small, India-made or contract-made labelers: Sun, Cipla, Wilshire/Azurity and Eugia.
  - Mid-tier, established generic suppliers (Hikma, Padagis, Pfizer/Hospira generic) have been the most consistently "available" in ASHP data, though Hikma had an early-2026 10 mL backorder.
- **Hikma appears to be a key upstream manufacturer**: both Padagis and Cipla market NDCs under Hikma's ANDA 091244. Any Hikma disruption (2019 API, early-2026 10 mL) therefore likely hits multiple labels at once, a hidden concentration risk. This is inferred from NDC-to-ANDA mapping; a labeler marketing under another firm's ANDA typically sources from that ANDA holder.
- **Leaders and share:** no IQVIA or volume data was found. Indirect evidence suggests share moved within Pfizer, from the constrained brand to its own Hospira generic, and toward Hikma, Padagis and new generic entrants (Xiromed, Alvogen, Eugia) as Sun exited. Whether "leaders captured share" cannot be confirmed.
- **Entry angle for Symbiotec (vertically integrated API to vials):**
  1. Supply reliability is the scarce attribute. The 2019 shortage was API-driven ("most manufacturers were impacted"), and recurring failures (crystallization, particulates, sterility) are formulation, API and fill-finish quality issues. An API-integrated entrant with robust 200 mg/mL oil formulation and demonstrated cGMP sterile capacity is directly positioned against them.
  2. The 10 mL multi-dose 200 mg/mL and 100 mg/mL 10 mL presentations have been the most backorder-prone: Pfizer brand 10 mL, Cipla 10 mL discontinued, Hikma 10 mL early 2026, Eugia 10 mL earlier. They are a logical first SKU set.
  3. No DEA production quota limits entry or scale-up (Schedule III). Barriers are DEA registration and import compliance.
  4. FDA's Q1/Q2 BE-waiver guidance (Feb 2026) lowers ANDA development cost. The flip side is a crowded, low-price generic field: a new entrant arrived in Sept 2026 (BPI/Ajenat), so differentiation must come from reliability, contract supply to telehealth pharmacies and wholesalers, and possibly enanthate (only Hikma and Eugia generics).
  5. The track record of Indian sites (Sun Halol import alert and exit; Cipla Goa warning letter; Eugia warning letter and recall) means FDA inspection outcome at the fill-finish site is the critical-path risk.

### Gaps
- No market-share or volume data (IQVIA, ARCOS) was found to test whether leaders gained share during shortages, or to rank the small labelers by volume.
- Supply reliability of the labelers ASHP does not track (Xiromed, Alvogen, Wilshire, NorthStar, BPI/Ajenat) is unknown. No backorder data was found for them.
- Contract manufacturers behind Xiromed, Alvogen/American Regent, Wilshire/Azurity and BPI/Ajenat were not identified.
- Pricing dynamics (WAC changes during shortages) were not researched.
