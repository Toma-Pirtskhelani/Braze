# TODO — the research run, end to end

The executable checklist. Work top to bottom; each phase has a **done when** you can
actually check. Tick boxes as you go and commit the ticks — this file is the run's
progress log as well as its plan.

Read [`STRATEGY.md`](docs/STRATEGY.md) first. It is short and it changes how several of
these phases should be done.

**Estimated:** phase 1 is about forty minutes of wall time, unattended. Phases 2–5 are
the analysis. Phases 6–7 are the presentation, and they will take as long as everything
before them combined.

If you are the operator, [`START-HERE.md`](START-HERE.md) has the prompts to paste.

An agent running this alone should read [`AGENTS.md`](AGENTS.md) first: it carries the
budgets, the escalation ladder for blocked sources, the model gates, and the stopping
conditions.

**Phases 0–1 are collection and want a fast model. Phases 2–6 are judgement and want a
capable one.** `tools/handoff.py` ends phase 1 with a report and a switch instruction.

---

## Phase 0 · Setup — 10 minutes

- [ ] `git clone https://github.com/Toma-Pirtskhelani/Braze.git && cd Braze`
- [ ] `python3 --version` → 3.9 or newer. No third-party packages are needed anywhere.
- [ ] Optional but worth it, both free and both remove a real constraint:
  - [ ] `export GITHUB_TOKEN=...` — lifts 60 req/hr to 5,000, needed for the full release walk
  - [ ] `export CERTSPOTTER_TOKEN=...` — anonymous callers get roughly one page of CT data
- [ ] `export SEC_CONTACT="your name your@email"` — SEC asks for a real contact
- [ ] `python3 deck/build_deck.py` → should report **3 slides**, no missing notes
- [ ] Read [`docs/STRATEGY.md`](docs/STRATEGY.md), [`docs/SOURCES.md`](docs/SOURCES.md),
      [`docs/METHOD.md`](docs/METHOD.md). In that order.

**Done when:** the scaffold deck builds and you can state, in one sentence, why the
financial chapter is stronger here than on a private vendor.

---

## Phase 1 · Capture and extract — one command, ~40 minutes unattended

```bash
python3 tools/run_all.py            # everything below, in order, idempotent
python3 tools/run_all.py --dry-run  # see the plan first
```

It runs each step, skips anything already done, **continues past optional failures**, and
writes `logs/run-status.md` saying what ran, what failed, and what to do next. Interrupt
it and rerun; nothing is lost.

What it does, if you would rather drive it by hand:

- [ ] `fetch_sitemap.py` → `data/site_inventory.csv`  *(required — nothing downstream works without it)*
- [ ] `sec_facts.py` → `data/financials*.csv`
- [ ] `sec_filings.py` → `data/filings.csv`, `data/insider_filing_counts.csv`
- [ ] `status_history.py` → `data/incidents.csv`, `data/status_components.csv`
- [ ] `github_org.py` → `data/repos.csv`, `data/sdk_releases.csv`
- [ ] `ct_probe.py` → `data/subdomains.csv` *(crt.sh is often down; there is a fallback,
      and a failure here is logged rather than fatal)*
- [ ] `fetch_filings.py` → `sources/filings/` — the 10-K, 10-Q, 8-K and proxy as text.
      **The 10-K is ~73,000 words and is the richest single source on the company**
- [ ] `fetch_issues.py` → `data/issues.csv` + `sources/panels/github_issues.txt`
- [ ] `fetch_docs.py` → ~1,352 pages into `sources/docs/`. Resumable. ~25 minutes
- [ ] `index_docs.py` → `data/docs_index.csv` — **index before reading anything**
- [ ] `extract_api.py` → `data/api_endpoints.csv` — the second lens on capability
- [ ] `capability_count.py` → `data/capabilities.csv`
- [ ] `code_reviews.py` → `data/review_themes.csv`
- [ ] `build_timeline.py` → `data/timeline.csv`

Then, by hand:

- [ ] Capture the sub-processor disclosure into `sources/clean/` **with a capture date**
- [ ] Capture `security.txt` and `robots.txt`
- [ ] Read the section histogram `index_docs.py` prints. That distribution is the first
      real finding of the project and it costs nothing
- [ ] Revise [`docs/CAPABILITY-TAXONOMY.tsv`](docs/CAPABILITY-TAXONOMY.tsv) with Braze's
      **own** vocabulary — product names beat category words, and you could not guess
      them before the corpus existed — then rerun `capability_count.py`

### The review panels, and why they are not a blocker

G2, Gartner Peer Insights, TrustRadius and Glassdoor all return **HTTP 403** to scripted
access. They are *enrichment*, not a dependency: `fetch_issues.py` captures 1,000+
unsolicited, dated, public issues as the customer-voice corpus instead, and
`code_reviews.py` codes it like any other panel.

Pre-created paste targets already exist in `sources/panels/`, each naming its URL and what
to capture. Work the ladder: **script → the operator's signed-in browser via
claude-in-chrome → ask them to paste, once.** `python3 tools/panels_status.py` reports the
state and the next tier. `code_reviews.py` skips unfilled targets, so a missing panel never
becomes a zero in a percentage.

Gartner is the one worth chasing: its shortlists say who buyers actually compared them
against, and no other source has that. See *the escalation ladder* in
[`AGENTS.md`](AGENTS.md).

- [ ] `python3 tools/handoff.py` → `logs/handoff-report.md`, then **stop and switch to a
      more capable model.** Everything after this point ends up in front of an audience

**Done when:** `logs/run-status.md` shows no **required** failure, `data/` has ten or more
CSVs, every optional failure is written down in `logs/fetch-failures.md`, and the handoff
report has been read.

**Do not skip the failure log.** A gap you have written down is evidence; a gap you have
not is a mistake.

---

## Phase 2 · Read the documentation — the core of the analysis

Count before you read. Never read a file end to end.

- [ ] Data ingestion: **find the freshness table.** Which paths are event-driven and
      which are batch? Limits are admitted in tables, not prose.
- [ ] Identity resolution: how many identifier values per type are active and
      segmentable? This produced the reference project's sharpest technical finding.
- [ ] Rate limits: ingest vs export. **Compare the two directions** — asymmetry between
      how easily data goes in and comes out is a commercial fact as much as a technical one.
- [ ] Data model: how many fields, event types, reserved attributes?
- [ ] Channels: enumerate every one. Note which have no marketing page.
- [ ] Sub-processors: which supplier serves which channel — **and which channel has none**?
- [ ] Architecture: what do the twelve regional clusters mean for residency and latency?
- [ ] For each: record the fact in `docs/FACTS.md` with `path:line-range`, a grade and a date

**Done when:** every claim you intend to make about the product resolves to a
documentation line range, and at least two limits have been found that marketing does
not mention.

---

## Phase 3 · The money — audited, and kept in proportion

- [ ] Revenue, gross profit, gross margin: 7 fiscal years and every quarter available
- [ ] R&D / S&M / G&A as absolute lines and as a share of revenue
- [ ] Share-based compensation against net loss
- [ ] Remaining performance obligation as forward visibility
- [ ] Acquisitions: price, date, and what the business-combination note says was bought
- [ ] Geographic revenue split — audited, not inferred
- [ ] Customer count as the 10-K **defines** it, with the definition quoted
- [ ] 10-K risk factors: what the company itself says could go wrong
- [ ] Check `data/financials_restated.csv`. **Anything in it is a conflict** — open a
      `CONFLICTS.md` entry
- [ ] Bound average contract value from disclosed revenue ÷ disclosed customer count, and
      say plainly that it is a bound rather than a price

**Done when:** the money chapter is written and is **no more than about a fifth** of the
planned deck. If it is growing past that, re-read the equity-research trap in
[`STRATEGY.md`](docs/STRATEGY.md).

---

## Phase 4 · The records they do not control

- [ ] CT logs: sort by first-seen date and **read the newest fifteen hosts first**. That
      is where unannounced things appear.
- [ ] Any host in CT that appears in no documentation and no marketing page → investigate
- [ ] SDK release cadence per platform; flag anything with no release in 12 months
- [ ] Incident history: per quarter, by duration, by component. Shape, never a comparison
      against a vendor who publishes nothing
- [ ] Careers board by function — where is headcount actually going?
- [ ] Companies House: resolve **which** UK entity is theirs by matching against the
      10-K subsidiary exhibit, before citing either
- [ ] `python3 tools/code_reviews.py` → coded themes, with the script cited rather than
      the number

**Done when:** you have at least one finding that appears in no marketing page anywhere.

---

## Phase 5 · Triangulate and write the record

- [ ] Every finding tested against a **second independent lens**. Anything that survives
      only one lens is downgraded or dropped
- [ ] Every hypothesis in [`STRATEGY.md`](docs/STRATEGY.md) §"Ten hypotheses" is either
      evidenced with a source path **or explicitly killed**. A hypothesis quietly dropped
      is a bias
- [ ] `docs/FACTS.md` complete: every number that will be spoken has a row, a grade, a
      source path and a date
- [ ] `docs/CONFLICTS.md` complete: every disagreement has a ruling
- [ ] Build `deck/evidence-record.html` to [`RECORD-SPEC.md`](docs/RECORD-SPEC.md) —
      Record chapters first, Slide Map last
- [ ] Run both mechanical checks in RECORD-SPEC (slide coverage, div balance)

**Done when:** every fact appears in exactly one Record chapter and the coverage check
reports zero unreferenced slides.

---

## Phase 6 · The deck

- [ ] Write slides to [`DECK-SPEC.md`](docs/DECK-SPEC.md): `deck/slides_b.py` onward, one
      file per part. `build_deck.py` discovers them automatically
- [ ] Every slide: one idea, one grade, notes written at the same time as the slide
- [ ] Pick slide 37's deep-dive question from what turned out to be contested **and**
      answerable — not from what was interesting to research
- [ ] `python3 deck/build_deck.py && python3 deck/make_script.py`
- [ ] Paste `tools/typography_audit.js` into the deck's console; fix every overflow
- [ ] **Screenshot every slide and look at it.** Markup that parses can still render a
      key number as a stray glyph
- [ ] Every number on every slide resolves to a `FACTS.md` row

**Done when:** 41 slides build clean, no missing notes, no overflow, and you have looked
at all 41.

---

## Phase 7 · Release

- [ ] `bash tools/make_release.sh` → dated HTML + PDF + zip in `dist/`
- [ ] Verify the PDF reports **no fallback fonts**. Georgia or Menlo in the font list
      means the static-font step failed — the fix is documented inline in the script
- [ ] Page count matches the slide count (the script reads it from the deck, not a
      hardcoded number)
- [ ] Update `README.md` with the real corpus statistics
- [ ] Fill in the corpus-composition table in `docs/EVIDENCE-GRADES.md`
- [ ] Commit and push

**Done when:** someone who has never seen the repository can open `dist/`, read the deck,
and check any number in it against a source path.

---

## Standing rules for the whole run

- **`sources/` is immutable.** Never edit a captured file.
- **`data/` is CSV only, and only what a script in `tools/` can regenerate.** A table you
  made by hand belongs in `docs/`.
- **Never read a file end to end.** Count, then read a bounded range.
- **Never merge company-declared and independent figures.**
- **Cite `path:line-range`, a grade, and a capture date.** Every time.
- **Corrections are recorded, not patched.** Old value stays visible in `FACTS.md`.
