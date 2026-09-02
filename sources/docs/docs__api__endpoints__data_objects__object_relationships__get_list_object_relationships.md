---
url: https://www.braze.com/docs/api/endpoints/data_objects/object_relationships/get_list_object_relationships
slug: docs__api__endpoints__data_objects__object_relationships__get_list_object_relationships
title: "List object relationships"
description: "This article outlines details about the List object relationships endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List object relationships

get

/data_objects/objects/{type_name}/{external_id}/object_relationships

Use this endpoint to list related data objects from one object anchor.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.read.

## Rate limit

This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the /data_objects/objects/{type_name}/{external_id}/object_relationships endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 type_name | 
 Required | 
 String | 
 Source object type | 

 external_id | 
 Required | 
 String | 
 Source object identifier | 

## Query parameters

The following table lists and describes the query parameters for the /data_objects/objects/{type_name}/{external_id}/object_relationships endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 anchor | 
 Optional | 
 String | 
 source (default) or target | 

 rel_kind | 
 Optional | 
 String | 
 Filter by one relationship kind | 

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
7
8

```
 | 
```
{
 "type_name": "account",
 "external_id": "acct-123",
 "anchor": "source",
 "rel_kind": "subaccount",
 "limit": 100,
 "offset": 0
}

```
 | 

### Sample cURL request

This example lists the subaccount records that acct-123 links out to, returning the first page of results.

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
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
17
18

```
 | 
```
{
 "items": [
 {
 "rel_kind": "subaccount",
 "to_data_object": {
 "type_name": "account",
 "external_id": "acct-456",
 "attributes": { "name": "Child Account" }
 },
 "attributes": {}
 }
 ],
 "total_count": 1,
 "has_more": false,
 "next_offset": null,
 "offset": 0,
 "limit": 100
}

```
 | 

With anchor=target, related objects are returned as from_data_object.

### Response parameters

The following table lists and describes the fields in a successful response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 items | 
 Required | 
 Array | 
 List of object relationship records | 

 items[].rel_kind | 
 Required | 
 String | 
 Relationship kind value | 

 items[].to_data_object | 
 Conditional | 
 Object | 
 Related object when anchor=source | 

 items[].from_data_object | 
 Conditional | 
 Object | 
 Related object when anchor=target | 

 items[].to_data_object.type_name | 
 Conditional | 
 String | 
 Related object type name | 

 items[].to_data_object.external_id | 
 Conditional | 
 String | 
 Related object external ID | 

 items[].to_data_object.attributes | 
 Conditional | 
 Object | 
 Related object attributes | 

 items[].from_data_object.type_name | 
 Conditional | 
 String | 
 Related object type name | 

 items[].from_data_object.external_id | 
 Conditional | 
 String | 
 Related object external ID | 

 items[].from_data_object.attributes | 
 Conditional | 
 Object | 
 Related object attributes | 

 items[].attributes | 
 Required | 
 Object | 
 Relationship attributes | 

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
 Type or object not found | 
 Confirm type_name and external_id both exist in the workspace. | 

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
