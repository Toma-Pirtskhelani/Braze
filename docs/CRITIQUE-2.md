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

---

## 9 · What was done — closing record, 2026-09-02

Written after the work, against §7 in the order given. Re-checkable with
`python3 tools/verify.py` and `bash tools/make_release.sh`.

### The scorecard, after

| | v2 | **v3 now** | Insider One | v3 vs reference |
|---|---|---|---|---|
| **Raster images in the deck** | **0** | **5** | 5 | **100%** |
| **Named human beings** | **0** | **14** | 6 founders | — |
| Record source citations (`<code>`) | 138 | **200** | 303 | 66% |
| Conflicts with rulings | 10 | **12** | 21 | 57% |
| `FACTS.md` rows | 219 | **244** | 101 | 242% |
| Record, words | 15,713 | **18,035** | 28,530 | 63% |
| Record tables / rows | 31 / 238 | **34 / 256** | 46 / 367 | 70% |
| Speaker notes, total | 9,008 | **9,665** | 9,770 | 99% |
| Speaker notes, mean/slide | 214 | **230** | 238 | 97% |
| Slides with notes under 60 words | 4 | **0** | — | ✔ |
| Slides overflowing | 0 | **0** (one at 3px) | 0 | ✔ |
| Slides with >120px dead space | 20/37 | **19/37** | 13/36 | still behind |
| PDF | 42pp, no fallback fonts | **42pp, no fallback fonts** | — | ✔ |
| `tools/verify.py` | 9 pass · 0 fail | **9 pass · 0 fail** | — | ✔ |

### Items 1–3 · The images

`sources/media/` now holds four files with a `PROVENANCE.md` naming the exact URL,
grade and slide for each. `tools/build_assets.py` trims, resizes and base64-encodes them
into `deck/assets.py` — **59 KB of image data**, against the reference project's 96 KB —
and the deck stays a single self-contained file. It is a script rather than a hand-edited
constant because `deck/assets.py` is derived, and the repository rule is that derived
things are reproducible.

Wired as: **slide 1** the Braze wordmark on a `.plate`; **slide 6** the wordmark as a
`.brandtag`; **slide 7** a named `.portrait` of the CEO plus the 2011 founders photograph;
**slide 9** the OfferFit logo as a `.brandtag`. Photographs are JPEG and logos PNG, which
is what took the payload from 468 KB to 59 KB.

**Three deviations, each deliberate.**

**The `.mark` class is still unused, and slide 1 uses `.plate` instead.** `.mark` is 50px
wide and was built for a square glyph; Braze's wordmark is 2.1:1 and would render 23px
tall. It is also black-on-transparent and invisible on this deck's ground, so it needs a
light plate regardless. The plate has a second virtue on a competitive teardown: a logo on
a white card reads as a *quoted object*, not as the deck's own brand.

**No North Star Y logo exists and none was invented.** `northstary.com`,
`northstary.com.au` and `north-star-y.com` do not resolve and have no Internet Archive
captures; a web search returns only Braze's own 2023 press releases. Several unrelated
companies trade as "North Star". Attaching one of their marks would be a fabricated
identification, which is the exact error this project exists to prevent. Slide 10 states
the absence instead — and the absence turned out to be a finding: **both acquired brands
were retired completely.** `offerfit.ai` still resolves and now serves a Braze page titled
"BrazeAI Decisioning Studio" carrying Braze's own wordmark. That is independent
corroboration of §3.1's reading of the $0.9m trademark allocation, and it is filed as
**C-11**.

**The founders photograph is captioned as a pair, never left-to-right.** Braze's alt text
says "CEO and CTO" and the page does not say which figure is which. The deck says so.

### Items 4–5 · The people

The 2026 DEF 14A was mined properly and it was the richest document in the corpus.
`FACTS.md` gains two new sections — §1.1b *Who runs it* and §1.1c *Who holds the seats,
and who holds the votes* — and `record/01-company.md` gains §1.2b, which is the longest
new section in this pass.

What came out of it:

- **Two of the three cofounders still run the company.** Bill Magnuson and Jon Hyman have
  both held executive office continuously since July 2011. The cofounder *identities* come
  from Braze's own pages and are graded `claimed`, because no SEC filing in this corpus
  uses the word "cofounder" or names the third, Mark Ghermezian, at all. The *tenure* is
  audited. The record says it that way.
- **One person holds four titles** — Chairman, CEO, President and director — the President
  role having been absorbed rather than refilled when Myles Kleeger resigned in June 2025.
- **Three of six executive officers departed or announced departure inside about a year.**
  Kleeger, then the CFO, then the General Counsel. The proxy gives no reason for any of
  them and **this record asserts none** — including, explicitly, no link to the material
  weakness in §2.1b, which a reader will otherwise assemble unaided.
- **Seven directors, six independent, chaired by the CEO with a Lead Independent Director**
  — and **the board is classified into three staggered classes.** That is the finding that
  pairs with the Class B retirement: one takeover defence was given up in January 2026 and
  the more durable one was kept. Slide 7 now says both.
- **After the conversion, nobody holds a blocking position.** MCG7 Capital 6.0%, the
  Battery Ventures partner 5.1%, the CEO 4.9%.
- A related-party line worth holding: Braze bought **~$3.8m of Datadog services in FY2026**
  and director David Obstler is Datadog's CFO — while chapter 5 records, from the
  sub-processor disclosure, that Datadog receives end-user identifiers. Two proper
  disclosures in two documents that do not reference each other. **Nothing improper is
  alleged**; it is recorded because a buyer's security review and a buyer's procurement
  review will each hit one half of it.

Slide 7 was rebuilt around this. It was a timeline of five dates, four of which have their
own slide later; it is now the governance slide its title promised.

### Item 6 · Two more conflicts

**C-10 · Who are the executive officers?** — the proxy's six against the live IR page's
ten, which is mostly a difference of scope and partly of date, with a ruling that dates
every roster and never merges them. It is also the only source for the two successors'
names.

**C-12 · Is "Creative Studio" a Braze product or a partner shelf?** — a `/product/` page in
two languages with top-level navigation, against **zero focused documentation pages**,
where the phrase in the docs labels a partner category holding Canva and Figma. The
docs-vs-marketing drift the review asked for, beyond the channel case in C-02.

I also checked and **rejected** a candidate that looked like a third: *Braze Bonfire* has
71 rows in the site inventory and zero documentation pages, but the 10-K calls it "our
virtual, global customer community". A community is not expected in a developer guide.
That non-finding is written into `FACTS.md` §5.1 so the next reader does not re-open it.

### Item 7 · Citation density

138 → **200** `<code>` references, 46% → 66% of the reference. Chapters 2, 5, 6, 7 and 8
were the thin ones (2.9–4.4 refs per thousand words against chapter 4's 12.0) and every
addition attaches a path to a claim that was already made — no new claims, no new words to
speak of. Chapter 1 now runs at 12.8.

While doing it I found and fixed a real defect in the checker itself: `build_record.py`'s
one-fact-one-home scan was reporting five false positives every run, all bare years, and
my new citations added a sixth class — line numbers inside backticked paths. It now strips
backticked spans and bare years before matching. **The check went from five permanent
false alarms to zero**, and on its first clean run it immediately caught a genuine
collision (1.8% meaning two different things in two chapters), which is the entire point.
A check that cries wolf gets ignored, and this one was being ignored by me.

### Item 8 · Thin notes, and the dead space

**Thin notes: fixed.** All four were part dividers, and a divider earning 400 words would
be padding. They now run 130–190 words each — a real handover between parts rather than a
caption. **Zero slides under 60 words**; mean 230 against the reference's 238.

**Dead space: 20/37 → 19/37, median 140px → 132px. I am not going to chase this further,
and this is the one place I disagree with the review.** See below.

### Item 9 · The release

42 pages, 42 slides, five fonts, **no fallback fonts**. Images verified present in the PDF
as six embedded XObjects.

---

## 10 · Where I disagree with this review

Three places, and the first is the substantive one.

**1 · The dead-space metric is measuring the wrong thing, and the prediction attached to
it was mechanically impossible.** §5 predicted that adding images would resolve "three or
four of the airiest" slides. It could not: `.brandtag` is `position:absolute` in
`css.py:71`, so a logo placed in one contributes exactly zero to body height by design —
which is correct, because a corner badge should not push content around. The one image
that *does* sit in the flow, on slide 7, took that slide from 193px of slack to 3px of
overflow, which is the whole effect available.

I did work the underlying problem twice. In the last pass, sparse slides got a CSS
quantity query that scales the hero element to its frame. In this pass, every card, tile,
flow step and logo outside a split column grew, and slide 26 — the worst offender at 247px
— gained a genuine three-tile band about Webhooks being the fifth-deepest and least-sold
channel in the platform. Net movement across both passes: **21 slides over the threshold
to 19, median 140px to 132px.** The metric barely moves because it is dominated by slides
carrying two or three content blocks in a 490px frame, and the only remaining levers are
inflating type past the point where it reads well, or adding content for the sake of area.
The brief's own rule forbids the second and taste forbids the first.

**A fifth of a slide in white space is not a defect in a presentation deck**; it is the
difference between a slide and a page. The reference project's 13/36 is a fact about its
content mix, not a target this deck should hit by dilution. I have made the deck denser
where density was earned and I have stopped. If the operator disagrees, the fix is to
merge slides — which is a content decision, not a CSS one, and I would want to be told
which pairs.

**2 · One of §5's two "unrecorded" conflicts was already recorded.** The customer-count
definitions are **C-08**, added in the previous pass and quoted approvingly in §2 of this
same review. The three rosters are also set out in `record/07-market.md` §7.1. I recorded
C-12 instead, which is a genuine gap the review correctly identified in the abstract.

**3 · "Nobody is named" was right, and the diagnosis of why was half right.** §4 says the
proxy was cited "seven times, and only for numbers", implying it went unread. What
actually happened is narrower and worth recording because it is a repeatable failure: the
proxy was read *for the questions already being asked* — compensation design, pay ratio,
headcount definition — and every one of those was answered well. Nobody asked "who are
these people", so the section that answers it was never opened. That is the same failure
mode as missing the material weakness in the first pass, logged as correction 4, and it
has now happened twice. The lesson is not "read the proxy"; it is **read the document for
what it volunteers, not only for what you came to ask.**

---

## 11 · What is still weak

- **Dead space, on the review's terms.** 19 of 37 measured slides carry more than 120px.
  Argued above; recorded as a disagreement rather than a fix.
- **Slide 7 overflows by 3px.** Below the threshold of visibility and clear of the footer,
  but it is not zero and I would rather say so than round it away.
- **Citation density is 66% of the reference, not 100%.** The remaining gap is in prose
  that reasons *about* facts cited in the table directly above it. Attaching a path to
  every such sentence would repeat the same path three times a paragraph, which is noise
  of the kind item 7's own checker just had to be fixed for.
- **The third cofounder is a dead end.** Mark Ghermezian appears in no filing. MCG7
  Capital is the largest disclosed holder, holds partly through an entity named "Appboy BH
  LLC", and is connected by the proxy to no named person. Everything beyond that would be
  inference about a private individual and is not in this repository.
- **`.mark` and `.stat` remain unused in the design system**, and `data/careers_departments.csv`
  is the only CSV with a single capture date rather than a series.
- **Two record chapters are still under 2,000 words** — acquisitions at 1,640 and AI at
  1,731 — for the reason given last time: the argument finished.
