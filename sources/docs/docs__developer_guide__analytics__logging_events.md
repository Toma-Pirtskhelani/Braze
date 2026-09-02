---
url: https://www.braze.com/docs/developer_guide/analytics/logging_events
slug: docs__developer_guide__analytics__logging_events
title: "Log custom events"
description: "Learn how to log custom events through the Braze SDK."
section: developer_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Log custom events

Learn how to log custom events through the Braze SDK.

note

For wrapper SDKs not listed, use the relevant native Android or Swift method instead.

For eCommerce recommended events, see Log eCommerce events.

## Logging a custom event

To log a custom event, use the following event-logging method.

- web
 
- android
 
- swift
 
- flutter
 
- cordova
 
- infillion
 
- react native
 
- roku
 
- unity

For a standard Web SDK implementation, you can use the following method:

```

1

```
 | 
```
braze.logCustomEvent("YOUR_EVENT_NAME");

```
 | 

If you’d like to use Google Tag Manager instead, you can use the Custom Event tag type to call the logCustomEvent method and send custom events to Braze, optionally including custom event properties. To do this:

- Enter the Event Name by either using a variable or typing an event name.
 
- Use the Add Row button to add event properties.

For native Android, you can use the following method:

- java
 
- kotlin

```

1

```
 | 
```
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);

```
 | 

```

1

```
 | 
```
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)

```
 | 

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")

```
 | 

```

1

```
 | 
```
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];

```
 | 

```

1

```
 | 
```
braze.logCustomEvent('YOUR_EVENT_NAME');

```
 | 

Use the Braze Cordova plugin method:

```

1

```
 | 
```
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");

```
 | 

The logCustomEvent API accepts:

- eventName (required string): Use up to 255 characters. Do not start the name with $. Use alphanumeric characters and punctuation.
 
- eventProperties (optional object): Add key-value pairs for event metadata. Use keys up to 255 characters, and do not start keys with $.

For property values, use string (up to 255 characters), numeric, boolean, arrays, or nested JSON objects.

For implementation details, see the Braze Cordova SDK source:

- www/BrazePlugin.js logCustomEvent method (lines 138-140)
 
- www/BrazePlugin.js JSDoc (lines 128-140)
 
- Android handler in src/android/BrazePlugin.kt (lines 108-115)
 
- iOS handler in src/ios/BrazePlugin.m (lines 308-313)
 
- iOS method declaration in src/ios/BrazePlugin.h (line 24)

If you’ve integrated Infillion Beacons into your Android app, you can optionally use visit.getPlace() to log location-specific events. requestImmediateDataFlush verifies that your event will log even if your app is in the background.

- java
 
- kotlin

```

1
2

```
 | 
```
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();

```
 | 

```

1
2

```
 | 
```
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()

```
 | 

```

1

```
 | 
```
Braze.logCustomEvent("YOUR_EVENT_NAME");

```
 | 

```

1

```
 | 
```
m.Braze.logEvent("YOUR_EVENT_NAME")

```
 | 

```

1

```
 | 
```
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");

```
 | 

## Adding metadata properties

When you log a custom event, you have the option to add metadata about that custom event by passing a properties object with the event. Properties are defined as key-value pairs. Keys are strings and values can be string, numeric, boolean, Date objects, arrays, or nested JSON objects.

To add metadata properties, use the following event-logging method.

- web
 
- android
 
- swift
 
- flutter
 
- cordova
 
- react native
 
- roku
 
- unity

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
braze.logCustomEvent("YOUR-EVENT-NAME", {
 you: "can", 
 pass: false, 
 orNumbers: 42,
 orDates: new Date(),
 or: ["any", "array", "here"],
 andEven: {
 deeply: ["nested", "json"]
 }
});

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

```
 | 
```
Braze.logCustomEvent("YOUR-EVENT-NAME",
 new BrazeProperties(new JSONObject()
 .put("you", "can")
 .put("pass", false)
 .put("orNumbers", 42)
 .put("orDates", new Date())
 .put("or", new JSONArray()
 .put("any")
 .put("array")
 .put("here"))
 .put("andEven", new JSONObject()
 .put("deeply", new JSONArray()
 .put("nested")
 .put("json"))
 )
));

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

```
 | 
```
Braze.logCustomEvent("YOUR-EVENT-NAME",
 BrazeProperties(JSONObject()
 .put("you", "can")
 .put("pass", false)
 .put("orNumbers", 42)
 .put("orDates", Date())
 .put("or", JSONArray()
 .put("any")
 .put("array")
 .put("here"))
 .put("andEven", JSONObject()
 .put("deeply", JSONArray()
 .put("nested")
 .put("json"))
 )
))

```
 | 

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
12
13

```
 | 
```
AppDelegate.braze?.logCustomEvent(
 name: "YOUR-EVENT-NAME",
 properties: [
 "you": "can",
 "pass": false,
 "orNumbers": 42,
 "orDates": Date(),
 "or": ["any", "array", "here"],
 "andEven": [
 "deeply": ["nested", "json"]
 ]
 ]
)

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

```
 | 
```
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
 properties:@{
 @"you": @"can",
 @"pass": @(NO),
 @"orNumbers": @42,
 @"orDates": [NSDate date],
 @"or": @[@"any", @"array", @"here"],
 @"andEven": @{
 @"deeply": @[@"nested", @"json"]
 }
}];

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
braze.logCustomEvent('custom_event_with_properties', properties: {
 'key1': 'value1',
 'key2': ['value2', 'value3'],
 'key3': false,
});

```
 | 

Log custom events with a properties object:

```

1
2
3
4
5

```
 | 
```
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);

```
 | 

You can also pass properties inline:

```

1
2
3
4

```
 | 
```
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
 "key": "value",
 "amount": 42,
});

```
 | 

The official Cordova sample app includes string, numeric, boolean, array, and nested object properties:

- sample-project/www/js/index.js (lines 230-251)

Sample project excerpt:

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

```
 | 
```
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
 "Cart Value": 4.95,
 "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
 "array key": [1, "2", false],
 "object key": {
 "k1": "1",
 "k2": 2,
 "k3": false,
 },
 "deep key": {
 "key": [1, "2", true]
 }
});

```
 | 

For API and native bridge details, see:

- www/BrazePlugin.js JSDoc (lines 128-140)
 
- Android handler in src/android/BrazePlugin.kt (lines 108-115)
 
- iOS handler in src/ios/BrazePlugin.m (lines 308-313)

```

1
2
3
4
5

```
 | 
```
Braze.logCustomEvent("custom_event_with_properties", {
 key1: "value1",
 key2: ["value2", "value3"],
 key3: false,
});

```
 | 

```

1

```
 | 
```
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})

```
 | 

```

1

```
 | 
```
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));

```
 | 

important

The time and event_name keys are reserved and cannot be used as custom event properties.

## Best practices

There are three important checks to carry out so that your custom event properties log as expected:

- Establish which events are logged
 
- Verify log
 
- Verify values

Multiple properties may be logged each time a custom event is logged.

### Verify events

Check with your developers which event properties are being tracked. Keep in mind that all event properties are case-sensitive. For additional information on tracking custom events, check out these articles based on your platform:

- Android
 
- iOS
 
- Web

### Verify log

To confirm that the event properties are successfully tracked, you can view all event properties from the Custom Events page.

- Go to Data Settings > Custom Events.
 
- Locate your custom event from the list.
 
- For your event, select Manage Properties to view the names of the properties associated with an event.

### Verify values

After adding your user as a test user, follow these steps to verify your values:

- Perform the custom event within the app.
 
- Wait for roughly 10 seconds for the data to flush.
 
- Refresh the Event User Log to view the custom event and the event property value that was passed with it.

## Troubleshooting custom events

Use these scenarios to troubleshoot custom event logging across SDKs.

### Verifying the custom event trigger

If a custom event doesn’t appear, the tracked action in your app may not match the action you’re testing.

- Confirm with your developer team which app action triggers the custom event.
 
- Check for deprecated code paths after SDK upgrades, such as references to appboy instead of braze.

### Custom events are logged to an anonymous profile

If you don’t identify a user before logging a custom event, Braze can associate that event with an anonymous profile.

- Call changeUser() before performing the custom event so Braze logs it to an identified user profile.
 
- Test with an identified test user, then review the Event User Log.

### Verifying custom event logging setup

If custom events aren’t appearing as expected, confirm that your developer team has implemented custom event logging for the right app action.

- Ask your developer team to verify that the event is logged correctly and triggered from the expected user action.
 
- When your team opens a ticket with Braze Support, include verbose logs and relevant code snippets.
 
- If your app uses Swift or Android, your developer team can use the SDK debugger prerequisites to help generate verbose logs.
 
- If your developer team can’t identify the issue, open a Braze Support ticket.

- 

New Stuff!
