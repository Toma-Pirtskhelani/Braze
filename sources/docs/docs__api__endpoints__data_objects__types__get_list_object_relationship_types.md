---
url: https://www.braze.com/docs/api/endpoints/data_objects/types/get_list_object_relationship_types
slug: docs__api__endpoints__data_objects__types__get_list_object_relationship_types
title: "List object relationship types"
description: "This article outlines details about the List object relationship types endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List object relationship types

get

/data_objects/types/{type_name}/object_relationship_types

Use this endpoint to list relationship kinds available for object-to-object links for a given anchor direction.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.read.

## Rate limit

This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the /data_objects/types/{type_name}/object_relationship_types endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 type_name | 
 Required | 
 String | 
 Data object type machine name | 

## Query parameters

The following table lists and describes the query parameters for the /data_objects/types/{type_name}/object_relationship_types endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 anchor | 
 Optional | 
 String | 
 source (default) or target | 

 limit | 
 Optional | 
 Integer | 
 Page size. Default 100. Clamped to 1 through 250 | 

 offset | 
 Optional | 
 Integer | 
 Offset. Default 0. Negative values are floored to 0 | 

## Example request

This section includes a sample parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for request parameters.

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
 "type_name": "account",
 "anchor": "source",
 "limit": 10,
 "offset": 0
}

```
 | 

### Sample cURL request

This example lists the object relationship kinds available to the account type when account is the source of the relationship.

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account/object_relationship_types?anchor=source&limit=10&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'

```
 | 

## Response

This section includes a sample successful response and the response fields.

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

```
 | 
```
{
 "items": [
 {
 "from_type_name": "account",
 "to_type_name": "account",
 "rel_kind": "subaccount",
 "display_name": "subaccount",
 "related_type_name": "account"
 }
 ],
 "total_count": 1,
 "has_more": false,
 "next_offset": null,
 "offset": 0,
 "limit": 10
}

```
 | 

related_type_name is the type on the other side of the relationship for the selected anchor.

### Response parameters

The following table lists and describes the fields in a successful response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 items | 
 Required | 
 Array | 
 List of available object relationship types | 

 items[].from_type_name | 
 Required | 
 String | 
 Source data object type name | 

 items[].to_type_name | 
 Required | 
 String | 
 Target data object type name | 

 items[].rel_kind | 
 Required | 
 String | 
 Relationship kind value | 

 items[].display_name | 
 Required | 
 String | 
 Display label for the relationship kind | 

 items[].related_type_name | 
 Required | 
 String | 
 Opposite-side type for the requested anchor | 

 total_count | 
 Required | 
 Integer | 
 Total number of matching records | 

 has_more | 
 Required | 
 Boolean | 
 Whether another page of results is available | 

 next_offset | 
 Optional | 
 Integer | 
 Offset for the next page when has_more is true | 

 offset | 
 Required | 
 Integer | 
 Current page offset | 

 limit | 
 Required | 
 Integer | 
 Page size used by the request | 

## Errors

The following table lists common errors for this endpoint and how to resolve them.

 Status | 
 Cause | 
 Guidance | 

 400 | 
 Invalid anchor | 
 Use source or target for anchor. | 

 404 | 
 Type not found (data-object-type-not-found) | 
 Confirm type_name exists in the workspace and matches the machine name exactly. | 

 401 | 
 Missing or invalid REST API key | 
 Verify the Authorization header uses Bearer YOUR_REST_API_KEY and that the key is active. | 

 403 | 
 API key lacks permission or request is blocked by allowlist | 
 Confirm the key has data_objects.read and that your source IP is on the key allowlist, if configured. | 

 429 | 
 Rate limit exceeded | 
 Retry after X-RateLimit-Reset and reduce request frequency. | 

- 

New Stuff!
