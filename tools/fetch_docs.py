#!/usr/bin/env python3
"""Fetch the documentation corpus -> sources/docs/*.md

Technical documentation is the single most valuable corpus in this method. It is
written for people who will hit the limits, so it is consistently more honest than
marketing: it has to describe the product that exists.

This is a POLITE, RESUMABLE crawler:
  - one request at a time with a delay, because there is no reason to be rude
  - skips any slug already on disk, so an interrupted run resumes for free
  - every failure is recorded in logs/fetch-failures.md rather than swallowed;
    a gap you know about is evidence, a gap you do not is a mistake

Each page is written with YAML frontmatter (url, title, description, fetched date,
section) so tools/index_docs.py can build an index without reading any body text.

Dependency-free by design - this must run on a bare Python 3.

Usage:  python3 tools/fetch_docs.py [--limit N] [--delay S] [--force]
"""
import html
import os
import re
import sys
import time
from datetime import date
from urllib.parse import urlparse

import config

DEST = os.path.join(config.SOURCES, "docs")
DROP = re.compile(r"<(script|style|nav|header|footer|svg|noscript|form|button)\b.*?</\1>",
                  re.S | re.I)
MAIN = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S | re.I)
FALLBACK = re.compile(r'<div[^>]*id="main_content"[^>]*>(.*?)</div>\s*</div>', re.S | re.I)


def text_of(fragment):
    """HTML -> readable markdown-ish text. Deliberately simple: this feeds counting
    and citation by line range, not rendering."""
    s = fragment
    s = DROP.sub(" ", s)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"<(h[1-6])[^>]*>(.*?)</\1>",
               lambda m: "\n\n" + "#" * int(m.group(1)[1]) + " " + m.group(2) + "\n", s, flags=re.S | re.I)
    s = re.sub(r"<li[^>]*>", "\n- ", s, flags=re.I)
    s = re.sub(r"<(p|div|tr|br)\b[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"</(td|th)>", " | ", s, flags=re.I)
    s = re.sub(r"<pre[^>]*>(.*?)</pre>",
               lambda m: "\n```\n" + re.sub(r"<[^>]+>", "", m.group(1)) + "\n```\n", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
    return s.strip()


def de_chrome(body):
    """Cut the navigation banner that sits above the page's own h1.

    -> (body, chrome). The chrome is returned, not discarded: repeated site furniture
    carries real claims ("trusted by N brands", certifications, the status banner) and
    is worth keeping once, in sources/boilerplate.txt. Keeping it on every page instead
    would make every later count wrong.
    """
    m = re.search(r"^# .+$", body, re.M)
    if not m or m.start() > 3000:        # no h1, or the page really does open with prose
        return body, ""
    return body[m.start():].strip(), body[:m.start()].strip()


def one(url, delay):
    raw = config.get(url, timeout=45, retries=2)
    doc = raw.decode("utf-8", "replace")
    m = MAIN.search(doc) or FALLBACK.search(doc)
    body, chrome = de_chrome(text_of(m.group(1) if m else doc))
    t = re.search(r"<h1[^>]*>(.*?)</h1>", doc, re.S | re.I)
    title = html.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip() if t else ""
    d = re.search(r'<meta name="description" content="(.*?)"', doc, re.S | re.I)
    desc = html.unescape(d.group(1)).strip().replace("\n", " ") if d else ""
    time.sleep(delay)
    return title, desc, body, chrome


def main():
    args = sys.argv[1:]
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else 0
    delay = float(args[args.index("--delay") + 1]) if "--delay" in args else 0.4
    force = "--force" in args

    inv = os.path.join(config.DATA, "site_inventory.csv")
    if not os.path.exists(inv):
        raise SystemExit("run tools/fetch_sitemap.py first - this reads data/site_inventory.csv")
    import csv
    urls = [r["url"] for r in csv.DictReader(open(inv))
            if "/docs" in urlparse(r["url"]).path]
    if not urls:
        raise SystemExit("no /docs URLs in the inventory; widen the filter in this script")

    os.makedirs(DEST, exist_ok=True)
    os.makedirs(config.LOGS, exist_ok=True)
    todo, skipped = [], 0
    for u in urls:
        slug = urlparse(u).path.strip("/").replace("/", "__") or "index"
        path = os.path.join(DEST, slug + ".md")
        if os.path.exists(path) and not force:
            skipped += 1
            continue
        todo.append((u, slug, path))
    if limit:
        todo = todo[:limit]

    print("%d docs in inventory | %d already on disk | fetching %d at %.1fs intervals"
          % (len(urls), skipped, len(todo), delay))
    if todo:
        print("estimated: %d min" % max(1, round(len(todo) * (delay + 0.6) / 60)))

    ok, fails = 0, []
    today = date.today().isoformat()
    for n, (u, slug, path) in enumerate(todo, 1):
        try:
            title, desc, body, chrome = one(u, delay)
        except RuntimeError as e:
            fails.append((u, str(e)[:160]))
            continue
        bp = os.path.join(config.SOURCES, "boilerplate.txt")
        if chrome and not os.path.exists(bp):
            with open(bp, "w", encoding="utf-8") as fh:
                fh.write("# Site furniture removed from every fetched page\n"
                         "# Captured once, from %s on %s.\n"
                         "# It repeats site-wide, so it is ONE claim, cited once - never N.\n\n%s\n"
                         % (u, today, chrome))
        parts = [x for x in urlparse(u).path.split("/") if x]
        fm = ["---",
              "url: %s" % u,
              "slug: %s" % slug,
              'title: "%s"' % title.replace('"', "'"),
              'description: "%s"' % desc[:300].replace('"', "'"),
              "section: %s" % ("/".join(parts[1:3]) if len(parts) > 1 else ""),
              "fetched: %s" % today,
              "evidence: company-own (technical)",
              "---", ""]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(fm) + body + "\n")
        ok += 1
        if n % 50 == 0 or n == len(todo):
            print("   %4d/%d  %s" % (n, len(todo), slug[:70]))

    if fails:
        p = os.path.join(config.LOGS, "fetch-failures.md")
        with open(p, "a", encoding="utf-8") as fh:
            fh.write("\n## docs fetch %s - %d failures of %d\n\n" % (today, len(fails), len(todo)))
            for u, e in fails:
                fh.write("- `%s` - %s\n" % (u, e))
        print("\n%d failures recorded in logs/fetch-failures.md" % len(fails))
        print("A gap you have written down is evidence. A gap you have not is a mistake.")

    total = len([f for f in os.listdir(DEST) if f.endswith(".md")])
    print("\nfetched %d | corpus now %d documents in sources/docs/" % (ok, total))
    print("next: python3 tools/index_docs.py")


if __name__ == "__main__":
    main()
