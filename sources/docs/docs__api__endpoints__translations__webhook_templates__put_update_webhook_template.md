---
url: https://www.braze.com/docs/api/endpoints/translations/webhook_templates/put_update_webhook_template
slug: docs__api__endpoints__translations__webhook_templates__put_update_webhook_template
title: "Update translations for a webhook template"
description: "This article outlines details about the endpoint for updating translations for a webhook template."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update translations for a webhook template

put

/templates/webhook/translations

Use this endpoint to update translations for a webhook template. For more information about translation features, see Multi-language messages.

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
 The ID of your webhook template. | 

 locale_id | 
 Required | 
 String | 
 The UUID of the locale to update. The locale must be configured for the webhook template. | 

 translation_map | 
 Required | 
 Object | 
 An object containing the updated translations. | 

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
10
11

```
 | 
```
curl --location --request PUT 'https://rest.iad-03.braze.com/templates/webhook/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
 "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
 "translation_map": {
 "id_0": "¡Hola!",
 "id_1": "¿Te gustaría comprar esto?"
 }
}'

```
 | 

## Response

There are five status code responses for this endpoint: 200, 400, 403, 404, and 429.

### Example success response

The status code 200 returns the following empty response body.

```

1

```
 | 
```
{}

```
 | 

### Example error response

The status code 400 could return the following response body.

```

1
2
3

```
 | 
```
{
 "message": "Locale not found"
}

```
 | 

- 

New Stuff!
