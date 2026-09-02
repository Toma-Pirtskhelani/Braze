---
url: https://www.braze.com/docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template
slug: docs__api__endpoints__translations__webhook_templates__get_view_translations_webhook_template
title: "View translations for a webhook template"
description: "This article outlines details about the endpoint for viewing translations for a webhook template."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View translations for a webhook template

get

/templates/webhook/translations

Use this endpoint to view translations for a webhook template. You can return all configured locales or filter the response by locale. For more information about translation features, see Multi-language messages.

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

 locale_id | 
 Optional | 
 String | 
 The locale UUID to return. If omitted, the response includes all locales configured for the webhook template. | 

## Example request

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'

```
 | 

Replace TEMPLATE_ID with the ID of your webhook template and LOCALE_ID with the UUID of the locale you want to return. Omit locale_id to return all configured locales.

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
19
20
21
22
23
24
25
26
27
28
29
30

```
 | 
```
{
 "translations": [
 {
 "translation_map": {
 "id_0": "¡Hola!",
 "id_1": "¿Te gustaría comprar esto?"
 },
 "locale": {
 "uuid": "c7c12345-de35-1234-5678-abcdefa99a3f",
 "name": "es-MX",
 "country": "MX",
 "language": "es",
 "locale_key": "es-mx"
 }
 },
 {
 "translation_map": {
 "id_0": "你好！",
 "id_1": "你想買這個嗎？"
 },
 "locale": {
 "uuid": "a1b12345-cd35-1234-5678-abcdefa99a3f",
 "name": "zh-HK",
 "country": "HK",
 "language": "zh",
 "locale_key": "zh-hk"
 }
 }
 ]
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
 "message": "Invalid locale ID"
}

```
 | 

- 

New Stuff!
