# -*- coding: utf-8 -*-
"""Part IV — open questions. Slides 36-41 (divider + 5 content slides).

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
            "What public sources could not answer, and what would close it",
            "What to remember"],
           foot="Where the evidence runs out, this says so")}
</section>''',
"""Part four. One hard question answered properly, the reliability record, and then an
honest account of where public sources ran out.

That last part is not a disclaimer. **A gap you have written down is evidence. A gap you
have not written down is a mistake.**""",
    "s", "Part IV: Open questions")

# ── 37 DEEP DIVE ─────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Deep dive: how real-time is it">
  {head("Deep dive", "&ldquo;Is it really real-time?&rdquo; &mdash; answered properly")}
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

Then note the last box: even the export runs on a five-minute cadence, through a paid
add-on.

Now — this is not a gotcha and I would not present it as one in front of them. Braze
publishes this table themselves. That is the point of the whole method: **their
documentation is more honest than anyone's marketing, including their own.**

The question to put in a prospect's hand is the third card. Not "is it real-time" — they
will say yes and be right. Ask **which path my data takes, and what the latency is on
that path.**""",
    "s", "Deep dive: how real-time is it")

# ── 38 RELIABILITY ───────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Reliability, measured">
  {head("Reliability &middot; a decade on the public record", "451 incidents since 2016, and the rate is falling")}
  <div class="body">
    {bars([("2019", 49), ("2020", 57), ("2021", 48), ("2022", 39),
           ("2023", 60, "weak"), ("2024", 43), ("2025", 27, "strong"),
           ("2026 to Aug", 35, "medium")])}
    {figs([("79 min", "median incident duration"),
           ("311 min", "p90 &mdash; the long tail is long"),
           ("29.6%", "of non-maintenance incidents were major or critical"),
           ("63 v 27", "Dashboard incidents vs Outbound Messaging")], size="sm", focus=3)}
    <p><strong>Never compare this to a vendor who publishes nothing.</strong> A decade of visible incidents is
    a disclosure practice, not a defect count &mdash; and silence has not earned anyone a better record.</p>
  </div>
</section>''',
"""A decade of incidents, because they publish a status page and most vendors do not.

Four hundred and fifty-one incidents since 2016. The rate peaked in 2023 at sixty and
fell to twenty-seven in 2025 — **the quietest full year on record, over a period when
revenue grew seven and a half times.** That kills the hypothesis I wrote that incidents
would rise with scale.

With the caveat attached: 2026 stands at thirty-five through August, running at roughly
double the 2025 monthly rate. One year does not make a trend, and I am not calling it
one.

The last figure is the shape I would actually use. **The Dashboard appears in
sixty-three incidents; Outbound Messaging in twenty-seven.** The control plane your
marketers work in fails more than twice as often as the sending path. Messages get out;
the console is where you feel the outage.

And the rule at the bottom, which matters most: **do not compare this against a
competitor who publishes nothing.** Braze looks worse than a silent vendor purely by
being transparent, and rewarding that would be dishonest analysis.""",
    "s", "Reliability, measured")

# ── 39 WHAT WE COULD NOT ANSWER ──────────────────────────────────────────────
add(f'''<section class="s" data-g="m" data-t="What we could not answer">
  {head("The honest residue", "Four gaps, and what would close each one")}
  <div class="body">
    {tiles([("", "Does satisfaction fall with customer size?",
             "The one hypothesis that could not be tested at all. <strong>All three review sites paywall exactly that breakdown</strong>, and only 7 of 860 coded records carry a segment. <em>Closed by:</em> paid panel access, or an investor-day disclosure"),
            ("", "What else is in the certificate estate?",
             "The host list is <strong>partial</strong> &mdash; 833 hosts through a rate-limited fallback after crt.sh returned errors all day. Everything found stands; <strong>nothing is claimed about what is absent</strong>. <em>Closed by:</em> an API token"),
            ("", "The real split of open roles by function",
             "The careers board&rsquo;s filter would not drive reliably, so only the 15-function taxonomy and a front-of-list sample were captured. <strong>No percentage is offered.</strong> <em>Closed by:</em> the Greenhouse board API"),
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

**Third.** No function-level headcount split, so no percentage from me.

**Fourth.** Pricing — as expected — and one specific thing: they cut the profile-lookup
rate limit tenfold for new customers on a dated boundary and never say why.

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
    {cards([("3 &middot; Pull the Greenhouse board API",
             "Cheap, and turns &lsquo;15 functions&rsquo; into where headcount is actually going &mdash; the strategy stated in hiring rather than in a keynote.", "g"),
            ("4 &middot; Re-run this in ninety days",
             "Every number here is reproducible by script. The two to watch: whether the gross-margin decline continues, and whether the 2026 incident rate settles or climbs.", "g")],
           cols=2)}
    <p>The full backlog &mdash; fourteen open questions, each with what would close it &mdash; is in
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

**Third, the careers API** — cheap, and it turns fifteen function names into where
headcount is actually going. Hiring is strategy stated out loud.

**Fourth, and this is the real point: re-run all of it in ninety days.** Every number in
this deck was produced by a script from a public source. Not one of them is a judgement
call about where to look. The two I would watch are whether the margin decline continues,
and whether the 2026 incident rate settles.""",
    "s", "What to research next")

# ── 41 CLOSE ─────────────────────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Close">
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
