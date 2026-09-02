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

---

## 7 · What was done — closing record, 2026-09-02

Against §5, in order. Nothing in `sources/` was reopened; no fact, conflict or record
section was added. This was presentation work, as instructed.

### Definition of done, checked

| | Target | Result |
|---|---|---|
| Every headline passes the covered-slide test | — | **42 / 42**, rewritten or deliberately kept |
| Mean headline length | ≤ 6 words | **6.02** |
| Longest headline | ≤ 10 | **9** (three of them) |
| Two-beat headlines | more than 4 | **8** |
| No image's edge aligns with nothing | — | **plate 74px = title 74px; brandtags y=64 = eyebrow y=64** |
| One photographic treatment per slide | — | **yes** — the second one was dropped |
| `tools/verify.py` | 0 failures | **9 pass · 0 fail** |
| Release re-cut | 42 pages, no fallback fonts | **42 pages, 5 fonts, none fallback, 5 images embedded** |
| Slides overflowing | 0 | **0** (was 2 at 2–3px) |
| All 42 looked at | — | yes |

### Item 1 · The headlines

**26 of 42 rewritten**, including all ten flagged in §4.4. Mean 7.3 → **6.02 words**;
two-beat structures 4 → **8**; nothing now over nine words; slide 42 has a headline.

The ten that had to change:

| # | Was | Now | Kind |
|---|---|---|---|
| 6 | Who they say they are | **Lawyered, filed, and still says real-time** | claim |
| 8 | Seven years of audited revenue | **7.7× bigger, a billion already contracted** | claim |
| 13 | Wide, thin, and carrying a heavy base | **No second home market** | claim |
| 15 | Strong culture; the complaints are about ceilings | **Well rated. The complaints are about progression** | claim |
| 20 | Their table. Their words. Three of four are not real-time | **Their words: three of four are not real-time** | claim |
| 21 | Generous at the top, narrow at the bottom, quiet when it fails | **A merge can fail and still return success** | claim |
| 24 | Liquid is the substrate, and it is also the complaint | **Liquid does the work, and draws the complaints** | claim |
| 27 | Thirteen documented. Ten marketed. The drift runs both ways | **Thirteen documented. Ten marketed.** | claim |
| 28 | Broad, and documented shallowly | **Wide network, one page deep** | claim |
| 42 | *(none)* | **One thing to remember** | label |

Sixteen more were over the word budget or were labels written as sentences — the sharpest
of them **"They name four. Buyers weigh eight."** (was eleven words), and
**"One campaign, end to end"** (was a seven-word label). The three §4.5 names as
already-right — slides 9, 11 and 25 — were not touched.

Two things went wrong doing this and are worth recording because both were silent.

**A replacement landed on a `data-t` label instead of a headline, twice.** Slides 2 and 6
had headlines identical to their labels, so a naive string replace hit the label first.
Caught by dumping every `data-t` after the pass and reading the list. Both labels are
restored; §4.5's warning was correct and I still walked into it.

**A third landed on a card title.** Slide 16's old headline was also the text of an
executive-summary card on slide 5, and the replace hit slide 5. Caught by auditing the
built deck and finding slide 16 unchanged. The card is restored. **Every one of the 26 new
strings was then verified to appear inside a `head()` call**, not anywhere else.

### Items 2–5 · The image system

**a.** The title plate and the title now share a left edge at **74px**. The diagnosis is
slightly different from §3.1's: `.title-s` carried `padding-left:104px` and **it has never
applied** — `section.s` is element-plus-class and out-specifies a bare class, so the title
slide has always sat on the same 74px margin as every other slide. What actually hung
17px out of line was the *wordmark inside the plate*, pushed right by the plate's own
padding. The dead declaration is deleted rather than resurrected (with a comment saying
why), and the plate's padding is tightened so the mark sits a few pixels from the "B".

**b.** `.brandtag` moved to `top:56px`. Measured after: the card's top edge and the
eyebrow's top edge are both at **y = 64** in stage coordinates, on slides 6 and 9. One
horizon.

**c and d.** **The TechCrunch photograph is dropped, as recommended.** With it gone, (c)
dissolves: one image in the column, one width, no ragged edge. The file stays in
`sources/media/` because it is real evidence — the only photograph of the founding pair on
any Braze property — and `PROVENANCE.md` now records it as *captured, not used*, with the
reason. `tools/build_assets.py` no longer encodes it and says in a comment what restoring
it would take. `deck/assets.py` fell from 82 KB to **49 KB**.

**5.** The §3.3 rule is in `deck/COMPONENTS.md`, alongside the headline mechanism from §4
and the `data-t` warning, so both survive this conversation.

### Item 6 · Dead space

Re-measured: **20 of 37 slides over 120px, median 132px** — one worse than before, because
dropping the photograph gave slide 7 back its slack. That trade is right and I would make
it again. Two hairline overflows (2px and 3px) that had been sitting under my own
threshold were cleared, so the deck is now genuinely at **zero**.

My position on the metric is unchanged from CRITIQUE-2 §10 and I have not spent more time
on it.

---

## 8 · Where I push back on this review

You asked whether any of this critique repeats the mistake §2 admits to. **One thing does,
and it is the same shape.**

**"Mean headline length at or under 6 words" is a measurable target that invites the
behaviour it is meant to prevent.** §2 says a target that is easy to measure will be hit
whether or not it is right — and then §6 sets one. It landed at 6.02, and I want to be
explicit that some of the final tenths came from trimming words like *simply* and *since
2016* out of headlines that already passed the covered-slide test. Those trims are
improvements, but they were made to a number, not to a reader.

The deeper problem is that the reference deck's 5.0 mean is a fact about **its mix of
slides, not about good headline length**. That deck has more pure orientation slides; this
one has more slides carrying a finding, and a finding takes more words than a label.
`"They name four. Buyers weigh eight."` is five words because the finding happens to be
symmetrical. `"A merge can fail and still return success"` is eight because that is what
the finding is, and no shorter version is honest. **The mechanism in §4.2 is right and I
used it on all 42. The mean is a by-product and should not have been a criterion.** If a
future pass finds itself shaving a word off an accurate headline, it should stop.

Two smaller ones.

**§3.1a's diagnosis was wrong in a way that mattered.** The prescription — align the plate
with the title column at 104px — would have moved the plate 30px *away* from the text it
was supposed to align with, because the text is at 74px and always has been. Following the
instruction literally would have made the defect worse. The instruction to *align them* was
right; the coordinate was not, and the underlying cause was a CSS specificity bug neither
of us had looked for.

**§4.4 calls out five failure classes and names ten slides, then §4.5 says "the nine named
above".** All ten were rewritten.

---

## 9 · What is still weak

- **Dead space**, on this review's terms: 20 of 37 slides carry more than 120px. Argued in
  CRITIQUE-2 §10 and not revisited.
- **`.mark` and `.stat` are still unused** in the design system. `.mark` is a 50px square
  slot and Braze's wordmark is 2.1:1 on transparent black, so it needs a plate; the class
  now has no caller and should probably be deleted by whoever next touches `css.py`.
- **No North Star Y logo**, for the reason in `PROVENANCE.md`. Unchanged and unfixable
  from public sources.
- **Four headlines are still nine words** — slides 9, 10, 11 and 39. Two of them (9 and
  11) are named in §4.5 as already right; 10 mirrors 9's shape deliberately, and 39 is the
  favourable-findings slide, where the turn needs the words.
- **The evidence record is at 61% of the reference by words and 57% by conflicts**, and
  per §1 that is where it stops.
