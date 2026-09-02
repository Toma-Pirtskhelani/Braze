---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/user_retargeting
slug: docs__user_guide__channels__whatsapp__message_features_and_optimization__user_retargeting
title: "User retargeting"
description: "This reference article covers how users can retarget their messages by users WhatsApp interactions."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# User retargeting

In addition to changing the user’s subscription state, Braze will also record interactions with the user profile for filtering and triggering messages.

These filters and triggers allow you to filter users that have received WhatsApp messages or received WhatsApp messages from a specific WhatsApp campaign or Canvas step.

## Retargeting options

note

When building audiences with user retargeting, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the CCPA. Marketers should implement the relevant filters for users’ eligibility within their Canvas and/or Campaign entry criteria.

### Filter users by WhatsApp

Users can be filtered by when they last received a WhatsApp or if they have received a WhatsApp from a specific WhatsApp campaign. Filters can be set in the Target Users step of the campaign builder.

#### Filter by last received WhatsApp

#### Filter by received messages from WhatsApp campaign

Filters users who have received a message from a specific WhatsApp campaign. With this filter, you also have the option to filter off those that have not received messages from a WhatsApp campaign.

note

When a WhatsApp message is delivered, opened, or clicked, Braze updates data for all profiles that share the same phone number as the profile that logged the interaction, so users who share that number with someone who received, opened, or clicked the message can match “received” filters even if they were not directly sent it.

### Filter by engagement

Retarget users who have, or have not, read a WhatsApp campaign or Canvas step.

#### Retarget users who have opened/read a specific WhatsApp Campaign

- Create a segment using the Clicked/Opened Campaign filter.
 
- Select read WhatsApp message.
 
- Choose the desired campaign.

#### Retarget users who have opened/read a specific Canvas Step

- Create a segment using the Clicked/Opened Step filter.
 
- Select read WhatsApp message.
 
- Choose the desired Canvas and Canvas steps.

#### Filter by campaign or Canvas attribution

Filter for users who have opened/read to a specific WhatsApp campaign or Canvas component or tag.

- 

New Stuff!
