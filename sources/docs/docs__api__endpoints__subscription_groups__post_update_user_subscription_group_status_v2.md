---
url: https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2
slug: docs__api__endpoints__subscription_groups__post_update_user_subscription_group_status_v2
title: "Update user’s subscription group status (V2)"
description: "This article outlines details about the Update user's subscription group status Braze V2 endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update user’s subscription group status (V2)

post

/v2/subscription/status/set

Use this endpoint to batch update the subscription state of up to 50 users on the Braze dashboard.

You can access a subscription group’s subscription_group_id by navigating to the Subscription Group page.

To see examples or test this endpoint for Email Subscription Groups:

See me in Postman

To see examples or test this endpoint for SMS Subscription Groups:

See me in Postman

To see examples or test this endpoint for WhatsApp Groups:

See me in Postman

## Prerequisites

To use this endpoint, you need an API key with the subscription.status.set permission.

note

If you’re interested in using this endpoint with LINE subscription groups, contact your customer success manager. 

For LINE subscription groups, we recommend using a custom attribute to track website or app consent separately, and then targeting campaigns using that custom attribute in combination with the LINE subscription state. This approach ensures your subscription state accurately reflects users who have actually subscribed in the LINE app. Manually adding users to LINE subscription groups using the API may lead to out-of-sync states and failed sends since Braze cannot re-subscribe users in the LINE app or send messages to users who have blocked an account in LINE.

## Differences from V1

The V2 endpoint differs from the V1 endpoint in the following ways:

- Multiple subscription groups: V2 lets you update multiple subscription groups in a single API request, while V1 supports only one subscription group per request.
 
- Update both email and SMS in one call: When using external_ids, you can update both email and SMS subscription groups for the same users in a single API call. With V1, you must make separate API calls for email and SMS subscription groups.
 
- Using email or phone identifiers: If you use emails or phones instead of external_ids, you cannot update both email and SMS subscription groups in the same request. You must make separate API calls—one for email subscription groups and one for SMS subscription groups.

important

Phone number format: Phone numbers must be in E.164 format (for example, +12223334444). Phone numbers that are not in E.164 format are rejected.

## How Braze handles orphaned subscription states

An orphaned subscription state is a subscription state stored for a phone number or email address that isn’t associated with any user profile. For SMS, email, WhatsApp, and LINE, Braze handles orphaned subscription states as follows:

- If a user is deleted and is the only user associated with a given phone number or email address, the subscription state for that phone number or email address is deleted immediately.
 
- If you call /subscription/status/set or /v2/subscription/status/set with a phone number or email address that is not currently associated with any user profile, Braze stores that subscription state for up to 30 days, after which it is automatically deleted.

- If use_double_opt_in_logic is set to true and no user profile is associated with the provided phone number, the subscription state is not updated; a user must exist to enter the double opt-in workflow.

- If a new user profile is created with a phone number or email address that has an orphaned subscription state stored for it, that user inherits the stored subscription state but only within the 30-day window. This 30-day grace period is intentional and exists to handle race conditions when creating a user and setting its channel identifier’s subscription state happen in separate API calls. An example of this race condition is when a /subscription/status/set request is processed for a phone number before the /users/track request creating the corresponding user profile is processed.

## Rate limit

This endpoint has a rate limit of 5,000 requests per minute shared across the /subscription/status/set and /v2/subscription/status/set endpoint as documented in API rate limits.

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
{
 "subscription_groups":[
 {
 "subscription_group_id": (required, string),
 "subscription_state": (required, string),
 "external_ids": (required*, array of strings),
 "emails": (required*, array of strings),
 "phones": (required*, array of strings in E.164 format),
 "use_double_opt_in_logic": (optional, boolean)
 }
 ]
}

```
 | 

tip

When creating new users using the /users/track endpoint, you can set subscription groups within the user attributes object, which allows you to create a user and set the subscription group state in one API call.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 subscription_group_id | 
 Required | 
 String | 
 The id of your subscription group. | 

 subscription_state | 
 Required | 
 String | 
 Available values are unsubscribed (not in subscription group) or subscribed (in subscription group). | 

 external_ids | 
 Required* | 
 Array of strings | 
 The external_id of the user or users, may include up to 50 ids. | 

 emails | 
 Required* | 
 String or array of strings | 
 The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). 

If multiple users (external_id) in the same workspace share the same email address, all users that share the email address are updated with the subscription group changes. | 

 phones | 
 Required* | 
 String in E.164 format | 
 You can pass user phone numbers as an array of strings. Must include at least one phone number (up to 50). Phone numbers must be in E.164 format (for example, +12223334444). 

If multiple users (external_id) in the same workspace share the same phone number, then all users that share the phone number are updated with the same subscription group changes. | 

 use_double_opt_in_logic | 
 Optional | 
 Boolean | 
 Defaults to false if omitted. For SMS subscription groups, set to true to enter the user into the SMS double opt-in workflow when their subscription status is set to subscribed. Users entered into the double opt-in workflow in this way receive at most one opt-in prompt reply message per day, regardless of the number of times they are entered into the workflow. If this parameter is omitted or set to false, users are subscribed without entering the double opt-in workflow. This parameter is not applicable to email subscription groups. | 

important

Identifier selection:

- To update both email and SMS subscription groups in a single API call, use external_ids. You cannot include both emails and phones in the same request.
 
- If you use emails or phones instead of external_ids, make separate API calls—one for email subscription groups and one for SMS subscription groups.
 
- You can send emails, phones, or external_ids individually.

### Example requests

The following example uses external_ids to update both email and SMS subscription groups in a single API call. This is only possible when using external_ids—you cannot update both email and SMS subscription groups in one call when using emails or phones.

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
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "subscription_groups":[
 {
 "subscription_group_id":"subscription_group_identifier",
 "subscription_state":"subscribed",
 "external_ids":["example-user","[email protected]"]
 },
 {
 "subscription_group_id":"subscription_group_identifier",
 "subscription_state":"subscribed",
 "external_ids":["example-user","[email protected]"]
 }
 ]
}

```
 | 

## Email

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "subscription_groups":[
 {
 "subscription_group_id":"subscription_group_identifier",
 "subscription_state":"subscribed",
 "emails":["[email protected]","[email protected]"]
 }
 ]
}
'

```
 | 

## SMS and WhatsApp

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "subscription_groups":[
 {
 "subscription_group_id":"subscription_group_identifier",
 "subscription_state":"subscribed",
 "phones":["+12223334444","+15556667777"]
 }
 ]
}
'

```
 | 

- 

New Stuff!
