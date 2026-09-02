---
url: https://www.braze.com/docs/developer_guide/getting_started/platform_overview
slug: docs__developer_guide__getting_started__platform_overview
title: "Getting started: Platform overview"
description: "This article covers the basic parts and capabilities of the Braze platform. Links from this article connect to essential Braze topics."
section: developer_guide/getting_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# Getting started: Platform overview

This article covers the basic parts and capabilities of the Braze platform. Links from this article connect to essential Braze topics.

tip

Check out our free Developer Learning Path course along with these articles.

## What is Braze?

Braze is a customer engagement platform. It ingests user data, surfaces user actions and behaviors, and lets you act on them. The platform has three primary components: the SDK, the dashboard, and the REST API.

If you’re a marketer looking for a more general overview of Braze, check out the Getting Started section for marketers, instead.

### SDK

The Braze SDKs can be integrated into your mobile and web applications to provide powerful marketing, user management, and analytics tools.

In brief, when fully integrated, the SDK:

- Collects and syncs user data into a consolidated user profile
 
- Automatically collects session data, device info, and push tokens
 
- Captures marketing engagement data and custom data specific to your business
 
- Is architected for security and penetration tested by third parties
 
- Is optimized for low-battery or slow-network devices
 
- Supports server-side JWT signatures for added security
 
- Has write-only access to your systems (can’t retrieve user data)
 
- Powers push notifications, in-app messages, and Content Card messaging channels

### Dashboard user interface

The dashboard is the UI that controls all of the data and interactions at the heart of the Braze platform. Marketers will use the dashboard to do their job and create content. Developers use the dashboard to manage settings for integrating apps, such as API keys and push notification credentials.

If you’re just getting started, your team administrator should add you (and all other team members who need access to Braze) as users on your dashboard.

### REST API

The Braze API allows you move data in and out of Braze at scale. Use the API to bring in updates from your backend, data warehouses, and other first and third-party sources. Additionally, use the API to add custom events for segmentation purposes directly from a web-based applications. You can trigger and send messages through the API, allowing technical resources to include complex JSON metadata as part of your campaigns.

The API also provides a web service where you can record actions taken by your users directly via HTTP, rather than through the mobile and web SDKs. Combined with webhooks, this means you can track actions and trigger activities for users inside and outside your app experience. The API guide lists available Braze API endpoints and their uses.

For more on the parts and pieces of Braze, check out: Getting Started: Architecture overview.

## Data analysis and action

Data stored in Braze is retained and usable for segmentation, personalization, and targeting as long as you’re a Braze customer. That allows you to act on user profile data (for example, session activity or purchases) until you choose to deprecate that information. For instance, a streaming service could track each subscriber’s viewed content from their first day on the service (even if that was many years ago) and use that data to power relevant messaging.

### App analytics

The Braze dashboard displays graphs updated in real time based on analytics metrics and custom events that you instrument. Consistent measurement and optimization using A/B testing, custom reporting, analytics, and automated intelligence helps to support your customer engagement and differentiation.

### User segmentation

Segmentation allows you to create groups of users based on powerful filters of their in-app behavior, demographic data, and similar. Braze also allows you to define any in-app user action as a “custom event” if the desired action is not captured by default. The same is true of user characteristics via “custom attributes.” After a user segment is created on the dashboard, your users will move in and out of the segment as they meet (or fail to meet) the defined criteria. For example, you can create a segment that includes all users who have spent money in-app and last used the app more than two weeks ago.

For more on our data models, check out: Getting Started: Analytics overview.

## Multichannel messaging

After you have defined a segment, Braze messaging tools allow you to engage with your users in a dynamic, personalized way. Braze was designed with a channel-agnostic, user-centric data model. Messaging is done inside your app or site (such as sending in-app messages or through graphic elements like Content Card carousels and banners) or outside your app experience (such as sending push notifications or emails). For example, your marketers can send a push notification and an email to the example segment defined in the previous section.

 Channel | 
 Description | 

 Content Cards* | 
 Send highly-targeted and dynamic in-app notifications without interrupting the customer. | 

 Email | 
 Send rich HTML messages by building your email using the rich-text editor, our drag-and-drop editor, or by uploading one of your existing HTML templates. | 

 In-app messages | 
 Send unobtrusive in-app notifications using the Braze custom-built native user interface. | 

 Push | 
 Automatically trigger push notifications from messaging campaigns or news items using the Apple Push Notification Service (APNs) for iOS or Firebase Cloud Messaging (FCM) for Android. | 

 SMS, MMS, and RCS* | 
 Use SMS, MMS, or RCS to send transactional notifications, share promotions, send reminders, and more. | 

 Web push | 
 Send web browser notifications, even if your users aren’t currently active on your site. | 

 Webhooks | 
 Use webhooks to trigger non-app actions, providing other systems and applications with real-time data. | 

 WhatsApp* | 
 Directly connect with your users and customers by leveraging the popular peer-to-peer messaging platform: WhatsApp. | 

*Available as an add-on feature.

### Customizable components

 All Braze components are crafted to be accessible, adaptive, and customizable. You can start with Braze by using the default BrazeUI components and customizing them to suit your brand needs and use case.

 To go beyond the default options, you can write custom code to update a message channel’s look and feel to more closely match your brand. This includes changing a component’s font type, font size, and colors. Marketers maintain control of the audience, content, on-click behavior, and expiration directly in the Braze dashboard.

 You can also create completely custom components to control what your messaging looks like, how it behaves, and how they interact with other messaging channels (for example, triggering a Content Card based on a push notification). Braze provides SDK methods to allow you to log metrics like impressions, clicks, and dismissals in the Braze dashboard. Each messaging channel has an analytics article to help facilitate this.

## Integrating Braze

Braze is designed for rapid integration. The average time-to-value is six weeks across our customer base. For more on the integration process, see Getting Started: Integration overview.

## Resources to bookmark

As a technical resource, you’ll be involved in a lot of the nuts and bolts of Braze. Here are good resources to bookmark outside of our documentation. As you’re going forward, keep our Terms to Know glossary handy in case you have questions on Braze terms.

 Resource | 
 What You’ll Learn | 

 Debugging the SDK | 
 When troubleshooting your integration, the SDK debugging tool will be a helpful tool. Make sure you have it on hand! | 

 Braze Public GitHub | 
 You’ll find detailed integration information and sample code in our GitHub repository. | 

 Android SDK GitHub Repository | 
 The Android SDK GitHub repository. | 

 Android SDK Reference | 
 Class documentation for the Android SDK. | 

 iOS (Swift) SDK GitHub Repository | 
 The Swift SDK GitHub repository. | 

 iOS (Swift) SDK Reference | 
 Class documentation for the iOS SDK. | 

 Web SDK GitHub Repository | 
 The Web SDK GitHub repository. | 

 Web SDK Reference | 
 Class documentation for the iOS SDK. | 

 SDK Changelogs | 
 Braze has predictable monthly releases, in addition to releases for any critical issues and major OS updates. | 

 Braze API Postman Collection | 
 Download our Postman collection here. | 

 Braze System Status Monitor | 
 Our status page is updated whenever there are incidents or outages. Go to this page to subscribe to alerts. | 

- 

New Stuff!
