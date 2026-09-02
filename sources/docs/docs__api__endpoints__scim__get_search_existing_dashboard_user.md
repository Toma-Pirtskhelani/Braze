---
url: https://www.braze.com/docs/api/endpoints/scim/get_search_existing_dashboard_user
slug: docs__api__endpoints__scim__get_search_existing_dashboard_user
title: "Search existing dashboard user account by email"
description: "This article outlines details about the Search for an existing dashboard user account by email Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Search existing dashboard user account by email

get

scim/v2/Users?filter=userName%20eq%20”user%40test.com”

Use this endpoint to look up an existing dashboard user account by specifying their email in the filter query parameter.

Note that when the query parameter is URL encoded, it reads like this:

/scim/v2/Users?filter=userName%20eq%20%[email protected]%22

See me in Postman

important

This endpoint requires the custom SCIM integration. If you set up an identity provider (IdP) integration (Okta or Entra ID), you can’t use this endpoint; only one SCIM bridge can be set up per company.

## Prerequisites

To use this endpoint, you’ll need a SCIM token. You’ll use your service origin as the X-Request-Origin header. For more information, refer to Automated user provisioning.

## Rate limit

This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the /scim/v2/Users/ PUT, GET, DELETE, and POST endpoints as documented in API rate limits.

## Query parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 filter | 
 Required | 
 String | 
 SCIM filter expression to search by email. Braze supports userName eq "[email protected]" only. The email value must be wrapped in double quotes. | 

important

Braze only supports exact-match filters on userName using the eq operator. Other SCIM filter fields or operators return a 400 response.

## Request parameters

```

1
2
3

```
 | 
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE

```
 | 

note

If you receive a 401 response, confirm you’re using a SCIM token (not a REST API key), that X-Request-Origin matches your service origin, and that your IP address is on the SCIM allowlist. For details, refer to Automated user provisioning.

## Example request

```

1
2
3
4

```
 | 
```
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%[email protected]%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34

```
 | 
```
{
 "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
 "totalResults": 1,
 "Resources": [
 {
 "userName": "[email protected]",
 "id": "dfa245b7-24195aec-887bb3ad-602b3340",
 "name": {
 "givenName": "Test",
 "familyName": "User"
 },
 "department": "finance",
 "createdAt": "2024 Nov 11, 4:20 PM",
 "lastSignInAt": "N/A",
 "permissions": {
 "companyPermissions": ["manage_company_settings"],
 "appGroup": [
 {
 "appGroupId": "241adcd25789fabcded",
 "appGroupName": "Test Workspace",
 "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
 "team": [
 {
 "teamId": "241adcd25789fabcded",
 "teamName": "Test Team",
 "teamPermissions": ["admin"]
 }
 ]
 }
 ]
 }
 }
 ]
}

```
 | 

## Response parameters

 Parameter | 
 Data type | 
 Description | 

 schemas | 
 Array of strings | 
 SCIM list response schema. | 

 totalResults | 
 Integer | 
 Number of matching dashboard users (0 if no match). | 

 Resources | 
 Array | 
 Array of user objects. Each object uses the same fields as GET: Look up an existing dashboard user account. | 

### User object fields

 Parameter | 
 Data type | 
 Description | 

 id | 
 String | 
 The user’s resource ID. | 

 userName | 
 String | 
 The user’s email address. | 

 name | 
 Object | 
 Contains givenName and familyName. | 

 department | 
 String | 
 The user’s department, if set. | 

 createdAt | 
 String | 
 When the user account was created. Returns N/A when unset; otherwise formatted as YYYY Mon DD, H:MM AM/PM. | 

 lastSignInAt | 
 String | 
 When the user last signed in. Returns N/A if the user has not signed in; otherwise formatted as YYYY Mon DD, H:MM AM/PM. | 

 permissions | 
 Object | 
 Company, workspace, team, and role permissions. See the permissions object. | 

### Error states

If the filter parameter is missing or malformed, the endpoint returns:

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
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
 "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
 "status": 400,
 "detail": "Request is unparsable, syntactically incorrect, or violates schema."
}

```
 | 

- 

New Stuff!
