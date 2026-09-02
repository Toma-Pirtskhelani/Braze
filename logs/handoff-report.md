# Handoff — collection complete, analysis pending

Generated 2026-09-02 by `tools/handoff.py`.

## What was collected

| table | rows |
|---|---|
| `data/api_endpoints.csv` | 135 |
| `data/capabilities.csv` | 38 |
| `data/docs_index.csv` | 1,352 |
| `data/docs_sections.csv` | 6 |
| `data/filings.csv` | 737 |
| `data/financials.csv` | 778 |
| `data/financials_annual.csv` | 26 |
| `data/financials_quarterly.csv` | 17 |
| `data/financials_restated.csv` | 0 |
| `data/incidents.csv` | 451 |
| `data/insider_filing_counts.csv` | 56 |
| `data/issues.csv` | 845 |
| `data/repos.csv` | 137 |
| `data/review_coding.csv` | 860 |
| `data/review_themes.csv` | 21 |
| `data/sdk_releases.csv` | 494 |
| `data/site_inventory.csv` | 6,366 |
| `data/status_components.csv` | 132 |
| `data/subdomains.csv` | 833 |
| `data/timeline.csv` | 2,678 |

| corpus | count |
|---|---|
| documentation pages | 1352 |
| filing documents | 56 |
| review panels captured | 6 |
| raw captures | 0 |

## What is missing, and why it is not blocking

All review panels captured.

**Sources still outstanding** (from `logs/fetch-failures.md`):

- `crt.sh/?q=%25.braze.com&output=json` | HTTP 502 Bad Gateway, sustained | **Outstanding.** crt.sh is frequently down; retry. Cert Spotter is the fallback

Each needs an outcome before the deliverable ships: retried, permanently unavailable (then stated in the deck as an absence), or needs a human.

## What now needs judgement

These are the decisions the rest of the project turns on. None of them has a right answer a script can check.

1. **Revise the capability taxonomy.** `docs/CAPABILITY-TAXONOMY.tsv` still holds the generic starter patterns written before the corpus existed. Product names beat category words and you could not guess them before now. Revise it, rerun `capability_count.py`, and note in `FACTS.md` that the numbers moved because the pattern set moved.

2. **Read the documentation for limits.** The freshness table, the identity model, ingest-versus-export rate limits. Limits get admitted in tables, not prose. Two of the strongest findings on the reference project came from exactly here.

3. **Read the 10-K, and keep it in proportion.** Item 1A risk factors are the only section a company is legally obliged to be candid in. Then stop: the money chapter is about a fifth of the deck, and abundant SEC data will eat the whole thing if you let it.

4. **Rule on every conflict.** Each entry in `docs/CONFLICTS.md` needs a sentence a presenter can say out loud. "Quote the range, never a precise figure" is a ruling. Picking one value is not.

5. **Kill or evidence every hypothesis.** `docs/STRATEGY.md` carries ten. Each must end the project evidenced with a source path or explicitly killed. A hypothesis quietly dropped is a bias, and it is the failure a lone agent is most prone to.

6. **Decide what NOT to say.** Findings that survive only one lens get downgraded or cut. This is the judgement that most needs a capable model, and the one with no checklist.

---

## Switch models here

Collection is routine and wants a fast model. Analysis is judgement and wants a capable one — a cheaper model will make these calls plausibly and wrongly, which is worse than making them slowly.

Everything before this point is reversible: rerun a tool, refetch a page. Everything after it ends up in front of an audience.

**Switch to Opus 5 (`/model opus`), then open with:**

```
Read CLAUDE.md, AGENTS.md and logs/handoff-report.md.

Collection is done. Work TODO.md phases 2 through 7: read the documentation for limits, read the 10-K, go to the records they do not control, triangulate, then write the record and the deck.

Record every finding in docs/FACTS.md with a source path, a grade and a date as you go. Run tools/verify.py before you tell me anything is done.
```

