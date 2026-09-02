# -*- coding: utf-8 -*-
"""Part II — the product. Slides 17-31 (divider + 14 content slides).

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
"""Part two is the product, and we walk one campaign through seven stages.

I do it this way because it forces every claim to attach to a moment you would actually
notice as a customer — and because the two stages I have highlighted, **data in** and
**delivery out**, are where everything interesting turned out to be.""",
    "s", "Part II: The product")

# ── 18 HOW ONE CAMPAIGN WORKS ────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="How one campaign works">
  {head("The whole thing &middot; end to end", "What actually happens when a campaign runs")}
  <div class="body">
    {flow([("01", "Data arrives", "SDK, API, or a warehouse sync"),
           ("02", "Profile updated", "MongoDB &mdash; and it is billed per attribute"),
           ("03", "Segment recomputed", "membership changes as data lands"),
           ("04", "Canvas triggers", "the journey builder decides who continues"),
           ("05", "Content composed", "Liquid, Connected Content, catalogs"),
           ("06", "Message delivered", "email and SMS via named third parties"),
           ("07", "Response logged", "and it flows back to step 1")],
          mark={1: "s", 2: "s", 6: "m"})}
    <p>Seven stages. <strong>Two of them are where the evidence turned out to be interesting</strong> &mdash;
    how fresh the data is at stage one, and who physically sends the message at stage six. Everything
    in between is competent and largely as advertised, and I will say so as we go.</p>
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
               "Writing reaches ~4.5m objects a minute. Reading profiles back by identifier reaches ~12,500 a minute for a customer who joined after August 2024"),
              ("", "But they are different operations",
               "Writing event objects versus reading whole profiles. The ratio shows where priority sits, not like-for-like throughput"),
              ("", "And bulk export exists",
               "Segment export to cloud storage sits under the default 250,000/hour limit. The sanctioned bulk route is generous")],
             cols=3)}
    </div>
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
add(f'''<section class="s" data-g="s" data-t="Stage 1: Data">
  {head("Stage 1 &middot; data and freshness", "Their table. Their words. Three of four are not real-time")}
  <div class="body">
    {cards([("Standard CDI sync",
             "&ldquo;<strong>Not real-time</strong>; minimum 15-minute sync cadence&rdquo;", "r"),
            ("CDI Segments",
             "&ldquo;<strong>Not real-time</strong>; refreshes on your Segment Extension schedule&rdquo;", "r"),
            ("CDI Canvas triggers",
             "&ldquo;<strong>Not real-time</strong>; bounded by sync schedule (minimum 15 minutes)&rdquo;", "r"),
            ("/users/track and the SDKs",
             "&ldquo;<strong>Near-real-time</strong> (async processing)&rdquo;", "g")],
           cols=4)}
    <p>Warehouse syncs run &ldquo;from every 15 minutes to once per month&rdquo;. Going faster is not self-serve:
    <em>&ldquo;contact your customer success manager or use REST API ingestion.&rdquo;</em>
    <strong>If your customer data lives in a warehouse, fifteen minutes is the floor.</strong></p>
  </div>
</section>''',
"""Here is the slide six callback.

Braze publishes a comparison of its four ingestion paths and **grades the latency of each
one itself**. Three of the four carry the words "not real-time". The fourth says
"near-real-time, async processing".

This is not me characterising their product. This is their table.

And the practical sentence for a prospect: **if your customer data lives in a warehouse,
fifteen minutes is the floor** — and going faster is not something you can switch on. You
have to call your customer success manager, or re-plumb onto the API.

The fair framing, which I would use in front of them: real-time is true of the SDK path.
It is one word covering two architectures. Ask which one you are buying.""",
    "s", "Stage 1: Data")

# ── 21 STAGE 2 · IDENTITY ────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Stage 2: Identity">
  {head("Stage 2 &middot; identity", "Generous at the top, narrow at the bottom, quiet when it fails")}
  <div class="body">
    {figs([("unlimited", "aliases per profile"),
           ("1", "alias per label &mdash; unique across the base"),
           ("5", "identifier types accepted on ingest"),
           ("1", "identifier type for warehouse segments", "neg")], size="sm")}
    {cards([("A merge can decline and still report success",
             "&ldquo;If both profiles have invalid phone numbers, Braze does not merge them &hellip; <strong>The endpoint still returns 202 Accepted with a success message</strong>, so the HTTP response does not indicate that the merge was skipped.&rdquo;", "r"),
            ("Reporting splits after a merge",
             "Dashboard summaries attribute a pre-merge send to the surviving profile. Currents, Query Builder and Messaging History attribute it to the orphaned one. Both are right by their own rules, and they disagree.", "a")],
           cols=2)}
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
  {head("Stage 3 &middot; decisioning", "Two engines, two databases, one of them bought")}
  <div class="body">
    {split(
      '<div><div class="klabel colhead">RULE-BASED &mdash; MONGODB</div>'
      + tiles([("", "Segmentation", "Custom events, attributes, purchases and most targeting"),
               ("", "Segment Extensions", "SQL, but served from Snowflake"),
               ("", "Global Control Group", "Holdouts, and profiles in it never merge")], cols=1)
      + '</div>',
      '<div><div class="klabel colhead">MODEL-BASED &mdash; SNOWFLAKE</div>'
      + tiles([("", "Predictive Suite", "Churn and event prediction &mdash; 7 focused doc pages"),
               ("", "AI item recommendations", "Snowflake-backed"),
               ("", "Decisioning Studio", "Was OfferFit until June 2025")], cols=1)
      + '</div>')}
    <p><strong>The split has a customer-visible consequence Braze flags itself:</strong>
    &ldquo;Removing data from one system does not automatically remove it from the other.&rdquo;
    Deleting bad event data means doing it in MongoDB, separately from anything Snowflake-backed.</p>
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

Note the seven documentation pages on Predictive Suite. Hold that for slide thirty-one.""",
    "s", "Stage 3: Decisioning")

# ── 23 STAGE 4 · BUILDING ────────────────────────────────────────────────────
add(f'''<section class="s" data-g="m" data-t="Stage 4: Building">
  {head("Stage 4 &middot; building a journey", "Canvas is the strongest thing in the platform")}
  <div class="body">
    {figs([("249", "focused documentation pages on Canvas"),
           ("10", "Canvas API endpoints"),
           ("385", "G2 reviews tagged &lsquo;Ease of Use&rsquo;"),
           ("139", "tagged &lsquo;Learning Curve&rsquo;", "neg")], size="sm")}
    <div class="quote"><div class="q">&ldquo;Canvas makes it easy to build complex, branching lifecycle flows &hellip;
      Being able to trigger contextual push notifications, in-app messages, and emails from live event
      streams &mdash; <strong>without needing engineering for every small tweak</strong> &mdash; is a huge win.&rdquo;</div>
      <div class="qd">Enterprise IT manager, G2 &middot; 5/5 &middot; August 2026</div></div>
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
  {head("Stage 5 &middot; content and personalisation", "Liquid is the substrate, and it is also the complaint")}
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
    <p><strong>Say what the disclosure names, not what exists.</strong> Absence here is not proof of no
    intermediary &mdash; APNs, FCM and the WhatsApp/LINE/Kakao business APIs may sit outside the
    definition of a sub-processor. What is certain is that <strong>email has three interchangeable
    senders</strong>, which is deliberate redundancy on their highest-volume channel.</p>
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
  {head("Stage 7 &middot; interaction and the loop back", "The response comes back, and it is billed differently")}
  <div class="body">
    {figs([("71", "focused doc pages on Webhooks"),
           ("5 min", "Currents export cadence &mdash; or every 15,000 events"),
           ("add-on", "Currents is &ldquo;an optional Braze add-on&rdquo;", "neg"),
           ("free", "engagement events are not billed as data points")], size="sm")}
    <p>Inbound and two-way handling is real: webhooks are a first-class documented channel, and
    engagement tracking &mdash; opens, clicks, push receipts &mdash; is explicitly excluded from data-point
    billing. <strong>But getting the raw event stream back out is a paid add-on that exports on a
    five-minute cadence</strong>, which is the mechanism behind the reporting complaint on slide 14.</p>
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
  {head("Channels &middot; counted from both ends", "Thirteen documented. Ten marketed. The drift runs both ways")}
  <div class="body">
    {split(
      '<div><div class="klabel colhead">DOCUMENTED, WITH NO MARKETING PAGE</div>'
      + logos(["Banners", "Transactional email", "Landing pages", "Live notifications", "Webhooks"], cols=1,
              accent=("Landing pages",))
      + '</div>',
      '<div><div class="klabel colhead">MARKETED, BUT MISSING FROM THEIR OWN DOCS CHANNEL INDEX</div>'
      + logos(["KakaoTalk"], cols=1, accent=("KakaoTalk",))
      + '<p style="margin-top:18px">Four KakaoTalk documentation pages exist &mdash; setup, message creation, click '
        'tracking, reporting &mdash; and a product page at <span class="mono">/product/kakaotalk-messenger</span>. '
        'The channels index mentions it <strong>zero</strong> times.</p></div>',
      ratio="1fr 1fr")}
    <p><strong>Landing pages is the one to notice</strong>: eleven user-guide pages plus three partner pages,
    a substantial documented capability sold under no name at all.</p>
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
  {head("Integrations &middot; the Alloys network", "Broad, and documented shallowly")}
  <div class="body">
    {figs([("150+", "technology partners &mdash; their claim"),
           ("322", "partner documentation pages"),
           ("~810", "average words per partner page"),
           ("~2,708", "average words per developer-guide page")], size="sm", focus=2)}
    <p>The integration network is real and wide. But the documentation shape says something about its
    depth: <strong>the partner section is the second-largest in the corpus by page count and close to the
    thinnest by words per page</strong> &mdash; a lot of short entries, roughly one per partner. The developer
    guide, a third the size, carries more than three times the words per page.</p>
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
add(f'''<section class="s" data-g="s" data-t="Infrastructure">
  {head("Infrastructure &middot; the status page as a disclosure", "Fifteen clusters, seven subsystems each &mdash; and one exception")}
  <div class="body">
    {split(
      '<div><div class="klabel colhead">THE SEVEN SUBSYSTEMS IN EVERY CLUSTER</div>'
      + logos(["Dashboard", "SDK Data Collection", "Data Processing", "REST APIs",
               "Outbound Messaging", "Currents", "Cloud Data-Ingestion"], cols=1)
      + '</div>',
      '<div><div class="klabel colhead">THE FIFTEEN CLUSTERS</div>'
      + logos(["US 01", "US 02", "US 03", "US 04", "US 05", "US 06", "US 07", "US 08",
               "US 10", "EU 01", "EU 02", "AU 01", "ID 01", "JP 01", "KR 01"], cols=5,
              accent=("US 08",))
      + '<p style="margin-top:16px">Corroborated independently: the sub-processor disclosure lists AWS regions for '
        'the US, EU, Australia, Indonesia, Japan and South Korea &mdash; the same six geographies. '
        '<strong>There is no US 09.</strong></p></div>',
      ratio="0.8fr 1.2fr")}
  </div>
</section>''',
"""The status page is an architecture disclosure Braze made by accident.

Fifteen regional clusters, and every one exposes the same seven subsystems. That is a
functional decomposition of the entire product, published live and updated during
outages. Notice that Currents and Cloud Data Ingestion are first-class subsystems, not
features.

The geography checks out against a completely unrelated document: the sub-processor
disclosure lists AWS regions for the same six territories.

Two small things. There is no US 09 — they run one to eight, then ten. I do not know
why, and I am not going to invent a reason.

And US 08 is highlighted, because that is the next slide.""",
    "s", "Infrastructure")

# ── 30 ANALYTICS ─────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Analytics">
  {head("Analytics &middot; what you can measure", "The most consistent complaint in the corpus")}
  <div class="body">
    {figs([("36%", "of recent TrustRadius reviewers call reporting limited and unintuitive", "neg"),
           ("140", "G2 reviews tagged &lsquo;Missing Features&rsquo;"),
           ("27", "focused doc pages on the Global Control Group"),
           ("2am ET", "when your billing dashboard refreshes &mdash; daily, cached")], size="sm")}
    {cards([("What is genuinely there",
             "Holdouts and a Global Control Group for incrementality, campaign and Canvas analytics endpoints, KPI endpoints, and a Snowflake data share that avoids copying data at all.", "g"),
            ("What reviewers keep hitting",
             "&ldquo;The out-of-the-box reporting still feels too basic unless you export raw data through paid add-ons like Currents&rdquo; &mdash; and, separately, a wish for &ldquo;more robust native reporting on long-term retention cohorts&rdquo;.", "r")],
           cols=2)}
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
  {head("The AI &middot; five independent lenses", "Bought recently, and running on other people&rsquo;s models")}
  <div class="body">
    {split(
      '<div><div class="klabel colhead">LENS 1 &mdash; FOCUSED DOCUMENTATION PAGES</div>'
      + bars([("Email", 347), ("Canvas", 249), ("Segmentation", 242), ("Liquid", 123),
              ("Recommendations", 73), ("BrazeAI brand", 32), ("Decisioning Studio", 22, "medium"),
              ("Agents", 17, "medium"), ("Predictive Suite", 7, "weak")])
      + '</div>',
      '<div><div class="klabel colhead">LENSES 2&ndash;5</div>'
      + tiles([("", "0 of 135 API endpoints", "28 namespaces. None of them AI, prediction, agent or decisioning"),
               ("", "3 external model suppliers", "Anthropic, OpenAI and Google &mdash; named in their own sub-processor disclosure"),
               ("", "The engine was bought", "Decisioning Studio was OfferFit until June 2025. $303.2m"),
               ("", "Reviewers name copywriting", "Two G2 reviewers say the AI copy needs &ldquo;a careful human hand&rdquo;. None mentions decisioning")], cols=1)
      + '</div>',
      ratio="1.05fr 0.95fr")}
  </div>
</section>''',
"""This is the slide most likely to go wrong, so I am going to be careful.

**I am not going to tell you their AI is thin.** That sentence is unfalsifiable and the
evidence does not need it.

Here is what five independent lenses say instead.

**Documentation.** Predictive Suite has seven focused pages. Agents seventeen.
Decisioning Studio twenty-two. Canvas has two hundred and forty-nine.

**The API.** Of a hundred and thirty-five published endpoints across twenty-eight
namespaces, the number in an AI, prediction, agent or decisioning namespace is **zero**.

**The models.** Anthropic, OpenAI and Google — named in their own compelled disclosure.

**The engine.** Bought, June 2025, three hundred and three million dollars.

**And customers.** Reviewers talk about AI copywriting, and two of them independently say
it needs a human pass. Nobody in the sample mentions decisioning at all.

So the defensible sentence is: real, shipping, recently and largely acquired, running on
three suppliers' models, with no API of its own. Every clause sourced separately. Let the
audience draw the conclusion.""",
    "s", "The AI, honestly")
