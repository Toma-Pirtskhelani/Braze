# The money

> Growth is decelerating and efficiency is improving at the same time, and the two are connected rather than coincidental. Revenue growth has halved since FY2023 while sales and marketing fell from 56.7% of revenue to 44.3%; operating cash flow has been positive and growing for three years; and the net loss persists mainly because share-based compensation now exceeds it. One caveat qualifies everything here, and it is stated first.

{{slides: 8, 33}}

Every figure in this chapter is audited, filed under legal penalty, and re-derivable by
running `python3 tools/sec_facts.py`, which writes `data/financials_annual.csv` and
`data/financials_quarterly.csv` from the SEC XBRL company-facts API. Fiscal years end 31 January — see §1.1 for why that
matters when re-deriving them.

## 2.1b · The caveat that travels with every figure in this chapter

Braze disclosed a **material weakness in its internal control over financial reporting**
as at 31 January 2026. The CEO and CFO concluded that disclosure controls were "not
effective at the reasonable assurance level". The weakness is specific: "ineffective
information technology general controls, or ITGCs, in the areas of **user access and
program change management** over the information technology systems that support our
financial reporting processes" — and the company states that automated and IT-dependent
manual controls relying on that environment were consequently ineffective too.

[[audited]] {{src: sources/filings/2026-03-25_10-K_000013.txt:3258,3286 @ 2026-03-25}}

Both halves belong in the same breath, because either one alone misleads.

The reassuring half is substantial, and it is the company's own and the auditor's: the
material weakness "did not result in any identified misstatements to the financial
statements, and there were no changes to previously issued financial results"; management
concluded the statements "fairly present in all material respects"; and Ernst & Young
issued an attestation report on internal control over financial reporting
(`sources/filings/2026-03-25_10-K_000013.txt:3286`). Remediation is
under way with "significant progress" claimed and no completion date given. OfferFit was
excluded from the assessment, as SEC guidance permits in an acquisition's first year — it
is 1.4% of total assets and 1.8% of revenue (`sources/filings/2026-03-25_10-K_000013.txt:3258`),
so the exclusion is immaterial to the figures below.

The unreassuring half is that the control environment producing every number in this
chapter was judged not effective by the people who signed it, and the specific area is
user access and change management.

How much should that change your confidence? Less than the phrase "material weakness"
suggests, and more than zero. A material weakness is a statement about the *probability*
that an error could occur and go undetected, not a finding that one did. Here the
independent checks all came back clean: no misstatement identified, nothing restated, an
auditor attestation, and — separately and mechanically — this project's own restatement
sweep across twenty-nine XBRL concepts found no superseded value — `data/financials_restated.csv`,
produced by `tools/sec_facts.py` (conflict **C-05**).
Three confirmations that the outputs are sound, against one disclosure that the process
producing them is not yet controlled to standard.

Two disciplines apply. **Do not extrapolate this into a claim about customer data
security.** It is scoped to financial-reporting systems and says nothing about the
platform, and the temptation to make that leap — for a company whose product is data
infrastructure — is exactly why the scope should be restated every time. And do not bury
it: a competitor briefing that omits this and is later asked about it has damaged its own
credibility for no gain.

## 2.1 · Seven years of revenue and margin

| Fiscal year | Revenue ($m) | Growth | Gross margin |
|---|---|---|---|
| FY2020 | 96.4 | — | 63.0% |
| FY2021 | 150.2 | 55.9% | 63.7% |
| FY2022 | 238.0 | 58.5% | 67.0% |
| FY2023 | 355.4 | 49.3% | 67.4% |
| FY2024 | 471.8 | 32.7% | 68.7% |
| FY2025 | 593.4 | 25.8% | 69.1% |
| FY2026 | 738.2 | 24.4% | 67.1% |

[[audited]] {{src: data/financials_annual.csv @ 2026-09-02}}

Two things happen in the final row and they should be read together. Growth continues to
decelerate — it has roughly halved over three years — and gross margin falls for the first
time in six years, by 2.0 points.

The deceleration is the less interesting of the two, because it is what happens to every
subscription business as its base grows: adding $145m to a $593m base is a larger absolute
achievement than adding $117m to a $355m base, and the percentage falls anyway. Note also
that FY2026's growth is close to flat against FY2025 — the halving happened between FY2023
and FY2025, and has since largely stopped. An account that says "growth is collapsing" is
describing a period that ended two years ago.

The margin fall is the one that repays attention, and Braze explains it themselves in terms
specific enough to check: "primarily due to acquisition related operating costs, including
personnel costs of acquired workforce and amortization expense of acquired technology, in
addition to increased costs related to our tech stack."

The acquisition is OfferFit (chapter 3), whose developed technology is amortised **to cost
of revenue** rather than to operating expense. That accounting choice is why an AI
acquisition shows up in the gross-margin line rather than below it, and it is why the
decline is best read not as pricing pressure but as the price of buying an AI product. What
the sentence does not do is split the two causes. "Increased costs related to our tech
stack" is unquantified, and for a company that has just added three foundation-model
providers to its sub-processor list (chapter 6), the size of that component is the single
most useful undisclosed number in the filing. It is open question 59.

{{src: sources/filings/2026-03-25_10-K_000013.txt:1565 @ 2026-03-25}}

## 2.2 · Losses, cash and the equity cost

| Fiscal year | Net loss ($m) | Operating cash flow ($m) | Share-based comp ($m) |
|---|---|---|---|
| FY2022 | −76.7 | −35.4 | 47.2 |
| FY2023 | −139.0 | −22.3 | 72.2 |
| FY2024 | −129.2 | +6.8 | 97.2 |
| FY2025 | −103.7 | +36.7 | 115.1 |
| FY2026 | −131.3 | +71.4 | 143.7 |

[[audited]] {{src: data/financials_annual.csv @ 2026-09-02}}

The favourable reading and the uncomfortable one are both in this table and both are true.

Favourably: operating cash flow crossed into positive territory in FY2024 and has grown
every year since, roughly doubling each time. A company generating $71.4m of operating cash
is not a company in difficulty, whatever the loss line says, and this is the number to reach
for when someone characterises Braze as loss-making and therefore fragile. It is not
fragile. It funds itself.

Uncomfortably: share-based compensation has exceeded the entire net loss for two consecutive
years — 111% of it in FY2025 and 109% in FY2026. The arithmetic consequence is worth stating
plainly, because it is the fact most often fudged in both directions: **on these figures,
excluding share-based compensation, the business is around break-even.** That is not the
same as saying it is profitable. Share-based compensation is a real cost; it is simply borne
by shareholders through dilution rather than by the company through cash.

The dilution is measurable. Weighted-average diluted shares went from 94.6m in FY2023 to
107.9m in FY2026 (`data/financials_annual.csv`) — a rise of 14.1% in three years. So the honest summary is that Braze funds
its own operations from cash while transferring roughly a seventh of the equity to employees
over three years, and reports the result as a loss. Each of those three clauses gets misused
on its own.

For a competitor the practical reading is that **the loss line is not a pressure point**.
Anyone building a sales narrative around Braze running out of money is arguing against three
years of rising operating cash flow and $124.3m of cash on the balance sheet.

## 2.3 · Where the money goes

| Fiscal year | S&M share of revenue | R&D share of revenue |
|---|---|---|
| FY2020 | 59.5% | 21.1% |
| FY2022 | 53.4% | 24.8% |
| FY2023 | 56.7% | 27.4% |
| FY2024 | 52.4% | 25.4% |
| FY2025 | 47.6% | 22.6% |
| FY2026 | 44.3% | 22.6% |

[[audited]] {{src: data/financials_annual.csv @ 2026-09-02}}

This table killed a hypothesis. The analysis went in expecting growth to be decelerating
*while sales spend held* — the familiar pattern of a company buying its last few points of
growth. The evidence says the opposite: S&M has fallen more than twelve points as a share of
revenue since FY2023, to its lowest in the seven-year series, while growth decelerated. Braze
is decelerating and getting more efficient at the same time.

Three other parts of this record explain how, and together they make it a finding rather than
a curiosity. Revenue per employee rose 82% over the same period (§1.3), with the bulk of it
banked in a single year when hiring nearly stopped. The compensation plan pays 40% of its
financial component on non-GAAP operating income, with a hard gate that pays nothing at all
if a threshold is missed (§1.4). And operating cash flow turned positive in the same year the
hiring pause happened. A cost discipline visible in four independent places is a policy, not
an accident.

R&D tells a quieter story. It peaked at 27.4% of revenue in FY2023 and has settled at 22.6%
for two years. In absolute terms it is still growing — $167.1m in FY2026, from `data/financials_annual.csv` —
but as a share of revenue Braze now spends less on R&D than it did three years ago, during a period in which it
also bought its AI product rather than building it (chapter 3). Those two facts are not proof
of a strategy, but they point the same way, and a competitor should notice that the R&D line
did not spike to fund an AI programme.

Sales and marketing still outspends research and development by 1.96 times — $327.0m against
$167.1m in FY2026 — which is ordinary for enterprise software and worth stating plainly
rather than treating as a finding.

## 2.4 · Contracted revenue and geography

| Fact | Value | Grade | Source |
|---|---|---|---|
| Remaining performance obligation, FY2026 | $1,033.0m | [[audited]] | `data/financials_annual.csv` |
| RPO relative to FY2026 revenue | 1.40× | [[audited]] | derived from `data/financials_annual.csv` |
| United States revenue, FY2026 | $405.1m — 54.9% | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:2421` |
| International revenue, FY2026 | $333.1m — 45.1% | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:2421` |

Remaining performance obligation crossed a billion dollars in FY2026, having risen every year
from $234.2m in FY2021 (`data/financials_annual.csv`). At 1.40 times current-year revenue it is a genuine forward-visibility
measure and, unlike a pipeline number, it is contracted and audited.

This is the most commercially useful number in the chapter and it is routinely under-used.
RPO is revenue Braze has already signed and not yet recognised. For anyone selling against
Braze it says, with an auditor's signature on it, that **roughly a year and a half of current
revenue is not available to compete for** — not because customers would not move, but because
they are inside contract terms. It reframes the competitive question from "can we win this
account" to "when does it come up", and for most of the base the answer is not this year.
Chapter 7's retention figures then tell you what happens when it does.

The geographic split is an audited disclosure rather than an inference, and it carries a
sentence that matters more than the percentages: "Other than the United States, no other
individual country accounted for 10% or more of total revenue for any of the periods
presented." International share has been near-flat for three years — 43.4%, 45.0%, 45.1%, from the
segment note at `sources/filings/2026-03-25_10-K_000013.txt:2421` —
so the international business is growing at roughly the same rate as the whole, not faster.

Put that beside the infrastructure. Forty-five per cent of revenue is international and none
of it concentrates, supported by fifteen regional clusters (chapter 4) and fifteen legal
entities across fourteen territories (§1.5). That is a wide, thin footprint carrying a heavy
fixed base — expensive, and the necessary shape if regional data residency is part of what is
being sold. It also means no single non-US market is large enough that losing it would be
visible in the consolidated numbers, which cuts both ways: resilient to a bad year in any one
country, and lacking a second home market to fall back on.

#### What would change this chapter

A restatement — none has occurred, and both the mechanical sweep and the 10-K confirm it
(**C-05**). Remediation of the material weakness, which would remove §2.1b's caveat and would
be disclosed in the next 10-K or 10-Q. A second consecutive year of gross-margin decline,
which would move FY2026 from an acquisition effect to a pattern. Any disclosure that splits
"increased costs related to our tech stack" from acquisition amortisation (question 59). And
a change in the S&M trajectory, which would say the efficiency programme had run its course.
