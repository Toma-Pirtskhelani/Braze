# What we could not answer

> Eight questions this analysis could not close from public sources, each with the source that would close it — plus the two places where a number moved and the old value is deliberately still visible, and the ledger of ten hypotheses graded honestly, three of which died in Braze's favour.

{{slides: 2, 3, 5, 33, 37, 40, 41, 42}}

A gap written down is evidence. A gap not written down is a mistake. The full backlog
lives in `docs/QUESTIONS.md`; what follows is the residue that matters to a reader of
this record, in the order a competitor would care about.

## 8.0a · The four documents the deck rests on

Slide 5 exists because the operator watched the deck and could not follow it. Seventeen
specialist terms were in use and none was defined; two of them — "10-K" and
"sub-processor" — carried whole findings, and one of those landed on the title slide. The
slide is not a glossary. It is the argument for why these four sources beat marketing,
with the definitions riding along inside it.

| Document | What it is | Why it is hard to falsify |
|---|---|---|
| **10-K** | The audited annual report to the SEC | Signed by the CEO and CFO, audited by Ernst & Young, wrong at legal risk. Seven years captured |
| **DEF 14A (proxy)** | Filed before the annual shareholder meeting | Must name every executive officer and director, their pay, and who owns the company |
| **Sub-processor disclosure** | A public list of outside suppliers that touch customer data | Data-protection law requires it to be *complete*, so it names middlemen marketing never would |
| **Status page** | A live record of every incident since 2016 | Written during the outage, by someone trying to fix it |

Nothing on that slide is a new finding, and it cites nothing this record does not already
carry: the filings are in §1 and §2, the sub-processor disclosure runs through chapters 5
and 6, and the status page is chapter 4's operational record. **What it adds is the reason
to believe the rest**, delivered before the first claim rather than after it.

The general lesson is worth recording next to the corrections log, because it is the same
class of error. **A term the analyst has read four hundred times is invisible to them and
opaque to everyone else.** Nothing in the evidence was wrong; the deck was simply
unreadable to the person it was built for, and no amount of verification catches that.
Only showing it to somebody does.

## 8.0 · The hypothesis ledger, and why three killed results are on a slide

Ten hypotheses were written into `docs/STRATEGY.md` **before any source was captured**,
each with a stated condition that would kill it. That ordering is the whole point: a
hypothesis written after the reading is a conclusion wearing a question's clothes, and a
hypothesis quietly dropped when it fails is a bias that leaves no trace.

They ended: **four evidenced, four killed, one partially evidenced, one untestable.**

The distribution matters more than any single verdict. If ten out of ten had confirmed,
the honest reading would not be that the analysis was unusually perceptive — it would be
that the hypotheses were written to confirm, and every critical finding in this record
would deserve to be discounted accordingly. Four failures out of ten is what a set of
genuine priors looks like.

**Three of the four killed results went in Braze's favour**, and in the first draft of
this project all three reached the record and none reached the deck. That asymmetry was
not a decision anyone made; it is what happens by default, because a favourable finding
has nowhere obvious to go in a competitive deck and an unfavourable one does. It is now
slide 40, on the grounds that an analysis reading as uniformly critical invites its
audience to discount all of it — including the parts that are hardest to argue with.

| # | Hypothesis, as written beforehand | How it died | Detail |
|---|---|---|---|
| H1 | Growth is decelerating while sales spend holds | Sales and marketing fell faster than growth did, to its lowest share in the seven-year series (`data/financials_annual.csv`) | ch2 §2.3 |
| H4 | Some supported platforms are effectively unmaintained | Every SDK repository publishing releases had shipped within 13 days of capture, and the archived one has had its documentation removed too (`data/sdk_releases.csv`, `data/repos.csv`) | ch4 |
| H9 | Incident rate has risen with scale | Incidents peaked in 2023 and fell to the quietest full year on the status page in 2025 (`data/incidents.csv`) | ch4 |

[[documented]] {{src: docs/STRATEGY.md @ 2026-09-02}}

The fourth kill, H6, is in Braze's favour too but is left off the slide because chapter 5
already states it plainly where it belongs: the channel roster is broad, not narrow, and
the finding inverted into something more interesting than the hypothesis.

One discipline to note about how these are quoted. Each killed hypothesis keeps its
caveat attached in the same breath — 2026's incident count runs at roughly double the
2025 monthly rate, and `braze-roku-sdk` sits idle with its documentation still live.
A favourable finding stripped of its caveat is exactly as dishonest as an unfavourable
one stripped of its context, and it is more tempting because nobody objects.

## 8.1 · The eight open questions

| # | Question | What would close it |
|---|---|---|
| 52 | Why does the sub-processor disclosure name only Amazon and Google as hosting providers when the allowlist IPs Braze publishes for instance US-08 are all registered to Microsoft? | A revised sub-processor list, the DPA schedule a customer receives, or a direct answer from Braze |
| 53 | Is the `aze` region code Azure, and is US-08 a distinct class of instance? | A Braze statement, a customer on US-08, or a wider certificate-transparency capture |
| 54 | Does satisfaction fall as customer size rises? | Paid access to the G2, Gartner or TrustRadius rating-by-company-size breakdowns — all three paywalled |
| 55 | Why was the profile-lookup rate limit cut tenfold for customers onboarding after 22 August 2024, and were existing customers told? | A changelog entry, a support answer, or customers either side of the date |
| 57 | Can the customer roster be verified independently of the self-published stories? | Tag crawls, certificate transparency naming customer subdomains, or job ads naming the stack |
| 58 | What else is in the certificate-transparency estate? | A `CERTSPOTTER_TOKEN`; crt.sh returned HTTP 502 throughout this run |
| 59 | Does the gross-margin decline continue, and how much of it is AI cost rather than acquisition amortisation? | The FY2027 10-K, or quarterly cost-of-revenue detail |
| 46 | Actual list pricing and discounting policy | A public-sector procurement award, or a customer contract |

There were nine until late in the work. **Question 56 — the exact split of open roles by
function — closed**, from the source this table had already named: the Greenhouse board
API. The answer is in chapter 7 §7.5 and the correction is logged in §8.2. It is worth
one sentence here because it is the only gap in this project that closed after being
written down, and it closed because the row said what would close it. **A gap recorded
with its remedy is an instruction to a later reader; a gap recorded as a shrug is not.**

Two of the remaining eight deserve emphasis because they bound claims made elsewhere in
this record.

**Question 58 bounds chapter 4.5.** The host list is partial — 833 hosts in
`data/subdomains.csv`, captured through a rate-limited fallback after the primary source
returned errors all day; the failures are logged in `logs/fetch-failures.md`.
Everything said about what *was* provisioned stands. Nothing is said about what is
absent, because the check was not exhaustive and an absence from an incomplete list is
not a finding.

**Question 54 is the one hypothesis that could not be tested at all.** The analysis went
in expecting enterprise satisfaction to be lower than small-business satisfaction, as it
usually is. All three review sites paywall exactly that breakdown, and only seven of the
860 coded records in `data/review_coding.csv` carry a customer-size segment — far too few
for anything. The nearest
audited proxy points mildly the other way and measures something different: net retention
among customers with $500k or more of annual recurring revenue is slightly *above* the
all-customer figure (chapter 7). That is expansion, not satisfaction, and it is not
offered as a substitute.

## 8.2 · Where a number moved — the corrections log

Required by `RECORD-SPEC.md` and mirroring `docs/FACTS.md`, with the old values still
visible so a stale copy of this document can be recognised on sight. A record that shows
its own errors is the reason to trust the rest of it.

| # | Fact | Was | Is now | Why it changed | Date |
|---|---|---|---|---|---|
| 1 | Status-page grouping | "132 in 12 groups" | 132 rows in **17 named groups**, of which **15 are regional clusters** | The setup-time reconnaissance counted by eye. Counting `data/status_components.csv` gives 17 named groups and 15 clusters | 2026-09-02 |
| 2 | Capability page counts | Journey orchestration 319 · Identity resolution 136 · Segmentation 339 | Canvas 249 · Identity 110 · Segmentation 242 | **The pattern set moved, not the product.** The taxonomy in `docs/CAPABILITY-TAXONOMY.tsv` was revised from generic category words to Braze's own product names. Counts from the two runs are not comparable, and both are reproducible from the `pattern` column of `data/capabilities.csv` | 2026-09-02 |
| 3 | KakaoTalk's status | Read at first pass as documented but not marketed | **Marketed**, but missing from Braze's own docs channel index | A truncated search appeared to show no marketing page. Checking the full `/product/` enumeration found one | 2026-09-02 |
| 4 | The money chapter's completeness | Written with no reference to internal control over financial reporting | Carries the **material weakness** disclosure and both its halves (§2.1b) | The first pass read the 10-K for what it was looking for and missed Item 9A entirely. Found in self-review | 2026-09-02 |
| 5 | `DECK-SPEC.md`'s cluster count | "12 named regional clusters" | Corrected in the specification itself to 15 | Correction 1 was recorded here but the specification that repeated the error was left uncorrected for a further pass. A spec known to be wrong will mislead the next reader | 2026-09-02 |
| 6 | The hiring split by function | "~284–300 open roles", split by department recorded as **uncapturable** | **296 open roles across 15 hiring departments**, with the exact split (ch7 §7.5) | The board's web filter would not drive under automation, so the gap was written down — correctly, at the time. The same board is published as unauthenticated JSON with the grouping already done. **When a page will not yield, look for the API behind it before recording a gap** | 2026-09-02 |

Correction 2 is the one that matters most to a sceptical reader, and it is the reason the
capability taxonomy is published rather than merely described. **A number that moves
because the measurement moved is not a finding**, and presenting it as one would be the
easiest way to mislead an audience in this entire project.

Correction 4 is the one that matters most to a careful one. The first pass of this analysis
wrote an entire financial chapter without noticing that the company had disclosed its
financial-reporting controls were not effective. Nothing else in this record is more
important as a warning about how the omission happened: the filing was searched for
answers to questions already being asked, rather than read for what it volunteered.

## 8.2b · Disagreements found in a dedicated sweep

Five conflicts existed after the first pass, all of which surfaced incidentally while
writing other chapters. A dedicated sweep on 2026-09-02 — the discipline the reference
project used to find twenty-one — added four more, and they cluster in exactly the place
incidental discovery misses: **the definitions under the most-quoted numbers.**

| Conflict | The disagreement | Ruling in one line |
|---|---|---|
| **C-06** | Each review panel's own surfaces disagree about its review count — Glassdoor 563 vs 524, Gartner 263 vs 267, TrustRadius 348 vs 162 | Quote each site's headline rating with its own headline base, never mixed |
| **C-07** | The headcount in §1.3 counts full-time employees; the proxy's pay-ratio population on the same date is full-time **and** part-time, and is never sized | Say "full-time employees", never "headcount" |
| **C-08** | A "customer" is an **ultimate parent entity**, so the §7.1 metric counts corporate groups while the 178 stories count brands | The $283,000 bound is per corporate group, and the two rosters are not comparable |
| **C-09** | The 15 "Braze Group" entities include Braze KK, a majority-held VIE with outside investors — not a wholly-owned subsidiary | Name the exception when citing the entity list |

Nine conflicts is still well short of the twenty-one the reference project recorded, and
the honest reason is not that Braze generates fewer disagreements. It is that four of the
nine here were found in a single deliberate hour, and no comparable sweep has been run over
the documentation corpus, the incident history or the site inventory. That is a known gap
in method rather than a finding about the company, and it is recorded as such.

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
