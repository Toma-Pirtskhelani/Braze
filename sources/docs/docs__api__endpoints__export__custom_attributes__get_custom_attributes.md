---
url: https://www.braze.com/docs/api/endpoints/export/custom_attributes/get_custom_attributes
slug: docs__api__endpoints__export__custom_attributes__get_custom_attributes
title: "Export custom attributes"
description: "This article outlines details about the Export custom attributes Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export custom attributes

get

/custom_attributes

Use this endpoint to export a list of custom attributes recorded for your app. The attributes are returned in groups of 50, sorted alphabetically.

## Prerequisites

To use this endpoint, you’ll need an API key with the custom_attributes.get permission.

## Rate limit

We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the /events, /events/list, and /purchases/product_list endpoints, as documented in API rate limits.

## Query parameters

Note that each call to this endpoint will return 50 attributes. For more than 50 attributes, use the Link header to retrieve the data on the next page as shown in the following example response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 cursor | 
 Optional | 
 String | 
 Determines the pagination of the custom attributes. | 

## Example requests

### Without cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

### With cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
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

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "attributes" : [
 {
 "array_length": 100, (number) the maximum array length, or null if not applicable,
 "data_type": "Number", (string) the data type,
 "description": "The attribute description", (string) the attribute description,
 "name": "The attribute name", (string) the attribute name,
 "status": "Active", (string) the attribute status,
 "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
 },
 ...
 ]
}

```
 | 

### Fatal error response codes

For status codes and associated error messages that will be returned if your request encounters a fatal error, reference Fatal errors.

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
