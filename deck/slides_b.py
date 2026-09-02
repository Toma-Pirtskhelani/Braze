# -*- coding: utf-8 -*-
"""Part I — the company. Slides 4-16 (divider + 12 content slides).

Every figure on every slide in this file resolves to a row in docs/FACTS.md. Where a
number is a bound rather than a measurement it says so on the slide, not only in the
notes — a caveat that lives only in the speaker notes is a caveat the audience never
hears.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *                                   # noqa: F403,E402

# ── 4 DIVIDER ────────────────────────────────────────────────────────────────
add(f'''<section class="s div-s" data-g="s" data-t="Part I: The company">
  {divider("Part I", "The company",
           ["Who they are, and who controls them now",
            "What they bought, and what it cost",
            "What a customer pays &mdash; bounded, not guessed",
            "Who buys it, and who buyers compare them against"],
           foot="Audited filings unless marked otherwise")}
</section>''',
"""Part one is the company. Four questions.

The thing that makes this part unusual: **Braze is listed**, so most of what follows is
filed under legal penalty rather than claimed on a website. Where I use a marketing
number instead, I will say so.""",
    "s", "Part I: The company")

# ── 5 EXECUTIVE SUMMARY ──────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Five things">
  {head("Executive summary", "If you remember five things")}
  <div class="body">
    {cards([("Their own documentation is the best source against them",
             "Three of four ingestion paths are labelled &ldquo;not real-time&rdquo; by Braze. The profile-export limit was cut 10&times; for customers joining after August 2024. Both are published, in tables.", "g"),
            ("The AI decisioning engine was bought, not built",
             "OfferFit, acquired June 2025 for $303.2m and renamed AI Decisioning Studio. The models come from Anthropic, OpenAI and Google &mdash; named in their own sub-processor disclosure.", "g"),
            ("One instance is not on the same cloud as the others",
             "The IPs Braze tells you to allowlist for US-08 are registered to Microsoft. Every other instance&rsquo;s are Amazon. Their sub-processor list names only Amazon and Google.", "a")],
           cols=3)}
    {cards([("Decelerating and getting more efficient at once",
             "Growth halved from 49.3% to 24.4% since FY2023 while sales and marketing fell from 56.7% of revenue to 44.3%. Operating cash flow has been positive three years running.", "g"),
            ("Buyers weigh them against twice as many vendors as they name",
             "The 10-K names four competitors. Gartner&rsquo;s buyer-derived shortlist has eight &mdash; and the five extra are specialists Braze never mentions.", "g")],
           cols=2)}
  </div>
</section>''',
"""Five things.

**One. Their documentation is more honest than their marketing, and it is the best
source you have.** Every hard limit in this deck came from Braze's own technical pages.

**Two. The AI decisioning product is an acquisition.** OfferFit, bought June 2025 for
three hundred and three million dollars, renamed AI Decisioning Studio. That is in the
auditor's note, not in a rumour.

**Three, and this is the one nobody else will have.** Braze publishes the IP addresses
you must allowlist per instance. The ones for US-08 are all registered to Microsoft.
Every other instance is Amazon. Their sub-processor disclosure names only Amazon and
Google. I will show you all three sources.

**Four. The financial story is better than the loss line suggests** — decelerating
growth, but improving efficiency and three years of positive operating cash flow.

**Five. Their competitive set is wider than they say it is.**""",
    "s", "Five things")

# ── 6 WHO THEY SAY THEY ARE ──────────────────────────────────────────────────
add(f'''<section class="s" data-g="w" data-t="Who they say they are">
  {head("Their story &middot; in their own words", "Who they say they are")}
  <div class="body">
    <div class="quote"><div class="qbody">&ldquo;Our platform empowers <strong>real-time engagement</strong> between brands and their
      customers &hellip; made possible by our proprietary, enterprise-grade <strong>stream processing
      architecture</strong> &hellip; We have designed it to <strong>listen like a human would</strong>, process new
      information in context, and <strong>react instantaneously</strong>.&rdquo;</div>
      <div class="qd">Braze 10-K, Item 1 &middot; filed 25 March 2026</div></div>
    {tiles([("", "The claim", "A single platform, fed by streaming first-party data, reacting in the moment across every channel"),
            ("", "Why it is quoted here", "This is the company&rsquo;s own narrative in a filed document &mdash; the strongest form of a marketing claim, not a technical one"),
            ("", "What to hold on to", "&ldquo;Real-time&rdquo; is doing a lot of work in that sentence. Slide 20 shows their own table grading it")],
           cols=3)}
  </div>
</section>''',
"""This is Braze describing Braze, in the 10-K.

I quote it from the filing rather than the website deliberately. It is the most
carefully-lawyered version of their story that exists, and it still leads with
**real-time**.

Hold that word. It comes back on slide twenty, where their own documentation grades four
ingestion paths and labels three of them "not real-time".

That is not a gotcha, and I will not present it as one. It is one word covering two
architectures — and knowing which one a prospect is buying is worth more than the
argument.""",
    "w", "Who they say they are")

# ── 7 ORIGINS ────────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Origins">
  {head("Origins &middot; and who controls it now", "Fifteen years, and a governance change nine months old")}
  <div class="body">
    {timeline([("2011", "Founded", "Incorporated in Delaware"),
               ("Nov 2021", "IPO", "$456.8m net proceeds"),
               ("Jun 2023", "North Star Y", "Buys its own AU/NZ reseller"),
               ("Jun 2025", "OfferFit", "$303.2m &mdash; becomes AI Decisioning Studio"),
               ("Jan 2026", "Class B retired", "Founder super-voting ends")])}
    <div class="ruleband">
      <div class="klabel">THE PART THAT IS EASY TO MISS</div>
      <p>On <strong>30 January 2026</strong> the Class B stock converted to Class A. In the 10-K&rsquo;s words:
      <em>&ldquo;our executive officers and early investors no longer hold super-voting rights. Consequently, our
      voting power is now more widely distributed among our public stockholders.&rdquo;</em></p>
    </div>
  </div>
</section>''',
"""Founded 2011, public since November 2021, four hundred and fifty-seven million dollars
of net IPO proceeds.

The line that matters is the last one, and it is nine months old. **The dual-class
structure ended in January 2026.** Founders and early investors no longer hold
super-voting stock.

I am not going to tell you what that means, because the evidence does not say. What I
will say is that a company whose direction was insulated from its shareholders until
this year is now not insulated — and if you compete with them, that is a change in who
can apply pressure and how fast they may need to respond to it.""",
    "s", "Origins")

# ── 8 HOW THEY GOT THIS BIG ──────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="How they got this big">
  {head("Capital &middot; and what it bought", "Seven years of audited revenue")}
  <div class="body">
    {bars([("FY2020", 96.4), ("FY2021", 150.2), ("FY2022", 238.0), ("FY2023", 355.4),
           ("FY2024", 471.8), ("FY2025", 593.4), ("FY2026", 738.2, "strong")], unit="m")}
    {figs([("$456.8m", "net IPO proceeds, Nov 2021"),
           ("7.7&times;", "revenue growth, FY2020 to FY2026"),
           ("$124.3m", "cash at FY2026 year end"),
           ("$1,033.0m", "contracted, not yet recognised")], size="sm")}
    <div class="ruleband">
      <div class="klabel">THE CAVEAT THAT TRAVELS WITH EVERY NUMBER IN THIS PART</div>
      <p>Braze disclosed a <strong>material weakness in internal control over financial reporting</strong> at
      31 January 2026 &mdash; ineffective IT general controls over <strong>user access and program change
      management</strong> on the systems that produce these figures. <strong>And, in the same breath:</strong> it
      &ldquo;did not result in any identified misstatements&rdquo;, nothing was restated, and Ernst &amp; Young
      attested. Remediation is under way with no completion date given.</p>
    </div>
  </div>
</section>''',
"""Revenue, seven audited years: ninety-six million to seven hundred and thirty-eight.
**Seven point seven times in six years.**

They raised four hundred and fifty-seven million net at IPO and hold a hundred and
twenty-four million in cash at the last year end.

The number on the right is the one I would put in front of a CFO: **a billion and
thirty-three million dollars of remaining performance obligation** — revenue that is
contracted and not yet recognised. That is one point four times the current year's
revenue, already signed.

If you are competing with Braze for a renewal, that is the number telling you how much
of their base is locked in and for how long.

Now the band at the bottom, and I want it on the slide rather than in my pocket. **Braze
disclosed a material weakness in internal control over financial reporting** at the last
year end — ineffective IT general controls over user access and change management on the
systems that produce these numbers. Their CEO and CFO signed that disclosure controls
were not effective.

**And in the same breath, because either half alone misleads:** it produced no identified
misstatement, nothing was restated, and the auditor still attested. Every number I am
about to show you stands. But the control environment behind them was judged not
effective by the people who signed it, and remediation has no published completion date.

I missed this on my first pass through the filing. It is the reason the money part of
this deck carries a band that the product part does not.""",
    "s", "How they got this big")

# ── 9 ACQUISITION 1 ──────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Acquisition: OfferFit">
  {head("Acquisition one &middot; June 2025", "They bought their AI, and the filing says so")}
  <div class="body">
    <div class="quote"><div class="qbody">&ldquo;the Company completed the acquisition of <strong>OfferFit, Inc.</strong>
      (&lsquo;OfferFit&rsquo;) <strong>which is now known as AI Decisioning Studio</strong> for total
      consideration of <strong>$303.2 million</strong>.&rdquo;</div>
      <div class="qd">Ernst &amp; Young, critical audit matter &middot; Braze 10-K, 25 March 2026</div></div>
    {figs([("$303.2m", "total consideration"),
           ("77%", "of the price was goodwill"),
           ("$56.7m", "developed technology, amortised to cost of revenue"),
           ("2 Jun 2025", "closed")], size="sm")}
  </div>
</section>''',
"""This is the single most useful sentence in the filings.

**OfferFit — which is now known as AI Decisioning Studio.** The product Braze markets as
BrazeAI Decisioning Studio is a company they bought, fifteen months ago, for three
hundred and three million dollars. A hundred and ninety-five in cash, a hundred and eight
in stock.

Seventy-seven per cent of that price was goodwill — which is what a price looks like when
what you are buying is a team and a position rather than assets.

And note where the technology amortisation lands: **cost of revenue**. That is why this
acquisition shows up in their gross margin, which is slide thirty-three.

The 10-K calls what they bought "OfferFit's multi-agent decisioning engine". So when we
get to the AI slide, remember that the agentic layer has a purchase price.""",
    "s", "Acquisition: OfferFit")

# ── 10 ACQUISITION 2 ─────────────────────────────────────────────────────────
_ns_left = '<div>' + figs([("$26.8m", "total consideration"),
                           ("$26.0m", "earn-out available"),
                           ("$0", "earn-out paid", "neg")], cols=1, size="sm") + '</div>'
_ns_right = '<div>' + cards([
    ("What it was",
     "North Star Y, Pty Ltd &mdash; Braze&rsquo;s <strong>exclusive reseller in Australia and New Zealand</strong>. Buying it took the market direct.", "g"),
    ("What the filing records",
     "Braze &ldquo;reduced the contingent consideration liability &hellip; <strong>to zero as it was determined that the sellers did not satisfy the earn-out qualifications</strong>.&rdquo;", "a"),
    ("How to read it",
     "An earn-out that does not vest means the revenue targets written into the deal were not met. It does not say the acquisition failed &mdash; and the filings do not say that either.", "g")],
    cols=1) + '</div>'

add(f'''<section class="s" data-g="s" data-t="Acquisition: North Star Y">
  {head("Acquisition two &middot; June 2023", "They bought a market, and the earn-out paid nothing")}
  <div class="body">
    {split(_ns_left, _ns_right, ratio="0.8fr 1.6fr")}
  </div>
</section>''',
"""Two years earlier they bought their own Australia and New Zealand reseller — twenty-six
point eight million, to take that market direct.

The sellers could have earned up to twenty-six million more, on qualified revenue
performance, over the two years after completion.

**They earned none of it.** The FY2026 filing records the contingent consideration
reduced to zero because the sellers did not satisfy the earn-out qualifications.

I want to be careful here, because this is the kind of fact that is easy to over-read.
It does not say the acquisition failed. It says the revenue targets set in June 2023
were not met. If you sell against Braze in Australia or New Zealand, that is worth
knowing and it is not on any website.""",
    "s", "Acquisition: North Star Y")

# ── 11 WHAT IT COSTS ─────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="What it costs">
  {head("Price &middot; bounded, not guessed", "Nobody publishes a price. You can still bound one")}
  <div class="body">
    {figs([("~$283,000", "revenue &divide; customers, FY2026 &mdash; a <em>bound</em>, not a price")], size="lg", cols=1)}
    <div class="ruleband">
      <div class="klabel">AND THE MECHANIC UNDERNEATH IT &mdash; FROM THEIR DOCUMENTATION</div>
      {tiles([("", "You are billed per data point",
               "&ldquo;a session start, session end, custom event, or purchase recorded, as well as <strong>any attribute set</strong> on an end user profile&rdquo; &mdash; each one counts separately"),
              ("", "Engagement is free",
               "Push tokens, device info, email opens and push clicks are <strong>not</strong> counted. That is a genuinely customer-friendly boundary"),
              ("", "Their own advice is to send less",
               "&ldquo;<strong>Don&rsquo;t waste data points. Only update changing data!</strong>&rdquo; &mdash; a platform sold on streaming everything, priced so that you send less of it")],
             cols=3)}
    </div>
  </div>
</section>''',
"""No vendor in this category publishes a price and Braze is no exception. But a listed
company gives you something better than a guess: **seven hundred and thirty-eight million
of revenue across two thousand six hundred and nine customers is about two hundred and
eighty-three thousand dollars each.**

Say "bounded at". Never say "costs". It mixes a two-thousand-seat enterprise with a
startup and it includes professional services.

The mechanic underneath is the useful part. You are billed per **data point** — and their
definition includes *any attribute set on a profile*. A session start and a session end
are two data points.

Engagement tracking is free, which is fair and I will say so.

But look at the third card. Their own documentation says **"Don't waste data points. Only
update changing data."** A platform positioned on continuous streaming of behavioural
data, advising customers to build programmes to send less of it. That tension is theirs,
not mine — and a Gartner reviewer independently calls out overages getting expensive
quickly.""",
    "s", "What it costs")

# ── 12 WHO USES IT ───────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Who uses it">
  {head("Customers &middot; three rosters, never merged", "How many customers depends on who is counting")}
  <div class="body">
    {figs([("2,609", "the 10-K&rsquo;s defined metric, 31 Jan 2026"),
           ("333", "customers at $500k+ ARR &mdash; up from 202 in FY2024"),
           ("178", "self-published customer stories"),
           ("&mdash;", "independent detection: not attempted")], size="sm", focus=0)}
    <div class="ruleband">
      <div class="klabel">EXPANSION IS SLOWING, AND THE ENTERPRISE PREMIUM HAS NEARLY GONE</div>
      {bars([("FY2024 &middot; all customers", 117), ("FY2024 &middot; $500k+ ARR", 120),
             ("FY2026 &middot; all customers", 109), ("FY2026 &middot; $500k+ ARR", 110, "medium")], unit="%")}
    </div>
  </div>
</section>''',
"""Three customer counts and they must never be merged.

**Two thousand six hundred and nine** is the 10-K's defined, audited metric. A hundred
and seventy-eight is the number of customer stories they chose to publish — that is
marketing, and it is not a sample of anything. Independent detection I did not attempt,
and I am recording that as a gap rather than a zero.

Now the bars, because there are two movements and the second is easy to miss.

Net retention is falling — a hundred and seventeen to a hundred and nine. Braze explains
that themselves: customers renewing at levels closer to current needs rather than
betting on future demand.

The subtler one: **large customers used to expand three points faster than average. Now
they expand one point faster.** Whatever premium the enterprise cohort had is nearly
gone — while the number of those accounts has grown from two hundred and two to three
hundred and thirty-three. More big logos, each growing more slowly.""",
    "s", "Who uses it")

# ── 13 WHERE THEY OPERATE ────────────────────────────────────────────────────
_geo_left = '<div>' + figs([("54.9%", "United States, FY2026"),
                            ("45.1%", "international"),
                            ("0", "other countries above 10% of revenue", "neg")], cols=1, size="sm") + '</div>'
_geo_right = '<div>' + cards([
    ("The sentence that matters",
     "&ldquo;Other than the United States, <strong>no other individual country accounted for 10% or more of total revenue</strong> for any of the periods presented.&rdquo;", "g"),
    ("Set against the footprint",
     "<strong>15 regional clusters</strong> and <strong>15 legal entities across 14 territories</strong> &mdash; from the status page and the sub-processor disclosure respectively.", "g"),
    ("So what",
     "Forty-five per cent of revenue is international and none of it concentrates. That is a wide, thin footprint carrying a heavy infrastructure and legal base.", "a")],
    cols=1) + '</div>'

add(f'''<section class="s" data-g="s" data-t="Where they operate">
  {head("Geography &middot; audited, not inferred", "Wide, thin, and carrying a heavy base")}
  <div class="body">
    {split(_geo_left, _geo_right, ratio="0.7fr 1.7fr")}
  </div>
</section>''',
"""Geography, audited, from the segment note — not inferred from customer domains, which
is what you would be doing with a private vendor.

Forty-five per cent of revenue is international. And then the sentence that does the
work: **other than the United States, no individual country reaches ten per cent of
revenue.**

Put that next to the footprint. Fifteen regional clusters on the status page. Fifteen
legal entities across fourteen territories in the sub-processor list. Offices and hiring
in twenty-six locations.

That is a wide, thin international business carrying a heavy fixed base. It is a
strategic bet on international rather than a harvest of it — and it is the kind of thing
that shows up in gross margin before it shows up in growth.""",
    "s", "Where they operate")

# ── 14 WHAT CUSTOMERS SAY ────────────────────────────────────────────────────
# One chart, ONE SCALE. These were briefly two side-by-side bars() calls, which
# normalise independently - so "Ease of Use 385" and "Missing Features 140" rendered at
# identical length and the slide implied praise and criticism were equally common. They
# are not, and the asymmetry is the finding.
_rev_bars = bars([("Ease of Use", 385), ("Intuitive", 188),
                  ("Customer Support", 151), ("Helpful", 148),
                  ("Missing Features", 140, "weak"), ("Learning Curve", 139, "weak"),
                  ("Limitations", 102, "weak"), ("Steep Learning Curve", 86, "weak")])

add(f'''<section class="s" data-g="m" data-t="What customers say">
  {head("Review panels &middot; coded, not summarised", "Well liked, with two consistent complaints",
        "G2 <strong>4.5/5</strong> across 1,702 reviews &middot; Gartner <strong>4.5/5</strong> across 263 ratings &middot; TrustRadius <strong>8.8/10</strong> across 348 reviews")}
  <div class="body">
    <div class="klabel colhead">G2&rsquo;S OWN TAGS, OVER ITS WHOLE REVIEW BASE &mdash; PRAISE IN GREY, CRITICISM IN RED, ONE SCALE</div>
    {_rev_bars}
    <p><strong>Two themes recur across unrelated panels, which is what makes them worth quoting:
    reporting, and the learning curve.</strong> TrustRadius codes reporting as &ldquo;limited and unintuitive,
    a sentiment shared by 36% of reviewers&rdquo;.</p>
  </div>
</section>''',
"""Braze is genuinely well liked. Four and a half out of five on two panels, eight point
eight out of ten on the third, across more than two thousand reviews. I am not going to
soften that.

These tags are G2's own coding over their whole review base, not my sample — and they
are on **one scale**, deliberately, because the shape is the point: the single most
common praise tag is nearly three times the most common criticism.

Two complaints recur across panels that have nothing to do with each other, and that is
what makes them worth your attention. **Reporting**, and the **learning curve**.

TrustRadius puts a number on the first: thirty-six per cent of their recent reviewers
describe reporting as limited and unintuitive.

Hold that too, because when we get to the platform section you will see the mechanism
behind it — the raw-data export that fixes it is a paid add-on called Currents.""",
    "m", "What customers say")

# ── 15 WHAT EMPLOYEES SAY ────────────────────────────────────────────────────
add(f'''<section class="s" data-g="m" data-t="What employees say">
  {head("Glassdoor &middot; and the careers board", "Strong culture; the complaints are about ceilings")}
  <div class="body">
    {figs([("4.1<em>/5</em>", "524 ratings"), ("82%", "would recommend"),
           ("90%", "approve of the CEO"), ("71%", "positive business outlook")], size="sm")}
    {tiles([("", "Work-life balance is not the problem",
             "It tracks the overall rating almost exactly over six months, around 4.0&ndash;4.1. No divergence &mdash; so no trend is claimed"),
            ("", "What their own summary names",
             "Management effectiveness and &ldquo;clarity in direction&rdquo;; &ldquo;limited upward mobility and discrepancies in compensation relative to market rates&rdquo;"),
            ("", "Still hiring hard",
             "Roughly 284&ndash;300 open roles across 15 functions and 26 locations &mdash; including Bucharest, which matches a Romanian entity in the sub-processor list")],
           cols=3)}
  </div>
</section>''',
"""Employees rate them well. Four point one, eighty-two per cent would recommend, ninety
per cent approve of the CEO.

I went looking for a work-life-balance decline because that is the usual story at this
stage of a company's life. **It is not there.** Work-life balance tracks the overall
rating almost exactly. I am reporting that because it is what the evidence says, not
because it is interesting.

The complaints in Glassdoor's own summary are about ceilings rather than conditions:
management clarity, limited upward mobility, and compensation against market.

And they are hiring hard — roughly three hundred open roles across fifteen functions.
One small corroboration I like: the board lists Bucharest, and the sub-processor
disclosure lists a Braze entity in "Ireland and Romania". Two unrelated documents
describing the same thing is how you know both are real.""",
    "m", "What employees say")

# ── 16 WHO THEY COMPETE WITH ─────────────────────────────────────────────────
_cmp_named = ('<div><div class="klabel colhead">NAMED IN THE 10-K &mdash; THEIR CHOICE</div>'
              + logos(["Adobe", "Salesforce", "Iterable", "Klaviyo"], cols=2) + '</div>')
_cmp_buyer = ('<div><div class="klabel colhead">GARTNER&rsquo;S BUYER-DERIVED SHORTLIST &mdash; NOT THEIR CHOICE</div>'
              + logos(["Salesforce", "Adobe", "Iterable", "Oracle", "Optimove",
                       "Blueshift", "MoEngage", "CleverTap"], cols=4,
                      accent=("Oracle", "Optimove", "Blueshift", "MoEngage", "CleverTap")) + '</div>')

add(f'''<section class="s" data-g="m" data-t="Who they compete with">
  {head("Competition &middot; two lists", "Buyers weigh them against twice as many vendors as they name")}
  <div class="body">
    {split(_cmp_named, _cmp_buyer)}
    <div class="ruleband">
      <div class="klabel">THE GAP IS THE FINDING</div>
      <p>Three of their four names appear on the buyer list &mdash; so this is not a vendor misreading its market.
      But <strong>five vendors buyers actually compare them against appear nowhere in the 10-K</strong>, and they are
      mostly the mobile-engagement specialists rather than the suites Braze positions against.</p>
    </div>
  </div>
</section>''',
"""Two lists. On the left, the four competitors Braze names in its own 10-K. On the right,
the vendors Gartner reports buyers *also considered* — derived from the buyers, not from
Braze.

Three names are shared. So this is not a company misreading its own market, and I will
not claim it is.

**The asymmetry is the finding.** The buyer list is twice as long, and the five extra —
Oracle, Optimove, Blueshift, MoEngage, CleverTap — are named nowhere in the filing. Four
of those five are mobile-engagement specialists, not suites.

If you built a competitive briefing only from Braze's own comparison pages, you would
walk into the room missing five of the eight vendors in it.

One more thing from the same source, and it is in Braze's favour: where Gartner's
reviewers rate Braze above Salesforce and Adobe, they name the same two things both
times — service and support, and ease of integration.""",
    "m", "Who they compete with")
