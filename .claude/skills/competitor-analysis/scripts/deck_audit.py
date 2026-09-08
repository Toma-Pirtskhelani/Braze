#!/usr/bin/env python3
"""Audit the deck as a PRESENTATION, not as an evidence base.

    python3 tools/deck_audit.py
    python3 tools/deck_audit.py --reference /path/to/reference-deck.html
    python3 tools/deck_audit.py --strict          # exit 1 on any FAIL

WHY THIS EXISTS

tools/verify.py has ten checks and every one is about evidence discipline: is the
number sourced, is the conflict ruled on, does the record cover the slide. On the
reference project it reported 9 passed / 0 failed on a deck that then needed four
rounds of human review before it was presentable.

A gate that passes everything is not a gate. This is the other half: the checks that
catch a deck which is perfectly sourced and unwatchable. Every check below was
derived from a defect found by a human reader AFTER an automated pass said the deck
was fine, so each one has already earned its place once.

None of these is a matter of taste. Each measures something that was wrong, was
found by a person, and cost a rework cycle.
"""
import argparse
import html
import json
import os
import re
import statistics as st

# ── the two headline kinds ───────────────────────────────────────────────────
# A LABEL is a noun phrase for orientation. A CLAIM states a finding. Claim power is
# inversely proportional to frequency: a deck where every headline argues has no
# emphasis left. The reference deck runs 70/29; a deck at 39/58 reads as shouting.
VERB = re.compile(
    r"\b(is|are|was|were|has|have|had|do|does|did|can|will|would|"
    r"bought|buys|run|runs|ran|paid|pays|publish|publishes|weigh|weighs|"
    r"comes|come|came|depends|depend|falling|fell|rising|rose|designs|presses|"
    r"names|name|hiring|takes|took|draws|answered|answers|expected|expects|"
    r"close|closes|remember|return|returns|fail|fails|says|said|marketed|"
    r"documented|sells|sold|costs|cost|means|meant|shows|showed|carries|carry|"
    r"lands|landed|leaves|left|keeps|kept|holds|held|gets|got|makes|made)\b", re.I)

# Language pointing at the VENDOR'S BUSINESS - what the audience should do about it.
SOWHAT = re.compile(
    r"\b(means?|matters?|so if|for a buyer|buyers?|competitors?|advantage|risks?|"
    r"depends?|leverage|exposed|threat|opportunit\w*|cannot copy|beat|wins?|loses?|"
    r"switch\w*|lock.?in|negotiat\w*|displace|defend\w*|vulnerab\w*|costs? you|"
    r"you should|worth asking|ask them|decide|choose)\b", re.I)

# Language pointing at the ANALYSIS ITSELF - how the analyst knows. Necessary, but a
# deck that runs two-to-one this way is talking to itself.
METHOD = re.compile(
    r"\b(disclosur\w*|documented|corpus|sources?|captur\w*|graded?|evidence|"
    r"traceab\w*|verif\w*|recorded|stated|public sources|says what|we did not|"
    r"not visible|filed|audited|re-?deriv\w*|provenance|methodolog\w*)\b", re.I)

# Terms an audience does not arrive knowing. Extend per project; the point is that a
# term's FIRST use must sit near a definition, not that these exact words are banned.
JARGON = ["10-K", "10-Q", "DEF 14A", "proxy statement", "earn-out", "goodwill",
          "material weakness", "sub-processor", "subprocessor", "RPO", "ITGC",
          "allowlist", "XBRL", "holdout", "attestation", "purchase-price allocation",
          "remaining performance obligation", "dual-class", "S-1"]
# A definition looks like a parenthetical or a dash-gloss within this many characters
DEFINE_WINDOW = 110

BUDGETS = {
    "label_ratio_min": 0.55,     # at least 55% of headlines are labels
    "headline_words_mean_max": 6.5,
    "headline_words_max": 11,
    "claim_run_max": 3,          # consecutive claim headlines
    "body_words_max": 130,       # per slide, excluding the headline
    "body_words_mean_max": 115,
    "sowhat_ratio_min": 0.60,    # so-what : method, on slide
    "min_images": 3,
}


def load(path):
    """-> [ {n, label, grade, head, body_words, text, notes, notes_words, imgs, html} ]"""
    raw = open(path, encoding="utf-8").read()
    doc = re.sub(r"(?s)<script.*?</script>", " ", raw)
    doc = re.sub(r'src="data:[^"]*"', 'src="[img]"', doc)
    out = []
    for i, sec in enumerate(re.findall(r'(<section class="s[^"]*".*?</section>)', doc, re.S), 1):
        t = re.search(r'data-t="([^"]*)"', sec)
        g = re.search(r'data-g="([^"]*)"', sec)
        h = (re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S)
             or re.search(r"<h1[^>]*>(.*?)</h1>", sec, re.S))
        head = " ".join(html.unescape(re.sub(r"<[^>]+>", "", h.group(1))).split()) if h else ""
        text = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", sec)).split())
        body = text
        if head:                                   # body = everything after the headline
            body = text.replace(head, " ", 1)
        out.append({
            "n": i,
            "label": html.unescape(t.group(1)) if t else "",
            "grade": g.group(1) if g else "",
            "head": head,
            "head_words": len(head.split()) if head else 0,
            "kind": ("" if not head else ("CLAIM" if VERB.search(head) else "LABEL")),
            "body_words": len(body.split()),
            "text": text,
            "imgs": len(re.findall(r"<img", sec)),
            "html": sec,
        })
    m = re.search(r"const NOTES=(\[.*?\]), LABELS=", raw, re.S)
    if m:
        notes = [re.sub("<[^>]+>", "", x) for x in json.loads(m.group(1))]
        for s, n in zip(out, notes):
            s["notes"] = n
            s["notes_words"] = len(n.split())
    return out


# ── checks ───────────────────────────────────────────────────────────────────

def chk_headline_mix(slides):
    heads = [s for s in slides if s["head"]]
    if not heads:
        return "SKIP", "no headlines found", None
    lab = sum(1 for s in heads if s["kind"] == "LABEL")
    cla = len(heads) - lab
    ratio = lab / len(heads)
    detail = "%d labels / %d claims (%.0f%% labels)" % (lab, cla, 100 * ratio)
    if ratio < BUDGETS["label_ratio_min"]:
        return "FAIL", (detail + " — every slide argues, so none of them lands. "
                        "Convert the weakest claims to plain labels."), ratio
    return "PASS", detail, ratio


def chk_claim_runs(slides):
    heads = [s for s in slides if s["head"]]
    run = best = 0
    where = 0
    for s in heads:
        run = run + 1 if s["kind"] == "CLAIM" else 0
        if run > best:
            best, where = run, s["n"]
    if best > BUDGETS["claim_run_max"]:
        return "FAIL", ("%d consecutive claim headlines, ending at slide %d — the "
                        "audience stops hearing them as claims" % (best, where)), best
    return "PASS", "longest run of consecutive claims: %d" % best, best


def chk_headline_length(slides):
    w = [s["head_words"] for s in slides if s["head"]]
    if not w:
        return "SKIP", "no headlines", None
    mean = st.mean(w)
    longest = max(slides, key=lambda s: s["head_words"])
    bad = [s for s in slides if s["head_words"] > BUDGETS["headline_words_max"]]
    detail = "mean %.1f words, longest %d (slide %d)" % (mean, longest["head_words"], longest["n"])
    if mean > BUDGETS["headline_words_mean_max"] or bad:
        return "WARN", (detail + (" — %d over %d words: %s"
                        % (len(bad), BUDGETS["headline_words_max"],
                           ", ".join(str(s["n"]) for s in bad[:6])) if bad else "")), mean
    return "PASS", detail, mean


# A CHECK THAT WAS BUILT AND DELETED, recorded so nobody builds it again.
#
# "A headline must not use a word the slide never says" sounds right — it comes from a
# real defect, where a slide headed "the complaints are about progression" never used
# the word progression and the reader went looking for it.
#
# Implemented, it fired on 23-36 of 43 slides at every threshold tried, and inspection
# showed the hits were good writing:
#   "Nobody publishes a price"      — a conclusion; the body carries the evidence for it
#   "Only two channels have a named middleman" — plain-English gloss of "sub-processor"
#   "Canvas is the strongest thing in the platform" — a verdict drawn from the counts
#
# A claim headline is SUPPOSED to synthesise. Requiring its words to appear literally
# pushes the deck toward restating its own body, which is the opposite of the goal.
# The original defect was about salience, not vocabulary, and salience is not
# mechanically checkable. Left to the covered-slide test a human runs.
#
# The general lesson, already in docs/METHOD.md: a checker that cries wolf gets
# ignored, and tuning a wrong check until it goes quiet is worse than deleting it.


def chk_body_density(slides):
    w = [s["body_words"] for s in slides]
    mean = st.mean(w)
    over = [s for s in slides if s["body_words"] > BUDGETS["body_words_max"]]
    detail = "mean %.0f words/slide, %d over %d" % (mean, len(over), BUDGETS["body_words_max"])
    if mean > BUDGETS["body_words_mean_max"] or len(over) > len(slides) * 0.25:
        return "WARN", (detail + " — the screen is doing the presenter's job; move the "
                        "overflow into the notes: " +
                        ", ".join(str(s["n"]) for s in over[:8])), mean
    return "PASS", detail, mean


def chk_sowhat(slides):
    """Does the deck talk about the vendor's business, or about its own evidence?"""
    body = " ".join(s["text"] for s in slides)
    sw, me = len(SOWHAT.findall(body)), len(METHOD.findall(body))
    ratio = sw / max(me, 1)
    detail = "so-what %d : method %d = %.2f" % (sw, me, ratio)
    if ratio < BUDGETS["sowhat_ratio_min"]:
        return "FAIL", (detail + " — the deck describes its own evidence more than what "
                        "that evidence means. End each substantive slide on a line "
                        "addressed to the audience, not to the analyst."), ratio
    return "PASS", detail, ratio


def chk_jargon(slides):
    """Every specialist term must be defined at or before first use."""
    undefined = []
    for term in JARGON:
        first = None
        for s in slides:
            if re.search(re.escape(term), s["text"], re.I):
                first = s
                break
        if not first:
            continue
        m = re.search(re.escape(term), first["text"], re.I)
        window = first["text"][m.start(): m.end() + DEFINE_WINDOW]
        if not re.search(r"[(—–-]", window):     # paren or dash gloss nearby
            undefined.append((term, first["n"]))
    if undefined:
        return "WARN", ("%d term(s) used before being defined: %s"
                        % (len(undefined),
                           "; ".join("%s (slide %d)" % u for u in undefined[:6]))), len(undefined)
    return "PASS", "every specialist term is glossed at first use", 0


def chk_images(slides):
    n = sum(s["imgs"] for s in slides)
    on = [s["n"] for s in slides if s["imgs"]]
    if n < BUDGETS["min_images"]:
        return "FAIL", ("%d image(s) in the whole deck — a deck of type and rules reads "
                        "as a document being narrated. The CSS ships .mark, .plate, "
                        ".brandtag and .portrait; use them." % n), n
    return "PASS", "%d images on slides %s" % (n, ",".join(map(str, on))), n


GRADE_CLASSES = re.compile(r'class="[^"]*\b(acc|mk-[smw])\b')


def chk_grade_colour(slides):
    """Grade colours are the evidence system. Reusing amber to mean anything else
    teaches the audience one meaning on slide 3 and contradicts it later."""
    hits = [s["n"] for s in slides if GRADE_CLASSES.search(s["html"])]
    if hits:
        return "WARN", ("grade-accent classes used on slides %s — confirm each carries an "
                        "EVIDENCE meaning, not a second one"
                        % ",".join(map(str, hits[:8]))), len(hits)
    return "PASS", "no grade colours reused for other meanings", 0


def chk_notes(slides):
    if "notes_words" not in slides[0]:
        return "SKIP", "no speaker notes found", None
    w = [s["notes_words"] for s in slides]
    thin = [s["n"] for s in slides if s["notes_words"] < 60]
    detail = "mean %d words, longest %d, median %d" % (st.mean(w), max(w), st.median(w))
    if thin:
        return "WARN", (detail + " — %d slide(s) under 60 words: %s"
                        % (len(thin), ",".join(map(str, thin[:8])))), st.mean(w)
    return "PASS", detail, st.mean(w)


CHECKS = [
    ("headline mix (label:claim)", chk_headline_mix),
    ("no long runs of claims", chk_claim_runs),
    ("headline length", chk_headline_length),
    ("body density", chk_body_density),
    ("so-what vs method language", chk_sowhat),
    ("jargon defined at first use", chk_jargon),
    ("deck has a visual language", chk_images),
    ("grade colours mean grades", chk_grade_colour),
    ("speaker notes", chk_notes),
]

SYM = {"PASS": "✓", "WARN": "!", "FAIL": "✗", "SKIP": "·"}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", nargs="?", help="path to the built deck (default: auto-detect)")
    ap.add_argument("--reference", help="a deck to compare against, head to head")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any FAIL")
    a = ap.parse_args()

    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = a.deck
    if not path:
        cand = [f for f in os.listdir(os.path.join(here, "deck"))
                if f.endswith("-deck.html")]
        if not cand:
            raise SystemExit("no deck found - build it first, or pass a path")
        path = os.path.join(here, "deck", cand[0])

    slides = load(path)
    if not slides:
        raise SystemExit("no slides parsed from %s" % path)

    print("%s\n%d slides\n%s" % (os.path.basename(path), len(slides), "=" * 74))
    results, values = [], {}
    for name, fn in CHECKS:
        try:
            state, detail, val = fn(slides)
        except Exception as e:                     # noqa: BLE001 - a broken check is a fail
            state, detail, val = "FAIL", "check raised: %s" % e, None
        results.append((state, name, detail))
        values[name] = val
        print("  %s %-30s %s" % (SYM[state], name, detail))

    counts = {k: sum(1 for r in results if r[0] == k) for k in SYM}
    print("=" * 74)
    print("  %d passed · %d warnings · %d failed · %d skipped"
          % (counts["PASS"], counts["WARN"], counts["FAIL"], counts["SKIP"]))

    if a.reference and os.path.exists(a.reference):
        ref = load(a.reference)
        print("\nversus %s (%d slides)\n%s"
              % (os.path.basename(a.reference), len(ref), "=" * 74))
        print("  %-30s %>12s %>12s".replace(">", "") % ("metric", "this deck", "reference"))
        for name, fn in CHECKS:
            try:
                _, _, mine = fn(slides)
                _, _, theirs = fn(ref)
            except Exception:                      # noqa: BLE001
                continue
            if mine is None or theirs is None:
                continue
            fmt = (lambda v: "%.2f" % v) if isinstance(mine, float) else (lambda v: "%d" % v)
            flag = ""
            if isinstance(mine, (int, float)) and isinstance(theirs, (int, float)):
                worse = (name in ("headline mix (label:claim)", "so-what vs method language")
                         and mine < theirs) or \
                        (name in ("body density", "headline length", "no long runs of claims")
                         and mine > theirs)
                flag = "  <- worse" if worse else ""
            print("  %-30s %12s %12s%s" % (name, fmt(mine), fmt(theirs), flag))

    if counts["FAIL"]:
        print("\nFailures are craft defects, not opinions. Each one below cost the "
              "reference project a full rework cycle.")
    if a.strict and counts["FAIL"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
