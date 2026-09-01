# Evidence grading, conflicts, and corrections

## The five grades

Ordered by how hard it would be for the vendor to have made the statement untrue.

| grade | source | why it sits here |
|---|---|---|
| `audited` | SEC filings, filed statutory accounts, XBRL | Signed off by auditors, filed under legal penalty. Restatement is itself a filed, visible event |
| `infrastructure` | Certificate transparency logs | Recorded by independent operators, append-only. The subject cannot edit or retract it |
| `documented` | Technical docs, API spec, public VCS, status page, **compelled disclosures** | Self-published but written to be operationally correct. An engineer following a wrong endpoint files a ticket; a status page is read live during an outage |
| `third-party` | Review panels, analyst notes, registries | Published by someone else. The vendor may curate or respond, and review panels are solicited — independent, but not disinterested |
| `claimed` | Marketing, press releases, case studies, comparison pages | Written to persuade. Fine for what they claim; no support for whether it is true |

**Compelled disclosures** (sub-processor lists, DPAs) sit inside `documented` but deserve
a note in the citation: they are legally required to be complete, and that is what gives
them force.

## The rules

1. **A claim's grade is the grade of its weakest supporting source**, never its best.
2. **Repetition is not corroboration.** Site furniture repeated across a thousand pages
   is one claim, cited once. Strip it to a boilerplate file so it cannot be counted N
   times.
3. **Company-declared and independent figures never merge silently.** Carry an
   `evidence` column in every CSV. Where two rosters exist, keep two rosters.
4. **Absence of evidence is reported as absence of evidence** — except where the check
   was exhaustive and is stated as such.
5. **Dates from `lastmod` and page frontmatter are suspect.** They are often build
   timestamps. Prefer CT logs, VCS history, filing dates, incident timestamps.
6. **Keep more resolution in the record than on the slide.** Five grades in the record,
   three on the deck, with an explicit mapping.

## Conflicts

Where two credible sources disagree, **both are recorded and neither is chosen.** Each
entry carries a **ruling**: the exact sentence to say out loud.

```
### C-NN · <the question in six words>

| | value | source | grade | as of |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

**Why they differ:** <different definitions, dates, populations, or a real contradiction>

**Ruling:** <the sentence to use>
```

Rulings that have earned their keep:

- *"Quote the range, never a precise figure"* — for headcount, where four published
  values disagree
- *"Quote the ordering, never the decimal"* — for market share, where one source
  reported three different positions
- *"Give both numbers and explain the gap; never call either a lie"* — for customer
  counts measured two ways

Number entries sequentially and **never renumber**. A conflict later resolved keeps its
number and gains a *Resolved* line; the history is the point.

### Three things that look like conflicts and are not

- **Different definitions of the same word.** A filing's "customer" and a marketing
  "customer" may both be right. State both definitions instead.
- **Different dates.** A figure that changed is not a figure in dispute.
- **Marketing contradicting an audited filing.** That is an *error*, not a
  disagreement. Give the filed figure, note it is filed under penalty, say so without
  drama.

### One that is easy to miss and *is* a conflict

**A restated financial figure.** If the same period's number changed between filings,
that is a recorded, dated disagreement by the company with itself. Extract restatements
programmatically and open an entry for each.

## Corrections

**A file that shows its own errors is the reason to trust the rest of it.**

Keep a *numbers that were wrong and are now right* table with the old value still
visible, what it is now, why it changed, and the date. Never quietly patch a figure: a
stale copy of a deck is already circulating, and the only way its holder can recognise
it as stale is if the old value is still findable.

| Fact | Was | Is now | Why it changed | Date |
|---|---|---|---|---|

This is also the cheapest credibility you will ever buy. An analysis with a visible
corrections log is read as careful. One with none is read as unchecked.
