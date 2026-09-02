# -*- coding: utf-8 -*-
"""Part 0 — the frame.

These three slides carry no findings about Braze. They are the method, and they are
correct before any research has been done, which is why they ship with the scaffold.

Everything after this file is written by the research run. Add slides_b.py, slides_c.py
and so on; deck/build_deck.py discovers them automatically, in filename order.

The component vocabulary is in deck/lib.py: head, figs, stats, tiles, bars, flow,
timeline, logos, cards, big, split, divider, worldmap. Read that file before inventing
a new layout — the design system is small on purpose.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *                                   # noqa: F403,E402
from assets import LOGO                             # noqa: F401,E402

# ── 1 TITLE ──────────────────────────────────────────────────────────────────
# The source strip is an inventory of what was READ, not of what was found. Every
# figure here was verified reachable on 2026-09-01 and is re-checkable in one command.
# Update the counts as the corpus grows; never put a finding in this strip.
SOURCES = [("Their documentation",   "1,352 pages"),
           ("SEC filings",           "737 documents"),
           ("Audited financials",    "FY2019 &rarr; now"),
           ("Public code",           "137 repos"),
           ("Status page",           "451 incidents"),
           # "Sub-processor" is the deck's earliest piece of jargon and it lands on the
           # title slide. Defining it in the value line costs nothing and means the term
           # is understood before it is used ten more times.
           ("Sub-processors",        "17 outside suppliers")]
_src = ''.join(f'<div class="srcitem"><div class="sn">{n}</div><div class="sv">{v}</div></div>'
               for n, v in SOURCES)

# The wordmark IS the title. It used to sit on a white plate above an <h1>Braze</h1> set
# in Instrument Serif - the company's name said twice, in two typefaces, sixty pixels
# apart, with the plate the brightest object on the slide. Now there is one name, in
# Braze's own violet, with nothing behind it. Identification as the SUBJECT comes from
# what surrounds it: "Competitor analysis" beneath, and a byline saying public sources.
MARK = f'<img class="titlemark" src="{LOGO}" alt="Braze">'

add(f'''<section class="s title-s" data-g="s" data-t="Competitor Analysis">
  {MARK}
  <div class="subject">Competitor analysis</div>
  <p class="lede">Growing slower every year, spending less to do it &mdash; and its newest capability was bought, not built.</p>
  <div class="srcstrip">{_src}</div>
  <div class="byline"><span><strong>Toma Pirtskhelani &middot; Product Manager</strong></span><span>Public sources only &middot; September 2026</span></div>
</section>''',
"""This is a competitor analysis of **Braze**.

The one thing to know before we start: Braze is a **listed company**, and that changes
the nature of the evidence. Where a private vendor gives you claims, Braze files audited
accounts four times a year under legal penalty — and publishes a status page, a public
code repository, and a sub-processor list it is legally obliged to keep complete.

Everything here comes from sources you can check yourself. **Their own technical
documentation. Their SEC filings. Their public code. Their status page. And customer
and employee review panels, read and coded rather than summarised.**

No press release is taken at face value. Where their marketing and their own
documentation disagree, I will show you both.""",
    "s", "Competitor Analysis")

# ── 2 METHOD ─────────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="How we approach it">
  {head("Method &middot; how this is built", "Four parts, three rules")}
  <div class="body">
    {flow([("PART I", "The company", "who owns it &middot; what it costs &middot; who buys it"),
           ("PART II", "The product", "seven stages of one campaign"),
           ("PART III", "Strategy", "where the money goes &middot; what protects them"),
           ("PART IV", "Open questions", "what public sources cannot answer")])}
    <div class="ruleband">
      <div class="klabel">AND THREE RULES THAT APPLY TO ALL FOUR</div>
      {cards([("Every claim is graded",
               "Marked by how strong its source is. The bar at the foot of each slide shows where we are.", "g"),
              ("Marketing is labelled as marketing",
               "Their own words appear &mdash; but never as evidence.", "a"),
              ("Gaps become a backlog",
               "Anything needing a non-public source goes on the open-questions list, and grows as you add to it.", "r")],
             cols=3)}
      <p style="margin-top:14px"><strong>And ten expectations were written down before any of this was
      read. Four turned out wrong &mdash; slide 40 shows which.</strong></p>
    </div>
  </div>
</section>''',
"""Four parts. **Who the company is. How the product actually works. Where the strategy is
going. And what we still cannot answer.**

Three rules run through all of it, and they are on the slide because they are what makes
the rest usable rather than merely interesting.

**Every claim is graded by how strong its source is.** A bar at the foot of every slide
tells you where we are, and a claim takes the grade of its *weakest* supporting source,
never its best. If one number in a sentence comes from a marketing page, the sentence is
marked as marketing.

**Marketing is labelled as marketing.** Braze's own words appear here often, because a
listed company's own words are worth quoting and sometimes they are the finding. They
never appear as evidence for a technical claim.

**And gaps become a backlog.** As we go I will flag the questions that need sources we do
not have. Each one is written down with what would close it, so it is a list to prioritise
rather than a list of things I quietly skipped over. One of them closed while this deck
was being built.""",
    "s", "How we approach it")

# ── 3 GRADING ────────────────────────────────────────────────────────────────
# Note the top grade differs from the private-vendor version of this deck: for a
# listed company, audited filings outrank everything, including their documentation.
add(f'''<section class="s" data-g="s" data-t="How we grade">
  {head("Method &middot; evidence grading", "How to judge every claim here")}
  <div class="body">
    <div class="tiles" style="grid-template-columns:repeat(3,1fr);gap:18px">
      <div class="tile grade" style="border-left:3px solid var(--strong)">
        <div class="klabel" style="color:var(--strong)">STRONG</div>
        <div class="gh">Audited filings, and their own technical documentation</div>
        <div class="td">Signed off by auditors and filed under legal penalty &mdash; or behaviour the platform must actually support</div>
      </div>
      <div class="tile grade" style="border-left:3px solid var(--medium)">
        <div class="klabel" style="color:var(--medium)">MEDIUM</div>
        <div class="gh">Independent records</div>
        <div class="td">Customer reviews, infrastructure traces, incident history, real transacted prices</div>
      </div>
      <div class="tile grade" style="border-left:3px solid var(--weak)">
        <div class="klabel" style="color:var(--weak)">WEAK</div>
        <div class="gh">Marketing, or disputed</div>
        <div class="td">Their own claims, or sources that contradict each other</div>
      </div>
    </div>
    <p>Five grades are kept in the evidence record. Three reach the slides, mapped in
    <span class="mono">docs/EVIDENCE-GRADES.md</span>. <strong>A claim takes the grade of its weakest
    supporting source, never its best.</strong></p>
  </div>
</section>''',
"""Three grades on the slides, five in the record behind them.

**Strong** is a filing or their own technical documentation. An audited number is
signed by someone with legal exposure. Documentation is written for people who will
hit the limits, so it describes the product that exists rather than the one being sold.

**Medium** is independent: what customers say, what the infrastructure shows, what an
outage record admits.

**Weak** is their marketing, or anywhere two credible sources disagree — and where
they disagree I will show you both rather than pick one.

One rule underneath all of it: **a claim takes the grade of its weakest source, never
its best.**""",
    "s", "How we grade")
