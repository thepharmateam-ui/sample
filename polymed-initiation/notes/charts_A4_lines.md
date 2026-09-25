I checked 20 proposed exhibits against the ledger: 15 charts and 5 tables, most valuable first. All ~200 fact IDs resolve, and every chart series uses only numeric facts. Text-valued facts (ranges like "around 70-72%") appear only in notes and table cells, with `|range` or `|plain`.

Three things to know before adding the new derived formulas:
- **Derived formulas can only use base facts.** `reconcile.py` only resolves IDs with a four-digit number (`[A-Z]{1,3}-\d{4}`), so a formula cannot reference another derived fact such as `D-WC-011`. Every formula below is built from base facts. Chart series can still use existing derived IDs.
- **Comtrade values are stored in raw dollars.** They need `/1000000` derived conversions, as ch43 and ch44 already do.
- **PendraCare's figures mix units** (CY24 in € mn, CY25 in € thousand). They should not share a series.

I left out ideas that already have an exhibit elsewhere: infusion revenue and share (`rev_therapy`, `mix_q`, `inf_hist`), China's exports by region (`b2_china_exports`), US syringe imports (`b5_syringes`), India's catheter exports by destination (`b4_dest`), export sales by region (`geo_outside`), launches (`launches`), mark-ups (`b3_mhfda`), stents (`card_stents`), PendraCare's P&L (`card_pendra`) and Citieffe's geography (`ortho_geo`).

---

## Ranked proposals

### 1. `renal_pli` (chart) – `/home/user/sample/polymed-initiation/draft/22_A4_3_renal.md`
- **(a) Where:** in "### Regulation and policy…", after the "**PLI: approved, invested, unpaid.**" bullets (ending "Outcome…", line 189), before "**Device regulation and reimbursement.**".
- **(b)–(c) Spec:**
```
{"id":"renal_pli","type":"column","title":"On our proxy, renal sales above the FY20 base have fallen short of the PLI threshold every year since FY23, and the gap has widened","cats":["FY23","FY24","FY25","FY26"],"scale":"mn","unit":"Rs mn","dec":0,"series":[{"name":"Renal revenue above FY20 base (our proxy)","facts":["D-WB-041","D-WB-040","D-WB-039","D-WB-038"]},{"name":"PLI threshold, incremental sales (Category A)","facts":["WB-0020","WB-0021","WB-0022","WB-0023"]}],"label_all":true,"note":"Proxy = consolidated renal revenue less FY20 renal revenue of {{D-0625}} (FY23-FY24 placement-document table; FY25-FY26 4QFY26 presentation); eligible sales may be defined differently. FY27 requires {{F-0013}}. Shortfall {{D-WB-063}} in FY23 and {{D-WB-066}} in FY26 (our calculation). No incentive received by Jul-2026, against {{F-0016}} invested of {{F-0015}} committed."}
```
- **Facts verified:** D-WB-041=Rs. 500mn, D-WB-040=Rs. 688mn, D-WB-039=Rs. 1.2bn, D-WB-038=Rs. 1.6bn; WB-0020=Rs. 600mn, WB-0021=Rs. 1.2bn, WB-0022=Rs. 1.8bn, WB-0023=Rs. 2.3bn; F-0013=Rs. 2.8bn, D-0625=Rs. 257mn, F-0016=Rs. 556mn, F-0015=Rs. 720mn.
- **(d) New derived** (`derived_WB.py`, Rs mn, dec 0):
  - D-WB-063 = `WB-0020-(D-0057-D-0625)` → 100
  - D-WB-064 = `WB-0021-(D-0055-D-0625)` → 512
  - D-WB-065 = `WB-0022-(CB-0871-D-0625)` → 550
  - D-WB-066 = `WB-0023-(CB-0870-D-0625)` → 681
- **(e) Redundant text:** the "Why it has missed" bullet ("Polymed generated {{D-WB-041}}, {{D-WB-040}}, {{D-WB-039}} and {{D-WB-038}}…") shrinks to one clause plus an EXREF. The threshold list in the "Terms" bullet can shrink to "rising each year to {{F-0013}} in FY27".

### 2. `card_pacifier` (chart) – `/home/user/sample/polymed-initiation/draft/27_A4_8_cardiology.md`
- **(a) Where:** in "### Traction…", after the PACIFIER bullets (ending "Disclosure quality…", line 58), before "### PendraCare…".
```
{"id":"card_pacifier","type":"stacked_column","title":"PACIFIER had enrolled 840 of its 2,000 patients by Aug-2026; at the Feb-Aug pace the rest would take about 11 months, past the end-FY27 target","cats":["Feb-2026","May-2026","Aug-2026"],"unit":"patients","dec":0,"series":[{"name":"Enrolled (printed with a '+')","facts":["CB-1203","CB-0598","CB-0192"]},{"name":"Still to enrol (our calculation)","facts":["D-WC-093","D-WC-094","D-WC-011"]}],"totals":true,"note":"3QFY26, 4QFY26 and 1QFY27 presentations; the Feb-2026 figure is for the RisoR study in India. Design: {{CB-1972|num}} patients in India, {{CB-1971|num}} in Europe; full enrolment targeted by end-FY27. Feb-Aug 2026 pace ~{{D-WC-012}} a month, so ~{{D-WC-013}} to finish from Aug-2026 (our calculation). The 4QFY26 deck also printed {{CB-1089|num}}+ enrolled on another slide."}
```
- **Facts verified:** CB-1203=200 patients, CB-0598=650, CB-0192=840, D-WC-011=1,160, CB-1970=2,000, CB-1972=1,960, CB-1971=40, D-WC-012=107, D-WC-013=11 months, CB-1089=2,000.
- **(d) New derived** (`derived_WC.py`, count, dec 0): D-WC-093 = `CB-1970-CB-1203` → 1,800; D-WC-094 = `CB-1970-CB-0598` → 1,350. The column totals then show 2,000.
- **(e) Redundant text:** the "Enrolment", "Our arithmetic" and "Disclosure quality" bullets move into the chart and note. Keep only the conclusion "no European sales before FY29".

### 3. `oem_mix` (chart; first chart in ch29) – `/home/user/sample/polymed-initiation/draft/29_A4_10_components_oem.md`
- **(a) Where:** in "### The evidence on OEM and private label", replacing the `oem_share` table (lines 37-49).
```
{"id":"oem_mix","type":"share_hbar","title":"Private label was about 30% of Polymed's sales in FY21-FY22 and a quarter of exports, with none in India; PendraCare sold almost half its output to OEMs","cats":["Polymed, Oct-2020 deck","Polymed, FY21","Polymed, FY22","Polymed exports, Feb-2023","Polymed India, Feb-2023","PendraCare, CY24"],"unit":"% of sales","series":[{"name":"Own brand","facts":["CC-0996","CC-0277","CC-0279","D-WA-054","D-WA-055","CB-2502"]},{"name":"OEM and private label","facts":["CC-0997","CC-0278","CC-0280","CC-0436","CC-0437","CB-2501"]}],"label_w":190,"note":"FY21-FY22 as stated by the MD (4QFY22 call); the May-2022 deck shows {{CC-0871}}:{{CC-0872}}. Export and India own-brand shares are our calculation, 100 minus the white-label share given in Feb-2023 (exports '{{CC-0435|plain}}' branded). CRISIL Ratings: own brand {{B-0748|range}} in FY22 and {{B-0749|range}} in FY23-FY24. Management targets {{CC-0281|range}} own brand. PendraCare CY24 is pre-acquisition. No group split has been given since Feb-2023."}
```
- **Facts verified:** CC-0996=70%, CC-0997=30%, CC-0277=70%, CC-0278=30%, CC-0279=72%, CC-0280=28%, CC-0871=72%, CC-0872=28%, CC-0436=25%, CC-0437=0%, CB-2502=52%, CB-2501=48%. Text-only facts in the note: CC-0435 "close to around 75%", B-0748 "around 70-72%", B-0749 "around 70%", CC-0281 "as close to 80%".
- **(d) New derived** (`derived_WA.py`, %, dec 0): D-WA-054 = `100-CC-0436` → 75; D-WA-055 = `100-CC-0437` → 100.
- **(e) Redundant text:** the whole `oem_share` table (the CRISIL rows and the target move into the note).

### 4. `dx_traded` (chart; first chart in ch24) – `/home/user/sample/polymed-initiation/draft/24_A4_5_diagnostics.md`
- **(a) Where:** after the "**Made or bought.**" paragraph (line 29), before "### What has been disclosed".
```
{"id":"dx_traded","type":"column","title":"Traded-goods sales, which once included blood-collection tubes, have roughly halved since FY24, when the diagnostics plant opened","cats":["FY22","FY23","FY24","FY25","FY26"],"scale":"mn","unit":"Rs mn","dec":0,"series":[{"name":"Sale of traded goods, consolidated","facts":["WB-0037","WB-0038","WB-0039","WG-0001","WG-0002"]}],"label_all":true,"note":"FY22-FY24 from the Aug-2024 placement document, which names blood-collection tubes first among traded goods (and haemodialysis machines in FY22); FY25-FY26 from the FY26 annual report's revenue note, which names no items. Traded goods were {{D-WG-001}} of product sales in FY24 and {{D-WG-002}} in FY26, a {{D-WG-003}} change (our calculations). The Faridabad diagnostics plant started production in 1QFY24."}
```
- **Facts verified:** WB-0037=Rs. 88mn, WB-0038=Rs. 83mn, WB-0039=Rs. 92mn, WG-0001=Rs. 59mn, WG-0002=Rs. 47mn, D-WG-001=0.7%, D-WG-002=0.3%, D-WG-003=-49%.
- **(d) New derived:** none. The FY23 and FY25 manufactured-goods totals exist only inside snippets, so shares for those years cannot be derived.
- **(e) Redundant text:**
  - In "Made or bought": "traded sales ran between {{WB-0038}} and {{WB-0039}}" and "have fallen {{D-WG-003|abs}} to {{WG-0002}}…".
  - The two traded-goods rows of `dx_disclosure`.

### 5. `arc_rev` (chart; first chart in ch25) – `/home/user/sample/polymed-initiation/draft/25_A4_6_anaesthesia_resp_critical.md`
- **(a) Where:** after the paragraph following `arc_disclosure` ("The FY26 BRSR drops…", line 55), before "### Critical care: the growth project".
```
{"id":"arc_rev","type":"column","title":"Anaesthesia and respiratory revenue has grown more slowly than the company on each comparable basis since FY18","cats":["FY18","FY19","FY20","FY21-FY24","FY25"],"scale":"mn","unit":"Rs mn","dec":0,"series":[{"name":"Placement document, consolidated product sales","facts":["D-0581","D-0583","D-0585","-","-"]},{"name":"BRSR share x standalone revenue (our calculation)","facts":["-","-","-","-","D-WA-004"]}],"label_all":true,"note":"FY18-FY20 from the Feb-2021 placement document (9MFY21: {{D-0587}}). FY25 = BRSR share of {{A-0899}} x standalone revenue of {{A-0351}}; the halves are on different bases and the FY26 BRSR drops the line. CAGR FY18-FY20 {{D-WA-052}} vs {{D-WH-004}} for all product sales; FY20-FY25 the line grew {{D-WA-053}} vs {{D-WH-013}} for the company on the same mixed bases (our calculations)."}
```
- **Facts verified:** D-0581=Rs. 184mn, D-0583=Rs. 198mn, D-0585=Rs. 229mn, D-0587=Rs. 238mn, D-WA-004=Rs. 461mn, A-0899=2.9%, A-0351=Rs. 16.0bn, D-WH-004=14.7%, D-WH-013=2.4x.
- **(d) New derived** (`derived_WA.py`): D-WA-052 = `((D-0585/D-0581)**(1/2)-1)*100` → 11.6%; D-WA-053 = `A-0899/100*A-0351/D-0585` → 2.0x.
- **(e) Redundant text and a correction:**
  - The rupee values in `arc_disclosure` can go, leaving it as a share log.
  - Line 55's "grown roughly in line with the group" is contradicted by these numbers (11.6% vs 14.7%; 2.0x vs 2.4x). It should read "more slowly".

### 6. `p1h_ebitda` (chart) – `/home/user/sample/polymed-initiation/draft/21_A4_2_vascular_oncology.md`
- **(a) Where:** after the `p1h_fin` table (line 67), before "The company's own slides also disagree…".
```
{"id":"p1h_ebitda","type":"column","title":"On the company's own slide, Plan1Health's EBITDA rose almost twelvefold from CY20 to CY25 while revenue tripled","cats":["CY20","CY22","CY24","CY25"],"unit":"EUR '000","dec":0,"series":[{"name":"Revenue (company slide)","facts":["CB-0099","CB-0101","CB-0103","CB-0105"]},{"name":"EBITDA, revenue x slide margin (our calculation)","facts":["D-WA-048","D-WA-049","D-WA-050","D-WA-051"]}],"label_all":true,"note":"1QFY27 presentation; CY21 and CY23 not shown. Printed margins {{CB-0100}}, {{CB-0102}}, {{CB-0104}}, {{CB-0106}}; the slide claims {{CB-0107}} revenue and {{CB-0108}} EBITDA since 2020. Statutory CY25: EBIT {{B-0724}} ({{D-WA-021}} margin), net profit {{B-0725}}. Management's call figures of {{CC-0702|range}} (FY24) and {{CA-0374|range}} (Nov-2025) are higher."}
```
- **Facts verified:** CB-0099=€3.24mn, CB-0101=€4.83mn, CB-0103=€8.11mn, CB-0105=€10.5mn (all "EUR thousand"); CB-0100=3.7%, CB-0102=3.8%, CB-0104=10.9%, CB-0106=13.4%; CB-0107=3.2x, CB-0108=11.8x; B-0724=€1.07mn, D-WA-021=10.2%, B-0725=€681k.
- **(d) New derived** (unit "EUR thousand", dec 0):
  - D-WA-048 = `CB-0099*CB-0100/100` → 120
  - D-WA-049 = `CB-0101*CB-0102/100` → 184
  - D-WA-050 = `CB-0103*CB-0104/100` → 884
  - D-WA-051 = `CB-0105*CB-0106/100` → 1,409
  - Check: 11.76x, consistent with CB-0108's 11.8x.
- **(e) Redundant text:**
  - The last sentence of line 69 ("The 1QFY27 deck also claims {{CB-0107}}…").
  - The `p1h_fin` rows "Revenue, euros" and "EBITDA margin (company slide)".

### 7. `acq_margin` (chart) – `/home/user/sample/polymed-initiation/draft/21_A4_2_vascular_oncology.md`
- **(a) Where:** after the "**Links with the parent.**" bullets (ending "The 'P1H playbook'", line 74), before "### Oncology in Vision 2030…".
```
{"id":"acq_margin","type":"column","title":"The 'P1H playbook' took Plan1Health's margin from 4% to 13% in five years; PendraCare's fell to 1% in CY25 while Citieffe's held at 18%","cats":["CY20","CY22","CY24","CY25"],"unit":"EBITDA margin, %","dec":1,"series":[{"name":"Plan1Health (company slide)","facts":["CB-0100","CB-0102","CB-0104","CB-0106"]},{"name":"PendraCare (company figures)","facts":["-","-","D-WC-004","D-WC-005"]},{"name":"Citieffe (company, excl. one-offs)","facts":["-","-","D-WC-026","D-WC-027"]}],"label_all":true,"note":"PendraCare consolidated from 23-Sep-2025 and Citieffe from 7-Nov-2025, so CY24 is pre-deal. PendraCare CY24 is pro forma; CY25 margins are our calculation from the 1QFY27 deck's rounded figures. Citieffe on IFRS: {{D-WC-023}} (CY24), {{D-WC-022}} (CY25). Management puts the two new businesses at {{CA-0171|range}} and targets {{CA-0172|range}} in two to three years."}
```
- **Facts verified:** D-WC-004=14.1%, D-WC-005=1.0%, D-WC-026=17.9%, D-WC-027=17.8%, D-WC-023=16.0%, D-WC-022=15.8%. CA-0171 and CA-0172 are text ("around 12% to 14%", "around 18% to 20%").
- **(d) New derived:** none.
- **(e) Redundant text:** the restated margins in ch21 driver 4 (line 117), ch27 margin driver 1 (line 159) and ch28 margin driver 1 (line 137) can each become an EXREF.

### 8. `arc_cc` (table) – `/home/user/sample/polymed-initiation/draft/25_A4_6_anaesthesia_resp_critical.md`
- **(a) Where:** in "### Critical care: the growth project", after the "Launch date" bullet, replacing the "Scale claims", "Targets" and "Investment" bullets (lines 61-63).
```
::: table id="arc_cc" title="Critical care: management has reported launches, hires and hospitals reached, but no revenue against its Rs. 0.75-1bn ambition" note="As stated on each call; hires are shared with oncology or cardiology, and the 1QFY27 launch count includes infusion."
| Date | Launches and reach | People added | Revenue ambition or outcome |
|---|---|---|---|
| Aug-2023 (1QFY24 call) | {{CC-0562|range}} launches planned for FY24 | – | {{CC-0569|range}} in three to four years ("just making a guess"), at "a better margin" |
| Feb-2024 (3QFY24 call) | Soft launch completed | ~{{CC-0622|range}}, with cardiology | – |
| Jul-2024 (1QFY25 call) | "{{CA-0707|plain}}" | – | – |
| Feb-2025 (3QFY25 call) | – | ~{{CA-0574}}, with oncology | – |
| May-2025 (4QFY25 call) | – | {{CA-0540}} in FY25, with cardiology; "contribution is very less" | Growth of "{{CA-0506}}" hoped for FY26 |
| Aug-2025 (1QFY26 call) | {{CA-0441}} products in the prior 12 months | – | – |
| Nov-2025 (2QFY26 call) | {{CA-0351}} products in 12 months; {{CA-0352}} hospitals | – | Imports ~{{CA-0664|range}} of Indian demand (Oct-2024) |
| Aug-2026 (1QFY27 deck) | {{CB-0190}} launches across infusion and critical care | – | FY26 outcome [not disclosed] |
:::
```
- **Facts verified:** CC-0562="10-12", CC-0569="75-100 (Rs cr)" (renders Rs. 0.75-1.0bn), CC-0622="around 20", CA-0707="four to five products in each category", CA-0574=60, CA-0540=70, CA-0506="almost 2 and 1/2 times", CA-0441="over 20", CA-0351="20 plus", CA-0352=500, CA-0664="around 80%, 90%", CB-0190=6.
- **(e) Redundant text:** the three bullets named above.

### 9. `card_deal` (table) – `/home/user/sample/polymed-initiation/draft/27_A4_8_cardiology.md`
- **(a) Where:** in "### PendraCare…", after the "**The deal.**" sentence, replacing the five bullets (lines 63-67). It mirrors `ortho_deal` in ch28.
```
::: table id="card_deal" title="Polymed paid an enterprise value of about €18-19mn for 90% of PendraCare, 13x CY24 EBITDA, with earn-outs and a 2030 buy-out still to come"
| Item | Value | Source |
|---|---|---|
| Stake bought | {{A-0100}} of PendraCare Holdings and Wellinq Medical, via Risor Holdings BV ({{A-0864}} economic interest) | AR26; BRSR26 |
| Upfront equity; loans repaid; total upfront | {{CB-2484}}; {{CB-2485}}; {{CB-2486}} | Acquisition deck |
| Net external debt taken over | {{CB-2487}} | Acquisition deck |
| Enterprise value | {{CB-2530}} (press release); ~{{CB-2143}} (Sep-2025 AGM deck); {{CB-0111}} (1QFY27 deck) | Company |
| Multiples (company) | {{CB-2488}} CY24 revenue of {{CB-2477}}; {{CB-2489}} CY24 EBITDA of {{CB-2479}} | Acquisition deck |
| Deferred terms | Earn-outs over {{CB-2490}} years; remaining {{CB-2491}} bought in 2030 on calendar 2029 EBITDA; amounts [not disclosed] | Acquisition deck |
| Funding | {{B-0836}} from the Aug-2024 QIP, lent to Risor by Poly Medicure BV ({{B-0669}}) | Monitoring agency; BV accounts |
| Accounted consideration | {{A-0687}} cash plus {{A-0688}} contingent, total {{A-0689}} | AR26 note |
| Purchase-price allocation | Net identifiable assets {{A-0691}}, incl. product intangibles {{A-0690}}; provisional goodwill {{A-0692}} | AR26 |
| Management targets | EBITDA synergies {{CB-2506}} in three to four years; revenue {{CA-0812|range}} by 2030 | Deck; deal call |
:::
```
- **Facts verified:** A-0100=90%, A-0864=90%, CB-2484=€11mn, CB-2485=€3.2mn, CB-2486=€14.2mn, CB-2487=€2.9mn, CB-2530=€18.3mn, CB-2143=€18mn, CB-0111=€18.8mn, CB-2488=1.8x, CB-2477=€9.9mn, CB-2489=13x, CB-2479=€1.4mn, CB-2490="4-5", CB-2491=10%, B-0836=Rs. 1.5bn, B-0669=€14.6mn, A-0687=Rs. 1.5bn, A-0688=Rs. 314mn, A-0689=Rs. 2.2bn, A-0691=Rs. 629mn, A-0690=Rs. 365mn, A-0692=Rs. 1.6bn, CB-2506=€3-4mn, CA-0812="close to EUR25 million".
- **(e) Redundant text:** the deal bullets. In point 4 of "Four points stand out", the list of EVs can go, keeping only the Risor date conflict.

### 10. `inf_us_imports` (chart) – `/home/user/sample/polymed-initiation/draft/20_A4_1_infusion.md`
- **(a) Where:** in "### Market and competition", after numbered point 4 (line 224), before "Polymed's differentiation…". Inserting it inside the numbered list would break the numbering.
```
{"id":"inf_us_imports","type":"hbar","title":"India supplied 0.5% of US imports of catheters, cannulae and needles in 2025, about an eighth of what China or Malaysia shipped","cats":["China","Malaysia","India"],"unit":"US$ mn, CY2025","dec":1,"series":[{"name":"US imports, HS 901839","facts":["D-WA-031","D-WA-032","D-WA-033"]}],"label_w":90,"note":"UN Comtrade, US as reporter; converted from US dollars (our calculation). All suppliers, not only Polymed. Total {{F-0177}}; India's share {{D-WA-029}}; imports from India rose {{D-WA-034}} from {{F-0179}} in 2024. Larger sources (Mexico, Costa Rica, Ireland, Japan) are not in the ledger."}
```
- **Facts verified:** F-0178=$467.8mn, F-0181=$431.8mn, F-0180=$52.4mn, F-0179=$45.2mn, F-0177=$10.4bn, D-WA-029=0.5%.
- **(d) New derived** (USD mn, dec 1):
  - D-WA-031 = `F-0178/1000000` → 467.8
  - D-WA-032 = `F-0181/1000000` → 431.8
  - D-WA-033 = `F-0180/1000000` → 52.4
  - D-WA-034 = `(F-0180/F-0179-1)*100` → 15.9%
- **(e) Redundant text:** the last sentence of point 3 ("the US imported {{F-0181}}… of the {{F-0177}} total").
- **Option:** the source file `sources/text/F_CT_USA_M_901839_2025.txt` also lists Mexico, Costa Rica, Ireland and Japan (rows 1-4) and ranks India 17th. Adding those four as facts would turn this into a full supplier ranking.

### 11. `card_price` (chart) – `/home/user/sample/polymed-initiation/draft/27_A4_8_cardiology.md`
- **(a) Where:** after the "### Customers, channel and pricing" bullets (line 134).
```
{"id":"card_price","type":"hbar","title":"Polymed's drug-eluting balloon and IVL system sell for at least three times the capped price of a drug-eluting stent","cats":["Bare-metal stent, NPPA ceiling","Drug-eluting stent, NPPA ceiling","Polymed DEB and IVL, ASP floor"],"unit":"Rs per unit","dec":0,"series":[{"name":"Price","facts":["E-0172","E-0171","WC-0039"]}],"label_w":230,"note":"Ceilings as revised, per Frost & Sullivan's 2025 report for SMT; the DEB/IVL ASP is 'in excess of' the figure (MD, Feb-2026), {{D-WC-095}} the DES ceiling (our calculation). Indian stents typically sell for Rs. {{CA-0596|range}} (MD, Feb-2025). Pipeline products to be priced between {{WC-0040}} and {{WC-0041}}."}
```
- **Facts verified:** E-0172=10,510 Rs per stent, E-0171=38,267, WC-0039=Rs. 115,000, WC-0040=Rs. 100,000, WC-0041=Rs. 1.0mn. CA-0596 is text ("around Rs. 10,000 to Rs. 12,000").
- **(d) New derived:** D-WC-095 = `WC-0039/E-0171` → 3.0x.
- **(e) Redundant text:** the "Price points" bullet (line 133). Optionally, the `card_india` rows for the DES ceiling and the typical DES price.

### 12. `card_tiers` (chart) – `/home/user/sample/polymed-initiation/draft/27_A4_8_cardiology.md`
- **(a) Where:** in "### Market…", after "Three features of the market…" (line 127).
```
{"id":"card_tiers","type":"share_hbar","title":"Four-fifths of India's stent volume carries FDA or CE approval, which RisoR will lack until PACIFIER supports a CE filing","cats":["India stent volumes, 2024"],"unit":"% of volumes","series":[{"name":"US FDA-approved DES","facts":["E-0166"]},{"name":"CE-approved","facts":["WC-0028"]},{"name":"Low-cost stents","facts":["WC-0029"]}],"label_w":150,"note":"Frost & Sullivan for Integris Medtech (Oct-2025) [vendor estimate]. RisoR has Indian approval only, so on this taxonomy it sits in the low-cost tier until it wins a CE mark (our reading). The same report puts Indian companies at ~{{E-0164}} of DES volumes in FY25."}
```
- **Facts verified:** E-0166=30%, WC-0028=50%, WC-0029=20%, E-0164=60%.
- **(e) Redundant text:** the `card_india` row "Stent volumes by approval".

### 13. `inf_rebates` (chart) – `/home/user/sample/polymed-initiation/draft/20_A4_1_infusion.md`
- **(a) Where:** after the "Five points follow:" bullets (line 151), before "In India, Para 20…".
```
{"id":"inf_rebates","type":"column","title":"Standalone rebates and discounts have more than doubled in two years, though they are still under 1% of revenue","cats":["FY24","FY25","FY26"],"scale":"mn","unit":"Rs mn","dec":0,"series":[{"name":"Rebates and discounts deducted from revenue, standalone","facts":["A-0824","A-0480","A-0479"]}],"label_all":true,"note":"Standalone revenue notes, FY25 and FY26 annual reports; not split by product line. Share of standalone revenue from operations: {{D-WA-035}}, {{D-WA-036}}, {{D-WA-037}}; FY26 was {{D-WA-038}} FY24 (our calculations)."}
```
- **Facts verified:** A-0824=Rs. 53mn, A-0480=Rs. 73mn, A-0479=Rs. 116mn, A-0733=Rs. 13.1bn, A-0351=Rs. 16.0bn, A-0350=Rs. 16.6bn.
- **(d) New derived** (dec 1):
  - D-WA-035 = `A-0824/A-0733*100` → 0.4%
  - D-WA-036 = `A-0480/A-0351*100` → 0.5%
  - D-WA-037 = `A-0479/A-0350*100` → 0.7%
  - D-WA-038 = `A-0479/A-0824` → 2.2x
- **(e) Redundant text:** the numbers in the "Rebates are rising" bullet.

### 14. `dx_comp` (table) – `/home/user/sample/polymed-initiation/draft/24_A4_5_diagnostics.md`
- **(a) Where:** in "### Competition", replacing the four bullets (lines 61-64). Keep the closing paragraph at line 66.
```
::: table id="dx_comp" title="Polymed's collection range meets BD's $1.9bn specimen unit at the top and a Faridabad neighbour and Chinese tender winners below; none discloses Indian tube sales"
| Competitor | Where it meets Polymed | Scale and position |
|---|---|---|
| BD (US) | Vacutainer tubes, needles, wingsets, blood-gas devices; reported in Medical Essentials from Oct-2025 | Specimen Management {{E-0202}} (FY Sep-2025), up {{WG-0011}}; FDA warning letter open |
| Nipro (Japan) | Neotube vacuum tubes | Group revenue {{E-0264}}; tube sales [not disclosed] |
| Greiner Bio-One, Sarstedt, Terumo | Tubes and collection systems | Profiled by 360iResearch; no filed tube data |
| HMD (India, Faridabad) | Vaku tubes, needles, winged sets, holders (with Estar, Israel) | Operating income {{D-0501}} (FY23, CRISIL); exports {{E-0349}} |
| KDL (China) | Vacuum tubes, collection needles | Won every tube and needle category in a Liaoning-led alliance tender (CY25); {{WA-0016}} CE registrations incl. collection containers; revenue {{E-0280}} |
| Weigao (China) | Collection bundled with storage and separation | Blood management {{E-0270}} (CY25), up {{WF-0017}} |
:::
```
- **Facts verified:** E-0202=$1.9bn, WG-0011=2.0%, E-0264=JPY 660.5bn, D-0501=Rs. 8.5bn, E-0349=20.8%, WA-0016=22, E-0280=RMB 2.3bn, E-0270=RMB 995.1mn, WF-0017=13.5%.

### 15. `ortho_te` (chart) – `/home/user/sample/polymed-initiation/draft/28_A4_9_orthopaedics.md`
- **(a) Where:** in "### Market…", after the `ortho_share` chart (line 99), before the "Global" bullet.
```
{"id":"ortho_te","type":"column","title":"The global trauma and extremities market fell only 6% in the Covid year and has grown every year since, to ~$12bn in 2024","cats":["CY18","CY19","CY20","CY21","CY22","CY23","CY24E"],"unit":"US$ bn","dec":1,"series":[{"name":"Trauma and extremities market","facts":["CB-2412","CB-2415","CB-2418","CB-2421","CB-2424","CB-2427","CB-2430"]}],"label_all":true,"note":"Industry reports cited in the Citieffe acquisition deck (Sep-2025) [vendor estimate]; 2024 is an estimate; the deck's projections to 2028 are omitted. In 2024 trauma was {{CB-2431}} and extremities {{CB-2432}}. The segment fell {{CB-2445|abs}} in 2020 vs {{CB-2446|abs}} for all orthopaedics; orthopaedics {{CB-2379}} in 2024."}
```
- **Facts verified:** CB-2412=$9.5bn, CB-2415=$9.9bn, CB-2418=$9.3bn, CB-2421=$10.3bn, CB-2424=$10.8bn, CB-2427=$11.3bn, CB-2430=$11.9bn, CB-2431=$8.7bn, CB-2432=$3.2bn, CB-2445=-6.1%, CB-2446=-11%, CB-2379=$61bn.
- I used the printed totals rather than a stack: CY19's parts sum to 9.8 against a printed total of 9.9.
- **(e) Redundant text:** the Covid-dip sentence at line 23.

### 16. `oem_catalogue` (table) – `/home/user/sample/polymed-initiation/draft/29_A4_10_components_oem.md`
- **(a) Where:** in "### What Polymed offers…", replacing the component bullets (lines 19-23). Keep the paragraph at line 25.
```
::: table id="oem_catalogue" title="Nearly every component Polymed sells to other device makers also appears in its own branded range, from stopcocks to a drug-eluting stent"
| Component category (Nov-2024 catalogue) | Polymed-branded equivalent | Section |
|---|---|---|
| Diagnostic catheters | Concath | A4.8 |
| CVC catheters | Polymed CVC (one to four lumens), Novocent range | A4.2 |
| Haemodialysis catheters | Haemocent and Haemocent Pro ("also sold as components") | A4.3 |
| Midline, mini-midline, PICC | Poly Lead midlines; Polymed PICC and neonatal PICC kits | A4.2 |
| Anaesthesia conduction catheter | Epidural kit (launched FY26-FY27) | A4.6 |
| Cobalt-chromium stent, sirolimus or everolimus | Serolin Pro and RisoR DES (on sale from Mar-2025) | A4.8 |
| PTFE-coated and hydrophilic guidewires | Filoflex, Aquareach | A4.8 |
| Tear-away introducers, dilators | Tear-away introducers among recent launches | A4.2 |
| Stopcocks, flow regulators, T-connectors | Polyway stopcocks, Polyflo Novo, extension lines | A4.1 |
| Extruded tubing | In-house; a {{F-0017}} tubing project with a {{F-0018}} MIS-RID grant | A4.1 |
:::
```
- **Facts verified:** F-0017=Rs. 1.0bn, F-0018=Rs. 100mn. The brand mappings are taken from ch20, ch21, ch22, ch25 and ch27 as drafted.
- **(e) Redundant text:** the bullets. The grant sentence at line 27 shrinks to a clause.

### 17. `gus_premium` (table) – `/home/user/sample/polymed-initiation/draft/26_A4_7_gastro_uro_surgery.md`
- **(a) Where:** after the surgery section (line 70), before "### Competition…".
```
::: table id="gus_premium" title="Polymed covers the drainage segments FMI sees as largest but none of the premium urinary catheters; enteral connectors are its one upgrade under way"
| Line | Where the market is upgrading | Polymed's offer | Gap |
|---|---|---|---|
| Foley catheters | All-silicone, hydrophilic, silver-alloy/antimicrobial (Grand View cites CAUTI) | Two-way silicone-elastomer-coated latex only | No all-silicone, three-way, hydrophilic or antimicrobial; no suprapubic set |
| Intermittent catheters | Coated catheters | PVC Nelaton, female, rectal | No hydrophilic range |
| Urine collection | Closed systems with needle-free sampling | Polyuro Premium; Polyurimeter with closed sampling port | Covered |
| Enteral feeding | ISO 80369 (ENFit-type) connectors | Export catalogue range; Indian launches in the Sep-2026 AGM deck | Conformity [not disclosed]; absent from Oct-2025 domestic catalogue |
| Wound drainage | Active drains, {{WH-0009}} of FMI's market | Polyvac, Novovac, Neovac, Ultravak, Redon | Covered |
| Chest drainage | Thoracic and cardiovascular, {{WH-0010}} of FMI's market | Polyseal, Ultra Cath Novo | Covered |
:::
```
- **Facts verified:** WH-0009=57.6%, WH-0010=42.3%.
- **(e) Redundant text:**
  - Line 58: "The catalogues list no all-silicone…".
  - Line 60: "Of its segments (…), Polymed competes only in coated latex…".
  - Line 70: the WH-0009/WH-0010 clause.
  - Margin driver 3 ("Mix").

### 18. `inf_peers` (chart) – `/home/user/sample/polymed-initiation/draft/20_A4_1_infusion.md`
- **(a) Where:** after the `inf_comp` table (line 217), before "We draw four points…".
```
{"id":"inf_peers","type":"hbar","title":"Polymed's infusion line is a tenth of ICU Medical's consumables business and a fortieth to a fiftieth of BD's and B. Braun's infusion units","cats":["B. Braun Hospital Care (CY25)","BD Medication Delivery Solutions (FY Sep-2025)","ICU Medical consumables (CY25)","Polymed infusion (FY26)"],"scale":"bn","unit":"Rs bn","dec":1,"series":[{"name":"Revenue","facts":["D-WA-039","D-WA-040","D-WA-041","CB-0864"]}],"label_w":270,"note":"{{E-0242}}, {{E-0198}} and {{E-0209}} converted at RBI reference rates of 13-Dec-2025 ({{WD-0024}}, {{WD-0023}}), our calculation. Periods and scopes differ. Weigao ({{E-0269}}) and KDL ({{E-0280}}) are excluded: the ledger has no rupee-renminbi rate. Order of magnitude only."}
```
- **Facts verified:** E-0242=€5.1bn, E-0198=$4.6bn, E-0209=$1.1bn, WD-0024=Rs. 106.1/€, WD-0023=Rs. 90.5/$, CB-0864=Rs. 10.0bn, E-0269=RMB 6.4bn.
- **(d) New derived** (Rs mn, dec 0): D-WA-039 = `E-0242*WD-0024` → Rs. 540.2bn; D-WA-040 = `E-0198*WD-0023` → Rs. 414.0bn; D-WA-041 = `E-0209*WD-0023` → Rs. 100.4bn.
- **Overlap:** partly overlaps `b2_global` (ch41), which gives multiples of group revenue.

### 19. `inf_cn_in` (chart) – `/home/user/sample/polymed-initiation/draft/20_A4_1_infusion.md`
- **(a) Where:** after numbered point 4, just before `inf_us_imports`.
```
{"id":"inf_cn_in","type":"column","title":"China exports about five times India's value of catheters, cannulae and needles, and grew faster in 2025","cats":["CY2024","CY2025"],"unit":"US$ mn","dec":0,"series":[{"name":"China","facts":["D-WA-042","D-WA-043"]},{"name":"India","facts":["D-WA-044","D-WD-026"]}],"label_all":true,"note":"UN Comtrade, each country as reporter, HS 901839; converted from US dollars (our calculation). Country totals. 2025 growth: China {{D-WA-045}}, India {{D-WA-046}}; China {{D-WA-047}} India's. India's FY26 TradeStat figure ({{F-0182}}) uses a different source and period."}
```
- **Facts verified:** F-0165=$2.3bn, F-0166=$2.6bn, F-0133=$482.4mn, D-WD-026=$525.9mn (already exists, reused).
- **(d) New derived:**
  - D-WA-042 = `F-0165/1000000` → 2,322.4
  - D-WA-043 = `F-0166/1000000` → 2,602.5
  - D-WA-044 = `F-0133/1000000` → 482.4
  - D-WA-045 = `(F-0166/F-0165-1)*100` → 12.1%
  - D-WA-046 = `(F-0134/F-0133-1)*100` → 9.0%
  - D-WA-047 = `F-0166/F-0134` → 4.9x

### 20. `card_cathlabs` (chart) – `/home/user/sample/polymed-initiation/draft/27_A4_8_cardiology.md`
- **(a) Where:** next to `card_tiers`, after line 127.
```
{"id":"card_cathlabs","type":"column","title":"India's cath labs almost quadrupled between 2015 and 2023 but are a third of the number Frost & Sullivan says it needs","cats":["2015","2023","Needed"],"unit":"cath labs","dec":0,"series":[{"name":"Cath labs in India","facts":["WC-0030","E-0152","E-0153"]}],"label_all":true,"note":"Frost & Sullivan for Integris Medtech (Oct-2025) [vendor estimate]; 2023 and the need are printed as 'more than'. About {{WC-0031|range}} labs added a year. 2023 was {{D-WC-096}} the 2015 count and {{D-WC-097}} of the need (our calculation)."}
```
- **Facts verified:** WC-0030=650, E-0152=2,500, E-0153=7,500, WC-0031="200 to 250".
- **(d) New derived:** D-WC-096 = `E-0152/WC-0030` → 3.8x; D-WC-097 = `E-0152/E-0153*100` → 33%.
- **(e) Redundant text:** the `card_india` row "Cath labs".

---

## Further options, lower priority
- **`inf_scale` (ch20, hbar):** CA-0188=600mn units (Polymed), WA-0004=600mn units (B. Braun Penang), E-0301=36mn a year (HMD's 2014 plant, capacity). The bases differ; new derived `CA-0188/E-0301` → 17x.
- **`blood_sep` (ch23, column):** share of blood separated into components, WF-0010=52% (low-income), WF-0008=81% (lower-middle-income), WF-0009=98% (high-income). Source is WHO.
- **`oem_comp` (ch29 table):** Teleflex OEM, KDL, Caina, Angiplast, Lars, Iscon. It partly overlaps `b2_india` and `b5_deals`.
- **Citieffe receivables ageing (ch28):** needs 8 new base facts. SUB26MEDC p.16 gives the buckets in € '000 (not yet due / <30 days / 30-60 / 61-120): 2,279 / 306 / 323 / 369 in 2025 and 2,806 / 566 / 273 / 92 in 2024.
- **`card_stents` (existing chart):** could add the Aug-2025 point (CA-0438=1,350 units).

## Problems found while checking
- **ch29 line 58 contradicts the ledger and ch34.** It says Vitromed "is not a customer", but AR26 p.88 shows goods sold to it: A-0549=Rs. 229mn in FY26 and A-0550=Rs. 247mn in FY25. Ch34 line 88 and the `vitromed` table both say Vitromed buys goods from Polymed.
- **ch25 line 55 overstates the line's growth.** "Roughly in line with the group" is not supported; see #5.

## Gaps: chapters where the data cannot support (more) charts
- **ch26:** no volumes, prices or margins beyond `gus_rev`. The vendor market sizes come from four different vendors (Grand View, IMARC, 360iResearch, FMI) and are largely forecasts. The F&S urology data are a 2020 vintage, marked "historical context only", and use mixed bases. That is why ch26 gets a table only.
- **ch29:** component, CDMO and OEM revenue are undisclosed. The CDMO market figures (A-0203 "<100" US$ mn; A-0204 "6-7" US$ bn for 2035F) are text and forecasts. Sales to Plan1Health exist only for FY24 and FY26.
- **ch24:** the FY22 revenue statements are text ranges (CC-0215, CC-0191, CC-0286). The PLI-implied sales figure is a single point (D-WG-004). Tests per capita are text ("less than 5"). The tube-market numbers are 360iResearch forecasts.
- **ch25:** critical-care revenue has never been disclosed; the launch counts are text. The ETT and face-mask market sizes come from different publishers.
- **ch20:**
  - The flush-syringe share is a single point (A-0870).
  - The cannula share after FY16 is a text range (CA-0745).
  - US revenue targets and outcomes, and price-increase history, are text ranges.
  - The three PIVC vendor market sizes cannot share an exhibit.
  - Weigao and KDL need a rupee-renminbi rate.
- **ch21:** vascular and oncology revenue is undisclosed at group level; the port, PICC, CVC and sheath market sizes come from different publishers and years.
- **ch27:** cardiology revenue has only two quarterly points (1QFY26, 1QFY27).
- **ch28:** Citieffe revenue exists only for CY24-CY25.