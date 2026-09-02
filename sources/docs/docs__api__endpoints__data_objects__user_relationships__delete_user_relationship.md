---
url: https://www.braze.com/docs/api/endpoints/data_objects/user_relationships/delete_user_relationship
slug: docs__api__endpoints__data_objects__user_relationships__delete_user_relationship
title: "Delete user relationship"
description: "This article outlines details about the Delete user relationship endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete user relationship

delete

/data_objects/objects/{type_name}/{external_id}/users

Use this endpoint to remove one user-to-object relationship.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.user_relationships.delete.

## Rate limit

This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the /data_objects/objects/{type_name}/{external_id}/users endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 type_name | 
 Required | 
 String | 
 Object type | 

 external_id | 
 Required | 
 String | 
 Object identifier | 

## Request parameters

The following table lists and describes the JSON request body parameters for the /data_objects/objects/{type_name}/{external_id}/users endpoint.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 braze_id | 
 Required | 
 String | 
 Braze user ID | 

 rel_kind | 
 Required | 
 String | 
 Relationship kind | 

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

```
 | 
```
{
 "braze_id": "507f1f77bcf86cd799439011",
 "rel_kind": "account_user"
}

```
 | 

### Sample cURL request

This example removes the account_user relationship between the specified user and acct-123. The user profile and the account record both remain.

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
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
 "braze_id": "507f1f77bcf86cd799439011",
 "rel_kind": "account_user"
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
 Confirm the request body includes valid braze_id and rel_kind values. | 

 404 | 
 Relationship or object not found | 
 Confirm the object, user, and relationship key values all exist. | 

 401 | 
 Missing or invalid REST API key | 
 Verify the Authorization header uses Bearer YOUR_REST_API_KEY and that the key is active. | 

 403 | 
 API key lacks permission or request is blocked by allowlist | 
 Confirm the key has data_objects.user_relationships.delete and that your source IP is on the key allowlist, if configured. | 

 429 | 
 Rate limit exceeded | 
 Retry after X-RateLimit-Reset and reduce request frequency. | 

- 

New Stuff!
