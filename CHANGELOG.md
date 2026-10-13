# Changelog — Cardo Careers

All notable changes to this repo. Dates use YYYY-MM-DD (owner timezone: Africa/Dar_es_Salaam).

## 2026-10-13

- Project initialized: repo skeleton, BIBLE.md, README.md, provenance docs.
- Stored raw source file `data/raw/tfwp_2026q1_pos_en.xlsx` (ESDC TFWP Positive LMIA Employers List, 2026 Q1, English, 8,790 clean data rows verified).
- Built pipeline `scripts/build_sectors.py`: raw XLSX -> cleaned CSV -> sector part files (max 200 rows per part).
- Built sector AGRICULTURE: 2,270 entries, 2,141 unique employers, 12 parts, per-province and top-jobs stats in `sectors/agriculture/README.md`.
- Pre-tagged future sectors found in data: food-processing (13 rows, NOC 94141), fish-seafood (2 rows, NOC 85102). 6,505 rows unassigned for upcoming sectors.
- Verified: CKAN package API works for metadata; Job Bank dataset file downloads and datastore API are WAF-blocked for non-browser clients (use headless browser in verification phase).
