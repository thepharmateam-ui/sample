# Derived calculations for writer WG (A4.5 diagnostics / blood collection).
# Every row is "our calculation" and is labelled so in the text.
DERIVED = []


def d(i, formula, unit, dec, metric, period, note, entity="", segment="", section="A4.5"):
    DERIVED.append({"id": f"D-WG-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "segment": segment, "period": period, "note": "our calculation: " + note,
                    "section": section})


# --- Traded goods (which the Aug-2024 placement document says included blood-collection tubes in FY22-FY24) ---
d(1, "WB-0039/(WB-0039+WG-0003)*100", "%", 1, "traded_goods_share", "FY24",
  "consolidated traded goods over consolidated sale of products (manufactured + traded)", "Polymed consolidated", "total")
d(2, "WG-0002/(WG-0002+A-0645)*100", "%", 1, "traded_goods_share", "FY26",
  "consolidated traded goods over consolidated sale of products (manufactured + traded)", "Polymed consolidated", "total")
d(3, "WG-0002/WB-0039*100-100", "%", 0, "traded_goods_growth", "FY24-FY26",
  "change in consolidated traded-goods sales, FY26 over FY24", "Polymed consolidated", "total")

# --- PLI (IVD) incentive: eligible incremental sales implied by the incentive received for FY24 ---
d(4, "WG-0006/CC-0176*100", "Rs mn", 0, "pli_implied_incremental_sales", "FY24",
  "incentive received for FY24 (~Rs 1.4 cr, TR2Q25) divided by the 5% incentive rate management cited (TR3Q22); "
  "eligible sales above the scheme base year, not diagnostics revenue", "Polymed standalone", "diagnostics")
