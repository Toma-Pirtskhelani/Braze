---
url: https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events
slug: docs__user_guide__data__distribution__braze_currents__event_glossary__message_engagement_events
title: "Message engagement events"
description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using Currents."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Message engagement events

Search or filter to find the Currents events you need. These schemas consist of the Braze Events that are directly related to message sending.

 Search events
 
 Results update automatically as you type.

 Schema scope and related resources

Storage schemas apply to the flat file event data we send to Data Warehouse Storage partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage). For schemas that apply to the other partners, refer to our list of available partners and check their respective pages.

tip

These events are also available as SQL tables in the Query Builder, SQL Segment Extensions, and Snowflake Data Sharing. For SQL table schemas and column details, refer to the SQL table reference.

Contact your account manager or open a support ticket if you need access to additional event entitlements. If you can’t find what you need in this article, check out our Customer Behavior Events Library or our Currents sample data examples.

 Explanation of message engagement event structure and platform values

## Event structure

This event breakdown shows what type of information is generally included in a message engagement event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

Message engagement events are comprised of user-specific properties, campaign/canvas tracking properties, and event-specific properties.

### User ID schema

Note the naming conventions for user IDs.

 Braze schema | 
 Currents schema | 
 Description | 

 braze_id | 
 "USER_ID" | 
 The unique identifier that is automatically assigned by Braze. | 

 external_id | 
 "EXTERNAL_USER_ID" | 
 The unique identifier of a user’s profile that is set by the customer. | 

### Platform values

Certain events return a platform value that specifies the platform of the user’s device.

The following table details the possible returned values:

 User device | 
 Platform value | 

 iOS | 
 ios | 

 Android | 
 android | 

 FireTV | 
 kindle | 

 Kindle | 
 kindle | 

 Web | 
 web | 

 tvOS | 
 tvos | 

 Roku | 
 roku | 

 Considerations for message engagement events

- Currents drops events with payloads greater than 900 KB.
 
- Objects related to Canvas Flow have IDs you can use for grouping and translate to human-readable names through the Export Canvas details endpoint.
 
- Certain fields might not show their most recent state immediately after you update a campaign or Canvas:

- campaign_name
 
- canvas_name
 
- canvas_step_name
 
- conversion_behavior
 
- canvas_variation_name
 
- experiment_split_name
 
- message_variation_name

- If you need complete consistency for these fields, wait one hour after the last update before you send messages to your users.

## Agent executed events

This is the Kafka record schema for when an Agent Console agent is executed.

- cloud storage
 
- custom http connector

Loading schema…

Loading schema…

## Tool invocation events

This is the Kafka record schema for when a tool is executed. A tool is a function given to an LLM to fulfill an objective.

- cloud storage
 
- custom http connector

Loading schema…

Loading schema…

## Content Optimizer Component Store Update events

Updates to the component store

- cloud storage
 
- amplitude
 
- custom http connector
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Uninstall events

This event occurs when a user uninstalls an app. Use this data to track when users uninstall an app. While this is currently a message engagement event, this will be changed to a user behavior event in the future.

important

This event is not fired when the user actually uninstalls the app, as that’s impossible to track exactly. Braze sends a daily silent push to determine if the app still exists on your user’s device, and if we get an error on that silent push, it is assumed the app has been uninstalled.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Global Subscription State Change events

This event occurs when Braze receives a request to update the global subscription state of the user.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
state_change_source returns a string of the full source name. For example, the source CSV import returns the string CSV Import. Available sources are listed in the following table:

 Source | 
 Description | 

 SDK | 
 SDK endpoints | 

 Dashboard | 
 When a user’s subscription state is updated from the User Profile page in the dashboard | 

 Subscription Page | 
 When a user unsubscribes through an email link that is not the preference center | 

 REST API | 
 REST API endpoints | 

 CSV import | 
 CSV user import | 

 Preference Center | 
 When a user is updated from the preference center | 

 Inbound Message | 
 When a user is updated by inbound messages from end-users through channels, such as SMS | 

 Migration | 
 When a user is updated by internal migrations or maintenance scripts | 

 User Merge | 
 When a user is updated by the merging users process | 

 Canvas User Update Step | 
 When a user is updated by the Canvas User Update step | 

 Push Token Registration | 
 When a user is updated by the token registration process | 

 List-Unsubscribe | 
 When a user unsubscribes via Braze mailto or one-click list-unsubscribe header | 

 Other | 
 Includes any other sources, such as demo or provider sync jobs, or SMS and Whatsapp event callbacks | 

## Subscription Group State Change events

This event occurs when the subscription state of a user in a subscription group changes.

important

Subscription groups are only available for email, SMS, RCS, and WhatsApp channels at this time.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- 
state_change_source returns a string of the full source name. For example, the source CSV import will return the string CSV import. Available sources are listed as follows:

Source | 
Description | 

SDK | 
SDK endpoints | 

Dashboard | 
When a user's subscription state is updated from the User Profile page in Dashboard | 

Subscription Page | 
When a user unsubscribes through an email link that is not the preference center | 

REST API | 
REST API endpoints | 

CSV import | 
CSV user import | 

Preference Center | 
When a user is updated from the preference center | 

Inbound Message | 
When a user is updated by inbound messages from end-users through channels such as SMS | 

Migration | 
When a user is updated by internal migrations or maintenance scripts | 

User Merge | 
When a user is updated by the user merge process | 

Canvas User Update Step | 
When a user is updated by the Canvas user update step | 

## Campaign Conversion events

This event occurs when a user does an action that has been set as a conversion event in a campaign.

important

Note that the conversion event is encoded in the conversion_behavior field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The conversion_behavior_index field represents which conversion event, such as 0 = A, 1 = B, 2 = C, 3 = D.

note

The message_extras field is only available in send events (for example, Email Send, Push Send). It is not included in conversion events. To associate message_extras data with downstream engagement, use dispatch_id or send_id to join send events with conversion events in your data warehouse. For evaluating copy effectiveness by conversion rate, consider using campaign variants instead.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Campaign Control Group Enrollment events

This event occurs when a user is enrolled in a control variant set on a multi-variant campaign. This event is generated as there will be no channel send event for this user.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Canvas Conversion events

This event occurs when a user does an action that has been set as a conversion event in Canvas.

important

Note that the conversion event is encoded in the conversion_behavior field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The conversion_behavior_index field represents which conversion event, such as 0 = A, 1 = B, 2 = C, 3 = D.

note

The message_extras field is only available in send events (for example, Email Send, Push Send). It is not included in conversion events. To associate message_extras data with downstream engagement, use send_id to join send events with conversion events in your data warehouse. For evaluating copy effectiveness by conversion rate, consider using Canvas variants instead.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Canvas Entry events

This event occurs when a user enters into the Canvas. This event tells you which variant the user entered into.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Canvas Content Optimizer Step Conversion events

Conversion events for content optimizer canvas step

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Canvas Content Optimizer Step Send events

The canvas sends for content optimization canvas step

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Exit Match Audience events

This event occurs when a user has exited a Canvas by matching an audience.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Exit Perform Event events

This event occurs when a user has exited a Canvas by performing an event.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Experiment Step Conversion events

This event occurs when a user converts for a Canvas experiment step.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Experiment Split Entry events

This event occurs when a user enters a Canvas experiment step path.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Canvas Step Progression events

This event occurs when a user progresses through a step in a Canvas with some outcome. Note that this event doesn’t occur when steps are entered or exited. Currently, only split steps (Audience Paths, Decision Split, Action Paths, Experiment) and advance outcomes generate step progression events.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Banner Abort events

This event occurs when an originally scheduled banner message was aborted for some reason.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 Banner messages every 1 week

## Banner Click events

This event occurs when a user clicks a banner.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Banner Dismissal events

This event occurs when a user dismisses a banner.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Banner Impression events

This event occurs when a user views a banner.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Content Card Abort events

This event occurs if a Content Card message was aborted based on Liquid aborts, etc.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).
 
- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 Content Card messages every 1 week

## Content Card Click events

This event occurs when a user clicks a Content Card.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.

## Content Card Dismiss events

This event occurs when a user dismisses a Content Card.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.

## Content Card Impression events

This event occurs when a user views a Content Card.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.

## Content Card Send events

This event occurs when a Content Card gets sent to a user.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
message_extras allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language or country), and Canvas entry properties. Refer to Message extras to learn more.

## Email Abort events

This event occurs if an email message was aborted based on Liquid aborts, etc.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).
 
- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 email messages every 1 week

- 
message_extras is populated only when an abort occurs after the {% message_extras %} tag runs during rendering.

## Email Bounce events

This event occurs when an Internet Service Provider returns a hard bounce. A hard bounce signifies a permanent deliverability failure.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. For more information, see Dispatch ID behavior.

## Email Click events

This event occurs when a user clicks an email. Multiple events may be generated for the same campaign if a user clicks multiple times or clicks different links within the email.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment
 
- shopify

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. For more information, see Dispatch ID behavior.

## Email Deferral events

This event occurs when an Internet Service Provider does not immediately deliver the email to a non-hard bounced email address and Braze retries the email for up to 72 hours. Typical reasons for deferrals include reputation-based email volume rate-limiting from the inbox provider, temporary connectivity issues, recipient’s mailbox is full, or DNS errors.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled.

## Email Delivery events

This event occurs when an email sent made it successfully to the end-users inbox.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled.

## Email Mark As Spam events

This event occurs when the end-user hits the “spam” button on the email. Note that this does not represent the fact the email went into the spam folder as Braze does not track this.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled.

## Email Open events

This event occurs when a user opens an email. Multiple events may be generated for the same campaign if a user opens the email multiple times.

important

It’s known behavior that the email open event fields device_model and mailbox_provider are empty. You can ignore these for now.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment
 
- shopify

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled.

## Email Retry events

This event occurs when a message is deprioritized or frequency capped and will be retried later within the configured retry window. This is only available for Message Prioritization beta customers.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Email Send events

This event occurs when an email send request was successfully communicated between Braze and SendGrid. However, this does not mean the email was received in the user’s inbox. Braze does not log events to user profiles or any Currents destination (such as Snowflake) if the event cannot be matched to both the email and user ID associated with the email event.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment
 
- shopify

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. For more information, see Dispatch ID behavior.

- 
message_extras allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to Message extras to learn more.

## Email Soft Bounce events

This event occurs when an Internet Service Provider returns a soft bounce. A soft bounce signifies that an email could not be delivered because of a temporary deliverability failure.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. For more information, see Dispatch ID behavior.

## Email Unsubscribe events

This event occurs when the end-user has clicked “unsubscribe” from the email.

important

The Unsubscribe event is considered a specialized click event that is fired when your user clicks the unsubscribe link in the email (either a normal unsubscribe link within the email body or footer, or using the list-unsubscribe header), not when the user changes state to unsubscribed. If subscription state change is sent through the API, or with a custom (non-Braze) unsubscribe link, it does not trigger an email unsubscribe event on Currents.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

- The behavior for dispatch_id differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. For more information, see Dispatch ID behavior.

## Feature Flag Experiment Impression events

This event occurs whenever a user has had an opportunity to interact with your feature, or when they could have interacted if the feature is disabled (in the case of a control group in an A/B test).

Feature flag impressions are only logged once per session.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## In-App Message Abort events

This event occurs when an originally scheduled in-app message was aborted.

note

Abort events are only logged for templated in-app messages. Standard in-app messages don’t log abort events because Liquid evaluation occurs before the trigger action. For more details on in-app message abort behavior, refer to In-app messages FAQ.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 in-app messages every 1 week

## In-App Message Click events

This event occurs when a user clicks an in-app message.

note

For in-app messages, dispatch_id returns null.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.

## In-App Message Impression events

This event occurs when a user views an in-app message.

note

For in-app messages, dispatch_id returns null.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.

## Landing Page Click events

This event occurs when an end-user clicks on select elements and form fields on a landing page

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Landing Page Form Submission events

This event occurs when an end-user completes a form on a landing page and clicks on the button to submit the information

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Landing Page Impression events

This event occurs when an end-user’s browser loads and displays a landing page

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## LINE Abort events

This event occurs when a scheduled LINE message cannot be delivered, before sending to LINE.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).
 
- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 LINE messages every 1 week

- 
message_extras is populated only when an abort occurs after the {% message_extras %} tag runs during rendering.

## LINE Click events

This event occurs when a user clicks a link in a LINE message where the link’s domain matches the click tracking domain.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## LINE Inbound Receive events

This event occurs when a LINE message is received from a user.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## LINE Retry events

This event occurs when a message is deprioritized or frequency capped and will be retried later within the configured retry window. This is only available for Message Prioritization beta customers.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## LINE Send events

This event occurs when a LINE message is sent to LINE.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## Live Activity Outcome events

This event occurs when Braze receives a response from a third party provider (e.g. APNs) after the Live Activity send

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Live Activity Send events

This event occurs when the Braze system makes a request to its provider regarding Live Activity.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Push Notification Abort events

This event occurs if a push notification message was aborted based on Liquid aborts, etc.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).
 
- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 push messages every 1 week

- 
message_extras is populated only when an abort occurs after the {% message_extras %} tag runs during rendering.

## Push Notification Bounce events

This event occurs when an error is received from either Apple Push Notification Service or Fire Cloud Messaging. This means that the push message was bounced, and therefore not delivered to the user’s device.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- If you’re using Kafka to ingest Currents data, contact your customer success manager or account manager to enable the feature flipper for sending ad_id.
 
- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## Push Notification iOS Foreground Open events

This event is not supported by our Swift SDK and is now deprecated using our Obj-C SDK.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.
 
- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## Push Notification Open events

This event occurs when a user directly clicks on the push notification to open the application. Currently, Push Open Events refer specifically to “Direct Opens” rather than “Total Opens”. This does not include statistics shown at the campaign level of “influenced opens” as these are not attributed at the user level.

note

In rare cases, a push open may appear before the corresponding push send event in Currents data because of the following:

- Your SDK has an incorrect clock.
 
- High batch write latency. The recorded send time can lag behind early deliveries, so very quick opens may be logged before the batch’s final send timestamp is written. Large sends are dispatched and recorded in batches.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.
 
- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## Push Notification Retry events

This event occurs when a message is deprioritized or frequency capped and will be retried later within the configured retry window. This is only available for Message Prioritization beta customers.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Push Notification Send events

This event occurs when Braze processes a push message for a user, communicating this to Apple Push Notification Service or Fire Cloud Messaging. This does not mean the push was delivered to the device, just that a message was sent.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- For ad_id, ad_id_type, and ad_tracking_enabled, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for iOS and Android.
 
- If you’re using Kafka to ingest Currents data, contact your customer success manager to enable sending ad_id.
 
- 
message_extras allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to Message extras to learn more.
 
- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## RCS Abort events

This event is created when an RCS send is interrupted due to an error detected within Braze, and the message is dropped.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 RCS messages every 1 week

## RCS Click events

An event that is created when the user interacts with an RCS message in a way that involves tapping or clicking on a UI element.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## RCS Delivery events

This event is created when an RCS message is successfully delivered to a user’s mobile device.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## RCS Inbound Received events

This event is created when Braze receives an RCS message that originates from the user.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## RCS Read events

This event is created when a user opens an RCS message on their device, indicating that they have seen or read the message content.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## RCS Rejection events

An event that is created when an RCS message fails to be delivered to a user’s mobile device due to intervention by the carrier.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## RCS Send events

This event is created when an RCS message is sent out of Braze to our last-mile delivery partners.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## SMS Abort events

This event occurs if an SMS message was aborted based on Liquid aborts, etc.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 SMS messages every 1 week

- 
message_extras is populated only when an abort occurs after the {% message_extras %} tag runs during rendering.

## SMS Carrier Send events

This event occurs when an SMS is sent to the carrier.

important

CarrierSend is supported only for users on legacy infrastructure.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## SMS Delivery events

This event occurs when an SMS was successfully delivered to the user’s mobile phone.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## SMS Delivery Failure events

This event occurs when an SMS experiences delivery failure. Use this event and the provided error codes to help troubleshoot issues with SMS delivery.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## SMS Inbound Received events

This event occurs when one of your users sends an SMS to a phone number in one of your Braze SMS subscription groups.

When Braze receives an inbound SMS, we attribute that inbound message to any user that shares that phone number. As a result, you may receive multiple events per inbound message if multiple users in your Braze instance share the same phone number. If you require attribution of specific user IDs based on previous messages sent to that user, you can use the SMS Delivered event to attribute Inbound Received events to the user ID who most recently received a message from your Braze number.

If we detect that this inbound message is a reply to an outbound campaign or Canvas component sent from Braze, we will also include the campaign or Canvas metadata with the event. Braze defines a reply as an inbound message coming within four hours of an outbound message. However, there is a one-minute cache for the attributed campaign information of the last outbound SMS received.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## SMS Rejection events

This event occurs when an SMS send gets rejected by the carrier. This can happen for several reasons. Use this event and the provided error codes to help troubleshoot issues with SMS delivery.

note

Braze emits users.messages.sms.Rejection to Currents, Snowflake Data Sharing, and related exports only when the Braze user profile still exists in the workspace when the event is processed for logging. If that profile was deleted beforehand, you won’t see this event in your warehouse or Currents export. The same processing rule applies to other users.messages.sms.* outbound events Braze logs through the same pipeline (for example delivery, delivery failure, and sent-to-carrier). Workspace-level SMS metrics can still include aggregate counts that don’t map one-to-one to rows in Snowflake.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## SMS Retry events

This event occurs when a message is deprioritized or frequency capped and will be retried later within the configured retry window. This is only available for Message Prioritization beta customers.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## SMS Send events

This event occurs when a user sends an SMS.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment
 
- shopify

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
message_extras allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to Message extras to learn more.
 
- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## SMS Short Link Click events

This event occurs when a user clicks an SMS short link.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment
 
- shopify

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Survey Response events

Survey responses submitted by end users

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Webhook Abort events

This event occurs if a webhook message was aborted based on Liquid aborts, etc.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).
 
- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 webhook messages every 1 week

- 
message_extras is populated only when an abort occurs after the {% message_extras %} tag runs during rendering.

## Webhook Failure events

This event occurs if a webhook message was delivered but failed with an error response from the endpoint.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## Webhook Retry events

This event occurs when a message is deprioritized or frequency capped and will be retried later within the configured retry window. This is only available for Message Prioritization beta customers.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## Webhook Send events

This event occurs when a webhook was processed and sent to the third party specified in that webhook. Note that this does not signify whether or not the request was received.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
message_extras allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language or country), and Canvas entry properties. Refer to Message extras to learn more.
 
- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## WhatsApp Abort events

This event occurs if a WhatsApp message was aborted based on Liquid aborts, etc.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).
 
- The abort_type field describes the reason the message was aborted. For a full list of values, see Abort types.
 
- 
abort_type will be frequency_capped if the message was aborted due to a global frequency cap rule.
 
- 
abort_log includes information about the specific rule that triggered the abort. An example is: Frequency cap rule: 5 WhatsApp messages every 1 week

- 
message_extras is populated only when an abort occurs after the {% message_extras %} tag runs during rendering.

## WhatsApp Tracked Link Click events

This event occurs when a user clicks a link or button in a WhatsApp message where the link’s domain matches the click tracking domain.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## WhatsApp Delivery events

This event occurs when an WhatsApp message sent made it successfully to the user’s device.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## WhatsApp Failure events

This event occurs when WhatsApp cannot deliver the message to the user. A hard bounce signifies a permanent deliverability failure.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## WhatsApp Inbound Received events

This event occurs when one of your users sends a WhatsApp message to a phone number in one of your Braze WhatsApp subscription groups.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## WhatsApp Read events

This event occurs when an WhatsApp message is read by the user.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

## WhatsApp Retry events

This event occurs when a message is deprioritized or frequency capped and will be retried later within the configured retry window. This is only available for Message Prioritization beta customers.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

## WhatsApp Send events

This event occurs when a send request was successfully communicated between Braze and WhatsApp. Though, this does not mean the message was received by the user.

- cloud storage
 
- amplitude
 
- custom http connector
 
- mixpanel
 
- mparticle
 
- segment

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

Loading schema…

### Property details

- 
dispatch_id is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same dispatch_id. Use dispatch_id to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).

 Channels and platforms

 Agent

 Banner

 Content Cards

 Email

 Feature Flags

 In-App Messages

 LINE

 Live Activity

 Push

 RCS

 SMS

 Webhooks

 WhatsApp

 iOS

 Message actions

 Abort

 Bounce

 Clicks

 Deferral

 Delivery

 Dismissal

 Failure

 Impressions

 Inbound Received

 Opens

 Outcome

 Profile

 Read

 Rejection

 Retry

 Sends

 Spam

 Subscription

 Uninstall

 User journey

 Campaign

 Canvas

 Conversion

 Entry

 Exit

 Progression

- 

New Stuff!
