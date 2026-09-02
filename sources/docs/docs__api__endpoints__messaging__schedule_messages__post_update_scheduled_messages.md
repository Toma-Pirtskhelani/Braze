---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages
slug: docs__api__endpoints__messaging__schedule_messages__post_update_scheduled_messages
title: "Update scheduled messages"
description: "This article outlines details about the Update scheduled messages Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update scheduled messages

post

/messages/schedule/update

core endpoint

Use this endpoint to update scheduled messages.

This endpoint accepts updates to either the schedule or messages parameter or both. Your request must contain at least one of those two keys.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the messages.schedule.update permission.

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
8
9

```
 | 
```
{
 "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
 "schedule": {
 // optional, see create schedule documentation
 },
 "messages": {
 // optional, see available messaging objects documentation
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 schedule_id | 
 Required | 
 String | 
 The schedule_id to update (obtained from the response to create schedule). | 

 schedule | 
 Optional | 
 Object | 
 See schedule object. | 

 messages | 
 Optional | 
 Object | 
 See available messaging objects. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "schedule_id": "schedule_identifier",
 "schedule": {
 "time": "2017-05-24T20:30:36Z"
 },
 "messages": {
 "apple_push": {
 "alert": "Updated Message!",
 "badge": 1
 },
 "android_push": {
 "title": "Updated title!",
 "alert": "Updated message!"
 },
 "sms": {
 "subscription_group_id": "subscription_group_identifier",
 "message_variation_id": "message_variation_identifier",
 "body": "This is my SMS body.",
 "app_id": "app_identifier"
 }
 }
}'

```
 | 

- 

New Stuff!
