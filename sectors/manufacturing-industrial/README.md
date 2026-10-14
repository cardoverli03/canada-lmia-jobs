# MANUFACTURING-INDUSTRIAL - Cardo Careers sector data

- Source: ESDC TFWP Positive LMIA Employers List, 2026-Q1 (English)
- Total entries: **527** | Unique employers: **491**
- Files (SKILLED and UNSKILLED are separate, never mixed): **SKILLED: 3 part(s)** (433 rows), **UNSKILLED: 1 part(s)** (94 rows) — max 200 rows per file
- Skill split: SKILLED 433, UNSKILLED 94 (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)
- Live market signal (Job Bank, September 2026): 1874 postings, 3054 vacancies, median wage ~$29.5/hr equivalent
  - Postings by province: Québec 745, Ontario 584, British Columbia 212

## Files

**SKILLED** (TEER 0-3), 433 entries:

- `manufacturing-industrial-skilled-part01.csv`
- `manufacturing-industrial-skilled-part02.csv`
- `manufacturing-industrial-skilled-part03.csv`

**UNSKILLED** (TEER 4-5), 94 entries:

- `manufacturing-industrial-unskilled-part01.csv`

## Entries by province

| Province | Entries |
|----------|---------|
| QC | 277 |
| ON | 164 |
| BC | 39 |
| AB | 26 |
| FOREIGN-HQ | 15 |
| SK | 2 |
| NB | 2 |
| MB | 1 |
| NS | 1 |

## Top requested jobs

- Machinists and machining and tooling inspectors: 102
- Electrical mechanics: 44
- Electrical and electronics engineering technologists and technicians: 37
- Mechanical engineering technologists and technicians: 32
- Industrial engineering and manufacturing technologists and technicians: 25
- Electrical and electronics engineers: 23
- Cabinetmakers: 23
- Mechanical engineers: 21
- Drafting technologists and technicians: 20
- Chemical technologists and technicians: 18

## Top repeat hirers (total approved positions)

- LES PRODUITS PBM LTEE: 24
- Produits forestiers Résolu: 11
- Ice River Springs Water Co. Inc.: 11
- La Charpenterie inc.: 11
- Ontario Shipyards Inc.: 10
- Cascades Canada ULC: 10
- Maibec inc.: 9
- Paraza Pharma Inc.: 8
- Les Équipements de ferme Raymond E Laliberté Inc.: 8
- Usinage CNC Production inc.: 6

## Check it yourself (built into every part file)

Every row carries two ready-made links: JobBankCheck (opens Job Bank pre-filled with a quoted search for that employer, newest first) and WebSearch (finds the employer's official site / careers page). Click, look, decide. An approved LMIA is NOT a promise of a current opening - the links are how you check the live situation in seconds.

## Verification (the hunt)

Verified 2026-10-14 — top 12 hirers by approved positions (see `data/hunt/2026-10-14_manufacturing-industrial_batch05.csv` for full evidence):

**ACTIVE — live hiring channels:**
- **LES PRODUITS PBM LTEE** (24 pos) — https://produitspbm.com/carrieres/
- **La Charpenterie inc.** (11 pos) — https://www.lacharpenterieinc.com/postuler
- **Atlas Molded Products of Canada ULC** (6 pos) — https://recruiting.adp.com/srccar/public/RTI.home?c=1173015&d=ExternalCareerSite
- **Ontario Shipyards Inc.** (10 pos) — https://www.onshipyards.com

**BOT-WALLED (site exists, challenge blocks us):** Cascades Canada ULC (10); Maibec inc. (9); Les Fibres Futures (6); Produits American Biltrite Ltée (6); Ice River Springs Water Co. Inc. (11)

**NO-SITE-FOUND:** Produits forestiers Résolu (11); Les Équipements de ferme Raymond E Laliberté Inc. (8); KI Canada Corporation (6)

Job Bank cross-check still blocked from our network (tarpit) — every row's `JobBankCheck` link does this check from YOUR device in seconds.
