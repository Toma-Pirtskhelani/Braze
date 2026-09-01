#!/usr/bin/env python3
"""sources/docs/*.md -> data/docs_index.csv and data/docs_sections.csv

Build the index BEFORE reading anything. On the reference project this one script was
the highest-return hour of the whole method: it turns "where is X discussed?" from a
grep over tens of megabytes into a lookup, and it lets you find a document by what it
IS rather than by what words it happens to contain.

Reads frontmatter and a bounded structural scan of each body - headings, code blocks,
tables, links, byte counts. Never the whole body into memory for analysis.

Usage:  python3 tools/index_docs.py
"""
import csv
import os
import re
from collections import Counter

import config

SRC = os.path.join(config.SOURCES, "docs")
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def frontmatter(text):
    m = FM.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).split("\n"):
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip().strip("\"'")
    return out


def main():
    names = sorted(f for f in os.listdir(SRC) if f.endswith(".md")) if os.path.isdir(SRC) else []
    if not names:
        raise SystemExit("sources/docs/ holds no .md files - run tools/fetch_docs.py first")

    rows = []
    for fn in names:
        raw = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read()
        fm = frontmatter(raw)
        body = FM.sub("", raw, count=1)
        heads = re.findall(r"^(#{1,6}) +(.+)$", body, re.M)
        rows.append({
            "slug": fm.get("slug", fn[:-3]),
            "file": fn,
            "title": fm.get("title", ""),
            "description": fm.get("description", "")[:300],
            "section": fm.get("section", ""),
            "url": fm.get("url", ""),
            "fetched": fm.get("fetched", ""),
            "bytes": len(raw.encode()),
            "body_bytes": len(body.encode()),
            "words": len(re.findall(r"\w+", body)),
            "headings": len(heads),
            "h2s": sum(1 for h, _ in heads if len(h) == 2),
            "code_blocks": body.count("```") // 2,
            "tables": body.count(" | "),
            "links": len(re.findall(r"https?://", body)),
            "evidence": fm.get("evidence", "company-own (technical)"),
        })

    if not rows:
        raise SystemExit("no .md files parsed in sources/docs/")

    with open(config.out("docs_index.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    sec = Counter(r["section"].split("/")[0] for r in rows)
    with open(config.out("docs_sections.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["section", "docs", "words", "code_blocks"])
        for s in sorted(sec, key=lambda s: -sec[s]):
            grp = [r for r in rows if r["section"].split("/")[0] == s]
            w.writerow([s, len(grp), sum(r["words"] for r in grp),
                        sum(r["code_blocks"] for r in grp)])

    print("documents: {:,} | words: {:,}".format(len(rows), sum(r["words"] for r in rows)))
    print("code blocks: %d | tables (cells): %d"
          % (sum(r["code_blocks"] for r in rows), sum(r["tables"] for r in rows)))
    print("\ntop sections by document count:")
    for s, c in sec.most_common(20):
        words = sum(r["words"] for r in rows if r["section"].split("/")[0] == s)
        print("   %-34s %5d docs  %8d words" % (s or "(none)", c, words))
    print("\nwrote data/docs_index.csv, data/docs_sections.csv")
    print("next: python3 tools/capability_count.py")


if __name__ == "__main__":
    main()
