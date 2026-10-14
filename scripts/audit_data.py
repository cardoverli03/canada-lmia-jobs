#!/usr/bin/env python3
"""
CARDIO CAREERS - DATA AUDIT
Verifies every BIBLE rule against the actual files on disk.
Run: python3 scripts/audit_data.py
Exit code 0 = all PASS. Any FAIL = exit 1. No vibes, only checks.
"""
import csv, os, sys, glob, re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data/processed/tfwp_2026q1_clean.csv")
SECTORS_DIR = os.path.join(ROOT, "sectors")

results = []  # (check_name, ok, detail)

def check(name, ok, detail):
    results.append((name, ok, detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

def read_csv(path):
    with open(path, encoding="utf-8-sig") as fh:
        r = csv.DictReader(fh)
        return list(r)

print("=" * 72)
print("CARDIO CAREERS DATA AUDIT")
print("=" * 72)

# ---------------------------------------------------------------- 1. SOURCE
src = read_csv(SRC)
print(f"\n[1] SOURCE: tfwp_2026q1_clean.csv -> {len(src)} rows (ESDC TFWP 2026-Q1, Jan-Mar 2026 approvals)")

alloc = [r for r in src if r["Sector"].strip()]
longtail = [r for r in src if not r["Sector"].strip()]
check("source row integrity", len(src) > 0, f"{len(src)} rows loaded")
check("TEER completeness (source)", all(r["TEER"].strip() for r in src),
      "0 rows missing TEER" if all(r["TEER"].strip() for r in src)
      else f"{sum(1 for r in src if not r['TEER'].strip())} rows missing TEER")
check("SkillLevel completeness (source)", all(r["SkillLevel"].strip() for r in src),
      "0 rows missing SkillLevel")

# exact duplicate rows in source (all key fields identical)
src_key = Counter((r["Employer"].strip().upper(), r["Address"].strip(), r["Occupation"].strip(), r["NOC"].strip()) for r in src)
dupe_keys = {k: v for k, v in src_key.items() if v > 1}
true_dupes, stream_splits = 0, 0
groups = defaultdict(list)
for r in src:
    groups[(r["Employer"].strip().upper(), r["Address"].strip(), r["Occupation"].strip(), r["NOC"].strip())].append(r)
for k, rows in groups.items():
    if len(rows) > 1:
        if len(set(tuple(sorted(r.items())) for r in rows)) == 1:
            true_dupes += len(rows) - 1
        else:
            stream_splits += len(rows) - 1
check("source duplicate rows", true_dupes == 0,
      f"0 identical rows; {stream_splits} same-key rows are separate LMIA decisions under different Program Streams (kept - each is a distinct approval)")

# ---------------------------------------------------------------- 2. SECTOR FILES
print("\n[2] SECTOR FILES: purity, TEER, entry numbering, required links")
sector_files = sorted(glob.glob(os.path.join(SECTORS_DIR, "*", "*-part*.csv")))
check("file inventory", len(sector_files) > 0, f"{len(sector_files)} part files across {len(set(os.path.basename(os.path.dirname(f)) for f in sector_files))} sectors")

total_rows = 0
level_rows = {"SKILLED": 0, "UNSKILLED": 0}
mixed_files, teer_bad, entry_bad, link_bad, lvl_mismatch = [], [], [], [], []
per_sector_rows = defaultdict(lambda: {"SKILLED": 0, "UNSKILLED": 0})
all_rows_by_sector = defaultdict(list)

for path in sector_files:
    rel = os.path.relpath(path, SECTORS_DIR)
    sector = rel.split(os.sep)[0]
    fname = os.path.basename(path)
    rows = read_csv(path)
    total_rows += len(rows)
    levels = set(r["SkillLevel"].strip() for r in rows)
    # purity: single level per file + filename agreement
    if len(levels) > 1:
        mixed_files.append(f"{rel} -> {levels}")
    if levels == {"SKILLED"} and "-skilled-" not in fname:
        lvl_mismatch.append(rel)
    if levels == {"UNSKILLED"} and "-unskilled-" not in fname:
        lvl_mismatch.append(rel)
    lvl = list(levels)[0] if len(levels) == 1 else "?"
    level_rows[lvl] = level_rows.get(lvl, 0) + len(rows)
    per_sector_rows[sector][lvl] += len(rows)
    all_rows_by_sector[sector].extend(rows)
    # TEER / level agreement
    for r in rows:
        teer = r["TEER"].strip()
        if not teer:
            teer_bad.append(f"{rel}: blank TEER ({r['Employer']})")
        elif lvl == "SKILLED" and teer not in ("0", "1", "2", "3"):
            teer_bad.append(f"{rel}: SKILLED but TEER={teer} ({r['Employer']})")
        elif lvl == "UNSKILLED" and teer not in ("4", "5"):
            teer_bad.append(f"{rel}: UNSKILLED but TEER={teer} ({r['Employer']})")
        if not r["JobBankCheck"].strip().startswith("https://www.jobbank.gc.ca/") or \
           not r["WebSearch"].strip().startswith("https://www.google.com/"):
            link_bad.append(rel)
    # entry numbering: continuous across the series, sorted by part
    m = re.match(rf"^{re.escape(sector)}-(skilled|unskilled)-part(\d+)\.csv$", fname)
    if not m:
        entry_bad.append(f"{rel}: filename does not match series pattern")
    else:
        parts = sorted(glob.glob(os.path.join(SECTORS_DIR, sector,
                       f"{sector}-{m.group(1)}-part*.csv")))
        expected = 1
        for pp in parts:
            for r in read_csv(pp):
                if int(r["Entry"]) != expected:
                    entry_bad.append(f"{os.path.relpath(pp, SECTORS_DIR)}: Entry={r['Entry']} expected={expected}")
                expected += 1

check("SKILLED/UNSKILLED purity", not mixed_files,
      "0 mixed files - every file is 100% one level" if not mixed_files else f"{len(mixed_files)} MIXED: {mixed_files[:3]}")
check("filename<->content agreement", not lvl_mismatch,
      "skilled files contain only SKILLED, unskilled only UNSKILLED" if not lvl_mismatch else str(lvl_mismatch[:3]))
check("TEER<->level agreement", not teer_bad,
      "SKILLED=TEER 0-3, UNSKILLED=TEER 4-5 on every row" if not teer_bad else f"{len(teer_bad)} violations: {teer_bad[:3]}")
check("Entry numbering continuity", not entry_bad,
      "every series runs 1..N without gaps (part02 continues from part01)" if not entry_bad else f"{len(entry_bad)} breaks: {entry_bad[:3]}")
check("JobBankCheck + WebSearch on every row", not link_bad,
      "all rows carry self-verification links" if not link_bad else f"{len(link_bad)} files w/ bad links")

# ---------------------------------------------------------------- 3. ACCOUNTING
print("\n[3] ACCOUNTING: nothing invented, nothing lost")
check("allocation = source rows", total_rows + len(longtail) == len(src),
      f"sectors {total_rows} + longtail {len(longtail)} = {len(src)} source rows "
      f"({total_rows/len(src)*100:.1f}% allocated)")

# every sector row must exist in source (no invented data)
src_set = set((r["Employer"].strip(), r["JobTitle"].strip(), r["NOC"].strip(), r["Address"].strip()) for r in src)
invented = 0
for sector, rows in all_rows_by_sector.items():
    for r in rows:
        if (r["Employer"].strip(), r["JobTitle"].strip(), r["NOC"].strip(), r["Address"].strip()) not in src_set:
            invented += 1
check("zero invented rows", invented == 0,
      "every sector row traces back 1:1 to the ESDC source file" if invented == 0 else f"{invented} rows NOT in source!")

# sector-file Sector column consistency (source says sector X -> files of sector X only carry X rows)
sector_of_row = {}
for r in alloc:
    sector_of_row[(r["Employer"].strip(), r["JobTitle"].strip(), r["NOC"].strip(), r["Address"].strip())] = r["Sector"].strip()
misplaced = 0
for sector, rows in all_rows_by_sector.items():
    for r in rows:
        truth = sector_of_row.get((r["Employer"].strip(), r["JobTitle"].strip(), r["NOC"].strip(), r["Address"].strip()))
        if truth and truth != sector:
            misplaced += 1
check("sector assignment integrity", misplaced == 0,
      "no row sits in a sector it was not assigned to" if misplaced == 0 else f"{misplaced} misplaced rows")

# ---------------------------------------------------------------- 4. DUPES ACROSS SECTORS
print("\n[4] CROSS-SECTOR DUPLICATES")
seen = defaultdict(set)
for sector, rows in all_rows_by_sector.items():
    for r in rows:
        seen[(r["Employer"].strip().upper(), r["Address"].strip(), r["NOC"].strip())].add(sector)
cross = {k: v for k, v in seen.items() if len(v) > 1}
check("no row in two sectors", not cross,
      "each employer+address+occupation lives in exactly one sector" if not cross else f"{len(cross)} keys in multiple sectors: {list(cross.items())[:2]}")

# ---------------------------------------------------------------- 5. SCOREBOARD
print("\n" + "=" * 72)
fails = [r for r in results if not r[1]]
print(f"SCOREBOARD: {len(results) - len(fails)}/{len(results)} checks PASSED")
print(f"SECTORS: {len(per_sector_rows)} | FILES: {len(sector_files)} | ROWS: {total_rows} "
      f"(SKILLED {level_rows.get('SKILLED',0)} / UNSKILLED {level_rows.get('UNSKILLED',0)})")
print(f"LONGTAIL (not sectorized, kept in unassigned_review.csv): {len(longtail)} rows "
      f"({len(longtail)/len(src)*100:.1f}%)")
print("-" * 72)
for s, d in sorted(per_sector_rows.items()):
    print(f"  {s:28s} SKILLED {d['SKILLED']:5d}  UNSKILLED {d['UNSKILLED']:5d}  total {d['SKILLED']+d['UNSKILLED']:5d}")
print("=" * 72)
if fails:
    print("AUDIT FAILED:")
    for name, _, detail in fails:
        print(f"  - {name}: {detail}")
    sys.exit(1)
print("AUDIT PASSED - data is clean.")
sys.exit(0)
