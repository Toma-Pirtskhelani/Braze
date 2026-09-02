---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in
slug: docs__user_guide__channels__sms_mms_and_rcs__message_features_and_optimization__keyword_processing__double_opt_in
title: "Double opt-in"
description: "This reference article covers the double opt-in feature, and explains how to enable the feature, select opt-in keywords and reply messages, and enter users into..."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Double opt-in

The double opt-in feature requires users to explicitly confirm their opt-in intent before they can receive SMS, MMS, or RCS messages. This focuses messaging on engaged users and supports compliance best practices.

When double opt-in is turned on, users are sent a message that asks for their explicit consent before they can be messaged by your campaigns or Canvases.

While not an explicit requirement of the Telephone Consumer Protection Act of 1991 (TCPA), Braze recommends that you configure double opt-in to confirm users are aware and consenting to be a part of your SMS, MMS, or RCS program. For more information about compliance, view Laws, regulations, and abuse prevention for SMS, MMS, and RCS.

## Double opt-in workflows

Double opt-in empowers you to obtain explicit consent through inbound and outbound opt-in campaigns.

### Outbound

When a user provides their phone number, they are sent a message that asks for their consent.

### Inbound

When a user sends a message that contains an opt-in keyword, they are sent a message that asks for their consent.

## Enabling double opt-in

To turn on double opt-in, go to the Global Keywords table in the applicable subscription group, and select Edit in the Opt-In Keyword Category. Next, select your opt-in method (Opt-In or Double Opt-In). Selecting Double Opt-In expands the page to show additional configurable fields.

### Configurable fields

 Category | 
 Fields | 
 Description | 

 Opt-In Prompt | 
 Keywords | 
 These are the keywords that a user can text to indicate opt-in intent. START is a required keyword. This opt-in prompt is also sent to the user when their subscription status is updated by sources listed in the Subscription sources section. | 

   | 
 Reply Message | 
 This is the initial response a user receives after texting an opt-in keyword (for example, “Reply Y to confirm you want to receive messages from this number. Msg&Data Rates may apply.” ) | 

 Double Opt-In Confirmation | 
 Keywords | 
 These are the keywords a user can reply with to confirm their opt-in intent. At least one keyword is required. These keywords should be specified in the Opt-In Prompt Reply Message field. | 

   | 
 Reply Message | 
 This is the confirmation response a user receives after they have explicitly confirmed their opt-in and are now messageable. The user’s subscription group status is set to Subscribed. | 

When a user receives an opt-in prompt, they have 30 days to confirm their opt-in intent. If a user wants to subscribe after the 30-day window, they need to text an opt-in keyword to start the double opt-in workflow again.

## Subscription group status

Only after the user completes the double opt-in workflow does their subscription group status update to Subscribed. If the user begins the workflow but doesn’t complete it, they remain Unsubscribed and cannot be sent messages from that subscription group.

Users can also be entered into the double opt-in workflow if they are subscribed from other sources (for example, REST API, SDK).

## Subscription sources

Users can also enter the double opt-in workflow through subscription updates that occur outside of inbound messages. These sources include updates from the REST API, SDK, and preference center. When a user enters the double opt-in workflow through these sources, they receive the Opt-In Prompt Reply Message.

important

When users are entered into the double opt-in workflow through sources other than inbound messages, they receive at most one opt-in prompt reply message in a rolling 24-hour period, regardless of the number of times they are entered into this workflow.

Each subscription source has a different enrollment behavior, as described in the following table.

 Source | 
 Double Opt-In Enrollment Behavior | 

 SDK | 
 Users automatically enter the double opt-in workflow when subscribed through the Braze SDK. | 

 REST API | 
 Users can be entered into the workflow when the subscription status is set through /subscription/status/set, /v2/subscription/status/set or /users/track and the optional parameter use_double_opt_in_logic is passed as true (for example, [{“subscription_group_id” : “subscription_group_identifier”, “subscription_state” : “subscribed”, “use_double_opt_in_logic”: true}]). If this parameter is omitted, users won’t be entered into the double opt-in workflow. 

When using use_double_opt_in_logic with the REST API, if no user profile is associated with the provided phone number, the subscription state isn’t updated, and the user can’t enter the double opt-in workflow. | 

 Shopify | 
 Users aren’t entered into the double opt-in workflow when their subscription status is set by our Shopify integration. | 

 User Import | 
 Users aren’t entered into the double opt-in workflow when their subscription status is set by User Import. | 

 Preference Center | 
 Users automatically enter the double opt-in workflow when subscribed through a preference center. | 

 User Update Step | 
 Users can be entered into the double opt-in workflow when their subscription status is set through the User Update step and the optional parameter use_double_opt_in_logic is passed as true. If this parameter is omitted, users aren’t entered into the double opt-in workflow. | 

## Multi-language support

For inbound messages, double opt-in is supported for all languages defined in the subscription group. This means you can define your auto-responses in different languages and Braze will send the auto-response associated with a specific language when a matching keyword is received.

Users who enter the double opt-in workflow through subscription updates that occur outside of inbound messages (for example, SDK, REST API, Shopify) will only be sent the English keywords.

- 

New Stuff!
