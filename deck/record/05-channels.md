# Channels and delivery

> Thirteen channels are documented, which is broad rather than narrow — the hypothesis that Braze's channel list would prove thinner than its positioning was killed by the evidence. What the roster does show is a documentation site and a marketing site that have drifted apart in both directions at once, and a compelled disclosure showing that only two of the thirteen channels have a named delivery intermediary at all.

{{slides: 26, 28, 29}}

## 5.1 · The roster, counted from both ends

Braze's own documentation channel index lists twelve:

**In-product** — in-app messages, Content Cards, Banners.
**Out-of-product** — Email, Transactional email, Landing pages, LINE, Live notifications,
Push, SMS/MMS/RCS, Webhooks, WhatsApp.

[[documented]] {{src: sources/docs/docs__user_guide__channels.md:14-64 @ 2026-09-02}}

A thirteenth exists and is not on that list. **KakaoTalk** has four documentation pages —
setup, message creation, click tracking and reporting, which is a fully documented channel
rather than a stub (`sources/docs/docs__user_guide__channels__kakaotalk__*.md`) — and a
marketing product page at `/product/kakaotalk-messenger`, in `data/site_inventory.csv`. It is
mentioned zero times on Braze's own channels index.

The drift runs the other way too. Five documented channels have no dedicated marketing
product page anywhere on the site: **Banners, Transactional email, Landing pages, Live
notifications and Webhooks**. The largest of them is not small — Landing pages carries
eleven user-guide pages plus three partner pages
(`sources/docs/docs__user_guide__messaging__landing_pages*.md`), a substantial documented
capability sold under no name.

### Why the drift is the finding, not the count

The honest answer to "how many channels does Braze have" is three different numbers
depending on which document you trust, which is why this is conflict **C-02**. But the
count is the least interesting thing here.

A documentation site and a marketing site are maintained by different people on different
cadences, and the gap between them is a reliable measure of which parts of a product the
company is currently *selling* versus which parts it merely *supports*. On that reading:

- **Landing pages, Banners, Transactional email, Live notifications and Webhooks are
  supported but not sold.** Eleven documentation pages exist for landing pages because
  customers use them and need help; no marketing page exists because landing pages are not
  how Braze wins a deal against Salesforce. These are retention features, not acquisition
  features, and their documentation-to-marketing ratio says so.
- **KakaoTalk is sold but not indexed**, which is the rarer direction and more likely an
  oversight than a strategy — a channel added to the marketing taxonomy and missed when
  the docs index was last revised.

Investment also differs sharply by channel in a way the roster hides. `/product/line`
exists in four languages; `/product/kakaotalk-messenger` in two. Both are East Asian
messaging channels; one has had twice the localisation attention. For anyone competing in
Korea specifically, that ratio is a more honest signal of commitment than either channel's
presence on a list.

{{src: data/site_inventory.csv @ 2026-09-01}}

### The hypothesis this killed

The analysis went in expecting the channel list to be narrower than the positioning
implied — the usual finding when a vendor claims omnichannel. It is not. Thirteen
documented channels including WhatsApp, LINE, KakaoTalk, RCS, Banners, Landing pages, Live
notifications and Webhooks is a genuinely broad set, broader than several of the
specialists buyers shortlist Braze against (chapter 7). **Recorded as killed, in Braze's
favour**, because a hypothesis quietly dropped is a bias.

### The roster measured, not just listed

A channel list says nothing about how much of each channel exists. The documentation
corpus can be counted the same way chapter 6 counts the AI, and the result orders the
roster by how much Braze has had to explain.

| Channel | Focused doc pages | API endpoints |
|---|---|---|
| Email | 347 | 16 |
| In-app messages | 115 | 0 |
| SMS / MMS / RCS | 89 | 2 |
| Push (mobile) | 73 | 1 |
| Webhooks | 71 | 2 |
| WhatsApp | 56 | 0 |
| Content Cards | 47 | 0 |
| Banners | 28 | 0 |
| Landing pages | 21 | 0 |
| LINE | 11 | 0 |
| Web push | 11 | 0 |
| Live notifications | 8 | 2 |
| KakaoTalk | 5 | 0 |
| Transactional email | 4 | 1 |

[[documented]] {{src: data/capabilities.csv @ 2026-09-02}}

Three readings come out of this table that the roster alone cannot give you.

**The distribution is extremely uneven.** Email at 347 focused pages is more than the next
three channels combined, and roughly seventy times KakaoTalk's five. "Thirteen channels" is
true and it describes a set in which one channel is the product and twelve are
completeness.

**Depth tracks marketing, with two exceptions that go opposite ways.** Broadly the
best-documented channels are the marketed ones — but **Webhooks at 71 pages is the fifth
deepest channel in the platform and has no marketing page at all**, while **KakaoTalk at 5
pages has one**. Webhooks is a genuinely substantial, genuinely unmarketed capability;
KakaoTalk is marketed at roughly the documentation depth of a stub. If you are judging what
Braze can actually do from its product pages, those are the two places you would be most
wrong in each direction.

**Channel breadth is not channel parity, and nobody should present it as such.** A prospect
in Korea evaluating KakaoTalk support is looking at five focused pages and no API
endpoints. A prospect asking about LINE is looking at eleven. Those channels exist and are
real, and they are not comparable to what an email or push buyer receives. The fair
sentence is that Braze covers thirteen channels and covers three of them deeply.

## 5.2 · Who actually delivers each channel

The sub-processor disclosure is legally compelled to be complete, which is what gives it
force. Revision 1 June 2026 names 17 third-party sub-processors.

| Channel | Named delivery sub-processor |
|---|---|
| Email | Three — Amazon SES, Bird.com (SparkPost), Twilio (SendGrid) |
| SMS / mobile messages | Two — Infobip, Twilio |
| Everything else | None named |

[[documented]] {{src: sources/clean/braze-subprocessors.md:21-37 @ 2026-09-02}}

Email has three delivery providers named, plus a fourth supplier — Mailgun — for Email on
Acid previewing (`sources/clean/braze-subprocessors.md:21-37`). Mobile messages have two. **Push, in-app messages, Content Cards,
Banners, Webhooks, WhatsApp, LINE, KakaoTalk, Landing pages and Live notifications have no
delivery sub-processor named at all.**

### What that absence does and does not mean

The caveat travels in the same breath as the finding, because the finding is easy to
misuse. Absence from a sub-processor list is **not** proof of no intermediary. Platform
transports such as APNs and FCM, and the WhatsApp, LINE and Kakao business APIs, may not
be classified as sub-processors processing personal data on Braze's behalf — a message
handed to Apple for delivery to a device may sit outside the definition entirely. What can
be said is what the compelled disclosure names, and it names middlemen for email and SMS
and for nothing else.

Two conclusions do survive that caveat, and both are commercially useful.

**Email deliverability is not a single point of failure.** Three interchangeable providers
on the highest-volume channel is deliberate redundancy, and it is expensive to maintain —
three sets of IP reputation, three integrations, three contracts. A competitor hoping to
attack Braze on email reliability is attacking the part of the estate that has been
engineered hardest against exactly that. This is a favourable finding and it comes from a
document Braze had no marketing reason to publish.

**The in-product channels are genuinely Braze's own.** In-app messages, Content Cards and
Banners are rendered by Braze's SDK inside the customer's own application. There is no
carrier, no inbox provider, and no third party in the path — which is why no sub-processor
is named for them, and why those channels are the ones least exposed to a supplier
relationship going wrong. It is also why they are the channels where Braze's latency story
is strongest, since nothing leaves the device-to-Braze path.

## 5.3 · The rest of the supplier list, read for what it discloses

Beyond delivery, the same document discloses things no marketing page would.

- **Two hosting providers named** — Amazon Web Services, and Google LLC for Google Cloud
  Platform. What that omits is chapter 4's subject and the most significant single finding
  in this analysis.
- **End-user profiles are stored by a third party.** Rackspace US, Inc. provides "Database
  Administration as a Service (DBaaS), a managed database service provider that **hosts and
  stores End User profiles**." A buyer doing a security review should know that the profile
  store is operated by a managed-database vendor rather than by Braze directly — and the
  10-K independently confirms it, naming Rackspace alongside AWS as infrastructure (`sources/filings/2026-03-25_10-K_000013.txt`) Braze
  relies on.
- **Monitoring receives user identifiers.** "Braze may provide End User metadata, such as
  user identifiers, to DataDog for support and application troubleshooting." That is
  ordinary practice, disclosed properly, and it is the kind of line a data-protection
  officer will ask about.
- **Three foundation-model suppliers** — Anthropic, OpenAI and Google — dealt with in
  chapter 6.
- Databricks, dbt Labs, Domino Data Lab, ClickHouse, Snowflake, Cloudflare and Fastly make
  up the remainder: analytics, transformation, CDN and traffic management.

Braze separately claims "over 150 technology partners, which we call 'Alloys'". That is a
marketing figure appearing inside technical documentation and is graded accordingly.
[[claimed]] {{src: sources/docs/docs__developer_guide__getting_started__architecture_overview.md:82 @ 2026-09-02}}

### The shape of the integration layer, measured

The partner network can be measured rather than accepted. The documentation corpus carries
**322 partner pages** — the second-largest section by page count — averaging about 810
words each, against a developer guide that runs more than three times as many words per
page across a third as many pages (chapter 4). Both counts come from
`data/docs_sections.csv`, produced by `tools/index_docs.py`.

That is the documentation profile of a broad network described one short page at a time.
It is not a criticism: a connector may need only a short page, and 322 of them is a real
network that takes real effort to maintain. But it does mean the integration layer is
**wide and shallow in documentation terms**, and anyone told the integration story is deep
should measure it this way rather than counting logos. The depth is in the SDKs and the
API, which is where the words actually are.

#### What would change this chapter

A revision of the sub-processor document — this record uses revision 1 June 2026 and any
later revision supersedes it entirely, particularly if it adds or removes a delivery
provider. A new channel appearing in the docs index, or KakaoTalk being added to it, which
would close half of C-02. A marketing page appearing for any of the five unmarketed
channels, which would tell you Braze had decided to start selling one of them. And any
change to the three-provider email arrangement, which would be visible in the same
disclosure and would matter more than it sounds.
