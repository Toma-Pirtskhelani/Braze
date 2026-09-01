# Braze — competitor analysis environment

A **research environment**, not yet a research result. Everything needed to run a
rigorous, fully sourced competitive analysis of **Braze** (NASDAQ: BRZE) and produce two
deliverables: a presentable deck and an evidence record where every claim is graded and
traceable.

**This repository contains no findings about Braze, deliberately.** It contains the
method, the verified source catalogue, the extraction tooling, the deck design system,
and the specifications for what gets built. The findings arrive when you run it.

That line matters. A bootstrap repository pre-loaded with half-remembered facts is worse
than an empty one, because a later run will trust them. The only Braze-specific numbers
here describe *sources* — how many filings exist, how many documentation pages, how many
incidents are logged — and each was verified on 2026-09-01 and is re-checkable in one
command.

---

## Start here

| You want to… | Open |
|---|---|
| **Run the research** | **[`TODO.md`](TODO.md)** — the whole run, phase by phase, with a *done when* for each |
| Know what makes Braze different | [`docs/STRATEGY.md`](docs/STRATEGY.md) — read this before phase 0 |
| Know where to pull from | [`docs/SOURCES.md`](docs/SOURCES.md) — every source, verified, with what it yields |
| Understand the process | [`docs/METHOD.md`](docs/METHOD.md) — seven phases, and seven mistakes not to repeat |
| Know what the deck must answer | [`docs/DECK-SPEC.md`](docs/DECK-SPEC.md) — 41 slides, question by question |
| Quote a number *(once research has run)* | [`docs/FACTS.md`](docs/FACTS.md) — canonical value, grade, source. Stop there |
| Search the corpus without loading it | [`RETRIEVAL.md`](RETRIEVAL.md) |

If you are an agent working here, read [`CLAUDE.md`](CLAUDE.md) first.

---

## Set up

Python 3.9+. **No third-party packages** — every tool runs on a bare interpreter, on
purpose, so this works on any machine without an environment to break.

```bash
git clone https://github.com/Toma-Pirtskhelani/Braze.git
cd Braze

export SEC_CONTACT="your name your@email"   # SEC asks for a real contact
export GITHUB_TOKEN=...                     # optional: 60 req/hr -> 5,000
export CERTSPOTTER_TOKEN=...                # optional: lifts CT rate limiting

python3 deck/build_deck.py                  # sanity check -> "slides: 3"
```

Then follow [`TODO.md`](TODO.md) from phase 1.

Google Chrome is needed only for the PDF release step at the very end.

---

## Run the research

```bash
python3 tools/fetch_sitemap.py     # sitemaps      -> site_inventory.csv        (~30s)
python3 tools/sec_facts.py         # SEC XBRL      -> financials*.csv           (~15s)
python3 tools/sec_filings.py       # SEC EDGAR     -> filings.csv               (~20s)
python3 tools/status_history.py    # status page   -> incidents.csv             (~60s)
python3 tools/github_org.py        # braze-inc     -> repos.csv, sdk_releases   (~90s)
python3 tools/ct_probe.py          # CT logs       -> subdomains.csv            (varies)
python3 tools/fetch_docs.py        # docs site     -> sources/docs/*.md         (~25min)
python3 tools/index_docs.py        # the corpus    -> docs_index.csv            (~10s)
python3 tools/capability_count.py  # docs + API    -> capabilities.csv          (~20s)
python3 tools/code_reviews.py      # panels        -> review_themes.csv         (~5s)
python3 tools/build_timeline.py    # everything    -> timeline.csv              (~5s)

python3 deck/build_deck.py         # slides_*.py   -> deck/braze-deck.html
python3 deck/make_script.py        # the deck      -> docs/PRESENTATION-SCRIPT.md
bash   tools/make_release.sh       # both docs     -> dist/ HTML + PDF + zip
```

`make_script.py` reads the **built deck**, so the spoken script cannot drift from the
slides. Change a slide, rebuild both.

---

## What is here already

| | |
|---|---|
| **11 extraction tools** | All dependency-free; every one tested against the live source on 2026-09-01 |
| **The deck design system** | `deck/lib.py`, `css.py`, `icons.py` — ported from a deck that shipped, with a 3-slide working scaffold |
| **The PDF release pipeline** | `tools/make_release.sh`, including the non-obvious static-font fix documented inline |
| **The method** | Seven phases, plus nine mistakes made in anger and what each taught |
| **The source catalogue** | Every public source, verified reachable, with what it yields and what it costs |
| **Two Claude skills** | `competitor-analysis` (the portable method) and `braze` (retrieval over this base) |

---

## Layout

```
CLAUDE.md        operating rules for an agent working here — read first
README.md        you are here
TODO.md          the research run, phase by phase
RETRIEVAL.md     how to search the corpus without loading it

sources/         evidence exactly as captured — IMMUTABLE, never edited
  raw/           byte-exact original captures
  clean/         de-chromed captures under citable slugs
  docs/          the fetched documentation corpus
  panels/        G2 · Gartner · TrustRadius · Glassdoor · jobs board
  external/      API spec, CT output, filings, probes
  ai-sessions/   other models' research sessions, each with a fact-check header
  media/         logos and images used in the deck

data/            derived tables. CSV only. Every file regenerable by tools/
docs/            analysis and specifications written by a person
deck/            the generators, plus evidence-record.html
dist/            published deliverables — HTML, PDF, zip
tools/           the extraction and release scripts
logs/            provenance · fetch failures · the executed plan
.claude/skills/  the two skills
```

**The invariant:** `data/` holds only CSVs, and only things a script can regenerate.
Anything captured from the web goes in `sources/`. Anything written by a person goes in
`docs/`. That is what lets you trust a number in `data/` without re-deriving it.

---

## Why Braze can be analysed more deeply than a private vendor

Braze is listed, so the financial chapter inverts from the weakest part of such an
analysis to the strongest: **audited, group-level, quarterly figures filed under legal
penalty**, machine-readable back to FY2019. Alongside that sit 137 public repositories
with a decade of release history and a status page with 451 logged incidents going back
to 2016.

[`docs/STRATEGY.md`](docs/STRATEGY.md) sets out what that unlocks — and the trap that
comes with it, which is that abundant SEC data will pull the whole analysis toward the
income statement if you let it. It should not. The audience is deciding about a product
and a competitor, not about a share price.

---

## Standing constraints

Documents are never read end to end; bounded ranges only. Every claim carries
`source:line-range`, an evidence grade and a capture date. Company-declared and
independent evidence are never merged. Where two credible sources disagree, both are
recorded and neither is chosen. `sources/` is immutable. Corrections are kept visible,
not quietly patched.
