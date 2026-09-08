# The Braze deck, in full

Every slide in order: **what is on screen, and what to say over it.** Generated from the
deck itself by `deck/make_script.py`, so a slide and its script can never drift apart.

**10,154 spoken words — 78 minutes presented, or about 65 minutes to read.**
43 slides, 109 seconds each at a normal speaking pace.

---

## If you are learning Braze rather than presenting it

Read this file top to bottom. It is the most efficient thing in this repository for that,
because it was written to be **said to somebody who does not know Braze** — the argument
in the order it was built to land, with the evidence attached at the point it is used.

Then, and only then:

| For | Read |
|---|---|
| The traps — where sources disagree, and the exact wording to use | `docs/CONFLICTS.md` |
| What we expected before reading anything, and what was wrong | `docs/STRATEGY.md`, "How the ten ended" |
| The eight things nobody knows, and what would close each | `docs/QUESTIONS.md` §4 |
| The reasoning behind any single claim | the record chapter named under each part below |
| One specific number | `docs/FACTS.md` — 244 rows, a lookup table, never a read |

**What this cannot teach you.** Nobody on this project ever logged into Braze. It is built
entirely from public sources, so it is strong on the business, the money and the decisions,
and it tells you where the product's *limits* are rather than what using it feels like.
For that, read Braze's own documentation — 1,352 pages of it are captured in `sources/docs/`
and `grep` beats their site search — against the seven-stage walkthrough in Part II.

**Bold** marks the words to land on. Press **N** in the deck to read the narration beside
its slide.

---


## Part 0 — Frame

*How to judge everything that follows.*

**Deeper:** `deck/record/08-open.md` §8.0a — the four documents, and why they are hard to falsify.

### 01 · Competitor Analysis

**On screen**

Competitor analysis

Growing slower every year, spending less to do it — and its newest capability was bought, not built.

- **1,352 pages** — Their documentation
- **737 documents** — SEC filings
- **FY2019 → now** — Audited financials
- **137 repos** — Public code
- **451 incidents** — Status page
- **17 outside suppliers** — Sub-processors

Toma Pirtskhelani · Product Manager
Public sources only · September 2026

**Say**

> This is a competitor analysis of **Braze**.

> The one thing to know before we start: Braze is a **listed company**, and that changes
> the nature of the evidence. Where a private vendor gives you claims, Braze files audited
> accounts four times a year under legal penalty — and publishes a status page, a public
> code repository, and a sub-processor list it is legally obliged to keep complete.

> Everything here comes from sources you can check yourself. **Their own technical
> documentation. Their SEC filings. Their public code. Their status page. And customer
> and employee review panels, read and coded rather than summarised.**

> No press release is taken at face value. Where their marketing and their own
> documentation disagree, I will show you both.

### 02 · How we approach it
Method · how this is built — **Four parts, three rules**

**On screen**

- `PART I` **The company** — who owns it · what it costs · who buys it
- `PART II` **The product** — seven stages of one campaign
- `PART III` **Strategy** — where the money goes · what protects them
- `PART IV` **Open questions** — what public sources cannot answer

***AND THREE RULES THAT APPLY TO ALL FOUR***

- **Every claim is graded** — Marked by how strong its source is. The bar at the foot of each slide shows where we are.
- **Marketing is labelled as marketing** — Their own words appear — but never as evidence.
- **Gaps become a backlog** — Anything needing a non-public source goes on the open-questions list, and grows as you add to it.

**And ten expectations were written down before any of this was read. Four turned out wrong — slide 40 shows which.**

**Say**

> Four parts. **Who the company is. How the product actually works. Where the strategy is
> going. And what we still cannot answer.**

> Three rules run through all of it, and they are on the slide because they are what makes
> the rest usable rather than merely interesting.

> **Every claim is graded by how strong its source is.** A bar at the foot of every slide
> tells you where we are, and a claim takes the grade of its *weakest* supporting source,
> never its best. If one number in a sentence comes from a marketing page, the sentence is
> marked as marketing.

> **Marketing is labelled as marketing.** Braze's own words appear here often, because a
> listed company's own words are worth quoting and sometimes they are the finding. They
> never appear as evidence for a technical claim.

> **And gaps become a backlog.** As we go I will flag the questions that need sources we do
> not have. Each one is written down with what would close it, so it is a list to prioritise
> rather than a list of things I quietly skipped over. One of them closed while this deck
> was being built.

### 03 · How we grade
Method · evidence grading — **How to judge every claim here**

**On screen**

- **Audited filings, and their own technical documentation** — Signed off by auditors and filed under legal penalty — or behaviour the platform must actually support
- **Independent records** — Customer reviews, infrastructure traces, incident history, real transacted prices
- **Marketing, or disputed** — Their own claims, or sources that contradict each other

Five grades are kept in the evidence record. Three reach the slides, mapped in docs/EVIDENCE-GRADES.md. **A claim takes the grade of its weakest supporting source, never its best.**

**Say**

> Three grades on the slides, five in the record behind them.

> **Strong** is a filing or their own technical documentation. An audited number is
> signed by someone with legal exposure. Documentation is written for people who will
> hit the limits, so it describes the product that exists rather than the one being sold.

> **Medium** is independent: what customers say, what the infrastructure shows, what an
> outage record admits.

> **Weak** is their marketing, or anywhere two credible sources disagree — and where
> they disagree I will show you both rather than pick one.

> One rule underneath all of it: **a claim takes the grade of its weakest source, never
> its best.**


## Part I — The company

*Who they are, what they bought, what it costs, who buys it.*

**Deeper:** `deck/record/01-company.md`, `02-money.md`, `03-acquisitions.md`, `07-market.md`.

### 04 · Part I: The company
Part I — **The company**

**On screen**

- `01` Who they are, and who controls them now
- `02` What they bought, and what it cost
- `03` What a customer pays — bounded, not guessed
- `04` Who buys it, and who buyers compare them against

*Audited filings unless marked otherwise*

**Say**

> Part one is the company. Four questions: who they are and who controls them, what they
> have bought, what a customer pays, and who actually buys it.

> The thing that makes this part unusual is that **Braze is listed.** Almost everything in
> the next twelve slides is filed under legal penalty rather than claimed on a website —
> seven years of audited accounts, two acquisition prices with their purchase-price
> allocations, a customer count that is a *defined* metric, and a proxy statement naming
> every executive officer and director. With a private vendor you would be inferring most
> of this from job ads and press releases.

> Two things to watch for as we go. **Where I use a marketing number instead of a filed
> one, I will say so out loud** — those are the weak-graded claims and there are only a few.
> And the most useful slide in this part is probably not the one you expect: it is the
> customer-count slide, because the definition of "customer" turns out to change what the
> only available price figure actually means.

### 05 · The four documents
What this rests on — **Four documents a company cannot write freely**

**On screen**

- **The 10-K** — Their **audited annual report to the US regulator**. Signed by the chief executive and the finance chief, and wrong at legal risk. **Seven years of them.**
- **The proxy statement** — Filed before the shareholder meeting. Must name **every executive officer and director**, their pay, and who owns the company.

- **The sub-processor disclosure** — A public list of **every outside supplier that touches customer data**. The law obliges them to keep it complete, so it names middlemen no marketing page would.
- **The status page** — A live record of **every outage since 2016**, written during the outage. Nobody writes one of these to look good.

**None of these is marketing.** Three are filed under legal penalty and the fourth is written under pressure — so wherever this deck and Braze’s website disagree, the documents win.

**Say**

> Before any findings, thirty seconds on where this comes from — because four documents do
> most of the work in this deck and they are the reason to believe it.

> **The 10-K is their audited annual report to the American regulator.** Once a year, signed
> personally by the chief executive and the finance chief, audited by Ernst & Young. If it
> is wrong, that is a legal problem for named individuals. We have seven years of them.

> **The proxy statement** goes out before the shareholder meeting. It has to name every
> executive officer and director, say what each of them is paid, and disclose who owns the
> company. It is the only document in this set with people in it.

> **The sub-processor disclosure** is a public list of every outside supplier that touches
> customer data — data-protection law requires it to be complete. That completeness is the
> useful part: it names the middlemen that no marketing page would ever mention, and two of
> the sharpest findings in this deck come straight out of it.

> **And the status page** is a live record of every outage since 2016, written during the
> outage by someone trying to fix it. Nobody writes a status page to look good.

> The thing to take from this slide is not the four names. It is this: **none of them is
> marketing.** Three are filed under legal penalty and the fourth is written under pressure.
> So when their website and their filings disagree — and they do — you know which one I am
> going to believe, and now you know why.

### 06 · Five things
Executive summary — **If you remember five things**

**On screen**

- **Braze grades its own data delays, and three of four are slow** — Their documentation labels three of the four ways data gets in **“not real-time”**. Their table, not our characterisation.
- **The AI decisioning engine was bought, not built** — OfferFit, acquired June 2025 for **$303.2m**. The models come from Anthropic, OpenAI and Google.
- **One instance is not on the same cloud as the others** — The addresses Braze tells you to allowlist for **US-08** belong to Microsoft. Every other instance’s belong to Amazon.

- **They are slowing down and getting more efficient at the same time** — Growth has halved since FY2023 while sales spend fell further. **Three straight years of positive cash flow.**
- **Braze names four competitors. Buyers compare them against eight** — The five extra names are specialists Braze never mentions.

**Say**

> Five things.

> **One. Their documentation is more honest than their marketing, and it is the best
> source you have.** Every hard limit in this deck came from Braze's own technical pages.

> **Two. The AI decisioning product is an acquisition.** OfferFit, bought June 2025 for
> three hundred and three million dollars, renamed AI Decisioning Studio. That is in the
> auditor's note, not in a rumour.

> **Three, and this is the one nobody else will have.** Braze publishes the IP addresses
> you must allowlist per instance. The ones for US-08 are all registered to Microsoft.
> Every other instance is Amazon. Their sub-processor disclosure names only Amazon and
> Google. I will show you all three sources.

> **Four. The financial story is better than the loss line suggests** — decelerating
> growth, but improving efficiency and three years of positive operating cash flow.

> **Five. Their competitive set is wider than they say it is.**

### 07 · Who they say they are
Their story · in their own words — **Their biggest claim, in their most careful document**

**On screen**

> “Our platform empowers **real-time engagement** between brands and their customers … made possible by our proprietary, enterprise-grade **stream processing architecture** … We have designed it to **listen like a human would**, process new information in context, and **react instantaneously**.”
> — *Braze 10-K, Item 1 · filed 25 March 2026*

- **The claim** — A single platform, fed by streaming first-party data, reacting in the moment across every channel
- **Why it is quoted here** — This is the company’s own narrative in a filed document — the strongest form of a marketing claim, not a technical one
- **What to hold on to** — “Real-time” is doing a lot of work in that sentence. Slide 21 shows their own table grading it

**Say**

> This is Braze describing Braze, in the 10-K.

> I quote it from the filing rather than the website deliberately. It is the most
> carefully-lawyered version of their story that exists, and it still leads with
> **real-time**.

> Hold that word. It comes back on slide twenty-one, where their own documentation grades four
> ingestion paths and labels three of them "not real-time".

> That is not a gotcha, and I will not present it as one. It is one word covering two
> architectures — and knowing which one a prospect is buying is worth more than the
> argument.

### 08 · Origins
Origins · and who controls it now — **Origins, and who controls it now**

**On screen**

- **Bill Magnuson** · Chairman · CEO · President · Cofounder

  CTO from July 2011, chief executive since 2017, chairman — and President too since June 2025, when the previous President resigned. One person, four titles.
  Cofounder Jon Hyman is still CTO, an officer since 2011.

***AND WHO HOLDS THE SEATS***

- **Seven seats, six independent** — Magnuson is the exception. **Phillip Fernandez is Lead Independent Director** — the role a board creates when its chair is not.
- **And the board is classified** — Three staggered classes, so only about **a third stands in any year**. The super-voting stock is gone; this is not.
- **The votes, after January** — Class B converted **30 January 2026**. Largest holder **6.0%**, the CEO **4.9%**, the Battery partner **5.1%** — **no blocking position left.**

**Say**

> Founded 2011. Public since November 2021. And now the part this slide is actually for,
> because until this pass it answered only half its own question.

> **Who runs it.** Bill Magnuson — chief executive since January 2017, on the board since
> 2014, and the company's Chief Technology Officer before that from July 2011. He is also
> chairman. And since June 2025 he is President too, because the previous President
> resigned and the role was not refilled. One person holds four titles.

> His cofounder Jon Hyman is still Chief Technology Officer, and has been an officer since
> July 2011. **Two of the three cofounders are still running the company fifteen years
> on** — the third, Mark Ghermezian, appears in no filing at all. Braze names all three on
> its own website; the SEC filings name none of them as founders, which is why that
> particular fact is graded as a company claim rather than as audited.

> **Who holds the seats.** Seven directors, six of them independent — Magnuson is the
> exception because he is an executive. Phillip Fernandez is Lead Independent Director,
> which is the role a board creates when its chair is also its chief executive. The proxy
> defends that combination rather than glossing it, and I would quote their reasoning
> rather than mine.

> The one I would flag is the third card. **The board is classified into three staggered
> classes**, so only about a third of it stands for election in any year. Braze retired its
> super-voting stock in January and got a good deal of credit for it. The staggered board
> is still there, and a staggered board is the more durable of the two defences.

> **Who holds the votes.** After the conversion, ordinary arithmetic. The largest holder
> Braze discloses is at six per cent, the chief executive at just under five, and the
> Battery Ventures partner on the board at five. Nobody has a blocking position. Before
> January, the founders and early investors did.

> So the honest summary is that control got more conventional this year in one respect and
> did not move at all in another — and if you are modelling how fast Braze can be pushed to
> respond to a shareholder, both halves matter.

### 09 · How they got this big
Capital · and what it bought — **7.7× bigger, a billion already contracted**

**On screen**

- FY2020 · **96.4m**
- FY2021 · **150.2m**
- FY2022 · **238.0m**
- FY2023 · **355.4m**
- FY2024 · **471.8m**
- FY2025 · **593.4m**
- FY2026 · **738.2m**

- **$456.8m** — net IPO proceeds, Nov 2021
- **7.7×** — revenue growth, FY2020 to FY2026
- **$124.3m** — cash at FY2026 year end
- **$1,033.0m** — contracted, not yet recognised

***THE CAVEAT THAT TRAVELS WITH EVERY NUMBER IN THIS PART***

Braze disclosed a **material weakness in internal control over financial reporting** at 31 January 2026 — *a flaw in the checking, not an error in the numbers*. Ineffective IT controls over **user access and program change management** on the systems that produce these figures. **And, in the same breath:** it “did not result in any identified misstatements”, nothing was restated, and Ernst & Young attested.

**Say**

> Revenue, seven audited years: ninety-six million to seven hundred and thirty-eight.
> **Seven point seven times in six years.**

> They raised four hundred and fifty-seven million net at IPO and hold a hundred and
> twenty-four million in cash at the last year end.

> The number on the right is the one I would put in front of a CFO: **a billion and
> thirty-three million dollars of remaining performance obligation** — revenue that is
> contracted and not yet recognised. That is one point four times the current year's
> revenue, already signed.

> Let me reframe what that actually means for us, because it is routinely under-used. RPO
> is not pipeline and it is not a forecast; it is signed business sitting inside contract
> terms, with an auditor's signature on the total. **Roughly a year and a half of Braze's
> current revenue is not available for us to compete for** — not because those customers
> would refuse to move, but because they are not up for renewal. That changes the question
> from "can we win this account" to "when does it come up", and for most of their base the
> answer this year is: it does not.

> Now the band at the bottom, and I want it on the slide rather than in my pocket. **Braze
> disclosed a material weakness in internal control over financial reporting** at the last
> year end — ineffective IT general controls over user access and program change management
> on the systems that produce these numbers. Their CEO and CFO signed that disclosure
> controls were not effective at the reasonable assurance level.

> **And in the same breath, because either half alone misleads:** it produced no identified
> misstatement, nothing was restated, and Ernst & Young still issued an attestation report
> on internal control.

> If someone asks how much that should change their confidence in these figures, the honest
> answer is: less than the phrase "material weakness" sounds, and more than zero. A material
> weakness is a statement about the *probability* that an error could occur and go
> undetected. It is not a finding that one did. And here every independent check came back
> clean — no misstatement identified, nothing restated, an auditor attestation, and
> separately we ran a mechanical sweep across twenty-nine reported XBRL concepts looking for
> any figure Braze had quietly superseded in a later filing. We found none. Three
> confirmations that the outputs are sound, against one disclosure that the process
> producing them is not yet controlled to standard.

> Two things not to do with it. **Do not turn it into a claim about customer data
> security.** It is scoped to financial-reporting systems and says nothing about the
> platform — and for a company whose product is data infrastructure, that is exactly the
> leap an audience will make for you unless you close it off. And do not leave it out: a
> briefing that omits this and then gets asked about it by a prospect's finance team has
> spent its credibility for nothing.

> I missed this on my first pass through the filing. It is the reason the money part of
> this deck carries a band that the product part does not.

### 10 · Acquisition: OfferFit
Acquisition one · June 2025 — **They bought their AI, and the filing says so**

**On screen**

> “the Company completed the acquisition of **OfferFit, Inc.** (‘OfferFit’) **which is now known as AI Decisioning Studio** for total consideration of **$303.2 million**.”
> — *Ernst & Young, critical audit matter · Braze 10-K, 25 March 2026*

- **$303.2m** — total consideration
- **77%** — was goodwill — price not tied to any asset
- **$56.7m** — developed technology, amortised to cost of revenue
- **2 Jun 2025** — closed

***WHAT THE PURCHASE-PRICE ALLOCATION TELLS YOU***

Only **$66.6m of the $303.2m was identifiable**, and $56.7m of that is the software — so Braze bought a capability and its people, not revenue. The trademark went at **$0.9m**: nobody expected the name to survive. **So the margin drag runs to 2031, and any AI pricing they quote has to carry it.**

**Say**

> This is the single most useful sentence in the filings.

> **OfferFit — which is now known as AI Decisioning Studio.** The product Braze markets as
> BrazeAI Decisioning Studio is a company they bought, fifteen months ago, for three
> hundred and three million dollars. A hundred and ninety-five in cash, a hundred and eight
> in stock.

> Seventy-seven per cent of that price was goodwill — which is what a price looks like when
> what you are buying is a team and a position rather than assets.

> And note where the technology amortisation lands: **cost of revenue**. That is why this
> acquisition shows up in their gross margin, which is slide thirty-four.

> The 10-K calls what they bought "OfferFit's multi-agent decisioning engine". So when we
> get to the AI slide, remember that the agentic layer has a purchase price.

### 11 · Acquisition: North Star Y
Acquisition two · June 2023 — **They bought a market, and the earn-out paid nothing**

**On screen**

- **$26.8m** — paid at completion
- **$26.0m** — more, if revenue targets were met
- **$0** — of that was ever paid
- **What it was** — North Star Y, Pty Ltd — Braze’s **exclusive reseller in Australia and New Zealand**. Buying it took the market direct.
- **What the filing records** — Braze “reduced the contingent consideration liability … **to zero as it was determined that the sellers did not satisfy the earn-out qualifications**.”
- **How to read it** — An **earn-out** is money owed only if the business hits agreed targets. This one paid nothing, so the targets were not met — which does not say the acquisition failed, and the filings do not say that either.

**Say**

> Two years earlier they bought their own Australia and New Zealand reseller — twenty-six
> point eight million, to take that market direct.

> The sellers could have earned up to twenty-six million more, on qualified revenue
> performance, over the two years after completion.

> **They earned none of it.** The FY2026 filing records the contingent consideration
> reduced to zero because the sellers did not satisfy the earn-out qualifications.

> I want to spend a moment on how to read that, because it is the fact in this deck most
> easily over-read, and the reasoning matters more than the number.

> An earn-out is a price-setting device for a disagreement. The buyer thinks the business
> will do X. The seller thinks it will do more. Rather than argue about it, they agree the
> seller gets paid the difference if the seller turns out to be right. **So a zero payout
> tells you one thing precisely: the revenue trajectory the sellers signed up to in June
> 2023 did not happen.** And it tells you that from the buyer's own audited filing, in a
> document where getting it wrong has legal consequences. No website was ever going to say
> this.

> Here is what it does **not** say. It does not say the acquisition failed, and the filings
> do not say that either. Braze still owns the business. They still run an AU-01 cluster —
> you will see it on the infrastructure slide. And they have never taken an impairment
> against the twenty-eight point four million of goodwill from that deal, which they would
> have had to disclose. A perfectly benign reading is available: earn-out targets are where
> optimism gets priced, they are often set aggressively on purpose, and the business may be
> performing adequately just not at the seller's number.

> Two details close the loop. The two point eight million indemnification holdback was
> **released in full**, which means nobody made an indemnity claim against the sellers — so
> whatever happened was a performance shortfall, not a dispute about what was sold. And the
> results of the acquired business were recorded as "not material" to the consolidated
> statements, which is what you would expect of a regional reseller and tells you the
> shortfall never threatened the group numbers.

> So the sentence I would actually say out loud is the narrow one: **Braze paid twenty-six
> point eight million for direct control of Australia and New Zealand, structured up to
> half the potential value as performance-contingent, and the performance conditions were
> not met.** If you sell against them in that region, the public record contains no
> evidence of the acceleration the deal was priced for. That is worth knowing, and it is
> the most useful thing on this slide.

### 12 · What it costs
Price · bounded, not guessed — **Nobody publishes a price. You can still bound one**

**On screen**

- **~$283,000** — revenue ÷ customers, FY2026 — a *bound*, not a price

**An average, not a typical contract.** A few very large customers pull it up, and most pay far less. It is the ceiling of what an average customer costs, not what one does.

***AND THE MECHANIC UNDERNEATH IT — FROM THEIR DOCUMENTATION***

- **You are billed per data point** — “a session start, session end, custom event, or purchase recorded, as well as **any attribute set**” — each counts separately
- **Engagement is free** — Opens, clicks, push tokens and device info are **not** counted. A genuinely customer-friendly boundary
- **Their own advice is to send less** — “**Don’t waste data points. Only update changing data!**” — a platform sold on streaming everything, priced so you send less

**Say**

> No vendor in this category publishes a price and Braze is no exception. But a listed
> company gives you something better than a guess: **seven hundred and thirty-eight million
> of revenue across two thousand six hundred and nine customers is about two hundred and
> eighty-three thousand dollars each.**

> Say "bounded at". Never say "costs". It mixes a two-thousand-seat enterprise with a
> startup and it includes professional services.

> The mechanic underneath is the useful part. You are billed per **data point** — and their
> definition includes *any attribute set on a profile*. A session start and a session end
> are two data points.

> Engagement tracking is free, which is fair and I will say so.

> But look at the third card. Their own documentation says **"Don't waste data points. Only
> update changing data."** A platform positioned on continuous streaming of behavioural
> data, advising customers to build programmes to send less of it. That tension is theirs,
> not mine — and a Gartner reviewer independently calls out overages getting expensive
> quickly.

### 13 · Who uses it
Customers · three rosters, never merged — **Three ways to count a customer**

**On screen**

- **2,609** — the 10-K’s defined metric, 31 Jan 2026
- **333** — customers at $500k+ ARR — up from 202 in FY2024
- **178** — self-published customer stories
- **—** — independent detection: not attempted

***EXPANSION IS SLOWING, AND THE ENTERPRISE PREMIUM HAS NEARLY GONE***

- FY2024 · all customers · **117%**
- FY2024 · $500k+ ARR · **120%**
- FY2026 · all customers · **109%**
- FY2026 · $500k+ ARR · **110%**

**Say**

> Three customer counts and they must never be merged.

> **Two thousand six hundred and nine** is the 10-K's defined, audited metric. A hundred
> and seventy-eight is the number of customer stories they chose to publish — that is
> marketing, and it is not a sample of anything. Independent detection I did not attempt,
> and I am recording that as a gap rather than a zero.

> Now the bars, because there are two movements and the second is easy to miss.

> Net retention is falling — a hundred and seventeen to a hundred and nine. Braze explains
> that themselves: customers renewing at levels closer to current needs rather than
> betting on future demand.

> The subtler one: **large customers used to expand three points faster than average. Now
> they expand one point faster.** Whatever premium the enterprise cohort had is nearly
> gone — while the number of those accounts has grown from two hundred and two to three
> hundred and thirty-three. More big logos, each growing more slowly.

### 14 · Where they operate
Geography · audited, not inferred — **No second home market**

**On screen**

- **54.9%** — United States, FY2026
- **45.1%** — international
- **0** — other countries above 10% of revenue
- **The sentence that matters** — “Other than the United States, **no other individual country accounted for 10% or more of total revenue** for any of the periods presented.”
- **Set against the footprint** — **15 regional clusters** and **15 legal entities across 14 territories** — from the status page and the sub-processor disclosure respectively.
- **So what** — A wide, thin footprint on a heavy fixed base. **No single non-US market is large enough that losing it would show** — so outside the US you compete market by market, and so do they.

**Say**

> Geography, audited, from the segment note — not inferred from customer domains, which
> is what you would be doing with a private vendor.

> Forty-five per cent of revenue is international. And then the sentence that does the
> work: **other than the United States, no individual country reaches ten per cent of
> revenue.**

> Put that next to the footprint. Fifteen regional clusters on the status page. Fifteen
> legal entities across fourteen territories in the sub-processor list. Offices and hiring
> in twenty-six locations.

> That is a wide, thin international business carrying a heavy fixed base. It is a
> strategic bet on international rather than a harvest of it — and it is the kind of thing
> that shows up in gross margin before it shows up in growth.

### 15 · What customers say
Review panels · coded, not summarised — **Well liked, with two consistent complaints**

**On screen**

***G2’S OWN TAGS, OVER ITS WHOLE REVIEW BASE — PRAISE IN GREY, CRITICISM IN RED, ONE SCALE***

- Ease of Use · **385**
- Intuitive · **188**
- Customer Support · **151**
- Helpful · **148**
- Missing Features · **140**
- Learning Curve · **139**
- Limitations · **102**
- Steep Learning Curve · **86**

**Two themes recur across unrelated panels, which is what makes them worth quoting: reporting, and the learning curve.** TrustRadius codes reporting as “limited and unintuitive, a sentiment shared by 36% of reviewers”.

**Say**

> Braze is genuinely well liked. Four and a half out of five on two panels, eight point
> eight out of ten on the third, across more than two thousand reviews. I am not going to
> soften that.

> These tags are G2's own coding over their whole review base, not my sample — and they
> are on **one scale**, deliberately, because the shape is the point: the single most
> common praise tag is nearly three times the most common criticism.

> Two complaints recur across panels that have nothing to do with each other, and that is
> what makes them worth your attention. **Reporting**, and the **learning curve**.

> TrustRadius puts a number on the first: thirty-six per cent of their recent reviewers
> describe reporting as limited and unintuitive.

> Hold that too, because when we get to the platform section you will see the mechanism
> behind it — the raw-data export that fixes it is a paid add-on called Currents.

### 16 · What employees say
Glassdoor · and the careers board — **What employees say**

**On screen**

- **4.1*/5*** — 524 ratings
- **82%** — would recommend
- **90%** — approve of the CEO
- **71%** — positive business outlook

> Glassdoor’s own summary names the weak spots: **“limited upward mobility and discrepancies in compensation relative to market rates”**.
> — *Glassdoor company page · captured signed-in, 2 September 2026*

- **Not pay — progression** — Median employee pay is **$164,000**. Not a low-paying company, so this is a complaint about the ceiling, not the floor
- **Still hiring hard** — **296 open roles** across 15 departments — including Bucharest, matching a Romanian entity in the sub-processor list

***AND WHAT THEY ARE HIRING FOR — THE FORWARD-LOOKING HALF***

Sales **89** · Engineering **57** · Customer Experience **38**. **Go-to-market is 72.0% of the board against 19.6% for engineering and product.** So they are buying new logos rather than building — and that is where they will meet you.

**Say**

> Employees rate them well. Four point one, eighty-two per cent would recommend, ninety
> per cent approve of the CEO.

> **The quote is the slide.** That is Glassdoor's own summary of the weak spots, in
> Glassdoor's words, not mine: limited upward mobility, and pay against market. Read it out.

> Then the card beside it, because it is what stops that being misread. The proxy puts
> median employee compensation at a hundred and sixty-four thousand dollars. **This is not a
> low-paying company.** So "limited upward mobility" is a complaint about the ceiling rather
> than the floor — people are paid well and cannot see the next step. That is a different
> problem, and a harder one to fix with money.

> One thing that is *not* here, and I want to say why. I went looking for a
> work-life-balance decline because that is the usual story at this
> stage of a company's life. **It is not there.** Work-life balance tracks the overall
> rating almost exactly. I am reporting that because it is what the evidence says, not
> because it is interesting.

> The complaints in Glassdoor's own summary are about ceilings rather than conditions:
> management clarity, limited upward mobility, and compensation against market.

> And they are hiring hard: **two hundred and ninety-six open roles across fifteen
> departments**, taken from their own Greenhouse board rather than counted off the careers
> page.

> The band at the bottom is the part I would actually use. **Sales eighty-nine.
> Engineering fifty-seven. Customer Experience thirty-eight.** Add the go-to-market
> functions up and they are seventy-two per cent of the board, against under twenty per
> cent for engineering and product — **roughly three and a half to one.** The single
> largest department is Sales, on its own bigger than engineering and product combined.

> Read that against slide twelve. Retention says expansion inside the existing base is
> slowing and growth is moving to new logos. A hiring board that is three-quarters
> go-to-market is what executing that shift looks like from outside — and it is a *leading*
> indicator where retention is a lagging one.

> Two limits on how hard I would push it. **A requisition is an intention, not a person**;
> a board is a plan and plans get cut. And this is not a spend ratio — a sales req costs
> less than a senior engineering one, so three and a half to one in headcount sits
> comfortably with the audited two to one in money on slide thirty-four. Different
> measures, same direction, which is what corroboration actually looks like.

> One small corroboration I like: the board lists Bucharest, and the sub-processor
> disclosure lists a Braze entity in "Ireland and Romania". Two unrelated documents
> describing the same thing is how you know both are real.

> Worth saying how this number got here, because it is a method point. The first pass
> recorded the department split as uncapturable — the board's filter would not drive under
> automation — and wrote it down as an open question. It was published as JSON the whole
> time. **When a page will not yield, look for the API behind it before you record a
> gap.**

### 17 · Who they compete with
Competition · two lists — **They name four. Buyers weigh eight.**

**On screen**

***NAMED IN THE 10-K — THEIR CHOICE***

- Adobe · Salesforce · Iterable · Klaviyo

***GARTNER’S BUYER-DERIVED SHORTLIST — NOT THEIR CHOICE***

- Salesforce · Adobe · Iterable · Oracle · Optimove · Blueshift · MoEngage · CleverTap

***THE GAP IS THE FINDING***

**The brighter names on each side are the ones the other list does not have.** Three of their four appear on the buyer list, so this is not a vendor misreading its market — but five vendors buyers compare them against appear nowhere in the 10-K. **So those five are the ones to watch: Braze is not positioning against them, and will not have an answer ready.**

**Say**

> Two lists. On the left, the four competitors Braze names in its own 10-K. On the right,
> the vendors Gartner reports buyers *also considered* — derived from the buyers, not from
> Braze.

> Three names are shared. So this is not a company misreading its own market, and I will
> not claim it is.

> Note also that the asymmetry only runs one way. Klaviyo is on Braze's list and not on the
> buyers'; everything else Braze names, buyers confirm. So the hypothesis we went in with —
> that Braze would turn out to be shortlisted against a completely different set of vendors
> — was only **partly** borne out, and I want that on the record as partly rather than as a
> win.

> **The asymmetry that remains is the finding.** The buyer list is twice as long, and the
> five extra — Oracle, Optimove, Blueshift, MoEngage, CleverTap — are named nowhere in the
> filing.

> The character of those five is what matters, more than the count. Oracle is another suite.
> But Optimove, Blueshift, MoEngage and CleverTap are mobile-engagement and CDP
> **specialists**. And that changes the conversation, because Braze's own competitive frame
> is "none of our competitors offer a comparable comprehensive solution" — they are arguing
> they are broader than the suites. The buyer's frame includes a second, different question:
> *is this better than a focused specialist at the one thing I actually need?* Those require
> different answers. A briefing assembled only from Braze's own comparison pages prepares
> you beautifully for the first conversation and walks you straight into the second.

> Two things in Braze's favour from the same source, and I want them said with the same
> weight as the criticism.

> **First**, where Gartner's reviewers rate Braze above the two largest alternatives, they
> name the same things twice: service and support, and ease of integration and deployment —
> with evaluation and contracting added against Salesforce. That is independent,
> buyer-sourced, and consistent: Braze is easier to buy from and easier to deploy than Adobe
> or Salesforce. If we are going to quote Gartner when it helps us, we quote it here too.

> **Second**, three of their four names are on the buyer list. This is a company that
> understands its own market. Anyone hoping to find that Braze is confused about who it
> competes with should stop looking; the evidence says the opposite.

> The practical use of this slide is a shortlist, not a scoreboard. In an active deal, the
> five specialists are who else is in the room — and their presence tells you the buyer is
> weighing depth against breadth, which is the axis to prepare for.


## Part II — The product

*One campaign through seven stages, then the platform around it.*

**Deeper:** `deck/record/04-platform.md`, `05-channels.md`, `06-ai.md`.

### 18 · Part II: The product
Part II — **The product**

**On screen**

- `01` One campaign, seven stages, end to end
- `02` Where the limits are — in their words, not ours
- `03` Which channel has no middleman
- `04` What the AI actually is, on five lenses

*Their technical documentation unless marked otherwise*

- `01` **Data**
- `02` **Identity**
- `03` **Decisioning**
- `04` **Building**
- `05` **Content**
- `06` **Delivery**
- `07` **Interaction**

**Say**

> Part two is the product, and we walk one campaign through seven stages: data arrives, a
> profile updates, a segment recomputes, a journey triggers, content is composed, a message
> is delivered, a response comes back.

> I do it this way for two reasons. It forces every capability claim to attach to a moment
> you would actually notice as a customer, rather than sitting in a feature list. And it
> makes the weak points locate themselves — **the two stages I have highlighted, data in
> and delivery out, are where everything interesting turned out to be**, and they are the
> first and last thing that happens.

> The source for almost all of it is Braze's own technical documentation: 1,352 pages,
> read and indexed rather than skimmed. That matters because documentation is written to
> stop support tickets, not to win deals, so it admits limits that no marketing page
> will — and every hard limit in this deck came out of it.

> Be fair to them as we go. Stages three, four and five are good, reviewers say so, and I
> will say so too.

### 19 · How one campaign works
The whole thing · end to end — **One campaign, end to end**

**On screen**

- `01` **Data arrives** — from an app, an API, or a data warehouse
- `02` **Profile updated** — one record per person — billed per change
- `03` **Segment recomputed** — membership changes as data lands
- `04` **Journey triggers** — Braze calls this Canvas; it decides who continues
- `05` **Content composed** — the message is filled in for that person
- `06` **Message delivered** — email and SMS via named third parties
- `07` **Response logged** — and it flows back to step 1

Seven stages, and the two picked out are the ones worth arguing about: how fresh the data is going in, and who physically sends the message going out. **Everything between them is competent, so a pitch that attacks the middle will not land — aim at the ends.**

**Say**

> This is the loop. Data arrives, the profile updates, segments recompute, the journey
> decides, content is composed, the message goes out, the response comes back.

> I want to be fair before I am critical: **stages three, four and five are good.** Canvas
> is the most documented thing in the platform after email, reviewers praise it, and
> nothing I found contradicts that.

> The interesting evidence is at the two ends. **Stage one** — how fresh is the data,
> really. And **stage six** — who actually sends the message, which their sub-processor
> disclosure has to tell you.

> Note stage two as well: the profile update is the thing you are billed for.

### 20 · How data moves
Data · in, and back out — **The way in is not the way out**

**On screen**

- **60,000*/min*** — ingest — */users/track*, at 75 objects each
- **250*/min*** — read profiles back by identifier, at 50 ids each
- **250,000*/hr*** — bulk export to cloud storage

***STATE THIS FAIRLY — IT IS NOT A LOCK-IN STORY***

- **The asymmetry is real** — Writing reaches ~4.5m objects a minute. Reading profiles back reaches ~12,500 for a customer who joined after August 2024
- **But they are different operations** — Event objects versus whole profiles. The ratio shows where priority sits, not like-for-like throughput
- **And bulk export exists** — Segment export to cloud storage sits under a 250,000/hour limit. The sanctioned bulk route is generous

**So getting off Braze is a project, not a setting.** Price the migration work into any switching conversation, and make the bulk route — not the profile API — the plan.

**Say**

> Data in, data out.

> Ingest is generous — sixty thousand requests a minute at seventy-five objects each, so
> roughly four and a half million objects a minute.

> Reading profiles back **by identifier** is two hundred and fifty requests a minute at
> fifty identifiers each. About twelve and a half thousand profiles.

> Now — I could stand here and tell you that is a three-hundred-to-one lock-in ratio. It
> would land well and it would be wrong, so I am not going to.

> They are different operations, and **bulk export exists and is generously limited**. If
> you want your data out in volume, the sanctioned route works.

> The interesting thing is not the ratio. It is the two hundred and fifty, and where it
> came from — which is the next slide.

### 21 · Stage 1: Data
Stage 1 · data and freshness — **Their words: three of four are not real-time**

**On screen**

*Diagram:* Warehouse sync · their Cloud Data Ingestion · “Not real-time” · 15 min floor · Warehouse segments · read in place, no copy · “Not real-time” · Warehouse triggers · warehouse starts a journey · “Not real-time” · 15 min floor · /users/track · SDKs · app, server, stream · “Near-real-time” · Braze user profile · one record per person · billed per change

Warehouse syncs run “from every 15 minutes to once per month”. Going faster is not self-serve: *“contact your customer success manager or use REST API ingestion.”* **If your customer data lives in a warehouse, fifteen minutes is the floor.**

**Say**

> Here is the slide six callback.

> Braze publishes a comparison of its four ingestion paths and **grades the latency of each
> one itself**. Three of the four carry the words "not real-time". The fourth says
> "near-real-time, async processing".

> This is not me characterising their product. This is their table, redrawn.

> Look at what the diagram makes obvious that a list does not: **all four lanes end in the
> same place.** The same user profile, the same MongoDB store, billed the same way per
> attribute. What differs is only how long the data waits before it gets there — and for
> three of the four lanes the answer is a scheduled job with a fifteen-minute floor.

> That shared destination is the reason the distinction is worth your attention rather than
> being a technicality. If the four paths ended in four different systems you would expect
> four different latencies and think nothing of it. They do not. It is one profile store,
> one billing meter, one segmentation engine reading from it — and the freshness of what
> that engine sees depends entirely on which door your data came through. Two customers on
> identical contracts can get materially different behaviour out of the same product.

> And the practical sentence for a prospect: **if your customer data lives in a warehouse,
> fifteen minutes is the floor** — and going faster is not something you can switch on. You
> have to call your customer success manager, or re-plumb onto the API. That second option
> is not a configuration change; it is an engineering project, and it moves the work from
> Braze's side of the boundary to yours. Worth pricing that honestly when you compare: the
> comparison is not licence against licence, it is licence-plus-integration-work against
> licence.

> Now the fairness, and I want it in the same breath rather than as a footnote. **Braze
> published this table themselves.** They did not have to grade their own ingestion paths
> and they did it in plain words. The SDK and API path genuinely is near-real-time, and the
> qualifier they attach to it — async processing — is more honest than most of this
> category manages. Nothing here is a false claim, and if I present it as one I will be
> corrected in the room and deserve to be.

> What is true is that one word is covering two architectures. So the question is not "is
> it real-time", because they will say yes and they will be right. The question is
> **which path will my data take, and what is the latency on that path** — and the answer
> is in their own documentation before the meeting starts. We come back to this on the
> deep-dive slide, because it turned out to be the single most useful question this whole
> project produced.

### 22 · Stage 2: Identity
Stage 2 · identity — **A merge can fail and still return success**

**On screen**

- **unlimited** — aliases per profile
- **1** — alias per label — unique across the base
- **5** — identifier types accepted on ingest
- **1** — identifier type for warehouse segments

- **A merge can decline and still report success** — “If both profiles have invalid phone numbers, Braze does not merge them … **The endpoint still returns 202 Accepted with a success message.**”
- **Reporting splits after a merge** — The dashboard attributes a pre-merge send to the surviving profile. Currents — their paid data-export feed — attributes it to the orphaned one. Both are right by their own rules, and they disagree.

**So an engineering team should test a merge failure on day one** — send two profiles with bad phone numbers and check the profile, not the response code.

**Say**

> Identity is generous at the top and narrow at the bottom. Unlimited aliases on a
> profile — but a warehouse-driven segment can only be built on **one** identifier type,
> where ingestion accepts five.

> Then two behaviours from their own documentation that no marketing page will tell you,
> and both fail quietly.

> **A merge can decline and still tell you it worked.** If both profiles have invalid
> phone numbers, Braze skips the merge — and returns two-oh-two Accepted with a success
> message. Their words: the response "does not indicate that the merge was skipped."

> **And reporting splits after a merge.** The dashboard attributes a send one way; Currents
> and Query Builder attribute it the other. If you are joining Braze data to a warehouse,
> that is a reconciliation problem you will find at month end rather than at integration
> time.

### 23 · Stage 3: Decisioning
Stage 3 · decisioning — **Deciding who gets a message**

**On screen**

**Two systems decide who gets a message, and they sit on two different databases that do not talk to each other.** One follows rules you write; the other runs models.

***RULE-BASED — MONGODB***

- **Segmentation** — Custom events, attributes and most targeting
- **Segment Extensions** — SQL, but served from Snowflake
- **Global Control Group** — Holdouts — people left un-messaged, to measure lift

***MODEL-BASED — SNOWFLAKE***

- **Predictive Suite** — Churn and event prediction
- **AI item recommendations** — Snowflake-backed
- **Decisioning Studio** — Was OfferFit until June 2025

Braze flags the consequence itself: “Removing data from one system does not automatically remove it from the other.” **So deleting bad data means deleting it twice** — and a deletion request that only clears one side is a compliance problem, not a tidiness one.

**Say**

> Decisioning runs on two engines sitting on two different databases, and Braze publishes
> which is which.

> Rules and segmentation run on MongoDB. The model-driven things — Predictive Suite,
> recommendations, Decisioning Studio — run on Snowflake.

> That is a sensible architecture and I am not criticising it. But it has a consequence
> they flag themselves, under an "important" callout: **removing data from one system does
> not automatically remove it from the other.**

> If you have deletion obligations — and if you are in this category you do — that is a
> two-system problem, disclosed in their own documentation and in none of their marketing.

> Note the seven documentation pages on Predictive Suite. Hold that for slide thirty-two.

### 24 · Stage 4: Building
Stage 4 · building a journey — **Canvas is the strongest thing in the platform**

**On screen**

- **249** — focused documentation pages on Canvas
- **10** — Canvas API endpoints
- **385** — G2 reviews tagged ‘Ease of Use’
- **139** — tagged ‘Learning Curve’

> “Canvas makes it easy to build complex, branching lifecycle flows … Being able to trigger contextual push notifications, in-app messages, and emails from live event streams — **without needing engineering for every small tweak** — is a huge win.”
> — *Enterprise IT manager, G2 · 5/5 · August 2026*

**So do not attack Canvas.** It is the thing their customers like most, and a pitch that calls it weak will be contradicted by the room.

**Say**

> This is the slide where I tell you what is good, because an analysis that only finds
> problems was not an analysis.

> **Canvas is the strongest thing in this platform.** Two hundred and forty-nine focused
> documentation pages, ten API endpoints, and reviewers consistently praise it. The single
> most common positive tag on G2, three hundred and eighty-five times, is ease of use.

> The quote is from a five-star enterprise review and it names the thing that actually
> matters commercially: marketers can change journeys **without engineering**. That is the
> core of the value proposition and the evidence supports it.

> The counterweight is on the same slide and it is real: a hundred and thirty-nine reviews
> tag learning curve, eighty-six say steep learning curve. Easy once you know it; not easy
> to learn.

### 25 · Stage 5: Content
Stage 5 · content and personalisation — **Composing the message**

**On screen**

- **123** — focused doc pages on Liquid templating
- **43** — on Connected Content
- **38** — on Content Blocks
- **78** — on Catalogs

- **What it gives you** — Liquid templating, Connected Content for live API calls at send time, reusable Content Blocks, and product catalogs for item-level personalisation.
- **What reviewers say about it** — “Liquid personalization and Connected Content also make it straightforward to scale truly dynamic messaging” — and, from the same reviewer, “a challenging learning curve around Liquid syntax” for non-technical users.

**So ask who writes the messages.** If the answer is marketers rather than engineers, the learning curve is a real cost and it lands on the team you are selling to.

**Say**

> Content is Liquid — the templating language — plus Connected Content for live API calls
> at send time, Content Blocks for reuse, and catalogs for item-level personalisation.

> A hundred and twenty-three focused pages on Liquid alone. This is a serious
> personalisation layer and it is well documented.

> And the same reviewer who praises it names the cost in the same breath: **a challenging
> learning curve around Liquid syntax for non-technical users.**

> That is the honest shape of this product generally, and it comes up again and again in
> the review corpus. Very capable in the hands of someone technical. Harder than the
> marketing suggests for the marketer it is sold to.

### 26 · Stage 6: Delivery
Stage 6 · delivery — **Only two channels have a named middleman**

**On screen**

***CHANNELS WITH A NAMED DELIVERY SUB-PROCESSOR***

- **Email — three of them** — Amazon SES · Bird.com (SparkPost) · Twilio (SendGrid). Plus Mailgun for previewing
- **SMS / mobile messages — two** — Infobip · Twilio

***CHANNELS WITH NONE NAMED***

- Push · In-app · Content Cards · Banners · Webhooks · WhatsApp · LINE · KakaoTalk · Landing pages · Live notif.

Absence is not proof of no intermediary — APNs, FCM and the WhatsApp, LINE and Kakao business APIs may sit outside the definition. **So a buyer cannot establish from this document who touches their messages on eleven of thirteen channels.** That is a question to put to them, not a gap to assume the worst about — and on email, three interchangeable senders is deliberate redundancy.

**Say**

> This is the slide that only exists because they are legally obliged to publish it.

> The sub-processor disclosure — revision first of June this year — names seventeen third
> parties. For delivery, it names middlemen on exactly two channels. **Email has three.
> SMS has two. Everything else has none named.**

> Now, the caveat matters and I am putting it on the slide rather than hiding it in the
> notes: absence from a sub-processor list is not proof there is no intermediary. Apple's
> and Google's push transports, and the WhatsApp and LINE business APIs, may simply sit
> outside the definition.

> What you *can* take away is the email arrangement, and it is a point in Braze's favour:
> **three interchangeable delivery providers on their highest-volume channel.** If you were
> hoping email deliverability was a single point of failure you could attack, it is not.

### 27 · Stage 7: Interaction
Stage 7 · interaction and the loop back — **When the customer replies**

**On screen**

- **71** — focused doc pages on Webhooks
- **5 min** — Currents export cadence — or every 15,000 events
- **add-on** — Currents is “an optional Braze add-on”
- **free** — engagement events are not billed as data points

Inbound and two-way handling is real: webhooks are a first-class documented channel, and engagement tracking — opens, clicks, push receipts — is excluded from data-point billing.

***WEBHOOKS IS THE MOST UNDER-SOLD THING IN THE PLATFORM***

- **Fifth-deepest channel in the product** — 71 focused pages — behind only email, in-app, SMS and push, and sold under no name at all.
- **Which cuts both ways for us** — A real integration surface we should not pretend is absent — and one their own sellers are least likely to lead with.

**So the round trip costs more than the outbound leg.** Getting the raw stream back is a paid add-on on a five-minute cadence — budget for it when you compare list prices.

**Say**

> The loop closes. Responses come back as engagement events, and here Braze does something
> genuinely customer-friendly: **engagement tracking is free.** Opens, clicks, push
> receipts — none of it counts against your data points. Say that when you are being fair
> about their pricing.

> But look at the third figure. Getting the **raw** event stream back out means Currents,
> and Currents is — their word — "an optional Braze add-on". It exports every five minutes,
> or every fifteen thousand events.

> Connect that to slide fourteen. Thirty-six per cent of TrustRadius reviewers call
> reporting limited and unintuitive. A G2 reviewer says out-of-the-box reporting "feels too
> basic unless you export raw data through paid add-ons like Currents."

> **The complaint and the mechanism are two independent sources describing the same
> thing.** That is when you can be confident it is real.

### 28 · Channels
Channels · counted from both ends — **Thirteen documented. Ten marketed.**

**On screen**

***DEEP — FOCUSED DOCUMENTATION PAGES***

- Email · **347**
- In-app messages · **115**
- SMS / MMS / RCS · **89**
- Push · **73**
- Webhooks · **71**
- WhatsApp · **56**
- Content Cards · **47**

***THIN — REAL, BUT NOT COMPARABLE***

- Banners · **28**
- Landing pages · **21**
- LINE · **11**
- Web push · **11**
- Live notifications · **8**
- KakaoTalk · **5**
- Transactional email · **4**

Thirteen channels is broad — broader than several specialists on slide 17. But **three are the product and ten are completeness**: email alone outweighs the next three combined. **So compete on the thin ones.** A prospect buying for KakaoTalk or LINE is buying five and eleven pages of documentation, not the platform email buyers get. One line on the drift: five of these ship with no marketing page, and Webhooks — fifth deepest — is one of them.

**Say**

> Thirteen channels are documented. That is broad, not narrow — I went in expecting the
> opposite and the evidence killed it.

> What is interesting is the drift, and it runs in both directions at once.

> **Five documented channels have no marketing page anywhere.** The biggest is landing
> pages — eleven user-guide pages plus three partner pages. A real capability that is sold
> under no name.

> **And one marketed channel is missing from their own documentation index.** KakaoTalk has
> four doc pages and a product page, and their channels index mentions it zero times.

> Neither of those is damning. Together they tell you something useful about how the
> company runs: **the documentation and the marketing are maintained by people who are not
> talking to each other**, which is exactly the seam this whole method looks for.

### 29 · Integrations
Integrations · the Alloys network — **Wide network, one page deep**

**On screen**

- **150+** — technology partners — their claim
- **322** — partner documentation pages
- **~810** — average words per partner page
- **~2,708** — average words per developer-guide page

The network is real and wide, but its documentation is **second-largest by page count and close to thinnest by words per page** — one short entry per partner. **So treat 150+ as a directory, not a depth claim: test the two integrations you actually need before believing it.**

- **What is bought** — Delivery (Twilio, Infobip, SendGrid, SparkPost, SES), warehousing (Snowflake, Databricks, BigQuery), models (Anthropic, OpenAI, Google) — all from the sub-processor list
- **What is built** — The ingestion layer, Canvas, Liquid, the identity model, Currents, and the integration surface itself

**Say**

> Braze claims over a hundred and fifty technology partners, which they call Alloys.
> That is their number and I have graded it as a claim.

> What I can measure is the documentation. **Three hundred and twenty-two partner pages —
> the second largest section in the corpus — averaging about eight hundred and ten words
> each.** The developer guide is a third the size and averages more than three times the
> words per page.

> That is the shape of a broad network documented at one short page per partner. Wide, and
> shallow in documentation terms. Which is not a criticism — it may be all a connector
> needs — but if you are being told the integration layer is deep, this is the measurement
> that tests it.

> Underneath: the delivery, the warehouses and the models are all bought. The ingestion
> layer, Canvas, Liquid and the identity model are built.

### 30 · Infrastructure
Infrastructure · the status page as a disclosure — **Fifteen clusters, seven subsystems — and one exception**

**On screen**

*Diagram:* US ×9 · EU ×2 · JP 01 · KR 01 · ID 01 · AU 01
15 clusters, 6 territories
7 identical subsystems in every one
one of the nine US clusters is the exception — slide 35

***THE SEVEN SUBSYSTEMS, IDENTICAL IN EVERY CLUSTER***

- Dashboard · SDK Data Collection · Data Processing · REST APIs · Outbound Messaging · Currents · Cloud Data-Ingestion

The sub-processor disclosure lists AWS regions for the same six territories. **So data residency is available in six places and nowhere else — ask which cluster before the contract.**

**Say**

> The status page is an architecture disclosure Braze made by accident.

> Fifteen regional clusters across six territories, and every one exposes the same seven
> subsystems. That is a functional decomposition of the entire product, published live and
> updated during outages. Notice that Currents and Cloud Data Ingestion appear as
> first-class subsystems rather than as features — which tells you they can fail
> independently, and the incident record on slide 39 shows they do.

> The geography checks out against a completely unrelated document: the sub-processor
> disclosure lists AWS regions for the same six territories. Two sources, no relationship
> between them, same answer.

> For a buyer with data-residency obligations this map is the answer to the question they
> actually have. Not "do you support the EU" — everyone says yes — but "which of your
> clusters would my data sit in, and what else is in that cluster". Fifteen named clusters
> is a real answer.

> Two things to hold. There is no US 09 — they run one to eight, then ten. I do not know
> why, and I am not going to invent a reason.

> And US 08 is marked differently, because that is the next part.

### 31 · Analytics
Analytics · what you can measure — **What you can measure**

**On screen**

- **36%** — of recent TrustRadius reviewers call reporting limited and unintuitive
- **140** — G2 reviews tagged ‘Missing Features’
- **27** — focused doc pages on the Global Control Group
- **2am ET** — when your billing dashboard refreshes — daily, cached

- **What is genuinely there** — Holdouts and a Global Control Group for incrementality, campaign and KPI endpoints, and a Snowflake data share that avoids copying data at all.
- **What reviewers keep hitting** — “The out-of-the-box reporting still feels too basic unless you export raw data through paid add-ons like Currents.”

**So ask a prospect what they report on today, and who builds it.** If the answer involves exporting to a warehouse, they are already paying for the add-on that fixes this.

**Say**

> Analytics is where the review corpus is most consistent, across panels that have nothing
> to do with each other.

> To be fair first: incrementality measurement is properly supported — holdouts, a global
> control group, twenty-seven focused pages on it. There are analytics endpoints. And the
> Snowflake data share lets you query without copying data at all, which is genuinely good
> engineering.

> But thirty-six per cent of recent TrustRadius reviewers call reporting limited and
> unintuitive, and G2's most common criticism tag is missing features.

> And the mechanism is the one we saw at stage seven: the fix is a paid add-on.

> One small detail I enjoyed, because it is so specific: **your data-point usage dashboard
> — the thing that tells you what you are spending — is cached and refreshes once a day
> around 2am Eastern.** The billing meter is not real-time either.

### 32 · The AI, honestly
The AI · five independent lenses — **Bought recently, running on other people’s models**

**On screen**

- `2011–` **The platform** — segmentation, journeys, Liquid — a decade of it
- `Jun 2025` **The engine, bought** — OfferFit, $303.2m, renamed Decisioning Studio
- `Now` **The models, rented** — Anthropic, OpenAI and Google, named in their own disclosure

***AND WHAT EACH LAYER MEASURES — FOCUSED DOC PAGES***

- Email · **347**
- Canvas · **249**
- Segmentation · **242**
- Recommendations · **73**
- Decisioning Studio · **22**
- Agents · **17**
- Predictive Suite · **7**

***LENSES 2–5***

- **0 of 135 API endpoints** — 28 namespaces, none of them AI or decisioning
- **Reviewers name copywriting** — Two G2 reviewers say the AI copy needs “a careful human hand”
- **So the useful question is one line** — “Can I call your AI from my own systems?” Today the documented answer is no — which is what a data-science team needs to hear before they plan around it

**Say**

> This is the slide most likely to go wrong, so I am going to be careful.

> **I am not going to tell you their AI is thin.** That sentence is unfalsifiable and the
> evidence does not need it.

> Here is what five independent lenses say instead.

> **Documentation.** Predictive Suite has seven focused pages. Agents seventeen.
> Decisioning Studio twenty-two. Canvas has two hundred and forty-nine. "Focused" means the
> page is about the thing rather than mentioning it.

> **The API.** Of a hundred and thirty-five published endpoints across twenty-eight
> namespaces, the number in an AI, prediction, agent or decisioning namespace is **zero**.

> **The models.** Anthropic, OpenAI and Google — named in their own compelled disclosure.

> **The engine.** Bought, June 2025, three hundred and three million dollars.

> **And customers.** Reviewers talk about AI copywriting, and two of them independently say
> it needs a human pass. Nobody in the sample mentions decisioning at all.

> Now the caveats, because a documentation count is easy to over-read and I would rather
> raise the objection than be handed it. **A new product is under-documented by
> construction.** Decisioning Studio is fifteen months old inside Braze; Canvas has had a
> decade. And **some things are genuinely short to document** — Intelligent Timing is a
> toggle with a model behind it. So read these as *surface area*, which is what they
> measure, and not as a verdict on quality, which they cannot.

> Lens two is the one I would actually put in front of a technical buyer, because it has
> consequences they will hit. No AI namespace means the AI features cannot be orchestrated
> from outside the product: you cannot trigger a prediction, retrieve a recommendation or
> configure an agent programmatically. They cannot be tested in a CI pipeline the way a
> campaign trigger can. And they cannot be composed with the customer's own models. For an
> organisation that already runs data science, that is the difference between a platform
> capability and a black box.

> On the models, the fair framing matters. Using foundation models from suppliers is
> ordinary — almost nobody trains their own, and three rather than one is a sensible hedge.
> What is unusual is only that Braze is legally obliged to name them. So the narrow, firm
> claim is this: **any suggestion that Braze's AI is proprietary at the model layer is
> contradicted by Braze's own compelled disclosure.** What *is* proprietary is the
> integration, the data model the models see, and the decisioning logic they paid three
> hundred million for — a real asset, and I am not diminishing it.

> So the defensible sentence is: real, shipping, recently and largely acquired, running on
> three named suppliers' models, with no API of its own, documented at a fraction of the
> depth of the established platform. Every clause sourced separately, from a different kind
> of source, and no clause leaning on another.

> What it does not support is "their AI is thin". That sentence is unfalsifiable, the
> evidence does not need it, and the first prospect who opens the product and sees a working
> decisioning engine will disprove it for us. The sourced version survives that
> demonstration. And the genuinely useful question, which falls straight out of lens two, is
> one line: **can I call your AI from my own systems?** Today the documented answer is no.


## Part III — Strategy

*Where the money goes, what is coming, what protects them.*

**Deeper:** `deck/record/02-money.md` §2.3–2.4, `04-platform.md` §4.5.

### 33 · Part III: Strategy
Part III — **Strategy**

**On screen**

- `01` Where seven years of revenue actually went
- `02` What is provisioned that has not been announced
- `03` What would survive a competitor doing the same thing

*Audited, except where marked*

**Say**

> Part three. Three slides only, and the restraint is deliberate.

> The SEC data here is abundant, tidy and free, and it will happily eat a whole deck. Seven
> years of audited operating expense, quarterly cash flow, remaining performance obligation,
> a compensation plan with published targets — all of it interesting, and most of it beside
> the point. **You are deciding about a product and a competitor, not about a share
> price.** So the money gets one slide, what is coming gets one, and the last one is the
> argument about what would actually survive us competing hard.

> Watch the second of the three. It is the finding nobody else in this market will have,
> and it is also the one I am most careful about — three unrelated sources agreeing, stated
> as observations and deliberately not as a conclusion.

> And the third slide is the one to argue with. It names what protects Braze *and* what does
> not, and if you disagree with either list, that is the conversation worth having today.

### 34 · Where the money goes
Seven audited years · where revenue goes — **Decelerating and getting more efficient at once**

**On screen**

***SALES & MARKETING AS A SHARE OF REVENUE***

- FY2020 · **59.5%**
- FY2022 · **53.4%**
- FY2023 · **56.7%**
- FY2024 · **52.4%**
- FY2025 · **47.6%**
- FY2026 · **44.3%**

***REVENUE GROWTH OVER THE SAME YEARS***

- FY2021 · **55.9%**
- FY2022 · **58.5%**
- FY2023 · **49.3%**
- FY2024 · **32.7%**
- FY2025 · **25.8%**
- FY2026 · **24.4%**

The expectation was decelerating growth *propped up by* sales spend. The evidence says the opposite: **S&M fell more than twelve points as a share of revenue since FY2023 while growth halved**, and operating cash flow has been positive and rising since FY2024. **So do not plan around them running out of money, or buying growth back.** They can fund a price fight, and the loss line will not stop them.

**Say**

> Seven audited years of where the money goes, and this slide killed the hypothesis I
> wrote before I read anything.

> I expected decelerating growth propped up by ever-more sales spend. That is the usual
> pattern and it is the easy story.

> **The evidence says the opposite.** Sales and marketing has fallen from fifty-seven per
> cent of revenue to forty-four — the lowest in the series — while growth halved. They are
> decelerating *and* getting more efficient at the same time.

> And operating cash flow turned positive in FY2024 and has grown every year since, to
> seventy-one million.

> So if you are planning to compete with Braze on the assumption that they are burning
> money to buy growth and will have to stop: **that assumption is wrong**, and the audited
> numbers say so.

> The counterweight, in fairness: share-based compensation has now exceeded the entire net
> loss for two years running, and diluted shares are up fourteen per cent in three years.
> The loss is real; it is mostly equity, and shareholders are carrying it.

### 35 · What comes next
Unannounced · three sources, one answer — **One instance is not on the same cloud**

**On screen**

- **1 · Two company documents** — The sub-processor list names **Amazon and Google**. The 10-K names **Amazon and Rackspace**. **Neither names Microsoft.**
- **2 · Their own documentation** — Every address Braze lists for **US-08 is registered to Microsoft**. Every other instance is Amazon. Checked against ARIN.
- **3 · Certificate transparency** — 50 hosts sit on aze region codes matching no AWS identifier, where every other code does — including sdk-us08.

***HOW TO SAY THIS — AND HOW NOT TO***

A hosting arrangement may sit outside a sub-processor listing for reasons not visible from outside, and saying they failed to disclose would be a legal conclusion this evidence does not support. **So put it to them as a question: which entity operates my instance?**

**Say**

> This is the finding nobody else in your market will have, and it is also the one I am
> most careful about.

> Three sources that have nothing to do with each other.

> **One.** Their sub-processor disclosure — legally compelled to be complete, revised in
> June — names two hosting providers. Amazon and Google. Microsoft appears nowhere in it.

> **Two.** Their own documentation publishes the IP addresses you must allowlist for each
> instance. Every address for US-08 is registered to **Microsoft Corporation**. Every
> address for every other instance is Amazon. I checked all of them against ARIN's registry
> rather than recognising ranges by eye, and that lookup is saved in the repository.

> **Three.** Certificate transparency — the public log every issued TLS certificate lands
> in, which nobody at Braze curates — shows fifty hosts on region codes p-aze-us, s-aze-us
> and d-aze-us. Every other region code in that set maps to an AWS region identifier. These
> three map to none. And the hostnames sitting on them include sdk-us08 and subcenter-08.

> Why the triangulation is the point, rather than any one of the three. Each source on its
> own has an innocent explanation. A sub-processor list can lag a change. An IP registry
> lookup can catch a transitional address. A certificate naming convention can mean nothing
> at all. What is hard to explain away is that three sources with **no relationship to each
> other** — a compelled legal disclosure, a customer-facing allowlist, and a public
> cryptographic log — all point at the same instance, and only at that instance. That is the
> shape of a real finding rather than an artefact, and it is why this one is on a slide.

> One word on method, because someone will ask. I did not recognise IP ranges by eye — every
> address Braze publishes for every instance was resolved against ARIN's registry, and the
> raw lookups are in the repository to re-run. Recognising ranges by sight is how people get
> this wrong, and getting this one wrong would be expensive.

> Now the discipline, and it is the most important sentence on the slide. **I am not telling
> you Braze failed to disclose something.** That is a legal conclusion and this evidence
> does not support it. A hosting arrangement may sit outside a sub-processor listing for
> reasons that are entirely proper and simply not visible from where we are standing — a
> different contracting entity, a category that does not process personal data, a
> transitional arrangement. I do not know, and neither does anyone in this room.

> What I am telling you is narrower and still valuable: **three unrelated sources agree that
> one instance runs somewhere the disclosure does not mention.** State those three
> observations and stop.

> And that restraint is the commercially useful move, not a hedge. If we assert
> non-disclosure, we have made a claim about their compliance that they can rebut in one
> sentence, and we lose everything else in this deck along with it. If we hand a prospect
> three sourced observations and let them ask, the question lands with the only people who
> can answer it. **The question is for them; it is not a conclusion for us.** It is also, on
> my reckoning, the highest-value single answer available in this whole analysis, which is
> why it is the first thing on the next-steps slide.

### 36 · What protects them
Defensibility · the so-what test — **Three things a competitor cannot copy**

**On screen**

- **Contracted revenue, not pipeline** — **$1,033.0m of remaining performance obligation** — 1.40× current revenue, already signed. You cannot displace what is not up for renewal. This is the strongest of the three.
- **Ten years of streaming plumbing** — MongoDB, Snowflake, Kafka and Redis under fifteen clusters, with a decade of incidents to show it holds. Copyable in principle; slow in practice.
- **Marketer independence from engineering** — The thing reviewers actually praise: changing a journey without filing a ticket. That is a workflow habit, and habits are stickier than features.

***AND WHAT DOES NOT PROTECT THEM***

- **The AI** — Bought for $303.2m, running on models anyone can rent, with no API of its own. A feature race, not a moat.
- **The channel roster** — Broad and well built — and matched by several of the five specialists buyers shortlist them against but they never name.

**Say**

> What actually protects them, under the "so what would a competitor do about it" test.

> **The strongest thing is the least exciting.** A billion dollars of contracted,
> unrecognised revenue at one point four times current revenue. You cannot displace an
> account that is not up for renewal. That is a real moat and it is measured, not asserted.

> **Second, the plumbing.** A decade of streaming infrastructure across fifteen clusters,
> with a public incident record showing it holds. Copyable in principle. Slow and expensive
> in practice.

> **Third, and most underrated: the habit.** Marketers who can change a journey without
> filing an engineering ticket do not want to go back. That is stickier than any feature.

> And what does *not* protect them. **The AI does not.** It was bought, it runs on three
> suppliers' models that anyone can buy, and it has no API surface. That is a feature race.

> If I were briefing a sales team, I would say: do not attack the AI, attack the renewal
> calendar and the reporting.


## Part IV — Open questions

*What is unresolved, what went the other way, and what to do next.*

**Deeper:** `deck/record/08-open.md` — the open questions, the corrections log, the hypothesis ledger.

### 37 · Part IV: Open questions
Part IV — **Open questions**

**On screen**

- `01` One hard question, answered properly
- `02` A decade of reliability, measured rather than claimed
- `03` The hypotheses that died in Braze’s favour
- `04` What public sources could not answer, and what would close it
- `05` What to remember

*Where the evidence runs out, this says so*

**Say**

> Part four is the part most competitor decks do not have, and it is the reason to trust
> the other three.

> One hard question answered properly. A decade of reliability, measured rather than
> claimed. The three hypotheses that died in Braze's favour — because we wrote ten of them
> down before reading anything, and four came back wrong. Then an honest account of where
> the public record ran out, and a prioritised list of what to do about it.

> That last part is not a disclaimer and I would not present it apologetically. **A gap you
> have written down is evidence. A gap you have not written down is a mistake** — and the
> difference is that the first one tells the next person exactly where to dig.

> One of those gaps closed while this deck was being built, from the source the entry itself
> had named. That is what a well-written backlog does.

### 38 · Deep dive: how real-time is it
Deep dive — **“Is it real-time?” — answered properly**

**On screen**

- `ASK` **Which path?** — The answer differs by a factor of hundreds
- `SDK / API` **Near-real-time** — Their words, with ‘async processing’ attached
- `WAREHOUSE` **15 minutes, floor** — “Not real-time”, three times over
- `FASTER?` **Not self-serve** — “Contact your customer success manager”
- `EXPORT` **5 minutes** — And Currents is a paid add-on

- **Why this is the question that matters** — Most enterprise buyers keep customer data in a warehouse. For them the honest answer is fifteen minutes, and it is not a setting they can change.
- **Why it is not a gotcha** — Braze publishes this table themselves, and the SDK path genuinely is near-real-time. One word, two architectures — not a false claim.
- **What to actually ask them** — “Which ingestion path will *my* data take, and what is the latency on it?” **The answer is in their own documentation before the meeting.**

**Say**

> The deep dive. I picked this after the research, from what turned out to be both
> contested and answerable.

> Every vendor in this category says real-time. The question is what it means, and for
> Braze the answer differs by a factor of hundreds depending on which path your data takes.

> **SDK and API: near-real-time.** True, and their own qualifier — async processing — is
> honest.

> **Warehouse: fifteen minutes, and that is a floor.** Labelled "not real-time" three
> separate times in their own comparison table. And going faster is not a setting. It is a
> conversation with your customer success manager.

> Then note the last box, because it closes the loop in a way people miss: even getting the
> data back **out** runs on a five-minute cadence, through Currents, which is a paid add-on.
> So the round trip — warehouse in, decision made, event exported to your systems — is
> bounded at the slow end by a scheduled job and at the fast end by a line item.

> Why this is the question that matters, rather than one of a dozen. Most enterprise buyers
> in this category keep their customer data in a warehouse. That is where the CRM extract
> lands, where the transaction history lives, where the analytics team works. For those
> buyers — and they are the ones we compete for — the honest answer to "how fresh is my
> data in Braze" is fifteen minutes, and it is not a setting they can change. The buyer who
> gets the near-real-time answer is the buyer already sending events from their app through
> Braze's SDK, which is a different architecture and often a different company.

> Now — this is not a gotcha, and I would not present it as one in front of them. **Braze
> publishes this table themselves.** They graded their own ingestion paths, in their own
> words, and they did not have to. That is the point of the whole method rather than an
> aside: **a vendor's documentation is more honest than anyone's marketing, including their
> own**, because it is written by people whose job is to stop support tickets rather than to
> win deals.

> Which is also why this survives contact with them. If I stand up and say "Braze is not
> real-time", their solutions engineer opens the product, shows an event landing in seconds
> from the SDK, and I have lost the room and every other finding in the deck with it. If I
> say "three of your four documented ingestion paths are labelled not real-time and the
> warehouse floor is fifteen minutes", there is nothing to demonstrate against. It is their
> sentence.

> So the thing to put in a prospect's hand is the third card, and it is one sentence. Not
> "is it real-time" — they will say yes and be right. Ask **which path my data will take,
> and what the latency is on that path.** If the answer is the warehouse, the follow-up is
> what it costs to move to the API path and who does that work. Those two questions do more
> for us than any claim we could make.

### 39 · Reliability, measured
The operational record · a decade of it, public — **A decade of reliability, measured**

**On screen**

- 2019 · **49**
- 2020 · **57**
- 2021 · **48**
- 2022 · **39**
- 2023 · **60**
- 2024 · **43**
- 2025 · **27**
- 2026 to Aug · **35**

- **79 min** — median incident duration
- **29.6%** — of non-maintenance incidents were major or critical
- **63 v 27** — Dashboard incidents vs Outbound Messaging
- **97.3%** — of 845 unsolicited public issues closed — median 11 days
- **9 of 9** — SDK repos shipped within 13 days of capture

**The caveat belongs on the slide, not only in the notes:** 2026 stands at 35 through August, roughly **double the 2025 monthly rate**. One year is not a trend, and none is claimed. And **never compare this to a vendor who publishes nothing.**

**Say**

> A decade of incidents, because they publish a status page and most vendors do not.

> The rate peaked in 2023 at sixty and fell to twenty-seven in 2025 — **the quietest full
> year on record, over a period when revenue grew seven and a half times.** That kills the
> hypothesis I wrote that incidents would rise with scale.

> With the caveat attached, and it is on the slide rather than only in my notes: 2026
> stands at thirty-five through August, roughly double the 2025 monthly rate. One year
> does not make a trend.

> **The Dashboard appears in sixty-three incidents; Outbound Messaging in twenty-seven.**
> The control plane your marketers work in fails more than twice as often as the sending
> path. Messages get out; the console is where you feel the outage.

> Now the two numbers on the right, because an analysis that only found problems was not
> an analysis. **Ninety-seven per cent of eight hundred and forty-five unsolicited public
> issues are closed, median eleven days.** And every one of the nine SDK repositories that
> publishes releases shipped within thirteen days of capture — the platform whose repo is
> archived, Unreal, has had its documentation removed too. **The maintenance record matches
> the marketing**, which is not something I could say about every vendor.

> And the rule at the bottom: **do not compare this against a competitor who publishes
> nothing.** Braze looks worse than a silent vendor purely by being transparent.

### 40 · Where the evidence went their way
The hypotheses that died · in Braze’s favour — **Three things we expected to find, and did not**

**On screen**

- **H1 · “Growth is decelerating while sales spend holds”** — **Killed.** Growth did decelerate — and sales and marketing fell **from 56.7% of revenue to 44.3%** over the same period, its lowest in the seven-year series. Braze is decelerating *and* getting more efficient. Operating cash flow turned positive in FY2024 and has grown every year since.
- **H4 · “Some supported platforms are effectively unmaintained”** — **Killed.** **All nine SDK repositories** that publish releases had shipped within 13 days of capture. The one archived repo, Unreal, has had its documentation removed too — so the marketing and the maintenance record agree. One soft spot: braze-roku-sdk, 181 days idle with 38 Roku doc pages still live.
- **H9 · “Incident rate has risen with scale”** — **Killed.** Incidents peaked at 60 in 2023 and fell to **27 in 2025**, the quietest full year on the status page, while revenue grew 7.7×. Caveat attached: 2026 runs at about double the 2025 monthly rate.

**Slide 2 promised this.** Ten hypotheses were written before any source was read; four came back wrong. A set that all confirmed would have meant they were written to confirm.

**Say**

> I want this slide in the deck more than almost any other, and it is the one that would
> have been cut first.

> Before we read a single source we wrote down ten hypotheses — ten things we expected to
> find — so that afterwards they could be graded rather than quietly dropped. **Four of
> them were killed. Three of those four were killed in Braze's favour.**

> **One.** We expected the familiar late-stage pattern: growth decelerating while sales
> spend holds, a company buying its last few points of growth. The opposite is true. Sales
> and marketing fell more than twelve points as a share of revenue over three years, to the
> lowest in the seven-year series, while growth decelerated. They are decelerating and
> getting more efficient at the same time. That is a harder company to compete with, not an
> easier one.

> **Two.** We expected to find abandoned SDKs — the platform nobody maintains that is still
> on the marketing page. Every one of the nine repositories that publishes releases had
> shipped within thirteen days of when we looked. And the one platform whose repo is
> archived has had its documentation pulled too, so they are not selling something they
> stopped supporting. The single soft spot is Roku, idle six months with the docs still up,
> and that is a small thing.

> **Three.** We expected incidents to have risen with scale, because they usually do. They
> peaked in 2023 and fell to the quietest full year on the status page in 2025, while
> revenue grew seven and a half times. I have put the 2026 caveat on the slide rather than
> in my pocket, because it runs at about double the 2025 rate — but one year is not a
> trend, and I am not going to present it as one.

> Now the reason this matters more than the three findings themselves. **If every
> hypothesis we wrote had confirmed, that would tell you we wrote them to confirm.** The
> value of everything critical in this deck — the real-time finding, the AI provenance, the
> US-08 question — rests on our being willing to say when the evidence went the other way.

> So if someone in the room wants to discount this analysis as a hit piece, this is the
> slide to turn back to. We looked for three specific weaknesses. They were not there, and
> we said so.

### 41 · What we could not answer
The honest residue — **What we could not answer**

**On screen**

- **Does satisfaction fall with customer size?** — The one hypothesis we could not test. **All three review sites paywall that breakdown.** *Closed by:* paid panel access
- **What else is in the certificate estate?** — The host list is **partial** — 833 hosts through a rate-limited fallback. Everything found stands; **nothing is claimed about what is absent**. *Closed by:* an API token
- **Can the customer roster be checked independently?** — The only roster outside the 10-K is **178 self-published stories** — marketing, not a sample. Independent detection was **not attempted**. *Closed by:* tag crawls, or job ads naming Braze in the stack
- **Actual pricing, and why the export limit was cut** — No vendor publishes a rate card, and the 10× cut to the profile-lookup limit is documented without explanation. *Closed by:* a procurement award or a customer contract

**Say**

> Four things I could not answer, stated plainly.

> **The first is the one that annoys me most.** I went in expecting enterprise satisfaction
> to be lower than small-business satisfaction, because it usually is. All three review
> sites paywall exactly that breakdown. Seven of eight hundred and sixty coded records
> carry a customer size. **So the hypothesis is unresolved, not answered** — and I would
> rather tell you that than dress up a proxy as an answer.

> **Second.** The certificate list is partial. crt.sh was down all day and the fallback
> rate-limited. Everything I found is real; I am claiming nothing about what is missing,
> because I did not look exhaustively.

> **Third.** I cannot check their customer roster against anything independent. The only
> list outside the audited count is a hundred and seventy-eight stories they chose to
> publish, which is marketing. Detecting Braze in the wild — tag crawls, certificate
> records, job ads naming it in the stack — was not attempted in this run, and I am
> recording that as a gap rather than pretending the hundred and seventy-eight is a sample.

> **Fourth.** Pricing — as expected — and one specific thing: they cut the profile-lookup
> rate limit tenfold for new customers on a dated boundary and never say why.

> One more thing about this slide, and it is the point of keeping it. **There were five
> gaps here until quite late.** The fifth was the split of open roles by function: the
> careers board's filter would not drive under automation, so it went down as
> uncapturable. Then the same board turned out to be published as JSON with the grouping
> already done, and the answer is now on slide sixteen. The lesson generalises — **when a
> page will not yield, look for the API behind it before you write down a gap** — and it
> is in the corrections log rather than quietly patched.

> All of these are written down with what would close them. That is the difference between
> a gap and a mistake.

### 42 · What to research next
Backlog · prioritised — **Four questions worth the next week**

**On screen**

- **1 · Ask about US-08** — The highest-value single answer available. **Route:** the DPA schedule a customer already receives, or ask them.
- **2 · Buy one panel’s segment data** — It closes the only unresolved hypothesis, and it is the question your sales team asks first. **Route:** paid G2 or Gartner access.

- **3 · Detect the customer base independently** — The only roster outside the audited count is 178 stories Braze chose to publish. **Route:** tag crawls or job ads naming the stack. Not cheap.
- **4 · Re-run this in ninety days** — Every number here is reproducible by script. Watch the gross-margin decline and the 2026 incident rate.

**So the first two are worth a week and would change what we say; the last is worth an hour a quarter.** The full backlog is in docs/QUESTIONS.md.

**Say**

> If you gave me another week, this is the order.

> **First, ask about US-08.** It is the highest-value single answer available and it decides
> whether slide thirty-five is a curiosity or something procurement should raise. A
> customer can just look at their own DPA schedule.

> **Second, buy one panel's segment data.** It closes the hypothesis I could not test, and
> satisfaction-by-customer-size is the first thing your sales team will ask me.

> **Third, detect their customer base independently.** The only customer list we have
> outside the audited count is a hundred and seventy-eight stories they chose to publish.
> Tag crawls, certificate records and job ads naming Braze in the stack would give us a
> roster nobody curated. That one is not cheap, which is why it is third.

> The careers API was on this list until this morning, and it is not any more — we pulled
> it, and where their headcount is going is now on slide sixteen. Two hundred and
> ninety-six roles, seventy-two per cent go-to-market.

> **Fourth, and this is the real point: re-run all of it in ninety days.** Every number in
> this deck was produced by a script from a public source. Not one of them is a judgement
> call about where to look. The two I would watch are whether the margin decline continues,
> and whether the 2026 incident rate settles.

### 43 · Close
Close — **One thing to remember**

**On screen**

**Their strongest asset is a contract, not a capability.**

A billion dollars of next year is already signed, so most of the base is not winnable this year. They are growing slower and spending less to do it, so they can fund a fight. And the capability they paid $303.2m for runs on models anyone can rent, with no API of its own. **So compete on the renewal date and on the things they bought rather than built — not on the demo.**

- **1,352** — documentation pages read
- **451** — incidents
- **845** — public issues
- **17** — sub-processors
- **7** — audited years

**Say**

> One thing to remember.

> **Their documentation is more honest than anyone's marketing, including their own.**

> Every uncomfortable fact in this deck came from a page Braze wrote for its own
> engineers. Three of four ingestion paths labelled not real-time. A fifteen-minute
> warehouse floor. An export limit cut tenfold on a dated boundary, with existing customers
> grandfathered. A merge that returns success when it has silently declined.

> None of that is hidden. All of it is unread.

> And that is the transferable lesson, whichever vendor you point this at next: **the
> competitive advantage was not access. It was reading what they already published, and
> counting it.**
