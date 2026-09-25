# Derived calculations for writer WX (new exhibits in Part B, Part C, the front page and the approvals appendix).
# Every row is "our calculation" and is labelled so in the text.
DERIVED = []


def d(i, formula, unit, dec, metric, period, note, entity="", segment="", section="B4", geography=""):
    DERIVED.append({"id": f"D-WX-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "segment": segment, "geography": geography, "period": period,
                    "note": "our calculation: " + note, "section": section})


# --- B4 b4_us_duty: all additional US duties on India-origin goods after the Russian-oil order ---
d(1, "F-0212+F-0213", "%", 0, "tariff_rate_additional_total", "27-Aug-2025 to 6-Feb-2026",
  "country rate under EO 14326 plus the Russian-oil duty under EO 14329 (Federal Register basis)",
  "US additional duties on India-origin goods", "total", "B4", "India")

# --- B3 b3_pli_paid: PLI incentives paid as a share of the scheme's outlay ---
d(2, "F-0019/F-0008*100", "%", 1, "pli_disbursed_pct_outlay", "up to FY25",
  "PLI incentives released up to FY25 / total scheme outlay", "PLI scheme for medical devices", "total", "B3", "India")

# --- B2 b2_china_overseas: share of revenue earned outside the home market ---
d(3, "E-0266/E-0265*100", "%", 0, "overseas_revenue_share", "CY25",
  "overseas sub-total / total revenue", "Shandong Weigao", "total", "B2", "outside China")
d(4, "E-0393/(E-0391*10000)*100", "%", 0, "overseas_revenue_share", "CY25",
  "overseas revenue (RMB 10k) / total revenue (RMB 100mn, x10,000)", "Jiangxi Sanxin Medtec", "total", "B2", "outside China")
d(5, "(CB-0039-CB-0044)/CB-0039*100", "%", 0, "overseas_revenue_share", "FY26",
  "(consolidated revenue - India revenue) / consolidated revenue", "Polymed consolidated", "total", "B2", "outside India")

# --- C2 c2_empcost: standalone employee benefits expense / revenue from operations, by quarter ---
for _i, (_emp, _rev, _q) in enumerate([("A-1208", "A-1192", "1QFY25"), ("A-1140", "A-1108", "2QFY25"),
                                         ("A-1053", "A-1021", "3QFY25"), ("A-0942", "A-0912", "4QFY25"),
                                         ("A-1207", "A-1191", "1QFY26"), ("A-1139", "A-1107", "2QFY26"),
                                         ("A-0941", "A-0911", "3QFY26"), ("A-0940", "A-0910", "4QFY26"),
                                         ("A-1000", "A-0990", "1QFY27")]):
    d(6 + _i, f"{_emp}/{_rev}*100", "%", 1, "employee_cost_pct_revenue", _q,
      "employee benefits expense / revenue from operations, standalone quarterly results"
      + ("; 3QFY26 as restated in the 4QFY26 results" if _q == "3QFY26" else ""),
      "Polymed standalone", "total", "C", "total")

# --- B4 b4_hs_exports: India's exports from UN Comtrade, US dollars to US$ mn ---
for _i, (_fid, _yr, _hs) in enumerate([("F-0132", "CY2023", "901839"), ("F-0133", "CY2024", "901839"),
                                        ("F-0145", "CY2023", "901831"), ("F-0146", "CY2024", "901831"),
                                        ("F-0147", "CY2025", "901831")]):
    d(15 + _i, f"{_fid}/1000000", "USD mn", 1, "exports_usd_mn", _yr,
      f"India's exports under HS {_hs} (UN Comtrade), converted from US dollars to US$ mn",
      f"India exports HS {_hs}", "infusion" if _hs == "901831" else "vascular_access", "B4", "World")

# --- B5 (proposed b5_us_imports, not used in the drafts): shares of US imports in 2025 ---
d(20, "F-0176/F-0170*100", "%", 1, "us_import_share", "CY2025",
  "US syringe imports (HS 901831) from India / from all origins", "US imports HS 901831, India share", "infusion", "B5", "US")
d(21, "F-0173/F-0170*100", "%", 1, "us_import_share", "CY2025",
  "US syringe imports (HS 901831) from China / from all origins", "US imports HS 901831, China share", "infusion", "B5", "US")
d(22, "F-0178/F-0177*100", "%", 1, "us_import_share", "CY2025",
  "US imports of needles, catheters and cannulas (HS 901839) from China / from all origins",
  "US imports HS 901839, China share", "vascular_access", "B5", "US")
d(23, "F-0181/F-0177*100", "%", 1, "us_import_share", "CY2025",
  "US imports of needles, catheters and cannulas (HS 901839) from Malaysia / from all origins",
  "US imports HS 901839, Malaysia share", "vascular_access", "B5", "US")

# --- B3 b3_import_origin: origin shares of India's imports ---
d(24, "F-0161/F-0160*100", "%", 1, "import_origin_share", "CY2025",
  "India's HS 901890 imports (incl. dialysers) from China / from all origins (UN Comtrade)",
  "India imports HS 901890, China share", "renal", "B3", "China")
d(25, "F-0193/F-0192*100", "%", 1, "import_origin_share", "FY26",
  "India's HS 90189031 imports from China / from all origins (TradeStat)",
  "India imports HS 90189031, China share", "renal", "B3", "China")
d(26, "F-0164/F-0163*100", "%", 1, "import_origin_share", "CY2025",
  "India's HS 901839 imports (needles, catheters, cannulas) from China / from all origins (UN Comtrade)",
  "India imports HS 901839, China share", "vascular_access", "B3", "China")
d(27, "F-0051/F-0050*100", "%", 1, "import_origin_share", "11MFY26 (Apr-Feb)",
  "India's medical-device imports from China / from all origins (EPCMD, Apr-Feb FY26)",
  "India imports of medical devices, China share", "total", "B3", "China")
d(28, "F-0194/F-0192*100", "%", 1, "import_origin_share", "FY26",
  "India's HS 90189031 imports from Malaysia / from all origins (TradeStat)",
  "India imports HS 90189031, Malaysia share", "renal", "B3", "Malaysia")
d(29, "F-0162/F-0160*100", "%", 1, "import_origin_share", "CY2025",
  "India's HS 901890 imports (incl. dialysers) from Malaysia / from all origins (UN Comtrade)",
  "India imports HS 901890, Malaysia share", "renal", "B3", "Malaysia")

# --- B1 b1_rebates: standalone rebates and discounts / standalone revenue from operations ---
d(30, "A-0824/A-0733*100", "%", 1, "rebates_pct_revenue", "FY24",
  "rebates and discounts / revenue from operations, standalone", "Polymed standalone", "total", "B1", "total")
d(31, "A-0480/A-0441*100", "%", 1, "rebates_pct_revenue", "FY25",
  "rebates and discounts / revenue from operations, standalone", "Polymed standalone", "total", "B1", "total")
d(32, "A-0479/A-0440*100", "%", 1, "rebates_pct_revenue", "FY26",
  "rebates and discounts / revenue from operations, standalone", "Polymed standalone", "total", "B1", "total")

# --- B3 b3_pli_paid: Nipro India Corporation's share of PLI incentives paid up to FY25 ---
d(33, "F-0023/F-0019*100", "%", 1, "pli_share_of_disbursed", "FY23-FY25",
  "incentives released to Nipro India Corporation / all incentives released up to FY25",
  "Nipro India Corporation", "renal", "B3", "India")
