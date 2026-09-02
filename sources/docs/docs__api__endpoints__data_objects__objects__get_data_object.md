---
url: https://www.braze.com/docs/api/endpoints/data_objects/objects/get_data_object
slug: docs__api__endpoints__data_objects__objects__get_data_object
title: "Get data object"
description: "This article outlines details about the Get data object endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Get data object

get

/data_objects/objects/{type_name}/{external_id}

Use this endpoint to return one data object.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.read.

## Rate limit

This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the /data_objects/objects/{type_name}/{external_id} endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 type_name | 
 Required | 
 String | 
 Data object type machine name | 

 external_id | 
 Required | 
 String | 
 Object identifier | 

## Example request

This section includes a sample path-parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for the path parameters in this request.

```

1
2
3
4

```
 | 
```
{
 "type_name": "account",
 "external_id": "acct-123"
}

```
 | 

### Sample cURL request

This example retrieves the acct-123 account record and its stored attributes.

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
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

```
 | 
```
{
 "data_object": {
 "type_name": "account",
 "external_id": "acct-123",
 "attributes": { "name": "Acme", "industry": "software" }
 }
}

```
 | 

### Response parameters

The following table lists and describes the fields in a successful response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 data_object | 
 Required | 
 Object | 
 Returned data object record | 

 data_object.type_name | 
 Required | 
 String | 
 Data object type machine name | 

 data_object.external_id | 
 Required | 
 String | 
 Data object identifier | 

 data_object.attributes | 
 Required | 
 Object | 
 Object attributes keyed by field name | 

## Errors

The following table lists common errors for this endpoint and how to resolve them.

 Status | 
 Cause | 
 Guidance | 

 404 | 
 Type not found (data-object-type-not-found) or object not found (data-object-not-found) | 
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
