---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages
slug: docs__api__endpoints__messaging__schedule_messages__post_delete_scheduled_messages
title: "Delete scheduled messages"
description: "This article outlines details about the Delete scheduled messages Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete scheduled messages

post

/messages/schedule/delete

core endpoint

Use this endpoint to cancel a message that you previously scheduled before it has been sent.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the messages.schedule.delete permission.

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

```
 | 
```
{
 "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
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
 The schedule_id to delete (obtained from the response to create schedule). | 

## Example request

```

1
2
3
4
5
6

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "schedule_id": "schedule_identifier"
}'

```
 | 

- 

New Stuff!
