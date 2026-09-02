# Index — which file answers which question

## Start here, in this order

| Question | File |
|---|---|
| What do I do? | [`../TODO.md`](../TODO.md) |
| How do I run this unattended? | [`../AGENTS.md`](../AGENTS.md) |
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
| **How does this compare to the reference deck?** | [`COMPARISON.md`](COMPARISON.md) — slide by slide, as a spoken presentation |
| **What is wrong with the finished analysis?** | [`CRITIQUE-4.md`](CRITIQUE-4.md) — current, from the operator's read-through · [`-3`](CRITIQUE-3.md) · [`-2`](CRITIQUE-2.md) · [`-1`](CRITIQUE.md) |
| What is being counted as a capability? | [`CAPABILITY-TAXONOMY.tsv`](CAPABILITY-TAXONOMY.tsv) |
| What do I say over each slide? | `PRESENTATION-SCRIPT.md` *(generated)* |
| How do I write a slide? | [`../deck/COMPONENTS.md`](../deck/COMPONENTS.md) |

## By source type

| Source | Tool | Output |
|---|---|---|
| SEC XBRL financials | `tools/sec_facts.py` | `data/financials*.csv` |
| SEC filing index | `tools/sec_filings.py` | `data/filings.csv` |
| SEC filing documents | `tools/fetch_filings.py` | `sources/filings/*.txt` |
| Certificate transparency | `tools/ct_probe.py` | `data/subdomains.csv` |
| Public status page | `tools/status_history.py` | `data/incidents.csv` |
| Public repositories | `tools/github_org.py` | `data/repos.csv`, `data/sdk_releases.csv` |
| Public issue trackers | `tools/fetch_issues.py` | `data/issues.csv`, a coded panel |
| Sitemaps | `tools/fetch_sitemap.py` | `data/site_inventory.csv` |
| Documentation | `tools/fetch_docs.py` → `tools/index_docs.py` | `sources/docs/`, `data/docs_index.csv` |
| API surface | `tools/extract_api.py` | `data/api_endpoints.csv` |
| Capability measurement | `tools/capability_count.py` | `data/capabilities.csv` |
| Review panels | `tools/code_reviews.py` | `data/review_themes.csv` |
| Everything dated | `tools/build_timeline.py` | `data/timeline.csv` |

## Building and checking

| Task | Command |
|---|---|
| Run the whole pipeline | `python3 tools/run_all.py` |
| Check the analysis against its own rules | `python3 tools/verify.py` |
| Build the deck and its script | `python3 deck/build_deck.py && python3 deck/make_script.py` |
| Build the evidence record | `python3 deck/build_record.py` |
| Cut a dated release | `bash tools/make_release.sh` |

## Process and provenance

| Question | File |
|---|---|
| What ran, what failed, what next? | `../logs/run-status.md` |
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
