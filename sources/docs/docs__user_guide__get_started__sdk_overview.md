---
url: https://www.braze.com/docs/user_guide/get_started/sdk_overview
slug: docs__user_guide__get_started__sdk_overview
title: "SDK overview"
description: "This reference article covers the basics of the Braze SDK."
section: user_guide/get_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# SDK overview

The Braze SDK collects session data, identifies users, and records purchases and custom events through your website or app. You can also use the SDK to engage users by sending in-app messages and push notifications directly from the Braze dashboard.

In brief, the Braze SDK:

- Collects and syncs user data into a consolidated user profile
 
- Captures marketing engagement data and custom data specific to your business
 
- Powers push notifications, in-app messages, and Content Card messaging channels

## What is an SDK?

A software development kit (SDK) is a set of pre-made tools—just small blocks of code—that can be added to digital applications to support new capabilities. The Braze SDK is used to send and get information to and from your app or site. It’s designed to provide essential functionality right from the start: creating user profiles, logging custom events, triggering push notifications, etc.

Because this functionality comes default from Braze, your developers are freed up to focus on your core business. Without an SDK, every Braze client would have to create all the infrastructure and tools for data processing, segmentation logic, delivery options, anonymous user handling, campaign analytics, and a lot more completely from scratch. That would take a lot longer and be way more of a pain than the hour or so it takes to incorporate our SDK.

## Implementation

To incorporate an SDK into your app or site, someone will need to add the SDK’s code to the larger overall code base powering that application. This means your Engineering team will be involved, essentially tying our apps together so that information and actions flow between them. But although your developers are involved, the SDK is designed to be lightweight and user-friendly to integrate.

For the sake of saving you time and ensuring a smooth integration, we recommend you and your Engineering team set up your custom events, custom attributes, and the SDK at the same time. Learn more about the steps that your Marketing and Engineering teams will need to think through together by reading our implementation article.

## Data aggregation

The Braze SDK automatically captures user-level data, giving you key metrics for your app and user base. Group similar apps into a single workspace (for example, iOS and Android versions together) to view collected data across platforms and build a complete picture of user activity. See the article on the Home page for more information.

## In-app messaging

Use the SDK to compose and send in-app messages directly. You can choose slideup, modal, or fullscreen messages based on your campaign strategy. For composition details, refer to Create an in-app message.

## Push notifications

Push notifications are another great option to engage with your users and are especially useful to handle time-sensitive calls to action. Mobile push notifications appear on your users’ devices, and web push notifications appear even when your site is not open. For specifics on using push notifications, see our push notification article.

Users of your website or app need to opt-in to receive push notifications. See push priming for more details.

## Segmentation and delivery rules

By default, a campaign containing in-app messages will be sent to all versions of the app in that workspace. For example, the message will send to both web and mobile users. To send an in-app message exclusively to web or mobile, you will need to segment your campaign accordingly, which is supported by default through the Braze SDK.

You can create a segment of your web users by setting Apps and websites targeted to Users from specific apps, then select only your website for the Specific Apps.

This will allow you to target users based on their behavior in an intelligent way. If you wanted to target web users to encourage them to download your mobile app, you’d create this segment as your target audience. If you wanted to send a messaging campaign that included a mobile in-app message but not a web message, you would uncheck your website’s icon in your segment.

## Supported platforms

Braze provides SDKs for multiple platforms, like Web, Android, and Swift. For the complete list, see the Braze Developer Guide.

- 

New Stuff!
