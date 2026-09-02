---
url: https://www.braze.com/docs/releases/2026/2_5_26
slug: docs__releases__2026__2_5_26
title: "February 5, 2026 release"
description: "This article contains release notes for 2/5/2026."
section: releases/2026
fetched: 2026-09-02
evidence: company-own (technical)
---
# February 5, 2026 release

## BrazeAITM

### Content Optimizer

 Beta

Content Optimizer is a continuous, high-variant content testing Canvas step that delivers automated engagement optimization. Using a drag-and-droppable interface similar to the message step, you can define the components you want to test, generate variants using AI (or enter them manually), and use Liquid tags to map these components to your message content.

Built on a non-contextual multi-armed bandit optimizer, Content Optimizer sends a single message per user, determining which combination of component variants to deliver based on predictive recommendations. As the step gathers data over time, high-performing variants naturally increase in send allocation while poor-performing variants decrease. Content Optimizer works best with repeated-send Canvases that have consistent daily user volume (at least a few thousand users per day) to enable continuous optimization.

## Data & Reporting

### eCommerce recommended events

 Early access

To match eCommerce recommended events with the existing purchase event, we added the “Places Order” conversion event, which is similar to “Makes Purchase”.

## Channels & Touchpoints

### Translate locales in banners

 Early access

After adding locales to your workspace, you can target users in different languages all within a single banner.

### Configure width for drag-and-drop Content Blocks

Adjust the width of your Content Block by selecting the button in the navigation menu. The default width is 100% when not specified in your email global style settings; otherwise, the global settings will be honored.

### Use automated IP warming

 Early access

You can use automated IP warming to gradually increase your daily send volume, allowing inbox providers to learn and trust your sending patterns. Braze sends to your most engaged subscribers first, which allows daily volume to grow at a pace that matches best practices.

## Partnerships

### LinkedIn – Canvas Audience Sync

Using the Braze Audience Sync to LinkedIn, you can add user data from your Braze integration to LinkedIn customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (such as push, email, SMS, and webhook) in a Braze Canvas based on your user data can now trigger an ad to that user in your LinkedIn customer lists.

### Oracle Crowdtwist - Data & analytics

Oracle Crowdtwist is a leading cloud-native customer loyalty solution to empower brands to offer personalized customer experiences. Their solution offers over 100 default engagement paths, providing rapid time-to-value for marketers to develop a more complete view of the customer.

### Fullstory - Dynamic Content

Fullstory’s behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, Fullstory’s patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights.

### Open Loyalty - Data & analytics

Open Loyalty is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user’s loyalty status changes.

### DOTS.ECO - Extensions

DOTS.ECO lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

### Mailizio - Message orchestration

Mailizio is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio’s integration to Braze, you can export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

## APIs

### Media Library POST APIs

 General availability

Media Library assets can now be added via API, enabling customers, partners, and agencies to automate more of their message creation workflows. You can use the API to upload an asset file directly or copy a file from an existing URL. This feature unlocks integration and automation capabilities.

## Currents and Datashare

### Agent Console Events for Storage destinations and Datashare

 General availability

Two new events are now available for Storage destinations (AWS S3, GCS, and Azure Blob Storage) and Snowflake Datashare: agentconsole.AgentExecuted and agentconsole.ToolInvocation. These events enable you to analyze Agent Console usage and details in your downstream systems, helping you understand and get the most out of your agent usage. Agents allow you to create and deploy intelligent agents that can perform specific tasks across Braze, including generating content in canvases or catalogs and routing users down different paths based on intelligent decisioning. For more information, see the Currents changelog.

### New ‘Retry’ events for individual channels

 General availability

New retry events are now available for email, LINE, push notifications, SMS, webhooks, and WhatsApp channels. These events provide visibility into when frequency capping results in a scheduled message being delayed rather than aborted. When a message is deprioritized or frequency capped, it can now be retried within a configured retry window, giving you better insight into message delivery patterns and frequency capping impacts. For more information, see the Currents changelog.

### Add new ‘time_ms’ field to TokenStateChange event

 General availability

A new time_ms field has been added to the users.behaviors.pushnotification.TokenStateChange event, providing millisecond-level granularity for tracking push token state changes. This enhanced precision helps you understand the latest status of a push token when multiple changes occur within the same second, giving you confidence in downstream systems that you have the correct subscription status. For more information, see the Currents changelog.

### Send Anonymous user to Tealium Destinations

 General availability

Events that do not have an external user ID defined can now be streamed to Tealium destinations. When you select the “Include events from anonymous users” checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

#### Send Anonymous user to CustomHTTP Destinations

 Beta

Events that do not have an external user ID defined can now be streamed to CustomHTTP destinations. When you select the “Include events from anonymous users” checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

### Email Open event — “machine_open” field

The Email Open event now generates the “machine_open” field value so you can report on the Machine Open metric.

## SDK

The following SDK updates have been released. Swift SDK v14.0.1 fixes an issue with the handling of universal links. Android SDK v40.2.0 fixes a potential memory leak and resolves an issue with multiple sessions being opened when transparent activities are present. Expo SDK v3.2.0 adds the forwardUniversalLinks option (default: false) to configure the native Swift SDK handling of universal links.

### SDK breaking updates

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
