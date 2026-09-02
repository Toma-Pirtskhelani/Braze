---
url: https://www.braze.com/docs/user_guide/audience/suppression_lists
slug: docs__user_guide__audience__suppression_lists
title: "Suppression lists"
description: "This page covers how to use suppression lists to specify which users should never receive your messages."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Suppression lists

Suppression lists are groups of users who automatically do not receive any campaigns or Canvases. Suppression lists are defined by segment filters, and users will enter and exit suppression lists as they meet filter criteria. You can also set exception tags so that the suppression list won’t apply to campaigns or Canvases with those tags. Messages from campaigns or Canvases with exception tags will still reach suppression list users who are in the target segments.

## Why use suppression lists?

Suppression lists are dynamic and automatically apply to all forms of messaging, but you can set exceptions for selected tags. If your selected exception tags are used in a campaign or Canvas, then that suppression list won’t apply to that campaign or Canvas. Messages from campaigns or Canvases with exception tags will still reach any suppression list users that are part of your target segments.

### Message types and channels affected by suppression lists

Suppression lists will apply to all message types and channels except for feature flags. This means that suppression lists by default apply to all channels, campaigns, and Canvases, including:

- API campaigns
 
- API-triggered campaigns and Canvases
 
- Transactional emails

The only message type that suppression lists do not apply to is feature flags. Users in a suppression list won’t be suppressed from feature flags, but will be suppressed from all other channels.

You can use exception tags so that suppression list users are still targeted by particular campaigns and Canvases. For details, refer to step 4 in Setting up suppression lists. If you do not add exception tags to a suppression list, then users in that suppression list will not be targeted with any messaging besides feature flags.

note

Suppression lists are applied to API campaigns that are created in the Braze dashboard with a campaign_id. Suppression lists don’t apply to messages sent through Braze messaging endpoints without an associated campaign_id.

## Setting up suppression lists

note

All users can view suppression lists, but only users with admin permissions can create and manage suppression lists.

- Go to Audience > Suppression Lists.
 
- Select Create Suppression List and add a name.
 
- Use segment filters to identify the users in your suppression lists. You must select at least one.

important

Though the setup process seems similar to segment creation, a suppression list is a group of users that you do not want to send messages to regardless of segment membership.

- Determine whether to have exceptions based on tag by checking the box beneath your segment name (refer to Why use suppression lists? for more information), then add the tags of campaigns or Canvases that users in this suppression list should still receive. 

In other words, if you add the exception tag “Shipping confirmation”, users in your suppression list will be excluded from all messaging except those that use the tag “Shipping confirmation”.

- Save or activate your suppression list.

- When you save, your suppression list will be saved but won’t be activated, which means it won’t go into effect. Your suppression list will remain inactive until you activate it, and inactive suppression lists won’t impact messaging (users won’t be excluded from messages).
 
- When you activate, your suppression list will be saved and immediately go into effect, which means users in your suppression list will immediately be excluded from campaigns or Canvases (except for ones containing an exception tag).

note

Only admins can save or activate suppression lists. You can have up to five active suppression lists at a time in the beta.

You can deactivate or archive suppression lists when you no longer need them.

- To deactivate, select an active suppression list and select Deactivate. Deactivated suppression lists can be reactivated later.
 
- To archive, do so from the Suppression Lists page.

## Suppression list usage

To check if your suppression list prevented a user from receiving a message, use User Lookup in the Target Audience step within your campaign or Canvas. Here, you’ll be able to see which suppression list they’re part of.

note

Suppression lists update before a message sends, not after a campaign launches. This means a user who is added to a suppression list after campaign launch but before the message sends could still receive the message.

tip

You can also find applied suppression lists in the Summary step.

While creating a campaign or Canvas, use User Lookup within the Target Audience step to search for a user, and if they aren’t in the target audience, you can see the suppression list they’re part of.

### Campaign

If a user is in a suppression list, they won’t receive a campaign for which that suppression list applies. Refer to Message types and channels affected by suppression lists for cases when a suppression list won’t apply.

### Canvas

From the moment a user is added to a suppression list, they will not enter Canvases. If they have already entered a Canvas, they won’t receive Message steps. This means that if a user is already inside a Canvas when they are added to a suppression list, they will advance through the Canvas until the next Message step, at which point they will exit without receiving the Message step.

For example, let’s say a Canvas has a User Update step followed by a Message step. If a user enters the Canvas and then is added to a suppression list, that user will still proceed through the User Update step (where they may be updated), and then exit at the Message step, at which point they will be included in the exited metrics.

- 

New Stuff!
