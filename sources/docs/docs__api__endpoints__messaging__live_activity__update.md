---
url: https://www.braze.com/docs/api/endpoints/messaging/live_activity/update
slug: docs__api__endpoints__messaging__live_activity__update
title: "Update Live Activity"
description: "This article outlines details about the Update Live Activity endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update Live Activity

post

/messages/live_activity/update

Use this endpoint to update and end Live Activities displayed by your iOS app. This endpoint requires additional setup.

After you register a Live Activity, you can pass a JSON payload to update your Apple Push Notification service (APNs). See Apple’s documentation on updating your Live Activity with push notification payloads for more information.

If content-available isn’t set, the default Apple Push Notification service (APNs) priority is 10. If content-available is set, this priority is 5. Refer to Apple push object for more details.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need to complete the following:

- Generate an API key with the messages.live_activity.update permission.
 
- Register a Live Activity remotely or locally using the Braze Swift SDK.

important

If the final rendered payload is larger than the corresponding service’s maximum allowed size, the send won’t be successful.

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

```
 | 
```
{
 "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
 "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
 "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
 "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
 "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
 "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
 "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
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
 When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string.

Set activity_id to this custom string to define which Live Activity you want to update. | 

 content_state | 
 Required | 
 Object | 
 You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object.

The format of this request must match the shape you initially defined. | 

 end_activity | 
 Optional | 
 Boolean | 
 If true, this request ends the Live Activity. | 

 dismissal_date | 
 Optional | 
 Datetime 
(ISO-8601 string) | 
 This parameter defines the time to remove the Live Activity from the user’s UI. If this time is in the past and end_activity is true, the Live Activity will be removed immediately.

 If end_activity is false or omitted, this parameter only updates the Live Activity. | 

 stale_date | 
 Optional | 
 Datetime 
(ISO-8601 string) | 
 This parameter tells the system when the Live Activity content is marked as outdated in the user’s UI. | 

 notification | 
 Optional | 
 Object | 
 Include an apple_push object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. 
- If a notification is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI will slide down and display like a push notification.
- If a notification is included and the user is not active on their iPhone, their screen will light up to display the updated Live Activity UI on their lock screen.
- The notification alert will not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the alert will be displayed there. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
 "app_id": "{YOUR-APP-API-IDENTIFIER}",
 "activity_id": "live-activity-1",
 "content_state": {
 "teamOneScore": 2,
 "teamTwoScore": 4
 },
 "end_activity": false,
 "dismissal_date": "2023-02-28T00:00:00+0000",
 "stale_date": "2023-02-27T16:55:49+0000",
 "notification": {
 "alert": {
 "body": "It's halftime! Let's look at the scores",
 "title": "Halftime"
 }
 }
}'

```
 | 

## Response

There are two status code responses for this endpoint: 201 and 4XX.

### Example success response

A 201 status code is returned if the request was formatted correctly and we received the request. The status code 201 could return the following response body.

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
