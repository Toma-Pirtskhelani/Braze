# -*- coding: utf-8 -*-
"""The one place the subject company is named.

Every script in tools/ imports from here, so pointing this toolkit at a different
vendor is a single-file change. Nothing in this file is a finding: it is a set of
addresses, each verified reachable on the date noted in docs/SOURCES.md.

SEC requires a real contact in the User-Agent. Set SEC_CONTACT in your environment
if you would rather not use the default below.
"""
import os

COMPANY = "Braze, Inc."
SHORT = "Braze"

# SEC EDGAR — verified 2026-09-01: 737 filings
CIK = "0001676238"
TICKER = "BRZE"

# Fiscal year end, as (month, day). Braze closes 31 January, so the year ending
# 2025-01-31 is "FY2025" in the company's own language. Getting this wrong mislabels
# every period in data/financials_*.csv, so check it against the 10-K cover page.
FY_END = (1, 31)

# Web properties
DOMAIN = "braze.com"
DOCS_SITEMAP = "https://www.braze.com/docs/sitemap.xml"
SITE_SITEMAP = "https://www.braze.com/sitemap.xml"

# Public code and release history
GITHUB_ORG = "braze-inc"

# Atlassian Statuspage — public incident history
STATUSPAGE = "https://braze.statuspage.io"

# Contact string sent to SEC and other polite-crawl endpoints
# SEC asks for a real name and email in the User-Agent and throttles requests without
# one. Set SEC_CONTACT in your environment; it is deliberately not committed.
SEC_CONTACT = os.environ.get("SEC_CONTACT", "competitive research contact@example.com")
UA = os.environ.get("RESEARCH_UA", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Deck identity, so the company is named in exactly one file
DECK_TITLE = "%s Analysis" % SHORT
DECK_FILE = "%s-deck.html" % SHORT.lower().replace(" ", "-")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SOURCES = os.path.join(ROOT, "sources")
LOGS = os.path.join(ROOT, "logs")


def out(name):
    """Path of a derived CSV, creating data/ if needed."""
    os.makedirs(DATA, exist_ok=True)
    return os.path.join(DATA, name)


def get(url, contact=False, timeout=60, retries=3):
    """One polite GET. Returns bytes. Retries on transient failure."""
    import time
    import urllib.request
    import urllib.error
    hdr = {"User-Agent": SEC_CONTACT if contact else UA,
           "Accept-Encoding": "gzip, deflate"}
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
        except Exception as e:                       # noqa: BLE001 - report and retry
            last = e
            time.sleep(2 * (attempt + 1))
    # a plain exception, not SystemExit: callers with a fallback source must be able
    # to catch this. crt.sh being down is normal and must not end the run.
    raise RuntimeError("GET failed after %d tries: %s (%s)" % (retries, url, last))
