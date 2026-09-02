---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages
slug: docs__api__endpoints__messaging__schedule_messages__post_delete_scheduled_triggered_messages
title: "Delete scheduled API-triggered campaigns"
description: "This article outlines details about the Delete scheduled API-triggered campaigns Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete scheduled API-triggered campaigns

post

/campaigns/trigger/schedule/delete

core endpoint

Use this endpoint to cancel a Canvas message that you previously scheduled via API-triggered before it has been sent.

Scheduled messages or triggers that are deleted close to or during the time they were supposed to be sent are updated with best efforts, so Braze may apply last-second deletions to all, some, or none of your targeted users.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the campaigns.trigger.schedule.delete permission.

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

```
 | 
```
{
 "campaign_id": (required, string) the campaign identifier,
 "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
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
 See campaign identifier. | 

 schedule_id | 
 Required | 
 String | 
 The schedule_id to delete (obtained from the response to create schedule). | 

## Example request

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
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "campaign_id": "campaign_identifier",
 "schedule_id": "schedule_identifier"
}'

```
 | 

- 

New Stuff!
