# Critique v3 — the finishing pass

Written 2026-09-02 against commit `38d8907`, following [`CRITIQUE.md`](CRITIQUE.md) and
[`CRITIQUE-2.md`](CRITIQUE-2.md). This is the last one. It covers two things only, because
only two things are left: **how the pictures sit on the page**, and **what the slides are
called**.

It also opens with something the earlier two lacked: an account of where *those* critiques
were wrong, because some of what is wrong with the deck now is my fault.

---

## 1 · Where it actually stands

The substance is finished. Measured against the reference project:

| | Braze now | Insider One | |
|---|---|---|---|
| Speaker notes, total | **9,882** | 9,770 | **ahead** |
| Speaker notes, mean/slide | **235** | 238 | parity |
| Deck weight | **330 KB** | 335 KB | parity |
| Slides | 42 | 41 | parity |
| `FACTS.md` rows | **219** | 101 | **ahead** |
| Evidence record, words | 17,424 | 28,530 | 61% |
| Conflicts with rulings | 13 | 21 | 62% |
| Verifier | 9 pass · 0 fail | 9 pass · 0 fail | parity |
| Images in the deck | **5** | 5 | parity |
| Named people | **yes** | yes | parity |

**Stop growing the record and stop hunting conflicts.** 17,424 words and 13 conflicts is
enough. The remaining gap to the reference project is not a defect — that project covered a
company with a messier corporate history and more contradictions to record. Two rounds of
chasing its numbers is where the effort should end.

`sources/media/PROVENANCE.md` deserves a specific mention: it records where every image came
from, states the nominative-use basis, and marks the files immutable with
`tools/build_assets.py` as the only path into `deck/assets.py`. That is better discipline
than the reference project managed.

---

## 2 · What was wrong with my own critiques

Some of what is wrong with the deck now is a direct result of how I wrote v1 and v2. Worth
saying plainly, because it changes how this critique should be read.

**I gave numeric targets, and got numbers.** I wrote "bring six record chapters to ~2,000
words" and benchmarked everything as a percentage of the reference project. Chapters duly
arrived at 1,640–2,547 words. But word count was never the thing that mattered — the
reasoning between the facts was — and by naming a number I invited padding and made it
harder to tell growth from improvement. **A target that is easy to measure will be hit
whether or not it is the right target.**

**I benchmarked parity where parity was not the goal.** "Conflicts at 10 against 21" reads
as a 52% shortfall. But 21 was never correct-by-definition; it was however many real
disagreements one company happened to produce. I should have asked whether each *missing*
conflict existed, not whether the count matched.

**I used citation count as a proxy for citation quality.** Counting `<code>` tags is crude.
A chapter can be well sourced with fewer references and badly sourced with more.

**I asked for images without specifying how they should sit.** v2 §3.3 gave file names, CSS
classes and a code snippet — a checklist, not a design brief. Nothing in it said the images
had to share a geometry, or that one slide should not carry two different photo treatments.
The result is exactly what an under-specified brief produces: the images are present,
correctly sourced, honestly documented, and **badly placed**. That one is on me.

**And across two full critiques I never once looked at the slide titles** — the single most
audience-facing element of the entire deck. I measured dead pixels and counted `<div>`s and
did not read the headlines. That is the biggest miss in either document, and section 4
exists to repair it.

---

## 3 · The image system — what is wrong, and the geometry that fixes it

The images are the right images. The problem is entirely placement, and it is measurable.

### 3.1 · The four defects, with numbers

Measured at render, converted to the deck's own 1280×720 coordinates.

**a. The title-slide plate is misaligned with the title.** `.titleplate` sits at
**x ≈ 87px**. The title slide's text column starts at **x = 104px** (`.title-s` has
`padding-left:104px`). The brand plate hangs **17px to the left of every word beneath it**,
on the first slide anyone sees.

**b. The brand tags float at a height that matches nothing.** On slides 6 and 9 the
`.brandtag` top edge is at **y ≈ 66px**; the eyebrow above the headline is at **y ≈ 56px**.
Ten pixels off — close enough to look like a mistake rather than a decision. They are
correctly right-aligned to each other, which is the one thing that is right.

**c. Slide 7 puts two different photo shapes in one column at two different widths.** The
circular `.figurehead` renders **120px wide**; the rectangular `.photoblock` beneath it
renders **215px wide**. Both are left-aligned at the content margin, so the column has a
**ragged right edge**, and the wider photo's right edge lands at **289px** — within a pixel
or two of where the adjacent text column begins. It reads as a collision, because it is one.

**d. Two photographic treatments on one slide.** A clean circular portrait above a raw
rectangular screen-grab whose source is a low-resolution capture — visible cropped lettering
along its top edge, and it is being displayed at 192×145 from a 560×421 original that was
never clean to begin with.

### 3.2 · The rule that fixes all four

**Every image on a slide belongs to a column, and every column has one width.**

That is the whole principle. The reference deck obeys it without stating it: its portrait
sits inside a `split` whose left column has a fixed width, and its logos sit in plates whose
width is set explicitly per slide.

Concretely:

| Fix | What to do |
|---|---|
| **a** | Set the title plate's left edge to the title column: `104px`. It must align with the `B` of "Braze" below it |
| **b** | Give `.brandtag` `top:56px` so its top edge is the eyebrow's top edge. One shared horizon across every slide that carries a logo |
| **c** | Pick **one** left-column width for slide 7 — 200px is right — and make both the portrait and the photo exactly that wide. The circle becomes a 200px circle, or the photo shrinks to the circle's width. **Do not leave two widths** |
| **d** | Either drop the TechCrunch photograph, or give it the same treatment as the portrait. Two shapes on one slide is one shape too many. If it stays, it needs the same corner radius and the same border as its neighbour |

**On (d), the honest recommendation: drop it.** The image is low quality, it is the weakest
thing on an otherwise strong slide, and its caption already admits the analysis cannot tell
which founder is which. A single well-placed portrait says more than a portrait plus a bad
snapshot.

### 3.3 · One rule for the whole deck

Add this to `deck/COMPONENTS.md` so it survives:

> **Images sit on the same grid as type.** An image's left edge aligns with the text column
> it belongs to, or its right edge aligns with the slide's right margin — never neither.
> Its top edge aligns with the eyebrow, the headline, or the first line of the body it sits
> beside. One slide carries one photographic treatment. Two images in one column share one
> width.

---

## 4 · The title mechanism

This is the part to get right, and it is the part neither earlier critique addressed.

### 4.1 · The measurement

| | Insider One | Braze |
|---|---|---|
| Mean words per headline | **5.0** | 7.3 |
| Median | **5** | 8 |
| Longest | 10 | **12** |
| Headlines split into two short beats | **7** | 4 |

Braze's headlines are **46% longer** and use the two-beat structure **less often**. That is
precisely backwards: the two-beat structure is what makes the reference deck's titles land,
and length is what kills them.

### 4.2 · The mechanism, derived from what actually worked

Every headline is **one of exactly two kinds**. Decide which before writing it.

---

**KIND A — THE LABEL.** For a slide whose job is orientation: a stage in a sequence, an
inventory, a mechanism. The audience needs to know *where they are*, not to be persuaded.

- **2 to 5 words. A noun phrase. No verb.**
- Plain to the point of being boring. That is correct — the content carries the interest.

From the reference deck: *Getting the data in* · *Identity resolution* · *Geography* ·
*Industries* · *Three ways to see what worked* · *Where the campaign is assembled*

---

**KIND B — THE CLAIM.** For a slide that carries a finding. The headline **states the
finding**, not the topic of the finding.

- **5 to 9 words.** Over ten, cut it.
- **Prefer two short beats to one long clause.** The turn between them is the whole effect.
- Five shapes, all from the reference deck:

| Shape | Example |
|---|---|
| **Contrast** | *One person can run it. It takes weeks to learn.* |
| **Reversal** | *The barrier is not code. It is a line of credit.* |
| **Symmetry** | *Nine channels they name. Nine more they don't.* |
| **Verdict** | *Old machine learning, real. New agents, thin.* |
| **Flat statement** | *They publish no prices.* |

---

### 4.3 · The test

**Read the headline with the slide covered.** Then:

- If it is Kind A, a stranger should be able to say **what the slide is about**.
- If it is Kind B, a stranger should be able to say **what the slide argues**.
- If the honest answer is *"I can't tell what that means"* — it fails. Rewrite it.

### 4.4 · The five things that fail the test, and every Braze headline that does

**1 · Adjective strings with no subject.** The worst failure, because it reads as poetry and
carries no claim.

| Slide | Now | Why it fails |
|---|---|---|
| 13 Where they operate | *Wide, thin, and carrying a heavy base* | Three adjectives, no subject. Wide *what*? |
| 21 Stage 2: Identity | *Generous at the top, narrow at the bottom, quiet when it fails* | Three beats, no subject, and "quiet when it fails" is a riddle |
| 28 Integrations | *Broad, and documented shallowly* | A fragment. Nothing is doing anything |

**2 · Three beats where two would land.** Three beats dilute; the reference deck never goes
past two. Slides 20 (*Their table. Their words. Three of four are not real-time*) and 27
(*Thirteen documented. Ten marketed. The drift runs both ways*) both have a strong third
beat carrying a weak first two — cut to the strong part.

**3 · Jargon the room does not share.** Slide 24's *Liquid is the substrate, and it is also
the complaint* — "substrate" is a word for the analyst, not the audience. Slide 15's
*the complaints are about ceilings* — "ceilings" needs explaining, and a headline that needs
explaining has failed.

**4 · A topic where a finding exists.** Slide 6 is *Who they say they are* — a label on a
slide that has a real finding underneath it. The reference deck's equivalent was
*Their words, before any of ours*, which tells the audience how to listen. Slide 8's
*Seven years of audited revenue* is a description of the data, not of what the data shows.

**5 · No headline at all.** Slide 42 has none.

### 4.5 · What to do

Rewrite every one of the 42 headlines through the mechanism. For each: decide Kind A or
Kind B, then write to the word budget, then apply the covered-slide test.

**The nine named above are the ones that must change.** Most of the rest are already good —
*They bought their AI, and the filing says so*, *Only two channels have a named middleman*,
*Nobody publishes a price. You can still bound one* are all exactly right and should be left
alone.

**Do not invent a finding to get a Kind B headline.** If a slide is genuinely orientation,
give it a Kind A label and move on. A boring accurate label beats an exciting claim the
slide cannot support — and the whole project rests on never doing the second thing.

**One constraint that is easy to miss:** the headline and the `data-t` label are different
strings. The label is what shows in the grid and the footer, and it should stay short and
navigational. Rewriting headlines does not mean rewriting labels.

---

## 5 · The finishing list

Everything below is presentation. No source needs reopening.

| # | Do | Where |
|---|---|---|
| 1 | Rewrite all 42 headlines through §4's mechanism; the nine in §4.4 must change | `deck/slides_*.py` |
| 2 | Title plate left edge to 104px, aligned with the title text | `deck/css.py` or the slide |
| 3 | `.brandtag` top to 56px so it shares the eyebrow's horizon | `deck/css.py` |
| 4 | Slide 7: one column width for both images, or drop the TechCrunch photo — recommended | `deck/slides_*.py` |
| 5 | Add the image-grid rule from §3.3 | `deck/COMPONENTS.md` |
| 6 | Re-run the dead-space check; fix what images did not resolve | `tools/typography_audit.js` |
| 7 | Rebuild deck, script, record; re-cut the release; confirm 42 pages and no fallback fonts | `tools/make_release.sh` |
| 8 | Screenshot all 42 and look at them | — |
| 9 | Add a closing section here: what was done, what was rejected, why | this file |

**Do not** grow the record, hunt more conflicts, or add facts. That work is finished.

---

## 6 · Definition of done

- Every headline passes the covered-slide test
- Mean headline length is at or under 6 words
- No image's edge aligns with nothing
- One photographic treatment per slide
- `tools/verify.py` still 0 failures
- The release is re-cut and you have looked at all 42 slides

When that list is clear, this analysis is finished. It will be better researched than the
project it was modelled on, and it will finally look it.
