#!/usr/bin/env python3
"""Review corpus -> data/review_coding.csv and data/review_themes.csv

Why this is a script and not a reading exercise:

On the reference project the same 102 review answers were coded three times by hand
and produced three different sets of percentages. Reconciling them cost more than the
counting did. The lesson is in docs/METHOD.md and it is absolute:

    LOCK THE PATTERN SET IN A SCRIPT, AND CITE THE SCRIPT RATHER THAN THE NUMBER.

Anyone can rerun this and get the same percentages. If they disagree with a theme,
they can see exactly which regex produced it and argue with that instead of with you.

Input: any .txt/.md file under sources/panels/. Review sites block scripted access
(G2, Gartner, Glassdoor and TrustRadius all returned 403 during setup), so these
files are captured by a human or through a real browser session and pasted in.
Record the capture date at the top of each file.

Usage:  python3 tools/code_reviews.py [--split PATTERN]
        --split sets the record separator; the default splits on blank-line groups.
"""
import csv
import os
import re
import sys
from collections import Counter

import config

PANELS = os.path.join(config.SOURCES, "panels")

# Themes are intentionally coarse and few. A long tail of rare themes reads as
# precision and is not: with a hundred-odd records, anything under ~5% is noise.
COMPLAINT = [
    ("learning curve",      r"learning curve|steep|hard to learn|takes time to (learn|master)|not intuitive|complex(ity)? to (use|learn)"),
    ("implementation",      r"implement|onboard|set.?up (was|is) |integration (was|is) (hard|difficult)|migrat"),
    ("segmentation",        r"segment\w* (is|are|was|can be)? ?(slow|clunky|limited|confusing|painful)|building (a )?segment"),
    ("reporting / export",  r"report\w*|export|dashboard|analytics (is|are|was) (limited|lacking|basic)"),
    ("templates / editor",  r"templat|drag.and.drop|editor (is|was) |wysiwyg"),
    ("speed / performance", r"\bslow\b|lag|latency|takes (ages|forever)|performance (issue|problem)"),
    ("feature gaps",        r"missing|lack\w*|wish (it|they)|would like to see|no (native )?support for|limitation"),
    ("documentation",       r"document\w*|help (article|center)|knowledge base|\bdocs\b"),
    ("price / cost",        r"\bpric\w*|\bcost\w*|expensive|budget|\bbilling\b|contract value"),
    ("support",             r"support[^.]{0,40}(slow|unresponsive|poor|useless|no help)|response time|ticket"),
    ("bugs / reliability",  r"\bbug\b|broke|outage|downtime|unreliable|glitch"),
]

PRAISE = [
    ("ease of use",         r"easy to use|intuitive|user.friendly|simple to"),
    ("support",             r"support[^.]{0,40}(great|excellent|amazing|responsive|helpful|fantastic|top.notch)|customer success|\bcsm\b"),
    ("orchestration",       r"canvas|journey|orchestrat|workflow"),
    ("channels / reach",    r"multi.?channel|omni.?channel|all channels|channel (breadth|coverage)"),
    ("segmentation power",  r"segment\w* (is|are) (powerful|flexible|granular|easy)"),
    ("personalisation",     r"personali[sz]|liquid|dynamic content"),
    ("analytics",           r"analytic|report\w* (is|are) (great|powerful|useful)|insight"),
    ("integrations",        r"integrat\w* (is|are|was) (easy|seamless|great)|connects? (well|easily)"),
    ("reliability",         r"reliab|stable|uptime|never (goes )?down"),
    ("AI features",         r"\bai\b|machine learning|predictive|recommend"),
]

RATING = re.compile(r"\b([0-5](?:\.\d)?)\s*(?:/|out of)\s*5|\b([0-5](?:\.\d)?)\s*stars?\b", re.I)
SIZE = re.compile(r"\b(enterprise|mid.?market|small.?business|\bsmb\b)\b", re.I)


def records(text, splitter):
    chunks = [c.strip() for c in re.split(splitter, text) if c.strip()]
    return [c for c in chunks if len(c) > 60]       # drop nav fragments and headers


def main():
    args = sys.argv[1:]
    splitter = args[args.index("--split") + 1] if "--split" in args else r"\n\s*\n\s*\n+"

    if not os.path.isdir(PANELS):
        raise SystemExit("sources/panels/ does not exist")
    files = [f for f in sorted(os.listdir(PANELS)) if f.endswith((".txt", ".md"))]
    if not files:
        raise SystemExit(
            "sources/panels/ is empty.\n"
            "Review sites block scripted access - capture G2 / Gartner Peer Insights /\n"
            "TrustRadius / Glassdoor through a real browser session, save the text into\n"
            "sources/panels/<site>.txt with a capture date at the top, then rerun.")

    rows = []
    for fn in files:
        text = open(os.path.join(PANELS, fn), encoding="utf-8", errors="replace").read()
        panel = os.path.splitext(fn)[0]
        for i, rec in enumerate(records(text, splitter), 1):
            low = rec.lower()
            rm = RATING.search(rec)
            sm = SIZE.search(rec)
            comp = [n for n, p in COMPLAINT if re.search(p, low)]
            prai = [n for n, p in PRAISE if re.search(p, low)]
            rows.append({
                "panel": panel,
                "record": i,
                "chars": len(rec),
                "rating": (rm.group(1) or rm.group(2)) if rm else "",
                "segment": (sm.group(1).lower().replace("-", " ") if sm else ""),
                "complaints": "|".join(comp),
                "praise": "|".join(prai),
                "evidence": "third-party (review panel)",
            })

    with open(config.out("review_coding.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    theme_rows = []
    for kind, table in (("complaint", COMPLAINT), ("praise", PRAISE)):
        col = "complaints" if kind == "complaint" else "praise"
        counts = Counter(t for r in rows for t in r[col].split("|") if t)
        for name, _ in table:
            c = counts.get(name, 0)
            theme_rows.append({"kind": kind, "theme": name, "records": c,
                               "pct_of_records": round(100.0 * c / n, 1),
                               "denominator": n, "evidence": "third-party (review panel)"})
    theme_rows.sort(key=lambda r: (r["kind"], -r["records"]))
    with open(config.out("review_themes.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(theme_rows[0].keys()))
        w.writeheader()
        w.writerows(theme_rows)

    print("panels: %s" % ", ".join(files))
    print("records coded: %d\n" % n)
    for kind in ("complaint", "praise"):
        print("%s themes:" % kind)
        for r in [t for t in theme_rows if t["kind"] == kind][:11]:
            bar = "#" * int(r["pct_of_records"] / 2)
            print("   %-22s %4d  %5.1f%%  %s" % (r["theme"], r["records"], r["pct_of_records"], bar))
        print()
    ratings = [float(r["rating"]) for r in rows if r["rating"]]
    if ratings:
        print("ratings parsed: %d | mean %.2f" % (len(ratings), sum(ratings) / len(ratings)))
    print("""
READ THIS BEFORE QUOTING A PERCENTAGE
  - the denominator is RECORDS PARSED (%d), never the site's total review count.
    Say "of the %d reviews captured", not "of all reviews". They are different
    numbers and merging them is the most common error in review analysis.
  - a review panel is self-selected and vendors solicit reviews. Independent of the
    vendor's marketing, but not disinterested.
  - one record can carry several themes; percentages therefore sum above 100.

wrote data/review_coding.csv, data/review_themes.csv""" % (n, n))


if __name__ == "__main__":
    main()
