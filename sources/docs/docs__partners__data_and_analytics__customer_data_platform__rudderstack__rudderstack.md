---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack
slug: docs__partners__data_and_analytics__customer_data_platform__rudderstack__rudderstack
title: "RudderStack"
description: "This article outlines the partnership between Braze and RudderStack, an open-source customer data infrastructure offering seamless Braze integration for your Android, iOS, and web applications...."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# RudderStack

RudderStack is an open-source customer data infrastructure for collecting and routing customer event data to your preferred data warehouse and dozens of other analytics providers, such as Braze. It is enterprise-ready and offers a robust transformation framework to process your event data on the fly.

The Braze and RudderStack integration offers a native SDK integration for your Android, iOS, and web applications and a server-to-server integration from your backend services.

## Prerequisites

 Requirement | 
 Description | 

 RudderStack account | 
 A RudderStack account is required to take advantage of this partnership. | 

 Configured source | 
 A source is essentially the origin of any data sent to RudderStack, such as websites, mobile apps, or backend servers. You are required to configure the source before setting up Braze as a destination in RudderStack. | 

 Braze REST API key | 
 A Braze REST API key with users.track, users.identify, users.delete, and users.alias.new permissions.

This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze app key | 
 To get your app key in the Braze dashboard go to Settings > App Settings > Identification and find your app name. Save the associated identifier string. | 

 Data center | 
 Your data center aligns with your Braze dashboard instance. | 

## Integration

### Step 1: Add a source

To start sending data to Braze, you first need to make sure a source is set up in your RudderStack app. Visit RudderStack to learn how to set up your data source.

### Step 2: Configure destination

Now that your data source is set up, in the RudderStack dashboard, select ADD DESTINATION under Destinations. From the list of available destinations, select Braze and click Next.

In the Braze destination, provide the app key, Braze REST API key, data cluster, and native SDK option (device mode only). The native SDK option will use the Braze native SDK to send events if toggled on.

### Step 3: Choose the type of integration

You can choose to integrate RudderStack’s web and native client-side libraries with Braze using one the following approaches:

- Side-by-side / device mode: RudderStack will send the event data to Braze directly from your client (browser or mobile application).
 
- Server-to-server / cloud mode: The Braze SDK sends the event data directly to RudderStack, which is then transformed and routed to Braze.
 
- Hybrid mode: Use hybrid mode to send iOS and Android auto-generated and user-generated events to Braze using a single connection.

note

Learn more about RudderStack’s connection modes and the benefits of each.

#### Side-by-side integration (device mode)

With this mode, you can send your events to Braze using the Braze SDK set up on your website or mobile app.

Set up the mappings to the RudderStack SDK for your platform on the Braze GitHub repository, as described under supported methods:

- Android
 
- iOS
 
- Swift
 
- Web
 
- React Native
 
- Flutter

To complete the device mode integration, refer to the detailed RudderStack instructions for adding Braze to your project.

#### Server-to-server integration (cloud mode)

In this mode, the SDK sends the event data directly to the RudderStack server. RudderStack then transforms this data and routes it to the desired destination. This transformation is done in the RudderStack backend using RudderStack’s transformer module.

To enable the integration, you will need to map the RudderStack methods to Braze, as described under supported methods.

note

RudderStack’s server-side SDKs (Java, Python, Node.js, Go, Ruby) support only cloud mode. This is because their server-side SDKs operate in the RudderStack backend and cannot load any Braze-specific SDK.

important

The server-to-server integration does not support Braze UI features, such as push notifications or in-app messaging. These features are, however, supported by the device mode integration.

#### Hybrid mode

Use hybrid mode to send all events to Braze from your iOS and Android sources.

When you choose hybrid mode to send events to Braze, RudderStack:

- Initializes the Braze SDK.
 
- Sends all the user-generated events (identify, track, page, screen, and group) to Braze only through cloud mode and blocks them from being sent via device mode.
 
- Sends the auto-generated events (in-app messages, push notifications that require the Braze SDK) via device mode.

To send events via hybrid mode, use the hybrid mode option while connecting your source to the Braze destination. Then, add the Braze integration to your project.

## Step 4: Configure additional settings

After completing the initial setup, configure the following settings to correctly receive your data in Braze:

- Enable subscription groups in group call: Enable this setting to send the subscription group status in your group events. For more information, see Group.
 
- Use Custom Attributes Operation: Enable this setting if you want to use the nested custom attributes functionality in Braze to create segments and personalize your messages using a custom attribute object. For more information, see Send user traits as nested custom attributes.
 
- Track events for anonymous users: Enable this setting to track anonymous user activity and send this information to Braze.

### Device mode settings

The following settings are applicable only if you’re sending events to Braze via the device mode:

- Client-side Events Filtering: This setting lets you specify which events should be blocked or allowed to flow through to Braze. For more information on this setting, see Client-side Events Filtering.
 
- Deduplicate Traits: Enable this setting to deduplicate the user traits in the identify call.
 
- Show Braze logs: This setting is applicable only while using the JavaScript SDK as a source. Enable it to show the Braze logs to your users.
 
- OneTrust Cookie Categories: This setting lets you associate the OneTrust cookie consent groups to Braze.

## Supported methods

Braze supports the RudderStack methods identify, track, screen, page, group, and alias.

- identify
 
- track
 
- screen
 
- page
 
- group
 
- alias

The RudderStack identify method associates users with their actions. RudderStack captures a unique user ID and optional traits associated with that user, such as name, email, IP address, etc.

Delta management for identify calls

If you send events to Braze via device mode, you can save costs by deduplicating your identify calls. To do so, enable the Deduplicate Traits dashboard setting. RudderStack then sends only the changed or modified attributes (traits) to Braze.

Deleting a user

You can delete a user in Braze using the Suppression with Delete regulation of the RudderStack Data Regulation API.

RudderStack’s track method captures all the user activities and the properties associated with those activities.

Order completed

On using the RudderStack eCommerce API to call the track method for an event with the name Order Completed, RudderStack sends the products listed in that event to Braze as purchases.

RudderStack’s screen method allows you to record your users’ mobile screen views with any additional information about the viewed screen.

RudderStack’s page method lets you record your website’s page views. It also captures any other relevant information about that page.

RudderStack’s group method allows you to associate a user with a group.

Subscription group status

To update the subscription group status, enable the “Enable subscription groups in group call” setting in the RudderStack dashboard and send the subscription group status in the group call.

RudderStack’s alias method allows you to merge different identities of a known user. Note that RudderStack supports the alias call for Braze only in cloud mode.

## Send user traits as nested custom attributes

You can send the user traits to Braze as nested custom attributes and perform add, update, and remove operations on them. To do so, enable the “Use Custom Attributes Operation dashboard” setting in RudderStack while configuring the Braze destination. This feature is only available in cloud mode.

You can send the user traits as nested custom attributes in your identify events in the following format:

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
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39

```
 | 
```
rudderanalytics.identify("1hKOmRA4GRlm", {
 "cars": {
 "add": [{
 "age": 27,
 "id": 1,
 "name": "Alex Keener"
 }],
 "update": [{
 "age": 30,
 "id": 2,
 "identifier": "id",
 "name": "Rowan"
 },
 {
 "age": 27,
 "id": 1,
 "identifier": "id",
 "name": "Alex"
 }
 ]
 },
 "country": "USA",
 "email": "[email protected]",
 "firstName": "Alex",
 "gender": "M",
 "pets": [{
 "breed": "beagle",
 "id": 1,
 "name": "Scooby",
 "type": "dog"
 },
 {
 "breed": "calico",
 "id": 2,
 "name": "Garfield",
 "type": "cat"
 }
 ]
})

```
 | 

To send the user traits as custom user attributes via the track, page, or screen calls, pass traits as a contextual field in the event:

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
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45

```
 | 
```
rudderanalytics.track("Product Viewed", {
 revenue: 8.99,
 currency: "USD",
 },{
 "traits": {
 "cars": {
 "add": [{
 "age": 27,
 "id": 1,
 "name": "Alex Keener"
 }],
 "update": [{
 "age": 30,
 "id": 2,
 "identifier": "id",
 "name": "Alex"
 },
 {
 "age": 27,
 "id": 1,
 "identifier": "id",
 "name": "Rowan"
 }
 ]
 },
 "city": "Disney",
 "country": "USA",
 "email": "[email protected]",
 "firstName": "Alexa",
 "gender": "woman",
 "pets": [{
 "breed": "beagle",
 "id": 1,
 "name": "Scooby",
 "type": "dog"
 },
 {
 "breed": "calico",
 "id": 2,
 "name": "Garfield",
 "type": "cat"
 }
 ]
 }
});

```
 | 

note

For the update and remove operations, identifier is a required key. If add, update, or remove operations are not present in the nested array, RudderStack uses the create operation to create the properties by default. Refer to Array of objects for more information on sending nested custom attributes.

## Troubleshooting

### I see “[Braze Deduplication]: Duplicate user detected, the user is dropped” in RudderStack logs

This message comes from RudderStack when Deduplicate Traits is enabled and RudderStack drops unchanged user traits before forwarding to Braze. It is not a Braze error.

RudderStack compares incoming identify and track traits to the user profile and skips attributes with no delta to reduce Braze data point usage. For details, see RudderStack’s User Trait Deduplication in Braze guide.

If you need every trait sent on each call, turn off Deduplicate Traits in your RudderStack Braze destination settings. Be aware this can increase Braze data point consumption.

- 

New Stuff!
