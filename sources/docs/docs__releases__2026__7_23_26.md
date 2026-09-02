---
url: https://www.braze.com/docs/releases/2026/7_23_26
slug: docs__releases__2026__7_23_26
title: "July 23, 2026 release"
description: "This article contains release notes for July 23, 2026."
section: releases/2026
fetched: 2026-09-02
evidence: company-own (technical)
---
# July 23, 2026 release

## Data & Reporting

### Messaging Diagnostics dashboard

 General availability

The Messaging Diagnostics dashboard provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected. Contact your customer success manager for access to the feature.

### CSV Custom Events mapper

 General availability

The CSV import flow for custom events now includes a mapper that lets you map event names and event property headers to Braze fields before import. This update brings the custom events experience in line with the custom attributes flow and reduces the need to reformat files before upload. The flow includes uploading a CSV, mapping required fields and events, mapping event properties, and then selecting targeting preferences before import. If your file already matches the expected format, you can continue through the flow without making mapping changes.

### Catalogs free storage now supports up to 500 MB

 General availability

The free version of catalogs now supports up to 500 MB of storage across all CSV files.

## BrazeAITM

### Operator can now update Settings pages for you

 General availability

Operator can now make changes directly on more Settings pages, so you can describe a change in natural language instead of clicking through configuration screens. Supported pages include:

- Quiet hours
 
- Push settings
 
- Messaging rate limits
 
- Messaging rules and always-on approval workflows
 
- Other identifiers and API limits
 
- Contact information

For example, on the Quiet hours page, ask Operator to set quiet hours from 9 PM to 8 AM for SMS.

### Remote Braze MCP server

 Early access

The Braze MCP server is a remote-hosted connection that lets you connect AI agents such as Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity, and Claude Code directly to Braze. Through natural language, agents can read campaign, Canvas, and segment analytics, custom attributes, events, KPIs, and catalogs, and create or update email templates, Content Blocks, and media library assets. No user-profile PII is exposed.

To connect, paste a single endpoint URL into your MCP client—https://mcp.braze.com/mcp for US or https://mcp.braze.eu/mcp for EU—then sign in with OAuth, including SSO. The server launches with the available tools.

## Orchestration

### Teams audience scoping

 General availability

The Teams audience configuration now supports multiple filters.

## Channels & Touchpoints

### Survey rating scale for in-app messages and landing pages

 Early access

Add a numeric rating scale to a form block in both landing page surveys and in-app message surveys to capture sentiment, satisfaction, and likelihood-to-recommend without any custom code. Three ranges are supported: 1–10, 1–5, and 0–10 (the standard NPS range).

### WhatsApp limited time offer templates

 General availability

WhatsApp limited time offer templates display a time-sensitive promotional offer with an optional countdown as the offer nears expiration. Use this layout for time-boxed promotions, such as seasonal sales or offers personalized to a user attribute.

### Shopify self-serve SDK version upgrade

 General availability

New Shopify customers are provisioned on the latest Braze Web SDK and JavaScript SDK versions during setup. Existing customers can view their current SDK version in integration settings, get notified when a newer version is available, and self-serve upgrades from integration settings.

### HTML editor for Banners

 General availability

When you compose a Banner, you can now build it using the HTML editor. The HTML editor is best for teams that already maintain their own HTML templates or want full control over markup and styling for Banners. You can write or paste custom HTML directly into the editor.

### Replace a file in the media library

 General availability

You can now replace the file of an existing media library asset while keeping its URL and asset ID stable. Because the URL doesn’t change, any campaign, Canvas, Content Block, or template that references that asset automatically reflects the updated file, so you don’t have to manually re-upload or re-link it everywhere it’s used.

### Grid view for the media library

 General availability

The media library and select template libraries now offer a grid view alongside the existing list view. Grid view displays assets as thumbnails with key metadata (name, type, last modified), making it faster to find images and creative by sight instead of by filename. Filtering and search work the same in both views.

### Shareable Preview support for more channels

 General availability

Shareable Preview now supports the following additional channels:

- SMS, MMS, and RCS
 
- WhatsApp
 
- Push
 
- Content Cards
 
- LINE

From a campaign or message, generate a link and share it with reviewers who don’t have Braze dashboard access—brand, legal, or an outside agency, for example. Recipients open the link in any browser to see the message rendered as a customer would, including any test personalization.

### Push credentials update API

 General availability

You can now update push credentials programmatically with the Update push credentials endpoint. Each request updates one app and one platform (apple, firebase, huawei, or kindle) and accepts credential payloads as Base64-encoded values. This helps teams manage large app portfolios and credential rotation policies without relying on manual dashboard uploads.

## Partnerships

### Refiner - Surveys

Refiner is an in-app survey platform for SaaS and mobile apps. It enables product and voice-of-customer teams to launch targeted in-app surveys and continuously collect NPS, CSAT, CES, product feedback, and zero-party user data.

### Stayfilm - Visual and Interactive Content

Stayfilm is a REST API for automated, personalized video production at scale. The platform integrates data, images, text, soundtracks, narration, and visual effects to generate customized video content for eCommerce, marketplaces, CRM workflows, and marketing campaigns.

### Validity - Data and Analytics

Validity Everest is an email deliverability platform that helps you measure inbox placement and protect your sending reputation. The Braze and Validity integration syncs your Everest seed list to Braze, automatically seeds qualifying campaigns and Canvases, and pulls engagement metrics back into Validity Inbox so you can compare seed-based placement with real subscriber engagement.

## SDK

The following SDK updates have been released. For more details, see SDK Changelogs.

### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Android SDK 43.0.0

- Adds unregisterPush and logout methods.
 
- Adds additional fields to eCommerce events.
 
- Adds exponential backoff for push notification image loading.

- Swift SDK 17.0.0

- Adds additional fields to eCommerce events.
 
- Makes data states predictable after initialization.
 
- Adds non-blocking accessors for device and user identifiers.
 
- Removes the deprecated push-to-start update API on Braze.LiveActivities.

- Web SDK 6.10.1

- Adds unregisterPush and logout methods.
 
- Adds additional fields to eCommerce events.
 
- Fixes a Banner and Content Card issue related to redundant refreshes on startup.
 
- Adds a public method for Banner dismissal.

- Flutter SDK 21.0.0

- Updates the native iOS bridge.
 
- Removes deprecated methods.
 
- Updates changeUser, enableSDK, and disableSDK handlers to return completion results.

- Expo SDK 5.2.0

- Updates the sample app to Expo SDK 56.

- React Native SDK 22.0.0

- Adds support for Banner dismissals.
 
- Includes binding updates.

- 

New Stuff!
