---
url: https://www.braze.com/docs/api/endpoints/preference_center/get_create_url_preference_center
slug: docs__api__endpoints__preference_center__get_create_url_preference_center
title: "Generate preference center URL"
description: "This article outlines details about the Generate preference center URL Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Generate preference center URL

get

/preference_center/v1/{preferenceCenterExternalID}/url/{userID}

Use this endpoint to generate a URL for a preference center.

Each preference center URL is unique to each user.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the preference_center.user.get permission.

## Rate limit

This endpoint has a rate limit of 1,000 requests per minute, per workspace, as documented in API rate limits.

This rate limit is fixed and is not configurable.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 preferenceCenterExternalID | 
 Required | 
 String | 
 The ID for your preference center. | 

 userID | 
 Required | 
 String | 
 The user ID. | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 preference_center_api_id | 
 Required | 
 String | 
 The ID for your preference center. | 

 external_id | 
 Required | 
 String | 
 The external ID for a user. | 

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'

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
 "preference_center_url": "https://www.example.com/preferences"
}

```
 | 

note

This endpoint only generates URLs for the new preference center (such as preference centers created using our API or the drag-and-drop editor).

- 

New Stuff!
