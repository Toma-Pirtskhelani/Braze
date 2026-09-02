---
url: https://www.braze.com/docs/user_guide/messaging/governance/copy_across_workspaces
slug: docs__user_guide__messaging__governance__copy_across_workspaces
title: "Copy campaigns, Canvases, and landing pages across workspaces"
description: "This reference article provides an overview of how to copy campaigns, Canvases, and landing pages to different workspaces."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Copy campaigns, Canvases, and landing pages across workspaces

Copying campaigns, Canvases, and landing pages across workspaces lets you jumpstart content creation by using existing content from a different workspace as a starting point. This page covers how to copy campaigns, Canvases, and landing pages to different workspaces and lists what is and isn’t copied over.

When you copy a campaign, Canvas, or landing page to a different workspace, the copy remains as a draft until you edit it and launch the campaign or Canvas, or publish the landing page. This helps you keep and build off your successful messaging strategies.

- campaigns
 
- canvas
 
- landing pages

important

Copying campaigns across workspaces is generally available. Channel support for Content Cards isn’t currently available.

You can copy campaigns across workspaces for these supported channels: SMS, in-app messages, push notifications, email, and webhooks. You can also copy across email templates, feature flags, and Content Blocks. Note that multi-channel campaigns with unsupported channels can’t be copied over to a different workspace.

To copy a campaign to a different workspace:

- Select the gear icon next to the selected campaign.
 
- Select Copy to workspace.
 
- After copying, review and test your campaign to confirm that all fields work properly.

important

Copying Canvases across workspaces is generally available. The following channels aren’t currently supported: LINE, Content Cards, and WhatsApp.

You can copy Canvases across workspaces for these supported channels: email, in-app messages, push, webhooks, and SMS.

To copy a Canvas to a different workspace:

- Select the  menu next to the selected Canvas.
 
- Select Copy to workspace.
 
- After copying, review and test your Canvas to confirm that all fields work properly.

When copying a Canvas with Audience Sync steps, the settings aren’t copied over to the destination workspace, but the steps in the journey are.

You can copy landing pages across workspaces.

To copy a landing page to a different workspace:

- Go to Messaging > Landing Pages.
 
- Select the  menu next to the selected landing page.
 
- Select Copy to workspace.
 
- Review and test your landing page to confirm that all fields work properly.

note

You can copy a campaign or Canvas to another workspace at any point in its lifecycle, including after it’s launched. Braze copies the active version.

If you have saved draft changes for a campaign or saved a Canvas draft that you haven’t launched yet, Braze doesn’t include those pending edits. Launch the draft in the original workspace first, then copy.

## What’s copied across workspaces

Note that the following tables cover campaign and Canvas fields, and are not a comprehensive list of what is copied across workspaces and what is omitted. As a best practice, check the campaign, Canvas, and landing page details and test to confirm your message works as expected.

Landing pages are copied as drafts. Before publishing a copied landing page, review its page URL, custom domain settings, form submission handling, and any Liquid or workspace-specific references.

note

Translations are not copied when copying email campaigns, Canvases, or templates across workspaces. After copying, re-enter or re-upload translations in the destination workspace.

### Details

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Description | 
 Territories | 

 Type | 
 Tags | 

 Actions (nested) | 
 Segments and filters | 

 Conversion behaviors (nested) | 
 Approvals | 

 Quiet time configurations | 
 Trigger schedule | 

 Frequency capping configurations | 
 Campaign summaries | 

 Recipient subscription state | 
   | 

 Recurring schedule | 
   | 

 Is Transactional | 
   | 

 Copied | 
 Omitted | 

 Description | 
 Territories | 

 Type | 
 Tags | 

 Actions (nested) | 
 Segments and filters | 

 Conversion behaviors (nested) | 
 Approvals | 

 Quiet time configurations | 
 Trigger schedule | 

 Frequency capping configurations | 
 Canvas summaries | 

 Recipient subscription state | 
   | 

 Recurring schedule | 
 Exit criteria | 

 Is Transactional | 
   | 

Filter criteria from Canvas steps (for example, Decision Split steps) aren’t copied to the destination workspace. Reconfigure those filters after you copy.

### Conversion behaviors

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Type behavior | 
 Workspace IDs | 

 Campaign interaction | 
 Campaign ID | 

 Custom event name | 
   | 

 Product name | 
   | 

 Copied | 
 Omitted | 

 Type behavior | 
 Workspace IDs | 

 Canvas interaction | 
 Canvas ID | 

 Custom event name | 
   | 

 Product name | 
   | 

### Actions

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Type behavior | 
 Workspace IDs | 

 Campaign interaction | 
 Campaign ID | 

 Custom event name | 
   | 

 Product name | 
   | 

 Copied | 
 Omitted | 

 Type behavior | 
 Workspace IDs | 

 Canvas interaction | 
 Canvas ID | 

 Custom event name | 
   | 

 Product name | 
   | 

### Message variations

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Send percentage | 
 API ID | 

 Type | 
 Seed group IDs | 

   | 
 Link template IDs | 

   | 
 Internal user group IDs | 

 Copied | 
 Omitted | 

 Send percentage | 
 API ID | 

 Type | 
 Seed group IDs | 

   | 
 Link template IDs | 

   | 
 Internal user group IDs | 

### Email message variation

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Email body | 
 From address | 

 Message extras | 
 Reply to | 

 Title | 
 BCC | 

 Subject | 
 Link template | 

   | 
 Link aliasing | 

   | 
 Translations | 

 Copied | 
 Omitted | 

 Email body | 
 From address | 

 Message extras | 
 Reply to | 

 Title | 
 BCC | 

 Subject | 
 Link template | 

   | 
 Link aliasing | 

   | 
 Translations | 

### Email body

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Plain text | 
 Link aliasing | 

 HTML and drag-and-drop content | 
 Translations | 

 Preheader | 
   | 

 Inline CSS | 
   | 

 AMP HTML | 
   | 

 Copied | 
 Omitted | 

 Plain text | 
 Link aliasing | 

 HTML and drag-and-drop content | 
 Translations | 

 Preheader | 
   | 

 Inline CSS | 
   | 

 AMP HTML | 
   | 

### Email templates

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Email body | 
 API IDs | 

 Description | 
 Image IDs | 

 Subject | 
 Territories | 

 Headers | 
 Tags | 

   | 
 Translations | 

 Copied | 
 Omitted | 

 Email body | 
 API IDs | 

 Description | 
 Image IDs | 

 Subject | 
 Territories | 

 Headers | 
 Tags | 

   | 
 Translations | 

### Content Blocks

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Name | 
 Link aliasing | 

 Description | 
 API keys | 

 Content | 
 Territories | 

 HTML and drag-and-drop content | 
 Tags | 

 Copied | 
 Omitted | 

 Name | 
 Link aliasing | 

 Description | 
 API keys | 

 Content | 
 Territories | 

 HTML and drag-and-drop content | 
 Tags | 

### SMS message variation

- campaigns
 
- canvas

 Copied | 
 Omitted | 

 Body | 
 Messaging service | 

 Link shortening | 
 VCF media items | 

 Click tracking | 
   | 

 Media items | 
   | 

 Copied | 
 Omitted | 

 Body | 
 Messaging service | 

 Link shortening | 
 VCF media items | 

 Click tracking | 
   | 

 Media items | 
   | 

## Copying messages that contain Liquid

Liquid references within message bodies are copied over to the destination workspace, but the references may not function as expected. This means if a Canvas from Workspace A is copied to Workspace B, then Workspace B can’t reference Workspace A’s details, including Liquid references. For example, fields like trigger actions, audience filters, and Decision Split filter criteria aren’t copied over.

Keep track of the following Liquid references with dependencies when copying campaigns, Canvases, and landing pages across workspaces:

- Catalog item tags
 
- Connected Content tags
 
- Content Blocks
 
- Custom attributes
 
- Preference centers
 
- Product recommendations
 
- Subscription state tags
 
- Voucher and promotion tags

## Copying messages with feature flags

To copy a feature flag campaign and a Canvas with a Feature Flag step between workspaces, make sure the destination workspace has a feature flag experiment configured with an ID that matches either the feature flag referenced in the original campaign or the Feature Flag step referenced in the original Canvas.

If you copy a campaign or Canvas that has a Feature Flag step with a feature flag ID that doesn’t exist in the destination workspace, the Feature Flag step will be copied but its contents will not be.

## Copying messages with Content Blocks

When you copy a campaign across workspaces, Content Blocks won’t be copied. However, a Content Block can be referenced in the destination workspace if a block with the same name exists. Alternatively, you can create the Content Block (or these Liquid references) in the destination workspace to avoid errors when launching a campaign.

For Canvases that reference a Content Block, the Content Block must first be copied to the destination workspace.

- 

New Stuff!
