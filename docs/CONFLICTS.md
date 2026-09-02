# Conflicts register

Where two credible sources disagree, **both are recorded and neither is chosen.** Each
entry carries a **ruling**: the sentence to say out loud. Follow the ruling.

This is not fence-sitting. "Quote the ordering, never the decimal" and "quote the range,
never a precise figure" are more useful to a presenter than a number picked by coin
toss, and they are honest about what is actually known.

## How to open an entry

```
### C-NN · <the question in six words>

| | value | source | grade | as of |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

**Why they differ:** <the mechanism, if known — different definitions, different dates,
different populations, or a genuine contradiction>

**Ruling:** <the exact sentence to use out loud>
```

Number entries sequentially and never renumber. A conflict that is later resolved keeps
its number and gains a **Resolved** line — the history is the point.

## When something is *not* a conflict

Three cases that look like conflicts and are not:

- **Different definitions of the same word.** A 10-K "customer" and a marketing
  "customer" may both be right. That is a definitions problem: state both definitions,
  and do not put it here.
- **Different dates.** A figure that changed is not a figure in dispute. Date both and
  move on.
- **Marketing contradicting an audited filing.** For a listed company that is an
  *error*, not a disagreement. Give the filed figure, note that it is filed under
  penalty, and say so without drama. Only record it here if the discrepancy is itself
  the finding.

And one case that *is* a conflict and is easy to miss: **a restated financial figure.**
`tools/sec_facts.py` writes every superseded value to `data/financials_restated.csv`.
Anything that lands in that file gets an entry here.

---

## Register

### C-01 · Is the platform real-time or not?

| | value | source | grade | as of |
|---|---|---|---|---|
| A | "our platform empowers real-time engagement… high-volume, continuous streaming of user data to be processed in real time" | `sources/filings/2026-03-25_10-K_000013.txt:258,287,289` | audited (Item 1, filed) | 2026-03-25 |
| A′ | "The platform can handle any data in real time, regardless of how it's nested or structured" | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:32` | documented | 2026-09-02 |
| B | Of four named ingestion paths, three are labelled **"Not real-time"** and the fourth "Near-real-time (async processing)". Warehouse syncs have a 15-minute floor | `sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:86-90,32` | documented | 2026-09-02 |

**Why they differ:** they are describing different paths. The real-time claim is true of
the SDK and `/users/track` route, where events stream in and are processed
asynchronously within seconds. The "not real-time" labels apply to the three warehouse
routes — Standard CDI sync, CDI Segments and CDI Canvas triggers — which are scheduled,
with a 15-minute minimum cadence. Both statements are accurate about their own subject.
This is not an error and not a contradiction; it is one word covering two architectures.

**Ruling:** never say "real-time" or "not real-time" about Braze unqualified. Say:
**"Real-time applies to the SDK and API path. Braze's own comparison table labels three
of its four ingestion paths 'not real-time', with a fifteen-minute floor on warehouse
syncs — so if your customer data lives in a warehouse, fifteen minutes is the floor
unless you move to the API."** If pressed on the discrepancy, note that the vendor
documents this itself, in a table, and does not hide it.

---

### C-02 · How many channels does Braze have?

| | value | source | grade | as of |
|---|---|---|---|---|
| A | 12, per Braze's own documentation channel index | `sources/docs/docs__user_guide__channels.md:14-64` | documented | 2026-09-02 |
| B | 13 — the same 12 plus KakaoTalk, which has four documentation pages and a marketing product page but is absent from that index | `sources/docs/docs__user_guide__channels__kakaotalk__*.md`; `data/site_inventory.csv` | documented / claimed | 2026-09-02 |
| C | 10 have a dedicated marketing product page; 5 documented channels have none (Banners, Transactional email, Landing pages, Live notifications, Webhooks) | `data/site_inventory.csv` | claimed | 2026-09-01 |

**Why they differ:** the documentation index and the marketing site are maintained
separately and have drifted in both directions at once. KakaoTalk is sold but not
indexed; Banners, Landing pages, Live notifications, Transactional email and Webhooks
are documented but not sold as named products.

**Ruling:** give the number with its source attached — **"thirteen channels are
documented; their own channel index lists twelve and omits KakaoTalk; ten have a
marketing page."** The useful sentence is not the count but the drift:
**"Five documented channels have no marketing page, and one marketed channel is missing
from their own index."** Do not present any single number as *the* channel count.

---

### C-03 · Which cloud is Braze on?

| | value | source | grade | as of |
|---|---|---|---|---|
| A | Two hosting providers: Amazon Web Services and Google Cloud Platform. Microsoft is not named | `sources/clean/braze-subprocessors.md:21,31` (compelled disclosure, rev. 1 June 2026) | documented | 2026-09-02 |
| A′ | The 10-K risk factors: "We rely upon third-party providers of cloud-based infrastructure, including **Amazon Web Services and Rackspace**, to host our products." Microsoft is not named | `sources/filings/2026-03-25_10-K_000013.txt:631` | audited | 2026-03-25 |
| B | The allowlist IPs Braze publishes for instance **US-08** are all registered to Microsoft Corporation; every other instance's are registered to Amazon entities | `sources/docs/…connected_sources.md:239`; `sources/external/rdap-instance-ip-ownership_2026-09-02.json` (ARIN RDAP) | infrastructure | 2026-09-02 |
| B′ | Certificate transparency shows 50 hosts on `p-aze-us` / `s-aze-us` / `d-aze-us`, a region code matching no AWS identifier, including `sdk-us08`, `subcenter-08` and `itp-api-08` | `data/subdomains.csv` | infrastructure | 2026-09-02 |

**Why they differ:** unknown from outside. A sub-processor list covers entities
processing personal data on the controller's behalf; an infrastructure provider may sit
outside that definition, be covered by another arrangement, or the document may simply
be behind the estate. All three are possible and none is visible from public sources.

**Ruling:** state the observations and stop. Say: **"Their sub-processor disclosure of
1 June 2026 names Amazon and Google as hosting providers. The IP addresses their own
documentation tells you to allowlist for the US-08 instance are all registered to
Microsoft, where every other instance's are registered to Amazon — and certificate
transparency shows fifty hosts on a matching region code. We do not know why the
disclosure and the infrastructure differ, and that is a question for them, not a
conclusion for us."** Do **not** say they failed to disclose: that is a legal conclusion
this evidence does not support.

---

### C-04 · Is the AI built or bought?

| | value | source | grade | as of |
|---|---|---|---|---|
| A | "BrazeAI™", "BrazeAI Decisioning Studio™", "BrazeAI™ Agents" are presented as Braze products | `data/site_inventory.csv` (`/product/brazeai`, `/product/brazeai-decisioning-studio`, `/product/ai-agents`) | claimed | 2026-09-01 |
| B | AI Decisioning Studio **is** OfferFit, Inc., acquired 2 June 2025 for $303.2m: "OfferFit, Inc. ('OfferFit') which is now known as AI Decisioning Studio" | `sources/filings/2026-03-25_10-K_000013.txt:1788,3130` | audited | 2026-03-25 |
| C | The models come from three external suppliers — Anthropic, OpenAI and Google — each disclosed as providing "artificial intelligence models and machine learning infrastructure" | `sources/clean/braze-subprocessors.md:22,31,34` | documented | 2026-09-02 |

**Why they differ:** they do not, strictly — a product can be acquired, renamed and
still be the vendor's product, and using foundation models from suppliers is ordinary
practice. The conflict is one of *impression*: the branding implies an in-house AI
programme, and the filings and the sub-processor list together describe an acquired
engine running on bought models.

**Ruling:** never say "their AI is thin" — the evidence does not support it and the
sentence is unfalsifiable. Say the sourced version: **"The decisioning engine is
OfferFit, bought in June 2025 for three hundred and three million dollars and renamed.
The models behind the AI features come from Anthropic, OpenAI and Google, all three
named in their own sub-processor disclosure. What Braze built is the integration."**
Then give the counts and let the audience judge.

---

### C-05 · Restated financial figures

| | value | source | grade | as of |
|---|---|---|---|---|
| A | `data/financials_restated.csv` — 0 rows | `data/financials_restated.csv` | audited | 2026-09-02 |

**Why they differ:** they do not. This entry exists because
[`EVIDENCE-GRADES.md`](EVIDENCE-GRADES.md) rule 6 requires that anything landing in
`financials_restated.csv` gets a conflict entry, and a reader needs to be able to check
that the file was looked at rather than forgotten.

**Ruling:** **"Across the twenty-nine key XBRL concepts tracked, no superseded value was
found — none of the figures in this deck has been restated."** Recorded as a negative
result, deliberately, because an unchecked absence and a checked one are different
things.

**Added 2026-09-02, in self-review.** The 10-K independently confirms the same negative:
Braze disclosed a material weakness in internal control over financial reporting, and
states that it "did not result in any identified misstatements to the financial
statements, and there were no changes to previously issued financial results". So the
mechanical check and the company's own disclosure agree. The material weakness is not a
conflict — it is a **caveat that travels with every financial figure**, recorded in
`FACTS.md` §2.1b and in Record chapter 2.1b. Say both halves together: the control
environment was judged not effective, and nothing was misstated or restated.

<!--
### C-01 · <question>

| | value | source | grade | as of |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

**Why they differ:**

**Ruling:**
-->
