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

## Slide craft

- **One idea per slide.** If it takes two sentences to say what the slide is for, it is
  two slides.
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
