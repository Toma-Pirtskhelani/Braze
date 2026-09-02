---
url: https://www.braze.com/docs/api/endpoints/data_objects/object_relationships/delete_object_relationship
slug: docs__api__endpoints__data_objects__object_relationships__delete_object_relationship
title: "Delete object relationship"
description: "This article outlines details about the Delete object relationship endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete object relationship

delete

/data_objects/objects/{type_name}/{external_id}/object_relationships

Use this endpoint to delete one object-to-object relationship edge.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.object_relationships.delete.

## Rate limit

This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the /data_objects/objects/{type_name}/{external_id}/object_relationships endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 type_name | 
 Required | 
 String | 
 URL object type | 

 external_id | 
 Required | 
 String | 
 URL object identifier | 

## Request parameters

The following table lists and describes the JSON request body parameters for the /data_objects/objects/{type_name}/{external_id}/object_relationships endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 rel_kind | 
 Required | 
 String | 
 Relationship kind | 

 related_type_name | 
 Required | 
 String | 
 Related object type | 

 related_external_id | 
 Required | 
 String | 
 Related object identifier | 

 anchor | 
 Optional | 
 String | 
 source (default) or target | 

note

This DELETE endpoint expects a JSON request body. Validate that your HTTP client sends request bodies on DELETE calls.

## Example request

This section includes a sample JSON payload and a sample cURL request.

### Sample request payload

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
 "rel_kind": "subaccount",
 "related_type_name": "account",
 "related_external_id": "acct-456",
 "anchor": "source"
}

```
 | 

### Sample cURL request

This example removes the subaccount relationship between acct-123 and acct-456. Both account records remain.

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

```
 | 
```
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
 "rel_kind": "subaccount",
 "related_type_name": "account",
 "related_external_id": "acct-456",
 "anchor": "source"
}'

```
 | 

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code 200 could return the following response body.

```

1

```
 | 
```
{ "deleted": true }

```
 | 

### Response parameters

The following table lists and describes the fields in a successful response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 deleted | 
 Required | 
 Boolean | 
 Whether the relationship deletion succeeded | 

## Errors

The following table lists common errors for this endpoint and how to resolve them.

 Status | 
 Cause | 
 Guidance | 

 400 | 
 Validation error | 
 Confirm the request body includes valid rel_kind, related_type_name, related_external_id, and anchor values. | 

 404 | 
 Relationship or endpoint object not found | 
 Confirm both objects exist and the relationship key values match an existing edge. | 

 401 | 
 Missing or invalid REST API key | 
 Verify the Authorization header uses Bearer YOUR_REST_API_KEY and that the key is active. | 

 403 | 
 API key lacks permission or request is blocked by allowlist | 
 Confirm the key has data_objects.object_relationships.delete and that your source IP is on the key allowlist, if configured. | 

 429 | 
 Rate limit exceeded | 
 Retry after X-RateLimit-Reset and reduce request frequency. | 

- 

New Stuff!
