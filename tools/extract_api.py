#!/usr/bin/env python3
"""API reference pages -> data/api_endpoints.csv

THE SECOND LENS ON CAPABILITY, and the one that makes the first defensible.

Documentation volume tells you what a vendor has to support. The published API surface
tells you what a customer can actually build on. A capability with substantial
documentation and **zero dedicated endpoints** is a capability you cannot automate
against - and that gap, where it exists, is usually the sharpest single line in the
whole analysis.

The two lenses are independent: docs are written by technical writers, the API surface
by engineers. Neither is derived from the other, which is exactly what makes them
corroborating rather than circular.

Reads the already-fetched corpus - no network. Verified 2026-09-01: 200 of the 1,352
documentation URLs sit under /docs/api.

Usage:  python3 tools/extract_api.py
"""
import csv
import os
import re
from collections import Counter

import config

SRC = os.path.join(config.SOURCES, "docs")
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

# An endpoint line in Braze-style docs reads "GET /users/export/ids" or is given as a
# fenced request. Both are matched; anything else is left alone rather than guessed at.
VERB = r"(GET|POST|PUT|PATCH|DELETE)"
INLINE = re.compile(r"\b%s\s+(/[A-Za-z0-9_\-/{}.:]+)" % VERB)
HOSTED = re.compile(r"https?://([A-Za-z0-9.\-]+)(/[A-Za-z0-9_\-/{}.:]+)")


def frontmatter(text):
    m = FM.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip("\"'")
    return out


def main():
    if not os.path.isdir(SRC):
        raise SystemExit("sources/docs/ does not exist - run tools/fetch_docs.py first")
    names = sorted(f for f in os.listdir(SRC) if f.endswith(".md"))
    if not names:
        raise SystemExit("sources/docs/ holds no .md files - run tools/fetch_docs.py first")

    seen, rows = set(), []
    api_pages = 0
    for fn in names:
        raw = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read()
        fm = frontmatter(raw)
        url = fm.get("url", "")
        if "/api" not in url and "/api" not in fn:
            continue
        api_pages += 1
        body = FM.sub("", raw, count=1)
        group = fm.get("section", "").split("/")[0] or "api"

        for verb, path in INLINE.findall(body):
            key = (verb, path)
            if key in seen or len(path) < 3:
                continue
            seen.add(key)
            rows.append({
                "method": verb,
                "path": path,
                "host": "",
                "group": group,
                "name": fm.get("title", ""),
                "url": url,
                "doc_slug": fm.get("slug", fn[:-3]),
                "evidence": "documented (published API reference)",
            })
        for host, path in HOSTED.findall(body):
            if "rest" not in host and "api" not in host:
                continue
            key = ("", host + path)
            if key in seen:
                continue
            seen.add(key)
            rows.append({
                "method": "", "path": path, "host": host, "group": group,
                "name": fm.get("title", ""), "url": url,
                "doc_slug": fm.get("slug", fn[:-3]),
                "evidence": "documented (published API reference)",
            })

    if not rows:
        raise SystemExit(
            "no endpoints matched across %d API pages.\n"
            "The pattern set at the top of this script assumes 'VERB /path' notation.\n"
            "Open one API page, see how requests are written, and adjust - then say in\n"
            "the record that the count came from a pattern you can show." % api_pages)

    rows.sort(key=lambda r: (r["group"], r["path"]))
    with open(config.out("api_endpoints.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    paths = {r["path"] for r in rows}
    print("API pages read: %d" % api_pages)
    print("endpoint rows: %d | distinct paths: %d | distinct hosts: %d"
          % (len(rows), len(paths), len({r["host"] for r in rows if r["host"]})))
    print("\nby method:")
    for m, c in Counter(r["method"] or "(unversioned)" for r in rows).most_common():
        print("   %-14s %4d" % (m, c))
    print("\nby documentation group:")
    for g, c in Counter(r["group"] for r in rows).most_common(12):
        print("   %-30s %4d" % (g, c))
    print("""
BEFORE QUOTING THE COUNT
  - say whether you are quoting ROWS or DISTINCT PATHS. They differ, and quoting the
    larger one without saying which is how an endpoint count gets challenged.
  - an undocumented endpoint is still an endpoint. This counts the PUBLISHED surface,
    which is the right measure for "what can a customer build on", not for "what
    exists".
  - now rerun tools/capability_count.py: it picks this file up automatically and the
    capability table gains its second lens.

wrote data/api_endpoints.csv""")


if __name__ == "__main__":
    main()
