# E digest – Industry: markets, competitors, procurement, structural trends

Agent E (industry), 24-Sep-2026. The digest covers the business and the industry only; there is no valuation.

**Conventions**

- Fact IDs E-xxxx point to `ledger/shards/E.jsonl` (406 rows); D-xxxx point to `ledger/shards/D.jsonl`.
- Page numbers are the PDF page markers in `sources/text/<DOC>.txt`. HTML and JSON sources are p.1.
- Tiers follow `registry/external_docs_E.csv`:
  1. regulator or company filing
  2. offer-document industry chapter
  3. press, trade association or think tank
  4. rating agency
  5. aggregator
  6. market-research vendor, always tagged [vendor estimate]

**How to read the sources**

- Every offer-document industry chapter is a report the issuer commissioned. Treat its forecasts as the vendor's, not as fact. The chapters used:

| Doc | Issuer | Report | Topic | Note |
|---|---|---|---|---|
| RHP_NEPHRO | Nephrocare | Frost & Sullivan (F&S), Nov-2025 | dialysis services | |
| DRHP_GSURG | G Surgiwear | 1Lattice, Dec-2025 | devices and surgical disposables | |
| DRHP_INTEG | Integris | F&S, Oct-2025 | MedTech and cardiology | |
| DRHP_SMT | SMT | F&S, Jul-2025 | cardiovascular | |
| DRHP_HEAL | Healthium | F&S, Sep-2021 | surgical consumables | 2021 vintage; historical context only |
| PD24 | Polymed | CRISIL MI&A, Aug-2024 | industry chapter of Polymed's own QIP document | Company doc, tier 1 in `company_docs.csv`. Shown as tier 2 here because it is a commissioned industry chapter. |

- Global figures are calendar years (CY). 1Lattice and CRISIL give India figures in fiscal years (FY = year to March). F&S uses calendar years for India too.
- Four pages were read through WebFetch because curl was blocked (HTTP 401, 403 or empty 202). Their quotes may be abridged, and each text file starts with a NOTE header:
  - FDA_SYR_UPD (no ledger rows cite it)
  - FDA_ETO
  - BT_TERUMOBCT
  - CDM_NUMERI25
- No ledger figure is snippet-only. Every number was read on a fetched page. Tofler and Grand View Research pages returned HTTP 403 and are not used. The Shanghai exchange (SSE) site's anti-bot page was not bypassed; the Chinese annual reports came from CNINFO instead.

---

## Ten headline findings

1. **India market size depends on the source, and the sources cannot be reconciled because their definitions differ.**
   - CRISIL: Rs 900–915 bn in FY24, growing 11–12% a year to FY28 (E-0321, E-0324) [PD24 pp.134-135].
   - 1Lattice: USD 30.0 bn in FY25, growing 14.3% a year to FY30P (E-0066, E-0068) [DRHP_GSURG p.175].
   - F&S/IBEF: USD 16.4 bn in 2023, including exports (E-0176) [DRHP_SMT p.180].
   - Government of India: USD 11 bn (E-0388) [PIB_PLI_MAR24 p.1].
   - The most usable figure for Polymed's pool is CRISIL's consumables and disposables market: Rs 195 bn in FY24, 13% CAGR over FY19–24 and 11–12% expected to FY28 (E-0326 to E-0328) [PD24 pp.136-137]. Polymed held a 1.9% share in FY23 (E-0352) [PD24 p.166].
2. **Imports still meet 30–40% of Indian consumables demand** (E-0323) [PD24 p.134]. Import dependence is lower for needles and syringes and higher for catheters and cannulas [PD24 pp.139-140]. The substitution headroom is therefore in Polymed's core catheter and cannula lines.
3. **Renal is the fastest-growing Indian pool.**
   - Dialysis patients: 0.28 mn in 2024 rising to 0.52 mn in 2029F, a 12.7% CAGR (E-0020, E-0038, E-0039).
   - In-clinic treatments: 33.9 mn rising to 66.1 mn (E-0057, E-0058).
   - India has 40,000 haemodialysis (HD) machines against about 105,000 needed (E-0043 to E-0045).
   - PM-JAY pays an average Rs 1,650 per treatment, which caps the budget for consumables (E-0052) [RHP_NEPHRO pp.272-285].
   - Globally, about 450 mn dialysers were sold in 2025, of which Fresenius Medical Care (FMC) had 38% (E-0232, E-0233), and 110,000 HD machines were installed (E-0234) [FMC_20F25 p.1].
4. **Renal competition is rising at home and from China.**
   - Nipro's dialyser plant in Satara, built under the PLI scheme, was inaugurated in Mar-2024 alongside Polymed's Faridabad renal plant [PIB_PLI_MAR24 p.1].
   - Chinese companies that win volume-based procurement (VBP) tenders use the capacity those wins build "to attack overseas markets" [SANXIN_AR25 p.34]. Sanxin's overseas revenue rose 34.56% in 2025 (E-0393) [SANXIN_AR25 p.39].
5. **Chinese supply is shifting from the US towards Polymed's markets.**
   - China ran 78 VBP projects for consumables in 2025 (E-0285) [KDL_AR25 p.17]. The tenders have cut Chinese domestic prices: Weigao's gross margin was 46.3% in 1H26 (E-0276) [WEIGAO_IR26 p.21].
   - In 2025 China's device exports to the US fell 10.77%, while exports to the EU and UK rose 8.91% and to Latin America 13.29% (E-0290 to E-0292) [KDL_AR25 p.18].
   - Weigao's 1H26 US sales fell 3.3% while EMEA rose 13.6% [WEIGAO_IR26 p.25].
6. **The US market for Chinese syringes has narrowed.**
   - Four Chinese syringe makers, including Shanghai Kindly (KDL), were under FDA import alert by May-2024 (E-0277) [MTD_SYR p.1; FDA_RU240517 p.1].
   - A 50% Section 301 tariff on Chinese syringes and needles was announced (E-0278) [MTD_SYR p.1].
   - BD and ICU Medical both flag the Section 232 investigation into imported medical consumables (Sep-2025) as a new tariff risk for every importer [BD_10K25 p.1; ICUI_10K25 p.1].
7. **Most global incumbents raised prices; BD's net price effect was slightly negative.**
   - Terumo's pricing added JPY 14.6 bn to operating profit in FY Mar-2026, against a JPY 12.1 bn hit from US tariffs (E-0253, E-0254) [TERUMO_FY25 p.7].
   - Nipro cites "price pass-through measures" [NIPRO_FY25 p.3]. Baxter and B. Braun also raised prices [BAX_10K25 p.1; BBRAUN_AR25 p.44].
   - Pricing contributed -0.3% to BD's revenue growth in FY25 (E-0197). BD blames low-cost entrants and purchasing concentrated in group purchasing organisations (GPOs) and integrated delivery networks (IDNs) [BD_10K25 p.1].
8. **Indian rivals are raising private-equity capital.**
   - Temasek took a minority stake in Romsons, completed 22-Sep-2026. Oct-2025 reports of the talks put it at 15–20% of the company at about USD 1 bn (E-0295, E-0296) [MB_ROMSONS p.1].
   - KKR bought Healthium for about USD 839 mn (E-0146). ADIA took 3% of Meril for USD 200 mn (E-0147) [DRHP_INTEG p.216].
   - Romsons had FY24 revenue of Rs 8,621.18 mn at a 26.76% EBITDA margin (E-0100, E-0102) [DRHP_GSURG p.219]. It is the closest domestic peer on margin.
9. **Polymed's margins are well above peers.**
   - F&S puts Polymed's FY25 gross margin at 66.78% and EBITDA margin at 28.72%, against Integris's 43.95% gross margin (E-0167, E-0168, E-0170) [DRHP_INTEG p.260].
   - Global disposables majors earn lower gross margins: B. Braun 40.5%, ICU Medical 36.8%, Weigao 46.3% (E-0248, E-0213, E-0276).
   - Hourly manufacturing wages are below USD 2 in India against USD 5–6 in China (E-0184, E-0185) [DRHP_SMT p.185].
10. **Consolidation and regulation are reshaping adjacent lines.**
    - Teleflex:
      - is selling Acute Care (anaesthesia, respiratory, urology) to Intersurgical for USD 530 mn;
      - is selling its OEM business for about USD 1.5 bn;
      - bought BIOTRONIK Vascular Intervention for EUR 704.3 mn (E-0221 to E-0223) [TFX_10K25 p.1].
    - Carlyle bought Vantive, Baxter's former kidney-care business with USD 4,513 mn of 2024 sales, for USD 3.8 bn (E-0376, E-0377) [BAX_10K25 p.1].
    - Regulation:
      - The EU sunset date for DEHP in medical devices is 1-Jul-2030 (E-0382) [GMED_DEHP p.2].
      - About 50% of US sterile devices are sterilised with ethylene oxide (EtO) (E-0381) [FDA_ETO p.1].
      - Italian payback claims can be settled at 25% (E-0207) [BD_10K25 p.1].

---

## B3 India market size and drivers

### Market table – India devices and consumables (conflicting estimates side by side)

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| India medical devices market (CRISIL) | Rs 900–915 bn | FY24 | PD24 p.134 · E-0321 | 2 |
| India medical devices, CRISIL forecast | Rs 1,375–1,400 bn; 11–12% CAGR FY24–28P | FY28P | PD24 p.135 · E-0325, E-0324 | 2 |
| India medical devices market (1Lattice) | USD 30.0 bn rising to USD 58.5 bn; 14.3% CAGR | FY25 to FY30P | DRHP_GSURG p.175 · E-0066 to E-0068 | 2 |
| India medical equipment market (1Lattice) | USD 13.3 bn | FY25 | DRHP_GSURG p.176 · E-0069 | 2 |
| India device market incl. exports (F&S/IBEF) | USD 16.4 bn rising to USD 60.2 bn | 2023 to 2030F | DRHP_SMT p.180 · E-0176, E-0177 | 2 |
| India device domestic consumption (F&S) | USD 13.0 bn | 2023 | DRHP_SMT p.181 · E-0183 | 2 |
| India MedTech market (F&S, Integris) | USD 27.7 bn; 8.0% CAGR 2024–29F | 2029F | DRHP_INTEG pp.213-214 · E-0142, E-0143 | 2 |
| India device market (Government of India) | USD 11 bn | Mar-2024 | PIB_PLI_MAR24 p.1 · E-0388 | 1 |
| India device market (F&S 2021, historical) | USD 7.3 bn | 2020 | DRHP_HEAL p.125 · E-0115 | 2 |
| India consumables & disposables (CRISIL) | Rs 195 bn; 13% CAGR FY19–24 | FY24 | PD24 p.136 · E-0326, E-0327 | 2 |
| India consumables, CRISIL forecast | Rs 290–300 bn; 11–12% CAGR | FY28P | PD24 pp.136-137 · E-0353, E-0328 | 2 |
| India disposables & consumables (F&S) | USD 4.3 bn (26% of the device market), rising to USD 17.1 bn | 2023 to 2030F | DRHP_SMT p.181 · E-0181, E-0180, E-0182 | 2 |
| India surgical disposables (1Lattice) | USD 3.9 bn rising to USD 6.4 bn | FY25 to FY30P | DRHP_GSURG p.177 · E-0070, E-0071 | 2 |
| Share of device demand met by imports (CRISIL) | ~80% (p.134) vs 70–75% (p.139) | FY24 | PD24 · E-0322, E-0331 | 2 |
| Import dependence (1Lattice) | 70–80%, but imports = 40.8% of consumption on the same page | FY25 | DRHP_GSURG p.178 · E-0073, E-0075 | 2 |
| Imported share of consumables | 30–40% | FY24 | PD24 p.134 · E-0323 | 2 |
| Import dependence before PLI (Government) | 90% | 2020 | PIB_PLI_MAR24 p.1 · E-0389 | 1 |
| Device imports | Rs 650 bn (CRISIL); USD 8.7 bn (1Lattice) | FY24; FY25 | PD24 p.139 · E-0332; DRHP_GSURG p.178 · E-0074 | 2 |
| Domestic device manufacturers | >800 | FY24 | PD24 p.127 · E-0320 | 2 |
| Surgical procedures in India | 165.7 mn | FY25 | DRHP_GSURG p.183 · E-0077 | 2 |
| FDI equity inflows, medical & surgical appliances | Rs 39.8 bn | FY24 | PD24 p.142 · E-0338 | 2 |
| PLI outlay for devices | Rs 3,420 cr | FY21–FY28 | DRHP_HEAL p.129 · E-0121 | 2 |
| PLI approved applicants | 26 (138 products) | Mar-2024 | PIB_PLI_MAR24 p.1 · E-0390 | 1 |
| MedTech PE transactions since 2017 | 59 | mid-2024 | DRHP_INTEG p.216 · E-0148 | 2 |

### Findings

- **Structure.** India has more than 800 domestic makers. The industry is fragmented and "competing in low-priced, high-volume segments". MNCs that manufacture in India include 3M, Abbott, Baxter, BSX, B. Braun, BD, GE, J&J, Medtronic, Nipro, Philips, Siemens, Transasia and Terumo [PD24 p.127; PD24 p.134].
- **Consumables are still led by MNCs and imports.** Most Indian players serve a single segment, and the consumables market is "largely dominated together by MNC players and imports". Domestic makers mostly produce syringes, needles, sutures and dressings, plus utility consumables such as catheters, IV cannulas, nasal oxygen cannulas, masks and ventilator circuits [PD24 p.132].
- **Clusters.** CRISIL counts more than 20 manufacturing clusters. The key players in the north Haryana–Delhi cluster are HMD, Polymed, BL Lifesciences, BD and Hollister [PD24 pp.132-133].
- **Demand drivers (CRISIL).**
  - Better healthcare access and insurance.
  - Make in India and the PLI scheme.
  - Import substitution.
  - Price regulation and the government's focus on cost-effective care, which favour locally made products.
  - Since Covid, OEMs have been seeking cost-competitive alternatives, making India "an emerging hub for manufacturing of high complexity and medium volume medical devices" [PD24 p.141].
- **Insurance and PM-JAY.** Over 50% of Indians had some health insurance by early 2025 [DRHP_INTEG p.216]. PM-JAY was extended to everyone aged 70+ on 11-Sep-2024 [FMC_20F25 p.1].
- **A two-layer market.**
  - In the commodity layer (syringes, IV sets, gloves, gowns), domestic players compete on price, scale and reach into tier-2/3 cities.
  - In the premium layer (sterile barrier systems, interventional catheters, speciality drapes), MNCs and a few certified domestic firms compete on technology, international approvals and relationships with tertiary hospitals [DRHP_GSURG p.204].
- **Trade balance.** India became a net exporter of medical consumables and disposables in 2022-23 (IBEF, cited by F&S) [DRHP_SMT p.181]. The government says net device imports fell for the first time in 2023 [PIB_PLI_MAR24 p.1].
- **Few scaled players.** F&S writes that the "Indian MedTech industry has very few scaled companies, such as PolyMed, SMT and Healthium" [DRHP_SMT p.185]. PE interest rests on Indian firms' "high-quality products at low cost, competing with global MNCs" [DRHP_INTEG p.216].
- **Regulatory context** (agent F owns the policy texts).
  - Under MDR 2017 devices fall into classes A–D. Infusion sets are Class B and haemodialysers Class C [DRHP_GSURG pp.180-181]. Dialysis machines are Class C [RHP_NEPHRO p.280].
  - Since Oct-2023, import licences for every class need quality and safety documentation [DRHP_GSURG p.194].
- **Challenges CRISIL lists.**
  - Price-cap notifications (stents, knee implants).
  - Trade-margin data released for stents, knee implants and syringes.
  - GST of 5–18% and customs duty of 0–7.5%, with an inverted duty structure.
  - A component supply chain concentrated abroad [PD24 pp.151-152].
  - HMD's website says GST on its products fell to 5% from 22-Sep-2025 [HMD_WEB p.1].

---

## B1 Procurement and pricing

### Market table – pricing and procurement

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| BD: pricing contribution to revenue growth | -0.3% | FY25 (Sep-2025) | BD_10K25 p.1 · E-0197 | 1 |
| Terumo: pricing measures, operating-profit effect | JPY 14.6 bn | FY Mar-2026 | TERUMO_FY25 p.7 · E-0253 | 1 |
| Terumo: US tariff effect on operating profit | -JPY 12.1 bn | FY Mar-2026 | TERUMO_FY25 p.7 · E-0254 | 1 |
| ICU Medical: largest single distributor, share of revenue | 18% | CY25 | ICUI_10K25 p.1 · E-0215 | 1 |
| US hospitals using a GPO | 7,000 | Sep-2026 | HSCA_HOME p.1 · E-0379 | 3 |
| US GPO savings (industry-body claim) | USD 55 bn a year | Sep-2026 | HSCA_HOME p.1 · E-0380 | 3 |
| China consumables VBP projects | 78 | CY25 | KDL_AR25 p.17 · E-0285 | 1 |
| China stent VBP price cut | 40–50% | 2020 | DRHP_SMT p.198 · E-0399 | 2 |
| China stent price after VBP | CNY 700 | 2025 | DRHP_SMT p.178 · E-0174 | 2 |
| NPPA ceiling price, drug-eluting stent (DES) | Rs 38,267 per stent | 2025 | DRHP_SMT p.178 · E-0171 | 2 |
| NPPA ceiling price, bare-metal stent (BMS) | Rs 10,510 per stent | 2025 | DRHP_SMT p.178 · E-0172 | 2 |
| Price fall from the 2017 stent cap | up to 85% | 2017 | DRHP_SMT p.178 · E-0173 | 2 |
| Price fall from 2017 MRP caps (stents, knee implants) | 60–80% | 2017 | PD24 p.152 · E-0340 | 2 |
| PM-JAY average dialysis reimbursement | Rs 1,650 per treatment | 2025 | RHP_NEPHRO p.284 · E-0052 | 2 |
| PM-JAY dialysis rate, tier-I cities | Rs 1,800 per treatment | 2022 | RHP_NEPHRO p.264 · E-0007 | 2 |
| PMNDP public-private partnership reimbursement, low end | Rs 1,500 per treatment (range to Rs 1,800; 3% a year escalation) | 2021 | RHP_NEPHRO p.283 · E-0051 | 2 |
| Devices covered by the Public Procurement Order (local preference) | 19 | 2021 | DRHP_HEAL p.129 · E-0122 | 2 |
| Iscon: government share of sales (stale) | 65% | FY17 | BWR_ISCON p.2 · E-0309 | 4 |
| Italy payback settlement for 2015–18 | 25% of invoiced amounts | Jun-2025 | BD_10K25 p.1 · E-0207 | 1 |
| BD: Italy payback accrual | USD 62 mn | FY24 | BD_10K25 p.1 · E-0206 | 1 |
| Italy public spending on devices and services (WebFetch) | EUR 10 bn | 2024/25 | CDM_NUMERI25 p.1 · E-0384 | 3 |
| Discount of emerging vascular-device makers vs incumbents | 20–30% | 2025 | DRHP_SMT p.211 · E-0195 | 2 |
| GST range on devices, India | 5–18% | FY24 | PD24 p.152 · E-0339 | 2 |

### Findings

- **US buying power.**
  - GPOs and IDNs "concentrate purchasing decisions", which pushes prices down. Some distributors also manufacture, and provider consolidation adds buying power [BD_10K25 p.1].
  - Disposables reach US hospitals through acute-care, non-acute, laboratory and drug-wholesale distributors [BD_10K25 p.1]. CMS has proposed widening the DMEPOS competitive-bidding programme [BD_10K25 p.1].
  - Large competitors win "full-line" infusion contracts with hospitals and GPOs. Long-term fixed-price GPO contracts limit how much tariff cost ICU Medical can pass on [ICUI_10K25 p.1].
  - HSCA counts more than 100 national, regional and local GPOs that negotiate discounts on pooled volume [HSCA_HOME p.1].
- **Incumbents are still raising prices.**
  - Terumo offset US tariffs with pricing, mostly in cardiac and vascular (E-0253) [TERUMO_FY25 p.7].
  - Nipro cites "price pass-through measures" and "sales at appropriate price levels" [NIPRO_FY25 pp.3-4].
  - Part of B. Braun Hospital Care's growth came from price adjustments [BBRAUN_AR25 p.44].
  - Baxter cites "one-time pricing benefits and price increases". It also says customers buy on cost-effectiveness and that consolidation among customers and competitors causes pricing pressure [BAX_10K25 p.1].
  - BD's pricing effect was -0.3% (E-0197) [BD_10K25 p.1].
- **China VBP.**
  - Provincial-alliance VBP covers syringes, IV cannulae, vacuum blood-collection tubes and functional infusion sets. KDL won every category of syringes, blood-collection tubes and blood-collection needles in a 24-province tender led by Liaoning [KDL_AR25 p.21].
  - New "anti-involution" rules and supply-capacity requirements aim to concentrate the market in the leading companies [KDL_AR25 p.17].
  - Weigao's price cuts on core products cut its device operating profit sharply. New VBP rounds are rolling out across several regions in 2H26 [WEIGAO_AR25 p.13; WEIGAO_IR26 pp.32, 34].
  - VBP can bring volume to the winners. Nipro's China dialyser sales rose with the "official start of centralized procurement" [NIPRO_FY25 p.10], and Terumo's neuro "sales channels expanded with VBP" [TERUMO_FY25 p.8].
- **Indian procurement.**
  - Orders come case by case rather than under long-term contracts, and tender cycles and public-procurement delays make revenue unpredictable [DRHP_GSURG p.204].
  - Much of the demand for consumables and implants goes through government and institutional tenders, which are cancelled or re-bid and carry strict qualification criteria [DRHP_GSURG p.177].
  - Commodity consumables face "intense competition and pricing pressure" in institutional channels [DRHP_GSURG p.203]. Companies sell on GeM through distributors [DRHP_GSURG p.216].
  - Distribution has several tiers, and regional distributors and merchant exporters often hold the product registrations, which makes distributors hard to replace [DRHP_GSURG pp.212-213].
- **Dialysis procurement in India.**
  - Under PMNDP public-private partnerships, the private partner supplies staff, machines, the RO plant, dialysers and consumables, while the state provides space, power and water. Contracts run 5+5 years, and prices are set by competitive bidding with 3% annual escalation [RHP_NEPHRO pp.280, 283].
  - Organised chains buy centrally to get "cost-effective dialysis equipment and consumables" [RHP_NEPHRO p.282].
- **Buying criteria for surgical consumables** are quality, surgeon preference and cost. The decision-makers are clinicians, payers and hospital administrators [DRHP_HEAL pp.123, 129].
- **Cardiology pricing.**
  - NPPA caps stent prices and PM-JAY's PCI packages include the stent. Bulk buying by large providers further limits pricing [DRHP_INTEG pp.228, 251].
  - The stent caps raised stent usage by about 40% and helped domestic products [DRHP_SMT p.178].
- **Europe.**
  - Italy's Constitutional Court upheld the payback law in Jul-2024. A June-2025 decree lets companies settle 2015–18 claims at 25% of invoiced amounts [BD_10K25 p.1]. This matters for Citieffe and Plan1Health.
  - National and regional tenders, VBP and payback provisions pressure prices [TFX_10K25 p.1]. Price cuts in Germany and other EU markets are letting lower-priced cardiology makers in [DRHP_SMT pp.210-211].

---

## B2 Competitor universe

### Findings

- **Three kinds of players (F&S 2021).**
  - MNCs, in the premium segment.
  - Small domestic makers, low-cost and of variable quality.
  - About 5–6 "independent medical device companies" that are gaining share with MNC-grade quality at competitive prices [DRHP_HEAL pp.124, 127].
- **How other offer documents benchmark Polymed.**
  - Polymed is G Surgiwear's only listed peer in its Basis for Offer Price [DRHP_GSURG p.144]. 1Lattice's peer table calls it "Polymed Medical Devices" and lists it with Romsons, Meril, Biorad and global majors [DRHP_GSURG pp.219-221].
  - Integris and SMT both name Polymed and Laxmi Dental as their listed peers [DRHP_INTEG p.166; DRHP_SMT pp.120, 126].
  - Healthium said no comparable company was listed [DRHP_HEAL pp.98-104].
- **How the F&S reports classify Polymed.**
  - "Infusion, Vascular Access", one acquisition up to Mar-2025, medium diversification, Class I and II products only (E-0149) [DRHP_INTEG p.222].
  - SMT's F&S report says "Polymed is most focused on consumables" and ticks only PTCA balloons among its vascular products [DRHP_SMT p.210].
  - Integris's F&S report also ticks diagnostic catheters and other vascular accessories [DRHP_INTEG pp.251-252].
- **CRISIL on dialysers.** CRISIL calls Polymed the "first Indian company to indigenously manufacture dialyser in India" [PD24 p.131].
- **MNCs use India as a base.** BD manufactures in India, one of 18 countries, and runs R&D centres in India and China [BD_10K25 p.1]. ICU Medical does R&D in the US and India [ICUI_10K25 p.1].
- **Capital flowing to Indian rivals.**
  - Recent deals: KKR–Healthium, ADIA–Meril, Warburg Pincus–Micro Life (USD 210 mn, 2022) and Kotak Alt–Biorad (USD 48 mn, 2024) (E-0146, E-0147, E-0402, E-0403) [DRHP_INTEG p.216].
  - Temasek–Romsons, completed 22-Sep-2026 [MB_ROMSONS p.1; BS_ROMSONS p.1]. Romsons will look at acquisitions in India and abroad and at a listing "at an appropriate time" [BS_ROMSONS p.1; NP_ROMSONS p.1].
  - Healthium plans a debt-funded acquisition of 75% of an advanced-surgery device maker. The initial tranche costs about Rs 600 cr (E-0307), funded by commercial paper of up to Rs 650 cr [ICRA_HEAL p.3].

### Competitor table – India

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| Hindustan Syringes & Medical Devices (HMD) | New Delhi; plants in Faridabad [PD24 pp.162-163] | Syringes (Dispovan, Kojak AD), needles, IV cannula (Cathy+), scalp-vein sets, blood-collection tubes (Vaku-8), blades [HMD_WEB p.1] | FY23 operating income Rs 8,453 mn; OPBDIT margin 13.0%; exports 20.8% (E-0343, E-0347, E-0349) [PD24 pp.165-166]. Capacity >4.5 bn units a year (E-0299) [HMD_WEB p.1]; 2014 plant makes 350 mn syringes and 36 mn IV cannulas a year (E-0300, E-0301) [HMD_INFRA p.1]; >3 bn needles a year (E-0407) | Web figures are self-reported. HMD claims to be the world's largest maker of auto-disable (AD) syringes and to source its own raw materials. The same page gives >4,500 and 10,000+ dealers (E-0405, E-0406) [HMD_WEB p.1] |
| Romsons Group | India (founded in Amritsar, 1952) [MB_ROMSONS p.1] | Urology, anaesthesia, transfusion, respiratory, cardiac and patient-care disposables [DRHP_GSURG p.211] | FY24 revenue Rs 8,621.18 mn; EBITDA margin 26.76%; PAT margin 16.0% (E-0100, E-0102, E-0103) [DRHP_GSURG pp.219-220]. >80 countries and >1,500 distributors (E-0297, E-0404) [MB_ROMSONS p.1] | Temasek minority stake completed 22-Sep-2026. Reported talks put it at 15–20% at about USD 1 bn (E-0295, E-0296) [MB_ROMSONS p.1]. 1Lattice says 65+ countries [DRHP_GSURG p.211] |
| Healthium Medtech (KKR) | Bengaluru [PD24 p.162] | Sutures and surgical needles, advanced surgery, arthroscopy, UK urology [ICRA_HEAL p.1; DRHP_HEAL pp.137-139] | FY25 operating income Rs 860.9 cr; margin 12.5%, or 26.7% before ESOP cost; exports 48.5% (E-0304 to E-0306) [ICRA_HEAL pp.1-4]. FY23 Rs 7,085 mn (E-0346) [PD24 p.165] | KKR deal about USD 839 mn (E-0146). ICRA outlook Negative because of the debt-funded acquisition [ICRA_HEAL p.1] |
| Meril Life Sciences (Micro Life Sciences) | India (Vapi) | Stents, balloons, orthopaedics, surgical | FY24 revenue Rs 12,016.4 mn; EBITDA margin 25.92% (E-0104, E-0105) [DRHP_GSURG p.219] | ADIA paid USD 200 mn for 3% (E-0147); Warburg Pincus invested USD 210 mn in 2022 (E-0402) [DRHP_INTEG p.216]. It is unclear which Meril entity the figures cover |
| BD India | New Delhi; plant at Bawal [PD24 p.162] | Indian unit of BD | FY23 operating income Rs 13,014 mn; OPBDIT margin 9.8%; exports 15.9% (E-0344, E-0348, E-0350) [PD24 pp.165-166] | |
| B. Braun Medical (India) | Mumbai; 3 plants [PD24 p.162] | B. Braun group range (infusion therapy, anaesthesia, extracorporeal blood treatment and others) | FY23 operating income Rs 6,106 mn; OPBDIT margin 9.2%; exports 23.1% (E-0345, E-0354, E-0351) [PD24 pp.165-166] | |
| Nipro India | Plant at Satara (parent Nipro, Japan) | Dialysers | n.a. | Greenfield PLI dialyser plant inaugurated 2-Mar-2024 [PIB_PLI_MAR24 p.1] |
| Terumo Penpol (Terumo BCT) | India | Blood bags | 30 mn bags a year in 2018; 55% exported (E-0311, E-0312) [BT_TERUMOBCT p.1] | Stale 2018 data, read via WebFetch. The 2018 plan was to reach 40 mn |
| HLL Lifecare (Government of India PSU) | Thiruvananthapuram | Blood bags (HL Haemopack, Donato), sutures | Blood-bag capacity 12.5 mn pieces a year (E-0319) [HLL_AFT p.1] | Claims a "dominant market share" in Indian blood bags. First BIS licence under IS/ISO 3826-1 (Aug-2023) [HLL_BISPR p.1] |
| Iscon Surgicals | Plants in Jodhpur | Syringes, AD syringes, needles, infusion sets, ophthalmic cannulas | 240 mn syringes a year of capacity (Mar-2012); FY17 revenue Rs 48.65 cr (E-0308, E-0310) [BWR_ISCON pp.2-3] | Stale. Government share of sales 65% (E-0309) |
| Lars Medicare | India | IV cannula incl. safety, infusion sets, syringes; contract OEM | Claims distributors in 100+ countries (E-0387) [LARS_WEB p.1] | Self-reported |
| Angiplast | Ahmedabad | Infusion, transfusion, HD blood-tubing sets, transducer protectors, urology, gastro, components; OEM | 80% of production exported (E-0386) [ANGIPLAST_WEB p.1] | Self-reported. Has in-house EtO sterilisation |
| SMT (Sahajanand) | Surat [PD24 p.163] | Coronary stents, balloons | FY23 operating income Rs 7,959 mn (D-0509) [PD24 p.165]; 25.0% of India DES volume (E-0194) | |
| Integris Medtech | India | DES, balloons, diagnostics | 22.0% of India DES volume (E-0165); FY25 gross margin 43.95% (E-0170) [DRHP_INTEG pp.234, 260] | |
| Biorad Medisys | India | Orthopaedic implants | FY24 revenue Rs 3,386.4 mn (E-0108) [DRHP_GSURG p.219] | Kotak Alt invested USD 48 mn in 2024 (E-0403) |

### Competitor table – global

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| BD | US | Peripheral IV catheters (PIVC), PICC, syringes and needles, Vacutainer, ports, urology, critical care | Revenue USD 21,840 mn FY25 (E-0196); Medication Delivery Solutions USD 4,575 mn (E-0198); Medical segment operating margin 36.1% (E-0201) [BD_10K25 p.1] | Bought Edwards Critical Care for USD 3.914 bn (E-0208) |
| B. Braun | Germany | Infusion, regional anaesthesia, dialysis (Avitum), surgery (Aesculap) | Revenue EUR 9,396.4 mn CY25; EBITDA margin 13.0% (E-0241, E-0249) [BBRAUN_AR25 pp.43-45] | Built finished-goods inventory to 19.8 weeks for supply security [BBRAUN_AR25 p.43] |
| ICU Medical | US | Infusion consumables and systems, ports, anaesthesia and respiratory | Consumables USD 1,109.2 mn CY25; gross margin 36.8% (E-0209, E-0213) [ICUI_10K25 p.1] | Plants in the US, Costa Rica, Mexico and Czech Republic |
| Baxter | US | IV solutions, infusion systems | Infusion Therapies & Technologies USD 4,101 mn CY25 (E-0378) [BAX_10K25 p.1] | Sold its kidney-care business (Vantive) |
| Teleflex | US | Arrow vascular access, interventional cardiology; acute care and OEM being divested | Continuing revenue USD 1,992,713 thousand CY25 (E-0220) [TFX_10K25 p.1] | See A4.6 and A4.10 |
| Terumo | Japan | Cardiac and vascular access devices, infusion, blood and cell technologies | Revenue 11,319 (100M JPY) FY Mar-2026 (E-0252) [TERUMO_FY25 p.4] | |
| Nipro | Japan | Dialysers, blood circuits, AV fistula (AVF) needles, needles, blood-collection tubes, balloons | Revenue 6,605.3 (100M JPY) FY Mar-2026 (E-0264) [NIPRO_FY25 p.26] | Adding capacity in Odate, Thailand and Vietnam [NIPRO_FY25 p.7] |
| Fresenius Medical Care | Germany | Dialysis products and services | Care Enablement EUR 5,476 mn CY25 (E-0239) [FMC_20F25 p.1] | 38% of dialyser volume (E-0233) |
| Vantive (Carlyle) | US | Peritoneal dialysis (PD), HD, CRRT | 2024 sales USD 4,513 mn (E-0376) [BAX_10K25 p.1] | Bought for USD 3.8 bn (E-0377) |
| Intersurgical | UK | Airway, anaesthesia, respiratory | Paying USD 530 mn for Teleflex Acute Care (E-0222) [TFX_10K25 p.1] | |

### Competitor table – China

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| Shandong Weigao Group | Weihai, Shandong (HKEX 1066) | Infusion sets, syringes, IV cannulae, flush syringes, blood management, orthopaedics, dialysis (Weigao Blood Purification) | Revenue RMB 13,388,890 thousand CY25; overseas 27% (E-0265, E-0268) [WEIGAO_AR25 pp.7, 16]. 1H26 RMB 6,848,991 thousand (E-0273) [WEIGAO_IR26 p.25] | Its Indonesia JV starts local production in 2H26 [WEIGAO_IR26 p.34] |
| Shanghai Kindly (KDL) | Shanghai (603987.SH) | Syringes, needles from its own needle tubing, infusion sets; OEM, ODM and own brand | Revenue RMB 2,298,384,784.91 CY25; international RMB 795,430,481.34 (E-0280, E-0281) [KDL_AR25 pp.24-25] | On FDA import alert since May-2024 [FDA_RU240517 p.1]. Calls itself a top-10 Chinese exporter of polymer consumables [KDL_AR25 p.19] |
| Jiangxi Sanxin Medtec | Jiangxi (300453.SZ) | Dialysers, bloodlines, AVF and dialysis cannulae, HD machines, concentrates | Revenue RMB 16.4 (100 mn); blood purification RMB 13.61 (100 mn) (E-0391, E-0392) [SANXIN_AR25 p.2] | Overseas revenue up 34.56% (E-0393) |
| Jiangsu Shenli, Jiangsu Caina, Zhejiang Longde | China | Plastic syringes | n.a. | Subject to FDA warning letters and import alerts in 2024 [FDA_SYR_WL p.1; FDA_RU240517 p.1; FDA_WL_CAINA p.1] |
| Bain Medical (Guangzhou), Ningbo Tianyi, Guangdong Biolight | China | Dialysis products | n.a. | FMC names them as competitors [FMC_20F25 p.1] |

---

## B4 Export markets (market facts only; agent F owns the policy texts)

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| India medical device exports (CRISIL) | Rs 280 bn; 50–55% of production value | FY24 | PD24 p.140 · E-0333, E-0334 | 2 |
| Europe's share of India's device exports | 22% (USA 16%, UAE 4%, per the row note) | FY24 | PD24 p.140 · E-0335 | 2 |
| Consumables' share of India's device exports | 33% (read from a chart) | FY24 | PD24 p.141 · E-0337 | 2 |
| China's share of India's device imports | 16% | FY24 | PD24 p.140 · E-0336 | 2 |
| India device exports (F&S/IBEF) | USD 3.4 bn; to the US USD 668.9 mn | 2023 | DRHP_SMT p.180 · E-0178, E-0179 | 2 |
| India device exports (F&S 2021) | USD 1,180 mn; consumables 47% of exports in FY20 | 2020 | DRHP_HEAL p.128 · E-0119, E-0120 | 2 |
| China device exports | USD 504.69 (100 mn) | CY25 | KDL_AR25 p.18 · E-0286 | 1 |
| China device exports, customs basis (via Sanxin) | RMB 596.84 (100 mn) | CY25 | SANXIN_AR25 p.34 · E-0394 | 1 |
| China disposable-consumables exports | USD 109.11 (100 mn) | CY25 | KDL_AR25 p.18 · E-0287 | 1 |
| China exports to the US | USD 104.93 (100 mn); -10.77% | CY25 | KDL_AR25 p.18 · E-0289, E-0290 | 1 |
| China exports to the EU and UK | USD 112.61 (100 mn); +8.91% | CY25 | KDL_AR25 p.18 · E-0291 | 1 |
| China exports to Latin America | USD 44.86 (100 mn); +13.29% | CY25 | KDL_AR25 p.18 · E-0292 | 1 |
| China exports to the Middle East | USD 20.65 (100 mn); +6.63% | CY25 | KDL_AR25 p.19 · E-0293 | 1 |
| China exports to ASEAN | USD 54.17 (100 mn) | CY25 | KDL_AR25 p.18 · E-0294 | 1 |
| Weigao US sales | RMB 1,445,792 thousand CY25; -3.3% in 1H26 | CY25 / 1H26 | WEIGAO_AR25 p.16 · E-0267; WEIGAO_IR26 p.25 | 1 |
| ICU Medical: incremental US tariffs | USD 33.6 mn | CY25 | ICUI_10K25 p.1 · E-0217 | 1 |
| US reciprocal tariff on Costa Rica | 15% | Jul-2025 | ICUI_10K25 p.1 · E-0214 | 1 |
| US tariff on EU medical technology (per B. Braun) | 15% | CY25 | BBRAUN_AR25 p.41 · E-0250 | 1 |
| B. Braun: combined currency and US tariff effect | EUR 39.2 mn (negative) | CY25 | BBRAUN_AR25 p.42 · E-0246 | 1 |
| Section 301 tariff on Chinese syringes and needles (announced) | 50% | May-2024 | MTD_SYR p.1 · E-0278 | 3 |

- **Where Chinese exports are going.** The top-3 export markets (US, Germany, Japan) took 31.77% of China's device exports and the top 10 took 52.65% [KDL_AR25 pp.18-19].
  - Chinese makers are shifting towards Europe, Latin America, Central Asia and the Middle East, which are Polymed's main export regions (E-0290 to E-0294).
  - From 1-May-2026, new NMPA rules on export sales certificates support Chinese exports [KDL_AR25 p.17].
  - Weigao is moving from "exporting products" to "exporting capabilities" [WEIGAO_AR25 p.7].
  - Tariffs and market-access changes in some overseas regions raised Weigao's compliance costs [WEIGAO_IR26 p.32].
- **Protectionism affects everyone.**
  - B. Braun says protectionist procurement practices in China and India hurt sales of foreign devices [BBRAUN_AR25 p.41].
  - China restricted European medtech companies from public procurement in response to the EU International Procurement Instrument [BBRAUN_AR25 p.42].
  - Brazil's market grew, but tighter localisation rules limit foreign access [BBRAUN_AR25 p.42].
  - In ASEAN, "enormous pricing pressure" pushed German companies towards high-tech products while Chinese makers gained share [BBRAUN_AR25 p.42].
- **Tariff exposure of MNCs.**
  - Teleflex is hit through EU-made imports and Mexican products that do not qualify under USMCA. Its response is supply-chain changes, more USMCA-compliant output and price increases [TFX_10K25 p.1].
  - Commerce has 270 days to report on the Section 232 investigation, which could add tariffs on top of country tariffs [ICUI_10K25 p.1].
- **International buyers are turning to Indian suppliers** for cost, flexible specifications, packaging and order sizes, and faster turnaround, as an alternative to the US, Europe or China [DRHP_GSURG p.178]. "Many companies are moving manufacturing from China to India" [DRHP_GSURG p.176].

---

## B5 Structural trends

- **Safety devices.**
  - CRISIL lists the safety devices in use: safety IV cannulas and vein sets (infusion); safety blood-collection sets and fistula needles (dialysis); safety Huber needles and closed IV catheter systems (critical care) [PD24 p.137].
  - Vendor estimates disagree on how far safety PIVCs have penetrated: 62% (Persistence, CY25) against 30.3% (FMI, CY26) (E-0358, E-0361) [vendor estimate]. No regional split was found (see gaps).
  - Polymed received US FDA 510(k) clearance for IV safety catheters and administration sets in 2023 [PD24 p.166].
- **DEHP and PVC.**
  - The EU moved the REACH sunset date for DEHP in medical devices from May-2025 to 1-Jul-2030, with a latest application date of 1-Jan-2029 (E-0382) [GMED_DEHP p.2; FORESIGHT_DEHP p.1].
  - The main uses affected are PVC blood bags, tubing and infusion sets. HLL's Haemopack bags are PVC [HLL_BISPR p.1].
  - ICU Medical cites demand for environmentally friendly products and "materials of concern" as a competitive factor [ICUI_10K25 p.1].
  - FMC cut the material used in its 5008 bloodline portfolio [FMC_20F25 p.1].
- **EtO vs radiation sterilisation.**
  - About 50% of US sterile devices are EtO-sterilised (E-0381) [FDA_ETO p.1, WebFetch]. The FDA backs alternatives, calls radiation an "established Category A" method, and runs a pilot that makes it easier to switch between radiation sources [FDA_ETO p.1].
  - The EPA's NESHAP rule took effect on 5-Apr-2024, and device sterilisers were later given until Apr-2028. The EPA's interim registration decision (14-Jan-2025) tightens exposure limits and could reduce sterilisation capacity [BD_10K25 p.1].
  - Sterigenics sites have faced lawsuits [TFX_10K25 p.1]. Angiplast sterilises with EtO in-house [ANGIPLAST_WEB p.1].
- **Home dialysis is small.**
  - F&S puts PD below 5% and home HD below 1% of patients, and expects PD's share to stay minimal or fall over 2024–29 (E-0015, E-0016) [RHP_NEPHRO pp.267, 269].
  - FMC puts home therapy (mostly PD) at 11% globally and 15% in the US, with in-centre HD at 89% (E-0227, E-0228) [FMC_20F25 p.1].
- **More single-use dialysers.** Nipro expects Asian dialyser growth from the "shift to single use", although Indonesia's move is slow [NIPRO_FY25 pp.10, 15].
- **Reshoring and China+1.**
  - The drivers:
    - Hourly manufacturing wages are below USD 2 in India, USD 5–6 in China and USD 28–30 in the US (E-0184, E-0185) [DRHP_SMT p.185].
    - US–China decoupling and local-content rules [DRHP_INTEG p.251].
    - FDA action against Chinese syringes (A4.1).
    - The 2021 F&S report already called the "shift away from China" a tailwind for Indian share gains [DRHP_HEAL pp.125, 127].
  - Chinese makers are responding by localising abroad (Weigao's Indonesia JV) [WEIGAO_IR26 p.34].
- **Supply security.**
  - Hurricane Helene damaged a competitor's US IV-solutions plant in 3Q2024 and caused a national IV-fluid shortage [ICUI_10K25 p.1].
  - B. Braun raised finished-goods inventory to 19.8 weeks [BBRAUN_AR25 p.43].
- **Regulatory barriers are rising.**
  - EU MDR adds complexity and delays launches [DRHP_INTEG p.226]. It raises entry barriers and drives consolidation [DRHP_HEAL p.125].
  - Europe's funding crunch is "favorable to cost-leveraged overseas players" [DRHP_INTEG p.226].

---

## A4.1 Infusion therapy (IV cannulae, infusion sets, syringes and needles)

### Market table

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| PIVCs sold worldwide each year | 1.5 bn units | 2024 | CTG_NCT06727240 p.1 · E-0355 | 3 |
| Global PIVC market (TBRC via Research and Markets) [vendor estimate] | USD 5.74 bn | CY25 | VND_RNM_PIVC p.1 · E-0356 | 6 |
| Global PIVC market (Persistence) [vendor estimate] | USD 5.1 bn | CY26 | VND_PMR_PIVC p.1 · E-0357 | 6 |
| Global PIVC market (FMI) [vendor estimate] | USD 7.5 bn | CY26 | VND_FMI_PIVC p.1 · E-0360 | 6 |
| Safety PIVC share [vendor estimate] | 62% (Persistence, CY25) vs 30.3% (FMI, CY26) | CY25/CY26 | VND_PMR_PIVC · E-0358; VND_FMI_PIVC · E-0361 | 6 |
| North America's share of the PIVC market [vendor estimate] | 37% | CY25 | VND_PMR_PIVC p.1 · E-0359 | 6 |
| Global surgical catheters & cannulae (broad definition) | USD 39.4 bn; 7.6% CAGR CY19–24 | CY24 | DRHP_GSURG p.199 · E-0086, E-0087 | 2 |
| India surgical catheters & cannulae | USD 1.3 bn; 9.1% CAGR FY20–25; 34.4% of India surgical disposables | FY25 | DRHP_GSURG p.202 · E-0093, E-0094, E-0092 | 2 |
| Global disposable syringes | USD 25.0 bn | CY29P | DRHP_GSURG p.199 · E-0089 | 2 |
| India disposable syringes | USD 0.8 bn by FY30P; 13.8% of India surgical disposables in FY25 | FY30P | DRHP_GSURG p.202 · E-0096, E-0095 | 2 |
| India consumables & disposables | Rs 195 bn | FY24 | PD24 p.136 · E-0326 | 2 |
| China disposable-consumables exports | USD 109.11 (100 mn); syringe exports +7.32% | CY25 | KDL_AR25 p.18 · E-0287, E-0288 | 1 |

### Competitor table

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| BD (Medication Delivery Solutions) | US | Conventional and safety PIVC, PICC and midlines, needle-free connectors, flush syringes, hypodermics | USD 4,575 mn FY25: US 2,789, international 1,787 (E-0198 to E-0200) [BD_10K25 p.1] | Growth from vascular access and hypodermics, partly offset by China VBP |
| B. Braun (Hospital Care) | Germany | Infusion systems and supplies, regional anaesthesia, nutrition | EUR 5,090.8 mn CY25; +6.1% at constant currency (E-0242, E-0243) [BBRAUN_AR25 p.43] | Price adjustments helped; more competition in LatAm [BBRAUN_AR25 p.44] |
| ICU Medical | US | Infusion sets, needle-free connectors, Jelco PIVC, CSTDs, pumps | Consumables USD 1,109.2 mn (+6.1% constant currency); Infusion Systems USD 684.2 mn, CY25 (E-0209 to E-0211) [ICUI_10K25 p.1] | Sold 60% of its IV-solutions JV to Otsuka for USD 211.2 mn (E-0216) |
| Baxter | US | IV solutions, infusion pumps, administration sets | USD 4,101 mn CY25 (E-0378) [BAX_10K25 p.1] | Exited IV solutions in China |
| Terumo (Medical Care Solutions) | Japan | Infusion, syringes, hospital care | 2,161 (100M JPY) FY Mar-2026 (E-0255) [TERUMO_FY25 p.9] | Top share in infusion and syringe pumps in Japan [TERUMO_TR25 p.6] |
| Nipro | Japan | Needles (SafeTouch), infusion products | Needles 625.4 and infusion 248.5 (100M JPY), FY Mar-2026 (E-0261, E-0262) [NIPRO_FY25 p.25] | |
| Weigao | China | Infusion sets, syringes, IV cannulae, flush syringes | Medical-device products RMB 6,365,388 thousand CY25 (E-0269) [WEIGAO_AR25 p.17] | Flush-syringe prices fell sharply in the latest VBP [WEIGAO_AR25 p.13] |
| Shanghai Kindly (KDL) | China | Syringes, needles, infusion sets | Syringe output 199,297.96 万支 CY25 (万 = 10,000; E-0282); infusion sets 9,532.61 万支 (E-0283) [KDL_AR25 p.26] | Under FDA import alert |
| HMD | India | Syringes, needles, IV cannula, scalp-vein sets | 36 mn IV cannulas a year at its 2014 plant (E-0301) | See B2 |
| Romsons | India | Transfusion and patient-care disposables | FY24 Rs 8,621.18 mn (E-0100) | See B2 |
| Iscon Surgicals | India | Syringes, needles, infusion sets | See B2 (stale) | 65% of sales to government |
| Lars Medicare / Angiplast | India | IV cannula incl. safety (Lars); infusion and transfusion sets (Angiplast) | Web claims only (E-0386, E-0387) | Both also offer contract OEM manufacturing |

### Findings

- **No reliable independent PIVC market size exists.** Vendor figures range from USD 5.1 bn to 7.5 bn and disagree on the safety share (E-0356 to E-0361).
  - The one non-vendor figure is a trial-registry background statement: about 1.5 bn PIVCs are sold a year, up to 90% of hospitalised patients get one, and failure rates reach 69% [CTG_NCT06727240 p.1].
- **Imports vary by product.** India's import dependence is lower for needles and syringes and higher for catheters and cannulas [PD24 pp.139-140].
- **Price pressure and scale.**
  - BD says the "entry into the market of low-cost manufacturers has created increased pricing pressures" [BD_10K25 p.1].
  - KDL runs a fully integrated needle chain, from needle tubing to assembled devices, and has long supplied global majors [KDL_AR25 pp.19, 23].
- **China VBP covers infusion products.** Syringes, IV cannulae and functional infusion sets are all in China's provincial VBP [KDL_AR25 p.21].
- **Opening in the US for non-Chinese syringes and needles.**
  - The FDA told users on 30-Nov-2023 about possible failures of Chinese plastic syringes. It sent warning letters to Jiangsu Shenli, Medline and Sol-Millennium in Mar-2024 [FDA_SYR_WL p.1].
  - It put Zhejiang Longde and Shanghai Kindly on import alert in May-2024 [FDA_RU240517 p.1; AHA_SYR p.1].
  - It wrote to Jiangsu Caina, which made Cardinal Health's Monoject syringes and drew at least 41 US complaints (E-0279) [FDA_WL_CAINA p.1].
  - Distributors including Medline, Merit, Cardinal and Sol-Millennium recalled kits [FDA_SYR_RECALLS p.1].
  - In Aug-2024 the FDA still advised using syringes "not manufactured in China, if possible" [FDA_SYR_UPD p.1; WebFetch rendition, not verbatim].

---

## A4.2 Vascular access and oncology (ports, PICC, CVC, midlines)

### Market table

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global implantable ports [vendor estimate] | USD 1.4 bn (US USD 425.6 mn) | CY25 | VND_RNM_PORTS p.1 · E-0366 | 6 |
| Global PICC [vendor estimate] | USD 1.43 bn | CY26 | VND_RNM_PICC p.1 · E-0368 | 6 |
| Global central venous catheters (CVC) [vendor estimate] | USD 3.07 bn | CY26 | VND_RNM_CVC p.1 · E-0369 | 6 |
| Global HD catheters [vendor estimate] | USD 1.11 bn | CY26 | VND_RNM_HDCATH p.1 · E-0370 | 6 |
| Global catheter introducer sheaths [vendor estimate] | USD 1.93 bn | 2030F | VND_RNM_SHEATH p.1 · E-0367 | 6 |
| Catheters & cannulae share of global surgical disposables | 32.2% (p.198) vs 36.0% (p.199) | CY24 | DRHP_GSURG · E-0084, E-0085 | 2 |
| Italy device sector, exports plus domestic (WebFetch) | EUR 18.5 bn; 4,618 companies | 2024/25 | CDM_NUMERI25 p.1 · E-0383, E-0385 | 3 |

### Competitor table

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| BD (Peripheral Intervention; Medication Delivery Solutions) | US | Ports, chronic dialysis, drainage; PICC, midlines, port access | Peripheral Intervention USD 1,996 mn FY25 (E-0203) [BD_10K25 p.1] | China VBP hit Peripheral Intervention |
| ICU Medical | US | Port-A-Cath ports, oncology CSTDs, PIVC | Consumables USD 1,109.2 mn CY25 (E-0209) [ICUI_10K25 p.1] | Names BD, Baxter, B. Braun, AngioDynamics, Teleflex, EquaShield and Medtronic as competitors [ICUI_10K25 p.1] |
| Teleflex (Vascular) | US | Arrow CVC and PICC, intraosseous access | USD 917,731 thousand CY25 (E-0218) [TFX_10K25 p.1] | |
| Terumo (Cardiac & Vascular) | Japan | Access devices, sheaths | 6,764 (100M JPY) (E-0257) [TERUMO_FY25 p.8] | Claims the top global share in vascular access devices [TERUMO_TR25 p.19] |

### Findings

- **BD's product range overlaps Polymed's infusion and vascular-access lines** [BD_10K25 p.1]:
  - PIVCs and advanced peripheral catheters;
  - PICCs and acute dialysis catheters;
  - ultrasound vascular access;
  - flush syringes, disinfecting caps and needle-free connectors;
  - closed-system transfer devices (CSTDs);
  - spinal and epidural needles;
  - enteral syringes.
- **Italy is Plan1Health's home market.**
  - Public spending on devices is EUR 10 bn, 7.3% of public health spending. About 94% of companies are SMEs [CDM_NUMERI25 p.1, WebFetch].
  - Payback exposure is covered under B1 (E-0206, E-0207).
- **Sizes are vendor-only.** Port, PICC and CVC figures come only from vendors, and none gives a European split (see gaps).

---

## A4.3 Renal (dialysers, bloodlines, AVF needles, HD machines, PD)

### Market table – India

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| India dialysis patients | 0.28 mn rising to 0.52 mn; 12.7% CAGR (2019: 182 thousand) | 2024 to 2029F | RHP_NEPHRO pp.272, 278 · E-0020, E-0038, E-0039, E-0042 | 2 |
| India in-clinic dialysis treatments | 33.9 mn rising to 66.1 mn | 2024 to 2029F | RHP_NEPHRO p.285 · E-0057, E-0058 | 2 |
| India CKD population; prevalence | 123.0 mn; 8.7% | 2024 | RHP_NEPHRO pp.272, 278 · E-0018, E-0036 | 2 |
| India diagnosed ESRD; new ESRD cases a year | 4.2 mn; 325,000 | 2024 | RHP_NEPHRO pp.272, 278 · E-0019, E-0041 | 2 |
| India ESRD patients needing dialysis | 6.9 mn | 2029F | RHP_NEPHRO p.278 · E-0040 | 2 |
| Share of patients who access dialysis (base ambiguous) | ~15% | 2025 | RHP_NEPHRO p.265 · E-0010 | 2 |
| HD machines installed / required / gap | 40,000 / 105,000 / 65,000 | 2025 | RHP_NEPHRO p.279 · E-0043 to E-0045 | 2 |
| Patients dialysed three times a week | 50% | 2025 | RHP_NEPHRO p.279 · E-0046 | 2 |
| Nephrologists | 2,600 | 2025 | RHP_NEPHRO p.279 · E-0047 | 2 |
| Dialysis clinics | ~5,000 (2023); 4,000 (2020); 700 or ~1,000 (2010) | various | RHP_NEPHRO pp.264, 277 · E-0008, E-0035, E-0009, E-0034 | 2 |
| PMNDP (national dialysis programme) clinics; machines | 1,621 (Mar-2025); 11,148 (Feb-2025) | 2025 | RHP_NEPHRO pp.264, 280 · E-0048, E-0002 | 2 |
| India dialysis services market | USD 818.0 mn rising to USD 1,979.0 mn | 2024 to 2029F | RHP_NEPHRO p.285 · E-0054, E-0055 | 2 |
| India in-clinic HD services | USD 787.3 mn | 2024 | RHP_NEPHRO p.286 · E-0059 | 2 |
| Organised providers' share | 16.0% of volumes (2019) to 18.5% (2029F); ~20% (2024); 13.4% of revenue (2019) | various | RHP_NEPHRO pp.264, 282, 285 · E-0005, E-0006, E-0056, E-0049 | 2 |
| Annual HD spend per patient | USD 2,700 India vs USD 37,000 US | 2024 | RHP_NEPHRO p.272 · E-0022, E-0023 | 2 |
| Dialysis share of PM-JAY disbursements | 14% | 2025 | FMC_20F25 p.1 · E-0238 | 1 |
| NephroPlus treatments (largest chain) | 2,922,869 | FY25 | RHP_NEPHRO p.282 · E-0050 | 2 |

### Market table – global

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global dialysis patients | 4.26 mn (F&S, 2024); 4.5 mn (FMC, CY25); 7 mn (FMC, 2035F) | various | RHP_NEPHRO p.269 · E-0012; FMC_20F25 p.1 · E-0224, E-0226 | 2 / 1 |
| Growth in dialysis patients | 5.0% CAGR 2024–29F (F&S); 4–5% a year (FMC) | various | E-0014; E-0225 | 2 / 1 |
| In-centre HD share of patients | 89% | CY25 | FMC_20F25 p.1 · E-0227 | 1 |
| PD share of patients | 11% (FMC) vs <5% (F&S) | CY25 / 2024 | E-0228; E-0015 | 1 / 2 |
| Global dialysis market, products plus services | EUR 81–85 bn | CY25 | FMC_20F25 p.1 · E-0229 | 1 |
| Global dialysis products market | EUR 16 bn; FMC share 35% | CY25 | FMC_20F25 p.1 · E-0230, E-0231 | 1 |
| Global dialysers sold | 450 mn units; FMC share 38% | CY25 | FMC_20F25 p.1 · E-0232, E-0233 | 1 |
| HD machines installed in the year | 110,000 | CY25 | FMC_20F25 p.1 · E-0234 | 1 |
| Global dialyser market (IMARC) [vendor estimate] | USD 4.0 bn | CY25 | VND_RNM_DIALYZER p.1 · E-0363 | 6 |
| Global dialysis services revenue | USD 75.2 bn rising to USD 106.2 bn | 2024 to 2029F | RHP_NEPHRO p.275 · E-0029, E-0030 | 2 |
| Acute kidney failure patients on CKRT | 1.1 mn | CY25 | FMC_20F25 p.1 · E-0236 | 1 |
| FMC + DaVita share of US dialysis units | 70% | 2024 | RHP_NEPHRO p.271 · E-0017 | 2 |

### Competitor table

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| Fresenius Medical Care | Germany | Dialysers, bloodlines, AVF sets, HD machines, PD, CKRT | Care Enablement EUR 5,476 mn CY25; operating margin 6.0% (E-0239, E-0237) [FMC_20F25 p.1] | 38% of dialyser volume. Bloodline plants in Italy, Türkiye and Mexico; its Changshu (China) plant makes bloodlines, AVF sets and dialysers |
| Nipro | Japan | Dialysers, HDF filters, blood circuits, AVF needles, machines | Dialysis-related 2,161.6 (100M JPY), of which dialysers 1,171.3 and machines 319.0, FY Mar-2026 (E-0258 to E-0260) [NIPRO_FY25 p.25] | PLI dialyser plant in Satara, India [PIB_PLI_MAR24 p.1]. Its machine sales fell against the previous year's large tenders in India and the Middle East [NIPRO_FY25 p.10] |
| Vantive (Carlyle) | US | PD, HD, CRRT | 2024 sales USD 4,513 mn (E-0376) | Standalone and PE-owned since 31-Jan-2025 [BAX_10K25 p.1] |
| B. Braun Avitum | Germany | Dialysis products and centres, continence | EUR 1,900.5 mn CY25 (E-0244) [BBRAUN_AR25 p.45] | HD-machine earnings fell in 2025 |
| Jiangxi Sanxin Medtec | China | Dialysers, bloodlines, AVF cannulae, HD machines | Blood purification RMB 13.61 (100 mn); overseas revenue RMB 36,884.55 (10 thousand), +34.56% (E-0392, E-0393) [SANXIN_AR25 pp.2, 39] | 83 overseas product registrations [SANXIN_AR25 p.38]. Spins its own hollow-fibre membranes [SANXIN_AR25 p.16] |
| Weigao Blood Purification | China | Dialysis consumables | n.a. | A transaction involving the unit is in progress [WEIGAO_AR25 p.6]. FMC names it a competitor [FMC_20F25 p.1] |
| Toray, Asahi Kasei, Nikkiso, JMS (Japan); Mozarc, Outset, Quanta (home/HD systems) | various | Dialysers, machines | n.a. | FMC names them as competitors [FMC_20F25 p.1]. FMC names no Indian maker |
| Angiplast | India | HD blood-tubing sets, transducer protectors | n.a. | Calls these its core products [ANGIPLAST_WEB p.1] |

### Findings

- **What Polymed's renal plant makes.** The PLI plant at Faridabad makes dialysers, dialysis machines, PD kits, fistula needles, bloodlines and transducer protectors [PIB_PLI_MAR24 p.1].
- **Demand context.**
  - About half of Indian CKD patients first present at end-stage, so they start on emergency HD [RHP_NEPHRO p.279].
  - 90% of dialysis facilities are urban, and about 70% of patients are in nine states [RHP_NEPHRO p.278].
  - HD is more than 98% of dialysis therapy in India [RHP_NEPHRO p.286].
- **Market history.**
  - Before 2000, most dialysis equipment and supplies were imported [RHP_NEPHRO pp.276-277].
  - Private providers adopted high-flux membranes and automated machines, and FMC has brought in its advanced equipment [RHP_NEPHRO p.281].
  - DaVita left India in 2022 by selling to NephroPlus [RHP_NEPHRO p.275].
- **Nipro's regional outlook.** Nipro expects Asian dialyser growth from the shift to single use, Chinese growth from centralised procurement, and Americas growth from renewing large contracts with major dialysis providers [NIPRO_FY25 p.15].
- **China.**
  - China's dialysis VBP has finished a new renewal round, and the market is concentrating.
  - The VBP winners use the capacity those wins build to go after overseas markets, where dialysis rates are rising fast in Southeast Asia and Latin America. Chinese leaders are replacing foreign makers through scale and full-chain advantages [SANXIN_AR25 p.34].
- **Dialysis safety devices.** CRISIL lists safety fistula needles and safety blood-collection sets as the dialysis safety devices [PD24 p.137].

---

## A4.4 Blood management (blood bags)

### Market table

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global blood donations | 120.4 mn | latest (2023 data) | WHO_BLOOD p.1 · E-0400 | 1 |
| Donations per 1,000 people, lower-middle-income countries | 8.5 (high-income 28.9) | 2023 data | WHO_BLOOD p.1 · E-0401 | 1 |
| India blood units collected | 157.14 lakh (CY25); 146.01 lakh (CY24) | CY25 / CY24 | FACTLY_BLOOD p.1 · E-0315, E-0316 | 3 |
| India blood and components discarded | 17.43 lakh units | CY25 | FACTLY_BLOOD p.1 · E-0317 | 3 |
| India annual blood requirement (government estimate) | 14.6 mn units | 2025 | ORF_BLOOD p.1 · E-0318 | 3 |
| India blood collections; blood-bag market (stale, WebFetch) | 11 mn a year; ~USD 50 mn | 2018 | BT_TERUMOBCT p.1 · E-0313, E-0314 | 3 |
| Global blood bags (360iResearch) [vendor estimate] | USD 621.42 mn | CY26 | VND_RNM_BLOODBAG p.1 · E-0362 | 6 |
| EU REACH sunset date for DEHP in devices | 1-Jul-2030 | Reg (EU) 2023/2482 | GMED_DEHP p.2 · E-0382 | 3 |

### Competitor table

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| Terumo Blood and Cell Technologies (Terumo Penpol in India) | Japan | Blood bags, Reveos automated whole-blood processing, Rika plasma collection | 2,310 (100M JPY) FY Mar-2026 (E-0256) [TERUMO_FY25 p.10]. Terumo Penpol made 30 mn bags a year in 2018 and exported 55% (E-0311, E-0312) [BT_TERUMOBCT p.1] | Won Reveos tenders in Asia [TERUMO_FY25 p.10] |
| HLL Lifecare | India (Thiruvananthapuram) | PVC blood bags (HL Haemopack, Donato) | 12.5 mn pieces a year (E-0319) [HLL_AFT p.1] | Claims a "dominant market share" in India and exports to 20+ countries [HLL_BISPR p.1; HLL_AFT p.1] |
| Weigao (blood management) | China | Blood collection, storage and separation consumables and equipment | RMB 995,113 thousand CY25 (E-0270) [WEIGAO_AR25 p.17] | Serves 419 blood stations in China (E-0272) |

### Findings

- **India supply is growing but wasteful.**
  - India's reported blood collection rose 24% from 2023 to 2025, while discards more than doubled. Expiry causes about 45–46% of discards [FACTLY_BLOOD p.1].
  - About 70% of blood comes from voluntary donors. Only about 26% of people in eight EAG states live within 30 minutes of a blood bank ("blood deserts") [ORF_BLOOD p.1].
- **Collection is low in poorer countries.** 55 countries collect fewer than 10 donations per 1,000 people, all of them low- or middle-income [WHO_BLOOD p.1]. This is headroom in Polymed's RoW markets.
- **DEHP transition ahead.** The move to DEHP-free products is due by 2030 in the EU (B5).

---

## A4.5 Diagnostics (blood-collection tubes)

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global blood-collection tubes (360iResearch) [vendor estimate] | USD 4.64 bn | CY26 | VND_RNM_BCT p.1 · E-0364 | 6 |
| BD Specimen Management (BD Vacutainer) | USD 1,871 mn | FY25 (Sep-2025) | BD_10K25 p.1 · E-0202 | 1 |

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| BD | US | Vacutainer tubes and needles | USD 1,871 mn (E-0202) | Sales fell in China [BD_10K25 p.1] |
| Nipro | Japan | Neotube vacuum blood-collection tubes | n.a. | [NIPRO_FY25 p.22] |
| Shanghai Kindly (KDL) | China | Blood-collection tubes and needles | n.a. | Won every tube and needle category in a 24-province VBP [KDL_AR25 p.21] |
| HMD | India | Vaku-8 evacuated tubes | n.a. | Technology from Israel's Estar [HMD_WEB p.1] |
| Weigao | China | Blood-collection consumables | Within RMB 995,113 thousand (E-0270) | |

- **Tubes are in China's VBP.** Vacuum blood-collection tubes are covered by China's provincial VBP [KDL_AR25 p.21].
- **No India figure.** No market size for Indian blood-collection tubes was found (see gaps).

---

## A4.6 Anaesthesia, respiratory and critical care

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global endotracheal tubes [vendor estimate] | USD 2.54 bn | CY26 | VND_RNM_ETT p.1 · E-0374 | 6 |
| Global anaesthesia face masks [vendor estimate] | USD 252.42 mn | CY25 | VND_RNM_ANMASK p.1 · E-0375 | 6 |
| Global CVC [vendor estimate] | USD 3.07 bn | CY26 | VND_RNM_CVC p.1 · E-0369 | 6 |
| Acute kidney failure patients on CKRT | 1.1 mn | CY25 | FMC_20F25 p.1 · E-0236 | 1 |

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| Intersurgical | UK | Airway, anaesthesia, respiratory; adding Teleflex's urology care | Buying Teleflex Acute Care and Interventional Urology for USD 530 mn (E-0222) | Closing expected 2H2026 [TFX_10K25 p.1] |
| ICU Medical (Vital Care) | US | Anaesthesia, respiratory, haemodynamic monitoring | USD 437.9 mn CY25 (E-0212) [ICUI_10K25 p.1] | Fell after the sale of the IV-solutions JV |
| BD | US | Spinal and epidural needles and trays; advanced patient monitoring | Bought Edwards Critical Care for USD 3.914 bn (E-0208) [BD_10K25 p.1] | |
| B. Braun (Hospital Care) | Germany | Regional anaesthesia | EUR 5,090.8 mn (E-0242) | |
| Romsons / Angiplast | India | Anaesthesia and respiratory disposables; oxygen cannulas and masks | See B2 | [DRHP_GSURG p.211; ANGIPLAST_WEB p.1] |

- **Consolidation.** Anaesthesia and respiratory consumables are consolidating: Teleflex is carving out Acute Care and Intersurgical is buying it [TFX_10K25 p.1].
- **CKRT.** FMC puts its CKRT share at about 30% (E-0236 note) [FMC_20F25 p.1].
- **No combined market size** for anaesthesia and respiratory disposables was found (see gaps).

---

## A4.7 Gastro, urology, surgery and wound drainage

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global surgical disposables | USD 109.5 bn rising to USD 151.0 bn | CY24 to CY29P | DRHP_GSURG p.174 · E-0062, E-0063 | 2 |
| India surgical disposables | USD 3.9 bn rising to USD 6.4 bn | FY25 to FY30P | DRHP_GSURG p.177 · E-0070, E-0071 | 2 |
| India wound-management products | USD 0.8 bn | FY25 | DRHP_GSURG p.202 · E-0097 | 2 |
| Global surgical drapes | USD 5.5 bn | CY24 | DRHP_GSURG p.200 · E-0090 | 2 |
| Global surgical drainage devices (FMI) [vendor estimate] | USD 1.7 bn | CY25 | VND_FMI_DRAIN p.1 · E-0395 | 6 |
| Global urology consumables (2021 vintage) | USD 2.38 bn; Europe USD 1.3 bn; UK USD 331.1 mn | 2020 | DRHP_HEAL p.137 · E-0127, E-0128, E-0130 | 2 |
| Intermittent catheters' share of Europe urology consumables | 66% | 2020 | DRHP_HEAL p.137 · E-0129 | 2 |
| UK urology share: Coloplast; Coloplast + BD | 39.32%; 47.88% | FY21 | DRHP_HEAL p.139 · E-0131, E-0132 | 2 |
| Global Foley catheters (Grand View) [vendor estimate] | USD 1.9 bn | CY25 | VND_RNM_FOLEY p.1 · E-0371 | 6 |
| Global intermittent catheters (IMARC) [vendor estimate] | USD 3.1 bn | CY25 | VND_RNM_ICATH p.1 · E-0372 | 6 |
| Global enteral feeding devices [vendor estimate] | USD 3.18 bn | CY26 | VND_RNM_ENTERAL p.1 · E-0373 | 6 |
| India surgical consumables (wound closure, wound care, gloves; 2021 vintage) | USD 364.1 mn; Ethicon 16%, Healthium 7.91% (FY21) | 2020 | DRHP_HEAL pp.131, 134 · E-0124 to E-0126 | 2 |

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| BD (Urology & Critical Care) | US | Indwelling, intermittent and external urine catheters | USD 1,649 mn FY25 (E-0204) [BD_10K25 p.1] | |
| Coloplast; Hollister; Dentsply (Wellspect) | Denmark; US; US | Intermittent catheters, collection devices | Coloplast 39.32% of UK (FY21) | Lead the UK market with BD [DRHP_HEAL pp.137-139] |
| Teleflex, moving to Intersurgical | US / UK | Urology-care catheters and collectors | Part of the USD 530 mn deal (E-0222) | [TFX_10K25 p.1] |
| B. Braun (Aesculap) | Germany | Surgery | EUR 2,374.3 mn CY25 (E-0245) [BBRAUN_AR25 p.44] | |
| Healthium | India | Sutures, surgical consumables, UK urology | See B2 | |
| Angiplast; Romsons | India | Feeding bags, Ryle's tubes, urine bags, Foley and Nelaton catheters, wound drainage; urology | See B2 | [ANGIPLAST_WEB p.1; DRHP_GSURG p.211] |

- **UK urology.**
  - Independent suppliers (Clinisupplies, Great Bear, L.IN.C) are gaining share through hospital and community contracts. The share shift has caused marginal declines in selling prices for collection devices [DRHP_HEAL pp.137-139].
  - Direct-to-consumer and home-delivery channels earn higher prices than institutional sales [DRHP_HEAL pp.137-139].
- **Surgical gloves in India** are dominated by domestic companies because buyers are price-sensitive [DRHP_HEAL p.133].
- **No India figures** for urology, drains or enteral feeding were found (see gaps).

---

## A4.8 Cardiology (PendraCare guiding and diagnostic catheters, introducers; own stents and balloons)

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global cardiovascular devices | USD 64.8 bn rising to USD 100.6 bn | 2024 to 2029F | DRHP_INTEG p.225 · E-0150, E-0151 | 2 |
| Global interventional cardiology devices | USD 14.3 bn; stents, catheters and PTCA balloons ~80% | 2024 | DRHP_INTEG pp.229, 231 · E-0156, E-0157 | 2 |
| Global vascular interventional devices | USD 13,194.1 mn | 2024 | DRHP_SMT p.195 · E-0191 | 2 |
| Global interventional cardiology catheters (diagnostic, interventional, EP) | USD 3.6 bn; 10.6% CAGR to 2029F | 2024 | DRHP_INTEG p.232 · E-0159, E-0160 | 2 |
| Global cardiac accessories (guiding and diagnostic catheters, sheaths, inflation devices, Y-connectors) | USD 1,147.2 mn | 2024 | DRHP_SMT p.194 · E-0188 | 2 |
| Global PTCA balloons | USD 2.9 bn (Integris F&S) vs USD 1,250.5 mn (SMT F&S) | 2024 | E-0161; E-0189 | 2 |
| Global coronary stents | USD 5.7 bn (Integris F&S) vs USD 4,559.4 mn (SMT F&S) | 2024 | E-0158; E-0190 | 2 |
| Global introducer sheaths [vendor estimate] | USD 1.93 bn | 2030F | VND_RNM_SHEATH p.1 · E-0367 | 6 |
| India cardiovascular devices | USD 2.3 bn; 13.5% CAGR 2024–29F | 2024 | DRHP_INTEG p.228 · E-0154, E-0155 | 2 |
| India interventional cardiology | USD 480.0 mn rising to USD 817.6 mn (Integris F&S) vs USD 355.5 mn for vascular interventional (SMT F&S) | 2024 to 2029F | E-0162, E-0163; E-0187 | 2 |
| India coronary stents | USD 249.2 mn | 2024 | DRHP_SMT p.195 · E-0192 | 2 |
| India PCI procedures | 0.81 mn; below 500 per million people (US 1.2 mn procedures) | 2024 | DRHP_SMT pp.189, 198 · E-0396 to E-0398 | 2 |
| India cath labs: installed vs required | 2,500 vs 7,500 | 2023 | DRHP_INTEG p.227 · E-0152, E-0153 | 2 |
| Cardiology's share of the India device market (CRISIL) | 11% | FY24 | PD24 p.138 · E-0330 | 2 |
| Indian companies' share of India stent volume | 60% | FY25 | DRHP_INTEG p.234 · E-0164 | 2 |
| Top global players' share of DES | >90% | 2025 | DRHP_SMT p.210 · E-0193 | 2 |

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| Terumo (Cardiac & Vascular) | Japan | Radial access, guiding and diagnostic catheters, sheaths, guidewires | 6,764 (100M JPY) FY Mar-2026 (E-0257) [TERUMO_FY25 p.8] | Claims the top global share in vascular access devices since its 1985 angiographic catheter [TERUMO_TR25 p.19] |
| Teleflex Interventional (now including BIOTRONIK VI) | US | Drug-coated balloons (DCB), stents, balloons, catheters | USD 647,792 thousand CY25 (E-0219) [TFX_10K25 p.1] | Bought BIOTRONIK VI for EUR 704.3 mn (E-0221) |
| Nipro (vascular) | Japan | Balloon catheters, Y-connectors | 365.2 (100M JPY) (E-0263) [NIPRO_FY25 p.25] | |
| Medtronic, Abbott, Boston Scientific, B. Braun, Biotronik, MicroPort | various | Stents, balloons, catheters | Top players hold >90% of DES (E-0193) | [DRHP_INTEG pp.232-234] |
| SMT; Integris; Meril (Micro Life); Relisys | India | DES, balloons, accessories | SMT 25.0% and Integris 22.0% of India DES volume, each on its own claim (E-0194, E-0165) | [DRHP_INTEG p.234; DRHP_SMT p.211] |

- **Price pressure.**
  - Emerging makers such as SMT, Meril and Lepu price 20–30% below incumbents (E-0195). EU price cuts help them win share [DRHP_SMT pp.210-211].
  - NPPA caps and China's VBP limit pricing power [DRHP_SMT pp.178, 209].
- **Polymed's cardiology footprint** as the two F&S reports see it: PTCA balloons only [DRHP_SMT p.210], or PTCA balloons, diagnostic catheters and other vascular accessories [DRHP_INTEG pp.251-252].
- **Low procedure rates leave headroom.** India does fewer than 500 PCIs per million people, against more than 3,000 in the US, Germany, France and Italy. This drives demand for guiding catheters and sheaths (E-0398) [DRHP_SMT p.189].

---

## A4.9 Orthopaedics (Citieffe trauma; Italy, Mexico, US)

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Global orthopaedic implants | USD 52.9 bn | CY24 | DRHP_GSURG p.189 · E-0080 | 2 |
| Global orthopaedic devices (broad definition) | USD 169.2 bn | CY24 | DRHP_GSURG p.206 · E-0098 | 2 |
| Global trauma fixation devices (Renub) [vendor estimate] | USD 13.21 bn | CY25 | VND_RNM_TRAUMA p.1 · E-0365 | 6 |
| India orthopaedic implants | USD 3.0 bn; CAGR given as 14.7% (p.190) and 7.6% (p.191) | FY25 | DRHP_GSURG p.190 · E-0082 | 2 |
| India orthopaedic devices | USD 6.2 bn | FY25 | DRHP_GSURG p.207 · E-0099 | 2 |
| India implants, all types (CRISIL) | Rs 85 bn | FY24 | PD24 p.137 · E-0329 | 2 |
| India orthopaedic procedures | 3.6 mn | FY25 | DRHP_GSURG p.183 · E-0079 | 2 |
| Italy device sector; public spending (WebFetch) | EUR 18.5 bn; EUR 10 bn | 2024/25 | CDM_NUMERI25 p.1 · E-0383, E-0384 | 3 |
| Italy payback settlement | 25% of invoiced amounts | Jun-2025 | BD_10K25 p.1 · E-0207 | 1 |

| company | HQ | relevant products | scale | notes |
|---|---|---|---|---|
| Stryker, Zimmer Biomet, Smith+Nephew, DePuy Synthes, Arthrex | US / UK | Premium implants | n.a. | Dominate India's premium segment [DRHP_GSURG p.195] |
| Meril, Sharma Orthopaedic, Narang Medical, Biorad Medisys, Bonetech | India | Implants | Biorad FY24 Rs 3,386.4 mn (E-0108) | [DRHP_GSURG p.195] |
| Weigao (orthopaedics) | China | Orthopaedic implants | RMB 1,522,663 thousand CY25 (E-0271) [WEIGAO_AR25 p.17] | Orthopaedic prices fell under VBP (E-0276 note) [WEIGAO_IR26 p.21] |
| B. Braun (Aesculap) | Germany | Orthopaedics, spine, surgery | EUR 2,374.3 mn (E-0245) | |

- **India price caps.** India capped knee-implant prices in 2017 [PD24 pp.151-152].
- **No trauma figures for Citieffe's markets.** Trauma-specific market sizes for Italy, Mexico and the US were not found (see gaps).

---

## A4.10 Components and OEM

| metric | value | year | source doc | tier |
|---|---|---|---|---|
| Teleflex OEM business sold to Montagu and Kohlberg | USD 1.5 bn | Dec-2025 (signed) | TFX_10K25 p.1 · E-0223 | 1 |
| KDL needle output (heavy captive use) | 1,412,059.48 万支 | CY25 | KDL_AR25 p.26 · E-0284 | 1 |
| HMD injection needles (self-reported) | >3 bn a year | 2026 (website) | HMD_WEB p.1 · E-0407 | 1 |

- **Teleflex's OEM unit** makes extrusions, catheters, balloons and sheath/dilator introducers for other device makers. It is being sold as a stand-alone business [TFX_10K25 p.1].
- **KDL** sells as OEM, ODM and own brand, and has long supplied global device majors [KDL_AR25 pp.19, 23].
- **Indian contract makers.**
  - Angiplast and Lars sell as contract OEM suppliers. Angiplast also makes components (spikes, injection sites, connectors, clamps) [ANGIPLAST_WEB p.1; LARS_WEB p.1].
  - Iscon sells to OEMs as well as to government and export buyers [BWR_ISCON p.2].
- **Risk of Chinese private-label supply.** Jiangsu Caina made Cardinal Health's Monoject syringes, which led to Class I recalls, an FDA warning letter and detention without physical examination (E-0279) [FDA_WL_CAINA p.1].
- **OEMs are looking for cheaper sources.** Since Covid, OEMs have sought cost-competitive alternatives, which favours Indian suppliers [PD24 p.141].

---

## A8 Moat comparisons

| company | metric | value | period | source doc | tier |
|---|---|---|---|---|---|
| Poly Medicure (F&S) | gross margin | 66.78% | FY25 | DRHP_INTEG p.260 · E-0167 | 2 |
| Poly Medicure (F&S; includes forex gain) | EBITDA margin | 28.72% | FY25 | DRHP_INTEG p.260 · E-0168 | 2 |
| Poly Medicure (1Lattice) | EBITDA margin | 27.12% | FY25 | DRHP_GSURG p.219 · E-0107 | 2 |
| Poly Medicure (CRISIL) | OPBDIT margin | 26.0% (table) vs 25.8% (text) | FY23 | PD24 pp.165-166 · D-0524, D-0525 | 2 |
| Poly Medicure (CRISIL) | export share | 69.0% | FY23 | PD24 p.166 · D-0506 | 2 |
| Poly Medicure (F&S) | working-capital days | 120 | FY25 | DRHP_INTEG p.260 · E-0169 | 2 |
| Poly Medicure (CRISIL) | share of India consumables | 1.9% | FY23 | PD24 p.166 · E-0352 | 2 |
| Integris Medtech | gross margin | 43.95% | FY25 | DRHP_INTEG p.260 · E-0170 | 2 |
| Romsons | EBITDA margin | 26.76% | FY24 | DRHP_GSURG p.219 · E-0102 | 2 |
| Meril Life | EBITDA margin | 25.92% | FY24 | DRHP_GSURG p.219 · E-0105 | 2 |
| Healthium | OPBDIT margin | 29.1% (CRISIL, FY23); 12.5% reported, 26.7% before ESOP cost (FY25) | FY23 / FY25 | D-0529; ICRA_HEAL pp.1, 4 · E-0305 | 2 / 4 |
| HMD | OPBDIT margin; exports | 13.0%; 20.8% | FY23 | PD24 pp.165-166 · E-0347, E-0349 | 2 |
| BD India | OPBDIT margin; exports | 9.8%; 15.9% | FY23 | PD24 pp.165-166 · E-0348, E-0350 | 2 |
| B. Braun India | OPBDIT margin; exports | 9.2%; 23.1% | FY23 | PD24 pp.165-166 · E-0354, E-0351 | 2 |
| SMT | OPBDIT margin | 14.4% | FY23 | PD24 p.165 · D-0530 | 2 |
| B. Braun Group | gross margin; EBITDA margin | 40.5%; 13.0% | CY25 | BBRAUN_AR25 pp.42, 45 · E-0248, E-0249 | 1 |
| ICU Medical | gross margin | 36.8% | CY25 | ICUI_10K25 p.1 · E-0213 | 1 |
| BD Medical segment | operating margin | 36.1% | FY25 | BD_10K25 p.1 · E-0201 | 1 |
| Weigao | gross margin | 46.3% | 1H2026 | WEIGAO_IR26 p.21 · E-0276 | 1 |
| FMC Care Enablement | operating margin | 6.0% | CY25 | FMC_20F25 p.1 · E-0237 | 1 |
| Hourly manufacturing wage: India vs China | < USD 2 vs USD 5–6 | 2024 | DRHP_SMT p.185 · E-0184, E-0185 | 2 |
| India manufacturing and R&D cost vs US/EU | ~30% lower | 2025 | DRHP_SMT p.185 · E-0186 | 2 |

- **The margin figures are not like-for-like.**
  - F&S adds forex gains back into EBITDA [DRHP_INTEG p.260]. CRISIL restates and reclassifies reported numbers [PD24 p.162].
  - The global figures are gross or segment margins, not EBITDA. Compare them only in direction.
- **Qualitative moat points.**
  - F&S describes MedTech as having low competitive intensity (few listed players), high entry barriers and low risk of genericisation [DRHP_SMT p.185].
  - EU MDR raises entry barriers [DRHP_HEAL p.125].
  - F&S names Polymed among the Indian companies investing in R&D and quality to match global standards [DRHP_INTEG p.215].
  - Polymed holds a 510(k) clearance for its safety IV catheters [PD24 p.166].
  - Rivals also claim integration: HMD says it depends on no other country for raw materials [HMD_WEB p.1], and KDL makes its own needle tubing [KDL_AR25 p.19].

---

## C Industry risks

1. **Chinese supply redirected into Polymed's markets.** US tariffs and FDA action push Chinese exporters towards Europe, Latin America, the Middle East and ASEAN (E-0290 to E-0294) [KDL_AR25 pp.18-19]. VBP winners are building export capacity [SANXIN_AR25 p.34] and localising abroad (Weigao's Indonesia JV) [WEIGAO_IR26 p.34].
2. **Tender-based pricing and price controls are spreading.** These include:
   - China's VBP (E-0285);
   - India's NPPA caps (E-0171 to E-0173, E-0340);
   - fixed PM-JAY and PMNDP dialysis rates (E-0051, E-0052);
   - Italy's payback (E-0206, E-0207);
   - buying concentrated in US GPOs (E-0379).
   All of these limit price increases [DRHP_SMT p.209; DRHP_INTEG p.251; BD_10K25 p.1].
3. **US trade policy.**
   - The Section 232 investigation into medical consumables [BD_10K25 p.1; ICUI_10K25 p.1].
   - Reciprocal tariffs: Costa Rica 15% (E-0214), EU medtech 15% (E-0250).
   - Tariff costs at peers: ICU Medical USD 33.6 mn (E-0217), B. Braun EUR 39.2 mn including currency (E-0246), Terumo -JPY 12.1 bn (E-0254).
   - Tariff risk is two-sided for Indian exporters: a cost, but also an opening against Chinese rivals.
4. **Protectionist procurement.** Procurement practices in China and India favour local makers, China restricts EU firms from public tenders, and Brazil has tightened localisation rules [BBRAUN_AR25 pp.41-42].
5. **Sterilisation.** Tighter EtO rules (EPA NESHAP, exposure limits) could cut contract-steriliser capacity, and there is litigation against sterilisers [BD_10K25 p.1; TFX_10K25 p.1]. About 50% of US sterile devices depend on EtO (E-0381).
6. **Resin costs.** Oil-based resin prices are volatile, and some producers rely on a single resin supplier [BD_10K25 p.1; ICUI_10K25 p.1; TFX_10K25 p.1].
7. **Regulatory scrutiny of quality.**
   - FDA warning letters, import alerts and detention without physical examination hit the Chinese syringe suppliers (E-0277, E-0279).
   - EU MDR complexity and the DEHP transition (E-0382) raise compliance costs [DRHP_INTEG p.226].
8. **Rivals adding capacity.**
   - Nipro in Japan, Thailand and Vietnam [NIPRO_FY25 p.7], and in India at Satara [PIB_PLI_MAR24 p.1].
   - HMD claims more than 4.5 bn units of capacity (E-0299).
   - Baxter notes that "global and regional competitors continue to expand their manufacturing capacity" [BAX_10K25 p.1].
9. **Well-funded domestic rivals.** Temasek backs Romsons, KKR owns Healthium and ADIA and Warburg Pincus back Meril (E-0146, E-0147, E-0295, E-0402).
10. **Unpredictable Indian tenders.** Government and institutional tenders are cancelled or re-bid, and distributors hold product registrations [DRHP_GSURG pp.177, 204, 212-213].
11. **Supply disruptions.** Examples are the IV-fluid shortage after Hurricane Helene [ICUI_10K25 p.1] and the inventory B. Braun is holding for supply security [BBRAUN_AR25 p.43].
12. **Consolidation among customers and competitors.** Examples are Teleflex's divestitures and acquisitions, Vantive's sale to Carlyle and BD's purchase of Edwards Critical Care (E-0208, E-0221 to E-0223, E-0377).

---

## Conflicts register

| topic | value A | value B (and others) | comment |
|---|---|---|---|
| India device market size | CRISIL Rs 900–915 bn FY24 (E-0321) | 1Lattice USD 30.0 bn FY25 (E-0066); F&S USD 16.4 bn 2023 incl. exports (E-0176); F&S India MedTech USD 27.7 bn 2029F (E-0142); Government USD 11 bn (E-0388); F&S-2021 USD 7.3 bn 2020 (E-0115) | Definitions differ (exports, equipment, IVD) |
| India device growth | CRISIL 11–12% FY24–28 (E-0324) | 1Lattice 14.3% FY25–30 (E-0068); F&S 8.0% 2024–29 (E-0143) | |
| Import dependence | CRISIL ~80% (E-0322) vs 70–75% in the same document (E-0331) | 1Lattice 70–80% (E-0073) vs 40.8% of consumption on the same page (E-0075); Government 90% in 2020 (E-0389) | |
| Global device market | 1Lattice USD 732.0 bn CY24 (E-0060) | F&S USD 518.0 bn 2024 (E-0135); CRISIL USD 545 bn CY23 (E-0341); B. Braun ~USD 600 bn (E-0247); F&S-2021 USD 394.4 bn 2020 (E-0114) | |
| PD share of dialysis patients | F&S <5% (E-0015) | FMC 11% (E-0228) | |
| India dialysis clinics in 2010 | 700 (E-0009, p.264) | ~1,000 (E-0034, p.277) | Same document |
| Organised dialysis share | 16.0% of volumes 2019 (E-0005); 13.4% of revenue 2019 (E-0049) | ~20% in 2024 (E-0056) | Different bases |
| Catheters & cannulae share of global surgical disposables | 32.2% (E-0084, p.198) | 36.0% (E-0085, p.199) | Same document |
| Syringes' share of global surgical disposables | 14.6% (p.198, in the E-0088 note) | 15.9% (E-0088, p.199) | Same document |
| India orthopaedic implant CAGR | 14.7% (p.190) | 7.6% (p.191) | Same document (E-0082 note) |
| Global coronary stents 2024 | USD 5.7 bn (E-0158) | USD 4,559.4 mn (E-0190) | Two F&S reports |
| Global PTCA balloons 2024 | USD 2.9 bn (E-0161) | USD 1,250.5 mn (E-0189) | Two F&S reports |
| India interventional cardiology 2024 | USD 480.0 mn (E-0162) | USD 355.5 mn, vascular interventional (E-0187) | Scopes differ |
| India cardiac procedure volume | 0.4 mn cardiovascular procedures FY25 (E-0078) | 0.81 mn PCI 2024 (E-0396) | |
| Global PIVC market; safety share | USD 5.74 bn CY25 / USD 5.1 bn CY26 / USD 7.5 bn CY26 (E-0356, E-0357, E-0360) | Safety 62% (E-0358) vs 30.3% (E-0361) | All vendor estimates |
| Polymed EBITDA margin FY25 | F&S 28.72% (E-0168) | 1Lattice 27.12% (E-0107) | F&S includes forex gain |
| Polymed OPBDIT margin FY23 (CRISIL) | 26.0% in the table (D-0524) | 25.8% in the text (D-0525) | Same document |
| Romsons country reach | 65+ countries [DRHP_GSURG p.211] | >80 countries (E-0297) | |
| HMD dealers | >4,500 (E-0405) | 10,000+ (E-0406) | Same web page |
| China device exports 2025 | USD 504.69 (100 mn), CCCMHPIE (E-0286) | RMB 596.84 (100 mn), customs via Sanxin (E-0394) | Different scope and currency |
| India surgical procedures | 165.7 mn FY25 (E-0077) | 15.33 mn 2020 (E-0112) | Definitions differ |
| India surgical disposables FY25 in INR | INR 329.8 bn (p.177) | INR 327.4 bn (p.200) | Same document (E-0070, E-0091 notes) |
| India device imports FY20 | NITI Aayog USD 1,766 mn (E-0118) | 1Lattice USD 6.2 bn (E-0074 note) | Scopes differ |

---

## Gaps

Details are in `ledger/gaps_E.jsonl`. The main gaps:

- Safety PIVC penetration by region.
- An Indian IV-cannula market size.
- Market sizes for bloodlines and AVF needles.
- The value of the Indian dialysis-machine market.
- A current Indian blood-bag market size.
- Market sizes in India for blood-collection tubes, urology, drains and enteral feeding.
- An aggregate anaesthesia and respiratory market.
- Trauma markets in Italy, Mexico and the US.
- A guiding-catheter-only market size.
- FY25/FY26 financials for private Indian competitors.
- Eastern Medikit, Vygon India, Mitra and Sterimed (sites unreachable).
- Jiangxi Hongda and Lingyang (not found).
- The current list of firms under FDA Import Alert 89-04 (FDA site returned 401).
