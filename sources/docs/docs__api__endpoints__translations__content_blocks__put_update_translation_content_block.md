---
url: https://www.braze.com/docs/api/endpoints/translations/content_blocks/put_update_translation_content_block
slug: docs__api__endpoints__translations__content_blocks__put_update_translation_content_block
title: "Update translation in a Content Block"
description: "This article outlines details about the Update translation in a Content Block endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update translation in a Content Block

put

/content_blocks/translations

Use this endpoint to update multiple translations for a Content Block. See Locales in messages for more information about translation features.

## Prerequisites

To use this endpoint, you’ll need an API key with the content_blocks.translations.update permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per minute.

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 content_block_id | 
 Required | 
 String | 
 The ID of your Content Block. | 

 locale_id | 
 Required | 
 String | 
 The ID (UUID) of the locale. | 

 translation_map | 
 Required | 
 Object | 
 Object containing the new translations. | 

note

All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint’s response.

## Example request

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
 "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
 "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
 "translation_map": {
 "id_3": "Ein Absatz ohne Formatierung"
 }
}

```
 | 

## Response

There are four status code responses for this endpoint: 200, 400, 404, and 429.

### Example success response

```

1
2
3

```
 | 
```
{
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
 "message": "The provided locale code does not exist."
 }
 ]
}

```
 | 

- 

New Stuff!
