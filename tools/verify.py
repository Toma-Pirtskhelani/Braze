#!/usr/bin/env python3
"""Check the analysis against its own rules. Run before calling anything done.

    python3 tools/verify.py            # report
    python3 tools/verify.py --strict   # exit 1 on any failure, for CI or an agent gate

An unattended run needs something that tells it when it is wrong. Every check here
corresponds to a discipline this project claims to follow, and several correspond to a
mistake that was actually made on the reference project:

  - "maps to all 41 slides" that mapped 34   -> slide coverage is checked mechanically
  - a duplicated block in the record          -> div balance is counted
  - a number on a slide with no source        -> figures are matched against FACTS.md
  - data/ quietly acquiring a hand-made table -> the CSV-only invariant is enforced

A check that cannot run yet (no corpus, no record) reports SKIP, not FAIL. The point is
to be usable from the first hour, not only at the end.
"""
import csv
import os
import re
import sys

import config

R = config.ROOT
results = []


def check(name, fn):
    try:
        state, detail = fn()
    except Exception as e:                          # noqa: BLE001 - a broken check is a fail
        state, detail = "FAIL", "check raised: %s" % e
    results.append((state, name, detail))


def read(rel):
    p = os.path.join(R, rel)
    return open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else None


# ── structural invariants ────────────────────────────────────────────────────

def data_is_csv_only():
    d = os.path.join(R, "data")
    if not os.path.isdir(d):
        return "SKIP", "data/ does not exist"
    bad = [f for f in os.listdir(d)
           if not f.startswith(".") and not f.endswith(".csv")]
    if bad:
        return "FAIL", ("data/ must hold only CSVs a script can regenerate; found %s. "
                        "A hand-made table belongs in docs/." % ", ".join(bad[:5]))
    n = len([f for f in os.listdir(d) if f.endswith(".csv")])
    return "PASS", "%d CSVs, nothing else" % n


def sources_have_evidence_column():
    d = os.path.join(R, "data")
    if not os.path.isdir(d):
        return "SKIP", "no data/"
    missing = []
    for f in sorted(os.listdir(d)):
        if not f.endswith(".csv"):
            continue
        with open(os.path.join(d, f), encoding="utf-8", errors="replace") as fh:
            head = fh.readline()
        if "evidence" not in head and "period_end" not in head:   # wide tables are exempt
            missing.append(f)
    if missing:
        return "WARN", "no evidence column: %s" % ", ".join(missing)
    return "PASS", "every CSV carries an evidence column"


# ── the fact index ───────────────────────────────────────────────────────────

ROW = re.compile(r"^\|(?!\s*-)(.+)\|\s*$", re.M)

# Two grade vocabularies are in use across these projects: full words, and the
# abbreviations an earlier repository adopted. Both express the same discipline, so the
# check accepts either rather than forcing a rewrite of a shipped analysis.
GRADES = {"audited", "infrastructure", "documented", "third-party", "claimed", "conflicted",
          "aud", "inf", "doc", "3p", "clm", "cfl"}


def facts_rows():
    """Rows of tables whose header is Fact | Value | Grade | Source.

    Tracking the header matters: FACTS.md also carries a corrections table whose fourth
    column is prose, and reading that as a grade produces a page of false failures.
    """
    t = read("docs/FACTS.md")
    if not t:
        return []
    out, in_fact_table = [], False
    for m in ROW.finditer(t):
        cells = [c.strip() for c in m.group(1).split("|")]
        low = [c.lower() for c in cells]
        if "grade" in low and ("fact" in low or "value" in low):
            in_fact_table = True
            continue
        if "was" in low and "is now" in low:        # the corrections table starts here
            in_fact_table = False                   # tested BEFORE appending, or this
            continue                                # header is read as a fact row
        if not cells or not cells[0] or cells[0].startswith("---"):
            continue
        if in_fact_table and len(cells) >= 4:
            out.append(cells)
    return out


def split_grades(cell):
    return [p.strip().lower() for p in re.split(r"[/,]", re.sub(r"[*`]", "", cell)) if p.strip()]


def facts_are_sourced():
    rows = [r for r in facts_rows() if len(r) >= 4]
    # A row whose grade cell is a dash is an ANNOTATION, not a fact - a discipline note
    # or a caveat sitting inside the table. It needs no grade, but it must say where it
    # comes from, so it is still checked for a source below.
    real = [r for r in rows if r[2] and not r[2].startswith(("_", "—", "-"))]
    notes = [r for r in rows if r not in real]
    if not real:
        return "SKIP", "FACTS.md holds no fact rows yet"
    ungraded = [r[0] for r in real
                if not all(g in GRADES for g in split_grades(r[2]))]
    unsourced = [r[0] for r in real + notes
                 if not r[3].strip() or r[3].strip() in ("—", "-")]
    if ungraded or unsourced:
        return "FAIL", ("%d rows with an unrecognised grade (%s); %d with no source (%s)"
                        % (len(ungraded), ", ".join(ungraded[:3]),
                           len(unsourced), ", ".join(unsourced[:3])))
    return "PASS", ("%d fact rows graded and sourced, %d annotations sourced"
                    % (len(real), len(notes)))


def conflicts_have_rulings():
    """Every conflict must say what to do about it, however that is worded."""
    t = read("docs/CONFLICTS.md")
    if not t:
        return "SKIP", "no CONFLICTS.md"
    body = re.sub(r"(?s)<!--.*?-->", "", t)
    parts = re.split(r"^#{2,3} (C-\d+)", body, flags=re.M)
    if len(parts) < 3:
        return "SKIP", "no conflicts recorded yet"
    pairs = list(zip(parts[1::2], parts[2::2]))
    # "Ruling", "Assessment", "Verdict" - the wording differs between repositories;
    # what matters is that the entry tells a presenter what to say.
    verdict = re.compile(r"\*\*(ruling|assessment|verdict|what to say)", re.I)
    missing = [c for c, chunk in pairs if not verdict.search(chunk)]
    if missing:
        return "FAIL", ("%d of %d conflicts carry no ruling: %s"
                        % (len(missing), len(pairs), ", ".join(missing[:5])))
    return "PASS", "%d conflicts, every one with a ruling" % len(pairs)


# ── the deck ─────────────────────────────────────────────────────────────────

def deck_path():
    try:
        return os.path.join(R, "deck", config.DECK_FILE)
    except AttributeError:
        return os.path.join(R, "deck", "deck.html")


def deck_builds():
    import subprocess
    r = subprocess.run([sys.executable, "deck/build_deck.py"], cwd=R,
                       capture_output=True, text=True)
    if r.returncode != 0:
        return "FAIL", (r.stderr or r.stdout).strip().split("\n")[-1][:160]
    out = r.stdout
    n = re.search(r"slides:\s*(\d+)", out)
    missing = re.search(r"slides without notes:\s*(.+)", out)
    if missing and missing.group(1).strip() not in ("none", "[]"):
        return "FAIL", "slides without speaker notes: %s" % missing.group(1).strip()
    return "PASS", "%s slides, every one with notes" % (n.group(1) if n else "?")


def slides_covered_by_record():
    deck, rec = read(os.path.relpath(deck_path(), R)), read("deck/evidence-record.html")
    if not deck:
        return "SKIP", "deck not built"
    if not rec:
        return "SKIP", "no evidence record yet"
    missing, n = [], 0
    for sec in re.findall(r'(<section class="s[^"]*".*?</section>)', deck, re.S):
        m = re.search(r'data-t="([^"]*)"', sec)
        if not m:
            continue
        n += 1
        # a slide carrying no figure asserts nothing that needs proving
        if m.group(1) in rec or not re.search(r"\d", re.sub(r"<[^>]+>", " ", sec)):
            continue
        missing.append(m.group(1))
    if missing:
        return "FAIL", ("%d of %d slides make claims the record does not cover: %s"
                        % (len(missing), n, "; ".join(missing[:4])))
    return "PASS", "all %d slides covered or claim-free" % n


def record_div_balance():
    rec = read("deck/evidence-record.html")
    if not rec:
        return "SKIP", "no evidence record yet"
    o, c = len(re.findall(r"<div\b", rec)), rec.count("</div>")
    if o != c:
        return "FAIL", ("%d <div> vs %d </div> — a duplicated or unclosed block, "
                        "invisible until the layout breaks" % (o, c))
    return "PASS", "%d divs, balanced" % o


# Only shapes that carry a claim: comma-grouped counts, percentages, currency. Bare
# integers are excluded deliberately - they match years in a biography and product names
# like "Customer 360", and a check that cries wolf gets ignored.
# No magnitude suffix: "$325 million" and "$0 Migration" both tempt a suffix pattern
# into swallowing the next word's first letter, which produced "$0 m" as a phantom
# figure. Match the number, stop, and let the substring comparison handle "$500M".
NUM = re.compile(r"(?<![\w.$])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?%|\$\d[\d,.]*)")


def slide_numbers_are_in_facts():
    deck = read(os.path.relpath(deck_path(), R))
    facts = read("docs/FACTS.md")
    if not deck:
        return "SKIP", "deck not built"
    if not facts:
        return "SKIP", "no FACTS.md"
    body = re.sub(r"(?s)<script.*?</script>", " ", deck)
    body = re.sub(r"(?s)<style.*?</style>", " ", body)
    text = re.sub(r"<[^>]+>", " ", body)
    def variants(v):
        """A slide rounds; FACTS carries the precise value. 22% and 22.0% are the same
        claim, and flagging them as different is how a useful check becomes noise."""
        v = v.strip()
        out = {v, v.replace(",", "")}
        m2 = re.match(r"^(\d+)\.0(%?)$", v)
        if m2:
            out.add(m2.group(1) + m2.group(2))
        if re.match(r"^\d+%$", v):
            out.add(v[:-1] + ".0%")
        return out

    flat = facts.replace(",", "")
    seen, orphans = set(), []
    for m in NUM.finditer(text):
        v = m.group(1).strip()
        if v in seen:
            continue
        seen.add(v)
        if not any(x in facts or x in flat for x in variants(v)):
            orphans.append(v)
    if orphans:
        return "WARN", ("%d figures on slides do not appear in FACTS.md: %s. Every "
                        "number said out loud needs a canonical row."
                        % (len(orphans), ", ".join(orphans[:8])))
    return "PASS", "%d distinct figures, all present in FACTS.md" % len(seen)


# ── provenance ───────────────────────────────────────────────────────────────

def failures_are_resolved():
    t = read("logs/fetch-failures.md")
    if not t:
        return "SKIP", "no failure log"
    rows = [l for l in t.split("\n") if l.startswith("| `") or l.startswith("- `")]
    outstanding = [l for l in rows if "Outstanding" in l or "**Partial**" in l]
    if outstanding:
        return "WARN", ("%d source(s) still outstanding. Each needs an outcome before "
                        "shipping: retried, permanently unavailable (then stated as an "
                        "absence), or needs a human." % len(outstanding))
    return "PASS", "no outstanding fetch failures"


def hypotheses_resolved():
    t = read("docs/STRATEGY.md")
    if not t:
        return "SKIP", "no STRATEGY.md"
    facts = read("docs/FACTS.md") or ""
    if len([r for r in facts_rows() if len(r) >= 4]) < 12:
        return "SKIP", "research has not run yet"
    n = len(re.findall(r"^\| \d+ \|", t, re.M))
    return "WARN", ("%d hypotheses are on file. Each must end the project evidenced or "
                    "explicitly killed — a hypothesis quietly dropped is a bias. This "
                    "check counts them; only you can confirm they were resolved." % n)


CHECKS = [
    ("data/ is CSV only", data_is_csv_only),
    ("every CSV carries evidence", sources_have_evidence_column),
    ("FACTS rows graded and sourced", facts_are_sourced),
    ("conflicts carry rulings", conflicts_have_rulings),
    ("deck builds with notes", deck_builds),
    ("record covers every slide", slides_covered_by_record),
    ("record div balance", record_div_balance),
    ("slide figures exist in FACTS", slide_numbers_are_in_facts),
    ("fetch failures resolved", failures_are_resolved),
    ("hypotheses resolved", hypotheses_resolved),
]

SYM = {"PASS": "✓", "WARN": "!", "FAIL": "✗", "SKIP": "·"}


def main():
    strict = "--strict" in sys.argv
    print("%s — verification\n%s" % (config.COMPANY, "=" * 72))
    for name, fn in CHECKS:
        check(name, fn)
    for state, name, detail in results:
        print("  %s %-32s %s" % (SYM[state], name, detail))

    counts = {k: sum(1 for r in results if r[0] == k) for k in SYM}
    print("=" * 72)
    print("  %d passed · %d warnings · %d failed · %d not applicable yet"
          % (counts["PASS"], counts["WARN"], counts["FAIL"], counts["SKIP"]))
    if counts["FAIL"]:
        print("\nFailures are rule violations, not opinions. Fix them before shipping.")
    if strict and counts["FAIL"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
