# The company

> Braze is a fifteen-year-old New York software company that has been public since November 2021, and as of January 2026 it is no longer controlled by its founders through super-voting stock. Almost everything in this record is knowable because of that listing.

{{slides: 4, 5, 7}}

## 1.1 · The entity

| Fact | Value | Grade | Source |
|---|---|---|---|
| SEC registrant | Braze, Inc. | [[audited]] | `data/filings.csv` |
| CIK / ticker | 0001676238 / BRZE (Nasdaq) | [[audited]] | `data/filings.csv` |
| SIC classification | 7372 Services-Prepackaged Software | [[audited]] | `data/filings.csv` |
| Fiscal year end | 31 January | [[audited]] | `data/filings.csv` |
| Founded and incorporated | 2011, in Delaware | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:249,598` |
| Headquarters | 28 East 28th Street, Floor 12, New York, NY 10016 | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:598` |

Fiscal years end on 31 January, so "FY2026" means the year to 31 January 2026. This
matters more than it looks: XBRL's `fy` field labels the *filing*, not the period, and
reading it directly mislabels every year in the series. `tools/sec_facts.py` derives a
correct `period` column and every figure in chapter 2 keys on that.

{{src: data/filings.csv @ 2026-09-01}}

## 1.2 · Going public, and the end of founder control

| Fact | Value | Grade | Source |
|---|---|---|---|
| S-1 filed | 22 October 2021 | [[audited]] | `data/filings.csv` |
| Final prospectus (424B4) | 18 November 2021 | [[audited]] | `data/filings.csv` |
| Dual-class structure | Ended 30 January 2026 | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:1197` |

The governance change is recent enough to be easy to miss and material enough to matter.
On 30 January 2026 the Class B common stock was retired and automatically converted into
Class A, and the 10-K states the consequence plainly: "our executive officers and early
investors no longer hold super-voting rights. Consequently, our voting power is now more
widely distributed among our public stockholders."

For a competitor, the practical reading is that a company whose direction was until very
recently insulated from its own shareholders is now not. Nothing in the evidence says
what Braze will do with that; it is a change in who can apply pressure, and it is nine
months old.

{{src: sources/filings/2026-03-25_10-K_000013.txt:1197 @ 2026-03-25}}

## 1.3 · People and footprint

| Fact | Value | Grade | Source |
|---|---|---|---|
| Full-time employees | 1,988 as at 31 January 2026 | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:590` |
| Legal entities in the group | 15, across 14 territories | [[documented]] | `sources/clean/braze-subprocessors.md:41` |
| Total SEC filings | 737, 2017-07-20 → 2026-08-28 | [[audited]] | `data/filings.csv` |

The employee figure is the 10-K's own, as-of a single date, and counts differently from
a LinkedIn headcount; the two are never merged here, and no LinkedIn figure was captured
in this run.

The entity list comes from the sub-processor disclosure rather than from marketing, and
it names its own territories: Australia, Brazil, Canada, France, Germany, Ireland, Spain,
United States, Ireland & Romania, Japan, South Korea, United Kingdom, United Arab
Emirates, Singapore and Indonesia. One line in it is worth noticing — "Braze Ireland
Procurement Limited" is located in "Ireland & Romania", and the careers board lists
Bucharest as a hiring location. Two unrelated documents describing the same Romanian
presence is the kind of corroboration this method is built to find.

{{src: sources/clean/braze-subprocessors.md:41 @ 2026-09-02}}

#### What would change this chapter

A merger, a take-private, or a change of control — all of which would appear as an 8-K
within four business days. A materially different headcount would appear in the next
10-K. The entity list changes when the sub-processor document is revised; this record
uses revision 1 June 2026 and any later revision supersedes it.
