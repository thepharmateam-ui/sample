# Derived calculations for writer WI (new exhibits in Part A core: A2, A3, A5, A6, A7, A8, A9).
# Every row is "our calculation" and is labelled so in the text.
# Formulas reference base facts only (ids shaped like A-0001); reconcile.py converts amounts to Rs mn first.
DERIVED = []


def d(i, formula, unit, dec, metric, period, note, entity="", segment="", section="A3"):
    DERIVED.append({"id": f"D-WI-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "segment": segment, "period": period, "note": "our calculation: " + note,
                    "section": section})


# --- A3 q_growth: standalone quarterly growth where the deck gives none; consolidated organic growth ---
d(1, "(A-1191/A-1192-1)*100", "%", 1, "revenue_growth_yoy", "1QFY26",
  "standalone revenue from operations 1QFY26 over 1QFY25 (quarterly results)", "Polymed standalone", "total", "A3")
d(2, "(A-1107/A-1108-1)*100", "%", 1, "revenue_growth_yoy", "2QFY26",
  "standalone revenue from operations 2QFY26 over 2QFY25 (quarterly results)", "Polymed standalone", "total", "A3")
d(3, "(CB-0575/CB-0705-1)*100", "%", 1, "organic_revenue_growth_yoy", "4QFY26",
  "4QFY26 organic revenue (excl. PendraCare and Citieffe, company figure) over 4QFY25 consolidated revenue",
  "Polymed consolidated (organic)", "total", "A3")

# --- A2 export_inc: export incentives against foreign-exchange earnings (standalone) ---
d(4, "B-0296/B-0298*100", "%", 1, "export_incentive_pct_fx_earnings", "FY19",
  "export incentives over foreign-exchange earnings", "Polymed standalone", "total", "A2")
d(5, "B-0481/B-0484*100", "%", 1, "export_incentive_pct_fx_earnings", "FY22",
  "export incentives over foreign-exchange earnings", "Polymed standalone", "total", "A2")
d(6, "A-0469/A-0419*100", "%", 1, "export_incentive_pct_fx_earnings", "FY26",
  "export and other incentives over foreign-exchange earnings", "Polymed standalone", "total", "A2")
d(7, "A-0419/B-0298", "x", 1, "fx_earnings_multiple", "FY19-FY26",
  "FY26 foreign-exchange earnings over FY19", "Polymed standalone", "total", "A2")

# --- A9 md_pay_pat: MD + JMD remuneration (incl. commission) over standalone PAT ---
for i, (md_, jmd, pat, yr) in enumerate([
        ("B-0147", "B-0149", "B-0081", "FY13"), ("B-0255", "B-0257", "B-0167", "FY16"),
        ("B-0340", "B-0342", "B-0271", "FY19"), ("B-0394", "B-0395", "B-0360", "FY20"),
        ("B-0457", "B-0458", "B-0412", "FY21"), ("B-0510", "B-0511", "B-0472", "FY22"),
        ("B-0574", "B-0575", "B-0534", "FY23"), ("B-0640", "B-0641", "B-0591", "FY24")]):
    d(8 + i, f"({md_}+{jmd})/{pat}*100", "%", 1, "md_jmd_pay_pct_standalone_pat", yr,
      "remuneration of the MD and the JMD (an executive director before FY20) from the related-party note over standalone PAT",
      "Polymed standalone", "total", "A9")

# --- A9 oi_pbt: other income over standalone profit before tax ---
for i, (oi, pbt, yr) in enumerate([
        ("B-0361", "CC-0895", "FY20"), ("B-0413", "CC-0896", "FY21"), ("B-0473", "CC-0897", "FY22"),
        ("B-0592", "CB-2752", "FY24"), ("A-0354", "A-0366", "FY25"), ("A-0353", "A-0365", "FY26")]):
    d(16 + i, f"{oi}/{pbt}*100", "%", 1, "other_income_pct_pbt", yr,
      "standalone other income over standalone profit before tax", "Polymed standalone", "total", "A9")
d(22, "(A-0485+A-0486+A-0487)/A-0353*100", "%", 1, "treasury_fx_share_of_other_income", "FY26",
  "realised and unrealised mutual-fund gains plus FX gains over standalone other income", "Polymed standalone", "total", "A9")

# --- A6 headcount: BRSR permanent staff, long-run multiples and the FY26 Rule 5 change ---
d(23, "A-0904+A-0905", "count", 0, "headcount_permanent_brsr", "as of 31-Mar-2025",
  "BRSR permanent employees plus permanent workers", "Polymed standalone", "total", "A6")
d(24, "A-0858+A-0859", "count", 0, "headcount_permanent_brsr", "as of 31-Mar-2026",
  "BRSR permanent employees plus permanent workers", "Polymed standalone", "total", "A6")
d(25, "A-0735/B-0043", "x", 1, "headcount_multiple", "FY10-FY25",
  "employees at 31-Mar-2025 over employees at 31-Mar-2010", "Polymed standalone", "total", "A6")
d(26, "A-0351/B-0001", "x", 1, "revenue_multiple", "FY10-FY25",
  "FY25 standalone revenue from operations over FY10 net sales", "Polymed standalone", "total", "A6")
d(27, "(A-0144/A-0735-1)*100", "%", 1, "headcount_growth_yoy", "FY26",
  "Rule 5 count of permanent employees at 31-Mar-2026 over the count at 31-Mar-2025", "Polymed standalone", "total", "A6")

# --- A9 vitromed_hist: job work paid to parties other than Vitromed (Rs mn) ---
for i, (tot, vit, yr) in enumerate([
        ("B-0031", "B-0058", "FY10"), ("B-0119", "B-0141", "FY13"), ("B-0204", "B-0249", "FY16"),
        ("B-0308", "B-0332", "FY19"), ("B-0382", "B-0390", "FY20"), ("B-0430", "B-0452", "FY21"),
        ("B-0489", "B-0505", "FY22"), ("B-0550", "B-0569", "FY23"), ("B-0613", "B-0634", "FY24"),
        ("A-0507", "A-0548", "FY25"), ("A-0506", "A-0547", "FY26")]):
    d(28 + i, f"{tot}-{vit}", "Rs mn", 1, "job_work_other_than_vitromed", yr,
      "standalone job-work charges less job work paid to Vitromed Healthcare", "Polymed standalone", "job work", "A9")

# --- A9 qip24_pace: share of QIP-2024 net proceeds used ---
d(39, "B-0826/B-0816*100", "%", 1, "qip_proceeds_used_pct", "as of 31-Mar-2026",
  "QIP-2024 proceeds used by 31-Mar-2026 over net proceeds", "Polymed standalone", "QIP Aug-2024", "A9")
