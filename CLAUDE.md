# Working in this repository

A **research environment** for a sourced competitive analysis of **Braze**
(NASDAQ: BRZE, CIK 0001676238). The method, tooling and specifications are here; the
findings are not, until the research runs.

## The rule that matters most right now

**This repository contains no findings about Braze, and you must not add any that are
not sourced.** Do not write what you remember about Braze into `docs/`. Every number
that enters this repo carries a path to the source it came from, an evidence grade, and
a capture date — or it does not enter.

If you know something about Braze and cannot source it, it is a **hypothesis**. There is
a place for those: `docs/STRATEGY.md` §"Ten hypotheses", where each one must end the
project either evidenced or explicitly killed.

## Once the research has run

**When you need a number, read [`docs/FACTS.md`](docs/FACTS.md) and stop.**

It carries the canonical value for every figure, its grade, and the path to its source,
plus a *"numbers that were wrong and are now right"* table. Going hunting in `sources/`
for something already recorded wastes context and risks resurrecting a corrected figure.

## Where things are

| Looking for | Open |
|---|---|
| **How the operator starts a run** | [`START-HERE.md`](START-HERE.md) |
| What to do next | [`TODO.md`](TODO.md) |
| **How to run this unattended** | [`AGENTS.md`](AGENTS.md) — budgets, degradation rules, when to stop |
| How to write a slide | [`deck/COMPONENTS.md`](deck/COMPONENTS.md) |
| What makes Braze different from a private vendor | [`docs/STRATEGY.md`](docs/STRATEGY.md) |
| Where to pull a source from | [`docs/SOURCES.md`](docs/SOURCES.md) |
| A number | [`docs/FACTS.md`](docs/FACTS.md) |
| A disputed number | [`docs/CONFLICTS.md`](docs/CONFLICTS.md) — follow the ruling |
| What a slide must answer | [`docs/DECK-SPEC.md`](docs/DECK-SPEC.md) |
| How to search without drowning | [`RETRIEVAL.md`](RETRIEVAL.md) |

## How to search

The corpus will grow to tens of megabytes. **Never read a file end to end.** Count, then
read a bounded range.

```bash
rg -c -i 'identity resolution' sources/docs/ | sort -t: -k2 -rn | head   # where is it
sed -n '40,70p' sources/docs/docs__user_guide__data__identity.md          # then read just that
```

Two files with forty hits is a different finding from forty files with two hits. That
difference is often *the* finding.

## Layout, and the invariant that makes it trustworthy

```
sources/    evidence exactly as captured — IMMUTABLE, never edit
            (incl. media/ — logos and portraits, with PROVENANCE.md)
data/       derived tables. CSV only. Every file reproducible by tools/
docs/       analysis and specifications written by a person
deck/       generators + evidence-record.html
dist/       published deliverables (HTML, PDF)
tools/      the scripts that build data/ from sources/, and cut a release
logs/       provenance, fetch failures, the executed plan
```

**`data/` contains only CSV, and only things a script in `tools/` can regenerate.** A
table you produced by hand belongs in `docs/`. Anything captured from the web belongs in
`sources/` — never in `data/`. That invariant is what lets anyone trust a number in
`data/` without re-deriving it.

## Evidence discipline

Five grades, defined in [`docs/EVIDENCE-GRADES.md`](docs/EVIDENCE-GRADES.md): `audited`,
`infrastructure`, `documented`, `third-party`, `claimed` — plus `conflicted` as a state.

- **A claim takes the grade of its weakest supporting source, never its best.**
- **Never merge company-declared and independent figures.** Where two rosters exist, keep
  two rosters and explain the gap.
- **Where sources disagree, say so.** Record it in `CONFLICTS.md` with a ruling on what
  to say out loud, and follow the ruling.
- **A marketing claim contradicting an audited filing is an error, not a conflict.** Say
  so plainly, without drama. This is a distinction a private vendor rarely permits.
- **Cite `path:line-range`**, a grade, and a capture date.
- **Absence is a finding** — when the check was exhaustive and is stated as such. But
  search the filings before calling anything absent: a listed company discloses things in
  the 10-K that never reach a marketing page.

## Running things

```bash
python3 tools/run_all.py             # the whole pipeline, idempotent, ~40 min
python3 tools/verify.py              # ten rules the analysis must satisfy
```

Individually:

```bash
python3 tools/fetch_sitemap.py       # sitemaps      -> site_inventory
python3 tools/sec_facts.py           # SEC XBRL      -> financials, restatements
python3 tools/sec_filings.py         # SEC EDGAR     -> filings, insider counts
python3 tools/fetch_filings.py       # 10-K/10-Q/8-K -> sources/filings/*.txt
python3 tools/status_history.py      # status page   -> incidents, components
python3 tools/github_org.py          # braze-inc     -> repos, sdk_releases
python3 tools/fetch_issues.py        # issue tracker -> issues + a coded panel
python3 tools/ct_probe.py            # CT logs       -> subdomains
python3 tools/careers_board.py       # Greenhouse    -> careers_departments
python3 tools/fetch_docs.py          # docs site     -> sources/docs/  (resumable)
python3 tools/index_docs.py          # corpus        -> docs_index
python3 tools/extract_api.py         # API pages     -> api_endpoints
python3 tools/capability_count.py    # docs + API    -> capabilities
python3 tools/code_reviews.py        # panels        -> review coding
python3 tools/build_timeline.py      # everything    -> timeline
python3 tools/panels_status.py       # which panels are captured, and the ladder
python3 tools/handoff.py             # end collection: report + switch models

python3 tools/build_assets.py        # sources/media -> deck/assets.py (base64)
python3 deck/build_deck.py           # slides_*.py   -> deck/braze-deck.html
python3 deck/make_script.py          # the deck      -> docs/PRESENTATION-SCRIPT.md
python3 deck/build_record.py         # record/*.md   -> deck/evidence-record.html
bash   tools/make_release.sh         # both          -> dist/ HTML + PDF + zip
```

`build_deck.py` **discovers** `deck/slides_*.py` in filename order — adding a chapter is
one new file, with no edit to the assembler. `make_script.py` reads the built deck, so
the script cannot drift from the slides. `build_record.py` derives the slide map from the
built deck too, so the record cannot claim coverage it does not have — and it reports any
figure that appears in more than one chapter, which is the one-fact-one-home rule made
mechanical.

## Two things that will bite you

**XBRL's `fy` field describes the filing, not the period.** Braze's FY2026 10-K reports
FY2024 and FY2025 and labels both `fy2026`. Key on `start`/`end`. `sec_facts.py` derives
a correct `period` column; use it.

**Inside the scaled deck stage, `getBoundingClientRect()` returns transformed pixels.**
Comparing it against a layout width reports overflow that is not there. Use `scrollWidth`
vs `clientWidth`.

## Style, if you are writing for this project

Findings are stated plainly with their caveats attached, in the same sentence where
possible. No number appears without a source. Uncomfortable findings are stated fairly
and never as accusation — the discipline is what makes the favourable findings believable
too. Corrections are recorded, not quietly patched: `FACTS.md` keeps the old value
visible so a stale copy can be recognised.
