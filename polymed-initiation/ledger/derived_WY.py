# Derived calculations for the business-line exhibits added to A4.1-A4.10 (charts_A4_lines.md).
# Every row is "our calculation" and is labelled so in the text. IDs keep the D-WA / D-WB / D-WC numbering the
# exhibit spec assigned; formulas reference base facts only (reconcile.py resolves IDs shaped like A-0001).
DERIVED = []


def d(prefix, i, formula, unit, dec, metric, period, note, entity="", segment="", section="A4.1"):
    DERIVED.append({"id": f"D-{prefix}-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "segment": segment, "period": period, "note": "our calculation: " + note,
                    "section": section})


# --- A4.1: US imports of HS 901839 by supplier, CY2025 (UN Comtrade values are raw US dollars) ---
d("WA", 31, "F-0178/1000000", "USD mn", 1, "us_imports_usd_mn", "CY2025", "US imports of HS 901839 from China, converted to US$ mn", "US imports HS 901839 from China", "infusion")
d("WA", 32, "F-0181/1000000", "USD mn", 1, "us_imports_usd_mn", "CY2025", "US imports of HS 901839 from Malaysia, converted to US$ mn", "US imports HS 901839 from Malaysia", "infusion")
d("WA", 33, "F-0180/1000000", "USD mn", 1, "us_imports_usd_mn", "CY2025", "US imports of HS 901839 from India, converted to US$ mn", "US imports HS 901839 from India", "infusion")
d("WA", 34, "(F-0180/F-0179-1)*100", "%", 1, "us_imports_growth", "CY2025", "US imports of HS 901839 from India, 2025 over 2024", "US imports HS 901839 from India", "infusion")

# --- Rebates and discounts as a share of standalone revenue (the exhibit sits in B1 as b1_rebates) ---
d("WA", 35, "A-0824/A-0733*100", "%", 1, "rebates_share_of_revenue", "FY24", "standalone rebates and discounts / standalone revenue from operations", "Polymed standalone", "total")
d("WA", 36, "A-0480/A-0351*100", "%", 1, "rebates_share_of_revenue", "FY25", "standalone rebates and discounts / standalone revenue from operations", "Polymed standalone", "total")
d("WA", 37, "A-0479/A-0350*100", "%", 1, "rebates_share_of_revenue", "FY26", "standalone rebates and discounts / standalone revenue from operations", "Polymed standalone", "total")
d("WA", 38, "A-0479/A-0824", "x", 1, "rebates_multiple", "FY24-FY26", "FY26 standalone rebates and discounts over FY24", "Polymed standalone", "total")

# --- A4.1: peers' infusion revenue in rupees at RBI reference rates of 13-Dec-2025 (order of magnitude only) ---
d("WA", 39, "E-0242*WD-0024", "Rs mn", 0, "revenue_in_rupees", "CY25", "B. Braun Hospital Care sales (EUR mn) x RBI reference rate Rs/EUR, 13-Dec-2025", "B. Braun Hospital Care", "infusion")
d("WA", 40, "E-0198*WD-0023", "Rs mn", 0, "revenue_in_rupees", "FY Sep-2025", "BD Medication Delivery Solutions revenue (US$ mn) x RBI reference rate Rs/USD, 13-Dec-2025", "BD Medication Delivery Solutions", "infusion")
d("WA", 41, "E-0209*WD-0023", "Rs mn", 0, "revenue_in_rupees", "CY25", "ICU Medical consumables revenue (US$ mn) x RBI reference rate Rs/USD, 13-Dec-2025", "ICU Medical consumables", "infusion")

# --- A4.1: China and India exports of HS 901839 (UN Comtrade, each country as reporter) ---
d("WA", 42, "F-0165/1000000", "USD mn", 1, "exports_usd_mn", "CY2024", "China's exports of HS 901839, converted to US$ mn", "China HS 901839 exports", "infusion")
d("WA", 43, "F-0166/1000000", "USD mn", 1, "exports_usd_mn", "CY2025", "China's exports of HS 901839, converted to US$ mn", "China HS 901839 exports", "infusion")
d("WA", 44, "F-0133/1000000", "USD mn", 1, "exports_usd_mn", "CY2024", "India's exports of HS 901839, converted to US$ mn", "India HS 901839 exports", "infusion")
d("WA", 45, "(F-0166/F-0165-1)*100", "%", 1, "exports_growth", "CY2025", "China's exports of HS 901839, 2025 over 2024", "China HS 901839 exports", "infusion")
d("WA", 46, "(F-0134/F-0133-1)*100", "%", 1, "exports_growth", "CY2025", "India's exports of HS 901839, 2025 over 2024", "India HS 901839 exports", "infusion")
d("WA", 47, "F-0166/F-0134", "x", 1, "exports_multiple", "CY2025", "China's exports of HS 901839 over India's", "China vs India HS 901839 exports", "infusion")

# --- A4.2: Plan1Health EBITDA from the company slide's revenue and printed margin (EUR thousand) ---
d("WA", 48, "CB-0099*CB-0100/100", "EUR thousand", 0, "ebitda_implied", "CY20", "revenue x printed EBITDA margin, 1QFY27 deck slide", "Plan1Health", "vascular_access", "A4.2")
d("WA", 49, "CB-0101*CB-0102/100", "EUR thousand", 0, "ebitda_implied", "CY22", "revenue x printed EBITDA margin, 1QFY27 deck slide", "Plan1Health", "vascular_access", "A4.2")
d("WA", 50, "CB-0103*CB-0104/100", "EUR thousand", 0, "ebitda_implied", "CY24", "revenue x printed EBITDA margin, 1QFY27 deck slide", "Plan1Health", "vascular_access", "A4.2")
d("WA", 51, "CB-0105*CB-0106/100", "EUR thousand", 0, "ebitda_implied", "CY25", "revenue x printed EBITDA margin, 1QFY27 deck slide", "Plan1Health", "vascular_access", "A4.2")

# --- A4.6: anaesthesia and respiratory growth against the company ---
d("WA", 52, "((D-0585/D-0581)**(1/2)-1)*100", "%", 1, "revenue_cagr", "FY18-FY20", "anaesthesia and respiratory revenue CAGR, Feb-2021 placement-document product table", "Polymed consolidated", "anaesthesia_respiratory", "A4.6")
d("WA", 53, "A-0899/100*A-0351/D-0585", "x", 1, "revenue_multiple", "FY20-FY25", "FY25 BRSR share x standalone revenue over FY20 placement-document revenue (mixed bases)", "Polymed", "anaesthesia_respiratory", "A4.6")

# --- A4.10: own-brand shares implied by management's white-label shares (Feb-2023) ---
d("WA", 54, "100-CC-0436", "%", 0, "own_brand_share_implied", "Feb-2023", "100 minus the white-label share of exports management gave", "Polymed exports", "components_oem", "A4.10")
d("WA", 55, "100-CC-0437", "%", 0, "own_brand_share_implied", "Feb-2023", "100 minus the white-label share of India sales management gave", "Polymed India", "components_oem", "A4.10")

# --- A4.3: PLI Category A threshold less our proxy for incremental renal sales (Rs mn) ---
d("WB", 63, "WB-0020-(D-0057-D-0625)", "Rs mn", 0, "pli_threshold_shortfall", "FY23", "PLI incremental-sales threshold less (FY23 dialysis revenue less FY20)", "Polymed", "renal", "A4.3")
d("WB", 64, "WB-0021-(D-0055-D-0625)", "Rs mn", 0, "pli_threshold_shortfall", "FY24", "PLI incremental-sales threshold less (FY24 dialysis revenue less FY20)", "Polymed", "renal", "A4.3")
d("WB", 65, "WB-0022-(CB-0871-D-0625)", "Rs mn", 0, "pli_threshold_shortfall", "FY25", "PLI incremental-sales threshold less (FY25 renal revenue less FY20)", "Polymed", "renal", "A4.3")
d("WB", 66, "WB-0023-(CB-0870-D-0625)", "Rs mn", 0, "pli_threshold_shortfall", "FY26", "PLI incremental-sales threshold less (FY26 renal revenue less FY20)", "Polymed", "renal", "A4.3")

# --- A4.8: PACIFIER patients still to enrol, price and cath-lab ratios ---
d("WC", 93, "CB-1970-CB-1203", "count", 0, "registry_patients_remaining", "Feb-2026", "registry target less patients enrolled (printed with a '+')", "Polymed consolidated", "cardiology", "A4.8")
d("WC", 94, "CB-1970-CB-0598", "count", 0, "registry_patients_remaining", "May-2026", "registry target less patients enrolled (printed with a '+')", "Polymed consolidated", "cardiology", "A4.8")
d("WC", 95, "WC-0039/E-0171", "x", 1, "price_multiple", "Feb-2026", "DEB/IVL ASP floor (MD) over the NPPA DES ceiling price", "Polymed DEB and IVL", "cardiology", "A4.8")
d("WC", 96, "E-0152/WC-0030", "x", 1, "cath_labs_multiple", "2015-2023", "cath labs in 2023 over 2015 (Frost & Sullivan)", "India cath labs", "cardiology", "A4.8")
d("WC", 97, "E-0152/E-0153*100", "%", 0, "cath_labs_share_of_need", "2023", "cath labs in 2023 as a share of the number Frost & Sullivan says India needs", "India cath labs", "cardiology", "A4.8")
