#!/usr/bin/env python3
"""SEC filing documents -> sources/filings/*.txt

data/filings.csv is the INDEX. This fetches the documents themselves, because the
10-K is the single richest source on any listed company and no amount of index
metadata substitutes for its text.

What each form is worth reading for:
  10-K    the whole business. Item 1 (what they sell), Item 1A (risk factors -
          legally compelled candour about what could go wrong), Item 7 (MD&A -
          management explaining their own numbers), and the subsidiary exhibit
  10-Q    quarterly, with segment and geography splits
  8-K     material events, dated. Acquisitions, executive departures, restructuring
  DEF 14A executive compensation and the board - what management is paid to optimise

Verified 2026-09-01: the FY2026 10-K is 2.1 MB of HTML, 73,364 words of text.

Polite and resumable: one request at a time, skips anything already on disk, and
records every failure in logs/fetch-failures.md.

Usage:  python3 tools/fetch_filings.py [--forms 10-K,10-Q,8-K,DEF 14A] [--limit N]
"""
import csv
import html
import os
import re
import sys
import time
from datetime import date

import config

DEST = os.path.join(config.SOURCES, "filings")
DEFAULT_FORMS = ["10-K", "10-Q", "DEF 14A", "8-K"]
DROP = re.compile(r"(?s)<(script|style)\b.*?</\1>", re.I)


def to_text(raw):
    """EDGAR HTML/iXBRL -> readable text. Deliberately simple: this feeds search and
    citation by line range, not rendering."""
    s = raw.decode("utf-8", "replace")
    s = DROP.sub(" ", s)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    # table rows and cells become pipe-delimited lines so financial tables stay legible
    s = re.sub(r"</t[dh]>", " | ", s, flags=re.I)
    s = re.sub(r"</tr>", "\n", s, flags=re.I)
    s = re.sub(r"<(p|div|br|h[1-6])\b[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = s.replace(" ", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def main():
    args = sys.argv[1:]
    forms = ([f.strip() for f in args[args.index("--forms") + 1].split(",")]
             if "--forms" in args else DEFAULT_FORMS)
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else 0

    idx = os.path.join(config.DATA, "filings.csv")
    if not os.path.exists(idx):
        raise SystemExit("run tools/sec_filings.py first - this reads data/filings.csv")

    rows = [r for r in csv.DictReader(open(idx)) if r["form"] in forms]
    rows.sort(key=lambda r: r["filed"], reverse=True)
    if limit:
        rows = rows[:limit]

    os.makedirs(DEST, exist_ok=True)
    os.makedirs(config.LOGS, exist_ok=True)
    todo, skipped = [], 0
    for r in rows:
        slug = "%s_%s_%s" % (r["filed"], r["form"].replace(" ", "-").replace("/", "-"),
                             r["accession"].replace("-", "")[-6:])
        path = os.path.join(DEST, slug + ".txt")
        if os.path.exists(path):
            skipped += 1
            continue
        todo.append((r, path, slug))

    print("%d matching filings | %d already on disk | fetching %d" % (len(rows), skipped, len(todo)))
    if not todo:
        print("nothing to do")
        return

    ok, fails, today = 0, [], date.today().isoformat()
    for n, (r, path, slug) in enumerate(todo, 1):
        try:
            raw = config.get(r["url"], contact=True, timeout=120, retries=2)
        except RuntimeError as e:
            fails.append((r["url"], str(e)[:160]))
            continue
        text = to_text(raw)
        header = ("---\nform: %s\nfiled: %s\nperiod: %s\naccession: %s\nurl: %s\n"
                  "fetched: %s\nevidence: audited (SEC EDGAR)\n---\n\n"
                  % (r["form"], r["filed"], r["period"], r["accession"], r["url"], today))
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(header + text + "\n")
        ok += 1
        print("   %3d/%d  %-34s %8d words" % (n, len(todo), slug, len(text.split())))
        time.sleep(0.4)                             # SEC asks for <10 req/s; be well under

    if fails:
        with open(os.path.join(config.LOGS, "fetch-failures.md"), "a", encoding="utf-8") as fh:
            fh.write("\n## filings fetch %s - %d failures of %d\n\n" % (today, len(fails), len(todo)))
            for u, e in fails:
                fh.write("- `%s` - %s\n" % (u, e))
        print("\n%d failures recorded in logs/fetch-failures.md" % len(fails))

    total = len([f for f in os.listdir(DEST) if f.endswith(".txt")])
    print("\nfetched %d | sources/filings/ now holds %d documents" % (ok, total))
    print("""
WHERE TO READ FIRST
  the newest 10-K, Item 1A - risk factors are the only section a company is legally
  obliged to be candid in, and they name the competitors and constraints that
  marketing will not.

  rg -n -i 'item 1a' sources/filings/*10-K*.txt | head
""")


if __name__ == "__main__":
    main()
