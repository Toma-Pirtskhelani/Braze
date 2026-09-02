---
url: https://www.braze.com/docs/api/endpoints/templates/email_templates/get_list_email_templates
slug: docs__api__endpoints__templates__email_templates__get_list_email_templates
title: "List available email templates"
description: "This article outlines details about the List available email templates Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List available email templates

get

/templates/email/list

Use this endpoint to get a list of available email templates in your Braze account.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the templates.email.list permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 modified_after | 
 Optional | 
 String in ISO-8601 format | 
 Retrieve only templates updated at or after the given time. | 

 modified_before | 
 Optional | 
 String in ISO-8601 format | 
 Retrieve only templates updated at or before the given time. | 

 limit | 
 Optional | 
 Positive number | 
 Maximum number of templates to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000. | 

 offset | 
 Optional | 
 Positive number | 
 Number of templates to skip before returning rest of the templates that fit the search criteria. | 

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'

```
 | 

## Response

important

Templates built using the drag-and-drop editor for email are not provided in this response.

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
 "count": the number of templates returned
 "templates": [template with the following properties]:
 "email_template_id": (string) your email template's API Identifier,
 "template_name": (string) the name of your email template,
 "created_at": (string) the time the email was created at in ISO 8601,
 "updated_at": (string) the time the email was updated in ISO 8601,
 "tags": (array of strings) tags appended to the template
}

```
 | 

- 

New Stuff!
