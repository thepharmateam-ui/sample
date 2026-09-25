# Adversarial review R2 – A4.1, A4.2, A4.3, A4.6, A4.8, A4.9, A4.10, A5, A6

Reviewer: R2. Date: 24 Sep 2026. Scope: draft/20, 21, 22, 25, 27, 28, 29, 30, 31.
Format: file | problem | fix (or "left, because …").

## Summary
- Tokens traced: about 150 by hand to the cited source page, weighted to the snapshots, exhibit titles and ranked drivers. Visual-read slides and pages were rendered and checked: DK1Q27 pp.6, 12, 14; DK4Q25 p.11; DK4Q26 pp.38-39; DKAGM31 p.17; AR26 pp.15, 44, 45, 47, 48, 49; SUB26US p.2; PPP_MD_LC21B p.9. A mechanical re-find covered all 1,273 facts used in the nine files, with 0 failures.
- About 95 issues were fixed. By type:
  - factual or attribution errors against the source: ~28;
  - fabricated or non-verbatim quotes: 11;
  - inference, causality or judgement stated as fact: ~20;
  - cross-chapter contradictions: 8;
  - vendor or third-party data without source or vintage: 4;
  - wrong period labels: 3;
  - rating or valuation language: 2;
  - numbers typed or written in words: 4;
  - rendering glitches: ~18 instances.
- One new ledger fact: WRB-0001 (US medtech R&D intensity, AR26 p.45, visual read).
- Final checks: reconcile problems 0; lint 0 errors in the nine files; test build unresolved tokens=0; audit 0 UNTRACED.
- Most serious issue: A4.2 and A5 said Plan1Health sells direct in Italy. DK4Q26 p.39 gives that direct presence to Citieffe; Plan1Health sells through its 20+ distributors. The error carried into A4.2's Italian payback-exposure and EU-tender arguments. The next most serious: a fabricated slide quote in A4.2 (the Class III OEM line) and a garbled Teleflex divestiture in A4.6.

## Findings log

### A4.1 Infusion (draft/20)
- 20 | Price points Rs. 10-20 stated as fact ("Infusion devices sell at…"); source is the MD's "let's say INR10, INR15, INR20" (TR4Q26 p.18) | reworded as the MD's illustrative price points (snapshot, prose, Maharashtra bullet).
- 20 | "so the mark-up accrues to distributors and hospitals, not to Polymed" stated as fact | marked "we infer" and narrowed to hospital and any distributor.
- 20 | Chart title "the 1QFY27 pick-up came from India"; MD said growth "reflects the performance both domestic and internationally", led by domestic (TR1Q27S p.3, p.6) | title now "led by India"; 1QFY27 bullet attributes both.
- 20 | FY26 slowdown causes stated flatly ("was driven by Europe…") | attributed to management ("mainly because of slowdown in Europe", TR1Q26 p.6).
- 20 | "Infusion is overwhelmingly an export business" inverted what the data show (infusion = 80-90% of exports) | rewritten: exports are overwhelmingly infusion; share of infusion earned abroad flagged as our inference.
- 20 | Weigao "flush-syringe prices fell sharply after the latest VBP round" embellished WEIGAO_IR26 pp.21-22 | softened to Weigao's own words (VBP pricing hit flush-syringe revenue; lower prices among GM reasons).
- 20 | Contradiction inside chapter: "in FY22 [price increases] reached only ~25-30% of customers" vs table "5-7% for most customers" in FY22; the 25-30% remark (May-2023) is about the FY22-FY23 cost spike (TR4Q23 p.12) | rewritten with both statements dated and attributed.
- 20 | "Typical annual price increase 3-4%" is the domestic blended portfolio (TR3Q25 p.9) | row label now says domestic.
- 20 | US distributor contract "was worth ~$15mn" – source says "potential of revenue USD 15 million over five years" (TR1Q23 p.12) | reworded as management's potential revenue.
- 20 | MDR counts: "20 new products filed for approval in 2026" wrong (filed early 2025, CE marks due 2026, TR2Q26 p.10); "~25 more awaiting CE marking" asserts they are additional, not stated; ~75 CE products (Nov-2025) contradicted A5's 89 (DKAGM30) and 82 (DK4Q26) without comment | rewritten with dates, overlap flagged as unstated, company counts cross-referenced to A5.
- 20 | "so the room for import substitution lies in Polymed's core line" – our inference stated as CRISIL's | marked "in our view".
- 20 | "Trade data agree" (that SE Asia gained) – one-year levels cannot show a shift | reworded to what the data show (scale gap).
- 20 | "In 2024 Polymed was pursuing a criminal complaint against B. Braun" – complaint filed Nov-2012, dismissed 2014, still listed in PD24 p.246 | re-dated.
- 20 | F&S wage data without vintage | "(Frost & Sullivan, 2024 data)".
- 20 | Cross-chapter: margin driver presented 200+→530+ assembly machines as a rise; A6 reads the Aug→Nov-2025 step as a counting change | caveat and A6 cross-reference added.
- 20 | Gamma plant: "management cites both quality control and savings" – management cites control and safety vs EtO only (TR1Q25 p.3; TR1Q26 p.7); A6 says savings undisclosed | fixed.
- 20 | "Freight rose sharply in FY26 even though export prices are quoted ex-factory" – muddled causal claim | replaced with MD's statements (customers pay most freight, TR3Q24b p.15; "freight crisis", TR3Q26 p.8; "some disruption", TR4Q26 p.6).

### A4.2 Vascular access and oncology (draft/21)
- 21 | Fabricated quote: "a Class III implantables specialist and sole approved supplier to one of the largest OEMs…" not on DK1Q27 p.12 / DKAGM31 p.17 | replaced with the slides' verbatim phrases.
- 21 | "Italy: it [Plan1Health] gives the group its only direct sales operation in Europe" – DK4Q26 p.39 shows the direct presence in Italy is Citieffe's; P1H sells via 20+ distributors | corrected, cross-referenced to A4.9; P1H plan (more tenders, launches in Italy) added.
- 21 | Payback and IPI bullets rested on "Plan1Health sells directly to Italian hospitals" (unsupported) | rewritten: exposure inferred from P1H's tender plans and Citieffe's direct Italian sales, [not disclosed]; BD settlement dated (2015-18, Jun-2025 decree); Confindustria figure given vintage.
- 21 | "Alessandro Balboni, founder" – DKNOV20 p.9 gives CEO P1H, MD EMEA, ex-CEO Delta Med SpA and Paul Hartmann SpA; no founder claim | "founder" removed, background added.
- 21 | Causal claim "because these carry higher gross margins than infusion" – MD said the focus "helps us to even get a better gross margin" (TR4Q26 p.10) | attributed, comparison to infusion removed.
- 21 | Quote "currently made in Italy" is not in any source (TR2Q25 p.8: "products which we are making in Italy today") | quotes corrected in two places.
- 21 | Growth driver 2 levers ("new MDR filings for oncology, neonatal and pain products and cross-selling Polymed products through Plan1Health in Italy") not in cited TR2Q26 pp.9-10 | replaced with the company's stated P1H levers (DK4Q26 p.39) and its 1-product EU pipeline.
- 21 | Margin driver "Management expects moving labour-heavy processes to India" – not stated; slide lists "leveraged India manufacturing to reduce cost" | reworded to the slide and the MD's shift plan.
- 21 | Risk driver "This offsets part of the gain" stated as fact | "could offset"; exposure [not disclosed].
- 21 | Teleflex $917.7mn called "Arrow-branded vascular catheters" – it is the whole Vascular product category (incl. tip positioning, intraosseous, and recast anaesthesia items) | relabelled.
- 21 | Quoted margin claims ("almost 16-17%") not verbatim | quote marks removed, range formatting used.

### A4.3 Renal (draft/22)
- 22 | Opening stated as fact that pricing "is set by Chinese imports that enter duty-free through South-East Asia"; the chapter itself later says the trade data are "consistent with management's account… not proof" | attributed to management in the opening.
- 22 | Session length "three-to-five-hour" – RHP says "3 to 4 hours" (RHP_NEPHRO p.268); cited p.334 has no duration | corrected and re-cited.
- 22 | "against the two to three sessions a week that is typical" – RHP gives three a week as the "standard requirement" (p.268) | corrected.
- 22 | "Renal capacity was tripled over FY22" stated as done; source is a Jul-2021 plan (TR1Q22 p.3) and May-2022 outcome "almost double" (TR4Q22 p.18) | reworded as plan vs outcome.
- 22 | Margin driver "Capacity has doubled more than once since FY22" rests on plans and management statements | attributed ("on management's statements").
- 22 | Rendering: double tildes "~~Rs. 1.0bn", "~~Rs. 900mn", "~~Rs. 1.8bn", "~~Rs. 10.0bn" (typed ~ before |range tokens that already carry ~) | typed ~ removed.
- 22 | Rendering: "over 500+", "Over 350+", "more than 600+", "30++ engineers", "more than 50%+" (typed qualifiers duplicating the token's +) | duplicates removed.
- 22 | Rendering: "8mn units to 12mn units dialysers", "~1,100 units machines", "450 units machines", "~450mn units dialysers", "110,000 units haemodialysis machines", "~67.8mn units fistula needles" | switched to |num.
- 22 | FY26 quarters "sum to Rs. 1.9bn, slightly above the annual Rs. 1.9bn" (both rounded alike) | shown in Rs mn.
- 22 | Quarterly chart note said FY26 quarters came from "the following year's presentation" – 2Q-4QFY26 come from the FY26 decks | note corrected.
- 22 | PSC CKD recommendation paraphrased as "home PD as first-line therapy" – report says "preferred first-line renal replacement therapy for clinically suitable patients" (PIB_PSC176_2608, 177th report) | quoted with the qualifier and report number.

### A4.6 Anaesthesia, respiratory and critical care (draft/25)
- 25 | Teleflex deal mis-stated: $530mn buys Acute Care and Interventional Urology, and the $1.5bn is a separate OEM sale to Montagu and Kohlberg, not "a $1.5bn sale of its OEM unit and other divestitures" (TFX_10K25) | corrected.
- 25 | "Indian demand is almost entirely imported (80-90%)" overstates the MD's "around 80%, 90% import dependent" (TR2Q25 p.8) | "largely imported"; ICU-bed share (Jul-2021) dated.
- 25 | Cross-chapter: CRISIL quoted here as saying MNCs and imports dominate consumables, while A4.1 quotes CRISIL's imports at 30-40% of consumables (PD24 pp.134, 139) – both are in CRISIL, conflicting | both figures now shown here.
- 25 | "nebuliser marked up 1,688% (maker not named)" – the press report names the brand (Nebplus), which is not in Polymed's catalogues | corrected, catalogue cited.
- 25 | Quote "started FY25" not in TR4Q25 p.4 (MD: "which just started last year") | verbatim quote used.

### A4.8 Cardiology (draft/27)
- 27 | Snapshot attributed the 1QFY27 jump only to PendraCare; the MD cited PendraCare "together with genuine scale up of domestic business" (TR1Q27S p.3) | both drivers attributed.
- 27 | "Data follow at least a year after the last implant" – management said "6 months to 1 year" (TR2Q26 p.15) | corrected and attributed.
- 27 | PendraCare "describes itself as one of the few independent makers" – it is Polymed's description (DKAGM31 p.17; TRPEN p.2) | re-attributed.
- 27 | Risor "owned by Poly Medicure BV" – AR26 note 38.2 and BRSR show 90% (directors' report says wholly owned) | stake token and the conflict added.
- 27 | Capacity "1.5 mn units/year" printed as ">1.5 million" (DKAGM30 p.8) | "more than".
- 27 | NPPA cap cut prices "by 85%" – F&S says "by up to 85%" (DRHP_SMT p.178) | "up to".
- 27 | Vendor catheter CAGR 10.6% presented as current growth – it is F&S's 2024-2029 forecast | labelled as a forecast.
- 27 | "Management promised EUR 3-4mn synergies" – deck says "Expect to generate" | "targeted".
- 27 | Margin driver "DEB, IVL and PendraCare… sit well above capped stents" – no product margins disclosed | marked our view, [not disclosed].
- 27 | "cardiology capacity will move to" YEIDA – MD: "expand our cardio business… out of the Noida facility" (TR1Q27S p.15) | "expand into".
- 27 | Chart plotted Nov-2025 "YTD ~4,300" as cumulative without saying so (DK2Q26 p.6) | note now says year-to-date.
- 27 | Cross-chapter date conflict, left: PendraCare closing is 22-Sep-2025 in AR26 note 38.2 (used in A9) but 23-Sep-2025 in the decks (used here, A1, A3, A5); Citieffe 6-Nov (AR26) vs 7-Nov (decks). Left, because both are sourced; A4.9 now says "since acquisition" where it quotes AR26 figures. Owner of A9/A1 should pick one convention.

### A4.9 Orthopaedics (draft/28)
- 28 | Snapshot and text dated the AR26 contribution "from 7 Nov 2025 (annual report)"; AR26 says from the date of acquisition, 6-Nov-2025 (7-Nov is the decks' consolidation date) | re-labelled "from acquisition (6 Nov 2025 in the annual report)".
- 28 | "a complete trauma-implant franchise" contradicts the chapter's own "only one plate" (plates ~40% of trauma per management) | qualified.
- 28 | "The investment case rests on…" – rating-style language in a no-rating report | "The growth plan rests on…".
- 28 | CEO "has run Citieffe since 2019" – slide: "In Citieffe since 2019 ~34+ years of work experience" (DKAGM30 p.4) | reworded, "more than".
- 28 | Plates share (management statement, TRCIT p.7) grouped under "vendor estimates quoted by the company" | re-attributed to management.
- 28 | Gross-margin conflict omitted: AGM deck prints Citieffe CY25 gross profit EUR 16.6mn on EUR 17.7mn (DKAGM31 p.17) vs EUR 12.1mn in DK1Q27 p.14 | both shown (mirrors A4.8's treatment of PendraCare).
- 28 | "rather than on price" – no source says Citieffe does not compete on price | removed; claims attributed to the company.
- 28 | "double the business within five years, to EUR 25-30mn" – TRCIT gives both "double the business" (p.5) and "25 to 30 million" from "17, 18 million" (p.9), which is less than double | inconsistency shown; p.8 cited for "without any significant capex".
- 28 | Margin driver "moving labour-intensive steps to India" – MD: "some part of manufacturing, we will probably ship to India… once we have all the regulatory clearances" (TR4Q26 p.18) | reworded.

### A4.10 Components, OEM and contract manufacturing (draft/29)
- 29 | Quote "sole approved supplier to one of the largest OEMs…" not verbatim (DK1Q27 p.12: "Sole approved supplier for one of the largest OEM for Class III implants") | verbatim.
- 29 | CDMO market size (<$100mn 2025; $6-7bn 2035) carried no source or vintage – "a study cited in the FY26 annual report" | named: BCG-KIHT "Poised for Takeoff", May-2026 (AR26 p.44, visual check).
- 29 | "The FDA found at least 41 US complaints" – the warning letter says the firm received at least 41 complaints, found on inspection (FDA_WL_CAINA) | reworded.
- 29 | "Polymed's advantage over the Indian contract makers is its regulatory file" – judgement stated as fact | marked our view; plant MDR status attributed to the company (AR26 p.35).

### A5 Geographies and entities (draft/30)
- 30 | "Italy, through Plan1Health and Citieffe, is the only European market where the group sells direct" – DK4Q26 p.39: direct presence in Italy is Citieffe's; P1H uses 20+ distributors | corrected (same error fixed in A4.2).
- 30 | Cross-chapter: MDR transition deadline said to "matter most for Citieffe's implants", while A4.9 (and DK4Q26 p.39) say Citieffe's whole portfolio is MDR-approved | rewritten: P1H and Citieffe whole portfolios approved; PendraCare's pipeline most exposed.
- 30 | "Polymed's standalone business sells little through EU tenders today" – not stated in the cited sources | recast as our inference from the company's own tender strategy slide.
- 30 | ASEAN sentence misattributed: B. Braun describes "enormous pricing pressure" and Chinese share gains in ASEAN, not "Chinese makers have built plants in ASEAN countries"; Weigao JV "starts" – it is due to start (WEIGAO_IR26 p.34) | corrected.
- 30 | Rendering: "more than 25+ clinical staff" | duplicate removed.
- 30 | "Direct selling raises gross margin but adds fixed sales cost" – judgement stated flatly | marked our view.
- 30 | Entity table "Acquired 3 Sep 2025" for Risor/PendraCare is the SPA date; AR26 note 38.2 closing is 22-Sep-2025 | SPA, closing and deck consolidation dates all shown.

### A6 Manufacturing, capacity and R&D (draft/31)
- 31 | Opening "sell a cannula at a few rupees and still earn a mid-to-high-twenties operating margin" – numbers typed in words, causal claim stated as fact | tokenized (MD's Rs. 10-20 illustration; standalone EBITDA margin A-0311) and marked our view.
- 31 | "Sterilization moved in-house in 2025" – only Phase I (Class A/B licence) started Aug-2025; share in-house undisclosed | "began moving in-house".
- 31 | New plants "come on stream" – guidance | "are due on stream".
- 31 | "R&D spend is low by global standards" – no comparator given | added the AR26 MD&A comparators (India 2-4%, US 10-15%) with a new fact WRB-0001 (AR26 p.45, visual read) and "no source cited" caveat.
- 31 | A-0236 attributed to "the industry study cited in the annual report" – AR26 p.45 cites no source | corrected.
- 31 | Cross-chapter contradiction: "Renal capacity… is running out" (Aug-2025 statement, present tense) vs A4.3's under-absorption with capacity doubling and flat renal revenue | dated, and noted Palwal is now described without renal (TR1Q27S p.15); constraint read as less pressing (our view).
- 31 | "fell to 1.6x as capacity ran ahead of revenue" – AR26 p.48 gives no reason (checked visually) | marked our reading.
- 31 | Employee cost +29% attributed only to the wage rise; MD also cited headcount (TR1Q27S p.3) | both drivers.
- 31 | Approvals table "Product registrations in more than a hundred countries" – untokenized number in words, unsourced | replaced with A-0005 (sales in 125+ countries) and "registrations by country not disclosed".
- 31 | Driver 1 "which is why FY27 capex guidance is lower" – our causal link; MD's reason is that plants are nearly ready (TR4Q26 p.7) | attributed, citation added.
- 31 | "PACIFIER… the largest study Polymed has run" | qualified with the MD's "first… of this scale in India" (TR1Q26 p.6) and "disclosed".
- 20 | Numbers typed in words: "roughly three times its European price… a quarter of it in Africa" and "more than twenty firms" on the PPP cannula list | replaced with the price tokens (CC-0451/0452/0453) and "one of many firms" (list checked visually, PPP_MD_LC21B p.9; it also includes ophthalmic-cannula makers).
- 20 | "a move into a higher price tier, not just more volume" (not-X-but-Y construction, unlabelled judgement) | reworded, marked our view.
- 30 | "the currency crisis of 2024" – MD spoke in Feb-2024 of a then-current "currency crisis globally" (TR3Q24b p.14) | re-dated as the Feb-2024 statement.
- 30 | FDA lab-result statement cited to TR2Q26 p.10; it is on p.11 | citation corrected.
- 27 | Entry date: "entered cardiology in 2024" (AR26 timeline) conflicts with PD24 p.167 ("In Fiscal 2023, we expanded into cardiology"); A4.6 flags the same kind of conflict for critical care | both dates now shown.
- 31 | "India has 10 [plants], which includes the R&D centre" – AR26 p.15 (visual) pictures the R&D centre, Haridwar Plant 2 and the gamma plant around the production sites without itemizing the 10; AR26 p.58 lists Units I-IX | stated as not itemized (snapshot and text).
- 20 | Quote "more automation" not verbatim (TR4Q26 p.7: "pushing more on automation… mitigate some wage revisions") | verbatim quote used.

### Systematic checks across all nine files
- all | Verbatim-quote sweep (every quoted phrase normalised and searched in sources/text): fixed non-verbatim quotes in A4.2 ("under evaluation" – slide says P1H is "evaluating product submissions for FDA approvals", i.e. no filing disclosed; meaning was also wrong), A4.3 ("no significant service revenue"), A4.6 ("at a better margin", "with little contribution yet", "two and a half times"), plus the earlier A4.1/A4.2/A4.10 cases. Only editorial "[s]" brackets remain.
- all | Mechanical re-find of all 1,273 facts used in the nine files: 987 re-found on the cited page, 148 visual reads (headline ones checked by rendering: DK1Q27 pp.6, 12, 14; DK4Q26 pp.38-39; DKAGM31 p.17; AR26 pp.15, 44, 45, 47, 48; SUB26US p.2), 138 derived; 0 failures.
- all | Rendering sweep of every |range token in context: fixed doubled "~" and doubled "+/over/more than" qualifiers (renal, A5).
- 20 | Checked, left: "top five products earned Rs 9.6bn" (CB-2576) – tile "Growth in Top 5 Products 959.4" with deck-wide "Figs in Rs. Crs"; unit is the slide's default, standalone basis not footnoted (DK4Q25 p.11, rendered). Left, because the sentence does not claim standalone.

### Left unfixed (and why)
- Cross-chapter date convention for acquisitions (outside my files): A9 uses AR26 note 38 closing dates (PendraCare 22-Sep-2025); A1/A3 and my files use the decks' and AR26 MD&A's consolidation dates (23-Sep, 7-Nov). Both sourced; my files now show both where AR26 contribution figures are quoted. A9 owner should align.
- A4.8 "We therefore do not expect European sales of the RisoR stent before FY29" – a timing judgement, not a financial estimate; kept as our view with the arithmetic shown.
- A4.3 "Renal is… until FY26, its fastest-growing one" – consistent with DK1Q27 p.6 CAGRs (renal 39% vs others 23%); kept.

## Questions a PM would still have

**A4.1 Infusion**
- What is IV-cannula revenue today, split conventional / safety / blood-control / closed, and the realized price per unit in Europe vs the US? The only share (25-30%) is a Jul-2024 aside.
- How much of FY26's -1.5% was price vs volume, and how much of the FY27 3-5% price increase sticks against ~20% raw-material inflation?
- What was reclassified from infusion to "others" (Rs 399mn gap between summed quarters and the annual figure)?
- Where is the flush syringe (10.2% of standalone turnover, ~Rs 1.7bn) sold, how fast is it growing, and why is there no US 510(k)?
- What is infusion's gross margin versus the diversifying lines? Management implies the new lines lift group gross margin but never quantifies it.
- How much European infusion revenue is white-label, and how concentrated is it in the top five distributors?

**A4.2 Vascular access and oncology**
- What is group oncology and vascular-access revenue, including Polymed's own CVCs, midlines and Huber needles sold in India?
- How big is the Class III OEM contract within Plan1Health, and what are its term and exclusivity?
- Which definition produces management's 16-17% Plan1Health EBITDA against 13.4% on the company slide?
- Which Italian products move to India, and when are the Indian approvals expected?

**A4.3 Renal**
- What is the split of renal revenue between dialysers, bloodlines, fistula needles, HD catheters and machines, and what are the dialyser volumes?
- Is renal profitable at gross-margin level after the 1QFY27 price increase? How does this square with the DGTR petition's CY25 losses?
- What share of consumables goes to PPP operators, chains and government-run centres, and on what payment terms?
- What is utilization of the renal lines after the FY26 capacity doubling, and is renal still part of the Palwal plan?

**A4.6 Anaesthesia, respiratory and critical care**
- What were critical-care revenue and growth in FY26, against the "almost 2 and 1/2 times" ambition?
- Where did the anaesthesia and respiratory line go in the FY26 BRSR?
- How large is US private-label supply of Class I respiratory items (the McKesson listing)?

**A4.8 Cardiology**
- How does 1QFY27 cardiology revenue (Rs 286mn) split between PendraCare and India, and what are monthly DES volumes and realized stent prices?
- What is the bridge from PendraCare's CY24 EBITDA of EUR 1.4mn to ~EUR 84k in CY25, and what is the FY27 plan now that guidance has been withheld?
- What are the earn-out amounts, and what formula prices the 2030 buyout of the CEO's 10%?
- Which cardiology devices are made in-house, which by PendraCare and which bought in?

**A4.9 Orthopaedics**
- Which one-offs reconcile the company EBITDA (EUR 3.15mn) with the IFRS-derived figure (EUR 2.72mn)? The deal price was set on the adjusted number.
- What gross margin is right: the AGM deck's EUR 16.6mn, the 1QFY27 deck's EUR 12.1mn, or the 90%+ given at the deal?
- Who owes the receivables that are more than 120 days overdue (51% of gross, 24% covered), and are they Italian public hospitals?
- What is the plate launch timeline and approval route, and how does FY27 guidance of 10-12% square with the "mid- to high single digits" Citieffe was growing at in Aug-2026?

**A4.10 Components, OEM and CDMO**
- What are the current own-brand and OEM shares (last disclosed for FY22), and what is the margin gap between them?
- What are the economics of the two CDMO contracts: design fees against supply margins, 510(k) status and exclusivity?

**A5 Geographies and entities**
- What is revenue by country for the top ten markets, and what are US, West Asia and Latin America revenue in rupees?
- Which subsidiary took the ~Rs 90mn one-off provision in 4QFY26, and what was it for?
- Will the China plant close or renew its licence, and what would exit cost?
- What is the investment and breakeven plan for Brazil's direct model?

**A6 Manufacturing and R&D**
- What are capacity and utilization by unit today? The last certified data are FY24.
- How are "automatic assembly machines" counted? The count went from 200+ to 500+ in one quarter.
- What share of output is now gamma-sterilized in-house, what does it save, and when do the Class C/D licences come?
- Are needles drawn and ground in-house?
- What are the capex and commissioning plans for Palwal and YEIDA, and what product moves to each?
- How much of the planned doubling of R&D is expensed versus capitalized?
- 25, 28 | Verbatim quotes introduced digits ("almost 2 and 1/2 times", "in the next 5 years") that the audit flagged as untraced | first replaced by its token (CA-0506); second quote trimmed to "double the business".
