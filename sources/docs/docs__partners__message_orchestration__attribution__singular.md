---
url: https://www.braze.com/docs/partners/message_orchestration/attribution/singular
slug: docs__partners__message_orchestration__attribution__singular
title: "Singular"
description: "This reference article outlines the partnership between Braze and Singular, a unified marketing analytics platform that allows you to import paid install attribution data."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Singular

Singular is a unified marketing analytics platform that delivers attribution, cost aggregation, marketing analytics, creative reporting, and workflow automation.

This integration is maintained by Singular.

## About the integration

The Braze and Singular integration allows you to import paid install attribution data to segment intelligently within your lifecycle campaigns.

## Prerequisites

 Requirement | 
 Description | 

 Singular account | 
 A Singular account is required to take advantage of this partnership. | 

 iOS or Android app | 
 This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. | 

 Singular SDK | 
 In addition to the required Braze SDK, you must install the Singular SDK. | 

## Integration

### Step 1: Map user IDs

#### Android

If you have an Android app, you will need to include the following code snippet, which passes a unique Braze user ID to Singular.

```

1
2
3

```
 | 
```
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
 .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);

```
 | 

#### iOS

important

Prior to February 2023, our Singular attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze device_id and send it to Singular upon install because there is no disruption of service.

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the useUUIDAsDeviceId field is set to false so there is no disruption of the integration.

If set to true, you must implement the iOS device ID mapping for Swift in order to pass the Braze device_id to Singular upon app install in order for Braze to appropriately match iOS attributions.

- objective-c
 
- swift

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
SingularConfig* config = [[SingularConfig
 alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

 [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
 overrideExisting:YES];
 [Singular start:config];

```
 | 

```

1

```
 | 
```
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)

```
 | 

### Step 2: Get the Braze data import key

In Braze, navigate to Partner Integrations > Technology Partners and select Singular.

Here, you will find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one.

You will need to provide the data import key and REST endpoint to your Singular account manager to complete the integration.

### Step 3: Confirm the integration

After Braze receives attribution data from Singular, the status connection indicator on the Singular technology partners page in Braze changes from “Not Connected” to “Connected” and includes a timestamp of the last successful request.

This status changes only after Braze receives data about an attributed install. Braze ignores organic installs (excludes them from the Singular postback) and does not count them when determining if the connection is successful.

## Facebook and X (formerly Twitter) attribution data

Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Singular click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you’ll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Singular click tracking links, visit their documentation. You can insert the Singular click tracking links into your Braze campaigns directly. Singular will then use their probabilistic attribution methodologies to attribute the user that has clicked on the link. We recommend appending your Singular tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

- android
 
- ios

For Android, Braze allows customers to opt-in to Google Advertising ID collection (GAID). The GAID is also collected natively through the Singular SDK integration. You can include the GAID in your Singular click tracking links by utilizing the following Liquid logic:

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

For iOS, both Braze and Singular automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Singular click tracking links by utilizing the following Liquid logic:

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

If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Singular will still be able to attribute these clicks through their probabilistic modeling.

- 

New Stuff!
