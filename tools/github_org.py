#!/usr/bin/env python3
"""Public GitHub org -> data/repos.csv and data/sdk_releases.csv

A vendor that ships open-source SDKs publishes a record it cannot retouch: commit
dates, release cadence, which platforms get attention and which have gone quiet,
and how long issues stay open. Engineers do not write marketing copy in changelogs.

What this measures well
  - release CADENCE per platform, which is a maintenance signal, not a claim
  - which SDKs stopped moving, and when - the strongest "quietly deprecated" evidence
  - the spread of supported platforms, countable rather than asserted

What it cannot measure
  - anything about the server side. A busy SDK repo says nothing about the backend.
  - engineering headcount. Public commits are a fraction of the work.

Rate limits: 60 requests/hour unauthenticated, 5,000 with a token. Export
GITHUB_TOKEN to walk every repo's releases; without one this fetches the repo list
and the releases of SDK repos only.

Usage:  python3 tools/github_org.py [org]      (defaults to config.GITHUB_ORG)
"""
import csv
import json
import os
import re
import sys

import config

API = "https://api.github.com"
SDK = re.compile(r"sdk|segment|plugin|actions", re.I)


def gh(path, token):
    """-> (parsed json, rate-limit remaining). Errors come back as {"_error": ...} so
    the caller can stop cleanly on a rate limit rather than losing the whole walk."""
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


def main():
    org = sys.argv[1] if len(sys.argv) > 1 else config.GITHUB_ORG
    token = os.environ.get("GITHUB_TOKEN", "")
    print("org: %s  (%s)" % (org, "authenticated" if token else "anonymous, 60 req/hr"))

    repos, page = [], 1
    while page <= 5:
        batch, left = gh("/orgs/%s/repos?per_page=100&page=%d" % (org, page), token)
        if isinstance(batch, dict):
            raise SystemExit("GitHub error: %s" % batch.get("_error") or batch)
        if not batch:
            break
        repos += batch
        page += 1
    print("repos: %d  (rate limit remaining: %s)" % (len(repos), left))

    rows = []
    for r in repos:
        rows.append({
            "name": r["name"],
            "language": r.get("language") or "",
            "description": (r.get("description") or "").replace("\n", " ")[:160],
            "created": r["created_at"][:10],
            "pushed": r["pushed_at"][:10],
            "archived": r.get("archived", False),
            "stars": r.get("stargazers_count", 0),
            "forks": r.get("forks_count", 0),
            "open_issues": r.get("open_issues_count", 0),
            "license": ((r.get("license") or {}).get("spdx_id") or ""),
            "is_sdk": bool(SDK.search(r["name"])),
            "url": r["html_url"],
            "evidence": "company-own (technical, public VCS)",
        })
    rows.sort(key=lambda r: r["pushed"], reverse=True)
    with open(config.out("repos.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("wrote data/repos.csv")

    targets = [r for r in rows if r["is_sdk"] and not r["archived"]]
    if not token:
        targets = targets[:12]
        print("no token: sampling the %d most recently pushed SDK repos" % len(targets))

    rel = []
    for r in targets:
        page = 1
        while page <= (10 if token else 1):
            batch, left = gh("/repos/%s/%s/releases?per_page=100&page=%d"
                             % (org, r["name"], page), token)
            if isinstance(batch, dict) or not batch:
                break
            for x in batch:
                rel.append({
                    "repo": r["name"],
                    "platform": r["language"] or "",
                    "tag": x.get("tag_name", ""),
                    "published": (x.get("published_at") or "")[:10],
                    "prerelease": x.get("prerelease", False),
                    "body_bytes": len(x.get("body") or ""),
                    "url": x.get("html_url", ""),
                    "evidence": "company-own (technical, public VCS)",
                })
            page += 1
        print("   %-42s %4d releases  (limit left %s)"
              % (r["name"], sum(1 for x in rel if x["repo"] == r["name"]), left))

    if rel:
        rel.sort(key=lambda r: r["published"], reverse=True)
        with open(config.out("sdk_releases.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rel[0].keys()))
            w.writeheader()
            w.writerows(rel)
        dated = [r["published"] for r in rel if r["published"]]
        print("releases: %d across %d repos  (%s .. %s)"
              % (len(rel), len({r["repo"] for r in rel}), min(dated), max(dated)))
        print("wrote data/sdk_releases.csv")

    quiet = [r for r in rows if r["is_sdk"] and not r["archived"] and r["pushed"] < "2026-01-01"]
    if quiet:
        print("\nSDK repos with no push in 2026 - check whether these are quietly retired:")
        for r in quiet[:12]:
            print("   %-42s last push %s" % (r["name"], r["pushed"]))


if __name__ == "__main__":
    main()
