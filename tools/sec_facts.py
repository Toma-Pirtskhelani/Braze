#!/usr/bin/env python3
"""SEC XBRL company facts -> data/financials.csv and data/financials_restated.csv

This is the strongest financial evidence available anywhere on a US-listed company:
audited, filed under legal penalty, machine-readable, and reported every quarter.

Two things this script does that a naive read of the XBRL does not:

1. RESTATEMENTS ARE KEPT.  The same (concept, period) is often reported more than
   once with different values across filings. The newest filing wins in
   financials.csv; every superseded value is written to financials_restated.csv.
   A restatement is a conflict, and conflicts get recorded, never smoothed over.

2. DURATION AND INSTANT FACTS ARE DISTINGUISHED.  Revenue is a duration (start..end);
   cash is an instant (end only). Mixing them silently produces nonsense.

TRAP, verified on this company's own data: the `fy` and `fp` fields describe the FILING,
not the period. Braze's FY2026 10-K reports FY2024 and FY2025 revenue, and XBRL labels
both `fy2026`. Never key a table on `fy`. Use `start`/`end`, which is what the derived
`period` and `duration_days` columns below are computed from.

Usage:  python3 tools/sec_facts.py [--all]
        --all writes every us-gaap concept; the default writes the ~40 that matter.
"""
import csv
import json
import sys
from datetime import date

import config

# The concepts a competitive analysis actually uses. Everything else is noise until
# a specific question needs it, and --all is there for that.
KEY = [
    # income statement
    "RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues",
    "CostOfRevenue", "CostOfGoodsAndServicesSold", "GrossProfit",
    "ResearchAndDevelopmentExpense", "SellingAndMarketingExpense",
    "GeneralAndAdministrativeExpense", "OperatingExpenses",
    "OperatingIncomeLoss", "NetIncomeLoss",
    "ShareBasedCompensation",
    "EarningsPerShareBasic", "EarningsPerShareDiluted",
    # balance sheet
    "CashAndCashEquivalentsAtCarryingValue", "ShortTermInvestments",
    "MarketableSecuritiesCurrent", "AssetsCurrent", "Assets",
    "LiabilitiesCurrent", "Liabilities", "StockholdersEquity",
    "ContractWithCustomerLiabilityCurrent", "ContractWithCustomerLiability",
    "Goodwill", "IntangibleAssetsNetExcludingGoodwill",
    "AccountsReceivableNetCurrent",
    # cash flow
    "NetCashProvidedByUsedInOperatingActivities",
    "NetCashProvidedByUsedInInvestingActivities",
    "NetCashProvidedByUsedInFinancingActivities",
    "PaymentsToAcquireBusinessesNetOfCashAcquired",
    # the SaaS-specific ones
    "RevenueRemainingPerformanceObligation",
    "DeferredRevenueRevenueRecognized1",
    # headcount and equity
    "WeightedAverageNumberOfSharesOutstandingBasic",
    "WeightedAverageNumberOfDilutedSharesOutstanding",
]

URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json"

FY_END = config.FY_END          # (month, day) — set once, in tools/config.py


def label(start, end):
    """A period label an analyst can read, derived only from the dates themselves."""
    if not end:
        return "", 0
    e = date.fromisoformat(end)
    fy = e.year if (e.month, e.day) <= FY_END or e.month <= FY_END[0] else e.year + 1
    if not start:
        return "FY%d as at %s" % (fy, end), 0
    days = (e - date.fromisoformat(start)).days
    if days > 300:
        return "FY%d" % fy, days
    q = ((e.month - FY_END[0] - 1) % 12) // 3 + 1
    return "FY%d Q%d" % (fy, q), days


def main():
    want_all = "--all" in sys.argv
    raw = config.get(URL % config.CIK, contact=True)
    doc = json.loads(raw)
    print("entity: %s" % doc["entityName"])

    rows = []
    for taxonomy, concepts in doc["facts"].items():
        for concept, body in concepts.items():
            if not want_all and concept not in KEY:
                continue
            for unit, facts in body["units"].items():
                for f in facts:
                    period, days = label(f.get("start", ""), f.get("end", ""))
                    rows.append({
                        "concept": concept,
                        "taxonomy": taxonomy,
                        "label": (body.get("label") or "")[:120],
                        "unit": unit,
                        "kind": "duration" if f.get("start") else "instant",
                        "start": f.get("start", ""),
                        "end": f.get("end", ""),
                        "period": period,
                        "duration_days": days,
                        "filing_fy": f.get("fy", ""),      # the FILING's year, not the period's
                        "filing_fp": f.get("fp", ""),
                        "form": f.get("form", ""),
                        "value": f["val"],
                        "filed": f.get("filed", ""),
                        "accession": f.get("accn", ""),
                        "frame": f.get("frame", ""),
                        "evidence": "audited (SEC XBRL)",
                    })

    if not rows:
        raise SystemExit("no facts matched - is the CIK right?")

    # newest filing wins; everything it supersedes is a restatement
    rows.sort(key=lambda r: (r["concept"], r["unit"], r["start"], r["end"], r["filed"]))
    current, restated = {}, []
    for r in rows:
        k = (r["concept"], r["unit"], r["start"], r["end"])
        if k in current:
            prev = current[k]
            older, newer = (prev, r) if prev["filed"] <= r["filed"] else (r, prev)
            if older["value"] != newer["value"]:
                older = dict(older)
                older["superseded_by"] = newer["accession"]
                older["new_value"] = newer["value"]
                restated.append(older)
            current[k] = newer
        else:
            current[k] = r

    fields = list(rows[0].keys())
    with open(config.out("financials.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in sorted(current.values(), key=lambda r: (r["concept"], r["end"])):
            w.writerow(r)

    with open(config.out("financials_restated.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields + ["superseded_by", "new_value"])
        w.writeheader()
        w.writerows(sorted(restated, key=lambda r: (r["concept"], r["end"])))

    # the wide table a deck or a model actually reads from: one row per period,
    # annual and quarterly kept apart because mixing them is the classic error.
    for scope, keep in (("annual", lambda r: r["duration_days"] > 300 or r["kind"] == "instant"),
                        ("quarterly", lambda r: 0 < r["duration_days"] <= 300)):
        sel = [r for r in current.values() if keep(r) and r["unit"] in ("USD", "USD/shares", "shares")]
        # one row per period end. An instant and a duration share an end date; the
        # duration's label wins because it is the one an analyst says out loud.
        names = {}
        for r in sorted(sel, key=lambda r: r["kind"]):      # duration before instant
            names.setdefault(r["end"], r["period"])
        concepts_seen = sorted({r["concept"] for r in sel})
        table = {(r["end"], r["concept"]): r["value"] for r in sel}
        with open(config.out("financials_%s.csv" % scope), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["period_end", "period"] + concepts_seen)
            for end in sorted(names):
                w.writerow([end, names[end]] + [table.get((end, c), "") for c in concepts_seen])
        periods = names
        print("wrote data/financials_%s.csv  (%d periods x %d concepts)"
              % (scope, len(periods), len(concepts_seen)))

    concepts = sorted({r["concept"] for r in current.values()})
    ends = sorted({r["end"] for r in current.values() if r["end"]})
    print("facts: %d current, %d superseded" % (len(current), len(restated)))
    print("concepts: %d | periods: %s .. %s" % (len(concepts), ends[0], ends[-1]))
    if restated:
        print("RESTATEMENTS FOUND - record them in docs/CONFLICTS.md:")
        for r in restated[:8]:
            print("   %-46s %s  %s -> %s" % (r["concept"], r["end"], r["value"], r["new_value"]))
    print("wrote data/financials.csv, data/financials_restated.csv")


if __name__ == "__main__":
    main()
