# METHOD — how to run this analysis

Carried over from a competitor analysis that ran end to end on a private vendor, and
adapted for a listed one. This is the process; [`STRATEGY.md`](STRATEGY.md) is what
changes for Braze specifically, and [`SOURCES.md`](SOURCES.md) is where to point it.

The one-line version: **go to the records the company does not control, read their
documentation instead of their marketing, count instead of reading, and record every
disagreement instead of resolving it.**

---

## The seven phases, in the order that works

### 0 · Capture, and make it immutable

Fetch and paste everything first, into a directory that is never edited again. Keep the
byte-exact original *and* a de-chromed copy under a citable slug; the slug becomes the
citation unit for the rest of the project.

**Why it matters:** halfway through, a figure will look wrong. Being able to return to
the exact bytes you captured, with a date, is the difference between correcting it and
arguing about it.

`sources/` is immutable. `tools/fetch_docs.py` is resumable and records every failure in
`logs/fetch-failures.md`, because a gap you have written down is evidence.

### 1 · Index before you analyse

Build a machine-readable index of the corpus before reading any of it: slug, title,
description, section, dates, size, structure. One script, run once.

**Why:** it converts "where is X discussed?" from a grep over tens of megabytes into a
lookup, and it lets you find documents by what they *are* rather than by what words they
happen to contain. On the reference project this was the highest-return hour of the
whole method.

### 2 · Extract to tables, never to prose

Every number goes into a CSV produced by a script in `tools/`. Nothing is typed by hand.

**Why:** it makes numbers re-derivable, and re-derivation is what catches errors. The
single biggest correction on the reference project came from re-parsing a source
programmatically instead of trusting an earlier reading of it — and it found **four**
wrong figures in one pass.

This is why `data/` holds only CSVs, and only things a script can regenerate.

### 3 · Read the documentation, not the marketing

Marketing tells you what a company wants to be true. Technical documentation tells you
what it has to support. **Documentation is consistently more honest**, because it is
written for people who will hit the limits.

Two of the strongest findings on the reference project came straight out of the docs: a
data-freshness table admitting only one of four ingestion paths was event-driven, and an
identity page admitting only one active identifier value per type was segmentable. Both
were later confirmed independently by paying customers who had hit them from outside.

**Documentation and lived customer experience corroborating each other, from unrelated
sources, is as strong as competitive evidence gets.**

### 4 · Go to the records the company does not control

Where the non-obvious findings live, and the phase most analyses skip.

| Record | What it gives up |
|---|---|
| **Audited filings** (listed companies) | The real cost structure, quarterly, signed by an auditor. Risk factors are legally compelled candour |
| Certificate transparency | Hosts provisioned but never announced — unreleased products, internal tools, named customers |
| Legally-required sub-processor disclosure | The database engine, the iPaaS, every delivery supplier — **and which channel has no middleman** |
| Public version control | Release cadence per platform; which SDKs quietly stopped moving |
| Public status page | A decade of incidents, with durations, and a component list that discloses architecture |
| Company registries | The operating entity is often not called what the company is called |
| Careers board | Where headcount is going. The strategy, stated in hiring |

**The test to apply:** would this document be embarrassing to keep inaccurate? A
sub-processor list must be right by law. A 10-K must be right on penalty. A marketing
page need not be right at all.

### 5 · Count before you read

When a search returns more than a handful of files, get the distribution first.

```bash
rg -c -i 'agentic' sources/docs/ | sort -t: -k2 -rn | head
```

Two files with forty hits is a different finding from forty files with two hits. In the
capability measurement that difference *is* the finding: counting pages **focused** on a
topic (≥5 mentions in the body, a deliberately strict test) separates "mentions email"
from "is about email". `tools/capability_count.py` implements exactly this.

### 6 · Triangulate, then say only what survives

A finding is worth presenting when **independent lenses agree**. The reference project's
AI-maturity finding held because four did: documentation volume, published API surface,
the words customers used, and an analyst panel's coverage counts. None was derived from
the others.

Then bound the claim to what survives challenge. *"Their AI is thin"* is wrong and
easily rebutted. *"A decade of shipped ML, and an agentic layer with 15 focused pages
and zero dedicated endpoints that they renamed the company around"* is unfalsifiable
from their own documentation — and it lands harder because it is precise and credits
what deserves credit.

### 7 · Build two documents, not one

- a **deck**, where each slide carries one idea the audience must *see*, and the speaker
  notes carry what the presenter *says*
- a **record**, organised by subject, where every fact is stated **once**, in full, with
  its caveats — plus a slide-order index that points into it and holds no evidence

Keeping them separate is what stops the deck becoming a document and the document
becoming a transcript. Generating the spoken script *from the built deck* means the two
cannot drift.

---

## The disciplines that make it trustworthy

**Never merge company-declared and independent figures.** Record both, say which is
which, explain the gap rather than weaponising it.

**Record conflicts unresolved — with a ruling on what to say.** Each entry says what the
sources are, why they differ, and the sentence to use out loud. *"Quote the ordering,
never the decimal"* is more useful than picking a number.

**Grade every claim, and keep more resolution in the record than on the slide.** A claim
takes the grade of its weakest supporting source, never its best.

**Absence is a finding** — when the check was exhaustive, and stated as such. "No price
appears across 6,366 indexed URLs" is checkable. "I could not find pricing" is not.

**Keep corrections visible.** A file that shows its own errors is the reason to trust the
rest of it. `FACTS.md` carries a *numbers that were wrong and are now right* table so a
stale copy can be recognised on sight.

**Be fair on purpose.** Every uncomfortable finding should come from the company's own
documentation, a filing, or a paying customer. Delivered as observation rather than
accusation it lands harder — and it is what makes the favourable findings believable.

---

## What went wrong last time, and what it taught

Every row is a mistake the reference project actually made. Each cost real time.

| What happened | The lesson |
|---|---|
| An earlier pass's figures were carried forward and four were wrong | **Re-derive from source; never trust your own earlier reading** |
| The same 102 review answers were coded three times with three different results | **Lock the pattern set in a script** and cite the script, not the number |
| The same finding was written into four sections, each with a caveat the others lacked | **One fact, one home.** A reader of any single telling was misinformed |
| A "maps to all 41 slides" claim that mapped 34 | **Verify indexes mechanically**, or do not claim coverage |
| The deck build wrote to a session temp directory | **Deliverables must be reproducible from the repository**, or they are not deliverables |
| A slide's most important fact rendered as a stray glyph | **Look at the artefact.** Screenshot it; do not trust the markup |
| A press release contradicted the product documentation six days later | **Test claims against the docs, with a date** — and set a re-check, do not call it a lie |

Two more, learned while building this repository:

| What happened | The lesson |
|---|---|
| XBRL labels two different fiscal years `fy2026`, because the field describes the filing | **Read the schema, not the field name.** `sec_facts.py` now derives the period from dates |
| A width check compared a transform-scaled rect against a layout width and reported a false overflow | **Compare like with like.** Use `scrollWidth` vs `clientWidth` inside a scaled stage |

---

## Cost, roughly

The expensive parts are capture (once) and the two documents (many passes). The analysis
between them is comparatively cheap **because phases 0–2 made everything countable**.

If you are budgeting: front-load the indexing, and expect the presentation to take as
long as the research. The single highest-return *habit* is counting instead of reading.
