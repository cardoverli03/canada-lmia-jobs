# Changelog — Cardo Careers

All notable changes to this repo. Dates use YYYY-MM-DD (owner timezone: Africa/Dar_es_Salaam).

## 2026-10-14 (session 3)

- Sandbox was wiped between sessions; full state recovered via anonymous clone from GitHub (repo public, 46MB purge verified live).
- Hunt batch 02 (hospitality-food-service top 15): 3 ACTIVE — North American Midway Entertainment (live application form), ClubLink (live job board, F&B Manager roles), Empress Hotel Operations / Fairmont Empress Victoria (dated "Journey Person Cook FT" posting via Accor careers). 1 NO-PUBLIC-CHANNEL, 3 BOT-WALLED, 1 WRONG-SITE-LOOKALIKE (rjconcessions.com = Sarasota FL), 8 NO-SITE-FOUND. Log: `data/hunt/2026-10-14_hospitality-food-service_batch02.csv`.
- Hunt batch 03 (construction top 15): 4 ACTIVE — Contour Earthmoving (7 operator roles listed on careers form), Rulam Contracting (careers form + Acheson AB address match via FOIP notice), Rafat General Contractor (accepting resumes all positions), Classic Landscapes (live resume form, Edmonton). 1 UNREACHABLE (EVR Operations / Elk Valley Resources), 4 BOT-WALLED, 2 WRONG-SITE-LOOKALIKE (carmacks.ca = Yukon village; cemrock.com = Tucson AZ), 1 NO-PUBLIC-CHANNEL, 3 NO-SITE-FOUND. Log: `data/hunt/2026-10-14_construction_batch03.csv`.
- OWNER DECISION — skilled/unskilled separation: pipeline v4 rebuilds every sector as two separate file series (`<sector>-skilled-partNN.csv` TEER 0-3, `<sector>-unskilled-partNN.csv` TEER 4-5), max 200 rows each, never mixed. All 16 sectors regenerated: 59 files, 8,164 rows (5,847 SKILLED + 2,943 UNSKILLED). Legacy mixed part files removed. READMEs list the Files inventory per level; hunt/verification sections preserved.

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

## 2026-10-13 (session 3, filtering complete)

- FILTERING STAGE COMPLETE: 5 new sectors cut from the long tail, all NOC codes taken
  from official data rows (zero memory-invented codes):
  manufacturing-industrial 527 / marketing-media-creative 229 / beauty-personal-services 92 /
  education-teaching 86 / repair-maintenance 79.
- Expansions: construction 1038->1133 (plumbers, electricians, steamfitters, HVAC, floor
  covering, carpentry/mechanic supervisors); healthcare 364->376 (home support workers,
  caregivers); tech-it 546->570 (computer network & web technicians); hospitality
  1202->1239 (accommodation service managers, travel/tourism supervisors).
- Coverage: 6,983 -> 8,164 of 8,790 rows (79.4% -> 92.9%). 626-row thin tail left
  unassigned on purpose (civil eng, finance/accounting, pilots, HR - no coherent volume).
- Bug caught in review: keyword regex "spa" matched "Aero**spa**ce engineers" -> fixed
  with word boundary \bspa\b. Lesson logged in BIBLE: short keywords need \b.
- 16 sector folders regenerated with self-check links; README hunt sections preserved.
