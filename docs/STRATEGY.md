# Strategy — what is different about Braze, and what that changes

The method in [`METHOD.md`](METHOD.md) is company-agnostic and was proved on a private
vendor. Braze is not that. Applying the same seven phases without adjusting for the
differences would waste the biggest advantage and walk into the biggest trap.

This file is the adjustment. Read it before phase 0.

---

## The one structural difference: Braze is a listed company

**NASDAQ: BRZE. CIK 0001676238. 737 filings. Fiscal year ends 31 January.**

On the reference project, the financial chapter was the *most* caveated in the deck. One
UK reselling subsidiary filed audited accounts; everything else was inference. The
headline number came with three caveats attached and had to be described as a signal
rather than a cost line.

For Braze that inverts. Audited, group-level, quarterly figures are published under legal
penalty and available as machine-readable XBRL going back to FY2019. **The financial
chapter becomes the strongest chapter in the deck, not the weakest.**

What that unlocks that was impossible before:

| Now possible | Because |
|---|---|
| Gross margin as an actual trend, not a signal | Audited group figures, 7 fiscal years, quarterly |
| Where the money goes, precisely | R&D / S&M / G&A are separate audited lines |
| Contracted revenue not yet recognised | `RevenueRemainingPerformanceObligation` is disclosed |
| The real cost of the equity story | `ShareBasedCompensation` against net loss |
| Acquisition prices | `PaymentsToAcquireBusinessesNetOfCashAcquired`, plus 8-K and 10-K notes |
| What management is paid to optimise | DEF 14A compensation tables |
| Who owns it, and when that changed | 72 SC 13G/13D filings |
| What the company says could go wrong | 10-K risk factors — legally compelled candour |

---

## The trap that comes with it

**This must not become an equity-research note.**

SEC data is abundant, tidy, and quotable, and it will pull the whole analysis toward
the income statement if you let it. It should not. The audience is deciding about a
*product and a competitor*, not about a share price. Revenue growth does not tell them
whether a campaign can be built, whether two email addresses on one profile can both be
targeted, or which channel quietly has no middleman.

Three rules to hold the line:

1. **Product truth leads; money is corroboration.** A financial fact earns its slide
   when it explains a *product or strategy* fact — R&D as a share of revenue next to
   documentation volume per capability, for instance.
2. **No forecast, no valuation, no recommendation.** This is analysis of a competitor,
   not advice about a security. If a slide would look at home in a broker note, cut it.
3. **Cap the money chapter.** Roughly a fifth of the deck, in line with the reference
   project's Part III. Deeper on unit economics than that deck could go; not longer.

---

## The second difference: the engineering record is open

The reference vendor published a documentation site and an API spec. Braze publishes
**137 public repositories** with commit history, releases, issues and pull requests
across a decade — 494 releases in the SDK repos alone, 2016-12-13 → 2026-09-01 — plus a
public status page with **451 incidents back to 2016-10-09**.

That makes several things measurable that were previously only assertable:

- **Platform support, as maintenance rather than a logo wall.** A supported platform
  with no release in two years is a different claim from one shipping monthly.
- **Reliability, with a decade of shape.** Incidents per quarter, duration distribution,
  which components recur. Never as a competitor comparison unless the competitor also
  publishes one.
- **Where engineering attention goes**, cross-checked against where documentation
  volume goes and where the money goes. Three independent lenses on the same question.

---

## The third difference: this vendor has already been analysed

Work on the assumption — safe for any listed vendor of this size, and cheap to confirm
once — that Braze is already covered by sell-side analysts, by the category's analyst
firms, and by competitors' battle cards. **On that assumption, "we read the 10-K" is
worth nothing.** Everyone has read the 10-K.

The differentiated value is in the places nobody bothers to look, and they are exactly
the places this method already goes:

- documentation volume as a capability measurement, with the focused-page test
- the sub-processor disclosure, read for what it names and what it omits
- certificate transparency, for what was provisioned but never announced
- the status page component list, read as an architecture disclosure
- SDK release cadence, read as which platforms are actually maintained
- review panels *coded*, not summarised — and Gartner shortlists, for who buyers
  actually compared them against

**Assume every headline number is already known to the audience. Earn attention with
the synthesis and with the four or five things nobody has counted.**

---

## What the evidence grades have to change

Five grades, but the ordering shifts because the top of the ladder is now occupied:

| Grade | For a private vendor | For Braze |
|---|---|---|
| Strongest | Certificate transparency | **Audited SEC filings**, then CT |
| | Statutory filings (one subsidiary) | 10-K/10-Q/8-K — group, quarterly, audited |
| | Legally-compelled disclosure | Sub-processor list, unchanged |
| | Technical documentation | Documentation **and public VCS history** |
| Weakest | Marketing | Marketing, unchanged |

The practical consequence: **a marketing claim that contradicts a filing is not a
conflict, it is an error, and should be said so plainly.** With a private vendor you
usually cannot make that call. Here you often can. See [`CONFLICTS.md`](CONFLICTS.md)
for how to record the difference.

---

## Where this analysis will be weaker than the reference project

Stated up front, because a method honest about its preconditions gets trusted where it
does apply.

- **No transfer-pricing story.** The single sharpest financial finding on the reference
  project came from comparing a subsidiary's accounts against group claims. Braze
  consolidates; that particular seam does not exist.
- **Pricing is likely to stay opaque.** Listed status does not mean published price
  lists. Expect to reconstruct from procurement records, reseller listings and reviews,
  and expect the result to be a range with a wide confidence interval. Note that
  average contract value can often be *bounded* from disclosed revenue and disclosed
  customer counts — a route a private vendor does not offer.
- **Headcount will still be a range.** 10-K employee counts are as-of a date and
  count differently from LinkedIn. Record both; never merge.
- **A named-customer roster is partly marketing.** 178 customer-story URLs are
  self-selected. Independent detection (tag crawls, CT, job ads naming the stack)
  remains the corroborating lens.

---

## The deliverables, and the bar for each

Two documents, as in the reference project, plus the fact index that makes them
maintainable.

| Deliverable | Bar |
|---|---|
| `deck/braze-deck.html` | ~41 slides. One idea per slide, graded. Answers every question the reference deck answered, and goes deeper where the evidence allows — see [`DECK-SPEC.md`](DECK-SPEC.md) |
| `deck/evidence-record.html` | Record (subject chapters, **every fact stated once**) + Slide Map (deck order, pointers only). See [`RECORD-SPEC.md`](RECORD-SPEC.md) |
| `docs/FACTS.md` | Canonical value, grade and source path for every number used, plus a visible corrections log |

"Deeper where the evidence allows" is not a licence to be longer. It is a licence to be
*more certain* — to replace a caveat with an audited figure, and to say a thing plainly
that the reference deck could only imply.

---

## Ten hypotheses to test, and how each one dies

Written before the corpus was read, so they can be graded honestly afterwards. **These
are questions, not findings.** Every one must end the project either evidenced with a
source path, or explicitly killed. A hypothesis quietly dropped is a bias.

| # | Hypothesis | What would kill it |
|---|---|---|
| 1 | Growth is decelerating while sales spend holds | S&M as a share of revenue flat or falling with growth |
| 2 | The agentic/AI layer is newer and thinner than the positioning implies | Focused-page counts and endpoint counts comparable to established capabilities |
| 3 | Documentation is more honest than marketing about limits | Docs and marketing agree on every limit found |
| 4 | Some supported platforms are effectively unmaintained | Every SDK repo shipping releases in the last 12 months |
| 5 | The cluster architecture constrains something buyers care about | No customer-visible consequence in docs, reviews or incidents |
| 6 | The channel list is narrower than the category leader's positioning implies | An enumerable channel set as broad as any competitor's |
| 7 | Enterprise satisfaction is lower than SMB, as it usually is | Ratings flat or rising with company size |
| 8 | Buyers do not shortlist them against who they say they compete with | Gartner shortlists matching their own comparison pages |
| 9 | Incident rate has risen with scale | Incidents per quarter flat or falling since 2016 |
| 10 | There is something provisioned that has never been announced | CT logs showing nothing not already public |

Hypothesis 3 is the one worth most attention: on the reference project it held, and it
produced the two strongest technical findings in the deck.

---

## How the ten ended — resolved 2026-09-02

Every hypothesis below is either **evidenced** with a source path or **explicitly
killed**. Four were killed, and three of those four killed *favourably* — the evidence
went the other way and says something good about Braze. That distribution is the point:
a set of hypotheses that all confirmed would have meant they were written to confirm.

| # | Verdict | What the evidence said | Where |
|---|---|---|---|
| H1 | **Killed** | Growth is decelerating (49.3% → 24.4% over FY2023→FY2026), but S&M as a share of revenue fell faster, 56.7% → 44.3%. Sales spend is *not* holding; deceleration comes with improving efficiency, and operating cash flow turned positive in FY2024 and has grown every year since | `FACTS.md` §2.1, §2.2 |
| H2 | **Evidenced** | Agents 17 focused pages and Decisioning Studio 22, against Canvas 249; 0 of 135 published API endpoints in any AI namespace; and the decisioning engine was bought on 2 June 2025 (OfferFit, $303.2m) rather than built. "Newer" is proven by the acquisition date. "Thinner" is stated as counts, never as a verdict | `FACTS.md` §6, §3.1; `CONFLICTS.md` C-04 |
| H3 | **Evidenced — the strongest of the ten** | Every hard limit found came from documentation and appears in no marketing page: three of four ingestion paths labelled "Not real-time"; a 15-minute warehouse floor; the profile-lookup export limit cut 10× for customers onboarding after 2024-08-22; 75 objects per ingest request; a merge that returns 202 Accepted when it has silently declined; "removing data from one system does not automatically remove it from the other"; and "Don't waste data points. Only update changing data!" | `FACTS.md` §4.2, §4.3, §4.5, §4.6 |
| H4 | **Killed — favourably** | All nine SDK repos that publish releases shipped within 13 days of the capture. The one platform whose repo is archived, Unreal, has also had its documentation removed entirely — zero doc pages, zero site pages. The maintenance record matches the marketing. The single soft spot is `braze-roku-sdk`: 181 days idle while 38 Roku doc pages stay live | `FACTS.md` §4.9 |
| H5 | **Evidenced — but not where expected** | The regional clusters themselves are well handled. The customer-visible constraint is the *storage* split: MongoDB holds events, attributes and profiles while Snowflake holds SQL Segment Extensions, Prediction Suite and recommendations, and their own docs warn that "removing data from one system does not automatically remove it from the other". Clusters do surface to customers as per-instance allowlist IPs | `FACTS.md` §4.4, §4.7 |
| H6 | **Killed** | The channel set is broad, not narrow: 13 documented channels including WhatsApp, LINE, KakaoTalk, RCS, Banners, Landing pages, Live notifications and Webhooks. The finding inverts — five documented channels have no marketing page, and one marketed channel (KakaoTalk) is missing from their own docs channel index | `FACTS.md` §5.1; `CONFLICTS.md` C-02 |
| H7 | **Not resolved — untestable from public sources** | All three review sites paywall the rating-by-company-size breakdown; only 7 of 860 coded records carry a segment at all, far too few to test anything. The nearest audited proxy is a different measure and points mildly the other way: dollar-based net retention for customers ≥$500k ARR is *above* the all-customer figure (110% vs 109% in FY2026) — though that gap has closed from 3 points to 1 since FY2024. Recorded as an open question with what would close it | `FACTS.md` §2.4, §8.3; `QUESTIONS.md` #54 |
| H8 | **Partially evidenced** | Not a clean miss: 3 of the 4 competitors the 10-K names (Adobe, Salesforce, Iterable) do appear on Gartner's buyer-derived shortlist. But the shortlist is twice as long, and the 5 it adds — Oracle, Optimove, Blueshift, MoEngage, CleverTap — appear nowhere in the 10-K. The omission runs one way: Braze names suite vendors and Klaviyo; buyers also weigh five specialists | `FACTS.md` §8.2 |
| H9 | **Killed — favourably** | Incidents peaked in 2023 at 60 and fell to 27 in 2025, the quietest full year on the status page, while revenue grew 7.7× from FY2020 to FY2026. Rate per unit of scale has fallen sharply. Stated with its caveat: 2026 to date runs at roughly double the 2025 monthly rate | `FACTS.md` §4.8 |
| H10 | **Evidenced** | Certificate transparency shows 50 hosts on a `aze` region code matching no AWS identifier, tied by hostname to instance 08; the allowlist IPs Braze publishes for US-08 are all registered to Microsoft Corporation where every other instance's are Amazon; and the sub-processor disclosure of 1 June 2026 names only Amazon and Google as hosting providers. What it *means* is not knowable from outside and is recorded as a question, not a conclusion | `FACTS.md` §4.7; `CONFLICTS.md` C-03; `QUESTIONS.md` #52 |

**Tally: 4 evidenced · 4 killed · 1 partially evidenced · 1 untestable.**

---

## What "similar or deeper" means, concretely

The reference deck's 41 slides each answered one question. The Braze deck must answer
all of them. [`DECK-SPEC.md`](DECK-SPEC.md) maps them one by one and marks each as
**parity**, **deeper** (the evidence is stronger here), or **substitute** (the question
does not apply and what replaces it).

The honest summary of that mapping: roughly a third go deeper — almost all of them
financial, operational or engineering, and almost all because Braze publishes what the
reference vendor did not have to.
