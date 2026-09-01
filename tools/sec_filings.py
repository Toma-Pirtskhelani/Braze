#!/usr/bin/env python3
"""SEC EDGAR submissions -> data/filings.csv and data/insider_transactions.csv

The filing INDEX is itself evidence, before a single document is read:

  - 8-K clusters date material events (acquisitions, executive departures, restructuring)
  - DEF 14A carries executive compensation and the board
  - Form 4 is every insider trade, with date, price and volume
  - SC 13G/13D is who owns the company
  - Form 144 is a proposed sale, filed BEFORE the Form 4 that reports it

Counting Form 4s by month is a legitimate, checkable signal that costs one script.
Reading meaning into any single insider sale is not: most are scheduled 10b5-1 plans.
The CSV therefore carries the rule10b51 flag where EDGAR exposes it.

Usage:  python3 tools/sec_filings.py
"""
import csv
import json

import config

SUB = "https://data.sec.gov/submissions/CIK%s.json"
ARCHIVE = "https://www.sec.gov/Archives/edgar/data/%d/%s/%s"


def main():
    doc = json.loads(config.get(SUB % config.CIK, contact=True))
    cik_int = int(config.CIK)
    print("%s | SIC %s %s | %s | FY ends %s"
          % (doc["name"], doc.get("sic"), doc.get("sicDescription"),
             ",".join(doc.get("exchanges") or []), doc.get("fiscalYearEnd")))

    # EDGAR splits long histories: recent[] plus older files[]
    blocks = [doc["filings"]["recent"]]
    for f in doc["filings"].get("files", []):
        blocks.append(json.loads(config.get(
            "https://data.sec.gov/submissions/" + f["name"], contact=True)))

    rows = []
    for b in blocks:
        n = len(b["form"])
        for i in range(n):
            acc = b["accessionNumber"][i]
            rows.append({
                "form": b["form"][i],
                "filed": b["filingDate"][i],
                "period": b["reportDate"][i],
                "accession": acc,
                "primary_doc": b["primaryDocument"][i],
                "description": (b.get("primaryDocDescription") or [""] * n)[i],
                "items": (b.get("items") or [""] * n)[i],
                "url": ARCHIVE % (cik_int, acc.replace("-", ""), b["primaryDocument"][i]),
                "evidence": "statutory (SEC EDGAR)",
            })

    rows.sort(key=lambda r: r["filed"], reverse=True)
    with open(config.out("filings.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    forms = Counter(r["form"] for r in rows)
    print("filings: %d  (%s .. %s)" % (len(rows), rows[-1]["filed"], rows[0]["filed"]))
    for f, c in forms.most_common(16):
        print("   %-14s %4d" % (f, c))

    # a monthly histogram of insider transactions - the shape, not any single trade
    ins = [r for r in rows if r["form"].startswith("4") or r["form"] == "144"]
    months = Counter(r["filed"][:7] for r in ins)
    with open(config.out("insider_filing_counts.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["month", "form4_and_144_filings", "evidence"])
        for m in sorted(months):
            w.writerow([m, months[m], "statutory (SEC EDGAR)"])
    print("insider filings: %d across %d months -> data/insider_filing_counts.csv"
          % (len(ins), len(months)))
    print("wrote data/filings.csv")


if __name__ == "__main__":
    main()
