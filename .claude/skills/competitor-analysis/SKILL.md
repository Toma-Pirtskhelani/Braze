---
name: competitor-analysis
description: Run a rigorous, fully sourced competitive analysis of a software vendor and produce a graded evidence base, a deck and an evidence record. Use this when someone asks for a competitor teardown, a deep dive on a vendor, a battle card, "research this company properly", "what are X's real weaknesses", "we keep losing deals to X — find out why", or when they want to know what a vendor actually ships versus what it markets. Also use it when an existing analysis needs its claims graded, its conflicts recorded, or its numbers made re-derivable. Not for summarising what a vendor says about itself, and not for pricing-page comparisons.
---

# Competitive analysis, done so the numbers survive challenge

The premise, and everything else follows from it:

> **Go to the records the company does not control. Read their documentation instead of
> their marketing. Count instead of reading. Record every disagreement instead of
> resolving it.**

An analysis that summarises a vendor's own positioning is worth nothing — the audience
can read the website. The value is entirely in what a vendor cannot retouch and in
measurements anyone can re-run.

**Preconditions.** This needs a vendor with public technical documentation and at least
one filed or logged record. On a private company with a brochure site it degrades to
ordinary desk research. Say so rather than pretending; a method honest about where it
applies gets trusted where it does.

---

## The seven phases

### 0 · Capture, and make it immutable
Fetch and paste everything first, into a directory never edited again. Keep the
byte-exact original *and* a de-chromed copy under a citable slug. **Why:** a figure will
look wrong halfway through, and returning to the exact bytes with a date is the
difference between correcting it and arguing about it.

### 1 · Index before you analyse
Build a machine-readable index of the corpus before reading any of it — slug, title,
description, section, dates, size. **Why:** it turns "where is X discussed?" from a grep
over tens of megabytes into a lookup, and lets you find documents by what they *are*.
This is reliably the highest-return hour of the whole method.

### 2 · Extract to tables, never to prose
Every number goes into a CSV produced by a script. Nothing typed by hand. **Why:**
re-derivation is what catches errors. On the reference project, re-parsing one source
programmatically instead of trusting an earlier reading found **four** wrong figures in
a single pass.

### 3 · Read the documentation, not the marketing
Marketing says what a company wants to be true; documentation says what it has to
support. **Documentation is consistently more honest**, because it is written for people
who will hit the limits. Look specifically for *tables* — freshness tables, limit
tables, identifier tables. That is where constraints get admitted.

### 4 · Go to the records the company does not control
The phase most analyses skip, and where the non-obvious findings live. See
`references/records-to-pull.md`. **The test to apply: would this document be
embarrassing to keep inaccurate?** A sub-processor list must be right by law. A 10-K
must be right on penalty. A marketing page need not be right at all.

### 5 · Count before you read
```bash
rg -c -i 'agentic' sources/docs/ | sort -t: -k2 -rn | head
```
Two files with forty hits is a different finding from forty files with two hits. In the
capability measurement that difference *is* the finding — see
`references/measuring-capability.md` for the focused-page test.

### 6 · Triangulate, then say only what survives
A finding is presentable when **independent lenses agree** and none is derived from the
others. Then bound the claim to what survives challenge. *"Their AI is thin"* is wrong
and easily rebutted. *"A decade of shipped ML, and an agentic layer with 15 focused
pages and zero dedicated endpoints that they renamed the company around"* is
unfalsifiable from their own documentation — and lands harder because it is precise and
credits what deserves credit.

### 7 · Build two documents, not one
A **deck** where each slide carries one idea the audience must *see*, and a **record**
organised by subject where every fact is stated **once**, with its caveats. Generate the
spoken script *from the built deck* so the two cannot drift.
See `references/building-the-deck.md`.

---

## The four disciplines

**Never merge company-declared and independent figures.** Two customer counts from two
methods are two facts. Record both, say which is which, explain the gap rather than
weaponising it.

**Record conflicts unresolved — with a ruling on what to say.** *"Quote the ordering,
never the decimal"* and *"quote the range, never a precise figure"* are more useful to a
presenter than a number picked by coin toss. See `references/evidence-grading.md`.

**Absence is a finding** — when the check was exhaustive and is stated as such. "No
price appears across 6,366 indexed URLs" is checkable and quotable. "I could not find
pricing" is neither. This is the least intuitive discipline and it produces some of the
strongest lines: no adoption figure for an acquired product, no status page, no
`security.txt`, no page in the vendor's home language.

**Keep corrections visible.** A file that shows its own errors is the reason to trust
the rest of it. Keep a *numbers that were wrong and are now right* table with old values
still readable, so a stale copy can be recognised on sight.

---

## Grade everything

Five grades, ordered by how hard it would be for the vendor to have made the statement
untrue. Full definitions in `references/evidence-grading.md`.

| grade | source |
|---|---|
| `audited` | Filed accounts, SEC filings — signed off, filed under penalty |
| `infrastructure` | Certificate transparency — append-only, third-party logged |
| `documented` | Technical docs, API spec, public VCS, status page, compelled disclosures |
| `third-party` | Review panels, analyst notes — independent, not disinterested |
| `claimed` | Marketing, press releases, case studies |

**A claim takes the grade of its weakest supporting source, never its best.**

---

## Failure modes — each one cost real time

| What happens | The rule |
|---|---|
| Earlier figures carried forward, several wrong | **Re-derive from source; never trust your own earlier reading** |
| The same reviews coded three times, three answers | **Lock the pattern set in a script**, cite the script not the number |
| One finding written into four sections, each caveated differently | **One fact, one home.** A reader of any single telling was misinformed |
| "Maps to all 41 slides" that mapped 34 | **Verify indexes mechanically**, or do not claim coverage |
| The build wrote to a temp directory | **Deliverables must be reproducible from the repository** |
| A key number rendered as a stray glyph | **Look at the artefact.** Screenshot it; markup that parses can still render wrong |
| A press release contradicted the docs six days later | **Test claims against the docs, with a date** — set a re-check, do not call it a lie |
| A field named `fy` meant the filing's year, not the period's | **Read the schema, not the field name** |

---

## Getting started on a new vendor

```bash
python3 scripts/bootstrap.py <vendor-name> <domain>
```

That writes the directory scaffold, the invariants, and a `tools/config.py` to fill in.
If you are working in a repository that already has this toolkit, use its `tools/`
directly rather than re-deriving the extractors — `index_docs.py` on a thousand-page
corpus is the single highest-return script in the method and nobody should write it
twice.

## References, loaded when you reach that phase

- `references/records-to-pull.md` — the non-controlled-record checklist, by type and
  jurisdiction, with what each one gives up
- `references/evidence-grading.md` — the five grades, the conflict protocol, the
  corrections log
- `references/measuring-capability.md` — the focused-page test, and the second and third
  lenses that make it defensible
- `references/building-the-deck.md` — the deck/record split, and what belongs in each

## What this method will not do

It will not produce a market sizing, a valuation, or a recommendation about a security.
It will not tell you what a vendor's customers actually use, because no vendor publishes
adoption. And it will not be fast: capture is one long unattended run, and the
presentation takes as long as the research.

**Be fair on purpose.** Every uncomfortable finding should come from the company's own
documentation, a filing, or a paying customer. Delivered as observation rather than
accusation it lands harder — and it is what makes the favourable findings believable.
