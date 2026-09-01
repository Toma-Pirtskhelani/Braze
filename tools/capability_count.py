#!/usr/bin/env python3
"""Measure what a vendor actually ships -> data/capabilities.csv

THE CENTRAL MEASUREMENT OF THIS METHOD.

Marketing tells you what a company wants to be true. Documentation volume tells you
what it has to support. Nobody writes five hundred pages for a feature that does not
exist, and nobody writes fifteen for the thing they renamed the company around unless
it is newer and thinner than the renaming implies.

The FOCUSED-PAGE TEST is what makes the number defensible:

    a page counts for a capability only if the capability's vocabulary appears
    at least MIN_MENTIONS (default 5) times in its body

That threshold is deliberately strict. It separates "mentions email" from "is about
email", and without it every page that carries a nav menu counts for everything. The
resulting ratio survives challenge because anyone can rerun this script and get it.

Read the caveats printed at the end before quoting anything from here.

Taxonomy lives in docs/CAPABILITY-TAXONOMY.tsv so it can be revised as you learn the
vendor's own vocabulary - which you will, and should, after the first pass.

Usage:  python3 tools/capability_count.py [--min N]
"""
import csv
import os
import re
import sys

import config

TAX = os.path.join(config.ROOT, "docs", "CAPABILITY-TAXONOMY.tsv")
MIN_MENTIONS = 5


def load_taxonomy():
    if not os.path.exists(TAX):
        raise SystemExit("missing %s - it defines what to count" % TAX)
    out = []
    for line in open(TAX, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        out.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
    return out


def main():
    args = sys.argv[1:]
    minm = int(args[args.index("--min") + 1]) if "--min" in args else MIN_MENTIONS

    idx = os.path.join(config.DATA, "docs_index.csv")
    if not os.path.exists(idx):
        raise SystemExit("run tools/index_docs.py first")
    docs = list(csv.DictReader(open(idx)))
    src = os.path.join(config.SOURCES, "docs")

    api_path = os.path.join(config.DATA, "api_endpoints.csv")
    api = list(csv.DictReader(open(api_path))) if os.path.exists(api_path) else []

    bodies = {}
    for d in docs:
        p = os.path.join(src, d["file"])
        bodies[d["slug"]] = open(p, encoding="utf-8", errors="replace").read().lower()

    rows = []
    for group, name, pattern in load_taxonomy():
        rx = re.compile(pattern, re.I)
        focused, mentioned, total_hits = [], 0, 0
        for d in docs:
            hits = len(rx.findall(bodies[d["slug"]]))
            if hits:
                mentioned += 1
                total_hits += hits
            if hits >= minm:
                focused.append(d)
        eps = [a for a in api if any(rx.search(a.get(k, "") or "")
                                     for k in ("group", "name", "url", "path"))]
        rows.append({
            "group": group,
            "capability": name,
            "focused_pages": len(focused),
            "pages_mentioning": mentioned,
            "total_mentions": total_hits,
            "api_endpoints": len(eps),
            "share_of_corpus_pct": round(100.0 * len(focused) / max(1, len(docs)), 2),
            "example_slugs": " ".join(d["slug"] for d in
                                      sorted(focused, key=lambda d: -int(d["words"]))[:3]),
            "pattern": pattern,
            "evidence": "company-own (technical), measured",
        })

    rows.sort(key=lambda r: -r["focused_pages"])
    with open(config.out("capabilities.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("corpus: %d documents | focused threshold: >=%d mentions in the body\n"
          % (len(docs), minm))
    print("  %-34s %7s %8s %6s" % ("capability", "focused", "mentions", "eps"))
    for r in rows:
        print("  %-34s %7d %8d %6s"
              % (r["capability"][:34], r["focused_pages"], r["total_mentions"],
                 r["api_endpoints"] if api else "-"))
    if not api:
        print("\n  (no data/api_endpoints.csv yet - endpoint counts are the second lens;")
        print("   capture the API reference and the numbers above get much stronger)")

    print("""
BEFORE YOU QUOTE ANY OF THIS
  - it measures DOCUMENTATION, not capability. A thin section can mean an immature
    feature or a simple one. Say which you think it is, and why.
  - a new feature is under-documented by construction. Date the corpus and check the
    release notes before reading thinness as weakness.
  - the pattern set is a judgement. It is in docs/CAPABILITY-TAXONOMY.tsv and in the
    CSV's `pattern` column precisely so a reader can disagree with it.
  - the finding is only strong when a SECOND, independent lens agrees - published API
    surface, the words customers use in reviews, or analyst coverage counts.

wrote data/capabilities.csv""")


if __name__ == "__main__":
    main()
