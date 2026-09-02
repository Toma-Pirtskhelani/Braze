---
url: https://www.braze.com/docs/api/endpoints/translations/email_templates/get_view_source_template
slug: docs__api__endpoints__translations__email_templates__get_view_source_template
title: "View the source translations for an email template"
description: "This article outlines details about the View source translations for an email template endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# View the source translations for an email template

get

/templates/email/translations/source

Use this endpoint to view the source translations for an email template. See Locales in messages for more information about translation features.

## Prerequisites

To use this endpoint, you’ll need an API key with the templates.email.info permission.

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
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"

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

```
 | 
```
{
 "translations": {
 "translation_map": {
 "id_0": "Here's a limited time offer for your membership tier!",
 "id_1": "Welcome to a new fashion-forward season!"
 }
 },
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
