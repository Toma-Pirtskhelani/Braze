---
url: https://www.braze.com/docs/releases/2026/4_30_26
slug: docs__releases__2026__4_30_26
title: "April 30, 2026 release"
description: "This article contains release notes for April 30, 2026."
section: releases/2026
fetched: 2026-09-02
evidence: company-own (technical)
---
# April 30, 2026 release

## Data & Reporting

### Quick User Add for individual profile creation

 General availability

You can now create an individual user profile from Import Users by selecting Quick User Add and entering an email or external ID.

Previously, creating users from this workflow required CSV upload or an automated ingestion method.

For more information, see CSV import.

### Zero-copy CDI syncs for Canvas triggers

 General availability

CDI now supports the Canvas triggers data type for zero-copy personalization. You can trigger Canvases from warehouse or S3 data and pass context fields without persisting those fields on Braze user profiles.

Previously, CDI syncs required data to be written to Braze profiles for this type of personalization workflow.

For more information, see Zero-copy personalization using CDI.

### eCommerce recommended events

 General availability

eCommerce recommended events cover six steps in the purchase journey: product_viewed, cart_updated, checkout_started, order_placed, order_cancelled, and order_refunded. When you successfully send these events, Braze validates the data and makes it available to a growing set of platform features.

## Currents and Datashare

### New Banner and WhatsApp Currents updates

 General availability

Currents and Datashare now include a new Banner.Dismiss event and additional fields for existing WhatsApp events.

Previously, these Banner dismissal events and WhatsApp fields were not available in export data.

For more information, see Currents changelog.

## Orchestration

### Multi-language translations

 General availability

Compose multi-language messages with quick, one-time locale setup that doesn’t require complex code and enables you send to all of your markets with confidence.

### Granular permissions migration

 General availability

Managing who can access your account and perform specific actions is critical for both security and operational efficiency. To give you more control, Braze is introducing granular permissions, a more flexible and precise way to manage user access across your account.

### Send to Destination Canvas component

 General availability

The Send to Destination step allows you to send users from one Canvas to another. For example, if you have two Canvases that share messaging for promotional offers, you can use Send to Destination to connect these Canvases.

### Canvas Context enhancements

 General availability

In Canvas, you can now reference context variables to set:

- A removal event for Content Cards
 
- The expiration of Content Cards

For more details, see Card creation.

### Delivery validation advancement behavior for Message steps

 General availability

Delivery validations provide an additional check to confirm your audience meets the delivery criteria at message send. If a user doesn’t meet the set delivery validations for a Message step, you can use the Delivery validations advancement behavior setting to determine if the user should advance to the next step or exit the Canvas.

### Workspace messaging rate limits

 General availability

Use workspace messaging rate limits to regulate the delivery rate of your outgoing messages from your platform to make sure your users are receiving the messages they need to. Workspace messaging rate limits are rolling out gradually, so you may not see these settings in your dashboard yet.

## Channels & Touchpoints

### WhatsApp Template Builder

 Early access

The WhatsApp Template Builder lets you create and submit WhatsApp message templates directly in Braze—no need to switch between Braze and the Meta Business Manager. After Meta approves your template, use it in as many campaigns and Canvases as you’d like.

### Shopify product tags, metafields, and collections

 General availability

You can now sync Shopify product tags, collections, and metafields from your Shopify store into your Braze catalog. This provides richer product data for personalization, segmentation, and catalog-based messaging without custom workarounds.

## Partnerships

### GRAVTY - Data and Analytics - Loyalty

 General availability

GRAVTY® is an enterprise-grade loyalty platform from Loyalty Juggernaut Inc. (LJI) that enables brands across retail, travel, restaurants (including quick-service restaurants), and financial services to design, manage, and scale next-generation programs—driving measurable growth in engagement, retention, and customer lifetime value through personalized, data-led experiences.

## SDK

The following SDK updates have been released. For more details, see SDK changelogs.

### SDK breaking updates

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

- 

New Stuff!
