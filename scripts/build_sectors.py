#!/usr/bin/env python3
"""
Cardo Careers - sector filtering pipeline v4
============================================
Input : data/raw/tfwp_2026q1_pos_en.xlsx      (ESDC TFWP Positive LMIA Employers List, EN)
        data/raw/ircc-noc2021-teer.csv        (IRCC official NOC 2021 -> TEER table, 516 codes)
        data/raw/job-bank-open-data-all-job-postings-en-sept2026.csv  (Job Bank Sept 2026, UTF-16 TSV)
Output: data/processed/tfwp_2026q1_clean.csv  (full cleaned dataset, sector + TEER + SkillLevel tagged)
        data/processed/job-bank-sept2026-slim.csv
        data/processed/unassigned_review.csv  (leftovers to inspect)
        sectors/<name>/<name>-skilled-partNN.csv    (TEER 0-3, max 200 rows per part)
        sectors/<name>/<name>-unskilled-partNN.csv  (TEER 4-5, max 200 rows per part)
        sectors/<name>/README.md              (live stats: provinces, jobs, hirers, market signal)

Rules (see BIBLE.md):
  - English only. One row = one approved LMIA entry (employer + occupation + location).
  - Max 200 entries per part. Parts sorted Province -> positions desc -> employer.
  - SkillLevel: TEER 0-3 = SKILLED, TEER 4-5 = UNSKILLED (source: IRCC official table).
  - SKILLED and UNSKILLED ship as SEPARATE file series inside each sector folder
    (owner decision 2026-10-14: buyers shop by skill level; never mixed in one file).
  - Sector = NOC list match first, keyword fallback second. Leftovers stay unassigned.
"""

import os
import re
import sys
from urllib.parse import quote

import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_LMIA = os.path.join(REPO, "data", "raw", "tfwp_2026q1_pos_en.xlsx")
RAW_TEER = os.path.join(REPO, "data", "raw", "ircc-noc2021-teer.csv")
RAW_JB = os.path.join(REPO, "data", "raw", "job-bank-open-data-all-job-postings-en-sept2026.csv")
JB_SLIM_OUT = os.path.join(REPO, "data", "processed", "job-bank-sept2026-slim.csv")
QUARTER = "2026-Q1"
JB_MONTH = "September 2026"

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

# Sector definitions: NOC list match first, then keyword fallback (on lowercase JobTitle)
SECTOR_DEFS = {
    "agriculture": {
        "noc": AG_NOC,
        "kw": [r"farm", r"harvest", r"livestock", r"nursery", r"greenhouse", r"agricult"],
        "stream": "Primary Agriculture",
    },
    "fish-seafood": {
        "noc": {"85102", "94142"},
        "kw": [r"fish", r"seafood", r"aquaculture"],
    },
    "food-processing": {
        "noc": {"94141", "95106", "92012"},
        "kw": [r"food and beverage processing", r"food processing", r"meat plant", r"poultry plant", r"food plant"],
    },
    "healthcare-nursing": {
        "noc": {"31100","31101","31102","31110","31111","31112","31200","31201","31202","31203",
                "31300","31301","31302","32101","32102","32103","32104","32110","32111","32112",
                "32120","32121","32200","32201","32202","33100","33101","33102","33103","33109",
                "44101"},
        "kw": [r"nurse", r"physician", r"doctor", r"dentist", r"dental", r"pharmac", r"physiother",
               r"medical", r"paramedic", r"health", r"therapist", r"care aide", r"patient", r"midwife",
               r"home support", r"caregiver"],
    },
    "construction": {
        "noc": {"70010","72014","72106","72310","72400","72401","73100","73102","73110","73112",
                "73200","73400","75110",
                "72300","72200","72301","72402","73113","72013","72021"},
        "kw": [r"construction", r"carpenter", r"roofer", r"drywall", r"plasterer", r"concrete",
               r"bricklayer", r"tilesetter", r"glazier", r"ironworker", r"insulator", r"crane oper",
               r"plumber", r"electrician", r"steamfitter", r"pipefitter", r"sprinkler",
               r"heating, refrigeration", r"floor covering"],
    },
    "transport-trucking": {
        "noc": {"73300","73301","72024","75101","72410","72411"},
        "kw": [r"truck driver", r"bus driver", r"transit driver", r"courier", r"delivery driver",
               r"material handler", r"shipping", r"forklift", r"dispatcher", r"chauffeur", r"taxi"],
    },
    "hospitality-food-service": {
        "noc": {"60030","62020","62200","63200","63201","63202","65201","64300","64302","64314",
                "60031","62022"},
        "kw": [r"cook", r"chef", r"kitchen", r"bartender", r"barista", r"baker", r"food counter",
               r"food service", r"food and beverage", r"dishwash", r"restaurant", r"hotel front desk",
               r"accommodation", r"hotel", r"tourism"],
    },
    "cleaning-landscaping": {
        "noc": {"65310","62024","85121"},
        "kw": [r"cleaner", r"cleaning", r"janitor", r"housekeep", r"landscap", r"grounds maintenance", r"gardener"],
    },
    "retail-sales": {
        "noc": {"60020","62010","62100"},
        "kw": [r"retail", r"sales associate", r"salesperson", r"cashier", r"store clerk", r"merchandis"],
    },
    "tech-it": {
        "noc": {"20012","21211","21221","21222","21223","21231","21232","21234","22221","22220"},
        "kw": [r"software", r"developer", r"programmer", r"data scien", r"database",
               r"information system", r"cyber", r"web developer", r"systems analyst", r"devops",
               r"user support", r"computer network"],
    },
    "office-admin": {
        "noc": {"13100","13110","12200","12013","14100","14111","12101"},
        "kw": [r"administrative", r"receptionist", r"bookkeep", r"accounting technician",
               r"data entry", r"office clerk", r"secretary", r"records management"],
    },
    # --- sectors v1.5 (2026-10-13, built from the 1,807-row long tail; all NOC
    # codes taken from the official data rows themselves, titles verified in-data) ---
    "manufacturing-industrial": {
        "noc": {"72100","72101","72102","72104","72311","72201","72422","72010",
                "21310","21301","21321","22310","22301","22302","22312","22212","22100",
                "94105","94106","94111","94124","94204","94212","95101","95104","95109",
                "92013","90010"},
        "kw": [r"machinist", r"machine operator", r"assembler", r"metal fabricat", r"plastic",
               r"rubber", r"manufactur", r"woodworking", r"tool and die", r"industrial electrician",
               r"electrical mechanic", r"forging", r"metalworking"],
    },
    "education-teaching": {
        "noc": {"42202","41200","41220","41221"},
        "kw": [r"early childhood", r"professor", r"lecturer", r"teacher", r"kindergarten", r"educator"],
    },
    "beauty-personal-services": {
        "noc": {"63210","63211","60040"},
        "kw": [r"hairstylist", r"hair stylist", r"barber", r"esthetician", r"electrologist",
               r"beauty", r"salon", r"\bspa\b", r"personal service"],
    },
    "marketing-media-creative": {
        "noc": {"11202","10022","41402","52120","51120","53121","55109","21233"},
        "kw": [r"marketing", r"advertising", r"public relations", r"graphic design", r"web designer",
              r"producer", r"director", r"choreographer", r"market research", r"performer", r"actor",
              r"journalist", r"communications"],
    },
    "repair-maintenance": {
        "noc": {"74203","72423","72404","72020","73201","22311"},
        "kw": [r"automotive", r"heavy truck and equipment", r"motorcycle", r"all-terrain",
              r"aircraft mechanic", r"aircraft inspector", r"building maintenance",
              r"building superintendent", r"electronic service technician"],
    },
}

# Keyword fallback priority (fish/food before general, cleaning last-ish)
KW_PRIORITY = [
    "fish-seafood",
    "food-processing",
    "healthcare-nursing",
    "construction",
    "transport-trucking",
    "hospitality-food-service",
    "cleaning-landscaping",
    "retail-sales",
    "tech-it",
    "office-admin",
    "manufacturing-industrial",
    "education-teaching",
    "beauty-personal-services",
    "marketing-media-creative",
    "repair-maintenance",
]

MAX_PART_ROWS = 200


def jobbank_check_url(employer):
    """Ready-made Job Bank search link for an employer (quoted phrase, newest first).
    NOTE: URL format is the standard jobbank.gc.ca search shape; spot-check live
    when Job Bank access returns (sandbox IP was tarpitted 2026-10-13)."""
    return (
        "https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring="
        + quote(f'"{employer}"', safe="")
        + "&locationstring=&sort=D"
    )


def web_search_url(employer):
    """Ready-made web search link (official site / careers page discovery)."""
    return "https://www.google.com/search?q=" + quote(f'"{employer}" Canada careers', safe="")


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


def load_teer():
    t = pd.read_csv(RAW_TEER, dtype=str)
    return dict(zip(t["NOC2021"], t["TEER"].astype(str).str.strip()))


def load_clean():
    df = pd.read_excel(RAW_LMIA, skiprows=1)
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
    df["Sector"] = ""
    # 1) NOC list matches (including agriculture stream rule)
    for sector, d in SECTOR_DEFS.items():
        noc = df["NOC"].isin(d["noc"])
        if d.get("stream"):
            noc = noc | df["Program Stream"].eq(d["stream"])
        df.loc[df["Sector"].eq("") & noc, "Sector"] = sector
    # 2) keyword fallback on job title
    title = df["JobTitle"].str.lower().fillna("")
    for sector in KW_PRIORITY:
        if sector == "agriculture":
            continue  # agriculture already fully covered by stream+NOC
        pats = SECTOR_DEFS[sector]["kw"]
        mask = df["Sector"].eq("")
        for p in pats:
            mask = mask & ~title.str.contains(p, regex=True, na=False)
        hit = df["Sector"].eq("") & title.str.contains("|".join(pats), regex=True, na=False)
        df.loc[hit, "Sector"] = sector
        _ = mask  # (priority handled by sequential assignment on empty Sector)
    return df


def add_teer_skilllevel(df, teer_map):
    df["TEER"] = df["NOC"].map(teer_map).fillna("")
    df["SkillLevel"] = ""
    df.loc[df["TEER"].isin(["0", "1", "2", "3"]), "SkillLevel"] = "SKILLED"
    df.loc[df["TEER"].isin(["4", "5"]), "SkillLevel"] = "UNSKILLED"
    return df


def load_jb_slim():
    if os.path.exists(JB_SLIM_OUT):
        return pd.read_csv(JB_SLIM_OUT, dtype=str)
    cols = ["Job Title", "NOC21 Code", "NOC21 Code Name", "First Posting Date", "Vacancy Count",
            "Province/Territory", "City", "Work Location Postal Code",
            "Salary Minimum", "Salary Maximum", "Salary Per", "Employment Type", "Employment Term"]
    jb = pd.read_csv(RAW_JB, sep="\t", encoding="utf-16", usecols=cols, dtype=str, low_memory=False)
    jb.to_csv(JB_SLIM_OUT, index=False)
    return jb


def jb_market_signal(jb, sector):
    d = SECTOR_DEFS[sector]
    nocs = list(d["noc"])
    sub = jb[jb["NOC21 Code"].isin(nocs)].copy()
    n_postings = len(sub)
    n_vac = pd.to_numeric(sub["Vacancy Count"], errors="coerce").fillna(0).sum()
    wage = None
    sal_min = pd.to_numeric(sub["Salary Minimum"], errors="coerce")
    sal_max = pd.to_numeric(sub["Salary Maximum"], errors="coerce")
    per = sub["Salary Per"].fillna("")
    hourly = ((sal_min + sal_max) / 2).where(per.eq("Hour"))
    annual = (((sal_min + sal_max) / 2) / 2080).where(per.eq("Year"))
    rate = hourly.fillna(annual).dropna()
    if len(rate) > 0:
        wage = round(rate.median(), 2)
    top_prov = sub["Province/Territory"].value_counts().head(3)
    return n_postings, int(n_vac), wage, top_prov


def export_sector(df, sector, jb):
    out_dir = os.path.join(REPO, "sectors", sector)
    os.makedirs(out_dir, exist_ok=True)
    sub = df[df["Sector"] == sector].copy()
    sub = sub.sort_values(
        ["Province/Territory", "Approved Positions", "Employer"],
        ascending=[True, False, True],
        kind="mergesort",
    ).reset_index(drop=True)

    sub["Entry"] = sub.index + 1
    # Self-check links: the list verifies itself. Buyers (and we) click to see live
    # postings / find the official site. No employer-by-employer browser slavery.
    sub["JobBankCheck"] = sub["Employer"].apply(jobbank_check_url)
    sub["WebSearch"] = sub["Employer"].apply(web_search_url)

    cols = [
        "Entry", "Employer", "JobTitle", "NOC", "TEER", "SkillLevel",
        "City", "ProvinceCode", "Postal", "Program Stream",
        "Approved LMIAs", "Approved Positions", "Address",
        "JobBankCheck", "WebSearch",
    ]

    # Owner decision 2026-10-14: SKILLED and UNSKILLED are separate file series.
    # Buyers shop by skill level — never mixed in one file.
    # Remove legacy mixed part files from earlier pipeline versions.
    for old_name in os.listdir(out_dir):
        if old_name.startswith(f"{sector}-part") and old_name.endswith(".csv"):
            os.remove(os.path.join(out_dir, old_name))

    part_files = {}   # level -> list of generated filenames
    for level in ("SKILLED", "UNSKILLED"):
        lvl = sub[sub["SkillLevel"] == level].copy()
        lvl = lvl.sort_values(
            ["Province/Territory", "Approved Positions", "Employer"],
            ascending=[True, False, True],
            kind="mergesort",
        ).reset_index(drop=True)
        lvl["Entry"] = lvl.index + 1
        names = []
        for start in range(0, len(lvl), MAX_PART_ROWS):
            chunk = lvl.iloc[start : start + MAX_PART_ROWS]
            n = len(names) + 1
            name = f"{sector}-{level.lower()}-part{n:02d}.csv"
            chunk[cols].to_csv(os.path.join(out_dir, name), index=False)
            names.append(name)
        part_files[level] = names

    # README with live stats
    prov_counts = sub["ProvinceCode"].value_counts()
    top_jobs = sub["JobTitle"].value_counts().head(10)
    unique_emp = sub["Employer"].nunique()
    skill = sub["SkillLevel"].value_counts()
    repeat = sub.groupby("Employer")["Approved Positions"].sum().sort_values(ascending=False).head(10)

    lines = []
    lines.append(f"# {sector.upper()} - Cardo Careers sector data")
    lines.append("")
    lines.append(f"- Source: ESDC TFWP Positive LMIA Employers List, {QUARTER} (English)")
    lines.append(f"- Total entries: **{len(sub)}** | Unique employers: **{unique_emp}**")
    lines.append(
        "- Files (SKILLED and UNSKILLED are separate, never mixed): "
        + ", ".join(
            f"**{level}: {len(names)} part(s)** ({len(sub[sub['SkillLevel'] == level])} rows)"
            for level, names in part_files.items()
        )
        + f" — max {MAX_PART_ROWS} rows per file"
    )
    if len(skill):
        lines.append(f"- Skill split: " + ", ".join(f"{k} {v}" for k, v in skill.items()) + " (TEER 0-3 = SKILLED, 4-5 = UNSKILLED, source: IRCC)")
    if sector in SECTOR_DEFS:
        n_p, n_v, wage, top_prov = jb_market_signal(jb, sector)
        lines.append(f"- Live market signal (Job Bank, {JB_MONTH}): {n_p} postings, {n_v} vacancies" + (f", median wage ~${wage}/hr equivalent" if wage else ""))
        if len(top_prov):
            lines.append("  - Postings by province: " + ", ".join(f"{p} {c}" for p, c in top_prov.items()))
    lines.append("")
    lines.append("## Files")
    lines.append("")
    for level in ("SKILLED", "UNSKILLED"):
        names = part_files[level]
        if not names:
            continue
        n_rows = len(sub[sub["SkillLevel"] == level])
        lines.append(f"**{level}** (TEER {'0-3' if level == 'SKILLED' else '4-5'}), {n_rows} entries:")
        lines.append("")
        for n in names:
            lines.append(f"- `{n}`")
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
    lines.append("## Top repeat hirers (total approved positions)")
    lines.append("")
    for e, c in repeat.items():
        lines.append(f"- {e}: {c}")
    lines.append("")
    lines.append("## Check it yourself (built into every part file)")
    lines.append("")
    lines.append(
        "Every row carries two ready-made links: JobBankCheck (opens Job Bank "
        "pre-filled with a quoted search for that employer, newest first) and "
        "WebSearch (finds the employer's official site / careers page). Click, look, "
        "decide. An approved LMIA is NOT a promise of a current opening - the links "
        "are how you check the live situation in seconds."
    )
    lines.append("")

    # Preserve any existing hunt/verification section (added by hunt batches, not the pipeline)
    readme_path = os.path.join(out_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, encoding="utf-8") as f:
            old = f.read()
        idx = old.find("## Verification (the hunt)")
        if idx != -1:
            lines.append(old[idx:].rstrip())
            lines.append("")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(sub), {level: len(names) for level, names in part_files.items()}


def main():
    teer_map = load_teer()
    print(f"[teer] {len(teer_map)} NOC codes loaded from IRCC table")
    df, deduped = load_clean()
    print(f"[load] rows kept: {len(df)} (dropped {deduped} exact duplicates + footer notes)")
    df = tag_sectors(df)
    df = add_teer_skilllevel(df, teer_map)

    processed_path = os.path.join(REPO, "data", "processed", "tfwp_2026q1_clean.csv")
    df.to_csv(processed_path, index=False)
    print(f"[save] data/processed/tfwp_2026q1_clean.csv")

    print("\n=== sector counts ===")
    print(df["Sector"].replace("", "(unassigned)").value_counts().to_string())

    print("\n=== skill levels (all rows) ===")
    print(df["SkillLevel"].replace("", "(no teer)").value_counts().to_string())

    # leftovers for review
    left = df[df["Sector"].eq("")]
    left["Occupation"].value_counts().head(50).to_csv(
        os.path.join(REPO, "data", "processed", "unassigned_review.csv")
    )
    print(f"\n[leftover review] {len(left)} rows -> data/processed/unassigned_review.csv")

    jb = load_jb_slim()
    print(f"[jobbank slim] {len(jb)} postings loaded")

    print()
    for sector in SECTOR_DEFS:
        total, parts = export_sector(df, sector, jb)
        print(f"[{sector}] entries: {total} -> SKILLED {parts['SKILLED']} part(s), UNSKILLED {parts['UNSKILLED']} part(s)")

    print("\nDone.")


if __name__ == "__main__":
    sys.exit(main())
