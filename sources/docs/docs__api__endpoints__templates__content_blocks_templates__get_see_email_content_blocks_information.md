---
url: https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information
slug: docs__api__endpoints__templates__content_blocks_templates__get_see_email_content_blocks_information
title: "See Content Block information"
description: "This article outlines details about the See Content Blocks information Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# See Content Block information

get

/content_blocks/info

Use this endpoint to call information for your existing Content Blocks.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the content_blocks.info permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 content_block_id | 
 Required | 
 String | 
 The Content Block identifier. 

You can find this by either listing Content Block information through an API call or going to the API Keys page, then scrolling to the bottom and searching for your Content Block API identifier. | 

 include_inclusion_data | 
 Optional | 
 Boolean | 
 When set to true, the API returns back the Message Variation API identifier of campaigns and Canvases where this Content Block is included, to be used in subsequent calls. The results exclude archived or deleted campaigns or Canvases. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
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
 "content_block_id": (string) the Content Block identifier,
 "name": (string) the name of the Content Block,
 "content": (string) the content in the Content Block,
 "description": (string) the Content Block description,
 "content_type": (string) the content type, html or text,
 "tags": (array) An array of tags formatted as strings,
 "created_at": (string) The time the Content Block was created in ISO 8601,
 "last_edited": (string) The time the Content Block was last edited in ISO 8601,
 "inclusion_count" : (integer) the inclusion count,
 "inclusion_data": (array) the inclusion data,
 "message": "success"
}

```
 | 

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

 Error | 
 Troubleshooting | 

 Content Block ID cannot be blank | 
 Make sure that a Content Block is listed in your request and is encapsulated in quotes (""). | 

 Content Block ID is invalid for this workspace | 
 This Content Block doesn’t exist or is in a different company account or workspace. | 

 Content Block has been deleted—content not available | 
 This Content Block, though it may have existed earlier, has been deleted. | 

 Include Inclusion Data—error | 
 This parameter only accepts boolean values (true or false). Make sure the value for include_inclusion_data is not encapsulated in quotes (""), which causes the value to be sent as a string instead. See request parameters for details. | 

- 

New Stuff!
