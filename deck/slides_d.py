# -*- coding: utf-8 -*-
"""Part III — strategy. Slides 32-35 (divider + 3 content slides).

Three slides, not six. Seven years of audited operating expense is a real answer to a
question that could previously only be inferred, and the temptation to add four more
financial slides around it is exactly the equity-research trap docs/STRATEGY.md warns
about. The money chapter is held to roughly a fifth of the deck.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *                                   # noqa: F403,E402

# ── 32 DIVIDER ───────────────────────────────────────────────────────────────
add(f'''<section class="s div-s" data-g="s" data-t="Part III: Strategy">
  {divider("Part III", "Strategy",
           ["Where seven years of revenue actually went",
            "What is provisioned that has not been announced",
            "What would survive a competitor doing the same thing"],
           foot="Audited, except where marked")}
</section>''',
"""Part three. Three slides only, and that is deliberate.

The SEC data here is abundant and tidy and it will happily eat a whole deck. **You are
deciding about a product and a competitor, not about a share price**, so the money gets
one slide, the unannounced gets one, and the last one is the argument.""",
    "s", "Part III: Strategy")

# ── 33 WHERE THE MONEY GOES ──────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="Where the money goes">
  {head("Seven audited years &middot; where revenue goes", "Decelerating and getting more efficient at the same time")}
  <div class="body">
    {split(
      '<div><div class="klabel colhead">SALES &amp; MARKETING AS A SHARE OF REVENUE</div>'
      + bars([("FY2020", 59.5), ("FY2022", 53.4), ("FY2023", 56.7),
              ("FY2024", 52.4), ("FY2025", 47.6), ("FY2026", 44.3, "strong")], unit="%")
      + '</div>',
      '<div><div class="klabel colhead">REVENUE GROWTH OVER THE SAME YEARS</div>'
      + bars([("FY2021", 55.9), ("FY2022", 58.5), ("FY2023", 49.3),
              ("FY2024", 32.7), ("FY2025", 25.8), ("FY2026", 24.4, "medium")], unit="%")
      + '</div>')}
    <p>This killed the hypothesis it was built to test. The expectation was decelerating growth
    <em>propped up by</em> sales spend. <strong>The evidence says the opposite: S&amp;M has fallen more than
    twelve points as a share of revenue since FY2023, to its lowest in the series, while growth halved.</strong>
    Operating cash flow turned positive in FY2024 and has grown every year since &mdash; to $71.4m.</p>
  </div>
</section>''',
"""Seven audited years of where the money goes, and this slide killed the hypothesis I
wrote before I read anything.

I expected decelerating growth propped up by ever-more sales spend. That is the usual
pattern and it is the easy story.

**The evidence says the opposite.** Sales and marketing has fallen from fifty-seven per
cent of revenue to forty-four — the lowest in the series — while growth halved. They are
decelerating *and* getting more efficient at the same time.

And operating cash flow turned positive in FY2024 and has grown every year since, to
seventy-one million.

So if you are planning to compete with Braze on the assumption that they are burning
money to buy growth and will have to stop: **that assumption is wrong**, and the audited
numbers say so.

The counterweight, in fairness: share-based compensation has now exceeded the entire net
loss for two years running, and diluted shares are up fourteen per cent in three years.
The loss is real; it is mostly equity, and shareholders are carrying it.""",
    "s", "Where the money goes")

# ── 34 WHAT COMES NEXT ───────────────────────────────────────────────────────
_next_tiles = tiles([
    ("", "1 &middot; The compelled disclosure",
     "Their sub-processor list, revision 1 June 2026, names <strong>two</strong> hosting providers: "
     "Amazon Web Services and Google Cloud. <strong>Microsoft is not named anywhere in it.</strong>"),
    ("", "2 &middot; Their own documentation",
     "Braze publishes the IPs you must allowlist, per instance. Every address listed for "
     "<strong>US-08 is registered to Microsoft Corporation</strong>. Every other instance &mdash; "
     "US-10, AU-01, ID-01, JP-01, KR-01 &mdash; is Amazon. Checked against ARIN."),
    ("", "3 &middot; Certificate transparency",
     "50 hosts sit on region codes <span class='mono'>p-aze-us</span>, <span class='mono'>s-aze-us</span>, "
     "<span class='mono'>d-aze-us</span> &mdash; matching no AWS region identifier, where every other code "
     "does. They include <span class='mono'>sdk-us08</span> and <span class='mono'>subcenter-08</span>."),
    ], cols=3)

add(f'''<section class="s" data-g="s" data-t="What comes next">
  {head("Unannounced &middot; three sources, one answer", "One instance is not on the same cloud as the others")}
  <div class="body">
    {_next_tiles}
    <div class="ruleband">
      <div class="klabel">HOW TO SAY THIS &mdash; AND HOW NOT TO</div>
      <p><strong>State the three observations and stop.</strong> A hosting arrangement may sit outside a
      sub-processor listing for reasons not visible from outside. Saying they failed to disclose would be a
      legal conclusion this evidence does not support. <em>The question is for them, not a conclusion for us.</em></p>
    </div>
  </div>
</section>''',
"""This is the finding nobody else in your market will have, and it is also the one I am
most careful about.

Three sources that have nothing to do with each other.

**One.** Their sub-processor disclosure — legally compelled to be complete, revised in
June — names two hosting providers. Amazon and Google. Microsoft appears nowhere in it.

**Two.** Their own documentation publishes the IP addresses you must allowlist for each
instance. Every address for US-08 is registered to **Microsoft Corporation**. Every
address for every other instance is Amazon. I checked all of them against ARIN's registry
rather than recognising ranges by eye, and that lookup is saved in the repository.

**Three.** Certificate transparency shows fifty hosts on a region code that matches no
AWS identifier, and the hostnames on it include sdk-us08 and subcenter-08.

Now the discipline. **I am not telling you Braze failed to disclose something.** That is
a legal conclusion and this evidence does not support it. There may be a perfectly good
reason.

What I am telling you is that three unrelated sources say US-08 runs somewhere the
disclosure does not mention — and if you are in a procurement conversation against Braze,
that is a question worth someone asking.""",
    "s", "What comes next")

# ── 35 COMPETITIVE ADVANTAGES ────────────────────────────────────────────────
add(f'''<section class="s" data-g="s" data-t="What protects them">
  {head("Defensibility &middot; the so-what test", "Three things a competitor cannot simply copy")}
  <div class="body">
    {cards([("Contracted revenue, not pipeline",
             "<strong>$1,033.0m of remaining performance obligation</strong> &mdash; 1.40&times; current revenue, already signed. You cannot displace what is not up for renewal. This is the strongest of the three.", "g"),
            ("Ten years of streaming plumbing",
             "MongoDB, Snowflake, Kafka and Redis under fifteen regional clusters, with a decade of incident history to show it holds. Copyable in principle; expensive and slow in practice.", "g"),
            ("Marketer independence from engineering",
             "The thing reviewers actually praise: changing a journey without filing a ticket. That is a workflow habit, and habits are stickier than features.", "g")],
           cols=3)}
    <div class="ruleband">
      <div class="klabel">AND WHAT DOES NOT PROTECT THEM</div>
      {cards([("The AI",
               "Bought for $303.2m, running on Anthropic, OpenAI and Google models, with no API surface of its own. Anyone can buy the same models. This is a feature race, not a moat.", "r"),
              ("The channel roster",
               "Broad and well built &mdash; and matched by several of the five specialists buyers shortlist them against but they never name.", "a")],
             cols=2)}
    </div>
  </div>
</section>''',
"""What actually protects them, under the "so what would a competitor do about it" test.

**The strongest thing is the least exciting.** A billion dollars of contracted,
unrecognised revenue at one point four times current revenue. You cannot displace an
account that is not up for renewal. That is a real moat and it is measured, not asserted.

**Second, the plumbing.** A decade of streaming infrastructure across fifteen clusters,
with a public incident record showing it holds. Copyable in principle. Slow and expensive
in practice.

**Third, and most underrated: the habit.** Marketers who can change a journey without
filing an engineering ticket do not want to go back. That is stickier than any feature.

And what does *not* protect them. **The AI does not.** It was bought, it runs on three
suppliers' models that anyone can buy, and it has no API surface. That is a feature race.

If I were briefing a sales team, I would say: do not attack the AI, attack the renewal
calendar and the reporting.""",
    "s", "What protects them")
