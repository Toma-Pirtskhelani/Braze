---
url: https://www.braze.com/docs/api/endpoints/translations
slug: docs__api__endpoints__translations
title: "Translation Endpoints"
description: "This landing page lists the Braze translation endpoints."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Translation Endpoints 

Use the Braze translation endpoints to manage and update translations in your campaigns, Canvases, Content Blocks, email templates, and webhook templates.

## Campaign endpoints 

- 

 GET: View Translation for a Campaign

- 

 PUT: Update Translation in a Campaign

- 

 GET: View Campaign Default Source Translations

## Canvas endpoints

- 

 GET: View Translation for a Canvas

- 

 PUT: Update Translation in a Canvas

- 

 GET: View Canvas Default Source Translations

## Email template endpoints 

- 

 GET: View Email Template Default Source Translations

- 

 GET: View Specific Translation and Locale

- 

 GET: View All Translations and Locales

- 

 PUT: Update Translations in an Email Template

## Content Block endpoints 

- 

 GET: View All Translations for a Content Block

- 

 PUT: Update Translation in a Content Block

## Webhook template endpoints 

- 

 GET: View Webhook Template Default Source Translations

- 

 GET: View Webhook Template Translations

- 

 PUT: Update Translations in a Webhook Template

important

Access to the Braze translation endpoints is currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.

## How our translation endpoints work

Our translation endpoints work with multi-language composition, where a message can have different versions that can be rendered depending on the user receiving the message.

### Prerequisites

Before using these endpoints, you must add your locales.

### How to test your translations

There are two ways you can validate translation support using the API and the Braze dashboard across campaigns, Canvases (including individual steps), Content Blocks, email templates, and webhook templates:

- During composition (before launch)
 
- After launch (using post-launch drafts)

Before testing updating translations, you must:

- Add your locales.
 
- Create a message and use translation tags where appropriate.
 
- Save the message.
 
- Select the locales to be included.

- 

New Stuff!
