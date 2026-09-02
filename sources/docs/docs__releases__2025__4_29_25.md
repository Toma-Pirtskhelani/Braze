---
url: https://www.braze.com/docs/releases/2025/4_29_25
slug: docs__releases__2025__4_29_25
title: "April 29, 2025 release"
description: "This article contains release notes for April 1, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# April 29, 2025 release

## Troubleshooting Braze access

Troubleshooting Braze Access helps you navigate issues you may have when trying to access Braze, such as getting locked out of your account or working with a Braze dashboard that won’t perform as expected.

## Data flexibility

### Currents frequently asked questions

You can find answers to some frequently asked questions about Currents on the new Frequently asked questions page.

### Anonymous users

The “How it works” and “Assigning user aliases” sections in Anonymous users have new details about how anonymous users work and why you might want to assign them user aliases.

### Campaign drafts

Saving drafts can help you make large-scale changes to active campaigns. By creating a draft, you’re able to pilot planned changes before your next launch.

### Identifying and merging users

When identifying or merging users, you can now use the least_recently_updated parameter in the prioritization array to prioritize the least recently updated user.

### Scheduled user merging

Scheduled merging allows you to automate the merging of user profiles on a daily basis using preconfigured rules. Braze will notify the admins of your workspace 24 hours before the scheduled merge occurs, providing a reminder and time to review the configuration.

### Recipient object

You can now include braze_id in the recipient object, which allows you to request or write information in our endpoints.

### New data centers

Braze has launched two new data centers: US-10 and ID-01. You can sign up for region-specific data centers when setting up your Braze account.

## Unlocking creativity

### Landing page templates

Use landing page templates to create templates for your next campaigns. These templates can be accessed and managed in both the landing page editor and the Templates section of the dashboard.

### Landing page form field

When customizing your landing page, you can choose whether a form field is required or optional. Required fields must be filled out before the form can be submitted. Optional fields can be left blank or unselected by a user.

### Canvas pre-built templates

Braze Canvas offers several pre-built templates tailored specifically for eCommerce marketers, making it easier to implement essential strategies. This page offers some key templates you can use to enhance your customer journeys.

## Robust channels

### WhatsApp videos

 Early access

WhatsApp video files can now be hosted through either a URL or in the Braze media library.

### WhatsApp list messages

List messages appear as a body message with a list of clickable options. Each list can have multiple sections, and each list can have up to 10 rows.

### Copy preview link

Use Copy preview link in your HTML and drag-and-drop email messages, email templates, and Content Blocks to generate a shareable link that shows how your content will look like for a random user.

### Push registration diagram

We revamped our push notification documentation in the User Guide and added a new diagram to help visualize what push registration looks like on a larger scale.

## New Braze partnerships

### Updated partner categories

We updated the Technology Partners section with new categories and subcategories to improve your navigation experience.

### Shopify (new version) - eCommerce

A new version of the Shopify integration will be released in phases starting April, based on the type of Shopify store and the external ID used to set up the initial integration.

The older version of the integration will be deprecated on August 28, 2025. You must update to the newer version of the integration before August 28, 2025.

New Braze customers: Starting April 2025, Braze will be gradually rolling out the new Shopify connector for new onboardings and upgrading existing customers. To learn more about the new standard integration, refer to Shopify standard integration.

### Just Words - Dynamic Content

Just Words hyper-personalizes messaging at scale on lifecycle marketing channels, empowering you to dynamically test hundreds of variations and auto-refresh underperforming content.

### Tapcart - eCommerce

Tapcart is a leading mobile commerce platform for Shopify-powered brands, enabling merchants to create custom mobile apps that deliver personalized, engaging shopping experiences their customers love.

## SDKs

### Braze SDK version management

You can now learn about version management for the Braze SDK, so your app can stay up-to-date with the latest features and quality improvements.

### SDK docs audit

We’re currently auditing all our SDK content for developers to ensure all of our code samples are helpful and accurate. So far, we’ve made a variety of updates to our Android and Swift docs, and more are on the way.

## SDK updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Braze Unity SDK 8.0.0

- Updated the native iOS bridge from Braze Swift SDK 10.3.0 to 11.9.0.
 
- Updated the native Android bridge from Braze Android SDK 32.1.0 to 35.0.0.

- The minimum required Android SDK version is 25. See minimum Android SDK version details.

- Braze Segment Kotlin 3.0.0

- Updated Braze Android SDK from 32.1.0 to 35.0.0.

- The minimum required Android SDK version is 25. See minimum Android SDK version details.

- Braze Swift SDK 12.0.0

- The distributed static XCFrameworks now include their resources directly instead of relying on external resources bundles.

- When manually integrating the static XCFrameworks, you must select the Embed & Sign option for each XCFramework in the Frameworks, Libraries, and Embedded Content section of your target’s General settings.
 
- No changes are required for Swift Package Manager or CocoaPods integrations.

- Braze Segment Swift 6.0.0

- Updates the Braze Swift SDK bindings to require releases from the 12.0.0+ SemVer denomination.

- This allows compatibility with any version of the Braze SDK from 12.0.0 up to, but not including, 13.0.0.
 
- Refer to the changelog entry for 12.0.0 for more information on potential breaking changes.

- 

New Stuff!
