---
name: braze
description: Answer questions about Braze (NASDAQ BRZE), the customer-engagement platform, from the researched evidence base in this repository. Use this skill whenever Braze comes up — its pricing, funding, ownership, customers, headcount, financials, architecture, channels, AI capabilities, reliability, reviews, competitors or weaknesses — even if the question does not name the repository or ask for "research". Also use it when preparing or checking the deck or the evidence record, when someone asks "is this number right?", or when deciding where to look for something not yet captured.
---

# Braze — answering from the evidence base

This repository is a research **environment**. Depending on when you are reading this,
the corpus may be complete, partial, or empty. **Check before you answer**, and never
fill a gap from memory.

```bash
ls data/*.csv 2>/dev/null | wc -l        # how much has been extracted
ls sources/docs/*.md 2>/dev/null | wc -l # how much of the corpus exists
```

If the answer is zero, say so and offer to run the capture — do not answer from
recollection. The value of this evidence base is that nothing in it is asserted.

---

## Answer in this order

**1 · `docs/FACTS.md`.** The canonical value of every number, with its grade and the path
to its source.

```bash
rg -i 'gross margin' docs/FACTS.md
```

**2 · `docs/CONFLICTS.md`, if the number is disputed.** Each entry carries a **ruling** —
the sentence to say out loud. Follow the ruling rather than picking a value.

**3 · The derived tables in `data/`.** CSV, so one command each.

```bash
rg -i '10-K' data/filings.csv | cut -d, -f1,2,8
sort -t, -k3 -rn data/capabilities.csv | head
```

**4 · Only then the corpus.** Count, then read a bounded range — see `RETRIEVAL.md`.

Going to `sources/` for something already in FACTS burns context and risks resurrecting
a figure that was corrected. FACTS has a *"numbers that were wrong and are now right"*
table for exactly that reason.

---

## What is verified about the sources

These describe the *evidence base*, not Braze's business, and each was checked on
2026-09-01. They are safe to state, and they tell you where to send a question the
corpus has not yet answered.

| | |
|---|---|
| SEC | **CIK 0001676238, ticker BRZE, Nasdaq, SIC 7372, fiscal year ends 31 January.** 737 filings, 2017-07-20 → 2026-08-28 |
| Financials | XBRL company facts: 357 us-gaap concepts, key series from 2019-01-31 |
| Documentation | 1,352 pages in the docs sitemap |
| Site | 6,366 URLs across 8 sitemaps, 6 languages; 178 customer-story pages |
| Code | `github.com/braze-inc`, 137 public repos; 494 releases across 9 SDK repos |
| Reliability | `braze.statuspage.io`: 132 components in 12 groups, 451 incidents from 2016-10-09 |
| Panels | G2, Gartner Peer Insights, TrustRadius, Glassdoor — all 403 to scripts, need a browser or a paste |

Full catalogue with addresses: `docs/SOURCES.md`.

---

## How to frame an answer

**Attach the caveat in the same sentence as the number.** A figure with its caveat in a
later paragraph is how a reader ends up misinformed.

**Never merge company-declared and independent figures.** Customer count in particular
has at least three definitions here — the 10-K's defined metric, the 178 customer-story
pages, and any independent detection. Give both, say which is which, explain the gap.

**A marketing claim that contradicts an audited filing is an error, not a conflict.**
Braze is listed, so you can often make that call. Give the filed figure, note that it is
filed under penalty, and say it plainly without drama.

**Keep the money in proportion.** Audited SEC data is abundant and quotable and it will
pull an answer toward the income statement. The question is almost always about a
product and a competitor, not a share price. No forecasts, no valuation, no
recommendation about the security.

**Never assert that a capability is "thin".** State the counts from the focused-page
measurement and let the ratio speak — and credit what deserves credit. A precise,
generous claim is much harder to rebut than a dismissive one.

**Treat absence as a finding** — but for a listed company, **search the filings before
calling anything absent.** The 10-K discloses things that never reach a marketing page.

**Say when you do not know.** `docs/QUESTIONS.md` §4 lists what public sources probably
cannot answer, each with what *would* close it. That is a better answer than a guess.

---

## Traps already hit, so you do not have to

**XBRL's `fy` field describes the filing, not the period.** Braze's FY2026 10-K reports
FY2024 and FY2025 and labels both `fy2026`. Use the derived `period` column in
`data/financials.csv`, never `filing_fy`.

**`financials_annual.csv` and `financials_quarterly.csv` are separate on purpose.**
Mixing annual and quarterly rows is the classic error in this kind of table.

**Anything in `data/financials_restated.csv` is a conflict** and needs a `CONFLICTS.md`
entry — a company disagreeing with its own earlier filing is a recorded, dated fact.

**Two UK entities are named "Braze".** `BRAZE LIMITED` (09846844) and
`BRAZE MARKETING LTD` (10711967). **Neither is confirmed as the vendor's.** Match against
the 10-K subsidiary exhibit before citing either.

**Do not hand-count review themes.** Run `tools/code_reviews.py` and cite the script.
The same corpus coded by hand three times gave three different answers on the reference
project.

---

## When the corpus does not cover it

Say so, then point at the right source rather than guessing:

| Question | Where the answer lives |
|---|---|
| A financial figure | `tools/sec_facts.py`, then `data/financials_annual.csv` |
| When something happened | `data/timeline.csv`, or 8-K rows in `data/filings.csv` |
| What was provisioned and never announced | `data/subdomains.csv`, newest first |
| Whether a platform is maintained | `data/sdk_releases.csv` by repo and date |
| What breaks, and how often | `data/incidents.csv` |
| What customers say | `sources/panels/`, coded by `tools/code_reviews.py` |
| Who buyers shortlist them against | Gartner Peer Insights shortlists — the highest-value field on any review page |
| Anything after the capture date | Not covered. Offer to re-run the relevant tool |

For the *method* behind all of this — how to run the same analysis on a different vendor
— see the `competitor-analysis` skill and `docs/METHOD.md`. That is a separate concern
and deliberately contains no Braze facts.
