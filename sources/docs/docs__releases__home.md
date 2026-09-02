---
url: https://www.braze.com/docs/releases/home
slug: docs__releases__home
title: "What’s new in Braze"
description: "Braze release notes are published monthly so you can stay up-to-date on major product releases, ongoing product improvements, Braze partnerships,."
section: releases/home
fetched: 2026-09-02
evidence: company-own (technical)
---
# What’s new in Braze

tip

For more information on any of the updates listed on this page, contact your account manager or open a support ticket. Check out our SDK Changelogs for more information about our monthly SDK releases, improvements, and breaking changes.

August 20, 2026

## August 20, 2026 release

### Data & Reporting

#### Cloud Data Ingestion SQL editor

 General availability

The SQL editor lets you create and edit Cloud Data Ingestion (CDI) syncs by writing a SQL query against any table or view in your data warehouse, rather than building and maintaining a dedicated Braze-specific table. It’s available for all sync data types across all CDI data warehouse sources: Snowflake, Redshift, BigQuery, Databricks, and Fabric.

#### Cloud Data Ingestion visual mapper

 Beta

The visual mapper lets you create a Cloud Data Ingestion (CDI) sync by mapping an existing data warehouse table’s columns to Braze fields directly in the dashboard, with no SQL or dedicated table required. This beta release supports User Attributes syncs across all CDI data warehouse sources. The visual mapper and the SQL editor are complementary: use the visual mapper for direct column-to-field mapping, and the SQL editor for advanced cases like transformations, joins, and conditional logic.

#### Cloud Data Ingestion for Google Cloud Storage and Azure Blob Storage

 General availability

Cloud Data Ingestion (CDI) supports two new file storage sources: Google Cloud Storage, generally available now, and Azure Blob Storage, coming the week of August 31, 2026. Both sources work like the existing Amazon S3 source—Braze ingests files as soon as they’re written to the bucket or container—so customers on Google Cloud or Azure get the same speed and reliability without replicating files into S3 or building a custom integration.

#### Cloud Data Ingestion to BrazeAI Decisioning Studio

 Early access

Cloud Data Ingestion (CDI) can now sync data warehouse data directly to BrazeAI Decisioning Studio for customers using both products, so you can bring in data beyond your Braze workspace for reinforcement learning and AI decisioning without building custom ETL jobs. This early access release supports Snowflake sources, with additional data warehouse sources coming soon.

### BrazeAITM

#### Operator can navigate the dashboard for you

 General availability

Operator can navigate to a different dashboard page to complete your request. When a prompt needs a different part of the dashboard, Operator identifies the destination, proposes the navigation, and takes you there before continuing its work.

This lets Operator chain multi-step work from a single prompt. For example, if you ask Operator from the home page to set up your drag-and-drop editor settings to match your brand guidelines, it navigates you to the relevant email settings and continues helping you from there.

By default, Operator asks you to approve a proposed navigation before it moves you to a new page. To let Operator navigate without waiting for your approval each time, turn on Auto-approve actions.

#### Operator can act on more dashboard pages

 General availability

Operator can complete work from additional dashboard pages when you describe the outcome in natural language. Examples include building reports and dashboards, working from email template and Content Block list pages, importing or managing users, creating predictions, and updating more admin and settings surfaces.

For example, on the Report Builder page, ask Operator to build a report that shows workspace SMS engagement over the last 30 days.

For representative coverage, see What you can do with Operator. Ask Operator on the page you’re on for the most current answer.

#### Operator can create and edit Canvases

 General availability

Operator can create a draft Canvas from a natural-language description, and edit an existing Canvas the same way. Describe the journey you want—entry criteria, delays, and messages—and Operator assembles a draft you review and refine before you launch it.

For example, ask Operator to build an abandoned cart journey that waits one hour after cart abandonment, sends an email reminder, then a push after 24 hours if the user still hasn’t purchased.

For supported steps and limitations, see What you can do with Operator.

#### Content Optimizer step updates

 Beta

The Content Optimizer step includes the following updates:

- Step states: Content Optimizer steps show whether they’re in Learning, Optimizing, or Action Recommended, so you can see where each step stands.
 
- Pre-launch setup checks: Content Optimizer checks for key misconfigurations while you draft, so you can catch issues before you launch.
 
- Track which combination each user received: A new Liquid tag and user profile visibility let you track which variant combination each user received, end to end.
 
- New Currents data: Three new event types let you pull Content Optimizer data into your warehouse: users.canvas.costep.Send, users.canvas.costep.Conversion, and contentoptimizer.ComponentStore.

For setup details, see Content Optimizer step.

### Orchestration

#### Workspace quiet hours

 Early access

Workspace quiet hours let you set a default quiet hours window for a messaging channel across your entire workspace. Every campaign and Canvas on that channel respects the window in each recipient’s local time zone. You can keep the workspace default, or opt out and apply a campaign or Canvas-specific window instead.

Messages that would send during the window are held for later delivery or aborted, depending on the campaign type. Workspace quiet hours never modify message content.

#### Canvas threshold alerts

 Early access

Canvas threshold alerts notify you when user entries or messages sent fall outside the volume you expect. Set a threshold, choose how often Braze checks it (every 3 to 12 hours, or every 24 hours), and get notified by email, webhook, or both when a rule is met. You can create multiple alerts for the same Canvas, including on drafts—the alert starts checking after the Canvas launches.

#### Automatic Team assignment

 General availability

For users with Team-level permissions only, Braze can assign a Teams automatically during object creation.

### Channels & Touchpoints

#### Connected Content debugger

 Early access

The Connected Content debugger shows the live request and response for each Connected Content call in Preview & Test, so you can verify your endpoint, headers, and Liquid tags before you launch a campaign or Canvas. Open View details to inspect the URL, method, status code, request and response headers, payload, duration, and whether the response was served from cache.

During early access, the debugger is available for Content Cards, email, in-app messages, push, SMS/MMS/RCS, webhooks, and WhatsApp.

#### In-app message and landing page surveys

 General availability

Braze surveys collect feedback in in-app messages and landing pages that you can analyze and use in follow-up messaging.

#### KakaoTalk carousel message

 General availability

A KakaoTalk carousel message includes up to six scrollable cards. Each card has an image, header, message, optional Website URL, and at least one button.

#### WhatsApp Template Builder improvements

 General availability

WhatsApp Template Builder supports more creation paths and template options:

- Create templates while building campaigns and Canvases: Create a new WhatsApp template directly in the composer instead of only selecting existing templates from Content.
 
- Carousel response messages: Build carousel layouts as response messages, not only as outbound templates.
 
- New template types: Utility and Flow: Template Builder supports Utility templates and Flow templates, including when you create templates from campaigns, Canvases, or the standalone Content Templates experience.

#### Custom form blocks and JavaScript bridge for landing pages

 General availability

Landing pages now support custom form blocks and a JavaScript bridge, so you can capture custom form input and sync client-side events and attributes through your landing page experience.

#### Multi-step landing page forms

 General availability

Multi-step landing page forms let you split a long form across multiple steps in a single Form row, with a built-in confirmation step after submission.

#### Manage Subscriptions block for landing pages

 General availability

The Manage Subscriptions block lets users view, opt in to, and update email subscription groups on a landing page.

### Partnerships

#### Audience Sync: Google Data Manager API

 Early access

Audience Sync to Google supports Google Data Manager API in early access.

#### Amazon Bedrock - AI Model Provider

Amazon Bedrock is a fully managed AWS service that provides access to foundation models from leading AI companies through a unified API, so brands can build and scale generative AI applications on AWS.

For more information, see Amazon Bedrock.

#### Bynder - Message Orchestration - CMS and DAM

Bynder is a digital asset management (DAM) platform that helps customers create, manage, find, and distribute approved digital assets (images, videos, and other creative) from a single source of truth. When integrated with Braze, Bynder’s Universal Compact View (UCV) Google Chrome extension lets marketers search for and select Bynder assets without leaving the Braze dashboard. Insert links to those assets directly into campaigns and Canvases.

For more information, see Bynder.

#### Multiplied Media - Message Personalization - Visual and Interactive Content

Multiplied Media is a creative and automation studio that uses your CRM data to create personalized images, GIFs, and video—a unique asset for each customer. The Multiplied Media and Braze integration lets you send this media through email, push notifications, in-app messages, Content Cards, and WhatsApp.

For more information, see Multiplied Media.

### SDK

The following SDK updates have been released. For more details, see SDK Changelogs.

#### SDK breaking updates

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

#### Summary of recent SDK features and fixes

- Swift SDK v18.1.0: Adds push token logout methods, in addition to the existing push logout method, to support additional logout use cases. Also updates the eCommerce event type.
 
- Flutter SDK v22.0.0: Updates the native bridge to inherit functionality from the Android and Swift SDKs.
 
- Unity SDK v12.0.0: Updates the native bridge to inherit functionality from the Android and Swift SDKs.

For more details, see the SDK Changelogs.

July 23, 2026

## July 23, 2026 release

### Data & Reporting

#### Messaging Diagnostics dashboard

 General availability

The Messaging Diagnostics dashboard provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected. Contact your customer success manager for access to the feature.

#### CSV Custom Events mapper

 General availability

The CSV import flow for custom events now includes a mapper that lets you map event names and event property headers to Braze fields before import. This update brings the custom events experience in line with the custom attributes flow and reduces the need to reformat files before upload. The flow includes uploading a CSV, mapping required fields and events, mapping event properties, and then selecting targeting preferences before import. If your file already matches the expected format, you can continue through the flow without making mapping changes.

#### Catalogs free storage now supports up to 500 MB

 General availability

The free version of catalogs now supports up to 500 MB of storage across all CSV files.

### BrazeAITM

#### Operator can now update Settings pages for you

 General availability

Operator can now make changes directly on more Settings pages, so you can describe a change in natural language instead of clicking through configuration screens. Supported pages include:

- Quiet hours
 
- Push settings
 
- Messaging rate limits
 
- Messaging rules and always-on approval workflows
 
- Other identifiers and API limits
 
- Contact information

For example, on the Quiet hours page, ask Operator to set quiet hours from 9 PM to 8 AM for SMS.

#### Remote Braze MCP server

 Early access

The Braze MCP server is a remote-hosted connection that lets you connect AI agents such as Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity, and Claude Code directly to Braze. Through natural language, agents can read campaign, Canvas, and segment analytics, custom attributes, events, KPIs, and catalogs, and create or update email templates, Content Blocks, and media library assets. No user-profile PII is exposed.

To connect, paste a single endpoint URL into your MCP client—https://mcp.braze.com/mcp for US or https://mcp.braze.eu/mcp for EU—then sign in with OAuth, including SSO. The server launches with the available tools.

### Orchestration

#### Teams audience scoping

 General availability

The Teams audience configuration now supports multiple filters.

### Channels & Touchpoints

#### Survey rating scale for in-app messages and landing pages

 Early access

Add a numeric rating scale to a form block in both landing page surveys and in-app message surveys to capture sentiment, satisfaction, and likelihood-to-recommend without any custom code. Three ranges are supported: 1–10, 1–5, and 0–10 (the standard NPS range).

#### WhatsApp limited time offer templates

 General availability

WhatsApp limited time offer templates display a time-sensitive promotional offer with an optional countdown as the offer nears expiration. Use this layout for time-boxed promotions, such as seasonal sales or offers personalized to a user attribute.

#### Shopify self-serve SDK version upgrade

 General availability

New Shopify customers are provisioned on the latest Braze Web SDK and JavaScript SDK versions during setup. Existing customers can view their current SDK version in integration settings, get notified when a newer version is available, and self-serve upgrades from integration settings.

#### HTML editor for Banners

 General availability

When you compose a Banner, you can now build it using the HTML editor. The HTML editor is best for teams that already maintain their own HTML templates or want full control over markup and styling for Banners. You can write or paste custom HTML directly into the editor.

#### Replace a file in the media library

 General availability

You can now replace the file of an existing media library asset while keeping its URL and asset ID stable. Because the URL doesn’t change, any campaign, Canvas, Content Block, or template that references that asset automatically reflects the updated file, so you don’t have to manually re-upload or re-link it everywhere it’s used.

#### Grid view for the media library

 General availability

The media library and select template libraries now offer a grid view alongside the existing list view. Grid view displays assets as thumbnails with key metadata (name, type, last modified), making it faster to find images and creative by sight instead of by filename. Filtering and search work the same in both views.

#### Shareable Preview support for more channels

 General availability

Shareable Preview now supports the following additional channels:

- SMS, MMS, and RCS
 
- WhatsApp
 
- Push
 
- Content Cards
 
- LINE

From a campaign or message, generate a link and share it with reviewers who don’t have Braze dashboard access—brand, legal, or an outside agency, for example. Recipients open the link in any browser to see the message rendered as a customer would, including any test personalization.

#### Push credentials update API

 General availability

You can now update push credentials programmatically with the Update push credentials endpoint. Each request updates one app and one platform (apple, firebase, huawei, or kindle) and accepts credential payloads as Base64-encoded values. This helps teams manage large app portfolios and credential rotation policies without relying on manual dashboard uploads.

### Partnerships

#### Refiner - Surveys

Refiner is an in-app survey platform for SaaS and mobile apps. It enables product and voice-of-customer teams to launch targeted in-app surveys and continuously collect NPS, CSAT, CES, product feedback, and zero-party user data.

#### Stayfilm - Visual and Interactive Content

Stayfilm is a REST API for automated, personalized video production at scale. The platform integrates data, images, text, soundtracks, narration, and visual effects to generate customized video content for eCommerce, marketplaces, CRM workflows, and marketing campaigns.

#### Validity - Data and Analytics

Validity Everest is an email deliverability platform that helps you measure inbox placement and protect your sending reputation. The Braze and Validity integration syncs your Everest seed list to Braze, automatically seeds qualifying campaigns and Canvases, and pulls engagement metrics back into Validity Inbox so you can compare seed-based placement with real subscriber engagement.

### SDK

The following SDK updates have been released. For more details, see SDK Changelogs.

#### SDK breaking updates

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

June 25, 2026

## June 25, 2026 release

### Data & Reporting

#### Metric name update for Content Cards and Banners

The Unique Recipients metric has been renamed to Unique Daily Impressions for Content Cards and Banners. Unique Daily Impressions refer to the number received from Braze and is based on the user_id. Unique daily impressions are counted at the campaign or Canvas step level. For more details, refer to the Metrics glossary.

#### User deletion

 General availability

User deletion lets you manage your database by removing profiles that are no longer needed, created in error, or required to be deleted for compliance (such as GDPR or CCPA).

#### Data point exclusions

 General availability

eCommerce recommended events no longer count toward billable data points. You can adopt Braze eCommerce events (ecommerce.product_viewed, ecommerce.cart_updated, ecommerce.checkout_started, ecommerce.order_placed, ecommerce.order_cancelled, ecommerce.order_refunded) without data point consumption.

#### Event History tab

 General availability

The Event History tab on user profiles lists the user’s custom events and purchases from the past 30 days (up to 100 most recent). Use it to confirm an SDK or API integration is sending events as expected, debug why a user did (or didn’t) enter an event-triggered campaign or Canvas, or investigate a support escalation about a specific user.

#### Deliverability Center surfaces Microsoft SNDS data for Amazon SES customers

For workspaces that send email through Amazon SES, the Deliverability Center displays Microsoft SNDS metrics for your dedicated sending IPs. Braze backfills up to 90 days of historical SNDS data when this feature is turned on for your workspace.

### BrazeAITM

#### Unified BrazeAI assistants in Operator

The standalone BrazeAI assistants found throughout the dashboard are unified into BrazeAI Operator, establishing Operator as the single AI assistant for marketer-facing generative AI assistance across the dashboard. The following assistants now route through Operator:

- AI Liquid Agent
 
- AI Copywriter
 
- AI HTML Email Template agent
 
- AI Image generator
 
- Content QA with AI
 
- AI Copilot for Data Transformations

The existing entry points remain where each legacy assistant button used to live. Instead of opening a standalone assistant, these entry points now open the Operator pane with dynamic prompts that are pre-scoped to your task. These entry points provide a direct route into Operator so you can use these capabilities without adjusting your existing workflows.

#### Operator support for campaign creation and editing

Operator can now create and edit entire campaigns, not just compose messages. From a single natural-language prompt or campaign brief, Operator builds a ready-to-review campaign end to end—composing the message, scheduling delivery, targeting an audience, and assigning conversion events—then recaps what it built in the review step. Previously, Operator could compose the message (one of the five campaign creation steps); it now has visibility and control over the remaining Schedule, Target, Assign, and Review steps.

This functionality is available from the Campaigns page or from within any existing campaign. As a result, Operator can:

- Respond to prompts such as “I want to send our lapsed users a push notification with a 20% off promo code the next time they open the app or log a custom event that cancels their subscription”.
 
- Assist you in each individual step of the campaign wizard, with full visibility into what you’re working on and the ability to change form inputs on the page.
 
- Navigate to the correct step in the wizard to begin taking action, whether you start from an open campaign or the Campaigns page.

#### Operator support for Content Blocks

Operator can now create and edit Content Blocks—the reusable snippets you build once and reference across multiple messages—directly from a natural-language prompt. From the Content Blocks page, ask Operator to create a new Content Block from scratch or edit an existing one, and Operator generates or updates the content for you to review.

#### Agent Console templates built with Operator

When building an agent in Agent Console, you can choose to create a custom agent or select an option in Create an agent with Operator to use BrazeAI Operator to apply a starting template. Operator can pre-configure instructions, output fields, and context for the following Agent Console starting templates.

For more details, see Create custom agents.

#### Agent Console enhancements

You can do the following in the Agent Console:

- Configure pre-set use cases with Operator through the Create agent button dropdown.
 
- Duplicate existing agents from the agent list.
 
- Save agents as drafts during creation and complete configurations later.
 
- Set fallback output values for Canvas agents to prevent output variables from setting to null if the agent errors out.
 
- Set required input fields for a Catalog agentic field, so that the agent doesn’t run if a required input field value is empty or missing.
 
- Re-run an agent for all empty cells of an agentic column to fill any missing values without re-running the entire column.

#### Edit a launched Content Optimizer step

 Beta

After your Canvas is launched, you can now update a Content Optimizer step to:

- Add new variants to any existing component, either manually or using AI-generated suggestions, up to the five-variant limit per component.
 
- Deactivate variants to stop sending them to users.
 
- Re-activate previously deactivated variants, as long as doing so keeps the component at or below the five-variant limit.

### Channels & Touchpoints

#### User dismissals for Banners

 General availability

You can allow users to manually dismiss a Banner by selecting Banner can be dismissed when configuring dismissal behavior. This option is beneficial in scenarios where you want to promote a limited-time sale for all app users, but allow them to dismiss the message if they aren’t interested.

See Configure dismissal behavior for details on enabling dismissal and customizing the dismiss button.

#### Custom click tracking for Banners

 General availability

For more granular click tracking for Banners, you can assign a custom identifier to each interactive element using the Identifier for Reporting field in its properties panel.

#### Re-eligibility for Banners

When re-eligibility is enabled for Banner campaigns, users who dismiss a Banner can become eligible again after a configurable cooldown window that starts at dismissal. If re-eligibility isn’t turned on, dismissed users remain ineligible. To configure re-eligibility, see Configure re-eligibility. Note that Canvas Banner steps use Canvas re-entry settings instead.

#### Quick Push A/B Testing

 General availability

Quick Push A/B Testing now supports multi-platform push campaigns and Canvas steps through variant groups, so you can test aligned iOS and Android message variations in one workflow. For more information, refer to Multiple platform push messages.

#### Optimize with BrazeAI™

 Early access

Optimize with BrazeAI™ automatically turns on when you add multiple push variants, applies recommended experiment defaults, and optimizes toward the highest-performing variant. You can turn it off if you need to send immediately. For more information, see Optimizing A/B tests with BrazeAI.

#### WhatsApp test send results

After sending a test WhatsApp message, you can view a detailed delivery report directly in the message composer. This helps you confirm your message reached the intended recipient and troubleshoot failures before launch.

### Partnerships

#### Convercus - Data and Analytics - Loyalty

Convercus is a SaaS loyalty and coupon platform that helps brands and retailers grow customer frequency, basket value, and repurchase rates through omnichannel loyalty programs and personalized coupon campaigns.

#### Copy Pastd - Message Orchestration - Templates

Copy Pastd Building Blocks is a drag-and-drop email builder that pushes Liquid-powered Content Blocks and full templates directly into your Braze workspace. Design once, sync to Braze, and reuse the same components across campaigns, Canvases, and triggered flows without rebuilding HTML each time.

#### Databricks Mosaic - AI Model Providers

Databricks Mosaic is Databricks’ unified platform for building, deploying, and managing AI and machine learning models at scale on the Databricks Data Intelligence Platform.

#### DinMo - Data and Analytics - Reverse ETL

DinMo is a composable customer data platform (CDP) that connects your cloud data warehouse to Braze through reverse Extract, Transform, Load (ETL). Marketing teams can build audience segments from warehouse data, sync user attributes and events into Braze, and keep subscription statuses up to date without CSV uploads or engineering support.

#### EmailShepherd - Message Orchestration - Templates

EmailShepherd is an agentic email creation platform built on your Email Design System that allows your whole marketing team—and AI agents—to produce on-brand, production-ready emails without bottlenecks. The Braze integration publishes approved emails directly to your Braze workspace, so marketers can scale email production in Braze without sacrificing brand consistency.

#### Talkable - Message Personalization - Referrals

Talkable helps consumer brands turn happy customers into a scalable referral channel. With the Braze integration, marketing email opt-ins captured in Talkable referral campaigns flow into Braze in real time, giving your team the consent, context, and campaign data you need to welcome, segment, and engage every new advocate and friend.

### SDK

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Swift SDK 14.2.0
 
- Android SDK 42.3.0

- BannerView: BannerDismissSnapshot fields passed to onDismissCallback are now non-null. If the SDK cannot resolve placementId, stableKey, or trackingId, the callback is skipped and a warning is logged.

- Web SDK 6.8.0

- Adds support for new eCommerce event methods.

- Swift SDK 14.2.1
 
- Swift SDK 15.0.0

- Banners: onDismiss now receives Braze/BannerDismissalEvent instead of Braze/Banner.
 
- Raises the Xcode version to 26.0 (17A324).
 
- Raises the minimum Mac Catalyst deployment target from iOS 13 (macOS 10.15 Catalina) to iOS 16 (macOS 13 Ventura).

- Mac Catalyst users on macOS 12 Monterey or earlier are no longer supported.

- Removes the ability to control whether the SDK prevents showing in-app messages to different users in certain edge cases.

- Removes the option to configure through Braze.Configuration.preventInAppMessageDisplayForDifferentUser.
 
- The SDK will now always behave as if this configuration option were set to true.

- Updates the Braze.WebViewBridge.ScriptMessageHandler and Braze.WebViewBridge.SchemeHandler init to have non-optional channel parameter.

- Android SDK 42.3.1

- Adds support for new eCommerce event methods.
 
- Adds Banner dismissal methods for custom UI implementations.
 
- Includes HTML in-app message bug fixes.

- Swift SDK 15.0.1
 
- React Native 21.0.0

- Updates native Swift and Android SDK version bindings.
 
- Updates the native Swift SDK version bindings from Braze Swift SDK 14.0.4 to 15.0.1.
 
- Corrects Content Cards JSDoc.

- Raises the Xcode version to 26.0 (17A324).

- Swift SDK 15.1.0

- Adds support for new eCommerce event methods.
 
- Adds Banner dismissal methods for custom UI implementations.
 
- Adds example implementations for building custom UI with Banners.
 
- Adds pass-through Live Activities observability, allowing errors and update events to be tracked with more precision and granularity.
 
- Adds async callback-based getters for Content Cards and deprecates older getters.
 
- Improves state management stability.

- Segment Swift 9.0.0

- Updates the Braze Swift SDK bindings to require releases from the 15.0.0+ SemVer denomination.

- This allows compatibility with any version of the Braze SDK from 15.0.0 up to, but not including, 16.0.0.
 
- Raises the Xcode version to 26.0 (17A324).
 
- Refer to the changelog entry for 15.0.0 for more information on potential breaking changes.

- React Native 21.1.0
 
- Swift SDK 15.2.0

May 28, 2026

## May 28, 2026 release

### Data & Reporting

#### Push Performance dashboard

The Push Performance dashboard gives you a single, channel-level view of push engagement, including sends, bounces, deliveries, and direct, influenced, and total open rates over a configurable time window. Use it to understand the overall health of your push channel without rolling up data from individual campaigns or Canvases.

#### Geolocation fields in catalog selections

 General availability

Catalogs now support distance-based filtering with the new geolocation field type and Catalog Selection operators. This helps you create more relevant location-aware experiences, such as showing each user their nearest restaurant, filtering open properties within 50 km for a real estate campaign, or targeting stores near a specific event. Instead of approximating geographic targeting with city or region codes, you can filter catalog items by proximity to a center point, including a Liquid user attribute such as a user’s most recent location. For more information, see Selections.

#### Banner and RCS for Report Builder

Report Builder supports Banner as a channel and RCS as a sub-category under SMS, so you can measure performance for both directly in your custom reports alongside every other Braze channel.

#### ecommerce.cart_updated event actions

The ecommerce.cart_updated event supports add and remove actions alongside replace, allowing you to send incremental cart changes instead of a full cart snapshot on every update.

### BrazeAITM

#### Content Optimizer for SMS, MMS, and RCS messages

 Beta

You can use Content Optimizer to optimize hooks, bodies, and CTAs for SMS, MMS, and RCS messages. Content Optimizer helps you test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically.

### Orchestration

#### Workspace time zones

 General availability

Use workspace time zones to define specific time zones for individual workspaces. This makes scheduled campaigns and Canvases (that don’t use local time or Intelligent Timing) send according to the workspace’s designated time zone, rather than the overarching company time zone.

Workspace time zones for message sending are rolling out gradually, so you may not see these settings in your dashboard yet.

### Channels & Touchpoints

#### WhatsApp inbound_profile_name

You can automatically capture a user’s WhatsApp display name from Meta’s inbound messaging webhook and write it to the user’s Braze profile. When an inbound WhatsApp message is received, Braze exposes the profile name as a new WhatsApp Liquid attribute, {{whats_app.${inbound_profile_name}}}, which you can reference in a Canvas User Update step to save to a profile field.

#### Orphaned SMS subscription states

Braze automatically manages orphaned subscription state records (subscription data stored for a phone number or email address not tied to any user profile) to prevent unintended subscription state inheritance. This protects users from scenarios where a newly created user profile incorrectly inherits subscription state from a previously deleted or unrelated user.

### Partnerships

#### Chord - Customer Data Platform

Chord provides a customer data platform that captures and standardizes events from your eCommerce storefront. When you connect Chord to Braze, purchase activity, behavioral events, and identity updates flow into Braze so you can trigger campaigns and keep profiles current without building those pipelines yourself.

For more information, see Chord.

#### Better Email - Templates

Better Email is a collaborative email creation platform built around an Email Design System. Teams can design, manage, and export production-ready emails from a shared system of blocks and styles, ensuring brand consistency at scale without relying on developers or agencies.

For more information, see Better Email.

#### DailyPlay - Dynamic Content

DailyPlay is a gamification platform. Use it to launch personalized, branded games and built-in reward systems that deepen engagement and improve retention.

For more information, see DailyPlay.

### SDK

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Flutter SDK 19.0.0

- The minimum supported Dart version is 2.17.0.
 
- SDK logging is now controlled on the Dart layer.
 
- Updates the native SDK bindings, including the native Android bridge from Braze Android SDK 41.1.1 to 42.2.0.
 
- Fixes a crash.

- Cordova 16.0.1

- Fixes iOS initialization when using cordova-ios 8 with the SwiftDelegate template.

- Unity SDK 11.0.0

- Updates the native SDK bindings, including the native iOS bridge from Braze Swift SDK 13.2.0 to 14.1.0.
 
- Updates the native Android bridge from Braze Android SDK 36.0.0 to 42.2.0.

- The minimum required Android SDK version is 23. For more information, see Braze Android SDK version information.

- Updated the minimum required Unity version to Unity 6 (6000.0.66f2 or later).
 
- Removed News Feed.

- Removed RequestFeedRefresh(), RequestFeedRefreshFromCache(), LogFeedDisplayed(), LogCardImpression(string), LogCardClicked(string).

- Fixes minor bugs.

- React Native 20.1.0

- Updates the Android SDK bindings.
 
- Fixes a push notification deep linking issue.

- Segment Swift 8.0.0

- Updates the Braze Swift SDK bindings to require releases from the 14.0.0+ SemVer denomination.

- This allows compatibility with any version of the Braze SDK from 14.0.0 up to, but not including, 15.0.0.
 
- Refer to the changelog entry for 14.0.0 for more information on potential breaking changes.

- Adds support for SDK Authentication.

April 30, 2026

## April 30, 2026 release

### Data & Reporting

#### Quick User Add for individual profile creation

 General availability

You can now create an individual user profile from Import Users by selecting Quick User Add and entering an email or external ID.

Previously, creating users from this workflow required CSV upload or an automated ingestion method.

For more information, see CSV import.

#### Zero-copy CDI syncs for Canvas triggers

 General availability

CDI now supports the Canvas triggers data type for zero-copy personalization. You can trigger Canvases from warehouse or S3 data and pass context fields without persisting those fields on Braze user profiles.

Previously, CDI syncs required data to be written to Braze profiles for this type of personalization workflow.

For more information, see Zero-copy personalization using CDI.

#### eCommerce recommended events

 General availability

eCommerce recommended events cover six steps in the purchase journey: product_viewed, cart_updated, checkout_started, order_placed, order_cancelled, and order_refunded. When you successfully send these events, Braze validates the data and makes it available to a growing set of platform features.

### Currents and Datashare

#### New Banner and WhatsApp Currents updates

 General availability

Currents and Datashare now include a new Banner.Dismiss event and additional fields for existing WhatsApp events.

Previously, these Banner dismissal events and WhatsApp fields were not available in export data.

For more information, see Currents changelog.

### Orchestration

#### Multi-language translations

 General availability

Compose multi-language messages with quick, one-time locale setup that doesn’t require complex code and enables you send to all of your markets with confidence.

#### Granular permissions migration

 General availability

Managing who can access your account and perform specific actions is critical for both security and operational efficiency. To give you more control, Braze is introducing granular permissions, a more flexible and precise way to manage user access across your account.

#### Send to Destination Canvas component

 General availability

The Send to Destination step allows you to send users from one Canvas to another. For example, if you have two Canvases that share messaging for promotional offers, you can use Send to Destination to connect these Canvases.

#### Canvas Context enhancements

 General availability

In Canvas, you can now reference context variables to set:

- A removal event for Content Cards
 
- The expiration of Content Cards

For more details, see Card creation.

#### Delivery validation advancement behavior for Message steps

 General availability

Delivery validations provide an additional check to confirm your audience meets the delivery criteria at message send. If a user doesn’t meet the set delivery validations for a Message step, you can use the Delivery validations advancement behavior setting to determine if the user should advance to the next step or exit the Canvas.

#### Workspace messaging rate limits

 General availability

Use workspace messaging rate limits to regulate the delivery rate of your outgoing messages from your platform to make sure your users are receiving the messages they need to. Workspace messaging rate limits are rolling out gradually, so you may not see these settings in your dashboard yet.

### Channels & Touchpoints

#### WhatsApp Template Builder

 Early access

The WhatsApp Template Builder lets you create and submit WhatsApp message templates directly in Braze—no need to switch between Braze and the Meta Business Manager. After Meta approves your template, use it in as many campaigns and Canvases as you’d like.

#### Shopify product tags, metafields, and collections

 General availability

You can now sync Shopify product tags, collections, and metafields from your Shopify store into your Braze catalog. This provides richer product data for personalization, segmentation, and catalog-based messaging without custom workarounds.

### Partnerships

#### GRAVITY - Data and Analytics - Loyalty

 General availability

GRAVTY® is an enterprise-grade loyalty platform from Loyalty Juggernaut Inc. (LJI) that enables brands across retail, travel, restaurants (including quick-service restaurants), and financial services to design, manage, and scale next-generation programs—driving measurable growth in engagement, retention, and customer lifetime value through personalized, data-led experiences.

### SDK

The following SDK updates have been released. For more details, see SDK changelogs.

#### SDK breaking updates

 General availability

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- React Native SDK 19.2.0

- Delayed initialization support.

- Android SDK 42.0.0

- Bug fixes for In-app messages and Banners.

- Swift SDK 14.1.0

- Banner dismissals support.

- Web SDK 6.7.0

- Banner dismissals support.

- Android SDK 42.1.0

- Banner dismissals support.

- Braze Segment Android 17.0.0

- This is the final release of the Braze Segment Android plugin because it uses Analytics-Android, which reached end-of-support in March 2026. Migrate to the Braze Segment Kotlin plugin, which uses Analytics-Kotlin.
 
- Upgrades native SDK versions.

April 2, 2026

## April 2, 2026 release

### Data & Reporting

#### New Banner channel fields in Currents and Datashare events

Braze added fields for existing Banner channel events in Currents and Datashare exports. For a list of these event and field updates, see Changes in Version 7.

#### Mixpanel EU and India data center support for Currents

The Currents Mixpanel integration now supports Mixpanel’s EU and India data centers. When you configure a Mixpanel integration, you can choose which Mixpanel region Braze sends your data to. This update supports Mixpanel’s growing international footprint for mutual customers. For more information, see Mixpanel.

#### Reusable Cloud Data Ingestion (CDI) sources and syncs

 Early access

Cloud Data Ingestion (CDI) has a new design that separates sources and syncs, so you can reuse one source across multiple syncs. Existing syncs migrate automatically to the new sources and syncs model with no downtime. Go to Cloud Data Ingestion > Sources to view, edit, or create sources, then select a source from the dropdown when creating a sync. This change reduces repetitive setup, and creates a foundation for future enhancements. For more information, see Setting up data warehouse integrations.

### BrazeAITM

#### File support tickets from BrazeAI OperatorTM

 General availability

BrazeAI Operator now includes a flow to file Braze support tickets without leaving the dashboard. For steps, auto-included context, and tips for faster resolution, see File support tickets with BrazeAI Operator.

### Orchestration

#### Multi-language translations

 General availability

After adding locales to your workspace, use multi-language translations to target users in different languages all within a single push, email, Banner, in-app message, or Content Block.

#### Canvas Context enhancements

 General availability

In Canvas, you can now reference context variables to set:

- An expiration for Banners and in-app messages in a Message step
 
- A personalized delays for Action Paths steps

In the Context variable name field, you can also enter the context variable name or select it from the dropdown in the step editor. For more details, see Context and Context variables.

### Channels & Touchpoints

#### KakaoTalk

 General availability

KakaoTalk is a messaging channel that enables broadcast messaging and 1:1 chat with users. Create a personalized user experience by using Liquid and other dynamic content to build an environment that fosters and enhances a rich user experience with your brand.

#### Banners in Canvas

 General availability

You can use Banners as a messaging channel in Canvas Message steps. Banners allow you to personalize app or website content dynamically, reflecting real-time user eligibility and behavior.

### Partnerships

#### CataBoom - Message Personalization - Visual and Interactive Content

CataBoom is a gamification platform. Brands use it to build and launch interactive digital experiences, including spin-to-win games, quizzes, and instant-win games. Those experiences deepen engagement and collect first-party data.

#### Denada - Message Orchestration - Templates

Denada is an AI-powered marketing creative platform that lets subject matter experts create on-brand marketing materials through natural conversation. With Denada, teams can go from ideation to finished email content without needing design expertise.

#### Poq - eCommerce - Mobile app platform

Poq enables enterprise businesses to rapidly launch, manage, and scale fully native iOS and Android apps—delivering high-performance mobile experiences that drive commerce and bring your brand promise to life.

#### The Trade Desk – Canvas Audience Sync

Using the Braze Audience Sync to The Trade Desk, you can dynamically sync your first-party user data from Braze directly into The Trade Desk for ad retargeting, lookalike modeling, and suppression.

### SDK

#### Connect your Integrated Development Environment (IDE) to the Docs MCP

Use AI coding assistants to accelerate your Braze integration workflow by connecting your Integrated Development Environment (IDE) to the Braze Docs MCP through Context7. This gives your assistant direct access to current Braze documentation, so it can generate more accurate SDK guidance, code examples, and troubleshooting help in your development environment. For setup steps in Cursor, Claude Desktop, and VS Code, see Building with an LLM.

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Cordova 15.0.0

- Updated the native Android bridge from Braze Android SDK 39.0.0 to 41.1.1.
 
- Updated the native iOS bridge from Braze Swift SDK 13.2.0 to 14.0.1.
 
- Fixes an issue with subscribeToInAppMessage involving the success callback.

- Roku SDK 2.2.1

- Fixes a crash when processing a failed HTTP request for templated in-app messages while the device has intermittent or no connectivity.

- Web SDK 6.6.0

- Adds the cookieExpiryInDays initialization option to configure cookie duration from the default of 400 days.

- Flutter SDK 18.0.0

- Adds delayed initialization support.
 
- Streamlines the iOS integration process to not require writing native code to forward Content Cards, Banners, feature flags, in-app messages, or push notification updates from the native SDK.

- The SDK will now automatically set up these subscriptions when the Braze instance is created.
 
- This matches the existing behavior on Android.
 
- To migrate, remove any manual calls to braze.contentCards.subscribeToUpdates(), braze.banners.subscribeToUpdates(), braze.notifications.subscribeToUpdates, braze.featureFlags.subscribeToUpdates and braze.inAppMessagePresenter in the AppDelegate.
 
- By default, in-app messages will be presented. To override this, set a custom in-app message presenter using the postInitialization closure in BrazePlugin.configure(_:postInitialization:).

- Swift SDK 14.0.4

- Fixes a bug with push automation on SDK re-initialization.
 
- Fixes an issue where invalid images in push stories were not filtered out.

- Swift SDK 14.0.3

March 5, 2026

## March 5, 2026 release

### Data & Reporting

#### New data center

 General availability

Braze has launched a new data center: JP-01. You can sign up for region-specific data centers when setting up your Braze account.

#### Context variables

 General availability

Context variables are temporary pieces of data you can create and use within a user’s journey through a specific Canvas. Each time a user enters the Canvas—even if they have entered it before—the context variables will be redefined based on the latest entry data and Canvas setup. This approach allows each Canvas entry to maintain its own independent context, allowing users to have multiple active states within the same journey while retaining the specific context for each state.

#### Cloud Data Ingestion sources

 Early access

Cloud Data Ingestion has a new UI that separates sources from syncs, letting you reuse a single source across any number of syncs. This reduces duplicate configuration and simplifies setup when you have multiple syncs. If you have existing syncs, they’re automatically migrated to the new sources-and-syncs structure with no downtime. To get started, go to Cloud Data Ingestion > Sources to view, edit, or create sources, then select a source from the dropdown when creating a sync.

#### Additional fields for Currents and Data Share events

 General availability

Currents and Data Share events now include the following new fields to deepen the data available for analytics and downstream systems:

- agentconsole.AgentExecuted: Added error (string)—a description of any error that occurred.
 
- agentconsole.ToolInvocation: Added request_id (string)—a unique ID for the overall LLM request and complete execution.
 
- users.messages.rcs.InboundReceive: Added canvas_variation_name (string)—the name of the Canvas variation the user received.

#### Campaign and Canvas fields for Snowflake Data Share

 General availability

Snowflake Data Share now includes additional fields reflecting Campaign and Canvas information across 66 existing tables, including:

- campaign_name
 
- canvas_name
 
- canvas_step_name
 
- canvas_variation_name
 
- message_variation_name
 
- conversion_behavior
 
- experiment_split_name

#### CSV pre-import validation and error reporting

 General availability

CSV user imports now support pre-import validation and detailed error reporting. Before importing, select Validate file before importing on the Import Users page—Braze will scan your file and generate a report identifying rows that will fail entirely (errors) and rows that will succeed with some values skipped (warnings). You can download the report, fix your CSV, and re-upload, or proceed as-is. After the import completes, a downloadable report of any rows that failed is also available, with the exact reason for each issue.

#### Messaging diagnostics dashboard

 Early access

The Messaging Diagnostics dashboard provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected.

### BrazeAITM

#### Braze Agents in Agent Console

 General availability

Braze Agents are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences. When you create an agent, you define its purpose and set guardrails for how it should behave. After it’s live, the agent can be deployed in Braze to generate personalized copy, make real-time decisions, or update catalog fields.

### Orchestration

#### Granular user permissions

 Early access

Braze is introducing granular permissions, a more flexible way to manage user access. Refer to Migrating to granular permissions to learn about the migration process, including how legacy permissions map to granular permissions.

#### Channel-based rate limiting

 General availability

When setting a delivery speed rate limit for a multi-channel campaign or Canvas, you can choose to set either a shared rate limit or a channel-based limit. When a multichannel campaign or Canvas uses channel-based rate limiting, the rate limit applies to each of the selected channels. For example, you can set your campaign or Canvas to send a maximum of 5,000 webhooks and 2,500 SMS messages per minute across the campaign or Canvas.

#### Canvas Context step

 General availability

Canvas Context steps let you create and update one or more variables for a user as they move through a Canvas. For example, if you have a Canvas that manages seasonal discounts, you can use a context variable to store a different discount code each time a user enters the Canvas.

### Channels & Touchpoints

#### Translate locales in Content Blocks

 Early access

After adding locales to your workspace, you can target users in different languages all within a Content Block.

### Partnerships

#### Algolia - Search Recommendations

Algolia is a search and discovery platform that helps developers build fast, relevant, and scalable search experiences. With a powerful API-first approach, Algolia combines advanced ranking algorithms with AI-driven insights for seamless site search, navigation, and personalized content discovery.

#### Anthropic - AI Model Provider

Anthropic is an AI safety and research company developing Claude, a next-generation AI assistant built to be helpful, honest, and safe for a wide range of language tasks.

#### Canva - Message Personalization - Creative Studio

Canva syncs your images in Canva directly to the Braze Media library, streamlining your creative workflow and keeping your visual assets up to date across all your messaging channels.

#### DOTS.ECO - Rewards

DOTS.ECO lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

#### Figma - Message Personalization - Creative Studio

Figma is a collaborative design platform that allows you to build, design, and prototype products. Use this integration to send images and visual assets from Figma directly into the Braze media library.

#### Flybuy - Message Personalization - Location

Flybuy by Radius Networks is the leading omnichannel location platform leveraging AI-powered technology to optimize speed of service across pickup, delivery, drive-thru, and dine-in. Through its integrated Marketing Suite, Flybuy also enables brands to deliver hyper-targeted, moment-based messages, helping to drive engagement, increase check size, and support broader loyalty initiatives.

#### Google Gemini - AI Model Provider

Google Gemini is Google’s family of AI models that combines advanced reasoning across text, code, and images to help brands deliver smarter, more personalized experiences.

#### Limbik - Message Personalization - Personalization Engines

Limbik is your AI resonance layer—predicting how real audiences interpret and respond to messages, concepts, and AI outputs before they reach the market. Powered by continuous primary research across 60+ countries and 25+ languages, Limbik delivers human-validated synthetic audiences—digital populations that simulate real audience response at machine speed and with research-grade accuracy (95% confidence, 1.5% to 3% margin of error). Limbik gives you the ability to immediately ensure your messaging resonates with what your target audience believes and feels.

#### Linkrunner - Message Orchestration - Attribution

Linkrunner is a mobile attribution and analytics platform that helps you track and analyze your user acquisition campaigns.

#### Mailizio - Message Orchestration - Templates

Mailizio is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio’s integration to Braze, you can export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

#### Open Loyalty - Data and Analytics - Loyalty

Open Loyalty is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user’s loyalty status changes.

#### OpenAI - AI Model Provider

OpenAI creates advanced AI models, like GPT, that enable natural language understanding and generation, empowering brands to build and scale meaningful customer interactions.

#### Shopgate - Channels

Shopgate is a mobile commerce and omnichannel platform that helps merchants create shopping apps and improve the efficiency of brick-and-mortar stores through fulfillment tools and clienteling, meaning personalized in-store customer support based on customer data.

#### Splio - Data and Analytics - Cohort Import

Splio is an audience-building tool that lets you increase the number of campaigns and revenue without harming customer experience, and provides analytics to track the performance of CRM campaigns both online and offline.

### SDK

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Android SDK 41.1.1
 
- Flutter SDK 17.1.0
 
- Swift SDK 14.0.2
 
- Xamarin SDK 9.0.0

- Updated the Android binding from Braze Android SDK 37.0.0 to 41.0.0.
 
- Updated the iOS binding from Braze Swift SDK 13.3.0 to 14.0.1.
 
- Added new transitive NuGet dependencies required by the Braze Android SDK:

- Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
 
- Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
 
- Xamarin.Kotlin.StdLib has been updated from 2.0.21.3 to 2.3.0.1. If your project explicitly pins this package to an older version, you will need to update it to avoid restore errors.

- Removed the News Feed feature.

- This feature was removed from the native Android SDK in version 38.0.0.
 
- This feature was removed from the native Swift SDK in version 14.0.0.

- The BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData enum case has been renamed to BRZInAppMessageDismissalReason.WipeData.

- Expo Plugin 4.0.0

- This version requires 19.0.0 of the Braze React Native SDK.
 
- (Android) Fixed a memory leak in the data persistence layer.
 
- (Android) Added support for Braze.getInitialPushPayload() to handle push notification deep links when the app is launched from a terminated state. This resolves an issue where deep links from push notifications were not handled on Android when the app was cold started.

- React Native SDK 19.0.0

- Updates the native Swift SDK version bindings from Braze Swift SDK 13.3.0 to 14.0.1.
 
- Updates the native Android SDK version bindings from Braze Android SDK 40.0.2 to 41.0.0.

February 5, 2026

## February 5, 2026 release

### BrazeAITM

#### Content Optimizer

 Beta

Content Optimizer is a continuous, high-variant content testing Canvas step that delivers automated engagement optimization. Using a drag-and-droppable interface similar to the message step, define the components to test, generate variants using AI (or enter them manually), and use Liquid tags to map these components to your message content.

Built on a non-contextual multi-armed bandit optimizer, Content Optimizer sends a single message per user, determining which combination of component variants to deliver based on predictive recommendations. As the step gathers data over time, high-performing variants naturally increase in send allocation while poor-performing variants decrease. Content Optimizer works best with repeated-send Canvases that have consistent daily user volume (at least a few thousand users per day) to enable continuous optimization.

### Data & Reporting

#### eCommerce recommended events

 Early access

To match eCommerce recommended events with the existing purchase event, we added the “Places Order” conversion event, which is similar to “Makes Purchase”.

### Channels & Touchpoints

#### Translate locales in banners

 Early access

After adding locales to your workspace, target users in different languages all within a single banner.

#### Configure width for drag-and-drop Content Blocks

Adjust the width of your Content Block by selecting the button in the navigation menu. The default width is 100% when not specified in your email global style settings; otherwise, the global settings will be honored.

#### Use automated IP warming

 Early access

Use automated IP warming to gradually increase your daily send volume, allowing inbox providers to learn and trust your sending patterns. Braze sends to your most engaged subscribers first, which allows daily volume to grow at a pace that matches best practices.

### Partnerships

#### LinkedIn – Canvas Audience Sync

Using the Braze Audience Sync to LinkedIn, add user data from your Braze integration to LinkedIn customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria normally used to trigger a message (such as push, email, SMS, and webhook) in a Braze Canvas based on user data can now trigger an ad to that user in your LinkedIn customer lists.

#### Oracle Crowdtwist - Data & analytics

Oracle Crowdtwist is a leading cloud-native customer loyalty solution to empower brands to offer personalized customer experiences. Their solution offers over 100 out-of-the-box engagement paths, providing rapid time-to-value for marketers to develop a more complete view of the customer.

#### Fullstory - Dynamic Content

Fullstory’s behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, Fullstory’s patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights.

#### Open Loyalty - Data & analytics

Open Loyalty is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user’s loyalty status changes.

#### DOTS.ECO - Extensions

DOTS.ECO lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

#### Mailizio - Message orchestration

Mailizio is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio’s integration to Braze, export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

### APIs

#### Media Library POST APIs

 General availability

Media Library assets can now be added via API, enabling customers, partners, and agencies to automate more of their message creation workflows. Use the API to upload an asset file directly or copy a file from an existing URL. This feature unlocks integration and automation capabilities.

### Currents and Datashare

#### Agent Console Events for Storage destinations and Datashare

 General availability

Two new events are now available for Storage destinations (AWS S3, GCS, and Azure Blob Storage) and Snowflake Datashare: agentconsole.AgentExecuted and agentconsole.ToolInvocation. These events enable you to analyze Agent Console usage and details in your downstream systems, helping you understand and get the most out of your agent usage. Agents allow you to create and deploy intelligent agents that can perform specific tasks across Braze, including generating content in canvases or catalogs and routing users down different paths based on intelligent decisioning. For more information, see the Currents changelog.

#### New ‘Retry’ events for individual channels

 General availability

New retry events are now available for email, LINE, push notifications, SMS, webhooks, and WhatsApp channels. These events provide visibility into when frequency capping results in a scheduled message being delayed rather than aborted. When a message is deprioritized or frequency capped, it can now be retried within a configured retry window, giving you better insight into message delivery patterns and frequency capping impacts. For more information, see the Currents changelog.

#### Add new ‘time_ms’ field to TokenStateChange event

 General availability

A new time_ms field has been added to the users.behaviors.pushnotification.TokenStateChange event, providing millisecond-level granularity for tracking push token state changes. This enhanced precision helps you understand the latest status of a push token when multiple changes occur within the same second, giving you confidence in downstream systems that you have the correct subscription status. For more information, see the Currents changelog.

#### Send Anonymous user to Tealium Destinations

 General availability

Events that do not have an external user ID defined can now be streamed to Tealium destinations. When you select the “Include events from anonymous users” checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

##### Send Anonymous user to CustomHTTP Destinations

 Beta

Events that do not have an external user ID defined can now be streamed to CustomHTTP destinations. When you select the “Include events from anonymous users” checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

#### Email Open event — “machine_open” field

The Email Open event now generates the “machine_open” field value to report on the Machine Open metric.

### SDK

The following SDK updates have been released. Swift SDK v14.0.1 fixes an issue with the handling of universal links. Android SDK v40.2.0 fixes a potential memory leak and resolves an issue with multiple sessions being opened when transparent activities are present. Expo SDK v3.2.0 adds the forwardUniversalLinks option (default: false) to configure the native Swift SDK handling of universal links.

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Android SDK 41.0.0

- Renamed BrazeConfig.Builder.setIsLocationCollectionEnabled() to setIsAutomaticLocationCollectionEnabled().
 
- Renamed BrazeConfig.isLocationCollectionEnabled to isAutomaticLocationCollectionEnabled.
 
- Renamed BrazeConfigurationProvider.isLocationCollectionEnabled to isAutomaticLocationCollectionEnabled.

- Android SDK 40.2.0
 
- Expo Plugin 3.2.0
 
- Swift SDK 14.0.1

- 

New Stuff!
