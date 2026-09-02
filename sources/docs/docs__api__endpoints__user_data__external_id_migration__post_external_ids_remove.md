---
url: https://www.braze.com/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove
slug: docs__api__endpoints__user_data__external_id_migration__post_external_ids_remove
title: "Remove external ID"
description: "This article outlines details about the Remove external IDs endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Remove external ID

post

/users/external_ids/remove

Use this endpoint to remove your users’ old deprecated external IDs.

You can send up to 50 external IDs per request.

warning

This endpoint completely removes the deprecated ID and cannot be undone. Using this endpoint to remove deprecated external_ids that are still associated with users in your system can permanently prevent you from finding those users’ data.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the users.external_ids.remove permission.

## Rate limit

We apply a rate limit of 1,000 requests per minute to this endpoint, as documented in API rate limits.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY

```
 | 

```

1
2
3

```
 | 
```
{
 "external_ids" : (required, array of external identifiers to remove)
}

```
 | 

### Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 external_ids | 
 Required | 
 Array of strings | 
 External identifiers for the users to remove. | 

## Request example

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
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "external_ids" :[
 "existing_deprecated_external_id_string",
 ...
 ]
}'

```
 | 

important

Only deprecated IDs can be removed; attempting to remove a primary external ID will result in an error.

## Response

The response will confirm all successful removals, as well as unsuccessful removals with the associated errors. Error messages in the removal_errors field will reference the index in the array of the original request.

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
 "message" : (string) status message,
 "removed_ids" : (array of strings) successful remove operations,
 "removal_errors": (array of arrays) <minor error message>
}

```
 | 

The message field will return success for any valid request. More specific errors are captured in the removal_errors array. The message field returns an error in the case of:

- Invalid API key
 
- Empty external_ids array
 
- external_ids array with more than 50 items
 
- Rate limit hit (more than 1,000 requests/minute)

- 

New Stuff!
