---
url: https://www.braze.com/docs/releases/2025/11_11_25
slug: docs__releases__2025__11_11_25
title: "November 11, 2025 release"
description: "This article contains release notes for November 11, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# November 11, 2025 release

## Data flexibility

### Live Activities Push to Start Registered for App segmentation filter

The Live Activities Push to Start Registered for App filter segments your users by whether they are registered to start a Live Activity through iOS push notifications for a specific app.

### RFM SQL Segment Extension

You can create an RFM (recency, frequency, monetary) Segment Extension to target your best users by measuring their purchasing habits.

RFM analysis is a marketing technique that identifies your best users by scoring users on a scale from 0—3 for each category (recency, frequency, monetary), where 3 is the best score and 0 is the worst. Recency, frequency, and monetary values are all based on data from a specific time range of your choosing.

### Custom attributes — Values

When viewing a usage report, select the Values tab to view the top values of the selected custom attributes based on a sample of approximately 250,000 users.

### Sync logs and observability for Cloud Data Ingestion

 General availability

The Cloud Data Ingestion (CDI) Sync Log dashboard allows you to monitor all data processed by CDI, verify whether data was synced successfully, and diagnose any issues with “incorrect” or missing data.

### Multi-rule feature flag rollouts

Use multi-rule feature flag rollouts to define a sequence of rules for evaluating users, which allows for precise segmentation and controlled feature releases. This method is ideal for deploying the same feature to diverse audiences.

### Mapping to catalog fields for drag-and-drop product blocks

In your catalog settings, you can select the Product blocks toggle to map to specific fields and information in your catalog. This allows you to select which fields to use as the product title, product URL, and image URL.

### Frequency capping abort events in Currents

When using Currents, you can now reference abort_type in the channel abort events. This identifies that a message has been aborted due to frequency capping and includes which frequency capping rule caused the abort. This helps inform how you set up your frequency capping rules. Refer to Message engagement events for specific Currents event details.

## Robust channels

### Background row images

 General availability

You can add a background row image to an in-app message or landing page in the Row properties panel. Toggle on Background image, and then provide an image URL or select an image from the media library. Finally, configure your alt text, size, position, and whether the image repeats to create patterns across the row.

### Copy preview link

Use Copy preview link in your Banners, email custom footers, and email opt-in and unsubscribe pages to generate a shareable link that shows how your content looks for a random user.

### WhatsApp messages with optimized delivery

Use Meta’s advanced AI systems to deliver your marketing messages to more users who are most likely to engage with them, significantly boosting deliverability and message engagement.

WhatsApp messages with optimized delivery are sent using Meta’s new Marketing Messages Lite API, which provides superior performance compared to the traditional Cloud API. This new sending pipeline helps you better reach users who value and want to receive your messages.

### WhatsApp Flows

When incorporating a WhatsApp Flow message into a Braze Canvas or campaign, you may want to capture and utilize specific information that users submit through the Flow. Braze needs to receive additional information regarding the structure of the user response, specifically the expected shape of the JSON response, to generate the required nested custom attribute (NCA) schema.

Now you can give Braze the information about the response structure by saving the Flow response as a custom attribute and completing a test send.

### Editable user preview

You can edit individual fields from a random or existing user to help test dynamic content within your message. Select Edit to convert the selected user into a custom user you can modify.

## AI and ML automation

### BrazeAI Decisioning Studio™ Go

You can now set up your integration with BrazeAI Decisioning Studio™ Go by referencing these configuration articles for:

- Braze
 
- Klaviyo
 
- Salesforce Marketing Cloud

### New features for Braze Agents

 Beta

You can now customize your Braze Agent by:

- Applying brand guidelines for your agent to adhere to in its response.
 
- Referencing a catalog to further personalize your message.
 
- Structuring an agent’s output by providing the output format.
 
- Adjusting the temperature for the level of deviation for your agent’s output.

### ChatGPT models with BrazeAITM Operator

 Beta

You can select from these GPT models to use for different request types with Operator:

- GPT-5 nano
 
- GPT-5 mini (default)
 
- GPT-5

## New Braze partnerships

### StackAdapt - Advertising

StackAdapt is an AI-powered marketing platform that delivers targeted performance-driven advertising. It allows you to sync user profile data from Braze into the StackAdapt Data Hub. By connecting the two platforms, you can create a unified view of your customers and activate first-party data to improve ad performance.

### Cloudinary - Dynamic content

Cloudinary is an image and video platform that empowers you to manage, edit, optimize, and deliver images and video on a massive scale to any campaign across channels and customer journeys. When integrated and enabled, Cloudinary’s media management will power and provide dynamic, contextual, and personalized asset delivery for your Braze campaigns and Canvases.

### Kameleoon - A/B testing

Kameleoon is an optimization solution with experiment, AI-powered personalization, and feature management capabilities in a single unified platform.

## SDK updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- React Native SDK 18.0.0

- Fixes the Typescript type for the callback of subscribeToInAppMessage and addListener for Braze.Events.IN_APP_MESSAGE_RECEIVED.

- These listeners now properly return a callback with the new InAppMessageEvent type. Previously, the methods were annotated to return a BrazeInAppMessage type, but it was actually returning a String.
 
- If you are using either subscription API, ensure that the behavior of your in-app messages are unchanged after updating to this version. See our sample code in BrazeProject.tsx.

- The APIs logInAppMessageClicked, logInAppMessageImpression, and logInAppMessageButtonClicked now accept only a BrazeInAppMessage object to match its existing public interface.

- Previously, it would accept both a BrazeInAppMessage object as well as a String.

- BrazeInAppMessage.toString() now returns a human-readable string instead of the JSON string representation.

- To get the JSON string representation of an in-app message, use BrazeInAppMessage.inAppMessageJsonString.

- On iOS, [[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:] has been moved to [BrazeReactDataTranslator formatPushPayload:withLaunchOptions:].

- This new method is a now a class method instead of an instance method.

- Adds nullability annotations to BrazeReactUtils methods.
 
- Removes the following deprecated methods and properties from the API:

- getInstallTrackingId(callback:) in favor of getDeviceId.
 
- registerAndroidPushToken(token:) in favor of registerPushToken.
 
- setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:) in favor of setAdTrackingEnabled.
 
- PushNotificationEvent.push_event_type in favor of payload_type.
 
- PushNotificationEvent.deeplink in favor of url.
 
- PushNotificationEvent.content_text in favor of body.
 
- PushNotificationEvent.raw_android_push_data in favor of android.
 
- PushNotificationEvent.kvp_data in favor of braze_properties.

- Updates the native Android SDK version bindings from Braze Android SDK 39.0.0 to 40.0.2.

- .NET MAUI (Xamarin) SDK Version 8.0.0

- Updated the iOS binding from Braze Swift SDK 12.1.0 to 13.3.0. This includes Xcode 26 support.

- Flutter SDK 16.0.0

- Updates the native Android bridge from Braze Android SDK 39.0.0 to 40.0.0.

- Braze Swift SDK 13.3.0
 
- Web SDK 6.3.0
 
- Android SDK 40.0.0-40.0.2

- 

New Stuff!
