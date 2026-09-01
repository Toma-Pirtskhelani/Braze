#!/usr/bin/env python3
"""Sitemaps -> data/site_inventory.csv

The URL inventory is analysable before a single page is fetched. It answers, cheaply
and exhaustively:

  - how many pages exist per section, which is a rough map of what the company thinks
    it sells
  - which languages are published, which is a market-coverage signal that marketing
    copy will not give you straight
  - what is absent. "No page anywhere contains the word 'pricing'" is a finding, and
    an exhaustive one, because the sitemap is the company's own list of its pages.

Handles sitemap indexes (a sitemap of sitemaps) to one level, which is how localised
trees are usually published - one child sitemap per language.

Usage:  python3 tools/fetch_sitemap.py [url ...]     (defaults to the two in config)
"""
import csv
import re
import sys
from collections import Counter
from urllib.parse import urlparse

import config

LOC = re.compile(r"<loc>\s*(.*?)\s*</loc>", re.S)
MOD = re.compile(r"<lastmod>\s*(.*?)\s*</lastmod>", re.S)
ENTRY = re.compile(r"<(?:url|sitemap)>(.*?)</(?:url|sitemap)>", re.S)


def parse(xml):
    """-> (is_index, [(url, lastmod), ...])"""
    is_index = b"<sitemapindex" in xml[:2000]
    text = xml.decode("utf-8", "replace")
    out = []
    for block in ENTRY.findall(text):
        loc = LOC.search(block)
        if not loc:
            continue
        mod = MOD.search(block)
        out.append((loc.group(1), mod.group(1)[:10] if mod else ""))
    if not out:                                     # some sitemaps omit the wrappers
        out = [(u, "") for u in LOC.findall(text)]
    return is_index, out


def main():
    roots = sys.argv[1:] or [config.SITE_SITEMAP, config.DOCS_SITEMAP]
    rows, seen, fetched = [], set(), []

    queue = [(u, 0) for u in roots]
    while queue:
        url, depth = queue.pop(0)
        try:
            xml = config.get(url, timeout=60)
        except RuntimeError as e:
            print("  ! %s: %s" % (url, e))
            continue
        is_index, entries = parse(xml)
        fetched.append(url)
        print("%s%s  %s  %d entries"
              % ("  " * depth, "index" if is_index else "urls ", url, len(entries)))
        if is_index and depth < 2:
            queue += [(u, depth + 1) for u, _ in entries]
            continue
        for u, mod in entries:
            if u in seen:
                continue
            seen.add(u)
            p = urlparse(u)
            parts = [x for x in p.path.split("/") if x]
            rows.append({
                "url": u,
                "host": p.netloc,
                "section": parts[0] if parts else "(root)",
                "subsection": parts[1] if len(parts) > 1 else "",
                "depth": len(parts),
                "slug": parts[-1] if parts else "",
                "lastmod": mod,
                "from_sitemap": url,
                "evidence": "company-own (site inventory)",
            })

    if not rows:
        raise SystemExit("no URLs parsed - check the sitemap addresses in tools/config.py")

    rows.sort(key=lambda r: r["url"])
    with open(config.out("site_inventory.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("\n%d distinct URLs from %d sitemaps" % (len(rows), len(fetched)))
    print("\nby section:")
    for s, c in Counter(r["section"] for r in rows).most_common(18):
        print("   %-32s %5d" % (s, c))
    mods = sorted(r["lastmod"] for r in rows if r["lastmod"])
    if mods:
        print("\nlastmod range: %s .. %s  (%d of %d URLs carry one)"
              % (mods[0], mods[-1], len(mods), len(rows)))
        print("NOTE: lastmod is company-set and often a build timestamp rather than an")
        print("      edit date. Treat it as weak evidence and prefer CT logs or VCS.")
    print("\nwrote data/site_inventory.csv")


if __name__ == "__main__":
    main()
