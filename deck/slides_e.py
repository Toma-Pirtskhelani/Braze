# -*- coding: utf-8 -*-
"""Part IV — open questions. Slides 36-42 (divider + 6 content slides).

Slide 37 is the deep dive, and DECK-SPEC says to pick it after the research from
whatever turned out to be both contested and answerable. It went to the ingestion
freshness question: it is the thing a prospect will actually be told is fine, the
evidence settles it in Braze's own words, and it decides a real architecture choice.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *                                   # noqa: F403,E402

# ── 36 DIVIDER ───────────────────────────────────────────────────────────────
add(f'''<section class="s div-s" data-g="s" data-t="Part IV: Open questions">
  {divider("Part IV", "Open questions",
           ["One hard question, answered properly",
            "A decade of reliability, measured rather than claimed",
            "The hypotheses that died in Braze&rsquo;s favour",
            "What public sources could not answer, and what would close it",
            "What to remember"],
           foot="Where the evidence runs out, this says so")}
</section>''',
"""Part four is the part most competitor decks do not have, and it is the reason to trust
the other three.

One hard question answered properly. A decade of reliability, measured rather than
claimed. The three hypotheses that died in Braze's favour — because we wrote ten of them
down before reading anything, and four came back wrong. Then an honest account of where
the public record ran out, and a prioritised list of what to do about it.

That last part is not a disclaimer and I would not present it apologetically. **A gap you
have written down is evidence. A gap you have not written down is a mistake** — and the
difference is that the first one tells the next person exactly where to dig.

One of those gaps closed while this deck was being built, from the source the entry itself
had named. That is what a well-written backlog does.""",
    "s", "Part IV: Open questions")

# ── 37 DEEP DIVE ─────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Deep dive: how real-time is it">
  {head("Deep dive", "&ldquo;Is it real-time?&rdquo; &mdash; answered properly")}
  <div class="body">
    {flow([("ASK", "Which path?", "The answer differs by a factor of hundreds"),
           ("SDK / API", "Near-real-time", "Their words, with &lsquo;async processing&rsquo; attached"),
           ("WAREHOUSE", "15 minutes, floor", "&ldquo;Not real-time&rdquo;, three times over"),
           ("FASTER?", "Not self-serve", "&ldquo;Contact your customer success manager&rdquo;"),
           ("EXPORT", "5 minutes", "And Currents is a paid add-on")],
          mark={2: "s", 3: "w", 4: "w", 5: "m"})}
    {cards([("Why this is the question that matters",
             "Most enterprise buyers&rsquo; customer data lives in a warehouse. For them the honest answer is fifteen minutes, and it is not a setting they can change.", "g"),
            ("Why it is not a gotcha",
             "Braze publishes this themselves, in a comparison table, and the SDK path genuinely is near-real-time. The word covers two architectures &mdash; it is not a false claim.", "g"),
            ("What to actually ask them",
             "&ldquo;Which ingestion path will <em>my</em> data take, and what is the latency on that path?&rdquo; The answer is in their documentation before the meeting.", "a")],
           cols=3)}
  </div>
</section>''',
"""The deep dive. I picked this after the research, from what turned out to be both
contested and answerable.

Every vendor in this category says real-time. The question is what it means, and for
Braze the answer differs by a factor of hundreds depending on which path your data takes.

**SDK and API: near-real-time.** True, and their own qualifier — async processing — is
honest.

**Warehouse: fifteen minutes, and that is a floor.** Labelled "not real-time" three
separate times in their own comparison table. And going faster is not a setting. It is a
conversation with your customer success manager.

Then note the last box, because it closes the loop in a way people miss: even getting the
data back **out** runs on a five-minute cadence, through Currents, which is a paid add-on.
So the round trip — warehouse in, decision made, event exported to your systems — is
bounded at the slow end by a scheduled job and at the fast end by a line item.

Why this is the question that matters, rather than one of a dozen. Most enterprise buyers
in this category keep their customer data in a warehouse. That is where the CRM extract
lands, where the transaction history lives, where the analytics team works. For those
buyers — and they are the ones we compete for — the honest answer to "how fresh is my
data in Braze" is fifteen minutes, and it is not a setting they can change. The buyer who
gets the near-real-time answer is the buyer already sending events from their app through
Braze's SDK, which is a different architecture and often a different company.

Now — this is not a gotcha, and I would not present it as one in front of them. **Braze
publishes this table themselves.** They graded their own ingestion paths, in their own
words, and they did not have to. That is the point of the whole method rather than an
aside: **a vendor's documentation is more honest than anyone's marketing, including their
own**, because it is written by people whose job is to stop support tickets rather than to
win deals.

Which is also why this survives contact with them. If I stand up and say "Braze is not
real-time", their solutions engineer opens the product, shows an event landing in seconds
from the SDK, and I have lost the room and every other finding in the deck with it. If I
say "three of your four documented ingestion paths are labelled not real-time and the
warehouse floor is fifteen minutes", there is nothing to demonstrate against. It is their
sentence.

So the thing to put in a prospect's hand is the third card, and it is one sentence. Not
"is it real-time" — they will say yes and be right. Ask **which path my data will take,
and what the latency is on that path.** If the answer is the warehouse, the follow-up is
what it costs to move to the API path and who does that work. Those two questions do more
for us than any claim we could make.""",
    "s", "Deep dive: how real-time is it")

# ── 38 RELIABILITY ───────────────────────────────────────────────────────────
# Carries BOTH halves of the operational record. The favourable half - a 97.3% close
# rate on 845 unsolicited issues, and every SDK current - was written into the evidence
# record and reached no slide in the first draft. An analysis that only found problems
# was not an analysis, so it is on the slide now.
add(f'''<section class="s" data-g="s" data-t="Reliability, measured">
  {head("The operational record &middot; a decade of it, public", "451 incidents, and the rate is falling")}
  <div class="body">
    {bars([("2019", 49), ("2020", 57), ("2021", 48), ("2022", 39),
           ("2023", 60, "weak"), ("2024", 43), ("2025", 27, "strong"),
           ("2026 to Aug", 35, "medium")])}
    {figs([("79 min", "median incident duration"),
           ("29.6%", "of non-maintenance incidents were major or critical"),
           ("63 v 27", "Dashboard incidents vs Outbound Messaging"),
           ("97.3%", "of 845 unsolicited public issues closed &mdash; median 11 days"),
           ("9 of 9", "SDK repos shipped within 13 days of capture")], size="sm")}
    <p><strong>The caveat belongs on the slide, not only in the notes:</strong> 2026 stands at 35 through August,
    roughly <strong>double the 2025 monthly rate</strong>. One year is not a trend, and none is claimed.
    And <strong>never compare this to a vendor who publishes nothing.</strong></p>
  </div>
</section>''',
"""A decade of incidents, because they publish a status page and most vendors do not.

The rate peaked in 2023 at sixty and fell to twenty-seven in 2025 — **the quietest full
year on record, over a period when revenue grew seven and a half times.** That kills the
hypothesis I wrote that incidents would rise with scale.

With the caveat attached, and it is on the slide rather than only in my notes: 2026
stands at thirty-five through August, roughly double the 2025 monthly rate. One year
does not make a trend.

**The Dashboard appears in sixty-three incidents; Outbound Messaging in twenty-seven.**
The control plane your marketers work in fails more than twice as often as the sending
path. Messages get out; the console is where you feel the outage.

Now the two numbers on the right, because an analysis that only found problems was not
an analysis. **Ninety-seven per cent of eight hundred and forty-five unsolicited public
issues are closed, median eleven days.** And every one of the nine SDK repositories that
publishes releases shipped within thirteen days of capture — the platform whose repo is
archived, Unreal, has had its documentation removed too. **The maintenance record matches
the marketing**, which is not something I could say about every vendor.

And the rule at the bottom: **do not compare this against a competitor who publishes
nothing.** Braze looks worse than a silent vendor purely by being transparent.""",
    "s", "Reliability, measured")

# ── 39 WHERE THE EVIDENCE WENT THEIR WAY ─────────────────────────────────────
# Ten hypotheses were written before the corpus was read, precisely so they could be
# graded honestly afterwards. Three died in Braze's favour and, in the first draft, that
# reached the record and never reached the deck - which is the exact bias the hypothesis
# method exists to prevent. A deck that only finds problems invites an audience to
# discount all of it, so the favourable results get a slide of their own rather than a
# sentence in someone's notes.
_fav = cards([
    ("H1 &middot; &ldquo;Growth is decelerating while sales spend holds&rdquo;",
     "<strong>Killed.</strong> Growth did decelerate &mdash; and sales and marketing fell "
     "<strong>from 56.7% of revenue to 44.3%</strong> over the same period, its lowest in the seven-year "
     "series. Braze is decelerating <em>and</em> getting more efficient. Operating cash flow turned "
     "positive in FY2024 and has grown every year since.", "g"),
    ("H4 &middot; &ldquo;Some supported platforms are effectively unmaintained&rdquo;",
     "<strong>Killed.</strong> <strong>All nine SDK repositories</strong> that publish releases had shipped "
     "within 13 days of capture. The one archived repo, Unreal, has had its documentation removed too &mdash; "
     "so the marketing and the maintenance record agree. One soft spot: <span class='mono'>braze-roku-sdk</span>, "
     "181 days idle with 38 Roku doc pages still live.", "g"),
    ("H9 &middot; &ldquo;Incident rate has risen with scale&rdquo;",
     "<strong>Killed.</strong> Incidents peaked at 60 in 2023 and fell to <strong>27 in 2025</strong>, the "
     "quietest full year on the status page &mdash; over a period when revenue grew 7.7&times;. "
     "With its caveat attached: 2026 runs at roughly double the 2025 monthly rate through August, and one "
     "year is not a trend.", "g")], cols=3)

add(f'''<section class="s" data-g="s" data-t="Where the evidence went their way">
  {head("The hypotheses that died &middot; in Braze&rsquo;s favour", "Three things we expected to find, and did not")}
  <div class="body">
    {_fav}
    <div class="ruleband">
      <div class="klabel">WHY THIS SLIDE EXISTS</div>
      <p>Ten hypotheses were written <strong>before any source was read</strong>, so they could be graded
      honestly afterwards. Four were killed, three of them favourably; one could not be tested at all.
      <strong>A set of hypotheses that all confirmed would have meant they were written to confirm.</strong>
      Everything critical in this deck should be read against the fact that these three were looked for and
      were not there.</p>
    </div>
  </div>
</section>''',
"""I want this slide in the deck more than almost any other, and it is the one that would
have been cut first.

Before we read a single source we wrote down ten hypotheses — ten things we expected to
find — so that afterwards they could be graded rather than quietly dropped. **Four of
them were killed. Three of those four were killed in Braze's favour.**

**One.** We expected the familiar late-stage pattern: growth decelerating while sales
spend holds, a company buying its last few points of growth. The opposite is true. Sales
and marketing fell more than twelve points as a share of revenue over three years, to the
lowest in the seven-year series, while growth decelerated. They are decelerating and
getting more efficient at the same time. That is a harder company to compete with, not an
easier one.

**Two.** We expected to find abandoned SDKs — the platform nobody maintains that is still
on the marketing page. Every one of the nine repositories that publishes releases had
shipped within thirteen days of when we looked. And the one platform whose repo is
archived has had its documentation pulled too, so they are not selling something they
stopped supporting. The single soft spot is Roku, idle six months with the docs still up,
and that is a small thing.

**Three.** We expected incidents to have risen with scale, because they usually do. They
peaked in 2023 and fell to the quietest full year on the status page in 2025, while
revenue grew seven and a half times. I have put the 2026 caveat on the slide rather than
in my pocket, because it runs at about double the 2025 rate — but one year is not a
trend, and I am not going to present it as one.

Now the reason this matters more than the three findings themselves. **If every
hypothesis we wrote had confirmed, that would tell you we wrote them to confirm.** The
value of everything critical in this deck — the real-time finding, the AI provenance, the
US-08 question — rests on our being willing to say when the evidence went the other way.

So if someone in the room wants to discount this analysis as a hit piece, this is the
slide to turn back to. We looked for three specific weaknesses. They were not there, and
we said so.""",
    "s", "Where the evidence went their way")

# ── 40 WHAT WE COULD NOT ANSWER ──────────────────────────────────────────────
add(f'''<section class="s" data-g="m" data-t="What we could not answer">
  {head("The honest residue", "Four gaps, and what would close them")}
  <div class="body">
    {tiles([("", "Does satisfaction fall with customer size?",
             "The one hypothesis that could not be tested at all. <strong>All three review sites paywall exactly that breakdown</strong>, and only 7 of 860 coded records carry a segment. <em>Closed by:</em> paid panel access, or an investor-day disclosure"),
            ("", "What else is in the certificate estate?",
             "The host list is <strong>partial</strong> &mdash; 833 hosts through a rate-limited fallback after crt.sh returned errors all day. Everything found stands; <strong>nothing is claimed about what is absent</strong>. <em>Closed by:</em> an API token"),
            ("", "Can the customer roster be checked independently?",
             "The only roster outside the 10-K is <strong>178 self-published customer stories</strong>, which is a marketing selection and not a sample. Independent detection was <strong>not attempted</strong>, and that is recorded as a gap rather than a zero. <em>Closed by:</em> tag crawls, CT records naming customer subdomains, or job ads naming Braze in the stack"),
            ("", "Actual pricing, and why the export limit was cut",
             "No vendor publishes a rate card, and the 10&times; cut to the profile-lookup limit on 22 August 2024 is documented without explanation. <em>Closed by:</em> a procurement award, a customer contract, a changelog entry")],
           cols=2)}
  </div>
</section>''',
"""Four things I could not answer, stated plainly.

**The first is the one that annoys me most.** I went in expecting enterprise satisfaction
to be lower than small-business satisfaction, because it usually is. All three review
sites paywall exactly that breakdown. Seven of eight hundred and sixty coded records
carry a customer size. **So the hypothesis is unresolved, not answered** — and I would
rather tell you that than dress up a proxy as an answer.

**Second.** The certificate list is partial. crt.sh was down all day and the fallback
rate-limited. Everything I found is real; I am claiming nothing about what is missing,
because I did not look exhaustively.

**Third.** I cannot check their customer roster against anything independent. The only
list outside the audited count is a hundred and seventy-eight stories they chose to
publish, which is marketing. Detecting Braze in the wild — tag crawls, certificate
records, job ads naming it in the stack — was not attempted in this run, and I am
recording that as a gap rather than pretending the hundred and seventy-eight is a sample.

**Fourth.** Pricing — as expected — and one specific thing: they cut the profile-lookup
rate limit tenfold for new customers on a dated boundary and never say why.

One more thing about this slide, and it is the point of keeping it. **There were five
gaps here until quite late.** The fifth was the split of open roles by function: the
careers board's filter would not drive under automation, so it went down as
uncapturable. Then the same board turned out to be published as JSON with the grouping
already done, and the answer is now on slide fifteen. The lesson generalises — **when a
page will not yield, look for the API behind it before you write down a gap** — and it
is in the corrections log rather than quietly patched.

All of these are written down with what would close them. That is the difference between
a gap and a mistake.""",
    "m", "What we could not answer")

# ── 40 QUESTIONS BACKLOG ─────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="What to research next">
  {head("Backlog &middot; prioritised", "Four questions worth the next week")}
  <div class="body">
    {cards([("1 &middot; Ask about US-08",
             "The highest-value single answer in the backlog. It decides whether slide 34 is an infrastructure observation or a procurement question. <strong>Route:</strong> the DPA schedule a customer receives, or ask them directly.", "g"),
            ("2 &middot; Buy one panel&rsquo;s segment data",
             "It closes the only hypothesis that went unresolved, and satisfaction-by-size is the question your sales team will ask first. <strong>Route:</strong> paid G2 or Gartner access.", "g")],
           cols=2)}
    {cards([("3 &middot; Detect the customer base independently",
             "The only roster outside the audited count is 178 stories Braze chose to publish. Tag crawls, certificate records and job ads naming the stack would give a roster nobody curated. <strong>Route:</strong> a crawl, and it is not cheap.", "g"),
            ("4 &middot; Re-run this in ninety days",
             "Every number here is reproducible by script. The two to watch: whether the gross-margin decline continues, and whether the 2026 incident rate settles or climbs.", "g")],
           cols=2)}
    <p>The full backlog &mdash; eight open questions, each with what would close it &mdash; is in
    <span class="mono">docs/QUESTIONS.md</span>, and every finding in this deck resolves to a row in
    <span class="mono">docs/FACTS.md</span> with a source path and a capture date.</p>
  </div>
</section>''',
"""If you gave me another week, this is the order.

**First, ask about US-08.** It is the highest-value single answer available and it decides
whether slide thirty-four is a curiosity or something procurement should raise. A
customer can just look at their own DPA schedule.

**Second, buy one panel's segment data.** It closes the hypothesis I could not test, and
satisfaction-by-customer-size is the first thing your sales team will ask me.

**Third, detect their customer base independently.** The only customer list we have
outside the audited count is a hundred and seventy-eight stories they chose to publish.
Tag crawls, certificate records and job ads naming Braze in the stack would give us a
roster nobody curated. That one is not cheap, which is why it is third.

The careers API was on this list until this morning, and it is not any more — we pulled
it, and where their headcount is going is now on slide fifteen. Two hundred and
ninety-six roles, seventy-two per cent go-to-market.

**Fourth, and this is the real point: re-run all of it in ninety days.** Every number in
this deck was produced by a script from a public source. Not one of them is a judgement
call about where to look. The two I would watch are whether the margin decline continues,
and whether the 2026 incident rate settles.""",
    "s", "What to research next")

# ── 41 CLOSE ─────────────────────────────────────────────────────────────────
# The close slide had no headline at all - the big() line was doing the job, which reads
# fine on screen and leaves the slide unlabelled in the grid overview and in any structural
# read of the deck. A four-word Kind A label above it sets the payoff up rather than
# competing with it.
add(f'''<section class="s" data-g="s" data-t="Close">
  {head("Close", "One thing to remember")}
  <div class="body" style="display:flex;flex-direction:column;justify-content:center;height:100%">
    {big("Their documentation is more honest than anyone&rsquo;s marketing &mdash; including their own.",
         "Every hard limit in this deck came from a page Braze wrote for its own engineers: three of four ingestion paths labelled &ldquo;not real-time&rdquo;, a fifteen-minute warehouse floor, an export limit cut tenfold on a dated boundary, and a merge that returns success when it has quietly declined. None of it is hidden. All of it is unread.")}
    {figs([("1,352", "documentation pages read"),
           ("451", "incidents"),
           ("845", "public issues"),
           ("17", "sub-processors"),
           ("7", "audited years")], size="sm")}
  </div>
</section>''',
"""One thing to remember.

**Their documentation is more honest than anyone's marketing, including their own.**

Every uncomfortable fact in this deck came from a page Braze wrote for its own
engineers. Three of four ingestion paths labelled not real-time. A fifteen-minute
warehouse floor. An export limit cut tenfold on a dated boundary, with existing customers
grandfathered. A merge that returns success when it has silently declined.

None of that is hidden. All of it is unread.

And that is the transferable lesson, whichever vendor you point this at next: **the
competitive advantage was not access. It was reading what they already published, and
counting it.**""",
    "s", "Close")
