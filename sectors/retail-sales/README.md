# RETAIL-SALES - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **295** | Unique employers: **289**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 2 part(s)** (278 rows), **UNSKILLED: 1 part(s)** (17 rows) — max 200 rows per file
- Skill split: SKILLED 278, UNSKILLED 17 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 1369 postings, 1536 vacancies, median wage ~$27.01/hr equivalent
  - Postings by province: Ontario 388, British Columbia 294, Québec 239

## Files

**SKILLED** (TEER 0-3), 278 entries:

- `retail-sales-skilled-part01.csv`
- `retail-sales-skilled-part02.csv`

**UNSKILLED** (TEER 4-5), 17 entries:

- `retail-sales-unskilled-part01.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| ON | 88 |
| BC | 74 |
| AB | 69 |
| QC | 35 |
| MB | 11 |
| SK | 8 |
| NB | 3 |
| NS | 3 |
| PE | 2 |
| FOREIGN-HQ | 1 |
| NT | 1 |

## Top requested jobs

- Retail and wholesale trade managers: 139
- Retail sales supervisors: 103
- Technical sales specialists - wholesale trade: 25
- Cashiers: 13
- Retail and wholesale buyers: 11
- Retail salespersons and visual merchandisers: 4

## Top repeat hirers (total approved positions)

- DARS Brothers Ltd: 6
- H.A.L.T. HOLDINGS LTD: 6
- JPT Gamble Enterprises Ltd.: 5
- Lovely Imports and Retails Ltd: 5
- PRAKM Ventures Ltd.: 5
- 2857-4077 Québec Inc.: 5
- Two Bay Enterprizes Limited: 5
- AMPVIC Development  Inc.: 4
- Spokes Bicycle Rentals & Espresso Bar Inc: 2
- 7027622 Manitoba Inc: 2

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 8 hirers by approved positions (see `data/hunt/2026-10-14_retail-sales_batch11.csv` for full evidence):

**BOT-WALLED (site exists, challenge blocks us):** DARS Brothers Ltd (6)

**NO-SITE-FOUND:** JPT Gamble Enterprises Ltd. (5); 2857-4077 Québec Inc. (5); PRAKM Ventures Ltd. (5); H.A.L.T. HOLDINGS LTD (6); Lovely Imports and Retails Ltd (5); Two Bay Enterprizes Limited (5); AMPVIC Development  Inc. (4)

Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds.
