---
url: https://www.braze.com/docs/developer_guide/push_notifications/silent
slug: docs__developer_guide__push_notifications__silent
title: "Silent push notifications"
description: "Silent push notifications Learn how to set up silent push notifications for the Braze SDK. android swift fireos Prerequisites Before you can use this feature,..."
section: developer_guide/push_notifications
fetched: 2026-09-02
evidence: company-own (technical)
---
# Silent push notifications

Learn how to set up silent push notifications for the Braze SDK.

- android
 
- swift
 
- fireos

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK. You’ll also need to set up push notifications.

## Setting up silent push notifications

Silent notifications are available through the Braze Messaging API. To take advantage of them, you need to set the send_to_sync flag to true within the Android push object and ensure there are no title or alert fields set as it will cause errors when used alongside send_to_sync—however, you can include data extras within the object.

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK. You’ll also need to set up push notifications.

## iOS limitations

The iOS operating system may gate notifications for some features. Note that if you are experiencing difficulties with these features, the iOS’s silent notifications gate might be the cause. For more details, refer to Apple’s instance method and unreceived notifications documentation.

## Setting up silent push notifications

To use silent push notifications to trigger background work, you must configure your app to receive notifications even when it is in the background. To do this, add the Background Modes capability using the Signing & Capabilities pane to the main app target in Xcode. Select the Remote notifications checkbox.

Even with the remote notifications background mode enabled, the system will not launch your app into the background if the user has force-quit the application. The user must explicitly launch the application or reboot the device before the app can be automatically launched into the background by the system.

For more information, refer to pushing background updates and the application:didReceiveRemoteNotification:fetchCompletionHandler: documentation.

## Sending silent push notifications

To send a silent push notification, set the content-available flag to 1 in a push notification payload.

note

What Apple calls a remote notification is just a normal push notification with the content-available flag set.

The content-available flag can be set in the Braze dashboard as well as within our Apple push object in the messaging API.

warning

Attaching both a title and body with content-available=1 is not recommended because it can lead to undefined behavior. To ensure that a notification is truly silent, exclude both the title and body when setting the content-available flag to 1. For further details, refer to the official Apple documentation on background updates.

When sending a silent push notification, you might also want to include some data in the notification payload, so your application can reference the event. This could save you a few networking requests and increase the responsiveness of your app.

## Ignoring internal push notifications

Braze uses silent push notifications to internally handle certain advanced features, such as uninstall tracking. If your app takes automatic actions on application launches or background pushes, consider gating that activity so it’s not triggered by any internal push notifications.

For example, if you have logic that calls your servers for new content upon every background push or application launch, you may want to prevent triggering Braze’s internal pushes to avoid unnecessary network traffic. Because Braze sends certain kinds of internal pushes to all users at approximately the same time, significant server load may occur if on-launch network calls from internal pushes are not gated.

### Step 1: Check your app for automatic actions

Check your application for automatic actions in the following places and update your code to ignore Braze’s internal pushes:

- Push Receivers. Background push notifications will call application:didReceiveRemoteNotification:fetchCompletionHandler: on the UIApplicationDelegate.
 
- Application Delegate. Background pushes can launch suspended apps into the background, triggering the application:willFinishLaunchingWithOptions: and application:didFinishLaunchingWithOptions: methods on your UIApplicationDelegate. Check the launchOptions of these methods to determine if the application has been launched from a background push.

### Step 2: Use the internal push utility method

You can use the static utility method in Braze.Notifications to check if your app has received or was launched by a Braze internal push. Braze.Notifications.isInternalNotification(_:) returns true for all Braze internal push notifications, which include uninstall tracking and Feature flags sync notifications.

For example:

- swift
 
- objective-c

```

1
2
3
4
5
6
7

```
 | 
```
func application(_ application: UIApplication,
 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
 if (!Braze.Notifications.isInternalNotification(userInfo)) {
 // Gated logic here (for example pinging server for content)
 }
}

```
 | 

```

1
2
3
4
5

```
 | 
```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
 if (![BRZNotifications isInternalNotification:userInfo]) {
 // Gated logic here (for example pinging server for content)
 }
}

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK. You’ll also need to set up push notifications.

## Setting up silent push notifications

Silent notifications are available through the Braze Messaging API. To take advantage of them, you need to set the send_to_sync flag to true within the Android push object and ensure there are no title or alert fields set as it will cause errors when used alongside send_to_sync—however, you can include data extras within the object.

- 

New Stuff!
