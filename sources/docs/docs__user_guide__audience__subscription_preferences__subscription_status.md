---
url: https://www.braze.com/docs/user_guide/audience/subscription_preferences/subscription_status
slug: docs__user_guide__audience__subscription_preferences__subscription_status
title: "Subscription status"
description: "Learn how Braze tracks subscription status across email, LINE, SMS, RCS, and WhatsApp, and how status gates message delivery."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Subscription status

Learn how Braze tracks subscription status across messaging channels, how global and subscription group status interact, and where channel-specific rules apply.

Subscription status tells Braze whether a user is eligible to receive messages on a channel. Status can gate campaign and Canvas targeting, segment filters, and whether Braze attempts delivery.

## How subscription status works in Braze

Braze tracks subscription status at two levels:

 Level | 
 What it controls | 
 Channels | 

 Global subscription state | 
 Whether a user can receive messages on that channel at all | 
 Email, push | 

 Subscription group status | 
 Whether a user is opted in to a specific group within a channel | 
 Email, SMS, MMS, RCS, WhatsApp, LINE | 

Global state and subscription group status work together. For email, a user who is globally unsubscribed won’t receive email even if they’re subscribed to a subscription group. For SMS, RCS, WhatsApp, and LINE, users must be subscribed to the relevant subscription group to receive messages from that group.

You can view and update subscription status on a user’s profile in Engagement > Contact settings, through the REST API, SDK, CSV import, preference centers, and channel-specific opt-in flows. Braze doesn’t count subscription state changes against your data points.

note

Subscription groups add granular opt-in within a channel (for example, promotional versus transactional SMS). Global email state and subscription group membership work together when deciding who is reachable.

## Email

Braze has three global subscription states for email. These states gate whether users receive messages targeted at subscribed or opted-in audiences. For example, users in the unsubscribed state don’t receive messages targeted at subscribed or opted-in users.

 State | 
 Definition | 

 Opted-in | 
 A user has explicitly confirmed they want to receive email. Braze recommends an explicit opt-in process to get consent from users to send emails. | 

 Subscribed | 
 A user has neither unsubscribed nor explicitly opted in to receive emails. This is the default subscription state when a user profile is created. | 

 Unsubscribed | 
 A user has explicitly unsubscribed from your emails. | 

### Email-specific behavior

- Unsubscribes and spam reports: Braze automatically unsubscribes users who unsubscribe through a custom footer. If a user marks an email as spam, Braze sends only transactional email (messages sent with Send to all users including unsubscribed users).
 
- Hard bounces: When an email address hard bounces, Braze doesn’t automatically set the user’s subscription state to unsubscribed. Braze marks the address invalid and stops sending until the user updates their email address.
 
- Shared email addresses: When a user’s global email subscription state changes, Braze propagates that state to other profiles that share the same email address, up to 100 profiles per change.
 
- Email address updates: When a user updates their email address, their subscription state is set to subscribed unless the updated address already exists on another profile, in which case the user inherits that profile’s state.

For updating subscription state, checking status, preference centers, and campaign targeting, see Email subscriptions.

## LINE

LINE is the source of truth for LINE subscription status. Even if a user profile has a native_line_id, Braze won’t deliver LINE messages unless that user follows your LINE channel.

LINE subscription status is tracked by native_line_id, not external_id. If multiple profiles share the same native_line_id, they inherit the same LINE subscription status.

 State | 
 Definition | 

 Subscribed | 
 The user followed your LINE channel from within their LINE app. | 

 Unsubscribed | 
 The user hasn’t followed your LINE channel, or explicitly unfollowed it. | 

### Subscription sync tool

After a successful LINE channel integration, Braze deploys a subscription sync tool to align existing Braze profiles with LINE follower data:

- Profiles with a native_line_id that follows your channel are updated to subscribed.
 
- Followers without a matching Braze profile get an anonymous profile with native_line_id, a line_id user alias, and subscribed status.

You can’t set LINE subscription group state manually during integration—LINE controls status, and Braze syncs it.

### Follow and unfollow event updates

When Braze receives LINE webhook events for your integrated channel:

- Follow: All profiles with a matching native_line_id are set to subscribed. If no profile exists, Braze creates an anonymous user.
 
- Unfollow: All profiles with a matching native_line_id are set to unsubscribed.

For setup steps, user reconciliation, and use cases, see LINE setup and LINE subscription groups.

## SMS and RCS

SMS and RCS use subscription group status, not a separate global channel state. A user can be subscribed to a transactional group and unsubscribed from a promotional group at the same time.

 State | 
 Definition | 

 Subscribed | 
 The user is subscribed to receive SMS and RCS from a specific subscription group, either through the Braze subscription API, an opt-in keyword, or another supported method. When double opt-in is enabled, users must confirm opt-in before status updates to Subscribed. | 

 Unsubscribed | 
 The user opted out of that subscription group by texting an opt-out keyword or through the Braze subscription API. | 

### SMS and RCS-specific behavior

- Phone number inheritance: When a phone number is added or updated on a profile, the number inherits subscription group status from the profile or from any existing profile that already uses that number.
 
- Keyword handling: Users can opt in or out by texting default or custom keywords. Braze updates subscription state automatically.
 
- Compliance: Braze never sends SMS or RCS to users who aren’t subscribed to the selected subscription group.

For setup, sending, and managing subscription groups, see SMS, MMS, and RCS subscription groups.

## WhatsApp

WhatsApp also uses subscription group status. Meta requires explicit opt-in consent before you send marketing messages.

 State | 
 Definition | 

 Subscribed | 
 The user explicitly confirmed they want WhatsApp messages from your business, through an opt-in flow or the Braze subscription API. | 

 Unsubscribed | 
 The user hasn’t opted in, or their opt-in was removed. Unsubscribed users don’t receive messages from phone numbers in that subscription group. | 

### Opt-in requirements

To message users on WhatsApp, provide Braze with an external_id, a phone number, and an updated subscription status for each user. Collect opt-ins on your website, app, SMS, in-app messages, inbound WhatsApp threads, or through a CSV import of users who already opted in elsewhere.

### Opt-out methods

Users can opt out through:

- Inbound keyword workflows: Canvases or campaigns triggered by opt-out keywords (for example, “STOP”), with a follow-up step that updates subscription status.
 
- Marketing opt-out quick replies: Message templates with Meta’s marketing opt-out button, paired with a subscription group update step in your Canvas.
 
- Blocks and reports: If a user blocks your business, subsequent messages don’t deliver and aren’t billed, but Braze subscription status doesn’t update. User reports don’t change subscription status either.

### WhatsApp “Offers and Announcements” toggle

WhatsApp’s native Offers and Announcements toggle is separate from Braze subscription groups. When a user turns it off in WhatsApp, Meta blocks marketing delivery even if Braze shows subscribed. The two layers don’t sync automatically.

For step-by-step opt-in and opt-out workflows, see WhatsApp opt-ins and opt-outs and WhatsApp subscription groups.

## Segment and target by subscription status

Use subscription status filters in the segment builder to target or suppress audiences by channel—for example, Email Subscription Status, Push Subscription Status, and Subscription Group filters.

When building campaigns and Canvases, Send Settings and Target Audience options let you send only to users with a specific subscription status (such as subscribed and opted-in). For email and push filter definitions, see Segmentation filters.

- 

New Stuff!
