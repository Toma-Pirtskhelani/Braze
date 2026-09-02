---
url: https://www.braze.com/docs/user_guide/channels/push/platform_specific_resources/android/notification_options
slug: docs__user_guide__channels__push__platform_specific_resources__android__notification_options
title: "Notification options"
description: "This reference article covers several Android notification options and how to best use them within Braze campaigns."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Notification options

These are the some of the Android-specific push notification options available through Braze.

## Silent notifications

When you compose your push notification message, you cannot send an Android push message without a title—however, you can enter a single space instead. Keep in mind, if your message only contains a single space, it will be sent as a silent push notification. For more information, see Silent push notifications.

## Notification groups

If you want to categorize your messages and group them in your user’s notification tray, you can utilize Android’s Notification Channels feature through Braze.

First, create your Android push campaign, then look to the top of the Compose tab for the Notification Channel dropdown.

Select your Notification Channel from the dropdown. You must also select a fallback channel in the event that your Notification Channel settings malfunction.

If you don’t have any Notification Channels listed here, you can add one using the Notification Channel ID. Contact your developers to identify what your Notification Channel IDs are or to create new IDs as needed.

To add a Notification ID to your Notification Channel, click Manage Notification Channel in the Notification Channel dropdown menu and fill out the required fields. Notification Channels must be defined on the app before they can be used in the Braze platform.

- 

New Stuff!
