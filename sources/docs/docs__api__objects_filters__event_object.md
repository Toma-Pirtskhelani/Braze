---
url: https://www.braze.com/docs/api/objects_filters/event_object
slug: docs__api__objects_filters__event_object
title: "Event object"
description: "This reference article goes over the event object, what it is, and how it's a crucial part of event-based campaign strategies."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# Event object

This article explains the different components of an event object, how you can use this object, and examples to draw from.

## What is an event object?

An event object is an object that gets passed through the API when a specific event occurs. Events objects are housed in an events array. Each event object in the events array represents a single occurrence of a custom event by a particular user at the designated time value. The event object has many different fields that allow you to customize by setting and using event properties in messages, data collection, and personalization.

For steps on how to set up custom events for a specific platform, refer to the Platform Integration Guide in the Developer Guide. Refer to the relevant article based on your platform:

- Android
 
- iOS
 
- Web

### Object body

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
{
 // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
 "external_id" : (optional, string) External user ID,
 "user_alias" : (optional, User Alias Object) User alias object,
 "braze_id" : (optional, string) Braze user identifier,
 "email": (optional, string) User email address,
 "phone": (optional, string) User phone number,
 "app_id" : (optional, string) see App Identifier,
 "name" : (required, string) the name of the event,
 "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
 "properties" : (optional, Properties Object) properties of the event
 // Setting this flag to true will put the API in "Update Only" mode.
 // When using a "user_alias", "Update Only" mode is always true.
 "_update_existing_only" : (optional, boolean)
 // See following notes regarding anonymous push token imports
}

```
 | 

note

Events with timestamps in the future default to the current time. This ensures that custom events are recorded with accurate timing.

- External user ID
 
- App identifier
 
- ISO 8601 time code

note

Some identifier pairs can’t be used together in a single request. When both email and phone are provided, email takes precedence over phone. For full details, refer to Identifier resolution.

#### Update existing profiles only

To update only existing user profiles in Braze, you should pass the _update_existing_only key with a value of true within the body of your request. If this value is omitted, Braze will create a new user profile if the external_id does not already exist.

note

If you’re creating an alias-only user profile through the /users/track endpoint, _update_existing_only must be set to false. If this value is omitted, the alias-only profile will not be created.

## Event properties object

Custom events and purchases may have event properties. The “properties” values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs ($).

Property values can be any of the following data types:

 Data Type | 
 Description | 

 Numbers | 
 As either integers or floats | 

 Booleans | 
 true or false | 

 Datetimes | 
 Must be formatted as strings in the ISO 8601 format or in any of the following formats: 
- yyyy-MM-ddTHH:mm:ss:SSSZ 
- yyyy-MM-ddTHH:mm:ss 
- yyyy-MM-dd HH:mm:ss 
- yyyy-MM-dd 
- MM/dd/yyyy 
- ddd MM dd HH:mm:ss.TZD YYYY 

Not supported within arrays. 

Note that “T” is a time designator, not a placeholder, and should not be changed or removed. 

Time attributes without a time zone will default to midnight UTC (and will be formatted on the dashboard as the equivalent of midnight UTC in the company’s time zone). 

 Events with timestamps in the future will default to the current time. | 

 Strings | 
 255 characters or fewer. | 

 Arrays | 
 Arrays cannot include datetimes. | 

 Objects | 
 Objects will be ingested as strings. | 

Event property objects that contain array or object values can have an event property payload of up to 100 KB.

### Reserved keys

The following keys are reserved and cannot be used as custom event properties:

- time
 
- event_name

important

Using reserved keys as custom event property names will result in API errors when sending requests to the /users/track endpoint.

### Event property persistence

Event properties are designed for filtering of, and Liquid personalization in, messages triggered by their parent events. By default, they are not persisted on the Braze user profile. To use event property values in segmentation, refer to custom events, which details the various approaches to storing event property values long-term.

#### Event example request

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

```
 | 
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
 "events" : [
 {
 "external_id" : "user1",
 "app_id" : "your-app-id",
 "name" : "watched_trailer",
 "time" : "2013-07-16T19:20:30+01:00"
 },
 {
 "external_id" : "user1",
 "app_id" : "your-app-id",
 "name" : "rented_movie",
 "time" : "2013-07-16T19:20:45+01:00",
 "properties": {
 "movie": "The Sad Egg",
 "director": "Alex Smith"
 }
 },
 {
 "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
 "app_id" : "your-app-id",
 "name" : "watched_trailer",
 "time" : "2013-07-16T19:20:50+01:00"
 }
 ]
}

```
 | 

- ISO 8601 Time Code Wiki

## Event objects

Using the example provided, we can see that someone watched a trailer recently, and then rented a movie. While we cannot go into a campaign and segment the users based on these properties, we can use these properties strategically by using them in the form of a receipt, to send a custom message through a channel using Liquid. For example, “Hello Alex, Thanks for renting The Sad Egg by Alex Smith, here are some recommended movies based on your rental…”

- 

New Stuff!
