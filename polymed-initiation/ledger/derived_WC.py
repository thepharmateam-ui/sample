# Derived facts for writer WC (A4.8 cardiology, A4.9 orthopaedics, A5 geographies and entities, A6 manufacturing and R&D).
# Every entry is our calculation from cited ledger facts; the text labels each one "our calculation".
DERIVED = []


def d(i, formula, unit, dec, metric, entity, period, note, section, geography=""):
    DERIVED.append({"id": f"D-WC-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "period": period, "geography": geography,
                    "note": "our calculation: " + note, "section": section})


# ---------------------------------------------------------------- A4.8 cardiology
d(1, "CB-0595*1000", "units", 0, "stents_deployed_cumulative", "Polymed consolidated", "as of 30-Apr-2026",
  "unit conversion of '~11K units' (DK4Q26 p.7) to units", "A4.8")
d(2, "CB-0191*1000", "units", 0, "stents_deployed_cumulative", "Polymed consolidated", "Jul-2026",
  "unit conversion of '~13K units' (DK1Q27 p.22) to units", "A4.8")
d(3, "(CB-0119/1000/CB-2477-1)*100", "%", 1, "revenue_growth_yoy", "PendraCare", "CY25",
  "CY25 revenue (~EUR 8,200K, DK1Q27) vs CY24 pro forma revenue (EUR 9.9mn, DKPEN)", "A4.8")
d(4, "CB-2479/CB-2477*100", "%", 1, "ebitda_margin", "PendraCare", "CY24",
  "CY24 pro forma EBITDA / revenue (DKPEN p.11)", "A4.8")
d(5, "CB-0121/CB-0119*100", "%", 1, "ebitda_margin", "PendraCare", "CY25",
  "CY25 EBITDA / revenue (DK1Q27 p.13)", "A4.8")
d(6, "CB-2478/CB-2477*100", "%", 1, "gross_margin", "PendraCare", "CY24",
  "CY24 pro forma gross profit / revenue (DKPEN p.11)", "A4.8")
d(7, "CB-0120/CB-0119*100", "%", 1, "gross_margin", "PendraCare", "CY25",
  "CY25 gross profit / revenue as printed in DK1Q27 p.13 (the AGM deck prints EUR 6.3mn gross profit)", "A4.8")
d(8, "B-0691+WC-0002+WC-0003", "EUR", 0, "ebitda", "Risor Holdings BV consolidated (PendraCare)", "FY26 (post-acquisition)",
  "profit before tax plus finance cost plus D&A, ~23-Sep-2025 to 31-Mar-2026, unaudited accounts", "A4.8")
d(9, "B-0693/B-0690*100", "%", 1, "employee_cost_pct_revenue", "Risor Holdings BV consolidated (PendraCare)", "FY26 (post-acquisition)",
  "employee benefits expense / revenue from operations, ~23-Sep-2025 to 31-Mar-2026", "A4.8")
d(10, "(B-0690-WC-0004-WC-0005)/B-0690*100", "%", 1, "gross_margin", "Risor Holdings BV consolidated (PendraCare)", "FY26 (post-acquisition)",
  "(revenue - materials consumed - inventory change) / revenue, ~23-Sep-2025 to 31-Mar-2026", "A4.8")
d(11, "CB-1970-CB-0192", "count", 0, "registry_patients_remaining", "Polymed consolidated", "Aug-2026",
  "PACIFIER design target (2,000) less patients enrolled by Aug-2026 (840+)", "A4.8")
d(12, "(CB-0192-CB-1203)/6", "count", 0, "registry_enrolment_per_month", "Polymed consolidated", "Feb-2026 to Aug-2026",
  "patients enrolled between the 3QFY26 deck (200+, 6-Feb-2026) and the 1QFY27 deck (840+, 7-Aug-2026), divided by six months", "A4.8")
d(13, "(CB-1970-CB-0192)/((CB-0192-CB-1203)/6)", "months", 0, "registry_months_to_complete", "Polymed consolidated", "from Aug-2026",
  "remaining patients / Feb-Aug 2026 monthly enrolment pace", "A4.8")
d(14, "E-0152/WC-0030", "x", 1, "cath_labs_growth_multiple", "India cath labs", "2015-2023",
  "cath labs in 2023 (2,500+) / 2015 (~650), Frost & Sullivan for Integris DRHP", "A4.8")

# ---------------------------------------------------------------- A4.9 orthopaedics
d(20, "B-0700-B-0701-WC-0011", "EUR '000", 0, "ebitda", "Medistream SA consolidated (Citieffe)", "CY25",
  "IFRS profit before tax plus D&A plus net financial result (printed lines, SUB26MEDC p.6); the accounts print no EBITDA", "A4.9")
d(21, "WC-0008-WC-0010-WC-0012", "EUR '000", 0, "ebitda", "Medistream SA consolidated (Citieffe)", "CY24",
  "IFRS profit before tax plus D&A plus net financial result (printed lines, SUB26MEDC p.6)", "A4.9")
d(22, "(B-0700-B-0701-WC-0011)/B-0697*100", "%", 1, "ebitda_margin", "Medistream SA consolidated (Citieffe)", "CY25",
  "IFRS-derived EBITDA / sale of goods", "A4.9")
d(23, "(WC-0008-WC-0010-WC-0012)/B-0698*100", "%", 1, "ebitda_margin", "Medistream SA consolidated (Citieffe)", "CY24",
  "IFRS-derived EBITDA / sale of goods", "A4.9")
d(24, "B-0706/WC-0016*100", "%", 0, "receivables_over_120d_share", "Medistream SA consolidated (Citieffe)", "as of 31-Dec-2025",
  "trade receivables over 120 days / gross trade receivables (ageing table, SUB26MEDC p.16)", "A4.9")
d(25, "WC-0017/WC-0018*100", "%", 0, "receivables_over_120d_share", "Medistream SA consolidated (Citieffe)", "as of 31-Dec-2024",
  "trade receivables over 120 days / gross trade receivables (ageing table, SUB26MEDC p.16)", "A4.9")
d(26, "CB-2512/CB-2511*100", "%", 1, "ebitda_margin", "Citieffe", "CY24",
  "company-presented adjusted EBITDA (excludes one-offs) / revenue (PRCIT p.2)", "A4.9")
d(27, "CB-0143/CB-0141*100", "%", 1, "ebitda_margin", "Citieffe", "CY25",
  "company-presented EBITDA / revenue (DK1Q27 p.14)", "A4.9")
d(28, "(CB-0141/1000/CB-2511-1)*100", "%", 1, "revenue_growth_yoy", "Citieffe", "CY25",
  "company-presented CY25 revenue (DK1Q27) vs CY24 (PRCIT)", "A4.9")
d(29, "(B-0697/B-0698-1)*100", "%", 1, "revenue_growth_yoy", "Medistream SA consolidated (Citieffe)", "CY25",
  "IFRS sale of goods CY25 vs CY24", "A4.9")
d(30, "CB-0142/CB-0141*100", "%", 0, "gross_margin", "Citieffe", "CY25",
  "gross profit / revenue as printed in DK1Q27 p.14", "A4.9")
d(31, "CB-0451/CB-0450*100", "%", 0, "gross_margin", "Citieffe", "CY25",
  "gross profit / revenue as printed in the 31st AGM deck (DKAGM31 p.17)", "A4.9")
d(32, "B-0705/B-0704*100", "%", 0, "debt_to_equity", "Medistream SA consolidated (Citieffe)", "as of 31-Dec-2025",
  "interest-bearing financial liabilities / total equity", "A4.9")

# ---------------------------------------------------------------- A5 geographies and entities
d(40, "(A-0567/A-0568-1)*100", "%", 1, "revenue_growth_yoy", "Polymed standalone", "FY26", "standalone export sales to Europe FY26 vs FY25 (AR26 note 43)", "A5", "Europe")
d(41, "(A-0569/A-0570-1)*100", "%", 1, "revenue_growth_yoy", "Polymed standalone", "FY26", "standalone export sales to the Americas FY26 vs FY25", "A5", "Americas")
d(42, "(A-0571/A-0572-1)*100", "%", 1, "revenue_growth_yoy", "Polymed standalone", "FY26", "standalone export sales to Asia FY26 vs FY25", "A5", "Asia")
d(43, "(A-0573/A-0574-1)*100", "%", 1, "revenue_growth_yoy", "Polymed standalone", "FY26", "standalone export sales to Africa FY26 vs FY25", "A5", "Africa")
d(44, "(A-0575/A-0576-1)*100", "%", 0, "revenue_growth_yoy", "Polymed standalone", "FY26", "standalone export sales to other regions FY26 vs FY25", "A5", "Others")
d(45, "(A-0474/A-0475-1)*100", "%", 1, "revenue_growth_yoy", "Polymed standalone", "FY26", "standalone export sales FY26 vs FY25", "A5", "Export")
d(46, "A-0567/A-0474*100", "%", 0, "export_share", "Polymed standalone", "FY26", "Europe share of standalone export sales", "A5", "Europe")
d(47, "A-0569/A-0474*100", "%", 0, "export_share", "Polymed standalone", "FY26", "Americas share of standalone export sales", "A5", "Americas")
d(48, "A-0571/A-0474*100", "%", 0, "export_share", "Polymed standalone", "FY26", "Asia share of standalone export sales", "A5", "Asia")
d(49, "A-0573/A-0474*100", "%", 0, "export_share", "Polymed standalone", "FY26", "Africa share of standalone export sales", "A5", "Africa")
d(50, "(A-0472/A-0473-1)*100", "%", 1, "revenue_growth_yoy", "Polymed standalone", "FY26", "standalone domestic sales FY26 vs FY25", "A5", "India")
d(51, "(B-0712/B-0714-1)*100", "%", 0, "revenue_growth", "Poly Medicure (Laiyang) China", "FY24-FY26", "RMB sales FY26 vs FY24 (audited accounts)", "A5", "China")
d(52, "B-0716/B-0712*100", "%", 1, "gross_margin", "Poly Medicure (Laiyang) China", "FY26", "gross profit / sales, RMB", "A5", "China")
d(53, "WC-0023/B-0713*100", "%", 1, "gross_margin", "Poly Medicure (Laiyang) China", "FY25", "gross profit / sales, RMB", "A5", "China")
d(54, "(B-0681/B-0678-1)*100", "%", 0, "revenue_growth_yoy", "PolyHealth Medical Inc (US)", "FY26", "USD revenue FY26 vs FY25", "A5", "US")
d(55, "A-0622+A-0719", "Rs mn", 1, "net_profit", "Ultra for Medical Products (Egypt associate)", "CY25",
  "profit considered in consolidation (23% share) plus profit not considered (AOC-1 Part B) = the associate's full-year profit", "A5", "Egypt")
d(56, "(A-0622+A-0719)/A-0385*100", "%", 0, "net_margin", "Ultra for Medical Products (Egypt associate)", "CY25",
  "associate profit (AOC-1 Part B) / associate sales (Directors' Report)", "A5", "Egypt")
d(57, "A-0649/A-0039*100", "%", 1, "revenue_share", "Polymed consolidated", "FY26", "sales of foreign subsidiaries / consolidated revenue from operations", "A5", "Foreign subsidiaries")
d(58, "(A-0385/A-0816-1)*100", "%", 0, "revenue_growth", "Ultra for Medical Products (Egypt associate)", "CY23-CY25", "CY25 sales vs CY23 sales in Rs (Directors' Reports)", "A5", "Egypt")
d(59, "(A-0380/A-0381-1)*100", "%", 0, "revenue_growth_yoy", "Plan1Health", "CY25", "CY25 turnover vs CY24 in Rs (Directors' Report)", "A5", "Italy")

# ---------------------------------------------------------------- A6 manufacturing, capacity and R&D
d(70, "CB-0082*1000", "mn units", 0, "installed_capacity", "Polymed consolidated", "FY26", "unit conversion of ~1.9bn units (DK1Q27 p.10)", "A6")
d(71, "A-0800*1000", "mn units", 0, "production_volume", "Polymed consolidated", "FY25", "unit conversion of 1.27bn devices (AR25 p.65)", "A6")
d(72, "CB-2558*1000", "mn units", 0, "installed_capacity", "Polymed consolidated", "FY25 (May-2025)", "unit conversion of 'over 1.8bn devices' (DK4Q25 p.5)", "A6")
d(73, "((D-0151/D-0726)**(1/6)-1)*100", "%", 1, "installed_capacity_cagr", "Polymed consolidated", "FY18-FY24",
  "chartered-engineer capacity tables in the placement documents (PD21 FY18; PD24 FY24)", "A6")
d(74, "((D-0152/D-0727)**(1/6)-1)*100", "%", 1, "production_cagr", "Polymed consolidated", "FY18-FY24",
  "chartered-engineer production tables in the placement documents (PD21 FY18; PD24 FY24)", "A6")
d(75, "B-0827/B-0817*100", "%", 0, "qip_capex_utilised_pct", "Polymed standalone", "as of 31-Mar-2026",
  "QIP-2024 capex object used by 31-Mar-2026 / capex object", "A6")
d(76, "A-0860/(A-0859+A-0860)*100", "%", 0, "contract_worker_share", "Polymed standalone", "as of 31-Mar-2026",
  "contract ('other than permanent') workers / all workers, BRSR26", "A6")
d(77, "(A-0860/A-0877-1)*100", "%", 0, "contract_workers_change", "Polymed standalone", "FY26",
  "contract workers at 31-Mar-2026 vs 31-Mar-2025, BRSR26", "A6")
d(78, "CB-0580-CB-0567", "count", 0, "patents_granted_subsidiaries", "Polymed consolidated", "as of 31-Mar-2026",
  "consolidated patents (399) less standalone patents (348), DK4Q26 pp.4-5", "A6")
d(79, "(A-0412/B-0315)**(1/7)*100-100", "%", 0, "r_and_d_expense_cagr", "Polymed standalone", "FY19-FY26",
  "standalone R&D spend FY26 (AR26 Annexure-8) vs FY19 (AR19)", "A6")
d(80, "(WC-0025/B-0619-1)*100", "%", 0, "ppe_additions_growth", "Polymed standalone", "FY24-FY26",
  "standalone PPE additions FY26 vs FY24", "A6")
