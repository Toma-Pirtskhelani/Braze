---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs
slug: docs__api__endpoints__catalogs__catalog_management__synchronous__get_list_catalogs
title: "List catalogs"
description: "This article outlines details about the List catalogs Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List catalogs

get

/catalogs

Use this endpoint to return a list of catalogs in a workspace.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.get permission.

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog endpoints, as documented in API rate limits.

## Path and request parameters

There are no path or request parameters for this endpoint.

## Example request

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

### Example success response

The status code 200 could return the following response body.

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
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69

```
 | 
```
{
 "catalogs": [
 {
 "description": "My Restaurants",
 "fields": [
 {
 "name": "id",
 "type": "string"
 },
 {
 "name": "Name",
 "type": "string"
 },
 {
 "name": "City",
 "type": "string"
 },
 {
 "name": "Cuisine",
 "type": "string"
 },
 {
 "name": "Rating",
 "type": "number"
 },
 {
 "name": "Loyalty_Program",
 "type": "boolean"
 },
 {
 "name": "Created_At",
 "type": "time"
 }
 ],
 "name": "restaurants",
 "num_items": 10,
 "updated_at": "2022-11-02T20:04:06.879+00:00"
 },
 {
 "description": "My Catalog",
 "fields": [
 {
 "name": "id",
 "type": "string"
 },
 {
 "name": "string_field",
 "type": "string"
 },
 {
 "name": "number_field",
 "type": "number"
 },
 {
 "name": "boolean_field",
 "type": "boolean"
 },
 {
 "name": "time_field",
 "type": "time"
 }
 ],
 "name": "my_catalog",
 "num_items": 3,
 "updated_at": "2022-11-02T09:03:19.967+00:00"
 }
 ],
 "message": "success"
}

```
 | 

- 

New Stuff!
