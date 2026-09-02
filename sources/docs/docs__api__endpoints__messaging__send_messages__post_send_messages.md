---
url: https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages
slug: docs__api__endpoints__messaging__send_messages__post_send_messages
title: "Send messages immediately using the API only"
description: "This article outlines details about the Send messages immediately using API only Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Send messages immediately using the API only

post

/messages/send

core endpoint

Use this endpoint to send immediate messages to designated users using the Braze API.

If you are targeting a segment, a record of your request is stored in the Developer Console.

See me in Postman

important

If the final rendered payload is larger than the corresponding service’s maximum allowed size, the send won’t be successful.

important

When using this endpoint for API campaigns, the recipient must already exist in Braze for the request to succeed. This applies when specifying users in the external_user_ids or user_aliases parameters.

## Creating new users with API sends

If you need to create a user as part of a send using the API, you have two options:

### Option 1: Use /users/track then send

First, create the user with the /users/track endpoint, then wait for the data to propagate (generally, a few minutes is recommended) before initiating the API-only send. Note that Braze doesn’t guarantee data processing times on /users/track, so race conditions may occur if you don’t allow enough time between these calls.

### Option 2: Use an API-triggered campaign or Canvas

Use an API-triggered campaign or Canvas workflow. These allow you to create a recipient if one doesn’t already exist. This option simplifies your backend processes, but requires you to configure a campaign or Canvas in the Braze dashboard.

## Prerequisites

To use this endpoint, you’ll need to generate an API key with the messages.send permission.

## Rate limit

When using Connected Audience filters in your request, we apply a rate limit of 250 requests per minute to this endpoint. Otherwise, if specifying an external_id, this endpoint has a default rate limit of 250,000 requests per hour shared between the endpoints documented in API rate limits.

Braze endpoints support batching API requests. A single request to the messaging endpoints can reach any of the following:

- Up to 50 specific external_ids, each with individual message parameters
 
- An audience segment of any size, defined in the request as a connected audience object

Braze endpoints support batching API requests. A single request to the messaging endpoints can reach any of the following:

- Up to 50 specific external_ids
 
- A segment of any size created in the Braze dashboard, specified by its segment_id
 
- An audience segment of any size, defined in the request as a connected audience object

## Request body

tip

Be sure to include messaging objects in your body to complete your requests.

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

```
 | 
```
{
 // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
 // Including 'segment_id' will send to members of that segment
 // Including 'external_user_ids' and/or 'user_aliases' will send to those users
 // Including both will send to the provided users if they are in the segment
 "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
 "external_user_ids": (optional, array of strings) see external user identifier,
 "user_aliases": (optional, array of user alias object) see user alias,
 "segment_id": (optional, string) see segment identifier,
 "audience": (optional, connected audience object) see connected audience,
 "campaign_id": (optional*, string) required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
 "send_id": (optional, string) see send identifier,
 "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
 "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
 "messages": {
 "android_push": (optional, android push object),
 "apple_push": (optional, apple push object),
 "content_card": (optional, content card object),
 "email": (optional, email object),
 "kindle_push": (optional, kindle/fireOS push object),
 "web_push": (optional, web push object),
 "webhook": (optional, webhook object),
 "whats_app": (optional, WhatsApp object),
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
 You must set broadcast to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false (as of August 31, 2017). 

 If broadcast is set to true, a recipients list cannot be included. However, use caution when setting broadcast: true, as unintentionally setting this flag may cause you to send your message to a larger than expected audience. | 

 external_user_ids | 
 Optional | 
 Array of strings | 
 See external user ID. | 

 user_aliases | 
 Optional | 
 Array of user alias objects | 
 See user alias object. | 

 segment_id | 
 Optional | 
 String | 
 See segment identifier. | 

 audience | 
 Optional | 
 Connected audience object | 
 See connected audience. | 

 campaign_id | 
 Optional* | 
 String | 
 See campaign identifier for more information. 

*Required to track campaign metrics (such as Sends, Clicks, or Bounces) on the Braze dashboard, or to see events associated with this message in the user profile Message History tab. Without a campaign_id, Braze doesn’t increment dashboard deliverability stats. Sends still appear in the Message Activity Log, but not in email performance metrics in the dashboard. | 

 send_id | 
 Optional | 
 String | 
 See send identifier. | 

 override_frequency_capping | 
 Optional | 
 Boolean | 
 Ignore frequency_capping for campaigns, defaults to false. | 

 recipient_subscription_state | 
 Optional | 
 String | 
 Use this to send messages to only users who have opted in (opted_in), only users who have subscribed or are opted in (subscribed) or to all users, including unsubscribed users (all). 

Using all users is useful for transactional email messaging. Defaults to subscribed. | 

 messages | 
 Optional | 
 Messaging objects | 
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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
 "broadcast": "false",
 "external_user_ids": "external_user_identifiers",
 "user_aliases": {
 "alias_name": "example_name",
 "alias_label": "example_label"
 },
 "segment_id": "segment_identifier",
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
 "override_frequency_capping": "false",
 "recipient_subscription_state": "all",
 "messages": {
 "android_push": "(optional, Android Push Object)",
 "apple_push": "(optional, Apple Push Object)",
 "content_card": "(optional, Content Card Object)",
 "email": "(optional, Email Object)",
 "kindle_push": "(optional, Kindle/FireOS Push Object)",
 "web_push": "(optional, Web Push Object)"
 }
}'

```
 | 

## Response details

Message sending endpoint responses include the message’s dispatch_id for reference back to the dispatch of the message. The dispatch_id is the ID of the message dispatch, meaning the unique ID for each “transmission” sent from Braze. For more information, refer to Dispatch ID behavior.

- 

New Stuff!
