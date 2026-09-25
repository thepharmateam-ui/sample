# Derived calculations for writer WH (A4.7 gastroenterology and enteral, urology, surgery and wound drainage).
# Every row is "our calculation" and is labelled so in the text.
DERIVED = []


def d(i, formula, unit, dec, metric, period, note, entity="", segment="", section="A4.7"):
    DERIVED.append({"id": f"D-WH-{i:03d}", "formula": formula, "unit": unit, "dec": dec, "metric": metric,
                    "entity": entity, "segment": segment, "period": period, "note": "our calculation: " + note,
                    "section": section})


# --- FY18-FY20 growth from the Feb-2021 placement-document product table (consolidated product sales, Rs mn) ---
d(1, "((D-0617/D-0613)**(1/2)-1)*100", "%", 1, "revenue_cagr", "FY18-FY20",
  "surgery & wound drainage revenue CAGR FY18-FY20 (PD21 product table)", "Polymed consolidated", "surgery_wound")
d(2, "((D-0593/D-0589)**(1/2)-1)*100", "%", 1, "revenue_cagr", "FY18-FY20",
  "urology revenue CAGR FY18-FY20 (PD21 product table)", "Polymed consolidated", "urology")
d(3, "((D-0601/D-0597)**(1/2)-1)*100", "%", 1, "revenue_cagr", "FY18-FY20",
  "gastroenterology revenue CAGR FY18-FY20 (PD21 product table)", "Polymed consolidated", "gastro")
d(4, "((D-0655/D-0653)**(1/2)-1)*100", "%", 1, "revenue_cagr", "FY18-FY20",
  "total product sales CAGR FY18-FY20 (PD21 product table)", "Polymed consolidated", "total")
d(5, "D-0594+D-0602+D-0618", "%", 1, "revenue_share", "FY20",
  "urology + gastroenterology + surgery & wound drainage share of product sales (PD21)", "Polymed consolidated",
  "gastro_urology_surgery")
d(6, "D-0593+D-0601+D-0617", "Rs mn", 0, "revenue_by_therapy", "FY20",
  "urology + gastroenterology + surgery & wound drainage revenue (PD21)", "Polymed consolidated",
  "gastro_urology_surgery")

# --- FY25-FY26 from the BRSR shares of standalone turnover ---
d(7, "A-0849+A-0850", "%", 1, "revenue_share", "FY26",
  "surgery & wound drainage + urology share of standalone turnover (BRSR)", "Polymed standalone", "urology_surgery")
d(8, "(A-0849+A-0850)/100*A-0350", "Rs mn", 0, "revenue_by_therapy", "FY26",
  "surgery & wound drainage + urology BRSR shares x standalone revenue from operations", "Polymed standalone",
  "urology_surgery")
d(9, "(A-0897+A-0898)/100*A-0351", "Rs mn", 0, "revenue_by_therapy", "FY25",
  "surgery & wound drainage + urology BRSR shares x standalone revenue from operations", "Polymed standalone",
  "urology_surgery")
d(10, "(A-0849+A-0850)*A-0350/((A-0897+A-0898)*A-0351)*100-100", "%", 1, "revenue_growth_yoy", "FY26",
  "implied yoy change in surgery & wound drainage + urology revenue from BRSR shares", "Polymed standalone",
  "urology_surgery")

# --- Bridging FY20 (PD21, consolidated product sales) to FY25 (BRSR, standalone turnover); bases differ ---
d(11, "A-0897/100*A-0351/D-0617", "x", 1, "revenue_multiple", "FY20-FY25",
  "FY25 BRSR-implied standalone surgery & wound drainage revenue over FY20 PD21 revenue; different bases",
  "Polymed", "surgery_wound")
d(12, "A-0898/100*A-0351/D-0593", "x", 1, "revenue_multiple", "FY20-FY25",
  "FY25 BRSR-implied standalone urology revenue over FY20 PD21 revenue; different bases", "Polymed", "urology")
d(13, "A-0351/D-0655", "x", 1, "revenue_multiple", "FY20-FY25",
  "FY25 standalone revenue from operations over FY20 PD21 total product sales; different bases", "Polymed", "total")

# --- Check on management's 'under 5%' statement (Feb-2025) ---
d(14, "A-0897/100*A-0351/A-0040*100", "%", 1, "revenue_share", "FY25",
  "BRSR-implied standalone surgery & wound drainage revenue as % of FY25 consolidated revenue from operations "
  "(a floor for the consolidated share, as subsidiaries' sales are excluded)", "Polymed", "surgery_wound")
