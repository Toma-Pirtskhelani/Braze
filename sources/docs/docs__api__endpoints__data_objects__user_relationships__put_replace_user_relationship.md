---
url: https://www.braze.com/docs/api/endpoints/data_objects/user_relationships/put_replace_user_relationship
slug: docs__api__endpoints__data_objects__user_relationships__put_replace_user_relationship
title: "Replace user relationship"
description: "This article outlines details about the Replace user relationship endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Replace user relationship

put

/data_objects/objects/{type_name}/{external_id}/users

Use this endpoint to create or replace one user relationship.

important

Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on Settings > API Keys.

## Prerequisites

To use this endpoint, you need an API key with data_objects.user_relationships.update.

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

 attributes | 
 Optional | 
 Object | 
 Relationship attributes | 

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
7

```
 | 
```
{
 "braze_id": "507f1f77bcf86cd799439011",
 "rel_kind": "account_user",
 "attributes": {
 "role": "admin"
 }
}

```
 | 

### Sample cURL request

This example replaces the attributes on the account_user relationship between the user and acct-123, overwriting any attributes previously stored on it.

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

```
 | 
```
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
 "braze_id": "507f1f77bcf86cd799439011",
 "rel_kind": "account_user",
 "attributes": {
 "role": "admin"
 }
}'

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

```
 | 
```
{
 "user_relationship": {
 "type_name": "account",
 "external_id": "acct-123",
 "rel_kind": "account_user",
 "user": { "braze_id": "507f1f77bcf86cd799439011" },
 "attributes": { "role": "admin" }
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

 user_relationship | 
 Required | 
 Object | 
 Created or replaced user relationship record | 

 user_relationship.type_name | 
 Required | 
 String | 
 Data object type machine name | 

 user_relationship.external_id | 
 Required | 
 String | 
 Data object identifier | 

 user_relationship.rel_kind | 
 Required | 
 String | 
 Relationship kind value | 

 user_relationship.user | 
 Required | 
 Object | 
 Linked user object | 

 user_relationship.user.braze_id | 
 Required | 
 String | 
 Braze user identifier | 

 user_relationship.attributes | 
 Required | 
 Object | 
 Relationship attributes | 

## Errors

The following table lists common errors for this endpoint and how to resolve them.

 Status | 
 Cause | 
 Guidance | 

 400 | 
 Validation error | 
 Confirm rel_kind is valid for the object type and attributes match the relationship schema. | 

 404 | 
 Relationship or object not found (data-object-relationship-not-found) | 
 Confirm the object, user, and relationship key values all exist. | 

 422 | 
 Objects-per-user limit reached (data-objects-per-user-limit-exceeded) or users-per-object limit reached (users-per-data-object-limit-exceeded) | 
 Reduce the relationship count for the user or the object, or contact Braze support about your workspace limits. | 

 401 | 
 Missing or invalid REST API key | 
 Verify the Authorization header uses Bearer YOUR_REST_API_KEY and that the key is active. | 

 403 | 
 API key lacks permission or request is blocked by allowlist | 
 Confirm the key has data_objects.user_relationships.update and that your source IP is on the key allowlist, if configured. | 

 429 | 
 Rate limit exceeded | 
 Retry after X-RateLimit-Reset and reduce request frequency. | 

- 

New Stuff!
