# Derived calculations for writer WB (A4.3 renal, A4.4 blood, A4.5 diagnostics, A4.7 gastro/urology/surgery).
# Every row is "our calculation" and is labelled so in the text.
DERIVED = []


def d(i, formula, unit, dec, metric, period, note, entity="", segment="", section="A4.3"):
    DERIVED.append({"id": f"D-WB-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "segment": segment, "period": period, "note": "our calculation: " + note,
                    "section": section})


# --- BRSR product-family shares x standalone revenue from operations (Rs mn) ---
d(1, "A-0847/100*A-0350", "Rs mn", 0, "revenue_by_therapy", "FY26", "dialysis share of standalone turnover (BRSR) x standalone revenue", "Polymed standalone", "renal")
d(2, "A-0895/100*A-0351", "Rs mn", 0, "revenue_by_therapy", "FY25", "dialysis share of standalone turnover (BRSR) x standalone revenue", "Polymed standalone", "renal")
d(3, "A-0848/100*A-0350", "Rs mn", 0, "revenue_by_therapy", "FY26", "blood management & collection share (BRSR) x standalone revenue", "Polymed standalone", "blood_management", "A4.4")
d(4, "A-0896/100*A-0351", "Rs mn", 0, "revenue_by_therapy", "FY25", "blood management & collection share (BRSR) x standalone revenue", "Polymed standalone", "blood_management", "A4.4")
d(5, "A-0849/100*A-0350", "Rs mn", 0, "revenue_by_therapy", "FY26", "surgery & wound drainage share (BRSR) x standalone revenue", "Polymed standalone", "surgery_wound", "A4.7")
d(6, "A-0897/100*A-0351", "Rs mn", 0, "revenue_by_therapy", "FY25", "surgery & wound drainage share (BRSR) x standalone revenue", "Polymed standalone", "surgery_wound", "A4.7")
d(7, "A-0850/100*A-0350", "Rs mn", 0, "revenue_by_therapy", "FY26", "urology share (BRSR) x standalone revenue", "Polymed standalone", "urology", "A4.7")
d(8, "A-0898/100*A-0351", "Rs mn", 0, "revenue_by_therapy", "FY25", "urology share (BRSR) x standalone revenue", "Polymed standalone", "urology", "A4.7")
d(9, "A-0848*A-0350/(A-0896*A-0351)*100-100", "%", 1, "revenue_growth_yoy", "FY26", "implied yoy change in blood management & collection revenue from BRSR shares", "Polymed standalone", "blood_management", "A4.4")
d(10, "A-0849*A-0350/(A-0897*A-0351)*100-100", "%", 1, "revenue_growth_yoy", "FY26", "implied yoy change in surgery & wound drainage revenue from BRSR shares", "Polymed standalone", "surgery_wound", "A4.7")
d(11, "A-0850*A-0350/(A-0898*A-0351)*100-100", "%", 1, "revenue_growth_yoy", "FY26", "implied yoy change in urology revenue from BRSR shares", "Polymed standalone", "urology", "A4.7")

# --- Renal growth and installed base ---
d(12, "CB-0870/D-0621", "x", 0, "revenue_multiple", "FY18-FY26", "FY26 renal revenue (deck) over FY18 dialysis revenue (PD21 product table)", "Polymed consolidated", "renal")
d(13, "CB-0868/CB-1530*100-100", "%", 1, "revenue_growth_qoq", "4QFY26", "4QFY26 renal revenue over 3QFY26", "Polymed consolidated", "renal")
d(14, "CB-0194/E-0043*100", "%", 1, "installed_base_share", "Aug-2026", "Polymed installed machines (Aug-2026) over India's installed base per F&S (2025); different dates", "Polymed", "renal")
d(15, "F-0114/E-0043*100", "%", 0, "installed_base_share", "Sep-2026", "PMNDP HD machines (dashboard, Sep-2026) over India's installed base per F&S (2025); different dates", "PMNDP", "renal")

# --- Imports under HS 90189031, declared quantities in mn units ---
for i, (fid, yr) in enumerate([("WB-0002", "FY23"), ("WB-0003", "FY24"), ("WB-0004", "FY25"), ("WB-0005", "FY26")]):
    d(16 + i, f"{fid}/1000000", "mn units", 2, "imports_volume", yr, "declared import quantity from China, in mn units", "India imports from China", "renal")
for i, (fid, yr) in enumerate([("WB-0007", "FY23"), ("WB-0008", "FY24"), ("WB-0009", "FY25"), ("WB-0010", "FY26")]):
    d(20 + i, f"{fid}/1000000", "mn units", 2, "imports_volume", yr, "declared import quantity from Malaysia, in mn units", "India imports from Malaysia", "renal")
for i, (fid, yr) in enumerate([("WB-0011", "FY23"), ("WB-0012", "FY24"), ("WB-0013", "FY25"), ("WB-0014", "FY26")]):
    d(24 + i, f"{fid}/1000000", "mn units", 2, "imports_volume", yr, "declared import quantity from Hong Kong, in mn units", "India imports from Hong Kong", "renal")

# --- Declared unit values FY26 (US$ per unit; the line also covers machines) ---
d(28, "F-0193*1000000/WB-0005", "USD", 1, "import_unit_value", "FY26", "China import value over declared quantity", "India imports from China", "renal")
d(29, "F-0194*1000000/WB-0010", "USD", 1, "import_unit_value", "FY26", "Malaysia import value over declared quantity", "India imports from Malaysia", "renal")
d(30, "WB-0015*1000000/WB-0014", "USD", 1, "import_unit_value", "FY26", "Hong Kong import value over declared quantity", "India imports from Hong Kong", "renal")
d(31, "WB-0016*1000000/WB-0017", "USD", 1, "import_unit_value", "FY26", "Japan import value over declared quantity", "India imports from Japan", "renal")
d(32, "F-0195*1000000/WB-0018", "USD", 1, "import_unit_value", "FY26", "Germany import value over declared quantity (likely includes machines)", "India imports from Germany", "renal")

# --- Import value shares ---
d(33, "WB-0001/WB-0019*100", "%", 0, "import_share", "FY23", "China share of HS 90189031 import value", "India imports from China", "renal")
d(34, "F-0193/F-0192*100", "%", 0, "import_share", "FY26", "China share of HS 90189031 import value", "India imports from China", "renal")
d(35, "(F-0194+WB-0015)/F-0192*100", "%", 0, "import_share", "FY26", "Malaysia + Hong Kong share of HS 90189031 import value", "India imports from Malaysia and Hong Kong", "renal")
d(36, "(WB-0004+WB-0009+WB-0013)/1000000", "mn units", 1, "imports_volume", "FY25", "China + Malaysia + Hong Kong declared quantity, mn units", "India imports (China, Malaysia, HK)", "renal")
d(37, "(WB-0005+WB-0010+WB-0014)/1000000", "mn units", 1, "imports_volume", "FY26", "China + Malaysia + Hong Kong declared quantity, mn units", "India imports (China, Malaysia, HK)", "renal")

# --- PLI: renal revenue above the FY20 base vs Category A thresholds (Rs mn) ---
d(38, "CB-0870-D-0625", "Rs mn", 0, "renal_revenue_above_fy20_base", "FY26", "FY26 renal revenue less FY20 dialysis revenue (proxy for PLI incremental sales)", "Polymed", "renal")
d(39, "CB-0871-D-0625", "Rs mn", 0, "renal_revenue_above_fy20_base", "FY25", "FY25 renal revenue less FY20 dialysis revenue (proxy for PLI incremental sales)", "Polymed", "renal")
d(40, "D-0055-D-0625", "Rs mn", 0, "renal_revenue_above_fy20_base", "FY24", "FY24 dialysis revenue less FY20 (proxy for PLI incremental sales)", "Polymed", "renal")
d(41, "D-0057-D-0625", "Rs mn", 0, "renal_revenue_above_fy20_base", "FY23", "FY23 dialysis revenue less FY20 (proxy for PLI incremental sales)", "Polymed", "renal")

# --- Blood bags in the older annual reports ---
d(42, "B-0092/WB-0041*100", "%", 1, "revenue_share", "FY12", "blood-bag sales over finished goods sold", "Polymed standalone", "blood_management", "A4.4")
d(43, "B-0091/WB-0040*100", "%", 1, "revenue_share", "FY13", "blood-bag sales over finished goods sold", "Polymed standalone", "blood_management", "A4.4")
d(44, "B-0182/WB-0043*100", "%", 1, "revenue_share", "FY15", "blood-bag sales over finished goods sold", "Polymed standalone", "blood_management", "A4.4")
d(45, "B-0181/WB-0042*100", "%", 1, "revenue_share", "FY16", "blood-bag sales over finished goods sold", "Polymed standalone", "blood_management", "A4.4")
d(46, "B-0181/B-0182*100-100", "%", 0, "revenue_growth_yoy", "FY16", "blood-bag sales growth FY16 over FY15", "Polymed standalone", "blood_management", "A4.4")

# --- India blood collection ---
d(47, "F-0129/F-0130*100-100", "%", 0, "blood_collection_growth", "2023-2025", "e-Raktkosh collections 2025 over 2023", "India", "blood_management", "A4.4")
d(48, "F-0131/F-0129*100", "%", 0, "blood_discard_rate", "2025", "units discarded over units collected, 2025", "India", "blood_management", "A4.4")

# --- Other renal context ---
d(49, "WB-0024-WB-0025", "count", 0, "dialysis_machines_added", "Apr-2023 to Sep-2025", "NephroPlus fleet at 30-Sep-2025 less fleet at 31-Mar-2023", "NephroPlus", "renal")
d(50, "WB-0005/WB-0004*100-100", "%", 0, "imports_volume_growth", "FY26", "change in declared quantity from China", "India imports from China", "renal")
d(51, "WB-0010/WB-0009*100-100", "%", 0, "imports_volume_growth", "FY26", "change in declared quantity from Malaysia", "India imports from Malaysia", "renal")
d(52, "F-0192/WB-0019*100-100", "%", 0, "imports_growth", "FY23-FY26", "growth in total HS 90189031 import value FY23 to FY26", "India imports", "renal")
d(53, "(A-0848+A-0849+A-0850)", "%", 1, "revenue_share", "FY26", "blood + surgery + urology share of standalone turnover (BRSR)", "Polymed standalone", "others", "A4.7")

# --- Unit conversions for management estimates ---
d(54, "WB-0049/1000000", "mn units", 0, "market_size_volume", "Feb-2023", "MD's high-end dialyser consumption estimate in mn units", "India", "renal")
d(55, "WB-0050/1000000", "Rs mn", 1, "asp", "May-2023", "MD's low-end machine price in Rs mn", "India", "renal")
d(56, "WB-0051/1000000", "Rs mn", 1, "asp", "May-2023", "MD's high-end machine price in Rs mn", "India", "renal")

# --- Demand arithmetic and growth checks ---
d(57, "E-0057*2", "mn units", 1, "fistula_needle_demand", "2024", "in-clinic HD treatments x a pair of AV fistula needles per session (single use)", "India", "renal")
d(58, "((E-0058/E-0057)**(1/5)-1)*100", "%", 1, "dialysis_treatments_cagr", "2024-2029F", "CAGR of F&S in-clinic treatment forecast", "India", "renal")
d(59, "D-0057/D-0059*100-100", "%", 0, "revenue_growth_yoy", "FY23", "dialysis revenue FY23 over FY22 (PD24 product table)", "Polymed consolidated", "renal")
d(60, "D-0055/D-0057*100-100", "%", 0, "revenue_growth_yoy", "FY24", "dialysis revenue FY24 over FY23 (PD24 product table)", "Polymed consolidated", "renal")
d(61, "CB-0871/D-0055*100-100", "%", 0, "revenue_growth_yoy", "FY25", "renal revenue FY25 (deck) over FY24 dialysis revenue (PD24 table)", "Polymed consolidated", "renal")
d(62, "(CB-0348+CB-1822+CB-1530+CB-0868)", "Rs mn", 0, "revenue", "FY26", "sum of the four FY26 quarters as last reported (1QFY26 restated in the 1QFY27 deck)", "Polymed consolidated", "renal")
