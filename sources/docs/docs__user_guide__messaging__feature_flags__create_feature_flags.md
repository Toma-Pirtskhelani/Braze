---
url: https://www.braze.com/docs/user_guide/messaging/feature_flags/create_feature_flags
slug: docs__user_guide__messaging__feature_flags__create_feature_flags
title: "Create feature flags"
description: "This reference article covers how to create feature flags to coordinate new feature rollouts."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create feature flags

Feature flags allow you to remotely enable or disable functionality for a selection of users. Create a new feature flag within the Braze dashboard. Provide a name and an ID, a target audience, and a percentage of users for whom to enable to this feature. Then, using that same ID in your app or website’s code, you can conditionally run certain parts of your business logic. To learn more about feature flags and how you can use them in Braze, see About feature flags.

## Prerequisites

### SDK version

To use feature flags, ensure your SDKs are up to date with at least these minimum versions:

   Swift: 5.9.0+     Web: 4.6.0+     Android: 24.2.0+     Roku: 1.0.0+  Flutter: 6.0.0+  Unity: 4.1.0+  React Native: 4.1.0+  Cordova: 5.0.0+  

### Braze permissions

To manage feature flags in the dashboard, you’ll either need to be an Administrator, or have the following permissions:

 Permission | 
 What you can do | 

 Manage Feature Flags | 
 View, create, and edit feature flags. | 

 Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library | 
 View the list of available feature flags. | 

## Creating a feature flag

### Step 1: Create a new feature flag

Go to Messaging > Feature Flags, then select Create Feature Flag.

### Step 2: Fill out the details

Under Feature flag details, enter a name, ID, and description for your feature flag.

 Field | 
 Description | 

 Name | 
 A human-readable title for your marketers and administrators. | 

 ID | 
 The unique ID you’ll use in your code to check if this feature is enabled for a user. This ID cannot be changed later, so review the ID naming best practices before continuing. | 

 Description | 
 An optional description that gives some context about your feature flag. | 

 Properties | 
 Optional properties that remotely configure your feature flag. They can be overwritten in Canvas steps or feature flag experiments. | 

### Step 2a: Create custom properties

Under Properties, you can optionally create custom properties your app can access through the Braze SDK when your feature is enabled. You can assign a string, boolean, image, timestamp, JSON, or a number value to each variable, as well as set a default value.

- example

In the following example, the feature flag shows an out-of-stock banner for an eCommerce store using the custom properties listed:

 Property Name | 
 Type | 
 Value | 

 banner_height | 
 number | 
 75 | 

 banner_color | 
 string | 
 blue | 

 banner_text | 
 string | 
 Widgets are out of stock until July 1. | 

 dismissible | 
 boolean | 
 false | 

 homepage_icon | 
 image | 
 http://s3.amazonaws.com/[bucket_name]/ | 

 account_start | 
 timestamp | 
 2011-01-01T12:00:00Z | 

 footer_settings | 
 JSON | 
 { "colors": [ "red", "blue", "green" ], "placement": 123 } | 

tip

There is no limit to the number of properties you can add. However, a feature flag’s properties are limited to a total of 10,000 characters.

### Step 4: Choose segments to target

Before rolling out a feature flag, you need to choose a segment of users to target. Select Add Rule on your newly created flag and then use the filter group and segment dropdown menus to filter users out of your target audience. Add multiple filters to further narrow your audience.

### Step 5: Set the rollout traffic

By default, feature flags are always inactive, which allows you to separate your feature release’s date from your total user activation. To begin your rollout, use the Rollout Traffic section to enter a percentage in the text box. This will choose the percentage of random users in your selected segment to receive this new feature.

important

Do not set your rollout traffic greater than 0% until you are ready for your new feature to go live. When you initially define your feature flag in the dashboard, leave this setting at 0%.

important

To roll out a flag with just one rule or to a singular audience, add your first rule with segmentation criteria and rollout percentages selected. Lastly, confirm the Everyone Else rule is toggled off, and save your flag.

## Multi-rule feature flag rollouts

Use multi-rule feature flag rollouts to define a sequence of rules for evaluating users, which allows for precise segmentation and controlled feature releases. This method is ideal for deploying the same feature to diverse audiences.

### Evaluation order

Feature flag rules are evaluated from top to bottom, in the order they’re listed. A user qualifies for the first rule they meet. If a user doesn’t meet any rules, their eligibility is determined by the default “Everyone Else” rule.

### User qualification

- If a user meets the criteria for the first rule, they are immediately eligible to receive the feature flag.
 
- If a user doesn’t qualify for the first rule, they’re evaluated against the second rule, and so on.

The sequential evaluation continues until a user qualifies for a rule or reaches the “Everyone Else” rule at the bottom of the list.

### “Everyone Else” rule

The “Everyone Else” rule acts as a default. If a user doesn’t qualify for any preceding rules, their eligibility for the feature flag will be determined by the toggle setting of the “Everyone Else” rule. For example, if the “Everyone Else” rule is toggled “Off”, in the default state, a user who doesn’t meet the criteria for any other rules won’t receive the feature flag upon their session start.

### Re-ordering rules

By default, rules are ordered in the sequence that they’re created, but you can reorder these rules by dragging and dropping them in the dashboard.

### Multi-rule feature flag use cases

#### Gradually release a checkout page

Let’s say you work for an eCommerce brand and have a new checkout page that you want to rollout across different geographies to ensure stability. Using multi-rule feature flags, you can set the following:

- Rule 1: Your US segment is set to 100%.
 
- Rule 2: Your segment is set to 50% of your Brazilian users, so not all of them receive the flow at one time.
 
- Rule 3 (Everyone Else): For all other users, toggle on your “Everyone Else” rule and set it to 15%, so that a portion of all users can check out with the new flow.

#### Reach internal testers first

Let’s say you’re a product manager who wants to make sure your internal testers always receive the feature flag when you release a new product. You can add your internal testers segment to your first rule and set it to 100%, so that your internal testers are eligible during every feature rollout.

## Using the “enabled” field for your feature flags

After you’ve defined your feature flag, configure your app or site to check whether or not it is enabled for a particular user. When it is enabled, you’ll set some action or reference the feature flag’s variable properties based on your use case. The Braze SDK provides getter methods to pull your feature flag’s status and its properties into your app.

Feature flags are refreshed automatically at session start so that you can display the most up-to-date version of your feature upon launch. The SDK caches these values so they can be used while offline.

note

Be sure to log feature flag impressions.

Let’s say you were to rolling out a new type of user profile for your app. You might set the ID as expanded_user_profile. Then, you would have your app check to see if it should display this new user profile to a particular user. For example:

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

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
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
 console.log(`expanded_user_profile is enabled`);
} else {
 console.log(`expanded_user_profile is not enabled`);
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

```
 | 
```
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
 print("expanded_user_profile is enabled")
} else {
 print("expanded_user_profile is not enabled")
}

```
 | 

- java
 
- kotlin

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
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
 Log.i(TAG, "expanded_user_profile is enabled");
} else {
 Log.i(TAG, "expanded_user_profile is not enabled");
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

```
 | 
```
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
 Log.i(TAG, "expanded_user_profile is enabled.")
} else {
 Log.i(TAG, "expanded_user_profile is not enabled.")
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

```
 | 
```
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
 console.log(`expanded_user_profile is enabled`);
} else {
 console.log(`expanded_user_profile is not enabled`);
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

```
 | 
```
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
 Console.WriteLine("expanded_user_profile is enabled");
} else {
 Console.WriteLine("expanded_user_profile is not enabled");
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

```
 | 
```
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
 console.log(`expanded_user_profile is enabled`); 
} else {
 console.log(`expanded_user_profile is not enabled`);
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

```
 | 
```
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
 print("expanded_user_profile is enabled");
} else {
 print("expanded_user_profile is not enabled");
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

```
 | 
```
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
 print "expanded_user_profile is enabled"
else
 print "expanded_user_profile is not enabled"
end if

```
 | 

### Logging a feature flag impression

Track a feature flag impression whenever a user has had an opportunity to interact with your new feature, or when they could have interacted if the feature is disabled (in the case of a control group in an A/B test). Feature flag impressions are only logged once per session.

Usually, you can put this line of code directly underneath where you reference your feature flag in your app:

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

```

1

```
 | 
```
braze.logFeatureFlagImpression("expanded_user_profile");

```
 | 

```

1

```
 | 
```
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")

```
 | 

- java
 
- kotlin

```

1

```
 | 
```
braze.logFeatureFlagImpression("expanded_user_profile");

```
 | 

```

1

```
 | 
```
braze.logFeatureFlagImpression("expanded_user_profile")

```
 | 

```

1

```
 | 
```
Braze.logFeatureFlagImpression("expanded_user_profile");

```
 | 

```

1

```
 | 
```
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");

```
 | 

```

1

```
 | 
```
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");

```
 | 

```

1

```
 | 
```
braze.logFeatureFlagImpression("expanded_user_profile");

```
 | 

```

1

```
 | 
```
m.Braze.logFeatureFlagImpression("expanded_user_profile");

```
 | 

### Accessing properties

To access the properties of a feature flag, use one of the following methods depending on the type you defined in the dashboard.

If there is no such property of the corresponding type for the key you provided, these methods will return null.

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

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

```
 | 
```
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");

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
16
17
18
19
20

```
 | 
```
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the string property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty: Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty: String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty: [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")

```
 | 

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
17
18
19
20

```
 | 
```
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");

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
16
17
18
19
20

```
 | 
```
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String? = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")

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
16
17

```
 | 
```
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");

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
16
17
18
19
20
21
22
23

```
 | 
```
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");

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
16
17

```
 | 
```
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");

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
16
17
18
19
20

```
 | 
```
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");

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
16
17

```
 | 
```
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")

```
 | 

### Getting a list of all feature flags

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

```

1
2
3
4

```
 | 
```
const features = getAllFeatureFlags();
for(const feature of features) {
 console.log(`Feature: ${feature.id}`, feature.enabled);
}

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
let features = braze.featureFlags.featureFlags
for let feature in features {
 print("Feature: \(feature.id)", feature.enabled)
}

```
 | 

- java
 
- kotlin

```

1
2
3
4

```
 | 
```
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
 Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}

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
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
 Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}

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
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
 console.log(`Feature: ${feature.id}`, feature.enabled);
}

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
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
 Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}

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
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
 console.log(`Feature: ${feature.id}`, feature.enabled);
}

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
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
 print("Feature: ${feature.id} ${feature.enabled}");
});

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
features = m.braze.getAllFeatureFlags()
for each feature in features
 print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for

```
 | 

### Refreshing feature flags

You can refresh the current user’s feature flags mid-session to pull the latest values from Braze.

tip

Refreshing happens automatically upon session start. Refreshing is only needed prior to important user actions, such as before loading a checkout page, or if you know a feature flag will be referenced.

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

```

1
2
3
4
5

```
 | 
```
braze.refreshFeatureFlags(() => {
 console.log(`Feature flags have been refreshed.`);
}, () => {
 console.log(`Failed to refresh feature flags.`);
});

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

```
 | 
```
braze.featureFlags.requestRefresh { result in
 switch result {
 case .success(let features):
 print("Feature flags have been refreshed:", features)
 case .failure(let error):
 print("Failed to refresh feature flags:", error)
 }
}

```
 | 

- java
 
- kotlin

```

1

```
 | 
```
braze.refreshFeatureFlags();

```
 | 

```

1

```
 | 
```
braze.refreshFeatureFlags()

```
 | 

```

1

```
 | 
```
Braze.refreshFeatureFlags();

```
 | 

```

1

```
 | 
```
Appboy.AppboyBinding.RefreshFeatureFlags();

```
 | 

```

1

```
 | 
```
BrazePlugin.refreshFeatureFlags();

```
 | 

```

1

```
 | 
```
braze.refreshFeatureFlags();

```
 | 

```

1

```
 | 
```
m.Braze.refreshFeatureFlags()

```
 | 

### Listening for changes

You can configure the Braze SDK to listen and update your app when the SDK refreshes any feature flags.

This is useful if you want to update your app if a user is no longer eligible for a feature. For example, setting some state in your app based on whether or not a feature is enabled, or one of its property values.

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku
 
- react hook

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
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
 console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);

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

```
 | 
```
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
 print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()

```
 | 

- java
 
- kotlin

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
braze.subscribeToFeatureFlagsUpdates(event -> {
 Log.i(TAG, "Feature flags were updated.");
 for (FeatureFlag feature: event.getFeatureFlags()) {
 Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
 }
});

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
braze.subscribeToFeatureFlagsUpdates() { event ->
 Log.i(TAG, "Feature flags were updated.")
 event.featureFlags.forEach { feature ->
 Log.i(TAG, "Feature: ${feature.id}")
 }
}

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
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
 console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});

```
 | 

To listen for changes, set the values for Game Object Name and Callback Method Name under Braze Configuration > Feature Flags to the corresponding values in your application.

```

1
2
3
4

```
 | 
```
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
 console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});

```
 | 

In the Dart code in your app, use the following sample code:

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
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
 print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();

```
 | 

- flutter sdk 18.0.0+
 
- flutter sdk 17.1.0 and earlier

Feature flag data is automatically forwarded from both the Android and iOS native layers. No additional setup is required.

If you’re using Flutter SDK 17.1.0 or earlier, feature flag data forwarding from the iOS native layer requires manual setup. Your application likely contains a featureFlags.subscribeToUpdates callback that calls BrazePlugin.processFeatureFlags(featureFlags). To migrate to Flutter SDK 18.0.0, remove the BrazePlugin.processFeatureFlags(_:) call—data forwarding is now handled automatically.

For an example, see AppDelegate.swift in the Braze Flutter SDK sample application.

```

1
2

```
 | 
```
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")

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
import { useEffect, useState } from "react";
import {
 FeatureFlag,
 getFeatureFlag,
 removeSubscription,
 subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
 const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
 getFeatureFlag(id)
 );

 useEffect(() => {
 const listener = subscribeToFeatureFlagsUpdates(() => {
 setFeatureFlag(getFeatureFlag(id));
 });
 return () => {
 removeSubscription(listener);
 };
 }, [id]);

 return featureFlag;
};

```
 | 

## Checking user eligibility

To check which feature flags a user is eligible for in Braze, go to Audience > Search Users, then search for and select a user.

In the Feature Flags Eligibility tab, you can filter the list of eligible feature flags by platform, application, or device. You can also preview the payload that will be returned to the user by selecting next to a feature flag.

## Viewing the changelog

To view a feature flag’s changelog, open a feature flag and select Changelog.

Here, you can review when a change happened, who made the change, which category it belongs to, and more.

## Segmenting with feature flags

Braze automatically keeps track of which users are currently enabled for a feature flag. You can create a segment or target messaging using the Feature Flag filter. For more information about filtering on segments, see Creating a segment.

note

To prevent recursive segments, it is not possible to create a segment that references other feature flags.

## Best practices

### Don’t combine rollouts with Canvases or experiments

To avoid users being enabled and disabled by different entry points, you should either set the rollouts slider to a value greater than zero OR enable the feature flag in a Canvas or experiment. As a best practice, if you plan to use a feature flag in a Canvas or experiment, keep the rollout percentage at zero.

### Naming conventions

To keep your code clear and consistent, consider using the following format when naming your feature flag ID:

```

1

```
 | 
```
BEHAVIOR_PRODUCT_FEATURE

```
 | 

Replace the following:

 Placeholder | 
 Description | 

 BEHAVIOR | 
 The behavior of the feature. In your code, be sure the behavior is disabled by default and avoid using phrases like disabled in the feature flag name. | 

 PRODUCT | 
 The product the feature belongs to. | 

 FEATURE | 
 The name of the feature. | 

Here’s an example feature flag where show is the behavior, animation_profile is the product, and driver is the feature:

```

1

```
 | 
```
show_animation_profile_driver

```
 | 

### Planning ahead

Always play it safe. When considering new features that may require an off switch, it’s better to release new code with a feature flag and not need it than it is to realize a new app update is required.

### Be descriptive

Add a description to your feature flag. While this is an optional field in Braze, it can help answer questions others may have when browsing available feature flags.

- Contact details for who is responsible for the enablement and behavior of this flag
 
- When this flag should be disable
 
- Links to documentation or notes about the new feature this flag controls
 
- Any dependencies or notes on how to use the feature

### Clean up old feature flags

We’re all guilty of leaving features on at 100% rollout for longer than necessary.

To help keep your code (and Braze dashboard) clean, remove permanent feature flags from your code base after all users have upgraded and you no longer need the option to disable the feature. This helps reduce the complexity of your development environment, but also keeps your list of feature flags tidy.

- 

New Stuff!
