#!/usr/bin/env python3
"""Stop at the model gate: report what was collected, and what now needs judgement.

    python3 tools/handoff.py

WHY THERE IS A GATE

This project has two halves that want different things from a model.

  COLLECTION is routine. Run fourteen tools in order, handle a 403, retry a timeout,
  paste a panel into a file. It is mechanical, it is long, and it wants a fast model.

  ANALYSIS is judgement. Deciding that a documentation gap is a finding rather than a
  coincidence. Deciding which of two figures a slide should carry, and refusing to pick
  when the honest answer is a range. Deciding a hypothesis is dead. Choosing what NOT to
  say. Those decisions are where a competitive analysis is won or lost, and a cheaper
  model will make them plausibly and wrongly - which is worse than making them slowly.

So the run stops here. This writes logs/handoff-report.md and prints the prompt to open
the next session with.

The gate is not a formality. Everything before it is reversible - rerun a tool, refetch a
page. Everything after it ends up in front of an audience.
"""
import csv
import os
import re
from datetime import date

import config


def rows(name):
    p = os.path.join(config.DATA, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as fh:
        return max(0, sum(1 for _ in fh) - 1)


def count_dir(sub, ext=None):
    p = os.path.join(config.SOURCES, sub)
    if not os.path.isdir(p):
        return 0
    return len([f for f in os.listdir(p)
                if not f.startswith(".") and (ext is None or f.endswith(ext))])


DECISIONS = [
    ("Revise the capability taxonomy",
     "`docs/CAPABILITY-TAXONOMY.tsv` still holds the generic starter patterns written "
     "before the corpus existed. Product names beat category words and you could not "
     "guess them before now. Revise it, rerun `capability_count.py`, and note in "
     "`FACTS.md` that the numbers moved because the pattern set moved."),
    ("Read the documentation for limits",
     "The freshness table, the identity model, ingest-versus-export rate limits. Limits "
     "get admitted in tables, not prose. Two of the strongest findings on the reference "
     "project came from exactly here."),
    ("Read the 10-K, and keep it in proportion",
     "Item 1A risk factors are the only section a company is legally obliged to be "
     "candid in. Then stop: the money chapter is about a fifth of the deck, and abundant "
     "SEC data will eat the whole thing if you let it."),
    ("Rule on every conflict",
     "Each entry in `docs/CONFLICTS.md` needs a sentence a presenter can say out loud. "
     "\"Quote the range, never a precise figure\" is a ruling. Picking one value is not."),
    ("Kill or evidence every hypothesis",
     "`docs/STRATEGY.md` carries ten. Each must end the project evidenced with a source "
     "path or explicitly killed. A hypothesis quietly dropped is a bias, and it is the "
     "failure a lone agent is most prone to."),
    ("Decide what NOT to say",
     "Findings that survive only one lens get downgraded or cut. This is the judgement "
     "that most needs a capable model, and the one with no checklist."),
]


def main():
    today = date.today().isoformat()
    data_files = sorted(f for f in os.listdir(config.DATA)
                        if f.endswith(".csv")) if os.path.isdir(config.DATA) else []

    corpus = [("documentation pages", count_dir("docs", ".md")),
              ("filing documents", count_dir("filings", ".txt")),
              ("review panels captured", 0), ("raw captures", count_dir("raw"))]

    # panel state, from the same source of truth panels_status.py uses
    pdir = os.path.join(config.SOURCES, "panels")
    captured, waiting = [], []
    if os.path.isdir(pdir):
        for f in sorted(os.listdir(pdir)):
            if not f.endswith((".md", ".txt")):
                continue
            txt = open(os.path.join(pdir, f), encoding="utf-8", errors="replace").read()
            (waiting if re.search(r"^status:\s*EMPTY", txt, re.M) else captured).append(f)
    corpus[2] = ("review panels captured", len(captured))

    lines = ["# Handoff — collection complete, analysis pending", "",
             "Generated %s by `tools/handoff.py`." % today, "",
             "## What was collected", "", "| table | rows |", "|---|---|"]
    for f in data_files:
        n = rows(f)
        lines.append("| `data/%s` | %s |" % (f, "{:,}".format(n) if n is not None else "-"))
    lines += ["", "| corpus | count |", "|---|---|"]
    for name, n in corpus:
        lines.append("| %s | %d |" % (name, n))

    lines += ["", "## What is missing, and why it is not blocking", ""]
    if waiting:
        lines.append("**Review panels still empty:** %s"
                     % ", ".join("`sources/panels/%s`" % f for f in waiting))
        lines.append("")
        lines.append("Run `python3 tools/panels_status.py` for the escalation ladder. "
                     "`data/issues.csv` already covers the customer-voice requirement "
                     "from a source that needs no human, so no panel is load-bearing on "
                     "its own. Gartner is the one worth chasing: its shortlists say who "
                     "buyers actually compared this vendor against.")
    else:
        lines.append("All review panels captured.")
    fails = os.path.join(config.LOGS, "fetch-failures.md")
    if os.path.exists(fails):
        out = [l for l in open(fails, encoding="utf-8").read().split("\n")
               if "Outstanding" in l or "**Partial**" in l]
        if out:
            lines += ["", "**Sources still outstanding** (from `logs/fetch-failures.md`):", ""]
            lines += ["- " + re.sub(r"\s+", " ", l.strip("| "))[:160] for l in out[:8]]
            lines += ["", "Each needs an outcome before the deliverable ships: retried, "
                          "permanently unavailable (then stated in the deck as an "
                          "absence), or needs a human."]

    lines += ["", "## What now needs judgement", "",
              "These are the decisions the rest of the project turns on. None of them has "
              "a right answer a script can check.", ""]
    for i, (title, body) in enumerate(DECISIONS, 1):
        lines += ["%d. **%s.** %s" % (i, title, body), ""]

    lines += ["---", "",
              "## Switch models here", "",
              "Collection is routine and wants a fast model. Analysis is judgement and "
              "wants a capable one — a cheaper model will make these calls plausibly and "
              "wrongly, which is worse than making them slowly.", "",
              "Everything before this point is reversible: rerun a tool, refetch a page. "
              "Everything after it ends up in front of an audience.", "",
              "**Switch to Opus 5 (`/model opus`), then open with:**", "",
              "```",
              "Read CLAUDE.md, AGENTS.md and logs/handoff-report.md.",
              "",
              "Collection is done. Work TODO.md phases 2 through 7: read the "
              "documentation for limits, read the 10-K, go to the records they do not "
              "control, triangulate, then write the record and the deck.",
              "",
              "Record every finding in docs/FACTS.md with a source path, a grade and a "
              "date as you go. Run tools/verify.py before you tell me anything is done.",
              "```", ""]

    os.makedirs(config.LOGS, exist_ok=True)
    p = os.path.join(config.LOGS, "handoff-report.md")
    open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")

    print("=" * 72)
    print("  COLLECTION COMPLETE — MODEL GATE")
    print("=" * 72)
    print("  %d tables in data/ | %s"
          % (len(data_files), " | ".join("%d %s" % (n, name) for name, n in corpus if n)))
    if waiting:
        print("  %d review panel(s) still empty: %s" % (len(waiting), ", ".join(waiting)))
    print()
    print("  Written: logs/handoff-report.md")
    print()
    print("  Analysis needs judgement, not throughput. Switch models now:")
    print()
    print("      /model opus")
    print()
    print("  Then paste:")
    print()
    print("      Read CLAUDE.md, AGENTS.md and logs/handoff-report.md.")
    print("      Collection is done. Work TODO.md phases 2 through 7.")
    print("      Record every finding in docs/FACTS.md with a source path, a grade")
    print("      and a date as you go. Run tools/verify.py before telling me")
    print("      anything is done.")
    print()
    print("=" * 72)


if __name__ == "__main__":
    main()
