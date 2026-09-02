---
url: https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events_data
slug: docs__api__endpoints__export__custom_events__get_custom_events_data
title: "Export custom events"
description: "This article outlines details about the Export custom events Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export custom events

get

/events

Use this endpoint to export a list of custom events recorded for your app. The events are returned in groups of 50, sorted alphabetically.

## Prerequisites

To use this endpoint, you’ll need an API key with the events.get permission.

## Rate limit

We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the /custom_attributes, /events/list, and /purchases/product_list endpoints, as documented in API rate limits.

## Query parameters

Note that each call to this endpoint will return 50 events. For more than 50 events, use the Link header to retrieve the data on the next page as shown in the following example response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 cursor | 
 Optional | 
 String | 
 Determines the pagination of the custom events. | 

## Example requests

### Without cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

### With cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
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
13

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "events" : [
 {
 "name": "The event name", (string) the event name,
 "description": "The event description", (string) the event description,
 "included_in_analytics_report": false, (boolean) the analytics report inclusion,
 "status": "Active", (string) the event status,
 "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
 },
 ...
 ]
}

```
 | 

### Fatal error response codes

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference Fatal errors.

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
