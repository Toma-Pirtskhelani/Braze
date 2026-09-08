import os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# -*- coding: utf-8 -*-
"""Generate the speaker script straight from the deck, so the two never drift.

This reads the same slide modules the deck is built from. Change a slide, rerun both,
and the script cannot disagree with what is on screen - which it will, every time, if
the script is maintained by hand.

WHAT CHANGED, AND WHY IT MATTERS

The first version of this emitted only the eyebrow and the headline under "On screen",
and the speaker notes under it. That made the document unreadable on its own: the notes
say "look at the third figure" and "note the seven documentation pages" while the figures
and the counts were nowhere in the file. Every number on all 43 slides was missing, and
the header claimed otherwise.

So this now renders the slide BODY as well - every component the design system can
produce, turned into markdown. The file is a speaker script for a presenter and a
complete standalone document for a reader, and it can be neither if it omits the data
the narration is about.

PARTS maps a 1-based slide number to the section heading printed above it, and CHAPTERS
points each part at the evidence-record chapters that carry its reasoning.
"""
import glob
import html
import re
import sys
from html.parser import HTMLParser

sys.path.insert(0, HERE)
import lib                                          # noqa: E402

for m in sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "slides_*.py"))):
    __import__(m)

S = lib.SLIDES
if not S:
    raise SystemExit("no slides - run deck/build_deck.py first to see the same error")

PARTS = {
    1:  ("Part 0 — Frame", "How to judge everything that follows."),
    4:  ("Part I — The company", "Who they are, what they bought, what it costs, who buys it."),
    18: ("Part II — The product", "One campaign through seven stages, then the platform around it."),
    33: ("Part III — Strategy", "Where the money goes, what is coming, what protects them."),
    37: ("Part IV — Open questions", "What is unresolved, what went the other way, and what to do next."),
}

# Where to read further. These are the evidence-record chapters that carry the reasoning
# behind each part - the script gives the argument, the record gives the working.
CHAPTERS = {
    1:  "`deck/record/08-open.md` §8.0a — the four documents, and why they are hard to falsify.",
    4:  "`deck/record/01-company.md`, `02-money.md`, `03-acquisitions.md`, `07-market.md`.",
    18: "`deck/record/04-platform.md`, `05-channels.md`, `06-ai.md`.",
    33: "`deck/record/02-money.md` §2.3–2.4, `04-platform.md` §4.5.",
    37: "`deck/record/08-open.md` — the open questions, the corrections log, the hypothesis ledger.",
}
WPM = 130
READ_WPM = 240          # silent reading of a familiar-register document


# ── a very small HTML tree, enough for the components in deck/lib.py ────────────
class Node:
    __slots__ = ("tag", "cls", "kids", "text")

    def __init__(self, tag="", cls=""):
        self.tag, self.cls, self.kids, self.text = tag, cls, [], ""

    def has(self, c):
        return c in self.cls.split()


class Tree(HTMLParser):
    VOID = {"img", "br", "hr", "input", "meta", "link", "use", "path", "circle",
            "rect", "line", "polygon", "polyline", "ellipse"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        n = Node(tag, d.get("class", ""))
        self.stack[-1].kids.append(n)
        if tag not in self.VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].kids.append(Node(tag, dict(attrs).get("class", "")))

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if not data:
            return
        n = Node("#text")
        # whitespace between two inline tags is a word boundary, not nothing
        n.text = data if data.strip() else " "
        self.stack[-1].kids.append(n)


def parse(h):
    t = Tree()
    t.feed(h)
    return t.root


def flat(n):
    """All text under a node, whitespace-collapsed, <strong>/<em> preserved as markdown."""
    out = []

    def walk(x):
        if x.tag == "#text":
            out.append(x.text)
            return
        if x.tag in ("strong", "b"):
            inner = flat_inner(x)
            out.append("**" + inner + "**" if inner else "")
            return
        if x.tag in ("em", "i"):
            inner = flat_inner(x)
            out.append("*" + inner + "*" if inner else "")
            return
        for k in x.kids:
            walk(k)

    def flat_inner(x):
        s = []
        for k in x.kids:
            s.append(k.text if k.tag == "#text" else flat(k))
        return re.sub(r"\s+", " ", "".join(s)).strip()

    for k in n.kids:
        walk(k)
    return re.sub(r"\s+", " ", "".join(out)).strip()


def find(n, cls):
    """Direct-ish descendants carrying a class, not descending into a match."""
    hits = []

    def walk(x):
        for k in x.kids:
            if k.has(cls):
                hits.append(k)
            else:
                walk(k)
    walk(n)
    return hits


def first(n, tag):
    for k in n.kids:
        if k.tag == tag:
            return k
        r = first(k, tag)
        if r:
            return r
    return None


def child_text(n, cls):
    for h in find(n, cls):
        return flat(h)
    return ""


# ── component renderers ────────────────────────────────────────────────────────
def render(n, depth=0):
    """Turn one body-level node into markdown lines."""
    o = []

    if n.tag == "#text":
        t = re.sub(r"\s+", " ", n.text).strip()
        return [t] if t else []

    if n.tag == "svg":
        texts = []

        def grab(x):
            if x.tag == "text":
                t = flat(x)
                if t:
                    texts.append(t)
            for k in x.kids:
                grab(k)
        grab(n)
        return ["*Diagram:* " + " · ".join(texts)] if texts else ["*[diagram]*"]

    if n.has("head"):
        return []                                                # emitted separately

    if n.has("bars"):
        for r in find(n, "barrow"):
            o.append(f"- {child_text(r, 'bl')} · **{child_text(r, 'bv')}**")
        return o

    if n.has("figrow") or n.has("statrow"):
        for f in find(n, "fig") + find(n, "stat"):
            v = child_text(f, "fv") or child_text(f, "n")
            l = child_text(f, "fl") or child_text(f, "l")
            o.append(f"- **{v}** — {l}")
        return o

    if n.has("cards"):
        for c in find(n, "card"):
            h3 = first(c, "h3")
            p = first(c, "p")
            o.append(f"- **{flat(h3) if h3 else ''}** — {flat(p) if p else ''}")
        return o

    if n.has("tiles"):
        for t in find(n, "tile"):
            o.append(f"- **{child_text(t, 'tt') or child_text(t, 'gh')}** — "
                     f"{child_text(t, 'td')}")
        return o

    if n.has("flow"):
        for st in find(n, "step"):
            si, stt, sd = child_text(st, "si"), child_text(st, "st"), child_text(st, "sd")
            o.append(f"- `{si}` **{stt}**" + (f" — {sd}" if sd else ""))
        return o

    if n.has("logos"):
        o.append("- " + " · ".join(flat(x) for x in find(n, "logo")))
        return o

    if n.has("timeline"):
        for it in find(n, "tlitem"):
            o.append(f"- **{child_text(it, 'tld')}** {child_text(it, 'tlv')}"
                     + (f" — {child_text(it, 'tlc')}" if child_text(it, 'tlc') else ""))
        return o

    if n.has("quote"):
        body, attrib = child_text(n, "qbody"), child_text(n, "qd")
        o.append("> " + body)
        if attrib:
            o.append("> — *" + attrib + "*")
        return o

    if n.has("figurehead"):
        o.append(f"- **{child_text(n, 'fname')}** · {child_text(n, 'frole')}")
        for c in ("fnote", "fedu"):
            if child_text(n, c):
                o.append(f"  {child_text(n, c)}")
        return o

    if n.has("srcstrip"):
        for it in find(n, "srcitem"):
            o.append(f"- **{child_text(it, 'sv')}** — {child_text(it, 'sn')}")
        return o

    if n.has("routegrid"):
        for r in find(n, "route"):
            o.append("- " + flat(r))
        return o

    if n.has("foot"):
        t = flat(n)
        return [f"*{t}*"] if t else []

    if n.has("klabel"):
        t = flat(n)
        return [f"***{t}***"] if t else []

    if n.has("bigline"):
        return [f"**{flat(n)}**"]
    if n.has("bigsub"):
        return [flat(n)]

    if n.has("photoblock") or n.has("plate") or n.has("brandtag"):
        return []                                                # images, no text value

    if n.tag == "p":
        t = flat(n)
        return [t] if t else []

    if n.tag == "ul":
        for li in n.kids:
            if li.tag != "li":
                continue
            qn = child_text(li, "qn")
            body = flat(li)
            if qn and body.startswith(qn):
                body = body[len(qn):].strip()
                o.append(f"- `{qn}` {body}")
            else:
                o.append("- " + body)
        return o

    if n.tag == "img":
        return []

    # container: ruleband, split, plain divs, sections
    for k in n.kids:
        o += render(k, depth + 1)
    return o


def onscreen(h):
    root = parse(h)
    sec = root.kids[0] if root.kids else root
    m = first(sec, "h1") or first(sec, "h2")
    head = flat(m) if m else ""
    e = find(sec, "eyebrow") or find(sec, "pn")
    eye = flat(e[0]) if e else ""

    bodies = find(sec, "body")
    target = bodies[0] if bodies else sec
    lines = []
    for k in target.kids:
        if k.has("head") or k.tag in ("h1", "h2"):
            continue
        if k.has("eyebrow") or k.has("pn"):
            continue
        block = render(k)
        if block:
            if lines:
                lines.append("")
            lines += block
    # divider slides keep their question list, which lives outside .body
    if not bodies:
        pass
    out = []
    for ln in lines:
        ln = ln.rstrip()
        # a label or a paragraph after a list needs air; list items do not
        if ln and out and out[-1].startswith("- ") and not ln.startswith("- "):
            out.append("")
        # a small-caps label is a heading: air on both sides of it
        if ln.startswith("***") and ln.endswith("***") and out and out[-1]:
            out.append("")
        if ln and out and out[-1].startswith("***") and out[-1].endswith("***"):
            out.append("")
        if ln or (out and out[-1]):
            out.append(ln)
    while out and not out[-1]:
        out.pop()
    return eye, head, out


HEADER = """# The Braze deck, in full

Every slide in order: **what is on screen, and what to say over it.** Generated from the
deck itself by `deck/make_script.py`, so a slide and its script can never drift apart.

**{words:,} spoken words — {mins} minutes presented, or about {read} minutes to read.**
43 slides, {secs} seconds each at a normal speaking pace.

---

## If you are learning Braze rather than presenting it

Read this file top to bottom. It is the most efficient thing in this repository for that,
because it was written to be **said to somebody who does not know Braze** — the argument
in the order it was built to land, with the evidence attached at the point it is used.

Then, and only then:

| For | Read |
|---|---|
| The traps — where sources disagree, and the exact wording to use | `docs/CONFLICTS.md` |
| What we expected before reading anything, and what was wrong | `docs/STRATEGY.md`, "How the ten ended" |
| The eight things nobody knows, and what would close each | `docs/QUESTIONS.md` §4 |
| The reasoning behind any single claim | the record chapter named under each part below |
| One specific number | `docs/FACTS.md` — 244 rows, a lookup table, never a read |

**What this cannot teach you.** Nobody on this project ever logged into Braze. It is built
entirely from public sources, so it is strong on the business, the money and the decisions,
and it tells you where the product's *limits* are rather than what using it feels like.
For that, read Braze's own documentation — 1,352 pages of it are captured in `sources/docs/`
and `grep` beats their site search — against the seven-stage walkthrough in Part II.

**Bold** marks the words to land on. Press **N** in the deck to read the narration beside
its slide.

---
"""

out = [""]
for i, s in enumerate(S, 1):
    if i in PARTS:
        title, blurb = PARTS[i]
        out.append(f"\n## {title}\n")
        out.append(f"*{blurb}*")
        if i in CHAPTERS:
            out.append(f"\n**Deeper:** {CHAPTERS[i]}")
        out.append("")
    eye, head, screen = onscreen(s["html"])
    out.append(f"### {i:02d} · {html.unescape(s['label'])}")
    if head:
        out.append(f"{(eye + ' — ') if eye else ''}**{head}**")
    out.append("")
    if screen:
        out.append("**On screen**")
        out.append("")
        out += screen
        out.append("")
    if s["notes"]:
        out.append("**Say**")
        out.append("")
        for para in s["notes"].split("\n\n"):
            out.append("> " + para.strip().replace("\n", "\n> "))
            out.append("")

p = os.path.join(REPO, 'docs', 'PRESENTATION-SCRIPT.md')
words = len(re.findall(r"\w+", "\n".join(s["notes"] for s in S)))
body = "\n".join(out)
total = len(re.findall(r"\w+", body))
out[0] = HEADER.format(words=words, mins=max(1, round(words / WPM)),
                       secs=round(words / WPM * 60 / len(S)),
                       read=max(1, round(total / READ_WPM)))
os.makedirs(os.path.dirname(p), exist_ok=True)
open(p, 'w', encoding='utf-8').write("\n".join(out).rstrip() + "\n")
print(f"wrote docs/PRESENTATION-SCRIPT.md: {len(S)} slides, {words} spoken words, "
      f"{total} total, ~{words/WPM:.0f} min presented / ~{total/READ_WPM:.0f} min read")
