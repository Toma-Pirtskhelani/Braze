---
url: https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks
slug: docs__api__endpoints__templates__content_blocks_templates__get_list_email_content_blocks
title: "List available Content Blocks"
description: "This article outlines details about the List available Content Blocks Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List available Content Blocks

get

/content_blocks/list

Use this endpoint to list your existing Content Blocks information.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the content_blocks.list permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 modified_after | 
 Optional | 
 String in ISO-8601 format | 
 Retrieve only Content Blocks updated at or after the given time. | 

 modified_before | 
 Optional | 
 String in ISO-8601 format | 
 Retrieve only Content Blocks updated at or before the given time. | 

 limit | 
 Optional | 
 Positive Number | 
 Maximum number of Content Blocks to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000. | 

 offset | 
 Optional | 
 Positive Number | 
 Number of Content Blocks to skip before returning rest of the templates that fit the search criteria. | 

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'

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

```
 | 
```
{
 "count": "integer",
 "content_blocks": [
 {
 "content_block_id": (string) the Content Block identifier,
 "name": (string) the name of the Content Block,
 "content_type": (string) the content type, html or text,
 "liquid_tag": (string) the Liquid tags,
 "inclusion_count" : (integer) the inclusion count,
 "created_at": (string) The time the Content Block was created in ISO 8601,
 "last_edited": (string) The time the Content Block was last edited in ISO 8601,
 "tags": (array) An array of tags formatted as strings
 }
 ]
}

```
 | 

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

 Error | 
 Troubleshooting | 

 Modified after time is invalid | 
 The provided date is not a valid or parsable date. Reformat this value as a string in ISO 8601 format (yyyy-mm-ddThh:mm:ss.ffffff). | 

 Modified before time is invalid | 
 The provided date is not a valid or parsable date. Reformat this value as a string in ISO 8601 format (yyyy-mm-ddThh:mm:ss.ffffff). | 

 Modified after time must be earlier than or the same as modified before time. | 
 Change the modified_after value to a time that is earlier than the modified_before time. | 

 Content Block number limit is invalid | 
 The limit parameter must be an integer (positive number) greater than 0. | 

 Content Block number limit must be greater than 0 | 
 Change the limit parameter to an integer greater than 0. | 

 Content Block number limit exceeds maximum of 1000 | 
 Change the limit parameter to an integer less than 1000. | 

 Offset is invalid | 
 The offset parameter must be an integer greater than 0. | 

 Offset must be greater than 0 | 
 Change the offset parameter to an integer greater than 0. | 

- 

New Stuff!
