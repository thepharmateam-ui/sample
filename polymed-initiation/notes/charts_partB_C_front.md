No files were modified. Every fact ID below was checked against `ledger/facts.jsonl` with `build/lookup.py` and direct ledger reads, and all of them exist. Display values are shown in brackets next to each ID.

## Build and audit rules that shaped these proposals

- **Numeric facts only in charts.** Chart facts need a numeric `value_std`. Ranges such as "5-6" or "290-300" are stored as None, so they can only go in notes or tables.
- **`scale` only works on rupees.** It converts only `Rs mn` values. Raw UN Comtrade USD values need a `/1000000` derived fact, and values in "USD 100 mn" or RMB units need their own rescaling.
- **Title numbers must be traceable.** `verify/audit_numbers.py` flags any number in a title that doesn't match a value shown in the exhibit (bar tips, data-table cells or note tokens) to within 0.51 or 2%. Every title below passes that check.
- **Table cells can't hold loose digits.** A bare digit outside a token is flagged, unless it is a lone row number in column 1 or a whitelisted identifier such as "R1". This is why the heat grid uses R-numbers.
- **Derived formulas have limited inputs.** They can only reference shard facts that match `[A-Z]{1,3}-\d{4}`, so other derived IDs (D-xx-###) and IDs like WR1-#### can't be inputs.
- **Lint.** "Middle East" is an error in prose (use West Asia). "multiple" triggers a warning. Numeric ranges must use a hyphen, not an en dash.

## Proposals, most valuable first (16 charts, 4 tables)

### 1. B4 `b4_us_duty` (column)

- **(a) Where:** `draft/43_B4_export_regimes.md`, section "United States: clearance…". After the `b4_tariffs` table's source comment (line 51), before "Four points follow from the table".
- **(b) Title:** "The extra US duty on Indian medical instruments went from 10% to 50% in 2025 and has been 10% since late February 2026; Chinese syringes and needles have paid at least 100% throughout"
- **(c) Spec:** unit "% on top of MFN duty", dec 0, `label_all`.
  - cats: `["5-Apr-2025","7-Aug-2025","27-Aug-2025","7-Feb-2026","24-Feb-2026","24-Jul-2026"]`
  - Series "India-origin HS 9018, all additional duties": WD-0055 (10%), F-0212 (25%), D-WX-001 (50), F-0212, F-0218 (10%), F-0221 (10%).
  - Series "China-origin syringes and needles, Section 301 duty alone": F-0204 (100%) at every date.
  - **Note:**
    - The MFN duty is F-0227 ("Free").
    - The 18% rate announced in February 2026 was never applied (F-0215).
    - The China series is a floor. The IEEPA reciprocal rate (F-0211, 10%), the Section 122 surcharge (F-0218) and the forced-labour rate (F-0223, 12.5%) stacked on top, and the fentanyl duties are not in the ledger. Needles carry the same rate (F-0205, 100%).
    - The 20-24 Feb 2026 gap between the end of IEEPA and the start of Section 122 is not shown.
  - Use the India-only series if you think the China floor comparison is too lopsided.
- **(d) Derived:** D-WX-001 = F-0212+F-0213 = 50 (%, dec 0). This keeps the series on the Federal Register basis rather than using management's CA-0427 (50%).
- **(e) Redundant:**
  - In "Four points" item 1, the rate numbers CA-0379 (50%) and CA-0077 (10%). Keep the MD's quotes.
  - Item 2's China-versus-India rates move to the note.
  - Risk 3's evidence cell in C1 can shrink to an EXREF.
  - Overlap: A5's `us_tariff` table (India only) already covers this. Its title "from zero to 50% in August 2025" skips the 5-Apr-2025 baseline of 10%.

### 2. C1 `risk_heat` (table)

- **(a) Where:** `draft/50_C1_risks.md`, after the register's source comment (line 30), before "The three risks we weigh most".
- **(b) Title:** "Heat grid: only Chinese price competition in export infusion is rated high on both counts; five risks share the medium-medium cell"
- **(c) Table.** Cells are placed from the register's "H / M" column (first letter = likelihood, second = impact):

| Likelihood (rows) / impact (columns) | Low | Medium | High |
|---|---|---|---|
| High | – | Duty-free Chinese dialysers (R2); labour cost and attrition (R7) | Chinese price competition in export infusion (R1) |
| Medium | US trade policy (R3); West Asia disruption (R13); other-income volatility (R16) | Indian pricing policy (R4); raw-material inflation (R6); currency (R8); acquisition execution (R9); capex execution (R10) | – |
| Low | – | EU MDR certification (R5); related parties (R11); customer concentration and OEM dependence (R12); key-person and succession (R15) | Quality or regulatory action (R14) |

  - Note: "Placement follows the grades in Exhibit [[EXREF:risk_register]]." Optionally relabel the register's "#" column as R1-R16.
- **(e) Redundant:** none. However, the grid exposes a real inconsistency:
  - The register title says trade policy and acquisition execution "rank highest", yet R3 is graded M/L and R9 is M/M.
  - R2 and R7 (both H/M) outrank them.
  - "The three risks we weigh most" leaves out R7.
  - Either regrade or retitle.

### 3. B3 `b3_crisil_cons` (column)

- **(a) Where:** `draft/42_B3_india.md`, "How big is the market?". After the "For Polymed the relevant pool" bullets (line 27).
- **(b) Title:** "CRISIL: India's consumables market jumped in FY21 and has been flat at Rs. 183-195bn since"
- **(c) Spec:** cats FY19-FY24, scale bn, unit "Rs bn", dec 0, `label_all`.
  - Series: D-0413 (Rs. 108.0bn), D-0414 (Rs. 131.0bn), D-0415 (Rs. 189.0bn), D-0416 (Rs. 190.0bn), D-0417 (Rs. 183.0bn), D-0410 (Rs. 195.0bn).
  - **Note:**
    - This is a vendor estimate commissioned for Polymed's QIP document.
    - CAGR D-0411 (13%).
    - FY28 projection `{{D-0418|range}}` (290-300 Rs bn, vendor projection).
    - Polymed's FY23 share was E-0352 (1.9%) on D-0535 (Rs. 3.4bn).
- **(e) Redundant:**
  - Most numbers in the CRISIL bullet on line 25.
  - E-0326 duplicates D-0410; keep one.
  - The prose's "13% annual growth" hides that nearly all of it came in FY20-FY21.

### 4. B2 `b2_global_scale` (hbar)

- **(a) Where:** `draft/41_B2_competitors.md`, after the `b2_global` table comment (line 40).
- **(b) Title:** "BD's revenue is 105 times Polymed's and B. Braun's 53 times; even ICU Medical's consumables arm is 5.4 times"
- **(c) Spec:** unit "x Polymed's FY26 revenue", dec 1, `label_w` 280.

| Category | Fact |
|---|---|
| BD, group (FY Sep-2025) | D-WD-002 (105x) |
| B. Braun, group (CY25) | D-WD-004 (53x) |
| Fresenius Care Enablement (CY25) | D-WD-006 (31x) |
| BD Medication Delivery (FY Sep-2025) | D-WD-003 (22x) |
| Vantive (CY24) | D-WD-009 (22x) |
| Baxter Infusion Therapies (CY25) | D-WD-008 (20x) |
| Teleflex, continuing (CY25) | D-WD-007 (10x) |
| ICU Medical Consumables (CY25) | D-WD-005 (5.4x) |

  - **Note:** converted at WD-0023 (Rs. 90.5/$) and WD-0024 (Rs. 106.1/€), then divided by A-0039 (Rs. 18.8bn). Terumo, Nipro and the Chinese makers are excluded because there is no JPY or RMB reference rate in the sources.
- **(e) Redundant:** the "Size vs Polymed" column of `b2_global` and its table note; the number in "Four points" item 1.

### 5. B3 `b3_bcg_local` (stacked_column)

- **(a) Where:** `draft/42_B3_india.md`, after "Two readings survive the noise" (line 47).
- **(b) Title:** "BCG-KIHT: local manufacturing for India's own market rose from $2bn to $7bn over 2022-2025 while imports stayed at $9bn"
- **(c) Spec:** cats ["2022","2025"], unit "US$ bn", dec 0, `totals`.
  - Series "Imports": A-0169 ($9bn), A-0171 ($9bn).
  - Series "Local manufacturing for domestic demand": A-0170 ($2bn), A-0172 ($7bn).
  - **Note:**
    - CAGRs: A-0173 (1%) for imports, A-0174 (43%) for local manufacturing.
    - Local share rose from A-0176 (~20%) to A-0175 (~45%); the 2035 projection is A-0197 (75%, consultancy projection).
    - The next page of the report gives A-0193 ($8.8bn) and A-0194 ($7.2bn).
    - Do not mix in the BCG and CII series (A-0162 to A-0166).
- **(e) Redundant:** the sentence "BCG expects domestic production to meet A-0197…".

### 6. Front `front_cagr` (hbar)

- **(a) Where:** `draft/00_front.md`, after the 10-point list (line 48), before "Key debates".
- **(b) Title:** "Renal (39%) and India (21%) grew fastest over FY20-FY26; infusion (14%) and the rest of the world (15%) slowest"
- **(c) Spec:** unit "% a year", dec 0.

| Category | Fact |
|---|---|
| Line: renal | CB-0030 (39%) |
| Line: others (incl. acquisitions) | CB-0035 (23%) |
| Line: infusion | CB-0025 (14%) |
| Region: India | CB-0045 (21%) |
| Region: Europe | CB-0050 (20%) |
| Region: rest of world | CB-0055 (15%) |
| Group | CB-0040 (18%) |

  - **Note:** company-stated, from the same slide as [[EXREF:rev_therapy]] and [[EXREF:rev_geo]]. FY26 "others" includes CB-0576 (Rs. 1.2bn) of acquisitions.
- **Why not a mix or geography chart:** A1's `rev_therapy`, `mix_q` and `rev_geo` already show mix over time, and a front geography-share chart would repeat `rev_geo`'s title. Points 3 and 4 should EXREF those exhibits instead.
- **(e) Redundant:** point 4's list of regional shares (CB-0011, CB-0012, CB-0013).

### 7. C2 `c2_ebitda` (line)

- **(a) Where:** `draft/51_C2_dashboard.md`, after the table comment (line 29). Use `"height": 220`.
- **(b) Title:** "Consolidated EBITDA margin has run below standalone since the acquisitions were consolidated, reaching 21.0% against 27.3% in 4QFY26"
- **(c) Spec:** cats 3QFY25-1QFY27, dec 1, `"ymin": 15`.
  - Standalone: CB-1273 (28.1%), CB-0657 (27.6%), CB-0231 (26.5%), CB-1274 (26.7%), CB-1272 (26.8%), CB-0656 (27.3%), CB-0230 (28%).
  - Consolidated: CB-1399 (27.4%), CB-0759 (27.6%), CB-0281 (26.7%), CB-1400 (26.8%), CB-1398 (24.2%), CB-0758 (21%), CB-0280 (24.1%).
  - Optional gross-margin line: CB-1353 (65.5%), CB-0721 (66.4%), CB-0262 (68.4%), CB-1354 (69.4%), CB-1352 (68.4%), CB-0720 (66.7%), CB-0261 (73.4%).
  - **Basis note:** each quarter is taken from the latest deck that reports it. First-reported values differ: CB-2636 (27.1%) against CB-0759 (27.6%); CB-2002 (26.3%) against CB-0281 (26.7%). Guidance CA-0019 (25% to 27%).

### 8. C2 `c2_empcost` (line)

- **(a) Where:** same place as #7.
- **(b) Title:** "Standalone employee cost reached 20.6% of revenue in 1QFY27, the first quarter of Haryana's higher minimum wage, against 17.7% in 1QFY25"
- **(c) Spec:** cats 1QFY25-1QFY27, series D-WX-006 to D-WX-014, dec 1, ymin 15.
  - **Note:** 3QFY26 uses the restated A-0941 (Rs. 840mn) rather than A-1052 (Rs. 852mn) as first reported. The FY26 figure is D-CS-employee_cost-FY26 (18.8%). The wage increase is CA-0024 (35%).
- **(d) Derived** (employee benefits expense / revenue from operations, standalone results):

| ID | Quarter | Formula | Inputs | Value |
|---|---|---|---|---|
| D-WX-006 | 1QFY25 | A-1208/A-1192*100 | Rs. 651mn / Rs. 3.7bn | 17.7 |
| D-WX-007 | 2QFY25 | A-1140/A-1108*100 | Rs. 730mn / Rs. 4.0bn | 18.1 |
| D-WX-008 | 3QFY25 | A-1053/A-1021*100 | Rs. 711mn / Rs. 4.1bn | 17.3 |
| D-WX-009 | 4QFY25 | A-0942/A-0912*100 | Rs. 720mn / Rs. 4.2bn | 17.1 |
| D-WX-010 | 1QFY26 | A-1207/A-1191*100 | Rs. 699mn / Rs. 3.8bn | 18.2 |
| D-WX-011 | 2QFY26 | A-1139/A-1107*100 | Rs. 829mn / Rs. 4.2bn | 19.9 |
| D-WX-012 | 3QFY26 | A-0941/A-0911*100 | Rs. 840mn / Rs. 4.2bn | 20.1 |
| D-WX-013 | 4QFY26 | A-0940/A-0910*100 | Rs. 781mn / Rs. 4.4bn | 17.6 |
| D-WX-014 | 1QFY27 | A-1000/A-0990*100 | Rs. 889mn / Rs. 4.3bn | 20.6 |

- **(e) Redundant:** the dashboard's "Latest" cell for this KPI can move from the FY26 figure to D-WX-014.

### 9. B3 `b3_pli_paid` (column)

- **(a) Where:** after the existing `b3_pli` chart (line 91).
- **(b) Title:** "PLI incentives paid rose to Rs. 1.3bn in FY25, but the Rs. 2.7bn paid since FY23 is 7.8% of the scheme's outlay, and none went to Polymed"
- **(c) Spec:** cats FY23-FY25, scale mn, unit "Rs mn", dec 0.
  - Series: F-0020 (Rs. 368mn), F-0021 (Rs. 987mn), F-0022 (Rs. 1.3bn). These sum exactly to F-0019 (Rs. 2.7bn).
  - **Note:**
    - Outlay F-0008 (Rs. 34.2bn); Nipro received F-0023 (Rs. 349mn).
    - Conflict: the March 2026 release gives F-0024 (Rs. 1.6bn to Dec-2025), lower than the parliamentary answer.
- **(d) Derived:** D-WX-002 = F-0019/F-0008*100 = 7.8. Optional: D-WX-033 = F-0023/F-0019*100 = 13.1 (Nipro's share of payments).
- **(e) Redundant:**
  - The numbers in the "Who has been paid" bullet.
  - `b3_pli`'s title clause about Polymed receiving nothing; keep it in only one of the two titles.

### 10. B3 `b3_import_origin` (table)

- **(a) Where:** after the `b3_trade` chart (line 56).
- **(b) Title:** "China supplies about a fifth of India's imports of dialysis apparatus and other medical instruments, but only 8.5% of its needle, catheter and cannula imports"
- **(c) Table:**

| Line (source, period) | All origins | China | China's share | Malaysia | Malaysia's share |
|---|---|---|---|---|---|
| HS 901890, incl. dialysers (UN Comtrade, 2025) | F-0160 ($1.3bn) | F-0161 ($268.6mn) | D-WX-024 (20.6) | F-0162 ($30.1mn) | D-WX-029 (2.3) |
| HS 90189031 (TradeStat, FY26) | F-0192 ($112.39mn) | F-0193 ($23.21mn) | D-WX-025 (20.7) | F-0194 ($13.74mn) | D-WX-028 (12.2) |
| HS 901839 (UN Comtrade, 2025) | F-0163 ($392.2mn) | F-0164 ($33.3mn) | D-WX-026 (8.5) | – | – |

  - **Note:**
    - HS 90189031 sits inside HS 901890.
    - All devices, Apr-Feb FY26: D-WX-027 (16.0) = F-0051/F-0050 ($1.4bn / $9.0bn); CRISIL's E-0336 (16%) agrees.
    - Germany is the largest origin of HS 90189031: F-0195 ($45.8mn).
    - TradeStat FY26 for HS 901839: China F-0202 ($30.46mn) of F-0203 ($397.93mn).
- **(e) Redundant:** the CRISIL sentence on China's E-0336 share (line 47).

### 11. B2 `b2_india_exports` (hbar)

- **(a) Where:** after `b2_india_scale` (line 100).
- **(b) Title:** "Polymed exported 69% of its FY23 revenue, more than any maker in CRISIL's comparison; the Indian arms of BD and B. Braun exported 15.9% and 23.1%"
- **(c) Spec:** dec 1.
  - cats: Poly Medicure, SMT, Healthium, B. Braun India, HMD, BD India.
  - Series: D-0506 (69%), D-0510 (62.2%), D-0500 (44.6%), D-0496 (23.1%), D-0502 (20.8%), D-0498 (15.9%).
  - E-0349 duplicates D-0502.
- **(e) Redundant:**
  - The "Export shares on CRISIL's basis" sentence in `b2_india_scale`'s note.
  - The export shares in "Four points" item 2.
  - This chart also backs up the existing chart's title claim, which the revenue chart alone doesn't show.

### 12. B4 `b4_india_share` (hbar)

- **(a) Where:** `draft/43_B4_export_regimes.md`, after the intro paragraph (line 3).
- **(b) Title:** "India supplies 1.1-1.7% of the medtech imports of Europe and the Americas, 4.3% in West Asia and Africa and 0.6% in Asia-Pacific"
- **(c) Spec:** dec 1. Source is BCG-KIHT 2025, read visually from the annual report chart.

| Category | Fact |
|---|---|
| West Asia and Africa | A-0215 (~4.3%) |
| Europe | A-0211 (~1.7%) |
| Latin America and Caribbean | A-0217 (~1.6%) |
| America (as labelled in source) | A-0213 (~1.1%) |
| Asia-Pacific excl. India | A-0209 (~0.6%) |

  - **Note:** regional import market sizes are A-0216 ($24bn), A-0212 ($79bn), A-0218 ($16bn), A-0214 ($77bn) and A-0210 ($96bn); India's exports were A-0177 ($4bn).

### 13. B3 `b3_duty` (table)

- **(a) Where:** after the "Taxes and duties" paragraph (line 95).
- **(b) Title:** "In renal, taxes favour the importer: finished dialysers enter at 0% duty and 5% GST while Polymed pays duty on materials and 18% GST on inputs, per management"
- **(c) Rows (levy, rate, basis):**

| Levy | Rate | Basis |
|---|---|---|
| Duty and GST on dialysers via ASEAN | CA-0178 ("0% duty, only 5% GST") | Management |
| Customs duty on dialysis products, non-FTA | CC-0523 (7.5%); raised from nil per CC-0177 (7.5%) | Management |
| Health cess on HS 9018-9022 imports | F-0099 (5%) | Statute |
| Customs duty on Polymed's raw materials | WM-0062 (2.5%) | Management |
| GST on finished dialysers | WM-0060 (5%) | Management |
| GST on Polymed's inputs | WM-0061 (18%) | Management |
| GST on devices from 22-Sep-2025 | F-0096 (12% to 5%) | Statute |
| GST on certain apparatus from 22-Sep-2025 | F-0097 (18% to 5%) | Statute |
| Cap on annual MRP increases | F-0067 (10%) | Statute |

  - WB-0045 and WB-0046 duplicate WM-0062 and WM-0061. CRISIL's E-0339 (5-18%) predates the GST cut.
- **(e) Redundant:** the rates in the "Taxes and duties" paragraph, and the zero-duty clause on line 105.

### 14. B2 `b2_china_overseas` (hbar)

- **(a) Where:** after the "three forces" list (line 66).
- **(b) Title:** "Chinese makers still earn most of their revenue at home: overseas sales were 22-35% of 2025 revenue at Sanxin, Weigao and KDL, against 69% outside India for Polymed"
- **(c) Spec:** dec 0.
  - Series: D-WX-005 (Polymed, FY26), D-WA-024 (KDL, 35%), D-WX-003 (Weigao), D-WX-004 (Sanxin).
- **(d) Derived:**
  - D-WX-003 = E-0266/E-0265*100 = 27. Inputs: RMB 3.6bn / RMB 13.4bn. This matches Weigao's disclosed E-0268 (27%).
  - D-WX-004 = E-0393/(E-0391*10000)*100 = 22. Inputs: 36,884.6 RMB 10k / RMB 1.6bn. The ledger tags E-0393 as the renal segment, but its snippet is Sanxin's total overseas revenue.
  - D-WX-005 = (CB-0039-CB-0044)/CB-0039*100 = 69. Inputs: Rs. 18.8bn and Rs. 5.8bn. This equals CB-0084 (69%).

### 15. B5 `b5_us_imports` (table)

- **(a) Where:** after `b5_syringes` (line 79).
- **(b) Title:** "In 2025 India supplied 1.0% of US syringe imports and 0.5% of US needle, catheter and cannula imports; China and Malaysia each supplied over 4% of the latter"
- **(c) Table:**

| Origin | Syringes (HS 901831), 2025 | Share | Needles, catheters, cannulas (HS 901839), 2025 | Share |
|---|---|---|---|---|
| All origins | F-0170 ($1.5bn) | – | F-0177 ($10.4bn) | – |
| China | F-0173 ($126.0mn) | D-WX-021 (8.2) | F-0178 ($467.8mn) | D-WX-022 (4.5) |
| Malaysia | – | – | F-0181 ($431.8mn) | D-WX-023 (4.2) |
| India | F-0176 ($14.8mn) | D-WX-020 (1.0) | F-0180 ($52.4mn) | D-WA-029 (0.5%) |

  - **Note, 2024 values:** India F-0175 ($930k) and F-0179 ($45.2mn); China F-0172 ($170.5mn); all origins F-0169 ($1.3bn).
- **(e) Redundant:** the "Total US syringe imports" clause in `b5_syringes`'s note. A4.1 (out of scope) repeats the HS 901839 numbers in prose.

### 16. B4 `b4_hs_exports` (column)

- **(a) Where:** after the paragraph on line 80, before `b4_dest`.
- **(b) Title:** "India's exports of needles, catheters and cannulas rose from $434.5mn in 2023 to $525.9mn in 2025, and its syringe exports to $71.2mn"
- **(c) Spec:** cats 2023-2025, unit "US$ mn", dec 1.
  - Series HS 901839: D-WX-015, D-WX-016, D-WD-026 ($525.9mn).
  - Series HS 901831: D-WX-017, D-WX-018, D-WX-019.
  - **Note:** TradeStat shows FY26 at F-0182 ($512.33mn), i.e. flat. US-bound values: F-0135 ($39.8mn), F-0136 ($49.1mn), D-WD-018 ($54.8mn).
- **(d) Derived:**
  - D-WX-015 = F-0132 ($434.5mn)/1000000 = 434.5
  - D-WX-016 = F-0133 ($482.4mn)/1000000 = 482.4
  - D-WX-017 = F-0145 ($52.8mn)/1000000 = 52.8
  - D-WX-018 = F-0146 ($59.8mn)/1000000 = 59.8
  - D-WX-019 = F-0147 ($71.2mn)/1000000 = 71.2
- **(e) Redundant:** the "were D-WD-026 in 2025" clause.

### 17. C2 `c2_growth` (line)

- **(a) Where:** same place as #7.
- **(b) Title:** "Renal growth slowed from 46.2% to -3.8% over five quarters while infusion recovered to 11.1%"
- **(c) Spec:** cats 1QFY26-1QFY27.
  - Consolidated: CB-1979 (4.8%), CB-1632 (5.7%), CB-1336 (16.4%), CB-0708 (21.3%), CB-0255 (30.3%).
  - Domestic: CB-1964 (20.1%), CB-1587 (16.9%), CB-1467 (16.2%), CB-0599 (25%), CB-0308 (16.2%).
  - Infusion: CB-2052 (-1.7%), CB-1819 (-2.4%), CB-1527 (5%), CB-0866 (1.9%), CB-0345 (11.1%).
  - Renal: CB-2055 (46.2%), CB-1827 (18.1%), CB-1535 (15.1%), CB-0872 (21.3%), CB-0349 (-3.8%).
  - **Note:** organic growth was CB-0319 (12.4%). Drop the domestic line if you want to avoid repeating A3's `q_table`.

### 18. B3 `b3_crisil_segments` (stacked_column)

- **(a) Where:** after the `b3_size` table comment (line 22).
- **(b) Title:** "CRISIL: consumables were Rs. 195bn of India's device market in FY24, behind equipment at Rs. 538bn"
- **(c) Spec:** cats FY19, FY24; scale bn; dec 0; `totals`.

| Segment | FY19 | FY24 |
|---|---|---|
| Equipment | D-0428 (Rs. 306.0bn) | D-0401 (~Rs. 538.0bn) |
| Consumables | D-0413 (Rs. 108.0bn) | D-0410 (Rs. 195.0bn) |
| Implants | D-0424 (Rs. 41.0bn) | D-0420 (Rs. 85.0bn) |
| IVD | D-0426 (Rs. 46.0bn) | D-0430 (Rs. 82.0bn) |

  - **Note:** the segments sum to D-0394 (Rs. 501.0bn) for FY19. For FY24 they sum to the bottom of D-0390 (900-915 Rs bn).
  - FY20-FY23 segment values are printed on PD24 pp.135-138 (visible in these facts' snippets) but have not been extracted. Extracting them would allow a full FY19-FY24 stack.

### 19. Appendix `appr_us_counts` (hbar, 2 series)

- **(a) Where:** `draft/96_appendix_approvals.md`, after the "What the list shows" bullets (line 55).
- **(b) Title:** "The FDA database holds more 510(k)s than the company counts: 6 against 4 for Polymed, 11 against 10 for Citieffe, and PendraCare's 4 are not counted"
- **(c) Spec:**
  - Series "Company count (May-2026 presentation)": CB-1095 (4), CB-1097 (10), "-", CB-1099 (1).
  - Series "FDA database": D-0876 (6), D-0877 (11), D-0878 (4), D-0879 (1).
  - **Note:** CB-0093 (15) against D-WE-001 (22), a gap of D-WE-002 (7).
- **(e) Redundant:** the numbers in the "The count" and "Reconciling the two" bullets.

### 20. B1 `b1_rebates` (column)

- **(a) Where:** after the `b1_price` table comment (line 139).
- **(b) Title:** "Polymed's rebates and discounts rose to Rs. 116mn in FY26 from Rs. 73mn in FY25, still under 1% of standalone revenue"
- **(c) Spec:** series A-0824 (Rs. 53mn), A-0480 (Rs. 73mn), A-0479 (Rs. 116mn); scale mn.
- **(d) Derived:**
  - D-WX-030 = A-0824/A-0733*100 = 0.4 (denominator Rs. 13.1bn)
  - D-WX-031 = A-0480/A-0441*100 = 0.5 (denominator Rs. 16.0bn)
  - D-WX-032 = A-0479/A-0440*100 = 0.7 (denominator Rs. 16.6bn)
  - Leave out the FY23 figure D-0302: it is tagged "consolidated".
- **(e) Redundant:** the rebates cell in `b1_price`. A4.1's "Rebates are rising" bullet already has these numbers.

**New derived file.** Put D-WX-001 to D-WX-033 in a new `ledger/derived_WX.py` using the `D-WX-` prefix, so none of them collides with the existing D-WD-026. All values above were recomputed on standardized ledger values.

## Dashboard: KPIs with at least 4 quarterly points in the ledger

The dashboard table can't hold in-cell sparklines. Use #7, #8 and #17 as small charts below the table instead.

- **Four or more points on one basis:**
  - Consolidated reported growth: 7 quarters (3QFY25-1QFY27, including CB-2897 at 24.9% and CB-2593 at 16.6%).
  - Domestic growth: 5 quarters.
  - Infusion growth: 5 quarters.
  - Renal growth: 5 quarters.
  - Consolidated gross margin: 11 quarters.
  - Standalone EBITDA margin: 9 quarters (1Q and 2QFY25 missing).
  - Consolidated EBITDA margin: 14 quarters.
  - Employee cost ratio: 9 quarters, derived.
- **Close, but needs work:**
  - Standalone growth has 5 deck points with gaps: CB-2888 (28.1%), CB-2688 (16.6%), CB-1218 (1.9%), CB-0612 (5.2%), CB-0198 (12.3%). Adding (A-1191/A-1192-1)*100 = 4.5 and (A-1107/A-1108-1)*100 = 3.5 fills the gaps.
  - Europe and RoW have 5 reported points each, but the basis changes in 3QFY26 when acquisitions are consolidated. The organic figures exist only for 1QFY27 (CB-0324, CB-0329).
  - Infusion share has 9 points but is restated between decks: 1QFY26 is CB-2059 (63%), CB-1844 (62%) or CB-0364 (58%) depending on the deck.
- **Fewer than 4 points:**
  - Organic growth (1 point).
  - West Asia growth (1).
  - Machines placed (annual).
  - Cardiology revenue (2: CB-0351 at Rs. 29mn, CB-0350 at Rs. 286mn).
  - Orthopaedics revenue (1).
  - Cash conversion cycle (annual).
  - QIP capex (2: A-1106 at Rs. 353mn, A-0584 at Rs. 620mn). Total QIP use has 6 points (B-0820 to B-0826) and could serve as a proxy.
  - Vitromed job work (annual).
  - Stents: points are irregular and already charted in A4.8's `card_stents`.

## Files and topics with no worthwhile candidate

- **`draft/53_C4_channel_checks.md`:** the table is a qualitative plan. A table of starting readings for the checks would only repeat `b3_dial`, the appendix and `b4_freight`. Separately, row 7 has the wrong HS code: 901839 covers needles, catheters and cannulas, while dialysers are HS 90189031.
- **B1, apart from #20:**
  - The MRP payment-mix series has only two numeric points (CC-0205 at 75%, CC-0206 at 50%).
  - Price increases, government share and discounts to the multinationals are ranges or text.
  - The BD regional price example is already in A4.1's `inf_price` table.
- **B5, apart from #15:**
  - Labour costs for China, the US and Europe are ranges (E-0185, WD-0017, WD-0018), so they can't be charted.
  - The two safety-share estimates come from conflicting vendors (E-0358 at 62%, E-0361 at 30.3%).
- **EU MDR certificate counts:** the ledger has no EU-wide count, only F-0236 (51 notified bodies). Polymed's own counts (CC-0409, CB-2118 at 89, CA-0377 at 75, CB-1102 at 82) are on different bases, so they should stay in the `appr_eu_timeline` table. A stacked chart of EU approvals and pipeline by entity would repeat the A5, A6 and appendix tables.
- **PMNDP:** the only series is two points (F-0076, F-0077), and it is already covered in A4.3 and `b3_demand`. A chart of machines needed against installed would mix F&S, government and management sources.
- **Front, second chart:** a mix or geography chart would repeat the key-facts tiles and A1's charts.