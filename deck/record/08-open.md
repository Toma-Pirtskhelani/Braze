# What we could not answer

> Nine questions this analysis could not close from public sources, each with the source that would close it — plus the two places where a number moved and the old value is deliberately still visible.

{{slides: 2, 3, 32, 36, 39, 40}}

A gap written down is evidence. A gap not written down is a mistake. The full backlog
lives in `docs/QUESTIONS.md`; what follows is the residue that matters to a reader of
this record, in the order a competitor would care about.

## 8.1 · The nine open questions

| # | Question | What would close it |
|---|---|---|
| 52 | Why does the sub-processor disclosure name only Amazon and Google as hosting providers when the allowlist IPs Braze publishes for instance US-08 are all registered to Microsoft? | A revised sub-processor list, the DPA schedule a customer receives, or a direct answer from Braze |
| 53 | Is the `aze` region code Azure, and is US-08 a distinct class of instance? | A Braze statement, a customer on US-08, or a wider certificate-transparency capture |
| 54 | Does satisfaction fall as customer size rises? | Paid access to the G2, Gartner or TrustRadius rating-by-company-size breakdowns — all three paywalled |
| 55 | Why was the profile-lookup rate limit cut tenfold for customers onboarding after 22 August 2024, and were existing customers told? | A changelog entry, a support answer, or customers either side of the date |
| 56 | What is the exact split of open roles by function? | The Greenhouse board API, or a working pass over the board's department filter |
| 57 | Can the customer roster be verified independently of the self-published stories? | Tag crawls, certificate transparency naming customer subdomains, or job ads naming the stack |
| 58 | What else is in the certificate-transparency estate? | A `CERTSPOTTER_TOKEN`; crt.sh returned HTTP 502 throughout this run |
| 59 | Does the gross-margin decline continue, and how much of it is AI cost rather than acquisition amortisation? | The FY2027 10-K, or quarterly cost-of-revenue detail |
| 46 | Actual list pricing and discounting policy | A public-sector procurement award, or a customer contract |

Two of these deserve emphasis because they bound claims made elsewhere in this record.

**Question 58 bounds chapter 4.5.** The host list is partial — 833 hosts, captured
through a rate-limited fallback after the primary source returned errors all day.
Everything said about what *was* provisioned stands. Nothing is said about what is
absent, because the check was not exhaustive and an absence from an incomplete list is
not a finding.

**Question 54 is the one hypothesis that could not be tested at all.** The analysis went
in expecting enterprise satisfaction to be lower than small-business satisfaction, as it
usually is. All three review sites paywall exactly that breakdown, and only seven of the
860 coded records carry a customer-size segment — far too few for anything. The nearest
audited proxy points mildly the other way and measures something different: net retention
among customers with $500k or more of annual recurring revenue is slightly *above* the
all-customer figure (chapter 7). That is expansion, not satisfaction, and it is not
offered as a substitute.

## 8.2 · Where a number moved

The corrections log, mirroring `docs/FACTS.md`, with the old values still visible so a
stale copy of this document can be recognised on sight.

| Fact | Was | Is now | Why it changed |
|---|---|---|---|
| Status-page grouping | "132 in 12 groups" | 132 rows in 17 named groups, of which 15 are regional clusters | The setup-time reconnaissance counted by eye. Counting the CSV gives 17 named groups and 15 clusters. `DECK-SPEC.md` repeated the same error and is wrong for the same reason |
| Capability page counts | Journey orchestration 319, Identity resolution 136, Segmentation 339 | Canvas 249, Identity 110, Segmentation 242 | **The pattern set moved, not the product.** The taxonomy was revised from generic category words to Braze's own product names. Counts from the two runs are not comparable, and both are reproducible from the `pattern` column of `data/capabilities.csv` |
| KakaoTalk's status | Read at first pass as documented but not marketed | Marketed, but missing from Braze's own docs channel index | A truncated search appeared to show no marketing page. Checking the full `/product/` enumeration found one |

The middle row is the important one, and it is the reason the taxonomy is published
rather than described. A number that moves because the measurement moved is not a
finding, and presenting it as one would be the easiest way to mislead an audience in this
entire project.

## 8.3 · What was substituted, and what that cost

| Blocked | Substituted with | What is lost |
|---|---|---|
| crt.sh (HTTP 502 all day, twice) | Cert Spotter, rate-limited without a token | A partial host list. Stated as partial everywhere it is used |
| Rating by company size on all three review panels | Nothing equivalent exists publicly | Hypothesis 7 is unresolved rather than answered |
| Per-department headcount on the careers board | The department taxonomy and a front-of-list sample | No function split. No percentage is offered |
| Independent customer detection | Not attempted | The 178 published stories are not treated as a roster |

Every review panel that returned HTTP 403 to a script was captured through a browser
session instead, and Glassdoor required the operator to sign in before its content became
readable at all — recorded here because the capture route is part of the evidence.

#### What would change this chapter

Any of the nine questions closing. The most valuable single answer would be question 52,
because it decides whether chapter 4.5 is an observation about infrastructure or
something a buyer's procurement team needs to raise.
