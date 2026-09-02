---
url: https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled
slug: docs__api__endpoints__messaging__schedule_messages__get_messages_scheduled
title: "List upcoming scheduled campaigns and Canvases"
description: "This article outlines details about the List upcoming scheduled campaigns and Canvases Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List upcoming scheduled campaigns and Canvases

get

/messages/scheduled_broadcasts

Use this endpoint to return a JSON list of information about scheduled campaigns and entry Canvases between now and a designated end_time specified in the request.

Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint include campaigns and Canvases created and scheduled in the Braze dashboard.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the messages.schedule_broadcasts permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 end_time | 
 Required | 
 String in ISO-8601 format | 
 End date of the range to retrieve upcoming scheduled campaigns and Canvases. This is treated as midnight in UTC time by the API. | 

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

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

```
 | 
```
{
 "scheduled_broadcasts": [
 {
 "name": (string) the name of the scheduled broadcast,
 "id": (stings) the Canvas or campaign identifier,
 "type": (string) the broadcast type either Canvas or Campaign,
 "tags": (array) an array of tag names formatted as strings,
 "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
 "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone
 }
 ]
}

```
 | 

- 

New Stuff!
