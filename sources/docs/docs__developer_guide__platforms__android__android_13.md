---
url: https://www.braze.com/docs/developer_guide/platforms/android/android_13
slug: docs__developer_guide__platforms__android__android_13
title: "Upgrading to Android 13"
description: "This article covers Android 13, SDK updates, changes to push permission, SDK compatibility, and more."
section: developer_guide/platforms
fetched: 2026-09-02
evidence: company-own (technical)
---
# Upgrading to Android 13

This guide describes relevant changes introduced in Android 13 (2022) and the required upgrade steps for your Braze Android SDK integration.

Refer to the Android 13 developer documentation for a full migration guide.

## Android 13 Braze SDK

To prepare for Android 13, upgrade your Braze SDK to the latest version (v21.0.0+). Doing so gives you access to the “no-code” push primer feature.

## Changes in Android 13

### Push permission

Android 13 introduces a major change in how users manage apps that send push notifications. In Android 13, apps are required to obtain permission before push notifications can be shown.

This new permission follows a similar pattern to iOS and Web push, where you only have one attempt to obtain permission. If a user chooses Don't Allow or dismisses the prompt, your app cannot ask for permission again.

Note that apps are granted an exemption for users who previously had push notifications enabled prior to updating to Android 13. These users will remain eligible to receive push when they update to Android 13 without having to request permission.

#### Permission prompt timing

Targeting Android 13

Apps targeting Android 13 can control when to request permission and show the native push prompt.

If your user upgrades from Android 12 to 13, your app was previously installed, and you were already sending push, the system automatically pre-grants the new notification permission to all eligible apps. In other words, these apps can continue to send notifications to users, and users don’t see a runtime permission prompt.

For more details on this see Android’s Developer Documentation for effects on updates to existing apps.

Targeting Android 12 or earlier

If your app does not yet target Android 13, then when a new user on Android 13 installs your app, they automatically see a push permission prompt when your app creates its first notification channel (via notificationManager.createNotificationChannel). Users who already have your app installed and then upgrade to Android 13 are never shown a prompt and are automatically granted push permission.

note

Braze SDK v23.0.0 automatically creates a default notification channel if one does not already exist when a push notification is received. If you don’t target Android 13, this causes the push permission prompt to be shown, which is required to show the notification.

## Preparing for Android 13

It is strongly recommended that your app targets Android 13 in order to control when users are prompted for push permission.

Targeting Android 13 lets you optimize your push opt-in rates by prompting users at more appropriate times and leads to a better user experience in how and when your app asks for push permission.

To start using our new “no-code” push primer feature, upgrade your Android SDK to the latest version (v23.0.0+).

- 

New Stuff!
