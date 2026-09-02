---
url: https://www.braze.com/docs/releases/2025/8_19_25
slug: docs__releases__2025__8_19_25
title: "August 19, 2025 release"
description: "This article contains release notes for August 19, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# August 19, 2025 release

## Time zone consistency standardization to Canvas Context

 Early access

If you’re participating in the Canvas Context step early access, all timestamps with a datetime type from trigger event properties in action-based Canvases will always be normalized to UTC. To learn more about this, refer to Time zone consistency standardization.

## Data flexibility

### Self-serve custom domains

Self-serve custom domains empower you to configure and manage your own custom domains for SMS, RCS, and WhatsApp—directly from your Braze dashboard. You can easily add, monitor, and manage up to 10 custom domains in one place.

### Segment funnel statistics

Select View funnel statistics to display the statistics for that filter group and see how each added filter impacts your segment statistics. You’ll see an estimated count and percentage for users who are targeted by all filters up to that point. After the statistics are displayed for a filter group, they will update automatically whenever you change the filters.

### New response fields for /campaigns/details endpoint for push notifications

The messages response for push notifications now includes two new fields:

- image_url: An image URL for an Android notification image, an iOS notification image, or a web push icon image.
 
- large_image_url: A web notification image URL for Android Chrome and Windows web push actions.

### Defining PII fields

Selecting and defining certain fields as PII fields only affects what Users can view on the Braze dashboard and does not impact how the End User data in such PII fields is handled.

Consult your legal team to align your dashboard’s settings with any privacy regulations and policies applicable to your company, including those related to data retention.

### Sharing a Report Builder download link

You can share a dashboard link to the report by selecting Share and then Share a link or Send or schedule an email.

## Unlocking creativity

### Custom head tags for drag-and-drop emails

Use <head> tags to add CSS and metadata in your email message. For example, you can use these tags to add a stylesheet or favicon. Liquid is supported in <head> tags.

## Robust channels

### Fuzzy out-out best practices

We’ve added a best practices section to help you thoughtfully configure your fuzzy opt-out message and create a clear, compliant, and positive experience for your subscribers.

### WhatsApp Flows

 Early access

WhatsApp Flows is an enhancement to the existing WhatsApp channel, allowing you to create interactive and dynamic messaging experiences.

### WhatsApp inbound product questions

Users can respond to your product or catalog message with product questions. These arrive as inbound messages, which can then be sorted with an Action Path.

Additionally, Braze extracts the product ID and catalog ID from these questions, so if you wish to automate responses or send questions to another team (such as customer support), you can include those details.

## AI and ML automation

### New BrazeAI™ use case articles

We’ve added new use case articles to help you get the most out of BrazeAI™. These guides highlight practical ways to apply AI to your engagement strategies, including:

- Predictive Churn: Identify customers at risk of churning and take action early.
 
- Predictive Events: Anticipate key user actions and shape experiences in real time.
 
- Recommendations: Deliver more relevant content and products based on customer behavior.

### MCP server

 Beta

The Braze MCP server, a secure and read-only connection, lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, and provide insights without altering data.

## SDK updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Swift SDK 13.0.0

- Extends the functionality of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:) to be triggered for “Optional” authentication errors.

- The delegate method BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:) will now be triggered for both “Required” and “Optional” authentication errors.
 
- If you want to only handle “Required” SDK authentication errors, add a check ensuring that BrazeSDKAuthError.optional is false inside your implementation of this delegate method.

- Fixes the usage of Braze.Configuration.sdkAuthentication to take effect when enabled.

- Previously, the value of this configuration was not consumed by the SDK and the token was always attached to requests if it was present.
 
- Now, the SDK will only attach the SDK authentication token to outgoing network requests when this configuration is enabled.

- The setters for all properties of Braze.FeatureFlag and all properties of Braze.Banner have been made private. The properties of these classes are now read-only.
 
- Removes the Braze.Banner.id property, which was deprecated in version 11.4.0.

- Instead, use Braze.Banner.trackingId to read a banner’s campaign tracking ID.

- React Native SDK 16.0.0

- Updates the native Android SDK version bindings from Braze Android SDK 36.0.0 to 37.0.0.
 
- Updates the native Swift SDK version bindings from Braze Swift SDK 12.0.0 to 13.0.0.

- The sdkAuthenticationError event will now trigger for both “Required” and “Optional” authentication errors.

- Xamarin SDK 7.0.0

- Added support for .NET 9.0 for the iOS and Android bindings.

- This removes support for .NET 8.0.
 
- This requires a minimum version of iOS 12.2.

- Updated the Android binding from Braze Android 32.0.0 to 37.0.0.
 
- Updated the iOS binding from Braze Swift SDK 10.0.0 to 12.1.0.
 
- This release contains APIs for the Banners feature but is not currently fully supported by this SDK. If you wish to use Banners in your .NET MAUI app, contact your customer support manager before integrating into your application.

- Cordova SDK 13.0.0

- Updated the internal iOS implementation of enableSdk method to use setEnabled: instead of _requestEnableSDKOnNextAppRun, which was deprecated in the Swift SDK.
 
- Calling this method no longer requires the app to be re-launched to take effect. The SDK will now become enabled as soon as this method is executed.
 
- Updated the native Android bridge from Braze Android SDK 36.0.0 to 37.0.0.

- 

New Stuff!
