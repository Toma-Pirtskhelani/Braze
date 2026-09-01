# Records the company does not control

Phase 4. Ordered by how hard it would be for the vendor to have made the statement
untrue. **The test: would this document be embarrassing to keep inaccurate?**

---

## Financial and statutory

| Record | Where | What it gives up | Applies to |
|---|---|---|---|
| **SEC filings** | `data.sec.gov/submissions/CIK<10-digit>.json` | Audited revenue, margin, cost lines, quarterly. Risk factors are legally compelled candour | US-listed |
| **SEC XBRL** | `data.sec.gov/api/xbrl/companyfacts/CIK<10>.json` | Every reported number, machine-readable, restatements visible | US-listed |
| Proxy statement (DEF 14A) | EDGAR | What management is paid to optimise; the board | US-listed |
| Insider transactions (Form 4/144) | EDGAR | Dated insider trades. Read the *shape*, never a single trade — most are scheduled plans | US-listed |
| Ownership (SC 13G/13D) | EDGAR | Who owns it and when that changed | US-listed |
| **UK Companies House** | `find-and-update.company-information.service.gov.uk` | Filed accounts for a UK entity, directors, parent chain | Any vendor with a UK entity |
| Other registries | Handelsregister (DE), KVK (NL), ACRA (SG), Ticaret Sicil (TR) | The operating entity is often not called what the company is called | Varies |

**Find the CIK:** `https://www.sec.gov/files/company_tickers.json`, or search EDGAR by
name. SEC requires a real contact string in the User-Agent.

**Trap:** in XBRL, `fy` and `fp` describe the *filing*, not the period. A single 10-K
reports two fiscal years and labels both with the filing's year. Key on `start`/`end`.

**Caution on subsidiary accounts:** for a group that consolidates, one subsidiary's
filed accounts reflect transfer pricing as much as unit economics. Say so in the same
sentence as the number, or do not use it.

---

## Infrastructure

| Record | Where | What it gives up |
|---|---|---|
| **Certificate transparency** | `crt.sh/?q=%25.DOMAIN&output=json`; fall back to `api.certspotter.com/v1/issuances` | Hosts provisioned but never announced — unreleased products, internal tools, **named customers** |
| Passive DNS | Various | Same, less reliably |
| Public status page | `status.DOMAIN`, often `<name>.statuspage.io` | Incident history with durations; the component list is an architecture disclosure made by accident |
| `security.txt` | `DOMAIN/.well-known/security.txt` | Its **absence** is as informative as its content |
| `robots.txt` | `DOMAIN/robots.txt` | Sometimes names paths that appear nowhere else |

**Read the newest CT entries first.** That is where unannounced things appear. crt.sh is
frequently down; keep a fallback and record the gap rather than skipping it.

**Statuspage APIs:** `/api/v2/components.json` for the component tree,
`/api/v2/incidents.json` for the most recent 50, and `/history.json?page=N` for the long
tail. The two feeds have *different shapes* — the history feed renders timestamps inside
`<var>` tags and carries no resolved timestamp.

---

## Compelled disclosures

| Record | Where | What it gives up |
|---|---|---|
| **Sub-processor list** | `DOMAIN/legal/subprocessors` or the trust centre | The database engine, the iPaaS, every delivery supplier — **and which channel has no middleman** |
| DPA / trust centre | Same | Certifications, regions, retention |
| Patent filings | Espacenet, USPTO | What they thought was worth protecting, and when |
| Trademark filings | USPTO, EUIPO | Product names before launch |

Capture the sub-processor list **with a date**. On the reference project it changed from
16 entities to about 40 mid-analysis, and the correction was only visible because both
versions had been kept.

---

## Engineering

| Record | Where | What it gives up |
|---|---|---|
| **Public repositories** | `api.github.com/orgs/<org>/repos` | Release cadence per platform; which SDKs quietly stopped moving |
| Releases and tags | `/repos/<org>/<repo>/releases` | A dated shipping history nobody wrote for marketing |
| Package registries | npm, Maven, PyPI, CocoaPods | Download counts, version history |
| Issue trackers | The same repos | What users hit, in their words, with the vendor answering |

Release cadence measures **maintenance**, not capability, and says nothing about the
server side. A supported platform with no release in two years is a different claim from
one shipping monthly — and that is the finding.

GitHub allows 60 requests/hour anonymously, 5,000 with a token.

---

## People

| Record | Where | What it gives up |
|---|---|---|
| Careers board | The vendor's own | Open roles **by function**. The strategy, stated in hiring |
| LinkedIn | Company page | Headcount as a **range**. Never a precise figure |
| Glassdoor | Company page | Sentiment and, more usefully, its trend |
| Conference talks | YouTube, slides | Engineers say things in talks that never reach a marketing page |

---

## Buyers

| Record | Where | What it gives up |
|---|---|---|
| **Gartner Peer Insights** | Peer Insights vendor page | Ratings, deployment region, and **shortlists** |
| G2 | Product reviews | Rating, star distribution, **company-size mix** |
| TrustRadius | Product reviews | Longer-form, often more specific |
| Public procurement | Government tender portals | **Actual contracted prices**, occasionally |

**Gartner shortlists are the highest-value field on any review site.** Who a buyer
actually compared the vendor against is worth more than any competitor page, because the
vendor did not choose it.

Review sites block scripted access. Use a real browser session, or ask the operator to
paste. That is a five-minute human step, not a failure.

---

## What to do when a source fails

Write it down. `logs/fetch-failures.md`, with the URL, the error and the date.

A gap you have written down is evidence — it can be retried, and it can be stated
honestly in the deliverable. A gap you have not written down is a mistake, and it will
be discovered by whoever asks the one question you did not check.
