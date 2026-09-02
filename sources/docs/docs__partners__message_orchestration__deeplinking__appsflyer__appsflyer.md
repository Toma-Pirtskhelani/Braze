---
url: https://www.braze.com/docs/partners/message_orchestration/deeplinking/appsflyer/appsflyer
slug: docs__partners__message_orchestration__deeplinking__appsflyer__appsflyer
title: "AppsFlyer"
description: "This reference article outlines the partnership between Braze and AppsFlyer, a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps...."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# AppsFlyer

AppsFlyer is a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps through marketing analytics, mobile attribution, and deep linking.

The Braze and AppsFlyer integration allows you to better understand how to optimize and build more holistic campaigns by leveraging mobile install attribution data from AppsFlyer.

You can also pass your AppsFlyer audiences (cohorts) directly to Braze with the AppsFlyer Audiences integration, allowing you to create powerful customer engagement campaigns targeted toward just the right users at just the right time.

## Prerequisites

 Requirement | 
 Description | 

 AppsFlyer account | 
 An AppsFlyer account is required to take advantage of this partnership. | 

 iOS or Android app | 
 This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. | 

 AppsFlyer SDK | 
 In addition to the required Braze SDK, you must install the AppsFlyer SDK. | 

 Email domain setup complete | 
 You must have completed the IP and domain setup step of setting up your email during Braze onboarding. | 

 SSL certificate | 
 Your SSL certificate must be configured. | 

## Integration

### Step 1: Map device ID

- android
 
- ios
 
- unity

If you have an Android app, you must pass a unique Braze device ID to AppsFlyer.

Ensure the following lines of code are inserted at the correct place—after the Braze SDK is launched and before the initialization code for the AppsFlyer SDK. See the AppsFlyer Android SDK integration guide for more information.

```

1
2
3
4
5

```
 | 
```
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
 customData["brazeCustomerId"] = deviceId
 setAdditionalData(customData)
}

```
 | 

important

Prior to February 2023, our AppsFlyer attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze device_id and send it to AppsFlyer upon install because there is no disruption of service.

For those using the Swift SDK v5.7.0+, if you want to continue using IDFV as the mutual identifier, you must confirm that the useUUIDAsDeviceId field is set to false to avoid a disruption of the integration.

If set to true, you must implement the iOS device ID mapping for Swift in order to pass the Braze device_id to AppsFlyer upon app install in order for Braze to appropriately match iOS attributions.

- swift
 
- objective-c

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
let configuration = Braze.Configuration(
 apiKey: "<BRAZE_API_KEY>",
 endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]

```
 | 

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
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
 @"brazeDeviceId": braze.deviceId
}];

```
 | 

To map the device ID in Unity, use the following:

```

1
2
3
4

```
 | 
```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);

```
 | 

### Step 2: Get the Braze data import key

In Braze, navigate to Partner Integrations > Technology Partners and select AppsFlyer.

Here, you find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in AppsFlyer’s dashboard.

### Step 3: Configure Braze in AppsFlyer’s dashboard

- In AppsFlyer, navigate to the Integrated Partners page from the navigation menu. Next, search for Braze and select the Braze logo to open a configuration window.
 
- Within the Integration tab, switch on Activate Partner.
 
- Provide the data import key and REST endpoint that you found in the Braze dashboard.
 
- Toggle Advanced Privacy off and save your configuration.

important

When entering the Braze REST endpoint in AppsFlyer’s Integration tab, enter only the domain (for example, rest.fra-02.braze.eu) without the https:// protocol and without the /attribution/appsflyer path. AppsFlyer automatically prepends the protocol and appends the path. Including either in your input causes postback failures.

Additional information on these instructions is available in AppsFlyer’s documentation.

### Step 4: Confirm the integration

On the AppsFlyer technology partners page in Braze, the connection indicator shows Not Connected until you generate a data import API key in Step 2. After you generate the key, the indicator changes to Connected and displays a timestamp. That timestamp reflects when the integration was first set up in Braze (when the data import key was created), not when AppsFlyer last sent a postback.

To confirm that install attribution data is flowing from AppsFlyer, use Step 5 to verify that non-organic install data appears in Braze segment filters. Braze ignores organic installs from AppsFlyer postbacks and does not store them as attributed install data.

### Step 5: Viewing user attribution data

#### Available data fields

If your integration was successful, Braze maps all non-organic install data to segment filters.

 AppsFlyer data field | 
 Braze segment filter | 

 media_source | 
 Attributed Source | 

 campaign | 
 Attributed Campaign | 

 af_adset | 
 Attributed Adgroup | 

 af_ad | 
 Attributed Ad | 

You can segment your user base by attribution data in the Braze dashboard using the Install Attribution filters.

Additionally, attribution data for a particular user is available on each user’s profile in the Braze dashboard.

note

Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties, and, therefore, our partners cannot send that data to Braze.

## Integrate AppsFlyer with Braze for deep linking

Deep links—links that direct users toward a specific page or place within an app or website—are used to create a tailored user experience.

While widely used, issues can arise when using emailed deep links with click tracking#8212another important feature used in collecting user data. These issues are due to Email Service Providers (ESPs) wrapping deep links in a click-recording domain, breaking the original link. As such, supporting deep links requires additional setup.

AppsFlyer provides a service that avoids these issues, enabling AppsFlyer to serve as an intermediary between the ESP server and your domain name. Its role as a proxy enables the provision of association files (AASA/asset links), which facilitates deep linking.

## Step 1 - Create a Click Tracking Domain

Following the initial elements of Braze’s Email set-up guidance, create an email sending domain and a click tracking domain. For support, you can raise a ticket via the Braze Dashboard to initiate setup for the new CTD with the Braze Email team.

Creating a new CTD is mandatory, even if you already use an existing one. This ensures that there is no impact on the traffic of current live email campaigns.

important

AppsFlyers creates the SSL certificate. At this stage, email links are likely not secured, meaning the URL prefix is HTTP instead of HTTPS. This is resolved in later steps.

## Step 2 - Create a OneLink Template in AppsFlyer

Create a OneLink template and configure Universal Links/App Links under “When app is installed”. This template is used later to create OneLink links for your email campaigns.

note

If you already have an existing OneLink template configured that enables Universal Links/App Links, you can use it.

## Step 3 - Set up your Braze Integration in Appsflyer

Now it’s time to set your Braze integration in AppsFlyer. This step and the following one (“Configure your app”) can be set up at the same time.
To set your Braze integration in AppsFlyer:

### 1. In AppsFlyer, from the side menu, select Engage > ESP integration.

### 2. Select Braze.

### 3. Select the OneLink template you want to use for email campaigns, then click Next.

### 4. Enter your click tracking domain and “Braze endpoint” value, which was provided with the new CTD created in step 1, then click Validate connection.

This validates that the click-tracking domain points to the endpoint you entered.

By “Braze Endpoint”, AppsFlyer is asking for the details provided by Braze in Step 1 of this guide, specifically the new CTD.

Then click Validate connection, which validates that the click-tracking domain points to the endpoint you entered.
When done, click Next.

### 5. Route link traffic to AppsFlyer:

#### a. Copy and send the customized pre-fabricated instructions in AppsFlyer to your IT or domain administrator.

Your administrator must reroute your email campaign traffic from the ESP servers to the AppsFlyer servers by updating your DNS CNAME records with the new domain that AppsFlyer provided.

As a result, every time a link is clicked, the click is redirected to AppsFlyer, which in turn redirects it to the ESP endpoint.

#### b. After copying and sending the instructions, click Done.

Your Braze integration has been created.

important

Your Braze integration status is pending and starts working only after the CNAME record is mapped. It can take up to 24 hours after mapping for a new integration to start working and become active.

## Step 4: Configure your App (Developer-Task)

Appsflyer offers guidance on correct app configuration, which should be followed by your web or app teams in order to support universal linking.

## Step 5: Confirm SSL Click-tracking is enabled with Braze

At this stage, after you share and validate the CTD details in Appsflyer, we recommend performing a test send to confirm if your Onelink sending domain has an SSL certificate. This is in line with our Email Setup guide.

You can perform quality assurance and troubleshooting by sending a deep link using OneLink. See the AppsFlyer documentation for details on using OneLink.

If CTD links are identified as HTTP, contact Braze’s Email Ops team to enable SSL click-tracking. This ensures that all HTTP links are automatically converted to HTTPS.
You can use the following sample message text when contacting your Customer Success Manager, or by raising a ticket in the Braze Dashboard again, like in step 1:

```

1
2

```
 | 
```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS. 

```
 | 

### AppsFlyer click tracking URLs in Braze (optional)

You can use AppsFlyer’s OneLink attribution links in Braze campaigns across push, email, and more. This allows you to send back install or re-engagement attribution data from your Braze campaigns into AppsFlyer. As a result, you can measure your marketing efforts more effectively and make data-driven decisions.

You can simply create your OneLink tracking URL in AppsFlyer and directly insert it into your Braze campaigns. AppsFlyer then uses their probabilistic attribution methodologies to attribute the user that has clicked on the link. We recommend appending your AppsFlyer tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This deterministically attributes the user that has clicked on the link.

- android
 
- ios

For Android, Braze allows customers to opt in to Google Advertising ID collection (GAID). The AppsFlyer SDK integration also collects the GAID. You can include the GAID in your AppsFlyer click-tracking links by using the following Liquid logic:

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

For iOS, both Braze and AppsFlyer automatically collect the IDFV natively through our SDK integrations. You can use the IDFC as the device identifier. You can include the IDFV in your AppsFlyer click-tracking links by using the following Liquid logic:

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

- 

New Stuff!
