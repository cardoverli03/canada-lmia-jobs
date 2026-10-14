# Cardo Careers

Filtered, organized sector lists of Canadian employers with approved LMIAs,
built from official Government of Canada open data, for Cardo Careers digital products.

**Agents: read [`BIBLE.md`](BIBLE.md) first — it contains the full business context,
data source documentation, product spec, rules and decisions log.**

## How the data works — the mechanic

The LMIA list is **history**: proof of which employers ran TFWP approvals in Q1 2026.
We use that history as a **target map**, then add live layers on top:

```
LAYER 1 — TARGET MAP (static, from official ESDC data)
  8,790 approval decisions / 7,884 employers / Q1 2026
  filtered into 16 sectors, split SKILLED (TEER 0-3) vs UNSKILLED (TEER 4-5)
  every row carries: employer, city, province, occupation, positions approved
  + JobBankCheck link  -> opens Job Bank search for that exact employer, newest first
  + WebSearch link     -> finds the employer's official site

LAYER 2 — THE HUNT (manual verification, browser + evidence URLs)
  top 191 hirers checked in their official hiring channels, Oct 13-14 2026
  43 stamped ACTIVE with evidence URL + date (data/hunt/ + sector READMEs)
  verdicts: ACTIVE / NO-SITE-FOUND / BOT-WALLED / NO-PUBLIC-CHANNEL /
            UNREACHABLE / WRONG-SITE-LOOKALIKE — nothing invented

LAYER 3 — SELF-VERIFICATION (built into every row)
  the buyer clicks JobBankCheck on ANY row -> sees today's live postings
  (a Job Bank posting exists only while an employer is actively recruiting)
  and each live posting shows its own apply-by deadline
```

**One-line version:** the list tells you WHO proved they hire through TFWP;
the JobBankCheck link tells you IF they are hiring today and by WHEN.

## Quick facts

- Core data: ESDC TFWP Positive LMIA Employers List, **2026 Q1** (English) — 8,790 clean entries, TEER/SkillLevel tagged from the official IRCC table
- **16 sectors · 59 files · 8,164 in-sector rows (5,338 SKILLED + 2,826 UNSKILLED) · 626 longtail documented** — parts of max 200 entries, one skill level per file, Entry numbering continuous per series
- Sectors: agriculture 2,270 | hospitality-food-service 1,239 | construction 1,133 | tech-it 570 | manufacturing-industrial 527 | transport-trucking 503 | healthcare-nursing 376 | office-admin 329 | retail-sales 295 | cleaning-landscaping 248 | marketing-media-creative 229 | food-processing 124 | fish-seafood 64 | repair-maintenance 79 | beauty-personal-services 92 | education-teaching 86
- Hunt: 191 top hirers verified Oct 13–14 2026 — **43 ACTIVE** with evidence URLs (`data/hunt/`)
- Data audit: **14/14 checks passed** (`python3 scripts/audit_data.py`, report in [`docs/DATA-INTEGRITY.md`](docs/DATA-INTEGRITY.md))
- Regenerate lists: `python3 scripts/build_sectors.py`
- Positioning: we sell information and organization. Never promises. Never job guarantees.
- LMIA validity truth: a positive LMIA lasts 6 months from issuance, so all Q1 2026 approval letters have expired by ~Sep 30 2026 — the lists' value is the proven repeat-TFWP employer map (664 employers filed 2+ approvals in one quarter) plus the live verification layers above. Full math in [`docs/DATA-INTEGRITY.md`](docs/DATA-INTEGRITY.md) §4.
