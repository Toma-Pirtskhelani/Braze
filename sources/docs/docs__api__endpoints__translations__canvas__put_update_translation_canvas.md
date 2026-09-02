---
url: https://www.braze.com/docs/api/endpoints/translations/canvas/put_update_translation_canvas
slug: docs__api__endpoints__translations__canvas__put_update_translation_canvas
title: "Update translation in a Canvas"
description: "This article outlines details about the Update translation in a Canvas endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update translation in a Canvas

put

/canvas/translations

Use this endpoint to update multiple translations for a Canvas. See Locales in messages for more information about translation features.

If you want to update translations after a Canvas has been launched, you’ll need to save your message as a draft first.

## Prerequisites

To use this endpoint, you’ll need an API key with the canvas.translations.update permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per minute.

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 workflow_id | 
 Required | 
 String | 
 The ID of the Canvas. | 

 step_id | 
 Required | 
 String | 
 The ID of your Canvas step. | 

 message_variation_id | 
 Required | 
 String | 
 The ID of your message variation. | 

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
8
9

```
 | 
```
{
 "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
 "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
 "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
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
