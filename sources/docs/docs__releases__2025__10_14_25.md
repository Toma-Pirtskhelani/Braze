---
url: https://www.braze.com/docs/releases/2025/10_14_25
slug: docs__releases__2025__10_14_25
title: "October 14, 2025 release"
description: "This article contains release notes for October 14, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# October 14, 2025 release

## BrazeAI Decisioning Studio™

BrazeAI Decisioning Studio™ replaces A/B testing with AI decisioning that personalizes everything, and maximizes any metric: drive dollars, not clicks. With BrazeAI Decisioning Studio™, you can optimize any business KPI. Refer to our dedicated section BrazeAI Decisioning Studio™ for sample use cases and key features.

## Data flexibility

### New Currents events

These new events were added to the Currents glossary:

- users.messages.rcs.Click
 
- users.messages.rcs.Rejection
 
- users.messages.line.Abort
 
- users.messages.line.Send
 
- users.messages.line.InboundReceive
 
- users.messages.line.Click
 
- users.messages.rcs.Delivery
 
- users.messages.rcs.InboundReceive
 
- users.messages.rcs.Read
 
- users.messages.rcs.Send
 
- users.messages.rcs.Abort
 
- users.messages.inappmessage.Abort

These new fields were added to the following Currents events:

- is_sms_fallback:

- users.messages.sms.Delivery
 
- users.messages.sms.DeliveryFailure
 
- users.messages.sms.Rejection

- message_id, in_reply_to, flow_id, flow_response_json, product_id, catalog_id:

- users.messages.whatsapp.InboundReceive

- message_id, flow_id, template_name:

- users.messages.whatsapp.Send
 
- users.messages.whatsapp.Delivery
 
- users.messages.whatsapp.Failure
 
- users.messages.whatsapp.Read

### Suppression lists

 General availability

Suppression lists are groups of users who automatically do not receive any campaigns or Canvases. Suppression lists are defined by segment filters, and users enter and exit suppression lists as they meet filter criteria.

### Zero-copy personalization

 Early access

Sync Canvas triggers using Cloud Data Ingestion for zero-copy personalization. This feature accesses user-specific information from your data storage solution and passes it to a destination Canvas. Canvas steps can optionally include personalization fields that are not persisted on Braze user profiles.

### Canvas Context variables for Audience Paths and Decision Split steps

 Early access

You can create context variable filters that use previously-declared context variables in Audience Paths and Decision Split steps.

## Unlocking creativity

### Deal Cards for emails

Use Deal Cards to provide key deal information directly at the top of email bodies. This allows recipients to quickly understand the offer details and take action.

### Templates for Banners

When you compose your Banner, you can now start with a blank template, use a Braze template, or select a saved Banner template.

## Robust channels

### Suppression lists

 General availability

Suppression lists specify groups of users who will never receive messages. Admins can create suppression lists with segment filters to narrow down a user group the same way you would for segmentation.

### LINE click tracking

 General availability

When LINE click tracking is turned on, Braze automatically shortens your URLs, adds tracking mechanisms, and records clicks in real time. While LINE offers aggregate click data, Braze provides granular user information that is timely and actionable. This data empowers you to create more targeted segmentation and retargeting strategies, such as segmenting users based on click behavior and triggering messages in response to specific clicks.

### SMS and RCS bot click filtering

 General availability

SMS and RCS bot click filtering enhances campaign analytics and workflows by excluding suspected bot clicks. A “bot click” refers to automated clicks on shortened links in SMS and RCS messages, such as those from web crawlers, Android and iOS link previews, or CPaaS security software. This feature facilitates accurate reporting, segmentation, and orchestration to engage real users.

### Transfer WhatsApp phone numbers

Transfer a WhatsApp Business Account (WABA) phone number and its associated subscription group from one workspace to another within Braze.

### WhatsApp Flows response messages and preview

In a Canvas, you can create a WhatsApp message step that uses a response message and flow message. You can also select Preview Flow to preview the Flow directly in Braze to confirm it behaves as expected.

### WhatsApp product messages

Product messages empower you to send interactive WhatsApp messages that showcase products directly from your Meta catalog.

### Integrating Braze and WhatsApp with an external system

Leverage the power of AI chatbots and live agent hand-offs on the WhatsApp channel to streamline your customer support operations. By automating routine inquiries and seamlessly transitioning to human agents when needed, you can significantly improve response times and enhance the overall customer experience.

## AI and ML automation

### Braze Agents

 Beta

Braze Agents are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences.

## New Braze partnerships

### Jasper - Templates

The Jasper integration with Braze empowers you to streamline content creation and campaign execution. With Jasper, your marketing teams can generate high-quality, on-brand copy in minutes. Braze then facilitates the delivery of these messages to the right audience at the optimal time. This integration fosters seamless workflows, reduces manual effort, and drives stronger engagement outcomes.

### Swym - Loyalty and retargeting

Swym helps eCommerce brands capture shopping intent with Wishlists, Save for Later, Gift Registry, and Back-in-Stock alerts. Using rich, permission-based data, you can craft hyper-targeted campaigns and deliver personalized shopping experiences that drive engagement, boost conversions, and increase loyalty.

## SDK updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Cordova SDK 14.0.0

- Updated the native Android bridge from Braze Android SDK 37.0.0 to 39.0.0.

- The minimum required GradlePluginKotlinVersion is now 2.1.0.

- Updated the native iOS bridge from Braze Swift SDK 12.0.0 to 13.2.0. This includes Xcode 26 support.
 
- Removes support for News Feed. The following APIs have been removed:

- launchNewsFeed
 
- getNewsFeed
 
- getNewsFeedUnreadCount
 
- getNewsFeedCardCount
 
- getCardCountForCategories
 
- getUnreadCardCountForCategories

- React Native SDK 17.0.0-17.0.1

- Updates the native Android SDK version bindings from Braze Android SDK 37.0.0 to 39.0.0.
 
- Removes support for News Feed. The following APIs have been removed:

- launchNewsFeed
 
- requestFeedRefresh
 
- getNewsFeedCards
 
- logNewsFeedCardClicked
 
- logNewsFeedCardImpression
 
- getCardCountForCategories
 
- getUnreadCardCountForCategories
 
- Braze.Events.NEWS_FEED_CARDS_UPDATED
 
- Braze.CardCategory

- Web SDK 6.2.0
 
- Flutter SDK 15.1.0
 
- Unity SDK 10.0.0

- Updated the native iOS bridge from Braze Swift SDK 12.0.0 to 13.2.0. This includes Xcode 26 support.

- 

New Stuff!
