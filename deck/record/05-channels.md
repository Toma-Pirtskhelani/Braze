# Channels and delivery

> Thirteen channels are documented, which is broad rather than narrow — but the documentation index and the marketing site have drifted apart in both directions at once, and the sub-processor disclosure shows that only two of the thirteen have a named delivery intermediary at all.

{{slides: 25, 27, 28}}

## 5.1 · The roster, counted from both ends

Braze's own documentation channel index lists twelve:

**In-product** — in-app messages, Content Cards, Banners.
**Out-of-product** — Email, Transactional email, Landing pages, LINE, Live notifications,
Push, SMS/MMS/RCS, Webhooks, WhatsApp.

[[documented]] {{src: sources/docs/docs__user_guide__channels.md:14-64 @ 2026-09-02}}

A thirteenth exists and is not on that list. **KakaoTalk** has four documentation pages —
setup, message creation, click tracking and reporting, a fully documented channel — and a
marketing product page at `/product/kakaotalk-messenger`. It is mentioned zero times on
Braze's own channels index.

The drift runs the other way too. Five documented channels have no dedicated marketing
product page anywhere on the site: **Banners, Transactional email, Landing pages, Live
notifications and Webhooks**. The largest of them is not small — Landing pages carries
eleven user-guide pages plus three partner pages, a substantial documented capability
that is sold under no name.

So the honest answer to "how many channels" is three different numbers depending on which
document you trust, which is why this is conflict **C-02**. The useful sentence is not
the count: *five documented channels have no marketing page, and one marketed channel is
missing from their own index.*

Investment also differs sharply by channel in a way the roster hides: `/product/line`
exists in four languages, `/product/kakaotalk-messenger` in two.

{{src: data/site_inventory.csv @ 2026-09-01}}

## 5.2 · Who actually delivers each channel

The sub-processor disclosure is legally compelled to be complete, which is what gives it
force. Revision 1 June 2026 names 17 third-party sub-processors.

| Channel | Named delivery sub-processor |
|---|---|
| Email | Three — Amazon SES, Bird.com (SparkPost), Twilio (SendGrid) |
| SMS / mobile messages | Two — Infobip, Twilio |
| Everything else | None named |

[[documented]] {{src: sources/clean/braze-subprocessors.md:21-37 @ 2026-09-02}}

Email has three delivery providers named, plus a fourth supplier, Mailgun, for Email on
Acid previewing. Mobile messages have two. **Push, in-app messages, Content Cards,
Banners, Webhooks, WhatsApp, LINE, KakaoTalk, Landing pages and Live notifications have
no delivery sub-processor named at all.**

The caveat travels in the same breath as the finding: absence from a sub-processor list
is not proof of no intermediary. Platform transports such as APNs and FCM, and the
WhatsApp, LINE and Kakao business APIs, may not be classified as sub-processors
processing personal data on Braze's behalf. What can be said is what the compelled
disclosure names — and it names middlemen for email and SMS, and for nothing else.

Read for what it says about resilience rather than about channels, the email arrangement
is the notable one: three interchangeable delivery providers for the highest-volume
channel is a deliberate redundancy, and a reasonable competitor should assume email
deliverability is not a single point of failure here.

## 5.3 · The rest of the supplier list, read for what it discloses

Beyond delivery, the same document discloses things no marketing page would:

- **Two hosting providers named** — Amazon Web Services, and Google LLC for Google Cloud
  Platform. What that omits is dealt with in chapter 4.
- **End-user profiles are stored by a third party.** Rackspace US, Inc. provides
  "Database Administration as a Service (DBaaS), a managed database service provider that
  **hosts and stores End User profiles**."
- **Monitoring receives user identifiers.** "Braze may provide End User metadata, such as
  user identifiers, to DataDog for support and application troubleshooting."
- **Three foundation-model suppliers** — Anthropic, OpenAI and Google — dealt with in
  chapter 6.
- Databricks, dbt Labs, Domino Data Lab, ClickHouse, Snowflake, Cloudflare and Fastly
  make up the remainder: analytics, transformation, CDN and traffic management.

Braze separately claims "over 150 technology partners, which we call 'Alloys'". That is a
marketing figure appearing inside technical documentation and is graded accordingly.
[[claimed]] {{src: sources/docs/docs__developer_guide__getting_started__architecture_overview.md:82 @ 2026-09-02}}

#### What would change this chapter

A revision of the sub-processor document — this record uses 1 June 2026 and any later
revision supersedes it entirely. A new channel appearing in the docs index, or KakaoTalk
being added to it. A marketing page appearing for any of the five unmarketed channels,
which would close the drift rather than resolve it.
