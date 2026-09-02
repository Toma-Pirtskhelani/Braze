---
url: https://www.braze.com/docs/developer_guide/storage
slug: docs__developer_guide__storage
title: "Storage"
description: "Learn about the different device-level properties that are stored by the Braze SDK."
section: developer_guide/storage
fetched: 2026-09-02
evidence: company-own (technical)
---
# Storage

Learn about the different device-level properties that are stored by the Braze SDK.

## Device properties

By default, Braze collects the following device-level properties to allow device, language, and time zone-based message personalization:

- web
 
- android
 
- swift

- BROWSER
 
- BROWSER_VERSION
 
- LANGUAGE
 
- OS
 
- RESOLUTION
 
- TIME_ZONE
 
- USER_AGENT

- AD_TRACKING_ENABLED
 
- ANDROID_VERSION
 
- CARRIER
 
- IS_BACKGROUND_RESTRICTED
 
- LOCALE
 
- MODEL
 
- NOTIFICATION_ENABLED
 
- RESOLUTION
 
- TIMEZONE

note

AD_TRACKING_ENABLED and TIMEZONE aren’t collected if they are null or blank. GOOGLE_ADVERTISING_ID is not collected automatically by the SDK and must be passed in via setGoogleAdvertisingId.

- Device Carrier (see note on the CTCarrier deprecation)
 
- Device Locale
 
- Device Model
 
- Device OS Version
 
- Push Authorization Status
 
- Push Display Options
 
- Push Enabled
 
- Device Resolution
 
- Device Time Zone

note

The Braze SDK does not collect IDFA automatically. Apps may optionally pass IDFA to Braze by implementing the methods in the following sections. Apps must obtain explicit opt-in to tracking by the end user through the App Tracking Transparency framework before passing IDFA to Braze.

- To set the advertising tracking state, use set(adTrackingEnabled:).
 
- To set the identifier for advertiser (IDFA), use set(identifierForAdvertiser:).

By default, all properties are enabled. However, you can enable or disable them manually. Keep in mind, some Braze SDK features require specific properties (such as local time zone delivery and time zone), so be sure to test your configuration before releasing to production.

- web
 
- android
 
- swift

For example, you can specify the device language to be allowlisted. For more information, see the devicePropertyAllowlist option for InitializationOptions.

```

1
2
3
4
5

```
 | 
```
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
 baseUrl: "BASE-URL",
 devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});

```
 | 

For example, you can specify the Android OS version and device locale to be allowlisted. For more information, see the setDeviceObjectAllowlistEnabled() and setDeviceObjectAllowlist() methods.

```

1
2
3

```
 | 
```
new BrazeConfig.Builder()
 .setDeviceObjectAllowlistEnabled(true)
 .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));

```
 | 

For example, you can specify the time zone and locale collection to be allowlisted. For more information, see the devicePropertyAllowList property of the configuration object.

- swift
 
- objective-c

```

1

```
 | 
```
configuration.devicePropertyAllowList = [.timeZone, .locale]

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
configuration.devicePropertyAllowList = @[
 BRZDeviceProperty.timeZone,
 BRZDeviceProperty.locale
];

```
 | 

tip

To learn more about automatically-collected device properties, see SDK Data Collection.

## Store cookies (web only)

After you initialize the Web Braze SDK, the SDK creates and stores first-party cookies (set on your own domain) with a 400-day expiration that automatically renews on new sessions.

Cookies only store user, session, and device identifiers. Other data—such as in-app messages waiting to trigger, content cards, and queued events or attributes not yet synced to Braze—is stored in localStorage.

The following cookies are stored:

 Cookie | 
 Description | 
 Size | 

 ab.storage.userId.[your-api-key] | 
 Used to determine whether the currently logged-in user has changed and to associate events with the current user. | 
 Based on the size of the value passed to changeUser | 

 ab.storage.sessionId.[your-api-key] | 
 Randomly-generated string used to determine whether the user is starting a new or existing session to sync messages and calculate session analytics. | 
 ~200 bytes | 

 ab.storage.deviceId.[your-api-key] | 
 Randomly-generated string used to identify anonymous users, and to differentiate users’ devices and to enable device-based messaging. | 
 ~200 bytes | 

 ab.optOut | 
 Used to store a user’s opt-out preference when disableSDK is called | 
 ~40 bytes | 

 ab._gd | 
 Temporarily created (and then deleted) to determine the root-level cookie domain, which allows the SDK to work properly across sub-domains. | 
 n/a | 

### Change cookie expiry

By default, Braze cookies expire after 400 days. To override this, use the cookieExpiryInDays option when initializing the Web SDK. Values must be greater than 0; if the option is omitted or set to 0 or less, the 400-day default applies. This option requires Web SDK 6.6.0 or later.

```

1
2
3
4
5

```
 | 
```
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
 baseUrl: "BASE-URL",
 cookieExpiryInDays: 30 // expires after 30 days
});

```
 | 

### Disable cookies

To disable all cookies, use the noCookies option when initializing the Web SDK. When cookies are disabled, the SDK uses localStorage instead to identify users and sessions. This prevents you from associating anonymous users who navigate across sub-domains and results in a new user on each subdomain.

```

1
2
3
4
5

```
 | 
```
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
 baseUrl: "BASE-URL",
 noCookies: true
});

```
 | 

To stop Braze tracking in general, or to clear all stored browser data, see the disableSDK and wipeData SDK methods, respectively. These two methods can be useful if a user revokes consent or if you want to stop all Braze functionality after the SDK is initialized.

- 

New Stuff!
