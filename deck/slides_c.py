# -*- coding: utf-8 -*-
"""Part II — the product. Slides 18-32 (divider + 14 content slides).

The spine is one campaign walked through seven stages, which is what makes a technical
analysis legible to a non-technical audience and forces every capability claim to attach
to a moment a customer would notice.

Nested triple-quoted f-strings terminate the outer string early on this Python, so any
column that needs a component is built into a variable first. See slides_b.py.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *                                   # noqa: F403,E402

# ── 17 DIVIDER ───────────────────────────────────────────────────────────────
_pipe = flow([("01", "Data", ""), ("02", "Identity", ""), ("03", "Decisioning", ""),
              ("04", "Building", ""), ("05", "Content", ""), ("06", "Delivery", ""),
              ("07", "Interaction", "")], key={1, 6})

add(f'''<section class="s div-s" data-g="s" data-t="Part II: The product">
  {divider("Part II", "The product",
           ["One campaign, seven stages, end to end",
            "Where the limits are &mdash; in their words, not ours",
            "Which channel has no middleman",
            "What the AI actually is, on five lenses"],
           foot="Their technical documentation unless marked otherwise",
           extra='<div class="pipeline">' + _pipe + '</div>')}
</section>''',
"""Part two is the product, and we walk one campaign through seven stages: data arrives, a
profile updates, a segment recomputes, a journey triggers, content is composed, a message
is delivered, a response comes back.

I do it this way for two reasons. It forces every capability claim to attach to a moment
you would actually notice as a customer, rather than sitting in a feature list. And it
makes the weak points locate themselves — **the two stages I have highlighted, data in
and delivery out, are where everything interesting turned out to be**, and they are the
first and last thing that happens.

The source for almost all of it is Braze's own technical documentation: 1,352 pages,
read and indexed rather than skimmed. That matters because documentation is written to
stop support tickets, not to win deals, so it admits limits that no marketing page
will — and every hard limit in this deck came out of it.

Be fair to them as we go. Stages three, four and five are good, reviewers say so, and I
will say so too.""",
    "s", "Part II: The product")

# ── 18 HOW ONE CAMPAIGN WORKS ────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="How one campaign works">
  {head("The whole thing &middot; end to end", "One campaign, end to end")}
  <div class="body">
    {flow([("01", "Data arrives", "from an app, an API, or a data warehouse"),
           ("02", "Profile updated", "one record per person &mdash; billed per change"),
           ("03", "Segment recomputed", "membership changes as data lands"),
           ("04", "Journey triggers", "Braze calls this Canvas; it decides who continues"),
           ("05", "Content composed", "the message is filled in for that person"),
           ("06", "Message delivered", "email and SMS via named third parties"),
           ("07", "Response logged", "and it flows back to step 1")],
          key={1, 6})}
    <p>Seven stages, and the two picked out are the ones worth arguing about: how fresh the data is
    going in, and who physically sends the message going out. <strong>Everything between them is
    competent, so a pitch that attacks the middle will not land &mdash; aim at the ends.</strong></p>
  </div>
</section>''',
"""This is the loop. Data arrives, the profile updates, segments recompute, the journey
decides, content is composed, the message goes out, the response comes back.

I want to be fair before I am critical: **stages three, four and five are good.** Canvas
is the most documented thing in the platform after email, reviewers praise it, and
nothing I found contradicts that.

The interesting evidence is at the two ends. **Stage one** — how fresh is the data,
really. And **stage six** — who actually sends the message, which their sub-processor
disclosure has to tell you.

Note stage two as well: the profile update is the thing you are billed for.""",
    "s", "How one campaign works")

# ── 19 HOW DATA MOVES ────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="How data moves">
  {head("Data &middot; in, and back out", "The way in is not the way out")}
  <div class="body">
    {figs([("60,000<em>/min</em>", "ingest &mdash; <em>/users/track</em>, at 75 objects each"),
           ("250<em>/min</em>", "read profiles back by identifier, at 50 ids each", "neg"),
           ("250,000<em>/hr</em>", "bulk export to cloud storage")], size="sm")}
    <div class="ruleband">
      <div class="klabel">STATE THIS FAIRLY &mdash; IT IS NOT A LOCK-IN STORY</div>
      {tiles([("", "The asymmetry is real",
               "Writing reaches ~4.5m objects a minute. Reading profiles back reaches ~12,500 for a customer who joined after August 2024"),
              ("", "But they are different operations",
               "Event objects versus whole profiles. The ratio shows where priority sits, not like-for-like throughput"),
              ("", "And bulk export exists",
               "Segment export to cloud storage sits under a 250,000/hour limit. The sanctioned bulk route is generous")],
             cols=3)}
    </div>
    <p><strong>So getting off Braze is a project, not a setting.</strong> Price the migration work into
    any switching conversation, and make the bulk route &mdash; not the profile API &mdash; the plan.</p>
  </div>
</section>''',
"""Data in, data out.

Ingest is generous — sixty thousand requests a minute at seventy-five objects each, so
roughly four and a half million objects a minute.

Reading profiles back **by identifier** is two hundred and fifty requests a minute at
fifty identifiers each. About twelve and a half thousand profiles.

Now — I could stand here and tell you that is a three-hundred-to-one lock-in ratio. It
would land well and it would be wrong, so I am not going to.

They are different operations, and **bulk export exists and is generously limited**. If
you want your data out in volume, the sanctioned route works.

The interesting thing is not the ratio. It is the two hundred and fifty, and where it
came from — which is the next slide.""",
    "s", "How data moves")

# ── 20 STAGE 1 · DATA ────────────────────────────────────────────────────────
# An inline SVG rather than four cards. The point of this slide is that four lanes arrive
# at the same profile store at wildly different speeds, and a diagram shows that in one
# look where a card grid makes the reader assemble it. Colours are the grade tokens, so
# the three "not real-time" lanes read as one group without a legend.
# The mono detail line uses ASCII "->" rather than an arrow glyph on purpose: the static
# WOFF that make_release.sh inlines for the PDF is the latin subset, which has no U+2192
# in JetBrains Mono, and Chrome silently substitutes Menlo for that one character. The
# release check catches it as a fallback font; the screen render looks fine either way.
def _lane(y, label, detail, latency, note, tone):
    col = {"w": "var(--weak)", "s": "var(--strong)"}[tone]
    sub = (f'<text x="353" y="{y+38}" fill="var(--dim)" font-size="10.5" '
           f'font-family="JetBrains Mono, monospace" text-anchor="middle">{note}</text>') if note else ''
    return (
      f'<rect x="2" y="{y}" width="250" height="46" rx="5" fill="var(--panel)" stroke="{col}" stroke-width="1.2"/>'
      f'<text x="16" y="{y+20}" fill="var(--vellum)" font-size="14" font-family="Libre Franklin, sans-serif" font-weight="600">{label}</text>'
      f'<text x="16" y="{y+37}" fill="var(--dim)" font-size="11" font-family="JetBrains Mono, monospace">{detail}</text>'
      f'<line x1="252" y1="{y+23}" x2="454" y2="{y+23}" stroke="{col}" stroke-width="1.4" stroke-dasharray="{"5 4" if tone=="w" else "0"}"/>'
      f'<polygon points="454,{y+19} 462,{y+23} 454,{y+27}" fill="{col}"/>'
      f'<text x="353" y="{y+17}" fill="{col}" font-size="12" font-family="JetBrains Mono, monospace" text-anchor="middle">{latency}</text>'
      + sub)

_ingest_svg = (
  '<div class="mapwrap"><svg viewBox="0 0 700 236" preserveAspectRatio="xMidYMid meet" '
  'style="width:100%;max-width:700px;height:auto;display:block">'
  + _lane(2,   "Warehouse sync",      "their Cloud Data Ingestion",  "&ldquo;Not real-time&rdquo;",  "15 min floor", "w")
  + _lane(60,  "Warehouse segments",  "read in place, no copy",    "&ldquo;Not real-time&rdquo;",  "",             "w")
  + _lane(118, "Warehouse triggers",  "warehouse starts a journey", "&ldquo;Not real-time&rdquo;", "15 min floor", "w")
  + _lane(176, "/users/track &middot; SDKs", "app, server, stream", "&ldquo;Near-real-time&rdquo;", "", "s")
  + '<rect x="466" y="2" width="232" height="220" rx="6" fill="var(--panel)" stroke="var(--line2)" stroke-width="1.2"/>'
  + '<text x="582" y="100" fill="var(--vellum)" font-size="15" font-family="Libre Franklin, sans-serif" font-weight="600" text-anchor="middle">Braze user profile</text>'
  + '<text x="582" y="122" fill="var(--dim)" font-size="11.5" font-family="JetBrains Mono, monospace" text-anchor="middle">one record per person &middot; billed per change</text>'
  + '</svg></div>')

add(f'''<section class="s" data-g="s" data-t="Stage 1: Data">
  {head("Stage 1 &middot; data and freshness", "Their words: three of four are not real-time")}
  <div class="body">
    {_ingest_svg}
    <p>Warehouse syncs run &ldquo;from every 15 minutes to once per month&rdquo;. Going faster is not self-serve:
    <em>&ldquo;contact your customer success manager or use REST API ingestion.&rdquo;</em>
    <strong>If your customer data lives in a warehouse, fifteen minutes is the floor.</strong></p>
  </div>
</section>''',
"""Here is the slide six callback.

Braze publishes a comparison of its four ingestion paths and **grades the latency of each
one itself**. Three of the four carry the words "not real-time". The fourth says
"near-real-time, async processing".

This is not me characterising their product. This is their table, redrawn.

Look at what the diagram makes obvious that a list does not: **all four lanes end in the
same place.** The same user profile, the same MongoDB store, billed the same way per
attribute. What differs is only how long the data waits before it gets there — and for
three of the four lanes the answer is a scheduled job with a fifteen-minute floor.

That shared destination is the reason the distinction is worth your attention rather than
being a technicality. If the four paths ended in four different systems you would expect
four different latencies and think nothing of it. They do not. It is one profile store,
one billing meter, one segmentation engine reading from it — and the freshness of what
that engine sees depends entirely on which door your data came through. Two customers on
identical contracts can get materially different behaviour out of the same product.

And the practical sentence for a prospect: **if your customer data lives in a warehouse,
fifteen minutes is the floor** — and going faster is not something you can switch on. You
have to call your customer success manager, or re-plumb onto the API. That second option
is not a configuration change; it is an engineering project, and it moves the work from
Braze's side of the boundary to yours. Worth pricing that honestly when you compare: the
comparison is not licence against licence, it is licence-plus-integration-work against
licence.

Now the fairness, and I want it in the same breath rather than as a footnote. **Braze
published this table themselves.** They did not have to grade their own ingestion paths
and they did it in plain words. The SDK and API path genuinely is near-real-time, and the
qualifier they attach to it — async processing — is more honest than most of this
category manages. Nothing here is a false claim, and if I present it as one I will be
corrected in the room and deserve to be.

What is true is that one word is covering two architectures. So the question is not "is
it real-time", because they will say yes and they will be right. The question is
**which path will my data take, and what is the latency on that path** — and the answer
is in their own documentation before the meeting starts. We come back to this on the
deep-dive slide, because it turned out to be the single most useful question this whole
project produced.""",
    "s", "Stage 1: Data")

# ── 21 STAGE 2 · IDENTITY ────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Stage 2: Identity">
  {head("Stage 2 &middot; identity", "A merge can fail and still return success")}
  <div class="body">
    {figs([("unlimited", "aliases per profile"),
           ("1", "alias per label &mdash; unique across the base"),
           ("5", "identifier types accepted on ingest"),
           ("1", "identifier type for warehouse segments", "neg")], size="sm")}
    {cards([("A merge can decline and still report success",
             "&ldquo;If both profiles have invalid phone numbers, Braze does not merge them &hellip; <strong>The endpoint still returns 202 Accepted with a success message.</strong>&rdquo;", "r"),
            ("Reporting splits after a merge",
             "The dashboard attributes a pre-merge send to the surviving profile. Currents &mdash; their paid data-export feed &mdash; attributes it to the orphaned one. Both are right by their own rules, and they disagree.", "a")],
           cols=2)}
    <p><strong>So an engineering team should test a merge failure on day one</strong> &mdash; send two
    profiles with bad phone numbers and check the profile, not the response code.</p>
  </div>
</section>''',
"""Identity is generous at the top and narrow at the bottom. Unlimited aliases on a
profile — but a warehouse-driven segment can only be built on **one** identifier type,
where ingestion accepts five.

Then two behaviours from their own documentation that no marketing page will tell you,
and both fail quietly.

**A merge can decline and still tell you it worked.** If both profiles have invalid
phone numbers, Braze skips the merge — and returns two-oh-two Accepted with a success
message. Their words: the response "does not indicate that the merge was skipped."

**And reporting splits after a merge.** The dashboard attributes a send one way; Currents
and Query Builder attribute it the other. If you are joining Braze data to a warehouse,
that is a reconciliation problem you will find at month end rather than at integration
time.""",
    "s", "Stage 2: Identity")

# ── 22 STAGE 3 · DECISIONING ─────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Stage 3: Decisioning">
  {head("Stage 3 &middot; decisioning", "Deciding who gets a message")}
  <div class="body">
    <p><strong>Two systems decide who gets a message, and they sit on two different databases
    that do not talk to each other.</strong> One follows rules you write; the other runs models.</p>
    {split(
      '<div><div class="klabel colhead">RULE-BASED &mdash; MONGODB</div>'
      + tiles([("", "Segmentation", "Custom events, attributes and most targeting"),
               ("", "Segment Extensions", "SQL, but served from Snowflake"),
               ("", "Global Control Group", "Holdouts &mdash; people left un-messaged, to measure lift")], cols=1)
      + '</div>',
      '<div><div class="klabel colhead">MODEL-BASED &mdash; SNOWFLAKE</div>'
      + tiles([("", "Predictive Suite", "Churn and event prediction"),
               ("", "AI item recommendations", "Snowflake-backed"),
               ("", "Decisioning Studio", "Was OfferFit until June 2025")], cols=1)
      + '</div>')}
    <p>Braze flags the consequence itself: &ldquo;Removing data from one system does not automatically
    remove it from the other.&rdquo; <strong>So deleting bad data means deleting it twice</strong> &mdash;
    and a deletion request that only clears one side is a compliance problem, not a tidiness one.</p>
  </div>
</section>''',
"""Decisioning runs on two engines sitting on two different databases, and Braze publishes
which is which.

Rules and segmentation run on MongoDB. The model-driven things — Predictive Suite,
recommendations, Decisioning Studio — run on Snowflake.

That is a sensible architecture and I am not criticising it. But it has a consequence
they flag themselves, under an "important" callout: **removing data from one system does
not automatically remove it from the other.**

If you have deletion obligations — and if you are in this category you do — that is a
two-system problem, disclosed in their own documentation and in none of their marketing.

Note the seven documentation pages on Predictive Suite. Hold that for slide thirty-two.""",
    "s", "Stage 3: Decisioning")

# ── 23 STAGE 4 · BUILDING ────────────────────────────────────────────────────
add(f'''<section class="s" data-g="m" data-t="Stage 4: Building">
  {head("Stage 4 &middot; building a journey", "Canvas is the strongest thing in the platform")}
  <div class="body">
    {figs([("249", "focused documentation pages on Canvas"),
           ("10", "Canvas API endpoints"),
           ("385", "G2 reviews tagged &lsquo;Ease of Use&rsquo;"),
           ("139", "tagged &lsquo;Learning Curve&rsquo;", "neg")], size="sm")}
    <div class="quote"><div class="qbody">&ldquo;Canvas makes it easy to build complex, branching lifecycle flows &hellip;
      Being able to trigger contextual push notifications, in-app messages, and emails from live event
      streams &mdash; <strong>without needing engineering for every small tweak</strong> &mdash; is a huge win.&rdquo;</div>
      <div class="qd">Enterprise IT manager, G2 &middot; 5/5 &middot; August 2026</div></div>
    <p><strong>So do not attack Canvas.</strong> It is the thing their customers like most, and a pitch
    that calls it weak will be contradicted by the room.</p>
  </div>
</section>''',
"""This is the slide where I tell you what is good, because an analysis that only finds
problems was not an analysis.

**Canvas is the strongest thing in this platform.** Two hundred and forty-nine focused
documentation pages, ten API endpoints, and reviewers consistently praise it. The single
most common positive tag on G2, three hundred and eighty-five times, is ease of use.

The quote is from a five-star enterprise review and it names the thing that actually
matters commercially: marketers can change journeys **without engineering**. That is the
core of the value proposition and the evidence supports it.

The counterweight is on the same slide and it is real: a hundred and thirty-nine reviews
tag learning curve, eighty-six say steep learning curve. Easy once you know it; not easy
to learn.""",
    "m", "Stage 4: Building")

# ── 24 STAGE 5 · CONTENT ─────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Stage 5: Content">
  {head("Stage 5 &middot; content and personalisation", "Composing the message")}
  <div class="body">
    {figs([("123", "focused doc pages on Liquid templating"),
           ("43", "on Connected Content"),
           ("38", "on Content Blocks"),
           ("78", "on Catalogs")], size="sm")}
    {cards([("What it gives you",
             "Liquid templating, Connected Content for live API calls at send time, reusable Content Blocks, and product catalogs for item-level personalisation.", "g"),
            ("What reviewers say about it",
             "&ldquo;Liquid personalization and Connected Content also make it straightforward to scale truly dynamic messaging&rdquo; &mdash; and, from the same reviewer, &ldquo;a challenging learning curve around Liquid syntax&rdquo; for non-technical users.", "a")],
           cols=2)}
    <p><strong>So ask who writes the messages.</strong> If the answer is marketers rather than engineers,
    the learning curve is a real cost and it lands on the team you are selling to.</p>
  </div>
</section>''',
"""Content is Liquid — the templating language — plus Connected Content for live API calls
at send time, Content Blocks for reuse, and catalogs for item-level personalisation.

A hundred and twenty-three focused pages on Liquid alone. This is a serious
personalisation layer and it is well documented.

And the same reviewer who praises it names the cost in the same breath: **a challenging
learning curve around Liquid syntax for non-technical users.**

That is the honest shape of this product generally, and it comes up again and again in
the review corpus. Very capable in the hands of someone technical. Harder than the
marketing suggests for the marketer it is sold to.""",
    "s", "Stage 5: Content")

# ── 25 STAGE 6 · DELIVERY ────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Stage 6: Delivery">
  {head("Stage 6 &middot; delivery", "Only two channels have a named middleman")}
  <div class="body">
    {split(
      '<div><div class="klabel colhead">CHANNELS WITH A NAMED DELIVERY SUB-PROCESSOR</div>'
      + tiles([("", "Email &mdash; three of them", "Amazon SES &middot; Bird.com (SparkPost) &middot; Twilio (SendGrid). Plus Mailgun for previewing"),
               ("", "SMS / mobile messages &mdash; two", "Infobip &middot; Twilio")], cols=1)
      + '</div>',
      '<div><div class="klabel colhead">CHANNELS WITH NONE NAMED</div>'
      + logos(["Push", "In-app", "Content Cards", "Banners", "Webhooks",
               "WhatsApp", "LINE", "KakaoTalk", "Landing pages", "Live notif."], cols=2)
      + '</div>',
      ratio="1.15fr 0.85fr")}
    <p>Absence is not proof of no intermediary &mdash; APNs, FCM and the WhatsApp, LINE and Kakao business
    APIs may sit outside the definition. <strong>So a buyer cannot establish from this document who touches
    their messages on eleven of thirteen channels.</strong> That is a question to put to them, not a gap to
    assume the worst about &mdash; and on email, three interchangeable senders is deliberate redundancy.</p>
  </div>
</section>''',
"""This is the slide that only exists because they are legally obliged to publish it.

The sub-processor disclosure — revision first of June this year — names seventeen third
parties. For delivery, it names middlemen on exactly two channels. **Email has three.
SMS has two. Everything else has none named.**

Now, the caveat matters and I am putting it on the slide rather than hiding it in the
notes: absence from a sub-processor list is not proof there is no intermediary. Apple's
and Google's push transports, and the WhatsApp and LINE business APIs, may simply sit
outside the definition.

What you *can* take away is the email arrangement, and it is a point in Braze's favour:
**three interchangeable delivery providers on their highest-volume channel.** If you were
hoping email deliverability was a single point of failure you could attack, it is not.""",
    "s", "Stage 6: Delivery")

# ── 26 STAGE 7 · INTERACTION ─────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Stage 7: Interaction">
  {head("Stage 7 &middot; interaction and the loop back", "When the customer replies")}
  <div class="body">
    {figs([("71", "focused doc pages on Webhooks"),
           ("5 min", "Currents export cadence &mdash; or every 15,000 events"),
           ("add-on", "Currents is &ldquo;an optional Braze add-on&rdquo;", "neg"),
           ("free", "engagement events are not billed as data points")], size="sm")}
    <p>Inbound and two-way handling is real: webhooks are a first-class documented channel, and
    engagement tracking &mdash; opens, clicks, push receipts &mdash; is excluded from data-point billing.</p>
    <div class="ruleband">
      <div class="klabel">WEBHOOKS IS THE MOST UNDER-SOLD THING IN THE PLATFORM</div>
      {tiles([("", "Fifth-deepest channel in the product",
               "71 focused pages &mdash; behind only email, in-app, SMS and push, and sold under no name at all."),
              ("", "Which cuts both ways for us",
               "A real integration surface we should not pretend is absent &mdash; and one their own sellers "
               "are least likely to lead with.")],
             cols=2)}
      <p style="margin-top:14px"><strong>So the round trip costs more than the outbound leg.</strong>
      Getting the raw stream back is a paid add-on on a five-minute cadence &mdash; budget for it when you
      compare list prices.</p>
    </div>
  </div>
</section>''',
"""The loop closes. Responses come back as engagement events, and here Braze does something
genuinely customer-friendly: **engagement tracking is free.** Opens, clicks, push
receipts — none of it counts against your data points. Say that when you are being fair
about their pricing.

But look at the third figure. Getting the **raw** event stream back out means Currents,
and Currents is — their word — "an optional Braze add-on". It exports every five minutes,
or every fifteen thousand events.

Connect that to slide fourteen. Thirty-six per cent of TrustRadius reviewers call
reporting limited and unintuitive. A G2 reviewer says out-of-the-box reporting "feels too
basic unless you export raw data through paid add-ons like Currents."

**The complaint and the mechanism are two independent sources describing the same
thing.** That is when you can be confident it is real.""",
    "s", "Stage 7: Interaction")

# ── 27 CHANNELS ──────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Channels">
  {head("Channels &middot; counted from both ends", "Thirteen documented. Ten marketed.")}
  <div class="body">
    {split(
      '<div><div class="klabel colhead">DEEP &mdash; FOCUSED DOCUMENTATION PAGES</div>'
      + bars([("Email", 347), ("In-app messages", 115), ("SMS / MMS / RCS", 89), ("Push", 73),
              ("Webhooks", 71), ("WhatsApp", 56), ("Content Cards", 47)])
      + '</div>',
      '<div><div class="klabel colhead">THIN &mdash; REAL, BUT NOT COMPARABLE</div>'
      + bars([("Banners", 28), ("Landing pages", 21), ("LINE", 11), ("Web push", 11),
              ("Live notifications", 8), ("KakaoTalk", 5), ("Transactional email", 4)])
      + '</div>',
      ratio="1fr 1fr")}
    <p>Thirteen channels is broad &mdash; broader than several specialists on slide 17. But <strong>three
    are the product and ten are completeness</strong>: email alone outweighs the next three combined.
    <strong>So compete on the thin ones.</strong> A prospect buying for KakaoTalk or LINE is buying five
    and eleven pages of documentation, not the platform email buyers get. One line on the drift: five of
    these ship with no marketing page, and Webhooks &mdash; fifth deepest &mdash; is one of them.</p>
  </div>
</section>''',
"""Thirteen channels are documented. That is broad, not narrow — I went in expecting the
opposite and the evidence killed it.

What is interesting is the drift, and it runs in both directions at once.

**Five documented channels have no marketing page anywhere.** The biggest is landing
pages — eleven user-guide pages plus three partner pages. A real capability that is sold
under no name.

**And one marketed channel is missing from their own documentation index.** KakaoTalk has
four doc pages and a product page, and their channels index mentions it zero times.

Neither of those is damning. Together they tell you something useful about how the
company runs: **the documentation and the marketing are maintained by people who are not
talking to each other**, which is exactly the seam this whole method looks for.""",
    "s", "Channels")

# ── 28 INTEGRATIONS ──────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="m" data-t="Integrations">
  {head("Integrations &middot; the Alloys network", "Wide network, one page deep")}
  <div class="body">
    {figs([("150+", "technology partners &mdash; their claim"),
           ("322", "partner documentation pages"),
           ("~810", "average words per partner page"),
           ("~2,708", "average words per developer-guide page")], size="sm", focus=2)}
    <p>The network is real and wide, but its documentation is <strong>second-largest by page count and
    close to thinnest by words per page</strong> &mdash; one short entry per partner. <strong>So treat 150+
    as a directory, not a depth claim: test the two integrations you actually need before believing
    it.</strong></p>
    {cards([("What is bought", "Delivery (Twilio, Infobip, SendGrid, SparkPost, SES), warehousing (Snowflake, Databricks, BigQuery), models (Anthropic, OpenAI, Google) &mdash; all from the sub-processor list", "g"),
            ("What is built", "The ingestion layer, Canvas, Liquid, the identity model, Currents, and the integration surface itself", "g")],
           cols=2)}
  </div>
</section>''',
"""Braze claims over a hundred and fifty technology partners, which they call Alloys.
That is their number and I have graded it as a claim.

What I can measure is the documentation. **Three hundred and twenty-two partner pages —
the second largest section in the corpus — averaging about eight hundred and ten words
each.** The developer guide is a third the size and averages more than three times the
words per page.

That is the shape of a broad network documented at one short page per partner. Wide, and
shallow in documentation terms. Which is not a criticism — it may be all a connector
needs — but if you are being told the integration layer is deep, this is the measurement
that tests it.

Underneath: the delivery, the warehouses and the models are all bought. The ingestion
layer, Canvas, Liquid and the identity model are built.""",
    "m", "Integrations")

# ── 29 INFRASTRUCTURE ────────────────────────────────────────────────────────
# The map earns its place here rather than on the revenue-geography slide: these are the
# fifteen named clusters from the status page, pinned at the regions their own endpoint
# hostnames give (iad = Ashburn VA, fra = Frankfurt, and the AWS region codes in CT for
# the rest). US-08 is not pinned separately: nothing in the corpus places it in a specific
# US region, and inventing a coordinate for the one cluster slide 35 is about would be the
# worst possible place to guess. The legend points at it in words instead of in colour.
_clusters_map = worldmap([
    (-77.5, 38.9, "US &times;9", "m", "left"),
    (  8.7, 50.1, "EU &times;2", "m", "above"),
    (139.7, 35.7, "JP 01",       "m", "right"),
    # Seoul and Tokyo are 12 degrees apart, which is narrower than two pin halos at this
    # projection. Labelling KR above rather than left keeps both readable without moving
    # either pin off its actual longitude.
    (127.0, 37.6, "KR 01",       "m", "above"),
    (106.8, -6.2, "ID 01",       "m", "below"),
    (151.2,-33.9, "AU 01",       "m", "below"),
])
_map_legend = ('<div class="maplegend">'
               '<span><i class="lg lg-m"></i>15 clusters, 6 territories</span>'
               '<span><i class="lg lg-s"></i>7 identical subsystems in every one</span>'
               '<span class="lgnote">one of the nine US clusters is the exception &mdash; slide 35</span>'
               '</div>')
_subsystems = ('<div><div class="klabel colhead">THE SEVEN SUBSYSTEMS, IDENTICAL IN EVERY CLUSTER</div>'
               + logos(["Dashboard", "SDK Data Collection", "Data Processing", "REST APIs",
                        "Outbound Messaging", "Currents", "Cloud Data-Ingestion"], cols=1)
               + '<p style="margin-top:12px">The sub-processor disclosure lists AWS regions for the same '
                 'six territories. <strong>So data residency is available in six places and nowhere else '
                 '&mdash; ask which cluster before the contract.</strong></p></div>')

add(f'''<section class="s" data-g="s" data-t="Infrastructure">
  {head("Infrastructure &middot; the status page as a disclosure", "Fifteen clusters, seven subsystems &mdash; and one exception")}
  <div class="body">
    {split('<div>' + _clusters_map + _map_legend + '</div>', _subsystems, ratio="1.25fr 0.75fr")}
  </div>
</section>''',
"""The status page is an architecture disclosure Braze made by accident.

Fifteen regional clusters across six territories, and every one exposes the same seven
subsystems. That is a functional decomposition of the entire product, published live and
updated during outages. Notice that Currents and Cloud Data Ingestion appear as
first-class subsystems rather than as features — which tells you they can fail
independently, and the incident record on slide 39 shows they do.

The geography checks out against a completely unrelated document: the sub-processor
disclosure lists AWS regions for the same six territories. Two sources, no relationship
between them, same answer.

For a buyer with data-residency obligations this map is the answer to the question they
actually have. Not "do you support the EU" — everyone says yes — but "which of your
clusters would my data sit in, and what else is in that cluster". Fifteen named clusters
is a real answer.

Two things to hold. There is no US 09 — they run one to eight, then ten. I do not know
why, and I am not going to invent a reason.

And US 08 is marked differently, because that is the next part.""",
    "s", "Infrastructure")

# ── 30 ANALYTICS ─────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Analytics">
  {head("Analytics &middot; what you can measure", "What you can measure")}
  <div class="body">
    {figs([("36%", "of recent TrustRadius reviewers call reporting limited and unintuitive", "neg"),
           ("140", "G2 reviews tagged &lsquo;Missing Features&rsquo;"),
           ("27", "focused doc pages on the Global Control Group"),
           ("2am ET", "when your billing dashboard refreshes &mdash; daily, cached")], size="sm")}
    {cards([("What is genuinely there",
             "Holdouts and a Global Control Group for incrementality, campaign and KPI endpoints, and a Snowflake data share that avoids copying data at all.", "g"),
            ("What reviewers keep hitting",
             "&ldquo;The out-of-the-box reporting still feels too basic unless you export raw data through paid add-ons like Currents.&rdquo;", "r")],
           cols=2)}
    <p><strong>So ask a prospect what they report on today, and who builds it.</strong> If the answer
    involves exporting to a warehouse, they are already paying for the add-on that fixes this.</p>
  </div>
</section>''',
"""Analytics is where the review corpus is most consistent, across panels that have nothing
to do with each other.

To be fair first: incrementality measurement is properly supported — holdouts, a global
control group, twenty-seven focused pages on it. There are analytics endpoints. And the
Snowflake data share lets you query without copying data at all, which is genuinely good
engineering.

But thirty-six per cent of recent TrustRadius reviewers call reporting limited and
unintuitive, and G2's most common criticism tag is missing features.

And the mechanism is the one we saw at stage seven: the fix is a paid add-on.

One small detail I enjoyed, because it is so specific: **your data-point usage dashboard
— the thing that tells you what you are spending — is cached and refreshes once a day
around 2am Eastern.** The billing meter is not real-time either.""",
    "s", "Analytics")

# ── 31 THE AI, HONESTLY ──────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="The AI, honestly">
  {head("The AI &middot; five independent lenses", "Bought recently, running on other people&rsquo;s models")}
  <div class="body">
    {flow([("2011&ndash;", "The platform", "segmentation, journeys, Liquid &mdash; a decade of it"),
           ("Jun 2025", "The engine, bought", "OfferFit, $303.2m, renamed Decisioning Studio"),
           ("Now", "The models, rented", "Anthropic, OpenAI and Google, named in their own disclosure")],
          key={2, 3})}
    {split(
      '<div><div class="klabel colhead">AND WHAT EACH LAYER MEASURES &mdash; FOCUSED DOC PAGES</div>'
      + bars([("Email", 347), ("Canvas", 249), ("Segmentation", 242),
              ("Recommendations", 73), ("Decisioning Studio", 22, "medium"),
              ("Agents", 17, "medium"), ("Predictive Suite", 7, "weak")])
      + '</div>',
      '<div><div class="klabel colhead">LENSES 2&ndash;5</div>'
      + tiles([("", "0 of 135 API endpoints", "28 namespaces, none of them AI or decisioning"),
               ("", "Reviewers name copywriting", "Two G2 reviewers say the AI copy needs &ldquo;a careful human hand&rdquo;"),
               ("", "So the useful question is one line", "&ldquo;Can I call your AI from my own systems?&rdquo; Today the documented answer is no &mdash; which is what a data-science team needs to hear before they plan around it")], cols=1)
      + '</div>',
      ratio="1.05fr 0.95fr")}
  </div>
</section>''',
"""This is the slide most likely to go wrong, so I am going to be careful.

**I am not going to tell you their AI is thin.** That sentence is unfalsifiable and the
evidence does not need it.

Here is what five independent lenses say instead.

**Documentation.** Predictive Suite has seven focused pages. Agents seventeen.
Decisioning Studio twenty-two. Canvas has two hundred and forty-nine. "Focused" means the
page is about the thing rather than mentioning it.

**The API.** Of a hundred and thirty-five published endpoints across twenty-eight
namespaces, the number in an AI, prediction, agent or decisioning namespace is **zero**.

**The models.** Anthropic, OpenAI and Google — named in their own compelled disclosure.

**The engine.** Bought, June 2025, three hundred and three million dollars.

**And customers.** Reviewers talk about AI copywriting, and two of them independently say
it needs a human pass. Nobody in the sample mentions decisioning at all.

Now the caveats, because a documentation count is easy to over-read and I would rather
raise the objection than be handed it. **A new product is under-documented by
construction.** Decisioning Studio is fifteen months old inside Braze; Canvas has had a
decade. And **some things are genuinely short to document** — Intelligent Timing is a
toggle with a model behind it. So read these as *surface area*, which is what they
measure, and not as a verdict on quality, which they cannot.

Lens two is the one I would actually put in front of a technical buyer, because it has
consequences they will hit. No AI namespace means the AI features cannot be orchestrated
from outside the product: you cannot trigger a prediction, retrieve a recommendation or
configure an agent programmatically. They cannot be tested in a CI pipeline the way a
campaign trigger can. And they cannot be composed with the customer's own models. For an
organisation that already runs data science, that is the difference between a platform
capability and a black box.

On the models, the fair framing matters. Using foundation models from suppliers is
ordinary — almost nobody trains their own, and three rather than one is a sensible hedge.
What is unusual is only that Braze is legally obliged to name them. So the narrow, firm
claim is this: **any suggestion that Braze's AI is proprietary at the model layer is
contradicted by Braze's own compelled disclosure.** What *is* proprietary is the
integration, the data model the models see, and the decisioning logic they paid three
hundred million for — a real asset, and I am not diminishing it.

So the defensible sentence is: real, shipping, recently and largely acquired, running on
three named suppliers' models, with no API of its own, documented at a fraction of the
depth of the established platform. Every clause sourced separately, from a different kind
of source, and no clause leaning on another.

What it does not support is "their AI is thin". That sentence is unfalsifiable, the
evidence does not need it, and the first prospect who opens the product and sees a working
decisioning engine will disprove it for us. The sourced version survives that
demonstration. And the genuinely useful question, which falls straight out of lens two, is
one line: **can I call your AI from my own systems?** Today the documented answer is no.""",
    "s", "The AI, honestly")
