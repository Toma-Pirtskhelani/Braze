---
url: https://www.braze.com/docs/releases/deprecations
slug: docs__releases__deprecations
title: "Deprecations"
description: "This page includes references to deprecated articles and provides a list of deprecated and unsupported features."
section: releases/deprecations
fetched: 2026-09-02
evidence: company-own (technical)
---
# Deprecations

Technology is always moving—inside Braze and outside it! And we do our best to keep up with it. Here, you’ll find the origins of Braze and its technology—how we supported people in the ‘before time’—before now, anyway…

You might have gotten here from searching a term for an integration or feature that no longer exists. This is our attempt to keep you informed on our progress and movement within the technology industry. You can find a list of deprecated and unsupported features and read deprecated articles by visiting the following links.

## Deprecated articles

- Custom push broadcast receiver for Android
 
- Eclipse SDK setup
 
- TLS 1.0 and 1.1 deprecation
 
- Twilio webhook integration
 
- Apptimize partnership
 
- Grouparoo partnership
 
- Shopify checkout.liquid deprecation

## Deprecations log

### Shopify checkout.liquid

Support withdrawn: August 2024 (phase 1), August 2025 (phase 2)

Support for Shopify checkout.liquid will begin deprecation in August 2024 and finish in August 2025. Shopify will be transitioning to Checkout Extensibility, which is more secure, performant, and customizable.

### Custom push broadcast receiver for Android

Support withdrawn: October 2022

Using a custom BroadcastReceiver for push notifications has been deprecated. Use subscribeToPushNotificationEvents() instead.

### Grouparoo partnership

Support withdrawn: April 2022

Support for Grouparoo has been discontinued as of April 2022.

### Braze Windows SDK

March 24, 2022: The Braze Windows SDK is deprecated, and no new Windows apps can be created in the Braze dashboard.

September 15, 2022: No new messages can be sent to Windows apps. Existing messages and data collection are unaffected.

January 11, 2024: Braze will no longer serve messages or collect data from Windows apps.

### Baidu push integration

March 24, 2022: The Braze Baidu push integration is deprecated, and no new Baidu apps can be created in the Braze dashboard. 

September 15, 2022: No new Baidu push messages can be created. Existing messages and data collection are unaffected.

January 11, 2024: Braze will no longer serve messages or collect data from Baidu apps.

### appboyBridge global variable

Support withdrawn: May 2021

Replaced by: brazeBridge

The global variable appboyBridge is deprecated and replaced by brazeBridge. appboyBridge will continue to function for existing customers, but we recommend you migrate to brazeBridge if you’re using appboyBridge.

### Amazon Moments partnership

Support withdrawn: June 2020

Support for Amazon Moments has been discontinued as of June 2020. Amazon Moments is being merged into Amazon Advertising and has deprecated their APIs and our integration.

### Factual partnership

Support withdrawn: June 2020

Support for Factual has been discontinued as of June 2020. Factual was recently acquired by Foursquare no longer integrates with the Braze Platform.

### Twilio webhook integration

Support withdrawn: January 2020

Support for the Twilio webhook integration has been discontinued as of January 31, 2020. If you wish to still access SMS services with Braze, see our SMS documentation.

### Apptimize partnership

Support withdrawn: August 2019

If you are currently using Apptimize with Braze, you will not experience a disruption of service. You can still set Apptimize custom attributes to Braze user profiles. However, no formal escalation support with the partner will be provided.

### Original in-app messages

Support withdrawn: February 2019

Replaced by: In-App Messaging

Braze has improved the look and feel of in-app messages to adhere to the latest UX and UI best practices and no longer supports the original in-app messages.

Braze moved over to a new form of in-app messages with the following SDK releases:

- iOS: 2.19.0
 
- Android: 1.13.0
 
- Web: 1.3.0

Prior to these releases, Braze supported “original in-app messages.” Previously, support for original in-app messages was provided for any customer who ran an in-app campaign prior to the new release. All of the campaign stats were unaffected by the change, and those who had sent original in-app messages had the opportunity to send others via the Create Campaign button on the Campaign page.

### Feedback widget

Support withdrawn: July 1, 2019.

The Braze SDK provided a feedback widget that could be added to your app to allow users to leave feedback using the submitfeedback method and pass it into either Desk.com or Zendesk and was managed on the dashboard.

### Google Cloud Messaging (GCM)

Support withdrawn: Braze removal of support: July 2018, Google removal of support: May 29, 2019

Replaced by: Firebase Cloud Messaging (FCM)

Google has removed support for GCM as of May 29, 2019. Braze has discontinued support for GCM from the Android SDKs in July 2018, which was noted within our Android SDK changelogs. This means that existing GCM tokens will continue to work, and you will be able to message your existing users. However, you will not be able to message new users.

Customers that have not already migrated to Firebase Cloud Messaging (FCM) may be affected by this change.

If you have not transitioned to FCM, all GCM push tokens registrations will fail. If your apps are currently supporting GCM, you’ll need to work with your development teams on transitioning from GCM to Firebase Cloud Messaging (FCM).

### Eclipse

Support withdrawn: 2014-2015

Replaced by: Android Studio

Braze has discontinued support for the Eclipse IDE due to Google sunsetting support for the Eclipse Android Developer Tools (ADT) plugin.

If you need assistance with your Eclipse integration prior to migration, contact Support for assistance.

### The Raw Event Stream (RES)

Support withdrawn: July 2018

Replaced by: Currents

The Raw Event Stream was the predecessor to Currents and was deprecated to make room for the future of Braze data.

### Delay while idle - GCM feature

Support withdrawn: November 2016

The Delay While Idle parameter was previously a part of the GCM push options. Google withdrew support for this option on November 15, 2016. Previously, when set to true, it indicated that the message should not be sent until the device becomes active.

### Custom endpoints

Support withdrawn: December 2019

Removal of Custom Endpoints. If you have a custom endpoint, you can continue to use it, but Braze no longer gives them out.

- 

New Stuff!
