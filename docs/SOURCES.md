# Source catalogue

Every public source worth pulling on Braze, what each one yields, and how to get it.
**Verified reachable on 2026-09-01** unless marked otherwise — the counts below describe
the *sources*, not Braze's business. Nothing here is a finding.

Re-verify before you rely on a count: endpoints move, and a stale catalogue is worse
than none. Anything that fails goes in [`logs/fetch-failures.md`](../logs/fetch-failures.md),
because a gap you have written down is evidence and a gap you have not is a mistake.

---

## Tier 1 — records Braze does not control

The phase most analyses skip, and where the non-obvious findings live. Ordered by how
hard it would be for Braze to have made the statement untrue.

### SEC EDGAR — the reason this analysis can go deeper than a private vendor's

Braze is listed on Nasdaq as **BRZE**, CIK **0001676238**, SIC 7372, **fiscal year ending
31 January**. Filings are audited, submitted under legal penalty, and machine-readable.

| What | Address | Verified |
|---|---|---|
| All filings | `https://data.sec.gov/submissions/CIK0001676238.json` | **737 filings, 2017-07-20 → 2026-08-28** |
| XBRL facts | `https://data.sec.gov/api/xbrl/companyfacts/CIK0001676238.json` | **357 us-gaap concepts; key series 2019-01-31 → 2026-04-30** |
| A filing's documents | `https://www.sec.gov/Archives/edgar/data/1676238/<accession>/` | via `filings.csv` |

Form counts, which are themselves a map of where to look:

| Form | Count | What it gives up |
|---|---|---|
| 10-K | 5 | The whole business, annually. Risk factors are the honest section: legally, they must disclose what could go wrong |
| 10-Q | 14 | Quarterly, including segment and geography splits |
| 8-K | 32 | Material events, dated. Acquisitions, executive departures, restructuring |
| DEF 14A | 5 | Executive compensation, the board, and what management is actually paid to optimise |
| Form 4 | 439 | Every insider transaction, with date, price, volume |
| Form 144 | 92 | A *proposed* insider sale — filed before the Form 4 that reports it |
| SC 13G / 13D (+ /A) | 72 | Who owns the company, and when their stake changed |
| S-8 | 8 | Shares registered for employee compensation — dilution, dated |

**Run:** `python3 tools/sec_facts.py` and `python3 tools/sec_filings.py`.

> **Trap, already hit and encoded in the tool.** XBRL's `fy`/`fp` fields describe the
> *filing*, not the period. Braze's FY2026 10-K reports FY2024 and FY2025 figures and
> XBRL labels both `fy2026`. Key on `start`/`end`. `sec_facts.py` derives a correct
> `period` column so you never have to think about this again.

### Certificate transparency

Independent log operators record every certificate issued. Append-only; the subject
cannot edit or retract it. On the reference project this surfaced an unannounced
product, an MCP server, and a named enterprise customer that appeared nowhere in
marketing.

| Source | Address | State on 2026-09-01 |
|---|---|---|
| crt.sh | `https://crt.sh/?q=%25.braze.com&output=json` | **502 Bad Gateway** all afternoon. Retry; it is often down |
| Cert Spotter | `https://api.certspotter.com/v1/issuances?domain=braze.com&include_subdomains=true&expand=dns_names` | **167 distinct names on the first page**, then HTTP 429 |

Anonymous Cert Spotter callers get roughly one page. A free token at
`sslmate.com/certspotter` lifts that — export `CERTSPOTTER_TOKEN`.

**Run:** `python3 tools/ct_probe.py` (tries crt.sh, falls back, keeps partial results).

### UK Companies House — a filed record, but check *which* company

Two candidate entities, **neither confirmed** as the vendor's:

| Company | Number |
|---|---|
| BRAZE LIMITED | `09846844` |
| BRAZE MARKETING LTD | `10711967` |

Resolve by matching the registered office and directors against the 10-K's subsidiary
list (10-K Exhibit 21). **Do not cite either until that match is made** — name collision
is common and "Braze Limited" may be an unrelated business.

Free API at `https://api.company-information.service.gov.uk/` (needs a free key).
Note the value is *lower* here than for a private vendor: a UK subsidiary's accounts
are a transfer-pricing artefact, and for Braze you already have the audited group.

---

## Tier 2 — company-own, but operationally constrained

Self-published, yet costly to get wrong because someone acts on it.

| Source | Address | Verified |
|---|---|---|
| Documentation | `https://www.braze.com/docs/` | **1,352 pages** in the docs sitemap |
| Docs sitemap | `https://www.braze.com/docs/sitemap.xml` | 1,352 `<loc>` entries |
| Release notes | `https://www.braze.com/docs/releases/home` | 200 (redirected from `/docs/help/release_notes/`) |
| Release notes, as source | `https://github.com/braze-inc/release-notes` | public repo, ~20 MB, pushed daily |
| Sub-processor disclosure | `https://www.braze.com/company/legal/subprocessors` | 200 |
| `security.txt` | `https://www.braze.com/.well-known/security.txt` | **200, 236 bytes — it exists** |
| Status page | `https://braze.statuspage.io` | **132 components, 451 incidents, 2016-10-09 → 2026-08-05** |
| Public code | `https://github.com/braze-inc` | **137 repos**, org created 2017-10-16 |

### Why the sub-processor page is worth more than it looks

It is legally compelled to be accurate and complete. It names the database engine, the
iPaaS, every delivery supplier — and, by omission, **which channel has no middleman**.
Capture it *with a date*: the reference project caught a vendor's list changing from 16
to ~40 entities mid-analysis, and the correction was only visible because both versions
were kept.

### The status page is a decade of operational history

132 components in **12 groups**: `US 01`–`US 04`, `EU 01`, `EU 02`, `AU 01`, `ID 01`,
`JP 01`, `KR 01` clusters, plus `Global Messaging Channels` and `Global Services`. The
component list is an architecture disclosure made by accident.

**Good for:** incidents per quarter, duration distribution, which components fail, which
named channel or region appears most. **Not good for:** comparison against a vendor with
no status page. That is an absence of evidence, never evidence of good uptime.

**Run:** `python3 tools/status_history.py`.

### The GitHub org measures maintenance, not capability

**137 public repos**; **494 releases across 9 SDK repos**, 2016-12-13 → 2026-09-01.
Release cadence per platform is a maintenance signal that no marketing page will give
you straight, and a repo that stopped moving is the strongest "quietly retired"
evidence there is. It says nothing about the server side.

Anonymous GitHub allows 60 requests/hour. Export `GITHUB_TOKEN` for the full walk.

**Run:** `python3 tools/github_org.py`.

---

## Tier 3 — company-own marketing

Fine for what they *claim*; no support for whether it is true. Read it to know their
story, then test the story against Tier 1 and 2.

**6,366 distinct URLs** across 8 sitemaps (`https://www.braze.com/sitemap.xml` is an index):

| Section | URLs | Worth pulling for |
|---|---|---|
| `resources` | 2,618 | Reports, guides, webinars. Their own framing of the market |
| `docs` | 1,352 | Tier 2 — see above |
| `ja` | 957 | Japanese tree. Localisation depth is a market-priority signal |
| `pt-br` / `fr` / `es` / `ko` | 313 / 198 / 192 / 175 | Same, per market |
| `customers` | **178** | Named customer stories. Cross-check against detected usage |
| `press-releases` | 95 | Dated announcements — feed the timeline |
| `company` | 47 | Leadership, careers, legal |
| `product` / `solutions` / `partners` | 29 / 14 / 4 | The positioning, in their words |

Six published languages: `en-us`, `ja`, `pt-br`, `fr`, `es`, `ko`.

**Run:** `python3 tools/fetch_sitemap.py`, then `python3 tools/fetch_docs.py`.

---

## Tier 4 — what customers say

### The scriptable one: public issue trackers

**1,091 issues across `braze-inc`** — 1,065 closed, 26 open, verified 2026-09-01. Fully
scriptable, and on several axes better evidence than a review panel:

- **Unsolicited.** Nobody was emailed a review request. People open an issue because
  something cost them a day.
- **Specific.** A stack trace and a reproduction, not "segmentation is clunky".
- **Dated, with a resolution**, so time-to-close is measurable.
- **The vendor answers in public**, which is itself a support-quality signal.

What it is not: representative. Issue authors are developers, not the marketers who buy
the product, so it describes the SDK surface rather than the dashboard. Never convert
issue counts into a satisfaction rating.

**Run:** `python3 tools/fetch_issues.py` → `data/issues.csv` and a panel file that
`code_reviews.py` codes like any other corpus.

### The bot-walled ones: enrichment, not a dependency

**All of these returned HTTP 403 to scripted access on 2026-09-01.** They are not
missing; they are bot-walled — and they are **not a blocker**, because the issue tracker
above covers the customer-voice requirement. Capture them if a browser session is
available, note the absence if not.

1. **Drive a real Chrome session** with the `claude-in-chrome` tools. Read the page, save
   the text to `sources/panels/<site>.txt`.
2. **Ask the operator to paste it.** A five-minute human step, worth it for Gartner.

Put a capture date at the top of every panel file. Then run
`python3 tools/code_reviews.py`, which locks the theme patterns in a script so the
same corpus cannot be coded three different ways.

| Panel | Address | Yields |
|---|---|---|
| G2 | `https://www.g2.com/products/braze/reviews` | Rating, review count, star distribution, **company-size mix** |
| Gartner Peer Insights | `https://www.gartner.com/reviews/market/multichannel-marketing-hubs/vendor/braze` | Ratings, deployment region, **shortlists — who they were compared against** |
| TrustRadius | `https://www.trustradius.com/products/braze/reviews` | Longer-form reviews, often more specific |
| Glassdoor | `https://www.glassdoor.com/Overview/Working-at-Braze-EI_IE1024231.11,16.htm` | Employee sentiment, work/life trend, CEO approval |
| LinkedIn | company page | Headcount **range** — never a precise figure |
| Careers board | `https://www.braze.com/company/careers` | Open roles by function. Strategy, stated in hiring |

**Gartner shortlists are the highest-value field in any of these.** Who a buyer
*actually* compared the vendor against is worth more than any competitor page, because
the vendor did not choose it.

`investors.braze.com` also returns 403 to scripts. Everything on it is in EDGAR; use
EDGAR and skip the fight.

---

## What is missing, and how to tell

Absence is a finding, but only when the check was exhaustive. These are exhaustive:

- **Price.** Search all 6,366 URLs for a number. "No price appears anywhere" is a
  checkable, quotable claim; "I could not find pricing" is not.
- **Adoption figures** for any specific feature. Vendors publish these when they are
  good.
- **Any channel they do not sell.** The channel list is enumerable from the docs; what
  is *not* on it is as interesting as what is.

And a caution: for a listed company, an absence in marketing is weaker evidence than
usual, because the 10-K may cover it. **Search the filings before calling anything absent.**

---

## Order to pull them in

Cheap and exhaustive first; expensive and partial last.

`python3 tools/run_all.py` does all of this in order, skipping what is already done and
continuing past optional failures. Individually:

```bash
python3 tools/fetch_sitemap.py       # ~30s   the map. Do this first, always
python3 tools/sec_facts.py           # ~15s   audited financials, machine-readable
python3 tools/sec_filings.py         # ~20s   the filing index is itself evidence
python3 tools/fetch_filings.py       # ~3min  the 10-K itself — ~73,000 words
python3 tools/status_history.py      # ~60s   a decade of incidents
python3 tools/github_org.py          # ~90s   release cadence per platform
python3 tools/fetch_issues.py        # ~3min  the customer voice, scriptable
python3 tools/ct_probe.py            # varies crt.sh is unreliable; retry later
python3 tools/fetch_docs.py          # ~25min 1,352 pages, polite and resumable
python3 tools/index_docs.py          # ~10s   index BEFORE reading anything
python3 tools/extract_api.py         # ~5s    the second lens on capability
python3 tools/capability_count.py    # ~20s   the focused-page measurement
python3 tools/code_reviews.py        # ~5s    codes every panel present
python3 tools/build_timeline.py      # ~5s    one chronology from every source
```
