---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages
slug: docs__api__endpoints__messaging__schedule_messages__post_schedule_messages
title: "Create scheduled messages"
description: "This article outlines details about the Create scheduled messages Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create scheduled messages

post

/messages/schedule/create

core endpoint

Use this endpoint to schedule a campaign, Canvas, or other message to be sent at a designated time and provides you with an identifier to reference that message for updates.

If you’re targeting a segment, a record of your request will be stored in the Developer Console after all scheduled messages have been sent.

tip

If you’re interested in sending messages immediately to designated users, use the /messages/send endpoint instead.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the messages.schedule.create permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

Braze endpoints support batching API requests. A single request to the messaging endpoints can reach any of the following:

- Up to 50 specific external_ids, each with individual message parameters
 
- An audience segment of any size, defined in the request as a connected audience object

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
{
 // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
 // Including 'segment_id' will send to members of that segment
 // Including 'external_user_ids' and/or 'user_aliases' will send to those users
 // Including both a Segment and users will send to the provided users if they are in the segment
 "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
 "external_user_ids": (optional, array of strings) see external user identifier,
 "user_aliases": (optional, array of user alias object) see user alias,
 "audience": (optional, connected audience object) see connected audience,
 "campaign_id": (optional, string) see campaign identifier,
 "send_id": (optional, string) see send identifier,
 "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
 "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
 "schedule": {
 "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
 "in_local_time": (optional, bool),
 "at_optimal_time": (optional, bool),
 },
 "messages": {
 "apple_push": (optional, apple push object),
 "android_push": (optional, android push object),
 "kindle_push": (optional, kindle/fireOS push object),
 "web_push": (optional, web push object),
 "email": (optional, email object),
 "webhook": (optional, webhook object),
 "content_card": (optional, content card object),
 "sms": (optional, SMS object)
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 broadcast | 
 Optional | 
 Boolean | 
 You must set broadcast to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false. 

 If broadcast is set to true, a recipients list cannot be included. However, use caution when setting broadcast: true, as unintentionally setting this flag may cause you to send your message to a larger-than-expected audience. | 

 external_user_ids | 
 Optional | 
 Array of strings | 
 See external user identifier. | 

 user_aliases | 
 Optional | 
 Array of user alias objects | 
 See user alias object. | 

 audience | 
 Optional | 
 Connected audience object | 
 See connected audience. | 

 segment_id | 
 Optional | 
 String | 
 See segment identifier. | 

 campaign_id | 
 Optional | 
 String | 
 See campaign identifier. | 

 send_id | 
 Optional | 
 String | 
 See send identifier. | 

 override_messaging_limits | 
 Optional | 
 Boolean | 
 Ignore frequency capping for campaigns, defaults to false | 

 recipient_subscription_state | 
 Optional | 
 String | 
 Use this to send messages to only users who have opted in (opted_in), only users who have subscribed or are opted in (subscribed) or to all users, including unsubscribed users (all). 

Using all users is useful for transactional email messaging. Defaults to subscribed. | 

 schedule | 
 Required | 
 Schedule object | 
 See schedule object | 

 messages | 
 Optional | 
 Messaging object | 
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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
 "broadcast": "false",
 "external_user_ids": "external_user_identifiers",
 "user_aliases": {
 "alias_name" : "example_name",
 "alias_label" : "example_label"
 },
 "segment_id": "segment_identifiers",
 "audience": {
 "AND": [
 {
 "custom_attribute": {
 "custom_attribute_name": "eye_color",
 "comparison": "equals",
 "value": "blue"
 }
 },
 {
 "custom_attribute": {
 "custom_attribute_name": "favorite_foods",
 "comparison": "includes_value",
 "value": "pizza"
 }
 },
 {
 "OR": [
 {
 "custom_attribute": {
 "custom_attribute_name": "last_purchase_time",
 "comparison": "less_than_x_days_ago",
 "value": 2
 }
 },
 {
 "push_subscription_status": {
 "comparison": "is",
 "value": "opted_in"
 }
 }
 ]
 },
 {
 "email_subscription_status": {
 "comparison": "is_not",
 "value": "subscribed"
 }
 },
 {
 "last_used_app": {
 "comparison": "after",
 "value": "2019-07-22T13:17:55+0000"
 }
 }
 ]
 },
 "campaign_id": "campaign_identifier",
 "send_id": "send_identifier",
 "override_messaging_limits": false,
 "recipient_subscription_state": "subscribed",
 "schedule": {
 "time": "",
 "in_local_time": true,
 "at_optimal_time": true
 },
 "messages": {
 "apple_push": (optional, Apple Push Object),
 "android_push": (optional, Android Push Object),
 "kindle_push": (optional, Kindle/FireOS Push Object),
 "web_push": (optional, Web Push Object),
 "email": (optional, Email object)
 "webhook": (optional, Webhook object)
 "content_card": (optional, Content Card Object)
 }
}'

```
 | 

## Response

### Example success response

```

1
2
3
4
5

```
 | 
```
{
 "dispatch_id": (string) the dispatch identifier,
 "schedule_id": (string) the schedule identifier,
 "message": "success"
}

```
 | 

- 

New Stuff!
