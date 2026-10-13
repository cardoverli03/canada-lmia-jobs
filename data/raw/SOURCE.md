# Source provenance — data/raw files

## tfwp_2026q1_pos_en.xlsx

- Dataset: Temporary Foreign Worker Program (TFWP): Positive Labour Market Impact Assessment (LMIA) Employers List
- Publisher: Employment and Social Development Canada (ESDC)
- Dataset page: https://open.canada.ca/data/dataset/90fed587-1364-4f33-a9ee-208181dc0b97
- Resource id: 4ee7a4e0-ffc3-47af-94e7-30929d1eeb67
- Resource URL: https://open.canada.ca/data/dataset/90fed587-1364-4f33-a9ee-208181dc0b97/resource/4ee7a4e0-ffc3-47af-94e7-30929d1eeb67/download/tfwp_2026q1_pos_en.xlsx
- Format: XLSX, English
- File last modified on source: 2026-07-21
- Downloaded: 2026-10-13 by Cardo Careers pipeline operator (sandbox fetch)
- SHA256: 2f48cb522180ff82e6768a68b679bed4d4c89efa28d1c5aca7bc1604c99a044e

Integrity: this file is stored exactly as downloaded. Never edit files in data/raw/.

## job-bank-open-data-all-job-postings-en-sept2026.csv — REMOVED FROM REPO (2026-10-13)

- Dataset: Job Postings Advertised on Canada's National Job Bank Website
- Publisher: Employment and Social Development Canada (ESDC)
- Dataset page: https://open.canada.ca/data/dataset/ea639e28-c0fc-48bf-b5dd-b8899bd43072
- Resource id: 03523cbf-a005-40ee-81ad-aca5bb74cf03
- Format: CSV (UTF-16, tab-separated), English
- File last modified on source: 2026-10-02
- Downloaded: 2026-10-13 via curl with full browser header fingerprint (plain curl is WAF-blocked with "Request Rejected")
- Contents verified: 52,368 postings, columns include NOC21 Code, First Posting Date, Vacancy Count, Province/Territory, City, Salary Min/Max
- IMPORTANT: contains NO employer name column (anonymized). Cannot be used for employer matching.
- **2026-10-13: the raw 46 MB file was deleted from the repo (local + git history + GitHub) on the owner's order. It is re-downloadable from the resource link above if ever needed. The derived market-signal file `data/processed/job-bank-sept2026-slim.csv` (7.2 MB) is kept. Do not commit raw Job Bank dumps again — see .gitignore rule.**

## noc-2021-v1.0-classification-structure.csv

- Source: Statistics Canada NOC 2021 Version 1.0 classification structure
- URL: https://www.statcan.gc.ca/en/subjects/standard/noc/2021/indexV1/noc-2021-v1.0-classification-structure.csv
- Downloaded: 2026-10-13. NOTE: does NOT contain TEER (hierarchy only). Kept for titles reference.

## ircc-noc2021-teer.csv

- Source: IRCC official page "Find your National Occupational Classification (NOC)" (canada.ca), full NOC 2021 unit-group TEER table
- Page: https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/eligibility/find-national-occupation-code.html
- Extracted: 2026-10-13 via headless browser (page is Akamai-tarpitted for curl; the raw HTML contains the full table as <tr><td>TEER</td><td>NOC</td><td>Title</td></tr>)
- Contents verified: 516 unit groups with TEER 0-5. This is the SkillLevel source (TEER 0-3 = SKILLED, TEER 4-5 = UNSKILLED).
