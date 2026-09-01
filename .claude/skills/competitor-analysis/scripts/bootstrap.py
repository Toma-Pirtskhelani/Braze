#!/usr/bin/env python3
"""Scaffold a competitor-analysis repository for a new vendor.

Creates the directory structure, the invariants, and a tools/config.py to fill in. If
run from inside a repository that already carries the toolkit, the extractors are copied
across rather than re-derived - index_docs.py on a thousand-page corpus is the single
highest-return script in the method and nobody should write it twice.

Usage:
    python3 bootstrap.py <Vendor Name> <domain> [target-dir]

Example:
    python3 bootstrap.py "Klaviyo" klaviyo.com ~/Klaviyo
"""
import os
import shutil
import sys

DIRS = [
    "sources/raw", "sources/clean", "sources/docs", "sources/panels",
    "sources/external", "sources/ai-sessions", "sources/media",
    "data", "docs", "deck", "tools", "logs", "dist",
]

TOOLKIT = ["config.py", "fetch_sitemap.py", "fetch_docs.py", "index_docs.py",
           "capability_count.py", "code_reviews.py", "build_timeline.py",
           "ct_probe.py", "status_history.py", "github_org.py",
           "sec_facts.py", "sec_filings.py", "make_release.sh",
           "typography_audit.js"]

# slides_a.py is NOT copied: the source repo's title slide carries that vendor's own
# source counts, and copying them into a new repo is exactly the kind of half-remembered
# fact this scaffold exists to keep out. A vendor-neutral one is written instead.
DECK = ["lib.py", "css.py", "icons.py", "build_deck.py", "make_script.py"]

CONFIG = '''# -*- coding: utf-8 -*-
"""The one place the subject company is named.

Every script in tools/ imports from here, so pointing this toolkit at a different
vendor is a single-file change. Nothing in this file is a finding: it is a set of
addresses. VERIFY EACH ONE before relying on it, and record what you found in
docs/SOURCES.md with the date.
"""
import os

COMPANY = "{company}"
SHORT = "{short}"

# SEC EDGAR - find the CIK at https://www.sec.gov/files/company_tickers.json
# Leave blank if the vendor is not US-listed; the sec_*.py tools will say so.
CIK = ""
TICKER = ""

# Fiscal year end as (month, day). CHECK THIS against the 10-K cover page - many SaaS
# companies do not close in December, and getting it wrong mislabels every period.
FY_END = (12, 31)

DOMAIN = "{domain}"
DOCS_SITEMAP = "https://{domain}/docs/sitemap.xml"      # VERIFY
SITE_SITEMAP = "https://{domain}/sitemap.xml"           # VERIFY

GITHUB_ORG = ""                                          # VERIFY, may not exist
STATUSPAGE = ""                                          # e.g. https://x.statuspage.io

# Deck identity, so the company is named in exactly one file
DECK_TITLE = "%s Analysis" % SHORT
DECK_FILE = "%s-deck.html" % SHORT.lower().replace(" ", "-")

SEC_CONTACT = os.environ.get("SEC_CONTACT", "research you@example.com")
UA = os.environ.get("RESEARCH_UA", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SOURCES = os.path.join(ROOT, "sources")
LOGS = os.path.join(ROOT, "logs")


def out(name):
    os.makedirs(DATA, exist_ok=True)
    return os.path.join(DATA, name)


def get(url, contact=False, timeout=60, retries=3):
    """One polite GET. Returns bytes. Retries on transient failure."""
    import time
    import urllib.request
    hdr = {{"User-Agent": SEC_CONTACT if contact else UA,
           "Accept-Encoding": "gzip, deflate"}}
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdr)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    import gzip
                    raw = gzip.decompress(raw)
                return raw
        except Exception as e:            # noqa: BLE001 - report and retry
            last = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("GET failed after %d tries: %s (%s)" % (retries, url, last))
'''

README = """# {company} — competitor analysis environment

A research environment, not yet a research result. **No findings about {company} live
here yet, deliberately** — a scaffold pre-loaded with half-remembered facts is worse
than an empty one, because a later run will trust them.

## Set up

```bash
export SEC_CONTACT="your name your@email"
python3 deck/build_deck.py            # sanity check
```

## First things to do

1. Fill in `tools/config.py` — CIK, sitemaps, GitHub org, status page. **Verify each.**
2. Work through `TODO.md`.
3. Record what each source actually returned, with the date, in `docs/SOURCES.md`.

## The invariant

`sources/` is immutable. `data/` is CSV only and only what a script can regenerate.
`docs/` is written by a person. That is what lets anyone trust a number in `data/`
without re-deriving it.
"""

SLIDES_A = '''# -*- coding: utf-8 -*-
"""Part 0 - the frame.

These slides carry no findings. They are the method, and they are correct before any
research has been done, which is why they ship with the scaffold.

Everything after this file is written by the research run. Add slides_b.py, slides_c.py
and so on; deck/build_deck.py discovers them automatically, in filename order. The
component vocabulary is in deck/lib.py - read it before inventing a new layout.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *                                   # noqa: F403,E402

# The source strip is an inventory of what was READ, not of what was found. Fill it in
# once the capture has run, with counts that are re-checkable in one command.
SOURCES = [("Their documentation", "&mdash;"), ("Their site inventory", "&mdash;"),
           ("Filings", "&mdash;"), ("Public code", "&mdash;"),
           ("Review panels", "&mdash;"), ("Infrastructure", "&mdash;")]
_src = "".join(f\'<div class="srcitem"><div class="sn">{{n}}</div><div class="sv">{{v}}</div></div>\'
               for n, v in SOURCES)

add(f\'\'\'<section class="s title-s" data-g="s" data-t="Competitor Analysis">
  <h1>{short}</h1>
  <div class="subject">Competitor analysis</div>
  <p class="lede">&mdash;</p>
  <div class="srcstrip">{{_src}}</div>
  <div class="byline"><span><strong>&mdash;</strong></span><span>Public sources only &middot; &mdash;</span></div>
</section>\'\'\',
"""This is a competitor analysis of **{company}**.

[Write this note once the research is done.]

Everything here comes from sources you can check yourself. No press release is taken at
face value. Where their marketing and their own documentation disagree, I will show you
both.""",
    "s", "Competitor Analysis")

add(f\'\'\'<section class="s" data-g="s" data-t="How we approach it">
  {{head("Method &middot; how this is built", "How we approach it")}}
  <div class="body">
    {{flow([("PART I", "The company", "who owns it &middot; what it costs &middot; who buys it"),
           ("PART II", "The product", "one campaign, stage by stage"),
           ("PART III", "Strategy", "where the money goes &middot; what protects them"),
           ("PART IV", "Open questions", "what public sources cannot answer")])}}
    <div class="ruleband">
      <div class="klabel">AND THREE RULES THAT APPLY TO ALL FOUR</div>
      {{cards([("Every claim is graded",
               "Marked by how strong its source is. The bar at the foot of each slide shows where we are.", "g"),
              ("Marketing is labelled as marketing",
               "Their own words appear &mdash; but never as evidence.", "a"),
              ("Gaps become a backlog",
               "Anything needing a non-public source goes on the open-questions list.", "r")],
             cols=3)}}
    </div>
  </div>
</section>\'\'\',
"""Four parts. **Who the company is. How the product actually works. Where the strategy
is going. And what we still cannot answer.**

One rule runs through all of it: every claim is graded by how strong its source is.""",
    "s", "How we approach it")
'''

TODO = """# TODO — {company}

## Phase 0 · Setup
- [ ] Fill in `tools/config.py` and verify every address in it
- [ ] Find the CIK (or confirm the vendor is not US-listed)
- [ ] Confirm whether a public GitHub org and a status page exist

## Phase 1 · Capture
- [ ] `python3 tools/fetch_sitemap.py`
- [ ] `python3 tools/sec_facts.py` and `sec_filings.py`  *(if listed)*
- [ ] `python3 tools/status_history.py`  *(if a status page exists)*
- [ ] `python3 tools/github_org.py`  *(if a public org exists)*
- [ ] `python3 tools/ct_probe.py`
- [ ] `python3 tools/fetch_docs.py`
- [ ] Panels — browser session or paste; capture date on line 1 of each file
- [ ] Every failure written into `logs/fetch-failures.md`

## Phase 2 · Index
- [ ] `python3 tools/index_docs.py`
- [ ] Revise `docs/CAPABILITY-TAXONOMY.tsv` with the vendor's own vocabulary
- [ ] `python3 tools/capability_count.py`
- [ ] `python3 tools/build_timeline.py`

## Phases 3-7
See the `competitor-analysis` skill. Read the documentation not the marketing, go to the
records they do not control, count before you read, triangulate, then build the deck and
the record.
"""


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    company, domain = sys.argv[1], sys.argv[2].replace("https://", "").strip("/")
    short = company.split()[0].rstrip(",")
    target = os.path.abspath(sys.argv[3] if len(sys.argv) > 3 else os.path.join(".", short))

    if os.path.exists(target) and os.listdir(target):
        raise SystemExit("%s exists and is not empty - refusing to scaffold over it" % target)

    for d in DIRS:
        os.makedirs(os.path.join(target, d), exist_ok=True)
        open(os.path.join(target, d, ".gitkeep"), "w").close()

    with open(os.path.join(target, "tools", "config.py"), "w") as fh:
        fh.write(CONFIG.format(company=company, short=short, domain=domain))
    for name, body in (("README.md", README), ("TODO.md", TODO)):
        with open(os.path.join(target, name), "w") as fh:
            fh.write(body.format(company=company))
    with open(os.path.join(target, "deck", "slides_a.py"), "w") as fh:
        fh.write(SLIDES_A.format(company=company, short=short))

    # copy the toolkit from the repo this skill is installed in, if it is there
    here = os.path.dirname(os.path.abspath(__file__))
    src_repo = os.path.abspath(os.path.join(here, "..", "..", "..", ".."))
    copied = []
    for sub, names in (("tools", TOOLKIT), ("deck", DECK), ("docs", ["CAPABILITY-TAXONOMY.tsv"])):
        for n in names:
            s = os.path.join(src_repo, sub, n)
            if os.path.exists(s) and not os.path.exists(os.path.join(target, sub, n)):
                shutil.copy2(s, os.path.join(target, sub, n))
                copied.append("%s/%s" % (sub, n))

    print("scaffolded %s at %s" % (company, target))
    print("directories: %d" % len(DIRS))
    if copied:
        print("toolkit copied (%d files): %s" % (len(copied), ", ".join(copied[:6]) + " ..."))
        print("\nNOTE: tools/config.py was written fresh for %s. The copied extractors\n"
              "      read from it, so fill it in and VERIFY every address first." % short)
    else:
        print("no toolkit found to copy - write the extractors, or clone a repository\n"
              "that already has them and replace tools/config.py")
    print("\nnext: cd %s && cat TODO.md" % target)


if __name__ == "__main__":
    main()
