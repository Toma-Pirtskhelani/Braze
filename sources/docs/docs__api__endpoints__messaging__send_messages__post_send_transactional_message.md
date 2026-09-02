---
url: https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_transactional_message
slug: docs__api__endpoints__messaging__send_messages__post_send_transactional_message
title: "Send transactional emails using API-triggered delivery"
description: "This article outlines details about the Send transactional email messages using API-triggered delivery Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Send transactional emails using API-triggered delivery

post

/transactional/v1/campaigns/{campaign_id}/send

Use this endpoint to send immediate, one-off transactional messages to a designated user.

This endpoint is used alongside the creation of a Braze Transactional Email campaign and corresponding campaign ID.

important

Transactional Email is currently available as part of select Braze packages. Contact your Braze customer success manager for more details.

Similar to the Send triggered campaign endpoint, this campaign type allows you to house message content inside of the Braze dashboard while dictating when and to whom a message is sent via your API. Unlike the Send triggered campaign endpoint, which accepts an audience or segment to send messages to, a request to this endpoint must specify a single user either by external_user_id or user_alias, as this campaign type is purpose-built for 1:1 messaging of alerts like order confirmations or password resets.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need to generate an API key with the transactional.send permission.

## Rate limit

The /transactional/v1/campaigns/{campaign_id}/send endpoint is a paid-for endpoint in units per hour (for example, 50,000 per hour depending on your package). There is no separate per-endpoint rate limit: you can send beyond your allotted volume, but only the allotted volume is covered by SLA. Requests to this endpoint count toward your overall external API rate limit. If you exceed that limit (for example, 250,000 requests per hour across all endpoints), Braze returns 429 and requests are throttled. The transactional volume count resets each hour, so after one hour, another allotment is available. Within the SLA-covered volume, 99.9% of emails will send in less than one minute.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 campaign_id | 
 Required | 
 String | 
 ID of the campaign | 

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

```
 | 
```
{
 "external_send_id": (optional, string) see the following request parameters,
 "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
 "recipient": (required, object)
 {
 // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
 "user_alias": (optional, User alias object) User alias of the user to receive message,
 "external_user_id": (optional, string) External identifier of user to receive message,
 "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 external_send_id | 
 Optional | 
 String | 
 A Base64 compatible string. Validated against the following regex:

 /^[a-zA-Z0-9-_+\/=]+$/ 

This optional field allows you to pass an internal identifier for this particular send, which is included in events sent from the Transactional HTTP event postback. When passed, this identifier is also used as a deduplication key, which Braze stores for 24 hours. 

Passing the same identifier in another request does not result in a new instance of a send by Braze for 24 hours. | 

 trigger_properties | 
 Optional | 
 Object | 
 See trigger properties. Personalization key-value pairs that apply to the user in this request. | 

 recipient | 
 Required | 
 Object | 
 The user you are targeting this message to. Can contain attributes and a single external_user_id or user_alias.

Note that if you provide an external user ID that doesn’t already exist in Braze, passing any fields to the attributes object creates this user profile in Braze and sends this message to the newly created user. 

If you send multiple requests to the same user with different data in the attributes object, first_name, last_name, and email attributes are updated synchronously and templated into your message. Custom attributes don’t have this same protection, so proceed with caution when updating a user through this API and passing different custom attribute values in quick succession. | 

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

```
 | 
```
curl -X POST \
 -H 'Content-Type:application/json' \
 -H 'Authorization: Bearer YOUR-REST-API-KEY' \
 -d '{
 "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
 "trigger_properties": {
 "example_string_property": YOUR_EXAMPLE_STRING,
 "example_integer_property": YOUR_EXAMPLE_INTEGER
 },
 "recipient": {
 "external_user_id": TARGETED_USER_ID_STRING
 }
 }' \
 https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send

```
 | 

## Response

The Send transactional email endpoint responds with the message’s dispatch_id which represents the instance of this message send. This identifier can be used along with events from the Transactional HTTP event postback to trace the status of an individual email sent to a single user.

### Example responses

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
 "dispatch_id": A randomly-generated unique ID of the instance of this send
 "status": Current status of the message
 "metadata" : Object containing additional information about the send instance
}

```
 | 

## Troubleshooting

The endpoint may also return an error code and a human-readable message in some cases, most of which are validation errors. Here are some common errors you may get when making invalid requests.

 Error | 
 Troubleshooting | 

 The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint | 
 The campaign ID provided is not for a transactional campaign. | 

 The external reference has been queued. Please retry to obtain send_id. | 
 The external_send_id has been created recently, try a new external_send_id if you are intending to send a new message. | 

 Campaign does not exist | 
 The campaign ID provided does not correspond to an existing campaign. | 

 The campaign is archived. Unarchive the campaign in order for trigger requests to take effect. | 
 The campaign ID provided corresponds to an archived campaign. | 

 The campaign is paused. Resume the campaign in order for trigger requests to take effect. | 
 The campaign ID provided corresponds to a paused campaign. | 

 campaign_id must be a string of the campaign api identifier | 
 The campaign ID provided is not a valid format. | 

 Error authenticating credentials | 
 The API key provided is invalid | 

 Invalid whitelisted IPs | 
 The IP address sending the request is not on the IP whitelist (if it is being used) | 

 You do not have permission to access this resource | 
 The API key used does not have permission to take this action | 

Most endpoints at Braze have a rate limit implementation that returns a 429 response code if you make too many requests. The transactional sending endpoint has a paid hourly allotment measured in units (for example, 50,000 units per hour, depending on your package). There is no separate per-endpoint rate limit for this endpoint: you can send beyond your allotted volume, but only the allotted volume is covered by SLA; requests above that allotment still send but are not covered by SLA. Requests to this endpoint count toward your overall external API rate limit. If you exceed that limit (for example, 250,000 requests per hour across all endpoints), Braze returns 429 and throttles requests until the limit resets. The transactional volume count resets each hour. Contact Braze Support if you need more information about this functionality.

## Transactional HTTP event postback

All transactional emails are complemented with event status postbacks sent as an HTTP request back to your specified URL. This will allow you to evaluate the message status in real-time and take action to reach the user on another channel if the message goes undelivered, or fallback to an internal system if Braze is experiencing latency.

You can associate these updates with individual messages using unique identifiers:

- dispatch_id: A unique ID Braze automatically generates for each message.
 
- external_send_id: A custom identifier you provide, such as an order number, to match updates with your internal systems.

For example, If you include external_send_id: 1234 in the request when sending an order confirmation email, all subsequent event postbacks for that email—like Sent or Delivered—will include external_send_id: 1234. This allows you to confirm whether the customer for order #1234 received their order confirmation email.

### Setting up postbacks

In your Braze dashboard:

- Go to Settings > Email Preferences.
 
- Under Transactional Event Status Postback, enter the URL where Braze should send status updates for your transactional emails.
 
- Test the postback.

### Postback body

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
 "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
 "status": (string, Current status of message from the following message status table,
 "metadata" : (object, additional information relating to the execution of an event)
 {
 "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
 "campaign_api_id" : (string, API identifier of this transactional campaign),
 "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
 "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
 "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
 "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
 "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
 "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
 "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
 "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
 "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
 }
}

```
 | 

#### Message status

 Status | 
 Description | 

 sent | 
 Message successfully dispatched to a Braze email sending partner | 

 processed | 
 Email sending partner has successfully received and prepared the message for sending to the user’s inbox provider | 

 aborted | 
 Braze was unable to successfully dispatch the message due to the user not having an emailable address, or Liquid abort logic was called in the message body. All aborted events include a reason field within the metadata object indicating why the message was aborted | 

 delivered | 
 Message was accepted by the user’s email inbox provider | 

 bounced | 
 Message was rejected by the user’s email inbox provider. All bounced events include a reason field within the metadata object reflecting the bounce error code provided by the inbox provider | 

### Example postback

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

```
 | 
```

// Sent Event
{
 "dispatch_id": "acf471119f7449d579e8089032003ded",
 "status": "sent",
 "metadata": {
 "received_at": "2020-08-31T18:58:41.000+00:00",
 "enqueued_at": "2020-08-31T18:58:41.000+00:00",
 "executed_at": "2020-08-31T18:58:41.000+00:00",
 "sent_at": "2020-08-31T18:58:42.000+00:00",
 "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
 "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
 }
}

// Processed Event
{
 "dispatch_id": "acf471119f7449d579e8089032003ded",
 "status": "processed",
 "metadata": {
 "processed_at": "2020-08-31T18:58:42.000+00:00",
 "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
 "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
 }
}

// Aborted
{
 "dispatch_id": "acf471119f7449d579e8089032003ded",
 "status": "aborted",
 "metadata": {
 "reason": "User not emailable",
 "aborted_at": "2020-08-31T19:04:51.000+00:00",
 "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
 "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
 }
}

// Delivered Event
{
 "dispatch_id": "acf471119f7449d579e8089032003ded",
 "status": "delivered",
 "metadata": {
 "delivered_at": "2020-08-31T18:27:32.000+00:00",
 "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
 "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
 }
}

// Bounced Event
{
 "dispatch_id": "acf471119f7449d579e8089032003ded",
 "status": "bounced",
 "metadata": {
 "bounced_at": "2020-08-31T18:58:43.000+00:00",
 "reason": "550 5.1.1 The email account that you tried to reach does not exist",
 "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
 "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
 }
}

```
 | 

- 

New Stuff!
