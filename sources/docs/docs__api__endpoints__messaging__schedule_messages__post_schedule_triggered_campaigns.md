---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns
slug: docs__api__endpoints__messaging__schedule_messages__post_schedule_triggered_campaigns
title: "Schedule API-triggered campaigns"
description: "This article outlines details about the Schedule API-triggered campaigns Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Schedule API-triggered campaigns

post

/campaigns/trigger/schedule/create

core endpoint

Use this endpoint to send dashboard created campaign messages via API-triggered delivery, allowing you to decide what action should trigger the message to be sent.

You can pass in trigger_properties that will be templated into the message itself.

Note that to send messages with this endpoint, you must have a campaign ID, created when you build an API-triggered campaign.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the campaigns.trigger.schedule.create permission.

## Rate limit

When using Connected Audience filters in your request, we apply a rate limit of 250 requests per minute to this endpoint. Otherwise, if specifying an external_id, this endpoint has a default rate limit of 250,000 requests per hour shared between the endpoints documented in API rate limits.

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

```
 | 
```
{
 "campaign_id": (required, string) see campaign identifier,
 "send_id": (optional, string) see send identifier,
 // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
 "recipients": (optional, array of recipients object),
 // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the Recipients Object will be used
 "audience": (optional, connected audience object) see connected audience,
 // Including 'audience' will only send to users in the audience
 // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
 // the message will send to entire segment targeted by the campaign
 "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
 "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see trigger properties,
 "schedule": {
 "time": (required, datetime as ISO 8601 string) time to send the message,
 "in_local_time": (optional, bool),
 "at_optimal_time": (optional, bool),
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 campaign_id | 
 Required | 
 String | 
 See campaign identifier | 

 send_id | 
 Optional | 
 String | 
 See send identifier. | 

 recipients | 
 Optional | 
 Array of recipients objects | 
 See recipients object. | 

 audience | 
 Optional | 
 Connected audience object | 
 See connected audience. | 

 broadcast | 
 Optional | 
 Boolean | 
 You must set broadcast to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false (as of August 31, 2017). 

 If broadcast is set to true, a recipients list cannot be included. However, use caution when setting broadcast: true, as unintentionally setting this flag may cause you to send your message to a larger than expected audience. | 

 trigger_properties | 
 Optional | 
 Object | 
 Personalization key-value pairs for all users in this send. See trigger properties. | 

 schedule | 
 Required | 
 Schedule object | 
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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "campaign_id": "campaign_identifier",
 "send_id": "send_identifier",
 "recipients": [
 {
 "user_alias": "example_alias",
 "external_user_id": "external_user_identifier",
 "trigger_properties": {}
 }
 ],
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
 "broadcast": false,
 "trigger_properties": {},
 "schedule": {
 "time": "",
 "in_local_time": false,
 "at_optimal_time": false
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
 "dispatch_id": "dispatch_identifier",
 "schedule_id": "schedule_identifier",
 "message": "success"
}

```
 | 

- 

New Stuff!
