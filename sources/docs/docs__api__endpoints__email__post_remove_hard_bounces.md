---
url: https://www.braze.com/docs/api/endpoints/email/post_remove_hard_bounces
slug: docs__api__endpoints__email__post_remove_hard_bounces
title: "Remove hard bounced emails"
description: "This article outlines details about the Remove hard bounced email addresses Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Remove hard bounced emails

post

/email/bounce/remove

Use this endpoint to remove email addresses from your Braze bounce list and bounce list maintained by your email provider.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the email.bounce.remove permission.

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

```
 | 
```
{
 "email": "[email protected]"
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

## Example request

```

1
2
3
4
5
6

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "email": "[email protected]"
}'

```
 | 

- 

New Stuff!
