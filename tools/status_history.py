#!/usr/bin/env python3
"""Public status page -> data/incidents.csv, data/status_components.csv

A vendor-run status page is self-published, but it is the rare company-own source
that is costly to falsify: customers watch it live during an outage, and the
timestamps are written by the incident, not by marketing.

What it is good for
  - the SHAPE of reliability over time (incidents per quarter, mean duration)
  - which named components exist, which is an architecture disclosure by accident
    (cluster names, regional instances, per-channel services)
  - whether an incident named a channel a competitor also sells

What it is NOT good for
  - a reliability comparison against a vendor with no status page. Absence of a
    status page is an absence of evidence, never evidence of good uptime. Record
    it as an absence and say so.

Usage:  python3 tools/status_history.py
"""
import csv
import json
import re
from datetime import datetime

import config


MONTHS = {m: i + 1 for i, m in enumerate(
    "January February March April May June July August September October "
    "November December".split())}

# the history feed renders times inside <var> tags, in the page's display timezone:
#   "Jun <var data-var='date'>12</var>, <var data-var='time'>10:58</var> - ... 14:13 EDT"
STAMP = re.compile(r"data-var='date'>(\d+)<|data-var='time'>([\d:]+)<")


def parse_stamp(s):
    """-> (day, 'HH:MM:SS', 'HH:MM:SS'). Times are display-local; only the gap matters."""
    day, times = 0, []
    for d, t in STAMP.findall(s or ""):
        if d:
            day = int(d)
        elif t:
            times.append(t if len(t) == 8 else t + ":00")
    return day, (times[0] if times else ""), (times[1] if len(times) > 1 else "")


def clock_minutes(a, b):
    if not (a and b):
        return ""
    to_m = lambda t: int(t[:2]) * 60 + int(t[3:5])       # noqa: E731
    d = to_m(b) - to_m(a)
    return d if d >= 0 else d + 24 * 60                  # incident crossed midnight


def dur_minutes(a, b):
    if not a or not b:
        return ""
    fmt = "%Y-%m-%dT%H:%M:%S"
    try:
        ta = datetime.strptime(a[:19], fmt)
        tb = datetime.strptime(b[:19], fmt)
        return round((tb - ta).total_seconds() / 60)
    except ValueError:
        return ""


def main():
    base = config.STATUSPAGE.rstrip("/")

    comps = json.loads(config.get(base + "/api/v2/components.json"))["components"]
    with open(config.out("status_components.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["name", "group", "status", "created_at", "description", "evidence"])
        by_id = {c["id"]: c["name"] for c in comps}
        for c in comps:
            w.writerow([c["name"], by_id.get(c.get("group_id"), ""), c["status"],
                        (c.get("created_at") or "")[:10], (c.get("description") or "")[:200],
                        "company-own (operational)"])
    print("components: %d -> data/status_components.csv" % len(comps))
    groups = sorted({by_id.get(c.get("group_id"), "") for c in comps} - {""})
    if groups:
        print("  component groups:", ", ".join(groups[:12]))

    # /api/v2/incidents.json caps at the most recent 50. The month-indexed HTML
    # archive under /history goes back to the page's creation; parse that for depth.
    inc = json.loads(config.get(base + "/api/v2/incidents.json"))["incidents"]
    rows = []
    for i in inc:
        upd = i.get("incident_updates") or []
        rows.append({
            "id": i["id"],
            "created_at": (i.get("created_at") or "")[:19],
            "resolved_at": (i.get("resolved_at") or "")[:19],
            "minutes": dur_minutes(i.get("created_at"), i.get("resolved_at")),
            "impact": i.get("impact", ""),
            "status": i.get("status", ""),
            "name": (i.get("name") or "").replace("\n", " ")[:180],
            "components": "|".join(c["name"] for c in (i.get("components") or [])),
            "updates": len(upd),
            "url": i.get("shortlink", ""),
            "evidence": "company-own (operational)",
        })

    have = {r["id"] for r in rows}
    empty_pages = 0
    for page in range(1, 41):
        try:
            doc = json.loads(config.get("%s/history.json?page=%d" % (base, page), retries=2))
        except json.JSONDecodeError:
            break
        months = doc.get("months") or []
        if not months:
            break
        on_page = sum(len(m.get("incidents", [])) for m in months)
        for m in months:
            for i in m.get("incidents", []):
                if i["code"] in have:
                    continue                        # already have it from the API feed
                have.add(i["code"])
                day, start, end = parse_stamp(i.get("timestamp", ""))
                iso = ("%s-%02d-%02d" % (m["year"], MONTHS.get(m["name"].split()[0], 0), day)
                       if day else "")
                rows.append({
                    "id": i["code"],
                    "created_at": ("%sT%s" % (iso, start)) if iso and start else iso,
                    "resolved_at": ("%sT%s" % (iso, end)) if iso and end else "",
                    "minutes": clock_minutes(start, end),
                    "impact": i.get("impact", ""),
                    "status": "resolved",
                    "name": (i.get("name") or "").replace("\n", " ")[:180],
                    "components": "",
                    "updates": "",
                    "url": "%s/incidents/%s" % (base, i["code"]),
                    "evidence": "company-own (operational)",
                })
        # Stop on genuinely empty pages, not on pages that merely overlap the API
        # feed - the recent months are covered twice and would end the walk at once.
        empty_pages = empty_pages + 1 if on_page == 0 else 0
        if empty_pages >= 3:
            break

    rows.sort(key=lambda r: r["created_at"], reverse=True)
    with open(config.out("incidents.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    quarters = Counter("%sQ%d" % (r["created_at"][:4], (int(r["created_at"][5:7]) - 1) // 3 + 1)
                       for r in rows if r["created_at"])
    mins = [r["minutes"] for r in rows if isinstance(r["minutes"], int)]
    print("incidents: %d  (%s .. %s)" % (len(rows), rows[-1]["created_at"][:10],
                                         rows[0]["created_at"][:10]))
    if mins:
        print("duration: median %d min, longest %d min" % (sorted(mins)[len(mins) // 2], max(mins)))
    print("by quarter:", "  ".join("%s:%d" % (q, c) for q, c in sorted(quarters.items())[-10:]))
    print("wrote data/incidents.csv")


if __name__ == "__main__":
    main()
