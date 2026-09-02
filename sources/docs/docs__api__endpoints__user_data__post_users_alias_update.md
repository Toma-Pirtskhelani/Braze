---
url: https://www.braze.com/docs/api/endpoints/user_data/post_users_alias_update
slug: docs__api__endpoints__user_data__post_users_alias_update
title: "Update user alias"
description: "This article outlines details about the Update user aliases Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update user alias

post

/users/alias/update

Use this endpoint to update existing user aliases.

Up to 50 user aliases may be specified per request.

Updating a user alias requires alias_label, old_alias_name, and new_alias_name to be included in the update user alias object. If there is no user alias associated with the alias_label and old_alias_name, no alias will be updated. If the given alias_label and old_alias_name is found, then the old_alias_name will be updated to the new_alias_name.

note

This endpoint does not guarantee the sequence of alias_updates objects being updated.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the users.alias.update permission.

## Rate limit

We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the /users/delete, /users/alias/new, /users/identify, and /users/merge endpoints, as documented in API rate limits.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY

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
 "alias_updates" : (required, array of update user alias object)
}

```
 | 

### Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 alias_updates | 
 Required | 
 Array of update user alias objects | 
 See user alias object.

 For more information on old_alias_name, new_alias_name, and alias_label, refer to User aliases. | 

### Endpoint request body with update user alias object specification

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
 "alias_label" : (required, string),
 "old_alias_name" : (required, string),
 "new_alias_name" : (required, string)
}

```
 | 

## Example request

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "alias_updates" :[
 {
 "alias_label": "example_alias_label",
 "old_alias_name" : "example_old_alias_name",
 "new_alias_name" : "example_new_alias_name"
 }
 ]
}'

```
 | 

- 

New Stuff!
