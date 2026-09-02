# Question backlog

What the analysis must answer, and what it probably cannot. Ordered so that the first
section is the deck's spine and the last is the honest residue.

Two rules for maintaining this file:

- **Never lose a question's content when rewording it.** Sharpen the phrasing; keep the
  substance.
- **A question that turns out to be unanswerable is not deleted.** It moves to §4 with a
  note on what source would close it. Absence is a finding.

---

## 1 · Questions the deck must answer

These map to [`DECK-SPEC.md`](DECK-SPEC.md) and each one becomes a slide.

**The company**
1. Who legally *is* Braze — registrant, subsidiaries, where each is incorporated?
2. Who founded it, who runs it now, and how much of the founding team is still in post?
3. What money came in, when, on what terms — pre-IPO and at the IPO?
4. What have they acquired, for how much, and what did each acquisition actually bring?
5. What does a customer really pay, and how wide is the range?
6. How many customers, on whose definition, and how do the definitions differ?
7. Which geographies carry the revenue, as opposed to which are marketed?
8. What do customers praise and complain about, coded rather than summarised?
9. What does working there look like, and which way is it trending?
10. Who do they say they compete with, and who do buyers actually shortlist them against?

**The product**
11. What happens end to end when one campaign runs?
12. How does data get in, how fresh is it, and which paths are event-driven?
13. How is one person resolved across devices and identifiers — and what are the limits?
14. What decides who gets what, and how much of that decisioning is model-driven?
15. How is a journey built, and what do users say about building one?
16. How is content composed and personalised?
17. How is a message physically delivered, and who is the middleman on each channel?
18. What happens when a customer replies?
19. How many channels exist, and which are never marketed?
20. What is the integration layer — built or bought?
21. What is it built on, and what does the architecture constrain?
22. What can a customer actually measure, and what can they export?
23. What in the AI is shipped ML, what is agentic, and what is renaming?

**Strategy**
24. Where does the money go — R&D, sales, and general, over seven audited years?
25. What is coming that has not been announced?
26. What actually protects them from a competitor doing the same thing?

**Frame and close**
27. What are the five things to remember?
28. How trustworthy is each claim, and how do we show that on every slide?
29. What could public sources not answer, and what would close each gap?

---

## 2 · Questions Braze uniquely permits

Not available on a private vendor. Each is a candidate for a slide of its own; not all
will earn one.

30. What is the audited gross margin trend, and what is driving it?
31. How much revenue is contracted but not yet recognised, and what does that say about
    forward visibility?
32. What is share-based compensation as a share of revenue, and what does that cost
    shareholders?
33. What does management's compensation plan pay them to optimise?
34. Who owns the company, and how has that changed?
35. What does the company itself say could go wrong, in the risk factors?
36. What does a decade of incident history show about reliability at scale?
37. Which supported platforms are actually maintained, judged by release cadence?
38. What does the fifteen-cluster regional architecture imply for a buyer with data
    residency requirements? (the setup-time "twelve" was wrong; see the corrections
    table in `FACTS.md`)

---

## 3 · Questions carried over from the reference analysis

The reference deck's audience asked these. They will be asked again, and they are worth
pre-answering.

39. How large are their customers, really — and does satisfaction change with size?
40. Where are their servers, and what does that mean for latency outside the US?
41. Which stages of the data pipeline are genuinely innovative and which are table
    stakes?
42. Why is a channel absent, when the category expects it?
43. Can customer distribution by geography and industry be verified independently, not
    just claimed?
44. Are there industry-specific demos or configurations, or is it one product for
    everyone?
45. When a vendor identifies a logged-out user across brands, what is the consent basis?

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
| 56 | What is the exact split of open roles by department? | The Greenhouse board API (`job-boards.greenhouse.io/braze`), or a working pass over the board's Department filter. Only the 15-department taxonomy and a front-of-list sample were captured |
| 57 | Can the customer roster be verified independently of the 178 self-selected customer stories? | Tag crawls of customer sites, CT records naming customer subdomains, or job ads naming Braze in the stack. Not attempted in this run |
| 58 | What else is in the certificate-transparency estate? | The captured host list is **partial** — 833 hosts from Cert Spotter, rate-limited, with crt.sh returning 502 throughout. A `CERTSPOTTER_TOKEN` would widen it. **No claim is made that anything is absent from CT; the list was not exhaustive** |
| 59 | Does the FY2026 gross-margin decline continue, and how much of it is the AI cost base rather than acquisition amortisation? | FY2027 10-K, or quarterly cost-of-revenue detail. The company attributes it to acquisition costs plus "increased costs related to our tech stack" without splitting the two |

---

## 5 · How to add to this file

New questions go to the end of the relevant section with the next free number. Numbers
are never reused, so a question referenced in a deck or a record stays findable even
after it moves between sections.
