# Source audit log: Vitamin D3 supply landscape

Output: `Vitamin D3 supply landscape sourced.md` (with `sources.json`). Audit date: 21 Oct 2026.

## Counts

| Item | Original | Sourced version |
|---|---|---|
| Linked citations (link instances) | 178 | 619 (+441) |
| Unique source URLs | 96 | 119 (+23, all taken from the research notes) |
| Explicit calculation notes | 0 (10 "my arithmetic / my conversion / on my numbers / my inference / my rough estimate" tags) | 40 (all vague tags removed) |
| "Analyst inference, based on …" labels | 0 | 82 |
| Absence-of-evidence tags ("not found in sources searched to Oct 2026") | 0 | 13 |
| Tables with a per-row Source column | 1 (price history) | 5 (capacity, routes, segments, price history, competitor scorecard) |

- FX assumptions are stated in each calculation that uses them: RMB 7.2/USD and ₹88/USD.
- The EUR-Lex URL is now percent-encoded (`2%281%29`).
- All 96 original URLs are kept.
- Headings are unchanged and carry no citations. Every heading claim is cited in the body directly beneath it.
- Short signpost sentences were merged into the cited sentence that follows them (e.g. "Several things are absent: …").

Spot-checks against the primary text:

- **Extracted documents in the scratchpad:** Garden IR (Apr 2025 and Apr 2026), Fermenta AR FY26 and Q1FY27, Tianfeng, Pacific Securities, ICICI Direct, the Symbiotec RHP and ICRIER PB55.
- **Fetched live:** the EDQM cholecalciferol CEP page and the SAMR decision.
- **Re-parsed:** the FDA Q3 2026 DMF spreadsheet.

## Claims rewritten or deleted

**Summary**

1. "Demand of roughly 7,000–10,800 t … running at about half its capacity" became "6,750–10,800 t … roughly half to three-quarters". BP's figure is 6,750 t. Utilisation is 6,750/14,600 = 46% and 10,836/14,740 = 74%.
2. The DSM cutback sentence cited Garden IR Apr 2025, which does not support it. It now cites Dongwu Securities and the dsm-firmenich press release. "So Fermenta is the only large integrated maker" is split out and labelled as inference.
3. "Yeast-fermented D3 has not been launched commercially" became "no commercial launch … was found". This is absence of evidence.
4. "₹7–90 cr" became "₹7–88 cr": 1 t × USD 800–10,000/kg × ₹88.

**Capacity and producers**

5. "Chinese broker tables are the only producer-level capacity data" became "the main". BP Equities is an Indian broker, and Kingdomway's AR discloses its own capacity.
6. "Other totals range from 10,840 t to 12,800 t" became "include". The notes also contain ~10,000 t and 17,300 t totals from lower-quality sources.
7. Capacity table:
   - Hisound "Sets prices for the market" became "Price leader in 2025 (quote raised to RMB 600/kg)".
   - DSM "Brokers report" became "Dongwu reports", since there is one broker source.
   - DSM "buys D3 from Garden" became "D3 supply contract with Garden renewed Apr 2026", which is what the IR record says.
8. "India has one producer" became "one scaled producer". Fermenta says it was "until very recently" India's only maker.
9. Deleted: SAMR HHI "(based on output shares)". The decision does not state the basis (checked on the fetched page).
10. "The lapse coincided with the stop-quoting stance from May 2024" was corrected. The lapse (Oct 2019 + 5 years = Oct 2024) fell within the period that began in May 2024; the two did not coincide.
11. dsm-firmenich "pushed back to mid-2026, not cancelled" became "still described as delayed in June 2026". "Not cancelled" was an interpretation.
12. "Chinese brokers report DSM shut D3 capacity" became "A Chinese broker, Dongwu Securities, reports".
13. The Garden–DSM 10–15-year agreements predate the April 2026 D3 renewal (Sina, Jul 2024; IR Apr 2025). They are no longer presented as part of it.
14. DSM CEPs "that name Sisseln, one revised Feb 2026" was corrected. EDQM shows "Site Sisseln" only on CEP 2019-351 (Jul 2025). CEP 2009-050 (Feb 2026) names no site.

**Non-animal D3**

15. Absence claims were reworded as "was found":
    - AIDP "the only named B2B algae D3 ingredient";
    - fermentation "has no commercial D3 product";
    - "no public bulk price exists";
    - "India has no anti-dumping duty on D3", which is now "no current duty was found", since India had an AD3 duty in 2002;
    - "D3 does not appear among the 41 PLI products", since the official schedule was not retrieved;
    - EU status "unresolved", which is now "no EU Novel Food decision was found".
16. Feed D3 "selling at" USD 0.065/MIU became "quoted at". The Garden IR figure is a quote raised by an investor; Garden said it prices at market.
17. "Pine oil, which is a phytosterol source" is now a separate sentence labelled as inference, because Innobio does not disclose its process.

**Volume and value**

18. "Early-2025 traded level of ~RMB 250/kg" became "quoted level", in the text and the table. Longzhong's transaction price was RMB 220–240/kg.
19. The human-grade market changed from "USD 130–150m" to "USD 130–140m", and Fermenta's revenue from "≈USD 33–34m" to "≈USD 33m". The arithmetic is ₹2,930m ÷ 88 ÷ 25% = USD 133m, or USD 138m at ₹85; USD 150m cannot be derived. This flows through:
    - the producer-level market moves from "~USD 200–400m" to "~USD 230–400m" (USD 233–405m);
    - "lichen parity equals the human-grade market" becomes "is close to it".
20. Garden customers "under long-term agreements" became "with long-term agreements in place with DSM". For BASF and Trouw the IR record says only "business dealings".
21. "Kingdomway uses its own D3 in Doctor's Best" became "a D3 maker that also owns Doctor's Best". No source confirms which D3 goes into Doctor's Best.

**Pricing**

22. Price table driver notes:
    - The May 2026 driver ("new capacity; overseas supply restored") is now attributed to Garden's 2025 AR comment on vitamins generally.
    - The Sep–Oct 2026 driver is marked as dsm-firmenich's June 2026 comment.
23. "Every spike came from supply, not demand" became "driven mainly by supply … although 2020 also saw a surge in supplement demand". QQ News and the report's own table cite supplement demand.
24. The list-to-traded gap "~3.5x" became "~3.4–3.8x" (360 ÷ 95–105).
25. "Down-leg shows up in every listed D3 producer" became "every D3 producer whose 2026 results were found (Garden, Fermenta, dsm-firmenich)". There are no 2026 data for NHU, Kingdomway or Zhejiang Medicine.
26. "Capacity 1.4–2x demand" became "~1.4–2.2x" (14,740/6,750 = 2.18).
27. Spike frequency "every two to five years" became "every one to five years". Spike years are 2009, 2014, 2016, 2017, 2018, 2020 and 2024.
28. Deleted: North American contracts "well above Chinese domestic levels, partly because Canada has fewer approved suppliers". dsm-firmenich ties the fewer-suppliers point to Canada's premium within North America. The notes have no same-month Chinese price to compare with.

**Cholesterol**

29. Added: Garden's own April 2026 IR gives NF-grade cholesterol design capacity of **840 t/yr** (plus 700 t/yr feed-grade). This sits next to Tianfeng's 1,200 t (a 2022 figure), in the text and the scorecard.
30. Garden 2023 margin: "when feed D3 averaged ~RMB 50–56/kg" became "traded at". No source computes an average.
31. NF cholesterol end uses now have sources:
    - shrimp feed: Garden IR Apr 2026;
    - cosmetics: Ang Likang AR;
    - lipid nanoparticles: Evonik.

**Symbiotec and economics**

32. Symbiotec DMFs "about 45" became "44 active". A re-parse of the FDA Q3 2026 spreadsheet gives 44 active and 2 inactive.
33. "Symbiotec would be the third phytosterol entrant" became "third phytosterol-route D3 entrant with a disclosed route, after Kerui and Fermenta". Innobio's pine-oil route is plausibly phytosterol-based but undisclosed.
34. Fermenta "400 existing customers" became "400+".
35. "USD 5,000–10,000/kg, roughly the per-IU price of food-grade beadlets" was corrected. On IndexBox's numbers, beadlets are USD 14,000–22,000/kg in pure-D3 terms and powder is USD 4,000–7,200/kg. The range now reads as lying between powder and beadlets.
36. Deleted: the India fortification market "of a few tonnes of pure D3 (my rough estimate)". ICRIER PB55 gives no FSSAI dose levels or volumes, and nothing else in the notes does. The text now says the size cannot be estimated from these sources.
37. Conclusion: plant-cholesterol LNP benchmark "Evonik and Kerui" became "Evonik". Ang Likang says Kerui's high-purity plant cholesterol goes mainly into cosmetics.

## Weak support (flag before publication)

**Single secondary, search-snippet or unverified sources**

| Source | Claim it carries |
|---|---|
| Business Standard (403; snippet) | Fermenta FY28 target |
| Indian Pharma Post (search summary) | ~1 t/yr plant D3 + 50 kg derivatives. The unit basis of "1 t" is unknown. |
| Expana (search summary) | AFIA's "100% China-dependent" statement |
| Tencent (snippet) | Hisound as a Xianju subsidiary. Contradicted by Xianju's 2024 AR. |
| Gelonghui (undated) | Several claims, listed below |
| Sina/Securities Times | Garden's RMB 660 quote. One notes file calls this snippet-only. |
| TechTimes | dsm-firmenich ANH 4.4% margin |
| SINOQUAL | Chundi's 10 t/10 t/2 t lines (not company-verified) |
| PopCJ | Kerui 30 t/yr; Chundi revenue (a secondary article citing the 2023 AR) |
| CLS 2023 | Ang Likang control "since 2023". The date is not confirmed in primary text. |
| Investing.com | Faes €63.5m |
| BizDevelopmentNews | Fermenta ₹401 cr D3 revenue. The AR's rounded figures give ₹402 cr. |
| Hzeyun | 12,800 t capacity; Nov 2024 quotes |
| Sohu | Zhejiang Medicine 300 t; Hisound has no captive cholesterol; cholesterol +20% |
| Garden Bio 2024 AR | Cited for "vitamins line includes vitamin A", applied to the 2025 figure |

Gelonghui is the only source for:
- 25-OH-D3 at RMB 4,000/kg;
- D3 at under 0.02% of feed cost;
- the Gansu Jiahui project;
- the Kingdomway outage detail;
- the US$75/kg export quote.

**Company self-claims**
- Garden: 30–40% share, the "only full chain", "ample" wool grease.
- Fermenta: "three largest", ~25% human-API share (2021, management via BP), "until very recently India's only manufacturer".
- Kerui: "first mass producer".
- Innobio: isotope verification.
- Nutraland/Euromonitor ranking (commissioned by Nutraland).
- Symbiotec website claims.
- Management's US$600m niche (via ICICI).
- dsm-firmenich Sisseln page (undated).

**Modelled prices and syndicated research**
- All IndexBox ingredient prices are modelled corridors, not transactions. They drive the ₹7–88 cr per-tonne range and the lichen-parity and US$600m calculations.
- The market sizes from Market Intelo, Future Data Stats, Market.us, GMI, SkyQuest and Dataintelo are low-reliability.

**Dated data**
- Tianfeng's DSM, Fermenta, Weishi, Zhejiang Medicine and Tianxin capacities (2023 Huajing data).
- Non-Garden NF cholesterol capacities (2014).
- Fermenta's 25% share (2021).
- India market value of ₹5.38bn (2018).
- Paricalcitol USD 110m (2014).

**Conflicts carried in the text**
- Symbiotec Q1 FY27 EBITDA margin: 21% (Arthneeti, used) vs 28% (another Sahi article).
- VITADEE Green: lichen (vegconomist) vs phytosterol (Fermenta).
- Fermenta's Indian patent: Sep 2025 (AR) vs ~Jun 2026 (vegconomist).
- Garden NF cholesterol: 1,200 t vs 840 t.
- Hisound capacity: 3,000, 2,000 or 800 t.

**Other weak points**
- The Dishman CEP withdrawal year (2023) comes from the notes. The EDQM page shows "withdrawn" but not the withdrawal date.
- Inferences with little or no direct evidence:
  - the 12–36-month qualification lag;
  - "cash cost of the marginal producer RMB 50–130/kg";
  - the RMB 80–150/kg base case;
  - "ingredient value measured in tens of millions of dollars";
  - "fits its platform better than any other Indian steroid maker's";
  - BA "can be extended back" to C27 (by analogy with Fermenta's patent);
  - thermal isomerisation, which is standard chemistry and not separately sourced.
- Absence claims (13 tags) cannot be cited positively:
  - no named brand-owner suppliers;
  - no global end-use split;
  - no consensus forecast;
  - no cost curve;
  - no BASF synthesis confirmation;
  - no DSM closure statement;
  - no Symbiotec FSSAI/D3 filings;
  - no lichen capacity disclosures;
  - no commercial yeast D3;
  - no EU Novel Food decision;
  - no current Indian D3 anti-dumping duty;
  - no public bulk prices for crystal, oil or vegan grades.

## Unresolved

- **"Arrives third":** the heading "Symbiotec arrives third in a niche smaller than its pitch" and the summary's "arrives third" are kept, because the heading structure is fixed. The body now qualifies "third" as third with a disclosed phytosterol route.
- **Zero vs close to zero:** the summary says value vegan D3 at "close to zero in FY27–29 estimates" and the conclusion says "zero in base estimates". Both are author judgements and were left as written; consider harmonising.
- **Garden's ~70% NF cholesterol share** (Tianfeng) is not reconciled with Garden's own 840 t/yr NF-grade figure. If 840 t is current, both the share and the 1,820 t global total may be overstated.
- **DSM's February 2026 CEP:** whether it covers Sisseln is not stated on EDQM.
- **Kerui:** whether its process uses BA is unverified.
- **Fermenta's "~1 t/yr":** whether this is crystal or oil is unknown.
