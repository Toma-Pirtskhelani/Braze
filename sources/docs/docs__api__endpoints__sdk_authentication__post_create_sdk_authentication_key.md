---
url: https://www.braze.com/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key
slug: docs__api__endpoints__sdk_authentication__post_create_sdk_authentication_key
title: "Create SDK Authentication key"
description: "This article outlines details about the Create SDK Authentication key Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create SDK Authentication key

post

/app_group/sdk_authentication/create

Use this endpoint to create a new SDK Authentication key for your app.

## Prerequisites

To use this endpoint, you’ll need an API key with the sdk_authentication.create permission.

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
5
6

```
 | 
```
{
 "app_id": "App API identifier",
 "rsa_public_key_str": "RSA public key string",
 "description": "description",
 "make_primary": false
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data type | 
 Description | 

 app_id | 
 Required | 
 String | 
 The app API identifier. | 

 rsa_public_key_str | 
 Required | 
 String | 
 The RSA public key string. Must be a valid RSA public key or it will return an error. | 

 description | 
 Required | 
 String | 
 Description for the SDK Authentication key. | 

 make_primary | 
 Optional | 
 Boolean | 
 If set to true, this key will be made the primary SDK Authentication key when it is created. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "app_id": "01234567-89ab-cdef-0123-456789abcdef",
 "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
 "description": "SDK Authentication Key for iOS App",
 "make_primary": false
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
 "id": "key id"
}

```
 | 

## Response parameters

 Parameter | 
 Data type | 
 Description | 

 id | 
 String | 
 The ID of the newly created SDK Authentication key. | 

### Validation rules

This endpoint has the following validation rules:

- You can have up to 3 SDK Authentication keys per app.
 
- The RSA public key string must be a valid RSA public key in the proper format.
 
- The app_id must be a valid app API identifier.
 
- The description cannot be empty.

- 

New Stuff!
