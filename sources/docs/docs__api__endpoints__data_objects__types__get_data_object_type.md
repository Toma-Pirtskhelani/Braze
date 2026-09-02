---
url: https://www.braze.com/docs/api/endpoints/data_objects/types/get_data_object_type
slug: docs__api__endpoints__data_objects__types__get_data_object_type
title: "Get data object type"
description: "This article outlines details about the Get data object type endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Get data object type

get

/data_objects/types/{type_name}

Use this endpoint to return one data object type and its schema definition.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.read.

## Rate limit

This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the /data_objects/types/{type_name} endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 type_name | 
 Required | 
 String | 
 Data object type machine name | 

## Example request

This section includes a sample path-parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for the path parameter in this request.

```

1
2
3

```
 | 
```
{
 "type_name": "account"
}

```
 | 

### Sample cURL request

This example retrieves the definition of the account data object type.

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account' \
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

```
 | 
```
{
 "data_object_type": {
 "type_name": "account",
 "metadata": { "display_name_source": "name" },
 "schema_def": {
 "type": "object",
 "properties": {
 "name": { "type": "string", "title": "Name" },
 "industry": { "type": "string", "title": "Industry" },
 "renewal_date": { "type": "string", "format": "date-time", "title": "Renewal date" }
 },
 "required": ["name"]
 }
 }
}

```
 | 

schema_def describes allowed object fields. Writes still reject undeclared fields even though this response schema is descriptive.

### Response parameters

The following table lists and describes the fields in a successful response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 data_object_type | 
 Required | 
 Object | 
 Returned data object type record | 

 data_object_type.type_name | 
 Required | 
 String | 
 Data object type machine name | 

 data_object_type.metadata | 
 Required | 
 Object | 
 Type metadata object | 

 data_object_type.schema_def | 
 Required | 
 Object | 
 JSON schema definition for object attributes | 

## Errors

The following table lists common errors for this endpoint and how to resolve them.

 Status | 
 Cause | 
 Guidance | 

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
