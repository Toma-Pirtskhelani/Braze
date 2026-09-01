import os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# -*- coding: utf-8 -*-
"""Assemble deck/evidence-record.html from deck/record/*.md + FACTS.md + the built deck.

WHY THIS IS GENERATED RATHER THAN WRITTEN

The reference project's first evidence record was written by hand in deck order, and the
same finding ended up in four sections, each carrying a caveat the others lacked. A
reader of any single telling was misinformed. Fixing it was a rewrite, not an edit.

Generating it enforces the architecture that prevents that:

  ONE FACT, ONE HOME.  Each chapter is one file. A fact appearing in two chapter files
  is caught here, by name, before it ships.

  THE SLIDE MAP IS DERIVED FROM THE BUILT DECK, so it cannot claim coverage it does not
  have. The reference project once shipped a record claiming to map 41 slides. It mapped
  34. That is not possible here.

Write chapters as markdown in deck/record/NN-name.md. The supported subset is
deliberately small - headings, paragraphs, bold, code, links, lists, tables,
blockquotes - plus two additions:

    [[audited]]  [[documented]]  [[third-party]]  [[claimed]]  [[conflicted]]
        renders an evidence-grade badge

    {{src: sources/docs/foo.md:120-160 @ 2026-09-01}}
        renders a citation line

Usage:  python3 deck/build_record.py
"""
import glob
import html as H
import re
import sys

sys.path.insert(0, os.path.join(REPO, "tools"))
try:
    import config
    COMPANY, DECK_FILE = config.COMPANY, config.DECK_FILE
except Exception:                                   # noqa: BLE001
    COMPANY, DECK_FILE = "Vendor", "deck.html"

RECORD_DIR = os.path.join(HERE, "record")
GRADES = {"audited": "g-audited", "infrastructure": "g-infra", "documented": "g-doc",
          "third-party": "g-third", "claimed": "g-claim", "conflicted": "g-claim"}


# ── a small, predictable markdown subset ─────────────────────────────────────

def inline(t):
    t = H.escape(t)
    t = re.sub(r"\{\{src:\s*(.+?)\}\}", r'<span class="src">source: <code>\1</code></span>', t)
    t = re.sub(r"\[\[([a-z-]+)\]\]",
               lambda m: '<span class="g %s">%s</span>' % (GRADES.get(m.group(1), "g-claim"), m.group(1)),
               t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def md(text):
    out, i = [], 0
    lines = text.split("\n")
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("|"):                      # table
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i])
                i += 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in block]
            body = [r for r in cells if not re.match(r"^[-: ]+$", "".join(r))]
            head, rest = body[0], body[1:]
            out.append('<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                       % ("".join("<th>%s</th>" % inline(c) for c in head),
                          "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r)
                                  for r in rest)))
            continue
        if re.match(r"^[-*] ", ln):                 # list
            items = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i]):
                items.append(inline(lines[i][2:]))
                i += 1
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in items))
            continue
        if ln.startswith(">"):                      # thesis
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip("> ").rstrip())
                i += 1
            out.append('<p class="thesis">%s</p>' % inline(" ".join(block)))
            continue
        m = re.match(r"^(#{1,4}) +(.*)$", ln)
        if m:
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl + 1, inline(m.group(2)), lvl + 1))
            i += 1
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^([-*>|#])", lines[i]):
            para.append(lines[i].strip())
            i += 1
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
    return "\n".join(out)


# ── inputs ───────────────────────────────────────────────────────────────────

def chapters():
    files = sorted(glob.glob(os.path.join(RECORD_DIR, "*.md")))
    if not files:
        raise SystemExit(
            "deck/record/ holds no chapters.\n"
            "Write one markdown file per subject chapter (01-company.md, 02-money.md, …).\n"
            "See docs/RECORD-SPEC.md for the eight-chapter structure and the rule that\n"
            "matters: a fact belongs to exactly one chapter, and everything else points at it.")
    out = []
    for n, p in enumerate(files, 1):
        raw = open(p, encoding="utf-8").read()
        m = re.match(r"^#\s+(.*)$", raw.split("\n")[0])
        title = m.group(1) if m else os.path.basename(p)[:-3]
        body = raw.split("\n", 1)[1] if m else raw
        sm = re.search(r"\{\{slides:\s*([\d,\s\-]+)\}\}", raw)
        slides = set()
        if sm:
            for part in sm.group(1).split(","):
                part = part.strip()
                if "-" in part:
                    a, b = part.split("-")
                    slides.update(range(int(a), int(b) + 1))
                elif part:
                    slides.add(int(part))
        body = re.sub(r"\{\{slides:[^}]*\}\}", "", body)
        out.append({"n": n, "id": "c%d" % n, "title": title, "slides": slides,
                    "body": md(body), "text": raw, "file": os.path.basename(p)})
    return out


def slide_map(chs):
    """Derived from the BUILT deck, so coverage cannot be claimed falsely."""
    p = os.path.join(HERE, DECK_FILE)
    if not os.path.exists(p):
        return "", 0, []
    deck = open(p, encoding="utf-8").read()
    rows, unmapped, titles = [], [], []
    for i, sec in enumerate(re.findall(r'(<section class="s[^"]*".*?</section>)', deck, re.S), 1):
        m = re.search(r'data-t="([^"]*)"', sec)
        if not m:
            continue
        t = m.group(1)
        titles.append(t)
        clean = H.unescape(re.sub(r"<[^>]+>", "", t))
        # A chapter may claim slides explicitly with `{{slides: 1, 4, 12}}`. That is
        # authoritative; title matching is only the fallback, and it is fuzzy by nature.
        hits = [c for c in chs if i in c["slides"]]
        if not hits:
            hits = [c for c in chs if not c["slides"] and
                    (clean.lower() in c["text"].lower() or t.lower() in c["text"].lower())]
        if hits:
            ref = " ".join('<a href="#%s">§%d</a>' % (c["id"], c["n"]) for c in hits)
        elif not re.search(r"\d", re.sub(r"<[^>]+>", " ", sec)):
            # A slide carrying no figure asserts nothing that needs proving. Frame and
            # method slides land here. This is a rule, not an exception list, so it keeps
            # working as the deck changes.
            ref = '<span class="src">no evidence claimed</span>'
        else:
            ref = '<span class="todo">not yet in the record</span>'
            unmapped.append("%02d %s" % (i, clean))
        rows.append("<tr><td>%02d</td><td>%s</td><td>%s</td></tr>" % (i, t, ref))
    return ("<div class=\"tw\"><table><thead><tr><th>#</th><th>Slide</th>"
            "<th>Record</th></tr></thead><tbody>%s</tbody></table></div>"
            % "".join(rows)), len(titles), unmapped


def duplicate_facts(chs):
    """A number appearing in two chapters is the failure this design exists to prevent."""
    num = re.compile(r"(?<![\w.$])(\d[\d,]{3,}(?:\.\d+)?|\d+\.\d+%)")
    where = {}
    for c in chs:
        for v in set(num.findall(c["text"])):
            where.setdefault(v, []).append(c["file"])
    return {v: f for v, f in where.items() if len(f) > 1}


CSS = """
:root{--paper:#FBFAF8;--ink:#1A1D23;--muted:#5D6675;--rule:#E2DFD8;--rule2:#CFCABF;
 --accent:#2C4A7C;--g-audited:#2F6B4F;--g-infra:#3E6B8A;--g-doc:#6B7A2F;--g-third:#B07B1E;
 --g-claim:#A6472F;--disp:"Newsreader",Georgia,serif;--body:"Public Sans",system-ui,sans-serif;
 --mono:"JetBrains Mono",ui-monospace,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#14171C;--ink:#E8E6E1;
 --muted:#98A0AD;--rule:#262B33;--rule2:#39404B;--accent:#7FA8DC}}
:root[data-theme="dark"]{--paper:#14171C;--ink:#E8E6E1;--muted:#98A0AD;--rule:#262B33;
 --rule2:#39404B;--accent:#7FA8DC}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.6;font-size:16px}
.w{max-width:52rem;margin:0 auto;padding:2rem 1.5rem 6rem}
h1,h2,h3,h4{font-family:var(--disp);font-weight:600;line-height:1.25;text-wrap:balance}
h1{font-size:2.5rem;margin-bottom:.4rem}
h2{font-size:1.85rem;margin:3rem 0 .5rem;padding-top:1.4rem;border-top:2px solid var(--rule2)}
h3{font-size:1.2rem;margin:1.8rem 0 .4rem}
h4{font-size:1rem;margin:1.2rem 0 .3rem;color:var(--muted)}
p{margin:.7rem 0} ul{margin:.7rem 0 .7rem 1.2rem} li{margin:.25rem 0}
a{color:var(--accent)}
.thesis{font-family:var(--disp);font-size:1.14rem;line-height:1.5;border-left:3px solid var(--accent);
 padding:.35rem 0 .35rem 1rem;margin:.9rem 0 1.4rem}
.tw{overflow-x:auto;margin:1.1rem 0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{text-align:left;padding:.45rem .7rem;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-family:var(--mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
code{font-family:var(--mono);font-size:.86em}
.g{font-family:var(--mono);font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;
 padding:.1rem .42rem;border-radius:3px;color:#fff;white-space:nowrap}
.g-audited{background:var(--g-audited)}.g-infra{background:var(--g-infra)}
.g-doc{background:var(--g-doc)}.g-third{background:var(--g-third)}.g-claim{background:var(--g-claim)}
.src{font-family:var(--mono);font-size:.76rem;color:var(--muted);display:block;margin:.2rem 0 .6rem}
.todo{color:var(--g-claim);font-family:var(--mono);font-size:.76rem}
.box{background:color-mix(in srgb,var(--rule) 40%,transparent);border:1px solid var(--rule);
 border-radius:6px;padding:.9rem 1.15rem;margin:1.1rem 0}
nav.parts{position:sticky;top:0;background:var(--paper);border-bottom:1px solid var(--rule);
 padding:.55rem 0;font-family:var(--mono);font-size:.71rem;display:flex;gap:.9rem;flex-wrap:wrap;z-index:5}
@media print{@page{size:A4 portrait;margin:15mm 14mm 16mm}
 *{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
 body{font-size:9.6pt}nav.parts{display:none!important}.w{max-width:none;padding:0}
 section.part{break-before:page}.box,.tw,table,tr,li{break-inside:avoid}
 thead{display:table-header-group}h1,h2,h3,h4,.thesis{break-after:avoid}
 a[href^="http"]::after{content:" (" attr(href) ")";font-size:7pt;color:var(--muted)}}
"""


def main():
    chs = chapters()
    smap, n_slides, unmapped = slide_map(chs)
    dupes = duplicate_facts(chs)

    nav = "".join('<a href="#%s">%d %s</a>' % (c["id"], c["n"], c["title"].split("·")[-1].strip()[:18])
                  for c in chs)
    parts = "".join(
        '<section class="part" id="%s"><h2>%d · %s</h2>%s</section>'
        % (c["id"], c["n"], c["title"], c["body"]) for c in chs)

    doc = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s — evidence record</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:wght@400;500;600;700&family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">
<style>%s</style></head><body>
<nav class="parts">%s<a href="#map">Slide map</a></nav>
<div class="w">
<header><h1>%s — evidence record</h1>
<p class="src">Public sources only · every claim graded and traceable</p>
<div class="box"><p><strong>How to read this.</strong> The chapters are the
<em>Record</em>: every fact is stated <strong>once</strong>, in full, with its caveats in
the same sentence as the number. The <a href="#map">Slide Map</a> is the deck in order and
holds no evidence — it points back into the chapters.</p>
<p>Grades run <span class="g g-audited">audited</span>
<span class="g g-infra">infrastructure</span> <span class="g g-doc">documented</span>
<span class="g g-third">third-party</span> <span class="g g-claim">claimed</span>, ordered by
how hard it would be for the vendor to have made the statement untrue.
<strong>A claim takes the grade of its weakest source.</strong></p></div></header>
%s
<section class="part" id="map"><h2>Slide map</h2>
<p>The deck in order, generated from the built deck so coverage cannot be overstated.
No evidence lives here — if a number appears in this table it belongs in a chapter.</p>
%s</section>
</div></body></html>""" % (COMPANY, CSS, nav, COMPANY, parts, smap or "<p>Deck not built yet.</p>")

    out = os.path.join(HERE, "evidence-record.html")
    open(out, "w", encoding="utf-8").write(doc)

    o, c = len(re.findall(r"<div\b", doc)), doc.count("</div>")
    print("chapters: %d  (%s)" % (len(chs), ", ".join(c["file"] for c in chs)))
    print("slides mapped: %d of %d" % (n_slides - len(unmapped), n_slides))
    print("divs: %d open / %d close  %s" % (o, c, "balanced" if o == c else "** UNBALANCED **"))
    print("bytes: %d -> deck/evidence-record.html" % len(doc))
    if unmapped:
        print("\nNOT YET IN THE RECORD — every slide needs a chapter that proves it:")
        for u in unmapped:
            print("   %s" % u)
    if dupes:
        print("\nONE FACT, ONE HOME — these figures appear in more than one chapter:")
        for v, files in sorted(dupes.items())[:10]:
            print("   %-14s %s" % (v, ", ".join(files)))
        print("   Keep each in a single chapter and point at it from the others.")


if __name__ == "__main__":
    main()
