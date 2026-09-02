---
url: https://www.braze.com/docs/api/endpoints/export/segments/get_segment
slug: docs__api__endpoints__export__segments__get_segment
title: "Export segment list"
description: "This article outlines details about Export the segments list Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export segment list

get

/segments/list

Use this endpoint to export a list of segments, each of which will include its name, Segment API identifier, and whether it has analytics tracking enabled.

The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the segments.list permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 page | 
 Optional | 
 Integer | 
 The page of segments to return, defaults to 0 (returns the first set of up to 100). | 

 sort_direction | 
 Optional | 
 String | 
 - Sort creation time from newest to oldest: pass in the value desc.
 - Sort creation time from oldest to newest: pass in the value asc. 

If sort_direction is not included, the default order is oldest to newest. | 

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
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
 "message": (string) returns 'success' when the request completes without errors,
 "segments" : [
 {
 "id" : (string) the Segment API identifier,
 "name" : (string) segment name,
 "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
 "tags" : (array) the tag names associated with the segment formatted as strings
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
