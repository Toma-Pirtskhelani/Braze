---
url: https://www.braze.com/docs/api/endpoints/preference_center/get_list_preference_center
slug: docs__api__endpoints__preference_center__get_list_preference_center
title: "List preference centers"
description: "This article outlines details about the List preference centers Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List preference centers

get

/preference_center/v1/list

Use this endpoint to list your available preference centers.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the preference_center.list permission.

## Rate limit

This endpoint has a rate limit of 1,000 requests per minute, per workspace, as documented in API rate limits.

## Path and request parameters

There are no path or request parameters for this endpoint.

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
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
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28

```
 | 
```
{
 "preference_centers": [
 {
 "name": "My Preference Center 1",
 "preference_center_api_id": "preference_center_api_id",
 "created_at": "2022-08-17T15:46:10Z",
 "updated_at": "2022-08-17T15:46:10Z"
 },
 {
 "name": "My Preference Center 2",
 "preference_center_api_id": "preference_center_api_id",
 "created_at": "2022-08-19T11:13:06Z",
 "updated_at": "2022-08-19T11:13:06Z"
 },
 {
 "name": "My Preference Center 3",
 "preference_center_api_id": "preference_center_api_id",
 "created_at": "2022-08-19T11:30:50Z",
 "updated_at": "2022-08-19T11:30:50Z"
 },
 {
 "name": "My Preference Center 4",
 "preference_center_api_id": "preference_center_api_id",
 "created_at": "2022-09-13T20:41:34Z",
 "updated_at": "2022-09-13T20:41:34Z"
 }
 ]
}

```
 | 

- 

New Stuff!
