---
url: https://www.braze.com/docs/api/endpoints/translations/email_templates/get_view_translation_template
slug: docs__api__endpoints__translations__email_templates__get_view_translation_template
title: "View all translations and locales for an email template"
description: "This article outlines details about the View all translations and locales for Email Template endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View all translations and locales for an email template

get

/templates/email/translations/

Use this endpoint to view all translations and locales for an email template. See Locales in messages for more information about translation features.

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

note

All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint’s response.

## Example request

```

1
2
3
4
5

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
--- template_id: "6ad1507f-ca10-44c4-95bf-6e4gay901kc5"

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
31
32

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
 },
 {
 "locale": {
 "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
 "name": "zh-HK",
 "country": "HK",
 "language": "zh",
 "locale_key": "zh-hk"
 },
 "translation_map": {
 "id_0": "你好",
 "id_1": "我的名字是 Jacky",
 "id_2": "圖書館在哪裡?"
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
