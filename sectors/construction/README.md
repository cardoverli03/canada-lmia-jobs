# CONSTRUCTION - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **1133** | Unique employers: **1069** | Parts: **6** (max 200 each)
- Skill split: SKILLED 1028, UNSKILLED 105 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 4654 postings, 8348 vacancies, median wage ~$34.45/hr equivalent
  - Postings by province: Ontario 1163, British Columbia 1093, Alberta 861

## Entries by province

| Province | Entries |
|----------|---------|
| ON | 372 |
| QC | 285 |
| BC | 245 |
| AB | 167 |
| NS | 15 |
| MB | 15 |
| SK | 12 |
| NB | 8 |
| FOREIGN-HQ | 6 |
| PE | 4 |
| NT | 3 |
| NL | 1 |

## Top requested jobs

- Carpenters: 162
- Welders and related machine operators: 156
- Construction trades helpers and labourers: 99
- Heavy-duty equipment mechanics: 91
- Residential and commercial installers and servicers: 65
- Construction millwrights and industrial mechanics: 65
- Plasterers, drywall installers and finishers and lathers: 58
- Contractors and supervisors, other construction trades, installers, repairers and servicers: 56
- Concrete finishers: 54
- Painters and decorators (except interior decorators): 49

## Top repeat hirers (total approved positions)

- Pioneer Construction Inc.: 25
- EVR Operations Limited: 25
- Contour Earthmoving Ltd: 22
- Rulam Contracting Ltd.: 21
- Rafat General Contractor Inc.: 20
- Dynamic Concrete Pumping Inc.: 20
- United Roofing Inc.: 17
- Lanco Aménagement inc.: 16
- CLASSIC LANDSCAPES LIMITED: 14
- PR Pomeroy Restoration & Construction (BC) Inc,: 14

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 15 hirers by approved positions (see `data/hunt/2026-10-14_construction_batch03.csv` for full evidence):

- **ACTIVE — live hiring channels:**
  - Contour Earthmoving (22 pos) — application form listing 7 open operator roles (Excavator/Dozer/Rock Truck/Packer/Heavy Haul/Pilot Truck/Fuel-Lube): https://www.contourearthmoving.com/careers.html
  - Rulam Contracting (21 pos) — live careers form; page privacy notice states Acheson AB address = exact LMIA match: https://rulam.ca/Careers
  - Rafat General Contractor (20 pos) — "currently accepting resumes for all positions": https://rafat.ca/careers/
  - Classic Landscapes (14 pos) — live resume form, Edmonton identity confirmed: https://classiclandscapes.com/about-us
- **UNREACHABLE:** EVR Operations (25 pos) — evr.ca live (Elk Valley Resources, Glencore; 25x Heavy-duty equipment mechanics = occupation match) but careers portal careers.glencore.com unresolvable from our network
- **BOT-WALLED:** Pioneer Construction (25), United Roofing (17), Lanco Aménagement (16), Bosa Construction (12) — sites exist behind Cloudflare/client challenges
- **WRONG-SITE-LOOKALIKE (excluded as evidence):** carmacks.ca = Village of Carmacks YUKON (municipality); cemrock.com = Cemrock Landscapes TUCSON AZ
- **NO-PUBLIC-CHANNEL:** Dynamic Concrete Pumping (20 pos) — site live, no public hiring page
- **NO-SITE-FOUND:** PR Pomeroy (14), Optimal Structural Formwork (13), Brunco Insulation (12, domain for sale)
- Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds
