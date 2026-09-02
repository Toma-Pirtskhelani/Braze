# The money

> Growth is decelerating and efficiency is improving at the same time: revenue growth has halved since FY2023 while sales and marketing has fallen from 56.7% of revenue to 44.3%, operating cash flow has been positive for three years, and the net loss persists mainly because share-based compensation now exceeds it.

{{slides: 8, 33}}

Every figure in this chapter is audited, filed under legal penalty, and re-derivable by
running `python3 tools/sec_facts.py`. Fiscal years end 31 January.

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
decelerate — it has roughly halved over three years — and gross margin falls for the
first time in six years, by 2.0 points.

The company explains the margin fall itself, and the explanation is specific: "primarily
due to acquisition related operating costs, including personnel costs of acquired
workforce and amortization expense of acquired technology, in addition to increased costs
related to our tech stack." The acquisition in question is OfferFit (chapter 3), whose
developed technology is amortised **to cost of revenue**. So the first margin decline in
six years is, on the company's own account, largely the price of buying its AI
decisioning engine. How much of the remainder is the AI cost base rather than the
acquisition is not split out, and is open question 59.

{{src: sources/filings/2026-03-25_10-K_000013.txt:1565 @ 2026-03-25}}

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

The reassuring half is substantial and is the company's own and the auditor's: the
material weakness "did not result in any identified misstatements to the financial
statements, and there were no changes to previously issued financial results";
management concluded the statements "fairly present in all material respects"; and Ernst
& Young issued an attestation report on internal control over financial reporting.
Remediation is under way with "significant progress" claimed and no completion date
given. OfferFit was excluded from the assessment, as SEC guidance permits in an
acquisition's first year — it is 1.4% of total assets and 1.8% of revenue.

The unreassuring half is that the control environment producing every number in this
chapter was judged not effective by the people who signed it, and the specific area is
user access and change management.

Two disciplines apply. **Do not extrapolate this into a claim about customer data
security** — it is scoped to financial-reporting systems and says nothing about the
platform. And note that it is consistent with, not contradicted by, conflict **C-05**:
the restatement check found nothing, and the 10-K independently confirms no previously
issued results changed.

## 2.2 · Losses, cash and the equity cost

| Fiscal year | Net loss ($m) | Operating cash flow ($m) | Share-based comp ($m) |
|---|---|---|---|
| FY2022 | −76.7 | −35.4 | 47.2 |
| FY2023 | −139.0 | −22.3 | 72.2 |
| FY2024 | −129.2 | +6.8 | 97.2 |
| FY2025 | −103.7 | +36.7 | 115.1 |
| FY2026 | −131.3 | +71.4 | 143.7 |

[[audited]] {{src: data/financials_annual.csv @ 2026-09-02}}

The favourable reading and the uncomfortable one are both in this table and both are
true.

Favourably: operating cash flow crossed into positive territory in FY2024 and has grown
every year since, roughly doubling each time. A company generating $71.4m of operating
cash is not a company in difficulty, whatever the loss line says.

Uncomfortably: share-based compensation has exceeded the entire net loss for two
consecutive years — 111% of it in FY2025 and 109% in FY2026. Stated as an observation
rather than an accusation: the loss is substantially a non-cash equity cost, and the
people bearing it are shareholders through dilution. Weighted-average diluted shares
went from 94.6m in FY2023 to 107.9m in FY2026, a rise of 14.1% in three years.

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
*while sales spend held* — the familiar pattern of a company buying its last few points
of growth. The evidence says the opposite: S&M has fallen more than twelve points as a
share of revenue since FY2023, its lowest in the seven-year series, while growth
decelerated. Braze is decelerating and getting more efficient at the same time.

Sales and marketing still outspends research and development by 1.96 times — $327.0m
against $167.1m in FY2026 — which is ordinary for enterprise software and worth stating
plainly rather than treating as a finding.

## 2.4 · Contracted revenue and geography

| Fact | Value | Grade | Source |
|---|---|---|---|
| Remaining performance obligation, FY2026 | $1,033.0m | [[audited]] | `data/financials_annual.csv` |
| RPO relative to FY2026 revenue | 1.40× | [[audited]] | derived from `data/financials_annual.csv` |
| United States revenue, FY2026 | $405.1m | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:2421` |
| International revenue, FY2026 | $333.1m — 45.1% of the total | [[audited]] | `sources/filings/2026-03-25_10-K_000013.txt:2421` |

Remaining performance obligation crossed a billion dollars in FY2026, having risen every
year from $234.2m in FY2021. At 1.40 times current-year revenue it is a genuine forward
visibility measure and, unlike a pipeline number, it is contracted and audited.

The geographic split is an audited disclosure rather than an inference, and it carries a
sentence that matters more than the percentages: "Other than the United States, no other
individual country accounted for 10% or more of total revenue for any of the periods
presented." Forty-five per cent of revenue is international and none of it concentrates.
Set that against fifteen regional clusters (chapter 4) and fifteen legal entities
(chapter 1), and the shape is a wide, thin international footprint carrying a heavy
infrastructure and legal base.

{{src: sources/filings/2026-03-25_10-K_000013.txt:2421 @ 2026-03-25}}

#### What would change this chapter

A restatement — none has occurred; across the twenty-nine key XBRL concepts tracked,
`data/financials_restated.csv` is empty, and that negative result is recorded as conflict
C-05 rather than left unstated. The next 10-K would change the trend lines. A second
consecutive year of margin decline would move the FY2026 fall from an acquisition effect
to a pattern.
