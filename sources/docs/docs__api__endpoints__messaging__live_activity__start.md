---
url: https://www.braze.com/docs/api/endpoints/messaging/live_activity/start
slug: docs__api__endpoints__messaging__live_activity__start
title: "Start Live Activity"
description: "This article outlines details about the Start Live Activity endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Start Live Activity

post

/messages/live_activity/start

Use this endpoint to remotely start Live Activities displayed in your iOS app. This endpoint requires additional setup.

After you create a Live Activity, make a POST request to target a segment, a connected audience, or specific users. Identify specific users by external user ID, user alias, or both. For more information about Apple’s Live Activities, see Starting and updating Live Activities with ActivityKit push notifications.

If content-available isn’t set, the default Apple Push Notification service (APNs) priority is 10. If content-available is set, this priority is 5. For more information, see Apple push object.

tip

To end a Live Activity, use the /messages/live_activity/update endpoint with end_activity set to true.

## Arranging automatic dismissal

To arrange automatic dismissal after a Live Activity starts, schedule a follow-up request to the update endpoint from your backend.

- Send a /messages/live_activity/start request with an activity_id you can reuse later.
 
- Store that activity_id and your target end time in your backend scheduler.
 
- At the target end time, send a /messages/live_activity/update request with end_activity set to true.
 
- Configure dismissal behavior in the same update request. For details, see the /messages/live_activity/update endpoint.
 
- Verify send and outcome events in the Message Activity Log.

See me in Postman

## Prerequisites

To use this endpoint, complete the following prerequisites:

- Generate an API key with the messages.live_activity.start permission.
 
- Create a Live Activity using the Braze Swift SDK.

important

If the final rendered payload is larger than the corresponding service’s maximum allowed size, the send won’t be successful.

important

When you target specific users, Braze starts a Live Activity only for external_user_ids and user_aliases that resolve to existing users.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request body

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
{
 "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
 "activity_id": "(required, string) Define a custom string as your `activity_id`. Use this ID to send update or end events to your Live Activity.",
 "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app.",
 "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
 "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
 "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
 "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Include `notification.alert.title` and `notification.alert.body`.",
 // Include one targeting method:
 // 1. "external_user_ids", "user_aliases", or both (combined maximum 50)
 // 2. "custom_audience"
 // 3. "segment_id"
 "external_user_ids": "(optional, array of strings) see external user identifier",
 "user_aliases": "(optional, array of user alias objects) see user alias object",
 "custom_audience": "(optional, connected audience object) see connected audience",
 "segment_id": "(optional, string) see segment identifier"
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 app_id | 
 Required | 
 String | 
 App API identifier retrieved from the API Keys page. | 

 activity_id | 
 Required | 
 String | 
 Define a custom string as your activity_id. Use this ID to send update or end events to your Live Activity. | 

 activity_attributes_type | 
 Required | 
 String | 
 The activity attributes type you define within liveActivities.registerPushToStart in your app. | 

 activity_attributes | 
 Required | 
 Object | 
 The static attribute values for the activity type (such as the sports team names, which don’t change). | 

 content_state | 
 Required | 
 Object | 
 You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object.

The format of this request must match the shape you initially defined. | 

 stale_date | 
 Optional | 
 Datetime 
(ISO-8601 string) | 
 This parameter tells the system when the Live Activity content is marked as outdated in the user’s UI. | 

 notification | 
 Required | 
 Object | 
 Include an apple_push object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. 
- If a notification is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI slides down and displays like a push notification.
- If a notification is included and the user is not active on their iPhone, their screen lights up to display the updated Live Activity UI on their lock screen.
- The notification alert does not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the alert displays there. | 

 external_user_ids | 
 Optional if user_aliases, segment_id, or custom_audience is provided | 
 Array of strings | 
 See external user ID. | 

 user_aliases | 
 Optional if external_user_ids, segment_id, or custom_audience is provided | 
 Array of user alias objects | 
 See user alias object. | 

 segment_id | 
 Optional if external_user_ids, user_aliases, or custom_audience is provided | 
 String | 
 See segment identifier. | 

 custom_audience | 
 Optional if external_user_ids, user_aliases, or segment_id is provided | 
 Connected audience object | 
 See connected audience. | 

You can include external_user_ids and user_aliases in the same request. Their combined array length can’t exceed 50. Braze targets users who match either parameter and sends only once when multiple identifiers resolve to the same user.

Don’t combine external_user_ids or user_aliases with segment_id or custom_audience. On this endpoint, use custom_audience to pass connected audience filters.

## Example request

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR_REST_API_KEY}' \
--data-raw '{
 "app_id": "{YOUR_APP_API_IDENTIFIER}",
 "activity_id": "football-chiefs-bills-2024-01-21",
 "content_state": {
 "teamOneScore": 0,
 "teamTwoScore": 0
 },
 "activity_attributes_type": "FootballActivity",
 "activity_attributes": {
 "team1Name": "Chiefs",
 "team2Name": "Bills"
 },
 "stale_date": "2024-01-22T16:55:49+0000",
 "notification": {
 "alert": {
 "body": "The game is starting! Tune in soon!",
 "title": "Chiefs v. Bills"
 }
 },
 "external_user_ids": ["user-id1", "user-id2"],
 "user_aliases": [
 {
 "alias_name": "user-name",
 "alias_label": "user-label"
 }
 ]
}'

```
 | 

## Response

There are two status code responses for this endpoint: 201 and 4XX.

### Example success response

A 201 status code returns if the request is formatted correctly and Braze receives it. The status code 201 can return the following response body.

```

1
2
3

```
 | 
```
{
 "message": "success"
}

```
 | 

### Example error response

The 4XX class of status code indicates a client error. Refer to the API errors and responses article for more information about errors you may encounter.

The status code 400 could return the following response body.

```

1
2
3

```
 | 
```
{
 "error": "\nProblem:\n message body does not match declared format\nResolution:\n when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}

```
 | 

- 

New Stuff!
