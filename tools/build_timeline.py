#!/usr/bin/env python3
"""Every dated row in data/ -> data/timeline.csv

One chronology, assembled from sources that were captured independently. Its value is
not the list: it is that events from different evidence classes land side by side, so
a gap or a coincidence becomes visible.

On the reference project the timeline is what showed an acquisition's capabilities
appearing in the documentation two years before the "vision" announcement that
claimed them as new.

Tolerant by design: it uses whatever CSVs exist and reports what was missing, so it
is useful from the first extraction onwards rather than only at the end.

Usage:  python3 tools/build_timeline.py
"""
import csv
import os

import config

# (file, date column, label template, kind, evidence)  - all optional
FEEDS = [
    ("subdomains.csv",     "first_seen",  "host provisioned: {host}",              "infrastructure", "infrastructure (CT)"),
    ("filings.csv",        "filed",       "{form} filed{items}",                   "filing",         "statutory (SEC)"),
    ("sdk_releases.csv",   "published",   "{repo} {tag}",                          "release",        "company-own (technical)"),
    ("incidents.csv",      "created_at",  "incident ({impact}): {name}",           "incident",       "company-own (operational)"),
    ("repos.csv",          "created",     "public repo created: {name}",           "release",        "company-own (technical)"),
    ("site_inventory.csv", "lastmod",     "page: {url}",                           "page",           "company-own (weak date)"),
    ("docs_index.csv",     "fetched",     "doc captured: {slug}",                  "capture",        "company-own (technical)"),
    ("financials_annual.csv", "period_end", "{period} reported",                   "financial",      "audited (SEC XBRL)"),
]

# these are high volume and would drown the file; included only with --all
NOISY = {"site_inventory.csv", "docs_index.csv"}


def main():
    import sys
    want_all = "--all" in sys.argv
    rows, used, missing = [], [], []

    for fn, datecol, tmpl, kind, evidence in FEEDS:
        p = os.path.join(config.DATA, fn)
        if not os.path.exists(p):
            missing.append(fn)
            continue
        if fn in NOISY and not want_all:
            used.append("%s (skipped, use --all)" % fn)
            continue
        n = 0
        for r in csv.DictReader(open(p)):
            d = (r.get(datecol) or "")[:10]
            if not (len(d) == 10 and d[4] == "-"):
                continue
            safe = {k: (v or "") for k, v in r.items()}
            safe.setdefault("items", "")
            if safe.get("items"):
                safe["items"] = " (%s)" % safe["items"]
            try:
                label = tmpl.format(**safe)
            except KeyError:
                continue
            rows.append({"date": d, "kind": kind, "event": label[:200],
                         "source_file": fn, "evidence": evidence})
            n += 1
        used.append("%s (%d)" % (fn, n))

    if not rows:
        raise SystemExit("nothing dated in data/ yet - run the extractors first")

    rows.sort(key=lambda r: (r["date"], r["kind"]))
    with open(config.out("timeline.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["date", "kind", "event", "source_file", "evidence"])
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    print("fed by: %s" % ", ".join(used))
    if missing:
        print("not yet extracted: %s" % ", ".join(missing))
    print("\n%d dated events  (%s .. %s)" % (len(rows), rows[0]["date"], rows[-1]["date"]))
    for k, c in Counter(r["kind"] for r in rows).most_common():
        print("   %-16s %6d" % (k, c))
    years = Counter(r["date"][:4] for r in rows)
    print("\nby year: %s" % "  ".join("%s:%d" % (y, c) for y, c in sorted(years.items())))
    print("\nwrote data/timeline.csv")


if __name__ == "__main__":
    main()
