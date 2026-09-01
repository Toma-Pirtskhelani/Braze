#!/usr/bin/env python3
"""Certificate transparency -> data/subdomains.csv

CT logs are the strongest evidence class available on a company's infrastructure.
Independent operators record every certificate a CA issues, the record is append-only,
and the subject cannot edit or retract it. A host that appears here was really
provisioned, on really that date.

On the reference project this single script surfaced an unannounced product, an MCP
server, and a named enterprise customer that appeared in no marketing page anywhere.

Two sources, because crt.sh is frequently down (it returned 502 throughout the
2026-09-01 setup run): crt.sh first, Cert Spotter as fallback. Cert Spotter paginates
and rate-limits anonymous callers, so pass CERTSPOTTER_TOKEN if you have one.

Usage:  python3 tools/ct_probe.py [domain ...]     (defaults to config.DOMAIN)
"""
import csv
import json
import os
import sys
import urllib.parse

import config


def from_crtsh(domain):
    url = "https://crt.sh/?q=%s&output=json" % urllib.parse.quote("%." + domain)
    raw = config.get(url, timeout=90, retries=2)
    if not raw.lstrip().startswith(b"["):
        raise ValueError("crt.sh did not return JSON")
    out = []
    for r in json.loads(raw):
        for name in r["name_value"].split("\n"):
            out.append((name.strip().lower(), r.get("not_before", "")[:10],
                        r.get("issuer_name", "")[:80], "crt.sh"))
    return out


def from_certspotter(domain):
    base = "https://api.certspotter.com/v1/issuances"
    tok = os.environ.get("CERTSPOTTER_TOKEN", "")
    after, out, pages = "", [], 0
    while pages < 40:
        url = ("%s?domain=%s&include_subdomains=true&expand=dns_names&expand=issuer"
               % (base, domain)) + (("&after=" + after) if after else "")
        if tok:
            url += "&token=" + tok
        try:
            batch = json.loads(config.get(url, timeout=60, retries=2))
        except RuntimeError as e:
            # anonymous callers are rate-limited after roughly one page. Keep what we
            # have rather than losing it - a partial CT list is still evidence, and the
            # count printed below tells you whether to rerun with a token.
            if out:
                print("  certspotter stopped after %d pages: %s" % (pages, e))
                break
            raise ValueError(str(e))
        if isinstance(batch, dict):                 # an error object
            raise ValueError("certspotter: %s" % batch.get("message", batch))
        if not batch:
            break
        for r in batch:
            for name in r.get("dns_names", []):
                out.append((name.strip().lower(),
                            (r.get("not_before") or "")[:10],
                            ((r.get("issuer") or {}).get("name") or "")[:80],
                            "certspotter"))
        after = batch[-1]["id"]
        pages += 1
    return out


def main():
    domains = sys.argv[1:] or [config.DOMAIN]
    seen = {}
    for domain in domains:
        rows = []
        for fetch in (from_crtsh, from_certspotter):
            try:
                rows = fetch(domain)
                print("%s via %s: %d name observations" % (domain, fetch.__name__, len(rows)))
                break
            except Exception as e:                  # noqa: BLE001 - fall through to next source
                print("  %s failed: %s" % (fetch.__name__, e))
        if not rows:
            print("  ! no CT source answered for %s" % domain)
            continue
        # earliest observation wins: that is when the host was first provisioned
        for name, first, issuer, src in rows:
            if not name or name.startswith("*."):
                continue
            k = name
            if k not in seen or (first and first < seen[k]["first_seen"]):
                seen[k] = {"host": name, "first_seen": first, "issuer": issuer,
                           "apex": domain, "source": src, "certs": 0,
                           "evidence": "infrastructure (certificate transparency)"}
            seen[k]["certs"] += 1

    if not seen:
        raise SystemExit(
            "no CT source answered.\n"
            "  crt.sh is frequently down - retry in an hour.\n"
            "  Cert Spotter rate-limits anonymous callers to about one page; a free\n"
            "  API token at sslmate.com/certspotter lifts that. Export CERTSPOTTER_TOKEN.\n"
            "  Record the gap in logs/fetch-failures.md either way.")

    rows = sorted(seen.values(), key=lambda r: (r["first_seen"] or "9999", r["host"]))
    with open(config.out("subdomains.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    dated = [r for r in rows if r["first_seen"]]
    print("\n%d distinct hosts" % len(rows))
    if dated:
        print("first seen: %s .. %s" % (dated[0]["first_seen"], dated[-1]["first_seen"]))
        print("\nnewest 15 - read these first, this is where unannounced things appear:")
        for r in dated[-15:][::-1]:
            print("   %s  %s" % (r["first_seen"], r["host"]))
    print("\nwrote data/subdomains.csv")


if __name__ == "__main__":
    main()
