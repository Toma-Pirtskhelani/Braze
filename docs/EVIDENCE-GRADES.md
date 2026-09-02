# Evidence grades

Every row in `data/`, every fact in `docs/FACTS.md`, and every claim in the record and
the deck carries one of these. They are ordered by **how hard it would be for Braze to
have made the statement untrue.**

## The five grades

| grade | source | why it sits here |
|---|---|---|
| **audited** | SEC 10-K / 10-Q / 8-K, XBRL company facts | Signed off by auditors and filed under legal penalty. Restatement is itself a filed, visible event. Strongest evidence available on this company. |
| **infrastructure** | Certificate transparency logs | Recorded by independent log operators when a certificate is issued. Append-only; Braze cannot edit or retract it. A host that appears here was really provisioned, on really that date. |
| **documented** | Technical documentation, API reference, public VCS history, status page | Self-published and written to be operationally correct — an engineer following a wrong endpoint files a ticket, and a status page is read live during an outage. Reliable about mechanism; silent about commercial reality. |
| **third-party** | G2, Gartner Peer Insights, TrustRadius, Glassdoor, LinkedIn, analyst notes | Published by someone else. Braze may curate or respond, and review panels are solicited and self-selected — independent, but not disinterested. |
| **claimed** | Marketing pages, press releases, customer stories, comparison pages | Self-published to persuade. Fine for what they claim; no support for whether it is true. |
| **conflicted** | two or more credible sources that disagree | Not a grade so much as a state. Both values are recorded, neither is chosen, and `docs/CONFLICTS.md` carries the ruling on what to say out loud. |

One source class sits awkwardly and deserves its own note: the **sub-processor
disclosure** is company-own but *legally compelled to be complete*. Grade it
`documented`, and say in the citation that it is a compelled disclosure — that is what
gives it force.

## How this differs from a private vendor

`audited` is a new top grade. It has two consequences worth stating explicitly:

1. **A marketing claim that contradicts a filing is not a conflict, it is an error.**
   With a private vendor you rarely get to make that call. Here you often can. Say it
   plainly and without drama: give the filed figure, give the marketing figure, and note
   that one of them is filed under penalty.
2. **Absence in marketing is weaker evidence than usual.** A listed company discloses
   things in the 10-K that never reach a marketing page. **Search the filings before
   calling anything absent.**

## Mapping to the deck

The record keeps five grades. The deck shows three, on the bar at the foot of every
slide:

| deck grade | record grades |
|---|---|
| **strong** (`s`) | `audited`, `infrastructure`, `documented` |
| **medium** (`m`) | `third-party` |
| **weak** (`w`) | `claimed`, `conflicted` |

More resolution is kept in the record than on the slide on purpose: the audience needs
to know how much to trust a claim, and the reader of the record needs to know exactly
why.

## Rules this repository follows

1. **A claim's grade is the grade of its weakest supporting source**, never its best.
2. **Repetition is not corroboration.** Site furniture repeated across every page is one
   claim, cited once. `tools/fetch_docs.py` strips it to `sources/boilerplate.txt`
   precisely so it cannot be counted N times.
3. **Company-declared and independent figures never merge silently.** Every CSV carries
   an `evidence` column. Where two rosters exist, keep two rosters.
4. **Absence of evidence is reported as absence of evidence**, not as absence of the
   thing — except where the check was exhaustive and is stated as such.
5. **Dates from `lastmod` and page frontmatter are suspect.** They are often build
   timestamps. Prefer CT logs, VCS history, filing dates and incident timestamps.
6. **A restated financial figure is a conflict.** `tools/sec_facts.py` writes every
   superseded value to `data/financials_restated.csv`; anything that lands there gets a
   row in `CONFLICTS.md`.

## Corpus composition by grade

Fill this in once the capture is complete — it is a useful honesty check on the whole
project. The reference project's table showed that even after a large documentation
fetch, the corpus was still overwhelmingly self-declared; what changed was that the bulk
had become *technical* self-declaration, which fails differently and much more visibly
than marketing copy does.

Filled 2026-09-02, from the capture that produced this analysis.

| grade | volume | what it is |
|---|---|---|
| **audited** | 737 filings indexed, 56 fetched as full text; 7 fiscal years of XBRL across 29 key concepts, 0 restated | 10-K, 10-Q, 8-K, DEF 14A, and `data/financials*.csv` |
| **infrastructure** | 833 certificate-transparency hosts (**partial** — crt.sh 502, Cert Spotter rate-limited); 8 RDAP registry lookups | `data/subdomains.csv`, `sources/external/rdap-instance-ip-ownership_2026-09-02.json` |
| **documented** | 1,352 documentation pages (1,565,479 words); 135 API endpoints; 137 repos; 494 SDK releases; 451 incidents; 845 public issues; 1 compelled sub-processor disclosure | `sources/docs/`, `sources/clean/`, and the derived tables in `data/` |
| **third-party** | 4 review panels — 2,837 ratings in aggregate (G2 1,702, Glassdoor 524, TrustRadius 348, Gartner 263); **14 individual review records captured** | `sources/panels/`, coded by `tools/code_reviews.py` |
| **claimed** | 6,366 site URLs, including 178 customer stories and 2,618 resource pages | `data/site_inventory.csv` |

**The honesty check this table exists for.** The corpus is still overwhelmingly
self-declared — but the bulk of it is now *technical* self-declaration, which fails
differently and much more visibly than marketing copy does. A documentation page that is
wrong generates a support ticket; a marketing page that is wrong generates nothing.

Two figures in it deserve to be read carefully rather than quoted. The
certificate-transparency host list is **partial**, so it supports claims about what was
provisioned and none at all about what is absent. And the third-party row has two
numbers on purpose: 2,837 is the base the *sites* computed their ratings over, and 14 is
what was captured here. Percentages in this analysis are quoted against the second
number and say so.
