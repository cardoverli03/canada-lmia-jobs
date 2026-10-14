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

`Entry, Employer, JobTitle, NOC, TEER, SkillLevel, City, ProvinceCode, Postal, Program Stream, Approved LMIAs, Approved Positions, Address, JobBankCheck, WebSearch`

- `SkillLevel`: SKILLED (TEER 0-3) / UNSKILLED (TEER 4-5), from the official IRCC TEER table. This column powers the future SKILLED and UNSKILLED product packs — no separate folder until that product phase.
- `JobBankCheck` / `WebSearch` (added 2026-10-13, owner decision): ready-made self-check links built into every row. JobBankCheck opens jobbank.gc.ca pre-filled with a quoted employer search, newest first; WebSearch finds the employer's official site. The list verifies itself — buyers click and see the live situation. We do NOT verify 8,000+ employers by hand (that would be slavery); hunt batches stamp ACTIVE badges on top hirers only. Link URL shape to be spot-checked live once Job Bank access returns (sandbox IP tarpitted 2026-10-13).

### 3.3 Cardo Activity Score (verification phase — not started yet)

Every employer entry gets a status mark. Status text tags (no emojis in files):

- `ACTIVE`  — live posting found (Job Bank and/or employer's own careers page). Date-stamped: "verified DD-MM-YYYY".
- `WATCH`   — no live posting found today, but fresh/recent LMIA history → they hire again; keep on list. (A positive LMIA is typically valid ~6 months for the worker to apply — verify current rule when verification phase starts.)
- `REPEAT`  — high Approved Positions count / appears in multiple quarters → chronic labour-shortage employer. Flag and prioritize for verification.
- `OLD`     — LMIA older than ~1 year, nothing live. Keep on list (still info), marked OLD.

Rules: verification is done in batches, TOP hirers first. We verify what we can and stamp the date. We NEVER present WATCH as ACTIVE.

Scope rule (owner decision 2026-10-13): we do NOT hand-verify every employer — that is slave work and the list doesn't need it. Every row ships with self-check links (JobBankCheck + WebSearch). Hunt batches verify top hirers only, for trust badges and marketing proof. Verification effort stays proportional: hours per sector, not weeks.

---

## 4. SECTOR DEFINITIONS (16 sectors — v1.5 built 2026-10-13, source 2026-Q1)

NOC 2021 5-digit codes from the Occupation column "NNNNN-Title". Assignment = NOC list match first, keyword fallback second (keyword priority order in `scripts/build_sectors.py`). Every NOC code added in v1.5 was taken from the official data rows themselves (title verified in-data), never from memory. Sector counts below are from 2026-Q1:

| Sector | Entries | Parts | Top jobs |
|--------|---------|-------|----------|
| agriculture | 2,270 | 12 | Harvesting labourers 1093, Livestock labourers 736 |
| hospitality-food-service | 1,239 | 7 | Cooks 353, Restaurant managers 295, Food service supervisors 235 |
| construction | 1,133 | 6 | Carpenters 162, Welders 156, Trades helpers 99 (+plumbers/electricians/steamfitters/HVAC) |
| manufacturing-industrial | 527 | 3 | Machinists 102, Electrical mechanics 44, EE eng technologists 37 |
| tech-it | 570 | 3 | Software developers 119, Software engineers 93 (+network technicians) |
| transport-trucking | 503 | 3 | Transport truck drivers 207 |
| healthcare-nursing | 376 | 2 | Nurse aides 131, GPs 59, RNs 26 (+home support workers/caregivers) |
| office-admin | 329 | 2 | Admin officers 83, Accounting techs 67 |
| retail-sales | 295 | 2 | Retail managers 139, Sales supervisors 103 |
| marketing-media-creative | 229 | 2 | Advertising/marketing/PR 69, Graphic designers 46, Producers/directors 26 |
| cleaning-landscaping | 248 | 2 | Landscaping labourers 87, Light duty cleaners 73 |
| food-processing | 124 | 1 | Industrial butchers, Processing labourers |
| beauty-personal-services | 92 | 1 | Services managers 46, Estheticians 23, Hairstylists/barbers 23 |
| education-teaching | 86 | 1 | Early childhood educators 48, University professors 20 |
| repair-maintenance | 79 | 1 | Building maintenance/superintendents 24, Mechanic-trade supervisors 19 |
| fish-seafood | 64 | 1 | Fish/seafood plant workers, Aquaculture labourers |

- Coverage: **8,164 of 8,790 rows (92.9%)**. **626 rows unassigned** (thin mixed-value tail: civil engineers 34, financial/accounting 44, air pilots 20, HR 15, logistics coordinators 23, printing, coaches, vets...) — see `data/processed/unassigned_review.csv`. Not enough coherent volume for honest standalone products; revisit if a future quarter grows any cluster.
- Skill split (all rows): SKILLED 5,847 / UNSKILLED 2,943 (IRCC TEER table).
- Agriculture rule unchanged: Program Stream == `Primary Agriculture` OR NOC in {80020, 82030, 84120, 85100, 85101, 85103, 21112}.
- Every sector README includes a "Live market signal" line from the Job Bank Sept 2026 slim CSV + the self-check-links explainer. Hunt sections survive regeneration.
- Keyword bug fixed 2026-10-13: "Aerospace engineers" matched regex `spa` (Aero**spa**ce) → word-boundary `\bspa\b` rule. Lesson: short keywords need `\b`.

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
- **2026-10-13** — Hunt batch 01 (agriculture top 18) executed via official employer websites (Job Bank tarpitted our IP). Results: 3 ACTIVE (Fraisebec, Monette Farms, Les Jardins Vegibec), 3 site-live-no-public-channel, 9 no-site-found, 2 bot-walled, 1 unreachable. SOP written: docs/HUNT-METHOD.md.
- **2026-10-13** — OWNER DECISION — self-checking lists: hand-verifying all employers is rejected ("we can't be slaves for our business"). Pipeline v3: every row in every sector part file now carries JobBankCheck (pre-filled Job Bank employer search, newest first) + WebSearch (find official site) links. List verifies itself; hunt batches continue for TOP hirers only (ACTIVE badges = marketing proof of care). All 11 sectors regenerated with the two link columns.
- **2026-10-14** — Hunt batch 02 (hospitality-food-service top 15): 3 ACTIVE — North American Midway Entertainment (live application form), ClubLink (live job board, F&B Manager roles posted), Empress Hotel Operations / Fairmont Empress Victoria (dated posting "Journey Person Cook FT" via Accor careers). 1 NO-PUBLIC-CHANNEL (South Shore Fish Shack), 3 BOT-WALLED (Totem Lodge, Cargill x2), 1 WRONG-SITE-LOOKALIKE (rjconcessions.com = Sarasota FL), 8 NO-SITE-FOUND (incl. numbered companies).
- **2026-10-14** — Hunt batch 03 (construction top 15): 4 ACTIVE — Contour Earthmoving (form with 7 operator roles), Rulam Contracting (careers form + Acheson AB address match via FOIP notice), Rafat General Contractor (accepting resumes all positions), Classic Landscapes (resume form, Edmonton confirmed). 1 UNREACHABLE (EVR Operations — careers.glencore.com unresolvable here; occupation match noted), 4 BOT-WALLED, 2 WRONG-SITE-LOOKALIKE (carmacks.ca = Yukon village; cemrock.com = Tucson AZ), 1 NO-PUBLIC-CHANNEL, 3 NO-SITE-FOUND.
- **2026-10-14** — Sandbox was wiped between sessions; full state recovered by anonymous clone from GitHub (repo is public, 46MB-purge verified). Lesson reaffirmed: GitHub is the single source of truth.
- **2026-10-13** — FILTERING COMPLETED to 92.9%: 5 new sectors cut from the 1,807-row long tail (manufacturing-industrial 527, marketing-media-creative 229, beauty-personal-services 92, education-teaching 86, repair-maintenance 79) + expansions (construction +95 with plumbers/electricians/steamfitters/HVAC/floor-covering; healthcare +12 caregivers; tech-it +24 network technicians; hospitality +37 accommodation/hotel). All NOC codes sourced from official data rows. 16 sectors total, 8,164/8,790 rows covered. 626-row thin tail left unassigned on purpose. Bug caught and fixed in review: regex `spa` matched "Aero**spa**ce" — word boundaries added.

---

## 8. CURRENT STATUS / NEXT STEPS

Done:
- Repo created + pushed to GitHub (`cardoverli03/canada-lmia-jobs`), Bible written
- 2026-Q1 EN raw file stored + provenance documented
- Pipeline built (`scripts/build_sectors.py`) — all 11 sectors generated
- Raw 46 MB Job Bank CSV deleted from local + history + GitHub (owner order)
- Pipeline v3 done: self-check links (JobBankCheck + WebSearch) on every row of all sectors.
- FILTERING STAGE COMPLETE: 16 sectors, 8,164/8,790 rows (92.9%), 626-row thin tail documented.
- HUNT batch 01 done (agriculture top 18 by Approved Positions): 3 ACTIVE (Fraisebec,
  Monette Farms, Les Jardins Vegibec), 3 site-live-no-public-channel, 9 no-site-found,
  2 bot-walled, 1 unreachable. Evidence: `data/hunt/2026-10-13_agriculture_batch01.csv`.
- Hunt SOP written: `docs/HUNT-METHOD.md` (verdict vocabulary, traps, toolchain).

Next (in order):
1. Hunt batches (top hirers only): manufacturing-industrial, construction, transport — retry Job Bank cross-check each batch
2. Spot-check JobBankCheck link format live once Job Bank access returns
3. Product phase (only on owner's GO): PDF layout (self-check links become clickable), CV templates, guides, cold emails, disclaimer pages
4. Business phase: Selar (or alternative) store, pricing page, marketing content plan

Standing rule for every future agent: update BIBLE.md (sections 4, 7, 8) after your work. Never break the info-not-promises rule.
