---
url: https://www.braze.com/docs/api/endpoints/user_data/post_user_identify
slug: docs__api__endpoints__user_data__post_user_identify
title: "Identify users"
description: "This article outlines details about the Identify users Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Identify users

post

/users/identify

Use this endpoint to identify an unidentified (alias-only, email-only, or phone number-only) user using the provided external ID.

See me in Postman

## How it works

Calling /users/identify combines a user profile that is identified by an alias (alias-only profile), email address (email-only profile), or phone number (phone number-only profile) with a user profile that has an external_id (identified profile), then removes the alias-only profile.

Identifying a user requires an external_id to be included in the following objects:

- aliases_to_identify
 
- emails_to_identify
 
- phone_numbers_to_identify

If there isn’t a user with that external_id, the external_id is added to the aliased user’s record, and the user is considered identified. Users can have only one alias for a specific label. If a user already exists with the external_id and has an existing alias with the same label as the alias-only profile, then the user profiles are not combined.

tip

To prevent unexpected loss of data when identifying users, we highly recommend that you first refer to data collection best practices to learn about capturing user data when alias-only user information is already present.

### Merging behavior

By default, this endpoint merges the following list of fields found exclusively on the anonymous user to the identified user.

List of fields that are merged

- First name
 
- Last name
 
- Email
 
- Gender
 
- Date of birth
 
- Phone number
 
- Time zone
 
- Home city
 
- Country
 
- Language
 
- Session count (the sum of sessions from both profiles)
 
- Date of first session (Braze picks the earlier date of the two dates)
 
- Date of last session (Braze picks the later date of the two dates)
 
- Custom attributes
 
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
 
- Campaign summaries (Braze picks the most recent date fields)
 
- Workflow summaries (Braze picks the most recent date fields)
 
- Message and message engagement history
 
- Custom event and purchase event count and first date and last date timestamps

- These merged fields update “for X events in Y days” filters. For purchase events, these filters include “number of purchases in Y days” and “money spent in last Y days”.

- Session data if the app exists on both user profiles

- For example, if our target user doesn’t have an app summary for “ABCApp” but our original user does, the target user has the “ABCApp” app summary on their profile after the merge.

## Prerequisites

To use this endpoint, you’ll need an API key with the users.identify permission.

## Rate limit

We apply a shared rate limit of 20,000 requests per minute to this endpoint. This rate limit is shared with the /users/delete, /users/alias/new, /users/merge, and /users/alias/update endpoints, as documented in API rate limits.

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

```
 | 
```
{
 "aliases_to_identify" : (required, array of alias to identify objects),
 "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
 "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},

```
 | 

### Request parameters

You can add up to 50 user aliases per request. You can associate multiple additional user aliases with a single external_id.

important

One of the following is required: aliases_to_identify, emails_to_identify, or phone_numbers_to_identify per request. For example, you can use this endpoint to identify users by email by using emails_to_identify in your request.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 aliases_to_identify | 
 Required | 
 Array of aliases to identify object | 
 See alias to identify object and user alias object. | 

 emails_to_identify | 
 Required | 
 Array of aliases to identify object | 
 Required if email is specified as the identifier. Email addresses to identify users. See Identifying users by email. | 

 phone_numbers_to_identify | 
 Required | 
 Array of aliases to identify object | 
 Phone numbers to identify users. | 

### Identifying users by email addresses and phone numbers

If an email address or phone number is specified as an identifier, you must also include prioritization in the identifier.

The prioritization must be an array specifying which user to merge if there are multiple users found. prioritization is an ordered array, meaning if more than one user matches from a prioritization, then merging does not occur.

The allowed values for the array are:

- identified
 
- unidentified
 
- most_recently_updated (refers to prioritizing the most recently updated user)
 
- least_recently_updated (refers to prioritizing the least recently updated user)

Only one of the following options may exist in the prioritization array at a time:

- identified refers to prioritizing a user with an external_id
 
- unidentified refers to prioritizing a user without an external_id

note

A merge does not occur if the email address or phone number matches multiple users. This includes cases where one of those users has the same external_id as the one specified in the request. In these cases, the endpoint returns "message": "success", but the user profiles are not combined. To avoid this, verify that the email address or phone number is associated only with unidentified users before calling this endpoint.

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
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "aliases_to_identify": [
 {
 "external_id": "external_identifier",
 "user_alias": {
 "alias_name": "example_alias",
 "alias_label": "example_label"
 }
 }
 ],
 "emails_to_identify": [
 {
 "external_id": "external_identifier_2",
 "email": "[email protected]",
 "prioritization": ["unidentified", "most_recently_updated"]
 }
 ]
}'

```
 | 

### Case sensitivity

The alias_name field is case-sensitive. A request that returns a 201 status code only confirms the request syntax was valid—it does not confirm the alias was matched. If the capitalization of alias_name in your request doesn’t exactly match the alias stored on the user profile, the operation will silently fail and the external_id won’t be assigned. For example, if the stored alias is [email protected], a request with [email protected] will return success but produce no result.

tip

For more information on alias_name and alias_label, check out our user aliases documentation.

### Why does my identify request return success but the profile did not merge?

201 Created with message: success means Braze accepted the request. It does not guarantee that every alias or email in the payload matched an existing profile—case mismatches on alias_name, duplicate profiles, or Braze prioritization rules can result in no visible merge even though the call succeeded. Verify that alias_name casing exactly matches stored values, check for duplicate profiles with /users/merge, and review prioritization when using emails_to_identify.

## Response

```

1
2
3
4

```
 | 
```
{
 "aliases_processed": 1,
 "message": "success"
}

```
 | 

- 

New Stuff!
