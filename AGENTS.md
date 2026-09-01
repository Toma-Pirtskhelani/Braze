# Runbook — running this analysis unattended

For an agent working alone. Read [`CLAUDE.md`](CLAUDE.md) for the rules and
[`docs/STRATEGY.md`](docs/STRATEGY.md) for what makes Braze different. This file is the
loop, the budgets, and the stopping conditions.

**Nothing in this repository requires a human.** Bot-walled sources are handled by
substitution, not by waiting — see *Degradation* below.

---

## The loop

```bash
python3 tools/run_all.py            # phases 1-4: capture, extract, build. ~40 min
python3 tools/verify.py             # what is still wrong
cat logs/run-status.md              # what ran, what failed, what to do next
```

Then, in order, and committing after each:

| Step | Do | Done when |
|---|---|---|
| 1 | `run_all.py` | `logs/run-status.md` shows no **required** failure |
| 2 | Revise `docs/CAPABILITY-TAXONOMY.tsv` with Braze's own vocabulary, rerun `capability_count.py` | The taxonomy uses product names, not category words |
| 3 | Read the documentation ([`TODO.md`](TODO.md) phase 2), writing each finding into `docs/FACTS.md` | Every product claim resolves to a `path:line-range` |
| 4 | Read the 10-K ([`TODO.md`](TODO.md) phase 3) | The money chapter is written and is ~a fifth of the planned deck |
| 5 | Records they do not control ([`TODO.md`](TODO.md) phase 4) | At least one finding appears in no marketing page |
| 6 | Write `deck/record/*.md`, run `deck/build_record.py` | 0 unmapped slides, 0 duplicate figures |
| 7 | Write `deck/slides_b.py` onward per [`docs/DECK-SPEC.md`](docs/DECK-SPEC.md) | `verify.py` reports 0 failures |
| 8 | `bash tools/make_release.sh` | PDF has no fallback fonts |

`run_all.py` is idempotent. Interrupt it, rerun it, lose nothing.

---

## Budgets — when to stop

An unattended run can burn a day on the wrong thing. These are ceilings, not targets.

| Activity | Ceiling | Then |
|---|---|---|
| Any single fetch tool | 1 retry cycle | Log it and move on. `run_all.py` already does this |
| Reading a documentation area | ~6 bounded reads | You have the finding or there is not one |
| Chasing one open question | 3 distinct sources | Move it to `QUESTIONS.md` §4 with what would close it |
| A single slide | 2 rebuild-and-look cycles | Ship it and note it, or cut it |
| Total corpus reading | Never read a file end to end | Count first, always |

**The strongest signal that you are off track is reading rather than counting.** If you
have opened more than a handful of files without running `rg -c` first, stop and count.

---

## Degradation — what to do when a source is unavailable

**Never wait for a human. Substitute, then record the substitution.**

| Blocked | Substitute | What you lose, and must say |
|---|---|---|
| G2 / Gartner / TrustRadius (403) | `tools/fetch_issues.py` — 1,000+ unsolicited public issues, dated, with resolution times | Issue authors are developers, not buyers. It tells you about the SDK surface, not the dashboard, and it is not a satisfaction measure |
| Glassdoor (403) | Careers board by function; `DEF 14A` compensation | Sentiment is unavailable. Say so; do not infer it |
| crt.sh (502) | Cert Spotter, with `CERTSPOTTER_TOKEN` | Possibly a partial host list. Say the list is partial |
| Both CT sources | Nothing equivalent | Record the absence. **Do not claim there is nothing unannounced** — you did not look |
| A price anywhere | Revenue ÷ disclosed customer count | A bound, not a price. Say "bounded at", never "costs" |

Every substitution goes in `logs/fetch-failures.md` **and** in the deck's open-questions
slide. A gap you have written down is evidence; a gap you have not is a mistake.

---

## Stop and ask a human only for these

Three cases. Everything else, decide and record the decision.

1. **A finding that would name a third party adversely** — a customer, a named
   individual, a partner. Write it into the record; keep it off the deck until asked.
2. **A source that requires accepting terms, logging in, or paying.** Do not accept
   terms on anyone's behalf.
3. **Evidence of something unlawful or a live security exposure.** Stop, write down what
   you saw and where, and hand it over. Do not probe further.

Rate limits, 403s, down endpoints and ambiguous figures are **not** in this list. They
have documented answers above.

---

## Self-check before declaring done

```bash
python3 tools/verify.py --strict     # exits 1 on any rule violation
```

Then confirm by hand what a script cannot:

- [ ] Every hypothesis in `docs/STRATEGY.md` is evidenced **or explicitly killed**. A
      hypothesis quietly dropped is a bias, and it is the failure a lone agent is most
      prone to
- [ ] Every uncomfortable finding is stated as observation, not accusation
- [ ] Every favourable finding that the evidence supports is actually in the deck. An
      analysis that only found problems was not an analysis
- [ ] The money chapter did not eat the deck
- [ ] You have **looked at** every slide, not just built it

---

## What good output looks like

Not "Braze is strong in X and weak in Y". That is a summary and the audience could have
written it.

> Their own data-freshness table admits only one of four ingestion paths is
> event-driven — `sources/docs/…:120-160`, captured 2026-09-14 — and a customer
> independently described hitting exactly that in a public issue eight months earlier.

Precise, sourced, dated, corroborated from two unrelated directions, and with nothing in
it to argue with. That is the bar.
