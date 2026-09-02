---
url: https://www.braze.com/docs/user_guide/channels/email/reporting/analytics_glossary
slug: docs__user_guide__channels__email__reporting__analytics_glossary
title: "Email analytics glossary"
description: "This glossary includes the terms you will find in the analytics section of your email campaign or Canvas, post-launch. This glossary does not include Currents..."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Email analytics glossary

These are terms you'll find in the analytics section of your email campaign or Canvas, post-launch. You can search for the metrics you need or filter by the type of metric. This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account.

 Search glossary

This glossary defines metrics on the Analytics tab for email campaigns and Canvases. Braze doesn’t offer a hosted “view this email in a browser” page—see Can I add a “view this email in a browser” link to my emails? for a workaround. For other troubleshooting that spans multiple metrics, see Email FAQ.

### Variation

Variation is the number of variations of a campaign, differing as defined by the creator.

Calculation: Count

### Emailable

Emailable is the total number of users who have an email address on record and have explicitly opted in or subscribed.

Calculation: Count

### Audience %

Audience is the percentage of users who received a particular message. This number is received from Braze.

Calculation: (Number of Recipients in Variant) / (Unique Recipients)

### Unique Recipients

Unique Recipients is the number of unique daily recipients, or users who received a new message in a day. For this count to increment for a user more than once, the user must receive a new message on a different day.

This number is received from Braze.

Calculation: Count

### Sends

Sends is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent.

This metric is provided by Braze.

Calculation: Count

### Messages Sent

Messages Sent is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent.

This metric is provided by Braze.

Calculation: Count

### Deliveries

Deliveries is the total number (or percentage) of message requests that are accepted by the receiving server. This doesn’t mean the message was delivered to a device, only that the message was accepted by the server.

For emails, Deliveries is the total number of messages (Sends) successfully sent to and received by emailable parties.

Calculation: (Sends) - (Bounces) 

note

For user-level received state and related logic (such as frequency capping), Braze generally marks a user when the send is processed and handed off for delivery—not when the email service provider (ESP) confirms final delivery to the inbox. That avoids timing gaps between ESP confirmation and in-product rules. It may differ from ESP- or third-party delivery reports.

### Deliveries %

Deliveries % is the percentage of total number of messages (Sends) successfully sent to and received by emailable parties.

Calculation: (Sends - Bounces) / (Sends) 

### Bounces

Bounces is the total number of messages that were unsuccessfully delivered to the intended recipients.

For email, Bounce % or Bounce Rate is the percentage of messages that were unsuccessfully sent or designated as “returned” or “not received” from send services used or not received by the intended emailable users.

An email bounce for customers using SendGrid consists of hard bounces, spam (spam_report_drops), and emails sent to invalid addresses (invalid_emails).

note

In Braze Currents, temporary ESP deferrals are often represented as soft bounces. Deliverability tools (for example, native SendGrid reporting or Looker models) may use deferrals for the same situation. Deferrals are usually temporary, and mail is often delivered after retries. After extended retries (up to roughly 72 hours for soft bounces in campaign analytics), a message may be treated as undeliverable depending on your ESP. Currents email events are append-only—a logged soft bounce is not removed later if the message eventually delivers.

 Calculation:

- Bounces: Count
 
- Bounce % or Bounce Rate %: (Bounces) / (Sends)

### Hard Bounce

A Hard Bounce is when an email fails to deliver to the recipient due to a permanent delivery error. A hard bounce might occur because the domain name doesn’t exist or because the recipient is unknown.

When an email hard bounces or is marked as spam, Braze marks the email address as invalid but does not update the user’s subscription status. Braze stops any future sends to that email address. To remove an email address from your hard bounce list, use the Remove hard bounced emails endpoint.

Calculation: Count 

### Soft Bounce

A Soft Bounce is when an email fails to deliver to the recipient due to a temporary delivery error, even though the recipient’s email address is valid. A soft bounce might occur because the recipient’s inbox is full, the server was down, or the message was too large for the recipient’s inbox.

If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver.

While soft bounces aren’t tracked in your campaign analytics, you can monitor the soft bounces in the Message Activity Log or exclude these users from your sending with the Soft Bounced segment filter. In the Message Activity Log, you can also see the reason for the soft bounces and understand possible discrepancies between the “sends” and “deliveries” for your email campaigns.

Calculation: Count 

### Spam

Spam is the total number of emails delivered that were marked as “spam” by the recipient. While Braze doesn’t change the subscription state of these users, these users will be automatically excluded in future emails, unless you’re sending a transactional email, which is configured to “send to all users including unsubscribe”.

 Calculation:

- Spam: Count
 
- Spam % or Spam Rate %: (Marked as Spam) / (Sends)

### Unique Opens

Unique Opens is the total number (or percentage) of delivered messages that have been opened by a single user at least once and are tracked over a seven-day period.

For email, this is tracked over a seven-day period. This means a single user who opens the same email again after seven days counts as a new unique open. As a result, dashboard unique open counts may be higher than a simple DISTINCT user_id query on Currents data. To match dashboard counts from Currents, filter for events where is_unique is true.

 Calculation:

- Unique Opens: Count
 
- Unique Opens % or Unique Open Rate: (Unique Opens) / (Deliveries)

### Unique Clicks

Unique Clicks is the distinct number of recipients who have clicked a link within a message at least once and is measured by dispatch_id.

This is tracked over a seven-day period for email and measured per dispatch_id (a single send attempt). This includes clicks on Braze-provided unsubscribe links. Tracked custom unsubscribe URLs also count toward Unique Clicks when a user selects the link. After seven days, another unique click counts for the same user if they click again. Dashboard email engagement metrics, including Unique Clicks, are calculated in Braze and are not reconciled from ESP aggregate reports. To match dashboard counts from Currents, filter for events where is_unique is true.

 Calculation:

- Unique Clicks: Count
 
- Unique Clicks % or Click Rate: (Unique Clicks) / (Deliveries)

#### Unexpected links on the email heatmap

When the email heatmap shows links you do not expect, inspect the message HTML for content blocks or spacing between words that create tracked URLs. Use the Link Table by Total Clicks on the heatmap view to identify URLs that do not match visible copy.

Braze does not expand Liquid tags in the message preview, so the heatmap renderer cannot match the clicked link in the preview. This is expected behavior. The heatmap renderer attempts to match clicked URLs with those in the message. When the URL is significantly different, such as when the entire URL is passed in as an event property, the heatmap cannot identify it.

### Total Clicks

Total Clicks is the total number of times users clicked links in the delivered email, including multiple clicks by the same user. This includes clicks on Braze unsubscribe links and tracked custom unsubscribe URLs.

When Total Clicks is much higher than Unique Clicks, security tools or mailbox providers scan links without users opening the message. Compare Unique Clicks when you evaluate engagement internally.

### Unsubscribers or Unsub

Unsubscribes reflect the standard unsubscribe link for Braze. Custom unsubscribe pages won’t increment this metric unless you update users using the API. Subscription Group Timeseries still reflects API-driven changes.

Unsubscribers or Unsub is the number of messages resulting in an unsubscription. Unsubscriptions occur when Braze processes an unsubscribe from the Braze unsubscribe URL in the message body or from the list-unsubscribe header when that path is handled by Braze.

 Calculation:

- Unsubscribers or Unsub: Count
 
- Unsubscribers % or Unsub Rate: (Unsubscribes) / (Deliveries)

#### Why Unsubscribes and unsubscribe-link clicks can differ

On the Analytics page for an email campaign or Canvas, compare the Unsubscribes count to clicks on the Braze unsubscribe URL in the per-link breakdown when you expand Total Clicks or Unique Clicks. The two often match but can differ:

- More Unsubscribes than clicks on the body unsubscribe URL: List-unsubscribe is an additional unsubscribe path in the email header (not the link in your message body). When a user unsubscribes that way, it counts toward Unsubscribes but does not count as a click on the tracked unsubscribe URL in the body.
 
- More clicks on the body unsubscribe URL than Unsubscribes: A user may select that link more than once. If they unsubscribe, resubscribe, and unsubscribe again, email analytics can record multiple clicks (for example, two) in the click breakdown.

For more information, see Why am I seeing a different number of unsubscribes than clicks on my unsubscribe link?.

### Revenue

Revenue is the total revenue in dollars from campaign recipients within the set primary conversion window.

Calculation: Count 

### Primary Conversions (A) or Primary Conversion Event

Primary Conversions (A) or Primary Conversion Event is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by you when building the campaign.

For email, push, and webhooks, we start tracking conversions after the initial send.

 Calculation:

- Primary Conversions (A) or Primary Conversion Event: Count
 
- Primary Conversions (A) % or Primary Conversion Event Rate: (Primary Conversions) / (Unique Recipients)

### Confidence

Confidence is the percentage of confidence that a certain variant of a message is outperforming the control group.

### Machine Opens

Machine Opens includes both non-human and human opens that indicate an open by an Apple Mail Privacy Protection (MPP)-enabled user. This means that a user can log multiple Machine Opens. Machine Opens are not automatically generated if the device isn’t connected to Wi-Fi, so a user can potentially open an email in the Apple Mail app before Apple pre-fetches images, which still results in a Machine Opens.

For MPP-enabled users:

- 1+ Machine Open: Apple pre-fetched the message or the user proactively opened an email on an iOS device
 
- 2+ Machine Opens: Braze does not have visibility into human versus non-human opens, so this may be made up of multiple human opens (across one Apple device or multiple) or a combination of human opens and 1 open associated with Apple pre-fetching the message

This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.

Calculation: Count 

### Other Opens

Other Opens includes human opens that are not impacted by MPP (such as a user opening an email in the Gmail app or on Gmail desktop, which subsequently fires a tracking pixel and logs a regular open). Other Opens are typically human opens, but there could also be scenarios where a machine opens the mail (a bot or an inbox service provider like Gmail or Yahoo). It is also possible for a user to open an email on a non-iOS device and log the Other Open before a Machine Open is logged.

Because Machine Opens can be user-driven, the relationship between Machine Opens and Other Opens is not human versus non-human, but rather, MPP-impacted versus not MPP-impacted. While Other Opens can still be relied on to measure some portion of human opens, it’s not currently possible to determine the percentage of Machine Opens that are human-driven, so determining a precise “true” open rate is not currently possible.

For MPP-enabled users:

- +1 Other Open(s): The user proactively opened an email on a non-iOS device
 
- +1 Machine Open(s) and +1 Other Opens: Apple pre-fetched the message or the user proactively opened an email on an iOS device and proactively opened an email on a non-iOS device

For non-MPP-enabled users:

- +1 Other Open(s): The user proactively opened an email on any device

Note that a user can also open an email (such as the open counts toward Other Opens) before a Machine Opens count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward Other Opens and only once toward Unique Opens.

Calculation: Count 

### Estimated Real Opens

Estimated Real Opens is an estimate of how many unique opens there would be if machine opens did not exist, and is the result of a proprietary Braze statistical model.

Braze recalculates this estimate as new open and click data arrives. The value typically stabilizes a few days after send but continues to update when new qualifying events occur.

### Click-to-Open Rate

Click-to-Open Rate is the percentage of opened emails that have been clicked by a single user or machine at least once, and is only available in the Report Builder.

Calculation: (Unique Clicks) / (Unique Opens) (for Email)

#### Message Open Likelihood scores (segmentation)

The Message Open Likelihood segment filter scores how likely a user is to open email on a scale of 0–100%. Users without enough send or open history for the channel appear as blank. For email, machine opens are excluded from the calculation, which uses recent message history on that channel (see Message Open Likelihood filter for individual channels).

## Email reporting troubleshooting and FAQs

### Unsubscribe links and Unique Clicks

When a recipient clicks an unsubscribe link, Braze counts it as a click because the action uses a URL. This applies to Braze-provided unsubscribe links and custom unsubscribe links in your message body. Those clicks contribute to Unique Clicks and Total Clicks alongside other link clicks. For metric definitions, see Unique Clicks and Why am I seeing a different number of unsubscribes than clicks on my unsubscribe link?.

### View in browser

Braze does not include a built-in “View this email in a browser” feature. Host the email content on an external landing page (such as your website) and add a link from the message using the email editor Link tool. For more information, see Can I add a “view this email in a browser” link to my emails?.

### Custom unsubscribe page updates

Changes to your custom unsubscribe page appear within a few minutes. Live sends use a short-lived cache of the page that’s refreshed when you save changes.

### Over-quota and full mailbox bounces

An over-quota or mailbox-full bounce means the recipient’s mailbox cannot accept new mail. You may see these addresses among new sign-ups with invalid or risky addresses, or among long-inactive profiles whose inboxes filled while they were dormant.

Review bounce rates by segment and source, remove or sunset addresses that repeatedly hard-bounce, and use confirmed or double opt-in for new subscribers. For list hygiene practices, see Deliverability pitfalls and spam traps and Email reporting.

### 550 5.7.1 unsolicited mail

A 550 5.7.1 response such as “Our system has detected that this message is likely unsolicited mail” often comes from strict mailbox providers (for example, Gmail) when reputation or engagement signals look poor. Common contributors include spam complaints, low engagement, purchased or rented lists, and sudden volume spikes.

Focus on consent-based list growth, sunset inactive subscribers, and monitor complaint and bounce rates. For more information, see Deliverability pitfalls and spam traps.

### Good email deliverability rates

Delivery is whether the receiving server accepts your message; you can measure it with metrics such as Deliveries and bounce rate. Deliverability (inbox placement) depends on provider filtering and isn’t shown as a single Braze metric.

As a general guide, aim for delivery near 99% with hard bounces under about 1%, and watch opens and clicks for engagement trends. Exact targets vary by industry and sending pattern. For practices that support reputation, see Improve email deliverability and Deliverability pitfalls and spam traps.

### “Campaign is already in delay window, so not enqueueing another”

In message activity or diagnostic logs for action-based campaigns, this processing outcome means Braze blocked a duplicate send while an earlier trigger for the same user is still within the campaign’s delivery window. A debounce lock prevents multiple enqueues for the same trigger burst.

You can see this outcome even when the campaign shows Send immediately if any of the following apply:

- The campaign uses an exception event or a send-time delay that affects timing.
 
- Users have a re-eligibility period, so they can’t receive the message again until that window passes.
 
- Another campaign or Canvas message step with higher priority consumed the send slot when triggers overlap.

If a user should have received the message but did not, check earlier outcomes for the same trigger (for example, email bounce or not enabled for the channel). Another message in the same workflow may have prevented this send.

### How does Braze calculate unique clicks for email?

Braze counts Unique Clicks over a seven-day window per recipient per dispatch_id. For the full definition, formulas, unsubscribe-link behavior, and Currents alignment, see Unique Clicks.

- 

New Stuff!
