# Writing guide – Poly Medicure initiation (business + industry)

The report is a sell-side **initiating-coverage report** for the Avendus Spark pharma/healthcare desk. It covers the **business and the industry only**. There are **no** forecasts, estimates, valuation, rating, target price, multiples or financial-statement section. Management guidance may be reported, but always attributed to management.

The reader is an institutional investor or the analyst themselves. They want to understand:
- what Polymed makes and how it makes money;
- what drives growth and margins, for each business line;
- the industry: markets, customers, competition and regulation;
- everything else they would not know to ask.

## 1. Zero fabrication – the one rule that overrides everything
- **Never type a number into prose or a table.** Every figure is a ledger token: `{{FACT_ID}}`, e.g. `{{CB-0039}}`. The build replaces it with the house-style display string ("Rs. 18.8bn") and a hover tooltip naming the source document and page.
- The ledger lives in `ledger/facts.csv` (human-readable) and `ledger/facts.jsonl`. Look facts up with grep, e.g. `grep -i "renal" ledger/facts.csv | grep FY26`.
- **Token modifiers:**
  - `|approx` adds `~`.
  - `|bn` / `|mn` force the Rs scale.
  - `|signed` adds `+`.
  - `|num` prints the bare number.
  - `|plain` prints the value exactly as the source printed it.
  - Combine them with commas: `{{CB-0024|bn,approx}}`.
- **Numbers you need but the ledger lacks:**
  - If the source contains the number, add the row to `ledger/shards/W<X>.jsonl` where X is your letter (WA, WB, WC, WD; fact ids `WA-0001`…) (your own shard, schema in `ledger/SCHEMA.md`) with its doc and page, then run `python3 build/reconcile.py`.
  - If the number is a calculation (a share, growth or CAGR computed by us), add it to `ledger/derived_W<X>.py` as `DERIVED += [{"id":"D-WA-001","formula":"CB-0024/CB-0039*100","unit":"%","dec":1,"metric":"infusion_share","period":"FY26","note":"our calculation"}]`. Say "our calculation" in the text.
  - If the source does not have it, write `[not disclosed]` and add the question to the what-to-watch table. **Never estimate a split management declined to give** (e.g. revenue of blood bags, urology, diagnostics or oncology).
- Numbers that need no token: years (2026), fiscal labels (FY26, 1QFY27, FY26-28), section IDs, exhibit numbers, dates (24 Sep 2026), regulation and instrument numbers (Reg. (EU) 2023/607, G.S.R. 515(E), HS 901839), product codes (K252677), gauge sizes (22G), and list markers 1) 2) 3).
- **Attribution.** Management statements are attributed with the right verb ("management guided", "the MD indicated", "management declined to disclose"). Third-party data carries its vintage in the text or source line. Vendor market-research numbers are labelled as vendor estimates, used as ranges, and never presented as fact.
- **Causality.** When management gave a reason, say so ("management attributed the decline to …"). When the reason is our inference, say "we infer" / "we read this as" and show the arithmetic. Never upgrade a hedge into a claim.

## 2. House voice (Avendus Spark)
- **Voice and density:**
  - Dense, declarative and evidence-first.
  - First-person plural: "We see / We note / We view / We estimate (only for our own calculations)".
  - Every claim carries a number or a named driver.
  - Sentences can be long and clause-chained: metric + comparison + driver + offset in one breath.
- **Causal connectives do the work:** driven by, aided by, underpinned by, supported by, partly offset by, on the back of, reflecting.
- **Judgement is stated flatly** ("we see downside risk to …", "which we view as reasonable"). No false balance.
- **Notation:**
  - Rs. 18.8bn / Rs. 723mn (≥Rs. 1bn in bn to one decimal), never crore or lakh. The tokens handle this.
  - Periods: 1QFY27, 4QFY26, FY26, CY25 (overseas entities report calendar years).
  - Growth: +19% yoy, qoq; margins in bps; uppercase CAGR; `~` on estimates.
  - Pair metrics with slashes: "revenue/EBITDA grew 22%/37% yoy" (both values as tokens).
  - Comparisons in parentheses: "(vs. Rs. 700mn in 4QFY26)".
  - Reasons enumerate inline as 1) … 2) … 3); transaction steps as a) … b) … c).
  - Ranges use a hyphen (6-7%). Use an en dash `–` only as punctuation, never an em dash.
  - "West Asia", not "Middle East", except inside a proper name or quote.
  - Oxford spelling: -our (favourable, labour) with -ize (utilization, specialized, sterilization); analyse, dialyser (use "dialyzer" only in official names).
- **Banned:**
  - Words: delve, leverage (verb), robust (unquantified), pivotal, poised to, underscore, crucial, transformative, testament to, game-changing, navigate (metaphorical), serves as, stands as.
  - Throat-clearing openers: It's worth noting, Importantly, That said, Overall, In conclusion.
  - Constructions: rule-of-three padding; "It's not X – it's Y"; participial tails ("…, positioning the company for growth"); bold phrases inside prose; bullet-point fragments where prose belongs.
- **Headings are descriptive.** A section may open with a one-sentence "so what" in plain prose.

## 3. Markdown conventions and blocks
- Heading levels:
  - `# Part A – The business` (part)
  - `## A4.3 Renal care` (section)
  - `### Market and demand` (sub-section)
  - `####` sparingly.
- **Chart exhibit.** The title is the message ("Infusion's share has fallen to half of revenue as renal and acquisitions grew faster"), not a label. The JSON is:
```
::: chart
{"id":"renal_rev","type":"column","title":"…message title…","cats":["FY23","FY24","FY25","FY26"],"scale":"bn","unit":"Rs bn","series":[{"name":"Renal","facts":["CB-0027","CB-0028","CB-0029","CB-0030"]}],"note":"optional note with {{tokens}}"}
:::
```
  - Types: `column`, `stacked_column` (add `"totals":true`), `hbar`, `stacked_hbar`, `share_hbar` (values are % shares), `line` (`"ymin":…` optional).
  - Keep to ≤6 series; the categorical colours follow series order.
  - Every series value is a fact ID. Use `"-"` for a gap.
- **Table exhibit.** A standard markdown table: tokens in numeric cells, text elsewhere, `–` for empty.
```
::: table id="renal_comp" title="…message title…" note="optional"
| Company | Products | Scale |
|---|---|---|
| … | … | {{E-0012}} |
:::
```
- **Callout.** Kinds: `note` (blue), `debate`, `risk` (warm).
```
::: callout title="Key debate" kind="debate"
text…
:::
```
- **Snapshot box** at the top of every business-line section. One `Key | value` pair per line; values may contain tokens:
```
::: snapshot title="Renal care at a glance"
Revenue FY26 | {{CB-0030}} ({{D-WB-001}} of consolidated)
Growth FY26 | {{CB-0031}}
What is disclosed | Annual and quarterly revenue; no product split
:::
```
- Cross-reference an exhibit with `[[EXREF:renal_rev]]`.

## 4. Business-line chapter template (A4.x)
0. Snapshot box: revenue FY23 to 1QFY27 where disclosed, share of group, growth, disclosure gaps.
1. **What it is and how it is used:** products, clinical use, the unit of demand (e.g. one cannula per insertion; one AV fistula needle pair and one bloodline set per haemodialysis session).
2. **Polymed's portfolio and position:** brands, approvals, capacity, plants, share claims (attributed).
3. **Market:** size, growth and structure, global and India, with the source's vintage.
4. **Customers, channel and pricing:** who buys, how and at what price points (if disclosed); tenders vs trade vs OEM.
5. **Competition:** named competitors, shares where known, Polymed's differentiation.
6. **Regulation and policy** specific to the line.
7. **Capacity and supply chain.**
8. **Company-specific growth drivers**, ranked: mechanism + evidence + timing, tagged management target vs our view.
9. **Company-specific margin drivers**, ranked.
10. **What to watch:** a table with columns KPI/risk | why it matters | latest datapoint | where disclosed. Also list open questions for management, which feed the question bank.

Length: the core lines (infusion, renal, cardiology, orthopaedics) run 1,200-1,800 words plus 3-5 exhibits each; the smaller lines 600-1,000 words plus 1-3 exhibits.

## 5. Sources to draw on
- **Digests:** `notes/*_digest.md`. Qualitative facts carry `[DOC p.N]` citations; keep the citation as an HTML comment at the end of the sentence (`<!-- DK4Q26 p.33 -->`) so the auditor can trace qualitative claims.
- **Product glossary:** `notes/D_product_glossary.md`.
- **Gap logs:** `ledger/gaps_*.jsonl`.
- **Primary texts:** `sources/text/<DOC>.txt` for anything you need to verify. If you find a new number, add it to your shard.
