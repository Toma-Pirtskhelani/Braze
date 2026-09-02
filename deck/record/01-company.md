# The company

> Braze is a fifteen-year-old New York software company that has been public since November 2021 and, since January 2026, is no longer controlled by its founders through super-voting stock — though the staggered board that is the other structural defence was kept. Two of its three cofounders still run it, while three of six executive officers turned over inside a year. The most useful single thing here is a ratio: revenue has grown three times faster than headcount since FY2022, and the compensation plan shows that this was deliberate.

{{slides: 4, 5, 7}}

## 1.1 · The entity, and why the fiscal calendar matters

| Fact | Value | Grade | Source |
|---|---|---|---|
| SEC registrant | Braze, Inc. | [[audited]] | `data/filings.csv` |
| CIK / ticker | 0001676238 / BRZE (Nasdaq) | [[audited]] | `data/filings.csv` |
| SIC classification | 7372 Services-Prepackaged Software | [[audited]] | `data/filings.csv` |
| Fiscal year end | 31 January | [[audited]] | `data/filings.csv` |
| Founded and incorporated | 2011, in Delaware | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:249,598` |
| Headquarters | 28 East 28th Street, Floor 12, New York, NY 10016 | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:598` |
| Total SEC filings | 737, 2017-07-20 → 2026-08-28 | [[audited]] | `data/filings.csv` |

The 31 January year end is not administrative trivia, and it is the first thing that will
trip up anyone re-deriving these numbers. "FY2026" means the year *ending* 31 January
2026 — so it is mostly calendar 2025. Worse, XBRL's `fy` field labels the **filing**, not
the period: the FY2026 10-K carries figures tagged `fy2026` that describe FY2024 and
FY2025. Keying on that field silently mislabels every year in the series.
`tools/sec_facts.py` derives a correct `period` column from `start`/`end` instead, and
every figure in chapter 2 keys on that. Anyone who pulls the same XBRL facts and gets
different years has hit this, not a disagreement with us.

{{src: data/filings.csv @ 2026-09-01}}

## 1.2 · Going public, and the end of founder control

| Fact | Value | Grade | Source |
|---|---|---|---|
| S-1 filed | 22 October 2021 | [[audited]] | `data/filings.csv` |
| Final prospectus (424B4) | 18 November 2021 | [[audited]] | `data/filings.csv` |
| Net IPO proceeds | ~$456.8m after discounts, commissions and expenses | [[audited]] | `sources/filings/2022-03-31_10-K_000005.txt:2061` |
| Dual-class structure | Ended 30 January 2026 | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:1197` |

The governance change is nine months old at the time of writing and is easy to miss
because it appears in a risk factor rather than a press release. On 30 January 2026 the
Class B common stock was retired and automatically converted into Class A. The 10-K
states the consequence without hedging: "our executive officers and early investors no
longer hold super-voting rights. Consequently, our voting power is now more widely
distributed among our public stockholders."

It is worth being precise about what this does and does not tell you, because it is the
kind of fact that invites over-reading. It does **not** say anything about intent,
performance or strategy. What it changes is the *mechanism*: for four years after the
IPO, a shareholder who disliked the direction of the company had limited ability to do
anything about it, and from January 2026 that is no longer true. For a competitor the
practical reading is about tempo rather than direction. A company answerable to a
distributed shareholder base responds faster to a bad quarter than one insulated from it,
and Braze has now had two consecutive years in which growth decelerated (chapter 2).
Whether that produces pressure is not knowable from the filings; that it *can* now is.

{{src: sources/filings/2026-03-25_10-K_000013.txt:1197 @ 2026-03-25}}

## 1.2b · Who runs it, who sits on the board, and what neither has to do with the votes

The first draft of this analysis answered "who controls it now" entirely with the Class B
conversion, which is half an answer. Control is who holds the votes **and** who holds the
seats, and the seats did not change at all this year.

### The people, named

| Person | Role | Since | Grade | Source |
|---|---|---|---|---|
| **Bill Magnuson** | Chairman, CEO, President, cofounder | CTO Jul 2011; director Aug 2014; CEO Jan 2017; President Jun 2025 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:780,1123` |
| **Jonathan Hyman** | Chief Technology Officer, cofounder | CIO Jul 2011; CTO Dec 2016 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1187` |
| Isabelle Winkles | Chief Financial Officer | Jan 2020 — resigned 29 May 2026 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1186,1177` |
| Astha Malik | Chief Business Officer | CMO Jun 2022; CBO Jun 2023 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1188` |
| Edward McDonnell | Chief Revenue Officer | Jul 2025, from Asana | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1189` |
| Susan Wiseman | General Counsel and Secretary | Jan 2016 — retiring by 30 Jun 2026 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1190,1181` |

**Braze was founded by three people and two of them still run it.** Braze's own company
page names them: *"Braze CEO Bill Magnuson and CTO Jon Hyman participated in a 2011
hackathon that led to a chance meeting with their third cofounder, Mark Ghermezian."*
[[claimed]] {{src: sources/external/braze-company-page_2026-09-02.md @ 2026-09-02}}

That sentence is graded `claimed` and it has to be, which is itself worth a line. **No SEC
filing in this corpus uses the word "cofounder" or names Mark Ghermezian at all.** What
the filings do establish, under legal penalty, is the tenure: Magnuson has held executive
office since July 2011 and Hyman since July 2011, which is the founding year. So the
strong version of the claim — two of the three founding team are still running the
company fifteen years on — rests on an audited fact for the tenure and a marketing page
for the word "founder". Say it that way.

The reference project this method comes from made a finding of exactly this shape: six
founders, all still in post after fourteen years, which says something real about
stability. **Braze's version is a mixed result and the mixture is the interesting part.**
Two founders in post is genuine continuity at the top. The third is absent from every
filing — and the largest disclosed holder of the stock is a private Canadian investment
company, MCG7 Capital Inc., holding 6.0% partly through an entity named **"Appboy BH
LLC"**. Appboy was Braze's original name. The proxy connects MCG7 to no named individual
and expressly says "no single person has voting or dispositive authority over such
securities", so **that is where this observation stops.**
[[audited]] {{src: sources/filings/2026-05-18_DEF-14A_021908.txt:6339 @ 2026-05-18}}

### One person holds four titles, and three of six seats turned over

Magnuson is Chairman, Chief Executive, President and a director. The President title
arrived in June 2025 for a specific reason the proxy states in a footnote: *"Mr. Kleeger
resigned as our President and Chief Commercial Officer on June 1, 2025 and, effective
immediately thereafter, Mr. Magnuson was appointed our President."* The role was absorbed
rather than refilled.
[[audited]] {{src: sources/filings/2026-05-18_DEF-14A_021908.txt:1175 @ 2026-05-18}}

That is one of three departures from a six-person executive team inside about a year:

- **Myles Kleeger**, President and Chief Commercial Officer — resigned **1 June 2025**.
- **Isabelle Winkles**, Chief Financial Officer — announced **28 April 2026**, resigning
  **29 May 2026**, after six years in the role.
- **Susan Wiseman**, General Counsel and Secretary — announced **7 April 2026**, retiring
  on or before **30 June 2026**, after ten years.

[[audited]] {{src: sources/filings/2026-05-18_DEF-14A_021908.txt:1175,1177,1181 @ 2026-05-18}}

**The proxy gives no reason for any of the three, and this record asserts none.** The
temptation here is obvious and must be named so it can be refused: a chief financial
officer resigning in the same year the company disclosed a material weakness in
financial-reporting controls (§2.1b) is a pattern a reader will assemble on their own.
There is nothing in any filing connecting them, the weakness produced no misstatement and
no restatement, and the departure was announced two months after the year end. **Stating
the two facts and declining to join them is the correct treatment**, and a briefing that
joins them has made a claim it cannot support in a room where someone will ask.

What *can* be said is narrower and still useful. Braze replaced its President, its chief
financial officer and its general counsel inside about fifteen months, while its founding
CEO and CTO stayed. Continuity is at the founder layer; turnover is in the professional
layer around it.

Both successions have since completed. Braze's own leadership page in September 2026 names
**Pankaj Malik** as Chief Financial Officer and Chief Accounting Officer and **Chris Lal**
as General Counsel and Corporate Secretary — neither of whom appears in any filing in this
corpus. That page lists ten leaders against the proxy's six executive officers, which is
mostly a difference of scope rather than of headcount, and is recorded as conflict
**C-10**.
[[claimed]] {{src: sources/external/braze-ir-leadership_2026-09-02.md @ 2026-09-02}}

### The board, and the defence that did not get retired

| Fact | Value | Grade | Source |
|---|---|---|---|
| Seats | Seven | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:700-756` |
| Independent | Six of seven; Magnuson is not, "due to his position as our President and Chief Executive Officer" | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:793` |
| Chair | The CEO, with Phillip Fernandez as Lead Independent Director | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:796` |
| Structure | Classified into three staggered classes | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:690-756` |
| Investor seat | Neeraj Agrawal, General Partner of Battery Ventures, director since April 2016; Battery entities and his own holdings total 5,711,181 shares — 5.1% | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:6255,6341` |

Six independent directors out of seven is a good ratio and should be said plainly. The
board is also experienced in a way that is specific rather than decorative: Phillip
Fernandez cofounded and ran Marketo, which is the closest thing to a direct predecessor
company in this category; David Obstler is the sitting CFO of Datadog; Yvonne Wassenaar
ran Puppet and sits on three other public boards.

Two things about that board are worth a competitor's attention, and only one of them is
critical.

**The chair is the chief executive.** The proxy does not gloss this — it argues for it,
saying that separating the roles "has the potential to give rise to divided leadership,
which could interfere with good decision-making". That is a real argument, made openly,
and the mitigation — a Lead Independent Director — is the standard one. Quote their
reasoning rather than characterising it.

**The board is classified**, into three staggered classes, so only about a third of it
stands for election in any year. This is the finding that pairs with §1.2 and it cuts
against the easy reading of the Class B retirement. Braze gave up super-voting stock in
January 2026 and the disclosure language was generous about what that meant for
shareholders. A staggered board is the other structural defence, it is arguably the more
durable of the two, and **it did not change.** So the honest summary of Braze's governance
in 2026 is that one takeover defence was retired and the other was kept — which is neither
a scandal nor the unqualified opening-up the risk-factor language suggests on its own.

### And the votes, which are now ordinary

| Holder | Shares | % | Grade |
|---|---|---|---|
| Entities affiliated with MCG7 Capital Inc. | 6,709,408 | 6.0% | [[audited]] |
| Neeraj Agrawal / Battery Ventures | 5,711,181 | 5.1% | [[audited]] |
| Bill Magnuson | 5,485,123 | 4.9% | [[audited]] |
| Jonathan Hyman | 2,029,437 | just under 2% | [[audited]] |

{{src: sources/filings/2026-05-18_DEF-14A_021908.txt:6255 @ 2026-05-18}}

Against 111,783,722 Class A shares outstanding, and with the Class B stock gone, **no
holder and no director has a blocking position.** MCG7 is the only 5%-or-greater holder
Braze discloses. For anyone modelling how quickly Braze could be pushed to respond to a
shareholder, that is the arithmetic — and it is new this year.

### The related-party line worth reading twice

The proxy discloses that Braze bought **approximately $3.8m of Datadog services in
FY2026**, and that director David Obstler is Datadog's Chief Financial Officer.
[[audited]] {{src: sources/filings/2026-05-18_DEF-14A_021908.txt:6420 @ 2026-05-18}}

That is an ordinary related-party disclosure, properly made, and **nothing improper is
alleged.** It is here because of what it connects to. Chapter 5 records, from an entirely
different document, that Braze "may provide End User metadata, such as user identifiers,
to DataDog for support and application troubleshooting". So a monitoring vendor that
receives end-user identifiers is also a company whose chief financial officer sits on
Braze's board — two facts, disclosed independently in two documents neither of which
references the other, and neither disclosure is deficient.

The reason to hold both is practical rather than insinuating: a buyer's data-protection
review will ask about the sub-processor, and a buyer's procurement team may separately ask
about board relationships. Knowing they are the same company means neither question
surprises you.

One last small thing, recorded because absence of it would be the finding: **the proxy
discloses its own late filings.** Three Section 16 reports covering thirteen transactions
were filed late by Battery Partners XI and its affiliates, and one initial statement by
Edward McDonnell. That is a housekeeping disclosure of the sort every proxy carries; it is
noted here only so a reader who finds it later knows it was seen and judged immaterial.
[[audited]] {{src: sources/filings/2026-05-18_DEF-14A_021908.txt:6367 @ 2026-05-18}}

## 1.3 · Headcount — and the ratio that actually matters

| Fiscal year | Full-time employees | Revenue per employee |
|---|---|---|
| FY2022 | 1,164 | $204k |
| FY2023 | 1,501 | $237k |
| FY2024 | 1,548 | $305k |
| FY2025 | 1,699 | $349k |
| FY2026 | 1,988 | $371k |

[[audited]] {{src: the "we had a total of N full-time employees" line in each 10-K, FY2022-FY2026, with revenue from data/financials_annual.csv @ 2026-09-02}}

A single headcount figure is nearly useless. The series is not.

Over five fiscal years Braze added **71%** more people and **210%** more revenue. Revenue
per full-time employee rose from $204,000 to $371,000 — an **82%** improvement. That is
operating leverage, it is audited, and it is the single most favourable thing in this
entire record. It is also the fact that makes chapter 2's story coherent rather than
merely reassuring: a company whose sales-and-marketing share of revenue falls twelve
points is not doing it by cutting marketing spend in isolation, it is doing it by getting
more revenue out of each person it employs.

One year in that table deserves its own sentence. **In FY2024, headcount grew 3.1% while
revenue grew by nearly a third.** That is not gradual efficiency; that is a hiring pause
held through a year of strong growth, and it is where most of the 82% improvement was
banked. Hiring resumed afterwards — FY2026 added 289 people, the largest absolute
increase in the series — but the ratio never went back.

The counterweight, and it belongs here rather than in a footnote: the same period is when
customer expansion slowed (chapter 7) and share-based compensation began exceeding the
entire net loss (chapter 2). Efficiency improved *and* growth decelerated. Both are true,
they are visible in the same years, and an account that gives you only one of them is
selling something.

### What the number does not cover

**1,988 counts full-time employees only.** Braze's own proxy, drawing a median employee on
the same date, uses a different population — "all of our full-time **and part-time**
employees… We did not include any independent contractors" — and never sizes it. So there
are at least three populations in play (full-time; full-time plus part-time; and those
plus contractors), Braze publishes one of them, and no independent headcount was captured
in this run to triangulate against. This is conflict **C-07**, and its ruling is simple:
say "1,988 full-time employees", never "headcount of 1,988".

{{src: sources/filings/2026-05-18_DEF-14A_021908.txt:5769 @ 2026-05-18}}

## 1.4 · What management is paid to optimise

This is the question `QUESTIONS.md` #33 asked and the first pass left open, because it
never opened a proxy statement. The answer is unusually legible.

| Fact | Value | Grade | Source |
|---|---|---|---|
| FY2026 bonus-plan weighting | Net CARR **60%**, non-GAAP operating income (loss) **40%** | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1994` |
| Profitability gate | Missing a specified non-GAAP operating income target as a share of gross profit results in "0% achievement of this performance metric" | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1994` |
| Growth cap | If retention fell below target, Net CARR achievement "would be limited to 110%" | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:1994` |
| CEO total compensation, FY2026 | $14,230,598 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:5771` |
| Median employee total compensation | $164,000 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:5771` |
| CEO pay ratio | 87 to 1 | [[audited]] | `sources/filings/2026-05-18_DEF-14A_021908.txt:5771` |

Read the three mechanics together and the plan describes a strategy more precisely than
any keynote does.

Sixty per cent of the financial component pays for **net contracted recurring revenue** —
growth, but *contracted* growth net of churn, which is a harder target than bookings.
Forty per cent pays for **non-GAAP operating income**, and that portion has a hard floor:
miss a specified operating-income-to-gross-profit threshold and the metric pays **nothing**,
regardless of how close you came. And the growth half is capped at 110% if retention
misses, which explicitly forbids buying CARR at the expense of the existing base.

That is a compensation plan built to produce exactly the pattern chapter 2 observes:
decelerating growth alongside improving efficiency. It does not prove causation. It does
mean that when a competitor asks "will Braze discount aggressively to win this deal?",
the honest answer from the public record is that the people approving that discount are
paid on a metric with a profitability gate attached, and were paid that way through the
year in which sales-and-marketing spend fell to its lowest share of revenue in seven
years.

The pay ratio is 87 to 1 on a median of $164,000. Both numbers are worth quoting together
rather than separately: a high median softens the ratio, and it also sits awkwardly beside
the Glassdoor complaint recorded in chapter 7 about "discrepancies in compensation
relative to market rates". A $164,000 median is not a low-paying company. The grievance,
if the reviews are read closely, is about *progression* rather than level — which is the
same thing the "limited upward mobility" comment says.

## 1.5 · The legal footprint, and one entity that is not what it looks like

| Fact | Value | Grade | Source |
|---|---|---|---|
| Group entities | 15, across 14 territories | [[documented]] | `sources/clean/braze-subprocessors.md:41` |
| Territories named | Australia, Brazil, Canada, France, Germany, Ireland, Spain, United States, Ireland & Romania, Japan, South Korea, United Kingdom, UAE, Singapore, Indonesia | [[documented]] | `sources/clean/braze-subprocessors.md:41` |

This list comes from the sub-processor disclosure rather than from marketing, which is
what makes it worth having: it is compelled to be complete, and it names its own
territories rather than gesturing at "global presence".

Two things in it repay attention.

**Braze KK, in Japan, is not a wholly-owned subsidiary.** Outside investors — Japan Cloud
Computing and M30 LLC — bought $10.0m of its stock across 2020 and 2021; employees hold
options over its shares; and a redeemable non-controlling interest sits outside permanent
equity on the balance sheet. Braze holds a majority and consolidates it as a Variable
Interest Entity. Anyone reasoning about Braze's Japanese operation from the entity list
alone would assume ownership and control that the filings do not support. This is conflict
**C-09**.

**"Braze Ireland Procurement Limited" is located in "Ireland & Romania"**, and the careers
board independently lists Bucharest as a hiring location. Two documents with no
relationship to each other — a data-protection disclosure and a job board — describing the
same Romanian engineering presence is the kind of corroboration this method exists to
find, and it is the only evidence in the corpus that Braze operates in Romania at all.
Neither document alone would have been enough to say so.

Set the footprint against the revenue. Fifteen legal entities and fifteen regional
clusters (chapter 4) support a business where, outside the United States, **no single
country reaches ten per cent of revenue** (chapter 2). That is a deliberately wide, thin
international structure, and it is expensive to run. It is also the necessary shape if
data-residency commitments are part of what you sell, which chapter 4 argues they are.

{{src: sources/clean/braze-subprocessors.md:41 @ 2026-09-02}}

#### What would change this chapter

A merger, take-private or change of control — all disclosed by 8-K within four business
days. A materially different headcount in the next 10-K, or, more usefully, any
disclosure that sizes the part-time population and closes C-07. A buy-out of the Braze KK
minority, which would resolve C-09 and would appear in the equity note. A change to the
bonus-plan weightings in the next proxy, which is the earliest public signal that the
growth-versus-profitability balance has been re-struck. The entity list changes whenever
the sub-processor document is revised; this record uses revision 1 June 2026 and any
later revision supersedes it.
