# US pricing for injectable corticosteroids: Medicare Part B ASP history (2016 to Q4 2026), per-vial prices, labelers, WAC/NADAC and Part B/D spending
*As of 21 October 2026. Researcher notes for the Symbiotec Pharmalab DCV / complex-injectable thesis (Solu-Medrol and Solu-Cortef generics).*

Abbreviations: MPSS = methylprednisolone sodium succinate (Solu-Medrol); HSS = hydrocortisone sodium succinate (Solu-Cortef); MPA = methylprednisolone acetate (Depo-Medrol); PL = CMS Part B payment limit; ASP = average sales price; DCV = dual-chamber vial (Pfizer's "Act-O-Vial").

**How the data was collected.** All 88 quarterly CMS files from Jan 2016 to Oct 2026 (44 payment-limit files and 44 NDC-HCPCS crosswalks) were downloaded from the [CMS ASP Pricing Files page](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files) and parsed with Python. Each file's URL is listed in `data/asp_source_files.csv`. The latest file is the [October 2026 Medicare Part B Payment Limit File (final)](https://www.cms.gov/files/zip/october-2026-medicare-part-b-payment-limit-files-final.zip) together with the [October 2026 NDC-HCPCS crosswalk (final)](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip). Where CMS later posted revised versions of the historical files (the "updated mmddyy" versions), those were used. Every figure in the ASP sections below comes directly from those files; any derived figure says how it was computed.

**Cleaned CSV outputs** are in `/home/user/sample/research_notes/Symbiotec DCV steroid injectables/data/`:
- ASP history: `asp_history.csv` (long format), `asp_payment_limit_wide.csv`, `asp_per_vial.csv`, `asp_per_vial_wide.csv`, `asp_growth_summary.csv`, `asp_qoq_moves_over_10pct.csv`.
- Crosswalk and labelers: `asp_crosswalk_ndcs_oct2026.csv`, `asp_crosswalk_labelers.csv`, `asp_crosswalk_labeler_counts_by_quarter.csv`.
- Medicare and Medicaid spending: `partb_spending_by_hcpcs_2016_2024.csv`, `partb_spending_by_molecule.csv`, `partd_spending_steroid_injectables_2020_2024.csv`, `medicaid_spending_steroid_injectables_2020_2024.csv`.
- Price points and approvals: `nadac_steroid_injectables_annual.csv`, `nadac_steroid_injectables_latest_by_ndc.csv`, `pfizer_wac_ct_disclosures.csv`, `fda_applications_openfda.csv`.
- Sources: `asp_source_files.csv`.

Two files in the folder are not mine: `partb_spending.csv` and `partd_spending.csv` were written at the same time by another researcher, so my versions carry the longer names above. The scripts are in `/tmp/claude-0/-home-user-sample/28da1d41-580b-501a-b778-8022ed0c448f/scratchpad/asp_scripts/`.

---

## Q1. What is the Part B payment limit and implied ASP per billing unit for each code, every quarter 2016 to Q4 2026, and what does that imply per vial?

### Takeaway
Hydrocortisone sodium succinate (J1720, per 100 mg) roughly tripled. Its payment limit went from $7.502 in Q1 2016 to $23.149 in Q4 2026, a CAGR of about 11%. It rose almost every quarter and set a new high in Q4 2026. Methylprednisolone sodium succinate (J2930/J2920, then J2919 from April 2024) rose from 2016 to a 2018–19 peak and has since been flat to falling. The 125 mg-equivalent ASP is about $6 today, against $6.57 at the Q3 2018 peak. The billing codes changed on 1 April 2024: J2920/J2930 became J2919 (5 mg), and J1020/J1030/J1040 became J1010 (1 mg). Per-vial conversions therefore need the unit rules set out below.

### Cited Findings

**HCPCS codes and dosage descriptors** (verified from the CMS payment-limit files)
- The MPSS codes:
  - J2920 "Methylprednisolone injection", 40 MG, and J2930 "Methylprednisolone injection", 125 MG, were present from Q1 2016 to Q1 2024 and are absent from Q2 2024 onward. — [CMS ASP pricing files](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files)
  - J2919 "Inj, methylpred sod succ 5mg", 5 MG, first appears in the April 2024 file with the note "Added April 2024". — [CMS April 2024 ASP pricing file](https://www.cms.gov/files/zip/april-2024-asp-pricing-file.zip)
- The MPA codes: J1010 "Inj, methylpred acetate 1 mg", 1 MG, was "Added April 2024". J1020, J1030 and J1040 (20, 40 and 80 mg) appear for the last time in the January 2024 file. — [CMS April 2024 ASP pricing file](https://www.cms.gov/files/zip/april-2024-asp-pricing-file.zip)
- Third-party coding references confirm that J2920 and J2930 were deleted for dates of service from 1 April 2024 and that J2919 is billed per 5 mg, so 1,000 mg = 200 units. — [AAPC J2919](https://www.aapc.com/codes/hcpcs-codes/J2919); [hcpcs.codes J2919](https://hcpcs.codes/j-codes/J2919/)
- J1720 "Hydrocortisone sodium succ i", 100 MG, appears in every quarter. Its dosage descriptor changed to "UP TO 100 MG" in the October 2026 crosswalk. — [CMS Oct 2026 crosswalk](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip)
- No other relevant codes are priced:
  - J1710 (hydrocortisone sodium phosphate) and J1700 (hydrocortisone acetate) do not appear in any 2016–2026 payment-limit file.
  - J7509 (oral methylprednisolone, 4 mg) appears but is not relevant.
  - Source: [CMS ASP pricing files](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files)
- Lag and file changes:
  - Each file states its ASP basis with a two-quarter lag. For example, the October 2026 file is "based on 2Q26 ASP data" and the January 2016 file on "3Q15 ASP data". — [CMS Oct 2026 payment limit file](https://www.cms.gov/files/zip/october-2026-medicare-part-b-payment-limit-files-final.zip)
  - From January 2026 CMS renamed the file "Medicare Part B Payment Limit File". From April 2026 it added a separate "Drugs Not Payable Under Part B" file. None of our codes appear in that file.
- Coinsurance: the files have carried a "Co-insurance Percentage" column (the IRA inflation-rebate coinsurance adjustment) since 2023. It reads **20.000 for every steroid code in every quarter**. No Part B inflation-rebate coinsurance reduction was triggered for these codes. — [CMS ASP pricing files](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files)

**Quarterly payment limits, $ per billing unit** (CMS files; ASP = PL / 1.06)

| Quarter | J2920 (40mg) | J2930 (125mg) | J2919 (5mg) | J1720 (100mg) | J1030 (40mg) | J1040 (80mg) | J1010 (1mg) | J1020 (20mg) |
|---|---|---|---|---|---|---|---|---|
| 2016-Q1 | 2.898 | 4.105 |  | 7.502 | 4.308 | 8.334 |  | 4.495 |
| 2016-Q2 | 2.955 | 4.213 |  | 7.462 | 4.489 | 8.564 |  | 4.493 |
| 2016-Q3 | 3.331 | 4.964 |  | 8.163 | 4.954 | 9.478 |  | 4.754 |
| 2016-Q4 | 3.726 | 5.126 |  | 8.531 | 5.222 | 9.800 |  | 4.821 |
| 2017-Q1 | 4.002 | 5.498 |  | 9.118 | 5.472 | 10.268 |  | 4.987 |
| 2017-Q2 | 4.064 | 5.568 |  | 9.034 | 5.568 | 10.614 |  | 4.990 |
| 2017-Q3 | 4.348 | 6.033 |  | 10.852 | 6.004 | 11.530 |  | 5.402 |
| 2017-Q4 | 4.337 | 6.093 |  | 11.279 | 6.362 | 12.260 |  | 5.592 |
| 2018-Q1 | 4.346 | 5.985 |  | 11.931 | 6.694 | 12.963 |  | 5.945 |
| 2018-Q2 | 4.537 | 6.672 |  | 12.050 | 6.638 | 12.909 |  | 4.837 |
| 2018-Q3 | 4.805 | 6.965 |  | 13.177 | 7.001 | 13.510 |  | 4.177 |
| 2018-Q4 | 4.717 | 6.942 |  | 13.051 | 6.773 | 13.321 |  | 4.314 |
| 2019-Q1 | 4.872 | 6.928 |  | 12.993 | 6.600 | 12.863 |  | 4.010 |
| 2019-Q2 | 4.464 | 6.361 |  | 13.043 | 6.462 | 12.489 |  | 3.895 |
| 2019-Q3 | 4.489 | 6.169 |  | 13.040 | 6.238 | 12.016 |  | 3.661 |
| 2019-Q4 | 4.487 | 6.119 |  | 12.901 | 6.245 | 11.934 |  | 3.697 |
| 2020-Q1 | 4.582 | 6.317 |  | 13.050 | 6.287 | 11.895 |  | 3.611 |
| 2020-Q2 | 4.478 | 6.392 |  | 12.896 | 6.047 | 11.630 |  | 3.439 |
| 2020-Q3 | 4.516 | 6.716 |  | 14.142 | 6.093 | 11.698 |  | 3.614 |
| 2020-Q4 | 4.171 | 5.636 |  | 14.151 | 5.880 | 11.193 |  | 3.462 |
| 2021-Q1 | 4.377 | 5.491 |  | 14.154 | 5.804 | 10.755 |  | 3.346 |
| 2021-Q2 | 4.275 | 5.793 |  | 14.207 | 5.735 | 10.741 |  | 3.214 |
| 2021-Q3 | 4.027 | 5.451 |  | 14.774 | 5.551 | 10.409 |  | 3.030 |
| 2021-Q4 | 4.108 | 5.565 |  | 14.811 | 5.625 | 10.676 |  | 3.165 |
| 2022-Q1 | 4.221 | 5.890 |  | 14.761 | 5.698 | 11.822 |  | 3.584 |
| 2022-Q2 | 4.248 | 6.120 |  | 14.743 | 5.915 | 10.518 |  | 3.192 |
| 2022-Q3 | 4.188 | 5.524 |  | 17.574 | 6.926 | 10.443 |  | 4.611 |
| 2022-Q4 | 4.277 | 5.742 |  | 17.874 | 7.452 | 11.591 |  | 1.491 |
| 2023-Q1 | 4.079 | 5.949 |  | 17.881 | 8.055 | 12.217 |  | 4.611 |
| 2023-Q2 | 4.131 | 5.467 |  | 17.911 | 8.084 | 12.747 |  | 4.611 |
| 2023-Q3 | 4.237 | 5.725 |  | 17.514 | 7.613 | 11.910 |  | 7.167 |
| 2023-Q4 | 3.433 | 4.985 |  | 17.672 | 7.202 | 10.757 |  | 7.099 |
| 2024-Q1 | 4.188 | 5.882 |  | 17.845 | 6.419 | 9.803 |  | 7.038 |
| 2024-Q2 |  |  | 0.273 | 18.459 |  |  | 0.134 |  |
| 2024-Q3 |  |  | 0.295 | 19.853 |  |  | 0.138 |  |
| 2024-Q4 |  |  | 0.304 | 19.397 |  |  | 0.119 |  |
| 2025-Q1 |  |  | 0.268 | 20.939 |  |  | 0.117 |  |
| 2025-Q2 |  |  | 0.251 | 20.580 |  |  | 0.110 |  |
| 2025-Q3 |  |  | 0.259 | 21.201 |  |  | 0.120 |  |
| 2025-Q4 |  |  | 0.210 | 21.312 |  |  | 0.119 |  |
| 2026-Q1 |  |  | 0.264 | 22.061 |  |  | 0.120 |  |
| 2026-Q2 |  |  | 0.241 | 22.141 |  |  | 0.112 |  |
| 2026-Q3 |  |  | 0.224 | 23.056 |  |  | 0.117 |  |
| 2026-Q4 |  |  | 0.255 | 23.149 |  |  | 0.123 |  |

Source: [CMS ASP pricing files, Jan 2016 to Oct 2026](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files). Files before 2016 (2015) were also parsed and are in the scratch raw folder but are not in the CSV outputs.

**Annual average implied ASP per billing unit** (= mean of the four quarterly PLs / 1.06; derived from the CMS files). 2024 is split between the old codes (Q1 only) and the new codes (Q2–Q4). 2026 covers all four 2026 files.

| Year | J2920 | J2930 | J2919 | J1720 | J1030 | J1040 | J1010 |
|---|---|---|---|---|---|---|---|
| 2016 | 3.045 | 4.342 |  | 7.467 | 4.475 | 8.532 |  |
| 2017 | 3.951 | 5.470 |  | 9.501 | 5.520 | 10.536 |  |
| 2018 | 4.341 | 6.265 |  | 11.842 | 6.393 | 12.430 |  |
| 2019 | 4.319 | 6.032 |  | 12.259 | 6.025 | 11.628 |  |
| 2020 | 4.186 | 5.911 |  | 12.792 | 5.733 | 10.947 |  |
| 2021 | 3.959 | 5.259 |  | 13.667 | 5.357 | 10.043 |  |
| 2022 | 3.994 | 5.490 |  | 15.319 | 6.130 | 10.466 |  |
| 2023 | 3.745 | 5.218 |  | 16.740 | 7.300 | 11.234 |  |
| 2024 | 3.951 (Q1) | 5.549 (Q1) | 0.274 (Q2–Q4) | 17.819 | 6.056 (Q1) | 9.248 (Q1) | 0.123 (Q2–Q4) |
| 2025 |  |  | 0.233 | 19.819 |  |  | 0.110 |
| 2026 |  |  | 0.232 | 21.322 |  |  | 0.111 |

**Billing-unit conventions used for per-vial conversion** (taken from the CMS crosswalk BILLUNITS field, i.e. billable units per package)
- MPSS before April 2024: 40 mg vial = 1 unit of J2920; 125 mg = 1 unit of J2930. Larger vials use J2930 units of 125 mg, so 500 mg = 4 units, 1 g = 8 and 2 g = 16. — [CMS Jan 2024 crosswalk](https://www.cms.gov/files/zip/january-2024-ndc-hcpcs-crosswalk.zip)
- MPSS from April 2024 (J2919, 5 mg): the Oct 2026 crosswalk lists 40 mg = 8 units, 125 mg = 25, 500 mg = 100, 1 g = 200 and 2 g = 400 (Pfizer NDC 00009-0850-01 = 400). — [CMS Oct 2026 crosswalk](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip)
- HSS (J1720, 100 mg): 100 mg = 1 unit, 500 mg = 5 and 1 g = 10.
  - **250 mg vial = 2.5 units in every crosswalk from 2015 to Q3 2026, but 3 units in the October 2026 crosswalk.** Examples: Pfizer 00009-0013-05 changed from 2.5 to 3 and HealthFirst 51662-1262-01 from 2.5 to 3, while the descriptor became "UP TO 100 MG".
  - The economic per-vial ASP therefore uses 2.5 units through Q3 2026. A provider billing a 250 mg vial under the "up to 100 mg" rule bills 3 units; both versions are in `asp_per_vial.csv`.
  - Sources: [CMS Jan 2016 crosswalk](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Part-B-Drugs/McrPartBDrugAvgSalesPrice/downloads/2016-January-ASP-NDC-HCPCS-Crosswalk.zip); [CMS Oct 2026 crosswalk](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip)
- MPA: 40 mg/mL 1 mL = 1 unit of J1030, and 80 mg/mL 1 mL = 1 unit of J1040, until Q1 2024. From Q2 2024 under J1010, 40 mg = 40 units and 80 mg = 80 units; a 5 mL vial of 40 mg/mL is 200 units, and so on. — [CMS Oct 2026 crosswalk](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip)

**Implied ASP per vial at selected quarters, $** (= PL × billing units per vial / 1.06; derived from CMS files)

| Vial | 2016-Q1 | 2018-Q3 | 2019-Q1 | 2021-Q4 | 2023-Q4 | 2024-Q1 | 2024-Q2 | 2025-Q4 | 2026-Q1 | 2026-Q4 |
|---|---|---|---|---|---|---|---|---|---|---|
| MPSS 40 mg | 2.73 | 4.53 | 4.60 | 3.88 | 3.24 | 3.95 | 2.06* | 1.58 | 1.99 | 1.92 |
| MPSS 125 mg | 3.87 | 6.57 | 6.54 | 5.25 | 4.70 | 5.55 | 6.44 | 4.95 | 6.23 | 6.01 |
| MPSS 500 mg | 15.49 | 26.28 | 26.14 | 21.00 | 18.81 | 22.20 | 25.75 | 19.81 | 24.91 | 24.06 |
| MPSS 1 g | 30.98 | 52.57 | 52.29 | 42.00 | 37.62 | 44.39 | 51.51 | 39.62 | 49.81 | 48.11 |
| MPSS 2 g | 61.96 | 105.13 | 104.57 | 84.00 | 75.25 | 88.78 | 103.02 | 79.25 | 99.62 | 96.23 |
| HSS 100 mg | 7.08 | 12.43 | 12.26 | 13.97 | 16.67 | 16.83 | 17.41 | 20.11 | 20.81 | 21.84 |
| HSS 250 mg (2.5 u) | 17.69 | 31.08 | 30.64 | 34.93 | 41.68 | 42.09 | 43.54 | 50.26 | 52.03 | 54.60 |
| HSS 250 mg (3 u, billed) | 21.23 | 37.29 | 36.77 | 41.92 | 50.02 | 50.50 | 52.24 | 60.32 | 62.44 | 65.52 |
| HSS 500 mg | 35.39 | 62.16 | 61.29 | 69.86 | 83.36 | 84.17 | 87.07 | 100.53 | 104.06 | 109.19 |
| HSS 1 g | 70.77 | 124.31 | 122.58 | 139.73 | 166.72 | 168.35 | 174.14 | 201.06 | 208.12 | 218.39 |
| MPA 40 mg/mL 1 mL | 4.06 | 6.60 | 6.23 | 5.31 | 6.79 | 6.06 | 5.06* | 4.49 | 4.53 | 4.64 |
| MPA 80 mg/mL 1 mL | 7.86 | 12.75 | 12.13 | 10.07 | 10.15 | 9.25 | 10.11* | 8.98 | 9.06 | 9.28 |

\*Series break at the April 2024 code change (see inferences).

**Annual average implied ASP per vial, $** (derived; same method)

| Year | MPSS 40 mg | MPSS 125 mg | MPSS 500 mg | MPSS 1 g | HSS 100 mg | HSS 250 mg (2.5u) | HSS 500 mg | HSS 1 g | MPA 40 mg/mL | MPA 80 mg/mL |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3.04 | 4.34 | 17.37 | 34.73 | 7.47 | 18.66 | 37.33 | 74.67 | 4.47 | 8.53 |
| 2017 | 3.95 | 5.47 | 21.88 | 43.76 | 9.50 | 23.75 | 47.50 | 95.01 | 5.52 | 10.54 |
| 2018 | 4.34 | 6.27 | 25.06 | 50.12 | 11.84 | 29.61 | 59.21 | 118.42 | 6.39 | 12.43 |
| 2019 | 4.32 | 6.03 | 24.13 | 48.26 | 12.26 | 30.64 | 61.29 | 122.59 | 6.03 | 11.63 |
| 2020 | 4.18 | 5.91 | 23.64 | 47.29 | 12.79 | 31.98 | 63.96 | 127.92 | 5.73 | 10.95 |
| 2021 | 3.96 | 5.26 | 21.04 | 42.08 | 13.66 | 34.16 | 68.33 | 136.67 | 5.36 | 10.04 |
| 2022 | 3.99 | 5.49 | 21.96 | 43.92 | 15.32 | 38.30 | 76.59 | 153.19 | 6.13 | 10.46 |
| 2023 | 3.75 | 5.22 | 20.87 | 41.75 | 16.74 | 41.85 | 83.70 | 167.40 | 7.30 | 11.24 |
| 2024 | 2.63* | 6.53* | 26.11* | 52.23* | 17.82 | 44.55 | 89.10 | 178.19 | 5.21* | 9.69* |
| 2025 | 1.86 | 5.83 | 23.30 | 46.60 | 19.82 | 49.55 | 99.09 | 198.19 | 4.40 | 8.79 |
| 2026 | 1.85 | 5.80 | 23.21 | 46.41 | 21.32 | 53.31 | 106.61 | 213.22 | 4.46 | 8.90 |

**Cross-checks**
- The Medicare Part B Spending by Drug dashboard reports an "Avg DY24 ASP Price" of $18.8885 for J1720, $0.290667 for J2919 and $0.130333 for J1010. These are calendar-2024 averages of the payment limits and match the means of the CMS files used here (J1720 2024 average PL = $18.889). — [data.cms.gov Part B Spending by Drug 2024 CSV](https://data.cms.gov/sites/default/files/2026-06/6616fc91-eb70-404c-9f27-1448e47a3a73/DSD_PTB_RY26_P06_V10_DYT24_HCPCS-%20260602.csv)
- The CMS crosswalk introduction text says Medicare pays Part B drugs at "106% of the Average Sales Price", with ASP reported at the 11-digit NDC level. Billable units per package equal the package amount divided by the HCPCS dosage descriptor. — [CMS Oct 2026 crosswalk intro text](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip)

### Inferences
- **ASP = PL / 1.06 is a reasonable back-out for all these codes.** They are ordinary single- or multi-source drugs: not biosimilars (no ASP+8%), not new drugs on WAC+3%, and not in the vaccine or blood AWP columns. The 2% sequestration cut applies to claim payment and is not reflected in the published limits, so 1.06 is still the right divisor. I did not check CMS's AMP-price-substitution lists; if a substitution had occurred, PL/1.06 would differ from true ASP for that quarter.
- **The April 2024 code change breaks the per-vial series for MPSS and MPA.**
  - Before April 2024, J2930's per-unit ASP was a volume-weighted average across 125 mg, 500 mg, 1 g and 2 g vials, with 40 mg vials priced separately under J2920.
  - From April 2024, J2919 blends all strengths, including the 40 mg vial, which is the most expensive per mg, into one per-5 mg price.
  - As a result, J2919-implied "per vial" prices overstate large vials slightly and understate the 40 mg vial heavily. The 40 mg figure fell from $3.95 to $2.06 at the switch purely through the code change.
  - The same blending applies to J1010 against J1030/J1040.
  - Within-code trends (Q2) are more reliable than per-vial levels across the break.
- **The October 2026 crosswalk counts 250 mg Solu-Cortef as 3 billing units instead of 2.5.** CMS computes HCPCS-level ASP by dividing NDC-level sales by billing units. If CMS applies the 3-unit convention from 3Q26 data onward (the January 2027 file), the J1720 per-unit ASP should fall mechanically by up to about 1/6 on the 250 mg share of volume, even with no change in market price. This is my inference; no CMS explanation was found.
- **Implied ASPs are per-unit blends across every labeler's NDC.** For J1720 through at least 2Q24 data, this is effectively Pfizer's Solu-Cortef net selling price, because Pfizer was the only non-repackager labeler (Q3). For MPSS it is a blend of Pfizer brand and 3–4 generic labelers.

### Gaps
- No archive.org copies were needed; all CMS files downloaded directly. The AMP price-substitution files, which CMS publishes separately, were not checked.
- CMS gives no reason for the October 2026 J1720 change from 2.5 to 3 billing units. Searches found no CMS guidance, and the code-specific descriptor change was observed only in the data.

---

## Q2. What are the CAGRs and percentage changes over 1, 3 and 5 years, and are there shortage-linked spikes?

### Takeaway
The growth paths diverge sharply:
- **J1720 hydrocortisone:** CAGR of about 9% over both 3 and 5 years and +8.6% over 1 year. It reached its all-time high in Q4 2026.
- **MPSS:** rose about 60% from 2016 to a 2018–19 peak, then fell about 15–30% to 2024. Under J2919 it has been flat to slightly down from Q2 2024 to Q4 2026 (−6.6%), with volatile quarters.
- **MPA (Depo-Medrol):** mixed. The 40 mg code rose into 2023, but J1010 has been flat to down since 2024.

The data does not link spikes to documented US shortages, except that Solu-Cortef supply constraints in 2023–2025 coincide with continued J1720 increases.

### Cited Findings
**Growth in implied ASP per vial to Q4 2026** (derived from the [CMS ASP files](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files); `asp_growth_summary.csv`)

| Series | 1y (Q4-25→Q4-26) | 3y CAGR (Q4-23→Q4-26) | 5y CAGR (Q4-21→Q4-26) | Since Q1-2016 CAGR | Peak quarter |
|---|---|---|---|---|---|
| HSS J1720, any vial size (constant 2.5/5/10 units) | +8.6% | +9.4% (+31.0% cumulative) | +9.3% (+56.3%) | +11.0% (+208.5%) | 2026-Q4 (latest) |
| MPSS 125 mg-equivalent (J2930 to J2919×25) | +21.4%† | +8.5%‡ | +2.7%‡ | +4.2%‡ | 2024-Q4 ($7.17)‡ |
| MPSS 40 mg (J2920 to J2919×8) | +21.5%† | −16.0%‡ | −13.1%‡ | −3.2%‡ | 2019-Q1 ($4.60) |
| MPA 40 mg/mL (J1030 to J1010×40) | +3.3% | −11.9%‡ | −2.7%‡ | +1.2%‡ | 2023-Q2 ($7.63) |
| MPA 80 mg/mL (J1040 to J1010×80) | +3.3% | −2.9%‡ | −1.6%‡ | +1.6%‡ | 2018-Q3 ($12.75) |

†The 1-year MPSS change is flattered by a trough in Q4 2025: PL $0.210, based on 2Q25 data. On annual averages, J2919 ASP was $0.233 in 2025 and $0.232 in 2026, i.e. flat.
‡These windows cross the April 2024 code change; see Q1 inferences.

**Within-code changes, implied ASP per billing unit** (derived; CMS files)
- **J1720 (100 mg):** $7.08 (Q1 2016) to $21.84 (Q4 2026), +208.6%, CAGR 11.1%. The low was $7.04 in Q2 2016 and the high is the latest quarter. Annual-average ASP went from $7.47 (2016) to $19.82 (2025), a 9-year CAGR of about 11.4%.
- **J2930 (125 mg):** $3.87 (Q1 2016) to $5.55 (Q1 2024), +43.3% (CAGR 4.6%).
  - It peaked at $6.57 in Q3 2018, so the peak-to-last change is −15.5%.
  - Annual-average ASP went from $4.34 (2016) to $5.22 (2023), a CAGR of about 2.7%.
- **J2920 (40 mg):** $2.73 to $3.95, +44.5%, with a peak of $4.60 in Q1 2019 (peak-to-last −14%).
- **J2919 (5 mg):** $0.2575 (Q2 2024) to $0.2406 (Q4 2026), −6.6% (CAGR −2.7%). The range was $0.198 (Q4 2025) to $0.287 (Q4 2024).
- **J1030 (40 mg):** +49.0% from Q1 2016 to Q1 2024, peaking at $7.63 in Q2 2023. **J1040 (80 mg):** +17.6%, peaking at $12.75 in Q3 2018.
- **J1010 (1 mg):** $0.1264 (Q2 2024) to $0.1160 (Q4 2026), −8.2%.

**Quarter-on-quarter moves of 10% or more in the payment limit** (CMS files; `asp_qoq_moves_over_10pct.csv`)
- J1720:
  - +20.1% in Q3 2017 (1Q17 data), from $9.034 to $10.852.
  - +19.2% in Q3 2022 (1Q22 data), from $14.743 to $17.574.
  - There were no 10%+ declines in the whole period.
- J2930:
  - +17.8% in Q3 2016 and +11.5% in Q2 2018.
  - −16.1% in Q4 2020.
  - −12.9% in Q4 2023, then +18.0% in Q1 2024.
- J2920: +12.7% and +11.9% in Q3 and Q4 2016; −19.0% in Q4 2023; +22.0% in Q1 2024.
- J2919: −11.8% in Q1 2025; −18.9% in Q4 2025; +25.7% in Q1 2026; +13.8% in Q4 2026.
- J1020 (20 mg, low volume): erratic, e.g. −67.7% in Q4 2022 and then +209% in Q1 2023. Treat this code as noisy.

**Shortage context found**
- The ASHP shortage page for methylprednisolone acetate (Depo-Medrol and generics) was reportedly dated 13 May 2026 and listed Pfizer Depo-Medrol on shortage because of manufacturing delays. This comes from a search-engine summary; fetching the page returned HTTP 403, so it is unverified. — [ASHP shortage detail id=1173](https://www.ashp.org/drug-shortages/current-shortages/drug-shortage-detail.aspx?id=1173)
- In May 2023 Pfizer obtained FDA approval to extend the use date of 32 lots of the Solu-Cortef 100 mg/2 mL Act-O-Vial by five months beyond the labeled 36-month expiry. That is evidence of a 2023 supply constraint (detail via search summary). — [Pfizer Hospital US, Solu-Cortef emergency date extension, 4 May 2023](https://www.pfizerhospitalus.com/sites/default/files/news_announcements/5-4-23%20Solu-Cortef%20Emergency%20Date%20Extension.pdf)
- Pfizer also ran a Solu-Cortef emergency request form process. — [Pfizer Solu-Cortef Emergency Request Form](https://www.pfizerhospitalus.com/sites/default/files/Solu-Cortef%20Emergency%20Request%20Form.pdf)
- Earlier MPSS disruption: Solu-Medrol was short in 2014 after a Pfizer injectable facility upgrade ran late. Hospira had discontinued all its MPSS products in January 2013 and Bedford Labs had stopped in 2011. — [Outsourcing-Pharma, 20 Feb 2014](https://outsourcing-pharma.com/Article/2014/02/20/Delays-in-upgrading-Pfizer-injectable-facility-causes-shortage)
- The FDA later announced that the Pfizer Solu-Medrol shortage was resolved. The article's date could not be confirmed. — [Pink Sheet](https://pink.pharmaintelligence.informa.com/PS060760/FDA-Announces-Resolution-Of-Pfizer-SoluMedrol-Shortage)
- Canada had a Solu-Cortef 250 mg shortage from 30 September to 18 October 2017, attributed to a demand increase. — [Health Canada drug shortage report 20792](https://healthproductshortages.ca/shortage/20792)

### Inferences
- **MPSS:** the 2016–2018 rise (J2930 +60% from Q1 2016 to Q3 2018) came while there were few generic labelers: only Fresenius Kabi in the crosswalk until Amneal and Sagent were added in Q3–Q4 2017. Erosion from 2019 onward follows the addition of Hikma (2020), Dr. Reddy's (2022) and others. This fits generic competition rather than a shortage spike, but no US shortage documentation for 2016–2018 was found to confirm or rule out a shortage premium.
- **J1720:** the series has no 10%+ declines at all, and each step-up holds. The step-ups (Q3 2017, Q3 2022) look like list-price increases by a sole source rather than temporary shortage spikes. Pfizer's WAC history in Q4 supports this, with +5% to +15% increases in 2025–2026.
- **The Q4 2025 J2919 trough** (2Q25 data) roughly coincides with the Pfizer Solu-Medrol WAC cuts visible between the March and July 2025 disclosures (Q4). The exact effective date of the cuts is unknown, so this is a hypothesis only.

### Gaps
- The ASHP and FDA shortage databases could not be accessed directly (ASHP returned 403), so I could not build a dated US shortage timeline for MPSS and HSS for 2016–2026. Pfizer's April 2025 Solu-Cortef "short-term interruption" notice (recovery expected 3Q 2025) appeared only in a search summary, without a retrievable primary URL.
- 2027 payment limits are not yet published (the January 2027 file is due around December 2026). These will be the first to reflect 3Q26 sales after the Apotex and Zydus HSS entries.

---

## Q3. Which NDCs and labelers map to each code (latest crosswalk and history), and how crowded is each molecule?

### Takeaway
- **HSS:** Pfizer (Solu-Cortef) was the only non-repackager labeler in the J1720 crosswalk from 2016 to Q4 2024.
  - Cipla entered the crosswalk in Q1 2025; its FDA ANDA was approved 5 September 2024.
  - Apotex (ANDA approved 5 February 2026) and Zydus (7 May 2026) entered in Q4 2026.
  - All three generics are **100 mg only**. The 250 mg, 500 mg and 1 g sizes, and the dual-chamber Act-O-Vial format, remain Pfizer-only in the crosswalk.
- **MPSS:** has had 4–5 non-repackager labelers since 2017–2020. In Q4 2026 these are Pfizer, Fresenius Kabi, Hikma, Dr. Reddy's and Civica.
- **MPA:** is the most crowded, with 7 labeler codes (6 companies).

### Cited Findings
**October 2026 ASP NDC-HCPCS crosswalk, labelers by code** ([CMS Oct 2026 crosswalk](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip); full NDC list in `asp_crosswalk_ndcs_oct2026.csv`)
- **J1720 (HSS), 12 NDCs:**
  - Pfizer Inc (Solu-Cortef) has 7 NDCs: 100 mg (00009-0011-03/-04 Act-O-Vial, 00009-0825-01), 250 mg (00009-0013-05/-06), 500 mg (00009-0016-12) and 1 g (00009-0005-01).
  - Cipla USA: 69097-0004-67, 100 mg.
  - Apotex Corp: 60505-6411-00, 100 mg.
  - Zydus Pharmaceuticals (USA): 70710-1907-01, 100 mg.
  - HF Acquisition Co. (HealthFirst), relabeled Solu-Cortef 100 and 250 mg: 51662-1261-01 and -1262-01.
- **J2919 (MPSS), 33 NDCs:**
  - Pfizer Inc (Solu-Medrol) has 12 NDCs covering 40 mg, 125 mg, 500 mg, 1 g and 2 g.
  - Fresenius Kabi USA: 40 mg, 125 mg and 1 g.
  - Hikma: 40 mg, 125 mg, 500 mg and 1 g.
  - Dr. Reddy's: 40 mg, 125 mg, 500 mg and 1 g.
  - Civica: 40 mg and 125 mg.
  - Repackagers: A-S Medication Solutions, Henry Schein and HealthFirst (all Solu-Medrol).
- **J1010 (MPA), 42 NDCs:**
  - Pfizer (Depo-Medrol); Amneal (labeler codes 60219 and 70121); Sandoz; Sagent; Endo USA (Par, 42023); Eugia US.
  - Repackager: A-S Medication Solutions (Depo-Medrol and generic).

**Non-repackager labeler count over time** (Pfizer plus generics; `asp_crosswalk_labeler_counts_by_quarter.csv`; [CMS crosswalks](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files))
- **HSS:** 1 from Q1 2016 to Q4 2024; 2 from Q1 2025 to Q3 2026 (Cipla added); 4 in Q4 2026 (Apotex and Zydus added). A-S Medication Solutions relabeled Solu-Cortef from 2015 to Q4 2017, and HealthFirst from Q4 2023.
- **MPSS:**
  - 2 in 2016 (Pfizer and Fresenius Kabi); Hospira dropped out after Q4 2015.
  - 4 by Q4 2017 (Amneal Biosciences from Q3 2017, Sagent from Q4 2017); 5 from Q2 2020 (Hikma).
  - Amneal and Sagent fall out after Q3 2022, while Dr. Reddy's enters in Q4 2022. That leaves 4 from Q4 2022 to Q2 2026.
  - 5 from Q3 2026 (Civica).
- **MPA:**
  - 3 in 2016 (Pfizer, Teva/Sicor, Sandoz), then 2 in 2017–2020.
  - Additions: Amneal 70121 (Q1 2021), Northstar (Q4 2021), Sagent (Q3 2022), Amneal 60219 (Q1 2023), Endo/Par (Q2 2023), Eugia (Q4 2023). This peaked at 9 labeler codes in Q4 2023 to Q1 2024.
  - Teva/Sicor last appears in Q1 2024 and Northstar in Q4 2024, leaving 7 in Q4 2026.

**FDA application holders** (openFDA Drugs@FDA API; `fda_applications_openfda.csv`) — [openFDA drugsfda HSS query](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22HYDROCORTISONE+SODIUM+SUCCINATE%22&limit=100); [MPSS query](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22METHYLPREDNISOLONE+SODIUM+SUCCINATE%22&limit=100); [MPA query](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22METHYLPREDNISOLONE+ACETATE%22&limit=100)
- **HSS, active ("Prescription") applications:**
  - NDA009866, Pharmacia and Upjohn (Pfizer), approved 27 April 1955: 100 mg, 250 mg, 500 mg and 1 g.
  - ANDA214050, Cipla, approved 5 September 2024: 100 mg only.
  - ANDA219856, Apotex, approved 5 February 2026: 100 mg only.
  - ANDA217191, Zydus, approved 7 May 2026: 100 mg only.
  - All older HSS ANDAs (Hospira, Abbott, Baxter, Abraxis, Watson, and others) are discontinued. The last of them was Hospira's ANDA040666 from 2006.
- **MPSS, active ANDAs:**
  - Fresenius Kabi: ANDA040583 (40 and 125 mg, 2004) and ANDA040612 (1 g, 2004).
  - Sagent: ANDA040888 (all five strengths, 2011).
  - Hikma: ANDA202691 (500 mg and 1 g, 2016) and ANDA203125 (40 and 125 mg, 2022).
  - Amneal: ANDA207549 (40 and 125 mg, 2016).
  - Tianjin Kingyork: ANDA212396 (all five strengths, approved 20 April 2021).
  - Eugia's ANDA207667 is listed as discontinued.
- **MPA, active ANDAs:**
  - Emerge (2005); Sandoz (two, 2009); Sagent (2018); Amneal (2019 and 2023).
  - PH Health (2022); Wilshire (2023); Eugia (2023).
  - Hikma (80 mg/mL, 16 April 2025); Caplin (26 January 2026).
- Secondary pointers: a search summary of an Apotex US product page said its generic HSS launched on 19 June 2026, and a medical database lists a marketing start of 31 July 2025 for Cipla's 100 mg/2 mL product. Neither was fetched (Apotex returned 403), so both are unverified. — [Apotex product page](https://www.apotex.com/products/us/detail.asp?m=71744); [Medthority Cipla HSS label](https://inte.medthority.com/fda/h/hydrocortisone-sodium-succinate/hydrocortisone-sodium-succinate-hydrocortisone-sodium-succinate-100-mg2ml-cipla-usa-inc)

### Inferences
- **Crowding supports the hypothesis.**
  - **HSS:** effectively a Pfizer monopoly for ASP purposes through 2Q24–2Q26 sales. Generics only arrived in 2025–2026 and only at 100 mg.
  - **MPSS:** 4–5 active manufacturers for six-plus years.
  - **MPA:** 6–9 labeler codes.
- **The MPSS crosswalk understates the number of ANDA holders.** Sagent and Amneal still hold active ANDAs but have been absent from the crosswalk since Q3 2022. Possible reasons: they are not marketing, not reporting ASP, or their NDCs are not mapped.
- **Dr. Reddy's MPSS (labeler 43598) is probably supplied under the Tianjin Kingyork ANDA212396**, since it has the same five strengths and entered after the 2021 approval. This is not verified. Civica (72572) is a relabeler-type nonprofit whose source manufacturer is not identified here.
- **The HSS large-vial and DCV formats are the open opportunity.** No ANDA exists for 250 mg, 500 mg or 1 g HSS, nor for any HSS dual-chamber presentation. That gap is directly relevant to a DCV entrant such as Symbiotec. The [Pfizer WAC disclosures](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-CORTEFCTPriceDisclosureShortForm07062026.pdf) show these sizes carry the highest per-vial WAC ($51–$201).

### Gaps
- The crosswalk lists NDCs mapped to codes, not market shares. Labeler-level unit or volume shares need IQVIA, or Medicaid SDUD (another researcher produced `sdud_*.csv` files in the same folder).
- Approval holder versus marketer relationships could not be confirmed with public sources: Kingyork and Dr. Reddy's, Civica's source manufacturer, and Endo/Par.

---

## Q4. What WAC/list and other public prices per vial are available by labeler and strength?

### Takeaway
Pfizer's own WAC disclosures (2024–2026) show the contrast directly:
- **Solu-Cortef list prices rose about 18–29% from July 2024 to July 2026** across all sizes.
- **Solu-Medrol list prices were flat**, apart from cuts of 24–42% on some NDCs in mid-2025.

Retail acquisition cost (NADAC) shows generic MPSS 125 mg at about one-third of the Solu-Medrol price. Generic HSS 100 mg is at about 56% of Solu-Cortef.

### Cited Findings
**Pfizer WAC per vial, from Connecticut prescriber price disclosures** (`pfizer_wac_ct_disclosures.csv`). Sources: [Solu-Cortef 9 Jul 2024](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-CORTEFCTPriceDisclosureShortForm07092024.pdf); [28 Mar 2025](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-CORTEFCTPriceDisclosureShortForm03282025.pdf); [28 Jul 2025](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-CORTEFCTPriceDisclosureShortForm07282025.pdf); [3 Oct 2025](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-CORTEFCTPriceDisclosureShortForm10032025.pdf); [9 Jan 2026](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-CORTEFCTPriceDisclosureShortForm01092026.pdf); [6 Jul 2026](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-CORTEFCTPriceDisclosureShortForm07062026.pdf). Solu-Medrol and Depo-Medrol PDFs follow the same URL pattern with the same dates.

*Solu-Cortef (single-vial WAC, $):*

| Presentation | 9-Jul-24 | 28-Mar-25 | 28-Jul-25 | 3-Oct-25 | 9-Jan-26 | 6-Jul-26 | Change Jul-24→Jul-26 |
|---|---|---|---|---|---|---|---|
| 100 mg vial (plain) | 15.86 | 18.24 | 19.15 | 19.15 | 20.11 | 20.11 | +26.8% |
| 100 mg/2 mL Act-O-Vial | 21.42 | 22.92 | 24.07 | 24.07 | 25.27 | 25.27 | +18.0% |
| 250 mg/2 mL Act-O-Vial | 39.64 | 42.41 | 44.53 | 44.53 | 51.21 | 51.21 | +29.2% |
| 500 mg/4 mL Act-O-Vial | 79.31 | 83.28 | 87.44 | 87.44 | 100.56 | 100.56 | +26.8% |
| 1 g/8 mL Act-O-Vial | 158.57 | 166.50 | 174.83 | 174.83 | 201.05 | 201.05 | +26.8% |

25-pack per-vial WAC (Jul 2026): 100 mg Act-O-Vial $24.81, and 250 mg $48.07 ($1,201.70 per 25).

*Solu-Medrol (per-vial WAC, $):*

| Presentation | 9-Jul-24 | 28-Mar-25 | 28-Jul-25 to 6-Jul-26 |
|---|---|---|---|
| 40 mg/1 mL Act-O-Vial (NDC A) | 6.76 | 6.76 | 5.11 (25-pk $127.84; −24%) |
| 40 mg/1 mL Act-O-Vial (NDC B) | 6.47 | 6.47 | 6.47 (25-pk $161.72) |
| 40 mg/1 mL Act-O-Vial (NDC C, 25-pk $134.23) | n/a | n/a | 5.37 |
| 125 mg/2 mL Act-O-Vial (NDC A) | 10.88 | 10.88 | 8.14 (25-pk $203.44; −25%) |
| 125 mg/2 mL Act-O-Vial (NDC B) | 10.42 | 10.42 | 10.42 (25-pk $260.44) |
| 125 mg/2 mL Act-O-Vial (NDC C, 25-pk $213.61) | n/a | n/a | 8.54 |
| 500 mg/4 mL Act-O-Vial | 47.38 | 47.38 | 47.38 |
| 500 mg/8 mL vial | 24.28 | 24.28 | 24.28 |
| 1 g/8 mL Act-O-Vial | 68.92 | 68.92 | 68.92 |
| 1 g/16 mL vial | 43.98 | 43.98 | 43.98 |
| 1 g/16 mL multi-dose vial | n/a | 43.98 | 25.35 (−42%) |
| 2 g | 108.86 | 108.86 | 108.86 |

*Depo-Medrol (per-vial WAC, $), unchanged from March 2025 to July 2026:*
- 40 mg/mL: 1 mL $11.36; 5 mL $49.29; 10 mL $98.69.
- 80 mg/mL: 1 mL $19.72; 5 mL $98.69.
- 20 mg/mL 5 mL: $35.56.
- One 40 mg/mL 1 mL NDC was listed at $3.99 (25-pk $115.50) in July 2025.
- Sources: [Depo-Medrol 28 Jul 2025](https://cdn.pfizer.com/pfizercom/products/ctprescribers/DEPO-MEDROLCTPriceDisclosureShortForm07282025.pdf); [6 Jul 2026](https://cdn.pfizer.com/pfizercom/products/ctprescribers/DEPO-MEDROLCTPriceDisclosureShortForm07062026.pdf)

Pfizer's disclosure text says these WACs are "Pfizer's published list prices for the products sold to wholesalers, before any discount, rebate, or other price reduction". — [Pfizer Solu-Medrol CT disclosure, 6 Jul 2026](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-MEDROLCTPriceDisclosureShortForm07062026.pdf)

**NADAC, the CMS retail pharmacy survey of acquisition cost, per vial ("EA") or per mL** (`nadac_steroid_injectables_*.csv`). Sources: [data.medicaid.gov NADAC 2026](https://data.medicaid.gov/dataset/fbb83258-11c7-47f5-8b18-5f8e79f7e704); earlier years from the yearly NADAC datasets on data.medicaid.gov.

Latest NADAC as of 21 October 2026:

| Product | Generic or brand | NADAC per vial |
|---|---|---|
| MPSS 125 mg (Hikma 00143-9754-25, Dr. Reddy's 43598-0129-25, Fresenius 63323-0258-03) | Generic | $3.27 |
| Solu-Medrol 125 mg (00009-0047-22) | Brand | $10.04 |
| Solu-Medrol 40 mg (00009-0039-xx) | Brand | $6.28 |
| HSS 100 mg (Cipla 69097-0004-67, Apotex 60505-6411-00, Zydus 70710-1907-01) | Generic | $14.46 |
| Solu-Cortef 100 mg Act-O-Vial (00009-0011-03/-04) | Brand | $25.53 / $24.68 (as of 1 Jul 2026 effective) |
| Solu-Cortef 100 mg vial (00009-0825-01) | Brand | $25.73 |
| Solu-Cortef 250 mg Act-O-Vial (00009-0013-05) | Brand | $51.43 |

Depo-Medrol is priced per mL:
- 40 mg/mL: $6.90 per mL (brand) against $7.49 per mL for Amneal's generic.
- 80 mg/mL: $11.65 per mL (brand) against $11.92 per mL (generic, Amneal).
- Generic 400 mg/10 mL vials (Sandoz, Eugia, Sagent, Endo, Amneal): $5.57 per mL.

**NADAC annual medians, $ per vial**

| Product | 2016 | 2018 | 2019 | 2020 | 2022 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| Solu-Cortef 100 mg vial | 7.44 | 11.12 | 9.64 | 10.32 | 13.12 | 14.78 | 18.27 | 19.50 |
| Solu-Cortef 100 mg Act-O-Vial |  |  | 12.95 | 14.09 | 17.70 | 20.55 | 22.88 | 24.02 |
| Solu-Cortef 250 mg Act-O-Vial |  |  |  |  |  | 37.92 | 42.59 | 48.98 |
| Solu-Medrol 40 mg vial | 3.49 | 4.27 | 4.27 |  |  | 6.25 | 6.23 | 6.28 |
| Solu-Medrol 125 mg vial | 7.68 | 9.40 | 9.40 |  |  | 9.46 | 9.53 | 9.88 |
| Generic MPSS 125 mg |  |  |  |  |  |  | 2.97 | 4.02 |
| Generic HSS 100 mg |  |  |  |  |  |  | 15.10 | 14.91 |

Missing years are years with no NADAC record for that description.

**Other price points**
- drugs.com lists a single Solu-Cortef 100 mg vial at about $25.00, and the Act-O-Vial 25-pack at $24.55 per unit ($613.67). — [drugs.com Solu-Cortef price guide](https://drugs.com/price-guide/solu-cortef)
- GoodRx showed about $12.77 for one 100 mg vial with a coupon; the page was last reviewed June 2024. — [GoodRx Solu-Cortef](https://www.goodrx.com/solu-cortef/dosage)

### Inferences
- **Solu-Cortef ASP is close to WAC.** The J1720 ASP per 100 mg (about $20.00 in Q3 2025, based on 1Q25 data) is 83–104% of the 2025 single-vial WAC: $24.07 for the Act-O-Vial and $19.15 for the plain vial. This implies modest gross-to-net for a sole-source hospital injectable. The large vials' WAC per 100 mg ($17.5–$17.8) also sits below the 100 mg Act-O-Vial's.
- **MPSS blended ASP sits well below brand WAC.** The J2919-implied 125 mg ASP of $6.01 (Q4 2026) is 58–74% of Solu-Medrol 125 mg WAC ($8.14–$10.42), but about 1.8x the generic 125 mg NADAC ($3.27). That is consistent with a market split between brand and low-priced generics.
- **The brand Act-O-Vial (DCV) premium over generic single-chamber vials is large in MPSS** (about 3x at 125 mg on NADAC). Generic HSS is pricing at about 56–58% of brand. This early generic discount is shallower than in MPSS, which suggests HSS pricing still has headroom while there are only three generics at a single strength.
- **The mid-2025 Solu-Medrol WAC cuts** on specific NDCs, likely the GPO/contract-labelled duplicates given the multiple NDCs per strength, look like Pfizer responding to generic MPSS competition. Solu-Cortef took increases in the same period.

### Gaps
- Generic WAC by labeler (Fresenius, Hikma, Dr. Reddy's, Cipla, Apotex, Zydus) is not public. It sits in First Databank and Medi-Span compendia and distributor catalogs (McKesson and Cardinal require login). 340B ceiling prices are not public.
- Pfizer WAC history before July 2024 could not be retrieved: the Wayback Machine CDX connection was reset, and the pfizer.com/ctprescribers index returned 403. Older WAC can be approximated from NADAC (brand) back to 2016.
- No 46brooklyn or Reuters price-increase coverage specific to these molecules was searched in depth, given the tool-call budget.

---

## Q5. What does the Medicare Part B Spending by Drug dashboard show for 2016–2024?

### Takeaway
Fee-for-service Part B spending on these molecules is small and its volumes are falling:
- **HSS:** about $0.44–0.68M per year, 24–49k claims.
- **MPSS:** $1.2–2.9M per year, 0.18–0.36M claims.
- **MPA:** $10–40M per year.

Average spend per unit tracks ASP. HSS spend per unit rose from $7.51 (2016) to $17.99 (2024), while MPSS was flat at about $5–6 per 125 mg-equivalent. The dataset excludes inpatient, Medicare Advantage and bundled (packaged) outpatient claims, so it captures only a sliver of US usage.

### Cited Findings
**Part B spending by HCPCS code** (latest release for each year; `partb_spending_by_hcpcs_2016_2024.csv`). Sources: [data.cms.gov Part B Spending by Drug, Excel reports including historical data, RY26](https://data.cms.gov/sites/default/files/2026-06/Medicare%20Part%20B%20Spending%20by%20Drug-%20Excel%20Reports%20including%20Historical%20Data%20RY26_0.zip); [DY2024 CSV](https://data.cms.gov/sites/default/files/2026-06/6616fc91-eb70-404c-9f27-1448e47a3a73/DSD_PTB_RY26_P06_V10_DYT24_HCPCS-%20260602.csv); [landing page](https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-spending-by-drug)

| Code | Year | Spend ($) | Dosage units | Claims | Beneficiaries | Avg spend per unit ($) |
|---|---|---|---|---|---|---|
| J1720 | 2016 | 410,894 | 54,721 | 49,205 | 14,155 | 7.51 |
| J1720 | 2017 | 511,083 | 53,771 | 48,417 | 13,482 | 9.50 |
| J1720 | 2018 | 594,410 | 50,236 | 45,623 | 12,554 | 11.83 |
| J1720 | 2019 | 597,288 | 48,404 | 43,691 | 12,134 | 12.34 |
| J1720 | 2020 | 590,909 | 45,086 | 40,851 | 10,623 | 13.11 |
| J1720 | 2021 | 642,328 | 45,378 | 41,505 | 10,837 | 14.16 |
| J1720 | 2022 | 680,268 | 43,568 | 40,136 | 10,380 | 15.61 |
| J1720 | 2023 | 441,127 | 26,194 | 24,445 | 8,291 | 16.84 |
| J1720 | 2024 | 480,303 | 26,692 | 24,926 | 7,252 | 17.99 |
| J2930 | 2016 | 1,665,733 | 369,782 | 241,291 | 139,456 | 4.50 |
| J2930 | 2018 | 2,325,195 | 361,205 | 258,010 | 150,545 | 6.44 |
| J2930 | 2019 | 2,272,931 | 363,602 | 263,586 | 154,629 | 6.25 |
| J2930 | 2020 | 1,684,294 | 271,134 | 186,448 | 97,429 | 6.21 |
| J2930 | 2021 | 1,487,852 | 267,477 | 183,879 | 95,003 | 5.56 |
| J2930 | 2022 | 1,609,868 | 280,964 | 194,495 | 105,258 | 5.73 |
| J2930 | 2023 | 1,469,059 | 270,488 | 190,838 | 102,416 | 5.43 |
| J2920 | 2016 | 465,606 | 147,866 | 92,080 | 45,881 | 3.15 |
| J2920 | 2019 | 654,079 | 146,771 | 95,383 | 47,743 | 4.46 |
| J2920 | 2023 | 457,487 | 117,447 | 84,462 | 39,944 | 3.90 |
| J2919 | 2024 (Apr–Dec) | 1,179,260 | 4,151,843 | 177,911 | 92,927 | 0.284 |
| J1030 | 2016 | 13,194,644 | 2,843,544 | 1,970,740 | 1,256,390 | 4.64 |
| J1030 | 2019 | 17,325,671 | 2,772,355 | 1,903,175 | 1,229,581 | 6.25 |
| J1030 | 2023 | 11,371,774 | 1,504,518 | 1,027,484 | 697,932 | 7.56 |
| J1040 | 2016 | 15,599,634 | 1,765,483 | 1,508,596 | 961,779 | 8.84 |
| J1040 | 2019 | 18,949,404 | 1,572,863 | 1,348,685 | 871,234 | 12.05 |
| J1040 | 2023 | 9,720,871 | 832,090 | 699,591 | 470,477 | 11.68 |
| J1010 | 2024 (Apr–Dec) | 10,310,247 | 80,220,708 | 1,297,268 | 890,806 | 0.129 |

The full 2016–2024 series for every code, including J1020, is in the CSV.

**Molecule totals** (derived: units × mg per unit; `partb_spending_by_molecule.csv`)
- **HSS:** spend $0.41M (2016) to $0.68M (2022) to $0.48M (2024). Volume fell from 5.47M mg (2016) to 2.67M mg (2024). Spend per 100 mg went from $7.51 to $17.99.
- **MPSS:** spend $2.13M (2016), $2.94M (2018 peak), $1.93M (2023). Volume fell from 52.1M mg to 38.5M mg (2016 to 2023). Spend per 100 mg-equivalent went from $4.09 (2016) to $5.81 (2018) to $5.00 (2023), and was $5.68 in 2024 (Apr–Dec J2919 only).
- **MPA:** spend $30.3M (2016), $40.1M (2018), $22.1M (2023).
- **Methodology:** the dataset covers Part B fee-for-service claims from physicians, DME suppliers, outpatient hospitals and others. It **excludes** Medicare Advantage beneficiaries ("over 35% of the Medicare population"), claims from critical access hospitals and Maryland hospitals, claims where Medicare is not primary, and "claims with total spending amounts of zero associated with the drug, which is due to bundling in Ambulatory Payment Classification groups". It is limited to HCPCS codes in the most recent year's ASP files. — [Part B Spending by Drug methodology (in RY26 zip)](https://data.cms.gov/sites/default/files/2023-02/DSD_PTB_R22_20230125_Methodology%20508.pdf)
- The DY2024 release omits J2920, J2930, J1020, J1030 and J1040 altogether (codes deleted in 2024). The 2024 figures for MPSS and MPA therefore cover only April–December under J2919 and J1010. — [DY2024 CSV](https://data.cms.gov/sites/default/files/2026-06/6616fc91-eb70-404c-9f27-1448e47a3a73/DSD_PTB_RY26_P06_V10_DYT24_HCPCS-%20260602.csv)
- The DY2024 Manufacturer Summary lists only Pfizer entities for J1720 (Pharmacia-Upjohn, Pfizer US Pharm), so Cipla does not appear in the 2024 Part B claims. For J2919 it lists Pfizer (several labels), Fresenius Kabi/APP, Hikma/West-Ward, Dr. Reddy's and A-S Medication. — [Part B Manufacturer/Drug use xlsx 2024](https://data.cms.gov/sites/default/files/2026-06/Medicare-Part-B-Drug-Dashboard-Manufacturer-Drug_use%20-%20260602.xlsx)

### Inferences
- **Part B FFS is not a market-size proxy for IV steroids.** Most Solu-Medrol and Solu-Cortef use is inpatient (paid under Part A DRGs) or in packaged hospital outpatient settings, all excluded here. These figures are useful for price per unit and directional trends only.
- **Volume declines (2019 to 2023 claims: MPSS −23%, HSS −44%, MPA −46%) are partly mechanical.** Medicare Advantage enrollment, which is excluded, has been rising. The sharp −39% drop in J1720 claims in 2023 coincides with the 2023 Solu-Cortef supply constraint (Q2), which is plausible but unproven.
- **HSS Part B spend per unit grew about 140% from 2016 to 2024** while units halved. Total HSS spend held roughly flat, in line with sole-source price-led revenue.

### Gaps
- No 2025 annual Part B dashboard data is published yet. A quarterly Part B file (Q1 2026) exists ([qddptb CSV](https://data.cms.gov/sites/default/files/2026-07/6d9e955a-d199-42cf-9f73-7e0d93c33b3e/qddptb_r2603_p06_v10_dqt2601_260722.csv)) and is in the raw folder, but I did not extract it.
- There is no public all-payer (hospital inpatient) volume data; IQVIA would be needed.

---

## Q6. Do Part D (and Medicaid) show meaningful spending on these molecules?

### Takeaway
Part D spending is negligible: roughly $0.1–1.0M per product per year, probably emergency or home-use vials. Medicaid gross (pre-rebate) spending is larger: Solu-Medrol is about $21M (2024), and Solu-Cortef about $3.4M plus $0.7M. Medicaid per-unit figures are not usable as prices because the units vary.

### Cited Findings
**Part D Spending by Drug 2024** (`partd_spending_steroid_injectables_2020_2024.csv`; [Part D DY24 CSV](https://data.cms.gov/sites/default/files/2026-06/98218f98-166c-4723-8438-c344a4ef96a6/DSD_PTD_RY26_P04_V10_DY24_BGM.csv))

| Product (manufacturer) | 2024 spend | 2020 spend |
|---|---|---|
| Solu-Cortef PF (Pfizer US Pharm) | $989,905 | $540,590 |
| Solu-Cortef (Pharmacia-Upjohn) | $123,492 | n/a |
| Generic HSS (Cipla) | $4,576 (first appearance) | n/a |
| Solu-Medrol PF (Pfizer) | $329,969 | n/a |
| Solu-Medrol | $18,937 | n/a |
| Generic MPSS, 6 manufacturers (Dr. Reddy's $185,630; App/Fresenius $136,560; Fresenius $91,027; West-Ward/Hikma $18,378; others) | $435,672 total | $582,141 total |
| Generic MPA, 6 manufacturers | $220,458 | n/a |
| Depo-Medrol | $25,135 | n/a |

**Medicaid Spending by Drug 2024** (gross, before rebates; `medicaid_spending_steroid_injectables_2020_2024.csv`; [Medicaid DY24 CSV](https://data.cms.gov/sites/default/files/2026-06/ae1c5e06-957d-42dd-b783-e7fe598c01c9/DSD_MCD_RY26_P06_V20_D24_BGM.csv))

| Product (manufacturer) | 2024 | 2023 |
|---|---|---|
| Solu-Medrol PF | $21.2M | $32.2M |
| Generic MPSS (Fresenius Kabi $3.9M; Dr. Reddy's $4.0M; Hikma $0.57M; APP/Fresenius $0.41M) | $8.95M | $8.3M |
| Solu-Cortef PF | $3.38M | $3.81M |
| Solu-Cortef | $0.70M | n/a |
| Generic HSS (Cipla) | $14,610 | n/a |
| Depo-Medrol | $5.74M | n/a |
| Generic MPA, 9 manufacturers | $3.12M | n/a |

### Inferences
- **Injectables are overwhelmingly Part B / Part A products.** Part D figures are too small to matter for the thesis.
- **Medicaid shows brand dominance in MPSS.** In 2024 Solu-Medrol PF was about 67% of combined MPSS Medicaid gross spend, and about 72% including the non-PF Solu-Medrol line ($1.30M). Both shares are my calculation from the Medicaid CSV: $21.2M PF + $1.30M non-PF + $8.95M generics + less than $0.001M A-Methapred. That is consistent with brand Act-O-Vial (DCV) usage persisting despite generics. The figures are gross of rebates, though, and reflect the Medicaid pharmacy and physician-administered-drug claims mix.
- **Generic HSS penetration was close to zero in 2024 in both Part D and Medicaid.** Cipla appears with less than $15k in each.

### Gaps
- Medicaid "units" are inconsistent: some states report per vial, others per mL. The per-unit spend therefore cannot be converted to a per-vial price, and I have not done so. Labeler-level SDUD unit shares are in the other researcher's `sdud_*.csv` files.

---

## Q7. Does the pricing data support the hypothesis that Medrol is crowded with price erosion while Cortef is less crowded and has held its price?

### Takeaway
Yes, strongly, with a forward-looking caveat:
- **Hydrocortisone sodium succinate** was effectively single-source (Pfizer) through 2024. Its Medicare ASP compounded at about 11% a year from 2016 to 2026, to $21.84 per 100 mg (Q4 2026, an all-time high). Pfizer is still taking WAC increases of 5–15%.
- **Methylprednisolone sodium succinate** has 4–5 active labelers. Its ASP peaked in 2018–19, has since drifted down or sideways, and saw Pfizer WAC cuts in 2025.
- **The caveat:** three 100 mg HSS generics (Cipla in 2024–25; Apotex and Zydus in 2026) have just entered, at roughly a 44% discount at retail. Their effect will only start to show in the 2027 ASP files.

### Cited Findings
- Implied ASP for J1720 went from $7.08 (Q1 2016) to $21.84 (Q4 2026), with no quarter-on-quarter decline of 10% or more. For J2930 it went from $3.87 to a $6.57 peak (Q3 2018) and then $5.55 (Q1 2024). J2919 moved from $0.2575 to $0.2406 (Q2 2024 to Q4 2026). — [CMS ASP pricing files](https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files)
- Non-repackager labelers in the October 2026 crosswalk: HSS 4 (Pfizer, plus Cipla, Apotex and Zydus at 100 mg only); MPSS 5; MPA 7 labeler codes. HSS had 1 from 2016 to Q4 2024. — [CMS Oct 2026 crosswalk](https://www.cms.gov/files/zip/october-2026-ndc-hcpcs-crosswalk-final.zip)
- FDA approvals for HSS generics: Cipla 5 September 2024, Apotex 5 February 2026, Zydus 7 May 2026, all 100 mg only. — [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22HYDROCORTISONE+SODIUM+SUCCINATE%22&limit=100)
- Pfizer WAC from July 2024 to July 2026: Solu-Cortef +18% to +29% across sizes, while Solu-Medrol was flat and three NDCs were cut by 24–42% in mid-2025. — [Pfizer CT disclosures](https://cdn.pfizer.com/pfizercom/products/ctprescribers/SOLU-MEDROLCTPriceDisclosureShortForm07062026.pdf)
- Latest NADAC (October 2026), generic as a share of brand: MPSS 125 mg $3.27 against Solu-Medrol 125 mg $10.04 (33%); HSS 100 mg $14.46 against Solu-Cortef 100 mg $25.5–25.7 (about 56%). — [data.medicaid.gov NADAC 2026](https://data.medicaid.gov/dataset/fbb83258-11c7-47f5-8b18-5f8e79f7e704)

### Inferences
- **The HSS opportunity is narrowing at 100 mg but remains open at 250 mg, 500 mg and 1 g, and in the DCV format.**
  - At 100 mg, three generics are already present and ASP erosion should begin in 2027 files.
  - At 250 mg, 500 mg and 1 g, and for the dual-chamber Act-O-Vial format, no ANDA exists yet according to openFDA, and the crosswalk lists only Pfizer.
  - Those sizes carry list prices of $51–$201 per vial (July 2026 WAC) and an implied ASP of $55–$218 per vial (Q4 2026).
  - A DCV generic of Solu-Cortef 250 mg, 500 mg or 1 g would enter a sole-source, price-rising segment.
- **MPSS generic economics are already commoditized.** The 125 mg generic NADAC is about $3–4 and the blended ASP per 125 mg is about $6. A DCV product would need to compete on the brand Act-O-Vial convenience premium (brand 125 mg about $8–10 WAC) rather than on generic pricing.
- **Expect a mechanical step-down in J1720.** If the October 2026 crosswalk change (250 mg = 3 units) carries into ASP calculations, the per-unit ASP falls in early-2027 files independently of competition. Analysts should not mistake that for generic erosion.

### Gaps
- Unit shares by labeler and GPO contract prices (Vizient, Premier) are not public, so the size of the brand-to-generic switch in hospitals cannot be quantified from public data.
- The ASP impact of the 2026 HSS generic launches cannot be observed until the January and April 2027 payment-limit files (3Q26 and 4Q26 sales).
