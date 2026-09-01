# Index — which file answers which question

## Start here, in this order

| Question | File |
|---|---|
| What do I do? | [`../TODO.md`](../TODO.md) |
| What is different about analysing Braze? | [`STRATEGY.md`](STRATEGY.md) |
| Where do I pull sources from? | [`SOURCES.md`](SOURCES.md) |
| How is this done at all? | [`METHOD.md`](METHOD.md) |
| How do I search the corpus? | [`../RETRIEVAL.md`](../RETRIEVAL.md) |

## By subject

| Question | File |
|---|---|
| What is the canonical value of a number? | [`FACTS.md`](FACTS.md) |
| Two sources disagree — what do I say? | [`CONFLICTS.md`](CONFLICTS.md) |
| How trustworthy is this claim? | [`EVIDENCE-GRADES.md`](EVIDENCE-GRADES.md) |
| What must each slide answer? | [`DECK-SPEC.md`](DECK-SPEC.md) |
| How is the evidence record structured? | [`RECORD-SPEC.md`](RECORD-SPEC.md) |
| What still needs answering? | [`QUESTIONS.md`](QUESTIONS.md) |
| What is being counted as a capability? | [`CAPABILITY-TAXONOMY.tsv`](CAPABILITY-TAXONOMY.tsv) |
| What do I say over each slide? | `PRESENTATION-SCRIPT.md` *(generated)* |

## By source type

| Source | Tool | Output |
|---|---|---|
| SEC XBRL financials | `tools/sec_facts.py` | `data/financials*.csv` |
| SEC filing index | `tools/sec_filings.py` | `data/filings.csv` |
| Certificate transparency | `tools/ct_probe.py` | `data/subdomains.csv` |
| Public status page | `tools/status_history.py` | `data/incidents.csv` |
| Public repositories | `tools/github_org.py` | `data/repos.csv`, `data/sdk_releases.csv` |
| Sitemaps | `tools/fetch_sitemap.py` | `data/site_inventory.csv` |
| Documentation | `tools/fetch_docs.py` → `tools/index_docs.py` | `sources/docs/`, `data/docs_index.csv` |
| Capability measurement | `tools/capability_count.py` | `data/capabilities.csv` |
| Review panels | `tools/code_reviews.py` | `data/review_themes.csv` |
| Everything dated | `tools/build_timeline.py` | `data/timeline.csv` |

## Process and provenance

| Question | File |
|---|---|
| What failed to fetch, and when? | `../logs/fetch-failures.md` |
| What was captured, from where, on what date? | `../logs/provenance.md` |
| What was actually executed? | `../logs/executed-plan.md` |

## Skills

| Skill | For |
|---|---|
| `.claude/skills/braze/` | Answering Braze questions from this evidence base |
| `.claude/skills/competitor-analysis/` | Running this method on a *different* vendor |

They are kept separate on purpose: the method carries no company facts, and the
retrieval skill carries no method. That is what lets either be used without the other.
