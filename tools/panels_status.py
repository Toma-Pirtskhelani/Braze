#!/usr/bin/env python3
"""Which review panels are captured, and what to do about the ones that are not.

    python3 tools/panels_status.py

THE ESCALATION LADDER. Review sites block scripted access, so every panel goes through
three tiers in order. Never skip a tier, and never stop at one without recording why.

  TIER 1 — script.  Already attempted and it fails: G2, Gartner Peer Insights,
           TrustRadius and Glassdoor all returned HTTP 403 on 2026-09-01. Do not spend
           time here.

  TIER 2 — the operator's own browser.  The claude-in-chrome tools drive a real Chrome
           session that is already signed in. This works where a script cannot, because
           it is a real browser with real cookies. Read the page, save the text into the
           paste target, set status: captured.

  TIER 3 — ask the operator to paste.  The targets in sources/panels/ already exist and
           say exactly what to capture. Ask once, clearly, naming the files. Then carry
           on with everything that does not depend on panels rather than blocking.

If a panel never arrives, that is not a failure — it is an absence, and an absence gets
stated in the deck with what it would have told you. What is NOT acceptable is a panel
that is quietly missing and never mentioned.
"""
import os
import re
import sys

import config

PANELS = os.path.join(config.SOURCES, "panels")
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
MARK = "PASTE BELOW THIS LINE"


def read_state(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    m = FM.match(raw)
    meta = {}
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    body = raw.split(MARK, 1)[1] if MARK in raw else FM.sub("", raw, count=1)
    words = len(body.split())
    empty = meta.get("status", "").upper().startswith("EMPTY") or words < 50
    return meta, words, empty


def main():
    if not os.path.isdir(PANELS):
        raise SystemExit("sources/panels/ does not exist")
    files = sorted(f for f in os.listdir(PANELS) if f.endswith((".md", ".txt")))
    if not files:
        raise SystemExit("sources/panels/ is empty - the paste targets are missing")

    captured, waiting = [], []
    print("%-26s %-10s %8s  %s" % ("panel", "status", "words", "source"))
    print("-" * 78)
    for f in files:
        p = os.path.join(PANELS, f)
        meta, words, empty = read_state(p)
        name = meta.get("panel", f)
        (waiting if empty else captured).append((f, name, meta))
        print("%-26s %-10s %8d  %s"
              % (name[:26], "waiting" if empty else "captured", words,
                 (meta.get("url") or "-")[:34]))

    print("-" * 78)
    print("%d captured, %d waiting\n" % (len(captured), len(waiting)))

    if not waiting:
        print("All panels captured. Run: python3 tools/code_reviews.py")
        return

    print("STILL WAITING — work the ladder in order:\n")
    print("  TIER 2 · your browser. For each panel below, open its url with the")
    print("           claude-in-chrome tools, read the page, and write the review text")
    print("           into the file between the PASTE line and the end. Then set")
    print("           status: captured and fill in captured: with today's date.\n")
    for f, name, meta in waiting:
        print("             sources/panels/%-18s %s" % (f, meta.get("url", "")))
    print("\n  TIER 3 · ask the operator, once, naming the files above. Say what each")
    print("           one would add. Then CONTINUE with everything that does not")
    print("           depend on panels - do not block the run waiting for a paste.\n")
    print("  If a panel never arrives it becomes an ABSENCE, stated in the deck with")
    print("  what it would have told you. `fetch_issues.py` already covers the")
    print("  customer-voice requirement, so no panel is load-bearing on its own.\n")
    print("  Gartner is the one most worth chasing: its shortlists say who buyers")
    print("  actually compared this vendor against, and no other source has that.")
    if waiting and "--strict" in sys.argv:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
