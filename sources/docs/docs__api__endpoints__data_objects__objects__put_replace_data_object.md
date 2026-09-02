---
url: https://www.braze.com/docs/api/endpoints/data_objects/objects/put_replace_data_object
slug: docs__api__endpoints__data_objects__objects__put_replace_data_object
title: "Replace data object"
description: "This article outlines details about the Replace data object endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Replace data object

put

/data_objects/objects/{type_name}/{external_id}

Use this endpoint to create or replace a data object with full-attribute replacement semantics.

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
 Full object attributes. Omitted fields are cleared | 

 display_name | 
 Optional | 
 String | 
 Display label for the object. When the type has a display-name source field, the value of that field takes precedence. Defaults to external_id | 

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
 "name": "Updated Account"
 }
}

```
 | 

### Sample cURL request

This example replaces the stored attributes on acct-123 with the ones in the payload. If no record with that identifier exists, this request creates it.

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
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
 "attributes": {
 "name": "Updated Account"
 }
}'

```
 | 

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code 200 could return the following response body. This endpoint returns 200 whether the request created or replaced the object.

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
 "attributes": { "name": "Updated Account" }
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
 Created or replaced data object record | 

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
 Stored object attributes keyed by field name | 

## Errors

The following table lists common errors for this endpoint and how to resolve them.

 Status | 
 Cause | 
 Guidance | 

 400 | 
 Validation error | 
 Confirm every field in attributes exists in the type schema and uses the correct data type. | 

 404 | 
 Type not found (data-object-type-not-found) | 
 Confirm type_name exists in the workspace and matches the machine name exactly. | 

 422 | 
 Record limit reached (data-object-record-limit-exceeded) when this request would create a new object | 
 Reduce object count for the type, or contact Braze support about your workspace limits. | 

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
