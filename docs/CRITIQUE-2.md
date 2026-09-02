# Critique v2 — after the first round of fixes

Written 2026-09-02 against commit `870e3c0`, following [`CRITIQUE.md`](CRITIQUE.md).
Same reviewer, same method: measured, not eyeballed, and calibrated against the Insider
One project throughout.

**Most of v1 was answered, and answered properly.** The record nearly doubled without
padding, four real conflicts were found by going looking for them, and every small defect
was fixed. That is a good response to criticism.

**One thing was not answered at all, and it is the one the operator cares about most: the
deck still has no pictures in it.** Not the world map — that was added. Pictures. The Braze
logo, the acquired companies' logos, a photograph of a human being.

---

## 1 · Scorecard

| | v1 | **v2 now** | Insider One | v2 vs reference |
|---|---|---|---|---|
| Evidence record, words | 8,375 | **15,713** | 28,530 | 55% |
| Record sub-headings (h3+h4) | 43 | **53** | 114 | 46% |
| Record source citations (`<code>`) | 114 | **138** | 303 | 46% |
| Record tables / rows | 25 / 180 | **31 / 238** | 46 / 367 | 65% |
| Conflicts with rulings | 5 | **10** | 21 | 48% |
| `FACTS.md` rows | 199 | **219** | 101 | **217%** |
| Speaker notes, total | 5,681 | **9,008** | 9,770 | 92% |
| Speaker notes, mean/slide | 138 | **214** | 238 | 90% |
| Speaker notes, longest | 268 | **567** | 858 | 66% |
| Slides | 41 | **42** | 41 | — |
| Deck weight | 125 KB | **228 KB** | 335 KB | 68% |
| Slides overflowing | 5 | **0** | 0 | ✔ |
| `worldmap()` used | no | **yes** | yes | ✔ |
| **Raster images in the deck** | **0** | **0** | **5** | **0%** |
| **Named human beings** | **0** | **0** | 6 founders | **0%** |
| Slides with >120px dead space | 19/41 | **20/37** | 13/36 | worse |

Eight of thirteen closed. Two did not move at all. One is new.

---

## 2 · What genuinely closed — do not revisit these

**The record chapters were rewritten, and not by padding.** Every chapter now sits between
1,640 and 2,547 words, and the added material is the reasoning that was missing: how to
read a purchase-price allocation, why a $0.9m trademark valuation says the OfferFit name
was never expected to survive, what a zero earn-out is precise about and what it is silent
on. Two chapters deliberately stopped under 2,000 words "because the argument finished" —
that is the correct instinct, and stating it is better than padding to a number.

**The conflicts sweep found things nothing else would have.** C-06 (review panels
disagreeing with their own denominators), C-07 (10-K and proxy giving different headcounts
for the same date, on different definitions), C-08 ("customer" meaning ultimate parent
entity, which changes what the price bound measures). These are exactly the class of
finding the sweep exists to produce.

**Every small defect from v1 §7 was fixed** — the stale "Empty" line, the missing record
corrections log, the wrong cluster count in `DECK-SPEC.md`, and five previously undetected
overflowing slides now at zero.

**The notes now peak.** Longest note went 268 → 567 words. There are now slides where the
presenter has room to argue.

---

## 3 · The visual gap — the whole of it

This is the section that matters. It did not move between v1 and v2.

### 3.1 · The design system has four picture slots and all four are empty

`deck/css.py` — ported unchanged from the reference project — defines and fully styles
four image containers:

| class | line | what it is for |
|---|---|---|
| `.title-s .mark` | `css.py:45` | 50px brand mark on the title slide |
| `.plate` | `css.py:74-75` | white rounded plate holding a logo, for a dark slide |
| `.brandtag` | `css.py:71-73` | logo badge, absolutely positioned top-right of a slide |
| `.portrait` | `css.py:76` | 120px circular photograph |

**Not one of them is used.** The deck contains **0 `<img>` tags, 0 base64 payloads, and no
`deck/assets.py`.** `sources/media/` is empty.

The reference deck uses all four, on exactly five slides:

| Insider One slide | asset | class |
|---|---|---|
| 01 Title | brand mark | `.mark` |
| "Who they say they are" | company logo | `.plate` |
| "How they got this big" | CEO portrait | `.portrait` |
| "Acquisition 1 — MindBehind" | acquired-company logo | `.brandtag` |
| "Acquisition 2 — Bluecore" | acquired-company logo | `.brandtag` |

The Braze deck has the *same five slides* — 1, 6 "Who they say they are", 7 "Origins",
9 "Acquisition: OfferFit", 10 "Acquisition: North Star Y" — and no image on any of them.

### 3.2 · What this costs

A 42-slide deck of type and rules reads as **a document being narrated**. The one thing an
audience can do while a presenter talks is look, and there is nothing to look at. It also
costs recognition: an audience shown the OfferFit slide has to be *told* the logo they may
already know; shown it, they place the company instantly.

It is not a small polish item. It is the difference between a research output and a
presentation.

### 3.3 · Exactly what to do

**Create `sources/media/` with four files.** All are publicly published brand assets, used
here to identify the companies being discussed — the same nominative use the reference
project made.

| file | source | used on |
|---|---|---|
| `braze-logo.png` (or `.svg`) | `braze.com` press/brand page, or the site header | slides 1 and 6 |
| `offerfit-logo.png` | OfferFit's own site or its acquisition press release | slide 9 |
| `north-star-y-logo.png` | North Star Y's site or the AU/NZ reseller announcement | slide 10 |
| `ceo-<surname>.png` | The company leadership page, or the investor-relations site | slide 7 |

Prefer SVG or a transparent PNG at ≥2× the display size. Keep each under ~200 KB — the
reference project's whole asset file is 96 KB for five images.

**Then create `deck/assets.py`**, following the reference pattern exactly: one uppercase
constant per asset, each a `data:image/png;base64,…` string, so the deck stays a single
self-contained file. The reference file's constants are `MARK`, `LOGO`, `CEO`,
`MINDBEHIND`, `BLUECORE`; the Braze equivalents are `MARK`, `LOGO`, `CEO`, `OFFERFIT`,
`NORTHSTAR`.

**Then wire them in**, using the classes that already exist:

```python
# slide 1, title
<img class="mark" src="{MARK}" alt="Braze mark">

# slide 6, who they say they are
<div class="plate" style="width:150px"><img src="{LOGO}" alt="Braze logo"></div>

# slide 7, origins
<img class="portrait" src="{CEO}" alt="...">

# slides 9 and 10, the acquisitions
<div class="brandtag" style="width:130px"><img src="{OFFERFIT}" alt="OfferFit"></div>
```

**One check afterwards:** `bash tools/make_release.sh` must still report no fallback fonts
and 42 pages. Embedded images do not affect fonts, but the release is the artefact and it
should be re-cut.

---

## 4 · Nobody is named — and this is why there is no photograph

A finding that only became visible while looking for the missing portrait.

**Not one human being is named anywhere in this analysis.** Not the chief executive, not a
founder, not a director. `FACTS.md`, all eight record chapters, and all 42 slides contain
zero personal names.

This is not for want of sources. **All five DEF 14A proxy statements were fetched** and sit
in `sources/filings/`. The 2026 proxy is **44,293 words** — the single most people-dense
document a listed company files, carrying the executive team, the board, the compensation
tables and the governance structure. It is **cited seven times, and only for numbers**:
CEO total compensation $14,230,598, and a pay ratio of 87 to 1.

The analysis therefore says what the chief executive is *paid* without saying who they
*are*.

Compare the reference project, which named all six founders with their roles and made a
finding of it — *"six founders, all still in post after fourteen years"* — a sentence that
says something real about stability, and one that could only be written because somebody
went and looked at who the people were.

**What to do:**

- From the 2026 DEF 14A: name the CEO and the named executive officers, with tenure. Name
  the board, and note how many are independent and how many are investor-designated.
- Slide 7 is called *"Origins · and who controls it now"* and currently answers only the
  Class B conversion. **Governance is who holds the votes *and* who holds the seats.** It
  is half-answered.
- Check founder tenure against the reference project's question: are the founders still
  in post? For a company that just retired its super-voting stock, that is the natural
  follow-up and it is answerable from the proxies.
- Then the portrait on slide 7 has a subject.

---

## 5 · What is still short

**The record is at 55%, not 100% — and that is now acceptable.** The chapters stopped where
their arguments finished, which is right. But the *citation density* is the thing to watch:
138 `<code>` source references against the reference project's 303. Roughly half as many
claims are individually traceable to a path. As chapters grew, sourcing did not grow with
them.

**Conflicts at 10 against 21.** Better than 5. The sweep was real. Two candidates named in
v1 still appear unrecorded: the **customer-count definitions** (the 10-K metric vs 178
customer-story pages vs independent detection — `STRATEGY.md` itself flags three), and any
**documentation-versus-marketing drift** beyond the channel case in C-02.

**Dead space did not improve** — median 130px against 135px, and 20 of 37 measured slides
still carry more than 120px. Item 5 of the v1 list was not done. On a 632px canvas this is
a fifth of the slide, consistently. With images added to five slides, three or four of the
airiest will resolve themselves; the rest need a figure row, a caption band, or a merge.

**Four slides still carry fewer than 60 words of notes.**

---

## 6 · Insider One versus Braze, in plain terms

For the operator, without the metrics.

**Where the Braze work is better.** It knows more, and it knows it more precisely. Two
hundred and nineteen canonical facts against a hundred and one. Audited quarterly
financials going back seven years, where the Insider One analysis had one small
subsidiary's accounts and a page of caveats. And it did something the Insider One project
never did: it wrote down ten guesses *before* looking, then went back and marked each one
proved or killed — including four it got wrong, three of which turned out in Braze's
favour and were published anyway. That is the most honest thing in either repository.

**Where the Braze work is behind.** It reads like a very good research file and looks like
a text document. The Insider One deck has a logo on the cover, a face on the founder slide,
and the acquired companies' logos on their slides — small things that take a viewer about
one second each and make the difference between *reading* a deck and *watching* one. The
Braze deck has none of them, and the slots for all of them are sitting empty in the
stylesheet.

It also has a curious absence: **the Braze analysis has no people in it.** It can tell you
the chief executive was paid $14.2 million and earns 87 times the median employee, but not
their name. The Insider One analysis named all six founders and observed that every one was
still there after fourteen years. That kind of detail is what makes an audience feel they
are being told about a company rather than about a filing.

**The short version.** The research is better. The book is nearly as good. The show is not
built yet, and it is roughly a day's work away from being.

---

## 7 · The to-do list, exactly

Ranked. Items 1 and 2 are the ones that change what the audience sees.

| # | Do this | Where |
|---|---|---|
| 1 | Source four images into `sources/media/`: Braze logo, OfferFit logo, North Star Y logo, CEO portrait | new files |
| 2 | Create `deck/assets.py` with `MARK`, `LOGO`, `CEO`, `OFFERFIT`, `NORTHSTAR` as base64 data URIs | new file |
| 3 | Wire them onto slides 1, 6, 7, 9, 10 using `.mark`, `.plate`, `.portrait`, `.brandtag` — all four already styled in `css.py` | `deck/slides_*.py` |
| 4 | Name the CEO, the named executive officers and the board from the 2026 DEF 14A; add tenure and independence | `FACTS.md` §1, `record/01-company.md` |
| 5 | Finish slide 7: governance is who holds the votes **and** who holds the seats | `deck/slides_*.py` |
| 6 | Two more conflicts: customer-count definitions, and any docs-vs-marketing drift beyond C-02 | `CONFLICTS.md` |
| 7 | Raise citation density — every substantive claim in the record gets a `path:line-range` | `deck/record/*.md` |
| 8 | Fix the airiest slides not resolved by images; bring the four thin-note slides up | `deck/slides_*.py` |
| 9 | Re-cut the release; confirm 42 pages, no fallback fonts | `tools/make_release.sh` |
| 10 | Add a closing section to this file recording what was done, what was rejected and why | `CRITIQUE-2.md` |

---

## 8 · One line

**The research is finished and the presentation is not.** Everything above is a day's work,
and none of it requires going back to the sources — except the one thing that does: find
out who runs this company.
