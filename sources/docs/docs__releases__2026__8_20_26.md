---
url: https://www.braze.com/docs/releases/2026/8_20_26
slug: docs__releases__2026__8_20_26
title: "August 20, 2026 release"
description: "This article contains release notes for August 20, 2026."
section: releases/2026
fetched: 2026-09-02
evidence: company-own (technical)
---
# August 20, 2026 release

## Data & Reporting

### Cloud Data Ingestion SQL editor

 General availability

The SQL editor lets you create and edit Cloud Data Ingestion (CDI) syncs by writing a SQL query against any table or view in your data warehouse, rather than building and maintaining a dedicated Braze-specific table. It’s available for all sync data types across all CDI data warehouse sources: Snowflake, Redshift, BigQuery, Databricks, and Fabric.

### Cloud Data Ingestion visual mapper

 Beta

The visual mapper lets you create a Cloud Data Ingestion (CDI) sync by mapping an existing data warehouse table’s columns to Braze fields directly in the dashboard, with no SQL or dedicated table required. This beta release supports User Attributes syncs across all CDI data warehouse sources. The visual mapper and the SQL editor are complementary: use the visual mapper for direct column-to-field mapping, and the SQL editor for advanced cases like transformations, joins, and conditional logic.

### Cloud Data Ingestion for Google Cloud Storage and Azure Blob Storage

 General availability

Cloud Data Ingestion (CDI) supports two new file storage sources: Google Cloud Storage, generally available now, and Azure Blob Storage, coming the week of August 31, 2026. Both sources work like the existing Amazon S3 source—Braze ingests files as soon as they’re written to the bucket or container—so customers on Google Cloud or Azure get the same speed and reliability without replicating files into S3 or building a custom integration.

### Cloud Data Ingestion to BrazeAI Decisioning Studio

 Early access

Cloud Data Ingestion (CDI) can now sync data warehouse data directly to BrazeAI Decisioning Studio for customers using both products, so you can bring in data beyond your Braze workspace for reinforcement learning and AI decisioning without building custom ETL jobs. This early access release supports Snowflake sources, with additional data warehouse sources coming soon.

## BrazeAITM

### Operator can navigate the dashboard for you

 General availability

Operator can navigate to a different dashboard page to complete your request. When a prompt needs a different part of the dashboard, Operator identifies the destination, proposes the navigation, and takes you there before continuing its work.

This lets Operator chain multi-step work from a single prompt. For example, if you ask Operator from the home page to set up your drag-and-drop editor settings to match your brand guidelines, it navigates you to the relevant email settings and continues helping you from there.

By default, Operator asks you to approve a proposed navigation before it moves you to a new page. To let Operator navigate without waiting for your approval each time, turn on Auto-approve actions.

### Operator can act on more dashboard pages

 General availability

Operator can complete work from additional dashboard pages when you describe the outcome in natural language. Examples include building reports and dashboards, working from email template and Content Block list pages, importing or managing users, creating predictions, and updating more admin and settings surfaces.

For example, on the Report Builder page, ask Operator to build a report that shows workspace SMS engagement over the last 30 days.

For representative coverage, see What you can do with Operator. Ask Operator on the page you’re on for the most current answer.

### Operator can create and edit Canvases

 General availability

Operator can create a draft Canvas from a natural-language description, and edit an existing Canvas the same way. Describe the journey you want—entry criteria, delays, and messages—and Operator assembles a draft you review and refine before you launch it.

For example, ask Operator to build an abandoned cart journey that waits one hour after cart abandonment, sends an email reminder, then a push after 24 hours if the user still hasn’t purchased.

For supported steps and limitations, see What you can do with Operator.

### Content Optimizer step updates

 Beta

The Content Optimizer step includes the following updates:

- Step states: Content Optimizer steps show whether they’re in Learning, Optimizing, or Action Recommended, so you can see where each step stands.
 
- Pre-launch setup checks: Content Optimizer checks for key misconfigurations while you draft, so you can catch issues before you launch.
 
- Track which combination each user received: A new Liquid tag and user profile visibility let you track which variant combination each user received, end to end.
 
- New Currents data: Three new event types let you pull Content Optimizer data into your warehouse: users.canvas.costep.Send, users.canvas.costep.Conversion, and contentoptimizer.ComponentStore.

For setup details, see Content Optimizer step.

## Orchestration

### Workspace quiet hours

 Early access

Workspace quiet hours let you set a default quiet hours window for a messaging channel across your entire workspace. Every campaign and Canvas on that channel respects the window in each recipient’s local time zone. You can keep the workspace default, or opt out and apply a campaign or Canvas-specific window instead.

Messages that would send during the window are held for later delivery or aborted, depending on the campaign type. Workspace quiet hours never modify message content.

### Canvas threshold alerts

 Early access

Canvas threshold alerts notify you when user entries or messages sent fall outside the volume you expect. Set a threshold, choose how often Braze checks it (every 3 to 12 hours, or every 24 hours), and get notified by email, webhook, or both when a rule is met. You can create multiple alerts for the same Canvas, including on drafts—the alert starts checking after the Canvas launches.

### Automatic Team assignment

 General availability

For users with Team-level permissions only, Braze can assign a Teams automatically during object creation.

## Channels & Touchpoints

### Connected Content debugger

 Early access

The Connected Content debugger shows the live request and response for each Connected Content call in Preview & Test, so you can verify your endpoint, headers, and Liquid tags before you launch a campaign or Canvas. Open View details to inspect the URL, method, status code, request and response headers, payload, duration, and whether the response was served from cache.

During early access, the debugger is available for Content Cards, email, in-app messages, push, SMS/MMS/RCS, webhooks, and WhatsApp.

### In-app message and landing page surveys

 General availability

Braze surveys collect feedback in in-app messages and landing pages that you can analyze and use in follow-up messaging.

### KakaoTalk carousel message

 General availability

A KakaoTalk carousel message includes up to six scrollable cards. Each card has an image, header, message, optional Website URL, and at least one button.

### WhatsApp Template Builder improvements

 General availability

WhatsApp Template Builder supports more creation paths and template options:

- Create templates while building campaigns and Canvases: Create a new WhatsApp template directly in the composer instead of only selecting existing templates from Content.
 
- Carousel response messages: Build carousel layouts as response messages, not only as outbound templates.
 
- New template types: Utility and Flow: Template Builder supports Utility templates and Flow templates, including when you create templates from campaigns, Canvases, or the standalone Content Templates experience.

### Custom form blocks and JavaScript bridge for landing pages

 General availability

Landing pages now support custom form blocks and a JavaScript bridge, so you can capture custom form input and sync client-side events and attributes through your landing page experience.

### Multi-step landing page forms

 General availability

Multi-step landing page forms let you split a long form across multiple steps in a single Form row, with a built-in confirmation step after submission.

### Manage Subscriptions block for landing pages

 General availability

The Manage Subscriptions block lets users view, opt in to, and update email subscription groups on a landing page.

## Partnerships

### Audience Sync: Google Data Manager API

 Early access

Audience Sync to Google supports Google Data Manager API in early access.

### Amazon Bedrock - AI Model Provider

Amazon Bedrock is a fully managed AWS service that provides access to foundation models from leading AI companies through a unified API, so brands can build and scale generative AI applications on AWS.

For more information, see Amazon Bedrock.

### Bynder - Message Orchestration - CMS and DAM

Bynder is a digital asset management (DAM) platform that helps customers create, manage, find, and distribute approved digital assets (images, videos, and other creative) from a single source of truth. When integrated with Braze, Bynder’s Universal Compact View (UCV) Google Chrome extension lets marketers search for and select Bynder assets without leaving the Braze dashboard. Insert links to those assets directly into campaigns and Canvases.

For more information, see Bynder.

### Multiplied Media - Message Personalization - Visual and Interactive Content

Multiplied Media is a creative and automation studio that uses your CRM data to create personalized images, GIFs, and video—a unique asset for each customer. The Multiplied Media and Braze integration lets you send this media through email, push notifications, in-app messages, Content Cards, and WhatsApp.

For more information, see Multiplied Media.

## SDK

The following SDK updates have been released. For more details, see SDK Changelogs.

### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Unity SDK 12.0.0

- Updated the native iOS bridge from Braze Swift SDK 14.1.0 to 18.0.0.
 
- Updated the native Android bridge from Braze Android SDK 42.2.0 to 43.0.0.

- Flutter SDK 22.0.0

- Updates the native Android bridge from Braze Android SDK 42.3.1 to 43.0.0.
 
- Updates the native iOS bridge from Braze Swift SDK 17.0.0 to 18.0.0.

- Swift SDK 18.0.0-18.1.0

- Renames Braze.Ecommerce.ProductViewedEvent.typeIdentifiers to type on Swift and Objective-C API surfaces.
 Renames Live Activities push-to-start update events on Braze.LiveActivities.UpdateEvent.ActivityType, which are emitted when using Braze.LiveActivities.subscribeToStateUpdates(_:):

- pushToStartOptedOut to pushToStartUnregistered
 
- pushToStartOptOutFlushed to pushToStartUnregisterFlushed

### Summary of recent SDK features and fixes

- Swift SDK v18.1.0: Adds push token logout methods, in addition to the existing push logout method, to support additional logout use cases. Also updates the eCommerce event type.
 
- Flutter SDK v22.0.0: Updates the native bridge to inherit functionality from the Android and Swift SDKs.
 
- Unity SDK v12.0.0: Updates the native bridge to inherit functionality from the Android and Swift SDKs.

For more details, see the SDK Changelogs.

- 

New Stuff!
