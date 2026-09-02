---
url: https://www.braze.com/docs/api/endpoints/translations/email_templates/get_view_translation_locale_template
slug: docs__api__endpoints__translations__email_templates__get_view_translation_locale_template
title: "View a specific translation and locale for email template endpoint"
description: "This article outlines details about the View specific translation and locale for email template endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View a specific translation and locale for email template endpoint

get

/templates/translations/email

Use this endpoint to view a specific translation and locale for an email template. See Locales in messages for more information about translation features.

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
 The ID for your email template. | 

 locale_id | 
 Optional | 
 String | 
 The ID (UUID) of the locale. | 

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
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
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
 "locale": {
 "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
 "name": "es-MX",
 "country": "MX",
 "language": "es",
 "locale_key": "es-mx"
 },
 "translation_map": {
 "id_0": "¡Hola!",
 "id_1": "Me llamo Jacky",
 "id_2": "¿Dónde está la biblioteca?"
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
