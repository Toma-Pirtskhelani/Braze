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

Everything else — founding, founders, HQ, headcount, subsidiaries, ownership — is
**pending**. Sources are named in [`SOURCES.md`](SOURCES.md).

## 2 · Money

Revenue, gross margin, operating expense by line, losses, cash, RPO, dilution, SBC.

_Pending. `tools/sec_facts.py` produces every one of these as an audited series.
Nothing goes in this section that is not traceable to `data/financials*.csv`._

## 3 · Acquisitions

What was bought, when, for how much, and what it brought.

_Pending. 8-K item dates, 10-K business-combination notes, and
`PaymentsToAcquireBusinessesNetOfCashAcquired`._

## 4 · The platform

Documentation volume, API surface, data model, limits, architecture, infrastructure.

| Fact | Value | Grade | Source | As of |
|---|---|---|---|---|
| Documentation pages (sitemap) | 1,352 | documented | `https://www.braze.com/docs/sitemap.xml` | 2026-09-01 |
| Indexed site URLs | 6,366 across 8 sitemaps | documented | `data/site_inventory.csv` | 2026-09-01 |
| Published languages | 6 (en-us, ja, pt-br, fr, es, ko) | documented | `data/site_inventory.csv` | 2026-09-01 |
| Public repositories | 137 | documented | `data/repos.csv` | 2026-09-01 |
| Status-page components | 132 in 12 groups | documented | `data/status_components.csv` | 2026-09-01 |

These five are **source-inventory counts**, not claims about the product. They are here
because they are the denominators other facts will be quoted against.

## 5 · Channels, delivery and partnerships

Which channels exist, which are marketed, who delivers each one.

_Pending. The sub-processor disclosure is the highest-value source here._

## 6 · The AI

What is shipped ML, what is agentic, what is renaming — counted, on four lenses.

_Pending. See `tools/capability_count.py` and the framing rule in the `braze` skill:
never assert thinness, state the counts and let the ratio speak._

## 7 · The verdicts

Synthesis. Nothing enters this section that is not derived from a numbered section above.

_Pending._

## 8 · Customers, market and competition

Customer count and how it is defined, geography, segment mix, who buyers shortlist.

_Pending. Note that customer count has at least three definitions here — the 10-K's
defined metric, the 178 customer-story pages, and independent detection. **Never merge
them.**_

---

## Numbers that were wrong and are now right

Empty, and it will not stay that way. **Every correction goes here with the old value
still visible**, so that a stale copy of a deck or a document can be recognised on sight.
A file that shows its own errors is the reason to trust the rest of it.

| Fact | Was | Is now | Why it changed | Date |
|---|---|---|---|---|
| _(none yet)_ | | | | |

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
