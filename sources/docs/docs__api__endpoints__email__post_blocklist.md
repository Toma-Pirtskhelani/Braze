---
url: https://www.braze.com/docs/api/endpoints/email/post_blocklist
slug: docs__api__endpoints__email__post_blocklist
title: "Blocklist emails"
description: "This article outlines the details about the Blocklist emails Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Blocklist emails

post

/email/blocklist

core endpoint

Use this endpoint to unsubscribe a user from email and mark them as hard bounced.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the email.blacklist permission.

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
 "email": ["blocklist_email1","blocklist_email2"]
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
 String email address to blocklist, or an array of up to 50 email addresses to blocklist. | 

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
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
 "email": ["blocklist_email1","blocklist_email2"]
}'

```
 | 

- 

New Stuff!
