# Question backlog

What the analysis had to answer, what it answered, and what it could not. Ordered so that
the first section is the deck's spine and the last is the honest residue.

**Status as at 2026-09-02, after the run.** Questions 1–45 were written before any source
was captured; each now carries where it was answered — `ch§` is a section of the evidence
record in [`deck/record/`](../deck/record/), `slide` is the built deck. Questions 46–59
are the residue: nothing public closed them, and each records what would.

Three rules for maintaining this file:

- **Never lose a question's content when rewording it.** Sharpen the phrasing; keep the
  substance.
- **A question that turns out to be unanswerable is not deleted.** It moves to §4 with a
  note on what source would close it. Absence is a finding.
- **A question answered only in part says so**, and names the part that is missing. An
  unqualified tick on a half-answer is the most expensive kind of error in this file,
  because nobody goes back to check a question already marked closed.

---

## 1 · Questions the deck must answer — all 29 answered

These map to [`DECK-SPEC.md`](DECK-SPEC.md) and each one became a slide.

**The company**
1. Who legally *is* Braze — registrant, subsidiaries, where each is incorporated?
   — **answered**, ch1 §1.5 · slide 5. 15 group entities across 14 territories, one of
   them a majority-held VIE (conflict C-09).
2. Who founded it, who runs it now, and how much of the founding team is still in post?
   — **answered**, ch1 §1.2 · slide 7. Includes the end of the dual-class structure.
3. What money came in, when, on what terms — pre-IPO and at the IPO?
   — **answered**, slide 8. Net IPO proceeds and the cash position; pre-IPO round terms
   were not pursued, being outside what the filings restate.
4. What have they acquired, for how much, and what did each acquisition actually bring?
   — **answered**, ch3 · slides 9, 10. Both prices, both allocations, one dead earn-out.
5. What does a customer really pay, and how wide is the range?
   — **answered in part**, ch7 §7.1 · slide 11. A *bound* of about $283,000 per corporate
   group, not a price, and no transacted price exists anywhere in the corpus. The range
   is unresolved and stays open as #46.
6. How many customers, on whose definition, and how do the definitions differ?
   — **answered**, ch7 §7.1 · slide 12. Three rosters that must never be merged.
7. Which geographies carry the revenue, as opposed to which are marketed?
   — **answered**, ch2 §2.4 · slide 13.
8. What do customers praise and complain about, coded rather than summarised?
   — **answered**, ch7 §7.4 · slide 14, using each panel's own coded tags over its full
   base rather than the fourteen captured review bodies.
9. What does working there look like, and which way is it trending?
   — **answered**, ch7 §7.5 · slide 15. The work-life-balance decline looked for was not
   found; that null result is recorded rather than dropped.
10. Who do they say they compete with, and who do buyers actually shortlist them against?
    — **answered**, ch7 §7.3 · slide 16.

**The product**
11. What happens end to end when one campaign runs? — **answered**, slide 18.
12. How does data get in, how fresh is it, and which paths are event-driven?
    — **answered**, ch4 · slide 20, from Braze's own latency table.
13. How is one person resolved across devices and identifiers — and what are the limits?
    — **answered**, ch4 · slide 21.
14. What decides who gets what, and how much of that decisioning is model-driven?
    — **answered**, ch4 · slide 22, with ch6 on the provenance of the models.
15. How is a journey built, and what do users say about building one? — **answered**,
    slide 23.
16. How is content composed and personalised? — **answered**, slide 24.
17. How is a message physically delivered, and who is the middleman on each channel?
    — **answered**, ch5 §5.2 · slide 25, from the compelled sub-processor disclosure.
18. What happens when a customer replies? — **answered**, slide 26.
19. How many channels exist, and which are never marketed? — **answered**, ch5 §5.1 ·
    slide 27. Three defensible counts, which is conflict C-02.
20. What is the integration layer — built or bought? — **answered**, ch5 §5.3 · slide 28.
21. What is it built on, and what does the architecture constrain? — **answered**, ch4 ·
    slide 29.
22. What can a customer actually measure, and what can they export? — **answered**,
    slide 30.
23. What in the AI is shipped ML, what is agentic, and what is renaming? — **answered**,
    ch6 · slide 31, on five independent lenses.

**Strategy**
24. Where does the money go — R&D, sales, and general, over seven audited years?
    — **answered**, ch2 §2.3 · slide 33.
25. What is coming that has not been announced? — **answered**, slide 34, as three
    sourced observations and explicitly not as a conclusion.
26. What actually protects them from a competitor doing the same thing? — **answered**,
    slide 35.

**Frame and close**
27. What are the five things to remember? — **answered**, slide 5.
28. How trustworthy is each claim, and how do we show that on every slide?
    — **answered**, slides 2, 3 and the grade badge carried on every figure.
29. What could public sources not answer, and what would close each gap? — **answered**,
    slide 39 and §4 below.

---

## 2 · Questions Braze uniquely permits

Not available on a private vendor. Each was a candidate for a slide of its own; not all
earned one, and the ones that did not are still in the record.

30. What is the audited gross margin trend, and what is driving it? — **answered**,
    ch2 §2.1 · slide 33. Braze's own explanation, with the unquantified half flagged
    as #59.
31. How much revenue is contracted but not yet recognised, and what does that say about
    forward visibility? — **answered**, ch2 §2.4 · slide 8.
32. What is share-based compensation as a share of revenue, and what does that cost
    shareholders? — **answered**, ch2 §2.2 · slide 33.
33. What does management's compensation plan pay them to optimise? — **answered**,
    ch1 §1.4. **Reached the record and no slide**, which is a deliberate call: it explains
    the cost discipline in ch2 §2.3 rather than standing on its own.
34. Who owns the company, and how has that changed? — **answered in part**, ch1 §1.2. The
    structural change is captured — the dual-class structure ended on 30 January 2026 and
    super-voting rights are gone. A beneficial-ownership percentage table was not
    extracted from the proxy; `data/insider_filing_counts.csv` holds only filing counts.
35. What does the company itself say could go wrong, in the risk factors? — **answered in
    part**. Individual risk factors are used where they carry a fact (ch1 §1.2 on founder
    departure, ch4 on the hosting disclosure). No systematic pass over the risk-factor
    section was made, and it would be a cheap addition to a second run.
36. What does a decade of incident history show about reliability at scale? — **answered**,
    ch4 · slide 38. 451 incidents since 2016, with the 2026 caveat on the slide.
37. Which supported platforms are actually maintained, judged by release cadence?
    — **answered**, ch4 · slide 38. All nine SDK repositories had shipped within 13 days
    of capture — a favourable finding, and one that killed a hypothesis.
38. What does the fifteen-cluster regional architecture imply for a buyer with data
    residency requirements? — **answered**, ch4 · slide 29 and ch2 §2.4. (The setup-time
    "twelve" was wrong; see the corrections table in `FACTS.md`.)

---

## 3 · Questions carried over from the reference analysis

The reference deck's audience asked these. They were asked again, and they are worth
pre-answering.

39. How large are their customers, really — and does satisfaction change with size?
    — **half answered**. Size is answered: 333 customers at $500k+ of ARR, ch7 §7.2. The
    satisfaction-by-size half is the one hypothesis nothing available could test, and it
    stays open as #54.
40. Where are their servers, and what does that mean for latency outside the US?
    — **answered**, ch4 · slide 29, corroborated against the sub-processor AWS regions.
41. Which stages of the data pipeline are genuinely innovative and which are table
    stakes? — **answered**, ch4, which is why the product part is built as seven stages
    rather than as a feature list.
42. Why is a channel absent, when the category expects it? — **answered**, ch5 §5.1. The
    finding inverted: the roster is broad, and the drift between the docs index and the
    marketing site is what carries the information.
43. Can customer distribution by geography and industry be verified independently, not
    just claimed? — **not attempted**, and recorded as a gap rather than as a zero. It is
    #57.
44. Are there industry-specific demos or configurations, or is it one product for
    everyone? — **not pursued**. `data/site_inventory.csv` carries `/solutions/` landing
    pages by vertical — financial services, gaming, luxury, media, on-demand, QSR, retail,
    travel — localised into several languages, but no pass was made over them and nothing
    establishes whether they are marketing pages or configurations. This is the
    weakest-covered question in the file and would be first on a second run's list.
45. When a vendor identifies a logged-out user across brands, what is the consent basis?
    — **answered in part**, ch4. What the documentation permits mechanically is captured;
    the consent basis is a legal question the documentation does not answer and no public
    source settles.

---

## 4 · Questions public sources probably cannot answer

Recorded so they are not silently dropped. Each carries what *would* close it.

| # | Question | What would close it |
|---|---|---|
| 46 | Actual list pricing and discounting policy | A leaked rate card, a public-sector procurement award, or a customer willing to share a contract |
| 47 | Net revenue retention by segment | Only disclosed in aggregate, if at all — an investor day may go further |
| 48 | Real engineering headcount and its split | LinkedIn ranges and job postings bound it; nothing confirms it |
| 49 | Which features customers actually use | No vendor publishes adoption. A user survey would be primary research |
| 50 | Roadmap beyond announced releases | CT logs and job postings hint; nothing confirms |
| 51 | Win/loss rates against named competitors | Requires being in the deals |
| 52 | **Why does the sub-processor disclosure of 1 June 2026 name only Amazon and Google as hosting providers, when the allowlist IPs Braze publishes for instance US-08 are all registered to Microsoft Corporation?** | An updated sub-processor list, the DPA schedule a customer receives, or a direct answer from Braze. Do not infer a disclosure failure from outside — see `CONFLICTS.md` C-03 |
| 53 | Is the `aze` region code in certificate transparency Azure, and is US-08 a distinct class of instance (single-tenant, enterprise, or a specific customer's)? | A Braze statement, a customer on US-08, or a wider CT capture with a `CERTSPOTTER_TOKEN` |
| 54 | Does customer satisfaction fall as company size rises? (hypothesis 7, unresolved) | Paid access to the G2, Gartner or TrustRadius rating-by-company-size breakdowns, all three of which are paywalled. An investor-day segment disclosure would also close it |
| 55 | Why was the `/users/export/ids` rate limit cut from 2,500 to 250 requests per minute for customers onboarding on or after 22 August 2024, and were existing customers told? | A changelog entry, a support answer, or a customer who onboarded either side of that date |
| 56 | ~~What is the exact split of open roles by department?~~ **CLOSED 2026-09-02.** 296 open roles across 15 hiring departments — Sales 89, Engineering 57, Customer Experience 38, and 72.0% of the board go-to-market against 19.6% engineering and product | Closed by the Greenhouse board API, exactly as this row predicted: `tools/careers_board.py` → `data/careers_departments.csv`, raw JSON kept at `sources/external/greenhouse-board-braze_2026-09-02.json`. Kept in the table rather than deleted, because what closed it is the reusable lesson: the page would not yield, the API behind it did |
| 57 | Can the customer roster be verified independently of the 178 self-selected customer stories? | Tag crawls of customer sites, CT records naming customer subdomains, or job ads naming Braze in the stack. Not attempted in this run |
| 58 | What else is in the certificate-transparency estate? | The captured host list is **partial** — 833 hosts from Cert Spotter, rate-limited, with crt.sh returning 502 throughout. A `CERTSPOTTER_TOKEN` would widen it. **No claim is made that anything is absent from CT; the list was not exhaustive** |
| 59 | Does the FY2026 gross-margin decline continue, and how much of it is the AI cost base rather than acquisition amortisation? | FY2027 10-K, or quarterly cost-of-revenue detail. The company attributes it to acquisition costs plus "increased costs related to our tech stack" without splitting the two |

---

## 5 · How to add to this file

New questions go to the end of the relevant section with the next free number. Numbers
are never reused, so a question referenced in a deck or a record stays findable even
after it moves between sections.
