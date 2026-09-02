---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs
slug: docs__user_guide__messaging__design_and_edit__personalize__sources__key_value_pairs
title: "Key-value pairs"
description: "This reference article covers key-value pairs and how to use them to send extra data payloads to user devices."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Key-value pairs

This page covers how to use key-value pairs to send extra data payloads to user devices. This feature is available across push, in-app, email, and Content Card messaging channels.

Use key-value pairs to add structured metadata to messages. These extra data payloads can enrich messages with additional contextual information that can influence how a message is rendered or processed.

Because key-value pairs are metadata, this data isn’t necessarily visible to the recipient, but can be used by your connected systems or processes to customize message handling.

Each pair consists of:

- Key: The identifier (Example: utm_source)
 
- Value: The associated data (Example: newsletter)

## Use cases

Here are some example use cases for adding metadata with key-value pairs:

- Tracking parameters: Attaching UTM parameters for analytics purposes

- Key: utm_campaign
 
- Value: spring_sale

- Custom tags: Adding tags for internal routing or categorization

- Key: priority
 
- Value: high

- Behavior triggers: Metadata used to trigger or customize in-app behaviors

- Key: deep_link
 
- Value: app://promo-page

## Push notifications

Key-value pairs can be added to Android, iOS, and web push notifications. You might use key-value pairs to update internal metrics and app content or customize push notification properties, such as alert prioritization, localization, and sounds.

In the message composer, select the Settings tab, select Add New Pair, and specify your key-value pairs.

When you add key-value pairs in the message composer, values are sent as strings. For iOS push, reserved Apple Push Notification service (APNs) alert keys you add through Alert Options (such as loc-args for localization arguments) are formatted with the correct JSON types in the payload. For custom keys, your app receives string values unless you parse them in your integration.

### iOS

Apple Push Notification service (APNs) supports setting alert preferences and sending custom data using key-value pairs. APNs makes use of the Apple-reserved aps library, which includes predetermined keys and values that govern alert properties.

#### APS library

 Key | 
 Value Type | 
 Value Description | 

 alert | 
 string or dictionary object | 
 For string inputs, displays an alert with the string as the message with Close and View buttons; for non-string inputs, displays an alert or banner depending on the input’s child properties | 

 badge | 
 number | 
 Governs the number that is displayed as the badge on the app icon | 

 sound | 
 string | 
 The name of the sound file to play as an alert; must be in the app’s bundle or Library/Sounds folder | 

 content-available | 
 number | 
 Input values of 1 signal to the app the availability of new information upon launch or session resumption | 

##### Alert properties library

 Key | 
 Value Type | 
 Value Description | 

 title | 
 string | 
 A short string that Apple Watch displays briefly as part of a notification | 

 body | 
 string | 
 The push notification’s content | 

 title-loc-key | 
 string or null | 
 A key that sets the title string for the current localization from the Localizable.strings file | 

 title-loc-args | 
 array of strings or null | 
 String values that can appear in place of the title localization format specifiers in title-loc-key | 

 action-loc-key | 
 array of string or null | 
 If present, the specified string sets the localization for the Close and View buttons | 

 loc-key | 
 string or null | 
 A key that sets the notification message for the current localization from the Localizable.strings file | 

 loc-args | 
 array of strings | 
 String values that can appear in place of the localization format specifiers in loc-key | 

 launch-image | 
 strings | 
 The name of an image file in the app bundle you wish to be used as the launch image when users tap the action button or move the action slide | 

The Braze message composer automatically handles the creation of the following keys: alert and its properties, content-available, sound, and category.

These values can be input in the Settings tab when building a push message. Select Alert Options and select an alert dictionary key for the key to be automatically populated in a new key-value entry.

When Braze sends a push notification to APNs, the payload will be formatted as a JSON.

Simple Payload

```

1
2
3

```
 | 
```
{
 "aps" : { "alert" : "Message received from Spencer" },
}

```
 | 

Complex Payload

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

```
 | 
```
{
 "aps" : {
 "alert" : {
 "body" : "Hi, welcome to our app!",
 "loc-key" : "France",
 "loc-args" : ["Bonjour", "bienvenue"],
 "action-loc-key" : "Button_Type_1",
 "launch-image" : "Paris"
 },
 "content-available" : 1
 },
}

```
 | 

##### Custom key-value pairs

In addition to the aps library payload values, you may send custom key-value pairs to a user’s device. The values in these pairs are restricted to primitive types: dictionary (object), array, string, number, and boolean.

Use cases for custom key-value pairs include but are not limited to internal metrics keeping and setting the context for the user interface. Braze allows you to send additional key-value pairs along with a push notification to be used through your application within the extras key. If you prefer to use another key, confirm that your app can handle this custom key.

warning

You should avoid handling a top-level key or dictionary called ab in your application.

Apple advises clients to avoid including customer information or any sensitive data as custom payload data. Furthermore, Apple recommends that any action associated with an alert message should not delete data on a device.

warning

If you’re using the HTTP/2 provider API, any individual payload you send to APNs cannot exceed a size of 4096 bytes. The legacy binary interface, which will soon be depreciated, only supports a payload size of 2048 bytes.

###### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as extras. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as “example_key”, and a value as "$json:{"foo": 1, "bar": 1}". This will result in a developer console output of "extras": { "test": { "foo": 1, "bar": 1 }

### Android

Braze allows you to send send additional data payloads in push notifications using key-value pairs.

#### Data payload

Similar to iOS push, you may send custom key-value pairs to a user’s device.

Some use cases for custom key-value pairs include internal metrics keeping and setting the context for the user interface, but they may be used for whatever purpose you choose.

important

Your app’s backend must be able to process custom key-value pairs for the data payload to function properly.

##### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as extras. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as “example_key”, and a value as "$json:{"foo": 1, "bar": 1}". This will result in a developer console output of "extras": { "test": { "foo": 1, "bar": 1 }.

##### FCM messaging options

Android push notifications can be further customized with FCM message options. These include notification priority, sound, delay, lifespan, and collapsibility. These values can be specified in the Settings tab when creating a push message. Refer to Advanced push notification settings for further instructions on how to set these options in the Braze message composer.

### Silent push notifications

A silent push notification is a push notification containing no alert message or sound, used to update your app’s interface or content in the background. These notifications make use of key-value pairs to trigger these background app actions. Silent push notifications also power our uninstall tracking.

Marketers should test that silent push notifications trigger expected behavior before sending them to their app’s users. After you compose your iOS or Android silent push notification, ensure that you only target a test user by filtering on external user ID or email address.

Upon campaign launch, you should check that you have not received any visible push notification on your test device.

note

iOS silent-notification gating may cause the following symptoms:

- Lower-than-expected uninstall tracking metrics for iOS users
 
- Inconsistent or delayed delivery of silent push notifications
 
- Push Stories that don’t display
 
- Push Stories that arrive without their expected images, video, or pages

This is an Apple platform limitation rather than a Braze issue. iOS may delay or drop background notifications for some Braze features, including uninstall tracking and Push Stories. For details on what iOS gates and when, see iOS limitations.

## In-app messages

You can add a key-value pair to an in-app message in the traditional editor by selecting the Settings tab, selecting Add New Pair, and then specifying your key-value pairs.

note

Key-value pairs cannot be set through the drag-and-drop editor for in-app messages.

### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as extras. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as “example_key”, and a value as "$json:{"foo": 1, "bar": 1}". This will result in a developer console output of "extras": { "test": { "foo": 1, "bar": 1 }.

## Emails

Both SparkPost and SendGrid support key-value pairs in emails. If you use SendGrid, key-value pairs will be sent as unique arguments. SendGrid allows you to attach an unlimited number of key-value pairs up to 10,000 bytes of data. These key-value pairs can be seen in posts from the SendGrid Event Webhook.

note

Bounced emails will not deliver key-value pairs to SparkPost or SendGrid.

## Content Cards

To add a key-value pair to a Content Card, go to the Settings tab in the Braze message composer and select Add New Pair.

note

Control variants do not support key-value pairs. If you need to capture analytics for control groups in A/B tests, create a message variant with a key-value pair such as control=true and hide it in your app code while logging impressions.

- 

New Stuff!
