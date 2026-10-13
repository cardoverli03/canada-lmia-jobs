# THE HUNT — Cardo Careers verification SOP

How every Cardo Careers verification batch works. Follow it exactly. The product's
value is honesty: an ACTIVE tag on our lists means WE verified it, on the stated date.

## Golden rules

1. **Never invent.** Only record what the browser actually showed. If it is not on
   the page, it does not exist.
2. **Wrong-name lookalikes are NOT matches.** Verify the employer identity on the
   page itself (company name, address, city). If the page cannot prove the identity,
   it is not evidence.
3. **Date-stamp everything.** Every verdict carries the verification date.
4. **Never present WATCH as ACTIVE.** An open application form is ACTIVE (a live
   application channel). It is NOT a dated job opening — say which one it is.
5. **Order of hunting: top Approved-Positions first**, sector by sector.

## Toolchain

- `agent-browser` (headless Chromium) — the only trusted reader. Plain curl is
  WAF-blocked on many Gov of Canada hosts, and Cloudflare-walled sites reject
  headless browsers anyway (verdict BOT-WALLED, retry later).
- Cheap curl probes (`timeout 8-12`) to test domains BEFORE opening them in the
  browser — avoids wedging the session on hanging hosts. 200 = open in browser,
  000/timeout = dead from this network, 403/429 = exists, bot-walled or
  rate-limited, try browser once.

## Method per employer

1. Compute the target list: employers sorted by Approved Positions (desc) from the
   sector part files (top 15-20 = one batch).
2. Official website attempt, in order:
   a. Direct domain probes (2-3 sensible name variants). `https://` first, then `www.`
   b. Open reachable candidates in the browser. **Verify the company identity on the
      page** (name in title/body/footer, city/address match with the LMIA row).
   c. Extract careers/jobs/emplois/carrieres links. If found: open, read everything,
      capture: page text, application method (form / email / phone), any dated
      listings.
   d. No careers link: probe `/careers /jobs /employment /carrieres /emplois` paths.
3. Job Bank cross-check (jobbank.gc.ca employer-name search) — **currently blocked
   from this sandbox IP** (TCP tarpit after the 2026-10-13 bulk fetch; retry each
   batch). When it works, it becomes step 2's first move.
4. Write one row per target in `data/hunt/YYYY-MM-DD_<sector>_batchNN.csv` with the
   verdict vocabulary below. Commit + push the same day.

## Verdict vocabulary (exact strings, keep consistent)

| Verdict | Meaning |
|---|---|
| `ACTIVE` | Live hiring/application channel verified on the employer's official site (evidence URL + date in the row) |
| `NO-PUBLIC-CHANNEL` | Official site verified live, but no public hiring/application page on it |
| `NO-SITE-FOUND` | No official website found (checked name-sensible domains; nothing assumed) |
| `WRONG-SITE-LOOKALIKE` | Same-name site exists but is a different company — excluded, never used as evidence |
| `BOT-WALLED` | Site exists but bot challenge (Cloudflare etc.) blocks verification |
| `UNREACHABLE` | Domain exists but times out / refuses from our network |
| `PENDING-JOBBANK` (note column) | Job Bank cross-check not yet possible — add as a note, never as a verdict |

## Batch log format

`data/hunt/YYYY-MM-DD_<sector>_batchNN.csv`
Columns: `Rank,Employer,City,Province,ApprovedPositions,Method,SourceChecked,Result,Verdict,EvidenceURL,VerifiedDate,Notes`

## Known traps (do not re-discover)

- `goodyearfarms.com` = California nursery, NOT Goodyear Farm Ltd (Queensville, ON).
- `vegibec.com` rate-limits (429) plain requests but opens fine in the browser.
- `fraisierefaucher.com` and `highlinemushrooms.com` = Cloudflare walls (as of
  2026-10-13).
- jobbank.gc.ca tarpits this sandbox IP (as of 2026-10-13). open.canada.ca is fine.
- Bing/DDG serve bot-walled or degraded results from this IP — do not rely on
  search engines; go direct to domains.
