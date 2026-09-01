# Executed plan

What was actually done, in order, with dates. Append as you go; this is the run's audit
trail and the answer to "how did this number get here?"

---

## 2026-09-01 — environment set up

Built from the learnings of a completed competitor analysis on a private vendor. **No
Braze research was performed** beyond probing each candidate source to confirm it exists
and to size the job — recorded in [`provenance.md`](provenance.md).

**Reconnaissance.** 25 candidate sources probed. The decisive finding was structural, not
about Braze's business: as a listed company it publishes audited, machine-readable
quarterly financials, which inverts the evidence profile relative to the reference
project and is what [`docs/STRATEGY.md`](../docs/STRATEGY.md) is written around.

**Tooling.** Eleven extractors written, all dependency-free, each tested against its live
source:

| Tool | Test result |
|---|---|
| `sec_facts.py` | 778 facts, 29 concepts, 2019-01-31 → 2026-04-30 |
| `sec_filings.py` | 737 filings parsed, 536 insider filings across 56 months |
| `status_history.py` | 132 components, 451 incidents back to 2016-10-09 |
| `github_org.py` | 137 repos, 494 releases across 9 SDK repos |
| `fetch_sitemap.py` | 6,366 URLs from 8 sitemaps |
| `fetch_docs.py` | 3-page smoke test; chrome stripping and boilerplate capture verified |
| `index_docs.py` | indexed the 3 test docs |
| `capability_count.py` | ran the focused-page test over them |
| `code_reviews.py` | ran against a synthetic fixture |
| `build_timeline.py` | 1,845 dated events merged from 4 independent sources |
| `ct_probe.py` | **both CT sources unavailable at the time** — see fetch-failures |

All test output was written to a scratch directory and discarded, so `data/` and
`sources/` ship empty.

**Bugs found and fixed while testing** — each is a trap the research run now avoids:

| Bug | Fix |
|---|---|
| `config.get()` raised `SystemExit`, so `ct_probe`'s crt.sh → Cert Spotter fallback never ran | Raise `RuntimeError`; callers with a fallback can catch it |
| XBRL `fy` describes the filing, not the period — two fiscal years both labelled `fy2026` | Derive `period` from `start`/`end`; document the trap in the script and in CLAUDE.md |
| Statuspage history walk stopped at the first page that overlapped the API feed | Break on genuinely empty pages, not on pages with no *new* incidents. 62 → **451** incidents |
| Wide financial tables emitted two rows per period, one from the instant fact and one from the duration | Key on period end; the duration's label wins |
| Cert Spotter rate-limits anonymous callers mid-pagination, losing everything | Keep partial results and report how far it got |
| Nav chrome leaked into every fetched page and would have inflated every later count | Cut above the page's own `h1`; keep the chrome once in `sources/boilerplate.txt` |
| `make_release.sh` asserted a hardcoded 41-page count | Read the slide count from the built deck |
| `bootstrap.py` copied the source repo's title slide and fiscal year into a new vendor's repo | Write a vendor-neutral `slides_a.py`; move `FY_END` and the deck title into `config.py` |

**Deck.** The design system was ported from the reference deck (`lib.py`, `css.py`,
`icons.py`) with a 3-slide scaffold carrying only method content. `build_deck.py` now
discovers `slides_*.py` automatically, so adding a chapter needs no edit to the
assembler. Verified in a browser: fonts load, no overflow, grade ledger renders.

**Documentation.** Strategy, source catalogue, method, evidence grades, deck spec, record
spec, question backlog, fact index skeleton, conflicts register, retrieval guide,
operating rules, and the phase-by-phase TODO.

**Skills.** `competitor-analysis` (portable method, four references, a bootstrap script
tested end to end by scaffolding a Klaviyo repo, and a record template) and `braze`
(retrieval over this evidence base, which grows as facts land). Both carry eval cases.

**Outstanding at handover:** CT logs were not captured — crt.sh was returning 502 and
Cert Spotter rate-limited. Recorded in [`fetch-failures.md`](fetch-failures.md); retry
before phase 5, as CT is the highest-value infrastructure source.

---

<!-- ## <date> — <phase>  -->
