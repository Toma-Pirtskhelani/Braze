# Building the two documents

Phase 7. Two documents, deliberately, because one document trying to be both becomes
neither: the deck turns into a report nobody can present, and the report turns into a
transcript nobody can check.

| | The deck | The record |
|---|---|---|
| Organised by | Narrative order | **Subject** |
| Carries | One idea per slide | Every fact, **stated once**, with caveats |
| Answers | "What should I understand?" | "Says who?" |
| Read | Live, at pace | Afterwards, by the sceptic |

## The split that makes it work

**The slide shows. The speaker notes say. The record proves.**

A slide is not a summary of the notes, and the notes are not a reading of the slide. If
the slide already says the sentence, the presenter has nothing to add and the audience
reads instead of listening.

**Generate the spoken script from the built deck**, never maintain it by hand. Two files
that must agree will not, and the drift is invisible until someone presents from the
wrong one.

## The record's architecture

This took the reference project longest to arrive at, and it was arrived at by getting
it wrong first. The first attempt organised the record in deck order; the same finding
ended up in four sections, each with a caveat the others lacked, and **a reader of any
single telling was misinformed.**

Two layers:

**Layer 1 — the Record.** Subject chapters. Every fact stated **once**, in full, with
its caveats in the same sentence as the number. Each chapter opens with a one-sentence
thesis and closes with what would change it.

**Layer 2 — the Slide Map.** One row per slide, in deck order, pointing into the Record.
**No evidence at all.** If a number appears in the Slide Map, it belongs in a chapter.

> **A fact belongs to exactly one chapter. Everything else points at it.**

Before adding a paragraph, check whether the fact already has a home. If linking to it
feels awkward, the chapters are wrong — that is not a reason to duplicate.

## Verify the map mechanically

The reference project once shipped a record claiming to map all 41 slides. It mapped 34.

```bash
python3 - <<'PY'
import re
deck = open('deck/<vendor>-deck.html').read()
rec  = open('deck/evidence-record.html').read()
slides = re.findall(r'data-t="([^"]*)"', deck)
missing = [t for t in slides if t not in rec]
print(f"{len(slides)} slides, {len(missing)} unreferenced"); print(*missing, sep='\n')
PY
```

Also check `<div>` balance. A duplicated block is invisible until the layout breaks, and
by then you are debugging CSS instead of the copy.

## Before you write a single slide

Four things, each corresponding to a mistake that cost a full rework cycle on the
project this reference came from. **The presentation there took nine rework rounds while
the research took two, and all four omissions below were fixable on day one.**

**1 · Name the audience in one sentence, in writing.** Their role, and the decision they
are trying to make. Skip it and you will write for an analyst who cares about
provenance, because that is the only reader the project has described. This is
measurable afterwards: count words pointing at the vendor's business (*means, risk,
depends, advantage, exposed, negotiate*) against words pointing at your own analysis
(*disclosure, documented, corpus, graded, traceable*). A good deck runs near 1:1. The
failure case ran 0.33.

**2 · Open the reference deck and read its headlines as a list.** Not a document *about*
it — the artefact. A deck's rhythm is only audible when the headlines sit in a column,
and ten minutes there beats any amount of prose description.

**3 · Decide the headline mix before writing headlines.** See below.

**4 · Check the design system's visual slots are filled.** A ported stylesheet carries
image containers a ported deck does not automatically use. Grep the CSS for them — on
the reference project four styled, empty containers survived two critique rounds because
nobody knew they were there.

## Headlines: two kinds, and the ratio matters more than either

Every headline is one of exactly two things. **Decide which before writing it.**

**LABEL** — for a slide whose job is orientation: a stage in a sequence, an inventory, a
mechanism. 2–5 words, a noun phrase, no verb. Plain to the point of boring, because the
content carries the interest.

> *Getting the data in* · *Identity resolution* · *Geography* · *Three ways to see what
> worked*

**CLAIM** — for a slide that carries a finding. It states **the finding**, not the topic
of the finding. 5–9 words; over ten, cut it. Two short beats beat one long clause — the
turn between them is the whole effect.

| Shape | Example |
|---|---|
| Contrast | *One person can run it. It takes weeks to learn.* |
| Reversal | *The barrier is not code. It is a line of credit.* |
| Symmetry | *Nine channels they name. Nine more they don't.* |
| Verdict | *Old machine learning, real. New agents, thin.* |
| Flat statement | *They publish no prices.* |

**Target two labels for every claim, and never more than three claims in a row.** This is
the rule most easily got wrong and it is worth more than the wording of any individual
headline. Claim power is inversely proportional to frequency: the reference deck runs 70%
labels and lands twelve punches; the project that copied it ran 39% labels with an
unbroken run of eight, and none of them registered. A genuinely generous finding about a
competitor — the kind that makes your critical findings credible — arrived as more of the
same and was wasted.

**The test:** read the headline with the slide covered. A stranger should be able to say
what it is *about* (label) or what it *argues* (claim). No prior slide's knowledge
allowed.

**Never invent a finding to earn a claim headline.** A boring accurate label beats an
exciting claim the slide cannot support, and the whole method rests on never doing the
second thing.

## Every substantive slide ends on the audience

The last line of a slide is what the room carries away. Point it at what the finding
*means for them*, not at how you know it.

> **Bad** (an instruction to the analyst): *"Say what the disclosure names, not what
> exists."*
> **Good** (a conclusion the audience can use): *"Their largest channel sits on one
> supplier — and that supplier also owns a competing product."*

Same rule for the closing slide. A deck that ends on how honest the vendor's
documentation was has ended on method. Presentations are judged on their last line.

## Slide craft

- **One idea per slide.** If it takes two sentences to say what the slide is for, it is
  two slides.
- **Cap on-slide body at ~120 words.** Anything more and the audience reads instead of
  listening; the overflow belongs in the notes, spoken.
- **Every slide carries a grade**, and it is the grade of the weakest supporting source.
  A grade bar at the foot pre-empts *"says who?"* before it is asked.
- **Emphasis by value, not hue.** Keep grade colours reserved for the evidence system,
  so a big number is never tinted amber and misread as a grade.
- **Uncomfortable findings as observation, never accusation.** The discipline is what
  makes the favourable findings believable — and there will be favourable findings, and
  they should be said plainly.
- **Look at the artefact.** Screenshot every slide. Markup that parses can still render
  a key number as a stray glyph, and it did.

## A design system, not the design system

The one in this repository — fixed 1280×720, a dark stage, a component vocabulary in
`deck/lib.py`, a grade ledger along the foot — is opinionated and it works. It is not
the only way to do this. On a project that already has a template, keep the *split*
(audience sees / presenter says / record proves) and use their template.

What is worth keeping regardless:

- **A fixed canvas.** Reflowing slides make overflow invisible until the room sees it.
- **A build step.** Slides as code means a slide can be held back rather than deleted,
  and the script can be generated rather than maintained.
- **An overflow check.** Inside a scaled stage, compare `scrollWidth` against
  `clientWidth` — `getBoundingClientRect()` returns transformed pixels and will report
  overflow that is not there.

## Releasing to PDF

Rendering these to PDF has three non-obvious requirements, and the third is the one that
silently ruins the output:

1. **Print CSS that unstacks the deck.** On screen one slide is visible at a time; for
   print each becomes its own page with the stage transform removed.
2. **`print-color-adjust: exact`.** Without it a dark deck prints white.
3. **Static fonts, not variable ones.** Chrome's `--print-to-pdf` silently drops
   variable fonts and falls back to Georgia and Menlo. Google Fonts serves static WOFF
   only to an old user agent, so fetch the CSS as Firefox 27 and inline every face as a
   data URI.

Verify by reading the font list out of the PDF bytes. Georgia or Menlo in there means
step 3 failed, and it is easy to miss by eye.
