#!/usr/bin/env python3
"""Run the whole capture and extraction pipeline. One command, unattended.

    python3 tools/run_all.py                 # everything not already done
    python3 tools/run_all.py --phase 1       # just the capture phase
    python3 tools/run_all.py --force         # redo steps whose output exists
    python3 tools/run_all.py --dry-run       # print the plan and stop

Design rules, because this runs without anyone watching:

  IDEMPOTENT. A step whose output already exists is skipped. Interrupt it, rerun it,
  lose nothing.

  OPTIONAL STEPS NEVER STOP THE RUN. crt.sh is down more often than it is up. A source
  that fails is recorded in logs/fetch-failures.md and the pipeline carries on - because
  a missing source is a finding to report, not a reason to abandon the analysis.

  REQUIRED STEPS DO STOP IT. If the sitemap cannot be read there is nothing downstream
  worth attempting, and continuing would produce a half-corpus that later looks whole.

  EVERY RUN LEAVES A REPORT at logs/run-status.md saying what ran, what was skipped,
  what failed, and what a human or agent should do next.
"""
import os
import subprocess
import sys
import time
from datetime import datetime

import config

PY = sys.executable or "python3"

# (phase, name, argv, required, output that proves it ran)
STEPS = [
    (1, "sitemaps",        ["tools/fetch_sitemap.py"],   True,  "data/site_inventory.csv"),
    (1, "sec facts",       ["tools/sec_facts.py"],       False, "data/financials.csv"),
    (1, "sec filings",     ["tools/sec_filings.py"],     False, "data/filings.csv"),
    (1, "status page",     ["tools/status_history.py"],  False, "data/incidents.csv"),
    (1, "github org",      ["tools/github_org.py"],      False, "data/repos.csv"),
    (1, "cert transparency", ["tools/ct_probe.py"],      False, "data/subdomains.csv"),
    (1, "careers board",   ["tools/careers_board.py"],  False, "data/careers_departments.csv"),

    (2, "filing documents", ["tools/fetch_filings.py"],  False, "sources/filings"),
    (2, "issue trackers",  ["tools/fetch_issues.py"],    False, "data/issues.csv"),
    (2, "documentation",   ["tools/fetch_docs.py"],      True,  "sources/docs"),

    (3, "index docs",      ["tools/index_docs.py"],      True,  "data/docs_index.csv"),
    (3, "api endpoints",   ["tools/extract_api.py"],     False, "data/api_endpoints.csv"),
    (3, "capabilities",    ["tools/capability_count.py"], True, "data/capabilities.csv"),
    (3, "review coding",   ["tools/code_reviews.py"],    False, "data/review_themes.csv"),
    (3, "timeline",        ["tools/build_timeline.py"],  True,  "data/timeline.csv"),

    (4, "build deck",      ["deck/build_deck.py"],       True,  None),
    (4, "build script",    ["deck/make_script.py"],      True,  None),
    (4, "build record",    ["deck/build_record.py"],     False, None),
    (4, "verify",          ["tools/verify.py"],          False, None),
    (4, "panel status",    ["tools/panels_status.py"],   False, None),
    (4, "handoff",         ["tools/handoff.py"],         False, None),
]

# Phase 4 steps declare no output file on purpose: the deck, the script and the record
# must be REBUILT every run, or a stale artefact silently survives a content change.
#
# The pipeline ENDS at the handoff gate. Phases 1-3 are collection - mechanical, long,
# and reversible. Everything after the gate is judgement, and wants a different model.
# See tools/handoff.py for why that boundary is drawn there.

PHASE_NAMES = {1: "capture — cheap, exhaustive, and mostly instant",
               2: "capture — the long fetches",
               3: "extract and measure",
               4: "check, and stop at the model gate"}


def exists(rel):
    if not rel:
        return False
    p = os.path.join(config.ROOT, rel)
    if os.path.isdir(p):
        return bool([f for f in os.listdir(p) if not f.startswith(".")])
    return os.path.exists(p)


def run(argv):
    t0 = time.time()
    try:
        r = subprocess.run([PY] + argv, cwd=config.ROOT, capture_output=True,
                           text=True, timeout=3600)
        return r.returncode, (r.stdout or "") + (r.stderr or ""), time.time() - t0
    except subprocess.TimeoutExpired:
        return 124, "timed out after 60 minutes", time.time() - t0


def main():
    args = sys.argv[1:]
    only = int(args[args.index("--phase") + 1]) if "--phase" in args else None
    force, dry = "--force" in args, "--dry-run" in args

    steps = [s for s in STEPS if only is None or s[0] == only]
    print("%s — pipeline\n%s" % (config.COMPANY, "=" * 64))
    if dry:
        for ph, name, argv, req, out in steps:
            state = "done" if exists(out) else "to run"
            print("  %d  %-18s %-28s %-9s %s"
                  % (ph, name, " ".join(argv), "required" if req else "optional", state))
        return

    results, phase = [], None
    for ph, name, argv, req, out in steps:
        if ph != phase:
            phase = ph
            print("\nPhase %d — %s\n%s" % (ph, PHASE_NAMES.get(ph, ""), "-" * 64))
        if exists(out) and not force:
            print("  · %-20s skipped (output exists)" % name)
            results.append((ph, name, "skipped", 0, ""))
            continue

        print("  → %-20s running…" % name, flush=True)
        code, log, secs = run(argv)
        tail = [l for l in log.strip().split("\n") if l.strip()][-1:] or [""]
        if code == 0:
            print("  ✓ %-20s %5.1fs  %s" % (name, secs, tail[0][:70]))
            results.append((ph, name, "ok", secs, tail[0][:120]))
        elif req:
            print("  ✗ %-20s FAILED (required) — stopping\n" % name)
            print(log[-1500:])
            results.append((ph, name, "FAILED", secs, tail[0][:200]))
            write_report(results, stopped=name)
            raise SystemExit(1)
        else:
            print("  ! %-20s failed (optional, continuing)  %s" % (name, tail[0][:60]))
            results.append((ph, name, "failed", secs, tail[0][:200]))

    write_report(results)


def write_report(results, stopped=None):
    os.makedirs(config.LOGS, exist_ok=True)
    p = os.path.join(config.LOGS, "run-status.md")
    ok = [r for r in results if r[2] == "ok"]
    bad = [r for r in results if r[2] in ("failed", "FAILED")]
    skip = [r for r in results if r[2] == "skipped"]

    lines = ["# Pipeline run — %s" % datetime.now().strftime("%Y-%m-%d %H:%M"), "",
             "%d ran, %d skipped, %d failed.%s"
             % (len(ok), len(skip), len(bad),
                "  **Stopped at a required step: %s**" % stopped if stopped else ""), "",
             "| phase | step | result | seconds | last line |", "|---|---|---|---|---|"]
    for ph, name, state, secs, tail in results:
        lines.append("| %d | %s | %s | %.0f | %s |"
                     % (ph, name, state, secs, tail.replace("|", "/")[:110]))

    lines += ["", "## What to do next", ""]
    if stopped:
        lines.append("A **required** step failed, so the run stopped. Nothing downstream "
                     "was attempted. Fix `%s` and rerun — completed steps are skipped." % stopped)
    elif bad:
        lines.append("Optional sources failed. Each is recorded in "
                     "`logs/fetch-failures.md`. Before the deliverable ships every one "
                     "needs an outcome: retried and succeeded, permanently unavailable "
                     "(then stated in the deck as an absence), or needs a human.")
        for _, name, _, _, tail in bad:
            lines.append("- **%s** — %s" % (name, tail[:150]))
    else:
        lines.append("Collection is complete. **Stop here and read "
                     "`logs/handoff-report.md`.** What follows is judgement rather than "
                     "throughput, and wants a more capable model — the report names the "
                     "decisions and carries the prompt to open the next session with.")

    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n%s\n%d ran · %d skipped · %d failed → logs/run-status.md"
          % ("=" * 64, len(ok), len(skip), len(bad)))
    if bad and not stopped:
        print("Optional sources failed; the pipeline continued. See logs/fetch-failures.md.")


if __name__ == "__main__":
    main()
