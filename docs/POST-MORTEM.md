# Post-mortem — what the scaffold got wrong

Written 2026-09-08, after the Braze analysis completed. About the **setup**, not the
research: what I built into this repository before any evidence was captured, and how
those decisions determined what came out the other end.

The research succeeded. The presentation took nine rework cycles and still lost a
head-to-head against the deck it was modelled on. That gap is a design fault in the
scaffold, and every one of its causes was fixable on day one.

---

## 1 · The number that frames everything

```
2   commits produced the research
9   commits were critique-and-rework on the presentation
```

Four full critique rounds (`CRITIQUE.md` → `CRITIQUE-4.md`), a head-to-head comparison
and a slide-by-slide editing guide. After all of it,
[`COMPARISON.md`](COMPARISON.md) still concluded the reference deck was the better
presentation.

**The scaffold made the research work first time and the presentation take nine
attempts.** That is not the agent underperforming. That is the environment specifying
one half of the job precisely and the other half barely at all.

---

## 2 · The nine mistakes

### 2.1 · I specified research rigour and left presentation craft to chance

What shipped on day one, all of it about evidence:

`METHOD.md` (seven phases) · `SOURCES.md` (four tiers, verified) ·
`EVIDENCE-GRADES.md` (five grades) · `CONFLICTS.md` (protocol) ·
`STRATEGY.md` (what is different here) · `RECORD-SPEC.md` (two-layer architecture) ·
`DECK-SPEC.md` (41 slides mapped by question)

For how the deck should **look and sound**, the entire guidance was four lines: one idea
per slide, the slide shows and the notes say, carry a grade, stay inside the safe line.

**I got exactly what I specified.** Excellent research, a mediocre deck. In hindsight the
four critique rounds were not discoveries — they were the scaffold's missing chapters
being written after the fact, at the worst possible time.

### 2.2 · I ported the design system without porting the design rules

`css.py` came across from the reference project unchanged. It defines and fully styles
four image containers — `.mark`, `.plate`, `.brandtag`, `.portrait`. I never wrote down
that they existed.

Worse, the port was **half a mechanism**: I copied the receiving end (CSS) and not the
supplying end (`assets.py`, the base64 constants) and not the instruction to use either.
The agent had four styled, empty sockets and no way to know they were sockets.

Result: **zero images survived two full critique rounds.** `CRITIQUE-2.md` had to spend a
section explaining that the CSS the repo already shipped had slots in it.

### 2.3 · My quality gate measured only what was easy to measure

`tools/verify.py`, ten checks, every one about evidence discipline:

```
data/ is CSV only · FACTS rows graded and sourced · conflicts carry rulings
deck builds with notes · record covers every slide · record div balance
slide figures exist in FACTS · fetch failures resolved · hypotheses resolved
```

**Not one check on whether the deck was watchable.** No headline check, no density check,
no image check, no jargon check.

So `verify.py` reported **9 passed / 0 failed** on a deck that then needed four rounds of
human review. A gate with a 100% pass rate on a deliverable that needs that much rework
is not a gate — it is a comfort blanket. It measured the half of the job I had already
specified well, and was silent on the half I had not.

### 2.4 · I never said who the deck was for

Across `STRATEGY.md`, `DECK-SPEC.md`, `AGENTS.md`, `TODO.md` and `CLAUDE.md`, the word
*audience* appears sixty times and **not once is the audience identified.** No role, no
seniority, no decision they are trying to make.

The consequence is measurable. `COMPARISON.md` found the deck used methodological
language at 7.3 per thousand words against business language at 2.4 — it talks about its
own evidence three times as often as about what the evidence means.

**The deck was written for an analyst who cares about provenance, because that is the
only reader the scaffold ever described.** Everything downstream — the closing lines
about disclosure hygiene, the final slide about how honest the documentation was —
follows from that omission.

### 2.5 · I never told it to open the reference deck

`/Users/toma/Insider-One/deck/insider-one-deck.html` sat on the same machine throughout.
My scaffold invokes "the reference project" constantly in prose. It **never once says
open it and read the slides.**

Zero mentions of the deck's path in `METHOD.md`, `DECK-SPEC.md` or `STRATEGY.md`. I
described a standard in words and left the working example of it unreferenced. Every
finding in `COMPARISON.md` — the headline ratio, the so-what balance, the note lengths —
was available on day one by opening a file.

### 2.6 · I wrote the slide plan before the evidence existed

`DECK-SPEC.md` mapped 41 slides on day one, before a single source was read. Two costs:

**It was factually wrong and stayed wrong.** It asserted "12 named regional clusters".
The real number is 15. The corrections table caught it; the spec was not fixed until a
critique flagged it, and a specification known to be wrong that stays in place misleads
whoever reads it next.

**It hard-coded a rhythm that did not fit.** I specified the reference project's
seven-stage product walk. The agent gave all seven stages claim headlines — which is
precisely the shouting problem `COMPARISON.md` identified. The reference deck walks four
plain stages then lands three punches; my spec never mentioned that, because I had
transcribed the *structure* of the deck I admired without noticing the *pattern* that made
it work.

### 2.7 · I shipped no exemplar

I was pleased with "this repository contains no findings about Braze, deliberately." That
was right for facts. I extended it too far: no model slide, no model record chapter, no
worked so-what line.

Three frame slides carrying only method is not an example of good work — it is an example
of scaffolding. **A component vocabulary without an exemplar is a paint set with no
picture on the box.**

### 2.8 · I built the most useful analytical tool last, by hand

`COMPARISON.md` — measuring headline kinds, so-what ratios, note distributions against the
reference deck — was the single most useful artifact of the whole arc. I produced it
manually, once, **after** four critique rounds.

Every measurement in it is mechanical. Had it been a script on day one, the agent could
have run it continuously and self-corrected. Instead I hand-computed at the end what the
machine could have reported at the start.

### 2.9 · I gated collection→analysis and missed analysis→presentation

`tools/handoff.py` stops the pipeline between collection and analysis, because those want
different models. Correct, and it worked.

But **evidence work and presentation work are also different skills**, and I did not gate
between them. The moment the record was finished was exactly when the craft rules should
have arrived. Instead they arrived four critiques later.

---

## 3 · The root cause

All nine reduce to one thing:

> **I specified the deliverable I knew how to verify, and described the one I did not.**

Evidence discipline is checkable — a number either has a source path or it does not — so
it got a spec, a protocol, a grading system and ten automated checks. Presentation craft
felt like taste, so it got four lines of prose and no checks at all.

But most of it was never taste. Headline mix is countable. Body density is countable. The
ratio of business language to methodological language is countable. Whether an image
exists is countable. **I treated the measurable as unmeasurable because measuring it was
unfamiliar, and paid for that with nine rework cycles.**

---

## 4 · What changed as a result

### 4.1 · `tools/deck_audit.py` — the missing half of the gate

Nine checks on the deck as a *presentation*. Every one derives from a defect a human
found **after** `verify.py` said the deck was fine, so each has already earned its place.

Run against the deck as it stands today, it reproduces in one second what took four
manual rounds:

```
✗ headline mix        16 labels / 26 claims (38% labels)
✗ no long runs        9 consecutive claim headlines, ending at slide 28
✗ so-what vs method   28 : 60 = 0.47
! body density        mean 118 words/slide, 13 over 130
! jargon              1 term used before being defined
```

With `--reference` it does the head-to-head automatically:

```
metric                        this deck    reference
headline mix                       0.38         0.68   <- worse
no long runs of claims                9            6   <- worse
headline length                    6.21         4.88   <- worse
body density                     117.56       102.54   <- worse
so-what vs method                  0.47         0.70   <- worse
```

That table is `COMPARISON.md`, generated. It is now step 4 of `run_all.py`.

### 4.2 · One check was built and deliberately deleted

*"A headline must not use a word the slide never says"* came from a real defect — a slide
headed *"the complaints are about progression"* where the word appeared nowhere.

Implemented, it fired on 23–36 of 43 slides at every threshold, and the hits were good
writing: *"Nobody publishes a price"* is a conclusion, *"middleman"* is a plain-English
gloss of *sub-processor*. **A claim headline is supposed to synthesise; requiring its
words to appear literally would push the deck toward restating its own body.**

It is deleted, with the reasoning left in the file so nobody rebuilds it. The original
defect was about salience, and salience is not mechanically checkable — it belongs to the
covered-slide test a human runs.

**The general rule, now in `METHOD.md`: a checker that cries wolf gets ignored, and tuning
a wrong check until it goes quiet is worse than deleting it.**

---

### 4.3 · It earned its place within the hour

While this post-mortem was being written, the deck was independently rewritten against
[`EDITING-GUIDE.md`](EDITING-GUIDE.md). Running the audit before and after turns "did that
work?" from a judgement into a measurement:

| | before | after | reference |
|---|---|---|---|
| label share of headlines | 0.38 | **0.57** | 0.68 |
| longest run of claim headlines | 9 | **5** | 6 |
| mean headline words | 6.2 | **5.7** | 4.9 |
| mean body words per slide | 117.6 | **114** | 102.5 |
| so-what : method language | 0.47 | **0.60** | 0.70 |

Every axis moved the right way, and every one is still short of the reference deck. **That
is a more useful answer than four rounds of prose produced**, it took one second, and it
would have been available on day one.

---

## 5 · The lesson worth carrying

**Specify both halves of the deliverable, or you will get one.**

An evidence base with no presentation is a file nobody reads. A presentation with no
evidence is a competitor's marketing deck. This project produced the first and then spent
nine cycles retrofitting the second — while the working example of what it should look
like sat unopened on the same disk.

The mechanics are in place now. What generalises is in
[`METHOD.md`](METHOD.md) §"What went wrong" and in the `competitor-analysis` skill.
