---
url: https://www.braze.com/docs/api/endpoints/export/segments/get_segment_analytics
slug: docs__api__endpoints__export__segments__get_segment_analytics
title: "Export segment analytics"
description: "This article outlines details about the Export segment analytics Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export segment analytics

get

/segments/data_series

Use this endpoint to retrieve a daily series of the estimated size of a segment over time. 

If you need the exact size of a segment, export its users with the /users/export/segment endpoint and count the exported profiles.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the segments.data_series permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 segment_id | 
 Required | 
 String | 
 See Segment API identifier.

 The segment_id for a given segment can be found on the API Keys page within your Braze account or you can use the Export segment list endpoint. | 

 length | 
 Required | 
 Integer | 
 Maximum number of days before ending_at to include in the returned series. Must be between 1 and 100 (inclusive). | 

 ending_at | 
 Optional | 
 Datetime 
(ISO-8601 string) | 
 Date on which the data series should end. Defaults to time of the request. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
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
 "time" : (string) the date as ISO 8601 date,
 "size" : (int) the size of the segment on that date
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
