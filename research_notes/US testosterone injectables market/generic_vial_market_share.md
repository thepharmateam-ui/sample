# US Generic Testosterone Cypionate & Enanthate Vials: Competitive Landscape and Market Share by Company

Scope: US only. Data pulled 21 Oct 2026. "Reported" = a figure published by a source. "COMPUTED" = my own aggregation of public raw data (Medicaid SDUD, Medicare Part D), with the method stated. All share figures are prescription or claim counts unless labelled otherwise. Neither dataset covers commercial or cash-pay channels, so they are **proxies** for national share, not IQVIA data.

Method notes for the computed data. These apply to every COMPUTED number below.
- **Medicaid SDUD (State Drug Utilization Data), 2022 to Q1 2026.** Source is data.medicaid.gov, datasets for [2022](https://data.medicaid.gov/dataset/200c2cba-e58d-4a95-aa60-14b99736808d), [2023](https://data.medicaid.gov/dataset/d890d3a9-6b00-43fd-8b31-fcba4c8e2909), [2024](https://data.medicaid.gov/dataset/61729e5a-7aa8-448c-8903-ba3e0cd0ea3c), [2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536) and [2026](https://data.medicaid.gov/dataset/2957a7f9-9a15-453e-9afd-3bbdcbac8fd3). I pulled the rows through the datastore API (e.g. `https://data.medicaid.gov/api/1/datastore/query/158a1baa-5506-400a-8ec3-97756f0b0536/0?conditions[0][property]=product_name&conditions[0][value]=TESTOS%&conditions[0][operator]=like`). That gave 52,831 rows for product names TESTOS%, DEPO-T%, XYOSTED% and AZMIRO%.
  - Each 11-digit NDC was classified by ingredient using the [openFDA NDC Directory](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=100). For NDCs no longer listed there, I used [NLM RxNav ndcstatus/ndcproperties](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00591412879&ndcstatus=ALL). Gels and solutions were excluded.
  - Shares are the sum of state rows (FFS + MCO). I excluded the "XX" national-total rows. Rows suppressed for counts under 11 count as zero, so the sum of states runs about 2% below the XX totals (e.g. 2025 cypionate: 583,739 vs 595,299 Rx).
  - The 2026 dataset contains **Q1 2026 only**, and Q1 2026 may still be incomplete as states report late.
- **Medicare Part D by manufacturer.** Annual figures (2020–2024) come from the CMS [Medicare Part D Spending by Drug, DY2024](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?filter[Gnrc_Name]=Testosterone%20Cypionate). 2025 full-year and Q1 2026 come from the CMS [Medicare Quarterly Part D Spending by Drug](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?filter[Gnrc_Name]=Testosterone%20Cypionate). CMS reports claims, spending and beneficiaries by manufacturer label name.
- **Units vs Rx.** SDUD "units reimbursed" contains state reporting errors, so Rx is the more robust metric. Examples: Hawaii MCO Q1 2025 reported 480,004 units on 26 Rx for Wilshire's 10 mL NDC 52536-0625-10, and Hawaii MCO Q3 2025 reported 94,219 units on 100 Rx for Padagis 0574-0820-01. These errors inflate Wilshire's and Padagis's unit shares in 2023–2025 (e.g. Wilshire is 28.5% of 2025 generic units but 11.8% of Rx).

---

## Q1. Who holds approved ANDAs/NDAs for testosterone cypionate and enanthate injection (Orange Book / Drugs@FDA)?

### Takeaway
The Orange Book lists 9 active ("RX") cypionate ANDAs and 3 active enanthate ANDAs, plus the brand and two 505(b)(2) NDAs.
- **Cypionate:** Pfizer's Depo-Testosterone (itself an ANDA), Hikma (×2), Padagis, Cipla, American Regent, Wilshire, Xiromed, Eugia (Aurobindo) and BPI Labs (approved Sept 2026). Sun Pharma's ANDA is now discontinued.
- **Enanthate:** Hikma, Eugia and Nexus.
- **No approved ANDA was found** for Sandoz, Amneal, Teva (the old Watson ANDAs are all discontinued), Slayback, Somerset, Gland, Lupin, Zydus, Dr. Reddy's, Steriscience, Endo/Par, MSN, Alembic or any Jiangsu-based company.

### Cited Findings
**Orange Book products file, Oct 2026 edition** ([FDA Orange Book data files](https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files); file downloaded from https://www.fda.gov/media/76860/download). Cross-checked against [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100), last updated 2026-10-20.

**Testosterone cypionate injection: active (RX) applications**

| Appl. | Holder (Orange Book full name) | Strengths | Approval date | TE code | Notes |
|---|---|---|---|---|---|
| ANDA 085635 | Pfizer Inc (Depo-Testosterone) | 100, 200 mg/mL (50 mg/mL discontinued) | Pre-1982 (Drugs@FDA: 1979-07-25) | AO | Brand is approved under an ANDA. RLD and Reference Standard. Hospira (Pfizer) sells the authorized generic under the same ANDA |
| ANDA 091244 | Hikma Farmacêutica (Portugal) SA | 200 mg/mL | 2012-05-01 | AO | Supplies Hikma, Padagis, Cipla and formerly Actavis (see Q2) |
| ANDA 090387 | Hikma Pharmaceuticals USA Inc | 100, 200 mg/mL | 2010-07-15 | AO | No current NDC listing found under this ANDA |
| ANDA 040530 | Padagis US LLC (ex-Perrigo) | 200 mg/mL | 2005-01-31 | AO | Made by Grand River Aseptic Manufacturing (see Q2) |
| ANDA 210362 | Cipla Ltd | 100, 200 mg/mL | 2018-06-19 | AO | NDC marketing start 2023-09-15 |
| ANDA 207742 | American Regent Inc | 200 mg/mL | 2017-06-16 | AO | Marketed by American Regent, Rising (2018–20) and Alvogen (2022–) |
| ANDA 206368 | Wilshire Pharmaceuticals Inc | 200 mg/mL | 2019-04-24 | AO | Made by Pharmaceutics International Inc (Pii) |
| ANDA 215351 | Xiromed Pharma España SL | 100, 200 mg/mL | 2023-04-13 | AO | Made by Laboratorios Farmalán, León, Spain |
| ANDA 211817 | Eugia Pharma Specialities Ltd (Aurobindo) | 100, 200 mg/mL | 2023-10-20 | AO | |
| ANDA 219478 | BPI Labs LLC | 200 mg/mL | **2026-09-03** | AO | Newest entrant |

**Testosterone cypionate: discontinued (DISCN) applications**

| Appl. | Holder | Approval date | Notes |
|---|---|---|---|
| ANDA 201720 | Sun Pharmaceutical Industries Ltd (100, 200 mg/mL) | 2013-06-03 | |
| ANDA 040615 | Caplin One Labs | 2006-08-10 | Previously distributed by Sandoz |
| ANDA 040652 | Rising | 2006-12-11 | |
| ANDA 084401, 086029, 086030 | Watson Labs / Watson Pharms | Pre-1982 | Now Teva/Actavis |
| ANDA 089326/089327 | Quad Pharms | | |
| NDA 017968 | Depo-Testadiol | | |

- **Azurity's Azmiro** (NDA 216318, testosterone cypionate 200 mg/mL, 505(b)(2), approved 2022-06-02) shows as **DISCN** in the Orange Book. However, the NDC Directory still lists Azmiro NDCs 24338-055 (syringe) and 24338-056 (vial), with marketing start 2024-10-04 and listings valid to 2026-12-31. Medicare Part D recorded 88 Azmiro claims in 2025. This conflicts with the DISCN status. — [Orange Book data files](https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files); [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=application_number:%22NDA216318%22); [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?filter[Gnrc_Name]=Testosterone%20Cypionate)

**Testosterone enanthate injection: active applications**

| Appl. | Holder | Strength | Approval date | Notes |
|---|---|---|---|---|
| ANDA 091120 | Hikma Farmacêutica (Portugal) SA | 200 mg/mL | 2012-09-18 | TE AO. Orange Book designates it the **Reference Standard** |
| ANDA 212659 | Eugia Pharma Specialities Ltd | 200 mg/mL | 2024-02-28 | |
| ANDA 040575 | Nexus Pharmaceuticals LLC | 200 mg/mL | 2006-06-14 | Status RX, but openFDA returns no current NDC listing |
| NDA 209863 | Antares Pharma (now Halozyme), Xyosted autoinjector | 50/75/100 mg per 0.5 mL, subcutaneous | 2018-09-28 | Not a vial |

**Testosterone enanthate: discontinued applications**
- NDA 009165 Delatestryl (Endo), the original RLD. The Federal Register determined it was not withdrawn for safety or efficacy reasons.
- ANDA 040647 (Rising, 2009).
- Watson ANDAs 083667, 085598 and 085599.
- Quad ANDAs 089324/089325.

**Other checks**
- An openFDA Drugs@FDA search on active ingredient found no tentative approvals and no additional ANDAs for either ester. — [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+ENANTHATE%22&limit=100)
- **Symbiotec Pharmalab** has no finished-dose ANDA. It does list bulk API NDCs for testosterone cypionate (22552-0010, listed since 2010-04-29) and testosterone enanthate (22552-0014). Other bulk API listers for cypionate:
  - Pfizer/Pharmacia (0009-0027)
  - Aspen Oss
  - Curia Spain
  - FIS
  - Farmabios
  - Steroid SpA
  - Trifarma
  - Jiangsu Jiaerke
  - Hubei Zhuxi Humanwell
  - Zhejiang Xianju
  - Shakti Lifescience
  - ASG Biochem
  - Brichem
  - SCH Global

  — [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=100)

### Inferences
- Approved-ANDA count overstates the number of real competitors. Only about 8 manufacturing sources supply the US cypionate market:
  - Hikma Portugal
  - Pfizer
  - Padagis via Grand River Aseptic Manufacturing (GRAM)
  - Pii for Wilshire
  - Farmalán for Xiromed
  - Cipla India
  - Eugia India
  - American Regent
  
  BPI Labs, approved Sept 2026, makes a ninth.
- Several companies the brief named (Sandoz, Teva/Actavis, Rising, Sun) are former participants, not current ANDA holders. Many Indian names in the brief (Lupin, Zydus, Dr. Reddy's, Gland, MSN, Alembic) have no approval. A Symbiotec-backed entrant would be roughly the 10th cypionate source.

### Gaps
- Pending ANDAs cannot be seen publicly, because no patents exist and so there are no Paragraph IV or tentative-approval signals. I could not identify who else has filed.
- I could not confirm what product, if any, ships under Hikma ANDA 090387 or Nexus ANDA 040575.

---

## Q2. Which labelers actually market product (DailyMed / NDC Directory)? Real labelers vs. repackagers

### Takeaway
Ten labeler codes carry nearly all generic cypionate volume. Hikma's Portuguese ANDA 091244 is sold under four labels: Hikma, Padagis (0574-0827), Cipla (69097-802) and, until May 2025, Actavis/Teva (0591-4128). Xiromed's product is also sold by McKesson's NorthStar Rx. Pfizer sells both the brand and a Hospira authorized generic. Repackagers (A-S Medication, Asclemed/Enovachem, Bryant Ranch, NuCare, Proficient Rx, RemedyRepack) list NDCs but show no Medicaid claims. For enanthate vials, Hikma is effectively the only marketed generic; Eugia's listing shows no claims yet.

### Cited Findings
Each row lists labeler (NDC prefix), product NDCs, ANDA, manufacturer per DailyMed, and marketing dates from the NDC Directory or RxNav. Sources: [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=100), [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00591412879&ndcstatus=ALL) and DailyMed SPLs linked per row.

**Real labelers: testosterone cypionate**

| Labeler (NDC prefix) | Product NDCs | ANDA | Manufacturer (DailyMed) | Market start | Source |
|---|---|---|---|---|---|
| Pfizer / Pharmacia & Upjohn (0009) | Depo-Testosterone 0009-0417, -0347, -0085, -0086 | 085635 | Pfizer | Brand | NDC Directory |
| Hospira, a Pfizer AG (0409) | 0409-6557, -6562 | 085635 | Pfizer | Since 2016-08-01 | NDC Directory |
| Hikma Pharmaceuticals USA (0143) | 0143-9659 (1 mL), -9726 (10 mL), -9005 (10 mL) | 091244 | "Manufactured by: Hikma Farmacêutica (Portugal)" | | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f60c5520-b336-44a2-95d5-f274939fa595) |
| Padagis (0574), own ANDA | 0574-0820 | 040530 | Grand River Aseptic Manufacturing, Grand Rapids MI, "Distributed by Padagis" | | Enovachem relabel SPL, [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=edcd5209-70db-4727-991e-3fdd185d9211) |
| Padagis (0574), Hikma-made | 0574-0827 | 091244 | "Manufactured by: Hikma Farmacêutica (Portugal)… Distributed by Padagis" | Since 2014-05-01 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e3e2da65-4b2a-4210-a6ff-cc08c8567381) |
| Cipla USA (69097), Hikma-made | 69097-802 | 091244 | "Manufactured by: Hikma Farmacêutica (Portugal)… Distributed by Cipla USA" | Since 2019-03-26 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b8ac5e07-b7e3-4a60-b0d1-8b1f3ad0c478) |
| Cipla USA (69097), own ANDA | 69097-536/-537 | 210362 | "Manufactured by: Cipla Ltd" | NDC start 2023-09-15 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=78d55bad-4a5b-4e21-aeb8-a4c6346208be) |
| Actavis Pharma / Teva (0591) | 0591-4128 | 091244 | Hikma-made | **Ended 2025-05-31** (2015-03-05 to 2025-05-31) | [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00591412879&ndcstatus=ALL) |
| Wilshire Pharmaceuticals (52536) | 52536-625 | 206368 | "Manufactured by: Pharmaceutics International, Inc… Manufactured for: Wilshire" | | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58ff6e0d-cc0a-4455-8254-d883d26a3b6d) |
| Xiromed LLC (70700) | 70700-288/-289/-290 | 215351 | "Made in Spain" | NDC start 2023-04-28 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cab949ca-fde9-c5a9-5561-21e98d86d078) |
| NorthStar Rx, McKesson (72603) | 72603-286 | 215351 | "Manufactured by: Laboratorios Farmalan SA" | NDC start 2024-11-01 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9ced69c7-cd37-efb6-1bf9-e21c01e56f5b) |
| Eugia US (55150) | 55150-276/-277/-278 | 211817 | Eugia Pharma Specialities, Hyderabad | NDC start 2023-10-20 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f901e2b2-f143-4237-8e95-0d134585490b) |
| Alvogen (47781) | 47781-910/-911 | 207742 | "Manufactured by: American Regent" | NDC start 2022-11-02 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ed65346b-31bc-f872-516d-78d5ab70229e) |
| American Regent (0517) | 0517-1830 | 207742 | | Active since 2019-07-19 | [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00517183001&ndcstatus=ALL) |
| Sun Pharmaceutical Industries Inc (62756) | 62756-015/-016/-017 | 201720 | "Manufactured by: Sun Pharmaceutical Industries Ltd" | Still listed in the NDC Directory although the Orange Book shows DISCN | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3653a602-4551-4e6c-84a7-31861f5dc482) |
| BPI Labs (54288) | 54288-150, -156 | 219478 | "Manufactured by: BPI Labs, LLC… Largo, FL" | 2026-09-14 | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=375dd035-b792-4cb7-9fe6-bb367b87bdba) |
| Ajenat Pharmaceuticals (82983) | 82983-424/-425 | 219478 | | 2026-09-14 | [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=application_number:%22ANDA219478%22) |

**Historical cypionate labelers, now exited**

| Labeler | NDC / ANDA | Marketed | Source |
|---|---|---|---|
| Sandoz (0781) | 0781-3074, ANDA 040615 | 2006-08-10 to 2013-05-30 | [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00781307470&ndcstatus=ALL) |
| Rising (64980) | 64980-467, ANDA 207742 | 2018-12 to 2020-06 | [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=64980046799&ndcstatus=ALL) |
| Actavis (0591) | 0591-3223, Watson ANDA 086030 | Ended 2017-05-31 | [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00591322379&ndcstatus=ALL) |

**Repackagers / relabelers** with current cypionate listings: A-S Medication Solutions (50090), Asclemed USA/Enovachem (76420, 87063), Bryant Ranch Prepack (72162, 71335, 63629), NuCare (68071), Proficient Rx (63187, 71205) and RemedyRepack (70518).
- Their sources are Padagis, Hikma, Wilshire, American Regent, Xiromed, Cipla and Pfizer.
- None of their 43 package NDCs shows any SDUD rows for 2023 through Q1 2026 (COMPUTED from a targeted SDUD "in" query).
- Asclemed also lists the **unapproved** "Testone CIK" kit (76420-650) containing testosterone cypionate.

— [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=100); [SDUD API](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536)

**Testosterone enanthate labelers**
- **Current:** Hikma (0143-9750, 5 mL multi-dose vial, ANDA 091120, "Manufactured by Hikma Farmacêutica (Portugal)") — [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e89d6458-428c-4256-97a3-f1fa851293c1). Eugia US (55150-336, ANDA 212659, made in Hyderabad, NDC active since 2024-02-28) — [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=82a98132-9d5f-40a5-8c4f-f52f2a5de60e).
- **Historical:** Actavis 0591-3221 (Watson ANDA 085598, marketed 2011-05-04 to 2019-12-31) — [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00591322126&ndcstatus=ALL). Padagis 0574-0821, distributing Nexus ANDA 040575, 2007-08-02 to 2011-09-30 — [RxNav](https://rxnav.nlm.nih.gov/REST/ndcproperties.json?id=00574082105&ndcstatus=ALL).

**Wilshire ownership:** a Dec 2014 press release described Wilshire Pharmaceuticals (Atlanta) as a wholly owned subsidiary of Arbor Pharmaceuticals. I did not verify current ownership. — [BioSpace 2014](https://www.biospace.com/b-wilshire-b-confirms-first-to-file-patent-challenge-relating-to-lastacaft)

### Inferences
- **Labeler share and manufacturer share differ a lot for this molecule.** Hikma Portugal is the manufacturer behind roughly 40–50% of generic Rx, because it supplies Padagis and Cipla as well as its own label.
- Padagis and Cipla are hybrid players: each sells both its own-ANDA product and Hikma-made product.
- NorthStar is a McKesson private-label channel for Xiromed product.
- A Symbiotec-linked entrant could use a similar supply or private-label model, e.g. supplying a US distributor or a wholesaler private label (NorthStar-style), rather than only building its own label.

### Gaps
- DailyMed SPLs did not state the API source (DMF holder) for any finished product, so I could not identify which API maker supplies Hikma, Xiromed, Eugia, Cipla and others.
- The Hospira AG label did not print a manufacturing site in the extract.

---

## Q3. Market share by labeler and manufacturer (Medicaid SDUD and Medicare Part D), and brand Depo-Testosterone share

### Takeaway
**Labeler level, 2025.** Hikma is the largest generic labeler: about 26% of Medicaid generic cypionate Rx and 23% of Medicare Part D generic claims. It is followed by Padagis (17–19%) and the Pfizer/Hospira authorized generic (15–16%). Next come Wilshire (10–12%), Xiromed (10–12%) and Cipla (about 10%). Eugia (3.5–5%), NorthStar (4–5%) and Alvogen (about 1%) are smaller.

**Manufacturer (ANDA) level.** Hikma Portugal supplies about 38–41% of generic volume in 2025 (COMPUTED), and its share rose back toward 47–49% in Q1 2026.

**Brand.** Depo-Testosterone fell from 6.8% of Medicaid cypionate Rx in 2022 to 2.1% in 2025 and 1.4% in Q1 2026. In Medicare it is now negligible (0.04% of 2025 claims). Pfizer in total, brand plus Hospira AG, still held about 15–18% in 2025, but fell to about 7–10% in Q1 2026, consistent with Pfizer supply problems.

### Cited Findings

**A. Medicaid SDUD, testosterone cypionate: Rx by labeler code** (COMPUTED). Columns are each labeler's share of generic Rx, which includes the Hospira AG and excludes brand and NDA products. Source: [SDUD datasets](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536).

| Labeler (code) | 2022 | 2023 | 2024 | 2025 | Q1 2026 |
|---|---|---|---|---|---|
| Hikma (00143) | 22.3% | **36.5%** | **33.3%** | **25.7%** | **32.2%** |
| Padagis (00574) | **34.0%** | 32.0% | 19.0% | 16.7% | 21.2% |
| Hospira/Pfizer AG (00409) | 2.5% | 13.3% | 21.6% | 16.4% | 8.2% |
| Wilshire (52536) | 2.0% | 3.1% | 8.9% | 11.8% | 10.5% |
| Xiromed (70700) | – | 1.2% | 2.2% | 10.1% | 10.1% |
| Cipla (69097) | 15.1% | 9.9% | 11.5% | 9.8% | 9.4% |
| NorthStar Rx (72603) | – | – | 0.0% | 4.8% | 4.0% |
| Eugia (55150) | – | – | 1.3% | 3.5% | 3.5% |
| Alvogen (47781) | – | 1.8% | 1.9% | 1.0% | 0.9% |
| Sun (62756) | 22.9% | 1.2% | 0.2% | 0.1% | 0.1% |
| Actavis/Teva (00591) | 1.1% | 1.0% | 0.2% | 0.1% | 0.0% |
| **Generic Rx (sum of states)** | 476,585 | 516,261 | 518,908 | 571,344 | 130,078 |
| **Brand Depo-Testosterone (00009) Rx** | 34,780 | 50,173 | 20,804 | 12,395 | 1,822 |
| **Brand share of ALL cypionate Rx** | **6.8%** | **8.9%** | **3.9%** | **2.1%** | **1.4%** |
| Pfizer total (brand + AG) share of all Rx | 9.1% | 21.0% | 24.6% | 18.1% | 9.5% |
| Total cypionate Rx, all products | 511,365 | 566,434 | 539,712 | 583,739 | 131,900 |
| Total amount reimbursed, all cypionate | $16.69M | $19.27M | $18.76M | $20.98M | $4.90M |

- **Absolute 2025 Medicaid Rx:**
  - Hikma 146,600
  - Padagis 95,474
  - Hospira AG 93,545
  - Wilshire 67,534
  - Xiromed 57,681
  - Cipla 56,250
  - NorthStar 27,642
  - Eugia 20,099
  - Alvogen 5,683
  
  (COMPUTED, [SDUD 2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536))
- **2025 Medicaid reimbursement per Rx** (COMPUTED) is about $34–40 for every generic: Hikma $36.1, Padagis $37.6, Hospira $34.0, Xiromed $39.8, Cipla $36.0, Eugia $38.3. Brand Depo-Testosterone shows an anomalously low $7.8 per Rx in Medicaid, which I have not explained. Generic reimbursement is 99.5% of Medicaid cypionate dollars.
- **Quarterly SDUD shares, % of all cypionate Rx** (COMPUTED). These show the event timeline:

| Quarter | Sun | Pfizer AG | Brand | Xiromed + NorthStar | Hikma |
|---|---|---|---|---|---|
| Q4 2022 | 18.0% | 2.3% | 8.0% | – | |
| Q1 2023 | 3.1% | 7.1% | 11.8% | – | |
| Q4 2023 | | 16.5% | | | 43.3% |
| Q4 2024 | | 22.6% | | 4.1% | |
| Q1 2025 | | | | 9.9% | |
| Q3 2025 | | | | 18.6% | |
| Q1 2026 | | 8.1% | | 13.9% | |

  - Sun's exit happened at the 2022/23 turn (18.0% to 3.1% in one quarter), and the brand and Pfizer AG absorbed the gap at first (AG 2.3% to 7.1%, brand 8.0% to 11.8%).
  - Hikma peaked at 43.3% in Q4 2023.
  - Hospira AG peaked at 22.6% in Q4 2024, then fell to 8.1% by Q1 2026.
  - Xiromed plus NorthStar ramped from 4.1% (Q4 2024) to 18.6% (Q3 2025).

  — [SDUD](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536)

**B. Medicaid SDUD by ANDA / manufacturer** (COMPUTED from NDC-level mapping in Q2). Columns are share of generic Rx.

| Manufacturer (ANDA) | 2022 | 2023 | 2024 | 2025 | Q1 2026 |
|---|---|---|---|---|---|
| Hikma Portugal ANDA 091244 (Hikma + Padagis-0827 + Cipla-802 + Actavis-4128) | 49.0% | 64.2% | 52.1% | **40.5%** | 48.9% |
| Pfizer AG (Hospira) ANDA 085635 | 2.5% | 13.3% | 21.6% | 16.4% | 8.2% |
| Xiromed ANDA 215351 (Xiromed + NorthStar) | – | 1.2% | 2.2% | **14.9%** | 14.1% |
| Wilshire / Pii ANDA 206368 | 2.0% | 3.1% | 8.9% | 11.8% | 10.5% |
| Cipla own ANDA 210362 | – | – | 4.7% | 6.0% | 7.7% |
| Padagis own ANDA 040530 (GRAM) | 23.6% | 15.2% | 7.2% | 5.8% | 6.2% |
| Eugia ANDA 211817 | – | – | 1.3% | 3.5% | 3.5% |
| American Regent ANDA 207742 (incl. Alvogen) | – | 1.8% | 1.9% | 1.0% | 0.9% |
| Sun ANDA 201720 | 22.9% | 1.2% | 0.2% | 0.1% | 0.1% |

- **Product-level splits** in SDUD Rx (COMPUTED):

| Product | 2022 | 2023 | 2024 | 2025 | Q1 2026 |
|---|---|---|---|---|---|
| Padagis own 0574-0820 | 112,471 | 78,533 | 37,349 | 32,972 | 8,011 |
| Padagis Hikma-made 0574-0827 | 49,618 | 86,811 | 61,179 | 62,502 | 19,522 |
| Cipla Hikma-made 69097-802 | 71,885 | 50,971 | 35,239 | 21,706 | 2,136 |
| Cipla own 69097-537/536 | 0 | 0 | 24,257 | 34,544 | 10,052 |

  Cipla is migrating from Hikma-sourced supply to its own ANDA (own ANDA = 82% of Cipla Medicaid Rx in Q1 2026). — [SDUD](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536)

**C. Medicare Part D, testosterone cypionate: claims by manufacturer.** Shares are of generic claims (reported data, shares COMPUTED). Sources: [CMS Part D Spending by Drug DY2024](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?filter[Gnrc_Name]=Testosterone%20Cypionate); [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?filter[Gnrc_Name]=Testosterone%20Cypionate).

| Mftr (CMS label) | 2022 | 2023 | 2024 | 2025 | Q1 2026 |
|---|---|---|---|---|---|
| West-Ward/Hikma | 18.2% | 31.5% | **31.1%** | **22.9%** | **29.2%** |
| Padagis (both CMS names: "Padagis" + "Perrigo/Padagis") | **34.1%** | **34.0%** | 21.4% | 19.1% | 24.3% |
| Hospira/Pfizer (AG) | 2.2% | 13.2% | 20.3% | 15.4% | 7.4% |
| Xiromed | – | 2.3% | 4.3% | 12.3% | 11.5% |
| Wilshire | 2.8% | 4.1% | 7.1% | 10.5% | 9.7% |
| Cipla USA | 13.5% | 10.6% | 12.0% | 9.5% | 9.1% |
| Eugia US | – | – | 1.8% | 5.2% | 5.0% |
| NorthStar Rx | – | – | – | 3.9% | 2.7% |
| Alvogen | – | 1.9% | 1.9% | 1.2% | 1.1% |
| Sun | 27.0% | 0.9% | 0.1% | 0.03% | 0.02% |
| Actavis/Teva | 2.4% | 1.4% | 0.03% | 0.003% | – |
| **Generic claims** | 826,420 | 935,403 | 1,118,253 | 1,257,735 | 320,749 |
| **Depo-Testosterone brand claims** | 5,308 (0.6% of all) | 19,910 (2.1%) | 2,818 (0.25%) | 502 (0.04%) | 38 (0.01%) |
| Azmiro (Azurity NDA) claims | – | – | – | 88 ($56.1K) | 23 |
| Total cypionate Part D spend | $40.66M | $38.95M | $41.55M | $41.79M | $11.25M |

- **Earlier Part D context.**
  - 2020: Padagis 40.9% (two labels combined), Hikma 15.9%, Sun 15.8%, Cipla 11.1%, Hospira 7.0%, Wilshire 5.2%.
  - 2021: Sun 25.2%, Padagis 36.0%, Hikma 18.6%, Cipla 11.9%.
  - Generic Part D claims grew from 771,644 (2020) to 1,257,735 (2025), +63%.
  
  — [CMS Part D Spending by Drug](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?filter[Gnrc_Name]=Testosterone%20Cypionate)
- **2025 Part D spend per claim** (reported spend ÷ claims, COMPUTED): Hikma $29.6, Cipla $29.6, Alvogen $27.6, Hospira $33.6, Wilshire $34.4, Xiromed $35.4, Perrigo/Padagis $36.1, Padagis $39.3, Eugia $33.1, NorthStar $31.6. — [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?filter[Gnrc_Name]=Testosterone%20Cypionate)

**D. Combined proxy: Medicaid Rx + Medicare Part D claims, generic cypionate** (COMPUTED; adds Rx and claims as equivalent prescription counts).

| Labeler | 2025 | Q1 2026 |
|---|---|---|
| Hikma | **23.8%** | **30.1%** |
| Padagis | 18.3% | 23.4% |
| Hospira/Pfizer AG | 15.7% | 7.6% |
| Xiromed | 11.6% | 11.1% |
| Wilshire | 10.9% | 9.9% |
| Cipla | 9.6% | 9.2% |
| Eugia | 4.7% | 4.6% |
| NorthStar | 4.2% | 3.0% |
| Alvogen | 1.2% | 1.0% |
| Sun / Actavis / American Regent label | ~0% | ~0% |
| Total generic Rx + claims | 1,829,079 | 450,827 |
| Brand Depo-Testosterone share of brand + generic | 0.7% | 0.4% |

**E. ESTIMATED manufacturer (ANDA) share, combined Medicaid + Part D** (COMPUTED with assumptions).
- *Assumption 1:* Part D's "Perrigo/Padagis" label equals the Hikma-made 0574-0827, and "Padagis" equals the own-ANDA 0574-0820. I inferred this because the two labels' year-to-year swings in Part D move in step with the two Padagis NDCs in SDUD. CMS does not state it.
- *Assumption 2:* Part D Cipla claims are split by the SDUD NDC mix: 61.4% own ANDA in 2025, 82.5% in Q1 2026.

| Manufacturer (ANDA) | 2024 | 2025 | Q1 2026 |
|---|---|---|---|
| Hikma Portugal ANDA 091244 | 51.2% | **38.3%** | 46.6% |
| Xiromed / Farmalán ANDA 215351 | 3.6% | 15.8% | 14.1% |
| Pfizer AG (Hospira) | 20.7% | 15.7% | 7.6% |
| Wilshire / Pii | 7.7% | 10.9% | 9.9% |
| Padagis own (GRAM) | 8.3% | 7.6% | 8.5% |
| Cipla own | 4.8% | 5.9% | 7.6% |
| Eugia | 1.7% | 4.7% | 4.6% |
| American Regent (incl. Alvogen) | 1.9% | 1.2% | 1.0% |
| Sun | 0.1% | ~0% | ~0% |

**F. Testosterone enanthate**

*Medicaid SDUD Rx* (COMPUTED). Generic vial share is Hikma's share of non-Xyosted Rx.

| | 2022 | 2023 | 2024 | 2025 | Q1 2026 |
|---|---|---|---|---|---|
| Hikma vial (0143-9750) | 5,107 | 7,102 | 6,606 | 7,999 | 1,651 |
| Hikma share of generic vial Rx | 92.6% | 95.3% | 94.7% | 98.5% | 100% |
| Actavis residual Rx (0591-3221, NDC marketing ended 2019) | 407 | 351 | 297 | 27 | – |
| Padagis obsolete NDC (reported with $0) | – | – | 73 | 93 | – |
| Xyosted autoinjector Rx | 7,334 | 13,488 | 17,730 | 20,686 | 4,835 |

  - Eugia's enanthate (55150-0336-01) has **zero** SDUD rows through Q1 2026.
  - Xyosted is 71.8% of 2025 Medicaid enanthate Rx and 96.2% of enanthate dollars ($14.06M of $14.62M).
  - Hikma's vial was reimbursed at $69.7 per Rx in 2025.
  
  — [SDUD](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536)

*Medicare Part D.* Generic testosterone enanthate is 100% West-Ward/Hikma in every year from 2020 to Q1 2026.

| Year | Hikma claims | Hikma spend | Xyosted claims | Xyosted spend |
|---|---|---|---|---|
| 2020 | 9,337 | | 10,827 | |
| 2022 | 9,118 | | | |
| 2024 | 10,421 | $796K | 36,669 | $28.9M |
| 2025 | 12,108 | $939K | 47,254 | $37.5M |
| Q1 2026 | 3,131 | | | |

  — [CMS Part D DY2024](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?filter[Gnrc_Name]=Testosterone%20Enanthate); [CMS Quarterly](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?filter[Gnrc_Name]=Testosterone%20Enanthate)

### Inferences
- **The two independent government datasets agree closely** on 2025 rankings and magnitudes: Hikma #1, then Padagis, Pfizer AG, Wilshire, Xiromed and Cipla in a 10–19% band, with Eugia and NorthStar around 4–5%. That agreement gives reasonable confidence the proxy reflects the national retail picture. It may under-represent cash/telehealth TRT channels, which skew to 10 mL vials and compounding.
- **Brand share against generics is now immaterial:** under 1% of combined government Rx in 2025 and 0.4% in Q1 2026. Pfizer's relevance comes almost entirely through the Hospira AG, whose share fell sharply in late 2025 and Q1 2026. That timing coincides with the Pfizer manufacturing delays reported by ASHP and international regulators (see Q4).
- **Recent entrants have taken meaningful share within about two years.** Xiromed went from launch in April 2023 to about 15% of generic volume (manufacturer level) by 2025. Eugia went from launch in Nov 2023 to about 4–5%. Wilshire rose from about 2–3% to about 11% as Sun exited. This suggests a new low-cost vial entrant could plausibly reach mid-single-digit share. The Sun exit and Pfizer supply problems both opened windows.
- **Price per Rx is low and compressing.** Medicaid paid about $34–40 per generic Rx in 2025, and Part D spend per claim was about $28–39. Medicare spend stayed flat at about $41M while claims rose 63% (2020–2025), implying falling price per claim. This fits a commoditised market.
- **Generic enanthate vials are effectively a Hikma monopoly,** but a small one: about 8K Medicaid and about 12K Part D claims in 2025, versus about 1.8M combined for cypionate. Eugia's 2024 approval has not yet produced visible claims.

### Gaps
- No IQVIA NPA/NSP Rx or unit share by labeler was publicly available. All shares above are government-channel proxies (Medicaid FFS/MCO and Medicare Part D) and exclude commercial and cash. The brief's labeler-code hypothesis "0591/0143 = Actavis/Hikma" is resolved as: 0591 = Actavis Pharma (Teva), 0143 = Hikma.
- The CMS mapping of "Perrigo/Padagis" vs "Padagis" to specific NDCs is inferred, not documented.
- SDUD Q1 2026 is likely incomplete, and Q2 2026 is not yet published.
- Medicaid unit data has errors (see method notes), so unit shares are unreliable for Wilshire and Padagis.

---

## Q4. Company commentary and IQVIA market-size figures

### Takeaway
Launch press releases quote IQVIA sizes for "Depo-Testosterone and its generics" of about $191M (12 months to April 2018, Cipla), $193.8M (12 months to Feb 2023, Xiromed) and $226.8M (12 months to Aug 2023, Aurobindo/Eugia). I found no earnings-call commentary from Hikma, Cipla, Aurobindo, Padagis or Pfizer naming testosterone cypionate as a material product or giving share. The supply events that reshaped share are documented: Sun's 2022 recall and exit, and Pfizer's 2025–26 manufacturing delays.

### Cited Findings
- **Xiromed, April 13, 2023 (press release):** ANDA approval for Testosterone Cypionate Injection USP, generic to Depo-Testosterone, with "Xiromed will launch immediately." It reported "Annual market sales for Depo-Testosterone® and its generics for the twelve-month period ending February, 2023 were $193.8 million, according to IQVIA." CEO Rob Spina said it is "the third product approval from Laboratorios Farmalan, our dedicated injectable hormonal facility in Leon, Spain." — [Xiromed press release](https://xiromed.com/usa/2023/04/13/xiromed-llc-launches-testosterone-cypionate-injection-usp/)
- **Aurobindo / Eugia, Oct 23, 2023 (stock-exchange filing):** final approval for 100 mg/mL and 200 mg/mL multi-dose vials and a 200 mg/mL single-dose vial. "The product is expected to be launched in November 2023. The approved product has an estimated market size of US$ 226.8 million for the twelve months ending August 2023, according to IQVIA." It was Eugia's 169th ANDA approval. — [Aurobindo filing PDF](https://www.aurobindo.com/api/uploads/corporateannouncements/Fy24_TESTOSTERONE%20CYPRIONATE%20INJ%20APPROVAL.pdf)
- **Cipla, June 2018:** final approval for 100 mg/mL and 200 mg/mL, AO-rated to Depo-Testosterone. Per IQVIA, "Depo-Testosterone and its generic equivalents had US sales of approximately $191M for the 12-month period ending April 2018." The Cipla PDF returned HTTP 503 when fetched, so this figure comes from a search-engine summary of the PDF and Business Standard coverage. — [Cipla PR](https://www.cipla.com/sites/default/files/1529557824_Press-Release-Testosterone%20Cypionate%20Inj.pdf); [Business Standard](https://www.business-standard.com/article/news-cm/cipla-receives-final-approval-for-testosterone-cypionate-injection-118062100140_1.html)
- **BPI Labs (ANDA 219478, approved 2026-09-03):** I found no press release or IQVIA figure. — [Orange Book data files](https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files)
- **Eugia's enanthate approval (Feb 28, 2024):** I found no IQVIA figure.
- **Sun Pharma recall, June 2022:** Sun recalled lots HAC1974A and HAC1978A of Testosterone Cypionate Injection 200 mg/mL (NDC 62756-015-40). The recall followed "an out-of-specification (OOS) and out-of-trend (OOT) impurity result" traced to "the active pharmaceutical ingredient (API) lot". — [California Board of Pharmacy recall notice, 06/08/22](https://www.pharmacy.ca.gov/about/recall_alerts/060822_sun.pdf)
- **ASHP shortage page, dated March 5, 2026:** It reportedly says Sun discontinued testosterone cypionate in late 2023, Pfizer's Depo-Testosterone is on shortage due to manufacturing delays, and Hikma, Padagis, Eugia and Cipla have product available. The page blocked direct fetch (403), so these details come from a search-result summary.
  - The SDUD data **contradicts the "late 2023" timing**: Sun's Medicaid share collapsed between Q4 2022 (18.0%) and Q1 2023 (3.1%). That points to supply ending around late 2022, with only residual Rx afterwards.
  
  — [ASHP Drug Shortage Detail](https://www.ashp.org/Drug-Shortages/Current-Shortages/Drug-Shortage-Detail.aspx?id=592)
- **Pfizer Depo-Testosterone supply problems in other markets:**
  - Health Canada: shortage for "Disruption of the manufacture of the drug", 2025-01-17 to 2025-10-23. — [Health Products Shortages Canada](https://healthproductshortages.ca/shortage/247166)
  - New Zealand PHARMAC: out-of-stock expected late Oct–Dec 2025 "due to delays at the factory making Depo-Testosterone". — [PHARMAC](https://pharmac.govt.nz/medicine-funding-and-supply/medicine-notices/testosterone)
- **openFDA drug-shortages endpoint (queried Oct 2026):** no current testosterone cypionate or enanthate entries. — [openFDA shortages API](https://api.fda.gov/drug/shortages.json?search=testosterone)
- **Hikma:** searches found no transcript in which Hikma discusses testosterone cypionate specifically. H1 2026 commentary covered injectables stabilisation generally. — [MarketBeat H1 2026 call summary](https://www.marketbeat.com/instant-alerts/hikma-pharmaceuticals-h1-earnings-call-highlights-2026-08-06/)

### Inferences
- **Bridge from IQVIA to government channels** (COMPUTED/ESTIMATED): IQVIA put the cypionate market at roughly $194–227M in 2023. Medicaid plus Part D reimbursed about $63M in 2025 ($21.0M + $41.8M) on about 1.84M Rx/claims, which is roughly 25–30% of the IQVIA dollar figure. Commercial, cash and telehealth make up the rest. This is a rough bridge only: IQVIA uses invoice/WAC-based dollars, while the CMS figures are gross reimbursement.
- **The IQVIA figures are not a trend series.** Each covers a different 12-month window and is self-reported in a press release. The rise from $191M (2018) to $227M (2023), against falling unit prices, implies strong volume growth. That matches the +63% growth in Part D claims from 2020 to 2025.

### Gaps
- I found no recent (2025–2026) IQVIA market size for testosterone cypionate or enanthate vials.
- I found no company-disclosed share figures, and no Indian annual-report or investor-presentation commentary (Cipla, Aurobindo, Sun) quantifying testosterone revenue.
- Searches for Padagis, Alvogen, Wilshire/Arbor and Pfizer commentary found nothing specific.

---

## Q5. Market concentration (top 3, HHI) and marginal players

### Takeaway
Concentration fell sharply as Sun exited and Xiromed, Eugia, Alvogen and Wilshire grew.
- **Labeler level:** top-3 share dropped from about 79–82% (2022–23) to about 57–59% in 2025, with HHI going from about 2,400–2,650 to about 1,520–1,580. It rebounded to about 64–65% top-3 (HHI about 1,850) in Q1 2026 as the Pfizer AG lost volume.
- **Manufacturer level:** concentration is higher. Hikma Portugal alone is about 38–49%, and top-3 is about 70% in 2025 and Q1 2026.
- **Marginal players:** Alvogen/American Regent (about 1%), Sun (exited, about 0%), Actavis/Teva (exited May 2025), the brand (under 1% combined), Azmiro (negligible), repackagers (no visible claims) and BPI Labs/Ajenat (launched Sept 2026, no data yet).

### Cited Findings
All rows are COMPUTED from SDUD and CMS Part D (sources above). Top-3 is the combined share of the three largest players. HHI is the sum of squared percentage shares.

| Basis | Period | Top-3 share | HHI | Largest player |
|---|---|---|---|---|
| Medicaid SDUD, generic Rx by labeler code | 2022 | 79.3% | 2,421 | Padagis 34.0% |
| | 2023 | 81.9% | 2,653 | Hikma 36.5% |
| | 2024 | 73.9% | 2,157 | Hikma 33.3% |
| | 2025 | 58.7% | 1,581 | Hikma 25.7% |
| | Q1 2026 | 63.9% | 1,881 | Hikma 32.2% |
| Medicare Part D, generic claims by manufacturer label (Padagis labels combined) | 2022 | 79.2% | 2,416 | |
| | 2023 | 78.7% | 2,468 | |
| | 2024 | 72.8% | 2,056 | |
| | 2025 | 57.4% | 1,521 | |
| | Q1 2026 | 65.0% | 1,842 | |
| Combined Medicaid + Part D, labeler level | 2025 | 57.8% | 1,535 | |
| | Q1 2026 | 64.6% | 1,848 | |
| Combined, manufacturer/ANDA level (estimated, see Q3-E) | 2024 | 80.2% | 3,219 | |
| | 2025 | 69.8% | 2,195 | |
| | Q1 2026 | 70.7% | 2,680 | |
| Medicaid only, manufacturer/ANDA level (no Part D assumptions) | 2025 | Hikma 40.5% + Pfizer AG 16.4% + Xiromed 14.9% = 71.8% | | |

**Marginal or low-share players, 2025 combined generic Rx + claims** (COMPUTED)
- Alvogen (American Regent-made), 1.2%. American Regent's own label is under 0.01% (14 Part D claims).
- Sun, 0.05%. Exited; Orange Book shows DISCN.
- Actavis/Teva, about 0.02%. Its NDC marketing ended 2025-05-31.
- Brand Depo-Testosterone, 0.7% of brand + generic.
- Azurity Azmiro, 88 Part D claims and 0 unsuppressed Medicaid Rx.
- Repackagers, zero SDUD rows.
- BPI Labs / Ajenat, no data yet (launched 2026-09-14).
- Eugia (4.7%) and NorthStar (4.2%) are small but growing.

### Inferences
- **For an entrant, the relevant structure has three tiers:**
  - Dominant: Hikma, about 40% of manufactured volume, as both the leading label and the supplier to Padagis and Cipla.
  - Mid-tier (10–16% each): Pfizer AG, Xiromed and Wilshire.
  - Tail (under 8% each): Padagis own, Cipla own, Eugia and American Regent.
- **Share is fluid.** Two supply shocks (Sun 2022/23, Pfizer 2025/26) and four entries (Alvogen 2022, Xiromed 2023, Eugia 2023, BPI 2026) moved double-digit share within a few quarters. Reliable supply appears to be a key competitive lever, which would favour an API-integrated entrant such as Symbiotec if its quality systems hold up (cf. Sun's API-impurity recall).
- **Hikma's dependence-based supply deals are a possible opening.** Padagis and Cipla both distribute Hikma-made product, and Cipla is visibly migrating to its own ANDA. A new low-cost source could target distributor or private-label relationships (Padagis, NorthStar, Alvogen-type), not only direct share.
- **Enanthate vials are highly concentrated** (Hikma about 100% of generic claims), but the market is tiny next to cypionate. Branded Xyosted dominates enanthate dollars.

### Gaps
- No IQVIA-based concentration figures are available.
- Commercial and cash channels, which may be more fragmented and more exposed to telehealth and compounding, are not covered.
- I had no 2026 data beyond Q1, so BPI Labs' impact cannot be measured.
