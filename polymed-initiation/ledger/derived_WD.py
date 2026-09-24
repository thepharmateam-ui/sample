# Derived facts for writer WD (Part B – the industry). Every value is our calculation from cited ledger inputs.
DERIVED = []

# --- B1: MRP vs the price a hospital paid (Maharashtra FDA survey, Polymed IV set)
DERIVED.append({"id": "D-WD-001", "formula": "F-0084/F-0083", "unit": "x", "dec": 1, "metric": "mrp_to_procurement_ratio", "entity": "Polymed IV set (Maharashtra FDA survey)", "segment": "infusion", "geography": "India", "period": "Sep-2026", "note": "our calculation: printed MRP / trade procurement price", "section": "B1,B3"})

# --- B2: competitors' revenue as a multiple of Polymed's FY26 consolidated revenue (A-0039), converted at the
#     RBI reference rate of 13-Dec-2025 (WD-0023 USD, WD-0024 EUR). Periods differ; a scale indicator only.
_M = "our calculation: competitor revenue x RBI reference rate (13-Dec-2025) / Polymed FY26 consolidated revenue; periods differ"
DERIVED.append({"id": "D-WD-002", "formula": "E-0196*WD-0023/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "BD", "period": "FY25 vs FY26", "note": _M, "section": "B2"})
DERIVED.append({"id": "D-WD-003", "formula": "E-0198*WD-0023/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "BD Medication Delivery Solutions", "period": "FY25 vs FY26", "note": _M, "section": "B2"})
DERIVED.append({"id": "D-WD-004", "formula": "E-0241*WD-0024/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "B. Braun", "period": "CY25 vs FY26", "note": _M, "section": "B2"})
DERIVED.append({"id": "D-WD-005", "formula": "E-0209*WD-0023/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "ICU Medical Consumables", "period": "CY25 vs FY26", "note": _M, "section": "B2"})
DERIVED.append({"id": "D-WD-006", "formula": "E-0239*WD-0024/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "Fresenius Medical Care Care Enablement", "period": "CY25 vs FY26", "note": _M, "section": "B2"})
DERIVED.append({"id": "D-WD-007", "formula": "E-0220/1000*WD-0023/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "Teleflex (continuing)", "period": "CY25 vs FY26", "note": _M + "; Teleflex reported in USD thousand", "section": "B2"})
DERIVED.append({"id": "D-WD-008", "formula": "E-0378*WD-0023/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "Baxter Infusion Therapies & Technologies", "period": "CY25 vs FY26", "note": _M, "section": "B2"})
DERIVED.append({"id": "D-WD-009", "formula": "E-0376*WD-0023/A-0039", "unit": "x", "dec": 0, "metric": "revenue_multiple_of_polymed", "entity": "Vantive", "period": "CY24 vs FY26", "note": _M, "section": "B2"})

# --- B5: US syringe imports (HS 901831) from China and India, UN Comtrade values in US$ scaled to US$ mn (our calculation)
_S = "our calculation: UN Comtrade value in US$ divided by 1,000,000"
DERIVED.append({"id": "D-WD-010", "formula": "F-0171/1000000", "unit": "USD mn", "dec": 1, "metric": "us_imports", "entity": "US imports HS 901831 (syringes) from China", "period": "CY2023", "note": _S, "section": "B5"})
DERIVED.append({"id": "D-WD-011", "formula": "F-0172/1000000", "unit": "USD mn", "dec": 1, "metric": "us_imports", "entity": "US imports HS 901831 (syringes) from China", "period": "CY2024", "note": _S, "section": "B5"})
DERIVED.append({"id": "D-WD-012", "formula": "F-0173/1000000", "unit": "USD mn", "dec": 1, "metric": "us_imports", "entity": "US imports HS 901831 (syringes) from China", "period": "CY2025", "note": _S, "section": "B5"})
DERIVED.append({"id": "D-WD-013", "formula": "F-0174/1000000", "unit": "USD mn", "dec": 2, "metric": "us_imports", "entity": "US imports HS 901831 (syringes) from India", "period": "CY2023", "note": _S, "section": "B5"})
DERIVED.append({"id": "D-WD-014", "formula": "F-0175/1000000", "unit": "USD mn", "dec": 2, "metric": "us_imports", "entity": "US imports HS 901831 (syringes) from India", "period": "CY2024", "note": _S, "section": "B5"})
DERIVED.append({"id": "D-WD-015", "formula": "F-0176/1000000", "unit": "USD mn", "dec": 1, "metric": "us_imports", "entity": "US imports HS 901831 (syringes) from India", "period": "CY2025", "note": _S, "section": "B5"})
DERIVED.append({"id": "D-WD-016", "formula": "F-0176/F-0175", "unit": "x", "dec": 0, "metric": "growth_multiple", "entity": "US imports HS 901831 (syringes) from India", "period": "CY2025 vs CY2024", "note": "our calculation: 2025 value / 2024 value", "section": "B5"})
