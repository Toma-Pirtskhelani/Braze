---
url: https://www.braze.com/docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template
slug: docs__api__endpoints__translations__webhook_templates__get_view_source_webhook_template
title: "View source translations for a webhook template"
description: "This article outlines details about the endpoint for viewing source translations for a webhook template."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View source translations for a webhook template

get

/templates/webhook/translations/source

Use this endpoint to view the default source translations for a webhook template. For more information about translation features, see Multi-language messages.

## Prerequisites

To use this endpoint, you’ll need an API key with the templates.translations.get permission.

## Rate limit

This endpoint has a rate limit of 250,000 requests per minute.

## Query parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 template_id | 
 Required | 
 String | 
 The ID of your webhook template. | 

## Example request

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'

```
 | 

Replace TEMPLATE_ID with the ID of your webhook template.

## Response

There are five status code responses for this endpoint: 200, 400, 403, 404, and 429.

### Example success response

The status code 200 could return the following response body.

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
 "translations": {
 "translation_map": {
 "id_0": "Hello!",
 "id_1": "Would you like to buy this?"
 }
 }
}

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
 "message": "This template does not have multi-language setup"
}

```
 | 

- 

New Stuff!
