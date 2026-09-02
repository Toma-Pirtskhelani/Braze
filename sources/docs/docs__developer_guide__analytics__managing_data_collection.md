---
url: https://www.braze.com/docs/developer_guide/analytics/managing_data_collection
slug: docs__developer_guide__analytics__managing_data_collection
title: "Manage data collection"
description: "Learn how to manage data collection for the Braze SDK."
section: developer_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Manage data collection

Learn how to manage data collection for the Braze SDK, so you can comply with any data-privacy regulations as needed.

- web
 
- android
 
- swift
 
- react native
 
- roku

## Disabling data tracking

note

This guide uses code samples from the Braze Web SDK 4.0.0+. To upgrade to the latest Web SDK version, see SDK Upgrade Guide.

- standard implementation
 
- google tag manager

To disable data-tracking activity on the Web SDK, use the method disableSDK(). This will sync any data logged before disableSDK() was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored.

Use the Disable Tracking or Resume Tracking tag type to disable or re-enable web tracking, respectively. These two options call disableSDK and enableSDK.

### Best practices

To provide users with the option to stop tracking, we recommend building a simple page with two links or buttons: one that calls disableSDK() when clicked, and another that calls enableSDK() to allow users to opt back in. You can use these controls to start or stop tracking via other data sub-processors as well.

note

The Braze SDK does not need to be initialized to call disableSDK(), allowing you to disable tracking for fully anonymous users. Conversely,enableSDK() does not initialize the Braze SDK so you must also call initialize() afterward to enable tracking.

## Resuming data tracking

To resume data collection, you can use the enableSDK() method.

## Logout and Unregister Push

The Braze SDK provides methods to stop targeting a device when a user unregisters from push notifications or logs out. These methods remove push registration data from the current user on the Braze server and the SDK, so Braze no longer sends future push notification campaigns to that user.

### Logout

When a user logs out from an application, call the SDK’s logout method to remove the device’s push registration from the current user and automatically perform cleanup actions on the SDK. The logout method performs the following:

- Unregisters the device’s push token from the current user on the Braze server.
 
- If the unregister call succeeds, the SDK wipes locally-stored SDK data and disables the SDK.
 
- On failure, invokes the errorCallback to allow the integrator to take action.

The following example shows callback-based logout handling. Use it when you need immediate success and error handling, and replace the logging with your app flow.

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

```
 | 
```
import { logout } from "@braze/web-sdk";

const successCallback = () => {
 console.log('Successfully logged out');
};

const errorCallback = () => {
 console.log('Failed to log out');
};

logout(successCallback, errorCallback);

```
 | 

#### Re-enable tracking and push after logout

After a successful logout, call enableSDK(), then re-register for notifications with your operating system (OS) or push provider by following Web push setup.

#### Avoid immediate unregister calls

Avoid calling logout or unregisterPush directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

### Unregister Push

To stop sending push to a device without additional automated cleanup, use the unregisterPush method. This removes the device’s push token from the current user on Braze’s server, and clears the locally-stored token.

The following example shows callback-based unregisterPush handling. Use it when you need immediate success and error handling, and replace the logging with your app flow.

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

```
 | 
```
import { unregisterPush } from "@braze/web-sdk";

const successCallback = () => {
 console.log('Successfully unregistered from push');
};

const errorCallback = () => {
 console.log('Failed to unregister from push');
};

unregisterPush(successCallback, errorCallback);

```
 | 

#### Re-register push after unregisterPush

After calling unregisterPush, re-register for notifications with your OS or push provider by following Web push setup before sending Braze push notifications again.

note

On supported browsers, when an active push subscription exists, unregisterPush also unregisters the Braze-managed service worker after unsubscribing from the browser Push API. If you set manageServiceWorkerExternally to true, the SDK does not unregister the service worker for you.

#### Avoid immediate unregister calls

Avoid calling logout or unregisterPush directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

## Google Play privacy questionnaire

Starting in April 2022, Android developers must complete Google Play’s Data safety form to disclose privacy and security practices. This guide provides instructions on how to fill out this new form with information on how Braze handles your app data.

As the app developer, you are in control of what data you send to Braze. Data received by Braze is processed according to your instructions. This is what Google classifies as a service provider.

important

This article provides information related to the data the Braze SDK processes as related to the Google safety section questionnaire. This article is not providing legal advice, so we recommend consulting with your legal team before submitting any information to Google.

### Questions

 Questions | 
 Answers for Braze SDK | 

 Does your app collect or share any of the required user data types? | 
 Yes, the Braze Android SDK collects data as configured by the app developer. | 

 Is all of the user data collected by your app encrypted in transit? | 
 Yes. | 

 Do you provide a way for users to request that their data be deleted? | 
 Yes. | 

For more information about handling user requests for their data and deletion, see Braze Data Retention Information.

### Data collection

The data collected by Braze is determined by your specific integration and the user data you choose to collect. To learn more about what data Braze collects by default and how to disable certain attributes, see our SDK data collection options.

 Category | 
 Data type | 
 Braze Usage | 

 Location | 
 Approximate location | 
 Not collected by default. | 

 Precise location | 

 Personal Info | 
 Name | 

 Email address | 

 User IDs | 

 Address | 

 Phone number | 

 Race and ethnicity | 

 Political or religious beliefs | 

 Sexual orientation | 

 Other info | 

 Financial info | 
 User payment info | 

 Purchase history | 

 Credit score | 

 Other financial info | 

 Health and fitness | 
 Health info | 
 Not collected by default. | 

 Fitness info | 

 Messages | 
 Emails | 
 Not collected by default. | 

 SMS or MMS | 

 Other in-app messages | 
 If you send In-app messages or push notifications through Braze, we collect information on when users have opened or read these messages. | 

 Photos and videos | 
 Photos | 
 Not collected. | 

 Videos | 

 Audio files | 
 Voice or sound recordings | 

 Music files | 

 Other audio files | 

 Files and docs | 
 Files and docs | 

 Calendar | 
 Calendar events | 

 Contacts | 
 Contacts | 

 App activity | 
 App interactions | 
 Braze collects session activity data by default. All other interactions and activity is determined by your app's custom integration. | 

 In-app search history | 
 Not collected. | 

 Installed apps | 
 Not collected. | 

 Other user-generated content | 
 Not collected by default. | 

 Other actions | 

 Web browsing | 
 Web browsing history | 
 Not collected. | 

 App information and performance | 
 Crash logs | 
 Braze collects crash logs for errors that occur within the SDK. This contains the user's phone model and OS level, along with a Braze specific user ID. | 

 Diagnostics | 
 Not collected. | 

 Other app performance data | 
 Not collected. | 

 Device or other IDs | 
 Device or other IDs | 
 Braze generates a device ID to differentiate users' devices, and checks if messages are sent to the correct intended device. | 

To learn more about other device data that Braze collects which may fall outside the scope of Google Play’s data safety guidelines, see our Android storage overview and our SDK data collection options.

## Disabling data tracking

To disable data-tracking activity on the Android SDK, use the method disableSDK(). This will cause all network connections to be canceled, meaning the Braze SDK will no longer pass any data to Braze servers.

## Wiping previously-stored data

You can use the method wipeData() to fully clear all client-side data stored on the device.

## Resuming data tracking

To resume data collection, you can use the enableSDK() method. Keep in mind, this will not restore any previously wiped data.

## Logout and Unregister Push

The Braze SDK provides methods to stop targeting a device when a user unregisters from push notifications or logs out. These methods remove push registration data from the current user on the Braze server and the SDK, so Braze no longer sends future push notification campaigns to that user.

### Logout

When a user logs out from an application, call the SDK’s logout method to remove the device’s push registration from the current user and automatically perform cleanup actions on the SDK. The logout method performs the following:

- Unregisters the device’s push token from the current user on the Braze server.
 
- If the unregister call succeeds, the SDK wipes locally-stored SDK data and disables the SDK.
 
- On failure, raises an error and an isRetriable flag to allow the integrator to take action.

The following callback example shows logout success and error handling. Use it for callback-based logout flows, and replace the logging with your retry or re-authentication logic.

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

```
 | 
```
// Completion callback
Braze.getInstance(context).logout { result ->
 result
 .onSuccess {
 Log.d(TAG, "Logout successful")
 }
 .onFailure { error ->
 val pushError = error as? BrazePushUnregistrationException
 Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
 }
}

```
 | 

The following coroutine example shows the suspending logout API. Use it in coroutine-based flows and customize the success and failure branches for your app.

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

```
 | 
```
lifecycleScope.launch {
 runCatching { Braze.getInstance(context).logout() }
 .onSuccess {
 Log.d(TAG, "Logout successful")
 }
 .onFailure { error ->
 val pushError = error as? BrazePushUnregistrationException
 Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
 }
}

```
 | 

#### Re-enable tracking and push after logout

After a successful logout, re-enable the SDK with enableSDK(), then re-register for notifications with your operating system (OS) or push provider by following Android push setup.

#### Avoid immediate unregister calls

Avoid calling logout or unregisterPush directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

### Unregister Push

To stop sending push to a device without additional automated cleanup, use the unregisterPush method. This removes the device’s push token from the current user on Braze’s server, and clears the locally-stored token.

The following callback example shows how to handle unregisterPush results. Use it when your flow is callback-based, and replace the logging with your own retry handling.

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

```
 | 
```
// Completion callback
Braze.getInstance(context).unregisterPush { result ->
 result
 .onSuccess {
 Log.d(TAG, "Push unregistered successfully")
 }
 .onFailure { error ->
 val pushError = error as? BrazePushUnregistrationException
 Log.e(
 TAG,
 "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
 )
 }
}

```
 | 

The following coroutine example shows the suspending unregisterPush API. Use it in coroutine-based flows and customize the success and failure branches for your app.

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

```
 | 
```
lifecycleScope.launch {
 runCatching { Braze.getInstance(context).unregisterPush() }
 .onSuccess {
 Log.d(TAG, "Push unregistered successfully")
 }
 .onFailure { error ->
 val pushError = error as? BrazePushUnregistrationException
 Log.e(
 TAG,
 "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
 )
 }
}

```
 | 

#### Re-register push after unregisterPush

After calling unregisterPush, re-register for notifications with your OS or push provider by following Android push setup before sending Braze push notifications again.

#### Avoid immediate unregister calls

Avoid calling logout or unregisterPush directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

## Apple’s privacy manifest

### What is tracking data?

Apple defines “tracking data” as data collected in your app about an end user or device that’s linked to third-party data (such as targeted advertising), or a data broker. For a complete definition with examples, see Apple: Tracking.

By default, the Braze SDK does not collect tracking data. However, depending on your Braze SDK configuration, you may be required to list Braze-specific data in your app’s privacy manifest.

### What is a privacy manifest?

A privacy manifest is a file in your Xcode project that describes the reason your app and third-party SDKs collect data, along with their data-collection methods. Each of your third-party SDKs that track data require its own privacy manifest. When you create your app’s privacy report, these privacy manifest files are automatically aggregated into a single report.

### API tracking-data domains

Starting with iOS 17.2, Apple will block all declared tracking endpoints in your app until the end user accepts an Ad Tracking Transparency (ATT) prompt. Braze provides tracking endpoints to route your tracking data, while still allowing you to route non-tracking first-party data to the original endpoint.

## Declaring Braze tracking data

tip

For a full walkthrough, see the Privacy Tracking Data tutorial.

### Prerequisites

The following Braze SDK version is required to implement this feature:

   Swift: 9.0.0+  

### Step 1: Review your current policies

Review your Braze SDK’s current data-collection policies with your legal team to determine whether your app collects tracking data as defined by Apple. If you’re not collecting any tracking data, you don’t need to customize your privacy manifest for the Braze SDK at this time. For more information about the Braze SDK’s data-collection policies, see SDK data collection.

important

If any of your non-Braze SDKs collect tracking data, you’ll need to review those policies separately.

### Step 2: Create a privacy manifest

First, check if you already have a privacy manifest by searching for a PrivacyInfo.xcprivacy file in your Xcode project. If you already have this file, you can continue to the next step. Otherwise, see Apple: Create a privacy manifest.

### Step 3: Add your endpoint to the privacy manifest

In your Xcode project, open your app’s PrivacyInfo.xcprivacy file, then right-click the table and check Raw Keys and Values.

Under App Privacy Configuration, choose NSPrivacyTracking and set its value to YES.

Under App Privacy Configuration, choose NSPrivacyTrackingDomains. In the domains array, add a new element and set its value to the endpoint you previously added to your AppDelegate prefixed with sdk-tracking.

### Step 4: Declare your tracking data

Next, open AppDelegate.swift then list each tracking property you want to declare by creating a static or dynamic tracking list. Keep in mind, Apple will block these properties until the end user accepts their ATT prompt, so only list the properties you and your legal team consider tracking. For example:

- static example
 
- dynamic example

In the following example, dateOfBirth, customEvent, and customAttribute are declared as tracking data within a static list.

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
20
21
22
23
24

```
 | 
```
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

 static var braze: Braze? = nil

 func application(
 _ application: UIApplication,
 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
 ) -> Bool {
 let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
 // Declare which types of data you wish to collect for user tracking.
 configuration.api.trackingPropertyAllowList = [
 .dateOfBirth,
 .customEvent(["event-1"]),
 .customAttribute(["attribute-1", "attribute-2"])
 ]
 let braze = Braze(configuration: configuration)
 AppDelegate.braze = braze
 return true
 }
}

```
 | 

In the following example, the tracking list is automatically updated after the end user accepts the App Tracking Transparency (ATT) prompt. Requesting authorization on app activation is a per-scene event, so this code belongs in your SceneDelegate.swift file’s sceneDidBecomeActive(_:) method rather than AppDelegate.swift’s applicationDidBecomeActive(_:) (required for apps that have adopted the UIScene life cycle). Your Braze instance remains reachable from SceneDelegate through the AppDelegate.braze static property configured in Step 1.

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

```
 | 
```
func sceneDidBecomeActive(_ scene: UIScene) {
 // Request and check your user's tracking authorization status.
 ATTrackingManager.requestTrackingAuthorization { status in
 // Let Braze know whether user data is allowed to be collected for tracking.
 let enableAdTracking = status == .authorized
 AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

 // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
 AppDelegate.braze?.updateTrackingAllowList(
 adding: [.firstName, .lastName],
 removing: [.everything]
 )
 }
}

```
 | 

### Step 5: Prevent infinite retry loops

To prevent the SDK from entering an infinite retry loop, use the set(adTrackingEnabled: enableAdTracking) method to handle ATT permissions. The adTrackingEnabled property in your SceneDelegate.swift method should be handled similar to the following:

```

1
2
3
4
5
6
7
8

```
 | 
```
func sceneDidBecomeActive(_ scene: UIScene) {
 // Request and check your user's tracking authorization status.
 ATTrackingManager.requestTrackingAuthorization { status in
 // Let Braze know whether user data is allowed to be collected for tracking.
 let enableAdTracking = status == .authorized
 AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
 }
}

```
 | 

## Disabling data tracking

To disable data-tracking activity on the Swift SDK, set the enabled property to false on your Braze instance. When enabled is set to false, the Braze SDK ignores any calls to the public API. The SDK also cancels all in-flight actions, such as network requests, event processing, etc.

## Wiping previously-stored data

You can use the wipeData() method to fully clear locally-stored SDK data on a user’s device.

For Braze Swift versions 7.0.0 and later, the SDK and the wipeData() method randomly generates a UUID for their device ID. However, if your useUUIDAsDeviceId is set to false or you’re using Swift SDK version 5.7.0 or earlier, you’ll also need to make a post request to /users/delete since your Identifier for Vendors (IDFV) will automatically be used as that user’s device ID.

If you use manual push integration, and your app calls wipeData() and later re-enables the SDK in the same app run, call registerForRemoteNotifications() again so Braze can receive a refreshed device token. For more information, see setting up push notifications.

## Resuming data tracking

To resume data collection, set enabled to true. Keep in mind, this will not restore any previously wiped data.

## Logout and Unregister Push

The Braze SDK provides methods to stop targeting a device when a user unregisters from push notifications or logs out. These methods remove push registration data from the current user on the Braze server and the SDK, so Braze no longer sends future push notification campaigns to that user.

### Logout

When a user logs out from an application, call the SDK’s logout method to remove the device’s push registration from the current user and automatically perform cleanup actions on the SDK. The logout method performs the following:

- Unregisters the device’s push token, and any Live Activities push-to-start tokens, from the current user on the Braze server.
 
- If the unregister call succeeds, the SDK wipes locally-stored SDK data and disables the SDK.
 
- On failure, raises an error and an isRetriable flag to allow the integrator to take action.

- swift
 
- objective-c

The following completion-handler example shows logout success and failure handling. Use it for callback-based flows, and replace the logging with your app’s retry or re-authentication logic.

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
// Completion handler
AppDelegate.braze?.logout { result in
 switch result {
 case .success:
 print("Logout successful")
 case .failure(let error):
 print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
 }
}

```
 | 

The following async example shows the suspending logout API. Use it for async workflows and customize the success and failure branches for your app.

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
// Async/await
do {
 try await AppDelegate.braze?.logout()
 print("Logout successful")
} catch let error as Braze.LogoutErrorResult {
 print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
}

```
 | 

This Objective-C example shows completion-based logout handling. Use it in Objective-C integrations and replace the logging with your app flow.

```

1
2
3
4
5
6

```
 | 
```
[AppDelegate.braze logoutWithCompletion:^(NSError * _Nullable error) {
 if (error) {
 NSNumber *isRetriable = error.userInfo[BRZLogoutErrorUserInfoKey.isRetriable];
 NSLog(@"Logout failed: %@, isRetriable=%@", error.localizedDescription, isRetriable);
 }
}];

```
 | 

note

logout does not end currently-running Live Activities. In the success callback, manually end any running Live Activities using ActivityKit’s end(_:dismissalPolicy:) method.

#### Re-enable tracking and push after logout

After a successful logout, set enabled back to true, then re-register for notifications with your operating system (OS) or push provider by following Swift push setup.

#### Avoid immediate unregister calls

Avoid calling logout or unregisterPush directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

### Unregister Push

To stop sending push to a device without additional automated cleanup, use the unregisterPush method. This removes the device’s push token from the current user on Braze’s server, and clears the locally-stored token.

- swift
 
- objective-c

The following completion-handler example shows unregisterPush success and failure handling. Use it for callback-based flows, and replace the logging with your own retry logic.

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
// Completion handler
AppDelegate.braze?.notifications.unregisterPush { result in
 switch result {
 case .success:
 print("Push unregistered successfully")
 case .failure(let error):
 print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
 }
}

```
 | 

The following async example shows the suspending unregisterPush API. Use it for async workflows and customize the success and failure branches for your app.

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
// Async/await
do {
 try await AppDelegate.braze?.notifications.unregisterPush()
 print("Push unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
 print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}

```
 | 

This Objective-C example shows completion-based unregisterPush handling. Use it in Objective-C integrations and replace the logging with your app flow.

```

1
2
3
4
5
6
7
8

```
 | 
```
[AppDelegate.braze.notifications unregisterPushWithCompletion:^(NSError * _Nullable error) {
 if (error) {
 NSNumber *isRetriable = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.isRetriable];
 NSNumber *statusCode = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.httpStatusCode];
 NSLog(@"Push unregistration failed: %@, isRetriable=%@ status=%@",
 error.localizedDescription, isRetriable, statusCode);
 }
}];

```
 | 

#### Re-register push after unregisterPush

After calling unregisterPush, re-register for notifications with your OS or push provider by following Swift push setup before sending Braze push notifications again.

#### Avoid immediate unregister calls

Avoid calling logout or unregisterPush directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

### Unregister push-to-start tokens for Live Activities

Live Activities can be started remotely using push-to-start tokens. To stop Braze from remotely starting Live Activities on a device, call the unregisterPushToStart method to unregister all currently-registered types (default) or a specified list of Activity types.

Note that currently-running Live Activities continue to receive updates and that this method will only remove the ability to start new activities remotely. For more information on Live Activities, see Live Activities.

#### End any running Live Activities

unregisterPushToStart does not end currently-running Live Activities. In the success callback, manually end any running Live Activities using ActivityKit’s end(_:dismissalPolicy:) method.

note

Avoid calling logout or unregisterPushToStart directly after calling registerPushToStart for a Live Activity. Due to the asynchronous nature of server processing, in rare cases, this can lead to the push-to-start token being re-added to the Braze user.

The following example shows how to unregister all push-to-start activity types. Use it when a signed-out user should no longer receive new remotely started Live Activities.

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

```
 | 
```
// Unregister all currently-registered activity types
// Completion handler
AppDelegate.braze?.liveActivities.unregisterPushToStart { result in
 switch result {
 case .success:
 print("Push-to-start unregistered successfully")
 case .failure(let error):
 print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
 }
}

// Async/await
do {
 try await AppDelegate.braze?.liveActivities.unregisterPushToStart()
 print("Push-to-start unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
 print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}

```
 | 

The following example shows how to unregister specific activity types. Use it when only selected Live Activities should stop being started remotely.

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
// Unregister specific activity types
AppDelegate.braze?.liveActivities.unregisterPushToStart(types: ["ActivityType1", "ActivityType2"]) { result in
 switch result {
 case .success:
 print("Push-to-start unregistered successfully")
 case .failure(let error):
 print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
 }
}

```
 | 

note

unregisterPushToStart doesn’t have an Objective-C API, as Live Activities rely on Swift-only types.

## IDFV collection

In previous versions of the Braze iOS SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user’s device ID. Beginning in Swift SDK v5.7.0, the IDFV field was optionally disabled, and instead, Braze would set a random UUID as the device ID. Starting in Swift SDK v7.0.0, the IDFV field will not be collected by default, and a UUID will be set as the device ID instead.

The useUUIDAsDeviceId feature configures the Swift SDK to set the device ID as a UUID. Traditionally, the iOS SDK would assign the device ID equal to the Apple-generated IDFV value. With this feature enabled by default on your iOS app, all new users created through the SDK would be assigned a device ID equal to a UUID.

If you still want to collect IDFV separately, you can use set(identifierforvendor:).

note

Apple is responsible for creating IDFV, and IDFV is Apple-managed. Braze does not transform or change IDFVs, and Apple makes no guarantees about casing or format.

note

Reading braze.deviceId blocks the calling thread until the SDK has completed its post-initialization operations. For main-thread or latency-sensitive contexts, use the non-blocking alternatives instead.

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
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.getDeviceId { deviceId in
 print("Device ID:", deviceId)
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let deviceId = await AppDelegate.braze?.getDeviceId()

```
 | 

```

1
2
3
4

```
 | 
```
// Completion handler — always delivers on the main thread.
[AppDelegate.braze getDeviceIdWithCompletion:^(NSString *deviceId) {
 NSLog(@"Device ID: %@", deviceId);
}];

```
 | 

### Considerations

#### SDK Version

In Swift SDK v7.0.0+, when useUUIDAsDeviceId is enabled (default), all new users created will be assigned a random device ID. All previously existing users will maintain their same device ID value, which may have been IDFV.

When this feature is not enabled, devices will continue to be assigned IDFV upon creation.

#### Downstream

Technology partners: When this feature is enabled, any technology partners that derive the IDFV value from the Braze device ID will no longer have access to this data. If the IDFV value derived from the device is needed for your partner integration, we recommend that you set this feature to false.

Currents: useUUIDAsDeviceId set to true means the device ID sent in Currents will no longer equal the IDFV value.

### Frequently asked questions

#### Will this change impact my existing users in Braze?

No. When enabled, this feature will not overwrite any user data in Braze. New UUID device IDs will only be created for new devices or when wipedata() is called.

#### Can I turn this feature off after turning it on?

Yes, this feature can be toggled on and off at your discretion. Previously stored device IDs will never be overwritten.

#### Can I still capture the IDFV value through Braze elsewhere?

Yes, you can still optionally collect the IDFV through the Swift SDK (collection is disabled by default).

## Prerequisites

Before you can use this feature, you’ll need to integrate the React Native Braze SDK.

## Disabling data tracking

To disable data collection, use the disableSDK method. After calling this method, the Braze SDK stops sending data to Braze servers.

```

1

```
 | 
```
Braze.disableSDK();

```
 | 

## Resuming data tracking

To resume data collection after disabling it, use the enableSDK method.

```

1

```
 | 
```
Braze.enableSDK();

```
 | 

## Wiping data

To delete all locally stored Braze SDK data on the device, use the wipeData method. After calling this method, the SDK is disabled and must be re-enabled with enableSDK.

```

1

```
 | 
```
Braze.wipeData();

```
 | 

## Flushing data

To request an immediate flush of any pending data to Braze servers, use requestImmediateDataFlush.

```

1

```
 | 
```
Braze.requestImmediateDataFlush();

```
 | 

## Setting ad-tracking enabled

To inform Braze whether ad-tracking is enabled for this device, use the setAdTrackingEnabled method. The SDK does not automatically collect this data.

```

1

```
 | 
```
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");

```
 | 

The second parameter is the Google Advertising ID and is only used on Android.

## Updating the tracking property allow list (iOS only)

To update the list of data types declared for tracking, use updateTrackingPropertyAllowList. This is a no-op on Android.

```

1
2
3
4
5
6
7
8

```
 | 
```
Braze.updateTrackingPropertyAllowList({
 adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
 removing: [],
 addingCustomEvents: ["my_custom_event"],
 removingCustomEvents: [],
 addingCustomAttributes: ["my_custom_attribute"],
 removingCustomAttributes: []
});

```
 | 

For more information, refer to Privacy Manifest.

## Logout and Unregister Push

This feature is not yet supported on the React Native SDK.

## Prerequisites

Before you can use this feature, you’ll need to integrate the Roku Braze SDK.

## Wiping previously-stored data

The Roku SDK doesn’t include a wipeData method. To produce a clean-slate state functionally equivalent to wipeData() on other Braze SDKs, clear the four Braze registry sections, then re-initialize the SDK.

The Braze Roku SDK persists data across the following registry sections:

 Section | 
 Contents | 

 braze.section.device_id | 
 The device UUID used to identify this device in Braze. | 

 braze.section.user_id | 
 The external user ID, if one has been set. | 

 braze.section.session | 
 The active session UUID, start time, and end time. | 

 braze.section.config | 
 Cached SDK configuration and feature flag data. | 

### Step 1: Clear the registry sections

Use roRegistry.Delete() to delete each Braze section, then call Flush() to persist the changes:

```

1
2
3
4
5
6
7
8

```
 | 
```
sub WipeBrazeData()
 registry = CreateObject("roRegistry")
 registry.Delete("braze.section.device_id")
 registry.Delete("braze.section.user_id")
 registry.Delete("braze.section.session")
 registry.Delete("braze.section.config")
 registry.Flush()
end sub

```
 | 

### Step 2: Re-initialize the Braze SDK

When you initialize the Braze SDK again, the SDK handles the missing registry data gracefully:

- The device ID section is empty, so the SDK generates a new UUID and treats the device as anonymous.
 
- The user ID section is empty, so the SDK defaults to an anonymous user (an empty string "").
 
- The session section is empty, so the SDK starts a new session.
 
- The config section is empty, so the SDK re-fetches the configuration from the server.

note

The Roku SDK doesn’t generate any server-side delete request when you clear the registry. If you also need to remove the user from Braze, send a request to /users/delete using the user’s external_id or braze_id.

## Logout and Unregister Push

This feature is not yet supported on the Roku SDK.

- 

New Stuff!
