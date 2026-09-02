---
url: https://www.braze.com/docs/api/endpoints/scim/post_create_user_account
slug: docs__api__endpoints__scim__post_create_user_account
title: "Create new dashboard user account"
description: "This article outlines details about the Create new dashboard user account Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create new dashboard user account

post

/scim/v2/Users

Use this endpoint to create a new dashboard user account by specifying email, given and family names, permissions (for setting permissions at the company, workspace, and team level).

See me in Postman

important

This endpoint requires the custom SCIM integration. If you set up an identity provider (IdP) integration (Okta or Entra ID), you can’t use this endpoint; only one SCIM bridge can be set up per company.

## Prerequisites

To use this endpoint, you’ll need a SCIM token. You’ll use your service origin as the X-Request-Origin header. For more information, refer to Automated user provisioning.

## Rate limit

This endpoint has a rate limit of 5000 requests per day, per company. This rate limit is shared with the /scim/v2/Users/ PUT, GET, and DELETE endpoints as documented in API rate limits.

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
Authorization: Bearer YOUR-SCIM-TOKEN-KEY

```
 | 

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

```
 | 
```
{
 "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
 "userName": "[email protected]",
 "name": {
 "givenName": "Test",
 "familyName": "User"
 },
 "department": "finance",
 "permissions": {
 "companyPermissions": ["manage_company_settings"],
 "roles": [
 {
 "roleName": "Test Role"
 },
 {
 "roleId": "2519dafcdba238ae7"
 }
 ],
 "appGroup": [
 {
 "appGroupName": "Test Workspace",
 "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
 "team": [
 {
 "teamName": "Test Team",
 "teamPermissions": ["basic_access","export_user_data"]
 }
 ]
 },
 {
 "appGroupName": "Other Test Workspace",
 "appGroupPermissionSets": [
 {
 "appGroupPermissionSetName": "Test Permission Set"
 }
 ]
 }
 ]
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data type | 
 Description | 

 schemas | 
 Required | 
 Array of strings | 
 Expected SCIM 2.0 schema name for the user object. | 

 userName | 
 Required | 
 String | 
 The user’s email address. | 

 name | 
 Required | 
 JSON object | 
 This object contains the user’s given name and family name. | 

 department | 
 Required | 
 String | 
 Valid department string from the department string documentation. | 

 permissions | 
 Optional | 
 JSON object | 
 Permissions object as described in the permissions object documentation. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM–TOKEN-HERE' \
--data raw '{
 "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
 "userName": "[email protected]",
 "name": {
 "givenName": "Test",
 "familyName": "User"
 },
 "department": "finance",
 "permissions": {
 "companyPermissions": ["manage_company_settings"],
 "roles": [
 {
 "roleName": "Test Role"
 },
 {
 "roleId": "2519dafcdba238ae7"
 }
 ],
 "appGroup": [
 {
 "appGroupName": "Test Workspace",
 "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
 "team": [
 {
 "teamName": "Test Team",
 "teamPermissions": ["basic_access","export_user_data"]
 }
 ]
 }
 ]
 }
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
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73

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
 "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
 "permissions": {
 "companyPermissions": ["manage_company_settings"],
 "roles": [
 {
 "roleName": "Test Role",
 "roleId": "519dafcdba23dfaae7",
 "appGroup": [
 {
 "appGroupId": "241adcd25789fabcded",
 "appGroupName": "Some Workspace",
 "appGroupPermissions": ["basic_access", "publish_cards"],
 "team": [
 {
 "teamId": "2519dafcdba238ae7",
 "teamName": "Some Team",
 "teamPermissions": ["export_user_data"]
 }
 ]
 }
 ]
 },
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
 "teamId": "2519dafcdba238ae7",
 "teamName": "Test Team",
 "teamPermissions": ["basic_access","export_user_data"]
 }
 ]
 },
 {
 "appGroupName": "Other Test Workspace",
 "appGroupPermissionSets": [
 {
 "appGroupPermissionSetName": "Test Permission Set"
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
 Expected SCIM 2.0 schema name for the user object. | 

 userName | 
 String | 
 The user’s email address. | 

 name | 
 JSON object | 
 This object contains the user’s first name and family name. | 

 department | 
 String | 
 Valid department string from the department string documentation. | 

 permissions | 
 JSON object | 
 Permissions object as described in the permissions object documentation. | 

 id | 
 String | 
 ID generated by Braze that is used for searching and managing user accounts. | 

 lastSignInAt | 
 String | 
 Date of last successful sign-on in UTC time. | 

### Error states

If a user with this userName or email address already exists in Braze, the endpoint will respond with:

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
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
 "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
 "detail": "User already exists in the database.",
 "status": 409
}

```
 | 

- 

New Stuff!
