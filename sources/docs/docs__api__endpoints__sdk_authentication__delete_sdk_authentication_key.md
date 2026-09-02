---
url: https://www.braze.com/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key
slug: docs__api__endpoints__sdk_authentication__delete_sdk_authentication_key
title: "Delete SDK Authentication key"
description: "This article outlines details about the Delete SDK Authentication key Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete SDK Authentication key

delete

/app_group/sdk_authentication/delete

Use this endpoint to delete an SDK Authentication key for your app.

important

The primary key can’t be deleted. If you attempt to delete the primary key, this endpoint will return an error.

## Prerequisites

To use this endpoint, you’ll need an API key with the sdk_authentication.delete permission.

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
 "app_id": "App API Identifier",
 "key_id": "key id"
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

 key_id | 
 Required | 
 String | 
 The ID of the SDK Authentication key to delete. | 

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
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "app_id": "01234567-89ab-cdef-0123-456789abcdef",
 "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
}'

```
 | 

## Response

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
{
 "keys": [
 {
 "id": "abcdef12-3456-7890-abcd-ef1234567890",
 "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
 "description": "SDK Authentication Key for iOS App",
 "is_primary": true
 }
 ]
}

```
 | 

## Response parameters

 Parameter | 
 Data type | 
 Description | 

 keys | 
 Array | 
 Array of remaining SDK Authentication key objects. | 

 keys[].id | 
 String | 
 The ID of the SDK Authentication key. | 

 keys[].rsa_public_key | 
 String | 
 The RSA public key string. | 

 keys[].description | 
 String | 
 Description of the SDK Authentication key. | 

 keys[].is_primary | 
 Boolean | 
 Whether this key is the primary SDK Authentication key. | 

### Validation rules

This endpoint has the following validation rules:

- The key_id must be a valid SDK Authentication key ID.
 
- The app_id must be a valid app API identifier.
 
- The SDK Authentication key must exist for the specified app.
 
- The primary SDK Authentication key can’t be deleted.

- 

New Stuff!
