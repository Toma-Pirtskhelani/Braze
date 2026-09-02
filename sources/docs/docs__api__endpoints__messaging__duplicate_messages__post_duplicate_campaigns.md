---
url: https://www.braze.com/docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns
slug: docs__api__endpoints__messaging__duplicate_messages__post_duplicate_campaigns
title: "Duplicate campaigns using the API"
description: "This article outlines details about the Duplicate campaigns endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Duplicate campaigns using the API

post

/campaigns/duplicate

core endpoint

Use this endpoint to duplicate campaigns. This API endpoint is similar to duplicating campaigns in the Braze dashboard.

## Prerequisites

To use this endpoint, you’ll need to generate an API key with the campaigns.duplicate permission.

## Rate limit

This endpoint is limited to 100 API calls per minute.

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
 "campaign_id": (required, string) The campaign identifier,
 "name": (required, string) The name of the resulting campaign,
 "description": (optional, string) The description of the resulting campaign,
 "tag_names": (optional, array of strings) The tags of the resulting campaign,
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 campaign_id | 
 Required | 
 String | 
 See campaign identifier. | 

 name | 
 Required | 
 String | 
 The name of the resulting campaign. | 

 description | 
 Optional | 
 String | 
 The description field for the resulting campaign. | 

 tag_names | 
 Optional | 
 Array of strings | 
 The tags for the resulting campaign. These must be existing tags. If you add new tags in the request, they overwrite any tags that were on the original campaign. | 

## Response

This endpoint returns a 202 status code, and the campaign creation occurs asynchronously. You can use the security event download to see records of when campaigns were duplicated and by which API key.

- 

New Stuff!
