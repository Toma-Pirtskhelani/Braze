---
url: https://www.braze.com/docs/developer_guide/sdk_integration/google_tag_manager
slug: docs__developer_guide__sdk_integration__google_tag_manager
title: "Google Tag Manager with the Braze SDK"
description: "Learn how to initialize the Braze SDK using methods like runtime initialization, delayed initialization, or Google Tag Manager."
section: developer_guide/sdk_integration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Google Tag Manager with the Braze SDK

Learn how to use Google Tag Manager (GTM) with the Braze SDK, so you can remotely control Braze event tracking and user attribute updates without requiring code changes or new app releases.

- web
 
- android
 
- swift

## About Google Tag Manager for Web

Google Tag Manager (GTM) lets you remotely add, remove, and edit tags on your website without requiring a production code release or engineering resources. Braze offers the following templates for the Web SDK:

 Tag Type | 
 Use Case | 

 Initialization tag | 
 This tag lets you integrate the Web Braze SDK without needing to modify your site’s code. | 

 Action tag | 
 This tag lets you create Content Cards, set user attributes, and manage data collection. | 

## Tag sequencing for Braze action tags

The Braze Initialization tag must fire before any tags that call Braze SDK methods (such as braze.getUser(), braze.logCustomEvent(), or braze.logPurchase()). If these methods fire before the SDK is initialized, you may encounter errors like Uncaught TypeError: Cannot read properties of undefined (reading 'getUser').

To configure tag sequencing in Google Tag Manager:

- Open the tag that calls Braze SDK methods (such as a Custom HTML tag or Braze action tag).
 
- Go to Advanced Settings > Tag Sequencing.
 
- Select A tag that fires before [this tag] is fired.
 
- Choose your Braze Initialization tag.

This ensures the SDK is fully loaded before any other tags attempt to call Braze methods.

For more detail, see Verify tag sequencing for custom events.

## Log purchases with GTM

In Braze action tags and Custom HTML tags, call braze.logPurchase() to record revenue. The legacy appboy.logPurchase() namespace is not supported in current Web SDK integrations.

## Logging custom events with GTM

You can log custom events using a Custom HTML tag in GTM. This approach uses the GTM data layer to pass event data from your site to a GTM tag that calls the Braze Web SDK.

### Step 1: Push the event to the data layer

In your site’s code, push an event to the data layer wherever you want to trigger the custom event. For example, to log a custom event when a button is clicked:

```

1

```
 | 
```
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>

```
 | 

### Step 2: Create a trigger in GTM

- In your GTM container, go to Triggers and create a new trigger.
 
- Set the Trigger Type to Custom Event.
 
- Set the Event Name to the same value you pushed to the data layer (for example, my_custom_event).
 
- Choose when the trigger should fire (for example, All Custom Events).

### Step 3: Create a Custom HTML tag

- In GTM, go to Tags and create a new tag.
 
- Set the Tag Type to Custom HTML.
 
- 
 
In the HTML field, add the following:

```

1
2
3

```
 | 
```
 <script>
 window.braze.logCustomEvent("my_custom_event");
 </script>

```
 | 

- Under Triggering, select the trigger you created in step 2.
 
- Save and publish your container.

To include event properties, pass them as the second argument:

```

1
2
3

```
 | 
```
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>

```
 | 

## Google’s EU User Consent Policy

important

Google is updating its EU User Consent Policy in response to changes to the Digital Markets Act (DMA), which is in effect as of March 6, 2024. This new change requires advertisers to disclose certain information to their EEA and UK end users, as well as obtain necessary consents from them. Review the following documentation to learn more.

As part of Google’s EU User Consent Policy, the following boolean custom attributes need to be logged to user profiles:

- $google_ad_user_data
 
- $google_ad_personalization

If setting these via the GTM integration, custom attributes require creating a custom HTML tag. The following is an example of how to log these values as boolean data types (not as strings):

```

1
2
3

```
 | 
```
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>

```
 | 

For more information, refer to Audience Sync to Google.

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK.

## Using Google Tag Manager for Android

In the following example, a music streaming app wants to log different events as users listen to songs. Using Google Tag Manager for Android, they can control which of the Braze third-party vendors receive this event, and create tags specific to Braze.

### Step 1: Create a trigger for custom events

Custom events are logged with actionType set to logEvent. The Braze custom tag provider in this example is expecting the custom event name to be set using eventName.

To get started, create a trigger that looks for an “Event Name” that equals played song

Next, create a new tag (also known as a “Function Call”) and enter the class path of your custom tag provider described later in this article. This tag will be triggered when you log the played song event.

In the tag’s custom parameters (also known as the key-value pairs), set eventName to played song. This will be the custom event name logged to Braze.

important

When sending a custom event, be sure to set actionType to logEvent, and set a value for eventName so Braze receives the correct event name and action to take.

You can also include additional key-value pair arguments to the tag, which will be sent as custom event properties to Braze. eventName and actionType will not be ignored for custom event properties. In the following example tag, genre is passed and defined using a tag variable in Google Tag Manager, which is sourced from the custom event logged in the app.

Because Google Tag Manager for Android uses Firebase as the data layer, the genre event property is sent to Google Tag Manager as a “Firebase - Event Parameter” variable.

When a user plays a song in the app, an event will be logged through Firebase and Google Tag Manager using the Firebase analytics event name that matches the tag’s trigger name, played song:

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
Bundle params = new Bundle();
params.putString("genre", "pop");
params.putInt("number of times listened", 42);
mFirebaseAnalytics.logEvent("played song", params);

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
val params = Bundle()
params.putString("genre", "pop")
params.putInt("number of times listened", 42);
mFirebaseAnalytics.logEvent("played song", params)

```
 | 

### Step 2: Log custom attributes

Custom attributes are set via an actionType set to customAttribute. The Braze custom tag provider is expecting the custom attribute key-value to be set via customAttributeKey and customAttributeValue:

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
Bundle params = new Bundle();
params.putString("customAttributeKey", "favorite song");
params.putString("customAttributeValue", "Private Eyes");
mFirebaseAnalytics.logEvent("customAttribute", params);

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
val params = Bundle()
params.putString("customAttributeKey", "favorite song")
params.putString("customAttributeValue", "Private Eyes")
mFirebaseAnalytics.logEvent("customAttribute", params)

```
 | 

### Step 3: Call changeUser()

Calls to changeUser() are made via an actionType set to changeUser. The Braze custom tag provider is expecting the Braze user ID to be set via an externalUserId key-value pair within your tag:

- java
 
- kotlin

```

1
2
3

```
 | 
```
Bundle params = new Bundle();
params.putString("externalUserId", userId);
mFirebaseAnalytics.logEvent("changeUser", params);

```
 | 

```

1
2
3

```
 | 
```
val params = Bundle()
params.putString("externalUserId", userId)
mFirebaseAnalytics.logEvent("changeUser", params)

```
 | 

### Step 4: Add a custom tag provider

With the tags and triggers set up, you will also need to implement Google Tag Manager in your Android app which can be found in Google’s documentation.

After the Google Tag Manager is installed in your app, add a custom tag provider to call Braze SDK methods based on the tags you’ve configured within Google Tag Manager.

Be sure to note the “Class Path” to the file - this is what you’ll enter when setting up a Tag in the Google Tag Manager console.

This example highlights one of many ways you can structure your custom tag provider. Specifically, it shows how to determine which Braze SDK method to call based on the actionType key-value pair sent from the GTM Tag.

The actionType shown in this example are logEvent, customAttribute, and changeUser, but you may prefer to change how your tag provider handles data from Google Tag Manager.

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
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125

```
 | 
```
public class BrazeGtmTagProvider implements CustomTagProvider {
 private static final String TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider.class);
 private static final String ACTION_TYPE_KEY = "actionType";

 // Custom Events
 private static final String LOG_EVENT_ACTION_TYPE = "logEvent";
 private static final String EVENT_NAME_VARIABLE = "eventName";

 // Custom Attributes
 private static final String CUSTOM_ATTRIBUTE_ACTION_TYPE = "customAttribute";
 private static final String CUSTOM_ATTRIBUTE_KEY = "customAttributeKey";
 private static final String CUSTOM_ATTRIBUTE_VALUE_KEY = "customAttributeValue";

 // Change User
 private static final String CHANGE_USER_ACTION_TYPE = "changeUser";
 private static final String CHANGE_USER_ID_VARIABLE = "externalUserId";

 private static Context sApplicationContext;

 /**
 * Must be set before calling any of the following methods
 * so that the proper application context is available when needed.
 *
 * Recommended to be called in your {@link Application#onCreate()}.
 */
 public static void setApplicationContext(Context applicationContext) {
 if (applicationContext != null) {
 sApplicationContext = applicationContext.getApplicationContext();
 }
 }

 @Override
 public void execute(Map<String, Object> map) {
 BrazeLogger.i(TAG, "Got google tag manager parameters map: " + map);

 if (sApplicationContext == null) {
 BrazeLogger.w(TAG, "No application context provided to this tag provider.");
 return;
 }

 if (!map.containsKey(ACTION_TYPE_KEY)) {
 BrazeLogger.w(TAG, "Map does not contain the Braze action type key: " + ACTION_TYPE_KEY);
 return;
 }
 String actionType = String.valueOf(map.remove(ACTION_TYPE_KEY));

 switch (actionType) {
 case LOG_EVENT_ACTION_TYPE:
 logEvent(map);
 break;
 case CUSTOM_ATTRIBUTE_ACTION_TYPE:
 setCustomAttribute(map);
 break;
 case CHANGE_USER_ACTION_TYPE:
 changeUser(map);
 break;
 default:
 BrazeLogger.w(TAG, "Got unknown action type: " + actionType);
 break;
 }
 }

 private void logEvent(Map<String, Object> tagParameterMap) {
 String eventName = String.valueOf(tagParameterMap.remove(EVENT_NAME_VARIABLE));
 Braze.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap));
 }

 private BrazeProperties parseMapIntoProperties(Map<String, Object> map) {
 BrazeProperties brazeProperties = new BrazeProperties();
 for (Map.Entry<String, Object> entry : map.entrySet()) {
 final Object value = entry.getValue();
 final String key = entry.getKey();
 if (value instanceof Boolean) {
 brazeProperties.addProperty(key, (Boolean) value);
 } else if (value instanceof Integer) {
 brazeProperties.addProperty(key, (Integer) value);
 } else if (value instanceof Date) {
 brazeProperties.addProperty(key, (Date) value);
 } else if (value instanceof Long) {
 brazeProperties.addProperty(key, (Long) value);
 } else if (value instanceof String) {
 brazeProperties.addProperty(key, (String) value);
 } else if (value instanceof Double) {
 brazeProperties.addProperty(key, (Double) value);
 } else {
 BrazeLogger.w(TAG, "Failed to parse value into an BrazeProperties "
 + "accepted type. Key: '" + key + "' Value: '" + value + "'");
 }
 }

 return brazeProperties;
 }

 private void setCustomAttribute(Map<String, Object> tagParameterMap) {
 String key = String.valueOf(tagParameterMap.get(CUSTOM_ATTRIBUTE_KEY));
 Object value = tagParameterMap.get(CUSTOM_ATTRIBUTE_VALUE_KEY);

 Braze.getInstance(sApplicationContext).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 if (value instanceof Boolean) {
 brazeUser.setCustomUserAttribute(key, (Boolean) value);
 } else if (value instanceof Integer) {
 brazeUser.setCustomUserAttribute(key, (Integer) value);
 } else if (value instanceof Long) {
 brazeUser.setCustomUserAttribute(key, (Long) value);
 } else if (value instanceof String) {
 brazeUser.setCustomUserAttribute(key, (String) value);
 } else if (value instanceof Double) {
 brazeUser.setCustomUserAttribute(key, (Double) value);
 } else if (value instanceof Float) {
 brazeUser.setCustomUserAttribute(key, (Float) value);
 } else {
 BrazeLogger.w(TAG, "Failed to parse value into a custom "
 + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'");
 }
 }
 });
 }

 private void changeUser(Map<String, Object> tagParameterMap) {
 String userId = String.valueOf(tagParameterMap.get(CHANGE_USER_ID_VARIABLE));
 Braze.getInstance(sApplicationContext).changeUser(userId);
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
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106

```
 | 
```
class BrazeGtmTagProvider : CustomTagProvider {

 override fun execute(map: MutableMap<String, Any>) {
 BrazeLogger.i(TAG, "Got google tag manager parameters map: $map")

 if (sApplicationContext == null) {
 BrazeLogger.w(TAG, "No application context provided to this tag provider.")
 return
 }

 if (!map.containsKey(ACTION_TYPE_KEY)) {
 BrazeLogger.w(TAG, "Map does not contain the Braze action type key: $ACTION_TYPE_KEY")
 return
 }
 val actionType = map.remove(ACTION_TYPE_KEY).toString()

 when (actionType) {
 LOG_EVENT_ACTION_TYPE -> logEvent(map)
 CUSTOM_ATTRIBUTE_ACTION_TYPE -> setCustomAttribute(map)
 CHANGE_USER_ACTION_TYPE -> changeUser(map)
 else -> BrazeLogger.w(TAG, "Got unknown action type: $actionType")
 }
 }

 private fun logEvent(tagParameterMap: MutableMap<String, Any>) {
 val eventName = tagParameterMap.remove(EVENT_NAME_VARIABLE).toString()
 Braze.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap))
 }

 private fun parseMapIntoProperties(map: Map<String, Any>): BrazeProperties {
 val brazeProperties = BrazeProperties()
 map.forEach { param ->
 val key = param.key
 val value = param.value
 when (value) {
 is Boolean -> brazeProperties.addProperty(key, value)
 is Int -> brazeProperties.addProperty(key, value)
 is Date -> brazeProperties.addProperty(key, value)
 is Long -> brazeProperties.addProperty(key, value)
 is String -> brazeProperties.addProperty(key, value)
 is Double -> brazeProperties.addProperty(key, value)
 else -> BrazeLogger.w(TAG, "Failed to parse value into an BrazeProperties "
 + "accepted type. Key: '" + key + "' Value: '" + value + "'")
 }
 }

 return brazeProperties
 }

 private fun setCustomAttribute(tagParameterMap: Map<String, Any>) {
 val key = tagParameterMap[CUSTOM_ATTRIBUTE_KEY].toString()
 val value = tagParameterMap[CUSTOM_ATTRIBUTE_VALUE_KEY]

 Braze.getInstance(sApplicationContext).getCurrentUser { brazeUser ->
 when (value) {
 is Boolean -> brazeUser.setCustomUserAttribute(key, value)
 is Int -> brazeUser.setCustomUserAttribute(key, value)
 is Long -> brazeUser.setCustomUserAttribute(key, value)
 is String -> brazeUser.setCustomUserAttribute(key, value)
 is Double -> brazeUser.setCustomUserAttribute(key, value)
 is Float -> brazeUser.setCustomUserAttribute(key, value)
 else -> BrazeLogger.w(
 TAG, "Failed to parse value into a custom "
 + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'"
 )
 }
 }
 }

 private fun changeUser(tagParameterMap: Map<String, Any>) {
 val userId = tagParameterMap[CHANGE_USER_ID_VARIABLE].toString()
 Braze.getInstance(sApplicationContext).changeUser(userId)
 }

 companion object {
 private val TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider::class.java)
 private val ACTION_TYPE_KEY = "actionType"

 // Custom Events
 private val LOG_EVENT_ACTION_TYPE = "logEvent"
 private val EVENT_NAME_VARIABLE = "eventName"

 // Custom Attributes
 private val CUSTOM_ATTRIBUTE_ACTION_TYPE = "customAttribute"
 private val CUSTOM_ATTRIBUTE_KEY = "customAttributeKey"
 private val CUSTOM_ATTRIBUTE_VALUE_KEY = "customAttributeValue"

 // Change User
 private val CHANGE_USER_ACTION_TYPE = "changeUser"
 private val CHANGE_USER_ID_VARIABLE = "externalUserId"

 private var sApplicationContext: Context? = null

 /**
 * Must be set before calling any of the following methods so
 * that the proper application context is available when needed.
 *
 * Recommended to be called in your [Application.onCreate].
 */
 fun setApplicationContext(applicationContext: Context?) {
 if (applicationContext != null) {
 sApplicationContext = applicationContext.applicationContext
 }
 }
 }
}

```
 | 

In your Application.onCreate() be sure to add the following initialization for the previous snippet:

- java
 
- kotlin

```

1

```
 | 
```
BrazeGtmTagProvider.setApplicationContext(this.getApplicationContext());

```
 | 

```

1

```
 | 
```
BrazeGtmTagProvider.setApplicationContext(this.applicationContext)

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK.

## Using Google Tag Manager for Swift

In the following example, a music streaming app wants to log different events as users listen to songs. Using Google Tag Manager for iOS, they can control which of the Braze third-party vendors receive this event and create tags specific to Braze.

### Step 1: Create a trigger for custom events

Custom events are logged with actionType set to logEvent. In this example, the Braze custom tag provider is expecting the custom event name to be set using eventName.

First, create a trigger that looks for an eventName that equals played song.

Next, create a new Tag (also known as a “Function Call”) and enter the class path of your custom tag provider described later in this article. This tag will be triggered when you log the played song event. Because eventName is set to played song it will be used as custom event name that’s logged to Braze.

important

When sending a custom event, set actionType to logEvent, and set a value for eventName so Braze receives the correct event name and action to take.

You can also include additional key-value pair arguments to the tag, which will be sent as custom event properties to Braze. eventName and actionType will not be ignored for custom event properties. In the following example tag, pass in genre, which was defined using a tag variable in Google Tag Manager and sourced from the custom event logged in the app.

The genre event property is sent to Google Tag Manager as a “Firebase - Event Parameter” variable since Google Tag Manager for iOS uses Firebase as the data layer.

When a user plays a song in the app, log an event through Firebase and Google Tag Manager using the Firebase analytics event name that matches the tag’s trigger name, played song:

- swift
 
- objective-c

```

1
2
3

```
 | 
```
let parameters: [String: Any] = ["genre": "pop",
 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)

```
 | 

```

1
2
3

```
 | 
```
NSDictionary *parameters = @{@"genre" : @"pop",
 @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];

```
 | 

### Step 2: Log custom attributes

Custom attributes are set via an actionType set to customAttribute. The Braze custom tag provider is expecting the custom attribute key-value to be set via customAttributeKey and customAttributeValue:

- swift
 
- objective-c

```

1
2
3

```
 | 
```
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)

```
 | 

```

1
2
3

```
 | 
```
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
 @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];

```
 | 

### Step 3: Call changeUser()

Calls to changeUser() are made via an actionType set to changeUser. The Braze custom tag provider is expecting the Braze user ID to be set via an externalUserId key-value pair within your tag:

- swift
 
- objective-c

```

1
2

```
 | 
```
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)

```
 | 

```

1
2

```
 | 
```
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];

```
 | 

### Step 4: Add a custom tag provider

With the tags and triggers set up, you will also need to implement Google Tag Manager in your iOS app which can be found in Google’s documentation.

After Google Tag Manager is installed in your app, add a custom tag provider to call Braze SDK methods based on the tags you’ve configured within Google Tag Manager.

Be sure to note the “Class Path” to the file - this is what you’ll enter when setting up a tag in the Google Tag Manager console.

This example highlights one of many ways you can structure your custom tag provider. Specifically, it shows how to determine which Braze SDK method to call based on the actionType key-value pair sent from the GTM Tag. This example assumes you’ve assigned the Braze instance as a variable in the AppDelegate.

The actionType supported in this example are logEvent, customAttribute, and changeUser, but you may prefer to change how your tag provider handles data from Google Tag Manager.

- swift
 
- objective-c

Add the following code to your BrazeGTMTagManager.swift file.

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
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69

```
 | 
```
import FirebaseAnalytics
import GoogleTagManager
import BrazeKit

let ActionTypeKey: String = "actionType"

// Custom Events
let LogEventAction: String = "logEvent"
let LogEventName: String = "eventName"

// Custom Attributes
let CustomAttributeAction: String = "customAttribute"
let CustomAttributeKey: String = "customAttributeKey"
let CustomAttributeValueKey: String = "customAttributeValue"

// Change User
let ChangeUserAction: String = "changeUser"
let ChangeUserExternalUserId: String = "externalUserId"

@objc(BrazeGTMTagManager)
final class BrazeGTMTagManager : NSObject, TAGCustomFunction {
 @objc func execute(withParameters parameters: [AnyHashable : Any]!) -> NSObject! {
 var parameters: [String : Any] = parameters as! [String : Any]
 guard let actionType: String = parameters[ActionTypeKey] as? String else {
 print("There is no Braze action type key in this call. Doing nothing.")
 return nil
 }
 parameters.removeValue(forKey: ActionTypeKey)
 if actionType == LogEventAction {
 logEvent(parameters: parameters)
 } else if actionType == CustomAttributeAction {
 logCustomAttribute(parameters: parameters)
 } else if actionType == ChangeUserAction {
 changeUser(parameters: parameters)
 }
 return nil
 }
 
 func logEvent(parameters: [String : Any]) {
 var parameters: [String : Any] = parameters
 guard let eventName: String = parameters[LogEventName] as? String else { return }
 parameters.removeValue(forKey: LogEventName)
 AppDelegate.braze?.logCustomEvent(name: eventName, properties: parameters)
 }
 
 func logCustomAttribute(parameters: [String: Any]) {
 guard let customAttributeKey = parameters[CustomAttributeKey] as? String else { return }
 let customAttributeValue = parameters[CustomAttributeValueKey]
 
 if let customAttributeValue = customAttributeValue as? String {
 AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
 } else if let customAttributeValue = customAttributeValue as? Date {
 AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
 } else if let customAttributeValue = customAttributeValue as? Double {
 AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
 } else if let customAttributeValue = customAttributeValue as? Bool {
 AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
 } else if let customAttributeValue = customAttributeValue as? Int {
 AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
 } else if let customAttibuteValue = customAttributeValue as? [String] {
 AppDelegate.braze?.user.setCustomAttributeArray(key: customAttributeKey, array: customAttibuteValue)
 }
 }
 
 func changeUser(parameters: [String: Any]) {
 guard let userId = parameters[ChangeUserExternalUserId] as? String else { return }
 AppDelegate.braze?.changeUser(userId: userId)
 }
}

```
 | 

Add the following code to your BrazeGTMTagManager.h file:

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
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end

```
 | 

And add the following code to your BrazeGTMTagManager.m file:

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
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90

```
 | 
```
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "BrazeKit"
#import "AppDelegate.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventAction = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeAction = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserAction = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
 NSMutableDictionary *mutableParameters = [parameters mutableCopy];
 
 NSString *actionType = mutableParameters[ActionTypeKey];
 if (!actionType) {
 NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
 return nil;
 }
 
 [mutableParameters removeObjectForKey:ActionTypeKey];
 
 if ([actionType isEqualToString:LogEventAction]) {
 [self logEvent:mutableParameters];
 } else if ([actionType isEqualToString:CustomAttributeAction]) {
 [self logCustomAttribute:mutableParameters];
 } else if ([actionType isEqualToString:ChangeUserAction]) {
 [self changeUser:mutableParameters];
 } else {
 NSLog(@"Invalid action type. Doing nothing.");
 }
 return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
 NSString *eventName = parameters[LogEventEventName];
 [parameters removeObjectForKey:LogEventEventName];
 [AppDelegate.braze logCustomEvent:eventName
 properties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
 NSString *customAttributeKey = parameters[CustomAttributeKey];
 id customAttributeValue = parameters[CustomAttributeValueKey];
 
 if ([customAttributeValue isKindOfClass:[NSString class]]) {
 [AppDelegate.braze logCustomEvent:customAttributeKey
 properties:parameters];
 } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
 [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
 dateValue:customAttributeValue];
 } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
 if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
 [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
 boolValue:[(NSNumber *)customAttributeValue boolValue]];
 } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
 strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
 strcmp([customAttributeValue objCType], @encode(long)) == 0) {
 [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
 intValue:[(NSNumber *)customAttributeValue integerValue]];
 } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
 strcmp([customAttributeValue objCType], @encode(double)) == 0) {
 [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
 doubleValue:[(NSNumber *)customAttributeValue doubleValue]];
 } else {
 NSLog(@"Could not map NSNumber value to Braze custom attribute:%@", customAttributeValue);
 }
 } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
 [AppDelegate.braze.user setCustomAttributeArrayWithKey:customAttributeKey
 array:customAttributeValue];
 }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
 NSString *userId = parameters[ChangeUserExternalUserId];
 [AppDelegate.braze changeUser:userId];
}

@end

```
 | 

## Troubleshooting

### Web SDK sessions attributed to the wrong user

If GTM fires Braze initialization or event tags before your app identifies the signed-in user, sessions and events may attach to the wrong profile. Initialize the Web SDK, call changeUser() with the signed-in user’s external_id, and then call openSession() before any tags that log events or set attributes. Use GTM tag sequencing or consent triggers so Braze tags run only after your authentication flow completes.

### Web SDK console logging with Shopify or script-tag installs

The Shopify app embed loads the Web SDK with console logging turned off. Set logging in your GTM Initialization tag or initialize() options. The Braze dashboard does not include a logging control for these loaders.

If Braze logs appear in the browser console, remove enableLogging: true from the GTM Initialization tag or custom HTML before you publish to production. After initialization, use toggleLogging() or the ?brazeLogging=true URL parameter. For the full Web SDK options, see Verbose logging.

If Braze does not initialize or events do not appear as expected, confirm your GTM container is published, triggers and tag firing order align with your SDK lifecycle and initialization strategy, and that test devices are not blocking Braze endpoints.

For initialization failures, verify the Braze tag or custom tag provider receives the expected actionType and parameters (see the Android, Swift, and Web tabs on this page). For verbose logging while validating GTM-fired events, enable your platform’s SDK debug logging as described in the platform integration guides linked from those tabs.

- 

New Stuff!
