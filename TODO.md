# TODO — the research run, end to end

The executable checklist. Work top to bottom; each phase has a **done when** you can
actually check. Tick boxes as you go and commit the ticks — this file is the run's
progress log as well as its plan.

Read [`STRATEGY.md`](docs/STRATEGY.md) first. It is short and it changes how several of
these phases should be done.

**Estimated:** phases 0–2 take about an hour of wall time, most of it the docs fetch
running unattended. Phases 3–6 are the analysis. Phases 7–8 are the presentation, and
they will take as long as everything before them combined.

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

## Phase 1 · Capture — 45 minutes, mostly unattended

Cheap and exhaustive first; expensive and partial last.

- [ ] `python3 tools/fetch_sitemap.py` → `data/site_inventory.csv`
- [ ] `python3 tools/sec_facts.py` → `data/financials*.csv`
- [ ] `python3 tools/sec_filings.py` → `data/filings.csv`, `data/insider_filing_counts.csv`
- [ ] `python3 tools/status_history.py` → `data/incidents.csv`, `data/status_components.csv`
- [ ] `python3 tools/github_org.py` → `data/repos.csv`, `data/sdk_releases.csv`
- [ ] `python3 tools/ct_probe.py` → `data/subdomains.csv`
      *(crt.sh is often down. If both sources fail, record it in `logs/fetch-failures.md`
      and retry later — do not silently skip it, CT is the highest-value infrastructure source)*
- [ ] `python3 tools/fetch_docs.py` → ~1,352 pages into `sources/docs/`. Resumable; rerun
      if interrupted. Budget ~25 minutes.
- [ ] Capture the API reference into `sources/external/` and extract to
      `data/api_endpoints.csv` — endpoint counts are the second lens on capability and
      the measurement is much weaker without them
- [ ] Capture the sub-processor disclosure into `sources/clean/` **with a capture date**
- [ ] Capture `security.txt`, `robots.txt` and the status-page component list
- [ ] Panels — these are 403 to scripts, so use a browser session or paste them in:
  - [ ] G2 → `sources/panels/g2.txt`
  - [ ] Gartner Peer Insights → `sources/panels/gartner.txt` *(capture the shortlists —
        who buyers compared them against is the highest-value field on the page)*
  - [ ] TrustRadius → `sources/panels/trustradius.txt`
  - [ ] Glassdoor → `sources/panels/glassdoor.txt`
  - [ ] Careers board → `sources/panels/jobs.txt`
- [ ] Every panel file opens with a capture date on line 1

**Done when:** `sources/` has the docs corpus and at least three panels, `data/` has six
or more CSVs, and every failure is written down in `logs/fetch-failures.md`.

**Do not skip the failure log.** A gap you have written down is evidence; a gap you have
not is a mistake.

---

## Phase 2 · Index — 10 minutes

- [ ] `python3 tools/index_docs.py` → `data/docs_index.csv`, `data/docs_sections.csv`
- [ ] Read the section histogram it prints. That distribution is the first real finding
      of the project and it costs nothing.
- [ ] Revise [`docs/CAPABILITY-TAXONOMY.tsv`](docs/CAPABILITY-TAXONOMY.tsv) using Braze's
      **own** vocabulary — product names beat category words, and you could not guess
      them before now
- [ ] `python3 tools/capability_count.py` → `data/capabilities.csv`
- [ ] `python3 tools/build_timeline.py` → `data/timeline.csv`

**Done when:** you can answer "which capability carries the most documentation, and which
carries almost none?" without opening a single source file.

---

## Phase 3 · Read the documentation — the core of the analysis

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

## Phase 4 · The money — audited, and kept in proportion

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

## Phase 5 · The records they do not control

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

## Phase 6 · Triangulate and write the record

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

## Phase 7 · The deck

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

## Phase 8 · Release

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
