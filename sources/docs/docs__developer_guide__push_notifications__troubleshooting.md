---
url: https://www.braze.com/docs/developer_guide/push_notifications/troubleshooting
slug: docs__developer_guide__push_notifications__troubleshooting
title: "Troubleshoot push notifications"
description: "Diagnose push notification delivery and display issues using a symptom index, standard investigation path, and platform-specific SDK checks."
section: developer_guide/push_notifications
fetched: 2026-09-02
evidence: company-own (technical)
---
# Troubleshoot push notifications

Use this page to diagnose push notification delivery and display issues on a device. For dashboard-side delivery checks (subscription status, segments, caps), see Troubleshoot push.

Before you debug, add yourself as a test user and review Sending test messages.

## Start here: Match your symptom

Find the behavior you’re seeing in the table, then follow that section’s steps. If you’re not sure which section applies, use the standard investigation path.

 Symptom | 
 Go to | 

 Push not received on one platform | 
 Select your SDK tab in Platform-specific troubleshooting | 

 Line breaks around Liquid tags look wrong when saving | 
 Line breaks in push notifications | 

 Dashboard delivery checks (subscription, segment, caps) | 
 Troubleshoot push | 

 Deep link from push doesn’t open correctly | 
 Deep linking troubleshooting | 

 Common push error codes | 
 Common push error messages | 

## Standard investigation path

Use this workflow for every push notification incident. Start at step 1.

- Confirm the device has a valid push token and push permission is granted in device settings.
 
- In the dashboard, confirm the test user matches the campaign or Canvas segment and is not in the control group.
 
- Send a test push to the test device.
 
- Enable verbose logging, reproduce the issue, and review platform-specific guidance in your SDK tab.
 
- If the issue persists, contact Braze Support with verbose logs, platform, SDK version, and campaign or Canvas ID.

## Platform-specific troubleshooting

Select your SDK tab for platform-specific setup and display checks.

- web
 
- android
 
- swift
 
- fireos
 
- flutter
 
- .net maui (xamarin)

## Troubleshooting

If you’re experiencing issues after setting up push notifications, consider the following:

- Web push notifications require that your site be HTTPS.
 
- Not all browsers can receive push messages. Ensure that braze.isPushSupported() returns true in the browser.
 
- Some browsers, such as Firefox, do not display images in push notifications. For details on browser support, refer to the MDN documentation for Notification images.
 
- If a user has denied a site push access, they won’t be prompted for permission again unless they remove the denied status from their browser preferences.

## Understanding the Braze push workflow

The Firebase Cloud Messaging (FCM) service is Google’s infrastructure for push notifications sent to Android applications. Here is the simplified structure of how push notifications are enabled for your users’ devices and how Braze can send push notifications to them:

```
---
config:
 theme: mc
---
sequenceDiagram
 participant Device as User Device
 participant App as Android App
 participant BrazeSDK as Braze SDK
 participant BrazeAPI as Braze Server
 participant Firebase as Google Firebase
 Note over Device, Firebase: Register Option 1<br/>Register Automatically using `com_braze_firebase_cloud_messaging_registration_enabled` in braze.xml
 App ->> Braze: App initializes Braze with the first Braze call<br>This could be automatic session handling
 BrazeSDK ->> App: Get push token from Firebase Manager
 BrazeSDK ->> BrazeAPI: Send push token to Braze Server
 Note right of BrazeAPI: Braze will remove push token from any<br>other user who may have previously<br> been logged in on the same device.
 Note over Device, Firebase: Register Option 2<br/>Manual registration.
 App ->> BrazeSDK: App sets `Braze.registeredPushToken`
 BrazeSDK ->> BrazeAPI: Send push token to Braze Server
 Note right of BrazeAPI: Braze will remove push token from any<br>other user who may have previously<br> been logged in on the same device. 
 Note over Device, Firebase: Push permission
 BrazeAPI ->> BrazeSDK: In-App Message containing push prompt
 BrazeSDK -> App: In-App Message is displayed
 App -> BrazeSDK: User requests permissions
 BrazeSDK -> App: Displays the Push Authorization prompt
 BrazeSDK -> BrazeAPI: If authorized and `com_braze_optin_when_push_authorized`, Opt-In value is sent.
 Note over Device, Firebase: Push Notification Is Sent
 BrazeAPI ->> Firebase: Sends push message 
 Firebase ->> Device: Push message sent
 Device ->> App: Android will send the push to the App.<br>This could be blocked to Do Not Disturb, Power Saving Mode, etc.
 App ->> BrazeSDK: Message is sent to BrazeFirebaseMessagingService
 BrazeSDK ->> Device: SDK will check if the push is from Braze.<br>If so, push data is transformed into a Push Notification and displayed.

```

### Step 1: Configure your Google Cloud API key

In developing your app, you’ll need to provide the Braze Android SDK with your Firebase sender ID. Additionally, you’ll need to provide an API Key for server applications to the Braze dashboard. Braze will use this API key to send messages to your devices. You will also need to check that FCM service is enabled in Google Developer’s console.

note

A common mistake during this step is using the app identifier API key instead of the REST API key.

### Step 2: Devices register for FCM and provide Braze with push tokens

In typical integrations, the Braze Android SDK will handle registering devices for FCM capability. This will usually happen immediately upon opening the app for the first time. After registration, Braze will be provided with an FCM Registration ID, which is used to send messages to that device specifically. We will store the Registration ID for that user, and that user will become “push registered” if they previously did not have a push token for any of your apps.

### Step 3: Launch a Braze push campaign

When a push campaign is launched, Braze makes requests to FCM to deliver your message. Braze uses the API key copied in the dashboard to authenticate and verify that we can send push notifications to the push tokens provided.

### Step 4: Remove invalid tokens

If FCM informs us that any of the push tokens we were attempting to send a message to are invalid, we remove those tokens from the user profiles they were associated with. If users have no other push tokens, they will no longer show up as “Push Registered” under the Segments page.

For more details about FCM, visit Cloud messaging.

## Use the push error logs

Braze provides push notification errors within the message activity log. This error log provides a variety of warnings which can be very helpful for identifying why your campaigns aren’t working as expected. Selecting an error message redirects you to relevant documentation to help you troubleshoot a particular incident.

## Troubleshooting

### Push isn’t sending

Your push messages might not be sending because of the following situations:

- Your credentials exist in the wrong Google Cloud Platform project ID (wrong sender ID).
 
- Your credentials have the wrong permission scope.
 
- You uploaded wrong credentials to the wrong Braze workspace (wrong sender ID).

For other issues that may prevent you from sending a push message, refer to User Guide: Troubleshooting Push Notifications.

### No “push registered” users showing in the Braze dashboard (prior to sending messages)

Confirm that your app is correctly configured to allow push notifications. Common failure points to check include:

#### Incorrect sender ID

Check that the correct FCM sender ID is included in the braze.xml file. An incorrect sender ID will lead to MismatchSenderID errors reported in the dashboard’s message activity log.

#### Braze registration not occurring

Since FCM registration is handled outside of Braze, failure to register can only occur in two places:

- During registration with FCM
 
- When passing the FCM-generated push token to Braze

We recommend setting a breakpoint or logging to confirm that the FCM-generated push token is being sent to Braze. If a token is not generated correctly or at all, we recommend consulting the FCM documentation.

#### Google Play Services not present

For FCM push to work, Google Play Services must be present on the device. If Google Play Services isn’t on a device, push registration will not occur.

note

Google Play Services is not installed on Android emulators without Google APIs installed.

#### Device not connected to the internet

Check that your device has good internet connectivity and isn’t sending network traffic through a proxy.

### Tapping push notification doesn’t open the app

Check if com_braze_handle_push_deep_links_automatically is set to true or false. To enable Braze to automatically open the app and any deep links when a push notification is tapped, set com_braze_handle_push_deep_links_automatically to true in your braze.xml file.

If com_braze_handle_push_deep_links_automatically is set to its default of false, you need to use a Braze Push Callback to listen for and handle the push received and opened intents.

### Push notifications bounced

If a push notification isn’t delivered, make sure it didn’t bounce by looking in the developer console. The following are descriptions of common errors that may be logged in the developer console:

#### Error: MismatchSenderID

MismatchSenderID indicates an authentication failure. Confirm your Firebase sender ID and FCM API key are correct.

#### Error: InvalidRegistration

InvalidRegistration can be caused by a malformed push token.

- Make sure to pass a valid push token to Braze from Firebase Cloud Messaging.

#### Error: NotRegistered

- NotRegistered may also occur when multiple registrations occur and a second registration invalidates the first token.

### Push notifications sent but not displayed on users’ devices

There are a few reasons why this could be occurring:

#### Application was force quit

If you force-quit your application through your system settings, your push notifications will not be sent. Launching the app again will re-enable your device to receive push notifications.

#### BrazeFirebaseMessagingService not registered

The BrazeFirebaseMessagingService must be properly registered in AndroidManifest.xml for push notifications to appear:

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
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
 android:exported="false">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT" />
 </intent-filter>
</service>

```
 | 

#### Firewall is blocking push

If you are testing push over Wi-Fi, your firewall may be blocking ports necessary for FCM to receive messages. Confirm that ports 5228, 5229, and 5230 are open. Additionally, since FCM doesn’t specify its IPs, you must also allow your firewall to accept outgoing connections to all IP addresses contained in the IP blocks listed in Google’s ASN of 15169.

#### Custom notification factory returning null

If you have implemented a custom notification factory, ensure that it is not returning null. This will cause notifications not to be displayed.

### “Push registered” users no longer enabled after sending messages

There are a few reasons why this could be happening:

#### Application was uninstalled

Users have uninstalled the application. This will invalidate their FCM push token.

#### Invalid Firebase Cloud Messaging server key

The Firebase Cloud Messaging server key provided in the Braze dashboard is invalid. The sender ID provided should match the one referenced in your app’s braze.xml file. The server key and sender ID are found here in your Firebase Console:

### Push clicks not logged

If push clicks are not being logged, it is possible that push click data has not been flushed to our servers yet. The Braze Android SDK may throttle flushes.

If you implemented a custom push handler, ensure that you are appropriately preserving native push analytics

Logging push clicks is a network operation and is bound by networking limitations. As such, while the Braze Android SDK attempts to accommodate for network failures and will retry failed requests, some event loss is to be expected.

### Deep links not working

#### Verify deep link configuration

Deep links can be tested with ADB. We recommend testing your deep link with the following command:

adb shell am start -W -a android.intent.action.VIEW -d "THE_DEEP_LINK" THE_PACKAGE_NAME

If the deep link fails to work, the deep link may be misconfigured. A misconfigured deep link will not work when sent through Braze push.

#### Verify custom handling logic

If the deep link works correctly with ADB but fails to work from Braze push, check whether any custom push open handling has been implemented. If so, verify that the custom handling code properly handles the incoming deep link.

#### Disable back stack behavior

If the deep link works correctly with ADB but fails to work from Braze push, try disabling back stack. To do so, update your braze.xml file to include:

```

1

```
 | 
```
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">false</bool>

```
 | 

## Understanding the Braze/APNs workflow

The Apple Push Notification service (APNs) is the infrastructure for sending push notifications to applications running on Apple’s platforms. Here is the simplified structure of how push notifications are enabled for your users’ devices and how Braze can send push notifications to them:

- You configure the push certificate and provisioning profile
 
- Devices register for APNs and provide Braze with push tokens
 
- You launch a Braze push campaign
 
- Braze removes invalid tokens

### Step 1: Configuring the push certificate and provisioning profile

To develop your app, create an SSL certificate to enable push notifications. This certificate is included in the provisioning profile your app is built with and must also be uploaded to the Braze dashboard. The certificate allows Braze to tell APNs that it is authorized to send push notifications on your behalf.

There are two types of provisioning profiles and certificates: development and distribution. We recommend using only distribution profiles and certificates to avoid any confusion. If you choose to use different profiles and certificates for development and distribution, ensure that the certificate uploaded to the dashboard matches the provisioning profile you are currently using.

warning

Do not change the push certificate environment (development versus production). Changing the push certificate to the wrong environment can lead to your users having their push token accidentally removed, making them unreachable by push.

### Step 2: Devices register for APNs and provide Braze with push tokens

When users open your app, they are prompted to accept push notifications. If they accept this prompt, APNs generates a push token for that particular device. The Swift SDK immediately and asynchronously sends the push token for apps using the default automatic flush policy. After we have a push token associated with a user, they show as “Push Registered” in the dashboard on their user profile under the Engagement tab and are eligible to receive push notifications from Braze campaigns.

note

Starting in macOS 13, on certain devices, you can test push notifications on an iOS 16 Simulator running on Xcode 14. For further details, refer to the Xcode 14 Release Notes.

#### Considerations for push token generation

- If users install your app on another device, Braze creates and captures another token the same way.
 
- If users reinstall your app, the SDK generates a new token and passes it to Braze. However, APNs and Braze may still log the original token as valid.
 
- If users uninstall your app, Braze does not immediately receive a notification, and the token still appears as valid until APNs retires it.
 
- At some point, APNs retires old tokens. Braze does not control or have visibility into this.

### Step 3: Launching a Braze push campaign

When a push campaign is launched, Braze makes requests to APNs to deliver your message. Specifically, the requests are passed to APNs for each current valid push token unless Send to a user’s most recent device is selected. After Braze receives a successful response from APNs, Braze logs a successful delivery on the user profile, though the user may not have received the actual message for reasons including:

- Their device is powered off.
 
- Their device isn’t connected to the internet (Wi-Fi or cellular).
 
- They recently uninstalled the app.

Braze uses the SSL push certificate uploaded in the dashboard to authenticate and verify that it is authorized to send push notifications to the push tokens provided. If a device is online, the notification should be received shortly after the campaign has been sent. Note that Braze sets the default APNs expiration date for notifications to 30 days.

### Step 4: Removing invalid tokens

If APNs informs us that any of the push tokens we were attempting to send a message to are invalid, we remove those tokens from the user profiles they were associated with.

note

It’s normal for APNs to initially return a success status even if a token becomes unregistered, as APNs doesn’t immediately report token invalidation events. APNs intentionally delays returning a 410 status for invalid tokens on a randomized schedule, designed to protect user privacy and prevent tracking of app uninstalls. You can safely continue sending notifications to an unregistered token until APNs returns a 410 status.

## Using the push error logs

The Message Activity Log lets you see any messages (especially error messages) associated with your campaigns and sends, including push notification errors. This error log provides a variety of warnings which can be very helpful for identifying why your campaigns aren’t working as expected. Selecting an error message redirects you to relevant documentation to help you troubleshoot a particular incident.

Common errors you might see here include user-specific notifications, such as “Received Unregistered Sending to Push Token”.

In addition, Braze also provides a push changelog on the user profile under the Engagement tab. This changelog provides insight into push registration behavior such as token invalidation, push registration errors, tokens being moved to new users, etc.

### Message Activity Log errors

#### Received unregistered sending to push token

- Make sure that the push token being sent to Braze from the method AppDelegate.braze?.notifications.register(deviceToken:) is valid. You can look in the Message Activity Log to see the push token. It should look something like 6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6, a long string containing a mix of letters and numbers. If your push token looks different, check your code for sending Braze the push tokens.
 
- Ensure that your push provisioning profile matches the environment you’re testing. Universal certificates may be configured in the Braze dashboard to send to either the development or production APNs environment. Using a development certificate for a production app or a production certificate for a development app does not work.
 
- Check that the push token you have uploaded to Braze matches the provisioning profile you used to build the app you sent the push token from.

#### Device token not for topic

APNs returns DeviceTokenNotForTopic (HTTP status 400) when the push token doesn’t match the topic (bundle ID) configured for your credentials. Braze may surface this in Message Activity Log or push delivery logs as DeviceTokenNotForTopic.

To resolve the mismatch:

- Confirm the app’s bundle ID matches the App Bundle ID in Braze (Settings > App Settings > Push Notification Settings).
 
- Verify the provisioning profile used to build the app includes push capability for that bundle ID.
 
- Confirm the push credential uploaded to Braze matches the app’s environment (development versus production).
 
- For .p8 keys, verify Team ID and Key ID in Braze match your Apple Developer account.
 
- Re-upload a valid .p8 key or .p12 certificate if credentials were rotated or revoked.

Prefer .p8 authentication keys when possible. For credential types and dashboard status indicators, see Migrate to a .p8 authentication key.

#### BadDeviceToken sending to push token

The BadDeviceToken is an APNs error code and does not originate from Braze. There could be a number of reasons for this response being returned, including the following:

- The app received a push token that was invalid for the credentials uploaded to the dashboard.
 
- Push was disabled for this workspace.
 
- The user has opted out of push.
 
- The app was uninstalled.
 
- Apple refreshed the push token, which invalidated the old token.
 
- The app was built for a production environment, but the push credentials uploaded to Braze are set for a development environment (or the other way around).

## Push registration issues

### No push registration prompt

If the application does not prompt you to register for push notifications, there is likely an issue with your push registration integration. Ensure you have followed our documentation and correctly integrated our push registration. You can also set breakpoints in your code to ensure the push registration code is running.

### No “push registered” users showing in the dashboard (prior to sending messages)

Ensure that your app is correctly configured to allow push notifications. Common failure points to check include:

- Check that your app is prompting you to allow push notifications. Typically, this prompt will appear upon your first open of the app, but it can be programmed to appear elsewhere. If it does not appear where it should be, the problem is likely with the basic configuration of your app’s push capabilities.

- Verify the steps for push integration were successfully completed.
 
- Check that the provisioning profile your app was built with includes permissions for push. Make sure that you’re pulling down all of the available provisioning profiles from your Apple developer account. To confirm this, perform the following steps:

- In Xcode, navigate to Preferences > Accounts (or use the keyboard shortcut Command+,).
 
- Select the Apple ID you use for your developer account and click View Details.
 
- On the next page, click Refresh and confirm that you’re pulling all available provisioning profiles.

- Check you have properly enabled push capability in your app.
 
- Check your push provisioning profile matches the environment you’re testing in. Universal certificates may be configured in the Braze dashboard to send to either the development or production APNs environment. Using a development certificate for a production app or a production certificate for a development app does not work.
 
- Check that you are calling our registerPushToken method by setting a breakpoint in your code.
 
- Make sure you’re testing using a device (push will not work on a simulator) and have good network connectivity.

## Push notifications sent but not displayed on users’ devices

### “Push registered” users no longer enabled after sending messages

This likely indicates that the user had an invalid push token. This can happen for several reasons:

#### Dashboard and app certificate mismatch

If the push certificate you uploaded in the dashboard is not the same one in the provisioning profile that your app was built with, APNs will reject the token. Verify that you have uploaded the correct certificate and completed another session in the app before attempting another test notification.

#### Application was uninstalled

If a user has uninstalled your application, their push token will be invalid and removed upon the next send.

#### Regenerating your provisioning profile

As a last resort, starting over fresh and creating a whole new provisioning profile can clear up configuration errors that come from working with multiple environments, profiles, and apps at the same time. There are many “moving parts” in setting up push notifications, so sometimes, it is best to retry from the beginning. This will also help isolate the problem if you need to continue troubleshooting.

### Messages not delivered to “push registered” users

#### App is foregrounded

On iOS versions that do not integrate push via the UserNotifications framework, if the app is in the foreground when the push message is received, it will not be displayed. You should background the app on your test devices before sending test messages.

#### Test notification scheduled incorrectly

Check the schedule you set for your test message. If it is set to local time zone delivery or Intelligent Timing, you may have just not received the message yet (or had the app in the foreground when it was received).

### User not “push registered” for the app being tested

Check the user profile of the user you are trying to send a test message to. Under the Engagement tab, there should be a list of “pushable apps.” Verify the app you are trying to send test messages to is in this list. Users will show up as “Push Registered” if they have a push token for any app in your workspace, so this could be something of a false positive.

The following would indicate a problem with push registration or that the user’s token had been returned to Braze as invalid by APNs after being pushed:

## Push clicks not logged

- Make sure you have followed the push integration steps.
 
- Braze does not handle push notifications received silently in the foreground (default foreground push behavior prior to the UserNotifications framework). This means that links will not be opened, and push clicks will not be logged. If your application has not yet integrated the UserNotifications framework, Braze will not handle push notifications when the application state is UIApplicationStateActive. Ensure that your app does not delay calls to push handling methods; otherwise, the Swift SDK may treat push notifications as silent foreground push events and not handle them.

## Deep links not working

For comprehensive troubleshooting across all channels—including universal links, custom schemes, email, and third-party providers like Branch—see Deep linking troubleshooting.

### Web links from push clicks not opening

Links in push notifications need to be ATS compliant to be opened in web views. Ensure that your web links use HTTPS. For more information, refer to ATS compliance.

### Deep links from push clicks not opening

Most of the code that handles deep links also handles push opens. First, ensure that push opens are being logged. If not, fix that issue (as the fix often fixes link handling).

If opens are being logged, check whether it is an issue with the deep link in general or with the deep linking push click handling. To do this, test to see if a deep link from an in-app message click works.

### Push Story image taps do nothing

If tapping a Push Story image does nothing, open the Notification Content Extension Info.plist and confirm UNNotificationExtensionUserInteractionEnabled is YES. The Swift SDK BrazePushStory module needs that key so the extension can receive taps. See Push stories.

## Understanding the Braze push workflow

The Firebase Cloud Messaging (FCM) service is Google’s infrastructure for push notifications sent to Android applications. Here is the simplified structure of how push notifications are enabled for your users’ devices and how Braze can send push notifications to them:

```
---
config:
 theme: mc
---
sequenceDiagram
 participant Device as User Device
 participant App as Android App
 participant BrazeSDK as Braze SDK
 participant BrazeAPI as Braze Server
 participant Firebase as Google Firebase
 Note over Device, Firebase: Register Option 1<br/>Register Automatically using `com_braze_firebase_cloud_messaging_registration_enabled` in braze.xml
 App ->> Braze: App initializes Braze with the first Braze call<br>This could be automatic session handling
 BrazeSDK ->> App: Get push token from Firebase Manager
 BrazeSDK ->> BrazeAPI: Send push token to Braze Server
 Note right of BrazeAPI: Braze will remove push token from any<br>other user who may have previously<br> been logged in on the same device.
 Note over Device, Firebase: Register Option 2<br/>Manual registration.
 App ->> BrazeSDK: App sets `Braze.registeredPushToken`
 BrazeSDK ->> BrazeAPI: Send push token to Braze Server
 Note right of BrazeAPI: Braze will remove push token from any<br>other user who may have previously<br> been logged in on the same device. 
 Note over Device, Firebase: Push permission
 BrazeAPI ->> BrazeSDK: In-App Message containing push prompt
 BrazeSDK -> App: In-App Message is displayed
 App -> BrazeSDK: User requests permissions
 BrazeSDK -> App: Displays the Push Authorization prompt
 BrazeSDK -> BrazeAPI: If authorized and `com_braze_optin_when_push_authorized`, Opt-In value is sent.
 Note over Device, Firebase: Push Notification Is Sent
 BrazeAPI ->> Firebase: Sends push message 
 Firebase ->> Device: Push message sent
 Device ->> App: Android will send the push to the App.<br>This could be blocked to Do Not Disturb, Power Saving Mode, etc.
 App ->> BrazeSDK: Message is sent to BrazeFirebaseMessagingService
 BrazeSDK ->> Device: SDK will check if the push is from Braze.<br>If so, push data is transformed into a Push Notification and displayed.

```

### Step 1: Configure your Google Cloud API key

In developing your app, you’ll need to provide the Braze Android SDK with your Firebase sender ID. Additionally, you’ll need to provide an API Key for server applications to the Braze dashboard. Braze will use this API key to send messages to your devices. You will also need to check that FCM service is enabled in Google Developer’s console.

note

A common mistake during this step is using the app identifier API key instead of the REST API key.

### Step 2: Devices register for FCM and provide Braze with push tokens

In typical integrations, the Braze Android SDK will handle registering devices for FCM capability. This will usually happen immediately upon opening the app for the first time. After registration, Braze will be provided with an FCM Registration ID, which is used to send messages to that device specifically. We will store the Registration ID for that user, and that user will become “push registered” if they previously did not have a push token for any of your apps.

### Step 3: Launch a Braze push campaign

When a push campaign is launched, Braze makes requests to FCM to deliver your message. Braze uses the API key copied in the dashboard to authenticate and verify that we can send push notifications to the push tokens provided.

### Step 4: Remove invalid tokens

If FCM informs us that any of the push tokens we were attempting to send a message to are invalid, we remove those tokens from the user profiles they were associated with. If users have no other push tokens, they will no longer show up as “Push Registered” under the Segments page.

For more details about FCM, visit Cloud messaging.

## Use the push error logs

Braze provides push notification errors within the message activity log. This error log provides a variety of warnings which can be very helpful for identifying why your campaigns aren’t working as expected. Selecting an error message redirects you to relevant documentation to help you troubleshoot a particular incident.

## Troubleshooting

### Push isn’t sending

Your push messages might not be sending because of the following situations:

- Your credentials exist in the wrong Google Cloud Platform project ID (wrong sender ID).
 
- Your credentials have the wrong permission scope.
 
- You uploaded wrong credentials to the wrong Braze workspace (wrong sender ID).

For other issues that may prevent you from sending a push message, refer to User Guide: Troubleshooting Push Notifications.

### No “push registered” users showing in the Braze dashboard (prior to sending messages)

Confirm that your app is correctly configured to allow push notifications. Common failure points to check include:

#### Incorrect sender ID

Check that the correct FCM sender ID is included in the braze.xml file. An incorrect sender ID will lead to MismatchSenderID errors reported in the dashboard’s message activity log.

#### Braze registration not occurring

Since FCM registration is handled outside of Braze, failure to register can only occur in two places:

- During registration with FCM
 
- When passing the FCM-generated push token to Braze

We recommend setting a breakpoint or logging to confirm that the FCM-generated push token is being sent to Braze. If a token is not generated correctly or at all, we recommend consulting the FCM documentation.

#### Google Play Services not present

For FCM push to work, Google Play Services must be present on the device. If Google Play Services isn’t on a device, push registration will not occur.

note

Google Play Services is not installed on Android emulators without Google APIs installed.

#### Device not connected to the internet

Check that your device has good internet connectivity and isn’t sending network traffic through a proxy.

### Tapping push notification doesn’t open the app

Check if com_braze_handle_push_deep_links_automatically is set to true or false. To enable Braze to automatically open the app and any deep links when a push notification is tapped, set com_braze_handle_push_deep_links_automatically to true in your braze.xml file.

If com_braze_handle_push_deep_links_automatically is set to its default of false, you need to use a Braze Push Callback to listen for and handle the push received and opened intents.

### Push notifications bounced

If a push notification isn’t delivered, make sure it didn’t bounce by looking in the developer console. The following are descriptions of common errors that may be logged in the developer console:

#### Error: MismatchSenderID

MismatchSenderID indicates an authentication failure. Confirm your Firebase sender ID and FCM API key are correct.

#### Error: InvalidRegistration

InvalidRegistration can be caused by a malformed push token.

- Make sure to pass a valid push token to Braze from Firebase Cloud Messaging.

#### Error: NotRegistered

- NotRegistered may also occur when multiple registrations occur and a second registration invalidates the first token.

### Push notifications sent but not displayed on users’ devices

There are a few reasons why this could be occurring:

#### Application was force quit

If you force-quit your application through your system settings, your push notifications will not be sent. Launching the app again will re-enable your device to receive push notifications.

#### BrazeFirebaseMessagingService not registered

The BrazeFirebaseMessagingService must be properly registered in AndroidManifest.xml for push notifications to appear:

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
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
 android:exported="false">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT" />
 </intent-filter>
</service>

```
 | 

#### Firewall is blocking push

If you are testing push over Wi-Fi, your firewall may be blocking ports necessary for FCM to receive messages. Confirm that ports 5228, 5229, and 5230 are open. Additionally, since FCM doesn’t specify its IPs, you must also allow your firewall to accept outgoing connections to all IP addresses contained in the IP blocks listed in Google’s ASN of 15169.

#### Custom notification factory returning null

If you have implemented a custom notification factory, ensure that it is not returning null. This will cause notifications not to be displayed.

### “Push registered” users no longer enabled after sending messages

There are a few reasons why this could be happening:

#### Application was uninstalled

Users have uninstalled the application. This will invalidate their FCM push token.

#### Invalid Firebase Cloud Messaging server key

The Firebase Cloud Messaging server key provided in the Braze dashboard is invalid. The sender ID provided should match the one referenced in your app’s braze.xml file. The server key and sender ID are found here in your Firebase Console:

### Push clicks not logged

If push clicks are not being logged, it is possible that push click data has not been flushed to our servers yet. The Braze Android SDK may throttle flushes.

If you implemented a custom push handler, ensure that you are appropriately preserving native push analytics

Logging push clicks is a network operation and is bound by networking limitations. As such, while the Braze Android SDK attempts to accommodate for network failures and will retry failed requests, some event loss is to be expected.

### Deep links not working

#### Verify deep link configuration

Deep links can be tested with ADB. We recommend testing your deep link with the following command:

adb shell am start -W -a android.intent.action.VIEW -d "THE_DEEP_LINK" THE_PACKAGE_NAME

If the deep link fails to work, the deep link may be misconfigured. A misconfigured deep link will not work when sent through Braze push.

#### Verify custom handling logic

If the deep link works correctly with ADB but fails to work from Braze push, check whether any custom push open handling has been implemented. If so, verify that the custom handling code properly handles the incoming deep link.

#### Disable back stack behavior

If the deep link works correctly with ADB but fails to work from Braze push, try disabling back stack. To do so, update your braze.xml file to include:

```

1

```
 | 
```
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">false</bool>

```
 | 

## Troubleshooting

### Tapping push notification doesn’t open the app

On Android, whether tapping a push notification automatically brings your app to the foreground and opens its deep link is controlled by the native com_braze_handle_push_deep_links_automatically flag, which defaults to false.

With the default of false:

- The native SDK still sends a BRAZE_PUSH_CLICKED broadcast and your Dart push_opened listener still fires as expected.
 
- The native SDK does not call startActivity(), so your app is not brought to the foreground and the deep link isn’t followed automatically.

If these two behaviors match what you’re seeing, the flag setting is likely the cause.
To confirm, check your device logs for a BrazePushReceiver entry handling com.braze.action.BRAZE_PUSH_CLICKED, followed by a push_opened event in your Flutter logs, with no corresponding app launch.

To fix this, set com_braze_handle_push_deep_links_automatically to true in your braze.xml:

```

1

```
 | 
```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>

```
 | 

For more information, see Add deep links (Android) in the Flutter push notifications guide.

### Other push delivery and registration issues

Since the Braze Flutter SDK for Android is built on top of the native Braze Android SDK, most other push delivery, registration, and logging issues (such as sender ID mismatches, missing Google Play Services, or BrazeFirebaseMessagingService not being registered) also apply to Flutter apps. For more information, see the native Android troubleshooting guide.

## Troubleshooting

### Push doesn’t appear after app is closed from task switcher

If you observe that push notifications no longer appear after the app is closed from the task switcher, your app is likely in Debug mode. .NET MAUI adds scaffolding in Debug mode that prevents apps from receiving push after their process is killed. If you run your app in Release Mode, you should see push even after the app is closed from the task switcher.

### Custom notification factory not being set correctly

Custom notification factories (and all delegates) must extend Java.Lang.Object to work properly across the C# and Java divide. See Xamarin on implementing Java interfaces for more information.

## Line breaks in push notifications

When composing push notifications with Liquid tags, line breaks adjacent to Liquid tags are automatically removed before the message is sent. In the push notification composer, these line breaks are re-added so your message remains readable while editing. If you notice line breaks around Liquid tags when saving your message, this is expected behavior.

- 

New Stuff!
