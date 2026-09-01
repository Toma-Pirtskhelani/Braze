# Record specification — the two-layer architecture

`deck/evidence-record.html` is the backbone of the presentation: the document that
proves everything the deck asserts, and the thing you hand to whoever asks "says who?"

**This architecture took the reference project longest to arrive at, and it was arrived
at by getting it wrong first.** Build it this way from the start.

---

## The failure it exists to prevent

The reference project's first record was organised in deck order. The consequence was
that the same finding got written into four different sections, each with a caveat the
others lacked. **A reader of any single telling was misinformed.** Reconciling the four
was a rewrite, not an edit.

The fix is one rule:

> **A fact belongs to exactly one chapter. Everything else points at it.**

Before adding a paragraph, check whether the fact already has a home. If it does, link
to it. If the link feels awkward, that is a sign the chapters are wrong, not a reason to
duplicate.

---

## Layer 1 — the Record

Subject chapters, not deck order. Every fact stated **once**, in full, with its caveats
attached in the same sentence as the number.

Suggested chapters, mirroring `FACTS.md` so the two stay navigable together:

| # | Chapter | Holds |
|---|---|---|
| 1 | The company | Entity, listing, history, leadership, ownership, headcount |
| 2 | The money | Revenue, margin, cost structure, cash, RPO, dilution — audited only |
| 3 | What they bought | Acquisitions: price, date, what each brought |
| 4 | The platform | Architecture, data model, identity, limits, infrastructure |
| 5 | Channels and delivery | What exists, what is marketed, who delivers it |
| 6 | The AI | Shipped ML, agentic layer, the four-lens measurement |
| 7 | The market | Customers, geography, segment mix, competition, what buyers shortlist |
| 8 | What we could not answer | Open questions, and what would close each one |

Each chapter opens with a **thesis** — one sentence a reader could repeat — and closes
with what would change it.

## Layer 2 — the Slide Map

One row per slide, in **deck order**, pointing into the Record. It holds **no evidence
at all**. If you find yourself putting a number in the Slide Map, it belongs in a
chapter and the map should link to it.

| Slide | Title | Claims | Record § |
|---|---|---|---|
| 07 | Origins | 2 | §1.2, §1.4 |

The map's job is to answer "which chapter proves slide 7?" in one glance, and to make
coverage **mechanically verifiable**. Generate it from the built deck rather than typing
it: the reference project once shipped a "maps to all 41 slides" claim that mapped 34.

---

## Non-negotiables

- **Every fact once.** Duplication is the failure mode this whole design prevents.
- **Caveats travel with numbers, in the same sentence.** "Gross margin fell 68% to 52%"
  is incomplete; the clause that says which entity and why is part of the fact. Split
  across paragraphs is how a reader ends up misinformed.
- **The corrections log lives here too**, mirroring `FACTS.md`, with old values visible.
- **Grades are shown**, at the five-grade resolution, not the deck's three.
- **Uncomfortable findings are stated as observation.** The discipline is what makes the
  favourable findings believable.
- **It renders in one file**, self-contained, printable to A4 via `tools/make_release.sh`.

## Verifying it

Mechanical checks, before calling it done:

```bash
# every slide in the deck appears in the Slide Map
python3 - <<'PY'
import re
deck = open('deck/braze-deck.html').read()
rec  = open('deck/evidence-record.html').read()
slides = re.findall(r'<section class="s[^"]*"[^>]*data-t="([^"]*)"', deck)
missing = [t for t in slides if t not in rec]
print(f"{len(slides)} slides, {len(missing)} not referenced in the record")
print(*missing, sep='\n')
PY

# div balance - a duplicated block is invisible until the layout breaks
python3 -c "d=open('deck/evidence-record.html').read(); print('open',d.count('<div'),'close',d.count('</div>'))"
```

Both of those caught real defects on the reference project. Run them.
