---
url: https://www.braze.com/docs/api/endpoints/data_objects/objects/patch_update_data_object
slug: docs__api__endpoints__data_objects__objects__patch_update_data_object
title: "Update data object"
description: "This article outlines details about the Update data object endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update data object

patch

/data_objects/objects/{type_name}/{external_id}

Use this endpoint to merge attributes into an existing data object.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.update.

## Rate limit

This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.

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

## Request parameters

The following table lists and describes the JSON request body parameters for the /data_objects/objects/{type_name}/{external_id} endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 attributes | 
 Required | 
 Object | 
 Top-level fields to merge | 

 display_name | 
 Optional | 
 String | 
 Display label for the object. When the type has a display-name source field, the value of that field takes precedence. When omitted, the existing display name is preserved | 

## Example request

This section includes a sample JSON payload and a sample cURL request.

### Sample request payload

```

1
2
3
4
5

```
 | 
```
{
 "attributes": {
 "credits": 750
 }
}

```
 | 

### Sample cURL request

This example updates the credits attribute on acct-123 and leaves the record’s other attributes unchanged.

```

1
2
3
4

```
 | 
```
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'

```
 | 

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code 200 could return the following response body. The attributes object reflects the result of the merge.

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
 "attributes": { "name": "Acme", "credits": 750 }
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
 Updated data object record | 

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
 Object attributes after merge | 

## Errors

The following table lists common errors for this endpoint and how to resolve them.

 Status | 
 Cause | 
 Guidance | 

 400 | 
 Validation error | 
 Confirm every field in attributes exists in the type schema and uses the correct data type. | 

 404 | 
 Type not found or object not found | 
 Confirm type_name and external_id both exist in the workspace. | 

 401 | 
 Missing or invalid REST API key | 
 Verify the Authorization header uses Bearer YOUR_REST_API_KEY and that the key is active. | 

 403 | 
 API key lacks permission or request is blocked by allowlist | 
 Confirm the key has data_objects.update and that your source IP is on the key allowlist, if configured. | 

 429 | 
 Rate limit exceeded | 
 Retry after X-RateLimit-Reset and reduce request frequency. | 

- 

New Stuff!
