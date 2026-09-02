---
url: https://www.braze.com/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status
slug: docs__api__endpoints__subscription_groups__get_list_user_subscription_group_status
title: "List user’s subscription group status"
description: "This article outlines details about the List user's subscription group status Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List user’s subscription group status

get

/subscription/status/get

Use this endpoint to get the subscription state of a user in a subscription group.

These groups will be available on the Subscription Group page. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.

If you collect email through a custom form and then set subscription group membership through the REST API, call this endpoint first to check whether a profile already exists. If no matching profile exists, create or subscribe the user with the Update user’s subscription group status endpoint. Otherwise, update the existing profile instead of creating a duplicate. For other collection patterns, see Collection best practices.

If you want to see examples or test this endpoint for Email Subscription Groups:

See me in Postman

If you want to see examples or test this endpoint for SMS Subscription Groups:

See me in Postman

If you want to see examples or test this endpoint for WhatsApp Groups:

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the subscription.status.get permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 subscription_group_id | 
 Required | 
 String | 
 The id of your subscription group. | 

 external_id | 
 Required* | 
 String | 
 The external_id of the user (must include at least one and at most 50 external_ids). 

When both an external_id and email/phone are submitted, only the external_id(s) provided will be applied to the result query. | 

 email | 
 Required* | 
 String | 
 The email address of the user. It can be passed as an array of strings with a maximum of 50.

 Submitting both an email address and phone number (with no external_id) will result in an error. | 

 phone | 
 Required* | 
 String in E.164 format | 
 The phone number of the user. If email is not included, you must include at least one phone number (with a maximum of 50).

 Submitting both an email address and phone number (with no external_id) will result in an error. | 

*One of external_id or email or phone is required for each user.

- For SMS and WhatsApp subscription groups, either external_id or phone is required. When both are submitted, only the external_id is used for querying and the phone number is applied to that user.
 
- For email subscription groups, either external_id or email is required. When both are submitted, only the external_id is used for the query and the email address is applied to that user.

## Example request

- multiple users
 
- sms and whatsapp
 
- email

```

1

```
 | 
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2

```
 | 

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&[email protected]' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

All successful responses will return Subscribed, Unsubscribed, or Unknown depending on status and user history with the subscription group.

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
 "status": {
 "1": "Unsubscribed",
 "2": "Subscribed"
 },
 "message": "success"
}

```
 | 

important

This endpoint returns the subscription group status independently of the user’s global subscription state. If a user is globally unsubscribed, the Braze dashboard shows them as unsubscribed from each subscription group. However, this endpoint still returns the last saved subscription group status (for example, Subscribed) because the global subscription state supersedes individual subscription groups without overwriting them.

Braze preserves individual subscription group states so that if the user globally resubscribes, each subscription group reverts to its previously saved status. To determine a user’s effective subscription state, check both their global subscription status and the subscription group status returned by this endpoint.

- 

New Stuff!
