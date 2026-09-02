#!/usr/bin/env python3
"""Public Greenhouse job board -> data/careers_departments.csv

Where a company is hiring is the cheapest forward-looking signal a competitor can get,
and it is one no marketing page offers. A careers board is not a roadmap, but the ratio
between departments is a statement about where the next year's cost is going.

This exists because the board's own web UI would not yield a department split: the
Department filter did not drive reliably under automation, so the first pass captured
only the taxonomy and a front-of-list sample and left the exact split as open question
56. Greenhouse publishes the same board as JSON, unauthenticated, with the department
grouping already done — which closes that question from a better source than scraping
the page would have.

What this measures well
  - the RATIO between functions, which is a hiring posture rather than a claim
  - the total count of open requisitions on one date, re-checkable by anyone

What it cannot measure
  - current headcount. A req is an intention, not a person; see FACTS.md §1 for the
    audited employee counts, which are a different measurement entirely.
  - how long a req has been open, or whether it will be filled. Greenhouse's public
    board carries no posting date.
  - anything about departments with zero open roles. Absence here is not evidence that
    a function does not exist.

Usage:  python3 tools/careers_board.py [board-token]   (defaults to config.SHORT lower)
"""
import csv
import datetime
import json
import os
import sys
import urllib.request

import config

API = "https://boards-api.greenhouse.io/v1/boards/%s/departments"


def main():
    token = sys.argv[1] if len(sys.argv) > 1 else config.SHORT.lower()
    url = API % token
    print("board: %s" % url)

    req = urllib.request.Request(url, headers={"User-Agent": config.UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            raw = r.read()
    except Exception as e:                          # noqa: BLE001
        # Optional source: a failure here leaves question 56 open and must not stop a run.
        print("FAILED: %s" % e)
        print("Record this in logs/fetch-failures.md; question 56 stays open.")
        return 1

    today = datetime.date.today().isoformat()
    keep = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "sources", "external",
                        "greenhouse-board-%s_%s.json" % (token, today))
    os.makedirs(os.path.dirname(keep), exist_ok=True)
    with open(keep, "wb") as fh:
        fh.write(raw)
    print("kept raw: sources/external/%s" % os.path.basename(keep))

    deps = json.loads(raw).get("departments", [])
    rows = []
    for d in deps:
        jobs = d.get("jobs", []) or []
        # Locations are free text on a Greenhouse board ("New York" vs "New York, NY"),
        # so this counts distinct strings and says so rather than implying a clean
        # office count.
        locs = {(j.get("location") or {}).get("name", "") for j in jobs}
        locs.discard("")
        rows.append({
            "department": d.get("name", ""),
            "open_roles": len(jobs),
            "distinct_location_strings": len(locs),
            "captured": today,
            "evidence": "company-own (public ATS board, unauthenticated JSON)",
        })

    rows.sort(key=lambda r: (-r["open_roles"], r["department"]))
    with open(config.out("careers_departments.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    total = sum(r["open_roles"] for r in rows)
    hiring = [r for r in rows if r["open_roles"] > 0]
    print("departments: %d listed, %d with at least one open role" % (len(rows), len(hiring)))
    print("open roles:  %d" % total)
    for r in hiring:
        print("   %4d  %-28s  %2d location strings"
              % (r["open_roles"], r["department"], r["distinct_location_strings"]))
    print("wrote data/careers_departments.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
