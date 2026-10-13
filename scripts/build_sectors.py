#!/usr/bin/env python3
"""
Cardo Careers - sector filtering pipeline
=========================================
Input : data/raw/tfwp_2026q1_pos_en.xlsx  (ESDC TFWP Positive LMIA Employers List, EN)
Output: data/processed/tfwp_2026q1_clean.csv            (full cleaned dataset)
        sectors/agriculture/agriculture-partNN.csv      (max 200 rows per part)
        sectors/agriculture/README.md                   (live stats for this sector)

Rules (see BIBLE.md):
  - English only.
  - One row = one approved LMIA entry (employer + occupation + location).
  - Max 200 entries per file part. Parts sorted Province -> positions desc -> employer.
  - Sector AGRICULTURE = Program Stream "Primary Agriculture" OR NOC in AG_NOC.
    NOC 94141 (industrial butchers/poultry) -> future FOOD PROCESSING sector.
    NOC 85102 (aquaculture/marine harvest)  -> future FISH & SEAFOOD sector.
"""

import os
import re
import sys
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_FILE = os.path.join(REPO, "data", "raw", "tfwp_2026q1_pos_en.xlsx")
QUARTER = "2026-Q1"

PROVINCE_MAP = {
    "Alberta": "AB",
    "British Columbia": "BC",
    "Manitoba": "MB",
    "New Brunswick": "NB",
    "Newfoundland and Labrador": "NL",
    "Northwest Territories": "NT",
    "Nova Scotia": "NS",
    "Nunavut": "NU",
    "Ontario": "ON",
    "Prince Edward Island": "PE",
    "Quebec": "QC",
    "Saskatchewan": "SK",
    "Yukon": "YT",
    "Employers carrying on business in Canada with Head Office outside of Canada": "FOREIGN-HQ",
}

AG_NOC = {"80020", "82030", "84120", "85100", "85101", "85103", "21112"}
FOOD_PROCESSING_NOC = {"94141"}
FISH_SEAFOOD_NOC = {"85102"}

MAX_PART_ROWS = 200


def parse_city(addr):
    """'St. John's, NL A1B 1W3' -> 'St. John's'"""
    if not isinstance(addr, str):
        return ""
    addr = addr.strip()
    m = re.match(r"^(.*?),\s*[A-Z]{2}\s+[A-Z]\d[A-Z]\s*\d[A-Z]\d$", addr)
    if m and m.group(1).strip():
        return m.group(1).strip()
    return addr.split(",")[0].strip()


def parse_postal(addr):
    if not isinstance(addr, str):
        return ""
    m = re.search(r"([A-Z]\d[A-Z]\s*\d[A-Z]\d)\s*$", addr.strip())
    return m.group(1) if m else ""


def load_clean():
    df = pd.read_excel(RAW_FILE, skiprows=1)
    df.columns = [str(c).strip() for c in df.columns]
    # strip every string cell (source cells are space-padded to fixed width)
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].astype(str).str.strip().replace({"nan": ""})
    # drop footer note rows
    df = df[df["Province/Territory"].isin(PROVINCE_MAP.keys())].copy()
    df["NOC"] = df["Occupation"].str.extract(r"^(\d{5})")
    df["JobTitle"] = df["Occupation"].str.replace(r"^\d{5}-", "", regex=True).str.strip()
    df["City"] = df["Address"].apply(parse_city)
    df["Postal"] = df["Address"].apply(parse_postal)
    df["ProvinceCode"] = df["Province/Territory"].map(PROVINCE_MAP)
    for c in ("Approved LMIAs", "Approved Positions"):
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)
    before = len(df)
    df = df.drop_duplicates()
    deduped = before - len(df)
    return df, deduped


def tag_sectors(df):
    ag = df["Program Stream"].eq("Primary Agriculture") | df["NOC"].isin(AG_NOC)
    fp = df["NOC"].isin(FOOD_PROCESSING_NOC) & ~ag
    fs = df["NOC"].isin(FISH_SEAFOOD_NOC) & ~ag
    df["Sector"] = ""
    df.loc[ag, "Sector"] = "agriculture"
    df.loc[fp, "Sector"] = "food-processing"
    df.loc[fs, "Sector"] = "fish-seafood"
    return df


def export_sector(df, sector):
    out_dir = os.path.join(REPO, "sectors", sector)
    os.makedirs(out_dir, exist_ok=True)
    sub = df[df["Sector"] == sector].copy()
    sub = sub.sort_values(
        ["Province/Territory", "Approved Positions", "Employer"],
        ascending=[True, False, True],
        kind="mergesort",
    )
    sub = sub.reset_index(drop=True)

    cols = [
        "Entry",
        "Employer",
        "JobTitle",
        "NOC",
        "City",
        "ProvinceCode",
        "Postal",
        "Program Stream",
        "Approved LMIAs",
        "Approved Positions",
        "Address",
    ]
    sub["Entry"] = sub.index + 1

    n_parts = 0
    for start in range(0, len(sub), MAX_PART_ROWS):
        chunk = sub.iloc[start : start + MAX_PART_ROWS]
        n_parts += 1
        part_path = os.path.join(
            out_dir, f"{sector}-part{n_parts:02d}.csv"
        )
        chunk[cols].to_csv(part_path, index=False)

    # sector README with live stats
    prov_counts = sub["ProvinceCode"].value_counts()
    top_jobs = sub["JobTitle"].value_counts().head(10)
    unique_emp = sub["Employer"].nunique()
    repeat = sub.groupby("Employer")["Approved Positions"].sum().sort_values(ascending=False).head(10)

    lines = []
    lines.append(f"# {sector.upper()} - Cardo Careers sector data")
    lines.append("")
    lines.append(f"- Source: ESDC TFWP Positive LMIA Employers List, {QUARTER} (English)")
    lines.append(f"- Total entries: **{len(sub)}**")
    lines.append(f"- Unique employers: **{unique_emp}**")
    lines.append(f"- Parts: **{n_parts}** (max {MAX_PART_ROWS} entries each)")
    lines.append(f"- Sector rule: Program Stream == 'Primary Agriculture' OR NOC in {sorted(AG_NOC)}")
    lines.append("")
    lines.append("## Entries by province")
    lines.append("")
    lines.append("| Province | Entries |")
    lines.append("|----------|---------|")
    for p, c in prov_counts.items():
        lines.append(f"| {p} | {c} |")
    lines.append("")
    lines.append("## Top requested jobs")
    lines.append("")
    for j, c in top_jobs.items():
        lines.append(f"- {j}: {c}")
    lines.append("")
    lines.append("## Top repeat hirers (total approved positions, all entries)")
    lines.append("")
    for e, c in repeat.items():
        lines.append(f"- {e}: {c}")
    lines.append("")
    lines.append("Status column (ACTIVE / WATCH) is added during the verification phase.")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(sub), n_parts


def main():
    df, deduped = load_clean()
    df = tag_sectors(df)
    print(f"[load] rows kept: {len(df)} (dropped {deduped} exact duplicates + footer notes)")

    processed_path = os.path.join(REPO, "data", "processed", f"tfwp_{QUARTER.replace('-', '').lower()}_clean.csv")
    df.to_csv(processed_path, index=False)
    print(f"[save] {os.path.relpath(processed_path, REPO)}")

    print("\n=== sector counts ===")
    print(df["Sector"].replace("", "(unassigned)").value_counts().to_string())

    for sector in ("agriculture",):
        total, parts = export_sector(df, sector)
        print(f"\n[{sector}] entries: {total} -> {parts} part files")

    print("\nDone.")


if __name__ == "__main__":
    sys.exit(main())
