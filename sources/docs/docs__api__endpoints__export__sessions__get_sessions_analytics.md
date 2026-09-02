---
url: https://www.braze.com/docs/api/endpoints/export/sessions/get_sessions_analytics
slug: docs__api__endpoints__export__sessions__get_sessions_analytics
title: "Export app session by time"
description: "This article outlines details about the Export app sessions analytics by time Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export app session by time

get

/sessions/data_series

Use this endpoint to retrieve a series of the number of sessions for your app over a designated time period.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the sessions.data_series permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

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
 See Segment API identifier. Segment ID indicating the analytics-enabled segment for which sessions should be returned. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
 "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
 "sessions" : (int)
 },
 ...
 ]
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
