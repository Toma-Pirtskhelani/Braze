---
url: https://www.braze.com/docs/api/endpoints/scim/delete_existing_dashboard_user
slug: docs__api__endpoints__scim__delete_existing_dashboard_user
title: "Remove dashboard user account"
description: "This article outlines details about the Remove a dashboard user account Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Remove dashboard user account

delete

/scim/v2/Users/{id}

Use this endpoint to permanently delete an existing dashboard user by specifying the resource id returned by the SCIM POST method.

This is similar to deleting a user in the Company Users section of the Braze dashboard.

See me in Postman

important

This endpoint requires the custom SCIM integration. If you set up an identity provider (IdP) integration (Okta or Entra ID), you can’t use this endpoint; only one SCIM bridge can be set up per company.

## Prerequisites

To use this endpoint, you’ll need a SCIM token. You’ll use your service origin as the X-Request-Origin header. For more information, refer to Automated user provisioning.

## Rate limit

This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the /scim/v2/Users/ PUT, GET, and POST endpoints as documented in API rate limits.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 id | 
 Required | 
 String | 
 The user’s resource ID. This parameter is returned by the POST /scim/v2/Users/ or GET /scim/v2/Users?filter=userName eq "[email protected]" methods. | 

## Request body

```

1
2
3

```
 | 
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY

```
 | 

## Example request

```

1
2
3
4

```
 | 
```
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \

```
 | 

## Response

### Example error response

```

1
2

```
 | 
```
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8

```
 | 

If a developer with this ID doesn’t exist in Braze, the endpoint will respond with:

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
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
 "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
 "detail": "User not found",
 "status": 404
}

```
 | 

- 

New Stuff!
