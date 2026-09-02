# -*- coding: utf-8 -*-
"""Part I — the company. Slides 4-17 (divider + 13 content slides).

Every figure on every slide in this file resolves to a row in docs/FACTS.md. Where a
number is a bound rather than a measurement it says so on the slide, not only in the
notes — a caveat that lives only in the speaker notes is a caveat the audience never
hears.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *                                   # noqa: F403,E402
from assets import CEO, LOGO, OFFERFIT              # noqa: F401,E402

# ── 4 DIVIDER ────────────────────────────────────────────────────────────────
add(f'''<section class="s div-s" data-g="s" data-t="Part I: The company">
  {divider("Part I", "The company",
           ["Who they are, and who controls them now",
            "What they bought, and what it cost",
            "What a customer pays &mdash; bounded, not guessed",
            "Who buys it, and who buyers compare them against"],
           foot="Audited filings unless marked otherwise")}
</section>''',
"""Part one is the company. Four questions: who they are and who controls them, what they
have bought, what a customer pays, and who actually buys it.

The thing that makes this part unusual is that **Braze is listed.** Almost everything in
the next twelve slides is filed under legal penalty rather than claimed on a website —
seven years of audited accounts, two acquisition prices with their purchase-price
allocations, a customer count that is a *defined* metric, and a proxy statement naming
every executive officer and director. With a private vendor you would be inferring most
of this from job ads and press releases.

Two things to watch for as we go. **Where I use a marketing number instead of a filed
one, I will say so out loud** — those are the weak-graded claims and there are only a few.
And the most useful slide in this part is probably not the one you expect: it is the
customer-count slide, because the definition of "customer" turns out to change what the
only available price figure actually means.""",
    "s", "Part I: The company")

# ── 5 THE FOUR DOCUMENTS ─────────────────────────────────────────────────────
# Added after the operator's read-through. Seventeen specialist terms were used in this
# deck and none was defined; the two worst - "10-K" and "sub-processor" - carried whole
# findings. A glossary slide is a slide nobody reads, so this is not one: it is the
# argument for why these four sources beat marketing, and the definitions ride along
# inside it. Everything after this slide can now say "the 10-K" and be understood.
add(f'''<section class="s" data-g="s" data-t="The four documents">
  {head("What this rests on", "Four documents a company cannot write freely")}
  <div class="body">
    {cards([("The 10-K",
             "Their <strong>audited annual report to the US regulator</strong>. Signed by the chief executive "
             "and the finance chief, and wrong at legal risk. <strong>Seven years of them.</strong>", "g"),
            ("The proxy statement",
             "Filed before the shareholder meeting. Must name <strong>every executive officer and "
             "director</strong>, their pay, and who owns the company.", "g")],
           cols=2)}
    {cards([("The sub-processor disclosure",
             "A public list of <strong>every outside supplier that touches customer data</strong>. The law "
             "obliges them to keep it complete, so it names middlemen no marketing page would.", "g"),
            ("The status page",
             "A live record of <strong>every outage since 2016</strong>, written during the outage. Nobody "
             "writes one of these to look good.", "g")],
           cols=2)}
    <p><strong>None of these is marketing.</strong> Three are filed under legal penalty and the fourth is
    written under pressure &mdash; so wherever this deck and Braze&rsquo;s website disagree, the documents win.</p>
  </div>
</section>''',
"""Before any findings, thirty seconds on where this comes from — because four documents do
most of the work in this deck and they are the reason to believe it.

**The 10-K is their audited annual report to the American regulator.** Once a year, signed
personally by the chief executive and the finance chief, audited by Ernst & Young. If it
is wrong, that is a legal problem for named individuals. We have seven years of them.

**The proxy statement** goes out before the shareholder meeting. It has to name every
executive officer and director, say what each of them is paid, and disclose who owns the
company. It is the only document in this set with people in it.

**The sub-processor disclosure** is a public list of every outside supplier that touches
customer data — data-protection law requires it to be complete. That completeness is the
useful part: it names the middlemen that no marketing page would ever mention, and two of
the sharpest findings in this deck come straight out of it.

**And the status page** is a live record of every outage since 2016, written during the
outage by someone trying to fix it. Nobody writes a status page to look good.

The thing to take from this slide is not the four names. It is this: **none of them is
marketing.** Three are filed under legal penalty and the fourth is written under pressure.
So when their website and their filings disagree — and they do — you know which one I am
going to believe, and now you know why.""",
    "s", "The four documents")

# ── 5 EXECUTIVE SUMMARY ──────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Five things">
  {head("Executive summary", "If you remember five things")}
  <div class="body">
    {cards([("Braze grades its own data delays, and three of four are slow",
             "Their documentation labels three of the four ways data gets in "
             "<strong>&ldquo;not real-time&rdquo;</strong>. Their table, not our characterisation.", "g"),
            ("The AI decisioning engine was bought, not built",
             "OfferFit, acquired June 2025 for <strong>$303.2m</strong>. The models come from Anthropic, "
             "OpenAI and Google.", "g"),
            ("One instance is not on the same cloud as the others",
             "The addresses Braze tells you to allowlist for <strong>US-08</strong> belong to Microsoft. "
             "Every other instance&rsquo;s belong to Amazon.", "a")],
           cols=3)}
    {cards([("They are slowing down and getting more efficient at the same time",
             "Growth has halved since FY2023 while sales spend fell further. <strong>Three straight years "
             "of positive cash flow.</strong>", "g"),
            ("Braze names four competitors. Buyers compare them against eight",
             "The five extra names are specialists Braze never mentions.", "g")],
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
  <div class="brandtag" style="width:104px"><img src="{LOGO}" alt="Braze"></div>
  {head("Their story &middot; in their own words", "Their biggest claim, in their most careful document")}
  <div class="body">
    <div class="quote"><div class="qbody">&ldquo;Our platform empowers <strong>real-time engagement</strong> between brands and their
      customers &hellip; made possible by our proprietary, enterprise-grade <strong>stream processing
      architecture</strong> &hellip; We have designed it to <strong>listen like a human would</strong>, process new
      information in context, and <strong>react instantaneously</strong>.&rdquo;</div>
      <div class="qd">Braze 10-K, Item 1 &middot; filed 25 March 2026</div></div>
    {tiles([("", "The claim", "A single platform, fed by streaming first-party data, reacting in the moment across every channel"),
            ("", "Why it is quoted here", "This is the company&rsquo;s own narrative in a filed document &mdash; the strongest form of a marketing claim, not a technical one"),
            ("", "What to hold on to", "&ldquo;Real-time&rdquo; is doing a lot of work in that sentence. Slide 21 shows their own table grading it")],
           cols=3)}
  </div>
</section>''',
"""This is Braze describing Braze, in the 10-K.

I quote it from the filing rather than the website deliberately. It is the most
carefully-lawyered version of their story that exists, and it still leads with
**real-time**.

Hold that word. It comes back on slide twenty-one, where their own documentation grades four
ingestion paths and labels three of them "not real-time".

That is not a gotcha, and I will not present it as one. It is one word covering two
architectures — and knowing which one a prospect is buying is worth more than the
argument.""",
    "w", "Who they say they are")

# ── 7 ORIGINS ────────────────────────────────────────────────────────────────
# Was a timeline of five dates, four of which get a slide of their own later. The slide
# is titled "and who controls it now" and answered only the Class B conversion, which is
# half a governance answer: control is who holds the votes AND who holds the seats.
# The portrait is the first named human being in this analysis. It is Braze's own
# investor-relations headshot, and it is captioned with the title Braze gives it.
# The 2011 TechCrunch photograph was here and has been dropped. It was sourced properly
# and it stays in sources/media/ as evidence, but it put a second photographic treatment on
# a slide that already had one: a clean 120px circle above a 216px rectangular screen-grab,
# two widths, a ragged right edge, and cropped lettering along the top of a low-resolution
# original. One well-placed portrait says more than a portrait plus a bad snapshot - and its
# caption was an admission that the source cannot say which founder is which.
_gov_left = ('<div>' + figurehead(
    CEO, "Bill Magnuson",
    "Chairman &middot; CEO &middot; President &middot; Cofounder",
    "CTO from July 2011, chief executive since 2017, chairman &mdash; and President too "
    "since June 2025, when the previous President resigned. One person, four titles.",
    "Cofounder Jon Hyman is still CTO, an officer since 2011.")
    + '</div>')

_gov_right = ('<div><div class="klabel colhead">AND WHO HOLDS THE SEATS</div>'
              + tiles([("", "Seven seats, six independent",
                        "Magnuson is the exception. <strong>Phillip Fernandez is Lead Independent "
                        "Director</strong> &mdash; the role a board creates when its chair is not."),
                       ("", "And the board is classified",
                        "Three staggered classes, so only about <strong>a third stands in any year</strong>. "
                        "The super-voting stock is gone; this is not."),
                       ("", "The votes, after January",
                        "Class B converted <strong>30 January 2026</strong>. Largest holder <strong>6.0%</strong>, "
                        "the CEO <strong>4.9%</strong>, the Battery partner <strong>5.1%</strong> &mdash; "
                        "<strong>no blocking position left.</strong>")], cols=1)
              + '</div>')

add(f'''<section class="s" data-g="s" data-t="Origins">
  {head("Origins &middot; and who controls it now", "Origins, and who controls it now")}
  <div class="body">
    {split(_gov_left, _gov_right, ratio="0.95fr 1.05fr")}
  </div>
</section>''',
"""Founded 2011. Public since November 2021. And now the part this slide is actually for,
because until this pass it answered only half its own question.

**Who runs it.** Bill Magnuson — chief executive since January 2017, on the board since
2014, and the company's Chief Technology Officer before that from July 2011. He is also
chairman. And since June 2025 he is President too, because the previous President
resigned and the role was not refilled. One person holds four titles.

His cofounder Jon Hyman is still Chief Technology Officer, and has been an officer since
July 2011. **Two of the three cofounders are still running the company fifteen years
on** — the third, Mark Ghermezian, appears in no filing at all. Braze names all three on
its own website; the SEC filings name none of them as founders, which is why that
particular fact is graded as a company claim rather than as audited.

**Who holds the seats.** Seven directors, six of them independent — Magnuson is the
exception because he is an executive. Phillip Fernandez is Lead Independent Director,
which is the role a board creates when its chair is also its chief executive. The proxy
defends that combination rather than glossing it, and I would quote their reasoning
rather than mine.

The one I would flag is the third card. **The board is classified into three staggered
classes**, so only about a third of it stands for election in any year. Braze retired its
super-voting stock in January and got a good deal of credit for it. The staggered board
is still there, and a staggered board is the more durable of the two defences.

**Who holds the votes.** After the conversion, ordinary arithmetic. The largest holder
Braze discloses is at six per cent, the chief executive at just under five, and the
Battery Ventures partner on the board at five. Nobody has a blocking position. Before
January, the founders and early investors did.

So the honest summary is that control got more conventional this year in one respect and
did not move at all in another — and if you are modelling how fast Braze can be pushed to
respond to a shareholder, both halves matter.""",
    "s", "Origins")

# ── 8 HOW THEY GOT THIS BIG ──────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="How they got this big">
  {head("Capital &middot; and what it bought", "7.7&times; bigger, a billion already contracted")}
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
      31 January 2026 &mdash; <em>a flaw in the checking, not an error in the numbers</em>. Ineffective IT
      controls over <strong>user access and program change management</strong> on the systems that produce
      these figures. <strong>And, in the same breath:</strong> it &ldquo;did not result in any identified
      misstatements&rdquo;, nothing was restated, and Ernst &amp; Young attested.</p>
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

Let me reframe what that actually means for us, because it is routinely under-used. RPO
is not pipeline and it is not a forecast; it is signed business sitting inside contract
terms, with an auditor's signature on the total. **Roughly a year and a half of Braze's
current revenue is not available for us to compete for** — not because those customers
would refuse to move, but because they are not up for renewal. That changes the question
from "can we win this account" to "when does it come up", and for most of their base the
answer this year is: it does not.

Now the band at the bottom, and I want it on the slide rather than in my pocket. **Braze
disclosed a material weakness in internal control over financial reporting** at the last
year end — ineffective IT general controls over user access and program change management
on the systems that produce these numbers. Their CEO and CFO signed that disclosure
controls were not effective at the reasonable assurance level.

**And in the same breath, because either half alone misleads:** it produced no identified
misstatement, nothing was restated, and Ernst & Young still issued an attestation report
on internal control.

If someone asks how much that should change their confidence in these figures, the honest
answer is: less than the phrase "material weakness" sounds, and more than zero. A material
weakness is a statement about the *probability* that an error could occur and go
undetected. It is not a finding that one did. And here every independent check came back
clean — no misstatement identified, nothing restated, an auditor attestation, and
separately we ran a mechanical sweep across twenty-nine reported XBRL concepts looking for
any figure Braze had quietly superseded in a later filing. We found none. Three
confirmations that the outputs are sound, against one disclosure that the process
producing them is not yet controlled to standard.

Two things not to do with it. **Do not turn it into a claim about customer data
security.** It is scoped to financial-reporting systems and says nothing about the
platform — and for a company whose product is data infrastructure, that is exactly the
leap an audience will make for you unless you close it off. And do not leave it out: a
briefing that omits this and then gets asked about it by a prospect's finance team has
spent its credibility for nothing.

I missed this on my first pass through the filing. It is the reason the money part of
this deck carries a band that the product part does not.""",
    "s", "How they got this big")

# ── 9 ACQUISITION 1 ──────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Acquisition: OfferFit">
  <div class="brandtag" style="width:132px"><img src="{OFFERFIT}" alt="OfferFit"></div>
  {head("Acquisition one &middot; June 2025", "They bought their AI, and the filing says so")}
  <div class="body">
    <div class="quote"><div class="qbody">&ldquo;the Company completed the acquisition of <strong>OfferFit, Inc.</strong>
      (&lsquo;OfferFit&rsquo;) <strong>which is now known as AI Decisioning Studio</strong> for total
      consideration of <strong>$303.2 million</strong>.&rdquo;</div>
      <div class="qd">Ernst &amp; Young, critical audit matter &middot; Braze 10-K, 25 March 2026</div></div>
    {figs([("$303.2m", "total consideration"),
           ("77%", "was goodwill &mdash; price not tied to any asset"),
           ("$56.7m", "developed technology, amortised to cost of revenue"),
           ("2 Jun 2025", "closed")], size="sm")}
    <div class="ruleband">
      <div class="klabel">WHAT THE PURCHASE-PRICE ALLOCATION TELLS YOU</div>
      <p>Only <strong>$66.6m of the $303.2m was identifiable</strong>, and $56.7m of that is the software
      &mdash; so Braze bought a capability and its people, not revenue. The trademark went at
      <strong>$0.9m</strong>: nobody expected the name to survive. <strong>So the margin drag runs to 2031,
      and any AI pricing they quote has to carry it.</strong></p>
    </div>
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
acquisition shows up in their gross margin, which is slide thirty-four.

The 10-K calls what they bought "OfferFit's multi-agent decisioning engine". So when we
get to the AI slide, remember that the agentic layer has a purchase price.""",
    "s", "Acquisition: OfferFit")

# ── 10 ACQUISITION 2 ─────────────────────────────────────────────────────────
# No North Star Y logo appears on this slide because none could be sourced: the domains do
# not resolve, there are no Internet Archive captures, and a web search returns only
# Braze's own press releases. Several unrelated companies trade as "North Star"; attaching
# one of their marks would be a fabricated identification. The absence is stated instead.
_ns_left = ('<div>' + figs([("$26.8m", "paid at completion"),
                            ("$26.0m", "more, if revenue targets were met"),
                            ("$0", "of that was ever paid", "neg")], cols=1, size="sm")
            + '</div>')
_ns_right = '<div>' + cards([
    ("What it was",
     "North Star Y, Pty Ltd &mdash; Braze&rsquo;s <strong>exclusive reseller in Australia and New Zealand</strong>. Buying it took the market direct.", "g"),
    ("What the filing records",
     "Braze &ldquo;reduced the contingent consideration liability &hellip; <strong>to zero as it was determined that the sellers did not satisfy the earn-out qualifications</strong>.&rdquo;", "a"),
    ("How to read it",
     "An <strong>earn-out</strong> is money owed only if the business hits agreed targets. This one paid "
     "nothing, so the targets were not met &mdash; which does not say the acquisition failed, and the "
     "filings do not say that either.", "g")],
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

I want to spend a moment on how to read that, because it is the fact in this deck most
easily over-read, and the reasoning matters more than the number.

An earn-out is a price-setting device for a disagreement. The buyer thinks the business
will do X. The seller thinks it will do more. Rather than argue about it, they agree the
seller gets paid the difference if the seller turns out to be right. **So a zero payout
tells you one thing precisely: the revenue trajectory the sellers signed up to in June
2023 did not happen.** And it tells you that from the buyer's own audited filing, in a
document where getting it wrong has legal consequences. No website was ever going to say
this.

Here is what it does **not** say. It does not say the acquisition failed, and the filings
do not say that either. Braze still owns the business. They still run an AU-01 cluster —
you will see it on the infrastructure slide. And they have never taken an impairment
against the twenty-eight point four million of goodwill from that deal, which they would
have had to disclose. A perfectly benign reading is available: earn-out targets are where
optimism gets priced, they are often set aggressively on purpose, and the business may be
performing adequately just not at the seller's number.

Two details close the loop. The two point eight million indemnification holdback was
**released in full**, which means nobody made an indemnity claim against the sellers — so
whatever happened was a performance shortfall, not a dispute about what was sold. And the
results of the acquired business were recorded as "not material" to the consolidated
statements, which is what you would expect of a regional reseller and tells you the
shortfall never threatened the group numbers.

So the sentence I would actually say out loud is the narrow one: **Braze paid twenty-six
point eight million for direct control of Australia and New Zealand, structured up to
half the potential value as performance-contingent, and the performance conditions were
not met.** If you sell against them in that region, the public record contains no
evidence of the acceleration the deal was priced for. That is worth knowing, and it is
the most useful thing on this slide.""",
    "s", "Acquisition: North Star Y")

# ── 11 WHAT IT COSTS ─────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="What it costs">
  {head("Price &middot; bounded, not guessed", "Nobody publishes a price. You can still bound one")}
  <div class="body">
    {figs([("~$283,000", "revenue &divide; customers, FY2026 &mdash; a <em>bound</em>, not a price")], size="lg", cols=1)}
    <p style="margin-top:-4px"><strong>An average, not a typical contract.</strong> A few very large customers
    pull it up, and most pay far less. It is the ceiling of what an average customer costs, not what one does.</p>
    <div class="ruleband">
      <div class="klabel">AND THE MECHANIC UNDERNEATH IT &mdash; FROM THEIR DOCUMENTATION</div>
      {tiles([("", "You are billed per data point",
               "&ldquo;a session start, session end, custom event, or purchase recorded, as well as <strong>any attribute set</strong>&rdquo; &mdash; each counts separately"),
              ("", "Engagement is free",
               "Opens, clicks, push tokens and device info are <strong>not</strong> counted. A genuinely customer-friendly boundary"),
              ("", "Their own advice is to send less",
               "&ldquo;<strong>Don&rsquo;t waste data points. Only update changing data!</strong>&rdquo; &mdash; a platform sold on streaming everything, priced so you send less")],
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
  {head("Customers &middot; three rosters, never merged", "Three ways to count a customer")}
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
     "A wide, thin footprint on a heavy fixed base. <strong>No single non-US market is large enough that losing it would show</strong> &mdash; so outside the US you compete market by market, and so do they.", "a")],
    cols=1) + '</div>'

add(f'''<section class="s" data-g="s" data-t="Where they operate">
  {head("Geography &middot; audited, not inferred", "No second home market")}
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
  {head("Glassdoor &middot; and the careers board", "What employees say")}
  <div class="body">
    {figs([("4.1<em>/5</em>", "524 ratings"), ("82%", "would recommend"),
           ("90%", "approve of the CEO"), ("71%", "positive business outlook")], size="sm")}
    <div class="quote"><div class="qbody">Glassdoor&rsquo;s own summary names the weak spots:
      <strong>&ldquo;limited upward mobility and discrepancies in compensation relative to market
      rates&rdquo;</strong>.</div>
      <div class="qd">Glassdoor company page &middot; captured signed-in, 2 September 2026</div></div>
    {tiles([("", "Not pay &mdash; progression",
             "Median employee pay is <strong>$164,000</strong>. Not a low-paying company, so this is a "
             "complaint about the ceiling, not the floor"),
            ("", "Still hiring hard",
             "<strong>296 open roles</strong> across 15 departments &mdash; including Bucharest, matching a Romanian entity in the sub-processor list")],
           cols=2)}
    <div class="ruleband">
      <div class="klabel">AND WHAT THEY ARE HIRING FOR &mdash; THE FORWARD-LOOKING HALF</div>
      <p>Sales <strong>89</strong> &middot; Engineering <strong>57</strong> &middot; Customer Experience
      <strong>38</strong>. <strong>Go-to-market is 72.0% of the board against 19.6% for engineering and
      product.</strong> So they are buying new logos rather than building &mdash; and that is where they
      will meet you.</p>
    </div>
  </div>
</section>''',
"""Employees rate them well. Four point one, eighty-two per cent would recommend, ninety
per cent approve of the CEO.

**The quote is the slide.** That is Glassdoor's own summary of the weak spots, in
Glassdoor's words, not mine: limited upward mobility, and pay against market. Read it out.

Then the card beside it, because it is what stops that being misread. The proxy puts
median employee compensation at a hundred and sixty-four thousand dollars. **This is not a
low-paying company.** So "limited upward mobility" is a complaint about the ceiling rather
than the floor — people are paid well and cannot see the next step. That is a different
problem, and a harder one to fix with money.

One thing that is *not* here, and I want to say why. I went looking for a
work-life-balance decline because that is the usual story at this
stage of a company's life. **It is not there.** Work-life balance tracks the overall
rating almost exactly. I am reporting that because it is what the evidence says, not
because it is interesting.

The complaints in Glassdoor's own summary are about ceilings rather than conditions:
management clarity, limited upward mobility, and compensation against market.

And they are hiring hard: **two hundred and ninety-six open roles across fifteen
departments**, taken from their own Greenhouse board rather than counted off the careers
page.

The band at the bottom is the part I would actually use. **Sales eighty-nine.
Engineering fifty-seven. Customer Experience thirty-eight.** Add the go-to-market
functions up and they are seventy-two per cent of the board, against under twenty per
cent for engineering and product — **roughly three and a half to one.** The single
largest department is Sales, on its own bigger than engineering and product combined.

Read that against slide twelve. Retention says expansion inside the existing base is
slowing and growth is moving to new logos. A hiring board that is three-quarters
go-to-market is what executing that shift looks like from outside — and it is a *leading*
indicator where retention is a lagging one.

Two limits on how hard I would push it. **A requisition is an intention, not a person**;
a board is a plan and plans get cut. And this is not a spend ratio — a sales req costs
less than a senior engineering one, so three and a half to one in headcount sits
comfortably with the audited two to one in money on slide thirty-four. Different
measures, same direction, which is what corroboration actually looks like.

One small corroboration I like: the board lists Bucharest, and the sub-processor
disclosure lists a Braze entity in "Ireland and Romania". Two unrelated documents
describing the same thing is how you know both are real.

Worth saying how this number got here, because it is a method point. The first pass
recorded the department split as uncapturable — the board's filter would not drive under
automation — and wrote it down as an open question. It was published as JSON the whole
time. **When a page will not yield, look for the API behind it before you record a
gap.**""",
    "m", "What employees say")

# ── 16 WHO THEY COMPETE WITH ─────────────────────────────────────────────────
# Both lists mark what is unique to them, in the same neutral treatment: Klaviyo appears
# only on Braze's list, the five specialists only on the buyers'. The old version accented
# one side in amber - the colour slide 3 teaches means medium-confidence evidence - which
# read as "these five are shakily sourced", the exact opposite of the point.
_cmp_named = ('<div><div class="klabel colhead">NAMED IN THE 10-K &mdash; THEIR CHOICE</div>'
              + logos(["Adobe", "Salesforce", "Iterable", "Klaviyo"], cols=2,
                      accent=("Klaviyo",)) + '</div>')
_cmp_buyer = ('<div><div class="klabel colhead">GARTNER&rsquo;S BUYER-DERIVED SHORTLIST &mdash; NOT THEIR CHOICE</div>'
              + logos(["Salesforce", "Adobe", "Iterable", "Oracle", "Optimove",
                       "Blueshift", "MoEngage", "CleverTap"], cols=4,
                      accent=("Oracle", "Optimove", "Blueshift", "MoEngage", "CleverTap")) + '</div>')

add(f'''<section class="s" data-g="m" data-t="Who they compete with">
  {head("Competition &middot; two lists", "They name four. Buyers weigh eight.")}
  <div class="body">
    {split(_cmp_named, _cmp_buyer)}
    <div class="ruleband">
      <div class="klabel">THE GAP IS THE FINDING</div>
      <p><strong>The brighter names on each side are the ones the other list does not have.</strong>
      Three of their four appear on the buyer list, so this is not a vendor misreading its market &mdash;
      but five vendors buyers compare them against appear nowhere in the 10-K. <strong>So those five are
      the ones to watch: Braze is not positioning against them, and will not have an answer ready.</strong></p>
    </div>
  </div>
</section>''',
"""Two lists. On the left, the four competitors Braze names in its own 10-K. On the right,
the vendors Gartner reports buyers *also considered* — derived from the buyers, not from
Braze.

Three names are shared. So this is not a company misreading its own market, and I will
not claim it is.

Note also that the asymmetry only runs one way. Klaviyo is on Braze's list and not on the
buyers'; everything else Braze names, buyers confirm. So the hypothesis we went in with —
that Braze would turn out to be shortlisted against a completely different set of vendors
— was only **partly** borne out, and I want that on the record as partly rather than as a
win.

**The asymmetry that remains is the finding.** The buyer list is twice as long, and the
five extra — Oracle, Optimove, Blueshift, MoEngage, CleverTap — are named nowhere in the
filing.

The character of those five is what matters, more than the count. Oracle is another suite.
But Optimove, Blueshift, MoEngage and CleverTap are mobile-engagement and CDP
**specialists**. And that changes the conversation, because Braze's own competitive frame
is "none of our competitors offer a comparable comprehensive solution" — they are arguing
they are broader than the suites. The buyer's frame includes a second, different question:
*is this better than a focused specialist at the one thing I actually need?* Those require
different answers. A briefing assembled only from Braze's own comparison pages prepares
you beautifully for the first conversation and walks you straight into the second.

Two things in Braze's favour from the same source, and I want them said with the same
weight as the criticism.

**First**, where Gartner's reviewers rate Braze above the two largest alternatives, they
name the same things twice: service and support, and ease of integration and deployment —
with evaluation and contracting added against Salesforce. That is independent,
buyer-sourced, and consistent: Braze is easier to buy from and easier to deploy than Adobe
or Salesforce. If we are going to quote Gartner when it helps us, we quote it here too.

**Second**, three of their four names are on the buyer list. This is a company that
understands its own market. Anyone hoping to find that Braze is confused about who it
competes with should stop looking; the evidence says the opposite.

The practical use of this slide is a shortlist, not a scoreboard. In an active deal, the
five specialists are who else is in the room — and their presence tells you the buyer is
weighing depth against breadth, which is the axis to prepare for.""",
    "m", "Who they compete with")
