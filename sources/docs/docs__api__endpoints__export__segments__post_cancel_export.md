---
url: https://www.braze.com/docs/api/endpoints/export/segments/post_cancel_export
slug: docs__api__endpoints__export__segments__post_cancel_export
title: "Cancel exports by segment"
description: "This article outlines details about Cancel exports by segment Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Cancel exports by segment

post

/export/segment/cancel

Use this endpoint to cancel all ongoing exports with a specified segment ID.

## Prerequisites

To use this endpoint, you’ll need an API key with the segments.list permission.

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
 "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 segment_id | 
 Required | 
 String | 
 The segment_id to cancel its ongoing exports. | 

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
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "segment_id": "segment_identifier"
}'

```
 | 

- 

New Stuff!
