---
url: https://www.braze.com/docs/api/endpoints/user_data/post_users_merge
slug: docs__api__endpoints__user_data__post_users_merge
title: "Merge users"
description: "This article outlines details about the Merge users Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Merge users

post

/users/merge

Use this endpoint to merge one user into another user.

Up to 50 merges may be specified per request. This endpoint is asynchronous.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the users.merge permission.

## Rate limit

We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the /users/delete, /users/alias/new, /users/identify, and /users/alias/update endpoints, as documented in API rate limits.

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
 "merge_updates" : (required, array of objects)
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 merge_updates | 
 Required | 
 Array | 
 An object array. Each object should contain an identifier_to_merge object and an identifier_to_keep object, which should each reference a user either by external_id, user_alias, phone, or email. | 

### Merge behavior

The following behavior is true for all Braze features that are not powered by Snowflake. User merges won’t be reflected for the Messaging History tab, Segment Extensions, Query Builder, and Currents.

important

The endpoint does not guarantee the sequence of merge_updates objects being updated.

This endpoint merges the following fields if they’re not found on the target user.

- First name
 
- Last name
 
- Email addresses (unless they are encrypted)
 
- Gender
 
- Date of birth
 
- Phone number
 
- Time zone
 
- Home city
 
- Country
 
- Language
 
- Device information
 
- Session count (the sum of sessions from both profiles)
 
- Date of first session (Braze picks the earlier date of the two dates)
 
- Date of last session (Braze picks the later date of the two dates)
 
- Custom attributes (Braze retains existing custom attributes on the target profile and includes custom attributes that didn’t exist on the target profile)
 
- Custom event and purchase event data
 
- Custom event and purchase event properties for “X times in Y days” segmentation (where X<=50 and Y<=30)
 
- Segmentable custom events summary

- Event count (the sum from both profiles)
 
- Event first occurred (Braze picks the earlier date of the two dates)
 
- Event last occurred (Braze picks the later date of the two dates)

- In-app purchase total in cents (the sum from both profiles)
 
- Total number of purchases (the sum from both profiles)
 
- Date of first purchase (Braze picks the earlier date of the two dates)
 
- Date of last purchase (Braze picks the later date of the two dates)
 
- App summaries
 
- Last_X_at fields (Braze updates the fields if the orphaned profile fields are more recent)
 
- Campaign interaction data (Braze picks the most recent date fields)
 
- Workflow summaries (Braze picks the most recent date fields)
 
- Message and message engagement history
 
- Braze merges session data only if the app exists on both user profiles.

note

When merging users, using the /users/merge endpoint works the same way as using the changeUser() method.

Braze handles three user types differently when merging: users marked for deletion, test users, and Global Control Group users. For details, see User merge behavior.

#### Custom event date and purchase event date behavior

These merged fields update “for X events in Y days” filters. For purchase events, these filters include “number of purchases in Y days” and “money spent in last Y days”.

### Merging users by email or phone number

If an email or phone is specified as an identifier, you must include an additional prioritization value in the identifier. The prioritization should be an ordered array specifying which user to merge if multiple users are found. This means if more than one user matches from a prioritization, then merging does not occur.

The allowed values for the array are:

- identified
 
- unidentified
 
- most_recently_updated (refers to prioritizing the most recently updated user)
 
- least_recently_updated (refers to prioritizing the least recently updated user)

Only one of the following options may exist in the prioritization array at a time:

- identified refers to prioritizing a user with an external_id
 
- unidentified refers to prioritizing a user without an external_id

important

If both profiles have invalid phone numbers, Braze does not merge them. Invalid numbers are not stored in E.164 format, and the merge job does not combine those profiles. The endpoint still returns 202 Accepted with a success message, so the HTTP response does not indicate that the merge was skipped. Correct the phone numbers on one or both profiles before merging.

## Example requests

### Basic request

This is a basic request body to show the pattern of the request.

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
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "merge_updates": [
 {
 "identifier_to_merge": {
 "external_id": "old-user1"
 },
 "identifier_to_keep": {
 "external_id": "current-user1"
 }
 },
 {
 "identifier_to_merge": {
 "email": "[email protected]",
 "prioritization": ["unidentified", "most_recently_updated"]
 },
 "identifier_to_keep": {
 "email": "[email protected]",
 "prioritization": ["identified", "most_recently_updated"]
 }
 },
 {
 "identifier_to_merge": {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "email"
 }
 },
 "identifier_to_keep": {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "email"
 }
 }
 }
 ]
}'

```
 | 

### Merging unidentified user

The following request would merge the most recently updated unidentified user with email address [email protected] into the user with an external ID john. In this example, using most_recently_updated filters the query to one unidentified user. So, if there were two unidentified users with this email address, only one would get merged into the user who has an external ID john.

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "merge_updates": [
 {
 "identifier_to_merge": {
 "email": "[email protected]",
 "prioritization": ["unidentified", "most_recently_updated"]
 },
 "identifier_to_keep": {
 "external_id": "john"
 }
 }
 ]
}'

```
 | 

### Merging unidentified user into identified user

This next example merges the most recently updated unidentified user with email address [email protected] into the most recently updated identified user with email address [email protected].

Using most_recently_updated filters the queries to one user (one unidentified user for identifier_to_merge, and one identified user for the identifier_to_keep).

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "merge_updates": [
 {
 "identifier_to_merge": {
 "email": "[email protected]",
 "prioritization": ["unidentified", "most_recently_updated"]
 },
 "identifier_to_keep": {
 "email": "[email protected]",
 "prioritization": ["identified", "most_recently_updated"]
 }
 }
 ]
}'

```
 | 

### Merging an unidentified user without including the most_recently_updated prioritization

If there are two unidentified users with the mail address [email protected], this example request doesn’t merge any users because there are two unidentified users with that email address. This request only works if there is only one unidentified user with the email address [email protected].

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "merge_updates": [
 {
 "identifier_to_merge": {
 "email": "[email protected]",
 "prioritization": ["unidentified"]
 },
 "identifier_to_keep": {
 "external_id": "john"
 }
 }
 ]
}'

```
 | 

## Response

There are two status code responses for this endpoint: 202 and 400.

### Example success response

The status code 202 could return the following response body.

```

1
2
3

```
 | 
```
{
 "message": "success"
}

```
 | 

### Example error response

The status code 400 could return the following response body. Refer to Troubleshooting for more information about errors you may encounter.

```

1
2
3

```
 | 
```
{
 "message": "'merge_updates' must be an array of objects"
}

```
 | 

## Troubleshooting

### A success response was returned but the merged user is still searchable

A successful response confirms the request was accepted, but the merge operation involves two steps: merging the profiles and then removing the source profile. Because of this, the identifier_to_merge profile may remain searchable in the dashboard for a short period after a successful response. This is expected behavior—wait a few minutes and then verify the merge is complete.

If the merged user still exists after several minutes, verify that the identifiers in your request are correct and belong to users in the same workspace as the API key used for the request.

### Error reference

The following table lists possible error messages that may occur.

 Error | 
 Troubleshooting | 

 'merge_updates' must be an array of objects | 
 Check that merge_updates is an array of objects. | 

 a single request may not contain more than 50 merge updates | 
 You can only specify up to 50 merge updates in a single request. | 

 identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string | 
 Check the identifiers in your request. | 

 'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep' | 
 Check that merge_updates only contains the two objects identifier_to_merge and identifier_to_keep. | 

- 

New Stuff!
