---
url: https://www.braze.com/docs/api/endpoints/translations/canvas/get_translation_canvas
slug: docs__api__endpoints__translations__canvas__get_translation_canvas
title: "View translation for a Canvas"
description: "This article outlines details about the View translation for a Canvas endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View translation for a Canvas

get

/canvas/translations

Use this endpoint to preview a translated message for a Canvas. See Locales in messages for more information about translation features.

## Prerequisites

To use this endpoint, you’ll need an API key with the canvas.translations.get permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per minute.

## Query parameters

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
 Optional | 
 String | 
 The ID (UUID) of the locale. | 

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
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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
10
11
12
13
14
15
16
17
18

```
 | 
```
{
 "translations": [
 {
 "translation_map": {
 "id_0": "¡Hola!",
 "id_1": "Me llamo Jacky",
 "id_2": "¿Dónde está la biblioteca?"
 },
 "locale": {
 "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
 "name": "es-MX",
 "country": "MX",
 "language": "es",
 "locale_key": "es-mx"
 }
 }
 ]
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
