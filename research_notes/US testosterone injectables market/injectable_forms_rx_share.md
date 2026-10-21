# US Testosterone Injectables Market: Dosage Forms, Molecules and Rx Share

Scope note: all figures are US-only. Each one carries its year and metric type: claims or prescriptions (≈TRx), NRx, units, or value (gross spend, reimbursement, WAC or NADAC). **[Reported]** means the figure comes straight from a source or dataset. **[Computed]** means I derived it from reported data. **[Estimate/Inference]** means it is analytical judgement. Public payer data (Medicare Part D, Medicare Part B, Medicaid SDUD) were pulled directly from the CMS and Medicaid APIs on 21 Oct 2026. These datasets are **not** representative of the whole US market. They miss commercial insurance and the cash-pay telehealth channel, which is younger and probably even more cypionate-heavy. Treat their shares as directional proxies, not IQVIA national TRx shares.

Dataset links used throughout:
- Medicare Part D Spending by Drug, annual file (DY2020–2024): [CMS API](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?keyword=testosterone)
- Medicare Quarterly Part D Spending by Drug (2025 Q1–Q4 and 2026 Q1): [CMS API](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)
- Medicare Part B Spending by Drug (DY2020–2024): [CMS API](https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data?keyword=testosterone)
- Medicaid State Drug Utilization Data (SDUD), national rows (state = "XX", FFS + MCO): [2023](https://data.medicaid.gov/dataset/d890d3a9-6b00-43fd-8b31-fcba4c8e2909), [2024](https://data.medicaid.gov/dataset/61729e5a-7aa8-448c-8903-ba3e0cd0ea3c), [2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536)
- NADAC weekly files: [2020](https://data.medicaid.gov/dataset/c933dc16-7de9-52b6-8971-4b75992673e0), [2021](https://data.medicaid.gov/dataset/d5eaf378-dcef-5779-83de-acdd8347d68e), [2022](https://data.medicaid.gov/dataset/dfa2ab14-06c2-457a-9e36-5cb6d80f8d93), [2023](https://data.medicaid.gov/dataset/4a00010a-132b-4e4d-a611-543c9521280f), [2024](https://data.medicaid.gov/dataset/99315a95-37ac-4eee-946a-3c523b4c481e), [2025](https://data.medicaid.gov/dataset/f38d0706-1239-442c-a3cc-40ef1b686ac0), [2026](https://data.medicaid.gov/dataset/fbb83258-11c7-47f5-8b18-5f8e79f7e704)
- FDA application data via openFDA Drugs@FDA: [testosterone cypionate](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100), [testosterone enanthate](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+ENANTHATE%22&limit=100)

---

## 1. Which testosterone injectable and implant forms are marketed in the US today?

### Takeaway
The US injectable testosterone market rests on generic **testosterone cypionate (TC) IM vials**: 100 and 200 mg/mL, sold as 1 mL and 10 mL multi-dose vials, plus at least one 200 mg/mL single-dose vial. About 9 application holders have an active Rx status, and **BPI Labs** was approved as recently as Sept 2026. Around that core sit a few niche products: the Pfizer brand **Depo-Testosterone** (now almost gone from pharmacy claims), generic **testosterone enanthate (TE) IM vials** (in practice Hikma), **Xyosted** (TE subcutaneous autoinjector, Halozyme/Antares), **Aveed** (testosterone undecanoate IM, Endo), **Azmiro** (TC 200 mg/mL single-dose prefilled syringe/vial, Azurity) and **Testopel** pellets (Endo). The oral products Jatenzo, Tlando and Kyzatrex are relevant here only as context.

### Cited Findings
**Testosterone cypionate IM (multi-dose vials, generic plus brand)**
- openFDA lists these TC applications with "Prescription" marketing status: Pfizer's Depo-Testosterone (ANDA085635; 100 and 200 mg/mL), Hikma (ANDA090387, 100/200 mg/mL, approved 15 Jul 2010; ANDA091244, 200 mg/mL, 1 May 2012), Padagis (ANDA040530, 200 mg/mL, 2005), American Regent (ANDA207742, 200 mg/mL, 2017), Cipla (ANDA210362, 100/200 mg/mL, 19 Jun 2018), Wilshire (ANDA206368, 200 mg/mL, 24 Apr 2019), Xiromed (ANDA215351, 100/200 mg/mL, 13 Apr 2023), Eugia/Aurobindo (ANDA211817, 100/200 mg/mL, 20 Oct 2023) and **BPI Labs (ANDA219478, 200 mg/mL, approved 3 Sep 2026)**. Sun's ANDA201720, Rising's and Caplin's TC ANDAs are listed as "Discontinued". [Reported] — [openFDA Drugs@FDA, TC](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100)
- Eugia's Oct 2023 approval covered 100 mg/mL and 200 mg/mL **multi-dose vials and a 200 mg/mL single-dose vial**. IQVIA put the market for the approved product at $226.8M for the 12 months to Aug 2023. [Reported] — [Aurobindo disclosure](https://www.aurobindo.com/api/uploads/corporateannouncements/Fy24_TESTOSTERONE%20CYPRIONATE%20INJ%20APPROVAL.pdf); [Business Standard](https://www.business-standard.com/companies/news/aurobindo-pharma-arm-receives-fda-nod-for-testosterone-cypionate-injection-123102300453_1.html)
- NADAC currently prices three TC presentations: "TESTOSTERONE CYP 200 MG/ML" (1 mL; 11 NDCs as of 21 Oct 2026), "TESTOSTERONE CYP 2,000 MG/10 ML" (10 mL of 200 mg/mL; 10 NDCs) and "TESTOSTERONE CYP 1,000 MG/10 ML" (10 mL of 100 mg/mL; 4 NDCs). [Reported] — [NADAC 2026](https://data.medicaid.gov/dataset/fbb83258-11c7-47f5-8b18-5f8e79f7e704)
- In 2025, Medicare Part D recorded TC claims from these labelers: Hikma (West-Ward), Pfizer/Hospira, Xiromed, Padagis (also listed as Perrigo/Padagis), Wilshire, Cipla, Eugia, Northstar Rx, Alvogen, plus small amounts from Sun, Teva/Actavis and American Regent. [Reported] — [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)

**Testosterone enanthate IM (generic vials)**
- openFDA lists TE 200 mg/mL ANDAs with "Prescription" status for Hikma (ANDA091120, 2012), Nexus (ANDA040575, 2006) and Eugia (ANDA212659, approved 28 Feb 2024). Delatestryl (Endo, NDA009165), the original brand, is discontinued. [Reported] — [openFDA Drugs@FDA, TE](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+ENANTHATE%22&limit=100)
- Medicare Part D shows only one TE vial manufacturer with claims in 2020–2025: West-Ward/Hikma, with 12,108 claims in 2025. [Reported] — [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)
- NADAC prices one TE description, "TESTOSTERONE ENAN 200 MG/ML", with a single NDC. [Reported] — [NADAC 2026](https://data.medicaid.gov/dataset/fbb83258-11c7-47f5-8b18-5f8e79f7e704)

**Testosterone enanthate SC autoinjector: Xyosted**
- Xyosted (NDA209863, Antares Pharma) was approved 28 Sep 2018 as a subcutaneous solution in 50, 75 and 100 mg/0.5 mL strengths. [Reported] — [openFDA Drugs@FDA, TE](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+ENANTHATE%22&limit=100)
- Halozyme, which acquired Antares in 2022, describes Xyosted as "the only FDA-approved SC testosterone enanthate product for once-weekly, at-home self-administration". It sells Xyosted through Cardinal, McKesson and Cencora. [Reported] — [Halozyme FY2024 10-K](https://www.sec.gov/Archives/edgar/data/1159036/000115903625000010/halo-20241231.htm)

**Testosterone undecanoate IM: Aveed**
- Aveed (NDA022219, Endo) was approved 5 Mar 2014 as an IM injectable and still has Rx status. [Reported] — [openFDA Drugs@FDA, Aveed](https://api.fda.gov/drug/drugsfda.json?search=openfda.brand_name:%22AVEED%22&limit=3)
- Aveed is given in clinic, so most of its volume shows up in Medicare **Part B** (HCPCS J3145) rather than Part D. See Q2. [Reported] — [CMS Part B Spending by Drug](https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data?keyword=testosterone)

**Azmiro (testosterone cypionate, Azurity)**
- Azmiro was approved under **NDA216318 on 2 Jun 2022** (200 mg/mL IM solution). In the openFDA extract accessed Oct 2026 its marketing status reads **"Discontinued"**. [Reported] — [openFDA Drugs@FDA, Azmiro](https://api.fda.gov/drug/drugsfda.json?search=openfda.brand_name:%22AZMIRO%22&limit=5)
- Azurity announced commercial availability on 11 Dec 2024, calling it the "first and only FDA-approved prefilled testosterone cypionate injection" (a 200 mg/mL single-dose syringe). [Reported] — [US Pharmacist](https://www.uspharmacist.com/article/azurity-pharmaceuticals-inc-announces-availability-of-azmiro-testosterone-cypionate-injection-for-intramuscular-use-ciii); [Drug Topics, Jan 2025](https://www.drugtopics.com/view/testosterone-replacement-therapy-azmiro-now-available-in-us)
- The Medical Letter calls Azmiro the first TC formulation available in **single-dose vials and prefilled syringes**. It notes that TC has long been sold in multi-dose vials (Depo-Testosterone and generics) and warns that TC can crystallize if stored below the recommended temperature. [Reported] — [Medical Letter](https://secure.medicalletter.org/TML-article-1724b)
- Uptake has been minimal: 88 Part D claims and $56.1K of spend in 2025, then 23 claims in Q1 2026. Medicaid SDUD shows 0 unsuppressed Rx in 2025. [Reported] — [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone); [SDUD 2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536)

**Testosterone pellets: Testopel**
- Testopel (ANDA080911, Endo) is a pellet for implantation, originally approved 13 Jul 1972, and still has Rx status. [Reported] — [openFDA Drugs@FDA, Testopel](https://api.fda.gov/drug/drugsfda.json?search=openfda.brand_name:%22TESTOPEL%22&limit=3)

**Oral testosterone (context only)**
- Tlando (NDA208088, Verity) was approved 28 Mar 2022 as an oral capsule. [Reported] — [openFDA Drugs@FDA, Tlando](https://api.fda.gov/drug/drugsfda.json?search=openfda.brand_name:%22TLANDO%22&limit=3)
- Kyzatrex (Marius; oral testosterone undecanoate) was approved in July 2022. [Reported] — [NC Biotech](https://www.ncbiotech.org/news/marius-gains-fda-approval-testosterone-replacement-therapy)
- Jatenzo (Clarus, now Tolmar) is in Part D with 11,013 claims and $11.6M of spend in 2025. [Reported] — [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)

### Inferences
- Generic TC vials are commoditized and crowded, with about 9 active approved sources and Part D claims from 10+ labelers. A new entrant (BPI Labs) was approved as recently as Sept 2026. Symbiotec would enter as roughly the 10th–12th TC vial source, so it has to compete on API cost, reliability and packaging (1 mL vs 10 mL, single-dose) rather than on product differentiation. [Inference]
- The TE vial market is effectively a Hikma monopoly at the pharmacy level, despite approved Eugia and Nexus ANDAs. A small, under-contested niche of roughly 12K Part D claims could be an adjacent opportunity for an enanthate API supplier. [Inference]
- Azmiro shows that convenience presentations of TC (prefilled or single-dose) have so far won almost no volume, and openFDA's "Discontinued" status, if accurate, confirms that. [Inference]

### Gaps
- The user asked about Xiromed testosterone enanthate. I found no TE ANDA for Xiromed in openFDA and no Part D TE claims from Xiromed, so its status is unconfirmed.
- I could not confirm why Azmiro shows "Discontinued" in openFDA, or whether that is an artefact of the data snapshot. It still had Part D claims in Q1 2026.
- openFDA did not return Jatenzo or Kyzatrex records under brand-name search, so their approval details rest on the cited news source only.
- Compounded testosterone (cypionate in grapeseed oil, creams) sold by 503A/503B pharmacies and telehealth clinics is not captured in any dataset I used.

---

## 2. What is the Rx share of each injectable form, and what share of total TRT do injectables hold?

### Takeaway
Every public dataset tells the same story. **Generic testosterone cypionate makes up about 92–96% of injectable testosterone prescriptions**, and Xyosted is the only other form with meaningful volume (about 3–4% of injectable Rx). TE vials, Aveed, pellets and brand Depo-Testosterone/Azmiro each hold about 1% or less. **Injectables account for roughly two-thirds (Medicare, 2025: 67%) to over 80% (Medicaid, 2025: 82%) of all TRT prescriptions.** EHR data (Truveta) put injectables at about 74% of patients on injectable or topical therapy in 2026. By **value**, injectables are much smaller because generic TC is so cheap: 43.5% of Medicare Part D testosterone spend in 2025, and about half of that injectable spend is Xyosted. The newest national IQVIA figures I found are from 2021: about 8.0M TRx in total, and a $545M injectable market at WAC against a $1.4B total TRT market.

### Cited Findings
**A. Medicare Part D (pharmacy-dispensed), claims ≈ TRx, gross spend before rebates**

[Reported] raw figures from [CMS Part D annual](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?keyword=testosterone) (2020–2024) and [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone) (2025 Q1–Q4); shares are [Computed]:

| Form (Part D) | 2020 claims | 2023 claims | 2024 claims | 2025 claims | 2025 share of injectable claims | 2025 share of all TRT claims | 2025 gross spend | 2025 share of injectable spend |
|---|---|---|---|---|---|---|---|---|
| Generic TC vials | 771,644 | 935,403 | 1,118,253 | 1,257,735 | 95.3% | 63.7% | $41.71M | 50.2% |
| Depo-Testosterone (brand TC) + Azmiro | 14,456 | 19,910 | 2,818 | 590 (502 + 88) | 0.04% | 0.03% | $0.09M | 0.1% |
| Xyosted (TE SC autoinjector) | 10,827 | 27,535 | 36,669 | 47,254 | 3.6% | 2.4% | $37.46M | 45.1% |
| Generic TE vials (Hikma) | 9,337 | 10,411 | 10,421 | 12,108 | 0.9% | 0.6% | $0.94M | 1.1% |
| Aveed (TU IM) | 664 | 757 | 846 | 844 | 0.06% | 0.04% | $1.73M | 2.1% |
| Testopel (pellet) | 404 | 919 | 1,127 | 1,141 | 0.09% | 0.06% | $1.23M | 1.5% |
| **Injectables + pellet subtotal** | **807,332** | **994,935** | **1,170,134** | **1,319,672** | 100% | **66.9%** | **$83.15M** | 100% |
| Topical/nasal/patch (generic "Testosterone", AndroGel, Androderm, Testim, Natesto) | 434,023 | 503,880 | 561,584 | 641,296 | — | 32.5% | $94.94M | — |
| Oral (Jatenzo, Tlando, methyltestosterone) | 0 | 5,450 | 8,323 | 12,283 | — | 0.6% | $13.15M | — |
| **Total TRT** | **1,241,355** | **1,504,265** | **1,740,041** | **1,973,251** | — | 100% | **$191.23M** | — |

- Injectables' share of Part D TRT **claims** [Computed]: 65.0% (2020), 64.7% (2022), 66.1% (2023), 67.2% (2024), 66.9% (2025), 67.6% (Q1 2026).
- Injectables' share of Part D TRT **gross spend** [Computed]: 22.2% (2020), 28.3% (2022), 32.8% (2023), 40.8% (2024), 43.5% (2025). The rise reflects collapsing topical prices plus Xyosted growth.
- Generic TC claims grew 63% from 2020 to 2025 (about **10.3% CAGR**), including +19.5% in 2024 and +12.5% in 2025 [Computed]. Over the same five years Xyosted claims rose 4.4x (10,827 to 47,254) [Computed].
- Q1 2026 Part D [Reported]: generic TC 320,749 claims ($11.24M), Xyosted 11,753 claims ($9.55M), TE vials 3,131, Aveed 212, Testopel 241, Depo-Testosterone 38, Azmiro 23. Injectables were 67.6% of claims [Computed]. — [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)
- In the annual file, Depo-Testosterone claims swing sharply: 14,456 (2020), 5,308 (2022), 19,910 (2023), 2,818 (2024). The 2023 spike looks like a temporary supply or substitution effect. [Reported] — [CMS Part D annual](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?keyword=testosterone)

**B. Labeler share within generic TC (Medicare Part D claims)**, [Computed] from [Reported] manufacturer-level rows ([annual file](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?keyword=testosterone) for 2024; [quarterly file](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone) for 2025):

| Labeler | 2024 claims (share) | 2025 claims (share) |
|---|---|---|
| Hikma (West-Ward) | 347,386 (31.1%) | 288,295 (22.9%) |
| Padagis (incl. Perrigo/Padagis) | 239,457 (21.4%) | 240,108 (19.1%) |
| Pfizer/Hospira generic | 227,107 (20.3%) | 193,646 (15.4%) |
| Xiromed | 47,567 (4.3%) | 154,456 (12.3%) |
| Wilshire | 79,310 (7.1%) | 131,520 (10.5%) |
| Cipla | 134,504 (12.0%) | 120,062 (9.5%) |
| Eugia (Aurobindo) | 20,419 (1.8%) | 65,151 (5.2%) |
| Northstar Rx | — | 48,482 (3.9%) |
| Alvogen | 21,068 (1.9%) | 15,583 (1.2%) |
| Sun, Teva/Actavis, American Regent | 1,435 (0.1%) | 432 (<0.1%) |
| **Total generic TC** | **1,118,253** | **1,257,735** |

**C. Medicare Part B (physician-administered in office), claims and spend**, [Reported] — [CMS Part B Spending by Drug](https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data?keyword=testosterone)
- J1071, TC per 1 mg: 421,841 claims (2020), 337,396 (2023), **313,953 (2024)**. 2024 spend was only $1.27M (31,841 beneficiaries).
- J3145, testosterone undecanoate (Aveed): 12,380 claims (2020), 14,579 (2023), **14,649 (2024)**. 2024 spend was **$19.94M** (3,821 beneficiaries).
- J3121, TE per 1 mg: 6,636 claims (2020), 3,814 (2023), 3,468 (2024). 2024 spend was $21.4K.

**D. Medicaid SDUD (national, FFS + MCO), prescriptions and total amount reimbursed**

[Reported] raw figures from [SDUD 2023](https://data.medicaid.gov/dataset/d890d3a9-6b00-43fd-8b31-fcba4c8e2909), [SDUD 2024](https://data.medicaid.gov/dataset/61729e5a-7aa8-448c-8903-ba3e0cd0ea3c) and [SDUD 2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536). NDCs were classified by form using NADAC descriptions and openFDA. Shares are [Computed]:

| Form (Medicaid) | 2023 Rx | 2024 Rx | 2025 Rx | 2025 share of injectable Rx | 2025 share of all TRT Rx in set | 2025 reimbursed | 2025 share of injectable reimbursement |
|---|---|---|---|---|---|---|---|
| Generic TC vials | 524,987 | 528,744 | 580,956 | 92.5% | 76.1% | $21.30M | 54.0% |
| Depo-Testosterone (brand TC) | 52,236 | 22,763 | 14,343 | 2.3% | 1.9% | $0.14M | 0.4% |
| Xyosted | 14,707 | 18,880 | 21,939 | 3.5% | 2.9% | $14.82M | 37.6% |
| Generic TE vials | 7,945 | 7,361 | 8,461 | 1.3% | 1.1% | $0.58M | 1.5% |
| Aveed | 1,381 | 1,374 | 1,296 | 0.2% | 0.2% | $1.81M | 4.6% |
| Testopel | 1,056 | 1,065 | 1,216 | 0.2% | 0.2% | $0.78M | 2.0% |
| Azmiro | — | — | 0 | 0% | 0% | $0 | 0% |
| **Injectables + pellet** | **602,312** | **580,187** | **628,211** | 100% | **82.2%** | **$39.44M** | 100% |
| Generic topical gels/solutions | 117,517 | 128,982 | 135,511 | — | 17.7% | $12.61M | — |
| **Total in set** | **719,855** | **709,242** | **763,826** | — | 100% | **$52.06M** | — |

- In Medicaid, injectables were 83.7% (2023), 81.8% (2024) and 82.2% (2025) of TRT Rx, and 67.6%, 72.9% and 75.8% of reimbursement. [Computed]
- Generic TC Medicaid Rx grew +0.7% in 2024 and **+10.7% in 2025**. [Computed]

**E. EHR-based all-payer proxy (Truveta)**
- People dispensed injectable testosterone rose from 3.3 per 1,000 adults (2018) to **6.2 per 1,000 (May 2026), +88%**. Topical rose from 1.7 to 2.2 per 1,000 (+27%). Injectable dispensing was "stable" from May 2025 to May 2026, while topical rose 4.4%. The analysis is preliminary, not peer reviewed, and may miss direct-to-consumer channels. [Reported] — [Truveta Research](https://www.truveta.com/blog/research/testosterone-rise-adults/)

**F. National IQVIA figures quoted in company filings (older)**
- 2019 (IQVIA NSP, WAC): total US TRT market about **$1.7B**; TRx +6.6% versus 2018, "entirely driven by" injectables, which grew **11.0%**. The injectable TRT market grew from **$361.7M (2018) to $408.4M (2019)**, +12.9%. [Reported] — [Antares FY2019 10-K](https://www.sec.gov/Archives/edgar/data/1016169/000156459020008465/atrs-10k_20191231.htm)
- 2020: about **7.6M** US TRT prescriptions (+6.8% versus 2019, IMS/IQVIA). Injectables are described as the dominant form by prescriptions, although gels historically led by dollars. [Reported] — [Lipocine FY2020 10-K](https://www.sec.gov/Archives/edgar/data/1535955/000110465921034761/tm211119d1_10k.htm); [Lipocine FY2019 10-K](https://www.sec.gov/Archives/edgar/data/1535955/000110465920032764/tm205342-1_10k.htm)
- 2021 (IQVIA NSP, WAC): total TRT market about **$1.4B**; TRx +5.1% to **8.0M**, with injectable TRx +5.4%. The injectable TRT market grew from **$484.4M (2020) to $545.0M (2021)**, +12.5% at WAC. [Reported] — [Antares FY2021 10-K](https://www.sec.gov/Archives/edgar/data/1016169/000101616922000028/atrs-20211231.htm)
- Xyosted's share of the **branded** TRT market among urologists and endocrinologists: about 43% and 37% (Dec 2019); about 65% and 52% (Dec 2021). [Reported] — [Antares FY2019 10-K](https://www.sec.gov/Archives/edgar/data/1016169/000156459020008465/atrs-10k_20191231.htm); [Antares FY2021 10-K](https://www.sec.gov/Archives/edgar/data/1016169/000101616922000028/atrs-20211231.htm)
- Historical context: in an older claims cohort of TRT initiators, 37.4% started on injection, 6.9% on patch and 55.8% on gel, and the gel share rose over that study period (the gel era). [Reported] — [JAMA Internal Medicine](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2293080)
- In an analysis of CMS prescriber data, endocrinologists and urologists prescribed topical testosterone more than other specialties (60.4% and 53.5% of their testosterone Rx), while family and internal medicine physicians leaned towards injections. [Reported] — [Int J Impot Res (Nature)](https://www.nature.com/articles/s41443-021-00497-6)
- A secondary blog says testosterone Rx rose from about 7.3M (2019) to "over 11 million" (2024), citing IQVIA. I could not verify the primary source. [Unverified] — [Levels blog](https://www.levels.com/blog/guide-to-testosterone-replacement-therapy)

### Inferences
- **Injectable share of total US TRT TRx, estimated at 65–75% in 2025.** Medicare (about 67%), Medicaid (about 82%) and Truveta EHR data (about 74% of injectable-plus-topical patients in May 2026, up from about 66% in 2018) all point to this range [Computed from Truveta's 6.2 / (6.2 + 2.2)]. The cash-pay telehealth channel, which public data miss, is believed to be heavily cypionate-weighted, so the true national figure is more likely at the upper end. [Estimate]
- **Split within injectables by TRx, estimated:** generic TC about 92–95%, Xyosted about 3–4%, TE vials about 1%, Aveed and pellets well under 1% each at the pharmacy level, and brand Depo-Testosterone and Azmiro under 1% combined (well under in Part D). Aveed and in-office TC are under-represented in pharmacy data because they are administered in clinic (see the Part B figures). [Estimate]
- **Split within injectables by value:** at payer gross cost, Xyosted (about $790 per Part D claim in 2025 [Computed: $37.46M / 47,254]) captures 38–45% of injectable spend despite about 3.5% of Rx. Generic TC (about $33 per Part D claim [Computed: $41.71M / 1,257,735]) takes about 50–54%. [Computed]
- The 2019 IQVIA growth figures imply an injectable TRx share of roughly 60–70% in 2018–19: total TRx grew 6.6% while injectables grew 11.0%, which fits that range if non-injectables were flat to slightly declining. This matches Part D's 65% in 2020. [Inference]
- The 2021 IQVIA statement that 5.1% TRx growth was "entirely driven by" injectables growing 5.4% cannot be reconciled arithmetically unless injectables were about 94% of TRx. Treat that phrase as loose wording, not a share datapoint. [Inference]
- Labeler share within generic TC moves by several points a year. Hikma fell from 31% to 23% between 2024 and 2025, while Xiromed rose from 4% to 12% and Eugia from 2% to 5%. That points to an open, tender- and price-driven market where a new low-cost entrant can win volume quickly. This is directly relevant to Symbiotec's entry thesis. [Inference]
- In-office TC administration (Part B J1071) fell 26% from 2020 to 2024, while pharmacy-dispensed TC (Part D) rose 45% over the same period [Computed]. The shift is towards self-injection, which favours 1 mL and 10 mL retail vials. [Inference]

### Gaps
- I found no current (2023–2026) **national IQVIA or Symphony TRx/NRx split by molecule or form**. Halozyme's FY2022–FY2024 10-Ks do not repeat the Antares-era IQVIA market tables, and the search results did not surface the FY2025 10-K. The 2021 IQVIA figures are the latest reported.
- I found no public NRx figures by form.
- No commercial-payer or cash-pay channel data was found. GoodRx data quoted in the press says TC scripts "doubled" from 2019 to 2025, but the figure is unattributed (see Q3).
- SDUD totals exclude brand-named topical and oral products (AndroGel brand, Natesto, Jatenzo, Kyzatrex, Tlando), because the pull covered product names starting with TESTO/DEPO/XYOSTED/AVEED/AZMIRO/TESTOPEL. Medicaid topical share is therefore slightly understated. SDUD also suppresses cells under 11 Rx.
- The 2025 Part D figures come from CMS's quarterly file, a different file from the 2020–2024 annual file, so methods may differ slightly. Part D spend is gross, before manufacturer rebates.

---

## 3. Recent trends: telehealth-driven growth, FDA labeling (2025–2026), the FDA expert panel, DEA telehealth rules, and market value

### Takeaway
Volume is growing fast and is concentrated in cypionate. Part D TC claims grew about 10% a year from 2020 to 2025, EHR-measured injectable use nearly doubled from 2018 to 2026, and press reports cite GoodRx data showing cypionate scripts doubling from 2019 to 2025. Value, however, is flat to down because generic prices keep falling. Regulation has turned clearly permissive. In Feb 2025 the FDA removed the cardiovascular boxed-warning language after TRAVERSE and added blood-pressure warnings. In Dec 2025 an FDA expert panel urged broader indications and removal of Schedule III status. In June 2026 HHS/FDA reportedly asked sponsors to drop the age-related hypogonadism limitation, which is single-source and unconfirmed. DEA telehealth prescribing flexibilities run to 31 Dec 2026, and a final special-registration rule went to OIRA in Aug 2026. Testosterone is still Schedule III as of Aug 2026.

### Cited Findings
**Volume growth and telehealth**
- Medicare Part D generic TC claims: 771,644 (2020), 826,420 (2022), 935,403 (2023), 1,118,253 (2024), 1,257,735 (2025). Beneficiaries rose from 195,172 to 308,533 over the same period. [Reported] — [CMS Part D annual](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?keyword=testosterone); [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)
- Truveta: injectable dispensing up 88% from 2018 to May 2026, versus +27% for topical. Testosterone prescribing among adults aged 18–34 more than doubled from 2018 to 2026. Direct-to-consumer channels may not be captured. [Reported] — [Truveta Research](https://www.truveta.com/blog/research/testosterone-rise-adults/)
- STAT News (Nov 2025) reports that testosterone cypionate scripts "doubled" from 2019 to 2025 (not clearly attributed; GoodRx data is cited elsewhere in the article). It names Ro, Hims and Hone as large telehealth prescribers entering or planning to enter the market, and DudeMeds, MaleExcel, Maximus, Titan and Alpha MD as men's-health clinics. Monthly fees run "from under $100 to several hundred dollars". A 2023 study identified 223 online men's clinics, and The Economist counted 325 new multi-site clinics with an online presence since early 2024. [Reported] — [STAT News](https://www.statnews.com/2025/11/21/online-testosterone-boom-doctors-see-risks-low-t-treatments/)
- An Epic Cosmos study found testosterone prescribing to women rose 2.6-fold, from 50.0 to 130.8 per 100,000 eligible women, between 2016 and 2025. [Reported] — [JACC: Advances](https://www.jacc.org/doi/10.1016/j.jacadv.2026.102724)
- Halozyme reported Q3 2025 proprietary product sales (mainly Xyosted plus Hylenex) of **$52.2M, +31% year on year** (from $39.9M), "primarily due to … XYOSTED, driven by continued market penetration". [Reported] — [Halozyme Q3 2025 10-Q](https://www.sec.gov/Archives/edgar/data/1159036/000115903625000045/halo-20250930.htm)

**FDA class labeling, Feb 2025 (post-TRAVERSE)**
- On 28 Feb 2025 the FDA announced class-wide labeling changes. It recommended **removing the boxed-warning language on increased risk of major adverse cardiovascular events** (MI, stroke, CV death), adding TRAVERSE results to all labels, and **keeping** the age-related hypogonadism "Limitation of Use". It also **required** product-specific increased-blood-pressure information for products with completed ambulatory BP monitoring studies, and a new BP warning for products without one. [Reported] — [FDA](https://www.fda.gov/drugs/drug-alerts-and-statements/fda-issues-class-wide-labeling-changes-testosterone-products); [Urology Times](https://urologytimes.com/view/fda-issues-label-changes-for-testosterone-products-following-traverse-post-market-studies); [Pharmacy Times](https://pharmacytimes.com/view/fda-issues-new-labeling-changes-clarifying-safety-of-testosterone-products-following-clinical-trials)

**FDA Expert Panel, 10 Dec 2025**
- The FDA convened an expert panel on TRT in men on 10 Dec 2025. Panelists favoured broadening eligibility beyond men with low testosterone tied to specific conditions (classical hypogonadism), said prostate-cancer warnings and contraindications lack evidentiary support, and **recommended removing testosterone's Schedule III status**. Commissioner Makary compared the discussion to the removal of boxed warnings on menopausal hormone therapy. The panel was advisory only. [Reported] — [FDA Expert Panel page](https://fda.gov/patients/fda-expert-panels/fda-expert-panel-testosterone-replacement-therapy-men-12102025); [RAPS](https://www.raps.org/resource/fda-panel-calls-for-easing-restrictions-on-testost.html); [Healio](https://healio.com/news/endocrinology/20251210/fda-panel-supports-expanding-population-indicated-for-testosterone-therapy); [Urology Times](https://urologytimes.com/view/experts-urge-fda-to-revisit-labeling-for-testosterone-replacement-therapy-in-men); [NPR via WWNO](https://www.wwno.org/npr-news/2025-12-12/testosterone-levels-have-declined-in-men-heres-what-the-fda-wants-to-do-about-it)

**2026 FDA follow-up (partly unconfirmed)**
- A news report says that in **June 2026 HHS/FDA asked sponsors to update TRT prescribing information**. The proposals would remove the age-related hypogonadism limitation of use, contraindicate TRT only in metastatic prostate cancer, and revise the BPH warnings. The article calls these "proposed changes" and says it was created with AI tools. [Reported, single secondary source] — [Yahoo News](https://www.yahoo.com/news/politics/articles/fda-2026-testosterone-replacement-therapy-210000576.html)
- Medical Daily (Aug 2026) says testosterone **remains Schedule III** and the indication has not been formally expanded. [Reported] — [Medical Daily](https://www.medicaldaily.com/beyond-fda-panel-what-men-actually-need-know-about-testosterone-therapy-2026-478127)
- A search summary mentioned an April 2026 Federal Register notice encouraging supplemental applications for a low-libido indication in idiopathic hypogonadism. I did not verify it against the Federal Register. [Unverified]

**DEA telehealth prescribing (testosterone is a Schedule III controlled substance)**
- DEA and HHS issued a **fourth temporary extension**, effective 1 Jan 2026, allowing Schedule II–V prescribing via audio-video telemedicine without a prior in-person visit **through 31 Dec 2026**. [Reported] — [Holland & Knight, Jan 2026](https://hklaw.com/en/insights/publications/2026/01/dea-and-hhs-extend-telemedicine-prescribing-flexibilities-through-2026); [Fierce Healthcare](https://www.fiercehealthcare.com/regulatory/dea-issues-fourth-extension-telehealth-controlled-substance-flexibilities-debate-enters); [Telehealth.org](https://telehealth.org/blog/dea-extends-telehealth-controlled-substance-prescribing-flexibilities-through-the-end-of-2026/)
- The DEA proposed three telemedicine special registrations in Jan 2025 and **submitted a final special-registration rule to OIRA on 25 Aug 2026**. It may be finalized before the flexibilities expire. [Reported] — [McDermott+](https://www.mcdermottplus.com/insights/dea-extends-telemedicine-flexibilities-for-controlled-substance-prescribing-for-2026/)

**Market value (US$)**
- IQVIA: Depo-Testosterone plus generic TC US sales were about **$191M** (12 months to Apr 2018) and **$193.8M** (12 months to Feb 2023). For Eugia's approved TC presentations, the figure was **$226.8M** (12 months to Aug 2023). Scopes differ slightly. [Reported] — [Cipla press release, 2018](https://www.cipla.com/sites/default/files/1529557824_Press-Release-Testosterone%20Cypionate%20Inj.pdf); [Xiromed, Apr 2023](https://xiromed.com/usa/2023/04/13/xiromed-llc-launches-testosterone-cypionate-injection-usp/); [Aurobindo, Oct 2023](https://www.aurobindo.com/api/uploads/corporateannouncements/Fy24_TESTOSTERONE%20CYPRIONATE%20INJ%20APPROVAL.pdf)
- IQVIA NSP at WAC: US injectable TRT market of $361.7M (2018), $408.4M (2019), $484.4M (2020) and $545.0M (2021). Total TRT was $1.7B (2019) and $1.4B (2021). [Reported] — [Antares FY2019 10-K](https://www.sec.gov/Archives/edgar/data/1016169/000156459020008465/atrs-10k_20191231.htm); [Antares FY2021 10-K](https://www.sec.gov/Archives/edgar/data/1016169/000101616922000028/atrs-20211231.htm)
- Medicare Part D gross spend on generic TC was flat even as volume rose: $40.24M (2020), $37.97M (2023), $41.39M (2024), $41.71M (2025). Average spend per dosage unit fell from $12.62 (2020) to $11.28 (2022), $9.30 (2023) and **$8.33 (2024)**. [Reported] — [CMS Part D annual](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?keyword=testosterone); [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)
- STAT cites a market report projecting the testosterone market (scope unclear) "to reach $2.5 billion". This is low-quality market-research framing. [Reported, low reliability] — [STAT News](https://www.statnews.com/2025/11/21/online-testosterone-boom-doctors-see-risks-low-t-treatments/)

### Inferences
- **Generic TC is a volume-up, price-down market.** In Part D, 2024 claims rose 19.5% and 2025 claims 12.5%, while gross spend rose 9.0% and 0.8% respectively [Computed]. That implies per-claim price erosion of about 9–10% a year. US generic TC value is probably roughly **$200–250M a year (IQVIA-type invoice-price basis, 2025)**, growing slowly or flat in dollars while volume grows about 10–15% a year. This is an estimate extrapolated from the 2023 IQVIA $194–227M figures and the Part D trends. [Estimate]
- The injectable TRT market including Xyosted and Aveed was $545M at WAC in 2021. Xyosted's growth (Part D spend +30% in 2024 and +30% in 2025 [Computed]) implies the total injectable value at WAC is likely above $600M by 2025, but WAC overstates net value for Xyosted. This is an estimate, not verified. [Estimate]
- Three changes could each lift TC vial demand further: (a) removing the CV boxed warning (done, 2025); (b) dropping the age-related hypogonadism limitation (proposed, 2026); and (c) a permanent DEA special registration for telehealth Schedule III prescribing. Descheduling would remove the DEA quota and registration burden for API makers and finished-dose manufacturers. The main downside risk is a telehealth "cliff" if the flexibilities lapse on 31 Dec 2026 without a final rule. [Inference]

### Gaps
- I could not confirm from FDA or the Federal Register whether the reported June 2026 labeling request exists or has been finalized.
- No DEA or HHS action on descheduling testosterone was found.
- I found no Xyosted-only full-year 2025 revenue (Halozyme reports it combined with Hylenex as "proprietary products"), and no 2025 Halozyme 10-K market data.
- No company-reported figures on how many TRT patients Hims, Ro, Hone or Maximus serve, or on their formulation mix, were found.
- No 2024–2026 IQVIA US$ value for the total injectable TRT market was found.

---

## 4. Price points: NADAC and WAC per vial for generic testosterone cypionate, 2020–2026

### Takeaway
On NADAC (retail pharmacy acquisition cost), generic **TC 200 mg/mL 1 mL vials cost about $11.01 per vial (Oct 2026)**, down from about $15.15 in Jan 2020 (−27%). **10 mL vials of 200 mg/mL (2,000 mg) cost about $35.20 per vial**, or $0.0176/mg (Oct 2026), down from about $48.59 in Jan 2020. Prices bottomed near $28 in late 2021, rebounded to about $40 in late 2023, and eased to $33–35 in 2025–26. **10 mL vials of 100 mg/mL cost about $43.23.** Generic TE 200 mg/mL is pricier per mL, at about $14.48/mL. The 1 mL vial costs about 3x more per mg than the 10 mL vial.

### Cited Findings
Raw NADAC per mL is [Reported]; per-vial figures are [Computed] as per-mL × vial volume. Sources: NADAC files for [2020](https://data.medicaid.gov/dataset/c933dc16-7de9-52b6-8971-4b75992673e0), [2021](https://data.medicaid.gov/dataset/d5eaf378-dcef-5779-83de-acdd8347d68e), [2022](https://data.medicaid.gov/dataset/dfa2ab14-06c2-457a-9e36-5cb6d80f8d93), [2023](https://data.medicaid.gov/dataset/4a00010a-132b-4e4d-a611-543c9521280f), [2024](https://data.medicaid.gov/dataset/99315a95-37ac-4eee-946a-3c523b4c481e), [2025](https://data.medicaid.gov/dataset/f38d0706-1239-442c-a3cc-40ef1b686ac0) and [2026](https://data.medicaid.gov/dataset/fbb83258-11c7-47f5-8b18-5f8e79f7e704).

| NADAC as-of date | TC 200 mg/mL, 1 mL ($/vial) | TC 200 mg/mL, 10 mL ($/mL → $/vial) | TC 100 mg/mL, 10 mL ($/mL → $/vial) | TE 200 mg/mL ($/mL) |
|---|---|---|---|---|
| 1 Jan 2020 | $15.15 | $4.86 → $48.59 | $3.87 → $38.71 | $13.57 |
| 30 Dec 2020 | $14.73 | $3.38 → $33.78 | $3.84 → $38.38 | $13.62 |
| 29 Dec 2021 | $15.25 | $2.82 → $28.17 | $3.66 → $36.62 | $11.81 |
| 28 Dec 2022 | $14.13 | $3.62 → $36.19 | $3.55 → $35.50 | $13.20 |
| 27 Dec 2023 | $14.30 | $3.98 → $39.75 | $4.64 → $46.35 | $13.10 |
| 25 Dec 2024 | $12.38 | $3.44 → $34.40 | $4.61 → $46.07 | $12.08 |
| 31 Dec 2025 | $11.54 | $3.34 → $33.45 | $4.75 → $47.52 | $14.25 |
| **21 Oct 2026** | **$11.01** | **$3.52 → $35.20** | **$4.32 → $43.23** | **$14.48** |

- Methodology note: before late 2023, NADAC grouped 1 mL and 10 mL 200 mg/mL TC NDCs under one description, "TESTOSTERONE CYP 200 MG/ML". I split them by price cluster: NDCs above $8/mL were treated as 1 mL (about 9–11 NDCs) and NDCs at or below $8/mL as 10 mL (3 NDCs). From late 2023 NADAC uses separate descriptions ("2,000 MG/10 ML", "1,000 MG/10 ML"). For 2020–2022 the 100 mg/mL figure is the single "TESTOSTERONE CYP 100 MG/ML" description, assumed to be the 10 mL vial. [Computed]
- All 11 NDCs priced for the 1 mL TC vial on 21 Oct 2026 share one NADAC rate, $11.00956/mL, classified "G". Labeler prefixes include 00143 (Hikma), 00409 (Hospira/Pfizer), 00574 (Padagis), 47781 (Alvogen), 52536 (Wilshire), 55150 (Eugia), 69097 (Cipla), 70700 (Xiromed) and 72603. The 10 mL 200 mg/mL vials are mostly $3.52037/mL, with one NDC (47781-0910-91) at $2.42226/mL. [Reported] — [NADAC 2026](https://data.medicaid.gov/dataset/fbb83258-11c7-47f5-8b18-5f8e79f7e704)
- Medicare Part D average gross spend per generic TC dosage unit (≈ per mL): $12.62 (2020), $11.97 (2021), $11.28 (2022), $9.30 (2023), $8.33 (2024). Spend per claim was about $33 in 2025 [Computed: $41.71M / 1,257,735]. For comparison, Xyosted cost about $301.74 per unit in 2024 and about $793 per claim in 2025 [Computed: $37.46M / 47,254]. Aveed cost $622.58 per unit in Part D (2024). [Reported/Computed] — [CMS Part D annual](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data?keyword=testosterone); [CMS Quarterly Part D](https://data.cms.gov/data-api/v1/dataset/4ff7c618-4e40-483a-b390-c8a58c94fa15/data?keyword=testosterone)
- Medicaid reimbursement per generic TC Rx was about $36.7 in 2025 [Computed: $21.30M / 580,956], versus about $676 per Xyosted Rx [Computed: $14.82M / 21,939]. — [SDUD 2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536)

### Inferences
- Pharmacy acquisition cost for a 200 mg/mL 10 mL vial (2,000 mg API) is about $35. At typical generic distribution margins, the manufacturer's net ex-factory price is probably a fraction of that, plausibly $15–25 per 10 mL vial and $4–8 per 1 mL vial, though this is not verified. API is a small share of cost; most of it sits in sterile fill-finish, vials and oil. That favours a vertically integrated API-plus-finished-dose model, which is relevant to Symbiotec. [Estimate]
- The 1 mL vial earns about 3x the per-mg price of the 10 mL vial ($0.055/mg versus $0.0176/mg, Oct 2026 NADAC) [Computed]. Per-claim gross cost in Part D also kept falling in 2024–25 even as volumes rose, which signals continued competitive pressure from new entrants such as Xiromed, Eugia, Northstar and BPI Labs. [Inference]
- NADAC prices for the 10 mL vial rose in 2022–2023, from about $28 to about $40. That fits the TC shortage and supply-tightness period in 2022–23 (covered in a separate notes file) and was followed by renewed deflation once new ANDAs launched. [Inference]

### Gaps
- No public **WAC** list prices per vial were retrieved; WAC sits behind paywalled compendia such as Medi-Span, First Databank and Red Book. NADAC is used as the acquisition-cost proxy.
- No manufacturer net or ex-factory price data was found.
- The NADAC description for TE 200 mg/mL does not state vial size (generic TE is typically a 5 mL multi-dose vial; not verified), so only the per-mL figure is given.
- No Azmiro, Xyosted or Aveed WAC per unit was found in sources I could verify. Part D per-unit gross spend is shown as a proxy.
