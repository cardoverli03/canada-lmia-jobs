# HOSPITALITY-FOOD-SERVICE - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **1239** | Unique employers: **1146**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 6 part(s)** (1132 rows), **UNSKILLED: 1 part(s)** (107 rows) — max 200 rows per file
- Skill split: SKILLED 1132, UNSKILLED 107 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 8150 postings, 12743 vacancies, median wage ~$20.15/hr equivalent
  - Postings by province: Ontario 2056, British Columbia 2040, Québec 1195

## Files

**SKILLED** (TEER 0-3), 1132 entries:

- `hospitality-food-service-skilled-part01.csv`
- `hospitality-food-service-skilled-part02.csv`
- `hospitality-food-service-skilled-part03.csv`
- `hospitality-food-service-skilled-part04.csv`
- `hospitality-food-service-skilled-part05.csv`
- `hospitality-food-service-skilled-part06.csv`

**UNSKILLED** (TEER 4-5), 107 entries:

- `hospitality-food-service-unskilled-part01.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| ON | 369 |
| BC | 297 |
| QC | 250 |
| AB | 179 |
| SK | 49 |
| NS | 33 |
| NB | 30 |
| MB | 13 |
| PE | 7 |
| NL | 5 |
| FOREIGN-HQ | 3 |
| NT | 2 |
| YT | 2 |

## Top requested jobs

- Cooks: 353
- Restaurant and food service managers: 295
- Food service supervisors: 235
- Chefs: 111
- Food counter attendants, kitchen helpers and related support occupations: 87
- Bakers: 56
- Butchers - retail and wholesale: 45
- Accommodation service managers: 22
- Accommodation, travel, tourism and related services supervisors: 15
- Hotel front desk clerks: 11

## Top repeat hirers (total approved positions)

- Totem Lodge Ltd: 34
- The Butcher Shoppe: 30
- North American Midway Entertainment-Canada Co.: 30
- ClubLink Corporation ULC: 26
- Cargill Ltd.: 22
- Cargill Meat Solutions, Guelph: 20
- 7043821 Canada Inc.: 19
- R & J Concessions INC: 15
- SAUJANI ENTERPRISES Inc: 12
- M.G.B. Ventures Inc: 11

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 15 hirers by approved positions (see `data/hunt/2026-10-14_hospitality-food-service_batch02.csv` for full evidence):

- **ACTIVE — live hiring channels:**
  - North American Midway Entertainment (30 pos) — online employment application form: https://www.namidway.com/careers
  - ClubLink Corporation (26 pos) — live job board with openings (Food & Beverage Manager roles posted): https://clublink.ca/about/employment/opportunities/
  - Empress Hotel Operations Corp / Fairmont Empress Victoria (11 pos) — dated posting "Journey Person Cook (Full-time)" with Apply link: https://careers.accor.com/global/en/jobs?q=Empress_Victoria
- **NO-PUBLIC-CHANNEL:** The South Shore Fish Shack (10 pos) — official site live, identity confirmed, no public hiring page
- **BOT-WALLED:** Totem Lodge (34, Cloudflare), Cargill Ltd. + Cargill Meat Solutions Guelph (42 combined, Akamai) — sites exist, retry from another network
- **WRONG-SITE-LOOKALIKE (excluded as evidence):** rjconcessions.com is a Sarasota FL company, not the Winnipeg MB employer
- **NO-SITE-FOUND:** The Butcher Shoppe (two US same-name sites excluded), numbered/opaque employers (7043821 Canada, 0859319 BC Ltd, M.G.B. Ventures, Saujani, S&T Allard, Ford Concessions)
- Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds
