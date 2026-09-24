# Fact ledger – schema and extraction rules

Every figure in the Poly Medicure (Polymed) initiation comes from a row in this ledger. Extraction agents write rows; the report never contains a hand-typed number.

## Files each extraction agent writes (X = the agent's prefix)
- `ledger/shards/X.jsonl`: one JSON object per line, one fact per row.
- `notes/X_digest.md`: qualitative findings grouped by report section, each bullet ending with a citation `[DOC p.N]`.
- `ledger/gaps_X.jsonl`: one row per checklist item not found: `{"question": ..., "searched": "DOC1 pp.x-y; DOC2 ...", "result": "not disclosed" | "partial: ..."}`.

Agents never edit any other file.

## JSONL row fields
| field | meaning |
|---|---|
| `fact_id` | `<prefix>-<4-digit seq>`, e.g. `A-0042` (unique within the shard) |
| `metric` | snake_case name, e.g. `revenue`, `ebitda_margin`, `export_share`, `capacity_units`, `market_size`, `tariff_rate` (see vocabulary below) |
| `entity` | whose number: `Polymed consolidated`, `Polymed standalone`, `PendraCare`, `Citieffe`, `Plan1Health`, `India medtech market`, `BD`, etc. |
| `segment` | `total`, `infusion`, `renal`, `others`, `orthopaedics`, `cardiology`, `blood_management`, `vascular_access`, `diagnostics`, `anaesthesia_respiratory`, `critical_care`, `gastro`, `urology`, `surgery_wound`, `oncology`, `components_oem`, or a free label |
| `geography` | `total`, `India`, `Europe`, `RoW`, `US`, `West Asia`, `Africa`, `LatAm`, `Asia`, `China`, `global`, etc. |
| `period` | `FY26` (year to 31 Mar 2026), `1QFY27`, `9MFY26`, `CY25` (calendar year, used for EU and other overseas entities), `as of 31-Mar-2026`, `Sep-2026` |
| `value` | a number exactly as printed (no conversion) or, for a qualitative fact, a short text |
| `unit` | exactly as printed: `Rs cr`, `Rs lakh`, `Rs mn`, `Rs`, `%`, `EUR mn`, `USD mn`, `units`, `mn units`, `bn units`, `pcs`, `days`, `count`, `x`, `text` |
| `basis` | `reported` (financial statements, results), `disclosed` (deck, AR narrative, BRSR), `guidance` (a forward target management gave), `management_statement` (a factual claim made on a call), `third_party` (rating agency, government, market research, press), `derived` (only if the document itself computes it) |
| `doc_id` | the source document id (see `registry/company_docs.csv`, `registry/external_docs.csv`) |
| `page` | the PDF page number from the `=== [DOC p.N] ===` marker in `sources/text/DOC.txt` (use 1 for HTML/JSON) |
| `snippet` | verbatim text from that page (≤200 chars) that contains the value, so an auditor can re-find it |
| `speaker` | for transcripts: who said it (e.g. `Himanshu Baid, MD`); else empty |
| `section` | the report section(s) this fact serves: `A1`…`A9`, `A4.1`…`A4.10`, `B1`…`B5`, `C` (comma-separated) |
| `note` | anything the auditor needs: restatements, definitions (e.g. "operating EBITDA excl. other income"), conflicts with another doc, `[vendor estimate]`, `[snippet only]` |

Example:
```json
{"fact_id":"CA-0007","metric":"revenue","entity":"Polymed consolidated","segment":"total","geography":"total","period":"FY26","value":1875.3,"unit":"Rs cr","basis":"reported","doc_id":"DK4Q26","page":10,"snippet":"Revenue from Operations 1,875.3","speaker":"","section":"A1,A3","note":""}
```

## Rules (non-negotiable)
1. **Extract, do not interpret.** No unit conversion, no computing growth rates or shares yourself. If the document states a growth rate, record it as its own row.
2. **Never invent or round.** Record the value exactly as printed. If a number is ambiguous (e.g. crore vs lakh, standalone vs consolidated, gross vs net), say so in `note`.
3. **Page numbers come from the markers in the text files.** For image-only pages (little or no text), render the page and read it visually:
   `python3 -c "import pymupdf;d=pymupdf.open('sources/pdf/DOC.pdf');d[N-1].get_pixmap(dpi=110).save('/tmp/claude-0/-home-user-sample/89e7b818-6b30-5219-af66-34a1d913360c/scratchpad/view_DOC_N.png')"`, then open the PNG with the Read tool. In that case put `[visual read]` in `note` and a best-effort transcription in `snippet`.
4. **Conflicts are recorded, not resolved.** If two documents give different values for the same metric and period, record both rows and cross-reference them in `note`.
5. **Forward-looking numbers** carry `basis: guidance` and the date in `note`, e.g. "guided 25-May-2026 (4QFY26 call)".
6. **Qualitative facts** (e.g. which plant makes what, who the customers are, a named competitor) go into the digest with a citation. They go into the ledger only if they carry a number.
7. **Do not read whole large documents.** Use Grep on `sources/text/DOC.txt` (the page markers make grep hits locatable), read the table of contents first, then read the relevant page ranges with the Read tool (offset/limit) or `sed -n`.

## Suggested metric vocabulary
`revenue`, `revenue_growth_yoy`, `gross_margin`, `ebitda`, `ebitda_margin`, `pat`, `other_income`, `rm_cost`, `rm_cost_pct_revenue`, `employee_cost`, `employee_cost_pct_revenue`, `power_fuel_cost`, `freight_cost`, `sterilization_cost`, `r_and_d_expense`, `r_and_d_pct_revenue`, `advertising_promotion`, `commission`, `export_incentive`, `pli_incentive`, `fx_gain_loss`, `capex`, `gross_block`, `asset_turnover`, `installed_capacity`, `production_volume`, `capacity_utilization`, `plants_count`, `headcount`, `products_count`, `sku_count`, `patents_granted`, `patents_pending`, `product_launches`, `export_share`, `revenue_by_geography`, `revenue_by_therapy`, `customer_concentration`, `top_customer_share`, `distributors_count`, `countries_served`, `receivable_days`, `inventory_days`, `payable_days`, `cash_conversion_cycle`, `net_cash`, `debt`, `guidance_revenue`, `guidance_revenue_growth`, `guidance_ebitda_margin`, `guidance_capex`, `dialysis_machines_installed`, `market_size`, `market_growth`, `market_share`, `asp`, `price_increase`, `tariff_rate`, `duty_rate`, `promoter_holding`, `rpt_amount`, `remuneration`, `acquisition_consideration`, `acquisition_ev`, `target_revenue`, `target_ebitda`.
