# Vitamin D3: government trade statistics as a public, non-broker market-size proxy

Prepared 21 Oct 2026 for the Symbiotec Pharmalab work. All data below was pulled live from official databases on 21 Oct 2026 unless a line says otherwise. Raw downloads are in `/tmp/claude-0/-home-user-sample/da2696f9-0447-5145-866a-ae62d71abce7/scratchpad/tradedl/` (india_eidb/, brazil/, comtrade/, eu/, us/, japan/).

Unit conventions:
- "kg" and "t" are **product weight** as declared to customs, not pure D3.
- Pure cholecalciferol is 40 MIU/g. So feed-grade 500,000 IU/g (500 KIU/g) powder is **1.25% pure D3**, 1 MIU/g oil is 2.5%, and 100,000 IU/g CWS is 0.25%.
- The industry demand benchmark of ~7,000–10,800 t/yr of 500 KIU/g powder therefore equals ~87.5–135 t of pure D3 (7,000 × 1.25% = 87.5 t; 10,800 × 1.25% = 135 t).

---

## 1. Bottom line

1. **China's official customs statistics cannot isolate D3.**
   - China's current tariff has no D3 line: unmixed D3 falls in **29362900** (10-digit 2936290000, "其他未混合的维生素及其衍生物"), a basket of all "other" vitamins.
   - A 10-digit sub-code **2936290010 "胆钙化醇" (cholecalciferol)** existed but is listed as expired. It and its sibling 2936290090 both show a last update of 3 Jan 2022, which suggests (inference) that the split was dropped with the 2022 tariff.
   - GACC's public statistics are released at 8 digits only, so no D3 series exists there in any year.
   - China's **29369010 "维生素AD3"** covers vitamin A+D3 mixtures, not straight D3.
   - Mirror data from importing countries is the only official route.
2. **Dedicated vitamin D lines exist in a few importing countries:**
   - US: **HTS 2936.29.5020** "Vitamins D and their derivatives".
   - India: **ITC-HS 29362940** "Vitamin D".
   - Brazil/Mercosur: **NCM 2936.29.21** "Vitamina D3 (colecalciferol)", plus 2936.29.29 for other vitamin D.
   - EU (CN 2936 29 00) and Japan (2936.29-000) have **no** D split.
3. **Best citable figures pulled (official, reproducible):**
   - **Brazil, NCM 29362921 imports (SECEX/MDIC Comex Stat).**
     - CY2025: **USD 14,755,015 FOB / 343,852 kg**. China supplied **148,904 kg / USD 4,293,217** (43% of volume, 29% of value).
     - Jan–Sep 2026: **USD 11,742,568 / 206,236 kg** (volume −17% YoY vs 249,748 kg in Jan–Sep 2025). China supplied **90,246 kg / USD 2,161,814**.
   - **India, ITC-HS 29362940 imports (DGCI&S via MoC&I tradestat).**
     - CY2025: **USD 16.67 mn / 212,562 kg**. China supplied **USD 2.81 mn / 43,865 kg** (21% of volume, 17% of value). Switzerland (dsm-firmenich) supplied **107,490 kg / USD 3.69 mn**.
     - FY2025-26: **USD 14.40 mn / 174,319 kg**.
     - FY2026-27 YTD (Apr–Jul 2026): **USD 3.55 mn / 13,032 kg**.
   - **India, ITC-HS 29362940 exports** (likely mostly Fermenta Biotech, India's main D3 producer; this is an inference, not stated in the data). FY2025-26: **USD 27.75 mn / 200,524 kg**. India is a net exporter on this line.
   - **China exports of the HS 293629 basket (GACC via UN Comtrade).** 2025: **USD 574.3 mn / 45,344 t**. Basket only; D3 is a minority of it (see §4.3).
4. **What these lines capture.**
   - Converted to pure D3, Brazil plus India straight-D3 imports come to only **~7.0–7.5 t pure D3 in 2025** (≈5–9% of the 87.5–135 t global benchmark).
   - They measure straight-D3 imports only. Brazil has no known D3 producer; India has domestic supply (Fermenta).
   - These lines **cannot be summed into a global market**. The US line could not be pulled from this environment (key/login needed). The EU and China lines are baskets. Much D3 crosses borders inside premixes (HS 2309.90) and AD3 mixtures (HS 2936.90).
5. **Best uses for the note:**
   - Unit-value and price tracking.
   - China's share in named markets: well below its ~83% capacity share in both Brazil and India, where dsm-firmenich via Switzerland/Germany/US is large.
   - A Brazil-scaled sanity check on the global demand estimate (§5).

---

## 2. Tariff lines that cover vitamin D3

| Jurisdiction | Code | Official description | Unit | D3-specific? | Source / authority |
|---|---|---|---|---|---|
| WCO HS (6-digit) | 2936.29 | Other vitamins and their derivatives (unmixed) | – | No (basket) | HS nomenclature |
| WCO HS | 2936.90 | Other, including natural concentrates (mixtures, e.g. AD3) | – | No | HS nomenclature |
| **China** (2026 tariff) | 29362900 / 2936290000 | 其他未混合的维生素及其衍生物 (不论是否溶于溶剂) | kg | **No**. The code status is "正常" (valid); last updated 2026-08-23 | GACC tariff, relayed by hsbianma.com code database: https://www.hsbianma.com/Code/2936290000.html |
| China (historic) | **2936290010** | **胆钙化醇** (cholecalciferol) (不论是否溶于溶剂). Regulatory conditions A, S (S = 进出口农药登记证明, because cholecalciferol is also a rodenticide) | kg | Yes, but **expired** (page last updated 2022-01-03). Not published in GACC statistics, which are 8-digit | https://www.hsbianma.com/Code/2936290010.html (third-party code database relaying GACC codes; confirm on GACC 商品编码 query) |
| China (historic) | 2936290090 | 其他未混合的维生素及其衍生物 | kg | No; expired (last updated 2022-01-03) | https://www.hsbianma.com/Code/2936290090.html |
| China | **29369010 / 2936901000** | **维生素AD3** (包括天然浓缩物, 不论是否溶于溶剂) | kg | No: A+D3 mixtures | https://www.hsbianma.com/Code/2936901000.html |
| **India** ITC-HS | **29362940** | **VITAMIN D** | KGS | **Yes** (all vitamin D forms and derivatives, including analogue APIs) | DGCI&S HS master in tradestat: POST https://tradestat.commerce.gov.in/meidb/hscode with `hscode=2936`. Sibling lines: 29362910 folic acid, 29362920 nicotinic acid/nicotinamide, 29362930 vitamin K, 29362950 vitamin H (biotin), 29362990 other vitamins, 29369000 other incl. natural concentrates. Also 30045036 "Vitamin D in tablets, capsules, syrup" (finished dosage, Ch. 30) |
| **US** HTSUS | **2936.29.50.20** | **Vitamins D and their derivatives** (under 2936.29.50 "Other", general duty Free) | kg | **Yes** (D2, D3, analogues) | USITC HTS REST: https://hts.usitc.gov/reststop/search?keyword=2936.29. Siblings: 2936.29.10.00 folic acid; 2936.29.16.10/.20/.30 niacin and niacinamide; 2936.29.20.00 aromatic; 2936.29.50.30 biotin; 2936.29.50.50 other |
| **Brazil / Mercosur** NCM | **2936.29.21** | **Vitamin D3 (colecalciferol), unmixed** (Comex Stat English label) | kg | **Yes, D3 only** | SECEX/MDIC Comex Stat API response (`"ncm":"Vitamin d3 (colecalciferol), unmixed"`); NCM item 2936.29.2 "Vitaminas D e seus derivados"; sibling 2936.29.29 "Outros" (other vitamin D) — https://ncm.fazcomex.com.br/29362921-vitamina-d3-colecalciferol/ |
| **EU** CN8 | 2936 29 00 | "Vitamins and their derivatives, used primarily as vitamins, unmixed (excl. vitamins A, B1, B2, B3, B5, B6, B12, C, E and their derivatives)" (Eurostat label as returned) | kg (100 kg in Comext) | **No** (basket; TARIC 10-digit not in Comext) | Eurostat Comext DS-045409 dimension labels |
| EU CN8 | 2936 90 00 | Provitamins and mixtures of vitamins … and natural concentrates | | No | same |
| Japan | 2936.29-000 | Other vitamins and their derivatives | KG | **No** | Japan Customs tariff 1 Jan 2026: https://www.customs.go.jp/english/tariff/2026_01_01/data/e_29.htm |

### Where does feed-grade D3 500 powder go: 2936.29 or 2309.90?

**Rule.** HS Chapter 29 Note 1(f) and the Explanatory Note to 29.36 keep a vitamin in 29.36 when stabilisers are added "for the purposes of preservation or transport". That covers anti-oxidants, anti-caking carbohydrates, gelatin/wax/fat coatings, and adsorption on silicic acid. The condition is that the quantity or processing does not exceed what preservation or transport needs, and does not render the product "particularly suitable for specific use rather than for general use". CBP HQ 965447 quotes the EN verbatim.

**US rulings show the boundary** (CBP CROSS, official; pulled via https://rulings.cbp.gov/api/ruling/{n}):
- **NY 890993 (13 Jan 1994):** Microvit D3 Prosol 500 and Prosol 1000 (Rhône-Poulenc, from France) were classified in **2936.29.5020**. The ruling describes them as water-dispersible powders "used exclusively in the manufacture of animal feed products", with "Vitamin D3 … protected by a water-dispersible, digestible coating (gelatin, carbohydrate) and an antioxidant (BHT), … blended with a water-soluble carrier (carbohydrate)".
- **HQ 965447 (23 Jul 2002):** BASF Lutavit D3 500 S was classified in **2309.90.2490** (2309.90.2890 once the TRQ was filled), not 2936.29.5020.
  - The lab analysis found 76% lactose, 10% sodium caseinate, 6% peanut oil, 2% ethoxyquin, 1.5% silica and 1.3% D3.
  - CBP's reasoning: the product was "processed far beyond that which is necessary for preservation or transportation" and "rendered for specific and not general use".
- **HQ 953829 (26 Jul 1993):** Microvit AD3 Supra 650/325 and 500/100 were classified in Chapter 29 (2936.90). HQ 965447 cites this ruling.
- **NY 870608 (1992):** bulk vitamin D3 from Japan was classified in 2936.29.5020.

**Practical reading:**
- Standard gelatin/sugar/starch-coated **D3 500 beadlets normally fall in 2936.29** (US 2936.29.5020, India 29362940, Brazil 2936.29.21).
- Unit values confirm this in the data. Brazil imports from China at USD 17–29/kg in 2023–25, and India imports from Switzerland at about USD 34/kg in CY2025 (107.5 t). Both are consistent with 500 KIU/g feed grade.
- **Carrier-heavy, application-specific forms** (milk-replacer grades) and **multi-ingredient premixes go to 2309.90**. **AD3 mixtures go to 2936.90** (China 29369010).
- So the national D lines measure "straight" D3 trade only and miss D3 shipped inside premixes and AD3.

---

## 3. Access status from this environment

| Database | Authority | Status on 21 Oct 2026 |
|---|---|---|
| tradestat.commerce.gov.in (EIDB annual and monthly) | Ministry of Commerce & Industry; data by DGCI&S | **Worked** (Laravel form POST with CSRF token) |
| Comex Stat API (api-comexstat.mdic.gov.br) | SECEX/MDIC, Brazil | **Worked** but heavily rate-limited (HTTP 429). The bulk CSV host balanca.economia.gov.br failed TLS because the server omits its Sectigo intermediate |
| UN Comtrade public preview API | UN Statistics Division, from national reporters | **Worked** (annual; HS6 only; monthly China preview returned no rows) |
| Eurostat Comext API (DS-045409) | Eurostat | **Worked** |
| US Census International Trade API | US Census Bureau | **Blocked: a key is now mandatory.** HTTP 302 to `https://api.census.gov/data/missing_key.html` with header `X-DataWebAPI-KeyError: 1` |
| USITC DataWeb | USITC | Site reachable; queries and API need a free Login.gov account and API token, so **not pulled** |
| stats.customs.gov.cn (海关统计数据在线查询平台) | GACC | **Blocked**: HTTP 412 with a JavaScript anti-bot challenge. In any case 8-digit only, so no D3 split |
| CBP CROSS rulings API | US CBP | Worked |

---

## 4. Data

### 4.1 India: ITC-HS 29362940 "VITAMIN D" (unit KGS). Authority: DGCI&S, published by MoC&I Export Import Data Bank

Retrieval (all on 21 Oct 2026):
- **Annual (financial year):** `POST https://tradestat.commerce.gov.in/eidb/commodity_wise_all_countries_import`. Form fields: `_token=<csrf from a GET of the same URL, same cookie jar>`, `Eidbhscode_cmaci=29362940`, `EidbYear_cmaci=2025` (returns FY2024-25 and FY2025-26; use 2019/2021/2023 for earlier years), `EidbReport_cmaci=2` (US$ mn). Each response also gives quantity in KGS by country.
- **Monthly / calendar year / YTD:** `POST https://tradestat.commerce.gov.in/meidb/commodity_wise_all_countries_import`. Form fields: `cwacimHSCODE=29362940`, `cwacimMonth=12`, `cwacimYear=2025`, `cwacimReportVal=1` (US$ mn) or `2` (Quantity), `cwacimReportYear=2` (calendar year) or `1` (FY). For exports use `/meidb/commodity_wise_all_countries_export` with `cwacex*` fields, or `/eidb/commodity_wise_all_countries_export` with `Eidbhscode_cmace` / `EidbYear_cmace` / `EidbReport_cmace`.
- Latest month with Final ("F") data: **July 2026**. August and September 2026 show "(A)" (alert) with zeros.

**India imports, 29362940, calendar year** (from the MEIDB Dec query with `cwacimReportYear=2`)

| CY | Total US$ mn | Total kg | From China US$ mn | From China kg | China share vol / val | Largest other sources (kg) |
|---|---|---|---|---|---|---|
| 2018 | 9.49 | 13,675 | 3.18 | 688 | 5% / 33% | Israel 5,261; Singapore 4,912 |
| 2019 | 12.22 | 21,787 | 4.83 | 4,914 | 23% / 40% | Israel 9,492; Singapore 5,661 |
| 2020 | 6.90 | 23,944 | 1.56 | 8,965 | 37% / 23% | Israel 5,490; Singapore 4,673; UK 4,234 |
| 2021 | 10.16 | 24,942 | 2.49 | 5,324 | 21% / 25% | Israel 9,480; Singapore 5,093; UK 4,622 |
| 2022 | 11.03 | 18,433 | 3.65 | 3,058 | 17% / 33% | Singapore 6,791; Israel 5,265 |
| 2023 | 8.28 | 52,754 | 2.00 | 9,176 | 17% / 24% | Singapore 19,116; France 13,513; Israel 7,815 |
| 2024 | 13.29 | 161,351 | 1.68 | 23,836 | 15% / 13% | Switzerland 96,746; France 19,740; Israel 9,555 |
| **2025** | **16.67** | **212,562** | **2.81** | **43,865** | **21% / 17%** | **Switzerland 107,490 (US$3.69 mn)**; France 23,299 (US$2.04 mn); UK 4,329 (US$3.36 mn); USA 4,110 (US$1.32 mn) |

**India imports, 29362940, financial year** (EIDB annual; matches MEIDB March FY totals)

| FY | Total US$ mn | Total kg | China US$ mn | China kg |
|---|---|---|---|---|
| 2018-19 | 12.73 | 14,857 | 5.13 | 1,071 |
| 2019-20 | 9.68 | 17,711 | 3.76 | 4,661 |
| 2020-21 | 6.87 | 31,032 | 1.26 | 9,027 |
| 2021-22 | 10.68 | 19,125 | 3.03 | 5,291 |
| 2022-23 | 10.88 | 23,991 | 3.16 | 4,598 |
| 2023-24 | 8.51 | 56,131 | 1.69 | 8,177 |
| 2024-25 | 14.67 | 199,773 | 1.66 | 33,655 |
| 2025-26 | 14.40 | 174,319 | 2.92 | 42,491 |
| **2026-27 YTD (Apr–Jul 2026, Final)** | **3.55** | **13,032** | **0.48** | **7,650** |
| Apr–Jul 2025 (comparator) | 5.04 | 51,796 | 1.40 | 17,659 |

FY2025-26 partners by value: UK 3.26 (4,366 kg), China 2.92 (42,491 kg), Switzerland 2.56 (72,855 kg), France 1.94 (21,669 kg), Netherlands 1.19 (4,755 kg), USA 0.85 (2,712 kg); all US$ mn. FY2024-25: Switzerland 5.01 (130,741 kg), UK 2.35, USA 1.88, China 1.66 (33,655 kg), Netherlands 1.29, France 1.12 (18,340 kg).

**Reading the India line:**
- It **includes vitamin D analogue APIs** (calcitriol/alfacalcidol/paricalcitol type). Tiny-kg, very-high-value rows show this: Taiwan CY2022 US$2.53 mn for 2 kg; Czech Republic US$0.71 mn for 55 kg; Japan US$0.47 mn for 25 kg. Value is therefore a poor D3 proxy. Use kg, and screen rows by unit value.
- The jump in volume from CY2024 is mostly Switzerland at about US$34–41/kg, i.e. feed-grade D3 500.
- Volumes are small because India has domestic supply (Fermenta), and because much feed D3 arrives inside premixes (2309.90), AD3 (29369000) and "other vitamins" (29362990).

**India exports, 29362940** (EIDB; Fermenta is the main Indian D3 producer, so this is a Fermenta-dominated proxy)

| FY | US$ mn | kg | Main destinations |
|---|---|---|---|
| 2018-19 | 13.56 | 28,048 | |
| 2019-20 | 11.16 | 28,173 | USA 6,945 kg (US$2.19 mn), Iran 4,047 kg |
| 2020-21 | 21.01 | 142,222 | |
| 2021-22 | 22.88 | 183,306 | USA 127,829 kg (US$6.54 mn) |
| 2022-23 | 15.03 | 69,681 | |
| 2023-24 | 12.41 | 86,956 | USA 38,113 kg |
| 2024-25 | 23.32 | 121,916 | |
| **2025-26** | **27.75** | **200,524** | USA 106,578 kg (US$5.10 mn, ~US$48/kg); Germany 38,345 kg (US$6.15 mn, ~US$160/kg); UAE 12,763 kg |
| 2026-27 YTD Apr–Jul | 7.41 | 46,509 | vs Apr–Jul 2025: US$10.52 mn / 64,295 kg |

Context lines (not vitamin-D specific), India imports, FY:
- **29362990 "Other vitamins and their derivatives":** FY2024-25 US$18.93 mn / 528,198 kg (China US$9.35 mn / 460,530 kg); FY2025-26 US$13.07 mn / 251,003 kg (China US$6.70 mn / 129,467 kg); Apr–Jul 2026 US$7.42 mn / 118,456 kg (China 106,057 kg).
- **29369000 "Other, incl. natural concentrates"** (includes AD3-type mixtures): FY2024-25 US$1.25 mn / 27,964 kg; FY2025-26 US$2.91 mn / 56,017 kg (China US$1.45 mn / 24,607 kg); Apr–Jul 2026 US$1.13 mn / 54,483 kg (China 43,150 kg).
- Some D3 may be mis-declared under 29362990. No public data can show how much.

### 4.2 Brazil: NCM 2936.29.21 "Vitamin D3 (colecalciferol), unmixed". Authority: SECEX / MDIC (Comex Stat)

Retrieval:
```
POST https://api-comexstat.mdic.gov.br/general?language=en
Content-Type: application/json
{"flow":"import","monthDetail":false,"period":{"from":"2019-01","to":"2025-12"},
 "filters":[{"filter":"ncm","values":["29362921"]}],"details":["country"],
 "metrics":["metricFOB","metricKG"]}
```
For 2026 YTD: same body with `"monthDetail":true,"period":{"from":"2026-01","to":"2026-12"}`. The latest month returned is **Sep 2026**. The API returns HTTP 429 often; retry after about 60 s. UI: https://comexstat.mdic.gov.br/ → Geral → Importação → filter NCM 29362921 → detail País.

| Year | FOB US$ | Net kg | UV US$/kg | China FOB US$ | China kg | China UV | Switzerland kg | USA kg (UV) | Germany kg |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 15,164,299 | 303,170 | 50.0 | 6,064,302 | 149,205 | 40.6 | 53,958 | 13,384 (192) | 2,280 |
| 2020 | 11,262,870 | 203,950 | 55.2 | 2,299,800 | 90,471 | 25.4 | 38,529 | 21,302 (192) | 19,155 |
| 2021 | 16,577,795 | 157,820 | 105.0 | 1,405,009 | 15,770 | 89.1 | 58,115 | 28,270 (222) | 34,464 |
| 2022 | 17,394,553 | 136,778 | 127.2 | 913,165 | 20,767 | 44.0 | 43,691 | 34,887 (219) | 29,240 |
| 2023 | 12,525,521 | 160,237 | 78.2 | 1,001,863 | 60,030 | 16.7 | 14,400 | 34,107 (220) | 33,320 |
| 2024 | 10,775,325 | 248,744 | 43.3 | 1,985,425 | 91,631 | 21.7 | 37,240 | 18,696 (117) | 59,610 |
| **2025** | **14,755,015** | **343,852** | **42.9** | **4,293,217** | **148,904** | **28.8** | 70,586 | 12,017 (199) | 34,040 |
| **2026 Jan–Sep** | **11,742,568** | **206,236** | **56.9** | **2,161,814** | **90,246** | **24.0** | 19,327 | 19,591 (286) | 23,220 |
| 2025 Jan–Sep (comparator) | 10,698,663 | 249,748 | 42.8 | – | – | – | – | – | – |

- CIF values are also available: 2025 CIF US$15,033,974; 2019 CIF US$15,451,735.
- Other 2025 suppliers: Denmark 27.1 t, Bulgaria 50.0 t (about US$10.9/kg), France 0.2 t (about US$2,396/kg, i.e. crystalline or high-potency), India 1.0 t.
- 2026 monthly import volumes, Jan–Sep (t): 32.0, 29.7, 27.3, 30.5, 13.3, 19.6, 12.3, 35.8, 5.8.
- **Jan–Sep 2026 vs Jan–Sep 2025: volume −17.4% (206,236 vs 249,748 kg); FOB value +9.8% (US$11.74 mn vs US$10.70 mn).** The 2025 comparator comes from the same API with `"monthDetail":true,"period":{"from":"2025-01","to":"2025-09"}`; 2025 monthly kg Jan–Sep: 34,604; 61,252; 17,722; 18,373; 20,054; 26,972; 31,164; 13,871; 25,736.
- Reading: this is the **cleanest public D3-only series**.
  - Chinese-origin unit values of US$17–29/kg in 2023–2026 fit feed-grade 500 KIU/g.
  - Swiss/US/German rows at US$50–290/kg are dsm-firmenich and other higher-potency or specialty grades.
  - China's share of Brazilian straight-D3 volume collapsed in 2021–22 (10–15%) and recovered to 43–44% in 2025–26.

### 4.3 China: GACC export statistics, available only for the basket (HS 293629 = China 29362900; HS 293690 = 29369010 AD3 + 29369090)

Retrieval (UN Comtrade public preview, no key): `GET https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=156&period=2025&cmdCode=293629&flowCode=X` returns all partners (add `&partnerCode=0` for world only). Authority: GACC, as reported to UNSD Comtrade. Some net weights carry Comtrade's "estimated" flag (for example 2023).

| Year | 293629 exports, world US$ | 293629 kg | UV US$/kg | 293690 exports US$ | 293690 kg |
|---|---|---|---|---|---|
| 2019 | 449,099,387 | 26,045,137 | 17.24 | 90,613,097 | 2,075,268 |
| 2020 | 588,873,785 | 32,593,414 | 18.07 | 92,954,470 | 2,217,828 |
| 2021 | 585,118,657 | 36,401,470 | 16.07 | 114,768,325 | 2,779,828 |
| 2022 | 534,163,619 | 36,756,974 | 14.53 | 72,054,393 | 1,940,590 |
| 2023 | 421,194,321 | 36,052,635 | 11.68 | 47,969,737 | 2,173,390 |
| 2024 | 559,290,299 | 47,607,336 | 11.75 | 57,709,436 | 2,991,805 |
| 2025 | 574,290,668 | 45,343,614 | 12.67 | 69,466,552 | 2,650,395 |

Largest 2025 destinations for 293629 (US$ / kg): USA 132,954,606 / 3,905,227; Netherlands 68,297,052 / 6,155,229; Brazil 28,717,990 / 2,804,311; Germany 27,538,586 / 1,763,505; Korea 22,897,856 / 3,116,225; Russia 16,766,675 / 1,825,929; Singapore 15,957,698 / 2,119,916; Mexico 14,654,533 / 1,740,732; India 14,337,792 / 507,230; Thailand 12,933,734 / 1,760,126. The 2019–2024 partner lists are in `comtrade/cn_x_293629_<year>.json`.

**How large is D3 inside China's basket? Mirror check (illustrative only)**
- India 2025: India's 29362940 imports from China (43.9 t, US$2.81 mn) are **~9% by volume and ~20% by value** of China's reported 293629 exports to India (507 t, US$14.34 mn).
- Brazil 2025: Brazil's 29362921 imports from China (148.9 t, US$4.29 mn) are **~5% by volume and ~15% by value** of China's 293629 exports to Brazil (2,804 t, US$28.72 mn).
- The Brazil volume ratio swings from 21% (2019) to 1.2% (2022) to 5.3% (2025). Applying any ratio to China's 45,344 t world total would be **unreliable**, so it is not done here.
- Besides D3, the basket includes niacin/niacinamide, biotin (including feed dilutions), folic acid, vitamin K and others. Its composition by vitamin is not published.

Official Chinese publications:
- GACC's monthly key-commodity tables and the Mysteel relay of customs vitamin data break out A, E, C, B1, B2, B5, B6 and B12 only. There is no D3 line. Total Chinese vitamin exports were 422,765 t in 2024 (Mysteel, Jan 2025: https://m.mysteel.com/a/25012014/7A8FCF99CE024563_abc.html; this source relays customs data).
- No China customs yearbook or CPIA figure for D3 export tonnage was found.
- Chinese D3 export volume figures that circulate online (for example "+25% YoY in Q1 2025", Gelonghui) come from brokers or consultancies and give no customs code. **Do not cite them as customs data.**
- CCM (cnchemicals.com, a consultancy) states that China's customs D3 code is "2936901000". That is the AD3 mixture line, so the claim is wrong for straight D3. CCM also states that in 2022 GACC raised a WTO specific trade concern over EU restrictions on Chinese D3. That WTO record was not verified.

### 4.4 EU: Eurostat Comext, CN 29362900 (basket) and 29369000. No D3 line

Retrieval: `GET https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-045409?format=JSON&lang=EN&freq=A&reporter=EU&partner=CN&partner=CH&partner=US&partner=IN&product=29362900&product=29369000&flow=1&indicators=VALUE_IN_EUROS&indicators=QUANTITY_IN_100KG&time=2019&…&time=2025`. Authority: Eurostat. Dataset updated 2026-10-16.

EU27 imports of CN 29362900 (EUR mn / t):

| Partner | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| China | 132.1 / 7,348 | 189.0 / 8,838 | 134.4 / 9,073 | 164.0 / 9,620 | **69.9 / 4,115** | 125.6 / 11,377 | 136.3 / 11,104 |
| Switzerland | 74.1 / 6,321 | 74.5 / 6,066 | 81.1 / 6,135 | 99.5 / 6,471 | 73.3 / 3,296 | 73.2 / 4,638 | 74.3 / 3,388 |
| India | 37.6 / 5,123 | 33.9 / 3,640 | 42.8 / 5,764 | 44.8 / 5,756 | 29.8 / 5,109 | 40.6 / 5,301 | 42.7 / 5,275 |
| USA | 28.3 / 373 | 27.7 / 405 | 20.0 / 275 | 20.5 / 273 | 25.4 / 292 | 26.0 / 295 | 31.4 / 303 |

EU27 imports of CN 29369000 from China (EUR mn / t): 2019 26.5 / 725; 2022 21.0 / 698; 2023 18.0 / 1,454; 2024 25.6 / 2,521; 2025 26.8 / 1,991.

Regulatory context for reading the 2023 dip in Chinese supply:
- Under Commission Decision 2002/994/EC, D3 (a lanolin-derived product of animal origin) for feed use from China was blocked from 2021–22.
- **Commission Implementing Decision (EU) 2023/1016 of 22 May 2023** (OJ L 136, 24.5.2023, pp. 75–77; in force 20 days after publication) restored access for "vitamin D3 and precursors used for its production" from China. Text: https://www.boe.es/doue/2023/136/L00075-00077.pdf
- The 2023 fall in 29362900 imports from China cannot be attributed to D3 alone, because the code is a basket.

### 4.5 US: HTS 2936.29.5020 "Vitamins D and their derivatives". **Not retrieved: the official database needed a key or login from here**

Exact steps for the user:
1. **USITC DataWeb** (https://dataweb.usitc.gov):
   - Sign in with a free Login.gov account and choose Query.
   - Trade Flow: *Imports for Consumption* (also run *General Imports*). Classification: *HTS Items*. Commodity: `2936295020` (10-digit).
   - Countries: *All*, with "break out countries" ticked.
   - Timeframe: Annual 2019–2025, plus Year-to-Date Jan through the latest month of 2026.
   - Data to report: *Customs Value* and *First Unit of Quantity* (kg). Optionally add *CIF Imports Value*. Run, then Download.
2. **Census API** (free key from https://api.census.gov/data/key_signup.html):
   - Annual query: `https://api.census.gov/data/timeseries/intltrade/imports/hs?get=CTY_CODE,CTY_NAME,GEN_VAL_YR,CON_VAL_YR,GEN_QY1_YR,CON_QY1_YR,UNIT_QY1&I_COMMODITY=2936295020&COMM_LVL=HS10&time=2025-12&key=YOUR_KEY`. The `_YR` fields are year-to-date, so `time=YYYY-12` gives the full year.
   - Repeat for 2019–2024, and use the latest 2026 month for YTD.
   - Without a key the API redirected to `missing_key.html` on 21 Oct 2026.
3. Expect the US line to include D2 (ergocalciferol), analogues and feed-grade D3 500 beadlets (per NY 890993). It excludes milk-carrier D3 premixes (2309.90, per HQ 965447) and AD3 (2936.90).
4. Context: China's reported 2025 exports to the US of the whole 293629 basket were US$132.95 mn / 3,905 t (Comtrade), so the D3 share is again a minority.

---

## 5. Converting to pure D3 and comparing with the demand estimates

Method:
- **Flat conversion:** every kg treated as 500 KIU/g, i.e. × 1.25%. This is a lower-bound style estimate when crystalline is present.
- **Tiered conversion,** using each partner row's unit value:
  - below US$100/kg → 500 KIU/g (× 1.25%);
  - US$100–1,000/kg → oil-type ~1 MIU/g (× 2.5%);
  - US$1,000–15,000/kg → crystalline cholecalciferol (× 100%; may include 25-OH-D3);
  - above US$15,000/kg → treated as analogue APIs and **excluded**.
- Thresholds are anchored on the existing price notes: China feed grade about RMB 50–130/kg (about US$7–18) in normal years and US$50–75/kg export quotes in the 2024–25 spike; pharma crystalline about RMB 18,000–19,000/kg (about US$2,500) at end-2019.

| Series | Product kg | Pure D3, flat | Pure D3, tiered | Share of 87.5–135 t global pure D3 |
|---|---|---|---|---|
| Brazil NCM 29362921 imports, CY2025 | 343,852 | 4.30 t | 4.61 t | 3.2–5.3% |
| Brazil, Jan–Sep 2026 | 206,236 | 2.58 t | 3.04 t | – |
| India 29362940 imports, CY2025 | 212,562 | 2.66 t | 2.89 t | 2.0–3.3% |
| India 29362940 imports, CY2024 | 161,351 | 2.02 t | 2.24 t | – |
| India 29362940 exports, FY2025-26 | 200,524 | 2.51 t | ~6.9 t (driven by rows at >US$1,000/kg, likely crystalline; the exporter is not identified in the data) | – |
| Brazil + India imports, 2025 | 556,414 | **~7.0 t** | **~7.5 t** | **~5–9%** |

**Brazil-scaled sanity check (assumption-heavy):**
- Brazil has no known D3 producer. Its straight-D3 imports of 344 t in 2025 (product weight, mostly 500 KIU/g-type by unit value) roughly equal its straight-D3 feed use, excluding D3 inside imported premixes and AD3.
- *Assumption, not re-verified here:* Brazil is about 6–7% of world compound feed output (on the order of 85–90 mn t of about 1.4 bn t in industry feed surveys).
- On that assumption, implied global feed D3 is about 344 / 0.065 ≈ **5,300 t of 500 KIU/g (≈66 t pure)**.
- This sits **below** the 7,000–10,800 t (87.5–135 t pure) industry range. That is consistent with the range once human, pharma and food uses (excluded here) and D3 inside premixes (also excluded) are added. It supports the **lower half** of the range rather than the 10,800 t theoretical figure.
- Treat this as a cross-check, not a market-size figure.

**Unit values as a price proxy** (official, but grade-mixed):
- Brazil's imports from China fell from US$89/kg (2021) to US$16.7/kg (2023), then rose to US$21.7 (2024), US$28.8 (2025) and US$24.0 (Jan–Sep 2026).
- India's imports from China were about US$70/kg (CY2024) and about US$64/kg (CY2025).
- The direction matches the 2023 trough, the 2024–25 spike and the 2026 easing described in `../Vitamin D3 supply landscape/pricing_and_dynamics.md`. The levels blend grades.

---

## 6. Official publications that state D3 trade volumes: search results

- **GACC / China customs yearbooks:** none found with D3 volumes. The publications are 8-digit, and the 29362900 basket hides D3.
- **CPIA (中国化学制药工业协会):** no customs-sourced D3 export figure was found publicly.
- **India DGCI&S / MoC&I:** the 29362940 data above is the official series. No DGCI&S publication discusses D3 separately.
- **Lok Sabha / Rajya Sabha:** no answer giving vitamin D import volumes was found. The nearest is a **Rajya Sabha answer of 14 May 1990**: import details for individual bulk drugs were "not monitored", except vitamin A, which was canalised through STC (https://rsdebate.nic.in/bitstream/123456789/256194/1/PQ_154_14051990_U723_p161_p163.pdf; summarised from the search result, PDF not opened).
- **DGTR:**
  - No vitamin D3 trade-remedy case. The historical anti-dumping duty on **Vitamin AD3 500/100 from China** dates from 2002.
  - The 2024–25 **vitamin A palmitate** case led to Notification 14/2025-Customs (ADD) of 6 Jun 2025. The final findings contain official vitamin A import data, not D3.
- **EU:** Implementing Decision (EU) 2023/1016 (above) is the official instrument on Chinese D3 market access. It gives no volumes.

---

## 7. Caveats

1. Product weight is not potency. Every tonnage above is declared product weight. Pure-D3 figures depend on the grade assumptions in §5.
2. The national D lines cover different things:
   - India 29362940 and US 2936.29.5020 include D2 and analogue APIs (value is distorted).
   - Brazil 2936.29.21 is D3 only; Brazil's 2936.29.29 covers other vitamin D.
   - None of them covers D3 inside premixes (2309.90) or AD3 (2936.90).
3. India EIDB partner quantity cells are sometimes blank while a value is shown (for example Taiwan). Totals here are the MEIDB "Total" rows, which sum the reported quantities.
4. The FY2026-27 India data is through July 2026 (Final). August and September 2026 are "Alert" with zeros and should not be read as actual zeros.
5. Comtrade China 293629 net weights are partly estimated (`isNetWgtEstimated`).
6. The Brazil NCM 2936.29.21 English label comes from the Comex Stat API. NCM text was not re-checked against the Receita Federal TEC.
7. China 10-digit code facts (2936290010 cholecalciferol, expired) rest on hsbianma.com, a third-party code database that relays GACC codes. Confirm on the GACC "互联网+海关" 商品编码 query if this is cited in print.

## 8. Not done / still open

- **US HTS 2936.29.5020** imports by country, 2019–2026 YTD: needs a DataWeb login or Census API key (steps in §4.5). This is the **single most valuable missing series**, given US feed size and dsm-firmenich/China supply.
- Brazil NCM 2936.29.29 (other vitamin D) and 2936.90.00 (AD3 and other mixtures), and Brazil exports of 2936.29.21: queued but blocked by HTTP 429 rate limits. Re-run with the JSON body above, changing `values` to `["29362929","29369000"]`.
- Other mirror markets with possible D lines were not checked: Argentina (same NCM 2936.29.21 via INDEC), Mexico (TIGIE/NICO), Korea (HSK 10-digit), Canada (HS10 statistical suffixes).
