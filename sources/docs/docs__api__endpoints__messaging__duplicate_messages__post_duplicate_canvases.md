---
url: https://www.braze.com/docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases
slug: docs__api__endpoints__messaging__duplicate_messages__post_duplicate_canvases
title: "Duplicate Canvases using the API"
description: "This article outlines details about the Duplicate Canvases endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Duplicate Canvases using the API

post

/canvas/duplicate

core endpoint

Use this endpoint to duplicate Canvases. This API endpoint is similar to duplicating Canvases in the Braze dashboard.

## Prerequisites

To use this endpoint, you must generate an API key with the canvas.duplicate permission.

## Rate limit

This endpoint is limited to 100 API calls per minute.

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
4
5
6

```
 | 
```
{
 "canvas_id": (required, string) The Canvas identifier,
 "name": (required, string) The name of the resulting Canvas,
 "description": (optional, string) The description of the resulting Canvas,
 "tag_names": (optional, array of strings) The tags of the resulting Canvas,
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 canvas_id | 
 Required | 
 String | 
 See Canvas identifier. | 

 name | 
 Required | 
 String | 
 The name of the resulting Canvas. | 

 description | 
 Optional | 
 String | 
 The description field for the resulting Canvas. | 

 tag_names | 
 Optional | 
 Array of strings | 
 The tags for the resulting Canvas. These must be existing tags. If you add new tags in the request, they overwrite any tags that were on the original Canvas. | 

## Response

This endpoint returns a 202 status code, and the Canvas creation occurs asynchronously. You can use the security event download to see records of when Canvases were duplicated and by which API key.

- 

New Stuff!
