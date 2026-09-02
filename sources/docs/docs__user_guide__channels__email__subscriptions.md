---
url: https://www.braze.com/docs/user_guide/channels/email/subscriptions
slug: docs__user_guide__channels__email__subscriptions
title: "Email subscriptions"
description: "This reference article covers the different user subscription states, how to manage email subscriptions, and how to segment users based on their."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Email subscriptions

Learn about global email subscription states, footers and unsubscribe pages, preference centers, and campaign targeting. For subscription groups across all channels, see Subscription groups.

This document is for informational purposes only. It is not intended to provide, nor may it be relied upon as providing legal advice in any capacity. Sending marketing and transactional emails may be subject to specific legal requirements. To ensure that you are doing so in compliance with all applicable laws, rules, and regulations specific to your company, you should seek the advice of your legal counsel and/or regulatory compliance team.

## Subscription states

Braze uses global subscription states to control which users receive email. For definitions of opted-in, subscribed, and unsubscribed, how global status differs from subscription groups, and how subscription status works on other channels, see Subscription status.

### Unsubscribed email addresses

Braze automatically unsubscribes any user who manually unsubscribes through a custom footer. If the user updates their email address and Resubscribe users when they update their email is enabled in Sending Configuration, normal sending resumes.

If a user marks one or more of your emails as spam, Braze sends only transactional emails to that user. Transactional emails refer to the Send to all users including unsubscribed users option in Target Audience.

tip

Refer to our IP warming best practices for guidance on how to re-engage your users effectively.

### Bounces and invalid emails

A Hard Bounce is when an email fails to deliver to the recipient due to a permanent delivery error. A hard bounce might occur because the domain name doesn’t exist or because the recipient is unknown.

A Soft Bounce is when an email fails to deliver to the recipient due to a temporary delivery error, even though the recipient’s email address is valid. A soft bounce might occur because the recipient’s inbox is full, the server was down, or the message was too large for the recipient’s inbox.

When an email address hard bounces, Braze doesn’t automatically set the user’s subscription state to “unsubscribed”. If an address hard bounces (invalid or doesn’t exist), Braze marks it invalid and doesn’t attempt further sends. If the user changes their email address, Braze resumes sending. Braze retries soft bounces for 72 hours.

### Updating email subscription states

There are four ways to update a user’s email subscription state:

#### SDK integration

Use the Braze SDK to update a user’s subscription state.

#### REST API

Use the /users/track endpoint to update the email_subscribe attribute for a user. For example, to set a user’s email subscription state to unsubscribed when they use a custom unsubscribe link, include email_subscribe: "unsubscribed" in the user attributes in your request.

#### User profile

- Find the user through Search Users.
 
- Under Engagement, select Unsubscribed, Subscribed, or Opted In to change the user’s subscription status.

The user profile also displays a timestamp for when the user’s subscription was last changed. A timestamp is recorded when the state is Opted-in or Unsubscribed, but not when the state is Subscribed — for example, a newly created profile that has never explicitly opted in or out has no subscription timestamp.

#### Preference center

Include Preference center Liquid at the bottom of your emails to let users opt in or out. Braze manages subscription state updates from the preference center.

### Checking email subscription state

Use any of the following methods to check a user’s email subscription state:

- REST API export: Use the Export users by segment or Export users by identifier endpoints to export individual user profiles in JSON format.
 
- User profile: Find the user’s profile on the Search Users page, then select the Engagement tab to view and manually update a user’s subscription state.

When a user updates their email address, their subscription state is set to subscribed. If the updated email address already exists elsewhere in a Braze workspace, the user inherits the subscription state from that existing user unless Resubscribe users when they update their email setting is turned on in Sending Configuration.

To troubleshoot subscription state changes, check the Currents Global Subscription State Change event (users.behaviors.subscription.GlobalStateChange), which includes the history and source of subscription state changes.

The following sources can trigger an email subscription state change:

 Source | 
 Description | 

 SDK | 
 User attribute update sent through a Braze SDK | 

 REST API | 
 User attribute update sent through the /users/track endpoint | 

 Dashboard | 
 Subscription state changed manually on the user profile page | 

 CSV Import | 
 Subscription state set during a user CSV import | 

 Preference Center | 
 User updated their preference from a Braze-hosted preference center | 

 Subscription Page | 
 User selected an unsubscribe link in an email and landed on the Braze subscription page | 

 List-Unsubscribe | 
 User unsubscribed through the email client’s native list-unsubscribe header | 

 Canvas User Update Step | 
 Subscription state updated by a User Update step in a Canvas | 

When a user’s global email subscription state changes, Braze propagates that state to other profiles that share the same email address, up to 100 profiles per change. Braze does not guarantee propagation when more than 100 profiles share the same email address. If users who share an email show different subscription states, contact Braze Support.

## Subscription groups

Email subscription groups let users opt in or out of specific email categories (such as newsletters or promotions) without changing their global email subscription state. Groups you create are available to add to your preference center.

For more information about creating groups, segmenting, archiving, and channel-specific behavior, see Subscription groups.

## Email preference center

The email preference center lets you manage which users receive subscription group newsletters. Find it in the dashboard under Subscription Groups. Each subscription group you create is added to the preference center list.

To learn more about how to add or customize a preference center, refer to Preference center.

## Changing email subscriptions

In most cases, users manage their email subscription through links included in the emails they receive. Insert a legally compliant footer with an unsubscribe link at the bottom of every email. When users select the unsubscribe URL, Braze unsubscribes them and shows a landing page confirming the change. Include this Liquid tag: ${set_user_to_unsubscribed_url}.

note

You can use the ${set_user_to_unsubscribed_url} Liquid tag only in email campaigns and Canvases. You cannot use this tag in other messaging channels.

When a user selects “Unsubscribe from all of the listed types of emails” in the preference center, Braze sets their global email subscription status to unsubscribed and unsubscribes them from all groups.

Recipient-side email unsubscribes—unsubscribe links, list-unsubscribe, preference center submissions, and ESP-reported unsubscribes—appear in the Snowflake USERS_MESSAGES_EMAIL_UNSUBSCRIBE table. Unsubscribes made through the REST API are not included in that table; those emit users.behaviors.subscriptiongroup.StateChange or users.behaviors.subscription.GlobalStateChange events instead. For the table schema, see USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED.

### Creating custom footers

If you don’t want to use the default footer, create a workspace-wide custom email footer and template it into every email using {{${email_footer}}}.

This lets you avoid creating a new footer for every email template or email campaign. For steps, see Custom email footer.

#### Managing subscription states for Chinese IP addresses

If you anticipate Chinese IP addresses, don’t rely solely on an unsubscribe link to maintain unsubscribed lists. Provide alternate unsubscribe paths such as a support ticket or customer representative email.

### Creating a custom unsubscribe page

When users select an unsubscribe URL in an email, they open a default landing page that confirms the subscription change.

To use a custom landing page instead:

- Go to Email Preferences > Subscription Pages and Footers.
 
- Add the HTML for your custom page.

Include a resubscribe link (for example {{${set_user_to_subscribed_url}}}) so users can undo an accidental unsubscribe. Like ${set_user_to_unsubscribed_url}, you can use this tag in only email campaigns and Canvases.

You can also send users to your site and update status with the Braze REST API (for example link with ?user_id={{${user_id}}} and then call /email/status.

note

If you use the dashboard footer instead of only an HTML content block, the template must still contain {{${set_user_to_unsubscribed_url}}} to save. To use a different unsubscribe URL temporarily, you can comment out the default tag. An example is: <!-- {{${set_user_to_unsubscribed_url}}} -->.

### Creating a custom opt-in page

Use a custom opt-in page to let users acknowledge and control notification preferences before subscription. This additional communication can help email campaigns stay out of spam folders.

- Go to Settings > Email Preferences.
 
- Select Subscription Pages and Footers.
 
- Customize the styling in the Custom opt-in page section to see how that indicates to your users that they’ve been subscribed.

Users reach this page through the {{${set_user_to_opted_in_url}}} tag. Like other email subscription Liquid tags, you can use this tag in only email campaigns and Canvases.

tip

Use a double opt-in process to improve outreach. Braze sends an additional confirmation email where a user confirms notification preferences via a link. After confirmation, the user is opted in.

## Subscriptions and campaign targeting

By default, Braze targets campaigns with push or email messages at users who are subscribed or opted in. Change this in Target Audience by selecting the dropdown next to Send to these users:.

Braze supports three targeting states:

- Users who are subscribed or opted-in (default).
 
- Only users who are opted-in.
 
- All users, including those who have unsubscribed.

important

It’s your responsibility to comply with any applicable spam laws when using these targeting settings.

## Segmenting by user subscriptions

Use the “Email Subscription Status” and “Push Subscription Status” filters to segment users by subscription status.

Use this to target users who have neither opted in nor out and encourage an explicit opt in. Create a segment with the filter “Email/Push Subscription Status is Subscribed” and send campaigns to users who are subscribed but not opted in.

- 

New Stuff!
