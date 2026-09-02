---
url: https://www.braze.com/docs/api/endpoints/preference_center/get_view_details_preference_center
slug: docs__api__endpoints__preference_center__get_view_details_preference_center
title: "View details for preference center"
description: "This article outlines details about the View details for preference center Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View details for preference center

get

/preference_center/v1/{preferenceCenterExternalID}

Use this endpoint to view the details for your preference centers, including when it was created and updated.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the preference_center.get permission.

## Rate limit

This endpoint has a rate limit of 1,000 requests per minute, per workspace, as documented in API rate limits.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 preferenceCenterExternalID | 
 Required | 
 String | 
 The ID for your preference center. | 

## Request parameters

There are no request parameters for this endpoint.

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

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

```
 | 
```
{
 "name": "My Preference Center",
 "preference_center_api_id": "preference_center_api_id",
 "created_at": "example_time_created",
 "updated_at": "example_time_updated",
 "preference_center_title": "Example preference center title",
 "preference_center_page_html": "HTML for preference center here",
 "confirmation_page_html": "HTML for confirmation page here",
 "redirect_page_html": null,
 "preference_center_options": {
 "meta-viewport-content": "width=device-width, initial-scale=2"
 },
 "state": "active"
}

```
 | 

- 

New Stuff!
