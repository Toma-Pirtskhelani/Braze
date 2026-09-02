---
url: https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events_analytics
slug: docs__api__endpoints__export__custom_events__get_custom_events_analytics
title: "Export custom events analytics"
description: "This article outlines details about the Export custom events analytics Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export custom events analytics

get

/events/data_series

Use this endpoint to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the events.data_series permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 event | 
 Required | 
 String | 
 The name of the custom event for which to return analytics. | 

 length | 
 Required | 
 Integer | 
 Maximum number of units (days or hours) before ending_at to include in the returned series. Must be between 1 and 100 (inclusive). | 

 unit | 
 Optional | 
 String | 
 Unit of time between data points. Can be day or hour, defaults to day. | 

 ending_at | 
 Optional | 
 Datetime 
(ISO-8601 string) | 
 Date on which the data series should end. Defaults to time of the request. | 

 app_id | 
 Optional | 
 String | 
 App API identifier retrieved from the API Keys page to limit analytics to a specific app. | 

 segment_id | 
 Optional | 
 String | 
 See Segment API identifier. Segment ID indicating the analytics-enabled segment for which event analytics should be returned. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "data" : [
 {
 "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
 "count" : (int) the number of occurrences of provided custom event
 },
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
