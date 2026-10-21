# Medicaid / Medicare utilization-based share and price proxies: Solu-Medrol (MPSS), Solu-Cortef (HSS), Depo-Medrol (MPA) and their generics, 2018–2026 Q1

*Data pulled 2026-10-21. Latest data: SDUD through 2026 Q1 (2026 dataset last modified 2026-07-10; 2020–2025 datasets re-published 2026-07-13). Medicare Part B, Part D and Medicaid Spending by Drug: DY2024 releases (modified 2026-06-25). All $ figures are nominal US$ and pre-rebate.*

**Output files** (in `/home/user/sample/research_notes/Symbiotec DCV steroid injectables/data/`):
- `sdud_labeler_share.csv`: molecule × strength × year × labeler. Units, Rx, $, share by units/Rx/$, $/unit, $/Rx, units/Rx. Built from national (state = "XX") rows.
- `sdud_clean_price_per_vial.csv`: state-level cleaned $/vial (Rx-weighted median, p25, p75), plus the share of Rx in "clean" cells.
- `sdud_brand_generic_summary.csv`: brand vs generic Rx share, number of generic labelers with ≥1% share, median $/vial and the generic-vs-brand gap.
- `sdud_ndc_year.csv`: NDC-level annual totals.
- `sdud_ndc_map.csv`: 147 NDCs, with molecule, strength, vial mL, labeler, NDA/ANDA, RxNorm concept and packaging.
- `partd_spending.csv`, `partb_spending.csv`, `medicaid_spending_by_drug.csv`: the CMS series in long format.
- Scripts are in `/tmp/claude-0/-home-user-sample/28da1d41-580b-501a-b778-8022ed0c448f/scratchpad/sdud_scripts/`.
- The ASP researcher's file `partb_spending_by_hcpcs_2016_2024.csv` in the same folder covers the retired Part B codes (J2920/J2930/J1020/J1030/J1040) from older CMS releases. Those files were not overwritten.

**Method in brief:**
1. **Building the NDC list.** I took every historical NDC for each injectable RxNorm concept of methylprednisolone, methylprednisolone acetate and hydrocortisone (succinate) from NLM RxNav (`allhistoricalndcs`, 816 NDCs). Each NDC was then classified with RxNav `ndcstatus`/`ndcproperties`, which give the RxNorm concept, labeler, NDA/ANDA and packaging. openFDA NDC was used to check current listings.
2. **Querying SDUD.** I queried the SDUD DKAN API by NDC list, not by product name, for national (XX) rows of each year 2018–2026. I did this because name matching alone missed Solu-Medrol 40 mg NDCs 0009-0039-28 and -30. SDUD truncates their name to "SOLU MEDRO" (no hyphen). Those two NDCs account for about 464k Rx and $34.5M over 2018–2026 Q1.
3. **Grouping.** Labelers were grouped by the first 5 digits of the NDC. No repackager NDCs had SDUD volume. Hospira's A-Methapred / A-Hydrocort (labeler 0409/0074) are Pfizer-owned ANDAs and are shown separately from the "Pfizer brand" (labeler 0009, Pharmacia & Upjohn).

## Q1. Medicaid SDUD: units, prescriptions and dollars by labeler, by molecule and strength, 2018–2026 Q1

### Takeaway
Generics have taken Solu-Medrol (MPSS) share in Medicaid, but Pfizer still dominates.
- **MPSS:** Pfizer held 75% of Medicaid MPSS prescriptions in 2025 (73.8% in 2026 Q1), down from 90.6% in 2018. The gain went to Dr. Reddy's (12.3% in 2025, 16.9% in Q1 2026), Fresenius Kabi (8.7%) and Hikma (3.9%).
- **HSS:** Solu-Cortef is still close to a monopoly. Pfizer had 94.6% of 2025 Rx and 93.2% in Q1 2026, and Cipla is the only generic with Medicaid volume (launched 2024).
- **MPA:** Depo-Medrol is the most genericized. Pfizer had 58.9% of 2025 Rx, Amneal 32.8% and Sagent 4.9%. Teva, the main generic in 2019–2022, has dropped to roughly zero.

### Cited Findings
- **What SDUD covers.** SDUD reports "covered outpatient drugs that are paid for by state Medicaid agencies", by state, NDC, number of prescriptions and dollars reimbursed — [data.medicaid.gov SDUD 2024 dataset](https://data.medicaid.gov/dataset/61729e5a-7aa8-448c-8903-ba3e0cd0ea3c).
- **Unit definitions.** For FFS, units reimbursed are "the number of units (based on Unit Type) of the drug 11-digit NDC reimbursed by the state". For MCO, they are units "dispensed". Counts below 11 are suppressed, with secondary suppression applied — [CMS SDUD field descriptions](https://www.cms.gov/files/document/medicaid-state-drug-utilization-data-field-descriptions.pdf); [SDUD FAQ](https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq).
- **National totals ("XX").** The "National Totals" view sums all 50 states and DC at NDC-11 level, with state code "XX" — [SDUD FAQ](https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq).
- **XX includes state-suppressed cells (my check).** For Solu-Cortef 100 mg NDC 0009-0011-03 in 2024 Q1 MCO, XX shows 3,092 Rx. The sum of unsuppressed state rows is 3,068 Rx, and 5 state rows were suppressed. That makes XX the most complete basis. The calculation is from the 2024 dataset — [SDUD 2024](https://data.medicaid.gov/dataset/61729e5a-7aa8-448c-8903-ba3e0cd0ea3c).
- **Labelers with SDUD volume, from the NDC map** — [RxNav](https://rxnav.nlm.nih.gov/REST/ndcstatus.json?ndc=00009003928); [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22methylprednisolone+sodium+succinate%22&limit=1000):
  - MPSS: Pfizer/Pharmacia & Upjohn (NDA011856), Fresenius Kabi (ANDA040583), Dr. Reddy's (ANDA212396), Hikma (ANDA203125 for 40/125 mg; 0143-9850/9851 for 500 mg/1 g), Sagent (ANDA040888), Amneal (ANDA207549), Civica (Hikma-made ANDA203125, first volume in 2026 Q1), Hospira A-Methapred (tiny).
  - HSS: Pfizer (NDA009866), Cipla (ANDA214050), Hospira A-Hydrocort (ANDA040666, negligible and gone after 2021).
  - MPA: Pfizer (NDA011757), Amneal (ANDA210043/216502), Teva (ANDA040557/040620) plus Northstar (Teva ANDAs), Sagent (ANDA201835), Sandoz (ANDA040794/040719/214870), Endo/Par (ANDA214297), Eugia (ANDA211930).
- **Generic NDCs listed but with no Medicaid volume yet** — [openFDA HSS](https://api.fda.gov/drug/ndc.json?search=generic_name:%22hydrocortisone+sodium+succinate%22&limit=1000); [RxNav history](https://rxnav.nlm.nih.gov/REST/rxcui/238755/allhistoricalndcs.json):
  - HSS 100 mg from Zydus (ANDA217191; NDCs 70710-1907, 70771-1966) and Apotex (ANDA219856; 60505-6411). In RxNorm these NDCs start 2026-06 and 2026-07, after the latest SDUD quarter.
  - Eugia MPSS (ANDA207667) also had no SDUD volume.
  - Caplin MPA (ANDA220556) is newly listed (NDC start 2026-03).
- **Symbiotec's own NDCs are bulk API only.** openFDA lists Symbiotec Pharmalab Limited (labeler 22552) with bulk-ingredient NDCs for hydrocortisone sodium succinate (22552-0007) and methylprednisolone acetate (22552-0023) — [openFDA HSS](https://api.fda.gov/drug/ndc.json?search=generic_name:%22hydrocortisone+sodium+succinate%22&limit=1000); [openFDA MPA](https://api.fda.gov/drug/ndc.json?search=generic_name:%22methylprednisolone+acetate%22&limit=1000).
- The tables below are computed from SDUD national rows, 2018–2026 Q1 — [SDUD 2018](https://data.medicaid.gov/dataset/a1f3598e-fc71-51aa-8560-78e7e1a61b09), [2019](https://data.medicaid.gov/dataset/daba7980-e219-5996-9bec-90358fd156f1), [2020](https://data.medicaid.gov/dataset/cc318bfb-a9b2-55f3-a924-d47376b32ea3), [2021](https://data.medicaid.gov/dataset/eec7fbe6-c4c4-5915-b3d0-be5828ef4e9d), [2022](https://data.medicaid.gov/dataset/200c2cba-e58d-4a95-aa60-14b99736808d), [2023](https://data.medicaid.gov/dataset/d890d3a9-6b00-43fd-8b31-fcba4c8e2909), [2024](https://data.medicaid.gov/dataset/61729e5a-7aa8-448c-8903-ba3e0cd0ea3c), [2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536), [2026](https://data.medicaid.gov/dataset/2957a7f9-9a15-453e-9afd-3bbdcbac8fd3). Unit and $ shares by labeler are in `sdud_labeler_share.csv`.

#### MPSS (Solu-Medrol and generics)
**MPSS All strengths - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 90.6 | 90.1 | 89.4 | 86.8 | 87.3 | 81.7 | 78.9 | 75.0 | 73.8 |
| Amneal | 0.3 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 | 0.1 | 0.0 | 0.0 |
| Civica (Hikma ANDA) | - | - | - | - | - | - | - | - | 0.1 |
| Dr. Reddy's | - | - | - | - | 0.4 | 4.3 | 7.6 | 12.3 | 16.9 |
| Fresenius Kabi | 8.8 | 9.3 | 9.9 | 12.6 | 11.8 | 12.5 | 11.2 | 8.7 | 6.1 |
| Hikma (West-Ward) | - | - | 0.2 | 0.2 | 0.2 | 0.9 | 2.1 | 3.9 | 3.2 |
| Sagent | 0.3 | 0.3 | 0.3 | 0.2 | 0.2 | 0.1 | 0.1 | 0.0 | - |
| Total Rx (all labelers) | 405,536 | 400,672 | 316,151 | 332,579 | 375,088 | 388,561 | 325,433 | 370,268 | 70,931 |
| Total $ reimbursed ($k) | 24,866 | 33,643 | 31,477 | 31,172 | 35,782 | 42,556 | 22,108 | 18,258 | 3,263 |

**MPSS All strengths - share of Medicaid $ reimbursed (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 87.3 | 92.9 | 92.4 | 90.5 | 93.4 | 80.8 | 76.1 | 76.6 | 70.8 |
| Amneal | 0.1 | 0.0 | 0.0 | 0.0 | 0.1 | 0.4 | 0.2 | 0.0 | 0.0 |
| Dr. Reddy's | - | - | - | - | 0.1 | 3.0 | 5.6 | 15.1 | 19.3 |
| Fresenius Kabi | 11.9 | 6.1 | 7.1 | 9.2 | 6.2 | 14.6 | 17.4 | 6.7 | 8.8 |
| Hikma (West-Ward) | - | - | 0.2 | 0.2 | 0.2 | 1.3 | 0.8 | 1.6 | 1.1 |
| Pfizer/Hospira ANDA | 0.0 | 0.8 | 0.0 | - | - | - | - | - | - |
| Sagent | 0.7 | 0.2 | 0.3 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 | - |
| Total Rx (all labelers) | 405,536 | 400,672 | 316,151 | 332,579 | 375,088 | 388,561 | 325,433 | 370,268 | 70,931 |
| Total $ reimbursed ($k) | 24,866 | 33,643 | 31,477 | 31,172 | 35,782 | 42,556 | 22,108 | 18,258 | 3,263 |

**MPSS 40 mg - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 91.3 | 91.2 | 90.8 | 88.9 | 89.1 | 83.5 | 80.3 | 77.0 | 74.7 |
| Amneal | 0.4 | 0.3 | 0.2 | 0.2 | 0.3 | 1.0 | 0.2 | - | 0.1 |
| Dr. Reddy's | - | - | - | - | 0.3 | 4.5 | 7.4 | 11.5 | 15.6 |
| Fresenius Kabi | 7.8 | 8.0 | 8.7 | 10.7 | 10.2 | 10.6 | 9.6 | 7.8 | 6.2 |
| Hikma (West-Ward) | - | - | - | - | - | 0.5 | 2.5 | 3.7 | 3.4 |
| Sagent | 0.4 | 0.4 | 0.3 | 0.2 | 0.1 | 0.0 | 0.0 | - | - |
| Total Rx (all labelers) | 80,753 | 83,451 | 63,425 | 69,495 | 83,867 | 88,649 | 74,482 | 83,999 | 16,573 |
| Total $ reimbursed ($k) | 5,654 | 6,943 | 6,153 | 6,170 | 6,757 | 9,369 | 4,685 | 2,915 | 432 |

**MPSS 125 mg - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 91.2 | 90.7 | 90.3 | 87.4 | 87.9 | 81.9 | 79.3 | 75.3 | 74.5 |
| Amneal | 0.2 | 0.3 | 0.3 | 0.2 | 0.2 | 0.4 | 0.1 | 0.0 | - |
| Civica (Hikma ANDA) | - | - | - | - | - | - | - | - | 0.1 |
| Dr. Reddy's | - | - | - | - | 0.4 | 4.2 | 7.7 | 12.6 | 17.1 |
| Fresenius Kabi | 8.3 | 8.7 | 9.1 | 12.2 | 11.3 | 12.6 | 10.9 | 8.3 | 5.5 |
| Hikma (West-Ward) | - | - | - | - | - | 0.8 | 1.9 | 3.8 | 2.9 |
| Sagent | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.1 | 0.1 | 0.0 | - |
| Total Rx (all labelers) | 299,674 | 292,176 | 231,200 | 240,352 | 268,889 | 277,274 | 233,533 | 267,325 | 51,117 |
| Total $ reimbursed ($k) | 14,994 | 23,686 | 22,953 | 22,561 | 25,677 | 28,260 | 15,407 | 13,185 | 2,419 |

**MPSS 500 mg - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 100.0 | 100.0 | 99.4 | 94.7 | 90.5 | 89.8 | 82.0 | 75.2 | 66.2 |
| Dr. Reddy's | - | - | - | - | 0.9 | 5.2 | 11.3 | 12.1 | 19.3 |
| Hikma (West-Ward) | - | - | 0.6 | 5.3 | 8.6 | 5.0 | 6.6 | 12.7 | 14.5 |
| Total Rx (all labelers) | 5,977 | 5,949 | 4,473 | 4,626 | 4,439 | 4,649 | 3,614 | 5,023 | 885 |
| Total $ reimbursed ($k) | 629 | 381 | 188 | 252 | 231 | 534 | 282 | 327 | 77 |

**MPSS 1000 mg - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 74.3 | 71.1 | 69.1 | 68.3 | 66.9 | 68.6 | 63.1 | 57.2 | 54.1 |
| Dr. Reddy's | - | - | - | - | 0.8 | 4.7 | 5.9 | 12.3 | 21.2 |
| Fresenius Kabi | 24.2 | 27.8 | 26.7 | 28.2 | 29.9 | 24.5 | 28.5 | 25.7 | 20.7 |
| Hikma (West-Ward) | - | - | 3.4 | 3.2 | 2.4 | 2.3 | 2.5 | 4.8 | 4.0 |
| Sagent | 1.4 | 1.2 | 0.7 | 0.4 | - | - | - | - | - |
| Total Rx (all labelers) | 18,490 | 18,724 | 16,904 | 17,956 | 17,547 | 17,694 | 13,633 | 13,637 | 2,298 |
| Total $ reimbursed ($k) | 3,579 | 2,623 | 2,181 | 2,186 | 3,113 | 4,389 | 1,732 | 1,709 | 334 |


- MPSS 2 g (0009-0796/0850) is 100% Pfizer in Medicaid, at 150–650 Rx a year. Eugia's 2 g NDC (55150-0265-50) has no SDUD volume — [SDUD 2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536).

#### HSS (Solu-Cortef and generics)
**HSS All strengths - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 99.8 | 99.9 | 99.8 | 100.0 | 100.0 | 100.0 | 99.6 | 94.6 | 93.2 |
| Cipla | - | - | - | - | - | - | 0.4 | 5.4 | 6.8 |
| Pfizer/Hospira ANDA | 0.2 | 0.1 | 0.2 | 0.0 | - | - | - | - | - |
| Total Rx (all labelers) | 34,766 | 38,185 | 37,111 | 40,491 | 42,706 | 35,759 | 37,242 | 37,303 | 7,860 |
| Total $ reimbursed ($k) | 7,573 | 5,072 | 3,739 | 4,628 | 4,572 | 4,224 | 3,035 | 2,575 | 513 |

**HSS All strengths - share of Medicaid $ reimbursed (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 99.7 | 100.0 | 99.9 | 100.0 | 100.0 | 100.0 | 99.9 | 97.2 | 96.5 |
| Cipla | - | - | - | - | - | - | 0.1 | 2.8 | 3.5 |
| Pfizer/Hospira ANDA | 0.3 | 0.0 | 0.1 | 0.0 | - | - | - | - | - |
| Total Rx (all labelers) | 34,766 | 38,185 | 37,111 | 40,491 | 42,706 | 35,759 | 37,242 | 37,303 | 7,860 |
| Total $ reimbursed ($k) | 7,573 | 5,072 | 3,739 | 4,628 | 4,572 | 4,224 | 3,035 | 2,575 | 513 |

**HSS 100 mg - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 99.8 | 99.9 | 99.8 | 100.0 | 100.0 | 100.0 | 99.6 | 94.4 | 93.0 |
| Cipla | - | - | - | - | - | - | 0.4 | 5.6 | 7.0 |
| Pfizer/Hospira ANDA | 0.2 | 0.1 | 0.2 | 0.0 | - | - | - | - | - |
| Total Rx (all labelers) | 33,276 | 36,711 | 35,649 | 38,397 | 40,003 | 34,161 | 36,198 | 36,146 | 7,623 |
| Total $ reimbursed ($k) | 7,083 | 4,634 | 3,674 | 4,534 | 4,393 | 3,934 | 2,925 | 2,419 | 471 |


- Solu-Cortef 250 mg, 500 mg and 1 g are 100% Pfizer in every year. Volumes are small: 250 mg had 716–1,199 Rx a year, 500 mg fewer than 1,400 and 1 g fewer than 260 — [SDUD 2018–2026](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536).

#### MPA (Depo-Medrol and generics), secondary
**MPA All strengths - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 88.7 | 80.2 | 76.0 | 70.0 | 59.0 | 63.6 | 61.8 | 58.9 | 57.3 |
| Amneal | - | - | 0.1 | 1.4 | 17.4 | 22.9 | 28.8 | 32.8 | 34.5 |
| Endo/Par Sterile | - | - | - | - | 0.0 | 0.3 | 1.5 | 1.3 | 1.1 |
| Eugia (Aurobindo) | - | - | - | - | - | 0.0 | 0.8 | 0.9 | 0.4 |
| Northstar (Teva ANDA) | - | - | - | 0.4 | 3.7 | 0.4 | 0.0 | 0.0 | - |
| Sagent | - | - | - | - | 1.3 | 3.2 | 5.9 | 4.9 | 5.6 |
| Sandoz | 0.3 | 0.2 | 0.1 | 0.1 | 0.0 | 0.0 | 0.4 | 1.1 | 1.0 |
| Teva | 11.0 | 19.6 | 23.8 | 28.1 | 18.5 | 9.5 | 0.8 | 0.0 | 0.0 |
| Total Rx (all labelers) | 912,714 | 909,074 | 811,096 | 835,171 | 580,271 | 625,715 | 486,471 | 542,247 | 109,930 |
| Total $ reimbursed ($k) | 24,914 | 18,377 | 12,964 | 12,779 | 11,155 | 12,580 | 8,178 | 10,661 | 2,244 |

**MPA 40 mg/mL x 1 mL - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 88.3 | 81.5 | 78.7 | 71.7 | 51.5 | 57.9 | 60.1 | 59.4 | 59.4 |
| Amneal | - | - | 0.2 | 3.6 | 32.2 | 34.0 | 39.4 | 40.5 | 40.5 |
| Northstar (Teva ANDA) | - | - | - | 0.4 | 2.4 | 0.4 | - | 0.0 | - |
| Sandoz | 0.8 | 0.5 | 0.3 | 0.3 | 0.1 | - | - | - | - |
| Teva | 10.9 | 18.0 | 20.8 | 24.1 | 13.9 | 7.6 | 0.5 | 0.1 | 0.0 |
| Total Rx (all labelers) | 186,383 | 193,387 | 167,775 | 189,584 | 163,934 | 184,314 | 153,576 | 182,717 | 37,932 |
| Total $ reimbursed ($k) | 6,247 | 4,464 | 3,345 | 3,344 | 3,466 | 4,135 | 2,524 | 3,333 | 812 |

**MPA 80 mg/mL x 1 mL - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 88.3 | 78.0 | 71.8 | 66.2 | 46.9 | 42.8 | 38.5 | 38.9 | 38.0 |
| Amneal | - | - | 0.1 | 2.8 | 33.8 | 48.3 | 60.9 | 61.0 | 61.9 |
| Northstar (Teva ANDA) | - | - | - | 0.2 | 2.6 | 0.1 | - | - | - |
| Sandoz | 0.2 | 0.1 | 0.1 | 0.0 | - | - | - | - | - |
| Teva | 11.5 | 21.9 | 28.0 | 30.8 | 16.6 | 8.8 | 0.6 | 0.0 | 0.1 |
| Total Rx (all labelers) | 176,810 | 164,972 | 158,695 | 169,832 | 143,126 | 166,695 | 127,565 | 143,079 | 27,914 |
| Total $ reimbursed ($k) | 5,615 | 3,976 | 2,923 | 3,180 | 3,236 | 3,885 | 2,397 | 2,586 | 501 |

**MPA 40 mg/mL x 10 mL - share of Medicaid prescriptions (%)**

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| Pfizer brand | 89.7 | 78.3 | 72.0 | 66.6 | 65.7 | 77.8 | 70.4 | 60.6 | 57.9 |
| Amneal | - | - | - | - | - | - | 1.4 | 12.1 | 17.4 |
| Endo/Par Sterile | - | - | - | - | - | 0.3 | 4.7 | 5.0 | 4.5 |
| Eugia (Aurobindo) | - | - | - | - | - | 0.1 | 2.9 | 3.7 | 2.2 |
| Northstar (Teva ANDA) | - | - | - | 0.6 | 5.9 | 0.8 | 0.0 | - | - |
| Sagent | - | - | - | - | 3.2 | 8.7 | 19.5 | 16.0 | 16.4 |
| Sandoz | 0.3 | 0.3 | 0.2 | 0.2 | 0.0 | - | 0.4 | 2.6 | 1.5 |
| Teva | 9.9 | 21.4 | 27.8 | 32.6 | 25.1 | 12.3 | 0.5 | - | - |
| Total Rx (all labelers) | 262,165 | 269,870 | 230,960 | 238,885 | 132,480 | 130,971 | 94,680 | 106,557 | 22,867 |
| Total $ reimbursed ($k) | 6,149 | 4,428 | 2,986 | 2,840 | 1,970 | 2,260 | 1,627 | 2,515 | 426 |


- Depo-Medrol 20 mg/mL × 5 mL (0009-0274-01) is 100% Pfizer, at 13–22k Rx a year — [SDUD](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536).

- **Cross-check against CMS Medicaid Spending by Drug (built from SDUD).** Claims agree closely. For MPSS in 2024, CMS shows 249,829 brand and 66,758 generic claims, against 256,676 and 68,757 in my SDUD-XX build, so the brand claim share is 78.9% in both. Dollars agree for 2020–2023: the 2020 Solu-Medrol total is $29.08M in CMS and $29.10M in SDUD-XX. Dollars diverge for 2024: CMS has Solu-Medrol at $22.5M and Dr. Reddy's at $3.98M, against $16.8M and $1.23M in the SDUD 2024 file re-published 2026-07-13 — [CMS Medicaid Spending by Drug DY2024](https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicaid-spending-by-drug); [API](https://data.cms.gov/data-api/v1/dataset/be64fce3-e835-4589-b46b-024198e524a6/data).

### Inferences
- **The hypothesis holds in this data: Medrol is crowded, Cortef is not.**
  - MPSS has three generic labelers with ≥1% Medicaid Rx share in 2023–2026 (DRL, Fresenius, Hikma), plus Civica just entering. Cumulative generic share went from about 9% (2018) to 25% (2025) and 26% (Q1 2026).
  - HSS had one generic (Cipla) at 5–7% share after roughly 1.5 years on market. Two more ANDA holders (Zydus, Apotex) only listed NDCs in mid-2026. The near-monopoly is therefore ending but had barely eroded by Q1 2026.
- **Dr. Reddy's is taking share and Fresenius Kabi is ceding it.** DRL (ANDA212396, approved around 2022) is the clear MPSS share-taker: 0.4% → 4.3% → 7.6% → 12.3% → 16.9% over 2022 → Q1 2026. Fresenius Kabi, the long-standing incumbent generic (about 9–13% share), is losing ground (6.1% in Q1 2026). This fits a price-led entrant displacing the incumbent generic more than the brand.
- **Solu-Medrol's brand share is much stickier in Medicaid than in Part D.** In Part D the brand had 46.6% of MPSS claims in 2024 (see Q4). A likely reason is that Medicaid volume is dominated by physician-administered and outpatient claims, where provider stocking (Act-O-Vial, GPO contracts) matters more than pharmacy substitution. This is an inference.
- **Strength mix.** In Medicaid MPSS, 125 mg (about 72% of Rx) and 40 mg (about 23%) dominate. The 1 g strength has the highest generic share: Fresenius about 21–30%, and Pfizer only 54–57% in 2025–Q1 2026. This is relevant if a DCV (Act-O-Vial-like) generic targets the 40/125 mg presentations, where brand share is still about 75%.

### Gaps
- **SDUD Rx are claims, not vials.** Shares by Rx are claim shares, and units are not consistently vials (see Q2 and Q5).
- **No hospital inpatient use.** SDUD excludes hospital inpatient drug use, which is bundled into DRG payments. It therefore misses the hospital-dominated bulk of the MPSS/HSS market (see Q5).
- **No source for the 2024 dollar difference.** I could not find documentation explaining why CMS Medicaid Spending by Drug and the re-published SDUD 2024 differ on dollars. It is likely post-release state resubmissions, but this is unconfirmed.

## Q2. Labeler share (units vs $), reimbursed $/unit by labeler, and the brand–generic price gap

### Takeaway
1. **Use Rx share as the share proxy.** In SDUD, unit and dollar shares are distorted. Units are inconsistent across states, especially after the 2024 HCPCS change to a 5-mg code for MPSS. Dollars are dominated by a few states that pay facility-level amounts per unit (CA, NY, NC, IA, VA).
2. **Cleaned reimbursement per vial** (Rx-weighted median of state cells whose units are vial-based):
   - MPSS 40 mg brand: ~$5.5 (2018–2024), falling to $3.75 in 2025 and $3.53 in Q1 2026.
   - MPSS 125 mg brand: $9.3 → $6.3 (2018 → 2025).
   - Solu-Cortef 100 mg: rose from $13.8 to $23.1 (2018 → 2025, +67%). Cipla's 100 mg was about 28% lower ($16.5) in 2025.
3. **Medicaid shows no brand premium for MPSS 40/125 mg or MPA.** Brand and generic medians are within ±10% (MPA) or generic is higher (MPSS). This is consistent with reimbursement by HCPCS fee schedule, not NDC.

### Cited Findings
- **Units/Rx run far above 1 in some states after the code change** (state-level SDUD 2025):
  - Pfizer MPSS 40 mg (1 mL): 11.3 units/Rx in MA MCO, 3.7 in TN MCO.
  - Dr. Reddy's 40 mg: 13.0 in NJ MCO.
  - Hikma's national MPSS units/Rx rose to 4.8 in 2025, making its unit share (11.9%) about 3x its Rx share (3.9%).
  - Source: [SDUD 2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536).
- **HCPCS change.** J2919 (methylprednisolone sodium succinate, per 5 mg) replaced J2920 (up to 40 mg) and J2930 (up to 125 mg) from April 2024. The secondary sources say a 1,000 mg infusion now bills 200 units instead of 8 — [Pabau HCPCS J2930 note](https://pabau.com/procedure-codes/hcpcs-code-j2930/); [NCI SEER CanMED HCPCS list](https://seer.cancer.gov/oncologytoolbox/canmed/hcpcs/?page=18). These sources are secondary, and hcpcs.codes lists a conflicting 2025 date — [hcpcs.codes J2919](https://hcpcs.codes/j-codes/J2919/).
- **Dollar skew by state** (state-level SDUD 2025, Pfizer brand):
  - MPSS 125 mg paid $395.79/unit in NY MCO (5,433 Rx), $151.42 in NC MCO and $126.00 in CA MCO, against $1.60 in OH MCO and $5.41 in MI MCO.
  - MPSS 40 mg paid $117.60/unit in CA MCO, against $1.57 in FL MCO.
  - Source: [SDUD 2025](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536).
- **National $/Rx moves with that skew.** Pfizer MPSS $/Rx (national XX, all strengths) was $59.08 (2018), peaked at $108.21 (2023), then fell to $50.37 (2025) and $44.16 (Q1 2026) — [SDUD](https://data.medicaid.gov/dataset/d890d3a9-6b00-43fd-8b31-fcba4c8e2909).
- **Rebates are not netted out.** SDUD Total Amount Reimbursed "is not reduced or affected by Medicaid rebates paid to the state" — [CMS SDUD field descriptions](https://www.cms.gov/files/document/medicaid-state-drug-utilization-data-field-descriptions.pdf).
- **Cleaned $/vial method.** State × NDC × year × utilization-type cells were kept when their units/Rx was consistent with vial units:
  - 1-mL presentations: 0.8–4.0 units/Rx. Here EA = mL = the old HCPCS unit.
  - Multi-mL vials: 0.8–1.5 units/Rx.
  - The headline is the Rx-weighted median; p25/p75 are in `sdud_clean_price_per_vial.csv`. Clean-cell coverage was about 87–99% of Rx for MPSS 40 mg and MPA 1 mL vials, about 63–96% for MPSS 125 mg, and about 25–50% for HSS 100 mg (many states report HSS in mL).
  - Source: computed from SDUD state rows — [SDUD 2018–2026](https://data.medicaid.gov/dataset/2957a7f9-9a15-453e-9afd-3bbdcbac8fd3).

**MPSS 40 mg - clean $ per vial** (Rx-weighted median state-cell $/vial; cells with units/Rx consistent with 1 vial per unit; min 50 Rx in clean cells)

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| ALL BRAND | 5.58 | 5.45 | 5.57 | 5.65 | 5.89 | 5.58 | 5.49 | 3.75 | 3.53 |
| ALL GENERIC | 6.52 | 7.39 | 5.74 | 6.98 | 7.93 | 9.60 | 8.96 | 5.91 | 3.76 |
| Pfizer brand | 5.58 | 5.45 | 5.57 | 5.65 | 5.89 | 5.58 | 5.49 | 3.75 | 3.53 |
| Amneal | 4.46 | 4.77 | 4.21 | - | 4.81 | 4.22 | - | - | - |
| Dr. Reddy's | - | - | - | - | 7.96 | 6.28 | 5.84 | 8.07 | 3.76 |
| Fresenius Kabi | 6.81 | 7.39 | 5.74 | 6.98 | 9.25 | 9.60 | 12.47 | 4.92 | 10.73 |
| Hikma (West-Ward) | - | - | - | - | - | 2.95 | 2.50 | 4.19 | 1.08 |
| Sagent | 5.33 | 8.80 | - | - | - | - | - | - | - |

**MPSS 125 mg - clean $ per vial** (Rx-weighted median state-cell $/vial; cells with units/Rx consistent with 1 vial per unit; min 50 Rx in clean cells)

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| ALL BRAND | 9.29 | 7.65 | 8.10 | 7.97 | 8.03 | 7.55 | 9.31 | 6.28 | 7.01 |
| ALL GENERIC | 10.60 | 7.73 | 11.20 | 10.34 | 11.43 | 14.30 | 10.18 | 7.30 | 5.81 |
| Pfizer brand | 9.29 | 7.65 | 8.10 | 7.97 | 8.03 | 7.55 | 9.31 | 6.28 | 7.01 |
| Amneal | 8.54 | 4.92 | 6.08 | 5.72 | 5.80 | 5.39 | 5.00 | - | - |
| Dr. Reddy's | - | - | - | - | 4.56 | 11.39 | 8.86 | 6.51 | 5.38 |
| Fresenius Kabi | 11.13 | 7.73 | 11.20 | 10.34 | 12.14 | 15.18 | 10.18 | 8.46 | 13.07 |
| Hikma (West-Ward) | - | - | - | - | - | 6.53 | 6.90 | 6.81 | 5.31 |
| Pfizer/Hospira ANDA | - | 534.68 | - | - | - | - | - | - | - |
| Sagent | 10.29 | 13.07 | 5.32 | 8.97 | 5.86 | 5.29 | 8.73 | - | - |

**MPSS 1000 mg - clean $ per vial** (Rx-weighted median state-cell $/vial; cells with units/Rx consistent with 1 vial per unit; min 50 Rx in clean cells)

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| ALL BRAND | 64.56 | 52.12 | 48.70 | 39.87 | 46.36 | 44.57 | 52.15 | 54.01 | 51.42 |
| ALL GENERIC | 45.56 | 37.38 | 44.03 | 51.13 | 43.01 | 36.90 | 28.67 | 40.97 | 42.52 |
| Pfizer brand | 64.56 | 52.12 | 48.70 | 39.87 | 46.36 | 44.57 | 52.15 | 54.01 | 51.42 |
| Dr. Reddy's | - | - | - | - | - | 40.54 | 33.04 | 40.97 | 42.52 |
| Fresenius Kabi | 45.56 | 37.38 | 40.68 | 40.91 | 43.01 | 36.90 | 22.98 | 40.28 | - |
| Hikma (West-Ward) | - | - | 65.66 | 51.13 | 46.14 | - | - | - | - |

**HSS 100 mg - clean $ per vial** (Rx-weighted median state-cell $/vial; cells with units/Rx consistent with 1 vial per unit; min 50 Rx in clean cells)

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| ALL BRAND | 13.77 | 15.39 | 14.63 | 15.11 | 17.90 | 20.53 | 23.13 | 23.05 | 21.05 |
| ALL GENERIC | - | - | 43.94 | - | - | - | - | 16.52 | - |
| Pfizer brand | 13.77 | 15.39 | 14.63 | 15.11 | 17.90 | 20.53 | 23.13 | 23.05 | 21.05 |
| Cipla | - | - | - | - | - | - | - | 16.52 | - |
| Pfizer/Hospira ANDA | - | - | 43.94 | - | - | - | - | - | - |

**MPA 40 mg/mL x 1 mL - clean $ per vial** (Rx-weighted median state-cell $/vial; cells with units/Rx consistent with 1 vial per unit; min 50 Rx in clean cells)

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| ALL BRAND | 6.51 | 6.25 | 6.28 | 5.78 | 6.21 | 7.54 | 6.07 | 4.95 | 4.85 |
| ALL GENERIC | 6.52 | 6.34 | 6.11 | 5.68 | 6.40 | 7.42 | 6.04 | 4.96 | 5.11 |
| Pfizer brand | 6.51 | 6.25 | 6.28 | 5.78 | 6.21 | 7.54 | 6.07 | 4.95 | 4.85 |
| Amneal | - | - | 5.58 | 5.91 | 6.26 | 7.37 | 6.04 | 4.96 | 5.11 |
| Northstar (Teva ANDA) | - | - | - | 5.99 | 6.47 | 4.77 | - | 1.20 | - |
| Sandoz | 6.63 | 6.46 | 6.13 | 5.75 | 5.94 | - | - | - | - |
| Teva | 6.47 | 6.34 | 6.11 | 5.61 | 6.41 | 7.58 | 6.74 | - | - |

**MPA 80 mg/mL x 1 mL - clean $ per vial** (Rx-weighted median state-cell $/vial; cells with units/Rx consistent with 1 vial per unit; min 50 Rx in clean cells)

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| ALL BRAND | 12.45 | 11.67 | 11.60 | 10.45 | 11.08 | 11.99 | 11.80 | 10.40 | 10.47 |
| ALL GENERIC | 12.55 | 11.98 | 10.57 | 10.05 | 10.77 | 11.67 | 10.66 | 9.49 | 9.56 |
| Pfizer brand | 12.45 | 11.67 | 11.60 | 10.45 | 11.08 | 11.99 | 11.80 | 10.40 | 10.47 |
| Amneal | - | - | 30.06 | 9.23 | 10.86 | 11.64 | 10.66 | 9.49 | 9.56 |
| Northstar (Teva ANDA) | - | - | - | 9.52 | 9.44 | 11.39 | - | - | - |
| Sandoz | 11.28 | 12.61 | 11.62 | - | - | - | - | - | - |
| Teva | 12.55 | 11.98 | 10.57 | 10.05 | 10.80 | 11.97 | 9.79 | - | - |

**MPA 40 mg/mL x 10 mL - clean $ per unit (likely mL)** (Rx-weighted median state-cell $/unit (likely mL); cells with units/Rx consistent with 1 unit (likely mL) per unit; min 50 Rx in clean cells)

| Labeler | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 Q1 |
|---|---|---|---|---|---|---|---|---|---|
| ALL BRAND | 6.62 | 6.44 | 5.63 | 5.85 | 7.15 | 8.45 | 6.44 | 5.33 | 4.79 |
| ALL GENERIC | 6.37 | 6.03 | 5.83 | 5.62 | 5.92 | 7.26 | 5.94 | 4.91 | 4.73 |
| Pfizer brand | 6.62 | 6.44 | 5.63 | 5.85 | 7.15 | 8.45 | 6.44 | 5.33 | 4.79 |
| Amneal | - | - | - | - | - | - | 4.23 | 5.06 | 4.73 |
| Endo/Par Sterile | - | - | - | - | - | 5.81 | 12.28 | 13.43 | 13.49 |
| Eugia (Aurobindo) | - | - | - | - | - | - | 5.32 | 5.24 | 4.79 |
| Northstar (Teva ANDA) | - | - | - | 5.53 | 5.92 | 7.12 | - | - | - |
| Sagent | - | - | - | - | 6.83 | 7.30 | 5.94 | 4.06 | 4.71 |
| Sandoz | 6.33 | 7.93 | - | - | - | - | 5.88 | 4.30 | 4.38 |
| Teva | 6.48 | 6.03 | 5.83 | 5.62 | 5.79 | 7.26 | 6.67 | - | - |


- **MPA multi-dose vials are priced per mL, not per vial.** The 5 mL and 10 mL MPA medians (about $5–7 for 40 mg/mL) match the 1 mL single-dose price. "Units" for these vials are therefore almost certainly mL (one dose drawn per claim), not whole vials — [SDUD](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536).
- **Outliers excluded from interpretation:**
  - Hospira A-Methapred 40 mg (0409-3217-05), 2019: $222,304 on 16 Rx nationally, of which only $19.78 was the Medicaid-paid amount. This looks like a reporting error.
  - Hospira 125 mg, 2019: a $534.68/vial clean median from a single state.
  - Source: [SDUD 2019](https://data.medicaid.gov/dataset/daba7980-e219-5996-9bec-90358fd156f1).

### Inferences
- **Price erosion: MPSS.** The brand 40 mg and 125 mg Medicaid reimbursement per vial fell by about a third between 2024 and 2025 (40 mg $5.49 → $3.75; 125 mg $9.31 → $6.28). That followed the April 2024 move to J2919 and the rise of DRL and Hikma. Over 2018–2024 the brand per-vial reimbursement had been broadly flat.
  - Medicaid physician-administered reimbursement typically keys off Medicare ASP-based HCPCS rates. The Part B 2024 average spend for J2919 was $0.284 per 5 mg, or about $2.27 per 40 mg and $7.10 per 125 mg. That is consistent with the medians above (see Q3).
  - **Implication:** the generic entry is showing up as falling code-level prices, not as a brand–generic gap.
- **Price direction: HSS.** Solu-Cortef reimbursement has been rising, not eroding: about +67% per 100 mg vial from 2018 to 2025 in Medicaid, and +52% in Medicare Part B average spend per J1720 unit (2018–2024).
  - Generic entry so far (Cipla at about 28% below the brand median in Medicaid) is limited.
  - With Zydus and Apotex now listed, HSS looks like the earlier-stage opportunity: higher and rising price per vial, fewer competitors. The flip side is that erosion is likely to accelerate from 2026–27.
- **The brand–generic gap is not observable in Medicaid MPSS/MPA reimbursement.** Brand and generic NDCs billed under the same HCPCS code get the same fee-schedule rate. The "gap" in SDUD is noise from state mix.
  - Manufacturer-level realized price differences need ASP, NADAC or WAC data (other researchers) or the Part D per-unit data (Q4: generic MPSS about 37% below brand per unit in 2024).

### Gaps
- **Pharmacy vs physician-administered claims cannot be separated.** SDUD does not distinguish pharmacy-dispensed from physician-administered claims, and has no site of care. So I could not isolate NDC-level (pharmacy, NADAC-based) pricing from HCPCS-based pricing.
- **mL-reporting states are excluded from the HSS $/vial.** For 2 mL vials, units/Rx of about 2 cannot distinguish "2 vials reported in EA" from "1 vial reported in mL". Those cells were excluded, which leaves HSS 100 mg $/vial resting on about 25–50% of Rx.

## Q3. Medicare Part B Spending by Drug: volume and spending context (J1720, J2920/J2930/J2919, J1020/J1030/J1040/J1010)

### Takeaway
- **HSS:** Medicare FFS Part B volume of J1720 fell from about 50k units (2018) to 26.7k (2024). Average spend per 100 mg unit rose from $11.83 to $18.00, and the DY2024 average ASP was $18.89. This corroborates Solu-Cortef price increases.
- **MPSS:** Part B units were about 360–364k (125 mg, J2930) and 117–147k (40 mg, J2920) a year through 2023. In 2024 the J2919 code (Apr–Dec) logged 4.15M 5-mg units (20.8M mg) at $1.18M.
- **MPA:** the largest Part B volume, at about 1.5M J1030 and 0.83M J1040 units in 2023, and 80.2M mg under J1010 in 2024.

### Cited Findings
- **2024 release.** The CMS Part B Spending by Drug DY2024 release (2020–2024) reports:
  - J1720 (HSS up to 100 mg): spending $590,909 (2020), $642,328 (2021), $680,268 (2022), $441,127 (2023), $480,303 (2024). Units 45,086 / 45,378 / 43,568 / 26,194 / 26,692. Average spend per unit $13.11 / $14.16 / $15.61 / $16.84 / $17.99. Average DY24 ASP $18.89.
  - J2919 (MPSS 5 mg), 2024: $1,179,260 spending, 4,151,843 units, 177,911 claims, 92,927 beneficiaries, $0.284 per unit, ASP $0.291.
  - J1010 (MPA 1 mg), 2024: $10,310,247, 80,220,708 units, 1,297,268 claims, $0.129 per unit.
  - Source: [CMS Part B Spending by Drug](https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-spending-by-drug); [API](https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data).
- **Retired codes are only in older releases.** The DY2024 release does not carry J2920/J2930/J1020/J1030/J1040. Earlier CMS releases (DY2022/DY2023), as extracted by the parallel ASP workstream into `partb_spending_by_hcpcs_2016_2024.csv`, show:
  - J2930 units: 361,205 (2018), 363,602 (2019), 271,134 (2020), 267,477 (2021), 280,964 (2022), 270,488 (2023). Average spend per unit $6.44 → $5.43.
  - J2920 units: 138,685 (2018) → 117,446 (2023). Average spend per unit $4.46 → $3.90.
  - J1030 units: 2,754,043 (2018) → 1,504,518 (2023).
  - J1040 units: 1,612,235 (2018) → 832,090 (2023).
  - J1720 units: 50,236 (2018) and 48,404 (2019).
  - Source: [CMS Part B Spending by Drug](https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-spending-by-drug).

### Inferences
- **Part B is the same order of magnitude as Medicaid SDUD, but neither is the full market.** Medicare FFS Part B MPSS 125 mg volume (about 270k J2930 units in 2023) is similar to Medicaid SDUD MPSS 125 mg Rx (about 277k in 2023). For a hospital-heavy molecule, neither dataset captures inpatient use, which is bundled into DRG/OPPS packaging.
- **J1720 volume drop.** The 40% fall in J1720 units in 2023 (43.6k → 26.2k) could reflect coding or packaging changes, or Solu-Cortef supply. I found no confirming source.

### Gaps
- **No NDC or manufacturer split in Part B.** It is HCPCS-level, so brand vs generic is not identifiable.
- **No J2920/J2930 rows for 2024.** Q1 2024 J2920/J2930 spending (before J2919) is not in the DY2024 release, so 2024 MPSS Part B is incomplete.
- **J1010 start date not confirmed.** The exact effective date of J1010 was not verified; the dataset shows it only in 2024.

## Q4. Medicare Part D Spending by Drug: brand vs generic manufacturer-level claims, spending and spend per dosage unit

### Takeaway
All three injectables appear in Part D, but volumes are small (Part D is pharmacy-dispensed).
- **MPSS:** genericized. Solu-Medrol had 46.6% of 2024 claims (14,318 of 30,716). Dr. Reddy's had 26.5%, Fresenius Kabi about 24.5% across two manufacturer labels, and Hikma about 2.3%. The generic average spend per dosage unit was about 37% below brand ($4.66 vs $7.40).
- **HSS:** Solu-Cortef 99.3% of 2024 claims; Cipla had 110 claims.
- **MPA:** Depo-Medrol only 7.4% of 2024 claims; Amneal about 88.5%.

### Cited Findings
- **MPSS, Part D DY2024 release (2020–2024):**
  - Solu-Medrol (all Pfizer labels) claims: 12,382 (2020), 9,841 (2021), 9,154 (2022), 9,513 (2023), 14,318 (2024).
  - Generic MPSS claims: 11,857 / 11,630 / 12,056 / 14,177 / 16,398.
  - 2024 generic manufacturer claims: Dr. Reddy's 8,141 ($185,630; $5.85 per unit), Fresenius Kabi 5,389 ($91,027; $7.26), App/Fresenius 2,155 ($136,560; $5.21), West-Ward/Hikma 366 and Hikma 334, Amneal 13.
  - Source: [CMS Part D Spending by Drug](https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-d-spending-by-drug); [API](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data).
- **HSS, Part D:**
  - Solu-Cortef claims: 10,543 (2020), 10,361 (2021), 11,723 (2022), 11,361 (2023), 15,174 (2024).
  - Pfizer US Pharm-labelled Solu-Cortef average spend per dosage unit rose from $8.25 (2020) to $13.83 (2024).
  - Cipla HSS: 110 claims, $4,576, $13.62 per unit (2024).
  - Source: [CMS Part D Spending by Drug](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data).
- **MPA, Part D:**
  - Depo-Medrol claims: 1,850 (2020), 981 (2021), 317 (2022), 704 (2023), 914 (2024).
  - Generic MPA claims: 396 / 3,142 / 9,366 / 11,411 / 11,520, mostly Amneal Biosciences (10,398 in 2024).
  - Brand average spend per dosage unit $14.53 vs generic $10.74 (2024).
  - Source: [CMS Part D Spending by Drug](https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data).
- **Rebates are not reflected.** Part D spending is gross drug cost and "do[es] not reflect any manufacturers' rebates or other price concessions" — [CMS Part D Spending by Drug description, data.cms.gov catalog](https://data.cms.gov/data.json).

### Inferences
- **Part D is the cleanest signal of pharmacy-channel substitution:**
  - MPSS generics already hold about half the Part D claims.
  - MPA is about 90% generic.
  - HSS remains about 99% brand.
  - This supports "Medrol crowded / Cortef uncrowded" in a second, independent dataset.
- **Cipla's Part D price.** Cipla's HSS per-unit Part D spend ($13.62) is close to Solu-Cortef's ($12.02–13.83 across Pfizer labels). An early entrant in a low-competition molecule does not appear to be discounting deeply at the pharmacy level. Note the tiny sample.

### Gaps
- **Small, partial slice.** Part D volumes are tiny relative to hospital use, and the release covers only 2020–2024. Older releases (2018–2019) are not in the current data.cms.gov catalog.
- **Manufacturer labels are inconsistent.** Part D manufacturer names (e.g., "App/Fresenius" vs "Fresenius Kabi", "Pfizer-Novaplus", "Phar-Prep/Pfizer") reflect labeler or private-label variants, not necessarily distinct companies.

## Q5. Caveats: how representative are these proxies?

### Takeaway
- **These are proxies, not true market share.** Medicaid SDUD (and Part B/Part D) cover outpatient and pharmacy plus physician-administered claims for a sub-population. They exclude hospital inpatient use, which dominates MPSS and HSS.
- **Dollars are pre-rebate reimbursement amounts.** They are skewed by state payment rules, not manufacturer net prices.
- **Use them for direction:** who is gaining, how many competitors, and whether reimbursement per vial is rising or falling. Do not use them for absolute share.

### Cited Findings
- **Physician-administered drugs are in SDUD.** The DRA 2005 requires states to collect NDC-level utilization for covered outpatient physician-administered drugs to secure manufacturer rebates. That is why physician-administered injectables like MPSS/MPA appear in SDUD with NDCs — [Medicaid.gov Physician-Administered Drugs](https://www.medicaid.gov/medicaid/prescription-drugs/state-prescription-drug-resources/physician-administered-drugs-pad/index.html).
- **NDC capture on PAD claims has been incomplete in some states.** OIG audits found states failing to bill rebates on PAD claims (often MCO claims) because of missing or invalid NDCs, e.g., Virginia about $5.8M in unbilled rebates — [HHS OIG Virginia PAD audit](https://oig.hhs.gov/reports/all/2016/virginia-did-not-bill-manufacturers-for-some-rebates-for-physician-administered-drugs-dispensed-to-enrollees-of-medicaid-managed-care-organizations).
- **SDUD amounts are pre-rebate** — [CMS SDUD field descriptions](https://www.cms.gov/files/document/medicaid-state-drug-utilization-data-field-descriptions.pdf).
- **Part D spending excludes rebates and price concessions**, and Part B metrics are at the HCPCS level — [data.cms.gov catalog](https://data.cms.gov/data.json); [CMS Part B Spending by Drug](https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-spending-by-drug).

### Inferences
- **Coverage and skew.** Medicaid MPSS volume (about 370k Rx in 2025) plus Medicare Part B (about 0.4M 125-mg-equivalent units in 2023) is a small slice of the US MPSS market. That market is dominated by inpatient and ED hospital use bought through GPOs, where shortages and contract awards drive share. Shares here likely over-represent physician-office and clinic-administered use and specific states.
- **Rebate effects.**
  - Brand (innovator) Medicaid rebates are larger than generic rebates, so net brand reimbursement is lower than shown.
  - The ARPA removal of the Medicaid rebate cap (effective 2024) could make the inflation-penalty rebate large for long-marketed brands with price increases, such as Solu-Cortef. That would leave Medicaid net prices for the brand much lower than gross.
  - This is directional, not quantified here.
- **Hospital channel.** For the hospital channel, IQVIA (Bloomberg) and the ASP/WAC/NADAC work by other researchers should be weighted more heavily. Use SDUD and Part D mainly to confirm direction: number of entrants, generic share momentum and price trend.

### Gaps
- **No public inpatient-level labeler-share dataset.** I found no public NDC-level dataset of hospital inpatient utilization by labeler. That would be needed for true market share.
- **Net prices not computed.** I did not quantify Medicaid rebate amounts (URA is confidential) or 340B effects. Net prices are therefore unknown.
