# Deck components

The whole vocabulary, from `deck/lib.py`. It is small on purpose: a deck built from
eight components looks like one deck, and a deck built from forty looks like a
collection of slides. **Read this before inventing a layout.**

Every slide is one call to `add()`:

```python
add(html, notes, grade, label)
```

| argument | |
|---|---|
| `html` | the `<section class="s" data-g="…" data-t="…">…</section>` block |
| `notes` | what the presenter *says*. `**bold**` marks the words to land on |
| `grade` | `"s"` strong · `"m"` medium · `"w"` weak — **the weakest supporting source** |
| `label` | the short title shown in the grid and the footer |

Pass `hidden=True` to keep a slide in the source and out of the deck. Nothing is ever
deleted; restoring it is a one-word change.

---

## The frame every content slide uses

```python
add(f'''<section class="s" data-g="m" data-t="Where they operate">
  {head("Part I &middot; the company", "Where they operate",
        "Revenue by region, from the filings &mdash; not from the customer logos")}
  <div class="body">
    {bars([("United States", 61), ("EMEA", 24), ("Rest of world", 15)], unit="%")}
  </div>
</section>''',
"""What to say. **Bold the words to land on.**""",
"m", "Where they operate")
```

`data-g` and the `grade` argument must agree — the first colours the ledger tick, the
second is what the build checks.

---

## Components

| call | use it for |
|---|---|
| `head(eyebrow, headline, sub=None)` | the top of nearly every slide |
| `figs(items, size, cols, focus)` | 2–6 big numbers. `items` are `(value, label)` or `(value, label, kind)` where kind is `''`, `'neg'`, `'boxed'` |
| `stats(items, big=False)` | a plainer number row, `(number, label)` |
| `bars(items, unit="")` | comparing magnitudes. `(label, value)` or `(label, value, colour)` |
| `flow(steps, key=(), mark=None)` | a left-to-right process. `(n, title, detail)` |
| `timeline(items, total=False)` | dated events. `(date, value, caption)`; `total=True` marks the last as a sum |
| `tiles(items, cols=3, size=24)` | icon + title + description. `(icon_name, title, description)` |
| `cards(items, cols=3)` | text blocks with a colour key. `(title, body, kind)` where kind is `g`/`a`/`r` |
| `logos(names, cols=6, accent=())` | a name grid, with some emphasised |
| `big(text, sub=None)` | one sentence, full bleed. The pause slide |
| `split(left, right, ratio)` | two components side by side |
| `divider(pn, title, questions, foot, extra)` | a part divider with its questions |
| `worldmap(pins)` | geography. `(lon, lat, label, strength, placement)` |

Icons available to `tiles`: `web email search chat whatsapp bell story phone sms headset
wrench cart bag beauty plane car bank antenna tag wallet chart clock id click user key
lock handshake building robot target`.

---

## Rules the design system enforces

**Emphasis by value, not by hue.** `figs(..., focus=1)` keeps one figure bright and dims
its siblings. Grade colours — green, amber, red — are reserved for the evidence system,
so a big number is never tinted amber and misread as a grade. `'neg'` stays red because
it reads as a warning, not a grade.

**One idea per slide.** If it takes two sentences to say what the slide is for, it is
two slides.

**Content stays inside the safe area.** The stage is 1280×720 with 56px top and 74px
side padding; the usable body height is about 632px. Overflow is silent until the room
sees it.

**Test overflow correctly.** Inside the scaled stage, `getBoundingClientRect()` returns
*transformed* pixels. Comparing it against a layout width reports overflow that is not
there — that mistake was made while building this scaffold. Use:

```js
[...document.querySelectorAll('section.s')]
  .filter(s => s.scrollWidth > s.clientWidth + 1 || s.scrollHeight > s.clientHeight + 1)
  .map(s => s.dataset.t)
```

or paste `tools/typography_audit.js` into the deck's console, which does the whole sweep.

---

## Adding a chapter

One new file. `deck/build_deck.py` discovers `deck/slides_*.py` in filename order, so
there is nothing to register.

```
deck/slides_a.py    Part 0 — the frame (ships with the scaffold)
deck/slides_b.py    Part I — the company
deck/slides_c.py    Part II — the product
…
```

Then rebuild both artefacts, always together:

```bash
python3 deck/build_deck.py && python3 deck/make_script.py
```

`make_script.py` reads the built deck, so the spoken script cannot drift from the
slides. Its `PARTS` dict maps a slide number to the part heading printed above it —
update it when the structure changes.

---

## Before calling a slide done

- [ ] It carries one idea
- [ ] Its grade is the grade of its **weakest** source
- [ ] Every figure on it has a row in `docs/FACTS.md` (`tools/verify.py` checks this)
- [ ] Notes are written, and say something the slide does not
- [ ] No overflow
- [ ] **You have looked at it.** Screenshot it. On the reference project a slide's most
      important number once rendered as a stray glyph and the markup looked perfect.
