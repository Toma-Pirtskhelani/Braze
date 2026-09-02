---
url: https://www.braze.com/docs/api/endpoints/preference_center/put_update_preference_center
slug: docs__api__endpoints__preference_center__put_update_preference_center
title: "Update preference center"
description: "This article outlines details about the Update a preference center Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update preference center

put

/preference_center/v1/{preferenceCenterExternalID}

Use this endpoint to update a preference center.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the preference_center.update permission.

## Rate limit

This endpoint has a rate limit of 10 requests per minute, per workspace, as documented in API rate limits.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 preferenceCenterExternalID | 
 Required | 
 String | 
 The ID for your preference center. | 

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

```
 | 
```
{
 "name": "preference_center_name",
 "preference_center_title": "string",
 "preference_center_page_html": "string",
 "confirmation_page_html": "string",
 "options": {
 "unknown macro": {links-tags}
 "options": {
 "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag,
 "links-tags": [
 {
 "rel": "string", (required) One of: "icon", "shortcut icon", or "apple-touch-icon",
 "type": "string", (optional) Valid values: "image/png", "image/svg", "image/gif", "image/x-icon", "image/svg+xml", "mask-icon",
 "sizes": "string", (optional),
 "color": "string", (optional) Use when type="mask-icon",
 "href": "string", (required)
 }
 ]
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 preference_center_page_html | 
 Required | 
 String | 
 The HTML for the preference center page. | 

 preference_center_title | 
 Optional | 
 String | 
 The title for the preference center and confirmation pages. If a title is not specified, the title of the pages will default to “Preference Center”. | 

 confirmation_page_html | 
 Required | 
 String | 
 The HTML for the confirmation page. | 

 state | 
 Optional | 
 String | 
 Choose active or draft. | 

 options | 
 Optional | 
 Object | 
 Attributes: 
meta-viewport-content: When present, a viewport meta tag will be added to the page with content= <value of attribute>.

 link-tags: Set a favicon for the page. When set, a <link> tag with a rel attribute is added to the page. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
 "name": "Example",
 "preference_center_title": "Example Preference Center Title",
 "preference_center_page_html": "HTML for preference center here",
 "confirmation_page_html": "HTML here with a message to users here",
 "state": "active"
}
'

```
 | 

## Example response

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
 "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
 "created_at": "2022-09-22T18:28:07Z",
 "updated_at": "2022-09-22T18:32:07Z",
 "message": "success"
}

```
 | 

- 

New Stuff!
