---
url: https://www.braze.com/docs/api/endpoints/templates/email_templates/post_create_email_template
slug: docs__api__endpoints__templates__email_templates__post_create_email_template
title: "Create email template"
description: "This article outlines details about the Create email templates Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create email template

post

/templates/email/create

Use this endpoint to create email templates on the Braze dashboard.

These templates will be available on the Templates & Media page. The response from this endpoint includes a field for email_template_id, which can be used to update the template in subsequent API calls.

tip

You can also call this endpoint through the Braze MCP server using the create_email_template function. This lets AI tools like Claude and Cursor create email templates through natural language prompts.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the templates.email.create permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY

```
 | 

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
 "template_name": (required, string) The name of your email template,
 "subject": (required, string) The email template subject line,
 "body": (required, string) The email template body that may include HTML,
 "plaintext_body": (optional, string) A plaintext version of the email template body,
 "preheader": (optional, string) The email preheader used to generate previews in some clients,
 "tags": (optional, Array of Strings) Tags must already exist,
 "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 template_name | 
 Required | 
 String | 
 Name of your email template. | 

 subject | 
 Required | 
 String | 
 Email template subject line. | 

 body | 
 Required | 
 String | 
 Email template body that may include HTML. Up to 400 KB. | 

 plaintext_body | 
 Optional | 
 String | 
 A plaintext version of the email template body. | 

 preheader | 
 Optional | 
 String | 
 Email preheader used to generate previews in some clients. | 

 tags | 
 Optional | 
 String | 
 Tags must already exist. | 

 should_inline_css | 
 Optional | 
 Boolean | 
 Enables or disables the inline_css feature per template. If not provided, Braze will use the default setting for the app group. One of true or false is expected. | 

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
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "template_name": "email_template_name",
 "subject": "Welcome to my email template!",
 "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
 "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
 "preheader": "My preheader is pretty cool.",
 "tags": ["Tag1", "Tag2"]
}'

```
 | 

## Example response

```

1
2
3
4

```
 | 
```
{
 "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
 "message": "success"
}

```
 | 

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

 Error | 
 Troubleshooting | 

 Template name is required | 
 Enter a template name. | 

 Tags must be an array | 
 Tags must be formatted as an array of strings, for example ["marketing", "promotional", "transactional"]. | 

 All tags must be strings | 
 Make sure your tags are encapsulated in quotes (""). | 

 Some tags could not be found | 
 To add a tag when creating an email template, the tag must already exist in Braze. | 

 Email must have valid Content Block names | 
 The email might contain Content Blocks that don’t exist in this environment. | 

 Invalid value for should_inline_css. One of true or false was expected | 
 This parameter only accepts boolean values (true or false). Make sure the value for should_inline_css is not encapsulated in quotes (""), which causes the value to be sent as a string instead. | 

- 

New Stuff!
