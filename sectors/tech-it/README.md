# TECH-IT - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **570** | Unique employers: **468**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 3 part(s)** (570 rows), **UNSKILLED: 0 part(s)** (0 rows) — max 200 rows per file
- Skill split: SKILLED 570 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 1029 postings, 1265 vacancies, median wage ~$40.07/hr equivalent
  - Postings by province: Ontario 524, Québec 260, British Columbia 121

## Files

**SKILLED** (TEER 0-3), 570 entries:

- `tech-it-skilled-part01.csv`
- `tech-it-skilled-part02.csv`
- `tech-it-skilled-part03.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| ON | 280 |
| QC | 172 |
| BC | 71 |
| AB | 27 |
| NS | 8 |
| MB | 5 |
| NB | 3 |
| SK | 2 |
| NT | 1 |
| NL | 1 |

## Top requested jobs

- Software developers and programmers: 119
- Software engineers and designers: 93
- Information systems specialists: 80
- Business system specialists: 48
- Computer and information systems managers: 35
- Web developers and programmers: 34
- Data scientists: 30
- Database analysts and data administrators: 30
- Computer network and web technicians: 24
- Cybersecurity specialists: 24

## Top repeat hirers (total approved positions)

- Groupe Technologies Desjardins inc.: 13
- Autodesk Canada Co.: 12
- CGI Information Systems & Management Consultants Inc.: 12
- Amazon Development Centre Canada ULC: 10
- COFOMO DÉVELOPPEMENT INC.: 10
- Loblaws Inc.: 9
- ALTEN Canada Inc.: 8
- Conseillers en gestion et informatique CGI Inc.: 8
- Ebates Canada, Inc.: 8
- ATI Technologies ULC: 8

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 12 hirers by approved positions (see `data/hunt/2026-10-14_tech-it_batch12.csv` for full evidence):

**ACTIVE — live hiring channels:**
- **Groupe Technologies Desjardins inc.** (13 pos) — https://www.desjardins.com/en/careers.html
- **Amazon Development Centre Canada ULC** (10 pos) — https://www.amazon.jobs/en/search?loc_query=Vancouver,+British+Columbia,+Canada
- **COFOMO DÉVELOPPEMENT INC.** (10 pos) — https://www.cofomo.com/en/careers/
- **Loblaws Inc.** (9 pos) — https://careers.loblaw.ca/
- **ATI Technologies ULC** (8 pos) — https://www.amd.com/careers
- **Electronic Arts (Canada), Inc.** (7 pos) — https://www.ea.com/careers
- **Fortinet Technologies (Canada) ULC** (7 pos) — https://www.fortinet.com/corporate/careers

**NO-PUBLIC-CHANNEL:** Ebates Canada, Inc. (8 pos)

**BOT-WALLED (site exists, challenge blocks us):** Autodesk Canada Co. (12)

**UNREACHABLE:** CGI Information Systems & Management Consultants Inc. (12); Conseillers en gestion et informatique CGI Inc. (8); ALTEN Canada Inc (0)

Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds.
