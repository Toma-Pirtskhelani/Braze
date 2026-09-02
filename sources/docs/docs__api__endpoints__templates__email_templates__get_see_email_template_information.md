---
url: https://www.braze.com/docs/api/endpoints/templates/email_templates/get_see_email_template_information
slug: docs__api__endpoints__templates__email_templates__get_see_email_template_information
title: "See email template information"
description: "This article outlines details about the See email template Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# See email template information

get

/templates/email/info

Use this endpoint to get information on your email templates.

important

Templates built using the drag-and-drop editor for email are not accepted.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the templates.email.info permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 email_template_id | 
 Required | 
 String | 
 See email template API identifier. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'

```
 | 

## Response

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

```
 | 
```
{
 "email_template_id": (string) Your email template's API Identifier,
 "template_name": (string) The name of your email template,
 "description": (string) The email template description,
 "subject": (string) The email template subject line,
 "preheader": (optional, string) The email preheader used to generate previews in some clients),
 "body": (optional, string) The email template body that may include HTML,
 "plaintext_body": (optional, string) A plaintext version of the email template body,
 "should_inline_css": (optional, boolean) Whether there is inline CSS in the body of the template - defaults to the css inlining value for the workspace,
 "tags": (string) Tag names,
 "created_at": (string) The time the email was created at in ISO 8601,
 "updated_at": (string) The time the email was updated in ISO 8601
}

```
 | 

Images in this response will show in the body variable as HTML.

- 

New Stuff!
