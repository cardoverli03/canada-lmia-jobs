# REPAIR-MAINTENANCE - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **79** | Unique employers: **79**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 1 part(s)** (66 rows), **UNSKILLED: 1 part(s)** (13 rows) — max 200 rows per file
- Skill split: SKILLED 66, UNSKILLED 13 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 612 postings, 782 vacancies, median wage ~$25.26/hr equivalent
  - Postings by province: Québec 192, Ontario 149, British Columbia 85

## Files

**SKILLED** (TEER 0-3), 66 entries:

- `repair-maintenance-skilled-part01.csv`

**UNSKILLED** (TEER 4-5), 13 entries:

- `repair-maintenance-unskilled-part01.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| ON | 31 |
| QC | 27 |
| AB | 7 |
| BC | 6 |
| NB | 3 |
| MB | 3 |
| FOREIGN-HQ | 1 |
| NL | 1 |

## Top requested jobs

- General building maintenance workers and building superintendents: 24
- Contractors and supervisors, mechanic trades: 19
- Automotive and heavy truck and equipment parts installers and servicers: 13
- Electronic service technicians (household and business equipment): 8
- Motorcycle, all-terrain vehicle and other related mechanics: 8
- Aircraft mechanics and aircraft inspectors: 7

## Top repeat hirers (total approved positions)

- PNEUS D.M.R. INC.: 8
- Eagle Copters Maintenance Ltd.: 8
- Powell Fabrication & Mfg. LLC: 4
- M1 Composites Technologie: 4
- Baie Ste Anne Seafoods (2014) Inc.: 3
- Totem Lodge Ltd: 3
- 1001092142 Ontario Limited: 2
- 2810411 Ontario Inc.: 2
- Actfast Restoration & Repairs LTD.: 2
- 2070800 Ontario Ltd.: 2

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 7 hirers by approved positions (see `data/hunt/2026-10-14_repair-maintenance_batch16.csv` for full evidence):

**ACTIVE — live hiring channels:**
- **PNEUS D.M.R. INC.** (8 pos) — https://www.pneusdmr.ca/offre-d-emploi

**BOT-WALLED (site exists, challenge blocks us):** Eagle Copters Maintenance Ltd. (8); Totem Lodge Ltd (3)

**NO-SITE-FOUND:** Powell Fabrication & Mfg. LLC (4); M1 Composites Technologie (4); 9079-2151 Québec inc. (2); Baie Ste Anne Seafoods (2014) Inc. (3)

Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds.
