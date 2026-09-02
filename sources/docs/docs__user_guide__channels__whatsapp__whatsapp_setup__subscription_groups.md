---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups
slug: docs__user_guide__channels__whatsapp__whatsapp_setup__subscription_groups
title: "WhatsApp subscription groups"
description: "This article outlines WhatsApp subscription groups, what subscription states are offered, and how subscription groups are set."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# WhatsApp subscription groups

WhatsApp subscription groups are created upon integrating WhatsApp with your app through the Technology Partner Portal. For a cross-channel overview of subscription groups, see Subscription groups.

note

You can add up to 450 subscription groups per workspace.

## WhatsApp subscription states

For WhatsApp subscription state definitions and how they relate to Meta opt-in requirements, see Subscription status.

### Setting users’ WhatsApp subscription groups

- Rest API: User profiles can be programmatically set by the /subscription/status/set endpoint using the Braze REST API.
 
- Web SDK: Users can be added to an email, SMS, or WhatsApp subscription group using the addToSubscriptionGroup method for Android, iOS, or Web.
 
- User import: Users can be added to email or SMS subscription groups via Import Users. When updating the subscription group status, you must have these two columns in your CSV: subscription_group_id and subscription_state. Refer to User import for more information.

### Checking a user’s WhatsApp subscription group

- 
 
User Profile: Individual user profiles can be accessed through the Braze dashboard from Audience > Search Users. Here, you can look up user profiles by email address, phone number, or external user ID. When you’re inside a user profile, under the Engagement tab, you can view a user’s WhatsApp subscription group and their status.

- 
 
Rest API: Individual user profiles subscription group can be viewed by the List user’s subscription groups endpoint or List user’s subscription group status endpoint by using Braze’s REST API.

## Archive subscription groups

If you need to stop using a WhatsApp subscription group, you can archive it to mark it as inactive.

Archiving a subscription group marks it as inactive but does not delete it from your workspace. If you need to remove a WhatsApp phone number or subscription group entirely, you must first archive the subscription group in the Subscription Group Manager before requesting deletion from Braze support.

To archive a subscription group:

- Go to Audience > Subscription Group Management.
 
- Find the WhatsApp subscription group you want to archive.
 
- Hover over the status for the subscription group and select Archive.

## WhatsApp opt-in and opt-out process

For an overview of WhatsApp subscription status, opt-in requirements, and opt-out behavior, see Subscription status.

Currently, users can subscribe and opt-in and opt-out to WhatsApp messaging in various ways, including SMS, through a website, a WhatsApp thread, phone, or in person. Note that opt-ins are required.

Opt-in keywords are not currently supported for the WhatsApp channel, so you are responsible for maintaining a user list. WhatsApp has a retrospective approach to opt-ins and rate limits: if users start reporting or blocking you, your rate limit is lowered.

## Updating a user’s subscription status to a WhatsApp Canvas

Regardless of the opt-in and opt-out methods you use, you can update the subscription status of user profiles with one of the following update methods:

- Create a Braze-to-Braze webhook that updates the subscription status via REST API, such as in the following example:

To avoid race conditions, any follow-up messaging after the webhook should be contained in a second Canvas that is triggered by outcomes from the first Canvas (such as a user has entered a Canvas variation and is in a WhatsApp subscription group).

- 
 
Use the advanced JSON editor to update the user profile with the following template:

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

```
 | 
```
 {
 "attributes": [
 {
 "subscription_groups": [{
 "subscription_group_id": "subscription_group_identifier_1",
 "subscription_state": "unsubscribed"
 },
 {
 "subscription_group_id": "subscription_group_identifier_2",
 "subscription_state": "subscribed"
 },
 {
 "subscription_group_id": "subscription_group_identifier_3",
 "subscription_state": "subscribed"
 }
 ]
 }
 ]
 }

```
 | 

note

Updates to a user’s subscription status may take up to 60 seconds.

- 

New Stuff!
