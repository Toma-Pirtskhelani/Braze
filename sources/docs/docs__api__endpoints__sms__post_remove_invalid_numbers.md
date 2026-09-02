---
url: https://www.braze.com/docs/api/endpoints/sms/post_remove_invalid_numbers
slug: docs__api__endpoints__sms__post_remove_invalid_numbers
title: "Remove invalid phone numbers"
description: "This article outlines details about the Remove invalid phone numbers Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Remove invalid phone numbers

post

/sms/invalid_phone_numbers/remove

Use this endpoint to remove “invalid” phone numbers from our invalid list.

This can be used to re-validate phone numbers after they have been marked as invalid.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the sms.invalid_phone_numbers.remove permission.

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
 "phone_numbers": (required, array of string in e.164 format)
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 phone_numbers | 
 Required | 
 Array of strings in e.164 format | 
 An array of up to 50 phone numbers to modify. | 

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
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "phone_numbers" : ["12183095514","14255551212"]
}'

```
 | 

- 

New Stuff!
