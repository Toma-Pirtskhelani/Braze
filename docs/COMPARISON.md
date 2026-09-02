# Insider One vs Braze — the two decks, compared as presentations

Written 2026-09-02 against Braze commit `0eb0205` (43 slides) and the Insider One deck
(41 slides). Judged on what the operator asked: **as a spoken presentation** — titles,
visuals, clarity, insight, impact, business value.

---

## The verdict, up front

**Insider One is the better presentation. Braze is the better research.** They are not the
same thing, and the gap between them has three measurable causes, all fixable without
touching a single fact.

The short version: **the Braze deck keeps the analyst in the frame.** It talks about its own
evidence roughly three times as often as it talks about what that evidence means for the
person watching. Insider One is close to balanced. That single habit explains most of why
one deck feels like a case being made and the other feels like a file being read out.

| | Insider One | Braze |
|---|---|---|
| **Titles** | ● ● ● ● ○ | ● ● ○ ○ ○ |
| **Visuals** | ● ● ● ○ ○ | ● ● ● ○ ○ |
| **Clarity** | ● ● ● ● ○ | ● ● ● ○ ○ |
| **Insight** | ● ● ● ○ ○ | ● ● ● ● ● |
| **Impact** | ● ● ● ● ● | ● ● ○ ○ ○ |
| **Business value** | ● ● ● ● ○ | ● ● ○ ○ ○ |
| **Evidence quality** | ● ● ● ○ ○ | ● ● ● ● ● |

---

## 1 · Cause one: every Braze slide shouts

`CRITIQUE-3.md` gave two kinds of headline — the **label** (a plain noun phrase, for
orientation) and the **claim** (a sentence that states a finding). It did not say what the
*proportion* should be. That omission is the single biggest reason this deck underperforms.

| | Insider One | Braze |
|---|---|---|
| Label headlines | **29 (70%)** | 17 (39%) |
| Claim headlines | **12 (29%)** | 25 (58%) |
| Longest unbroken run of claims | 6 | **8** |

**The ratio is inverted.** Insider One is a deck of labels with twelve moments where the
title becomes a sentence — and because it happens rarely, the audience learns the rhythm:
*when the title turns into a claim, something is being argued.* Braze makes a claim on
nearly six slides in ten, so none of them registers as a moment.

Look at what this does to Part II, the seven-stage product walk, in each deck:

| Stage | Insider One | Braze |
|---|---|---|
| 1 · Data | *Getting the data in* | *Their words: three of four are not real-time* |
| 2 · Identity | *Identity resolution* | *A merge can fail and still return success* |
| 3 · Decisioning | *What to send, and when* | *Two engines, two databases, one bought* |
| 4 · Building | *Where the campaign is assembled* | *Canvas is the strongest thing in the platform* |
| 5 · Content | *It designs for you. It will not let you design.* | *Liquid does the work, and draws the complaints* |
| 6 · Delivery | *Somebody else presses send* | *Only two channels have a named middleman* |
| 7 · Interaction | *Where they are genuinely ahead* | *The response comes back, billed differently* |

Insider One walks four plain stages and then lands three punches. **Braze lands seven
punches, which is the same as landing none.** By stage four the audience has stopped
hearing the title as a claim, so *"Canvas is the strongest thing in the platform"* — a
genuinely generous, credible, surprising thing to say about a competitor — arrives as more
of the same.

**The fix:** return stages 1–4 to labels. *Getting the data in. Resolving one person.
Deciding what to send. Building the journey.* Keep claims for stages 5, 6 and 7 and for the
findings elsewhere. Target roughly **two labels for every claim across the deck.**

---

## 2 · Cause two: the deck talks about its evidence instead of its meaning

This is the important one.

Counting words that point at **the vendor's business** (means, matters, risk, depends,
advantage, competitor, exposed, lock-in, negotiate…) against words that point at **the
analysis itself** (disclosure, documented, corpus, source, captured, graded, evidence,
traceable, recorded…):

| | so-what : method | so-what per 1k words | method per 1k words |
|---|---|---|---|
| **Insider One**, on slide | 0.77 | 3.9 | 5.0 |
| **Insider One**, spoken | **1.00** | 4.6 | 4.6 |
| **Braze**, on slide | **0.33** | 2.4 | **7.3** |
| **Braze**, spoken | 0.47 | 3.6 | **7.7** |

**Braze uses methodological language 46% more often than Insider One and business language
38% less.** Spoken, Insider One is exactly balanced — one "what this means" for every "here
is how we know". Braze runs two-to-one the other way.

The clearest illustration is the pair of slides about who physically sends the messages.
Same stage, same evidence class, same sub-processor disclosure underneath.

> **Insider One — "Somebody else presses send"**
> A table: channel → who delivers it → number of suppliers → throughput. Then:
> **"THE CONCENTRATION NOBODY MENTIONS — their largest channel sits on one supplier, and
> that supplier, Twilio, also owns Segment and sells a competing product."**

> **Braze — "Only two channels have a named middleman"**
> Lists the channels with a named delivery sub-processor and the channels without. Then:
> **"Say what the disclosure names, not what exists."**

Braze's slide is more careful and *less useful*. It closes on an instruction to the analyst
about epistemic hygiene. Insider One's closes on a strategic dependency the audience can act
on: your competitor's biggest channel runs through a company that competes with them. **One
slide tells you about a document. The other tells you about a vulnerability.**

The same pattern closes each deck. Insider One's final substantive slide answers a question
from the room — *"how hard is it really to become a WhatsApp BSP?"* — walks Meta's three
tiers and lands on **"The barrier is not code. It is a line of credit."** That is a
conclusion someone can build a plan around. Braze closes on **"Their documentation is more
honest than anyone's marketing"** — true, well-earned, and a statement about *how the
analysis went*, not about the company.

**The fix:** every slide in Part II and Part III needs a final line that answers *"so what
does that mean for us?"* The material is already in the record. On slide 26, the honest
so-what is that Braze's disclosure is thinner than its competitor's — and a buyer with a
data-residency requirement cannot tell from it who touches their messages. That is a finding
the audience can use. Say it.

---

## 3 · Cause three: the slides are fuller and the notes are thinner

| | Insider One | Braze |
|---|---|---|
| Body words per slide, mean | **107** | 123 |
| Body words per slide, max | **187** | 261 |
| Spoken words per slide, median | **209** | 169 |
| Slides with under 130 spoken words | 9 | 8 |

The means for spoken words are almost identical (235 vs 233) — but the **medians** are not,
and that is the tell. Braze's notes are bimodal: eleven slides carry more than 300 words and
the rest carry very few. Insider One's are evenly substantial.

The consequence in a room: on a Braze slide the audience is **reading more and listening
less**. Denser slides plus shorter notes means the screen is doing the presenter's job, and
the presenter is left describing what people can already see. Insider One's lighter slides
force the audience to look up.

**The fix:** cap on-slide body at ~120 words. Anything cut goes to the notes, where it is
spoken instead of read.

---

## 4 · Slide by slide, on the pairs that matter

**Channels.** Insider One: *"Nine channels they name. Nine more they don't."* — perfect
symmetry, and the body lists all nine named channels with one-word descriptors so the
audience sees the breadth and the hidden breadth at once. The takeaway is competitive: *they
are broader than they advertise, so do not underestimate the surface.* Braze: *"Thirteen
documented. Ten marketed."* — a good headline, but the body is an audit of which channels
appear in which index. That is a finding about their **content operations**, not their
product. A buyer does not care that KakaoTalk is missing from a documentation index.
**Insider One wins on relevance.**

**The AI.** Braze marshals five independent lenses — focused doc pages, API namespaces,
external model suppliers, acquisition date, review vocabulary. It is the more rigorous of
the two by a distance. But Insider One tells it as an **arc with dates**: Delphi, years old
and real; Sirius, 2023; Agent One, December 2025, the layer they renamed the company around.
*"Old machine learning, real. New agents, thin."* **Braze wins on evidence, Insider One wins
on transmission** — and in a room, transmission is the job.

**Acquisitions.** Braze is straightforwardly better. It has audited purchase prices, a
purchase-price allocation read correctly, and the North Star Y earn-out that paid **$0** —
a genuinely excellent finding with no Insider One equivalent, because that vendor never
published a price. **Braze wins clearly.**

**Money.** No contest. Seven years of audited revenue, gross margin, cash flow and the
material weakness in internal controls, against one small subsidiary's accounts and a page
of caveats. **Braze wins by a mile**, and this is the part of the deck where its structural
advantage as a listed company actually shows.

**The opening.** Insider One's title slide states a thesis: *"Built in Istanbul, owned out
of Singapore, aiming at America"* — geography, ownership and strategy in nine words, and the
audience knows what the deck argues before slide 2. Braze's says *"A customer engagement
platform — and a public company, which changes what can be known."* The second half is about
**the analysis**, not the company. **Insider One wins**, and it is the same cause as §2.

---

## 5 · Where Braze is plainly better

Said properly, because the rest of this document is critical.

**The evidence is stronger and it is not close.** 219 canonical facts against 101. Audited
quarterly financials across seven years. Five proxy statements. A decade of incident
history. Certificate transparency. 1,352 documentation pages measured with a stated,
re-runnable pattern set.

**It states what it expected and got wrong.** Ten hypotheses written before the corpus was
read, all ten resolved afterwards, four killed — three of them *in Braze's favour*. Insider
One has no equivalent, and no competitive deck I have seen does this. **Slide 40 —
"Three things we expected to find, and did not" — is the best slide in either deck**, and it
is the one an intelligent sceptic in the room will trust the whole deck because of.

**It is more careful.** Every disputed number carries a ruling. The material weakness is
reported with both halves — the weakness *and* that nothing was restated and the auditor
attested. That is the behaviour of an analyst who expects to be challenged.

**Its favourable findings are real.** *"Canvas is the strongest thing in the platform."*
*"451 incidents, and the rate is falling."* Insider One is more uniformly critical, which
makes it more fun and slightly less trustworthy.

---

## 6 · What to change, in order

Nothing here needs a source reopened.

| # | Change | Effect |
|---|---|---|
| 1 | **Return stages 1–4 to label headlines.** Target 2 labels per claim deck-wide | Restores the rhythm; the remaining claims land |
| 2 | **Give every Part II and III slide a closing so-what line** aimed at the audience, not the analyst | Fixes the 0.33 ratio — the single biggest gap |
| 3 | **Rewrite the title-slide lede as a thesis about Braze**, not about the analysis | The audience learns the argument on slide 1 |
| 4 | **Rewrite the close.** End on what Braze's position means for whoever is watching, not on how honest their documentation is | Presentations are judged on their last line |
| 5 | **Cap on-slide body at ~120 words**; move the overflow into the notes | Audience looks up instead of reading |
| 6 | **Rework the channels slide** around what the channel set means competitively, not around index drift | Converts an operations finding into a business one |
| 7 | Move slide 40 — the killed hypotheses — **earlier, into Part I** | It is the credibility slide; it is currently at 40 of 43 |

---

## 7 · The one-sentence answer

**Insider One is the better presentation because it never forgets there is a room in front
of it; Braze is the better analysis because it never forgets it might be wrong.** The second
is harder to build and easier to fix — and everything in section 6 is presentation craft on
top of a body of work that is already stronger than the deck it is being compared to.
