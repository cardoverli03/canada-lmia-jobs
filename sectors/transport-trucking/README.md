# TRANSPORT-TRUCKING - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **503** | Unique employers: **485**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 3 part(s)** (469 rows), **UNSKILLED: 1 part(s)** (34 rows) — max 200 rows per file
- Skill split: SKILLED 469, UNSKILLED 34 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 2949 postings, 6215 vacancies, median wage ~$31.35/hr equivalent
  - Postings by province: Ontario 791, Québec 773, British Columbia 424

## Files

**SKILLED** (TEER 0-3), 469 entries:

- `transport-trucking-skilled-part01.csv`
- `transport-trucking-skilled-part02.csv`
- `transport-trucking-skilled-part03.csv`

**UNSKILLED** (TEER 4-5), 34 entries:

- `transport-trucking-unskilled-part01.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| QC | 185 |
| ON | 130 |
| BC | 77 |
| AB | 55 |
| MB | 18 |
| NS | 14 |
| SK | 11 |
| NB | 7 |
| PE | 5 |
| NL | 1 |

## Top requested jobs

- Transport truck drivers: 207
- Automotive service technicians, truck and bus mechanics and mechanical repairers: 147
- Auto body collision, refinishing and glass technicians and damage repair estimators: 71
- Supervisors, motor transport and other ground transit operators: 43
- Material handlers: 31
- Dispatchers: 3
- Bus drivers, subway operators and other transit operators: 1

## Top repeat hirers (total approved positions)

- Lodex Transport Ltd.: 32
- 2264236 ONTARIO INC.: 20
- Aliments Nortera Inc.: 20
- Calmar Transport Inc: 16
- EVEREST TRANSPORTATION INC: 15
- HNM Logistics Inc.: 11
- Sysco Canada Inc.: 11
- Gpex Transport Inc: 10
- JS&MK Transport Ltd.: 10
- Highlight Motor Freight Inc.: 10

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 15 hirers by approved positions (see `data/hunt/2026-10-14_transport-trucking_batch04.csv` for full evidence):

- **ACTIVE — live hiring channels:**
  - Aliments Nortera (20 pos) — live board "65 positions" incl. LOGISTICS COORDINATOR Brossard QC (exact city match): https://jobs.norterafoods.com/en/careers/
  - Sysco Canada (11 pos) — careers.sysco.ca, 94 live results incl. AZ Delivery Driver Barrie + Transportation Supervisor: https://careers.sysco.ca/en/search-jobs
  - Gulzar Transport (10 pos) — live hiring page "Apply For Administrative Officer": https://gulzartransport.com/hiring/
  - Highlight Motor Freight (10 pos) — dedicated driver recruitment site, live application form, address "391 Creditstone Rd, Concord ON" = exact LMIA match: https://highlightmotorfreight.ca/en/driver-application-form.php
- **UNREACHABLE:** Lodex Transport (32 pos) — lodex.ca server-broken (500); lodex.com = Dubai consulting lookalike, excluded
- **BOT-WALLED:** AYR Motor Express (10 pos) — ayrmotor.com bot interstitial; ayr.com = fashion brand lookalike, excluded
- **WRONG-SITE-LOOKALIKE (excluded as evidence):** lodex.com (Dubai), ayr.com (clothing)
- **NO-PUBLIC-CHANNEL:** Calmar Transport (16 pos) — site live, no hiring page
- **NO-SITE-FOUND:** numbered companies (2264236 ON, 9591699 Canada), Everest Transportation + HNM Logistics + JS&MK (domains parked for sale), Hummer Freightways, Trican Transport, Gpex (Coming Soon placeholder)
- Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds
