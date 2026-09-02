---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns
slug: docs__api__endpoints__messaging__schedule_messages__post_update_scheduled_triggered_campaigns
title: "Update scheduled API-triggered campaigns"
description: "This article outlines details about the Update scheduled API-triggered campaigns Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update scheduled API-triggered campaigns

post

/campaigns/trigger/schedule/update

core endpoint

Use this endpoint to update scheduled API-triggered campaigns created in the dashboard, allowing you to decide what action should trigger the message to be sent.

You can pass in trigger_properties that Braze templates into the message itself.

Note that to send messages with this endpoint, you must have a campaign ID, created when you build an API-Triggered Campaign.

Any schedule completely overwrites the one you provided in the create schedule request or previous update schedule requests. For example, if you originally set the schedule to "schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true} and then later update it to "schedule" : {"time" : "2015-02-20T14:14:47"}, Braze sends the message at the specified time in UTC, not in the user’s local time.

Scheduled triggers that are updated close to or during the time they were supposed to be sent are updated with best efforts so that Braze can apply last-second changes to all, some, or none of your targeted users. Updates aren’t applied if the original schedule used local time and the original time has already passed in any time zone.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the campaigns.trigger.schedule.update permission.

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
 "campaign_id": (required, string) see campaign identifier,
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

 campaign_id | 
 Required | 
 String | 
 See campaign identifier | 

 schedule_id | 
 Required | 
 String | 
 The schedule_id to update (obtained from the response to create a schedule). | 

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
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "campaign_id": "campaign_identifier",
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
