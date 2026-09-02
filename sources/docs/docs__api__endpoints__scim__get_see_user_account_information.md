---
url: https://www.braze.com/docs/api/endpoints/scim/get_see_user_account_information
slug: docs__api__endpoints__scim__get_see_user_account_information
title: "Look up an existing dashboard user account by resource ID"
description: "This article outlines details about the Look up an existing dashboard user account resource ID Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Look up an existing dashboard user account by resource ID

get

/scim/v2/Users/{id}

Use this endpoint to look up an existing dashboard user account by specifying the resource id returned by the SCIM POST method.

See me in Postman

important

This endpoint requires the custom SCIM integration. If you set up an identity provider (IdP) integration (Okta or Entra ID), you can’t use this endpoint; only one SCIM bridge can be set up per company.

## Prerequisites

To use this endpoint, you’ll need a SCIM token. You’ll use your service origin as the X-Request-Origin header. For more information, refer to Automated user provisioning.

## Rate limit

This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the /scim/v2/Users/ PUT, GET, DELETE, and POST endpoints as documented in API rate limits.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 id | 
 Required | 
 String | 
 The user’s resource ID. This parameter is returned by the POST /scim/v2/Users/ or GET /scim/v2/Users?filter=userName eq "[email protected]" methods. | 

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
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
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
35
36
37
38
39
40
41
42
43
44
45
46
47
48

```
 | 
```
{
 "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
 "id": "dfa245b7-24195aec-887bb3ad-602b3340",
 "userName": "[email protected]",
 "name": {
 "givenName": "Test",
 "familyName": "User"
 },
 "department": "finance",
 "lastSignInAt": "2024 Nov 11, 4:20 PM",
 "createdAt": "2024 Nov 11, 4:20 PM",
 "permissions": {
 "companyPermissions": ["manage_company_settings"],
 "roles": [
 {
 "roleName": "Another Test Role",
 "roleId": "23125dad23dfaae7",
 "appGroup": [
 {
 "appGroupId": "241adcd25adfabcded",
 "appGroupName": "Production Workspace",
 "appGroupPermissionSets": [
 {
 "appGroupPermissionSetName": "A Permission Set",
 "appGroupPermissionSetId": "dfa385109bc38",
 "permissions": ["basic_access","publish_cards"]
 }
 ]
 }
 ]
 }
 ],
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

```
 | 

## Response parameters

 Parameter | 
 Data type | 
 Description | 

 schemas | 
 Array of strings | 
 SCIM user schema. | 

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
 Company, workspace, team, and role permissions for the user. See the permissions object. | 

### Error states

If no user exists for the provided resource id, the endpoint returns:

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
Content-Type: application/json

{
 "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
 "status": 404,
 "detail": "Resource not found"
}

```
 | 

- 

New Stuff!
