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
- **Latest English file as of 2026-10-13: `tfwp_2026q1_pos_en.xlsx` (2026 Q1, Jan–Mar), resource id `4ee7a4e0-ffc3-47af-94e7-30929d1eeb67`, published/updated 2026-07-21. Stored at `data/raw/`.**
- Verified contents of 2026-Q1 EN file: **8,790 clean data rows** after removing header + footer notes.
- Columns: Province/Territory | Program Stream | Employer | Address | Occupation (NOC 2021 code-title) | Incorporate Status | Approved LMIAs | Approved Positions
- Program streams present: High Wage (4092), Primary Agriculture (2265), Low Wage (2081), Global Talent Stream (316), Permanent Resident Only (36)
- Top provinces by rows: QC 3054, ON 2633, BC 1474, AB 903

Official caveats (from the dataset notes — repeat these to customers when relevant):
1. The list EXCLUDES employers with personal names (e.g. many caregivers), so it is NOT complete.
2. Employer names are manually entered — spelling can be inconsistent.
3. Approved LMIA positions ≠ workers who actually came. It tracks positions approved, not permits issued.
4. The two open.canada.ca links the project started from: one is the Job Bank postings dataset, the other is this LMIA list. English only for our products; French versions ignored.

### 2.2 Secondary source — Job Bank job postings (for live-verification phase)

- Official page: https://open.canada.ca/data/dataset/ea639e28-c0fc-48bf-b5dd-b8899bd43072
- Monthly CSV: all postings advertised on Job Bank (EN + FR). Latest at check: `job-bank-open-data-all-job-postings-en-sept2026.csv` (resource id `03523cbf-a005-40ee-81ad-aca5bb74cf03`, updated 2026-10-02).
- **WARNING: direct file downloads and the CKAN datastore API for this dataset are blocked by a WAF ("Request Rejected") for non-browser requests.** Workaround options for the verification phase: headless browser (agent-browser), or different request fingerprint. Do not waste time with plain curl.
- Note: the CKAN datastore API only exposes an older snapshot (Aug 2025 era) — do not trust it for freshness.

### 2.3 Why Job Bank matters (business logic)

- Employers applying for a TFWP LMIA must advertise the job on Job Bank (plus 2 other Canadian sources) around their application window.
- So: employer on the LMIA list + live Job Bank posting = strongest "hiring now" signal we can sell.
- Any employer can post on Job Bank (no LMIA needed to post) — a posting alone does NOT prove sponsorship. Never claim it does.

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

`Entry, Employer, JobTitle, NOC, City, ProvinceCode, Postal, Program Stream, Approved LMIAs, Approved Positions, Address`

### 3.3 Cardo Activity Score (verification phase — not started yet)

Every employer entry gets a status mark. Status text tags (no emojis in files):

- `ACTIVE`  — live posting found (Job Bank and/or employer's own careers page). Date-stamped: "verified DD-MM-YYYY".
- `WATCH`   — no live posting found today, but fresh/recent LMIA history → they hire again; keep on list. (A positive LMIA is typically valid ~6 months for the worker to apply — verify current rule when verification phase starts.)
- `REPEAT`  — high Approved Positions count / appears in multiple quarters → chronic labour-shortage employer. Flag and prioritize for verification.
- `OLD`     — LMIA older than ~1 year, nothing live. Keep on list (still info), marked OLD.

Rules: verification is done in batches, TOP hirers first. We verify what we can and stamp the date. We NEVER present WATCH as ACTIVE.

---

## 4. SECTOR DEFINITIONS

NOC 2021 (5-digit codes, from the Occupation column "NNNNN-Title").

### agriculture (BUILT — 2026-10-13)
- Rule: Program Stream == `Primary Agriculture` OR NOC in {80020, 82030, 84120, 85100, 85101, 85103, 21112}
- Result on 2026-Q1: **2,270 entries, 2,141 unique employers, 12 parts**
- Province spread: QC 1166, ON 500, BC 289, AB 146, SK 56, NS 44, MB 32, NB 19, PE 15, NL 3
- Top jobs: Harvesting labourers (1093), Livestock labourers (736), Agricultural service contractors and farm supervisors (164), Specialized livestock workers and farm machinery operators (131), Nursery and greenhouse labourers (129)

### food-processing (pre-tagged, sector not built)
- NOC 94141 (Industrial butchers and meat cutters, poultry preparers) found in other streams.

### fish-seafood (pre-tagged, sector not built)
- NOC 85102 (Aquaculture and marine harvest labourers).

### Planned sectors (rules to be defined the same way: stream OR NOC lists)
- construction, transport-trucking, healthcare-nursing, hospitality-food-service, manufacturing, retail-sales, cleaning-maintenance, and a SKILLED / UNSKILLED line (TEER-based).
- Rule of thumb for new sectors: inspect NOC value counts in `data/processed/tfwp_2026q1_clean.csv`, define NOC lists explicitly, never keyword-only.

---

## 5. REPO STRUCTURE & PIPELINE

```
cardo-careers/
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

---

## 8. CURRENT STATUS / NEXT STEPS

Done:
- Repo created, Bible written
- 2026-Q1 EN raw file stored + provenance documented
- Pipeline built (`scripts/build_sectors.py`)
- AGRICULTURE sector built: 2,270 entries → 12 parts + stats README

Next (in order):
1. Push repo to GitHub (waiting for owner's GitHub token / repo creation)
2. Define + build next sectors from the 6,505 unassigned rows (construction, transport, healthcare...)
3. Verification phase: Job Bank + employer sites via headless browser → Activity Score (top hirers first)
4. Product phase: PDF layout, CV templates, guides, cold emails, disclaimer pages
5. Business phase: Selar (or alternative) store, pricing page, marketing content plan

Standing rule for every future agent: update BIBLE.md (sections 4, 7, 8) after your work. Never break the info-not-promises rule.
