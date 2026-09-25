# Derived calculations for writer WF (A4.4 transfusion and blood management).
# Every row is "our calculation" and is labelled so in the text.
DERIVED = []


def d(i, formula, unit, dec, metric, period, note, entity="", segment="blood_management", section="A4.4"):
    DERIVED.append({"id": f"D-WF-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "segment": segment, "period": period, "note": "our calculation: " + note,
                    "section": section})


# --- Blood management & blood collection, placement-document product tables (consolidated product sales) ---
d(1, "D-0607/D-0605*100-100", "%", 0, "revenue_growth_yoy", "FY19", "blood management & collection FY19 over FY18 (PD21 product table)", "Polymed consolidated")
d(2, "D-0609/D-0607*100-100", "%", 0, "revenue_growth_yoy", "FY20", "blood management & collection FY20 over FY19 (PD21 product table)", "Polymed consolidated")
d(3, "D-0049/D-0051*100-100", "%", 0, "revenue_growth_yoy", "FY23", "blood management & collection FY23 over FY22 (PD24 product table)", "Polymed consolidated")
d(4, "D-0047/D-0049*100-100", "%", 0, "revenue_growth_yoy", "FY24", "blood management & collection FY24 over FY23 (PD24 product table)", "Polymed consolidated")
d(5, "((D-0047/D-0605)**(1/6)-1)*100", "%", 1, "revenue_cagr", "FY18-FY24", "CAGR of blood management & collection, FY18 (PD21) to FY24 (PD24); same product definition in both documents", "Polymed consolidated")
d(6, "((D-0070/D-0653)**(1/6)-1)*100", "%", 1, "revenue_cagr", "FY18-FY24", "CAGR of total product sales in the placement-document product tables, FY18 (PD21) to FY24 (PD24)", "Polymed consolidated", "total")

# --- Blood bags in the old Schedule VI annual reports (standalone finished goods sold) ---
d(7, "B-0091/B-0092*100-100", "%", 0, "revenue_growth_yoy", "FY13", "blood-bag sales FY13 over FY12", "Polymed standalone")
d(8, "B-0182/B-0091*100-100", "%", 0, "revenue_growth", "FY13-FY15", "blood-bag sales FY15 over FY13 (two years; FY14 not disclosed)", "Polymed standalone")
d(9, "((B-0181/B-0092)**(1/4)-1)*100", "%", 1, "revenue_cagr", "FY12-FY16", "CAGR of blood-bag sales FY12 to FY16", "Polymed standalone")
d(10, "((WB-0042/WB-0041)**(1/4)-1)*100", "%", 1, "revenue_cagr", "FY12-FY16", "CAGR of all finished goods sold FY12 to FY16", "Polymed standalone", "total")

# --- Basis check: BRSR-implied FY25 revenue against the placement document's FY24 figure ---
d(11, "A-0896/100*A-0351/D-0047", "x", 1, "ratio", "FY25 vs FY24", "BRSR-implied FY25 blood management & collection revenue (share x standalone revenue) over PD24 FY24 consolidated figure; different bases", "Polymed")

# --- Competitor and market arithmetic ---
d(12, "E-0311*(100-E-0312)/100", "mn units", 1, "domestic_volume", "2018", "Terumo Penpol output not exported (30mn bags x (1 - 55% export share))", "Terumo Penpol", "blood_management")
d(13, "E-0314/E-0313", "USD", 1, "market_value_per_collection", "2018", "India blood-bag market value over annual collections, as quoted by Terumo BCT in 2018", "India")
d(14, "E-0362/E-0400", "USD", 1, "market_value_per_donation", "2026 vs 2023 data", "vendor global blood-bag market (2026) over WHO global donations (2023 data); different vintages", "Global")
d(15, "F-0129/F-0128*100", "%", 0, "collection_vs_requirement", "2025", "e-Raktkosh collections 2025 over the government's 14.6mn-unit annual requirement estimate", "India")
d(16, "WF-0003/F-0130*100", "%", 1, "blood_discard_rate", "2023", "units discarded over units collected, 2023", "India")
d(17, "F-0131/WF-0003", "x", 1, "discards_multiple", "2023-2025", "units discarded in 2025 over 2023", "India")
d(18, "E-0316/F-0130*100-100", "%", 0, "blood_collection_growth", "2024", "e-Raktkosh collections 2024 over 2023", "India")
d(19, "F-0129/E-0316*100-100", "%", 0, "blood_collection_growth", "2025", "e-Raktkosh collections 2025 over 2024", "India")
