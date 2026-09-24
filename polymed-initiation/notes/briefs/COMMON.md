# Common brief for all drafting agents

You are drafting part of a sell-side **initiating-coverage report on Poly Medicure Ltd (Polymed, NSE: POLYMED)** for the Avendus Spark pharma/healthcare desk.
- **Scope:** business + industry only. No forecasts, valuation, rating or target price. Management guidance is fine if attributed.
- **Deliverable:** a self-contained HTML report built from markdown drafts. Working directory: `/home/user/sample/polymed-initiation`. Today is 24 Sep 2026; data runs to the 1QFY27 results (7-10 Aug 2026) and the 31st AGM (5 Sep 2026).

**Read first, in this order:**
1. `notes/WRITING_GUIDE.md`: voice, notation, token syntax, block syntax, business-line template. Mandatory.
2. `ledger/SCHEMA.md`: the ledger row format, if you need to add facts.
3. The two sections already drafted, as models of the finished product:
   - `draft/10_A1_revenue.md`
   - `draft/12_A3_fy26_reset.md`

**Evidence available:**
- Ledger: `ledger/facts.csv` / `ledger/facts.jsonl` (~9,000 facts). Search with `python3 build/lookup.py --grep "<regex>" [--shard XX]` or `python3 build/lookup.py FACT-ID ...`.
- Digests (qualitative findings with `[DOC p.N]` citations):
  - `notes/CA_digest.md`: FY25-FY27 call transcripts
  - `notes/CB_digest.md`: decks
  - `notes/CC_digest.md`: FY21-FY24 calls and decks
  - `notes/B_digest.md`: annual reports FY10-FY24, subsidiaries, CRISIL
  - `notes/A_digest.md`: FY26 annual report, BRSR, AGM, results
  - `notes/D_digest.md`: QIP placement documents, catalogues, FDA
  - `notes/D_product_glossary.md`
  - `notes/E_digest.md`: industry, peers, markets
  - `notes/F_digest.md`: policy, tariffs, trade
- Gap logs: `ledger/gaps_*.jsonl`.
- Primary texts: `sources/text/<DOC>.txt`, with page markers.

**Rules that override everything:**
- **Zero fabrication.**
  - Every number is a ledger token.
  - Every qualitative claim carries its source as an HTML comment `<!-- DOC p.N -->` at the end of the sentence or bullet.
  - Our own calculations go in your derived file and are labelled "our calculation" in the text.
  - Undisclosed splits stay `[not disclosed]`, and the question goes to your open-questions list.
- **Attribution.** Management claims are attributed as management's. Third-party market sizes carry their source and vintage, and vendor (market-research) estimates are labelled as such.
- **House style** as in the writing guide.
  - Prose paragraphs, with lists where they genuinely help scanning.
  - Tables for structured comparisons.
  - Exhibit titles state the message.

**Workflow:**
1. Plan your sections against the template, then gather facts: grep the ledger and the digests, and verify key numbers in `sources/text` where a digest is thin.
2. Write each section file in `draft/` (file names below).
3. If you add facts, write them to `ledger/shards/<LETTER>.jsonl` (letters: WA, WB, WC, WD) and derived calculations to `ledger/derived_<LETTER>.py`. Then run `python3 build/reconcile.py`.
4. Check your files:
   - Lint: `python3 verify/lint.py` (fix every ERROR in your files).
   - Test build:
     ```
     python3 -c "import sys; sys.path.insert(0,'build'); import build_report as b; b.load_facts(); b.build('/tmp/claude-0/-home-user-sample/89e7b818-6b30-5219-af66-34a1d913360c/scratchpad/test/<LETTER>.html', ['draft/<file1>.md','draft/<file2>.md'])"
     ```
     The build must report `unresolved tokens=0` and raise no KeyError.
   - Screenshot the build once: `NODE_PATH=/opt/node22/lib/node_modules node build/shoot.js <html> <outprefix> 1280 --full`, then view the PNG. Fix broken tables, overlapping labels and empty charts.
5. Append your open questions for management to `notes/questions_<LETTER>.md`, one per line: `theme | question | why it matters | what to listen for`. They feed the plant-visit question bank.
6. Touch only your own draft files, shard, derived file and questions file.

**Final reply:** 200 words or fewer. List the files written, the number of exhibits, facts added, and the biggest gaps you had to leave as `[not disclosed]`.
