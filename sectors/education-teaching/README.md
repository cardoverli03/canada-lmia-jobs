# EDUCATION-TEACHING - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **86** | Unique employers: **82**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 1 part(s)** (86 rows), **UNSKILLED: 0 part(s)** (0 rows) — max 200 rows per file
- Skill split: SKILLED 86 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 809 postings, 1170 vacancies, median wage ~$26.8/hr equivalent
  - Postings by province: Ontario 376, Québec 184, British Columbia 117

## Files

**SKILLED** (TEER 0-3), 86 entries:

- `education-teaching-skilled-part01.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| QC | 34 |
| BC | 21 |
| ON | 13 |
| AB | 8 |
| MB | 5 |
| SK | 3 |
| NB | 1 |
| YT | 1 |

## Top requested jobs

- Early childhood educators and assistants: 48
- University professors and lecturers: 20
- Secondary school teachers: 10
- Elementary school and kindergarten teachers: 8

## Top repeat hirers (total approved positions)

- University of British Columbia, Faculty Relations: 14
- Université Concordia: 9
- Northern Lights School Division No. 113: 8
- Garden Hill Education Authority: 7
- Royal Institute for the Advancement of Learning: 7
- University of Toronto: 6
- CORPORATION DE L'ECOLE DES HAUTES ETUDES COMMERCIALES DE MONTREAL: 6
- University of Alberta: 5
- Next Level Childcare Fraser Valley Inc.: 5
- University of Calgary: 5

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 12 hirers by approved positions (see `data/hunt/2026-10-14_education-teaching_batch13.csv` for full evidence):

**ACTIVE — live hiring channels:**
- **Université Concordia** (9 pos) — https://www.concordia.ca/hr/jobs.html
- **Royal Institute for the Advancement of Learning** (7 pos) — https://www.mcgill.ca/careers
- **University of Manitoba** (4 pos) — https://umanitoba.ca/careers

**NO-PUBLIC-CHANNEL:** CORPORATION DE L'ECOLE DES HAUTES ETUDES COMMERCIALES DE MONTREAL (6 pos)

**BOT-WALLED (site exists, challenge blocks us):** Northern Lights School Division No. 113 (8); University of Alberta (5); University of Calgary (5)

**UNREACHABLE:** University of British Columbia, Faculty Relations (14); University of Toronto (6)

**WRONG-SITE-LOOKALIKE (excluded as evidence):** Next Level Childcare Fraser Valley Inc.

**NO-SITE-FOUND:** Garden Hill Education Authority (7); Centre de services scolaire de la Pointe-de-l’île (4)

Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds.
