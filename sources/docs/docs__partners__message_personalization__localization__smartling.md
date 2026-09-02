---
url: https://www.braze.com/docs/partners/message_personalization/localization/smartling
slug: docs__partners__message_personalization__localization__smartling
title: "Smartling"
description: "This reference article outlines the partnership between Braze and Smartling, a cloud-based software for localization. The Braze Connector supports the translation of HTML email templates,..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Smartling

Smartling is an end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

This integration is maintained by Smartling.

## About the integration

The Braze Connector supports translations for messages in campaigns and Canvases (email, push, in-app messages, and banners), email templates, and Content Blocks. Refer to the following table to learn which editor types are supported for each channel or feature.

 Channel/Feature | 
 Traditional Editor (ex. HTML) | 
 Drag-and-Drop Editor | 

 Email | 
 ✅ | 
 ✅ | 

 IAM | 
 ✅ | 
 ✅ | 

 Push | 
 ✅ | 
 n/a | 

 Email Template | 
 ✅ | 
 ✅ | 

 Banners | 
 n/a | 
 ✅ | 

 Content Blocks | 
 ✅ | 
 ✅ | 

## Prerequisites

 Requirement | 
 Description | 

 Smartling account | 
 A Smartling account is required to take advantage of this partnership. | 

 Smartling translation project | 
 To connect your Braze account with Smartling, you must first sign in and create a translation project. | 

 Braze REST API key | 
 A Braze REST API key with the following permissions: 
- campaigns.translations.get
- campaigns.translations.update
- campaigns.list
- campaigns.details
- canvas.translations.get
- canvas.translations.update
- campaigns.details
- templates.email.create
- templates.email.update
- templates.email.list
- templates.email.info
- templates.translations.get
- templates.translations.update
- content_blocks.info
- content_blocks.list
- content_blocks.create
- content_blocks.update

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. | 

 Braze Multi Language Settings | 
 Complete Multi Language Settings in Braze | 

## Integration

### Step 1: Set up multi-language settings in Braze

See Braze’s multi-language setup instructions for setting up locales in Braze.

### Step 2: Set up the Braze project in Smartling TMS

Refer to the Smartling documentation for details on connector configuration.

### Connecting Braze to Smartling

- In your Smartling account, create a Braze Connector project type.

- In this project, select Settings > Braze Settings > Connect to Braze.
 
- Complete the required fields, like API URL and API Key. If the test connection is successful, save the connection. If the test is not successful, confirm you entered the correct API URL and API Key.

- Add additional project languages.

- In Braze Settings, verify that the values in the Target Language (Braze) column match the locales configured in Braze multi-language settings. The locale naming convention must match exactly.

### Step 3: Add translation tags to your Braze message

See Braze’s instructions on how to add translation tags to your messages:

- Email
 
- Push
 
- In-app messages

Here is an example of a HTML email campaign with translation tags.

You must save the message as a draft before you can select locales.

### Step 4: Manage translations in Smartling

After you connect and set up the Braze connector, find Braze content in the Braze tab in your Smartling project. For more information, see the Smartling documentation.

Smartling provides advanced features to search and select content by:

- Keyword search
 
- Braze content type
 
- Braze tagging

- In this example, the New Year promotion email campaign was created in Step 3.

- After you locate the campaign you want to translate, select the folder, choose the variants, and select Request Translation.

- Create a new job for the translation.

- After the job is authorized, edit each translation in the CAT tool.

- After the translations are complete, save and submit your translation to Braze.

### Step 5: Preview the message as a multi-language user in Braze

In Braze, preview your campaign as a multi-language user to confirm that the translations are applied correctly.

## Frequently asked questions

### Are translation tags supported for the drag-and-drop editor?

For the drag-and-drop editor (email, Content Block, in-app message), you must manually add translation tags as Liquid tags.

### How do you translate text within a Liquid tag?

Smartling recognizes Liquid tags and makes them uneditable variables in the composer. Any other text within the Liquid tag, such as default text or filters like join, also become uneditable in Smartling. However, remove the Liquid tag in Smartling and recreate the Liquid tag with the translated default text. A warning appears when saving the translation.

- 

New Stuff!
