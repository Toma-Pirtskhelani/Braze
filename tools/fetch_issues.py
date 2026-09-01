#!/usr/bin/env python3
"""Public issue trackers -> sources/panels/github_issues.txt and data/issues.csv

THE CUSTOMER-VOICE SOURCE THAT DOES NOT NEED A HUMAN.

G2, Gartner, TrustRadius and Glassdoor all return HTTP 403 to scripted access. That
makes them a human step, and a human step is a stop for an unattended run. Public issue
trackers are the substitute, and on several axes they are better evidence:

  - UNSOLICITED. Nobody was emailed a review request. People open an issue because
    something cost them a day.
  - SPECIFIC. "Segmentation is clunky" versus a stack trace and a reproduction.
  - DATED, and with a resolution. You can measure how long problems stay open.
  - THE VENDOR ANSWERS IN PUBLIC, which is itself a support-quality signal.

What it is NOT
  - representative. Issue authors are developers, not the marketers who buy the
    product. It tells you about the SDK surface, not the dashboard.
  - a satisfaction measure. Never convert issue counts into a rating.
  - a substitute for the review panels where those can be captured. It is a floor,
    not a replacement. Say which one a finding came from.

Verified 2026-09-01: 1,091 issues across braze-inc, 1,065 closed and 26 open.

Rate limits: 60 requests/hour anonymous, 5,000 with GITHUB_TOKEN. Export the token
for the full walk; without it this samples the most active repositories.

Usage:  python3 tools/fetch_issues.py [org] [--max-repos N]
"""
import csv
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime

import config

API = "https://api.github.com"


def gh(path, token):
    """-> (parsed json, rate-limit remaining). Errors come back as {"_error": ...}."""
    import urllib.request
    url = path if path.startswith("http") else API + path
    req = urllib.request.Request(url, headers={
        "User-Agent": config.UA,
        "Accept": "application/vnd.github+json",
        **({"Authorization": "Bearer " + token} if token else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.loads(r.read()), r.headers.get("X-RateLimit-Remaining", "?")
    except Exception as e:                          # noqa: BLE001
        return {"_error": str(e)}, "?"


def age_days(a, b):
    try:
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        return (datetime.strptime(b, fmt) - datetime.strptime(a, fmt)).days
    except (ValueError, TypeError):
        return ""


def main():
    argv, positional, max_repos = sys.argv[1:], [], 0
    i = 0
    while i < len(argv):
        if argv[i] == "--max-repos":
            max_repos = int(argv[i + 1])
            i += 2                                  # skip the flag AND its value
            continue
        if not argv[i].startswith("--"):
            positional.append(argv[i])
        i += 1
    org = positional[0] if positional else config.GITHUB_ORG
    if not org:
        raise SystemExit("no GitHub org set - fill in GITHUB_ORG in tools/config.py")
    token = os.environ.get("GITHUB_TOKEN", "")
    print("org: %s  (%s)" % (org, "authenticated" if token else "anonymous, 60 req/hr"))

    # prefer the already-extracted repo list; fall back to the API
    repo_csv = os.path.join(config.DATA, "repos.csv")
    if os.path.exists(repo_csv):
        repos = [r for r in csv.DictReader(open(repo_csv))]
        repos.sort(key=lambda r: -int(r.get("open_issues") or 0))
        names = [r["name"] for r in repos if r.get("archived") != "True"]
    else:
        batch, _ = gh("/orgs/%s/repos?per_page=100&sort=pushed" % org, token)
        if isinstance(batch, dict):
            raise SystemExit("GitHub error: %s" % batch.get("_error"))
        names = [r["name"] for r in batch if not r.get("archived")]

    if not max_repos:
        max_repos = 100 if token else 15
    names = names[:max_repos]
    print("walking %d repositories\n" % len(names))

    rows, left = [], "?"
    for name in names:
        page, got = 1, 0
        while page <= (20 if token else 2):
            batch, left = gh("/repos/%s/%s/issues?state=all&per_page=100&page=%d"
                             % (org, name, page), token)
            if isinstance(batch, dict):
                print("   %-40s stopped: %s" % (name, str(batch.get("_error"))[:40]))
                break
            if not batch:
                break
            for i in batch:
                if "pull_request" in i:             # the issues endpoint returns PRs too
                    continue
                body = re.sub(r"\s+", " ", (i.get("body") or ""))[:2000]
                rows.append({
                    "repo": name,
                    "number": i["number"],
                    "title": (i.get("title") or "").replace("\n", " ")[:200],
                    "state": i.get("state", ""),
                    "created": (i.get("created_at") or "")[:10],
                    "closed": (i.get("closed_at") or "")[:10],
                    "days_open": age_days(i.get("created_at"), i.get("closed_at") or ""),
                    "comments": i.get("comments", 0),
                    "labels": "|".join(l["name"] for l in (i.get("labels") or [])),
                    "author_is_member": (i.get("author_association") in
                                         ("MEMBER", "OWNER", "COLLABORATOR")),
                    "url": i.get("html_url", ""),
                    "body": body,
                    "evidence": "third-party (unsolicited, public issue tracker)",
                })
                got += 1
            page += 1
        if got:
            print("   %-40s %4d issues   (limit left %s)" % (name, got, left))

    if not rows:
        raise SystemExit("no issues retrieved - check the org name, or the rate limit")

    rows.sort(key=lambda r: r["created"], reverse=True)
    fields = [f for f in rows[0] if f != "body"]
    with open(config.out("issues.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    # a panel file so tools/code_reviews.py can code this like any other corpus
    os.makedirs(os.path.join(config.SOURCES, "panels"), exist_ok=True)
    p = os.path.join(config.SOURCES, "panels", "github_issues.txt")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("# Public issue trackers, %s org. Captured %s.\n"
                 "# Unsolicited and technical: developers, not buyers. Not a satisfaction\n"
                 "# measure and never to be converted into a rating.\n\n"
                 % (org, __import__("datetime").date.today().isoformat()))
        for r in rows:
            if r["author_is_member"]:               # exclude the vendor's own tickets
                continue
            fh.write("%s #%s [%s] %s\n%s\n\n\n"
                     % (r["repo"], r["number"], r["state"], r["title"], r["body"]))

    external = [r for r in rows if not r["author_is_member"]]
    closed = [r for r in rows if r["days_open"] != "" and r["state"] == "closed"]
    dates = sorted(r["created"] for r in rows if r["created"])
    print("\nissues: %d total | %d not opened by the vendor's own people"
          % (len(rows), len(external)))
    print("range: %s .. %s" % (dates[0], dates[-1]))
    if closed:
        d = sorted(int(r["days_open"]) for r in closed)
        print("time to close: median %d days, 90th percentile %d days"
              % (d[len(d) // 2], d[int(len(d) * 0.9)]))
    print("open now: %d" % sum(1 for r in rows if r["state"] == "open"))
    years = Counter(r["created"][:4] for r in rows if r["created"])
    print("by year: %s" % "  ".join("%s:%d" % y for y in sorted(years.items())))
    print("\nwrote data/issues.csv and sources/panels/github_issues.txt")
    print("next: python3 tools/code_reviews.py  (it will code this corpus too)")


if __name__ == "__main__":
    main()
