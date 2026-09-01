# Conflicts register

Where two credible sources disagree, **both are recorded and neither is chosen.** Each
entry carries a **ruling**: the sentence to say out loud. Follow the ruling.

This is not fence-sitting. "Quote the ordering, never the decimal" and "quote the range,
never a precise figure" are more useful to a presenter than a number picked by coin
toss, and they are honest about what is actually known.

## How to open an entry

```
### C-NN · <the question in six words>

| | value | source | grade | as of |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

**Why they differ:** <the mechanism, if known — different definitions, different dates,
different populations, or a genuine contradiction>

**Ruling:** <the exact sentence to use out loud>
```

Number entries sequentially and never renumber. A conflict that is later resolved keeps
its number and gains a **Resolved** line — the history is the point.

## When something is *not* a conflict

Three cases that look like conflicts and are not:

- **Different definitions of the same word.** A 10-K "customer" and a marketing
  "customer" may both be right. That is a definitions problem: state both definitions,
  and do not put it here.
- **Different dates.** A figure that changed is not a figure in dispute. Date both and
  move on.
- **Marketing contradicting an audited filing.** For a listed company that is an
  *error*, not a disagreement. Give the filed figure, note that it is filed under
  penalty, and say so without drama. Only record it here if the discrepancy is itself
  the finding.

And one case that *is* a conflict and is easy to miss: **a restated financial figure.**
`tools/sec_facts.py` writes every superseded value to `data/financials_restated.csv`.
Anything that lands in that file gets an entry here.

---

## Register

_Empty. Entries arrive with the research._

<!--
### C-01 · <question>

| | value | source | grade | as of |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

**Why they differ:**

**Ruling:**
-->
