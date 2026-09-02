---
url: https://www.braze.com/docs/api/endpoints/translations/email_templates/put_update_template
slug: docs__api__endpoints__translations__email_templates__put_update_template
title: "Update translations for an email template"
description: "This article outlines details about the Update translations for an email template endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update translations for an email template

put

/templates/email/translations/

Use this endpoint to update translations for an email template. See Locales in messages for more information about translation features.

## Prerequisites

To use this endpoint, you’ll need an API key with the templates.translations.update permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per minute.

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 template_id | 
 Required | 
 String | 
 The ID of your email template. | 

 locale_id | 
 Required | 
 String | 
 The ID of the locale. | 

 translations_map | 
 Required | 
 String | 
 The map of the translations for your email template. | 

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
 "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
 "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
 "translation_map": {
 "id_0": "¡Hola!",
 "id_1": "Me llamo Jacky",
 "id_2": "¿Dónde está la biblioteca?"
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
8

```
 | 
```
{
 "errors": [
 {
 "id": "1234567-abc-123-012345678",
 "message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
 }
 ]
}

```
 | 

- 

New Stuff!
