# FACTS — the canonical value of every number this project uses

**This file is empty of findings, by design.** The repository ships as a research
environment, not as an analysis. Every row below arrives when the research does.

## The rule this file exists to enforce

> **When you need a number, read this file and stop.**

Going hunting in `sources/` for something already recorded here burns context and risks
resurrecting a figure that was corrected. If a number is not here yet, find it, verify
it, and **add it here** — that is how the file stays worth trusting.

## How to add a row

Every fact carries four things and never fewer:

| field | rule |
|---|---|
| **Value** | Exactly as it will be said out loud, with its unit and its caveat |
| **Grade** | One of the five in [`EVIDENCE-GRADES.md`](EVIDENCE-GRADES.md). The **weakest** supporting source, never the best |
| **Source** | `path:line-range`, or a URL with a capture date. Never "the docs" |
| **As of** | The date the source was captured. Numbers rot |

If two credible sources disagree, do **not** pick one. Put both here, grade the fact
`conflicted`, and open a row in [`CONFLICTS.md`](CONFLICTS.md) with a ruling on what to
say out loud.

---

## 1 · Corporate

Legal entity, listing, incorporation, leadership, ownership, headcount, subsidiaries.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| SEC registrant | Braze, Inc. | audited | `data/filings.csv` | 2026-09-01 |
| CIK | 0001676238 | audited | `data/filings.csv` | 2026-09-01 |
| Ticker / exchange | BRZE / Nasdaq | audited | `data/filings.csv` | 2026-09-01 |
| SIC classification | 7372 Services-Prepackaged Software | audited | `data/filings.csv` | 2026-09-01 |
| Fiscal year end | 31 January | audited | `data/filings.csv` | 2026-09-01 |
| Founded / incorporated | 2011, in Delaware | audited | `sources/filings/2026-03-25_10-K_000013.txt:249,598` | 2026-03-25 |
| Headquarters | 63 Madison Building, 28 East 28th Street, Floor 12, New York, NY 10016 | audited | `sources/filings/2026-03-25_10-K_000013.txt:598` | 2026-03-25 |
| IPO | Final prospectus (424B4) filed 2021-11-18; S-1 filed 2021-10-22; 8-A12B 2021-11-12 | audited | `data/filings.csv` | 2026-09-01 |
| IPO net proceeds | ~$456.8m, after underwriting discounts, commissions and offering expenses | audited | `sources/filings/2022-03-31_10-K_000005.txt:2061` | 2022-03-31 |
| How the company describes itself | "our platform empowers real-time engagement… made possible by our proprietary, enterprise-grade stream processing architecture… designed it to listen like a human would… and react instantaneously". Filed in Item 1, but a *positioning* statement — graded as the company's own narrative, not as an audited figure | claimed | `sources/filings/2026-03-25_10-K_000013.txt:258` | 2026-03-25 |
| Documentation corpus size | 1,565,479 words across 1,352 pages: user_guide 696 pages, partners 322, api 200, developer_guide 106, releases 27, help 1 | documented | `data/docs_sections.csv` | 2026-09-02 |
| Documentation depth differs sharply by section | developer_guide averages ~2,708 words/page; partners averages ~810 | documented | derived from `data/docs_sections.csv` | 2026-09-02 |
| Dual-class structure | **Ended.** Class B retired and automatically converted to Class A on 2026-01-30; "our executive officers and early investors no longer hold super-voting rights" | audited | `sources/filings/2026-03-25_10-K_000013.txt:1197` | 2026-03-25 |
| Full-time employees | 1,988 as at 2026-01-31 | audited | `sources/filings/2026-03-25_10-K_000013.txt:590` | 2026-03-25 |
| Full-time employees, FY2022 → FY2026 | 1,164 · 1,501 · 1,548 · 1,699 · 1,988 | audited | `sources/filings/2022-03-31_10-K_000005.txt`, `2023-03-31_10-K_000031.txt`, `2024-04-01_10-K_000049.txt`, `2025-03-31_10-K_000054.txt`, `2026-03-25_10-K_000013.txt` — the "we had a total of N full-time employees" line in each | 2026-09-02 |
| Headcount growth vs revenue growth, FY2022 → FY2026 | Headcount **+71%**, revenue **+210%** | audited | derived from the row above and `data/financials_annual.csv` | 2026-09-02 |
| The year the two decoupled | FY2024: headcount grew **3.1%** (1,501 → 1,548) while revenue grew **32.7%** | audited | derived as above | 2026-09-02 |
| _Headcount is full-time only_ | The 10-K figure counts full-time employees. The proxy's pay-ratio population, on the same date, is "all of our full-time **and part-time** employees… not including any independent contractors" and is never sized. See CONFLICTS **C-07** | — | `sources/filings/2026-05-18_DEF-14A_021908.txt:5769` | 2026-09-02 |
| One "group entity" is not wholly owned | Braze KK (Japan) is a **majority-held** entity consolidated as a **Variable Interest Entity**, with outside investors (Japan Cloud Computing, M30 LLC) holding a redeemable non-controlling interest and employee options over its shares. See CONFLICTS **C-09** | audited | `sources/filings/2026-03-25_10-K_000013.txt:2477,2479` | 2026-03-25 |
| Legal entities in the group | 15, across 14 territories: Australia, Brazil, Canada, France, Germany, Ireland, Spain, United States, Ireland & Romania, Japan, South Korea, United Kingdom, UAE, Singapore, Indonesia | documented | `sources/clean/braze-subprocessors.md:41` | 2026-09-02 |
| Total SEC filings | 737, 2017-07-20 → 2026-08-28 | audited | `data/filings.csv` | 2026-09-01 |

## 2 · Money

Revenue, gross margin, operating expense by line, losses, cash, RPO, dilution, SBC.
All rows below are audited, from `data/financials_annual.csv` (XBRL company facts), and
every one is re-derivable with `python3 tools/sec_facts.py`. Fiscal years end 31 January.

### 2.1 · The seven-year series ($m)

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Revenue, FY2020 → FY2026 | 96.4 · 150.2 · 238.0 · 355.4 · 471.8 · 593.4 · 738.2 | audited | `data/financials_annual.csv` | 2026-09-02 |
| Revenue growth, FY2021 → FY2026 | 55.9% · 58.5% · 49.3% · 32.7% · 25.8% · 24.4% | audited | `data/financials_annual.csv` | 2026-09-02 |
| Gross margin, FY2020 → FY2026 | 63.0% · 63.7% · 67.0% · 67.4% · 68.7% · 69.1% · 67.1% | audited | `data/financials_annual.csv` | 2026-09-02 |
| FY2026 gross-margin decline | Down 2.0 points, 69.1% → 67.1% — the first fall in six years | audited | `data/financials_annual.csv`; `sources/filings/2026-03-25_10-K_000013.txt:1565` | 2026-09-02 |
| The company's own explanation for it | "primarily due to acquisition related operating costs, including personnel costs of acquired workforce and amortization expense of acquired technology, in addition to increased costs related to our tech stack" | audited | `sources/filings/2026-03-25_10-K_000013.txt:1565` | 2026-03-25 |
| Net loss, FY2020 → FY2026 | −31.8 · −31.8 · −76.7 · −139.0 · −129.2 · −103.7 · −131.3 | audited | `data/financials_annual.csv` | 2026-09-02 |
| Operating cash flow, FY2020 → FY2026 | −7.4 · −6.1 · −35.4 · −22.3 · **+6.8 · +36.7 · +$71.4m** — positive and growing for three consecutive years | audited | `data/financials_annual.csv` | 2026-09-02 |
| Cash and equivalents, FY2026 | $124.3m | audited | `data/financials_annual.csv` | 2026-09-02 |

### 2.1b · The caveat that travels with every figure above

Found in the self-review on 2026-09-02, after the first draft of this analysis was
written. It qualifies the whole of §2 and belongs with the numbers, not in a footnote.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Disclosure controls, as at 2026-01-31 | The CEO and CFO concluded they were **"not effective at the reasonable assurance level"** | audited | `sources/filings/2026-03-25_10-K_000013.txt:3258` | 2026-03-25 |
| The material weakness | "ineffective information technology general controls, or ITGCs, in the areas of **user access and program change management** over the information technology systems that support our financial reporting processes" | audited | `sources/filings/2026-03-25_10-K_000013.txt:3286` | 2026-03-25 |
| Knock-on effect the company states | Automated and IT-dependent manual controls relying on that environment "were ineffective because they could have been adversely impacted" | audited | `sources/filings/2026-03-25_10-K_000013.txt:3286` | 2026-03-25 |
| What it did **not** do — and this matters | "The material weakness did not result in any identified misstatements to the financial statements, and there were no changes to previously issued financial results" | audited | `sources/filings/2026-03-25_10-K_000013.txt:1176` | 2026-03-25 |
| Management's conclusion on the statements | The consolidated financial statements "fairly present in all material respects" the financial condition, results and cash flows | audited | `sources/filings/2026-03-25_10-K_000013.txt:3266` | 2026-03-25 |
| Auditor position | Ernst & Young "issued an attestation report on our internal control over financial reporting" | audited | `sources/filings/2026-03-25_10-K_000013.txt:3272` | 2026-03-25 |
| Remediation | In progress, "significant progress has been made to date"; completion date not given | audited | `sources/filings/2026-03-25_10-K_000013.txt:3290` | 2026-03-25 |
| OfferFit excluded from the ICFR assessment | Permitted for a first-year acquisition. It is 1.4% of consolidated total assets and 1.8% of total revenue | audited | `sources/filings/2026-03-25_10-K_000013.txt:3270` | 2026-03-25 |
| _How to say this_ | Say both halves in one breath: the control environment over the systems that produce these numbers was judged not effective, **and** no misstatement was identified, nothing was restated, and the auditor attested. Do not turn an ITGC finding into a claim about customer data security — it is scoped to financial-reporting systems | — | `docs/FACTS.md` §2.1b | 2026-09-02 |

### 2.2 · Where the money goes

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| S&M as a share of revenue, FY2020 → FY2026 | 59.5% · 47.0% · 53.4% · 56.7% · 52.4% · 47.6% · **44.3%** | audited | `data/financials_annual.csv` | 2026-09-02 |
| R&D as a share of revenue, FY2020 → FY2026 | 21.1% · 19.4% · 24.8% · 27.4% · 25.4% · 22.6% · 22.6% | audited | `data/financials_annual.csv` | 2026-09-02 |
| G&A, FY2026 | $146.3m (19.8% of revenue) | audited | `data/financials_annual.csv` | 2026-09-02 |
| S&M still outspends R&D | $327.0m vs $167.1m in FY2026 — 1.96× | audited | `data/financials_annual.csv` | 2026-09-02 |
| Revenue per full-time employee, FY2022 → FY2026 | $204k · $237k · $305k · $349k · **$371k** — a rise of **82%** | audited | derived from `data/financials_annual.csv` and the headcount series in §1 | 2026-09-02 |
| Customers per full-time employee | 1.18 · 1.18 · 1.32 · 1.35 · 1.31, FY2022 → FY2026 | audited | derived from the customer and headcount series | 2026-09-02 |

### 2.2b · What management is actually paid to optimise

Answers `QUESTIONS.md` #33, which the first pass left open. From the proxy statement,
which the first pass never opened.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| FY2026 bonus-plan metrics | **Net CARR weighted 60%**, **non-GAAP operating income (loss) weighted 40%** | audited | `sources/filings/2026-05-18_DEF-14A_021908.txt:1994` | 2026-05-18 |
| The profitability gate | "failure to achieve a specified target of Non-GAAP Operating Income (loss) as a percentage of our gross profit resulting in **0% achievement of this performance metric**" | audited | `sources/filings/2026-05-18_DEF-14A_021908.txt:1994` | 2026-05-18 |
| The growth cap | If retention was below a specified target, Net CARR achievement "would be limited to 110%" | audited | `sources/filings/2026-05-18_DEF-14A_021908.txt:1994` | 2026-05-18 |
| CEO total compensation, FY2026 | $14,230,598 | audited | `sources/filings/2026-05-18_DEF-14A_021908.txt:5771` | 2026-05-18 |
| Median employee total compensation, FY2026 | $164,000 | audited | `sources/filings/2026-05-18_DEF-14A_021908.txt:5771` | 2026-05-18 |
| CEO pay ratio | **87 to 1** | audited | `sources/filings/2026-05-18_DEF-14A_021908.txt:5771` | 2026-05-18 |

### 2.3 · The cost of the equity story

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Share-based compensation, FY2020 → FY2026 | 12.4 · 7.5 · 47.2 · 72.2 · 97.2 · 115.1 · 143.7 | audited | `data/financials_annual.csv` | 2026-09-02 |
| SBC as a share of the net loss | FY2024 75% · FY2025 **111%** · FY2026 **109%** — for two consecutive years SBC has exceeded the entire net loss | audited | `data/financials_annual.csv` | 2026-09-02 |
| Weighted-average diluted shares (m) | FY2023 94.6 → FY2026 107.9 | audited | `data/financials_annual.csv` | 2026-09-02 |
| Dilution since the first full post-IPO year | +14.1% over three fiscal years | audited | derived from the row above, `data/financials_annual.csv` | 2026-09-02 |

### 2.4 · Forward visibility and the customer base

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Remaining performance obligation | 234.2 · 373.6 · 455.7 · 639.2 · 793.1 · **$1,033.0m** ($m), FY2021 → FY2026 | audited | `data/financials_annual.csv` | 2026-09-02 |
| RPO relative to revenue, FY2026 | 1.40× current-year revenue already contracted | audited | derived from `data/financials_annual.csv` | 2026-09-02 |
| Customers | 2,609 as at 2026-01-31 | audited | `sources/filings/2026-03-25_10-K_000013.txt:1379` | 2026-03-25 |
| Customers with ARR ≥ $500,000 | 333 (FY2026), 247 (FY2025), 202 (FY2024) | audited | `sources/filings/2026-03-25_10-K_000013.txt:1400` | 2026-03-25 |
| Dollar-based net retention, all customers | 109% (FY2026), 111% (FY2025), 117% (FY2024) | audited | `sources/filings/2026-03-25_10-K_000013.txt:1400` | 2026-03-25 |
| Dollar-based net retention, customers ≥ $500k ARR | 110% (FY2026), 114% (FY2025), 120% (FY2024) | audited | `sources/filings/2026-03-25_10-K_000013.txt:1400` | 2026-03-25 |
| The gap between the two has closed | 3 points in FY2024 (120 vs 117) → 1 point in FY2026 (110 vs 109) | audited | derived from the two rows above | 2026-09-02 |
| The company's own explanation for the decline | "primarily due to customer turnover and renewals at lower subscription levels… customers to renew their contracts at levels more closely aligned with their current needs, rather than opting for larger commitments" | audited | `sources/filings/2026-03-25_10-K_000013.txt:1402` | 2026-03-25 |
| Average revenue per customer, FY2026 | **Bounded at ~$283,000** — $738.2m ÷ 2,609 customers. A bound, not a price: it mixes every contract size and includes professional services | audited | derived from `data/financials_annual.csv` and `…10-K…:1379` | 2026-09-02 |
| Revenue per employee, FY2026 | ~$371,000 — $738.2m ÷ 1,988 | audited | derived from `data/financials_annual.csv` and `…10-K…:590` | 2026-09-02 |

### 2.5 · Geography — audited, not inferred

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Revenue by geography, FY2026 | United States $405.1m (54.9%); International $333.1m (45.1%); total $738.2m | audited | `sources/filings/2026-03-25_10-K_000013.txt:2421` | 2026-03-25 |
| International share, FY2024 → FY2026 | 43.4% · 45.0% · 45.1% | audited | `sources/filings/2026-03-25_10-K_000013.txt:2421` | 2026-03-25 |
| Concentration outside the US | "Other than the United States, no other individual country accounted for 10% or more of total revenue for any of the periods presented" | audited | `sources/filings/2026-03-25_10-K_000013.txt:2421` | 2026-03-25 |
| How geography is determined | "based on the location of our users" | audited | `sources/filings/2026-03-25_10-K_000013.txt:2421` | 2026-03-25 |

## 3 · Acquisitions

What was bought, when, for how much, and what it brought. Two material acquisitions in
the company's history; both are disclosed with a price, which a private vendor rarely
permits.

### 3.1 · OfferFit, Inc. — now **BrazeAI Decisioning Studio**

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Date | 2 June 2025 (FY2026) | audited | `sources/filings/2026-03-25_10-K_000013.txt:3130` | 2026-03-25 |
| Total consideration | **$303.2m** — $195.3m cash and $107.6m in Braze Class A common stock (adjusted from a preliminary $302.9m) | audited | `sources/filings/2026-03-25_10-K_000013.txt:3130,1788` | 2026-03-25 |
| What it is now called | "OfferFit, Inc. ('OfferFit') **which is now known as AI Decisioning Studio**" | audited | `sources/filings/2026-03-25_10-K_000013.txt:1788` | 2026-03-25 |
| What was bought, in the company's words | "OfferFit's multi-agent decisioning engine" | audited | `sources/filings/2026-03-25_10-K_000013.txt:3130` | 2026-03-25 |
| Purchase-price allocation | Goodwill $233.4m; intangibles $66.6m; net tangible assets $2.9m | audited | `sources/filings/2026-03-25_10-K_000013.txt:3134` | 2026-03-25 |
| Share of the price that is goodwill | 77.0% ($233.4m of $303.2m) | audited | derived from the row above | 2026-09-02 |
| Intangibles detail | Developed technology $56.7m; customer relationships $9.0m; trademarks $0.9m | audited | `sources/filings/2026-03-25_10-K_000013.txt:3137` | 2026-03-25 |
| Where the amortisation lands | Developed technology amortised straight-line over 6 years **to cost of revenue** (≈$9.45m/yr at full run-rate) | audited | `sources/filings/2026-03-25_10-K_000013.txt:3139` | 2026-03-25 |
| Auditor's critical audit matter | E&Y flagged the $56.7m developed-technology valuation as complex, requiring significant management estimation | audited | `sources/filings/2026-03-25_10-K_000013.txt:1788-1792` | 2026-03-25 |

### 3.2 · North Star Y, Pty Ltd

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Date and what it was | 1 June 2023 — "Braze's exclusive reseller in Australia and New Zealand" | audited | `sources/filings/2025-03-31_10-K_000054.txt:2972` | 2025-03-31 |
| Total consideration | $26.8m — $20.6m cash, $6.1m Class A stock, $1.8m contingent consideration at fair value | audited | `sources/filings/2025-03-31_10-K_000054.txt:2974` | 2025-03-31 |
| Earn-out available | Capped at $10.0m for the first 12-month period and $16.0m for the second — **$26.0m** in total — on "qualified revenue performance metrics" | audited | `sources/filings/2025-03-31_10-K_000054.txt:2974` | 2025-03-31 |
| Earn-out actually paid | **Nil.** "The Company reduced the contingent consideration liability related to the acquisition of North Star Y, Pty Ltd to zero as it was determined that the sellers did not satisfy the earn-out qualifications" | audited | `sources/filings/2026-03-25_10-K_000013.txt:2569` | 2026-03-25 |
| Allocation | Goodwill $28.4m; intangibles $3.8m | audited | `sources/filings/2025-03-31_10-K_000054.txt:2976` | 2025-03-31 |
| Indemnification holdback | $2.8m, released in full during FY2025 | audited | `sources/filings/2025-03-31_10-K_000054.txt:2978` | 2025-03-31 |

## 4 · The platform

Documentation volume, API surface, data model, limits, architecture, infrastructure.

### 4.1 · Source-inventory counts

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Documentation pages (sitemap) | 1,352 | documented | `https://www.braze.com/docs/sitemap.xml` | 2026-09-01 |
| Documentation pages captured | 1,352 | documented | `data/docs_index.csv` | 2026-09-02 |
| Indexed site URLs | 6,366 across 8 sitemaps | documented | `data/site_inventory.csv` | 2026-09-01 |
| Published languages | 6 (en-us, ja, pt-br, fr, es, ko) | documented | `data/site_inventory.csv` | 2026-09-01 |
| Public repositories | 137 | documented | `data/repos.csv` | 2026-09-01 |
| Documented API endpoints | 135 | documented | `data/api_endpoints.csv` | 2026-09-02 |
| Status-page components | 132 rows = 17 group headers + 105 cluster components (15 clusters × 7) + 7 global channel + 3 global service | documented | `data/status_components.csv` | 2026-09-02 |

These are **source-inventory counts**, not claims about the product. They are the
denominators other facts are quoted against.

### 4.2 · Data ingestion and freshness

The single most load-bearing table in the documentation corpus. Braze names **four**
ingestion paths and grades each one's latency itself.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Named ingestion paths | 4: Standard CDI sync, CDI Segments (Connected Sources), CDI Canvas triggers, `/users/track` (and SDKs) | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:24` | 2026-09-02 |
| Ingestion paths Braze's own table labels "Not real-time" | 3 of 4 — Standard CDI sync, CDI Segments, CDI Canvas triggers | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:86-89` | 2026-09-02 |
| The one near-real-time path | `/users/track` / SDKs — "Near-real-time (async processing)" | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:90` | 2026-09-02 |
| Warehouse sync floor | 15 minutes; recurring syncs run "from every 15 minutes to once per month" | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:32` | 2026-09-02 |
| Faster than 15 min from a warehouse | Not self-serve — "contact your customer success manager or use REST API ingestion" | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:32` | 2026-09-02 |
| `/users/track` batching cap | 75 objects per request, combined across attributes, events and purchases (default) | documented | `sources/docs/docs__api__api_limits.md:29-31`; `…compare_data_ingestion_options.md:96` | 2026-09-02 |
| Connected-source query cap | 60-minute query runtime per connected source | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:94` | 2026-09-02 |
| CDI Canvas trigger throughput | ~3.75 million Canvas entries per hour per sync run | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:95` | 2026-09-02 |
| Warehouses supported by CDI | 4: Snowflake, Amazon Redshift, Databricks, Google BigQuery | documented | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:88` | 2026-09-02 |
| Currents export cadence | Every 5 minutes, or every 15,000 events, whichever comes first | documented | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:136` | 2026-09-02 |
| Currents commercial status | "an **optional** Braze **add-on**" — Braze's own word | documented | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:136` | 2026-09-02 |

**Conflicted:** whether the platform is "real-time" depends entirely on which path is
meant. See [`CONFLICTS.md`](CONFLICTS.md) **C-01**. Do not say "real-time" or "not
real-time" unqualified.

### 4.3 · Rate limits — the ingest/export asymmetry

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Ingest burst limit (`/users/track`) | 3,000 requests per 3 seconds for customers with data points in their pricing (= 60,000/min); other customers "configured according to your contract terms" | documented | `sources/docs/docs__api__api_limits.md:29-31` | 2026-09-02 |
| Profile-lookup export limit, customers onboarded **on/after 2024-08-22** | 250 requests per minute | documented | `sources/docs/docs__api__api_limits.md:37` | 2026-09-02 |
| Profile-lookup export limit, customers onboarded **before 2024-08-22** | 2,500 requests per minute | documented | `sources/docs/docs__api__api_limits.md:39` | 2026-09-02 |
| Size of that change | A **10× reduction** for new customers, at a dated boundary, with earlier customers grandfathered | documented | `sources/docs/docs__api__api_limits.md:37-39` | 2026-09-02 |
| `/users/export/ids` per-request cap | 50 external_ids or user_aliases per request | documented | `sources/docs/docs__api__endpoints__export__user_data__post_users_identifier.md:18` | 2026-09-02 |
| Resulting per-minute ceilings | Write ≈4.5m objects/min (60,000 req × 75 obj) vs read-back-by-identifier ≈12,500 profiles/min (250 req × 50 ids) for a post-2024-08-22 customer | documented | derived from the two rows above; both cited there | 2026-09-02 |
| _Caveat carried with the ratio_ | These are different operations — writing event objects vs reading whole profiles — so the ratio shows design and commercial priority, not like-for-like throughput | — | `docs/FACTS.md` §4.3 | 2026-09-02 |
| Bulk export exists and is generously limited | `/users/export/segment` (export to cloud storage) sits under the default 250,000 requests/hour limit | documented | `sources/docs/docs__api__endpoints__export__user_data__post_users_segment.md:41` | 2026-09-02 |
| Shared identity-endpoint limit | 20,000 requests/min shared across `/users/delete`, `/users/alias/new`, `/users/alias/update`, `/users/identify`, `/users/merge` | documented | `sources/docs/docs__api__api_limits.md:41-47` | 2026-09-02 |
| Broadcast send limit | 250 requests/min across all audiences and 10/min per unique audience, whichever hits first | documented | `sources/docs/docs__api__api_limits.md:68` | 2026-09-02 |

### 4.4 · Architecture

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Named backing stores | Snowflake, Kafka, MongoDB, Redis | documented | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:32` | 2026-09-02 |
| MongoDB-backed features | Custom events, custom attributes, user profiles, purchase events, most segmentation and targeting | documented | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:46-56` | 2026-09-02 |
| Snowflake-backed features | SQL Segment Extensions, Prediction Suite, AI Personalized Item Recommendations, Estimated Real Open Rate | documented | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:58-68` | 2026-09-02 |
| Admitted consequence of the split | "Removing data from one system does not automatically remove it from the other" — deleting erroneous custom-event data must be addressed in MongoDB separately from Snowflake | documented | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:70` | 2026-09-02 |
| Regional clusters on the status page | 15: US 01–US 08, US 10, EU 01, EU 02, AU 01, ID 01, JP 01, KR 01 | documented | `data/status_components.csv` | 2026-09-02 |
| US 09 | Not present on the status page. US clusters run 01–08 then 10 | documented | `data/status_components.csv` | 2026-09-02 |
| Subsystems exposed per cluster | 7, identical in every cluster: Dashboard, SDK Data Collection, Data Processing, REST APIs, Outbound Messaging, Currents, Cloud Data-Ingestion (CDI) | documented | `data/status_components.csv` | 2026-09-02 |
| Channel delivery is modelled globally, not per cluster | "Global Messaging Channels" is a single group of 7 (Email, SMS, In-App Messaging, WhatsApp, Push iOS, Push Android, Content Cards) | documented | `data/status_components.csv` | 2026-09-02 |
| Independent corroboration of the cluster geography | The sub-processor disclosure lists AWS regions US, EU, Australia, Indonesia (backup Singapore), Japan, South Korea (backup Japan) — the same six geographies the cluster names use | documented | `sources/clean/braze-subprocessors.md:21` | 2026-09-02 |

### 4.5 · Identity and the data model

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Aliases per user profile | No limit — "There's no limit to the number of aliases that you can set against a user profile" | documented | `sources/docs/docs__user_guide__data__unification__user_data__user_profile_lifecycle.md:106` | 2026-09-02 |
| Aliases per label | One — "Users can have only one alias for a specific label"; an alias_name must be unique per label across the user base | documented | `sources/docs/docs__api__endpoints__user_data__post_user_identify.md:32`; `…user_profile_lifecycle.md:108` | 2026-09-02 |
| Identifiers accepted on ingest | 5 for CDI sync and `/users/track`: external_id, user alias, braze_id, email, phone | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:113-118` | 2026-09-02 |
| Identifiers accepted for warehouse segmentation | 1 — CDI Segments must output `external_user_id` only | documented | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:113-118` | 2026-09-02 |
| Merge is silent when it declines | If both profiles have invalid phone numbers Braze does not merge them, but "the endpoint still returns 202 Accepted with a success message, so the HTTP response does not indicate that the merge was skipped" | documented | `sources/docs/docs__api__endpoints__user_data__post_users_merge.md:178` | 2026-09-02 |
| Profiles that never merge | Users marked for deletion, and Global Control Group users (merging would change random bucket numbers and affect experiments) | documented | `sources/docs/docs__user_guide__audience__manage_audience__merge_duplicate_users__merge_behavior.md:56-72` | 2026-09-02 |
| Post-merge reporting splits across surfaces | Dashboard campaign summaries attribute a pre-merge send to the surviving profile; Currents, Query Builder and Messaging History still attribute it to the orphaned profile's user ID | documented | `sources/docs/docs__user_guide__data__unification__user_data__user_profile_lifecycle.md:92-94` | 2026-09-02 |
| Orphaned profiles | "Orphaned users are not eligible to receive messages" | documented | `sources/docs/docs__user_guide__data__unification__user_data__user_profile_lifecycle.md:98` | 2026-09-02 |

### 4.6 · What a customer is billed for

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| The billable unit | "Data points" — "a billable unit of use of the Braze Services, measured by a session start, session end, custom event, or purchase recorded, as well as any attribute set on an end user profile" | documented | `sources/docs/docs__user_guide__data__infrastructure__data_points.md:18` | 2026-09-02 |
| Each counts separately | Every such item set on a profile "at one point in time shall each count as a single data point" — a session start and a session end are two | documented | `sources/docs/docs__user_guide__data__infrastructure__data_points.md:18` | 2026-09-02 |
| What is **not** billed | Push tokens, device information, and all campaign engagement tracking (email opens, push clicks); also user deletion, Connected Content in messaging, subscription-state changes, external-ID renames, blocked events/attributes | documented | `sources/docs/docs__user_guide__data__infrastructure__data_points.md:20,44-54` | 2026-09-02 |
| Braze's own cost advice to customers | "Don't waste data points. Only update changing data!" — and "we recommend setting up a program to prevent sending the same unchanging data" | documented | `sources/docs/docs__user_guide__data__infrastructure__data_points.md:36-38` | 2026-09-02 |
| Billing dashboard freshness | Data point usage is "cached (not real-time) every 24 hours around 2 am ET" | documented | `sources/docs/docs__user_guide__data__infrastructure__data_points.md:30` | 2026-09-02 |

### 4.7 · One instance is not on the same cloud as the others

Three independent sources, none of them a marketing page. This is the project's clearest
example of the method working: a compelled disclosure read for what it omits, an
append-only log read for what was provisioned, and a public registry used to check both.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Hosting providers named in the sub-processor disclosure | 2 — Amazon Web Services ("Third-party hosting provider") and Google LLC ("Third party hosting provider of Google Cloud Platform"). Microsoft is not named anywhere in the document | documented | `sources/clean/braze-subprocessors.md:21,31` | 2026-09-02 (rev. 1 June 2026) |
| Hosting providers named in the **10-K** | "We rely upon third-party providers of cloud-based infrastructure, **including Amazon Web Services and Rackspace**, to host our products." Microsoft is not named | audited | `sources/filings/2026-03-25_10-K_000013.txt:631` | 2026-03-25 |
| So two independent company documents name hosting providers | Neither names Microsoft — the sub-processor disclosure and the 10-K risk factors | documented / audited | `sources/clean/braze-subprocessors.md:21,31`; `sources/filings/2026-03-25_10-K_000013.txt:631` | 2026-09-02 |
| Braze publishes per-instance allowlist IPs | Yes — the IP addresses a customer must allow so Braze can reach their warehouse for Connected Sources, listed per instance | documented | `sources/docs/docs__user_guide__data__unification__cloud_ingestion__connected_sources.md:239,431,615,801` | 2026-09-02 |
| Registered owner of the **US-08** allowlist IPs | **Microsoft Corporation** — all 7 addresses checked, across the 40.74.0.0–40.125.127.255 and 52.145.0.0–52.191.255.255 ranges | infrastructure | `sources/external/rdap-instance-ip-ownership_2026-09-02.json` (ARIN RDAP) | 2026-09-02 |
| Registered owner of every other instance's allowlist IPs | Amazon entities — Amazon Technologies Inc., Amazon Data Services Northern Virginia, A100 ROW GmbH (Frankfurt), Amazon Corporate Services Pty Ltd (Sydney), Amazon AS-AP (Seoul) | infrastructure | `sources/external/rdap-instance-ip-ownership_2026-09-02.json` (ARIN RDAP) | 2026-09-02 |
| Exhaustiveness of that check | Every instance for which Braze publishes an IP list — US-08, US-10, AU-01, ID-01, JP-01, KR-01 and the generic US block — was checked. US-08 is the only one on Microsoft ranges | infrastructure | `sources/docs/…connected_sources.md`; `sources/external/rdap-instance-ip-ownership_2026-09-02.json` | 2026-09-02 |
| Certificate transparency agrees | 50 hosts sit on region codes `p-aze-us` (31), `s-aze-us` (12), `d-aze-us` (7) — a code matching no AWS region identifier, where every other code does (`p-use-1`, `p-apne-1`, `p-apse-2`, `s-euc-1`, `d-usw-2`…). Hosts on it include `sdk-us08…`, `subcenter-08…`, `itp-api-08…`, tying the code to instance 08 | infrastructure | `data/subdomains.csv` | 2026-09-02 |
| _How to say this_ | State the three observations and stop. Do not assert a disclosure failure: a hosting arrangement may fall outside a sub-processor listing for reasons not visible from outside. The open question is recorded in [`QUESTIONS.md`](QUESTIONS.md) | — | `docs/FACTS.md` §4.7 | 2026-09-02 |

### 4.8 · Reliability, measured over a decade

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Incidents on the public status page | 451, 2016-10-09 → 2026-08-05 | documented | `data/incidents.csv` | 2026-09-02 |
| Incidents per year | 2016:18 (from Oct) · 2017:37 · 2018:38 · 2019:49 · 2020:57 · 2021:48 · 2022:39 · 2023:60 · 2024:43 · 2025:27 · 2026:35 (to August) | documented | `data/incidents.csv` | 2026-09-02 |
| Peak and trough | Peak 2023 (60); quietest full year 2025 (27) | documented | `data/incidents.csv` | 2026-09-02 |
| 2026 run-rate | 35 in 8 months ≈ 4.4/month, against 2.25/month in 2025 — running roughly double the quietest year | documented | derived from `data/incidents.csv` | 2026-09-02 |
| Incident duration | Median 79 minutes; mean 143; p90 311 (5.2 hours); longest 1,398 minutes (23.3 hours) | documented | `data/incidents.csv` (448 of 451 carry a duration) | 2026-09-02 |
| Severity mix | minor 193 · maintenance 120 · none 40 · major 73 · critical 25. Excluding maintenance, 98 of 331 (29.6%) were major or critical | documented | `data/incidents.csv` | 2026-09-02 |
| Which components recur | Dashboard 63 · SDK Data Collection 46 · REST APIs 37 · Outbound Messaging 27 · Data Processing 26 · Currents 14 · CDI 13 | documented | `data/incidents.csv` | 2026-09-02 |
| The shape that reads out of it | The control plane (Dashboard, 63) is named in more incidents than the sending path (Outbound Messaging, 27) | documented | derived from `data/incidents.csv` | 2026-09-02 |
| _Caveat carried with all of it_ | Never compare this against a vendor that publishes no status page. A decade of visible incidents is a disclosure practice, not a defect count | — | `docs/FACTS.md` §4.8 | 2026-09-02 |

### 4.9 · The engineering record

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Public repositories | 137, of which 33 are SDK-related | documented | `data/repos.csv` | 2026-09-02 |
| SDK repos publishing releases | 9, with 494 releases, 2016-12-13 → 2026-09-01 | documented | `data/sdk_releases.csv` | 2026-09-02 |
| Most recent release across those 9 | Every one shipped within the last 13 days as at 2026-09-02 | documented | `data/sdk_releases.csv` | 2026-09-02 |
| Documented platforms whose SDK repo is idle > 6 months | 1 — `braze-roku-sdk`, 181 days since last push, not archived, 38 documentation pages still live | documented | `data/repos.csv`; `sources/docs/` (38 files matching "roku") | 2026-09-02 |
| Archived SDK repos | 6, including `braze-unreal-sdk` (archived) | documented | `data/repos.csv` | 2026-09-02 |
| What happened to the retired platform's docs | Unreal has **zero** documentation pages and zero site pages — the repo was archived and the documentation removed with it | documented | `data/repos.csv`; `sources/docs/` (0 files matching "unreal"); `data/site_inventory.csv` | 2026-09-02 |
| Public issues captured | 845, every one opened by a non-member of the org | documented | `data/issues.csv` | 2026-09-02 |
| Issue resolution | 822 of 845 closed (97.3%); median 11 days to close; 47% within 7 days; 64% within 30 days; 37 took more than a year | documented | `data/issues.csv` | 2026-09-02 |
| Issues opened per year | 2022:132 · 2023:181 · 2024:164 · 2025:129 · 2026:61 (to September) | documented | `data/issues.csv` | 2026-09-02 |
| _Caveat carried with the issue corpus_ | Issue authors are developers, not buyers. This describes the SDK surface, not the dashboard, and it is **not** a satisfaction measure | — | `docs/FACTS.md` §4.9 | 2026-09-02 |

## 5 · Channels, delivery and partnerships

Which channels exist, which are marketed, who delivers each one.

### 5.1 · The channel roster, counted from both directions

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Channels in Braze's own docs channel index | 12 — in-product: in-app messages, Content Cards, Banners; out-of-product: Email, Transactional email, Landing pages, LINE, Live notifications, Push, SMS/MMS/RCS, Webhooks, WhatsApp | documented | `sources/docs/docs__user_guide__channels.md:14-64` | 2026-09-02 |
| Channels documented in total | 13 — the 12 above plus KakaoTalk | documented | `sources/docs/docs__user_guide__channels.md:14-64`; `sources/docs/docs__user_guide__channels__kakaotalk__*.md` (4 pages) | 2026-09-02 |
| KakaoTalk is documented but not indexed | 4 KakaoTalk doc pages exist (setup, create message, click tracking, reporting) and the channels index page mentions KakaoTalk zero times | documented | `sources/docs/docs__user_guide__channels.md` (0 hits); `sources/docs/docs__user_guide__channels__kakaotalk__*.md` | 2026-09-02 |
| KakaoTalk **is** marketed | `/product/kakaotalk-messenger` exists, in 2 languages | claimed | `data/site_inventory.csv` | 2026-09-01 |
| Documented channels with no dedicated marketing product page | 5 — Banners, Transactional email, Landing pages, Live notifications, Webhooks | documented / claimed | `data/site_inventory.csv` (0 `/product/` or `/solutions/` matches for each); docs pages exist for all five | 2026-09-02 |
| Size of the largest unmarketed channel | Landing pages — 11 `user_guide/messaging/landing_pages` doc pages plus 3 partner pages, and no marketing product page | documented | `sources/docs/docs__user_guide__messaging__landing_pages*.md`; `data/site_inventory.csv` | 2026-09-02 |
| Language depth differs sharply by channel | `/product/line` in 4 languages; `/product/kakaotalk-messenger` in 2 | claimed | `data/site_inventory.csv` | 2026-09-01 |

### 5.2 · Who actually delivers each channel — the sub-processor disclosure

Legally compelled to be complete, revision **1 June 2026**. Graded `documented` per
[`EVIDENCE-GRADES.md`](EVIDENCE-GRADES.md), with the note that it is a *compelled*
disclosure, which is what gives it force.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Third-party sub-processors | 17 | documented | `sources/clean/braze-subprocessors.md:21-37` | 2026-09-02 |
| Braze group entities | 15, across 14 territories | documented | `sources/clean/braze-subprocessors.md:41` | 2026-09-02 |
| Email delivery providers named | 3 — Amazon SES, Bird.com (SparkPost), Twilio (SendGrid) | documented | `sources/clean/braze-subprocessors.md:21,23,37` | 2026-09-02 |
| Mobile-message (SMS) delivery providers named | 2 — Infobip, Twilio | documented | `sources/clean/braze-subprocessors.md:32,37` | 2026-09-02 |
| Channels with **no** delivery sub-processor named | Push, in-app messages, Content Cards, Banners, Webhooks, WhatsApp, LINE, KakaoTalk, Landing pages, Live notifications — every documented channel except email and SMS | documented | `sources/clean/braze-subprocessors.md:21-37` | 2026-09-02 |
| _Caveat carried with that row_ | Absence from a sub-processor list is not proof of no intermediary: platform transports such as APNs and FCM, and the WhatsApp/LINE/Kakao business APIs, may not be classified as sub-processors processing personal data on Braze's behalf. State it as what the disclosure names, not as what exists | — | `sources/clean/braze-subprocessors.md` | 2026-09-02 |
| Hosting providers | Amazon Web Services and Google Cloud Platform (both named as third-party hosting providers) | documented | `sources/clean/braze-subprocessors.md:21,31` | 2026-09-02 |
| Where end-user profiles are stored | Rackspace US, Inc. — "Database Administration as a Service (DBaaS), a managed database service provider that hosts and stores End User profiles" | documented | `sources/clean/braze-subprocessors.md:35` | 2026-09-02 |
| Monitoring receives user identifiers | "Braze may provide End User metadata, such as user identifiers, to DataDog" | documented | `sources/clean/braze-subprocessors.md:27` | 2026-09-02 |
| AWS regions named | United States, European Union, Australia, Indonesia (with backup in Singapore), Japan, South Korea (with backup in Japan) | documented | `sources/clean/braze-subprocessors.md:21` | 2026-09-02 |
| Technology partners ("Alloys") | "over 150" | claimed | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:82` | 2026-09-02 |

## 6 · The AI

What is shipped ML, what is agentic, what is renaming — counted, on four lenses.
**Never assert thinness. State the counts and let the ratio speak.**

### 6.1 · Lens 1 — documentation volume (focused pages, ≥5 mentions in body, of 1,352)

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Recommendations | 73 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |
| BrazeAI (umbrella brand) | 32 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |
| Generative AI | 26 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |
| Decisioning Studio | 22 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |
| Agents | 17 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |
| Intelligent Timing / Channel | 13 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |
| Predictive Suite (shipped ML) | 7 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |
| The comparison that matters | Canvas 249, Email 347, Segmentation 242, Liquid templating 123 focused pages | documented | `data/capabilities.csv` | 2026-09-02 |

### 6.2 · Lens 2 — published API surface

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Documented REST endpoints | 135, across 28 top-level namespaces | documented | `data/api_endpoints.csv` | 2026-09-02 |
| Endpoints in an AI/ML/prediction/recommendation/agent/decisioning namespace | 0 | documented | `data/api_endpoints.csv` — exhaustive check over all 135 paths | 2026-09-02 |
| For contrast, endpoints per established capability | Canvas 10, Catalogs 9, Subscription management 9, Identity 8, Email 16 | documented | `data/capabilities.csv` | 2026-09-02 |

### 6.3 · Lens 3 — who supplies the models

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| External foundation-model providers named as sub-processors | 3 — Anthropic PBC, OpenAI OpCo LLC, and Google LLC, each "provides artificial intelligence models and machine learning infrastructure to support data processing and advanced platform features" | documented | `sources/clean/braze-subprocessors.md:22,31,34` | 2026-09-02 |

### 6.4 · Lens 4 — the words customers use

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| AI mentions in the captured review panels | 13 across G2 (9), TrustRadius (2), Gartner (1), Glassdoor (1) | third-party | `sources/panels/*.md` | 2026-09-02 |
| What the positives name | "AI Advisor… a strong addition, providing robust capabilities and useful insights"; "SQL Query Builder with AI assistant"; "the AI personalization tool" | third-party | `sources/panels/g2.md:99,74`; `sources/panels/gartner.md:100` | 2026-09-02 |
| What the criticisms name | Two reviewers on G2 independently single out the AI copywriting assistant as needing "a careful human hand"; a TrustRadius reviewer says "AI features feel half baked" | third-party | `sources/panels/g2.md:137,189`; `sources/panels/trustradius.md:89` | 2026-09-02 |
| TrustRadius's own synthesis | "the platform's cost, particularly for advanced AI features, is a recurring consideration" | third-party | `sources/panels/trustradius.md:49` | 2026-09-02 |

## 7 · The verdicts

Synthesis. Nothing enters this section that is not derived from a numbered section above.

_Pending._

## 8 · Customers, market and competition

Customer count and how it is defined, geography, segment mix, who buyers shortlist.
Customer counts and financial metrics live in §2.4 — they are audited and belong there.

### 8.1 · Three customer rosters that must never be merged

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| The 10-K's defined metric | 2,609 customers as at 2026-01-31 | audited | `sources/filings/2026-03-25_10-K_000013.txt:1379` | 2026-03-25 |
| **What that metric counts** | "We define a customer as the separate and distinct, **ultimate parent-level entity** that has an active subscription" — so a group with ten brands on Braze is **one** customer. See CONFLICTS **C-08** | audited | `sources/filings/2026-03-25_10-K_000013.txt:1381` | 2026-03-25 |
| Customers, FY2022 → FY2026 | 1,375 · 1,770 · 2,044 · 2,296 · 2,609 | audited | the "we had N customers" line in each 10-K, FY2022–FY2026 | 2026-09-02 |
| Customer concentration | **None.** "For fiscal years ended January 31, 2026 and 2025, **no customer accounted for 10% or more of total revenue**" | audited | `sources/filings/2026-03-25_10-K_000013.txt:2173` | 2026-03-25 |
| Transacted prices found in any captured source | **Zero.** No rate card, procurement award or quoted contract value appears anywhere in the corpus. The ~$283,000 figure is a bound and has no corroborating price | — | exhaustive search of `sources/panels/`, `sources/docs/`, `sources/filings/` | 2026-09-02 |
| Self-selected published stories | 178 `customers/` URLs in the site inventory | claimed | `data/site_inventory.csv` | 2026-09-01 |
| Independent detection | Not attempted in this run. Recorded as a gap, not as zero | — | [`QUESTIONS.md`](QUESTIONS.md) | 2026-09-02 |

### 8.2 · Who they name, and who buyers actually compare them against

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Competitors named in the 10-K | 4 — Adobe, Salesforce, Iterable, Klaviyo | audited | `sources/filings/2026-03-25_10-K_000013.txt:502` | 2026-03-25 |
| The 10-K's own framing | "we believe that none of our competitors currently offer comparable comprehensive customer engagement solutions" | audited | `sources/filings/2026-03-25_10-K_000013.txt:502` | 2026-03-25 |
| Gartner's buyer-derived shortlist | 8 — Salesforce, Adobe, Iterable, Oracle, Optimove, Blueshift, MoEngage, CleverTap | third-party | `sources/panels/gartner.md:113-121` | 2026-09-02 |
| Overlap | 3 of the 4 Braze names appear on the buyer shortlist (Adobe, Salesforce, Iterable) | third-party | derived from the two rows above | 2026-09-02 |
| Named by Braze, absent from the buyer shortlist | Klaviyo | third-party | derived from the two rows above | 2026-09-02 |
| On the buyer shortlist, absent from the 10-K | 5 — Oracle, Optimove, Blueshift, MoEngage, CleverTap | third-party | derived from the two rows above | 2026-09-02 |
| Where Gartner reviewers rate Braze higher than the two largest alternatives | vs Salesforce: service and support, integration/deployment, evaluation and contracting. vs Adobe: service and support, integration/deployment | third-party | `sources/panels/gartner.md:124-127` | 2026-09-02 |

### 8.3 · What customers say — aggregate panel figures

Quote these site-level aggregates, **not** the 14-record captured sample. The sample is
for vocabulary and theme, never for a percentage.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| G2 | 4.5/5 from 1,702 reviews; distribution 5★ 1,136 · 4★ 520 · 3★ 34 · 2★ 5 · 1★ 7 | third-party | `sources/panels/g2.md:46-47` | 2026-09-02 |
| Gartner Peer Insights | 4.5/5 from 263 ratings; 48% five-star, 46% four-star, 6% three-star, 0% at two and one | third-party | `sources/panels/gartner.md:41-42` | 2026-09-02 |
| TrustRadius | 8.8/10 from 348 reviews and ratings | third-party | `sources/panels/trustradius.md:41` | 2026-09-02 |
| Glassdoor | 4.1/5 from 524 ratings; 82% would recommend; 90% CEO approval; 71% positive business outlook | third-party | `sources/panels/glassdoor.md:68-71` | 2026-09-02 |
| G2's own coded pros | Ease of Use 385 · Intuitive 188 · Customer Support 151 · Helpful 148 · Features 138 | third-party | `sources/panels/g2.md:54-57` | 2026-09-02 |
| G2's own coded cons | Missing Features 140 · Learning Curve 139 · Limitations 102 · Limited Features 93 · Steep Learning Curve 86 | third-party | `sources/panels/g2.md:54-57` | 2026-09-02 |
| TrustRadius's coded stat | Reporting "often described as limited and unintuitive, a sentiment shared by 36% of reviewers" (of 36 reviews in the last 18 months) | third-party | `sources/panels/trustradius.md:44-46` | 2026-09-02 |
| Themes coded by script across the whole corpus | `tools/code_reviews.py` over 860 records (841 of them GitHub issues): complaints — bugs/reliability 50.2%, documentation 20.6%, implementation 15.3%, reporting/export 13.4% | third-party | `data/review_themes.csv` | 2026-09-02 |
| The panels disagree with themselves | Glassdoor 563 reviews (search page) vs 524 ratings (company page); Gartner 263 Ratings vs 267 Verified Reviews; TrustRadius 348 Reviews and Ratings vs 162 under the default filter. See CONFLICTS **C-06** | third-party | `sources/panels/glassdoor.md:56,71`; `sources/panels/gartner.md:45,55`; `sources/panels/trustradius.md:42,64` | 2026-09-02 |
| _Denominator discipline_ | The 860-record denominator is dominated by GitHub issues, which are developer reports, not buyer satisfaction. Say "of the N records coded", never "of all reviews" | — | `data/review_themes.csv`; `tools/code_reviews.py` | 2026-09-02 |

### 8.4 · What employees say

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Glassdoor overall | 4.1/5 from 524 ratings | third-party | `sources/panels/glassdoor.md:68` | 2026-09-02 |
| Work-life balance trend | Flat over the six months to September 2026, tracking the overall rating (~4.0–4.1); no divergence | third-party | `sources/panels/glassdoor.md:88-92` | 2026-09-02 |
| What Glassdoor's own summary names as the weak spots | Management effectiveness and "clarity in direction"; "limited upward mobility and discrepancies in compensation relative to market rates" | third-party | `sources/panels/glassdoor.md:78-84` | 2026-09-02 |
| Open roles on the careers board | **296**, on the company's own Greenhouse board | documented | `data/careers_departments.csv`; `sources/external/greenhouse-board-braze_2026-09-02.json` | 2026-09-02 |
| Functions hired for | 15 departments carry at least one open role, of 21 listed on the board: Business Development, Customer Experience, Engineering, Finance, Growth, GTM Operations, GTM Strategy, Information Technology, Legal, Marketing, Partnerships, People, Product, Sales, Solutions Consulting | documented | `data/careers_departments.csv` | 2026-09-02 |
| The three largest | Sales **89**, Engineering **57**, Customer Experience **38** | documented | `data/careers_departments.csv` | 2026-09-02 |
| Go-to-market share of open roles | **213 of 296 — 72.0%** (Sales, Customer Experience, Marketing, Solutions Consulting, Partnerships, Growth, Business Development, GTM Strategy, GTM Operations) | documented | `data/careers_departments.csv` | 2026-09-02 |
| Engineering and Product share | **58 of 296 — 19.6%.** Go-to-market outnumbers product-building roles **3.7 to 1** | documented | `data/careers_departments.csv` | 2026-09-02 |
| _How to read the ratio_ | A requisition is an intention, not a person, and a sales req costs less than an engineering one — so this is not a spend ratio and must not be quoted as one. The audited spend ratio is S&M 1.96× R&D (§2.3), which is a different and smaller number pointing the same way | — | `data/financials_annual.csv`; `data/careers_departments.csv` | 2026-09-02 |
| Hiring locations | 26 distinct location strings on the page capture, including Bucharest — which matches "Braze Ireland Procurement Limited … Ireland & Romania" in the sub-processor disclosure | claimed / documented | `sources/panels/jobs.md:58-63`; `sources/clean/braze-subprocessors.md:41` | 2026-09-02 |
| _Superseded_ | The earlier "~284–300 across 25 pages of 12" was a front-of-list estimate from the board's web UI. The board's own JSON gives 296 exactly, inside that range. See the corrections table | claimed | `sources/panels/jobs.md:44-46` | 2026-09-02 |

---

## Numbers that were wrong and are now right

**Every correction goes here with the old value still visible**, so that a stale copy of
a deck or a document can be recognised on sight. A file that shows its own errors is the
reason to trust the rest of it. Four corrections are recorded below; the same table is
mirrored in the evidence record.

| Fact | Was | Is now | Why it changed | Date |
|---|---|---|---|---|
| Status-page component grouping | "132 in 12 groups" | 132 rows in **17 named groups** — 15 regional clusters × 7 components, plus Global Messaging Channels (7) and Global Services (3), plus the 17 group-header rows themselves | The setup-time reconnaissance counted groups by eye. Counting `data/status_components.csv` gives 17 named groups and 15 regional clusters, not 12. `DECK-SPEC.md` also says "12 named regional clusters" and is wrong for the same reason | 2026-09-02 |
| Capability focused-page counts | Journey orchestration 319 · Identity resolution 136 · Ingestion & streaming 172 · Segmentation 339 | Canvas (journeys) 249 · Identity (external_id / alias) 110 · Cloud Data Ingestion (CDI) 30 · Segmentation 242 | **The pattern set moved, not the product.** `docs/CAPABILITY-TAXONOMY.tsv` was revised on 2026-09-02 from generic category words to Braze's own product names, as the handoff report required. Any comparison between a pre- and post-revision count is meaningless; both runs are reproducible from the `pattern` column in `data/capabilities.csv` | 2026-09-02 |
| KakaoTalk's marketing status | Provisionally read as "documented but not marketed" during the first pass | **Marketed** — `/product/kakaotalk-messenger` exists. The finding inverts: KakaoTalk is marketed but absent from Braze's own documentation channel index | A first grep for `product/kakao` was truncated and appeared to return nothing. Checking the full `/product/` enumeration found the page | 2026-09-02 |
| Open roles, and the split by function | "~284–300 across 25 pages of 12", with the per-department split recorded as uncapturable (open question 56) | **296 open roles across 15 hiring departments**, with the exact split — Sales 89, Engineering 57, Customer Experience 38 and so on | The estimate came from paging the careers board's web UI, whose Department filter would not drive under automation. Greenhouse publishes the same board as unauthenticated JSON with the grouping already done: `tools/careers_board.py` fetches it, and the count lands inside the earlier range. The lesson is the general one — **when a page will not yield, look for the API behind it before recording a gap** | 2026-09-02 |

---

## Source-inventory reconnaissance, 2026-09-01

Recorded so the first research run knows what to expect and can tell a *changed* source
from a *broken* one. These describe sources, not Braze.

| Source | Observed | Note |
|---|---|---|
| SEC filings | 737, 2017-07-20 → 2026-08-28 | 5×10-K, 14×10-Q, 32×8-K, 5×DEF 14A, 439×Form 4 |
| SEC XBRL | 357 us-gaap concepts, 2019-01-31 → 2026-04-30 | no restatements among the 29 key concepts |
| Docs sitemap | 1,352 URLs | |
| Site sitemaps | 6,366 URLs, 6 languages | `resources` 2,618 · `customers` 178 · `press-releases` 95 |
| GitHub `braze-inc` | 137 repos; 494 releases in 9 SDK repos | 2016-12-13 → 2026-09-01 |
| Status page | 132 components, 451 incidents | 2016-10-09 → 2026-08-05 |
| `security.txt` | present, 236 bytes | its **absence** was a finding on the reference project |
| crt.sh | HTTP 502 all day | retry; Cert Spotter returned 167 names then rate-limited |
| G2 / Gartner / Glassdoor / TrustRadius | HTTP 403 to scripts | browser session or human paste required |
