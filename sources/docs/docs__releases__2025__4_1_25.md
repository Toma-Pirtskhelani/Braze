---
url: https://www.braze.com/docs/releases/2025/4_1_25
slug: docs__releases__2025__4_1_25
title: "April 1, 2025 release"
description: "This article contains release notes for April 1, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# April 1, 2025 release

## Updates to Braze navigation

The updated navigation in Braze is designed to help you efficiently access features and content across devices. Note that the option to switch between navigation versions is no longer available. Learn more at our dedicated Navigating Braze article.

## Developer Guide detangle

Previously, many platform-level tasks were split across multiple pages, such as integrating the Swift SDK being split across six pages. Additionally, shared features were individually documented for each platform, meaning searching for a topic like “Setting Up Push Notifications” would return 10 different pages.

Before:

Now, platform-level tasks have been merged into single pages and shared SDK features now exist on the same page (with the help of our new SDK-tabbing feature). For example, now there’s only one page for Integrating the Braze SDK, where you can switch between platforms by selecting a tab at the top of the page. When you do, even the in-page table of contents will update to reflect the currently-selected tab.

After:

## Data flexibility

### Update to Canvas entry properties

Canvas entry properties are now part of Canvas context variables. Each context variable includes a name, data type, and a value that can include Liquid. For more information, refer to the Context component.

### Updates to segmentation filters for phone number filters

Segmentation filters have been updated to reflect changes to two phone number filters:

- Unformatted Phone Number (formerly Phone Number): Segments your users by their unformatted phone number.
 
- Phone Number (formerly Sending Phone Number): Segments your users by the E.164 formatted phone number field.

### Delete custom data

As you build targeted campaigns and segments, you may find that you no longer need a custom event or custom attribute. You can now delete this custom data and remove its references from your app.

### Import users with email addresses and phone numbers

You can now use an email address or phone number to import users and omit an external ID or user alias.

### Service Provider initiated login troubleshooting

Service Provider (SP) initiated login now has a troubleshooting section to help you work through issues with SAML and single-sign on issues.

### User import troubleshooting

The User Import troubleshooting section has new and updated entries, including how to troubleshoot missing rows in your imported CSV files.

### Frequently asked questions for Segment Extensions

Check out our frequently asked questions for Segment Extensions, including how you can create a Segment Extension that uses multiple custom events.

### Personalized and extended delays

 Early access

You can set up a personalized delay for your users and use this with a Context step to select the context variable to delay by.

You can also now extend Delay steps up to two years. For example, if you’re onboarding new users for your app, you can add an extended delay for two months before sending a Message step to nudge the users who haven’t started a session.

### Default user profile attributes for Snowflake

 Beta

There are now three default user profile attributes in Snowflake. Each view is designed for a specific use case with its own performance considerations. For example, you can be provided a periodic snapchat of a user profile’s default attributes.

## Robust channels

### Messaging fundamentals

Messaging Fundamentals is a new section in Engagement Tools that houses the shared concepts and terms for campaigns and Canvases, such as archiving and localizing messages.

### WhatsApp custom domains

You can now assign custom domains to one or multiple WhatsApp subscription groups.

### Triggered in-app messages for Canvas

You can now select a trigger for your in-app messages to be triggered on session start, or by custom events and purchases. After any delays pass and the audience options are checked, in-app messages are set to live when a user reaches the Message step. If a user starts a session and performs the trigger event for the in-app message, the user will see the in-app message.

### Limit entrance volume for Canvas

You can limit the number of people who would potentially enter this Canvas by a selected cadence (daily, lifetime of the Canvas, or every time the Canvas is scheduled). For example, you can set the entry controls to allow the Canvas to only send to 5,000 users per day.

### New use case: Booking reminder email system

Learn how you can use Braze features to build a booking reminder email messaging service. The service will allow users to book appointments and will message users with reminders of their upcoming appointments. Though this use case uses email messages, you can send messages in any, or multiple, channels based on a single update to a user profile.

### Click tracking for specific links

You can turn off click tracking for specific links by adding HTML code to your email message in the HTML editor or to components in the drag-and-drop editor.

### Dynamic Apple Push Notification Service gateway management

Dynamic APNs gateway management enhances the reliability and efficiency of iOS push notifications by automatically detecting the correct APNs environment. Previously, you would manually select APNs environments (development or production) for your push notifications, which sometimes led to incorrect gateway configurations, delivery failures, and BadDeviceToken errors.

### Flutter support for Banners

 Early access

Banners now support Flutter. Additionally, all Banner Card documentation has been overhauled for easier usability. Check out the following articles to get started:

- About Banners
 
- Creating Banner campaigns
 
- Embedding Banners into your app

### WhatsApp click tracking

 Early access

Click tracking lets you measure when someone taps a link in your WhatsApp message—giving you a clear view into what content is driving engagement. Braze shortens your URLs, adds tracking behind the scenes, and logs click events as they happen.

### Frequently asked questions for push

Check out our new Push FAQ article that addresses some of the most frequently asked questions that arise when setting up push campaigns.

### Push troubleshooting

Push troubleshooting provides a number of steps to help you navigate delivery challenges with push notifications. For example, if you’re experiencing delivery challenges with push notifications, we’ve compiled steps you can take to troubleshoot the issue.

## New Braze partnerships

### Movable Ink Da Vinci - Dynamic Content

The Braze and Movable Ink Da Vinci integration empowers brands to deliver highly personalized messaging by leveraging Da Vinci’s AI-driven content decisioning engine. Da Vinci curates the most relevant content for each user and seamlessly deploys messages through Braze.

## SDK updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Flutter SDK 13.0.0

- Updates the native Android bridge from Braze Android SDK 33.0.0 to 35.0.0.

- The minimum required Android SDK version is 25. See minimum Android SDK version details.

- Swift SDK v11.8.0-11.9.0
 
- Web SDK v5.8.0

- 

New Stuff!
