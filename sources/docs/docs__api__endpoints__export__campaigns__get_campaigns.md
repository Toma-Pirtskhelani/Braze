---
url: https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns
slug: docs__api__endpoints__export__campaigns__get_campaigns
title: "Export campaigns list"
description: "This article outlines details about the Export campaigns list Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export campaigns list

get

/campaigns/list

Use this endpoint to export a list of campaigns, each of which will include its name, campaign API identifier, whether it is an API campaign, and tags associated with the campaign.

The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the campaigns.list permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 page | 
 Optional | 
 Integer | 
 The page of campaigns to return, defaults to 0 (returns the first set of up to 100). | 

 include_archived | 
 Optional | 
 Boolean | 
 Whether or not to include archived campaigns, defaults to false. | 

 sort_direction | 
 Optional | 
 String | 
 - Sort creation time from newest to oldest: pass in the value desc.
 - Sort creation time from oldest to newest: pass in the value asc. 

If sort_direction is not included, the default order is oldest to newest. | 

 last_edit.time[gt] | 
 Optional | 
 Time | 
 Filters the results and only returns campaigns that were edited greater than the time provided till now. Format is yyyy-MM-DDTHH:mm:ss. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
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

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "campaigns" : [
 {
 "id" : (string) the Campaign API identifier,
 "last_edited": (ISO 8601 string) the last edited time for the message
 "name" : (string) the campaign name,
 "is_api_campaign" : (boolean) whether the campaign is an API campaign,
 "tags" : (array) the tag names associated with the campaign formatted as strings
 },
 ...
 ]
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
