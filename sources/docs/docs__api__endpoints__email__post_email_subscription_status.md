---
url: https://www.braze.com/docs/api/endpoints/email/post_email_subscription_status
slug: docs__api__endpoints__email__post_email_subscription_status
title: "Change email subscription status"
description: "This article outlines the details about the Change user's email subscription status Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Change email subscription status

post

/email/status

core endpoint

Use this endpoint to set the global email subscription state for your users.

Users can be opted_in, unsubscribed, or subscribed (not specifically opted in or out).

note

This endpoint updates the user’s global email subscription state, which is different from subscription group status. The global subscription state applies across all emails, while subscription groups allow more granular control over specific types of emails. When a user is globally unsubscribed, they won’t receive emails regardless of their subscription group status. To query subscription group status, use the List user’s subscription group status endpoint.

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded is automatically set.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the email.status permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

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

```
 | 
```
{
 "email": "[email protected]",
 "subscription_state": "subscribed"
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 email | 
 Required | 
 String or array | 
 String email address to modify, or an array of up to 50 email addresses to modify. | 

 subscription_state | 
 Required | 
 String | 
 Either “subscribed”, “unsubscribed”, or “opted_in”. | 

## Troubleshooting SendGrid email blocks

When SendGrid blocks a recipient, update subscription status with this endpoint and review engagement with segment filters. Use Currents soft-bounce events for deliverability monitoring, and confirm subscription state before retrying sends.

## Example request

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
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
 "email": "[email protected]",
 "subscription_state": "subscribed"
}'

```
 | 

- 

New Stuff!
