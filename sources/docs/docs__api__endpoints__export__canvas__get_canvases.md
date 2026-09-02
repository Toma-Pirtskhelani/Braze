---
url: https://www.braze.com/docs/api/endpoints/export/canvas/get_canvases
slug: docs__api__endpoints__export__canvas__get_canvases
title: "Export Canvas list"
description: "This article outlines details about the Export Canvas list Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export Canvas list

get

/canvas/list

Use this endpoint to export a list of Canvases, including the name, Canvas API identifier and associated tags.

Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).

Archived Canvases will not be included in the API response unless the include_archived field is specified. Canvases that are stopped but not archived, however, will be returned by default.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the canvas.list permission.

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
 The page of Canvases to return, defaults to 0 (returns the first set of up to 100) | 

 include_archived | 
 Optional | 
 Boolean | 
 Whether or not to include archived Canvases, defaults to false. | 

 sort_direction | 
 Optional | 
 String | 
 - Sort creation time from newest to oldest: pass in the value desc.
 - Sort creation time from oldest to newest: pass in the value asc. 

If sort_direction is not included, the default order is oldest to newest. | 

 last_edit.time[gt] | 
 Optional | 
 Time | 
 Filters the results and only returns Canvases that were edited greater than the time provided until now. Format is yyyy-MM-DDTHH:mm:ss. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
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
 "canvases" : [
 {
 "id" : (string) the Canvas API identifier,
 "last_edited": (ISO 8601 string) the last edited time for the message,
 "name" : (string) the Canvas name,
 "tags" : (array) the tag names associated with the Canvas formatted as strings,
 },
 ... (more Canvases)
 ],
 "message": (string) returns 'success' when the request completes without errors
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
