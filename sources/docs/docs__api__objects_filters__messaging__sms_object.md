---
url: https://www.braze.com/docs/api/objects_filters/messaging/sms_object
slug: docs__api__objects_filters__messaging__sms_object
title: "SMS object"
description: "This reference article explains the different components of the Braze SMS object."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# SMS object

The sms object allows you to modify or create SMS messages via our messaging endpoints.

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

```
 | 
```
{
 "subscription_group_id": (required, string) the ID of your subscription group,
 "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
 "body": (required, string),
 "app_id": (required, string) see App Identifier,
 "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
 "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
 "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.
}

```
 | 

- App identifier

- Any valid app_id from an app configured in your workspace works for all users in your workspace, regardless of whether the user has the specific app on their profile or not.

- 

New Stuff!
