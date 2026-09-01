import os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# -*- coding: utf-8 -*-
"""Generate the speaker script straight from the deck, so the two never drift.

This reads the same slide modules the deck is built from. Change a slide, rerun both,
and the script cannot disagree with what is on screen - which it will, every time, if
the script is maintained by hand.

PARTS below maps a slide number to the section heading printed above it. Update it
when the deck's structure changes; the numbers are 1-based slide positions.
"""
import glob
import html
import re
import sys

sys.path.insert(0, HERE)
import lib                                          # noqa: E402

for m in sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "slides_*.py"))):
    __import__(m)

S = lib.SLIDES
if not S:
    raise SystemExit("no slides - run deck/build_deck.py first to see the same error")

PARTS = {
    1: "Part 0 — Frame",
    4: "Part I — The company",
    # 18: "Part II — The product",
    # 33: "Part III — Strategy",
    # 37: "Part IV — Open questions",
}
WPM = 130


def txt(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t)).strip()


def onscreen(h):
    m = re.search(r'<h1>(.*?)</h1>', h, re.S) or re.search(r'<h2>(.*?)</h2>', h, re.S)
    head = txt(m.group(1)) if m else ''
    e = (re.search(r'class="eyebrow">(.*?)</div>', h, re.S)
         or re.search(r'class="pn">(.*?)</div>', h, re.S))
    return (txt(e.group(1)) if e else ''), head


HEADER = """# Speaker script

Every slide of the deck, in order: what the audience sees, and what to say over it.
Generated from the deck itself, so slide numbers and titles can never drift apart.

**{words:,} spoken words — about {mins} minutes at a normal pace, {secs} seconds a slide.**

**Bold** marks the words to land on. Square brackets are notes to yourself, not lines
to say. Press **N** in the deck to read these beside the slide.

---
"""

out = [""]
for i, s in enumerate(S, 1):
    if i in PARTS:
        out.append(f"\n## {PARTS[i]}\n")
    eye, head = onscreen(s["html"])
    out.append(f"### {i:02d} · {html.unescape(s['label'])}")
    if head:
        out.append(f"*On screen:* {(eye + ' — ') if eye else ''}**{head}**")
    out.append("")
    for para in s["notes"].split("\n\n"):
        out.append("> " + para.strip().replace("\n", "\n> "))
        out.append("")

p = os.path.join(REPO, 'docs', 'PRESENTATION-SCRIPT.md')
words = len(re.findall(r"\w+", "\n".join(s["notes"] for s in S)))
out[0] = HEADER.format(words=words, mins=max(1, round(words / WPM)),
                       secs=round(words / WPM * 60 / len(S)))
os.makedirs(os.path.dirname(p), exist_ok=True)
open(p, 'w', encoding='utf-8').write("\n".join(out).rstrip() + "\n")
print(f"wrote docs/PRESENTATION-SCRIPT.md: {len(S)} slides, {words} spoken words, "
      f"~{words/WPM:.0f} min at {WPM} wpm")
