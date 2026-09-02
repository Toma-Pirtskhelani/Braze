# The platform

> Braze's documentation is markedly more honest than its marketing about what the platform will and will not do, and the limits it admits are commercial as much as technical: three of four ingestion paths are labelled "not real-time" by Braze itself, the endpoint that reads user profiles back out was cut tenfold for customers who joined after August 2024, and the billing unit is the individual attribute write.

{{slides: 1, 17, 18, 19, 20, 21, 22, 23, 24, 26, 29, 30, 34, 37, 38, 41}}

## 4.1 · The corpus this chapter rests on

| Fact | Value | Grade | Source |
|---|---|---|---|
| Documentation pages captured | 1,352 | [[documented]] | `data/docs_index.csv` |
| Words in the corpus | 1,565,479 | [[documented]] | `data/docs_sections.csv` |
| Documented REST endpoints | 135, across 28 top-level namespaces | [[documented]] | `data/api_endpoints.csv` |
| Public repositories | 137 | [[documented]] | `data/repos.csv` |

The corpus is shaped unevenly, and the shape is itself informative: 696 user-guide pages,
322 partner pages, 200 API pages, 106 developer-guide pages. The developer guide averages
about 2,700 words a page; the partner section averages about 810. The integration
network is broad and documented shallowly — a lot of short pages, one per partner.

{{src: data/docs_sections.csv @ 2026-09-02}}

## 4.2 · How fresh the data is — their table, not ours

Braze publishes a comparison of its four ingestion paths and grades each one's latency
itself. This is the single most load-bearing table in the corpus.

| Path | Braze's own latency description |
|---|---|
| Standard Cloud Data Ingestion sync | "Not real-time; minimum 15-minute sync cadence" |
| CDI Segments (Connected Sources) | "Not real-time; refreshes on your Segment Extension schedule" |
| CDI Canvas triggers | "Not real-time; bounded by sync schedule (minimum 15 minutes)" |
| `/users/track` and the SDKs | "Near-real-time (async processing)" |

[[documented]] {{src: sources/docs/docs__user_guide__example_library__data__compare_data_ingestion_options.md:86-90 @ 2026-09-02}}

Three of the four are labelled not real-time by the vendor. The fourth is qualified as
near-real-time with asynchronous processing. Warehouse syncs "can run from every 15
minutes to once per month", and going faster than fifteen minutes is not self-serve:
"contact your customer success manager or use REST API ingestion."

This is the substance of conflict **C-01**. The 10-K describes "high-volume, continuous
streaming of user data to be processed in real time" and the developer guide says "the
platform can handle any data in real time" — both true of the SDK and API path. The
correct sentence is not that Braze overstates, but that the word covers two
architectures: if your customer data lives in a warehouse, fifteen minutes is the floor
unless you move to the API.

Other admitted ceilings on the same page: 75 objects per `/users/track` request combined
across attributes, events and purchases; a 60-minute query runtime cap per connected
source; approximately 3.75 million Canvas entries per hour per sync run. Currents, the
streaming export, is "an optional Braze add-on" that exports "every five minutes, or
every 15,000 events, whichever comes first."

## 4.3 · Data in versus data out

| Direction | Endpoint | Limit |
|---|---|---|
| In | `/users/track` | 3,000 requests per 3 seconds for customers with data points in their pricing — 60,000 a minute — at 75 objects each |
| Out, by identifier | `/users/export/ids` | **250 requests per minute** if onboarded on or after 22 August 2024; **2,500** if before |
| Out, in bulk | `/users/export/segment` | The default 250,000 requests per hour |

[[documented]] {{src: sources/docs/docs__api__api_limits.md:29-39 @ 2026-09-02}}

Two things here, and the second is the interesting one.

The asymmetry is real but must be stated fairly. Writing can reach roughly 4.5 million
objects a minute; reading profiles back by identifier is capped at about 12,500 profiles
a minute for a customer who joined after August 2024, at 50 identifiers per request.
Those are different operations — writing event objects against reading whole profiles —
so the ratio shows where the design and commercial priority sits, not a like-for-like
throughput comparison. And bulk export exists and is generously limited, so this is not a
data-lock-in story and should not be told as one.

The dated boundary is the finding. On 22 August 2024 the profile-lookup limit was cut by
a factor of ten for new customers, and existing customers kept the old limit. Two
customers on the same product, doing the same thing, are subject to limits an order of
magnitude apart depending on when they signed. Braze documents this openly in a table.
Why it changed, and whether anyone was told, is open question 55.

## 4.4 · What it is built on

| Fact | Value | Grade | Source |
|---|---|---|---|
| Named backing stores | Snowflake, Kafka, MongoDB, Redis | [[documented]] | `sources/docs/docs__developer_guide__getting_started__architecture_overview.md:32` |
| MongoDB-backed | Custom events, custom attributes, user profiles, purchases, most segmentation | [[documented]] | `…architecture_overview.md:46-56` |
| Snowflake-backed | SQL Segment Extensions, Prediction Suite, AI Personalized Item Recommendations, Estimated Real Open Rate | [[documented]] | `…architecture_overview.md:58-68` |
| Regional clusters | 15: US 01–08, US 10, EU 01–02, AU 01, ID 01, JP 01, KR 01 | [[documented]] | `data/status_components.csv` |
| Subsystems per cluster | 7, identical in every one | [[documented]] | `data/status_components.csv` |

The status page is an architecture disclosure the vendor made by accident. Every cluster
exposes the same seven subsystems — Dashboard, SDK Data Collection, Data Processing,
REST APIs, Outbound Messaging, Currents, Cloud Data-Ingestion — which is a functional
decomposition of the product, published live and updated during outages. Note that
Currents and CDI are first-class per-cluster subsystems rather than features.

The cluster geography is corroborated independently: the sub-processor disclosure lists
AWS regions for the United States, European Union, Australia, Indonesia (with backup in
Singapore), Japan and South Korea — the same six geographies the cluster names use.
Channel delivery is modelled differently, as a single global group rather than per
cluster. There is no US 09; the US clusters run 01 to 08 and then 10.

The customer-visible consequence of the architecture is not the clusters. It is the
storage split, and Braze flags it themselves under an "important" callout: **"Removing
data from one system does not automatically remove it from the other."** Erroneous
custom-event data must be addressed in MongoDB, separately from anything Snowflake-backed.
For a buyer with deletion obligations, that is a two-system problem stated in the
vendor's own documentation.

{{src: sources/docs/docs__developer_guide__getting_started__architecture_overview.md:70 @ 2026-09-02}}

## 4.5 · One instance is not on the same cloud as the others

This is the clearest result the method produced, and it comes from three sources that
have nothing to do with each other.

- The sub-processor disclosure of 1 June 2026 names exactly two hosting providers:
  Amazon Web Services, and Google LLC for Google Cloud Platform. Microsoft is not named
  anywhere in the document. [[documented]]
- A **second, independent company document** says the same thing. The 10-K risk factors
  state: "We rely upon third-party providers of cloud-based infrastructure, **including
  Amazon Web Services and Rackspace**, to host our products." Microsoft is not named
  there either. [[audited]]
- Braze's own documentation publishes, per instance, the IP addresses a customer must
  allowlist so Braze can reach their warehouse. Every address listed for **US-08** is
  registered to **Microsoft Corporation**. Every address listed for every other instance
  — US-10, AU-01, ID-01, JP-01, KR-01 and the generic US block — is registered to an
  Amazon entity. The check covered every instance for which Braze publishes a list.
  [[infrastructure]]
- Certificate transparency shows 50 hosts on region codes `p-aze-us`, `s-aze-us` and
  `d-aze-us` — a code matching no AWS region identifier, where every other code in the
  estate does. Hosts on it include `sdk-us08`, `subcenter-08` and `itp-api-08`, tying
  the code to instance 08. [[infrastructure]]

{{src: sources/external/rdap-instance-ip-ownership_2026-09-02.json @ 2026-09-02}}
{{src: sources/docs/docs__user_guide__data__unification__cloud_ingestion__connected_sources.md:239 @ 2026-09-02}}

State the three observations and stop. A hosting arrangement may sit outside a
sub-processor listing for reasons not visible from outside, the document may be behind
the estate, or there may be an explanation nobody external can see. Asserting a
disclosure failure would be a legal conclusion this evidence does not support. The
question — why the disclosure and the infrastructure differ — is recorded as open
question 52 and as conflict **C-03**.

Note also that the certificate-transparency host list is **partial**: crt.sh returned
HTTP 502 throughout and the Cert Spotter fallback was rate-limited without a token. No
claim is made here that anything is *absent* from CT, because the list was not
exhaustive.

## 4.6 · Identity, and where it is quietly lossy

| Fact | Value | Grade | Source |
|---|---|---|---|
| Aliases per profile | No limit | [[documented]] | `sources/docs/docs__user_guide__data__unification__user_data__user_profile_lifecycle.md:106` |
| Aliases per label | One, and unique across the user base | [[documented]] | `sources/docs/docs__api__endpoints__user_data__post_user_identify.md:32` |
| Identifiers accepted on ingest | Five: external_id, user alias, braze_id, email, phone | [[documented]] | `…compare_data_ingestion_options.md:113-118` |
| Identifiers accepted for warehouse segmentation | One: `external_user_id` only | [[documented]] | `…compare_data_ingestion_options.md:113-118` |

The identity model is generous at the top and narrow at the bottom: unlimited aliases on
a profile, but a warehouse-driven segment can only be built on a single identifier type.

Two admitted behaviours deserve a buyer's attention because neither is visible from
marketing and both fail quietly.

**A merge can decline and still report success.** If both profiles carry invalid phone
numbers Braze does not merge them, and their documentation says so directly: "The
endpoint still returns 202 Accepted with a success message, so the HTTP response does not
indicate that the merge was skipped."

**Reporting splits across surfaces after a merge.** Dashboard campaign summaries
attribute a pre-merge send to the surviving profile; Currents, Query Builder and
Messaging History still attribute it to the orphaned profile's ID. Both are correct by
their own rules and they do not agree, which is a reconciliation problem for anyone
joining Braze data to a warehouse. Orphaned profiles are also not eligible to receive
messages.

{{src: sources/docs/docs__api__endpoints__user_data__post_users_merge.md:178 @ 2026-09-02}}

## 4.7 · What a customer is billed for

The billable unit is defined in the documentation with contract-grade precision: a "data
point" is "a billable unit of use of the Braze Services, measured by a session start,
session end, custom event, or purchase recorded, as well as any attribute set on an end
user profile", and each such item "shall each count as a single data point". A session
start and a session end are two.

Engagement is explicitly *not* billed — push tokens, device information, and all campaign
engagement tracking such as email opens and push clicks are excluded, as are user
deletion, Connected Content, subscription-state changes and external-ID renames. That is
a genuinely customer-friendly boundary and belongs in any fair account of the pricing.

The tension is in the advice Braze gives alongside it: **"Don't waste data points. Only
update changing data!"**, and "we recommend setting up a program to prevent sending the
same unchanging data." A platform positioned on continuous streaming of behavioural data
prices in a way that makes its customers build programmes to send less of it. Both facts
are theirs; the tension between them is the finding, and it is corroborated from an
unrelated direction by a Gartner reviewer citing "steep pricing and strict data-point
limits, where overages can become expensive very quickly" (chapter 7).

{{src: sources/docs/docs__user_guide__data__infrastructure__data_points.md:18,20,36-38 @ 2026-09-02}}

## 4.8 · A decade of reliability, and an engineering record

| Fact | Value | Grade | Source |
|---|---|---|---|
| Incidents published | 451, 2016-10-09 → 2026-08-05 | [[documented]] | `data/incidents.csv` |
| Median duration | 79 minutes | [[documented]] | `data/incidents.csv` |
| p90 duration | 311 minutes | [[documented]] | `data/incidents.csv` |
| Major or critical | 98 of 331 non-maintenance incidents — 29.6% | [[documented]] | `data/incidents.csv` |
| Public issues captured | 845, all from non-members of the org | [[documented]] | `data/issues.csv` |
| Issues closed | 822 — 97.3% — median 11 days | [[documented]] | `data/issues.csv` |

Incidents peaked in 2023 at 60 and fell to 27 in 2025, the quietest full year on the
status page, over a period when revenue grew 7.7 times. Incident rate per unit of scale
has fallen sharply, which kills the hypothesis that it would rise. The caveat travels
with it: 2026 stands at 35 through August, roughly double the 2025 monthly rate.

The component distribution has a shape worth naming. The Dashboard appears in 63
incidents, more than any other component and more than twice Outbound Messaging's 27.
The control plane that marketers use fails more often than the sending path.

None of this may be compared against a vendor that publishes no status page. A decade of
visible incidents is a disclosure practice, not a defect count, and a competitor with
silence has not thereby earned a better record.

On the engineering side the record is straightforwardly good. All nine SDK repositories
that publish releases shipped within thirteen days of capture. The one platform whose
repository is archived — Unreal — has had its documentation removed entirely, so the
marketing and the maintenance agree. The single soft spot is `braze-roku-sdk`: 181 days
since its last push while 38 Roku documentation pages remain live. And 845 unsolicited
public issues closed at 97.3% with a median of 11 days is a real operational number that
Braze does not control the denominator of.

The issue corpus describes the SDK surface, not the dashboard, and its authors are
developers rather than buyers. It is not a satisfaction measure and is not used as one.

#### What would change this chapter

A revised sub-processor list naming Microsoft would resolve §4.5 in one direction; a
statement that US-08 is something other than an Azure deployment would resolve it in
another. A change to the documented rate limits, or the removal of the two-tier export
limit, would date §4.3. Two consecutive quiet quarters would make the 2026 incident
uptick noise; two more like April 2026 would make it a trend.
