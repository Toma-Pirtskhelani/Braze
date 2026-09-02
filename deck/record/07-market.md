# The market

> Braze sells to 2,609 customers, expansion within them is slowing, and the vendors buyers actually weigh it against are twice as many as the four it names — with the five extra all being specialists it does not mention.

{{slides: 11, 12, 13, 14, 15, 16}}

## 7.1 · Three customer counts that must never be merged

| Roster | Count | Grade | Source |
|---|---|---|---|
| The 10-K's defined metric | 2,609 as at 31 January 2026 | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:1379` |
| Self-published customer stories | 178 `customers/` URLs | [[claimed]] | `data/site_inventory.csv` |
| Independent detection | Not attempted in this run | — | open question 57 |

The first is a defined, audited metric. The second is a marketing selection. The third
was not done, and is recorded as a gap rather than as a zero — nobody should read "178"
as the customer base or as a sample of it.

## 7.2 · Expansion is slowing, and the enterprise premium has almost gone

| Measure | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Dollar-based net retention, all customers | 117% | 111% | 109% |
| Dollar-based net retention, customers ≥$500k ARR | 120% | 114% | 110% |
| Customers with ARR ≥$500k | 202 | 247 | 333 |

[[audited]] {{src: sources/filings/2026-03-25_10-K_000013.txt:1400 @ 2026-03-25}}

Two movements, and the second is easy to miss.

Net retention is falling, and Braze explains why itself: "primarily due to customer
turnover and renewals at lower subscription levels… customers renew their contracts at
levels more closely aligned with their current needs, rather than opting for larger
commitments based on anticipated future demand." That is a demand-environment
explanation, and it is the company's own.

The subtler movement is the gap. Large customers used to expand three points faster than
the average — 120% against 117% in FY2024. In FY2026 they expand one point faster, 110%
against 109%. Whatever advantage the enterprise cohort had in expansion has nearly
closed. Meanwhile the *number* of large customers has grown strongly, from 202 to 333.
Braze is winning more big accounts and growing each of them more slowly.

Average revenue per customer can be bounded but not known: $738.2m of revenue across
2,609 customers is **about $283,000 each**. That is a bound, not a price — it mixes every
contract size and includes professional services — and it should always be said as
"bounded at", never as "costs".

## 7.3 · Who they name, and who buyers actually shortlist

The 10-K names four competitors: **Adobe, Salesforce, Iterable, Klaviyo**, alongside the
claim that "none of our competitors currently offer comparable comprehensive customer
engagement solutions."

Gartner Peer Insights publishes what buyers *also considered*, derived from the buyers
rather than the vendor. That list has eight: **Salesforce, Adobe, Iterable, Oracle,
Optimove, Blueshift, MoEngage, CleverTap**.

| | Named by Braze | On the buyer shortlist |
|---|---|---|
| Adobe, Salesforce, Iterable | yes | yes |
| Klaviyo | yes | no |
| Oracle, Optimove, Blueshift, MoEngage, CleverTap | no | yes |

[[third-party]] {{src: sources/panels/gartner.md:113-121 @ 2026-09-02}}

The overlap is real — three of the four names are shared, so this is not a vendor
misreading its own market. The asymmetry is what matters: buyers weigh Braze against five
vendors it never names, and those five are mostly the mobile-engagement specialists
(MoEngage, CleverTap, Blueshift, Optimove) rather than the suite vendors Braze positions
against. A competitor briefing built only from Braze's own comparison pages would miss
five of the eight vendors in the room.

Where Gartner's reviewers rate Braze *above* the two largest alternatives, they name the
same things twice: service and support, and ease of integration and deployment — against
Salesforce, with evaluation and contracting added.

## 7.4 · What customers say

Site-level aggregates, which are the figures to quote. The captured review bodies are a
sample of fourteen records used for vocabulary and theme, never for a percentage.

| Panel | Rating | Base |
|---|---|---|
| G2 | 4.5 / 5 | 1,702 reviews |
| Gartner Peer Insights | 4.5 / 5 | 263 ratings |
| TrustRadius | 8.8 / 10 | 348 reviews |

[[third-party]] {{src: sources/panels/g2.md:46 @ 2026-09-02}}

G2's own coded tags, which are counted over its full review base rather than over the
sample captured here, put the praise at Ease of Use (385), Intuitive (188), Customer
Support (151), Helpful (148) and Features (138); and the criticism at Missing Features
(140), Learning Curve (139), Limitations (102), Limited Features (93) and Steep Learning
Curve (86). TrustRadius's synthesis adds a coded figure of its own: reporting is "often
described as limited and unintuitive, a sentiment shared by 36% of reviewers", of the 36
reviews it published in the preceding eighteen months.

Two themes recur across unrelated panels and are therefore worth more than the rest:
**reporting is the most consistent complaint**, and **learning curve is the second**.
The reporting complaint is independently consistent with the platform evidence in chapter
4 — out-of-the-box reporting being thin enough that Currents, a paid add-on, is the
route to raw data.

Running `tools/code_reviews.py` over the whole corpus produces theme percentages against
a denominator of 860 records, but 841 of those are GitHub issues rather than buyer
reviews. That denominator is stated wherever the script's output is used, and its themes
describe the SDK surface, not satisfaction.

## 7.5 · What employees say

Glassdoor, captured signed-in: **4.1 out of 5 from 524 ratings, 82% would recommend, 90%
approve of the CEO, 71% positive business outlook.**

Work-life balance tracks the overall rating almost exactly over the six months to
September 2026 — both hovering around 4.0 to 4.1 — so there is no divergence worth
calling a trend, and none is claimed. Glassdoor's own summary names the weak spots as
management effectiveness and "clarity in direction", and "limited upward mobility and
discrepancies in compensation relative to market rates".

[[third-party]] {{src: sources/panels/glassdoor.md:68-92 @ 2026-09-02}}

The careers board shows roughly 284 to 300 open roles across fifteen functions and
twenty-six locations. An exact split by function could not be captured — the board's
filter would not drive reliably — so no percentage is offered, and the gap is open
question 56 rather than an estimate.

#### What would change this chapter

A fourth consecutive year of falling net retention would turn a demand-environment
explanation into a competitive one. A new name in the 10-K competition paragraph, or a
change in the Gartner shortlist, would move §7.3. Access to any of the three paywalled
by-company-size rating breakdowns would finally settle whether satisfaction falls with
customer size — the one hypothesis this analysis could not test.
