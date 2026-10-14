# AGRICULTURE - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **2270** | Unique employers: **2141**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 1 part(s)** (181 rows), **UNSKILLED: 11 part(s)** (2089 rows) — max 200 rows per file
- Skill split: UNSKILLED 2089, SKILLED 181 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 2115 postings, 17999 vacancies, median wage ~$17.95/hr equivalent
  - Postings by province: Québec 833, Ontario 546, British Columbia 399

## Files

**SKILLED** (TEER 0-3), 181 entries:

- `agriculture-skilled-part01.csv`

**UNSKILLED** (TEER 4-5), 2089 entries:

- `agriculture-unskilled-part01.csv`
- `agriculture-unskilled-part02.csv`
- `agriculture-unskilled-part03.csv`
- `agriculture-unskilled-part04.csv`
- `agriculture-unskilled-part05.csv`
- `agriculture-unskilled-part06.csv`
- `agriculture-unskilled-part07.csv`
- `agriculture-unskilled-part08.csv`
- `agriculture-unskilled-part09.csv`
- `agriculture-unskilled-part10.csv`
- `agriculture-unskilled-part11.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| QC | 1166 |
| ON | 500 |
| BC | 289 |
| AB | 146 |
| SK | 56 |
| NS | 44 |
| MB | 32 |
| NB | 19 |
| PE | 15 |
| NL | 3 |

## Top requested jobs

- Harvesting labourers: 1093
- Livestock labourers: 736
- Agricultural service contractors and farm supervisors: 164
- Specialized livestock workers and farm machinery operators: 131
- Nursery and greenhouse labourers: 129
- Managers in agriculture: 8
- Contractors and supervisors, landscaping, grounds maintenance and horticulture services: 6
- Agricultural representatives, consultants and specialists: 2
- Managers in horticulture: 1

## Top repeat hirers (total approved positions)

- Jealous Fruits Ltd.: 760
- Les Entreprises Pitre Inc.: 212
- Fraisebec Inc.: 190
- Ferme Onésime Pouliot: 166
- RGR Guinois inc.: 165
- Caledon Produce Farms Ltd.: 162
- Goodyear Farm Ltd: 148
- Monette Farms Ltd.: 144
- Oso Berry Farms Inc.: 141
- Highline Produce Limited: 130

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt) — batch 01, done 2026-10-13

Top 18 hirers hunted via their official websites (Job Bank cross-check pending —
jobbank.gc.ca tarpitted our sandbox IP on hunt day; method in `docs/HUNT-METHOD.md`,
full evidence in `data/hunt/2026-10-13_agriculture_batch01.csv`).

- **ACTIVE (3):** Fraisebec Inc. (emplois page: 200+ hires per harvest season, May-Oct,
  interpreter-for-foreign-workforce roles, application form + phone + email),
  Monette Farms Ltd. (live careers page, resume-upload application form, international
  seasonal team 9 months-2 years), Les Jardins Vegibec Inc. (English careers page with
  apply-now form).
- Official site verified live, no public hiring channel (3): Jealous Fruits, Ferme Onésime
  Pouliot (site documents foreign-worker housing), Caledon Produce Farms.
- No verifiable official site found (9): Pitre, RGR Guinois, Goodyear Farm (a same-name
  California nursery exists — NOT the employer), Oso Berry, Procyk, El Dorado,
  2104052 Alberta Ltd (numbered company), Verger Thomson, Nutrableu.
- Site exists but bot-walled (2): Fraisière Faucher (Cloudflare), Highline Mushrooms
  West (Cloudflare). Unreachable from our network (1): Highline Produce.

Status column (ACTIVE / WATCH / REPEAT / OLD) is folded into part files before the
product phase. ACTIVE above = live application channel verified on the stated date,
NOT a guarantee of current openings — full disclaimer in BIBLE.md section 6.
