# Critique v4 — the operator's read-through

Written 2026-09-02 against commit `0a6a5bc`. Unlike the first three, this one starts from
**the operator's own slide-by-slide comments after watching the deck**, each verified
against what the deck actually does.

Two things to hold on to while reading it.

**Silence is approval.** The operator commented on eleven slides. The other thirty-one were
read and passed over. **Do not touch them.** Every previous round improved things the
operator had not complained about; this round must not.

**Eleven comments, five causes.** They are not eleven unrelated notes. Four of the five
causes are systemic and will recur on slides nobody has complained about yet, so fix the
cause and then check the whole deck against it.

---

## 1 · The five causes

| # | Cause | Comments it explains | Severity |
|---|---|---|---|
| **A** | The deck assumes vocabulary the audience does not have | 5, 10, 12, 18, 22 | **highest** |
| **B** | Headlines use words that never appear on the slide | 6, 15 | high |
| **C** | Evidence-grade colours reused to mean something else | 16 | high — breaks a documented rule |
| **D** | Logos are placed as decoration rather than on the grid | 1, 6, 9 | medium |
| **E** | A correct number presented in a form that invites doubt | 11 | medium |

---

## 2 · Cause A — the vocabulary problem

This is the big one, and it is the root of five of the eleven comments.

**Seventeen specialist terms appear in the deck. Not one is defined.** Where each first
lands on the audience:

| Term | First appears | On how many slides |
|---|---|---|
| **sub-processor** | **slide 1** | 10 |
| **10-K** | **slide 5** | 7 |
| allowlist | slide 5 | 2 |
| material weakness | slide 8 | 1 |
| goodwill | slide 9 | 1 |
| **earn-out** | **slide 10** | 1 |
| Canvas · Liquid · MongoDB · Connected Content | slide 18 | 6 / 4 / 4 / 2 |
| CDI | slide 20 | 1 |
| Currents | slide 21 | 6 |
| Snowflake · Segment Extensions · holdout | slide 22 | 4 / 1 / 2 |
| RPO | slide 34 | 1 |

The operator's exact words on slide 12 — *"You should explain somewhere in the start what
is this 10-K"* — are the general case. **"Sub-processor" is worse: it is on the title
slide.**

### The fix — three moves, in order of value

**1 · Define on first use, in-line, in four words or fewer.** Not a glossary slide — a
glossary is a slide people do not read. The definition rides along with the first use and
never appears again:

> the **10-K** (their audited annual report to the regulator)
> an **earn-out** (extra payment, only if targets are hit)
> **goodwill** (the part of a price not attached to any identifiable asset)
> a **sub-processor** (an outside supplier that touches customer data)
> a **holdout** (a group deliberately left un-messaged, to measure lift)

**2 · Add one orientation slide after slide 4.** Not a glossary — *"the four documents this
analysis rests on"*: the 10-K, the proxy, the sub-processor disclosure and the status page,
one line each on what it is and why it cannot easily be false. This is the single highest-
value addition available, it costs one slide, and it makes every filing reference afterwards
land. It also strengthens the argument: the audience learns *why* these sources beat
marketing before hearing what they say.

**3 · Strip product jargon from captions where the caption is not about the product name.**
Slide 18's stage 2 currently reads *"MongoDB — and it is billed per attribute"*: a database
name and a billing model in six words, neither explained, and they are two unrelated ideas.
The stage caption should say what happens: *"the profile is updated — and you are billed per
change"*. The database name belongs on slide 22 where it is the point.

---

## 3 · Cause B — headlines that promise words the slide never says

**Slide 15.** The headline is *"Well rated. The complaints are about progression."* The word
**progression appears nowhere on the slide.** What is there, buried inside a card titled
"What their own summary names", is Glassdoor's own phrase: *"limited upward mobility and
discrepancies in compensation relative to market rates"*. The operator's question — *"what
progression, why can't I see that on the slide?"* — is exactly right: the headline
paraphrases into a word the body never uses.

Two ways to fix it, and **only one is honest**: promote the evidence, do not soften the
headline. Pull *"limited upward mobility"* out of the card and make it the thing the eye
lands on. Then the headline can stay, because the slide now says it.

Slide 15 is also carrying five separate ideas — four rating figures, a work-life-balance
finding, their own summary, the hiring count, and a hiring breakdown with a caveat. **That
is why the important one is invisible.** Cut the work-life-balance card: it exists to say
"no trend is claimed", which is a fine sentence for the notes and a waste of a card.

**Slide 6.** The headline is *"Lawyered, filed, and still says real-time."* The operator
does not understand it, and it fails the covered-slide test from
[`CRITIQUE-3.md`](CRITIQUE-3.md) §4.3: a stranger cannot say what it argues. "Lawyered" is
not a claim, and the turn depends on knowing that a 10-K is legally reviewed — which the
audience has not been told. It is a Kind B claim built on a fact the audience does not yet
have.

Rewrite it as a claim that stands alone. The finding is that a legally-reviewed document
still makes a marketing claim. Something in the shape of *"Their strongest claim, in their
most careful document"* — a claim, under nine words, and comprehensible cold.

---

## 4 · Cause C — the amber boxes on slide 16

The operator says the yellow boxes are not intuitive. They are right, and it is a rule
violation rather than a taste question.

On slide 16, five vendor names carry `class="logo acc"`, which resolves to
`border-color: var(--medium)` — **`#D9A441`, the deck's amber evidence-grade colour.**

`deck/COMPONENTS.md` states the rule the deck breaks here:

> Grade colours — green, amber, red — are reserved for the evidence system, so a big number
> is never tinted amber and misread as a grade.

By slide 16 the audience has been taught, on slide 3, that amber means *medium-confidence
evidence*. On this slide amber means *"on the buyer list but absent from the 10-K"*. Two
meanings, one colour, no legend. A viewer who learned the first meaning reads these five
vendors as shakily-sourced — the opposite of the point, since the Gartner shortlist is the
more independent of the two lists.

**A second defect the operator did not name:** the highlighting is one-directional. Klaviyo
appears in the 10-K list and *not* on the buyer list, and nothing marks it. The slide's
argument is a two-way gap; the visual encodes one way.

**The fix.** Take the colour off entirely. The two lists are already side by side with
headed columns — the gap is visible from the counts alone, and the rule band underneath
states it in words. If a visual marker is wanted, use a **neutral** one that carries no
grade meaning: a dot, a rule, or the existing `.logo` versus a dimmed variant. And mark
**both** asymmetries, or neither.

---

## 5 · Cause D — the logos

### Slide 1

The operator's three points, all correct:

**The name is said twice.** A white plate containing the black `braze` script wordmark, and
directly beneath it *"Braze"* set in Instrument Serif. Two typefaces, one word, 60 pixels
apart.

**The purple wordmark would be better.** Braze's brand colour is violet. The black-on-white
version needs a white plate to sit on, and on a dark deck that plate is a bright rectangle
that is the first thing the eye goes to — brighter than the title. **A purple-on-dark
wordmark needs no plate at all**, which removes the redundancy and the bright box in one
move.

**The date.** *"Public sources only · captured 1–2 September 2026"* → *"Public sources only ·
September 2026"*. Capture dates belong in `FACTS.md`, where they already are.

**Recommended layout:** the purple wordmark, no plate, at the position the serif "Braze"
occupies now; `COMPETITOR ANALYSIS` beneath it as it is; and drop the `<h1>Braze</h1>`. The
wordmark *is* the name. If the typographic title is preferred instead, keep the `<h1>` and
drop the logo from slide 1 entirely — it appears again on slide 6. **Either is right. Both
together is the mistake.**

### Slides 6 and 9

The `.brandtag` is a white plate pinned to the top-right corner. Two problems remain after
v3's fix:

**It is still the loudest object on the slide.** Same cause as slide 1: a white rectangle on
a dark ground. Use the purple wordmark with no plate on slide 6. OfferFit's logo may only
exist dark-on-light, in which case it keeps a plate — but then **the rule is: if any logo
needs a plate, they all get one.** Consistency beats optimising each slide alone.

**It aligns to a corner, not to the content.** Pinning to `top:56px; right:74px` puts it in
the corner of the *canvas*. The eye reads it against the eyebrow and the headline, which are
content. Align its optical top to the eyebrow's cap-height and its right edge to the body's
right margin, so it belongs to the same grid as the words.

---

## 6 · Cause E — slide 11's number is right, and the slide should say why it looks wrong

The operator asks whether the numbers are sure. **They are.** Verified:

- $738.2m FY2026 revenue ÷ 2,609 customers = **$282,944**, rounded to ~$283,000 ✓
- `FACTS.md:175` records it as *"Bounded at ~$283,000 … A bound, not a price: it mixes every
  contract size and includes professional services"* ✓
- `FACTS.md:458` records that **zero** transacted prices were found in any captured source ✓
- The slide already labels it *"a bound, not a price"* ✓

So the arithmetic and the sourcing are sound. **The doubt is well-founded anyway**, and the
slide should answer it rather than leave the audience to feel it: **a mean is not a typical
customer.** A handful of very large contracts pull it up, and most customers pay far less
than $283,000. `FACTS.md` says this — *"it mixes every contract size"* — and the slide does
not.

**The fix is one line, not a redesign.** Under the figure: *"An average, not a typical
contract — a few very large customers pull it up, and most pay far less."* That converts a
number the audience privately distrusts into one they can use, and it costs nothing but
honesty the record already contains.

---

## 7 · The remaining two, briefly

**Slide 5 — the five things.** The operator finds the title acceptable but the fifth fact
hard to digest. *"Buyers weigh them against twice as many vendors as they name. The 10-K
names four competitors. Gartner's buyer-derived shortlist has eight — and the five extra are
specialists Braze never mentions."* Three numbers (four, eight, five), two sources, one
undefined term, in a card the size of the other four.

Compress to the one thing worth remembering: **"Braze names four competitors. Buyers compare
them against eight."** The detail lives on slide 16, which is where the audience will meet
it properly.

Then apply the same test to the other four cards: **each should be one sentence a person
could repeat at dinner, plus at most one supporting line.** Card 1 currently carries two
separate findings (ingestion paths *and* the export limit) — split the second out or drop
it to the notes.

On the title: *"If you remember five things"* is fine, and a conventional
*"Executive summary"* is also fine. The eyebrow already says `EXECUTIVE SUMMARY`, so the
framework the operator is asking for is present. **Leave it.**

**Slide 10 — the acquisition.** Three fixes, in order:

1. **Define the term.** *"earn-out"* appears in the headline and three times in the body,
   undefined. Add four words at first use.
2. **Make the three figures tell the story in sequence.** They currently read as three
   unrelated amounts. They are one sentence: *"$26.8m paid. A further $26.0m available if
   targets were met. None of it paid."*
3. **Delete the missing-logo note.** *"No North Star Y mark appears here because none
   survives: the domains do not resolve and there is no archive capture."* That is admirable
   provenance discipline and it belongs in `sources/media/PROVENANCE.md`, where it already
   is. On the slide it is the analyst talking about their own process during a slide about an
   acquisition.

**Slide 18 and 22 — understandable, without complicating.** The operator's constraint is the
important half of the instruction. Do not add anything.

*Slide 18:* the closing line says two of the seven stages are where the evidence got
interesting, and the diagram does not show which. `flow()` already takes a `mark=` argument
for exactly this — mark stages 1 and 6. Then strip the jargon from the stage captions per
§2.3. **Nothing is added; two things are removed and one is highlighted.**

*Slide 22:* the structure — rule-based on MongoDB versus model-based on Snowflake — is
sound, and the payoff quote is excellent. What is missing is the one sentence saying why an
audience should care before the detail arrives: **two decision systems on two databases that
do not talk to each other.** Put that above the two columns, define "holdout" in four words,
and leave everything else.

---

## 8 · One question only the operator can answer

The Insider One title slide carried a byline: *"Toma Pirtskhelani · Product Manager at Optio
AI"*. **The Braze title slide has no byline at all.** The comment — *"there is no Toma
Pirtskehlani product manager at Optio"* — can be read either as *it is missing and should be
there* or as *do not put that on it*.

**Ask before building.** If a byline is wanted, it goes where the reference deck put it, on
the left of the footer line. If not, the footer keeps only *"Public sources only ·
September 2026"* on the right and the slide-count line on the left, as now.

---

## 9 · The work, in order

| # | Do | Slides |
|---|---|---|
| 1 | Define every specialist term at first use, in four words or fewer | throughout — start with **sub-processor** (slide 1) and **10-K** (slide 5) |
| 2 | Add the *"four documents this rests on"* orientation slide | after 4 |
| 3 | Purple wordmark, no plate; remove the duplicate name; date to *September 2026*; resolve the byline question | 1 |
| 4 | Same logo treatment on 6 and 9 — consistent plating, aligned to content not to the corner | 6, 9 |
| 5 | Rewrite the headline so it stands alone cold | 6 |
| 6 | Remove the amber; mark both asymmetries or neither | 16 |
| 7 | Promote *"limited upward mobility"* into the body; cut the work-life-balance card | 15 |
| 8 | Add the one-line "an average, not a typical contract" caveat | 11 |
| 9 | Compress the fifth card; one repeatable sentence per card | 5 |
| 10 | Define earn-out; sequence the three figures; delete the missing-logo note | 10 |
| 11 | `mark=` stages 1 and 6; strip jargon from captions | 18 |
| 12 | One framing sentence above the columns; define holdout | 22 |
| 13 | Rebuild all three artefacts, re-cut the release, look at all 43 slides | — |

**Do not touch slides 2, 3, 4, 7, 8, 13, 14, 17, 19, 20, 21, 23–42.** They were read and
approved.

---

## 10 · Definition of done

- No specialist term is used before it is defined
- Every headline passes the covered-slide test **cold**, with no prior slide's knowledge
- No evidence-grade colour carries a non-evidence meaning anywhere in the deck
- Every logo has the same treatment and sits on the content grid
- No slide carries more than one idea per card, and no card carries two findings
- `tools/verify.py` still reports 0 failures
- The release is re-cut, and all slides have been looked at

**Nothing in this round requires reopening a source.** Every fact needed is already in
`docs/FACTS.md`. This is entirely about making what is already true possible to follow.
