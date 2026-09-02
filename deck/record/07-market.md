# The market

> Braze sells to 2,609 customers where a "customer" is an ultimate parent entity, no single one of which is 10% of revenue. Expansion within that base is slowing and the premium large accounts used to enjoy has nearly vanished. And the vendors buyers actually weigh Braze against are twice as many as the four it names — with the five extra all being specialists it does not mention.

{{slides: 11, 12, 13, 14, 15, 16}}

## 7.1 · Three customer counts that must never be merged

| Roster | Count | Grade | Source |
|---|---|---|---|
| The 10-K's defined metric | 2,609 as at 31 January 2026 | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:1379` |
| Self-published customer stories | 178 `customers/` URLs | [[claimed]] | `data/site_inventory.csv` |
| Independent detection | Not attempted in this run | — | open question 57 |

The first is a defined, audited metric. The second is a marketing selection. The third was
not done, and is recorded as a gap rather than as a zero — nobody should read "178" as the
customer base or as a sample of it.

### What the 10-K metric actually counts, and why it changes the price

Braze defines the metric precisely, and the definition does more work than the number:
**"We define a customer as the separate and distinct, ultimate parent-level entity that has
an active subscription with us to use our products."**

[[audited]] {{src: sources/filings/2026-03-25_10-K_000013.txt:1381 @ 2026-03-25}}

*Ultimate parent-level entity.* A holding company running ten retail brands on Braze counts
once. A conglomerate with separate contracts for three divisions counts once. This is a
deliberately conservative way to count and it flatters nothing — but it has a direct
consequence for the only pricing figure this analysis can produce.

Revenue divided by customers is **about $283,000**. That is a bound, not a price, and the
definition tells you what kind of bound: it is **per corporate group**, not per brand, per
seat or per contract. A single-brand startup and a group running ten brands under one
master agreement are both one unit in that denominator. The real distribution behind
$283,000 is therefore far wider than the average suggests, and skewed by construction —
which is why the 333 customers at $500k+ of annual recurring revenue is the more useful
segmentation, and why "bounded at" is the only honest verb. This is conflict **C-08**.

Two further disciplines. **No transacted price appears anywhere in the corpus** — no rate
card, no procurement award, no quoted contract value in any review, filing or
documentation page. The search was exhaustive and found nothing, so the bound stands alone
and unsupported by any real observed price. And the 178 customer stories are brands, not
parents, so they are not a subset of 2,609 in any arithmetic sense.

### The one genuinely reassuring number in this chapter

**No customer accounted for 10% or more of total revenue in FY2026 or FY2025.**

[[audited]] {{src: sources/filings/2026-03-25_10-K_000013.txt:2173 @ 2026-03-25}}

This is a required disclosure and its absence of drama is the point. A business with 2,609
parent-level customers and no concentration above 10% has no single account whose loss
would be visible in the consolidated numbers. For anyone modelling competitive risk against
Braze, there is no keystone logo to unseat — the base has to be taken account by account,
which is slow, and which the contracted-revenue position in §2.4 makes slower still.

## 7.2 · Expansion is slowing, and the enterprise premium has almost gone

| Measure | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Dollar-based net retention, all customers | 117% | 111% | 109% |
| Dollar-based net retention, customers ≥$500k ARR | 120% | 114% | 110% |
| Customers with ARR ≥$500k | 202 | 247 | 333 |
| Total customers | 2,044 | 2,296 | 2,609 |

[[audited]] {{src: sources/filings/2026-03-25_10-K_000013.txt:1400,1379 @ 2026-03-25}}

Three movements here, and the second and third are easy to miss.

**Net retention is falling**, and Braze explains why itself
(`sources/filings/2026-03-25_10-K_000013.txt:1400`): "primarily due to customer
turnover and renewals at lower subscription levels… customers renew their contracts at
levels more closely aligned with their current needs, rather than opting for larger
commitments based on anticipated future demand." That is a demand-environment explanation,
it is the company's own, and it is plausible — every subscription vendor said a version of
it over this period. It is worth noting what it is *not*: it is not an explanation
involving competitive loss, and Braze does not offer one anywhere in
`sources/filings/2026-03-25_10-K_000013.txt`.

**The enterprise premium has nearly closed.** Large customers used to expand three points
faster than the average — 120% against 117% in FY2024. In FY2026 they expand one point
faster, 110% against 109%. Whatever advantage the large-account cohort had in expansion has
almost gone. This is the subtler and more consequential movement, because expansion within
large accounts is where a platform business earns its multiple, and it is the mechanism by
which land-and-expand is supposed to work.

**And yet the number of large accounts is growing fast** — 202 to 333 in two years, a rise
of about 65% while the total customer count grew about 28%. So Braze is winning
substantially more big accounts and growing each of them more slowly.

Those three facts together describe a specific transition, and naming it is more useful
than any one of them alone: **Braze is shifting from an expansion business to an
acquisition business.** Growth increasingly comes from new large logos rather than from
existing ones getting larger. That is a harder, more expensive way to grow — it is
consistent with a sales-and-marketing line that, despite falling every year, is still the
largest single cost in the business (§2.3) — and it is the pattern that makes the RPO figure in §2.4 the right thing to watch.
Retention above 100% still means the base grows without a single new customer; but at 109%
it grows slowly, and the burden shifts to the new-logo engine.

Note also what these figures cannot tell you. Dollar-based net retention is not
satisfaction, and it is not a competitive win-rate. It nets expansion against contraction
and churn across a whole cohort, so a company could lose accounts to a competitor and still
report 109% if the survivors expanded enough. It is the closest audited proxy available for
the health of the base, and it is a proxy.

## 7.3 · Who they name, and who buyers actually shortlist

The 10-K names four competitors: **Adobe, Salesforce, Iterable, Klaviyo**, alongside the
claim that "none of our competitors currently offer comparable comprehensive customer
engagement solutions" — `sources/filings/2026-03-25_10-K_000013.txt`.

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
misreading its own market, and the hypothesis that Braze would be shortlisted against
entirely different vendors was only **partially** borne out. That partial result is the
honest one and it is recorded as such.

The asymmetry is what matters, and it runs one way. Buyers weigh Braze against five vendors
it never names, and the character of those five is the finding: **Oracle is a suite vendor,
but Optimove, Blueshift, MoEngage and CleverTap are mobile-engagement and CDP specialists.**
Braze's own competitive frame is "we are more comprehensive than the suites"; the buyers'
frame includes "is this better than a focused specialist". Those require different answers,
and a competitive briefing built only from Braze's comparison pages would prepare for the
first conversation and walk into the second.

Where Gartner's reviewers rate Braze *above* the two largest alternatives, they name the
same things twice: service and support, and ease of integration and deployment — with
evaluation and contracting added against Salesforce. That is a consistent, independent,
buyer-sourced statement that Braze is easier to buy from and easier to deploy than Adobe or
Salesforce, and it should be quoted as readily as anything critical in this record.

## 7.4 · What customers say

Site-level aggregates, which are the figures to quote. The captured review bodies are a
sample of fourteen records used for vocabulary and theme, never for a percentage.

| Panel | Rating | Base |
|---|---|---|
| G2 | 4.5 / 5 | 1,702 reviews |
| Gartner Peer Insights | 4.5 / 5 | 263 ratings |
| TrustRadius | 8.8 / 10 | 348 reviews |

[[third-party]] {{src: sources/panels/g2.md:46 @ 2026-09-02}}

Braze is well liked, and that is the first thing to say. Two panels at 4.5 out of 5 and a
third at 8.8 out of 10, across more than two thousand ratings, is a strong result that no
amount of subsequent criticism should be allowed to obscure.

**The bases themselves disagree**, which is conflict **C-06**: Glassdoor's search page says
563 reviews where its company page says 524 ratings; Gartner shows 263 Ratings and 267
Verified Reviews; TrustRadius shows 348 in the header and 162 under the default filter. The
gaps are small on Gartner and very large on TrustRadius, where 186 of 348 are excluded by
the site's own default view. The ruling is to quote each site's headline rating with its own
headline base and never to mix them — and this is the second reason, after sample size,
that no percentage in this analysis is computed from captured review bodies.

G2's own coded tags (`sources/panels/g2.md:46`), counted over its full review base rather
than over the sample captured here, put the praise at Ease of Use (385), Intuitive (188), Customer Support (151), Helpful
(148) and Features (138); and the criticism at Missing Features (140), Learning Curve (139),
Limitations (102), Limited Features (93) and Steep Learning Curve (86). The most common
praise tag is nearly three times the most common criticism, which is the ratio to carry
away.

Two themes recur across unrelated panels and are therefore worth more than the rest:
**reporting is the most consistent complaint**, and **the learning curve is the second**.
TrustRadius codes reporting as "limited and unintuitive, a sentiment shared by 36% of
reviewers" (`sources/panels/trustradius.md`).

The reporting complaint corroborates independently with the platform evidence in chapter 4,
and the corroboration is what makes it solid rather than anecdotal: out-of-the-box reporting
is thin enough that Currents — a paid add-on exporting on a five-minute cadence — is the
route to raw data. A complaint from buyers and a mechanism in the documentation, arrived at
from unrelated directions, describing the same thing.

Running `tools/code_reviews.py` over the whole corpus produces theme percentages against a
denominator of 860 records in `data/review_themes.csv`, but 841 of those are GitHub issues
from `data/issues.csv` rather than buyer reviews.
That denominator is stated wherever the script's output is used, and its themes describe the
SDK surface, not satisfaction.

## 7.5 · What employees say

Glassdoor, captured signed-in: **4.1 out of 5 from 524 ratings, 82% would recommend, 90%
approve of the CEO, 71% positive business outlook.**

[[third-party]] {{src: sources/panels/glassdoor.md:68-92 @ 2026-09-02}}

Work-life balance tracks the overall rating almost exactly over the six months to September
2026 — both hovering around 4.0 to 4.1 — so there is no divergence worth calling a trend,
and none is claimed. The analysis went looking for a work-life-balance decline, which is the
usual story at this stage of a company's life, and did not find one.

Glassdoor's own summary names the weak spots as management effectiveness and "clarity in
direction", and "limited upward mobility and discrepancies in compensation relative to
market rates". That last phrase is worth setting against §1.4: the proxy discloses a median
employee total compensation of $164,000 (`sources/filings/2026-05-18_DEF-14A_021908.txt:5769`). This is not a low-paying company, so the grievance
is better read as being about *progression* than about level — which is precisely what
"limited upward mobility" says, and what the "limit to the number of folks who can score a
4/5" comment in the captured reviews describes.

### What they are hiring for, which is the forward-looking half

The careers board carries **296 open roles across fifteen hiring departments**, of
twenty-one listed.

| Department | Open roles |
|---|---|
| Sales | 89 |
| Engineering | 57 |
| Customer Experience | 38 |
| Marketing | 24 |
| Solutions Consulting | 23 |
| Partnerships | 16 |
| Growth | 15 |
| Information Technology | 13 |
| People | 7 |
| Business Development | 5 |
| Finance | 4 |
| GTM Strategy, GTM Operations, Legal, Product | 1–2 each |

[[documented]] {{src: data/careers_departments.csv @ 2026-09-02}}

The shape is unambiguous. **Go-to-market functions account for 213 of the 296 roles —
72.0% — against 58 for engineering and product, 19.6%.** Braze is hiring go-to-market
people over product-builders by roughly **3.7 to one**.

Read that against §7.2 and it stops being a personnel statistic. The retention figures
say expansion within the existing base is slowing and that growth is shifting to new
logos; a hiring board that is nearly three-quarters go-to-market is what executing that
shift looks like from the outside, and it is a leading indicator where retention is a
lagging one. The single largest department is Sales at 89 roles, more than engineering
and product combined.

Two disciplines on how far that can be pushed. **A requisition is an intention, not a
person** — a board is a plan, and plans get cut; nothing here contradicts or updates the
audited employee counts in §1.3. And **this is not a spend ratio**: a sales requisition
costs materially less than a senior engineering one, so 3.7:1 in headcount is consistent
with the audited 1.96:1 in money (§2.3) rather than in conflict with it. The two point the
same way at different magnitudes, which is what corroboration looks like when the
measures are genuinely different.

This closes open question 56. The first pass recorded the split as uncapturable, because
the board's Department filter would not drive under automation; the same board is
published as unauthenticated JSON with the grouping already done. The correction is in
chapter 8's log, and the transferable lesson is there too: **when a page will not yield,
look for the API behind it before recording a gap.**

Product at a single open role is the one number here worth not over-reading. One
requisition in a department is as likely to mean the team is fully staffed as anything
else, and a fifteen-person product organisation with no vacancy would show exactly this.

#### What would change this chapter

A fourth consecutive year of falling net retention would turn a demand-environment
explanation into a competitive one, and would be the single most important number in the
next 10-K. A reversal in the large-account premium would say the expansion engine had
restarted. A new name in the 10-K competition paragraph, or a change in the Gartner
shortlist, would move §7.3. And access to any of the three paywalled by-company-size rating
breakdowns would finally settle whether satisfaction falls with customer size — the one
hypothesis this analysis could not test at all.
