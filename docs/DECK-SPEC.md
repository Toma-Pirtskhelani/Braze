# Deck specification — 41 slides, question by question

The reference deck answered 41 questions about a competitor. This maps every one of
them onto Braze, names the evidence that answers it, and marks whether Braze can be
answered at **parity**, **deeper** (stronger evidence available here), or by a
**substitute** question when the original does not apply.

**Nothing below is a finding.** Every "answer" column names *where the answer will come
from*, not what it is. Fill the slides from `docs/FACTS.md` once the research has run.

Structure: **1 title · 4 part dividers · 36 content slides = 41.** Keep that shape —
the dividers do real work, giving the audience a breath and restating what the next
part is for.

Legend: **=** parity · **↑** deeper · **⇄** substitute

---

## Part 0 — Frame (slides 1–3)

| # | Slide | The question | Evidence | |
|---|---|---|---|---|
| 1 | Title | What is this, and what was read to build it? | Source inventory counts, verified and re-checkable | ↑ |
| 2 | How we approach it | What are the four parts and the three rules? | Method. Already written in `deck/slides_a.py` | = |
| 3 | How we grade | How do I know which claims to trust? | `docs/EVIDENCE-GRADES.md` | ↑ |

Slide 1 goes deeper only in the source strip: an audited-filings row and a status-page
row exist here that the reference deck could not offer. Slide 3 goes deeper because the
top grade changes — audited filings outrank documentation.

**Divider — Part I: The company.**

---

## Part I — The company (slides 5–16)

| # | Slide | The question | Evidence | |
|---|---|---|---|---|
| 5 | Executive summary | If you remember five things, what are they? | Written last, from the finished record | = |
| 6 | Who they say they are | What is their own story about themselves? | Marketing pages, 10-K Item 1. **Label as marketing** | = |
| 7 | Origins | Where did it come from and who still runs it? | S-1, DEF 14A, 10-K Item 1, press releases | = |
| 8 | How they got this big | What money came in, when, and on what terms? | S-1 + 10-K. **Pre-IPO rounds *and* the IPO itself, from the prospectus** | ↑ |
| 9 | Acquisition 1 | What did they buy, for how much, and what did it bring? | 8-K, 10-K business-combination notes, `PaymentsToAcquireBusinessesNetOfCashAcquired` | ↑ |
| 10 | Acquisition 2 | Same, for the next material one | As above. **Prices are disclosed here; the reference vendor never published one** | ↑ |
| 11 | What it costs | What does a customer actually pay? | Reviews, procurement records, resellers — **plus revenue ÷ customer count as a bound** | ↑ |
| 12 | Who uses it | How many customers, and how is that counted? | 10-K customer count (a *defined* metric) vs 178 customer-story URLs vs independent detection | ↑ |
| 13 | Where they operate | Which geographies really carry the business? | **10-K/10-Q geographic revenue split — audited**, vs localisation depth vs review origins | ↑ |
| 14 | What customers say | What do buyers praise and complain about? | G2 / Gartner / TrustRadius, coded by `tools/code_reviews.py` | = |
| 15 | What employees say | What does the inside look like? | Glassdoor trend, careers board, DEF 14A compensation | ↑ |
| 16 | Who they compete with | Who do they name, and who do buyers actually shortlist? | 10-K competition paragraph + their comparison pages vs **Gartner shortlists** | ↑ |

Two slides worth flagging. **#13** is a genuine upgrade: geographic revenue is an
audited disclosure, where the reference project had to infer geography from customer
domains. **#16** stays sharp only if the two halves are kept apart — who they name is
marketing; who buyers shortlist is independent, and the gap between them is the finding.

**Divider — Part II: The product.**

---

## Part II — The product (slides 18–31)

The reference deck walked one campaign through seven stages. Keep that spine: it is the
part that makes a technical analysis legible to a non-technical audience, and it forces
every capability claim to attach to a moment a customer would actually notice.

| # | Slide | The question | Evidence | |
|---|---|---|---|---|
| 18 | How one campaign works | What actually happens, end to end? | Docs, walked through and drawn | = |
| 19 | How data moves | Where does data enter, rest and leave? | Docs on ingestion, warehouse integration, export; rate limits | = |
| 20 | Stage 1 · Data | How does data get in, and how fresh is it? | Ingestion docs. **Look for a freshness table — that is where limits are admitted** | = |
| 21 | Stage 2 · Identity | How is one person resolved across devices? | Identity/alias docs. The reference project's sharpest technical finding lived here | = |
| 22 | Stage 3 · Decisioning | What decides who gets what? | Segmentation, predictive, decisioning docs | = |
| 23 | Stage 4 · Building | How is a journey actually built? | Orchestration docs + reviews on usability | = |
| 24 | Stage 5 · Content | How is a message composed and personalised? | Templating, dynamic content, generative-AI docs | = |
| 25 | Stage 6 · Delivery | How does it physically get sent, and by whom? | **Sub-processor disclosure — which channel has no middleman** | = |
| 26 | Stage 7 · Interaction | What happens when the customer replies? | Inbound, webhook, two-way channel docs | = |
| 27 | Channels | How many channels, and which are never marketed? | Docs enumeration vs marketing. **Absence of a channel is a finding** | = |
| 28 | Integrations | What connects, and is the layer built or bought? | Partner docs + sub-processor list + `braze-inc` integration repos | ↑ |
| 29 | Infrastructure | What is it built on, and what does that constrain? | Sub-processors + **status-page component groups: 12 named regional clusters** | ↑ |
| 30 | Analytics | What can you actually measure? | Reporting docs, export limits, incrementality/holdout support | = |
| 31 | The AI, honestly | What is real, what is new, what is renamed? | **Four lenses: focused-page counts, endpoint counts, review vocabulary, analyst coverage** | = |

**#29 is the clearest upgrade in Part II.** The status page names twelve regional
clusters and 132 components — an architecture disclosure the vendor made by accident,
and one no competitor's marketing will confirm or deny.

**#31 is the slide most likely to go wrong.** The reference project's rule holds
exactly: never say "their AI is thin". State the shipped ML and the agentic layer as
separate, counted things, and let the ratio speak. It is only defensible when several
independent lenses agree.

Two slides from the reference deck fold into Part II here rather than getting their own:
**design and usability** belongs inside #23, and **what they complain about** inside
#14 — unless the review coding produces something strong enough to stand alone, in
which case restore them and drop two Part III slides. Decide from the evidence, not now.

**Divider — Part III: Strategy.**

---

## Part III — Strategy (slides 33–35)

This is where Braze permits genuinely more than the reference project, and where the
temptation to overreach is strongest. Three slides, not six.

| # | Slide | The question | Evidence | |
|---|---|---|---|---|
| 33 | Where the money goes | What are they buying with revenue? | **R&D / S&M / G&A as audited lines, 7 fiscal years.** The reference deck could only ask where a funding round went | ↑ |
| 34 | What comes next | What is coming that they have not announced? | CT logs, release notes, job postings, 10-K forward language | = |
| 35 | Competitive advantages | What actually protects them? | Synthesis. Must survive the "so what would a competitor do about it" test | = |

**#33 replaces the reference deck's "where the funding went" and is strictly stronger.**
Seven years of audited operating expense is a real answer to a question that could
previously only be inferred. Resist adding four more financial slides around it — see
the equity-research trap in [`STRATEGY.md`](STRATEGY.md).

Candidates for a fourth Part III slide, if one earns it: **unit economics over time**
(gross margin trend against R&D share), **contracted-but-unrecognised revenue** as a
forward-visibility measure, or **what management is paid to optimise** from DEF 14A.
Add at most one, and only if it changes what a competitor would do.

**Divider — Part IV: Open questions.**

---

## Part IV — Open questions (slides 37–41)

| # | Slide | The question | Evidence | |
|---|---|---|---|---|
| 37 | Deep dive | One hard question, answered properly | Pick from the backlog once the research is in — see below | ⇄ |
| 38 | Reliability, measured | What does a decade of incidents show? | **451 incidents, 2016 → 2026, with durations.** No reference-deck equivalent | ⇄ |
| 39 | What we could not answer | Where do public sources run out? | Honest enumeration, with what would close each gap | = |
| 40 | Questions backlog | What should be researched next, and in what order? | `docs/QUESTIONS.md`, prioritised | = |
| 41 | Close | What is the one thing to remember? | One line. Earned, not asserted | = |

**#37 is the reference deck's "how hard is a BSP, really?" slot** — a single hard
question the audience will actually ask, answered with enough depth that nobody follows
up. Do not pick it now. Pick it after the research, from whatever turned out to be both
contested and answerable.

**#38 has no reference-deck equivalent and should exist.** A decade of timestamped
incident history is unusual, and reliability is a question buyers ask and vendors
deflect. State it as shape, never as a comparison against a vendor who publishes
nothing.

---

## Rules that apply to every slide

Carried from the reference deck, where they were arrived at the hard way.

- **One idea per slide.** If it needs two sentences to say what the slide is for, it is
  two slides.
- **The slide shows; the notes say.** Speaker notes are generated from the deck by
  `deck/make_script.py`, so they cannot drift. Write them as you write the slide.
- **Every slide carries a grade** (`s`/`m`/`w`) and it is the grade of the *weakest*
  supporting source.
- **Content stays inside the 632px safe line.** `tools/typography_audit.js` checks it.
  Test overflow with `scrollWidth` vs `clientWidth` — `getBoundingClientRect()` is
  scaled by the stage transform and will lie to you.
- **Uncomfortable findings are stated as observation, never as accusation.** It is what
  makes the favourable findings believable.
- **Look at the artefact.** Screenshot every slide before calling it done. On the
  reference project a slide's most important number once rendered as a stray glyph and
  the markup looked fine.

---

## Definition of done

- [ ] 41 slides build clean; `build_deck.py` reports no missing notes
- [ ] Every number on every slide resolves to a row in `docs/FACTS.md`
- [ ] Every slide's grade matches its weakest source
- [ ] `make_script.py` regenerated; script and deck agree by construction
- [ ] Every slide screenshotted and looked at
- [ ] Every claim traceable into `deck/evidence-record.html`, and stated there **once**
- [ ] Every hypothesis in `STRATEGY.md` either evidenced or explicitly killed
- [ ] `tools/make_release.sh` produces a PDF with no fallback fonts
