---
url: https://www.braze.com/docs/partners/message_orchestration/templates/email_love
slug: docs__partners__message_orchestration__templates__email_love
title: "Email Love"
description: "Learn how to integrate Braze with Email Love, a Figma plugin that enables you to design and export responsive and accessible HTML emails directly from..."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Email Love

Email Love is a Figma plugin that empowers you to design and export responsive and accessible HTML emails directly from Figma. Email Love’s Export to Braze feature uses the Braze API to seamlessly upload your email templates to Braze.

## Prerequisites

 Requirement | 
 Description | 

 Email Love account | 
 An Email Love account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with full Templates permission enabled. This can be created in the Braze dashboard from Settings > API Keys. | 

## Using Email Love with Braze

### Step 1: Run the plugin

To design your email template, you’ll first need to load the plugin. For more detailed instructions, refer to Email Love’s documentation for uploading your email to Braze.

### Step 2: Create your first frame

In the plugin, select the [+ No Template Selected] button to create a new frame for your email design.

### Step 3: Design the template with Email Love’s pre-built components

Select the frame you created and begin adding components (headers, content blocks, CTAs, and footers) from the plugin’s Assets library to structure your email.

### Step 4: Customize the Components

Modify components using Figma’s tools to adjust your text, images, colors, and layout elements to align the template’s design with your brand. If you add a footer component, a Braze unsubscribe link will automatically be included when you export.

### Step 5: Export your email template to Braze

- When you’re finished, select the frame you want to export. Note that you’ll need to use an Email Love footer that contains an unsubscribe link for the export to work.
 
- Select the Export button in the plugin and select Braze from the dropdown menu.
 
- Copy and paste your API key into the Braze API Key box within the Email Love Figma plugin.
 
- Select the Set API Key button.
 
- Select Change Instance ID, then select your Braze instance ID.

### Step 6: Edit your email in Braze

In Braze, go to Templates > Edit Templates > Edit Message. Inside the template editor, you can either edit your email HTML or use the Rich Text editor in the Classic tab.

## Support and troubleshooting

For more detailed instructions, refer to Email Love’s documentation on exporting an email design. For additional support, contact the Email Love support team.

- 

New Stuff!
