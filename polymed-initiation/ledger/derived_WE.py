# Derived facts for writer WE (appendices: product glossary, regulatory approvals, board and key management).
# Every entry is our calculation from cited ledger facts; the text labels each one "our calculation".
DERIVED = []


def d(i, formula, unit, dec, metric, entity, period, note, section, geography=""):
    DERIVED.append({"id": f"D-WE-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "period": period, "geography": geography,
                    "note": "our calculation: " + note, "section": section})


# ---------------------------------------------------------------- US FDA 510(k)
d(1, "D-0876+D-0877+D-0878+D-0879", "count", 0, "fda_510k_count", "Polymed group (Poly Medicure, Citieffe, PendraCare, Plan1Health)",
  "as of 24-Sep-2026", "sum of openFDA 510(k) records for the four applicants (6 + 11 + 4 + 1)", "Appendix", "US")
d(2, "D-0876+D-0877+D-0878+D-0879-CB-0093", "count", 0, "fda_510k_count_gap", "Polymed group",
  "Sep-2026 vs Aug-2026", "openFDA 510(k) records for the four applicants less the 15 US approvals cited in the 1QFY27 deck", "Appendix", "US")

# ---------------------------------------------------------------- board
d(3, "WM-0051-WE-0001", "count", 0, "executive_directors", "Polymed standalone", "as of 31-Mar-2026",
  "board size (12) less non-executive directors (8), AR26 p.51", "Appendix")
