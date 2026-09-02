---
url: https://www.braze.com/docs/api/endpoints/export/segments/get_segment_details
slug: docs__api__endpoints__export__segments__get_segment_details
title: "Export segment details"
description: "This article outlines details about the Export segment details Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export segment details

get

/segments/details

Use this endpoint to retrieve relevant information on a segment, which can be identified by the segment_id.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the segments.details permission.

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

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
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
 "created_at" : (string) the date created as ISO 8601 date,
 "updated_at" : (string) the date last updated as ISO 8601 date,
 "name" : (string) the segment name,
 "description" : (string) a human-readable description of filters,
 "text_description" : (string) the segment description,
 "tags" : (array) the tag names associated with the segment formatted as strings,
 "teams" : (array) the names of the Teams associated with the campaign
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
