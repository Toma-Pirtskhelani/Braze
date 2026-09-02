---
url: https://www.braze.com/docs/api/endpoints/translations/campaigns/get_source_campaign
slug: docs__api__endpoints__translations__campaigns__get_source_campaign
title: "View default source values for a campaign’s translation tags"
description: "This article outlines details about the campaign translation source endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View default source values for a campaign’s translation tags

get

/campaigns/translations/source

Use this endpoint to view all the default translation sources for a campaign’s translation tags. These are the values within the {% translation id %} source {% endtranslation %}. See Locales in messages for more information about translation features.

## Prerequisites

To use this endpoint, you’ll need an API key with the campaigns.translations.get permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per minute.

## Query parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 campaign_id | 
 Required | 
 String | 
 The ID of your campaign. | 

 message_variation_id | 
 Required | 
 String | 
 The ID of your message variation. | 

 locale_id | 
 Optional | 
 String | 
 A locale UUID to filter the responses. | 

 post_launch_draft_version | 
 Optional | 
 Boolean | 
 When true returns the latest draft version instead of the latest live published version. Defaults to false returning the latest live version. | 

note

All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint’s response.

## Example request

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

There are four status code responses for this endpoint: 200, 400, 404, and 429.

### Example success response

The status code 200 could return the following response header and body.

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
{
 "translations": {
 "translation_map": {
 "id_0": "Here's a Million Dollars",
 "id_1": "Hello World!"
 }
 },
 "message": "success"
}

```
 | 

### Example error response

The status code 400 could return the following response body. Refer to Troubleshooting for more information about errors you may encounter.

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
{
 "errors": [
 {
 "message": "This message does not support multi-language."
 }
 ]
}

```
 | 

- 

New Stuff!
