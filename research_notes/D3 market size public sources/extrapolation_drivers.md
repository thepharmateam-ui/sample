# Vitamin D3: drivers for extrapolating the global market from 2020/2022 bases to 2026

Prepared 21 Oct 2026 for the Symbiotec Pharmalab note. English-language public sources were preferred: company filings, regulator and official statistics, and trade press quoting named sources. Broker research is used only where flagged. This file extends `government_trade_data.md`, `india_west_public_filings.md` and `china_public_filings.md` in this folder, and `../Vitamin D3 supply landscape/pricing_and_dynamics.md`. It does not repeat their detail.

**Downloads** are in `/tmp/claude-0/-home-user-sample/da2696f9-0447-5145-866a-ae62d71abce7/scratchpad/extrap_dl/`, with subfolders `dsm/`, `fermdecks/`, `aaf/`, `india/`, `dsmfin/` and `brazil/`, plus the Alltech and FAO files at the top level. **Scripts** are in `/tmp/claude-0/-home-user-sample/da2696f9-0447-5145-866a-ae62d71abce7/scratchpad/extrap_scripts/`:
- `extrap.py`: the extrapolation.
- `uv_tiers.py`: trade unit-value tiers.
- `chart_bbox.py`: reads chart labels from PDFs.

**Tags**
- **[P]** primary: a company filing, regulator or official statistic.
- **[TP]** trade press quoting a named source.
- **[CO]** a company's own published commentary, such as an Alltech or dsm-firmenich article.
- **[B]** broker research.
- **[COMM]** a commercial price tracker or paid market research.
- **[SS]** taken from a web-search summary; the page itself was not opened.
- **[A]** my assumption or inference.

**Unit convention**, as in the other notes. Tonnages are on a **500,000 IU/g (D3-500) basis** unless stated otherwise.
- Pure crystalline D3 is 40 MIU/g, so 1 kg crystalline = 80 kg D3-500 equivalent.
- To convert D3-500 tonnes to pure D3, divide by 80 (equivalently, multiply by 1.25%).

---

## 0. Bottom line

1. **Feed volume driver: use Alltech's stated year-on-year growth rates chain-linked, not its headline levels.**
   - Headline levels rose from 1,187.7 Mt (2020) to 1,440 Mt (2025), +21%.
   - Most of that jump comes from restatements and wider survey coverage. The 2023 figure was restated from 1.29 bn t to 1.380 bn t in the 2025 Outlook. Surveyed mills rose from 28,235 to 38,837 in the 2026 Outlook.
   - Chain-linked, global compound feed grew **+6.1% from 2020 to 2025** and **+4.1% from 2022 to 2025**.
   - A poultry-weighted "D3-weighted" species index gives +8.7% for 2020–25. The weights are my assumption.
   - For 2026 I assume +1.5% (range +1.0% to +2.0%). FAO forecasts world meat output +1.0% in 2026.
2. **Human-grade volume.**
   - Fermenta's human-D3 volumes rose +71% in FY21 and +7% in FY22, fell −30% in FY23 and −18% in FY24, then rose +43% in FY25 and +21% in FY26.
   - On a calendar-year basis that is +13% for 2020–25, −7.5% for 2020–22 and +23% for 2022–25.
   - The market-wide signals are softer:
     - NBJ said in 2023 that the US vitamin D supplement market in 2025 would be 12.7% larger than in 2020.
     - CRN user penetration went 42% (2020), 52% (2021), 50% (2022).
     - dsm-firmenich reported destocking in 2022–Q1 2024.
   - Base assumption: human-grade volume is **×0.95 in 2022 and ×1.15 in 2026** versus 2020 (range ×1.05 to ×1.28).
3. **Feed-grade price (D3-500).** Estimated annual averages, global blended, in USD/kg:
   - **2020: ~26** (range 23–30). COVID spike to ~EUR 60/kg in Q2.
   - **2022: ~11.5** (10–13). Feedinfo range EUR 7–16/kg.
   - **2025: ~32** (27–40). dsm-firmenich says North America contract levels were USD 35–42/kg in Sep 2025.
   - **2026 YTD: ~21** (17–25). Fermenta's animal-nutrition realisation was −40% YoY in Apr–Jun 2026. Brazil's import unit value from China was USD 24/kg for Jan–Sep 2026.
4. **Human-grade price (crystalline 40 MIU/g).** About **USD 2,000–3,000/kg** in 2020 per Fermenta management. India's official export unit value for the crystalline-type tier was USD 1,569/kg (2020), 1,705 (2022) and 1,728 (2025). That is roughly **+10% over 2020–25 in USD**, consistent with Fermenta's reported price changes after FX.
5. **Watch the unit trap.**
   - Per IU, human crystalline and feed-grade prices are close: crystalline at USD 2,200/kg ≈ USD 27.5 per kg D3-500 equivalent, against USD 26/kg for feed grade in 2020.
   - The large "price gap" is mostly a potency effect.
   - Never multiply D3-500-equivalent tonnes by a crystalline USD/kg price. Divide by 80 first.
6. **Illustrative 2026 estimate (base case).** Base is 2020 = 6,250 t output, 20% human/pharma share. Feed and human are kept separate.

   | | 2020 | 2022 (derived) | 2026E |
   |---|---|---|---|
   | Feed-grade volume, t D3-500 | 5,000 | 5,094 | **5,383** |
   | Human/pharma volume, t D3-500 (t pure) | 1,250 (15.6) | 1,188 (14.8) | **1,438 (18.0)** |
   | Total, t D3-500 (t pure) | 6,250 (78.1) | 6,281 (78.5) | **6,821 (85.3)** |
   | Feed-grade value, USD m | 130 | 59 | **113** (92–135) |
   | Human-grade value at API (crystalline-equivalent) prices, USD m | 34 | 36 | **44** (31–59) |
   | Total at API-level prices, USD m | ~165 | ~94 | **~157** (122–194) |

   - The human-grade value **at "as-sold" (formulated) prices is much higher.** Fermenta's FY26 human-D3 revenue of ₹292.7 cr (≈USD 34m) divided by a 20–25% share gives **USD 135–170m**. The share is a management claim relayed by a broker, so treat this as a cross-check only.
   - The volume result is insensitive to the assumptions: 6,700–7,000 t across all sensitivities. Value depends mainly on the feed-grade price.

---

## 1. Volume driver: global compound feed production

### 1.1 Alltech Agri-Food Outlook / Global Feed Survey: headline series as published

| Data year | Report (release date) | Total, Mt | Stated YoY | Coverage | Exact wording | Source (type) |
|---|---|---|---|---|---|---|
| 2019 | 2020 Alltech Global Feed Survey (release c.28 Jan 2020; reprint 5 Feb 2020) | **1,126** | **−1.07%** | 145 countries, ~30,000 mills | "international feed tonnage decreased by 1.07% to 1.126 billion metric tons of feed produced last year, due largely to African swine fever (ASF)" | Alltech release reprinted by The National Provisioner, 5 Feb 2020: https://www.provisioneronline.com/articles/108929-alltech-global-feed-survey-reveals-first-production-decline-in-nine-years ; Alltech page: https://www.alltech.com/en-in/press-release/alltech-global-feed-survey-reveals-first-production-decline-nine-years (now redirects to search) [CO via TP] |
| 2020 | 2021 Agri-Food Outlook / 10th Global Feed Survey (launched 26 Jan 2021) | **1,187.7** | **+1%** | 142 countries, >28,000 mills | "international feed tonnage increased by 1%, to 1,187.7 million metric tons (MMT) of feed produced last year. China saw 5% growth and reclaimed its position as the top feed-producing country, with 240 MMT." | Feed & Additive Magazine, Feb 2021, p.8: https://www.feedandadditive.com/digital-magazines/Issue1_February2021/8/ ; AgNavigator (J. Byrne, 26 Jan 2021): https://www.agnavigator.com/Article/2021/01/26/china-back-on-top-in-global-feed-production-ranking/ [CO via TP] |
| 2021 | 2022 Agri-Food Outlook, 11th survey (reprint 9 Feb 2022) | **1,235** | **+2.3%** | >140 countries, >28,000 mills | "international feed tonnage has increased by 2.3 percent, to 1.235 billion metric tons of feed produced in 2021" | The National Provisioner, 9 Feb 2022: https://www.provisioneronline.com/articles/112062-2022-alltech-agri-food-outlook-reveals-global-feed-production-survey-data-and-trends-shaping-the-future [CO via TP]. Garden Bio's CB prospectus quotes the same report as 12.355 亿吨 (see `china_public_filings.md`) |
| 2022 | 2023 Agri-Food Outlook, 12th survey (released 24 Jan 2023) | **1,266** | **−0.42%** | 142 countries, >28,000 mills | "global feed production remained steady in 2022 at 1.266 billion metric tons (BMT) in 2022, a decrease of less than one-half of one percent (0.42%) from 2021's estimates" | Poultry Producer reprint, 24 Jan 2023: https://www.poultryproducer.com/?p=17574 ; Feed & Additive, 30 Jan 2023: https://www.feedandadditive.com/alltech-publishes-global-feed-research/ [CO via TP] |
| 2023 | 2024 Agri-Food Outlook, 13th survey (released 2 Apr 2024; adjusted 15 Apr 2024) | **1.29 bn** | **−0.2%** (−2.6 Mt) as released; **"adjusted on April 15, 2024" to −0.01%** | 142 countries, >27,000 mills | "global animal feed production held steady in 2023, totaling 1.29 billion metric tons (BMT), a marginal decrease of 0.2% from the previous year" | Milling MEA, 4 Apr 2024: https://millingmea.com/global-feed-production-remains-steady-despite-challenges-alltech-agri-food-outlook-2024/ [TP]. The adjustment footnote appears on Alltech pages (https://www.alltech.com/node/9523) but could not be rendered from here [SS] |
| 2024 | 2025 Agri-Food Outlook, 14th survey (page dated 29 Apr 2025) | **1,396** | **+1.2%** from a **restated 2023 of 1,380** | 142 countries, 28,235 mills | "global feed production rebounded in 2024 after a stagnant 2023, increasing from 1.380 billion metric tons (mt) (+1.2%) to 1.396 billion mt." Footnote: "*The figures used in Alltech's Agri-Food Outlook are updated throughout the year as official feed tonnage information becomes available. Our 2023 data has been adjusted to reflect final figures." | Alltech press release: https://www.alltech.com/press-release/2025-alltech-agri-food-outlook-shares-global-feed-production-survey-data [CO] |
| 2025 | 2026 Agri-Food Outlook, 15th survey (21 Apr 2026) | **1,440** (regions sum to 1,440.08) | **+2.9%, +40.136 Mt** | 142 countries, **38,837 mills** | "global feed production in 2025 reached an estimated total of 1.44 billion metric tons (mt) — representing an increase of 2.9% and 40.136 million mt from 2024… growth was uneven, increasingly regionalized and driven less by herd expansion than by structural change, productivity gains and shifts in how production is measured and recorded." | Alltech press release: https://www.alltech.com/press-release/2026-alltech-agri-food-outlook-shares-global-feed-production-survey-data [CO] |
| 2026 | — | no Alltech forecast published | — | — | The 2026 release gives no forward estimate | — |

### 1.2 Comparability breaks (why headline levels must not be used as a growth index)

**The headline-to-headline change and the stated YoY growth do not reconcile in any year.** Implied restated prior-year level = headline(t) / (1 + stated growth(t)):

| Year (t) | Prior year as first published | Prior year implied by the t release |
|---|---|---|
| 2020 | 2019: 1,126 | 1,175.9 (+4.4%) |
| 2021 | 2020: 1,187.7 | 1,207.2 |
| 2022 | 2021: 1,235 | 1,271.3 |
| 2023 | 2022: 1,266 | 1,290 |
| 2024 | 2023: 1,290 | **1,380 (+7.0%)** |
| 2025 | 2024: 1,396 | **1,399.9** (1,440.08 − 40.136) |

So the survey base is revised upwards almost every year, which is consistent with growing coverage.

**Specific method notes in the releases:**
- **2020 survey:** "the beef feed production estimation was recalculated to improve its accuracy. The new estimate takes into account the average days on feed and intake as a percentage of body weight in the feedlot. Last year's estimation was also recalculated." (Provisioner reprint, 5 Feb 2020)
- **2023 Outlook:** Middle East "up significantly at 24.7% (6.301 MMT), as a result of more accurate reporting…" (Poultry Producer, 24 Jan 2023). This is a coverage gain, not real growth.
- **2024 Outlook:** first published at −0.2%, then the 2023 numbers were "adjusted on April 15, 2024" to −0.01% [SS for the adjustment wording].
- **2025 Outlook (the "2024/2025 survey change"):** 2023 was restated from 1.29 to 1.380 bn t, "adjusted to reflect final figures". The timing of data collection also moved:
  - The 2022 and 2023 Outlooks were "collected… in the last quarter of 2021/2022".
  - The 2025 Outlook was "collected in the first quarter of 2025".
- **2026 Outlook:**
  - Surveyed mills rose from 28,235 to 38,837 (+38%).
  - Alltech attributes part of the growth to "shifts in how production is measured and recorded".
  - The text gives both "late 2025" and "first quarter of 2026" as the collection period.
- **Species and "other".** Species totals do not add up to the headline total; the remainder is unlabelled "other" species:
  - 2024: species sum to 1,327.5 Mt against 1,396 Mt, about 68.5 Mt other.
  - 2025: species sum to 1,370.8 Mt against 1,440 Mt, about 69.3 Mt other.

**Chain-linked index** (2019 = 100, using each release's stated YoY): 2020 101.0; 2021 103.32; 2022 102.89; 2023 102.88; 2024 104.11; 2025 107.13. The headline-level index for comparison: 2020 105.5; 2022 112.4; 2025 127.9.

| Growth | Chain-linked | Headline levels |
|---|---|---|
| 2020→2025 | **+6.1%** | +21.2% |
| 2022→2025 | **+4.1%** | +13.7% |

### 1.3 By species (Alltech)

| Species | 2019 share | 2020 share | 2021 YoY | 2022 YoY | 2023 YoY (as first published) | 2024 Mt (YoY) | 2025 Mt (YoY) |
|---|---|---|---|---|---|---|---|
| Broiler | 28% | 28% (+1%) | +2.3% | +1.27% | +3.5% (385.04 Mt, 29.9% [SS]) | 385.415 (+1.8%) | **400.379 (+3.7%)** |
| Layer | 14% | 14% | −1.4% | +0.31% | "steady growth" (not quantified) | 173.038 (+1.4%) | **180.126 (+3.2%)** |
| Pig | 24% | 24% (+1%) | +6.6% | "almost −3%" | −1.23% | 369.293 (−0.6%) | **380.907 (+3.0%)** |
| Dairy | 12% | 11% | +1.9% | −1.32% | −2.3% | 165.500 (+3.2%) | **170.294 (+2.6%)** |
| Beef | 10% | 10% (−1%) | −1.9% | −0.34% | −4.36% | 134.1 (+1.8%; 2023 = 131.6) | **134.181 (+0.5%)** |
| Aquaculture | 4% | 4% (+3%) | +3.7% | +2.7% | −4.4% | 52.966 (−1.1%) | **55.470 (+4.7%)** |
| Pet | 2% | 2% | +8.2% | +7.25% | +0.74% | 37.692 (+4.5%) | **39.276 (+2.4%)** |
| Equine | – | – | – | – | −3.9% | 9.630 (+2.3%) | 10.194 (+0.2%) |
| Other | 6% | 7% | – | – | – | ~68.5 (residual) | ~69.3 (residual) |

Sources for the table:
- 2019: Provisioner, 5 Feb 2020.
- 2020: AgNavigator, 26 Jan 2021. Its year-on-year figures came from search summaries of Pork Business, Feed & Grain and Petfood Industry [SS].
- 2021: Provisioner, 9 Feb 2022.
- 2022: Poultry Producer, 24 Jan 2023.
- 2023: Milling MEA, 4 Apr 2024. The broiler tonnage is [SS].
- 2024–25: the Alltech releases above.

**2025 grouped:** poultry 580.5 Mt (40.3% of 1,440), pig 380.9 (26.5%), ruminant 304.5 (21.1%), aqua 55.5 (3.9%), pet 39.3 (2.7%).

**Species-weighted index for D3** [A]:
- Weights reflect where feed D3 is used: broiler 40%, layer 20%, pig 20%, dairy 6%, beef 4%, aqua 5%, pet 5%. These are my weights; poultry gets the highest IU/kg inclusion. They are not sourced.
- Where a species figure was not published I assumed: layer 2020 0%, layer 2023 +1%, dairy 2020 0%, pet 2020 +4%.
- Result (2020 = 100): 2022 **102.97**; 2025 **108.69**.
- Total-tonnage chain-linked index rebased to 2020 = 100: 2022 101.87; 2025 106.07.
- Poultry outgrew ruminants and pigs, so a D3-weighted driver runs about 2.5 pp above total tonnage over 2020–25.

### 1.4 Cross-checks (FAO, IFIF)

| Item | Figure | Quote / note | Source (type) |
|---|---|---|---|
| World meat production 2020 | **337 Mt** cwe | "World meat production reached 337 million tonnes in 2020, up 45 percent…" | FAO, FAOSTAT Analytical Brief 41, *Agricultural production statistics 2000–2020* (PDF dated 23 Mar 2022): https://openknowledge.fao.org/server/api/core/bitstreams/b75223dd-4e30-43aa-85a9-4c587753b027/content [P] |
| World meat production 2022 | **362.4 Mt** cwe, +1.6% | "World meat production reached 362.4 million tonnes (in carcass weight equivalent) in 2022, up 1.6 percent from 2021." | FAO, *Meat Market Review – Overview of market and policy developments in 2022* (13 Oct 2023): https://www.fao.org/3/cc8200en/cc8200en.pdf [P] |
| World meat production 2025 | **387 Mt** cwe, +2.5%; poultry 156 Mt (+3.7%) | "World meat production reached 387 million tonnes (carcass weight equivalent) in 2025, up 2.5 percent from 2024 level." | FAO, *Meat Market Review: Overview of global market developments in 2025* (22 Apr 2026), handle cd9401en: https://openknowledge.fao.org/server/api/core/bitstreams/4f2924f5-0387-42bc-a5a3-c0864f51c285/content [P] |
| World meat production 2026F | **391 Mt**, +1.0% | Poultry drives growth; bovine and ovine fall; pig meat 129.5 Mt (+0.6%) | FAO *Food Outlook* June 2026, as reprinted by 3tres3 (Jul 2026): https://www.3tres3.com/en/print/22631 [TP; FAO original not opened] |
| Global compound feed (IFIF) | "over one billion tonnes annually"; turnover "over US $400 billion" | Undated, labelled "estimates only" | IFIF Global Feed Statistics: https://ifif.org/global-feed/statistics/ [P/association] |
| IFIF 2022 | 1.245 bn t (2022); poultry 44%, pig 28% | Via Feed & Additive | https://www.feedandadditive.com/digital-magazines/Issue48_January2025/67/ [SS] |

**Reading** [A]:
- FAO meat output rose +14.8% over 2020–25 and +6.8% over 2022–25, well above Alltech's chain-linked feed growth (+6.1% and +4.1%).
- Three things explain the gap: 2020 meat output was depressed by ASF in China; FAO revises its data; and Alltech's 2026 text stresses productivity gains, meaning less feed per kg of meat.
- D3 is dosed per tonne of feed, so feed tonnage is the right volume driver. FAO meat output is an upper-bound cross-check.

### 1.5 2026 feed assumption [A]

- **Base: +1.5%. Range: +1.0% to +2.0%.**
- Rationale:
  - The Alltech chain-linked average for 2021–25 is about +1.2% a year; 2025 alone was +2.9%.
  - FAO's 2026 meat forecast is +1.0%.
- D3 inclusion per tonne is held constant in the base case.
- Downside risks to inclusion:
  1. Feed mills cut D3 to "rigid" minimum levels during hog losses (China, 2023; Tianfeng and Lianhe, see `pricing_and_dynamics.md`).
  2. 25-OH-D3 is substituting for D3 (Garden IR, Apr 2025).

---

## 2. Human-nutrition D3 volume, 2020–2026

### 2.1 Fermenta Biotech (BSE 506414): company disclosures [P]

| FY (Apr–Mar) | Human D3 volume YoY | Human D3 avg price YoY | Human D3 revenue, ₹ cr | Animal (feed) volume YoY | Animal avg price YoY | Animal revenue, ₹ cr | Source |
|---|---|---|---|---|---|---|---|
| FY20 | – | – | – | – | – | – | base |
| **FY21** | **+71%** (human D3 40 MIU) | **+4%** | n/a | −35% | −17% | n/a | Q4FY21 call transcript, 1 Jul 2021 (BSE, 7 Jul 2021). Quote: "For the entire financial year 2021 there was a positive impact on the human side of the demand and consequently the volume and the average prices of human vitamin D3 40MIU were higher by 71% and 4% respectively over previous year. However, the volumes and the average prices of animal vitamin D3 feed… were lower by 35% and 17%." https://www.bseindia.com/xml-data/corpfiling/AttachHis/134cc08a-80c9-4d85-8f49-1038f77cba90.pdf |
| **FY22** | **+7%** | "fairly stable if not a little better" (Nov 2021) | 224 | −49% | −13% | 79 | Q4FY22 EP, 31 May 2022: "Volumes of Human Vitamin D3 in Q4-FY22 increased by 15% over Q3-FY22 and increased by 7% in FY22 over FY21… [Animal] decreaed by 49% in FY22 over FY21. The average prices were also lower by 13%." https://www.bseindia.com/xml-data/corpfiling/AttachHis/5324faf7-fada-4961-97ea-9c67d33c0cfb.pdf . Revenue from the FY25 AR (BSE, 19 Jul 2025), p.14: https://www.bseindia.com/xml-data/corpfiling/AttachHis/3010155e-4b55-42a2-a549-ba9b53873915.pdf |
| **FY23** | **−30%** | **+3%** | 163 | −17% | −25% | 37 | Q4FY23 EP, 1 Jun 2023: "Volumes of Vitamin D3 for Human Nutrition in FY23 decreased by 30% compared to FY22, while the average prices… were higher by 3%… Animal Feed Volumes in FY23 decreased by 17% over FY22 and average prices were lower by 25% on a consolidated level." https://www.bseindia.com/xml-data/corpfiling/AttachHis/6d149686-604f-4cee-9b62-fd9f9610442b.pdf |
| **FY24** | **−18%** | **+5%** | 141 | "subdued" | "subdued" | 38 | Q4FY24 EP (corrigendum), 12 Jun 2024: "Volumes of Vitamin D3 for Human Nutrition in Q4-FY24 was higher by 111% compared to Q3-FY24 and 18% lower in FY24 as compared to FY23, while the average prices… were higher by 5%." https://www.bseindia.com/xml-data/corpfiling/AttachHis/2d7f8096-42cc-44ca-9ac1-1407261693d5.pdf |
| **FY25** | **+43%** | "increased realisation" (CARE); implied ≈+13% in INR incl. mix [A] | 228 (216 in the FY25 AR before reclassification) | n/a | "relative stability" | 82 (94 before reclassification) | MD Prashant Nagre: "While human nutrition volumes grew by 43% in FY25 over FY24, we have further seen the volumes grow by 21% in FY26 over FY25." Indian Pharma Post, 30 May 2026: https://www.indianpharmapost.com/news/lite/fermenta-biotech-reports-26-revenue-growth-in-fy26-20397 [TP quoting the company]. CARE, 1 Oct 2025: https://www.careratings.com/upload/CompanyFiles/PR/202510131020_Fermenta_Biotech_Limited.pdf |
| **FY26** | **+21%** | implied ≈+6% in INR (293/228 ÷ 1.21) [A] | 293 (292.7, +28%) | **+49%** | implied ≈ −11% in INR (109/82 ÷ 1.49) [A] | 109 (108.5, +32%) | CARE, 20 Aug 2026: "~21% y-o-y growth in sales volumes of Vitamin D3 API for human nutrition and 49% y-o-y growth in sales volume of Vitamin D3 API for animal nutrition majorly driven by better market conditions in H1 FY26." https://www.careratings.com/upload/CompanyFiles/PR/202608120807_Fermenta_Biotech_Limited.pdf . FY26 AR, MD&A, revenue mix p.14: https://fermentabiotech.com/wp-content/uploads/2026/09/Annual-Report-2025-26-1.pdf |
| **Q1FY27** (Apr–Jun 2026) | +18% QoQ (YoY not given) | n/a | 76.5 (−10% YoY, +24% QoQ) | −20% YoY, −52% QoQ | **−40% YoY** | 12.6 (−41% YoY) | Q1FY27 investor presentation: "Animal nutrition remains the soft spot: volumes down 52% QoQ and 20% YoY with average realisation down 40% YoY; the Company chose volume discipline over chasing a weak price." https://fermentabiotech.com/wp-content/uploads/2026/09/Investor-PresentationQ1FY27.pdf (local copy: `fermenta_q1/q1.txt`) |

**Quarterly and qualitative points** [P unless noted]:
- **Q2FY21** (Jul–Sep 2020), analyst meet of 11 Nov 2020 (transcript on BSE, 23 Nov 2020): "Our human side sales volume for the quarter has grown by 26% on quarter-on-quarter basis and about 77% on a year-on-year basis." https://www.bseindia.com/xml-data/corpfiling/AttachHis/23445550-d343-4c2e-98b8-ed6d83f24557.pdf
- **Q4FY21:** "the volumes of human vitamin D3 40MIU were higher by 101% over the quarter four financial year 2020." (Q4FY21 transcript)
- **9MFY22:**
  - Human volumes "have grown by 19%" vs 9MFY21.
  - Animal feed volumes "down by 33%… prices were also down by 22%." (Q3FY22 call, 16 Feb 2022: https://www.bseindia.com/xml-data/corpfiling/AttachHis/9e5e419e-6095-47a2-a06e-bf49cfe9a712.pdf)
  - Q3FY22 human volumes were "lower by 31% over Q2-FY22 due to lower offtake" (Q3FY22 EP, 15 Feb 2022: https://www.bseindia.com/xml-data/corpfiling/AttachHis/6a3b4b52-bb14-41d0-a5ee-8e05c1f7cced.pdf).
- **9MFY23:**
  - Human volumes "decreased by 34% vs 9M-FY22".
  - Animal volumes +2%, prices −26%. (Q3FY23 EP, 15 Feb 2023: https://www.bseindia.com/xml-data/corpfiling/AttachHis/0d01b21b-4be3-4a67-bcb7-1f2de0f0ded9.pdf)
- **FY24 quarters:**
  - Q1FY24 human volumes −38% QoQ, prices +2% QoQ (EP, 17 Aug 2023: https://www.bseindia.com/xml-data/corpfiling/AttachHis/3eda258d-3e05-4203-9491-0bf011255523.pdf).
  - H1FY24 −49% YoY, prices +8% QoQ in Q2 (EP, 28 Nov 2023: https://www.bseindia.com/xml-data/corpfiling/AttachHis/72d9cddd-b33d-461f-a3e0-3896b186ca37.pdf).
  - 9MFY24 −38% YoY (EP, 20 Feb 2024: https://www.bseindia.com/xml-data/corpfiling/AttachHis/ab831047-42e0-4e9a-bdfa-91b3fdb4ee59.pdf).
- **Q1FY25:** human volumes "+48% compared to Q1FY24", average prices "+2%… compared to Q1FY24 and 10% higher over Q4FY24" (EP, 23 Aug 2024: https://www.bseindia.com/xml-data/corpfiling/AttachHis/7af5b634-ca39-4755-afae-04777a8daabd.pdf).
- **FY22 AR, PDF p.21:** "Until a couple of years ago, the human nutrition side of the business generated 55% of our Vitamin D revenues; during the year under review, this increased to around 75%." (Fermenta Annual Report 2021-22, BSE filing 16 Jul 2022; local copy `pubsrc/fermar/ar2022.txt`)
- **CARE, 17 Nov 2023:** "there was a spurt in demand of the same during FY21 and FY22 as consumers felt the need to rely on immunity boosting health supplements during the pandemic. The entire distribution chain… continued to maintain large inventory… However, with the pandemic over in FY22, consumption demand for Vitamin D3 health supplements fell drastically in FY23, due to which the distribution channel was saddled with surplus stocks, which took around three quarters to rationalise." https://www.careratings.com/upload/CompanyFiles/PR/202311131111_Fermenta_Biotech_Limited.pdf (local `pdfs/care2023.pdf`)
- **CARE, 9 May 2022:** FY21 revenue growth was "mainly on account of increase in contribution… from Vitamin D3 (for human consumption)… In FY21, contribution from Vit D3 for animal consumption has declined significantly owing to the onset of COVID-19 pandemic". https://www.careratings.com/upload/CompanyFiles/PR/09052022060155_Fermenta_Biotech_Limited.pdf (local `pdfs/care2022.pdf`)
- **FY26 AR** (p.10): human nutrition "grew 29 per cent year-on-year in FY26, on top of FY25's 62 per cent growth… reflecting normalisation of post-pandemic customer inventory, broader approvals for our spray-dried Vitamin D3 100,000 IU/g (D3 100 SD)…"

**Fermenta human-volume index.** Chained from the FY growth rates (FY20 = 100): FY21 171; FY22 183; FY23 128; FY24 105; FY25 150; FY26 182.

On a calendar-year basis [A], with CY(t) ≈ 0.25 × FY ending Mar(t) + 0.75 × FY ending Mar(t+1):

| CY | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| Index | 153 | 180 | 142 | 111 | 139 | 174 |

So CY2025/CY2020 = **1.13**, CY2022/CY2020 = **0.93** and CY2025/CY2022 = **1.23**.

**Caveat:** this is one producer, about 25% of human D3 API by its own claim (BP Equities 2021, broker). Its volumes include share shifts, channel restocking and destocking, and format mix (crystalline versus D3 100 SD).

### 2.2 dsm-firmenich / DSM commentary on human vitamin D demand [CO / P]

| Date | Statement | Source |
|---|---|---|
| 22 Apr 2020 | Frederic Boned (VP Human Nutrition & Health North America, DSM): "extremely high demand for ingredients associated with immunity such as vitamin C, zinc, vitamin A, vitamin D… 50-60% increases in some cases… Some of it is an artificial spike in demand due to consumer stockpiling behavior." | FoodNavigator-USA (E. Watson): https://www.foodnavigator.com/Article/2020/04/22/DSM-VP-talks-vitamin-C-pricing-supply-chain-resiliency-and-surging-demand-for-vitamin-C-A-D-E-B12-B6-and-zinc [TP] |
| FY2020 | DSM Integrated Annual Report 2020: Human Nutrition & Health "5% organic growth, with volumes up 7%", driven by COVID-19 immunity demand in dietary supplements and pharma | https://annualreport.dsm.com/ar2020/review-of-business/nutrition/nutrition-performance-2020/human-nutrition-health.html (host did not resolve from here) [P, SS] |
| FY2022 | DSM IAR 2022: the dietary supplements market was "soft predominantly in North America, as demand for immunity-boosting supplements moderated from the elevated levels seen during the COVID-19 pandemic" | https://annualreport.dsm.com/ar2022/review-of-business/health-nutrition-care/performance-2022.html [P, SS] |
| Q1 2023 (4 May 2023) | "End-use demand in immunity-optimizing dietary supplements was weak, especially in North America"; HNC organic sales −2% | Citeline/HBW Insight: https://insights.citeline.com/RS153639/Demand-For-Immunity-Supplements-Down-Reports-DSM [TP] |
| FY2023 | HNC organic sales −4% (volumes −6%, prices +2%): "Volumes were affected mainly by persistent destocking and softer consumer demand… Sales in Dietary Supplements were impacted by pressure on consumer discretionary spend, especially in North America and lower demand for immunity-supporting solutions post-COVID." | dsm-firmenich IAR 2023, HNC performance: https://annualreport.dsm-firmenich.com/2023/business/health-nutrition-care/performance-2023.html [P] |
| Q1 2024 (2 May 2024) | "Health, Nutrition & Care organic sales were down 9% (-6% volumes, -3% price) driven by the vitamin effect. The business saw ongoing customer destocking in some of its larger end markets, especially visible in Early Life Nutrition and Dietary Supplements." | dsm-firmenich Q1 2024 trading update: https://investors.dsm-firmenich.com/content/dam/dsm-firmenich/investors/documents/results-center/2024/press-release-dsm-firmenich-q1-fy2024-trading-update-20240502.pdf [P] |
| 18 Sep 2023 (ANH) | "The prolonged destocking process has caught many producers off guard." | dsm-firmenich ANH, "Vitamins: 4th Quarterly Market Update": https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamins-4th-quarterly-market-update.html [CO] |

### 2.3 US supplement-market indicators (CRN, NBJ, SPINS)

| Indicator | Figure | Quote | Source (type) |
|---|---|---|---|
| US vitamin D supplement sales, 52 weeks to 29 Nov 2020 (SPINS) | Mainstream **+34.4% to US$544m**; natural channel +36.5% to US$40m | "In the overall mainstream channel, vitamin D sales grew 34.4% to $544 million." | Nutritional Outlook (J. Grebow), 10 Feb 2021: https://www.nutritionaloutlook.com/view/vitamin-d-made-headlines-over-covid-19-studies-last-year-sales-of-vitamin-d-were-also-up-in-2020-what-will-2021-look-like-2021-ingredient-trends-to-watch-for-food-drinks-and-dietary-supplements [TP quoting SPINS] |
| US vitamin D market 2025 vs 2020 (NBJ forecast) | **+12.7%** | "The vitamin D market will also be 12.7% larger than it was in 2020… vitamin D sales are also dropping post pandemic but the decline came later and is not as steep as was seen for C." | New Hope / NBJ (R. Polito), 30 Jun 2023, from NBJ's 2023 Supplement Business Report: https://www.newhope.com/market-data-and-analysis/monitor-vitamins-c-and-d-show-different-sales-routes-now [TP/COMM] |
| US vitamin D 2020 growth (NBJ) | +47.5%; H1 2023 −9.7% (SPINS) | Drug Store News, as summarised in search results | https://drugstorenews.com/building-resistance-sales-declines (403 here) [SS] |
| CRN survey: vitamin D use | **42% (2020) → 52% (2021)** | "Over the past 12 months, vitamin D usage significantly increased since 2020 (52% vs. 42% in 2020)". Ipsos, 20–26 Aug 2021, n = 3,089 adults (2,421 supplement users); base not stated in the release | CRN, 21 Oct 2021: https://www.crnusa.org/newsroom/crn-reveals-initial-data-2021-consumer-survey-dietary-supplements [P/association] |
| CRN survey 2022 | **50%** of supplement users | "Vitamin D (50%)"; usage of immunity-boosting supplements "steady" | CRN 2022 release via Vitamin Retailer: https://vitaminretailer.com/crn-reveals-survey-data-from-2022-consumer-survey-on-dietary-supplements/ [SS] |
| NBJ, total US supplements | 2020 +14.5% to US$55.75bn; 2021 +7.5% to ~US$60bn | – | NBJ/GlobeNewswire, 28 Jun 2021 [SS] |

### 2.4 Synthesis: human-grade volume index [A]

| | Fermenta CY index (company-level) | Market end-demand signals | **Assumption used** |
|---|---|---|---|
| 2022 vs 2020 | 0.93 (destock) | US retail roughly flat to down from the 2020 spike; CRN usage 2022 above 2020 | **×0.95** (range 0.90–1.00) |
| 2025 vs 2020 | 1.13 | NBJ US +12.7% (value, 2025F vs 2020) | – |
| 2026 vs 2020 | 1.19–1.28 if FY27 is flat to +10% | – | **×1.15** (range 1.05–1.28) |
| 2026 vs 2022 | – | – | ×1.21 (1.17–1.28) |

**Human share of 2020 output.** Base 20%, range 11–30%. Evidence:
- FEFAC: "75% of the vitamin D3 produced worldwide is used to supplement animals' diets", i.e. 25% non-feed.
- CITIC via Hubei Gongtong's SZSE filing: 2021 food/pharma 2,119 t of 10,308 t = 20.6% [B].
- Garden 2010 legal opinion: food/pharma demand 1,750 t of 9,055 t = 19%.
- Jiemian 2020: about 89% feed, i.e. 11% human.
- EU cartel decision: about 10% of value was human.

All of these are in the other notes in this folder.

---

## 3. Prices

### 3.1 Feed grade D3-500: Feedinfo EUR/kg annual ranges, as reproduced in Fermenta's BSE presentations [TP/COMM via P]

Chart "Vitamin D3 500 Animal Feed Price Trend, Price (Euro/kg), Source: feedinfo.com, Min of Low / Max of High, Calendar Year". Values were read from the PDF text layer by label x-coordinates (`chart_bbox.py`).
- Nov 2020 deck, p.26: https://www.bseindia.com/xml-data/corpfiling/AttachHis/33107246-301d-4469-922a-4a7d52f54130.pdf
- Jun 2022 deck, p.26: https://www.bseindia.com/xml-data/corpfiling/AttachHis/e4b98091-5fc3-4e5b-b7c9-b6e99b804d54.pdf
- Aug 2023 Q1FY24 EP, p.8: https://www.bseindia.com/xml-data/corpfiling/AttachHis/3eda258d-3e05-4203-9491-0bf011255523.pdf
- Sep 2023 deck: same values as the Aug 2023 EP.

| Period | Min of low | Max of high | Deck |
|---|---|---|---|
| 2012 | 7.60 / 8 | 22 | Nov 2020; Aug 2023 |
| 2013 | 5.60 / 6 | 30 | |
| 2014 | 8.00 | 25 | |
| 2015 | 6.25 / 6 | 20 | |
| 2016 | 6.00 | 33 | |
| 2017 | 6.70 / 7 | 80 | |
| 2018 | 32 | 85 | |
| 2019 | 12.50 / 13 | 75 | |
| **Q1 2020** | **9.25** | **50** | Nov 2020 |
| **Q2 2020** | **22** | **60** | Nov 2020 |
| **Q3 2020** | **18** | **21** | Nov 2020 |
| **2020 (full year)** | **9** | **60** | Aug 2023 |
| 2021 | 12 | 20 | Aug 2023 |
| 2022 YTD (to ~May 2022) | 11 | 16 | Jun 2022 |
| **2022 (full year)** | **7** | **16** | Aug 2023 |
| Q1 2023 | 7 | 9 | Aug 2023 |
| Q2 2023 | 8 | 10 | Aug 2023 |

No later Fermenta deck with this chart was found. The Q1FY27 deck has no price chart.

### 3.2 Dated price points, feed grade (USD or EUR per kg)

| Date | Price | Grade / market | Quote / note | Source (type) |
|---|---|---|---|---|
| FY18 → FY19 | **USD 35 → 44/kg**, average | Feed grade, Fermenta realisations | "The average price for animal feed grade increased from USD 35$ in FY18 to USD 44$ in FY19." | CARE, 8 Jan 2020: https://www.careratings.com/upload/CompanyFiles/PR/Fermenta%20Biotech%20Limited-01-08-2020.pdf (local `pubsrc/care/c2.txt`) [P] |
| Late Mar 2020 | **USD 34.8/kg** (highest sale USD 44.1); +183% in a month | Global spot, D3-500 | Glowlit data | FeedNavigator, 27 Mar 2020: https://www.feednavigator.com/Article/2020/03/27/Price-trends-for-Vitamin-D3-500-Vitamin-C-L-threonine (404 now) [TP/COMM, SS] |
| End Apr 2020 (peak) | ≈**USD 57–59/kg** (implied) [A] | Global spot | Back-calculated: 8 Jun 2020 "31% less… $39.1 per KG"; Aug 2020 "64% less than at the end of April… 21.3 US$" | Feedstuffs/Glowlit [SS]; All About Feed |
| 8 Jun 2020 | **USD 39.1/kg** (Turkey USD 32) | Global spot | "Since the peak price at the end of April, spot buyers globally are paying 31% less" | Feedstuffs "Feed additive focus: Vitamin D3 500 and Vitamin B1 mono": https://www.feedstuffs.com/news/feed-additive-focus-vitamin-d3-500-and-vitamin-b1-mono (403 here) [TP/COMM, SS] |
| 2 Sep 2020 | **USD 21.1/kg** (Iran USD 22.41) | Global spot | "Spot buyers are paying 63% less for Vitamin D3 500 than they were in End of April, with the current global price around 21.1 USD per KG." | All About Feed (Glowlit): https://www.allaboutfeed.net/animal-feed/feed-additives/drop-in-price-of-vitamin-e50-and-d3-500/ [TP/COMM] |
| 9 Sep 2020 | USD 24.16/kg (+19% vs mid-Aug) | Global spot | – | All About Feed, "Vitamin B3 Niacinamide and Vitamin D3 500 lowered in price" [SS] |
| Jul–Sep 2020 and 11 Nov 2020 | **USD 17–20/kg** | Animal D3 | Satish Varma (Fermenta): "On the animal side, it is still in the $17 to $20 range, it has maintained in the last quarter as well, even today as we speak." | Fermenta analyst-meet transcript (BSE, 23 Nov 2020) [P] |
| Oct–Dec 2021 | "**$12 to $14**" | Animal feed, "as per feed info" | Sumesh Gandhi (Fermenta), 16 Feb 2022 call | Q3FY22 transcript [P] |
| 2022 | EUR 7–16/kg (Feedinfo); Fermenta FY23 avg −25% YoY | – | see 3.1, 2.1 | [P] |
| 18 Sep 2023 | qualitative: NA "lower prices due to oversupply and weak demand… expected to remain stable at low levels" | D3-500, North America | – | dsm-firmenich ANH Q4 2023 update (URL in 2.2) [CO] |
| 18 Mar 2024 | "Although some lower-priced vitamin D3 is available, forward indications suggest prices rising"; Kingdomway explosion halted output | Global | – | dsm-firmenich, "Q2 Vitamin Outlook": https://www.dsm-firmenich.com/anh/en_NA/news/articles/q2-vitamin-outlook.html [CO] |
| 17 Jun 2024 | "a significant firmer trend… pushing prices up, especially in North America" | – | – | https://www.dsm-firmenich.com/anh/en_NA/news/articles/q3-vitamin-market-update-rising-prices-and-supply-challenges-in-the-vitamin-industry.html [CO] |
| 16 Jul 2024 | FOB Shanghai +2% WoW; +3% MoM expected; no absolute price | China export | – | ChemAnalyst (P. Knight): https://www.chemanalyst.com/NewsAndDeals/NewsDetails/vitamin-d3-price-surge-in-china-rattles-global-nutraceutical-market-28996 [COMM] |
| 16 Sep 2024 | "In North America, where availability is particularly tight, prices are increasing significantly." | – | – | https://www.dsm-firmenich.com/anh/en_NA/news/articles/the-global-vitamin-market-navigating-volatility-in-q4-2024.html [CO] |
| 20 Nov 2024 / 16 Dec 2024 | Chinese suppliers "increased their price offers significantly" / "Availability remains limited, prices are firm" | – | – | All About Feed: https://www.allaboutfeed.net/animal-feed/feed-additives/vitamin-markets-vit-d3-500-prices-firmer-while-a-and-e-stable-at-high-level/ ; dsm-firmenich: https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-update.html [TP/CO] |
| 2024 (official) | **USD 21.7/kg** | Brazil imports from China, NCM 29362921 | – | Comex Stat, in `government_trade_data.md` [P] |
| 15 Jan 2025 | "High prices persist due to material shortages, with no immediate price reductions expected." | D3-500 | – | All About Feed: https://www.allaboutfeed.net/animal-feed/feed-additives/vitamin-markets-high-prices-for-vitamin-d-due-to-material-shortages/ [TP] |
| 17 Mar 2025 | "supply constraints from 7-dehydrocholesterol shortages keeping prices high… prices are firming again" | – | – | https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-overview-2024-trends-early-2025-outlook.html [CO] |
| 14 May 2025 | "Prices are trending slightly downward due to inventory clearance and exchange rate shifts, though supply remains tight." | D3-500 | – | All About Feed: https://www.allaboutfeed.net/animal-feed/feed-additives/vitamins-market-update-as-vitamin-e-a-and-d3-prices-decline [TP] |
| 16 Jun 2025 | "Vitamin D3 continues to be one of the most volatile segments, with prices staying elevated due to ongoing supply constraints and limited availability of a key intermediate." D3 subject to full US duty | – | – | https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-outlook-q3-2025.html [CO] |
| **15 Sep 2025** | **USD 35–42/kg**, Canada slightly higher | North America contract levels | "price levels at which volumes are contracted are understood to be in the $35-$42 range with Canada slightly higher." Chinese expansion "delayed until mid-2026" | dsm-firmenich Q4 2025 outlook: https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-outlook-q4-2025.html [CO] |
| 2025 (official) | **USD 28.8/kg** (China); USD 42.9 all origins | Brazil imports NCM 29362921 | – | Comex Stat [P] |
| CY2025 (official) | **USD 34.3/kg** (107.5 t) | India imports from Switzerland, 29362940 | – | DGCI&S [P] |
| 15 Dec 2025 | "Vitamin D3 remains unpredictable. Prices vary widely by producer strategy and regional regulations." | – | – | https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-update-q1-2026.html [CO] |
| 16 Mar 2026 | "producers remain active in offering, buyers are generally well covered, and competitive pressure persists" | – | – | https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-update-q2-2026.html [CO] |
| Apr–Jun 2026 | Animal realisation **−40% YoY** | Fermenta feed D3 (India and Germany) | see 2.1 | Q1FY27 deck [P] |
| 15 Jun 2026 | "Prices have slightly softened. Increased competitive activity and new approved sources may gradually influence regional pricing alignment" | – | – | https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-update-q3-2026.html [CO] |
| Jan–Sep 2026 (official) | **USD 24.0/kg** (China); USD 56.9 all origins | Brazil imports | – | Comex Stat [P] |
| 11 Sep 2026 | "Vitamin D3 remains relatively soft due to comfortable inventories and limited demand growth but further downside appears limited." | – | – | dsm-firmenich Q4 2026 update (published 11 Sep 2026): https://www.dsm-firmenich.com/anh/en_NA/news/articles/vitamin-market-update-q4-2026.html [CO] |
| May–Oct 2026 | China domestic RMB 128–132 (May), ~97 (Sep), ~95 (Oct); Garden list RMB 360 | China ex-works | Chinese sources | `pricing_and_dynamics.md` [TP, Chinese] |

### 3.3 Human / pharma grade

| Date | Price | Grade | Quote | Source (type) |
|---|---|---|---|---|
| Jul–Sep 2020 (Q2FY21) | **USD 2,000–3,000/kg** | Human D3 (crystalline 40 MIU), general market | Satish Varma: "General market vary from the human side between $2000 to $3000 per kg. The range will be varying depending on the customer and volume requirement". Also: "If it is $20 and this is $2000, I think margin should be more or less similar." | Fermenta transcript, BSE 23 Nov 2020 [P] |
| Aug 2021 | **≈₹2 lakh/kg** (≈USD 2,700 at ~₹74/USD [A]) | Fermenta India declared price, human D3 | "Our current declared prices in India are close to about 2 lakhs per kilo." | Q1FY22 call transcript, 17 Aug 2021 (BSE, 24 Aug 2021), copy at https://valoremadvisors.com/assets/admin/transcript_file/1698211336_1162ee6e-f8e6-4493-aa15-30b55d5495cb.pdf [P] |
| Nov 2021 | "fairly stable if not a little better… There has not been any moderation." | Human D3 | – | Q2FY22 transcript, BSE 24 Nov 2021: https://www.bseindia.com/xml-data/corpfiling/AttachHis/1700837c-87dd-4659-90b0-f91382bf6b12.pdf [P] |
| FY21 to Q1FY25 | **+4% (FY21), +3% (FY23), +5% (FY24), +2% YoY (Q1FY25)** | Fermenta human avg price, INR | see 2.1 | [P] |
| CY2020 / CY2022 / CY2025 | **USD 1,569 / 1,705 / 1,728 per kg** (3,460 / 2,592 / 5,138 kg) | India exports, 29362940, partner rows with unit value USD 1,000–15,000/kg (crystalline-type tier; my tiering) | – | DGCI&S via tradestat MEIDB, pulled 21 Oct 2026 (`extrap_dl/india/`) [P; tiering A] |
| Year-end 2019 | RMB 18,000–19,000/kg | China pharma grade | Chinese source | `pricing_and_dynamics.md` [TP, Chinese] |

**Human-grade price index** [A]. In USD terms, 2020→2022 ≈ **+9%** and 2020→2025 ≈ **+10%** (India crystalline-tier unit values). Fermenta's INR price changes after INR depreciation give about +11% from FY20 to FY26. Base used:
- **2020: USD 2,200/kg.** This lies between the India tier unit value (~1,570) and Fermenta's USD 2,000–3,000 quote.
- **2022: 2,390.**
- **2025: 2,420.**
- **2026: 2,420**, flat.
- Ranges: 1,600–3,300.

**Per-IU comparison** [A]. Crystalline at USD 2,200–2,420/kg is USD 27.5–30 per kg D3-500 equivalent. Feed-grade D3-500 averaged about USD 26 (2020), 11.5 (2022), 32 (2025) and 21 (2026 YTD). So per IU, human crystalline was:
- about 1.1× feed grade in 2020;
- about 2.6× in 2022, the feed trough;
- about 0.95× in 2025, the feed spike (30.3 against 32);
- about 1.4× in 2026.

### 3.4 Annual average estimates, feed grade (USD/kg D3-500, "global blended")

The method is a monthly path built from the dated points above, then a simple 12-month average. The blend weights China domestic by its roughly 23% share of world feed (Alltech 2025: 330/1,440 Mt) against Western and export prices for the rest. FX rates are approximations, not sourced here [A]:
- EUR/USD: about 1.14 (2020) and about 1.05 (2022).
- RMB/USD: about 6.9 (2020), about 6.7 (2022), about 7.2 (2025) and about 7.1 (2026).
- China prices include 13% VAT.

| Year | Estimate | Range | How built |
|---|---|---|---|
| **2020** | **~USD 26** (≈EUR 23) | 23–30 | Path in USD/kg: Jan ~11 (Feedinfo Q1 low EUR 9.25), Feb ~12, Mar ~22 (34.8 at 27 Mar), Apr ~50 (peak ~57–59 end-Apr), May ~50, Jun ~38 (39.1 on 8 Jun), Jul ~28, Aug 21.3, Sep ~22 (Feedinfo Q3 EUR 18–21), Oct–Dec ~19–20 (Fermenta "$18–20"). Average 26.0. China domestic RMB ~100 → 500–700 quotes → decline gives a similar average |
| **2022** | **~USD 11.5** (≈EUR 11) | 10–13 | Feedinfo 2022 EUR 7–16 (H1 11–16, down to 7 by year-end); monthly path EUR 14 → 7.5, average 11.1, ×1.05 = USD 11.7. China domestic RMB ~110 → <80 → ~60 (average ~80 ≈ USD 10.5 ex-VAT). Fermenta FY23 avg −25% YoY |
| 2024 (not needed) | ~USD 20–25 | – | H1 at the trough (RMB 55–85; EUR ~8–10 implied), H2 spike (RMB 220–250 market by Oct, export USD 50 Nov). Brazil China-origin unit value 21.7 |
| **2025** | **~USD 32** | 27–40 | Western ~USD 35: NA contracts USD 35–42 in Sep 2025, H1 higher, H2 easing; India import from Switzerland 34.3. China domestic RMB ~200 average ≈ USD 25 ex-VAT. Blend 0.23 × 25 + 0.77 × 35 ≈ 33. Brazil China-origin unit value 28.8 as a floor |
| **2026 YTD** (Jan–Oct) | **~USD 21** | 17–25 | Western ~USD 23: Fermenta −40% YoY on an Apr–Jun 2025 base of ~38; Europe EUR 17–20 in spring 2026 [Chinese source, undated]; Brazil China-origin 24.0. China domestic RMB ~120 average ≈ USD 15 ex-VAT. Blend ≈ 21 |

---

## 4. Official trade data as a consistency check (2020 vs 2022 vs latest)

All data was pulled 21 Oct 2026. Earlier pulls are in `government_trade_data.md`; the CY export figures and unit-value tiers below are new. Authorities: DGCI&S / MoC&I tradestat for India; SECEX/MDIC Comex Stat for Brazil [P].

| Series | 2020 | 2022 | Latest | Notes |
|---|---|---|---|---|
| India imports 29362940, **FY**, US$ mn / kg | FY2020-21: 6.87 / 31,032 | FY2022-23: 10.88 / 23,991 | FY2025-26: **14.40 / 174,319** | EIDB annual |
| India imports, **CY**, US$ mn / kg | 6.90 / 23,944 | 11.03 / 18,433 | CY2025: **16.67 / 212,562** | MEIDB Dec, cumulative CY |
| India imports CY, rows < US$100/kg (feed-type), kg (UV) | 5,491 (54.6) | 5,880 (64.6) | 197,469 (**46.0**; Switzerland 107,490 kg at 34.3) | `uv_tiers.py` |
| India exports 29362940, **FY**, US$ mn / kg | FY2020-21: 21.01 / 142,222 | FY2022-23: 15.03 / 69,681 | FY2025-26: **27.75 / 200,524** | EIDB annual |
| India exports, **CY** (new pull), US$ mn / kg | **17.63 / 114,306** | **16.97 / 106,865** | CY2025: **29.95 / 201,222** | MEIDB `cwacexReportYear=2`. Also CY2019 11.53 / 26,873; CY2021 23.27 / 155,717; CY2024 20.91 / 105,289 |
| India exports CY, rows < US$100/kg, kg (UV) | 93,873 (67.1); USA 82,047 kg at 70.9 | 80,116 (68.3); USA 69,653 at 73.4 | 133,473 (57.3); USA 108,367 at 55.8 | Probably Fermenta to its US arm; not a spot-price proxy |
| India exports CY, rows US$100–1,000/kg, kg (UV) | 16,973 (346) | 24,157 (294) | 62,611 (215); Germany 31,553 at 170 | Formulated or oil forms |
| India exports CY, rows US$1,000–15,000/kg (crystalline-type), kg (UV) | **3,460 (1,569)** | **2,592 (1,705)** | **5,138 (1,728)** | Human-grade price proxy |
| Brazil imports NCM 29362921 (D3 only), US$ / kg | 11,262,870 / 203,950 (UV 55.2) | 17,394,553 / 136,778 (UV 127.2) | 2025: **14,755,015 / 343,852 (UV 42.9)**; Jan–Sep 2026: 11,742,568 / 206,236 (−17% volume YoY) | Comex Stat |
| Brazil, China-origin kg (UV) | 90,471 (25.4) | 20,767 (44.0) | 2025: 148,904 (**28.8**); Jan–Sep 2026: 90,246 (24.0) | – |
| Brazil compound feed (Alltech) | 77.6 Mt | 81.948 Mt | 2025: 89.904 Mt (+16% vs 2020) | Section 1 |

**Reading** [A]:
1. **Volumes.** Straight-D3 import lines rose far faster than feed:
   - Brazil +69% from 2020 to 2025, against Brazilian feed +16%.
   - India imports ×9 from 2020 to 2025.
   - They dipped in 2021–22, when prices and supply were tight (2021–22 average Brazil 147 t, against 254 t in 2019–20 and 296 t in 2024–25).
   - That pattern reflects sourcing switches (straight D3 versus premix and AD3, and dsm-firmenich versus China) and 2025 stock-building ahead of US tariffs and expected increases. It is not consumption, and Brazil's Jan–Sep 2026 volume is −17%.
   - So trade does not contradict a modest (+6–9%) feed-D3 volume trend, but it cannot calibrate one.
2. **Prices.** Official unit values agree in direction with the price estimates:
   - China-origin feed-type: 2023 USD 16.7 → 2024 21.7 → 2025 28.8 → 2026 YTD 24.0.
   - Crystalline-type exports from India: roughly flat in USD (1,569 → 1,705 → 1,728).
   - The 2022 Brazil China-origin unit value (44.0, on only 20.8 t) is out of line with the 2022 feed trough. It is probably grade mix, so ignore it.
3. **Not refreshed: Brazil NCM 29362929 (other vitamin D).** A background re-query on 21 Oct 2026 (13:24–13:35 UTC) got HTTP 429 every time.

---

## 5. Extrapolation method and illustrative 2026 estimate

### 5.1 Formula

For each grade g (feed, human):

> Volume(g, 2026) = Volume(g, base year) × Driver(g, 2026) / Driver(g, base year)
>
> Value(g, 2026) = Volume(g, 2026) × Price(g, 2026), where Price is on the **same potency basis as Volume**

- **Feed driver:** Alltech chain-linked total-feed index, with the D3-weighted species index as a sensitivity, × (1 + 2026 growth). Inclusion rate is held constant.
- **Human driver:** the assumed index (2020 = 1.00; 2022 = 0.95; 2026 = 1.15), triangulated from Fermenta volumes, NBJ, CRN and dsm-firmenich (section 2.4).
- **Price bases:**
  - Feed: USD/kg D3-500, global blended average.
  - Human: USD/kg crystalline × (D3-500 tonnes / 80), i.e. API-equivalent.

### 5.2 Inputs and sources

| Input | Value used | Source |
|---|---|---|
| 2020 global output | 6,250 t (D3-500) | Boyar, *2020 China Vitamin Industry Development Report*, via Zhejiang Garden Biochemical CB prospectus (SZSE, 1 Mar 2023, p.1-1-375) [P relaying COMM; Chinese] |
| Human/pharma share, 2020 | 20% (11–30%) | FEFAC 2025; CITIC via Gongtong 2022 [B]; Garden 2010; Jiemian 2020; EU 2003/2/EC (see the other notes) |
| Feed index 2022 / 2025 vs 2020 | ×1.0187 / ×1.0607 | Alltech stated YoY, chain-linked (section 1.2) |
| Feed 2026 growth | +1.5% (1.0–2.0%) | [A]; FAO 2026 meat +1.0% |
| D3-weighted species alternative | 2022 ×1.0297; 2025 ×1.0869 | [A] weights (section 1.3) |
| Human index 2022 / 2026 | ×0.95 / ×1.15 | Section 2.4 [A] |
| Feed price 2020 / 2022 / 2025 / 2026 | USD 26 / 11.5 / 32 / 21 per kg | Section 3.4 |
| Human price 2020 / 2022 / 2025 / 2026 | USD 2,200 / 2,390 / 2,420 / 2,420 per kg crystalline | Section 3.3 |

### 5.3 Steps, base case

1. Split 2020: feed = 6,250 × 0.80 = **5,000 t**; human = 6,250 × 0.20 = **1,250 t** (= 15.6 t pure).
2. Feed 2026 = 5,000 × (107.13 / 101.00) × 1.015 = 5,000 × 1.0766 = **5,383 t**.
3. Human 2026 = 1,250 × 1.15 = **1,438 t** (= 18.0 t pure).
4. Total 2026 = **6,821 t D3-500 ≈ 85.3 t pure** (+9.1% vs 2020; ≈1.5% CAGR).
5. Feed value 2026 = 5,383 t × USD 21/kg = **USD 113m** (USD 92–135m at USD 17–25).
6. Human value 2026 (API-equivalent) = 18.0 t × USD 2,420/kg = **USD 43.5m** (USD 31–59m at USD 1,700–3,300).
7. Total at API-level prices = **≈USD 157m** (≈USD 122–194m on the price ranges alone).

### 5.4 Results by year (base case)

| | 2020 | 2022 (derived) | 2025 | 2026E |
|---|---|---|---|---|
| Feed volume, t D3-500 | 5,000 | 5,094 | 5,304 | **5,383** |
| Feed price, USD/kg | 26 | 11.5 | 32 | 21 |
| **Feed value, USD m** | **130** (115–150) | **59** (51–66) | **170** (143–212) | **113** (92–135) |
| Human volume, t D3-500 (t pure) | 1,250 (15.6) | 1,188 (14.8) | – | **1,438 (18.0)** |
| Human price, USD/kg crystalline | 2,200 | 2,390 | 2,420 | 2,420 |
| **Human value, API-equivalent, USD m** | **34** (25–47) | **36** (25–48) | – | **44** (31–59) |
| Total, t D3-500 | 6,250 | 6,281 | – | **6,821** |
| Total at API-level prices, USD m | ~165 | ~94 | – | **~157** |

### 5.5 Sensitivities, 2026

| Case | Feed t | Human t | Total t (pure) | Value USD m (feed + human) |
|---|---|---|---|---|
| Base | 5,383 | 1,438 | 6,821 (85.3) | 113 + 44 = **157** |
| D3-weighted species index | 5,516 | 1,438 | 6,954 (86.9) | 116 + 43 = 159 |
| Human share 11% | 5,989 | 791 | 6,779 (84.7) | 126 + 24 = 150 |
| Human share 30% | 4,710 | 2,156 | 6,867 (85.8) | 99 + 65 = 164 |
| Human growth low (×1.05) / high (×1.28) | 5,383 | 1,312 / 1,600 | 6,696 / 6,983 | 153 / 161 |
| Feed 2026 +1.0% / +2.0% | 5,357 / 5,410 | 1,438 | 6,794 / 6,847 | 156 / 157 |
| Feed price USD 17 / 25 | – | – | – | 135 / 178 |

Volume is robust at 6,700–7,000 t. Value is dominated by the feed-grade price assumption.

### 5.6 Using a 2022 base instead

- No public non-broker figure for 2022 global D3 output was found in English or Chinese public filings.
- The nearest figures are:
  - CITIC (broker) 2021 use of 10,308 t (feed 8,189 t), relayed in Hubei Gongtong's SZSE reply of 30 Aug 2022.
  - Garden's theoretical 2021 feed demand of 7,413 t (Alltech feed × 6 g/t; CB prospectus, 1 Mar 2023).
  - IFEEDER/DIS-LCS 2023 supply of 3,640 MT and demand of about 3,755 MT, basis unstated.
  - See `china_public_filings.md` and `india_west_public_filings.md`.
- Derived from the 2020 base, **2022 ≈ 6,281 t** (feed 5,094 t + human 1,188 t).

For any 2022 base, the 2022 → 2026 multipliers are:

| Multiplier | Base | Range |
|---|---|---|
| Feed volume | **×1.057** | ×1.052–1.062 |
| Human volume | **×1.21** | ×1.17–1.28 |
| Feed price | **×1.8** (USD 11.5 → 21) | – |
| Human price | **×1.01** | – |
| Feed value | **×1.93** | – |
| Human value | **×1.23** | – |

**Caution.** 2022 was both the feed-price trough and the start of the human destock, so a value base from 2022 roughly doubles on feed. A 2022 base from paid research (for example "USD x bn") is usually a finished-product or retail value, not an ingredient value. These multipliers apply only to ingredient-level bases.

### 5.7 Cross-checks [A]

- **Implied feed inclusion.** 5,000 t D3-500 over 1,188 Mt of feed (2020) = 4.2 g/t ≈ 2,100 IU/kg feed on average. The literature-style 6–8.4 g/t used by Garden and Tianfeng gives the "theoretical" 7,100–10,000 t. Actual output sits below theoretical, as expected.
- **Garden.** D3 and analogues revenue of RMB 386m in 2022 (≈USD 57m; Lianhe), at about a 30% share, implies a global industry of about USD 190m. That is above my 2022 total of about USD 94m. Garden's segment includes 25-OH-D3 and food grade at higher per-IU prices, which suggests my API-level values are conservative.
- **Fermenta-calibrated human value, "as-sold".** FY26 human revenue was ₹292.7 cr ≈ USD 33–34m at ₹85–89/USD [A]. Divided by a 20–25% share, that gives **USD 135–170m**. This is far above the USD 44m API-equivalent value. The gap reflects formulated formats (oils, CWS, spray-dried D3 100 SD, premixes) that sell at several times crystalline per IU, and/or a human share above 20%.
  - For a note on Symbiotec, which would sell API, the API-equivalent figure is the relevant addressable pool.
  - The as-sold figure is the relevant one for a formulator.
- **Fermenta-calibrated feed value.** FY26 animal revenue was ₹108.5 cr ≈ USD 12.5m. At a 5–6% share of feed volume (BP Equities 2021, broker), that implies about USD 200–250m for FY26 (Apr 2025–Mar 2026, the high-price period). My CY2025 feed value is USD 170m (143–212m). Fermenta's German sales are at European prices, above the global blend.

---

## 6. Caveats and gaps

1. **Alltech is a company survey, not official statistics.** In Alltech's own words, its figures "are estimates and are intended to serve as an informative resource". The full report, with country and species tables, needs registration (alltech.com/agri-food-outlook). Species YoY for 2020 and 2023 is incomplete.
2. **The 2020 base is a Chinese consultancy figure (Boyar) relayed in a CSRC-registered prospectus,** not an English primary source. The 80/20 feed/human split is an assumption.
3. **Fermenta human volumes are company volumes.** The calendar-year conversion is approximate.
4. **Feed price averages are reconstructed from sparse points.** No continuous public Feedinfo or Expana EUR/kg series exists after Q2 2023. 2024–26 relies on dsm-firmenich commentary, one dsm-firmenich USD 35–42 contract range, official trade unit values, Fermenta realisation changes and Chinese domestic quotes.
5. **FX rates are approximate and not sourced in this file.**
6. **Items marked [SS] were not opened:**
   - DSM 2020 and 2022 IAR wording;
   - the NBJ/Drug Store News +47.5% and −9.7% figures;
   - the CRN 2022 figure of 50%;
   - the Alltech 15 Apr 2024 adjustment;
   - the Glowlit March and June 2020 prices.
7. **Not found:**
   - any 2026 Alltech forecast;
   - an ICRA, CRISIL or India Ratings rationale for Fermenta (only CARE exists);
   - a public USD/kg for human D3 in 2024–26 other than official trade unit values;
   - a public 2022 global D3 output figure.
8. **Brazil NCM 29362929 and the US HTS 2936.29.5020 series are still missing.** Brazil was blocked by HTTP 429. The US needs a USITC DataWeb login or a Census API key; steps are in `government_trade_data.md` §4.5.
