# Critique — the Braze analysis, measured against the reference project

Written 2026-09-02 by a reviewer who did not do the work, against the completed analysis
at commit `4da710c`, and calibrated throughout against the Insider One project the method
came from.

**Read this first: the analysis is good.** The verifier passes 9/0, all ten hypotheses are
resolved rather than quietly dropped, and the self-review caught its own worst omission
before anyone else did. What follows is not a demolition. It is a list of places where
this analysis is measurably thinner than the one it was modelled on, and where the
presentation does not yet do the research justice.

Every number below is re-derivable. Nothing here is an impression.

---

## 1 · The verdict in one table

| | Braze | Insider One | |
|---|---|---|---|
| Fact rows in `FACTS.md` | **199** | 101 | **better** |
| `FACTS.md` words | **7,511** | 3,358 | **better** |
| Hypotheses stated and resolved | **10 / 10** | none registered | **better** |
| Verifier state | **9 pass, 0 fail** | 7 pass, 0 fail | **better** |
| Slides | 41 | 41 | parity |
| Components per slide | 1.7 | 2.0 | parity |
| Words per slide | 108 | 107 | parity |
| **Conflicts recorded** | **5** | 21 | **24%** |
| **Evidence record, words** | **8,375** | 28,530 | **29%** |
| **Record sub-sections (`h4`)** | **8** | 95 | **8%** |
| **Speaker notes, mean words/slide** | **138** | 238 | **58%** |
| **Speaker notes, longest slide** | **268** | 858 | **31%** |
| **Images, diagrams, maps in the deck** | **0** | mark, photo, logos, world map | **none** |
| Slides with >120px dead vertical space | **19 / 41 (46%)** | 13 / 36 (36%) | worse |

**The shape of the problem:** the *research* is deeper than the reference project. The
*evidence record* and the *spoken narrative* are roughly a third of it, and the deck has
no visual language of its own at all.

---

## 2 · What is genuinely better, and should not be touched

Say this plainly, because the rest of the document is criticism and criticism without
calibration is just noise.

**The hypothesis register is a real advance.** Ten hypotheses written before the corpus
was read, and all ten resolved afterwards with a source path — four killed, and three of
those killed *favourably*, meaning the evidence went against the analyst's prior and was
recorded anyway. The reference project had no such register. This is the single strongest
piece of intellectual discipline in either repository.

**The self-review found the material weakness.** The FY2026 10-K discloses that the CEO
and CFO concluded disclosure controls were "not effective at the reasonable assurance
level", from ineffective ITGCs over user access and change management. The first pass
wrote the entire money chapter without it. The self-review caught it, and — more
importantly — recorded **both halves**: the weakness, *and* that no misstatement was
identified, nothing was restated, and E&Y attested. Either half alone misleads. That is
exactly right.

**Four findings that no competitor's battle card will have.** The US-08 instance's
allowlist IPs registering to Microsoft when the sub-processor disclosure names only Amazon
and Google. North Star Y's $26m earn-out paying $0. AI Decisioning Studio being OfferFit,
bought for $303.2m and renamed. Three of four documented ingestion paths labelled "not
real-time" by Braze's own comparison table, against an Item 1 that opens with
"real-time".

**The escalation ladder worked end to end.** All four bot-walled panels were captured
through the browser, Glassdoor after the operator signed in, and the wrong pre-set
Glassdoor company ID was caught and corrected. `logs/fetch-failures.md` is closed out with
an outcome per row. That is the process working as designed.

**The corrections table is populated and honest** — including the admission that the
capability counts moved because the *pattern set* moved, not the product, and that
pre- and post-revision counts are not comparable.

---

## 3 · The evidence record is a third of the depth it needs

**This is the most serious gap, and it is not close.**

`deck/evidence-record.html` is **8,375 words in 8 chapters, with 8 sub-headings across the
whole document.** The reference record is 28,530 words with 95. Chapter word counts:

```
01-company        628      05-channels       732
02-money        1,255      06-ai             995
03-acquisitions   665      07-market       1,113
04-platform     2,332      08-open           994
```

Four chapters are under 1,000 words. `01-company` at 628 words is covering entity
structure, incorporation, leadership, ownership, headcount and fifteen subsidiaries across
fourteen territories — that is a paragraph each.

**Why this matters more than it looks.** The record is the document that answers "says
who?" It is what survives the meeting, what gets forwarded, and what a sceptical reader
opens when they want to challenge a number. `FACTS.md` at 199 rows is an excellent
*index*, but an index is not an argument. Right now the analysis has a superb lookup table
and a thin book.

**The specific failure:** the chapters read as annotated fact lists rather than as
arguments. Each has a thesis line and a `What would change this chapter` close — the
scaffolding is correct — but between them the prose is compressed to the point where the
*reasoning* is missing. Why does the cluster architecture matter to a buyer? What does an
earn-out paying zero actually tell you about how that acquisition was underwritten? The
facts are present; the analysis connecting them is not.

**What good looks like:** `04-platform` at 2,332 words is the right shape. Six of the
eight chapters need to reach roughly that.

---

## 4 · Five conflicts is too few, and the reason is structural

Five recorded conflicts against the reference project's twenty-one, for a company with
*more* public surface, not less.

The five that exist are well made — C-01 (real-time), C-03 (which cloud) and C-04 (AI
built or bought) are genuinely good, and C-05 exists only to prove the restatement file
was checked, which is the right instinct.

But a listed company with 737 filings, 1,352 documentation pages, 6,366 site URLs, four
review panels and a decade of incidents should be generating disagreements at a much
higher rate. Candidates that appear to have gone unrecorded:

- **Employee count.** `FACTS.md` gives 1,988 full-time as at 2026-01-31, audited. Glassdoor,
  LinkedIn and the careers board will not agree with that or with each other. The
  reference project's C-14 ruling — *quote the range, never a precise figure* — has no
  Braze equivalent, and one audited number presented alone is exactly the trap that ruling
  exists to prevent.
- **Customer count**, which `STRATEGY.md` itself flags as having at least three
  definitions — the 10-K's defined metric, the 178 customer-story pages, and independent
  detection. Three definitions and no conflict entry.
- **Channel count** is recorded as C-02, correctly. But the same *drift* pattern —
  documentation index versus marketing site — almost certainly recurs elsewhere and was
  not swept for.
- **The careers board.** The department histogram was not captured because the filter UI
  would not drive. That is honestly logged, but "~284–300 open roles" against 1,988
  employees is a claim with no cross-check.

**The test to apply:** the reference project found 21 conflicts because it went looking
for them as a distinct pass. There is no evidence of such a pass here — the five that
exist all surfaced incidentally while writing other chapters.

---

## 5 · The deck has no visual language

**Zero images. Zero SVG. Zero base64. `worldmap()` is never called.**

The design system in `deck/lib.py` ships a world map — an equirectangular dot grid with
labelled pins — and this analysis covers a company with **fifteen named regional clusters**
(`US-01` through `US-08`, `EU-01`, `EU-02`, `AU-01`, `ID-01`, `JP-01`, `KR-01`) and an
audited geographic revenue split. That is the single most obvious map in either project,
and the slide that should carry it does not.

There is no brand mark on the title slide, no product screenshot, no architecture diagram,
no photograph. The reference deck was 335 KB against this deck's 125 KB, and essentially
all of that difference is embedded imagery.

The consequence is not decorative. **A 41-slide deck of text panels reads as a document
being narrated**, and it gives an audience nothing to look at while the presenter makes a
point. Component density is fine — 1.7 per slide against 2.0 — but the components in use
are the *text* ones: 16 `figrow`, 15 `cards`, 11 `tiles`. `split`, the two-column layout
that carries most of the reference deck's visual rhythm, is used 9 times here against 32
there.

**Related, and measurable:** 19 of 41 slides carry more than 120px of dead vertical space,
median 135px, worst 256px on slide 9. The reference deck runs 13 of 36 and a median of
107px. Both decks are airy — that is partly the design system — but this one is
measurably airier, and on a 632px canvas 256px of dead space is 40% of the slide.

---

## 6 · The narrative peaks too low

Speaker notes average **138 words per slide against the reference project's 238**, and the
longest note here is **268 words against 858**.

That maximum is the tell. In the reference deck there are three or four slides where the
presenter stops and makes an actual case — walks the audience through why the number means
what it means, pre-empts the objection, lands the point. The longest note in this deck is
about a third of that, which means **there is no slide where the presenter is given room
to argue.** Forty-one slides of even, moderate commentary is a briefing, not a case.

Four slides carry fewer than 60 words of notes at all.

The material to fix this exists and is sitting in `FACTS.md` unused. The US-08 finding, the
material weakness with both its halves, the earn-out that paid nothing, the real-time
contradiction — each of those deserves a slide where the presenter has 400 words and takes
ninety seconds.

---

## 7 · Smaller defects, in descending order

1. **`FACTS.md`'s corrections section opens with "Empty, and it will not stay that way"
   and is immediately followed by three corrections.** Stale prose contradicting the table
   underneath it, in the one file whose whole purpose is being trustworthy at a glance.

2. **No corrections log in the evidence record.** `RECORD-SPEC.md` requires it —
   *"The corrections log lives here too, mirroring FACTS.md, with old values visible."*
   `08-open.md` mentions it in passing; there is no table.

3. **`DECK-SPEC.md` says "12 named regional clusters" and is wrong** — the corrections
   table records the true figure as 15 clusters in 17 groups and explicitly flags the spec
   as wrong. The spec was never corrected. A specification known to be wrong and left in
   place will mislead the next reader.

4. **No favourable-finding vocabulary anywhere in the deck.** Searching the rendered deck
   for *favourable*, *credit*, *strength*, *impressive* returns zero across all four. The
   hypothesis register shows three findings killed *favourably* — the evidence went
   Braze's way — but that balance does not appear to have reached the slides. An analysis
   that reads as uniformly critical invites the audience to discount all of it.

5. **The careers-board department split was never obtained.** Honestly logged as partial,
   but the reference project's equivalent finding — *"~80% of open roles in sales, one in
   engineering — the strategy, stated in hiring"* — was one of its sharpest lines, and
   there is no Braze counterpart. The Greenhouse board API is named in the log as an
   untried route.

6. **`QUESTIONS.md` shows little sign of having been worked.** The open-questions
   section still reads largely as the pre-research template.

---

## 8 · What to do, in priority order

Ranked by how much each changes the quality of what the audience receives.

| # | Fix | Effort | Why it is ranked here |
|---|---|---|---|
| 1 | **Bring six record chapters to ~2,000 words**, using `04-platform` as the model. Argument, not annotated facts | High | The record is the deliverable that survives the meeting, and it is at 29% |
| 2 | **Run a dedicated conflicts pass.** Sweep headcount, customer count, geography, pricing and channel drift specifically | Medium | Five is too few, and the gaps are in the highest-traffic numbers |
| 3 | **Give the deck a visual language.** Call `worldmap()` for the fifteen clusters; add an architecture diagram for the ingestion paths; put a mark on the title slide | Medium | Currently a text document being narrated |
| 4 | **Rewrite notes on the six strongest slides to 350–450 words.** US-08, the material weakness, the earn-out, real-time, the AI provenance, the Gartner shortlist | Medium | No slide currently gives the presenter room to argue |
| 5 | **Tighten the 19 airy slides.** Add a figure row, a caption band, or merge two thin slides | Low | Measurable, mechanical, immediately visible |
| 6 | **Fix the four small defects**: the stale "Empty" line, the missing record corrections log, the wrong cluster count in `DECK-SPEC.md`, and the unworked `QUESTIONS.md` | Low | Each is minutes, and each is the kind of thing a hostile reader finds first |
| 7 | **Surface the favourable findings.** Three hypotheses died in Braze's favour; the deck should say so | Low | Balance is what makes the critical findings credible |
| 8 | **Retry the careers board via the Greenhouse API** for the department histogram | Low | Optional. Only if it is cheap |

---

## 9 · The one-line summary

**The research is better than the reference project. The book and the performance are not.**
Everything in section 8 is presentation work on top of an evidence base that is already
sound — which is the good kind of problem, because none of it requires going back to the
sources.

---

## 10 · What was done — closing record, 2026-09-02

Written after the work, against section 8 in the order given. Every claim below is
re-checkable: `python3 tools/verify.py` for the gates, `bash tools/make_release.sh` for
the artefacts.

### The gates, after

| Gate | Before | After |
|---|---|---|
| `tools/verify.py` | 9 passed · 0 failed | **9 passed · 0 failed** · 1 standing manual warning |
| Evidence record | 8,375 words · 8 sub-headings | **16,275 words · 61 sub-headings** |
| Conflicts, all with rulings | 5 | **9** |
| `FACTS.md` rows | 189 | **219** |
| Deck | 41 slides | **42 slides** |
| Speaker notes | mean 138 · longest 268 | **mean 209 · longest 554** |
| Slides overflowing the safe line | 5 (undetected) | **0** |
| PDF | 41 pages, fallback fonts checked | **42 pages · 42 slides · no fallback fonts** |

Reference-project comparators, for calibration rather than as targets: record 28,530
words and 95 sub-sections, 21 conflicts, notes mean 238 and longest 858. The record is
now at 57% of the reference by words where it was at 29%, and the notes exceed it on the
strongest slides while sitting below it on the mean — which is the right shape, because
this deck has more slides that are a single sourced fact.

### Item by item

**1 · Record chapters to ~2,000 words — done, and not by padding.** Seven chapters
rewritten; `04-platform.md` left alone as the density model. What was added is the
reasoning that connects facts that were already there: how to read a purchase-price
allocation and why a $0.9m trademark valuation tells you the name was never going to
survive (§3.1); why a zero earn-out is precise about one thing and silent about
everything else (§3.2); how much a material weakness should actually move your confidence,
and the three independent checks that came back clean (§2.1b); what "ultimate parent-level
entity" does to the $283,000 price bound (§7.1); why the retention figures describe a
business shifting from expansion to acquisition (§7.2). Two chapters landed under 2,000
and are left there — `03-acquisitions.md` at 1,640 and `06-ai.md` at 1,731 — because the
argument finished. `01-company.md` at 1,877 likewise.

**2 · Dedicated conflicts pass — done.** Four new conflicts, each with a ruling: **C-06**
the review panels disagreeing with themselves on their own denominators; **C-07** the 10-K
and the proxy giving different headcounts for the same date, on different definitions;
**C-08** "customer" meaning ultimate parent entity, which changes what the price bound
measures; **C-09** the fifteen group entities including a majority-held VIE. None of these
were visible without going looking, which is the argument for the sweep.

**3 · Visual language — done.** `worldmap()` now carries the cluster geography on slide 29;
slide 20 is an inline SVG of four ingestion lanes converging on one profile store, which is
the shape of the finding rather than a list of it; the title slide carries an abstract mark.
The mark is deliberately **not** Braze's logo — reproducing a vendor's own branding on a
competitive teardown reads as impersonation, and an abstract glyph does the same layout job.

**4 · Notes on the strongest slides — done, seven not six.** Slides 8 (material weakness),
10 (earn-out), 15 (hiring), 16 (Gartner shortlist), 20 and 37 (real-time), 31 (AI
provenance), 34 (US-08), 39 (the favourable kills). Each carries the reasoning, the
counter-argument, and what not to say. The rule applied throughout: a note earns its length
by containing something the slide cannot show — usually the fairness, usually the sentence
that stops the finding being over-read.

**5 · The airy slides — partially done, and the metric was not chased.** Sparse bodies now
scale their hero element to the frame through a CSS quantity query rather than being
padded with content, and the worst case fell from 289px of unused height to 247px. But 20
slides still sit above the 120px threshold, and that is a deliberate stop: filling them
further would mean either inflating type past the point where it reads well, or adding
content for the sake of area, which is the padding the brief forbids. What *was* fixed is
more serious than the airiness and was not in the critique — see "what the critique missed"
below.

**6 · Small defects — all done.** The stale "Empty, and it will not stay that way" line is
gone. The record has a real corrections log at §8.2, now six numbered rows. `DECK-SPEC.md`
says fifteen clusters in both the table and the prose, and its slide-31 row says five lenses
rather than four. `QUESTIONS.md` is worked: all 45 pre-research questions now carry where
they were answered, seven are marked answered **in part** with the missing half named, and
two (#43, #44) are marked not attempted rather than quietly dropped.

**7 · Favourable findings — done, with a slide of its own.** New slide 39, *"Three things we
expected to find, and did not"*: H1 the efficiency result, H4 the SDK maintenance record, H9
the falling incident rate — each with its caveat attached in the same breath, because a
favourable finding stripped of its caveat is exactly as dishonest as an unfavourable one.
Recorded in the evidence record at §8.0 with the reasoning that matters more than the three
findings: four failures out of ten hypotheses is what genuine priors look like, and a set
that all confirmed would have meant they were written to confirm.

**8 · Careers board — done, and it closed an open question.** `tools/careers_board.py` pulls
the Greenhouse board as unauthenticated JSON. **296 open roles across 15 hiring departments:
Sales 89, Engineering 57, Customer Experience 38. Go-to-market is 72.0% of the board against
19.6% for engineering and product — 3.7 to one.** Read against §7.2's retention figures it is
a leading indicator of the shift from expansion to acquisition, and it is stated with two
limits: a requisition is an intention rather than a person, and headcount ratio is not spend
ratio (the audited figure is 1.96:1, §2.3). Question 56 is closed, the correction is logged,
and the transferable lesson is in the record: **when a page will not yield, look for the API
behind it before recording a gap.**

### Nothing was rejected outright

Every item was worked. Item 5 is the only one stopped short of its stated target, for the
reason given above; the judgement is recorded here rather than left as a silent shortfall.

### What the critique missed, and what this pass found

Two things worth more than several of the items above, neither of which was in the review.

**Five slides were overflowing their frame.** Content on slides 8, 14, 29, 31 and 38 ran past
the safe line into the footer. My own self-review had checked `scrollWidth`/`scrollHeight` on
the *section* and found nothing, because the section clips at the stage boundary — the
overflow was on the inner `.body`. Checking the wrong element returned a clean result and I
believed it. Fixed by tightening the bar-chart row pitch, removing a double-counted margin
under `.ruleband`, and reducing card padding inside split columns. **All 42 slides now
report zero overflow.**

**The title slide said "41 slides" as a hardcoded string.** It was correct until this pass
added one. A deck that miscounts itself on slide 1 undermines every count that follows, so
it is now a `__SLIDECOUNT__` token substituted by `build_deck.py` from the assembled deck
and cannot drift again.

Two smaller ones, both caught only by looking at the rendered slide rather than the markup:
a legend key on slide 29 pointed at a colour nothing on the map used, and an arrow glyph
inside the new SVG pulled Menlo into the PDF as a fallback font because JetBrains Mono's
latin subset has no U+2192.

And one stale claim that the closing question closed: slide 40 still listed the hiring split
as an open gap **after** item 8 had answered it. It would have been a false statement in
front of an audience, made by the same pass that produced the answer. It is replaced with
question 57, and the note now says out loud that a fifth gap was on that slide until the
Greenhouse API closed it.
