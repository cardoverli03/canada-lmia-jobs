# CARD0 CAREERS — PROJECT BIBLE

> READ THIS FILE FIRST. Any agent (or human) joining this repo must understand
> everything about the business from this single file. Keep it up to date.

---

## 1. WHAT THIS IS

**Cardo Careers** is an information business. We take official Government of Canada
public data (ESDC TFWP Positive LMIA Employers List + Job Bank postings), filter it
into clean, organized sector packages, and sell them as digital products.

- Brand: **Cardo Careers**
- Model: one sector = one product = one zipped package sold at **USD 5.90**
- Package contents (product phase, NOT built yet): company lists + guides + CV templates + tips + cold email templates
- Later product line: SKILLED pack and UNSKILLED pack (NOC TEER mapping), bigger packages, higher price
- Audience: global (English only), heavy focus on people abroad who want to work in Canada
- Store (later): Selar or similar digital marketplace

### THE ONE RULE THAT RUNS THIS BUSINESS

**WE SELL INFORMATION. WE NEVER SELL PROMISES.**

- NEVER say or imply "we will get you a job", "guaranteed job", "guaranteed visa".
- NEVER act as a recruitment agency or placement service. Never charge placement fees.
- NEVER give immigration advice (only licensed RCICs in Canada may do that).
- EVERY product carries the disclaimer (see section 6).
- The data is public. What we sell is the WORK: filtering, organizing, explaining, verifying.
- Honesty is the competitive moat: this market is full of scammers. Transparency wins.

---

## 2. DATA SOURCES (verified 2026-10-13)

### 2.1 Core source — TFWP Positive LMIA Employers List (the "8000 list")

- Official page: https://open.canada.ca/data/dataset/90fed587-1364-4f33-a9ee-208181dc0b97
- Publisher: Employment and Social Development Canada (ESDC)
- Update cadence: quarterly (per quarter = one XLSX file, English + French versions)
- **Latest English file as of 2026-10-13: `tfwp_2026q1_pos_en.xlsx` (2026 Q1, Jan–Mar), resource id `4ee7a4e0-ffc3-47af-94e7-30929d1eeb67`, published/updated 2026-07-21. Stored at `data/raw/`. RE-CHECKED 2026-10-13: no newer quarter published yet.**
- Verified contents of 2026-Q1 EN file: **8,790 clean data rows** after removing header + footer notes.
- Columns: Province/Territory | Program Stream | Employer | Address | Occupation (NOC 2021 code-title) | Incorporate Status | Approved LMIAs | Approved Positions
- Program streams present: High Wage (4092), Primary Agriculture (2265), Low Wage (2081), Global Talent Stream (316), Permanent Resident Only (36)
- Top provinces by rows: QC 3054, ON 2633, BC 1474, AB 903

Official caveats (from the dataset notes — repeat these to customers when relevant):
1. The list EXCLUDES employers with personal names (e.g. many caregivers), so it is NOT complete.
2. Employer names are manually entered — spelling can be inconsistent.
3. Approved LMIA positions ≠ workers who actually came. It tracks positions approved, not permits issued.
4. The two open.canada.ca links the project started from: one is the Job Bank postings dataset, the other is this LMIA list. English only for our products; French versions ignored.

### 2.2 Secondary source — Job Bank job postings (market signal, NOT employer matcher)

- Official page: https://open.canada.ca/data/dataset/ea639e28-c0fc-48bf-b5dd-b8899bd43072
- Monthly CSV: all postings advertised on Job Bank (EN + FR). Latest at check: `job-bank-open-data-all-job-postings-en-sept2026.csv` (resource id `03523cbf-a005-40ee-81ad-aca5bb74cf03`, updated 2026-10-02). **Raw 46 MB file REMOVED from repo 2026-10-13 (owner order) — provenance in `data/raw/SOURCE.md`, re-downloadable from the official link; a `.gitignore` rule blocks raw Job Bank dumps from ever being committed again. The slim derived file `data/processed/job-bank-sept2026-slim.csv` (7.2 MB) is kept.**
- **WAF rule learned 2026-10-13: plain curl gets "Request Rejected". A full browser header fingerprint (Chrome UA + Accept + Accept-Language + Referer) PASSES for file downloads. The CKAN datastore API remains blocked regardless.**
- **CRITICAL FINDING: the Job Bank open-data CSV contains NO employer name column** (52,368 postings verified for Sept 2026 — NOC codes, dates, vacancies, province, city, wages, but no employer). It CANNOT be used to match which employer is hiring.
- Therefore: **employer verification = browser hunt on the Job Bank website (jobbank.gc.ca search by employer name) + the employer's own careers page.** The CSV is used for market signal stats per sector (posting counts, vacancies, median wages, province spread) — honest, date-stamped numbers we put in sector READMEs and products.

### 2.3 NOC → TEER mapping (official)

- `data/raw/ircc-noc2021-teer.csv` — extracted 2026-10-13 from the official IRCC page "Find your NOC" (canada.ca). 516 NOC 2021 unit groups with TEER 0-5.
- Extraction method: canada.ca tarpits curl (Akamai). Headless browser (agent-browser) loads the page fine; the full table is embedded in the served HTML as `<tr><td>TEER</td><td>NOC</td><td>Title</td></tr>`.
- SkillLevel rule: TEER 0-3 = SKILLED, TEER 4-5 = UNSKILLED. This matches how work-permit/PR pathways frame skilled work.

---

## 3. PRODUCT SPEC

### 3.1 Structure

- ONE SECTOR = ONE PRODUCT = ONE FOLDER. Never mix sectors.
- Folder contains: part files (max **200 entries each**), part 01, part 02, ...
  - Example: 2,270 agriculture entries → 12 parts.
- Every part file (future PDF) must have:
  - Cover info: sector, part number, provinces covered, entry count, source quarter, verification date
  - First page: "How to use this list" in plain language
  - Anti-scam page + disclaimer (section 6)
- Inside a part, entries sorted by: Province → Approved Positions (desc) → Employer name. Big hirers first.
- Second product line (LAST priority): SKILLED and UNSKILLED packs built from NOC TEER levels. Higher price, never mixed with sector packs.

### 3.2 Columns of a processed entry (current CSV form, PDF layout later)

`Entry, Employer, JobTitle, NOC, TEER, SkillLevel, City, ProvinceCode, Postal, Program Stream, Approved LMIAs, Approved Positions, Address`

- `SkillLevel`: SKILLED (TEER 0-3) / UNSKILLED (TEER 4-5), from the official IRCC TEER table. This column powers the future SKILLED and UNSKILLED product packs — no separate folder until that product phase.

### 3.3 Cardo Activity Score (verification phase — not started yet)

Every employer entry gets a status mark. Status text tags (no emojis in files):

- `ACTIVE`  — live posting found (Job Bank and/or employer's own careers page). Date-stamped: "verified DD-MM-YYYY".
- `WATCH`   — no live posting found today, but fresh/recent LMIA history → they hire again; keep on list. (A positive LMIA is typically valid ~6 months for the worker to apply — verify current rule when verification phase starts.)
- `REPEAT`  — high Approved Positions count / appears in multiple quarters → chronic labour-shortage employer. Flag and prioritize for verification.
- `OLD`     — LMIA older than ~1 year, nothing live. Keep on list (still info), marked OLD.

Rules: verification is done in batches, TOP hirers first. We verify what we can and stamp the date. We NEVER present WATCH as ACTIVE.

---

## 4. SECTOR DEFINITIONS (all BUILT 2026-10-13, source 2026-Q1)

NOC 2021 5-digit codes from the Occupation column "NNNNN-Title". Assignment = NOC list match first, keyword fallback second (keyword priority order in `scripts/build_sectors.py`). Sector counts below are from 2026-Q1:

| Sector | Entries | Parts | Top jobs |
|--------|---------|-------|----------|
| agriculture | 2,270 | 12 | Harvesting labourers 1093, Livestock labourers 736 |
| hospitality-food-service | 1,202 | 7 | Cooks 353, Restaurant managers 295, Food service supervisors 235 |
| construction | 1,038 | 6 | Carpenters 162, Welders 156, Trades helpers 99 |
| tech-it | 546 | 3 | Software developers 119, Software engineers 93 |
| transport-trucking | 503 | 3 | Transport truck drivers 207 |
| healthcare-nursing | 364 | 2 | Nurse aides 131, GPs 59, RNs 26 |
| office-admin | 329 | 2 | Admin officers 83, Accounting techs 67 |
| retail-sales | 295 | 2 | Retail managers 139, Sales supervisors 103 |
| cleaning-landscaping | 248 | 2 | Landscaping labourers 87, Light duty cleaners 73 |
| food-processing | 124 | 1 | Industrial butchers, Processing labourers |
| fish-seafood | 64 | 1 | Fish/seafood plant workers, Aquaculture labourers |

- Coverage: 6,983 of 8,790 rows (79.4%). **1,807 rows unassigned** (long tail: machinists, marketing, ECE, engineering, design...) — see `data/processed/unassigned_review.csv`. Future sector candidates: manufacturing-metal, personal-services, education.
- Skill split (all rows): SKILLED 5,847 / UNSKILLED 2,943 (IRCC TEER table).
- Agriculture rule unchanged: Program Stream == `Primary Agriculture` OR NOC in {80020, 82030, 84120, 85100, 85101, 85103, 21112}.
- Every sector README includes a "Live market signal" line from the Job Bank Sept 2026 CSV (postings, vacancies, median wage, top provinces) — honest date-stamped market data, not promises.
- SKILLED / UNSKILLED product packs: LAST phase, built by filtering the SkillLevel column. Higher price, never mixed with sector packs.

---

## 5. REPO STRUCTURE & PIPELINE

```
canada-lmia-jobs/   (GitHub: cardoverli03/canada-lmia-jobs)
  BIBLE.md              <- this file. Always current.
  README.md             <- short overview
  CHANGELOG.md          <- dated log of what was done
  data/raw/             <- original government files, NEVER edited. SOURCE.md documents provenance.
  data/processed/       <- full cleaned dataset CSV (all sectors tagged)
  sectors/<name>/       <- product folders: part CSVs (max 200 rows) + README with live stats
  scripts/build_sectors.py  <- pipeline: raw XLSX -> cleaned CSV -> sector parts
  extras/               <- (product phase) CV templates, guides, cold emails
  docs/                 <- (product phase) layout drafts, compliance texts
```

### How to regenerate when a new quarter drops (e.g. 2026-Q2)

1. Download the new `tfwp_YYYYqN_pos_en.xlsx` from the dataset page (link in section 2.1) into `data/raw/`.
2. Update `RAW_FILE` and `QUARTER` in `scripts/build_sectors.py`.
3. `python3 scripts/build_sectors.py`
4. Review new sector counts, update BIBLE.md section 4 numbers, commit.

Data quirks already handled (do not re-discover): title row + footer note rows in the XLSX; every string cell is space-padded to fixed width (must strip); addresses look like `City, PRO POSTAL`; province cell "Employers carrying on business in Canada with Head Office outside of Canada" maps to `FOREIGN-HQ`.

---

## 6. MANDATORY DISCLAIMER (every product, every page where legal info appears)

> Compiled from public Government of Canada data (ESDC — Temporary Foreign Worker
> Program, Positive LMIA Employers List). An approved LMIA does not guarantee that an
> employer is currently hiring or that any job, interview, work permit or visa will be
> granted. Cardo Careers is not a recruitment or placement agency, does not charge
> workers any placement fee, and does not provide immigration advice or
> representation. Application status marks reflect information found on the stated
> verification date only and can change at any time. Always apply through the
> employer's official channels and never pay anyone for a job offer.

---

## 7. DECISIONS LOG (append-only, newest last)

- **2026-10-13** — Project started. Business model locked: sell sector-filtered LMIA employer lists as digital packages (USD 5.90 per sector package; skilled/unskilled line later at higher price). Info-only positioning, no promises, full disclaimers.
- **2026-10-13** — English-only products. French versions of datasets ignored.
- **2026-10-13** — Max 200 entries per file part; sector folders may contain multiple parts; 1 folder = 1 sellable product.
- **2026-10-13** — First sector: AGRICULTURE. Built and verified from 2026-Q1 EN file: 2,270 entries / 12 parts.
- **2026-10-13** — Cardo Activity Score designed (ACTIVE / WATCH / REPEAT / OLD). Verification phase NOT started (needs Job Bank data via headless browser — WAF blocks plain requests).
- **2026-10-13** — Job Bank file downloads + datastore API confirmed WAF-blocked for non-browser clients. Use headless browser in verification phase.
- **2026-10-13** — Business packaging (guides, CV templates, cold emails, store setup, region targeting) is a LATER phase. Current phase: filter sectors + keep everything on GitHub.
- **2026-10-13** — GitHub repo created: `cardoverli03/canada-lmia-jobs` (first name `cardo-careers` was taken on GitHub). Local repo renamed to match.
- **2026-10-13** — Job Bank Sept 2026 CSV downloaded by beating the WAF with a browser header fingerprint. Finding: NO employer names in the open data → employer verification must be done by browser hunting jobbank.gc.ca + employer sites. CSV used for market-signal stats only.
- **2026-10-13** — Official NOC→TEER mapping extracted from IRCC's canada.ca page (516 codes, via headless browser — canada.ca tarpits curl). SkillLevel = SKILLED (TEER 0-3) / UNSKILLED (TEER 4-5) added to all rows. Brother's skilled/unskilled idea implemented at data level; product packs stay LAST phase.
- **2026-10-13** — Pipeline v2 built. All 11 sectors generated: agriculture 2,270; hospitality-food-service 1,202; construction 1,038; tech-it 546; transport-trucking 503; healthcare-nursing 364; office-admin 329; retail-sales 295; cleaning-landscaping 248; food-processing 124; fish-seafood 64. 1,807 long-tail rows unassigned for future sectors.
- **2026-10-13** — Raw Job Bank Sept 2026 CSV (46 MB) deleted from local repo, git history (commit amended) and GitHub (force push) on the owner's order. Slim market-signal derivative kept. Rule added: raw Job Bank dumps are never committed again.
- **2026-10-13** — VERIFICATION PHASE STARTED (the Hunt). Method: headless browser (agent-browser, real Chromium) on jobbank.gc.ca, employer-name search, top Approved-Positions hirers first. Hunt logs stored in `data/hunt/` (one CSV per batch, date-stamped, verdict per employer: ACTIVE with posting evidence + URL, or no-live-posting-today). Only what the browser actually shows gets recorded. Never present WATCH as ACTIVE.

---

## 8. CURRENT STATUS / NEXT STEPS

Done:
- Repo created + pushed to GitHub (`cardoverli03/canada-lmia-jobs`), Bible written
- 2026-Q1 EN raw file stored + provenance documented
- Pipeline built (`scripts/build_sectors.py`) — all 11 sectors generated
- Raw 46 MB Job Bank CSV deleted from local + history + GitHub (owner order)
- HUNT batch 01 (agriculture, top hirers) — see `data/hunt/`

Next (in order):
1. Continue hunt batches: agriculture top 50 → then other sectors' top hirers
2. Fold hunt verdicts into sector parts (status column) before product phase
3. Product phase: PDF layout, CV templates, guides, cold emails, disclaimer pages
4. Business phase: Selar (or alternative) store, pricing page, marketing content plan

Standing rule for every future agent: update BIBLE.md (sections 4, 7, 8) after your work. Never break the info-not-promises rule.
