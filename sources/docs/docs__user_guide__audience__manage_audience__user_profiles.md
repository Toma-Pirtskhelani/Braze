---
url: https://www.braze.com/docs/user_guide/audience/manage_audience/user_profiles
slug: docs__user_guide__audience__manage_audience__user_profiles
title: "User profiles"
description: "This reference article describes how to access a user's profile in the dashboard, profile use cases, and what each profile contains."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# User profiles

User profiles are a great way to find information about specific users. All persistent data associated with a user is stored in their user profile.

## Access profiles

To access a user’s profile, go to the Search Users page and search for a user by any of the following:

- External user ID
 
- Braze ID
 
- Email
 
- Phone number
 
- Push token
 
- User alias with the format “[user_alias]:[alias_name]”, such as “amplitude_id:user_123”

If a match is found, you can view the information you’ve recorded for this user with the Braze SDK. Otherwise, if your search returns multiple user profiles, you can merge each profile individually or perform a bulk user merge. For a full walkthrough, see Merge duplicate users.

note

Search Users is not the same as User Lookup in the segment or campaign composer. User Lookup tests whether a specific user matches your audience and accepts only external_id or braze_id. Search Users on this page supports email, phone, push token, and user alias. For more information, see Testing segments.

important

When a phone number is used in the search, it is changed into E.164 format. Users whose phone numbers cannot be changed into E.164 format (for example, because the phone number has an invalid country code or area code) cannot be searched by phone number.

## Use cases

User profiles are a great resource for troubleshooting and testing because you can easily access information about a user’s engagement history, segment membership, device, and operating system.

For example, if a user reports a problem and you aren’t sure what device and operating system they are using, you can use the Overview tab to find this information (as long as you have their email or user ID). You can also view a user’s language, which could be helpful if you’re troubleshooting a multi-lingual campaign that didn’t behave as expected.

You can use the Engagement tab to verify whether a certain user received a campaign. In addition, if this particular user did receive the campaign, you can see when they received it. You can also verify whether a user is in a certain segment and whether a user is opted in to push, email, or both. This information is useful for troubleshooting purposes. For example, you should check this information if a user doesn’t receive a campaign that you expected them to receive or receives a campaign that you did not expect them to receive.

## Elements of user profile

There are five main sections of a user’s profile.

- Overview: Basic information about the user, session data, custom attributes, custom events, purchases, and the most recent device that the user logged into.
 
- Engagement: Information about the user’s contact settings, campaigns received, segments, communication stats, install attribution, and random bucket number.
 
- Event History: Custom events and purchases from the past 30 days, with full event properties shown as JSON.
 
- Messaging History: Recent messaging-related events for this user from the past 30 days.
 
- Feature Flags Eligibility: Validate which feature flags a user is currently eligible for across rollouts, canvas steps, and experiments.

- overview tab
 
- engagement tab
 
- event history tab

### Overview tab

The Overview tab contains basic information about a user and their interactions with your app or website.

 Overview category | 
 Contains | 

 Profile | 
 Gender, age group, location, language, locale, time zone, and birthday. | 

 Sessions overview | 
 How many sessions they had, when their first and last sessions were, and on which apps. | 

 Custom attributes | 
 Which custom attributes are attributed to this user and their associated value, including nested custom attributes. | 

 Recent devices | 
 How many devices they logged in on, details on each device, and their associated advertising IDs (if any). | 

 Custom events | 
 Which custom events this user has performed, how many times, and when they last performed each event. | 

 Purchases | 
 Lifetime revenue attributed to this user, their last purchase, total number of purchases, and a list of each purchase. | 

For more information on this data, see SDK data collection.

### Engagement tab

The Engagement tab contains information about a user’s interactions with the messages you sent them using Braze.

 Engagement category | 
 Contains | 

 Contact settings | 
 Subscription status for email, SMS, and push, and the subscription groups this user is associated with for these three channels. This section also includes changelog information for push tokens. Refer to email, SMS, and push for information on how subscriptions and opt-ins are set. | 

 Campaigns received | 
 Campaigns received reflects channel-specific send and view timing. Most channels record a send when Braze passes the message to the delivery provider, even when the message is not ultimately delivered. Content Cards are different: campaigns appear here only after the user views the card in the app. For a breakdown by channel, see When campaigns appear in Campaigns received. 

When a message is received, opened, or clicked, Braze updates data for all profiles that share the same channel identifier as the profile that logged the interaction (for example, the same email address for email, or the same phone number for SMS or WhatsApp). Users who share an identifier with someone who received, opened, or clicked the message can match this filter even if they were not originally in the campaign or were not directly sent the message.

These lists use messaging interaction data (including expiration rules) when determining what appears for retargeting and history.

 Select a campaign from the list to view it. | 

 Segments | 
 Segments this user is included in. Select a segment from the list to view it. | 

 Communication stats | 
 When this user last received messages from you from each channel. | 

 Install attribution | 
 Information about how and when a user installed your app. Learn more about understanding user installs. | 

 Miscellaneous | 
 The user’s random bucket number. | 

 Canvas messages received | 
 Canvas messages this user has received and when. Send timing follows the same channel rules as Campaigns received; see When campaigns appear in Campaigns received.

 When a message is received, opened, or clicked, Braze updates data for all profiles that share the same channel identifier as the profile that logged the interaction (for example, the same email address for email, or the same phone number for SMS or WhatsApp). Users who share an identifier with someone who received, opened, or clicked the message can match this filter even if they were not originally in the campaign or were not directly sent the message.

 Select a message from the list to view it. | 

 Predictions | 
 Churn prediction and event prediction scores for this user. | 

### Event History tab

note

To view the Event History tab, you need the Search Users, View User Event Properties, and View PII permissions, because event properties can contain personal data.

The Event History tab shows the custom events and purchases a user has logged. Use it to verify event data is arriving correctly and troubleshoot user-level issues directly in the dashboard—no data exports or external tooling required.

 Event History category | 
 Contains | 

 Event list | 
 Custom events and purchases from the past 30 days (up to 100 most recent), ordered newest first. | 

 Event type | 
 Whether the row is a Custom Event or Purchase. | 

 Timestamp | 
 When the event was logged. | 

 Event name | 
 The name of the custom event or purchase. | 

 Event properties | 
 Full event properties for the event, shown as JSON. | 

### When campaigns appear in Campaigns received

In general, Braze lists a campaign under Campaigns received after it attempts to send the message. A delivery to the user’s device or inbox is not required for a send to be logged. Canvas messages received follows the same channel-specific rules for each Canvas message type.

tip

When timestamps are displayed in relative format (such as “6 days ago”), hover over them to see the exact date and time.

- Email: Braze logs a send when the message is handed off to your email service provider (ESP). After that handoff, the message is not aborted because of Liquid logic, rate limiting, or the user being marked as unreachable. The next events are often a delivery or a bounce.
 
- Push: Braze logs a send when the message is handed off to the push provider (for example, Apple Push Notification service (APNs) or Firebase Cloud Messaging (FCM)). The provider usually tries to deliver immediately; if the device is unavailable (for example, offline), the provider may retry until the message expires.
 
- In-app messages: Braze logs a send when the campaign is launched.
 
- Content Cards: When Braze records a Sent event depends on delivery type and your Card Creation setting. A Content Card campaign appears under Campaigns received on the user profile only after the user views the card in the app. For the full breakdown, see When sends are logged and Campaigns Received and retargeting filters in the Content Card reporting article.
 
- SMS, WhatsApp, and webhooks: Braze logs a send when the message enters the delivery path for that channel (for example, the SMS or WhatsApp provider, or your webhook endpoint).

note

These descriptions cover when a send is logged for Campaigns received. They are separate from message aborts that can stop a message before it reaches a provider.

### Messaging History tab

The Message History tab of the user profile shows recent messaging-related events (about 40) for an individual user from the past 30 days. These events include the messages that the user was sent, received, interacted with, and more.

The data in this tab isn’t updated after a user is merged. Additionally, any events associated with messages sent through API (for example, the /messages/send endpoint) do not appear in this tab if there is no campaign ID specified in those sends.

important

RCS events aren’t currently supported in the Messaging History tab.

#### Viewing and understanding events

For each event in the Messaging History table, you can see the messaging channel, event type, timestamp the event occurred, the associated campaign or Canvas message, and the user’s device data. To filter for specific events, click Filters and select events from the list.

##### Message engagement events

The following message engagement events are available for email, SMS, push, in-app messages, Content Cards, and webhooks. To learn more about how specific events are tracked, refer to the Message engagement event glossary.

 Channel | 
 Engagement events available | 

 Email | 
 Bounce
Click
Deferral events
Delivery
Mark as spam
Open (see note on email open event)
Send
Soft bounce
Unsubscribe | 

 SMS | 
 Carrier send
Delivery
Delivery failure
Inbound receive
Rejection
Send | 

 Push | 
 Bounce
Influenced open
iOS Foreground
Open
Send | 

 In-app message | 
 Click
Impression | 

 Content Cards | 
 Click
Dismiss
Impression
Send | 

 Webhooks | 
 Send | 

 WhatsApp | 
 Abort
Delivery
Failure
Frequency capped
Inbound receive
Read
Send | 

##### Message abort events

Message abort events occur when a message sent to a user was aborted due to conditional logic in Liquid or Connected Content, or from Liquid rendering timeouts.

Abort events are available for the following channels:

- Email
 
- SMS
 
- Push
 
- Webhooks

Abort events are currently not available for in-app messages and Content Cards.

##### Frequency cap events

A frequency cap event occurs when a user is qualified to receive a message, but doesn’t actually receive it due to frequency capping settings. You can customize frequency capping settings from Settings > Frequency Capping Rules.

##### Blank destinations

Some message sends may appear in the Messaging History with blank destinations (signified by “—”). This is because some channels, such as Content Cards and webhooks, do not gather device data on message send.

Content Cards sends are logged when the card is available to be viewed. Because Content Cards can be viewed on multiple devices, device data is not logged for a send. Instead, this information is logged upon impression (when the card is actually viewed). Webhooks are sent to a system endpoint (not a device) so device data is not applicable.

#### Note on email open event

Email open tracking is error-prone in any tool, including Braze. With a variety of privacy protection features offered by different email clients that either block the automatic loading of images or load them proactively on the server, email open events are susceptible to both false positives and false negatives.

While email open statistics can be useful in aggregate, for example, to compare the effectiveness of different subject lines, you should not assume an individual open event for an individual user is meaningful.

#### Why are certain fields blank in the Message History tab?

Some fields may be absent in a user’s Message History tab in the following scenarios:

- When an event is missing data for Message Sent, this indicates that the campaign doesn’t have any message variations.
 
- When an event is missing data for Campaign/Canvas and Message Sent, this indicates that this message was sent from an API campaign (not API-triggered campaigns) that didn’t specify the campaign_id and message_variation_id. These fields are optional and may be left out of the request body. When these fields are specified, that information is populated into the message history logs.

- If a particular message is missing entirely from the messaging history but appears in the Campaigns Received log, it’s likely the user received the campaign before being identified as the current user. If an existing profile is orphaned, the Campaigns Received log is transferred, but the messaging history is not.

- When data is missing for Campaign/Canvas, a manual test may have been sent. Manual tests are logged in the Messaging History tab, but the campaign or Canvas that was sent won’t be logged.
 
- When a user is in a seed group or other internal test audience, Messaging History may show limited campaign or Canvas metadata compared to production sends.

## Data size constraints

Braze doesn’t enforce an overall capacity on the total size of a user profile. However, specific data types associated with users have defined size capacities.

### Custom attribute arrays

Custom attribute arrays (including arrays of objects) have a capacity of 100 KB. When you send an array that exceeds this capacity, the custom attribute isn’t processed. The API returns a success response (201), but the array doesn’t appear in the user profile and existing data for that attribute isn’t updated.

If your arrays approach this capacity, consider limiting the number of objects you populate to keep the total size within 100 KB.

For more information on custom attributes, see Custom attribute data types.

## Related articles

- User profile lifecycle
 
- POST: Export user profile by identifier
 
- POST: Delete users

- 

New Stuff!
