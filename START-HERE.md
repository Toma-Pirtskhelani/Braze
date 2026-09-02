# Start here — running the Braze research

Copy-paste instructions, in order. Two Claude Code sessions: one cheap and mechanical,
one expensive and thoughtful, with a hard stop between them.

Everything is designed so you do nothing except paste four prompts and, once, some
review text. If you are short of time, the only step that genuinely needs you is
**step 3**, and even that is optional.

---

## Step 0 · Set up — five minutes, once

```bash
git clone https://github.com/Toma-Pirtskhelani/Braze.git
cd Braze

export SEC_CONTACT="Toma Pirtskhelani your@email"   # SEC asks for a real contact
export GITHUB_TOKEN=...                             # optional: 60 req/hr → 5,000
export CERTSPOTTER_TOKEN=...                        # optional: lifts CT rate limiting

python3 deck/build_deck.py     # sanity check → "slides: 3"
claude                         # start Claude Code in this directory
```

Python 3.9+. **No packages to install** — every tool runs on a bare interpreter.

Both tokens are free and each removes a real constraint, but the run works without them.

---

## Step 1 · Collection — Sonnet 5, about 45 minutes

In Claude Code:

```
/model sonnet
```

Then paste:

> Read CLAUDE.md and AGENTS.md, then run the collection pipeline: `python3 tools/run_all.py`.
>
> It is idempotent and continues past optional failures, so let it finish. When a source
> fails, record it in `logs/fetch-failures.md` and move on — a missing source is a finding
> to report, not a reason to stop.
>
> For the review panels, work the escalation ladder in AGENTS.md: try my browser with the
> claude-in-chrome tools first, and only ask me to paste if that fails.
>
> When the pipeline reaches the handoff gate, stop there and show me the report. Do not
> start the analysis.

**What happens:** it fetches the sitemaps, the SEC filings and XBRL financials, the 10-K
text, the status-page incident history, the GitHub org and its release history, the public
issue trackers, the certificate-transparency logs, and about 1,352 documentation pages.
Then it indexes the corpus, measures capability, and builds a timeline.

Most of the wall time is the documentation fetch. You can leave it.

---

## Step 2 · The review panels — the one part that may need you

G2, Gartner Peer Insights, TrustRadius and Glassdoor block scripted access. The agent will
work three tiers in order, and you only appear at the third:

1. **Script.** Fails with HTTP 403. Already known; no time is spent here.
2. **Your browser.** The claude-in-chrome tools drive your real, signed-in Chrome. This
   usually works. Approve the tool prompts when they appear.
3. **You paste.** If the browser route fails, the agent will ask you once, naming files
   that already exist and already say what to capture:

   ```
   sources/panels/g2.md            sources/panels/glassdoor.md
   sources/panels/gartner.md       sources/panels/jobs.md
   sources/panels/trustradius.md
   ```

   Open the URL at the top of each file, copy the review text, paste it **below the
   PASTE line**, and change `status: EMPTY — awaiting capture` to `status: captured`.

   Paste raw text, not a summary. A summary is already an analysis, and the point of
   coding the corpus with a script is that nobody's judgement gets between the reviews
   and the count.

**None of this is load-bearing.** `tools/fetch_issues.py` already captured 1,000+
unsolicited public issues as the customer-voice corpus, so a missing panel becomes a
recorded absence rather than a hole. If you only do one, do **Gartner** — its shortlists
say who buyers actually compared Braze against, and no other source has that.

Check the state at any time with `python3 tools/panels_status.py`.

---

## Step 3 · The gate

The pipeline ends by writing `logs/handoff-report.md` and printing a stop notice. Read the
report. It says what was collected, what is missing and why that does not block, and the
six decisions that now need judgement.

**Switch models here.** Collection is routine; analysis is not. Everything up to this
point can be redone by rerunning a tool. Everything after it ends up in front of an
audience, and a cheaper model will make those calls plausibly and wrongly — which is worse
than making them slowly.

---

## Step 4 · Analysis — Opus 5, the long part

```
/model opus
```

Then paste:

> Read CLAUDE.md, AGENTS.md and logs/handoff-report.md.
>
> Collection is done. Work TODO.md phases 2 through 6: read the documentation for limits,
> read the 10-K, go to the records they do not control, triangulate, then write the
> evidence record and the deck.
>
> Record every finding in docs/FACTS.md as you go, with a source path, a grade and a
> capture date. Where two sources disagree, record both in docs/CONFLICTS.md with a ruling
> on what to say out loud — do not pick one.
>
> Every hypothesis in docs/STRATEGY.md must end either evidenced or explicitly killed.
> Run `python3 tools/verify.py` before you tell me anything is done.

This is the part that takes real time. Let it work through the phases; it will commit as
it goes.

**Watch for two things.** That the money chapter stays at about a fifth of the deck —
audited SEC data is abundant and will eat the whole thing if nobody stops it. And that
favourable findings actually appear: an analysis that only found problems was not an
analysis.

---

## Step 5 · Release

```
bash tools/make_release.sh
```

Produces dated HTML and PDF of both documents plus a zip, in `dist/`. The script rebuilds
everything from source first, so a release cannot be stale, and it verifies that no
fallback fonts crept into the PDF.

---

## If you want to check on it yourself

```bash
python3 tools/verify.py          # ten rules the analysis must satisfy
python3 tools/panels_status.py   # which panels are captured
cat logs/run-status.md           # what ran, what failed, what next
cat logs/fetch-failures.md       # every source that did not answer
rg -i 'gross margin' docs/FACTS.md   # look up any number
```

`verify.py` is the honest one. It checks that every figure spoken on a slide resolves to a
canonical row, that every conflict carries a ruling, and that the record covers every slide
that makes a claim. It has already caught real gaps in a finished analysis.

---

## The four prompts, together

For copying without the commentary.

**1 — collection (Sonnet 5):**

```
Read CLAUDE.md and AGENTS.md, then run the collection pipeline:
`python3 tools/run_all.py`. It is idempotent and continues past optional failures,
so let it finish. When a source fails, record it in logs/fetch-failures.md and move
on. For the review panels, work the escalation ladder in AGENTS.md: try my browser
with the claude-in-chrome tools first, and only ask me to paste if that fails. When
the pipeline reaches the handoff gate, stop there and show me the report. Do not
start the analysis.
```

**2 — analysis (Opus 5):**

```
Read CLAUDE.md, AGENTS.md and logs/handoff-report.md. Collection is done. Work
TODO.md phases 2 through 6: read the documentation for limits, read the 10-K, go to
the records they do not control, triangulate, then write the evidence record and the
deck. Record every finding in docs/FACTS.md as you go, with a source path, a grade
and a capture date. Where two sources disagree, record both in docs/CONFLICTS.md with
a ruling on what to say out loud — do not pick one. Every hypothesis in
docs/STRATEGY.md must end either evidenced or explicitly killed. Run
`python3 tools/verify.py` before you tell me anything is done.
```

**3 — review (Opus 5, when it says it is finished):**

```
Review your own work brutally. Run tools/verify.py. Then check the things it cannot:
is every hypothesis in STRATEGY.md resolved, is every uncomfortable finding stated as
observation rather than accusation, are the favourable findings actually present, and
did the money chapter stay at about a fifth of the deck? Screenshot every slide and
look at it. Tell me what is weak before I find it myself.
```

**4 — release (either model):**

```
Run `bash tools/make_release.sh`, confirm the PDF has no fallback fonts and the page
count matches the slide count, then commit and push everything.
```
