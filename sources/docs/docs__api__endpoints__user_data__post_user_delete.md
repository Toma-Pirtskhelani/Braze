---
url: https://www.braze.com/docs/api/endpoints/user_data/post_user_delete
slug: docs__api__endpoints__user_data__post_user_delete
title: "Delete users"
description: "This article outlines details about the Delete users Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete users

post

/users/delete

core endpoint

Use this endpoint to delete any user profile by specifying a known user identifier.

Up to 50 external_ids, user_aliases, braze_ids, email_addresses, or phone_numbers can be included in a single request. Only one of external_ids, user_aliases, braze_ids, email_addresses, or phone_numbers can be included in a single request.

If you have a use case that can’t be solved with bulk user deletion through the API, contact the Braze Support team for assistance.

warning

Deleting user profiles cannot be undone. The delete action permanently removes users, which may cause discrepancies in your data. For details, see Effects of deleting user profiles.

See me in Postman

## Prerequisites

To use this endpoint, you need an API key with the users.delete permission.

## Rate limit

We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the /users/alias/new, /users/identify, /users/merge, and /users/alias/update endpoints, as documented in API rate limits.

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
4
5
6
7

```
 | 
```
{
 "external_ids" : (optional, array of string) External IDs to be deleted,
 "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
 "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
 "email_addresses": (optional, array of string) User emails to be deleted,
 "phone_numbers": (optional, array of string) User phone numbers to be deleted
}

```
 | 

### Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 external_ids | 
 Optional | 
 Array of strings | 
 External identifiers to be deleted. | 

 user_aliases | 
 Optional | 
 Array of user alias object | 
 User aliases to be deleted. | 

 braze_ids | 
 Optional | 
 Array of strings | 
 Braze user identifiers to be deleted. | 

 email_addresses | 
 Optional | 
 Array of strings | 
 User emails to be deleted. Refer to Deleting users by email for more information. | 

 phone_numbers | 
 Optional | 
 Array of strings | 
 User phone numbers to be deleted. | 

### Deleting users by email addresses and phone numbers

If an email address or phone number is specified as an identifier, an additional prioritization value is required in the identifier. prioritization must be an ordered array and should specify which user to delete if there are multiple users. This means deleting users does not occur if more than one user matches a prioritization.

The allowed values for the array are:

- identified
 
- unidentified
 
- most_recently_updated (refers to prioritizing the most recently updated user)

Only one of the following options may exist in the prioritization array at a time:

- identified refers to prioritizing a user with an external_id
 
- unidentified refers to prioritizing a user without an external_id

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
13
14
15
16
17
18
19
20
21

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "external_ids": ["external_identifier1", "external_identifier2"],
 "braze_ids": ["braze_identifier1", "braze_identifier2"],
 "user_aliases": [
 {
 "alias_name": "user_alias1", "alias_label": "alias_label1"
 },
 {
 "alias_name": "user_alias2", "alias_label": "alias_label2"
 }
 ],
 "email_addresses": [
 {
 "email": "[email protected]",
 "prioritization": ["unidentified", "most_recently_updated"]
 }
 ]
}'

```
 | 

## Response

```

1
2
3

```
 | 
```
{
 "deleted" : (required, integer) number of user IDs queued for deletion
}

```
 | 

## Effects of deleting user profiles

When you remove a user with this endpoint, the following occurs:

- The user profile is deleted (nulled).
 
- Workspace user counts (such as total users on the analytics home) update to account for the removed users.
 
- The removed user still counts toward the aggregated conversion percentage. Custom event counts and purchase counts are not updated for removed users.

### Multiple profiles with a shared email address

To merge user profiles that share the same email address, call the /users/merge endpoint.

## Troubleshooting

### A success response was returned but the user still appears

A successful response confirms the request was queued, not that deletion is complete. Deletion typically finishes in under a second, but it can take up to five minutes for the change to propagate across all caches. If you immediately search for the user in the dashboard or export their data via the API, you may still see results during this propagation window.

If the user still exists after several minutes, verify that the identifier in your request matches the user’s actual profile:

- external_ids array: Confirm each value matches a user’s external ID exactly.
 
- braze_id: You can find a user’s braze_id by exporting their data with the /users/export/ids endpoint or by exporting a segment to CSV (where the braze_id appears as “Appboy ID”).
 
- Alias-only or email-only profiles: If the profile has no external_id, create a segment filtering for External User ID is blank combined with the known email or phone number, then export to CSV to retrieve the braze_id.

To confirm whether a user has been deleted, call the /users/export/ids endpoint using the same identifier type you used in the delete request (for example, including the value in external_ids, braze_id, or user_aliases). If the user no longer exists, the response contains "users": [] and may include "invalid_user_ids" listing that identifier.

- 

New Stuff!
