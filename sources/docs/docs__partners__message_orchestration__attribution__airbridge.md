---
url: https://www.braze.com/docs/partners/message_orchestration/attribution/airbridge
slug: docs__partners__message_orchestration__attribution__airbridge
title: "Airbridge"
description: "This reference article outlines the partnership between Braze and Airbridge, which offers people-based attribution and incrementally measurement to measure true marketing effectiveness across devices, identities,..."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Airbridge

Airbridge is a unified mobile measurement platform for discovering sources of growth through mobile attribution, incremental measurement, and marketing mix modeling.

This integration is maintained by Airbridge.

## About the integration

The Braze and Airbridge integration lets you pass all non-organic install attribution data from Airbridge to Braze to build personalized marketing campaigns.

## Prerequisites

 Requirement | 
 Description | 

 Airbridge account | 
 An Airbridge account is required to take advantage of this partnership. | 

 iOS or Android app | 
 This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. | 

 Airbridge SDK | 
 In addition to the required Braze SDK, you must install the Airbridge Android or iOS SDK. | 

## Integration

### Step 1: Map device ID

The server-to-server integration can be enabled by including the following code snippets in your apps.

#### Android

If you have an Android app, you will need to pass a unique Braze device ID to Airbridge.

- android

- java
 
- kotlin

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

```
 | 
```
// MainApplciation.java
@Override
public void onCreate() {
 super.onCreate();
 // Initialize Airbridge SDK
 AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
 // Make Airbridge SDK explicitly start tracking
 .setAutoStartTrackingEnabled(false)
 .build();
 Airbridge.init(this, config);
 
 // Set device alias into Airbridge SDK
 Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
 // Explicitly start tracking
 Airbridge.startTracking();
}

```
 | 

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

```
 | 
```
// MainApplication.kt
override fun onCreate() {
 super.onCreate()
 // Initialize Airbridge SDK
 val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
 // Make Airbridge SDK explicitly start tracking
 .setAutoStartTrackingEnabled(false)
 .build()
 Airbridge.init(this, config)

 // Set device alias into Airbridge SDK
 Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
 // Explicitly start tracking
 Airbridge.startTracking()
}

```
 | 

#### iOS

If you have an iOS app, you may opt to collect IDFV by setting the useUUIDAsDeviceId field to false. If not set, iOS attribution will likely not map accurately from Airbridge to Braze. For more information, refer to Collecting IDFV.

- ios

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
8
9
10
11

```
 | 
```
// AppDelegate.swift
func application(
 _ application: UIApplication,
 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
 AirBridge.setAutoStartTrackingEnabled(false)
 AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

 AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
 AirBridge.startTracking()
}

```
 | 

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
// AppDelegate.m
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
 AirBridge.autoStartTrackingEnabled = NO;
 [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

 [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
 [AirBridge startTracking];
}

```
 | 

#### React Native

- typescript

```

1
2
3
4

```
 | 
```
Braze.getInstallTrackingId(function (error, brazeID) {
 Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
 Airbirdge.state.startTracking()
})

```
 | 

#### Cordova

- typescript

```

1
2
3
4

```
 | 
```
AppboyPlugin.getDeviceId(function (brazeID) {
 Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
 Airbridge.state.startTracking()
})

```
 | 

#### Flutter

- typescript

```

1
2
3
4

```
 | 
```
BrazePlugin.getInstallTrackingId().then((brazeID) {
 Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
 Airbridge.state.startTracking()
})

```
 | 

#### Unity

- c#

```

1
2
3

```
 | 
```
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()

```
 | 

### Step 2: Get the Braze data import key

In Braze, navigate to Partner Integrations > Technology Partners and select Airbridge.

Here, you will find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Airbridge’s dashboard.

### Step 3: Configure Braze in Airbridge’s dashboard

- In Airbridge, navigate to Integrations > Third-party Integrations in the navigation sidebar and select Braze.
 
- Provide the data import key and REST endpoint that you found in the Braze dashboard.
 
- Select the event type (Install Event or Install & Deeplink Open Event) and save.

note

The attribution data for campaigns that led to deeplink open events are updated on the device-level. For example, if two users use a single device and one user performs a deeplink open event, the attribution data of this event is also reflected to the other user’s data.

For more detailed instructions, visit Airbridge.

### Step 4: Confirm the integration

After Braze receives attribution data from Airbridge, the status connection indicator on the Airbridge technology partners page in Braze changes from “Not Connected” to “Connected” and includes a timestamp of the last successful request.

This status changes only after Braze receives data about an attributed install. Braze ignores organic installs (excludes them from the Airbridge postback) and does not count them when determining if the connection is successful.

## Available data fields

Airbridge can send four types of attribution data to Braze listed in the following data field chart. This data can be viewed in the Airbridge dashboard and is used for user install attribution and filtering.

Assuming you configure your integration as suggested, Braze will map install data to segment filters.

 Airbridge data field | 
 Braze segment filter | 
 Description | 

 Channel | 
 Install Attribution Source | 
 The channel the installs or deeplink opens are attributed to | 

 Campaign | 
 Install Attribution Campaign | 
 The campaign the installs or deeplink opens are attributed to | 

 Ad Group | 
 Install Attribution Adgroup | 
 The ad group the installs or deeplink opens are attributed to | 

 Ad Creative | 
 Install Attribution Ad | 
 The ad creative the installs or deeplink opens are attributed to | 

Your user base can be segmented by attribution data in the Braze dashboard using the Install Attribution filters.

## Meta Business attribution data

Attribution data for Meta Business campaigns is not available through our partners. This media source does not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Airbridge click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns shows which campaigns drive app installs and re-engagement. Use the results to measure marketing performance and decide where to invest resources for stronger ROI.

To get started with Airbridge click tracking links, visit Airbridge. After set up is completed, you can directly insert the Airbridge click tracking links into your Braze campaigns. Airbridge will then use its probabilistic attribution methodologies to attribute the user that has clicked on the link. We recommend appending your Airbridge tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

- android
 
- ios

For Android, Braze allows customers to opt-in to Google Advertising ID collection (GAID). The GAID is also collected natively through the Airbridge SDK integration. You can include the GAID in your Airbridge click tracking links by utilizing the following Liquid logic:

```

1
2
3

```
 | 
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}

```
 | 

For iOS, both Braze and Airbridge automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Airbridge click tracking links by utilizing the following Liquid logic:

```

1
2
3

```
 | 
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}

```
 | 

note

This recommendation is purely optional

If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Airbridge will still be able to attribute these clicks through their probabilistic modeling.

- 

New Stuff!
