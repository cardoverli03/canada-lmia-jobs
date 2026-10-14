# DATA INTEGRITY — the clean-data audit

Audit date: **2026-10-14** (owner timezone Africa/Dar_es_Salaam)
Re-run any time: `python3 scripts/audit_data.py` — exit 0 = clean, exit 1 = broken.
No vibes. Every claim below is a script check or a count you can reproduce.

---

## 1. Audit scoreboard — 14/14 PASSED

| # | Check | Result |
|---|-------|--------|
| 1 | Source row integrity | 8,790 rows from ESDC 2026-Q1 file |
| 2 | TEER completeness | 0 rows missing TEER |
| 3 | SkillLevel completeness | 0 rows missing SKILLED/UNSKILLED |
| 4 | Duplicate rows | **0 identical rows**; 31 same-key rows are separate LMIA decisions under different Program Streams (kept — each is a distinct approval) |
| 5 | File inventory | 59 part files across 16 sectors |
| 6 | SKILLED/UNSKILLED purity | **0 mixed files** — every file is 100% one level |
| 7 | Filename ↔ content agreement | skilled files contain only SKILLED rows, unskilled only UNSKILLED |
| 8 | TEER ↔ level agreement | SKILLED = TEER 0-3, UNSKILLED = TEER 4-5 on every single row |
| 9 | Entry numbering | continuous 1..N per series, no gaps (part02 continues from part01) |
| 10 | JobBankCheck + WebSearch | present and well-formed on all 8,164 rows |
| 11 | Accounting | sectors 8,164 + longtail 626 = 8,790 source rows (92.9% allocated) |
| 12 | Zero invented rows | every sector row traces 1:1 to the ESDC source |
| 13 | Sector assignment integrity | no row sits in a sector it was not assigned to |
| 14 | Cross-sector duplicates | each employer+address+occupation lives in exactly one sector |

## 2. The real numbers

- **8,790** LMIA approval decisions (ESDC TFWP Positive LMIA list, **2026 Q1 = approvals issued Jan 1 – Mar 31, 2026**)
- **7,884** distinct employers · **33,216** approved positions · **10,832** approved LMIAs
- Streams: High Wage 4,092 · Primary Agriculture 2,265 · Low Wage 2,081 · Global Talent Stream 316 · PR-pathway 36
- **16 sectors · 59 files · 8,164 rows in-sector (5,338 SKILLED / 2,826 UNSKILLED) · 626 longtail documented** in `data/processed/unassigned_review.csv`
- Earlier logs said "5,847 SKILLED + 2,943 UNSKILLED" — that was computed from the full source INCLUDING the 626 un-allocated rows. The file-truth is 5,338 / 2,826 = 8,164. Corrected 2026-10-14.

## 3. What this data IS / what it is NOT (iron law)

**IS:**
- A map of every employer that **proved** it hires through the Temporary Foreign Worker Program by receiving positive LMIAs in Q1 2026 — with occupation, city, province, stream, positions approved.
- A repeat-hirer signal: 664 employers (8.4%) filed 2+ approvals **in a single quarter**; repeat filers hold 26% of all positions. TFWP hiring is cyclical — seasonal farms, hotels, trucking fleets re-apply every cycle.
- Self-verifying: every row carries `JobBankCheck` (pre-filled Job Bank employer search, newest first) and `WebSearch` links. A buyer confirms live status in 5 seconds without trusting us.

**IS NOT:**
- NOT a list of currently-valid approval letters (see §4).
- NOT a list of job vacancies. Approved positions ≠ open seats today.
- NOT a guarantee of sponsorship, hiring, or wages. We sell information and verification shortcuts. Never promises.

## 4. The 6-month question — answered honestly

Owner asked: *"the list is Jan–Mar — LMIA lasts 6 months — does that mean many approvals are expired?"*

**The math:**
1. A positive LMIA is valid for **6 months from the date of issuance**.
2. This list = approvals issued between Jan 1 and Mar 31, 2026.
3. 6 months from issuance ⇒ those approval letters expired between ~Jul 2026 and **Sep 30, 2026 at the latest**.
4. Audit date: Oct 14, 2026 ⇒ **100% of the individual approval letters on this list are now past their validity window.** Not "many" — all, by the calendar.

**Why the data is still clean and still valuable:**
- The ESDC list was never a vacancy list. Its value is that it identifies **employers with a recent, proven track record of running LMIA approvals** — the exact population that re-applies. There is no public "employers currently holding valid LMIAs" list. This is the closest public signal, and it is 6 months fresh (Q1 2026), which is the newest ESDC quarterly release.
- Repeat-filer behavior: 664 employers filed multiple approvals inside one quarter — farms, hotels, processors, trucking firms that run TFWP every season. They are structurally likely to be mid-cycle on new applications right now (Q3/Q4 2026 approvals are not yet published).
- **The live layer is what carries the truth, and it is dated AFTER the expiry window:**
  - Hunt: 191 top hirers checked **Oct 13–14, 2026** in their official hiring channels → **43 ACTIVE** (live careers pages, application forms, job boards today). Logged with evidence URLs in `data/hunt/`.
  - JobBankCheck on every row: a Job Bank posting can only exist if an employer is actively recruiting around an LMIA process; each posting displays its own **apply-by deadline**. This is how "deadline" questions get answered per-employer, live, not from a static list.
  - Job Bank Sept 2026 slim file (52,368 postings, `data/processed/job-bank-sept2026-slim.csv`) is kept as the market-signal layer (occupation demand by province/city), NOT as employer evidence — the open data contains no employer names.

**Product-copy rule that falls out of this (for the product chat, not here):**
- Never say "312 open jobs". Say "312 positions approved last quarter — hit the JobBankCheck link to see today's live postings and their deadlines".
- The 43 ACTIVE badges are dated. They are a snapshot of Oct 13–14, 2026, honestly labeled as such.

## 5. The deadline field — what exists and what doesn't

- The ESDC source columns are: Province/Territory, Program Stream, Employer, Address, Occupation, Incorporate Status, Approved LMIAs, Approved Positions. **No expiry date. No deadline. ESDC does not publish one.**
- Deadlines exist only per-posting on Job Bank (each live posting shows its own closing date) → surfaced through the JobBankCheck link on every row.
- Hunt logs carry `VerifiedDate` (when WE checked) — that is our data's own timestamp, not a deadline.

## 6. Hunt tally (16 batches, Oct 13–14 2026)

| Verdict | Count | Meaning |
|---|---|---|
| ACTIVE | **43** | live hiring channel verified, evidence URL logged |
| NO-SITE-FOUND | 85 | no sensible official site (incl. numbered companies) |
| BOT-WALLED | 37 | site up, gated by bot-protection (Cloudflare/Workday) |
| NO-PUBLIC-CHANNEL | 12 | site live, no public careers section |
| UNREACHABLE | 10 | site/network unreachable from this network |
| WRONG-SITE-LOOKALIKE | 4 | name-twin sites excluded (traps documented) |
| **Total checked** | **191** | top hirers by Approved Positions, biggest first |

## 7. Bugs found and fixed during this audit (we hunt our own data too)

1. Two hunt-log rows had column-shift corruption from pasted URLs (Amazon batch12, Trican batch04). Content was recoverable; rows rewritten and re-verified. Amazon = ACTIVE (43rd badge), Trican = NO-SITE-FOUND.
2. SKILLED/UNSKILLED totals in earlier docs (5,847/2,943) included the 626 un-allocated longtail rows. Corrected to file-truth 5,338/2,826.

**Bottom line: the filtering is verified clean. Every row is real, traceable, de-duplicated, level-pure, and self-verifying. The freshness story is honest: static list = Q1 2026 proof of TFWP activity; live truth = JobBankCheck links + 43 dated ACTIVE badges.**
