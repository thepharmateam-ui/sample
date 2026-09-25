I have 18 exhibits for you: 14 charts and 4 tables, ranked by value. All 18 are fully specified and checked; nothing was edited.

**How I checked**
- Every fact ID below was looked up in the ledger, and its display value is shown next to it. Every value used in a chart is numeric.
- **New formulas can't reuse old derived facts.** `build/reconcile.py` only resolves references shaped like `A-0001`, so a formula can't point at `D-CS-*` or `D-M-*` facts. Every new formula below is written over the underlying facts. I suggest putting them in a new `ledger/derived_WI.py` as `D-WI-001` to `D-WI-039`. Their values were computed the way `reconcile.py` computes them (all amounts converted to Rs mn first).
- **Chart options match the renderer** (`build/svgcharts.py`): `ymin` works on line charts only, `totals` on stacked columns only. A line chart draws straight across a missing point, so no line series below has a gap in the middle; the one gap is in a column chart.

## Ranked index

| # | File (`/home/user/sample/polymed-initiation/draft/`) | id | Type |
|---|---|---|---|
| 1 | `12_A3_fy26_reset.md` | `q_growth` | line |
| 2 | `30_A5_geographies_entities.md` | `geo_hist` | stacked_column |
| 3 | `32_A7_drivers.md` | `q_margin` | line |
| 4 | `34_A9_governance.md` | `inst_holding` | line |
| 5 | `11_A2_business_model.md` | `export_inc` | column |
| 6 | `11_A2_business_model.md` | `labour_cost` | stacked_column |
| 7 | `11_A2_business_model.md` | `wc_days` | **table** |
| 8 | `34_A9_governance.md` | `md_pay_pat` | line |
| 9 | `12_A3_fy26_reset.md` | `fy27_guide` | **table** |
| 10 | `31_A6_manufacturing_rnd.md` | `util_hist` | line |
| 11 | `34_A9_governance.md` | `oi_pbt` | column |
| 12 | `31_A6_manufacturing_rnd.md` | `headcount` | column |
| 13 | `11_A2_business_model.md` | `vol_price` | **table** |
| 14 | `33_A8_moat.md` | `peer_export` | hbar |
| 15 | `30_A5_geographies_entities.md` | `india_channel` | **table** |
| 16 | `34_A9_governance.md` | `qip24_pace` | column |
| 17 | `10_A1_revenue.md` | `cagr_bars` | hbar |
| 18 | `34_A9_governance.md` | `vitromed_hist` | stacked_column |

None of these ids is already in use.

---

## 1. A3 `q_growth` (line)
- **(a) Where:** under "## A3 The FY26 reset…". Insert after the `q_rev` chart (ends line 21), before "### What happened, quarter by quarter" (line 23).
- **(b, c) Spec:**
```
{"id":"q_growth","type":"line","title":"The Indian company's growth fell from 28% to 2-5% a quarter through FY26 and recovered to 12% in 1QFY27; acquisitions lifted the consolidated rate from 3QFY26","cats":["3QFY25","4QFY25","1QFY26","2QFY26","3QFY26","4QFY26","1QFY27"],"unit":"% yoy","dec":1,"series":[{"name":"Consolidated, reported","facts":["CB-2897","CB-2593","CB-1979","CB-1632","CB-1336","CB-0708","CB-0255"]},{"name":"Standalone (Poly Medicure Ltd)","facts":["CB-2989","CB-2688","D-WI-001","D-WI-002","CB-1218","CB-0612","CB-0198"]}],"note":"Growth as reported in each quarter's presentation; standalone 1QFY26 and 2QFY26 are our calculation from the quarterly results. Standalone excludes every foreign subsidiary. PendraCare was consolidated from 23-Sep-2025 and Citieffe from 7-Nov-2025. Consolidated organic growth, excluding both, was {{D-WI-003}} in 4QFY26 (our calculation on the company's organic revenue of {{CB-0575}}) and {{CB-0319}} in 1QFY27."}
```
- **Checks:**
  - Consolidated: CB-2897 24.9% · CB-2593 16.6% · CB-1979 4.8% · CB-1632 5.7% · CB-1336 16.4% · CB-0708 21.3% · CB-0255 30.3%
  - Standalone: CB-2989 28.1% · CB-2688 16.6% · D-WI-001 4.5% (new) · D-WI-002 3.5% (new) · CB-1218 1.9% · CB-0612 5.2% · CB-0198 12.3%
  - Note: D-WI-003 6.5% (new) · CB-0575 Rs. 4.7bn · CB-0319 12.4%
- **(d) New formulas:**
  - D-WI-001 `(A-1191/A-1192-1)*100`, inputs Rs. 3.8bn and Rs. 3.7bn
  - D-WI-002 `(A-1107/A-1108-1)*100`, inputs Rs. 4.2bn and Rs. 4.0bn
  - D-WI-003 `(CB-0575/CB-0705-1)*100`, inputs Rs. 4.7bn and Rs. 4.4bn
- **(e) Can be trimmed:**
  - Line 4: "Standalone revenue grew only ~{{CA-0093}}".
  - Line 14: "Standalone revenue grew {{CB-0198}}".
  - The `q_table` "yoy" column, since it is now plotted.

## 2. A5 `geo_hist` (stacked_column)
- **(a) Where:** "### Where the revenue comes from". Insert after the two-bullet list (lines 20-22), before the `geo_outside` chart (line 24).
- **(b, c) Spec:**
```
{"id":"geo_hist","type":"stacked_column","title":"Exports from the Indian plants more than doubled over FY21-FY25 and then fell 3% in FY26; the subsidiaries' sales tripled with the acquisitions","cats":["FY21","FY22","FY23","FY24","FY25","FY26"],"scale":"bn","unit":"Rs bn","dec":1,"series":[{"name":"India","facts":["B-0419","D-0287","D-0279","D-0278","A-0473","A-0647"]},{"name":"Exports from India","facts":["B-0420","D-0288","D-0282","D-0281","A-0475","A-0648"]},{"name":"Foreign subsidiaries","facts":["B-0421","D-0289","D-0285","D-0284","A-0650","A-0649"]}],"totals":true,"note":"Sale of products by customer location, from the consolidated revenue notes (FY22-FY24 as reproduced in the Aug-2024 placement document). Excludes other operating revenue such as export incentives, so totals fall short of revenue from operations. FY25 domestic and export sales are from the standalone note, which the consolidated note matches. FY21 exports are after intra-group eliminations ({{B-0418}} before). In FY26 exports fell {{D-WC-045|abs}} while the subsidiaries' sales rose {{D-WC-060}} (our calculations)."}
```
- **Checks:**
  - India: B-0419 Rs. 2.3bn · D-0287 Rs. 3.0bn · D-0279 Rs. 3.4bn · D-0278 Rs. 4.1bn · A-0473 Rs. 4.8bn · A-0647 Rs. 5.8bn
  - Exports: B-0420 Rs. 5.1bn · D-0288 Rs. 5.7bn · D-0282 Rs. 7.2bn · D-0281 Rs. 8.9bn · A-0475 Rs. 11.0bn · A-0648 Rs. 10.7bn
  - Subsidiaries: B-0421 Rs. 389mn · D-0289 Rs. 433mn · D-0285 Rs. 472mn · D-0284 Rs. 685mn · A-0650 Rs. 680mn · A-0649 Rs. 2.1bn
  - Note: B-0418 Rs. 5.1bn · D-WC-045 -3.2% · D-WC-060 213%
  - For the title: exports rose 2.16x from FY21 to FY25; subsidiaries rose 3.13x in FY26.
- **(d) New formulas:** none.
- **(e) Can be trimmed:**
  - Line 3: "FY26 split the two apart: … fell {{D-WC-045|abs}} … rose {{D-WC-060}}".
  - The `geo_outside` note's "Total outside India rose {{D-WC-061}} to {{A-0702}}".

## 3. A7 `q_margin` (line)
- **(a) Where:** "### Margin drivers, ranked". Insert after the paragraph at line 31 ("The consolidated margin is lower…"), before the `margin_drivers` table (line 33).
- **(b, c) Spec:**
```
{"id":"q_margin","type":"line","title":"The standalone margin held at 26.5-28% through the acquisitions; the consolidated margin fell to 21% in 4QFY26 and was back only to 24% in 1QFY27","cats":["3QFY25","4QFY25","1QFY26","2QFY26","3QFY26","4QFY26","1QFY27"],"unit":"Operating EBITDA margin, %","dec":1,"ymin":15,"series":[{"name":"Standalone","facts":["CB-1273","CB-0657","CB-0231","CB-1274","CB-1272","CB-0656","CB-0230"]},{"name":"Consolidated","facts":["CB-1399","CB-0759","CB-0281","CB-1693","CB-1398","CB-0758","CB-0280"]}],"note":"Operating EBITDA excluding other income, each quarter as last shown in the presentations (so 4QFY25 consolidated is the restated figure, against {{CB-2636}} first reported). Management says 3QFY26 excludes acquisition-related costs; 4QFY26 includes the ~{{CA-0120}} one-off in a foreign subsidiary. In 1QFY27 consolidated gross margin was {{CB-0261}} against {{CB-0213}} standalone: the acquired businesses add gross margin but not yet EBITDA margin."}
```
- **Checks:**
  - Standalone: CB-1273 28.1% · CB-0657 27.6% · CB-0231 26.5% · CB-1274 26.7% · CB-1272 26.8% · CB-0656 27.3% · CB-0230 28%
  - Consolidated: CB-1399 27.4% · CB-0759 27.6% · CB-0281 26.7% · CB-1693 26.8% · CB-1398 24.2% · CB-0758 21% · CB-0280 24.1%
  - Note: CB-2636 27.1% · CA-0120 Rs. 90mn · CB-0261 73.4% · CB-0213 71.5%
  - I started at 3QFY25 because standalone margins for 1QFY25 and 2QFY25 are not in the ledger.
- **(d) New formulas:** none.
- **(e) Can be trimmed:**
  - The numbers in line 31.
  - "while consolidated EBITDA margin was {{CB-0280}}" in row 1 of `margin_drivers`.

## 4. A9 `inst_holding` (line)
- **(a) Where:** "### Shareholding…". Insert after the "three consequences" list (lines 76-79), before "Promoter shares carried no pledge" (line 81).
- **(b, c) Spec:**
```
{"id":"inst_holding","type":"line","title":"Foreign portfolio investors have halved their stake in a year to under 6%, while domestic mutual funds have more than doubled theirs since 2023 to nearly 10%","cats":["Sep-2023","Jun-2024","Jun-2025","Sep-2025","Dec-2025","Mar-2026","Jun-2026"],"unit":"% of equity","dec":1,"series":[{"name":"Foreign portfolio investors","facts":["CC-0834","D-0340","CB-2081","CB-1916","CB-1571","CB-1013","CB-0370"]},{"name":"Mutual funds","facts":["CC-0833","D-0338","CB-2078","CB-1913","CB-1570","CB-1012","CB-0369"]}],"note":"Quarter-end holdings as shown in the investor presentations; Jun-2024 from the Aug-2024 placement document, before the QIP (institutions went from {{CB-3239}} to {{CB-3240}} on the QIP). Dates are unevenly spaced. Insurance companies held {{CB-0371}} and AIFs {{CB-0372}} at Jun-2026, against {{D-0341}} and {{D-0339}} at Jun-2024."}
```
- **Checks:**
  - FPI: CC-0834 14.5% · D-0340 9.9% · CB-2081 11.4% · CB-1916 9.8% · CB-1571 9.4% · CB-1013 5.9% · CB-0370 5.6%
  - Mutual funds: CC-0833 4.0% · D-0338 6.3% · CB-2078 7.3% · CB-1913 8% · CB-1570 8.1% · CB-1012 8.8% · CB-0369 9.6%
  - Note: CB-3239 19.3% · CB-3240 23.6% · CB-0371 3.0% · CB-0372 3.5% · D-0341 2.3% · D-0339 0.7%
  - Insurance and AIFs are in the note rather than plotted, because their end labels (3.0 and 3.5) would overlap.
- **(d) New formulas:** none.
- **(e) Can be trimmed:** nothing strictly. The "Public institutions … {{D-M-015}}" bullet (line 78) could point to the exhibit.

## 5. A2 `export_inc` (column)
- **(a) Where:** "### Costs and margins…". Insert after the "Export incentives." paragraph (line 145), before "### Working capital" (line 147).
- **(b, c) Spec:**
```
{"id":"export_inc","type":"column","title":"Export incentives fell by three-quarters as MEIS was phased out, and at Rs. 133mn in FY26 are still below FY19's Rs. 167mn on exports 2.8 times as large","cats":["FY13","FY16","FY19","FY20","FY21","FY22","FY23","FY24","FY25","FY26"],"scale":"mn","unit":"Rs mn","dec":0,"series":[{"name":"Export incentives (standalone)","facts":["B-0096","B-0185","B-0296","B-0369","B-0423","B-0481","B-0542","B-0606","A-0470","A-0469"]}],"label_all":true,"note":"Other operating revenue in the standalone accounts; FY25-FY26 are labelled 'export and other incentives' and the RoDTEP/drawback split is not given. Incentives equalled {{D-WI-004}} of foreign-exchange earnings in FY19, {{D-WI-005}} in FY22 and {{D-WI-006}} in FY26, and FX earnings in FY26 were {{D-WI-007}} their FY19 level (our calculations). Management: MEIS was {{CC-0001}} in FY19, {{CC-0002}} in FY20 and {{CC-0003}} from 1-Jan-2021; RoDTEP was {{CC-0098}} in Nov-2021."}
```
- **Checks:**
  - Series: B-0096 Rs. 32mn · B-0185 Rs. 40mn · B-0296 Rs. 167mn · B-0369 Rs. 157mn · B-0423 Rs. 77mn · B-0481 Rs. 42mn · B-0542 Rs. 50mn · B-0606 Rs. 79mn · A-0470 Rs. 126mn · A-0469 Rs. 133mn
  - Note: CC-0001 4% · CC-0002 2% · CC-0003 0% · CC-0098 0.5%
- **(d) New formulas:**
  - D-WI-004 `B-0296/B-0298*100` = 4.3%
  - D-WI-005 `B-0481/B-0484*100` = 0.8%
  - D-WI-006 `A-0469/A-0419*100` = 1.2%
  - D-WI-007 `A-0419/B-0298` = 2.8x
  - Inputs: B-0298 Rs. 3.9bn, B-0484 Rs. 5.4bn, A-0419 Rs. 10.7bn.
- **(e) Can be trimmed:** the first sentence of line 145, which compares {{A-0272}} (Rs. 133mn) with {{B-0296}}.

## 6. A2 `labour_cost` (stacked_column)
- **(a) Where:** "### Costs and margins…". Insert after the "four patterns" list (ends line 134), before the `op_margin` chart (line 136).
- **(b, c) Spec:**
```
{"id":"labour_cost","type":"stacked_column","title":"Employee cost rose from 16% to 19% of revenue as job work fell from 9% to 6%, keeping combined labour cost at 24-28% since FY13","cats":["FY13","FY16","FY19","FY20","FY21","FY22","FY23","FY24","FY25","FY26"],"unit":"% of standalone revenue","dec":1,"series":[{"name":"Employee cost","facts":["D-CS-employee_cost-FY13","D-CS-employee_cost-FY16","D-CS-employee_cost-FY19","D-CS-employee_cost-FY20","D-CS-employee_cost-FY21","D-CS-employee_cost-FY22","D-CS-employee_cost-FY23","D-CS-employee_cost-FY24","D-CS-employee_cost-FY25","D-CS-employee_cost-FY26"]},{"name":"Job work","facts":["D-CS-job_work-FY13","D-CS-job_work-FY16","D-CS-job_work-FY19","D-CS-job_work-FY20","D-CS-job_work-FY21","D-CS-job_work-FY22","D-CS-job_work-FY23","D-CS-job_work-FY24","D-CS-job_work-FY25","D-CS-job_work-FY26"]}],"totals":true,"note":"Our calculation from the standalone accounts, as in the cost table. Job work is assembly contracted out, {{D-M-006}} of it to the promoter firm Vitromed in FY26 (Section A9)."}
```
- **Checks:**
  - Employee cost: 16.0, 17.5, 18.7, 19.7, 17.5, 17.0, 17.6, 17.5, 17.5, 18.8%
  - Job work: 9.0, 8.1, 8.2, 8.3, 7.5, 7.4, 7.2, 7.0, 6.7, 6.3%
  - Stacked totals: 25.0, 25.6, 26.9, 28.0, 25.0, 24.4, 24.8, 24.5, 24.2, 25.1%
  - D-M-006: 84%
- **(d) New formulas:** none.
- **(e) Can be trimmed:**
  - The ratio numbers in patterns 2 and 3 (lines 132-133).
  - In A8 ("What would strengthen…", line 84), replace the idea with an `[[EXREF:labour_cost]]` link rather than a new chart.

## 7. A2 `wc_days` (TABLE)
- **(a) Where:** "### Working capital: a long cycle by design". Insert after the bullet list (ends line 152), before the paragraph at line 154.
- **(b, c) Spec:**
```
::: table id="wc_days" title="Receivable days had eased to 73 by FY24; on the company's standalone measure they jumped to 98 in FY26 and the cash cycle lengthened by a month" note="Definitions differ by source and should not be spliced: the Feb-2021 placement document gives an 'average debtor cycle' ({{D-0778}} for 9MFY21), the Aug-2024 document 'trade receivables days', CRISIL its rating ratios and the company a standalone 'trade working capital' slide. Management quotes {{CA-0079}} for its own measure of the cash cycle at Mar-2026."
| Measure | Basis and source | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Receivable days | Consolidated; placement documents | {{D-0775}} | {{D-0776}} | {{D-0777}} | – | {{D-0254}} | {{D-0253}} | {{D-0252}} | – | – |
| Receivable days | Consolidated; CRISIL | – | – | {{B-0775}} | {{B-0774}} | {{B-0773}} | – | – | – | – |
| Inventory days | Consolidated; CRISIL | – | – | {{B-0778}} | {{B-0777}} | {{B-0776}} | – | – | – | – |
| Creditor days | Consolidated; CRISIL | – | – | {{B-0781}} | {{B-0780}} | {{B-0779}} | – | – | – | – |
| Debtor days | Standalone; company | – | – | – | – | – | – | – | {{CB-0929}} | {{CB-0928}} |
| Inventory days | Standalone; company | – | – | – | – | – | – | – | {{CB-0931}} | {{CB-0930}} |
| Creditor days | Standalone; company | – | – | – | – | – | – | – | {{CB-0933}} | {{CB-0932}} |
| Cash conversion cycle | Standalone; company | – | – | – | – | – | – | – | {{CB-0935}} | {{CB-0934}} |
| Receivables turnover (x) | Consolidated; annual report | – | – | – | – | – | – | – | {{A-0337}} | {{A-0336}} |
:::
```
- **Checks:**
  - Placement documents: D-0775 81 days · D-0776 80 · D-0777 70 · D-0778 65 · D-0254 80 · D-0253 76 · D-0252 73
  - CRISIL: B-0775 74 · B-0774 77 · B-0773 85 · B-0778 80 · B-0777 82 · B-0776 88 · B-0781 105 · B-0780 85 · B-0779 89
  - Company standalone: CB-0929 78 · CB-0928 98 · CB-0931 136 · CB-0930 152 · CB-0933 31 · CB-0932 35 · CB-0935 183 · CB-0934 215
  - Annual report and management: A-0337 5.4x · A-0336 4.3x · CA-0079 140 days
- **(d) New formulas:** none.
- **(e) Can be trimmed:** the "Receivables" (line 150) and "Cash conversion cycle" (line 152) bullets.

## 8. A9 `md_pay_pat` (line)
- **(a) Where:** "### Remuneration". Insert after the `md_pay_ratio` chart (ends line 133), before the `pay_fy26` table (line 135).
- **(b, c) Spec:**
```
{"id":"md_pay_pat","type":"line","title":"The two promoter MDs' pay has moved with profit, at 13-15% of standalone PAT in most years since FY13, before dropping to 10.6% in FY26","cats":["FY13","FY16","FY19","FY20","FY21","FY22","FY23","FY24","FY25","FY26"],"unit":"% of standalone PAT","dec":1,"series":[{"name":"MD + JMD pay","facts":["D-WI-008","D-WI-009","D-WI-010","D-WI-011","D-WI-012","D-WI-013","D-WI-014","D-WI-015","D-M-009","D-M-008"]}],"note":"Our calculation: remuneration including commission of Himanshu Baid (MD) and Rishi Baid (JMD; an executive director before FY20) from the related-party notes, over standalone profit after tax. Commission is capped at {{WM-0054}} of Section 198 profits for each (Aug-2024 placement document). In FY26 the MD received {{A-0427}} and the JMD {{A-0428}}."}
```
- **Checks:** D-WI-008…015 are new: 15.0 · 14.3 · 13.2 · 12.8 · 14.0 · 14.5 · 14.2 · 13.5%. Then D-M-009 12.8% · D-M-008 10.6% · WM-0054 5% · A-0427 Rs. 181mn · A-0428 Rs. 176mn.
- **(d) New formulas**, each "(MD + JMD) / standalone PAT × 100":

| id | Year | Formula | MD | JMD | Standalone PAT | Result |
|---|---|---|---|---|---|---|
| D-WI-008 | FY13 | `(B-0147+B-0149)/B-0081*100` | Rs. 18mn | Rs. 18mn | Rs. 240mn | 15.0% |
| D-WI-009 | FY16 | `(B-0255+B-0257)/B-0167*100` | Rs. 34mn | Rs. 33mn | Rs. 473mn | 14.3% |
| D-WI-010 | FY19 | `(B-0340+B-0342)/B-0271*100` | Rs. 44mn | Rs. 43mn | Rs. 663mn | 13.2% |
| D-WI-011 | FY20 | `(B-0394+B-0395)/B-0360*100` | Rs. 60mn | Rs. 58mn | Rs. 924mn | 12.8% |
| D-WI-012 | FY21 | `(B-0457+B-0458)/B-0412*100` | Rs. 92mn | Rs. 90mn | Rs. 1.3bn | 14.0% |
| D-WI-013 | FY22 | `(B-0510+B-0511)/B-0472*100` | Rs. 107mn | Rs. 104mn | Rs. 1.5bn | 14.5% |
| D-WI-014 | FY23 | `(B-0574+B-0575)/B-0534*100` | Rs. 130mn | Rs. 125mn | Rs. 1.8bn | 14.2% |
| D-WI-015 | FY24 | `(B-0640+B-0641)/B-0591*100` | Rs. 172mn | Rs. 167mn | Rs. 2.5bn | 13.5% |

- **(e) Can be trimmed:** the `pay_fy26` row "MD + JMD as % of standalone PAT", which duplicates the last two points.

## 9. A3 `fy27_guide` (TABLE)
- **(a) Where:** "### What management is guiding for FY27 and FY30". Replace the bullet list (lines 100-103). Keep the lead-in at line 99 and the Vision 2030 paragraph at line 105.
- **(b, c) Spec:**
```
::: table id="fy27_guide" title="FY27 guidance: 23-28% consolidated growth with a full year of the acquisitions, margins guided at or below FY26 and lower capex" note="Management guidance given 25-May-2026 (4QFY26 call) and described as maintained on 10-Aug-2026, except where dated. Implied consolidated growth is our calculation on FY26 revenue. Domestic and international targets are for the standalone company."
| Metric | FY26 delivered | FY27 guidance |
|---|---|---|
| Consolidated revenue | {{A-0039}} ({{CA-0107|signed}}) | {{CA-0135|range}}, implying {{D-M-001|num}}-{{D-M-002}} growth |
| Standalone revenue | {{A-0350}} (~{{CA-0093}}) | {{CA-0136|range}} (May-2026), widened to {{CA-0057|range}} (Aug-2026) |
| Domestic growth | {{A-0265}} (consolidated) | {{CA-0058}} (standalone) |
| International growth | {{A-0276}} incl. acquisitions; organic 'flattish' | {{CA-0059}} (standalone) |
| Standalone EBITDA margin | {{A-0311}} | {{CA-0139|range}} |
| Consolidated EBITDA margin | {{A-0028}} | {{CA-0140|range}} |
| Capex | ~{{CA-0127}} | {{CA-0141|range}} |
:::
```
- **Checks:**
  - FY26 delivered: A-0039 Rs. 18.8bn · CA-0107 12.3% · A-0350 Rs. 16.6bn · CA-0093 4% · A-0265 19.6% · A-0276 9.3% · A-0311 26.8% · A-0028 24.4% · CA-0127 Rs. 3.0bn
  - Revenue guidance: CA-0135 "INR2,300 crores to INR2,400 crores" · D-M-001 22.6% · D-M-002 28.0% · CA-0136 "INR1,900 crores to INR1950 crores" · CA-0057 "INR1,900 crores to INR2,000 crores"
  - Other guidance: CA-0058 "over 20%" · CA-0059 "over 15%" · CA-0139 "25% to 27%" · CA-0140 "between 23% and 25%" · CA-0141 "INR200 crores to INR225 crores"
- **(d) New formulas:** none.
- **(e) Can be trimmed:** lines 100-103. Line 67 (the widened standalone range) could become a pointer to this table.

## 10. A6 `util_hist` (line)
- **(a) Where:** "### Capacity and utilization". Insert after the "What the series shows" bullets (ends line 66), before the `cap_fy24` table (line 68).
- **(b, c) Spec:**
```
{"id":"util_hist","type":"line","title":"Certified utilization held near 80% until FY24, when new plants pulled it to 70%; the placement document's own MD&A quotes figures 7-10 points higher","cats":["FY18","FY19","FY20","FY22","FY23","FY24"],"unit":"% of installed capacity","dec":1,"ymin":60,"series":[{"name":"Chartered-engineer certificates","facts":["D-0728","D-0731","D-0734","D-0159","D-0156","D-0153"]},{"name":"Aug-2024 placement document, MD&A","facts":["-","-","-","D-0162","D-0161","D-0160"]}],"note":"Group totals including the China, Italy and Egypt plants, from the certificates in the Feb-2021 and Aug-2024 placement documents. FY21 was not certified and nothing has been certified since FY24. Management put utilization at {{WRC-0001}} in Jul-2024, a blended {{CA-0685|range}} in Oct-2024 and {{CA-0173|range}} for post-2021 capacity in May-2026."}
```
- **Checks:**
  - Certificates: D-0728 82.1% · D-0731 80.5% · D-0734 81.9% · D-0159 78.2% · D-0156 80.1% · D-0153 70.5%
  - PD24 MD&A: D-0162 85.1% · D-0161 88.0% · D-0160 80.7% (7-10 points above the certificates)
  - Note: WRC-0001 75% · CA-0685 "close to around 60%, 65%" · CA-0173 "close to around 65% to 70%"
- **(d) New formulas:** none.
- **(e) Can be trimmed:**
  - Line 60: "Utilization fell from {{D-0156}} to {{D-0153}}. The same placement document's MD&A gives {{D-0160}}…".
  - The last sentence of the `cap_hist` note.
  - The Oct-2024 sub-bullet (line 64).

## 11. A9 `oi_pbt` (column)
- **(a) Where:** "### Capital allocation". Insert after the "Cash and payout" bullets (ends line 204), before "We see capital allocation…" (line 206).
- **(b, c) Spec:**
```
{"id":"oi_pbt","type":"column","title":"Other income rose to 27% of standalone pre-tax profit in FY26, from 11-20% in FY20-FY25, as treasury and currency gains grew","cats":["FY20","FY21","FY22","FY23","FY24","FY25","FY26"],"unit":"% of standalone PBT","dec":1,"series":[{"name":"Other income as % of PBT","facts":["D-WI-016","D-WI-017","D-WI-018","-","D-WI-019","D-WI-020","D-WI-021"]}],"label_all":true,"note":"Our calculation from standalone other income and profit before tax; FY23 standalone PBT is not in our sources. In FY26 realised and unrealised mutual-fund gains ({{A-0485}}, {{A-0486}}) and FX gains ({{A-0487}}) made up {{D-WI-022}} of standalone other income. On a consolidated basis other income was {{D-M-023}} of PBT."}
```
- **Checks:** D-WI-016…021 are new: 15.3 · 11.1 · 19.9 · 17.4 · 20.3 · 26.8%. Note: A-0485 Rs. 402mn · A-0486 Rs. 126mn · A-0487 Rs. 381mn · D-WI-022 75.9% (new) · D-M-023 28%.
- **(d) New formulas**, each "other income / standalone PBT × 100":

| id | Year | Formula | Other income | Standalone PBT | Result |
|---|---|---|---|---|---|
| D-WI-016 | FY20 | `B-0361/CC-0895*100` | Rs. 186mn | Rs. 1.2bn | 15.3% |
| D-WI-017 | FY21 | `B-0413/CC-0896*100` | Rs. 193mn | Rs. 1.7bn | 11.1% |
| D-WI-018 | FY22 | `B-0473/CC-0897*100` | Rs. 387mn | Rs. 1.9bn | 19.9% |
| D-WI-019 | FY24 | `B-0592/CB-2752*100` | Rs. 582mn | Rs. 3.3bn | 17.4% |
| D-WI-020 | FY25 | `A-0354/A-0366*100` | Rs. 898mn | Rs. 4.4bn | 20.3% |
| D-WI-021 | FY26 | `A-0353/A-0365*100` | Rs. 1.2bn | Rs. 4.5bn | 26.8% |

  - D-WI-022 `(A-0485+A-0486+A-0487)/A-0353*100` = 75.9%
- **(e) Can be trimmed:** the second sentence of the "Other income" bullet (line 201), which moves to the note.

## 12. A6 `headcount` (column)
- **(a) Where:** "### Workforce and wages". Insert after the first paragraph (line 136), before the `workforce` table (line 138).
- **(b, c) Spec:**
```
{"id":"headcount","type":"column","title":"Standalone headcount rose 3.5x over FY10-FY25 while revenue grew almost 12x; the reported FY26 count fell 15%, a drop the BRSR does not show","cats":["FY10","FY13","FY16","FY19","FY20","FY21","FY22","FY23","FY24","FY25","FY26"],"unit":"employees on the rolls, 31 March","dec":0,"series":[{"name":"Standalone employees","facts":["B-0043","B-0137","B-0223","B-0323","B-0389","B-0437","B-0496","B-0557","B-0620","A-0735","A-0144"]}],"label_all":true,"note":"Ten-year summaries and directors' reports; FY26 is the Rule 5 annexure count, the measure that gave {{A-0751}} for FY25, and fell {{D-WI-027|abs}}. Excludes contract workers ({{A-0860}} at 31-Mar-2026). The BRSR counts {{D-WI-024}} permanent employees and workers at 31-Mar-2026 against {{D-WI-023}} a year earlier. Over FY10-FY25 headcount grew {{D-WI-025}} and standalone revenue {{D-WI-026}} (our calculations)."}
```
- **Checks:**
  - Series: B-0043 890 · B-0137 1,329 · B-0223 1,594 · B-0323 1,952 · B-0389 2,034 · B-0437 2,039 · B-0496 2,140 · B-0557 2,339 · B-0620 2,651 · A-0735 3,082 · A-0144 2,614
  - Note: A-0751 3,082 · A-0860 2,745
- **(d) New formulas:**
  - D-WI-023 `A-0904+A-0905` = 2,952 (1,451 + 1,501; unit count, dec 0)
  - D-WI-024 `A-0858+A-0859` = 3,063 (1,548 + 1,515)
  - D-WI-025 `A-0735/B-0043` = 3.5x
  - D-WI-026 `A-0351/B-0001` = 11.8x (Rs. 16.0bn / Rs. 1.4bn)
  - D-WI-027 `(A-0144/A-0735-1)*100` = -15.2%
- **(e) Can be trimmed:** in line 136, "the Directors' Report counts {{A-0144}} permanent employees on the standalone rolls".

## 13. A2 `vol_price` (TABLE)
- **(a) Where:** "### Price and volume: most growth has come from units". Insert after the two bullets (lines 40-42), before the placement-document paragraph (line 44).
- **(b, c) Spec:**
```
::: table id="vol_price" title="Units drove FY25 growth: devices sold rose 25% against 22.5% standalone revenue growth, and revenue per device slipped from Rs. 11.4 to Rs. 11.2" note="Devices sold as printed in the 3QFY25 and 4QFY25 presentations (standalone); no later counts are in our sources. The 9MFY25 and 4QFY25 counts add up to less than the FY25 total, and likewise for FY24; we have not been able to reconcile them. Revenue per device is standalone revenue from operations over devices sold (our calculation). For FY22 the MD put volume at ~{{CC-0275}} and price at ~{{CC-0274}} of growth."
| Period | Devices sold | Growth in devices sold | Standalone revenue growth | Revenue per device |
|---|---|---|---|---|
| 3QFY25 | {{CB-2876}} | {{CB-2878}} | {{CB-2989}} | – |
| 4QFY25 | {{CB-2564}} | {{CB-2566}} | {{CB-2688}} | – |
| 9MFY25 | {{CB-2880}} | {{CB-2882}} | {{CB-2990}} | – |
| FY24 | {{CB-2574}} | – | – | {{D-WA-017}} |
| FY25 | {{CB-2573}} | {{CB-2575}} | {{CB-2689}} | {{D-WA-016}} |
:::
```
- **Checks:**
  - 3QFY25: CB-2876 322mn units · CB-2878 23% · CB-2989 28.1%
  - 4QFY25: CB-2564 372mn units · CB-2566 24.6% · CB-2688 16.6%
  - 9MFY25: CB-2880 964mn units · CB-2882 18.9% · CB-2990 24.8%
  - FY24: CB-2574 1.2bn units · D-WA-017 Rs. 11.4
  - FY25: CB-2573 1.4bn units · CB-2575 24.7% · CB-2689 22.5% · D-WA-016 Rs. 11.2
  - Note: CC-0275 75% · CC-0274 25%
- **(d) New formulas:** none.
- **(e) Can be trimmed:**
  - The bullets at lines 41-42. Line 42 compares standalone device growth (WM-0006, 19%) with *consolidated* revenue growth (CA-0558, 23.2%); the table uses the matching standalone figure, CB-2990 (24.8%).
  - The parenthetical in A1 line 101.

## 14. A8 `peer_export` (hbar)
- **(a) Where:** "### Where the advantage comes from". Insert after the `peer_margin` chart (ends line 43), before "### Where it is vulnerable" (line 45).
- **(b, c) Spec:**
```
{"id":"peer_export","type":"hbar","title":"Polymed earns a larger share of revenue abroad than any Indian or Chinese peer we track","cats":["Polymed, consolidated (FY26)","Healthium (FY25)","Shanghai Kindly (CY25)","Weigao (CY25)","B. Braun India (FY23)","Hindustan Syringes (FY23)","BD India (FY23)"],"unit":"% of revenue from outside the home market","dec":1,"label_w":200,"series":[{"name":"Share of revenue from outside the home market","facts":["CB-0084","E-0306","D-WA-024","E-0268","E-0351","E-0349","E-0350"]}],"note":"Periods and definitions differ, as labelled: Polymed's 'international business' includes the foreign subsidiaries (the BRSR gives {{A-0857}} for standalone exports); Healthium per ICRA; KDL our calculation from its annual report; Weigao's overseas share; the Indian arms of BD and B. Braun and HMD per CRISIL in the Aug-2024 placement document. Indicative only."}
```
- **Checks:** CB-0084 69% · E-0306 48.5% · D-WA-024 35% · E-0268 27% · E-0351 23.1% · E-0349 20.8% · E-0350 15.9% · A-0857 65.0%.
- **(d) New formulas:** none.
- **(e) Can be trimmed:** "{{E-0268}} of it overseas" in line 49.

## 15. A5 `india_channel` (TABLE)
- **(a) Where:** "### India: the growth engine is the private hospital". Insert after the bullet list (ends line 188), before "### Company-specific drivers by region" (line 190).
- **(b, c) Spec:**
```
::: table id="india_channel" title="The sales force has more than doubled since 2019 and Indian distributors are up by half since FY22, but hospital reach has stayed at about 8,000 since late 2023" note="Company counts, most printed with a '+'. Sales associates are for India unless marked; distributor counts for FY22-FY24 are fiscal year-end figures from the Aug-2024 placement document. Management counts ~{{CA-0533}} larger Indian hospitals as addressable and plans {{CB-1115}}+ sales hires in FY27."
| As of | Sales associates | Distributors in India | Hospitals reached in India |
|---|---|---|---|
| Oct-2019 | {{CC-1067}} | – | {{CC-1066}} |
| May-2022 | {{CC-0864}} | {{D-0203}} (FY22) | {{CC-0863}} |
| Nov-2023 | {{CC-0769}} (group) | {{D-0202}} (FY23) | {{CC-0777}} |
| Jun-2024 | {{D-0036}} | {{D-0201}} (FY24) | {{D-0006}} |
| Feb-2025 | {{CB-2868}} | {{CB-2869}} | – |
| May-2025 | {{CB-2555}} | {{CB-2556}} | – |
| Aug-2025 | {{CB-2090}} | {{CB-2091}} | – |
| Feb-2026 | – | – | {{CA-0298}} |
| May-2026 | {{CB-1028}} (group) | {{CB-1116}} | – |
| Aug-2026 | {{CB-0018}} (India, US, Italy, Mexico) | – | – |
:::
```
- **Checks:**
  - Sales associates: CC-1067 250+ · CC-0864 275+ · CC-0769 350+ · D-0036 440 · CB-2868 475 · CB-2555 510 · CB-2090 530 · CB-1028 570 · CB-0018 590
  - Distributors in India: D-0203 425 · D-0202 463 · D-0201 506 · CB-2869 600 · CB-2556 630 · CB-2091 630 · CB-1116 650
  - Hospitals reached: CC-1066 5,000+ · CC-0863 6,500+ · CC-0777 8,000+ · D-0006 8,000 · CA-0298 8,000
  - Note: CA-0533 20,000 · CB-1115 100
  - For the title: sales associates are 2.36x their Oct-2019 level; Indian distributors are 1.53x their FY22 level.
- **(d) New formulas:** none.
- **(e) Can be trimmed:**
  - The numbers in the "Coverage" and "Channel" bullets (lines 186-187).
  - A2 line 78: "At Jun-2024 it had {{D-0036}} sales staff covering {{D-0006}} hospitals and {{D-0201}} distributors".

## 16. A9 `qip24_pace` (column)
- **(a) Where:** "### Capital allocation". Insert after the `qip24` table (ends line 172, source comment at 173), before "The monitoring agency's 4QFY26 report…" (line 175).
- **(b, c) Spec:**
```
{"id":"qip24_pace","type":"column","title":"Half the Aug-2024 QIP had been used by Mar-2026, mostly on the two acquisitions and general purposes; plant capex had drawn only Rs. 0.6bn","cats":["Dec-2024","Jun-2025","Sep-2025","Dec-2025","Mar-2026"],"scale":"bn","unit":"Rs bn, cumulative","dec":1,"series":[{"name":"QIP-2024 proceeds used","facts":["B-0822","B-0824","B-0823","B-0825","B-0826"]},{"name":"of which plant capex","facts":["-","-","-","A-1106","A-0584"]}],"label_all":true,"note":"Monitoring-agency reports and quarterly results, against net proceeds of {{B-0816}}; {{D-WI-039}} had been used by 31-Mar-2026 (our calculation). The Sep-2025 step includes the PendraCare consideration ({{A-1305}}); the inorganic object of {{B-0818}} was fully used by Dec-2025. Plant capex was {{D-WC-075}} of its {{B-0817}} object, against {{B-0828}} scheduled by FY26."}
```
- **Checks:**
  - Used (cumulative): B-0822 Rs. 850mn · B-0824 Rs. 1.3bn · B-0823 Rs. 2.9bn · B-0825 Rs. 4.7bn · B-0826 Rs. 5.0bn
  - Plant capex: A-1106 Rs. 353mn · A-0584 Rs. 620mn
  - Note: B-0816 Rs. 9.9bn · A-1305 Rs. 1.5bn · B-0818 Rs. 2.5bn · D-WC-075 12% · B-0817 Rs. 5.0bn · B-0828 Rs. 3.0bn
- **(d) New formulas:** D-WI-039 `B-0826/B-0816*100` = 50.8%.
- **(e) Can be trimmed:** the bullet "The acquisition money went first, to PendraCare and Citieffe" (line 160).

## 17. A1 `cagr_bars` (hbar)
- **(a) Where:** "### Two-thirds of revenue is earned outside India". Insert after the `rev_geo` chart (ends line 87), before "### What the disclosure does and does not tell us" (line 89).
- **(b, c) Spec:**
```
{"id":"cagr_bars","type":"hbar","title":"Renal (39% a year) and India (21%) led FY20-FY26 growth; infusion (14%) and the rest of the world (15%) lagged the group's 18%","cats":["Renal","Others, incl. acquisitions","India","Europe","Group","Rest of world","Infusion"],"unit":"Revenue CAGR FY20-FY26, %","dec":0,"series":[{"name":"CAGR, FY20-FY26","facts":["CB-0030","CB-0035","CB-0045","CB-0050","CB-0040","CB-0055","CB-0025"]}],"note":"Company-stated CAGRs from the 1QFY27 presentation, the source of the therapy and region charts above. 'Others' includes PendraCare and Citieffe in FY26."}
```
- **Checks:** CB-0030 39% · CB-0035 23% · CB-0045 21% · CB-0050 20% · CB-0040 18% · CB-0055 15% · CB-0025 14%.
- **(d) New formulas:** none.
- **(e) Can be trimmed:**
  - The CAGR clauses in lines 79-81.
  - The CAGR sentence in the `rev_therapy` note.
  - The "Revenue CAGR was {{CB-0040}}" sentence in the `rev_long` note.

## 18. A9 `vitromed_hist` (stacked_column)
- **(a) Where:** "### Related parties…". Insert after line 90 ("Over time Vitromed's share…"), before the `vitromed` table (line 92).
- **(b, c) Spec:**
```
{"id":"vitromed_hist","type":"stacked_column","title":"Vitromed still receives five-sixths of Polymed's job work, and payments to it rose eightfold over FY10-FY26","cats":["FY10","FY13","FY16","FY19","FY20","FY21","FY22","FY23","FY24","FY25","FY26"],"scale":"mn","unit":"Rs mn","dec":0,"series":[{"name":"Paid to Vitromed","facts":["B-0058","B-0141","B-0249","B-0332","B-0390","B-0452","B-0505","B-0569","B-0634","A-0548","A-0547"]},{"name":"Other job workers","facts":["D-WI-028","D-WI-029","D-WI-030","D-WI-031","D-WI-032","D-WI-033","D-WI-034","D-WI-035","D-WI-036","D-WI-037","D-WI-038"]}],"totals":true,"note":"Standalone job-work charges and the related-party note; other job workers is the total less Vitromed (our calculation). Vitromed's share was {{D-M-025}} in FY10 and {{D-M-006}} in FY26."}
```
- **Checks:**
  - Vitromed: B-0058 Rs. 104mn · B-0141 Rs. 214mn · B-0249 Rs. 300mn · B-0332 Rs. 441mn · B-0390 Rs. 494mn · B-0452 Rs. 513mn · B-0505 Rs. 578mn · B-0569 Rs. 669mn · B-0634 Rs. 765mn · A-0548 Rs. 893mn · A-0547 Rs. 870mn
  - D-M-025 93% · D-M-006 84% (FY26 share 83.6%; FY26 payments 8.3x FY10)
- **(d) New formulas:** D-WI-028…038 are "total job work less Vitromed" (unit Rs mn):

| id | Year | Formula | Total job work | Result (Rs mn) |
|---|---|---|---|---|
| D-WI-028 | FY10 | `B-0031-B-0058` | Rs. 112mn | 7.4 |
| D-WI-029 | FY13 | `B-0119-B-0141` | Rs. 226mn | 11.7 |
| D-WI-030 | FY16 | `B-0204-B-0249` | Rs. 320mn | 19.5 |
| D-WI-031 | FY19 | `B-0308-B-0332` | Rs. 478mn | 37.9 |
| D-WI-032 | FY20 | `B-0382-B-0390` | Rs. 539mn | 45.4 |
| D-WI-033 | FY21 | `B-0430-B-0452` | Rs. 560mn | 46.6 |
| D-WI-034 | FY22 | `B-0489-B-0505` | Rs. 648mn | 70.8 |
| D-WI-035 | FY23 | `B-0550-B-0569` | Rs. 772mn | 102.4 |
| D-WI-036 | FY24 | `B-0613-B-0634` | Rs. 910mn | 144.7 |
| D-WI-037 | FY25 | `A-0507-A-0548` | Rs. 1.1bn | 180.5 |
| D-WI-038 | FY26 | `A-0506-A-0547` | Rs. 1.0bn | 170.3 |

- **(e) Can be trimmed:**
  - The first two rows of the `vitromed` table; keep the share and sales-to-Vitromed rows.
  - "the rupee amount has grown {{D-M-024}} since FY10" (line 90).

---

## New derived formulas, all together (`ledger/derived_WI.py`, not created)
Use the existing `DERIVED.append({...})` format.
- **D-WI-001 to 003:** quarterly growth (#1). Unit %.
- **D-WI-004 to 007:** export-incentive rates and the FX earnings multiple (#5). The last is a multiple (x).
- **D-WI-008 to 015:** MD + JMD pay as % of standalone PAT (#8). Unit %.
- **D-WI-016 to 022:** other income as % of standalone PBT, plus the treasury/FX share of FY26 other income (#11). Unit %.
- **D-WI-023 to 027:** BRSR counts (unit count, dec 0), headcount and revenue multiples (x), and the FY26 headcount change (%) (#12).
- **D-WI-028 to 038:** other job workers (#18). Unit Rs mn.
- **D-WI-039:** share of QIP-2024 proceeds used (#16). Unit %.

Every input was confirmed to exist and to be numeric.

## Gaps and ideas I checked but did not propose
- **A7:** thin by design. Apart from `q_margin`, its content is qualitative driver tables.
- **Guidance vs delivery (A3, A7):** no historical chart is possible. The past guidance facts are stored as text ranges (CC-0017 "17-18", CC-0599 "22-24", CA-0690, CA-0364, CA-0517), so they can't be plotted without new numeric facts. The existing `guidance_history` and `guidance_scorecard` tables already cover the record.
- **A8 peers:** only `peer_export` is proposed.
  - R&D-intensity benchmarks are text ranges: A-0236 "2-4%", D-0482 "8-9", D-0488 "6-7", WRB-0001 "10-15%".
  - Peer gross margins aren't comparable. Polymed's is materials-only, while E-0248, E-0213 and E-0276 are full cost-of-goods figures under IFRS/GAAP.
- **A1:** already exhibit-dense (5 exhibits), so only `cagr_bars`.
- **Rejected to avoid duplicating existing exhibits:**
  - automation counts (`auto_hist`)
  - R&D spend (`rnd_hist` and the cost table; the company's printed FY10/FY15/FY16 ratios B-0049, B-0214, B-0213 are also text)
  - capex (`capex_hist`)
  - capacity (`cap_hist` and `cap_fy24`)
  - subsidiary P&L (`sub_pnl`, and `p1h_rev` in A4.2)
- **Spare options if you want more** (all IDs verified):
  - A9 `returns`: company-adjusted RoCE and ROE. RoCE: CB-1133 19%, CB-1139 23%, CB-1145 23%, CB-1151 16%. ROE: CB-1134 15%, CB-1140 19%, CB-1146 18%, CB-1152 13%. The definition shifted: the Jul-2024 deck gave FY24 RoCE of 20.9% (CC-0759).
  - A5 `affiliates`: China plant sales fell from B-0245 Rs. 178mn (FY16) to A-0378 Rs. 112mn (FY26); Egypt associate sales rose from B-0243 Rs. 546mn (CY15) to A-0385 Rs. 1.2bn (CY25).
  - A6 `patents`: CB-1956 334 (Jun-2025), CB-1580 375, CB-1198 394, CB-0580 399 (Mar-2026), with standalone CB-0567 348.

## Data issues found while checking
- **Device counts don't add up.** 9MFY25 (CB-2880, 964mn) plus 4QFY25 (CB-2564, 372mn) is 1,336mn, but FY25 (CB-2573) is 1,436mn. FY24 has the same kind of gap: 811mn + 299mn versus 1,151mn.
- **FY26 headcount conflict.** The Rule 5 count is A-0144 (2,614, down 15%), but the BRSR shows permanent staff up to 3,063 (A-0858 + A-0859).
- **A2 basis mismatch** at line 42, as noted under #13.
- **Missing inputs:** FY23 standalone PBT is not in the ledger. Standalone EBITDA margins for 1QFY25 and 2QFY25 are also missing.

**Side effect:** one of my lookups imported `build/reconcile.py`, which wrote a git-ignored bytecode cache file, `build/__pycache__/reconcile.cpython-311.pyc`. No draft, ledger or source file was changed, and the ledger timestamps are unchanged.