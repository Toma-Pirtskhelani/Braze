---
url: https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status
slug: docs__api__endpoints__subscription_groups__post_update_user_subscription_group_status
title: "Update user’s subscription group status"
description: "This article outlines details about the Update user's subscription group status Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update user’s subscription group status

post

/subscription/status/set

core endpoint

Use this endpoint to batch update the subscription state of up to 50 users on the Braze dashboard.

You can access a subscription group’s subscription_group_id by navigating to the Subscription Group page.

If you want to see examples or test this endpoint for Email Subscription Groups:

See me in Postman

If you want to see examples or test this endpoint for SMS and RCS Subscription Groups:

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the subscription.status.set permission.

note

If you’re interested in using this endpoint with LINE subscription groups, contact your customer success manager.

## How Braze handles orphaned subscription states

An orphaned subscription state is a subscription state stored for a phone number or email address that isn’t associated with any user profile. For SMS, email, WhatsApp, and LINE, Braze handles orphaned subscription states as follows:

- If a user is deleted and is the only user associated with a given phone number or email address, the subscription state for that phone number or email address is deleted immediately.
 
- If you call /subscription/status/set or /v2/subscription/status/set with a phone number or email address that is not currently associated with any user profile, Braze stores that subscription state for up to 30 days, after which it is automatically deleted.

- If use_double_opt_in_logic is set to true and no user profile is associated with the provided phone number, the subscription state is not updated; a user must exist to enter the double opt-in workflow.

- If a new user profile is created with a phone number or email address that has an orphaned subscription state stored for it, that user inherits the stored subscription state but only within the 30-day window. This 30-day grace period is intentional and exists to handle race conditions when creating a user and setting its channel identifier’s subscription state happen in separate API calls. An example of this race condition is when a /subscription/status/set request is processed for a phone number before the /users/track request creating the corresponding user profile is processed.

## Rate limit

This endpoint has a rate limit of 5,000 requests per minute shared across the /subscription/status/set and /v2/subscription/status/set endpoint as documented in API rate limits.

## Request body

- sms and rcs
 
- email

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

```
 | 
```
{
 "subscription_group_id": (required, string) the id of your subscription group,
 "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
 "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
 "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
 "use_double_opt_in_logic": (optional, boolean) defaults to `false`; when `subscription_state` is "subscribed", set to `true` to enter the user into the SMS double opt-in workflow,
 // SMS and RCS subscription group - you must include one of external_id or phone
 }

```
 | 

* SMS and RCS subscription groups: Braze accepts only external_id or phone.

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

```
 | 
```
{
 "subscription_group_id": (required, string) the id of your subscription group,
 "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
 "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
 "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
 // Email subscription group - you must include one of external_id or email
 // Note that sending an email address that is linked to multiple profiles updates all relevant profiles
 }

```
 | 

* Email subscription groups: You must include either email or external_id.

This property should not be used for updating a user’s profile information. Use the /users/track property instead.

tip

Adding existing users to a subscription group: This endpoint is the recommended way to backfill or bulk-update subscription group membership for existing users. You can pass up to 50 external_ids, email addresses, or phone numbers per request. Users can also update their own subscription status through an email preference center link.

Creating new users with a subscription group: When creating new users using the /users/track endpoint, you can set subscription groups within the user attributes object, which allows you to create a user and set the subscription group state in one API call.

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

 external_id | 
 Required* | 
 Array of strings | 
 The external_id of the user or users, may include up to 50 ids. | 

 email | 
 Required* | 
 String or array of strings | 
 The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). 

If multiple users (external_id) in the same workspace share the same email address, then Braze updates all users that share the email address with the subscription group changes. | 

 phone | 
 Required* | 
 String in E.164 format | 
 The phone number of the user, can be passed as an array of strings. Must include at least one phone number (up to 50). 

If multiple users (external_id) in the same workspace share the same phone number, then Braze updates all users that share the phone number with the same subscription group changes. | 

 use_double_opt_in_logic | 
 Optional | 
 Boolean | 
 Applies only to SMS subscription groups; ignored for email and other subscription group types. Defaults to false if omitted. For SMS subscription groups, set to true to enter the user into the SMS double opt-in workflow when their subscription status is set to subscribed. Users entered into the double opt-in workflow in this way receive at most one opt-in prompt reply message per day, regardless of the number of times they are entered into the workflow. If this parameter is omitted or set to false, users are subscribed without entering the double opt-in workflow. | 

## Example requests

### Email

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
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "subscription_group_id": "subscription_group_identifier",
 "subscription_state": "unsubscribed",
 "external_id": "external_identifier",
 "email": ["[email protected]", "[email protected]"]
}
'

```
 | 

### SMS and RCS

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
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "subscription_group_id": "subscription_group_identifier",
 "subscription_state": "unsubscribed",
 "external_id": "external_identifier",
 "phone": ["+12223334444", "+11112223333"]
}
'

```
 | 

## Example success response

The status code 201 could return the following response body.

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

## Troubleshooting intermittent update failures

If subscription group updates intermittently fail or appear out of sync, wait several minutes between update requests or call /subscription/user/status to confirm the user’s state before sending another update.

important

The endpoint accepts only the email or phone value, not both. If you provide both, you receive this response: {"message":"Either an email address or a phone number should be provided, but not both."}

For your subscription update to apply to phone numbers, confirm you sent E.164-formatted phone numbers (for example, +15555550123), used the correct subscription_group_id, and passed phone (not both phone and email) in the same request body. For multi-number updates, use the phone array format shown in SMS and RCS.

- 

New Stuff!
