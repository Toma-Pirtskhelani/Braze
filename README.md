# Braze — competitor analysis

A rigorous, fully sourced competitive analysis of **Braze** (NASDAQ: BRZE), plus the
environment that produced it. Two deliverables, both in [`dist/`](dist/): a 41-slide deck
and an evidence record where every claim is graded and traceable to a source path.

**The research has run.** It ran on 2026-09-01 and 2026-09-02.

```
1,352 documentation pages          737 SEC filings, 56 read in full
7 fiscal years of audited XBRL     451 incidents, 2016 → 2026
845 unsolicited public issues      833 certificate-transparency hosts (partial)
137 repositories, 494 releases     17 disclosed sub-processors
4 review panels, coded             189 canonical facts, every one sourced
```

Everything above is re-derivable. `python3 tools/run_all.py` rebuilds the whole corpus;
`python3 tools/verify.py` checks the analysis against ten rules it claims to follow.

**What the analysis found**, in one line each — with the full versions in
[`docs/FACTS.md`](docs/FACTS.md) and [`deck/evidence-record.html`](deck/evidence-record.html):

- Braze's own documentation labels **three of its four ingestion paths "not real-time"**,
  with a fifteen-minute floor on warehouse syncs. Their marketing, and the 10-K, lead
  with real-time. Both are true of different paths — see `CONFLICTS.md` C-01.
- The **AI decisioning engine was bought**: OfferFit, June 2025, $303.2m, renamed AI
  Decisioning Studio. The models come from Anthropic, OpenAI and Google, all three named
  in Braze's own compelled sub-processor disclosure.
- **One instance is not on the same cloud as the others.** The allowlist IPs Braze
  publishes for US-08 are registered to Microsoft; every other instance's are Amazon; the
  sub-processor disclosure names only Amazon and Google. Recorded as an observation and
  an open question, not as a conclusion.
- Growth has halved since FY2023 **while sales and marketing fell from 56.7% of revenue
  to 44.3%** — decelerating and getting more efficient at once. That killed the
  hypothesis it was written to test.
- Of ten hypotheses written before the corpus was read, **four were evidenced, four were
  killed, one was partly evidenced and one could not be tested at all** —
  [`docs/STRATEGY.md`](docs/STRATEGY.md) records how each one ended.

**The discipline that makes it worth trusting.** Every number carries a source path, an
evidence grade and a capture date. Where two sources disagree, both are recorded and
neither is chosen — the ruling on what to say out loud is in
[`docs/CONFLICTS.md`](docs/CONFLICTS.md). Where a number moved, the old value stays
visible in the corrections table. Where public sources ran out, that is written down with
what would close the gap.

---

## Start here

| You want to… | Open |
|---|---|
| **Start the research** | **[`START-HERE.md`](START-HERE.md)** — the four prompts to paste, in order |
| Follow the run phase by phase | [`TODO.md`](TODO.md) — every phase, with a *done when* for each |
| **Run it as an agent, alone** | **[`AGENTS.md`](AGENTS.md)** — the loop, the budgets, what to substitute when a source is blocked |
| Know what makes Braze different | [`docs/STRATEGY.md`](docs/STRATEGY.md) — read this before phase 0 |
| Know where to pull from | [`docs/SOURCES.md`](docs/SOURCES.md) — every source, verified, with what it yields |
| Understand the process | [`docs/METHOD.md`](docs/METHOD.md) — seven phases, and seven mistakes not to repeat |
| Know what the deck must answer | [`docs/DECK-SPEC.md`](docs/DECK-SPEC.md) — 41 slides, question by question |
| Quote a number *(once research has run)* | [`docs/FACTS.md`](docs/FACTS.md) — canonical value, grade, source. Stop there |
| **Edit the deck to the target standard** | [`docs/EDITING-GUIDE.md`](docs/EDITING-GUIDE.md) — the execution document |
| **Compare against the reference deck** | [`docs/COMPARISON.md`](docs/COMPARISON.md) — the two presentations, slide by slide |
| **See what is still weak** | [`docs/CRITIQUE-4.md`](docs/CRITIQUE-4.md) — current · [`-3`](docs/CRITIQUE-3.md) · [`-2`](docs/CRITIQUE-2.md) · [`-1`](docs/CRITIQUE.md) |
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

Then follow [`START-HERE.md`](START-HERE.md) — it carries the exact prompts.

Google Chrome is needed only for the PDF release step at the very end.

---

## Run the research

One command does the whole capture and extraction, unattended:

```bash
python3 tools/run_all.py           # ~40 min. Idempotent — interrupt and rerun freely
python3 tools/verify.py            # what is still wrong
cat logs/run-status.md             # what ran, what failed, what to do next
```

It skips steps already done, **continues past optional failures**, and stops only when
something required breaks. Individual tools if you prefer to drive it yourself:

```bash
python3 tools/fetch_sitemap.py     # sitemaps      -> site_inventory.csv        (~30s)
python3 tools/sec_facts.py         # SEC XBRL      -> financials*.csv           (~15s)
python3 tools/sec_filings.py       # SEC EDGAR     -> filings.csv               (~20s)
python3 tools/fetch_filings.py     # 10-K/10-Q/8-K -> sources/filings/*.txt     (~3min)
python3 tools/status_history.py    # status page   -> incidents.csv             (~60s)
python3 tools/github_org.py        # braze-inc     -> repos.csv, sdk_releases   (~90s)
python3 tools/fetch_issues.py      # issue tracker -> issues.csv + a panel      (~3min)
python3 tools/ct_probe.py          # CT logs       -> subdomains.csv            (varies)
python3 tools/fetch_docs.py        # docs site     -> sources/docs/*.md         (~25min)
python3 tools/index_docs.py        # the corpus    -> docs_index.csv            (~10s)
python3 tools/extract_api.py       # API pages     -> api_endpoints.csv         (~5s)
python3 tools/capability_count.py  # docs + API    -> capabilities.csv          (~20s)
python3 tools/code_reviews.py      # panels        -> review_themes.csv         (~5s)
python3 tools/build_timeline.py    # everything    -> timeline.csv              (~5s)

python3 deck/build_deck.py         # slides_*.py   -> deck/braze-deck.html
python3 deck/make_script.py        # the deck      -> docs/PRESENTATION-SCRIPT.md
python3 deck/build_record.py       # record/*.md   -> deck/evidence-record.html
bash   tools/make_release.sh       # both docs     -> dist/ HTML + PDF + zip
```

Both generated documents read from their source, so neither can drift: `make_script.py`
reads the built deck, and `build_record.py` derives the slide map from it too.

---

## It runs without a human, and it stops when it should

No step in this repository blocks on a person. The review sites that block scripted
access (G2, Gartner, TrustRadius, Glassdoor all return 403) are handled by
**a three-tier ladder**: script → your own signed-in browser via the claude-in-chrome
tools → ask you to paste into files that already exist and already say what to capture.
And none of it is load-bearing, because `fetch_issues.py` captures 1,000+ unsolicited,
dated public issues as the customer-voice corpus regardless.

There is one deliberate stop. Collection is mechanical and wants a fast model; analysis
is judgement and wants a capable one. `tools/handoff.py` ends the pipeline with a report
of what was collected and what now needs deciding, and tells you to switch.
[`AGENTS.md`](AGENTS.md) carries the ladder, the model gates, the budgets, and the three
cases — and only three — where an agent should stop and ask.

---

## What is here already

| | |
|---|---|
| **14 extraction tools** | All dependency-free; every one tested against the live source |
| **An orchestrator** | `tools/run_all.py` — the whole pipeline, idempotent, with a status report |
| **A self-check** | `tools/verify.py` — ten rules the analysis must satisfy, `--strict` for a gate |
| **A model gate** | `tools/handoff.py` — ends collection with a report and a switch instruction |
| **Panel escalation** | `tools/panels_status.py` + pre-created paste targets in `sources/panels/` |
| **The deck design system** | `deck/lib.py`, `css.py`, `icons.py` + a working scaffold and [`deck/COMPONENTS.md`](deck/COMPONENTS.md) |
| **A record generator** | `deck/build_record.py` — enforces one-fact-one-home and derives the slide map from the deck |
| **The PDF release pipeline** | `tools/make_release.sh`, including the non-obvious static-font fix documented inline |
| **The method** | Seven phases, plus nine mistakes made in anger and what each taught |
| **The source catalogue** | Every public source, verified reachable, with what it yields and what it costs |
| **Two Claude skills** | `competitor-analysis` (the portable method) and `braze` (retrieval over this base) |

---

## Layout

```
START-HERE.md    the four prompts to paste, in order — start here
CLAUDE.md        operating rules for an agent working here
AGENTS.md        the unattended loop: budgets, escalation ladder, model gates
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
