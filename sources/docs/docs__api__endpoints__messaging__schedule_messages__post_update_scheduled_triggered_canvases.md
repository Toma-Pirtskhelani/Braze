---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases
slug: docs__api__endpoints__messaging__schedule_messages__post_update_scheduled_triggered_canvases
title: "Update scheduled API-triggered Canvases"
description: "This article outlines details about the Update scheduled API-triggered Canvases Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update scheduled API-triggered Canvases

post

/canvas/trigger/schedule/update

core endpoint

Use this endpoint to update scheduled API-triggered Canvases that were created in the dashboard.

This allows you to decide what action triggers the message to send. You can pass in trigger_properties that Braze templates into the message itself.

Note that to send messages with this endpoint, you must have a Canvas ID, created when you build a Canvas.

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests.

- For example, if you originally provide "schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true} and then in your update you provide "schedule" : {"time" : "2015-02-20T14:14:47"}, Braze sends your message at the provided time in UTC, not in the user’s local time.
 
- Scheduled triggers that you update close to or during the time they were supposed to send are updated with best efforts, so Braze may apply last-second changes to all, some, or none of your targeted users.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the canvas.trigger.schedule.update permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY

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
{
 "canvas_id": (required, string) see Canvas identifier,
 "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
 "schedule": {
 // required, see create schedule documentation
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 canvas_id | 
 Required | 
 String | 
 See Canvas identifier. | 

 schedule_id | 
 Optional | 
 String | 
 The schedule_id to update (obtained from the response to create schedule). | 

 schedule | 
 Required | 
 Object | 
 See schedule object. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "canvas_id": "canvas_identifier",
 "schedule_id": "schedule_identifier",
 "schedule": {
 "time": "2017-05-24T21:30:00Z",
 "in_local_time": true
 }
}'

```
 | 

- 

New Stuff!
