---
url: https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events
slug: docs__api__endpoints__export__custom_events__get_custom_events
title: "Export custom events list"
description: "This article outlines details about the Export custom events list Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export custom events list

get

/events/list

Use this endpoint to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the events.list permission.

## Rate limit

We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the /custom_attributes, /events, and /purchases/product_list endpoints, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 page | 
 Optional | 
 Integer | 
 The page of event names to return, defaults to 0 (returns the first set of up to 250). | 

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
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

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "events" : [
 "Event A", (string) the event name,
 "Event B", (string) the event name,
 "Event C", (string) the event name,
 ...
 ]
}

```
 | 

### Fatal error response codes

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference Fatal errors & responses.

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
