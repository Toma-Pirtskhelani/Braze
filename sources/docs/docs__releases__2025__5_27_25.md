---
url: https://www.braze.com/docs/releases/2025/5_27_25
slug: docs__releases__2025__5_27_25
title: "May 27, 2025 release"
description: "This article contains release notes for May 27, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# May 27, 2025 release

## Data flexibility

### Copying Canvases across workspaces

 General availability

You can now copy Canvases across workspaces. This lets you jumpstart your message composition by starting with a copy of a Canvas in a different workspace. For more information on what’s copied over, refer to Copying campaigns and Canvases across workspaces.

### Messaging rules for approval workflow

 General availability

Use messaging rules in your approval workflow to limit the number of reachable users before an additional approval is required—this way, you can review your campaigns and Canvases before you target a larger audience.

### Entity relationship diagrams for Snowflake and Braze

Earlier this year, we created entity relationship tables for data shared between Snowflake and Braze. This month, we added new interactive diagrams where you can pan, grab, and zoom into the details of each table, giving you a better idea of how your data interacts with Braze.

## Unlocking creativity

### Recommended events

 Early access

Recommended events map to the most common eCommerce use cases. By using recommended events, you can unlock pre-built Canvas templates, reporting dashboards that map to the customer lifecycle, and more.

## Robust channels

### Banners channel

 General availability

With Banners, you can create personalized messaging for your users, all while extending the reach of your other channels, such as email or push notifications. You can embed Banners directly in your app or website, which lets you engage with users through an experience that feels natural.

### Rich Communication Services (RCS) channel

 General availability

Rich Communication Services (RCS) enhances traditional SMS by enabling brands to deliver messages that are not only informative but also far more engaging. Now supported on both Android and iOS, RCS brings features like high-quality media, interactive buttons, and branded sender profiles directly into users’ pre-installed messaging apps, eliminating the need to download a separate app.

### Push Settings page

 General availability

Use the Push Settings page to configure key settings for your push notifications, including the Push Time to Live (TTL) and the default FCM priority for Android campaigns. These settings help optimize the delivery and effectiveness of your push notifications, ensuring a better experience for your users.

### Promotion codes for in-app message campaigns

 Early access

You can use promotion codes in in-app message campaigns by inserting a promotion code list snippet into the message body of your in-app message campaign.

### Handling webhook errors and rate limiting

About webhooks has a new section that describes how Braze handles webhook errors and rate limiting.

### In-app message locales

After adding locales to your workspace, you can target users in different languages all within a single in-app message.

### Amazon SES as an Email Sending Provider (ESP)

You can now use Amazon SES as an ESP, similar to how you would use SendGrid and SparkPost. Refer to SSL at Braze and Universal Links and App Links for nuances in SSL set up and click-tracking on a link-to-link basis.

## New Braze partnerships

### Eagle Eye - Loyalty

The Braze and Eagle Eye bi-directional integration allows you to activate loyalty and promotional data directly in Braze, allowing marketers to personalize customer engagement using real-time data such as point balances, promotions, and reward activities.

### Eppo - A/B Testing

The Braze and Eppo integration allows you to set up A/B tests in Braze and analyze results in Eppo to uncover insights and tie message performance to long-term business metrics like revenue or retention.

### Mention Me - Referrals

Together, Mention Me and Braze can be your gateway to attracting premium customers and fostering unwavering brand loyalty. By seamlessly integrating first-party referral data into Braze, you can deliver highly-personalized omnichannel experiences targeted at your brand fans. To get started, see Technology Partners: Mention Me.

### Shopify - eCommerce

Connect multiple Shopify store domains to a single workspace to have a holistic view of your customers across all markets. Build and launch automation programs and journeys in a single workspace without duplicating efforts across regional stores.

## Other

### Update to Building accessible messages in Braze

We’ve updated our Building accessible messages in Braze article with clearer, more prescriptive guidance on creating accessible messages. This article now includes expanded best practices for content structure, alt text, buttons, and color contrast, along with a new section on ARIA handling for custom HTML messages.

This update is part of our broader effort to support more accessible messaging experiences in Braze. We know accessibility is an evolving area, and we’ll keep sharing what we learn.

If you have feedback about the accessibility of Braze or messages sent from Braze, we’d love to hear from you. Open the Support menu in the global header and select Share feedback to send us your thoughts.

## SDK updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Android SDK 36.0.0

- This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. Note that while we are re-introducing the ability to compile, we are not reintroducing formal support for < API 25, and cannot guarantee that the SDK will work as intended on devices running those versions.
 
- If your app supports those versions, you should:

- Validate your integration of the SDK works as intended on physical devices (not just emulators) for those API versions.
 
- If you cannot validate expected behavior, you must either call disableSDK, or not initialize the SDK on those versions. Otherwise, you may cause unintended side effects or degraded performance on your end users’ devices.

- Fixed an issue where in-app messages would cause a read on the main thread.
 BrazeInAppMessageManager.displayInAppMessage is now a Kotlin suspend function.

- If you do not call this function directly, you do not need to make any changes.

- AndroidX Compose BOM updated to 2025.04.01 to handle updates in the Jetpack Compose APIs.

- React Native SDK 15.0.0

- Updates the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
 
- Updates the native iOS version bindings from Braze Swift SDK 11.9.0 to 12.0.0.
 
- Updates the unit representation of PushNotificationEvent.timestamp to milliseconds on iOS.

- Previously, this value would be represented in seconds on iOS. This will now match the existing Android implementation.

- Web SDK 5.9.0
 
- Flutter SDK 14.0.0 5.9.0

- This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for < API 25. Read the Braze Android SDK changelog entry.
 
- Updates the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
 
- Updates the native iOS bridge from Braze Swift SDK 11.9.0 to 12.0.0.

- 

New Stuff!
