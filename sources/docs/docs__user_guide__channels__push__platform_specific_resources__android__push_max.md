---
url: https://www.braze.com/docs/user_guide/channels/push/platform_specific_resources/android/push_max
slug: docs__user_guide__channels__push__platform_specific_resources__android__push_max
title: "Push Max"
description: "Push Max amplifies Android push notifications by tracking failed push notifications and resending the push when the user is more likely to receive it."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Push Max

Learn about Push Max and how you can use this feature to potentially improve the deliverability of Android push notifications to Chinese OEM devices.

## What is Push Max?

Push Max amplifies Android push notifications by tracking failed push notifications and resending the push when the user is more likely to receive it.

Some Android devices manufactured by Chinese Original Equipment Manufacturers (OEMs), such as Xiaomi, OPPO, and Vivo, employ a robust battery optimization scheme to extend battery life. This behavior may have the unintended consequence of shutting down background app processing, which reduces the deliverability of push notifications on these devices if the app is not in the foreground. This circumstance occurs most often in the Asia-Pacific (APAC) markets.

## Availability

- Available for Android push notifications only
 
- Not supported for action-based or API-triggered messages
 
- Not supported when the option to only send to the user’s last used device is selected

## Prerequisites

Push notifications sent using Push Max will only be delivered to devices that have at least the following minimum SDK version:

   Android: 29.0.1+  

## Using Push Max

- campaigns
 
- canvas

To use Push Max in your campaign:

- Create a push campaign.
 
- Select Android Push as your platform.
 
- Go to the Schedule Delivery step.
 
- Select Send using Push Max.

To use Push Max in your Canvas:

- Add a Message step to your Canvas.
 
- Select Android Push as your platform.
 
- Go to the Delivery Settings tab.
 
- Select Send using Push Max.

The following two features, Intelligent Timing and Time to Live, can be used in tandem with Push Max to potentially increase the deliverability of your Android push notifications.

### Intelligent Timing

Push Max works best when Intelligent Timing is turned on. Intelligent Timing can calculate and send the push notification at a time when the user is most likely to be using the app and the push is most likely to be delivered.

### Time to Live (TTL)

Time to Live (TTL) can track failed push notifications to Firebase Cloud Messaging (FCM) and retry the notification when the user is likely to receive it.

By default, Time to Live is set to 28 days, which is the maximum. You can decrease the default TTL for all new Android push messages from Settings > Workspace Settings > Push Settings, or you can configure the number of days on a per message basis in the Settings tab when composing an Android push notification.

## Things to know

### Promotion codes

We recommend that you don’t use Braze promotion codes in messages where Push Max is turned on.

This is because promotion codes are unique. If a push notification that contains a promotion code fails to deliver, when that notification is resent due to Push Max, a new promotion code will be sent. This can result in you consuming promotion codes faster than expected.

### Canvas event properties and entry properties

Push Max may not work as expected if you include Liquid references to Canvas entry properties or event properties in your message. This is because the entry and event properties are not available when Push Max is attempting to resend the message.

- 

New Stuff!
