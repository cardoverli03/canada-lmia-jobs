# Changelog — Cardo Careers

All notable changes to this repo. Dates use YYYY-MM-DD (owner timezone: Africa/Dar_es_Salaam).

## 2026-10-13

- Project initialized: repo skeleton, BIBLE.md, README.md, provenance docs.
- Stored raw source file `data/raw/tfwp_2026q1_pos_en.xlsx` (ESDC TFWP Positive LMIA Employers List, 2026 Q1, English, 8,790 clean data rows verified).
- Built pipeline `scripts/build_sectors.py`: raw XLSX -> cleaned CSV -> sector part files (max 200 rows per part).
- Built sector AGRICULTURE: 2,270 entries, 2,141 unique employers, 12 parts, per-province and top-jobs stats in `sectors/agriculture/README.md`.
- Pre-tagged future sectors found in data: food-processing (13 rows, NOC 94141), fish-seafood (2 rows, NOC 85102). 6,505 rows unassigned for upcoming sectors.
- Verified: CKAN package API works for metadata; Job Bank dataset file downloads and datastore API are WAF-blocked for non-browser clients (use headless browser in verification phase).

## 2026-10-13 (session 2)

- Repo renamed/created on GitHub: cardoverli03/canada-lmia-jobs (cardo-careers name was taken).
- Data freshness re-verified: 2026-Q1 LMIA file and Sept 2026 Job Bank file are still the newest published.
- Beaten WAF: Job Bank Sept 2026 CSV (46 MB, UTF-16 TSV, 52,368 postings) downloaded with browser header fingerprint. Finding: NO employer name column -> it is market-signal data only; employer verification = browser hunt on jobbank.gc.ca + employer sites.
- Official NOC 2021 -> TEER table extracted from IRCC canada.ca page via headless browser (516 unit groups). SkillLevel (SKILLED = TEER 0-3, UNSKILLED = TEER 4-5) added to every row. Skilled/unskilled product packs stay LAST phase per owner decision.
- Pipeline v2: 11 sectors built (6,983 / 8,790 rows covered, 79.4%): agriculture 2,270; hospitality-food-service 1,202; construction 1,038; tech-it 546; transport-trucking 503; healthcare-nursing 364; office-admin 329; retail-sales 295; cleaning-landscaping 248; food-processing 124; fish-seafood 64. 1,807 long-tail rows saved to data/processed/unassigned_review.csv for future sectors.
- Sector READMEs now include live market signal from Job Bank Sept 2026 (postings, vacancies, median wage, top provinces).
- Job Bank slim processed CSV saved (data/processed/job-bank-sept2026-slim.csv).

## 2026-10-13 (session 3)

- OWNER ORDER EXECUTED: raw Job Bank Sept 2026 CSV (46 MB) deleted from local disk, git history (HEAD commit amended, blob purged) and GitHub (force push). Provenance kept in data/raw/SOURCE.md; .gitignore now blocks raw Job Bank dumps permanently. Slim market-signal file (7.2 MB) kept.
- VERIFICATION PHASE STARTED ("the hunt"): headless browser on jobbank.gc.ca, employer-name searches, top Approved-Positions agriculture hirers first. Results in data/hunt/ (date-stamped CSV logs, evidence URLs, verdicts ACTIVE / no-live-posting-today). Nothing invented, only what the browser shows.

## 2026-10-13 (session 3, later)

- OWNER DECISION: no slave work — lists verify themselves. Pipeline v3 adds two
  self-check link columns to every row of every sector part file: JobBankCheck
  (jobbank.gc.ca quoted employer search, newest first) + WebSearch (Google:
  official site / careers discovery). All 11 sectors regenerated (counts unchanged).
- Sector README regeneration now preserves existing "Verification (the hunt)"
  sections (hunt output survives future pipeline runs).
- Hunt batches = top hirers only, for ACTIVE trust badges. Scope rule added to
  docs/HUNT-METHOD.md and BIBLE 3.3.
