---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/judo
slug: docs__partners__message_personalization__dynamic_content__visual_and_interactive_content__judo
title: "Judo"
description: "This reference article outlines the partnership between Braze and Judo, a no-code server-driven UI platform that allows you to add location context and tracking to..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Judo

Judo is a server-driven UI platform that empowers publishers to efficiently deliver rich, engaging in-app user experiences without app updates.

This integration is maintained by Judo.

## About the integration

The Braze and Judo integration provides bespoke experiences in your campaigns and Canvases. Instead of a simple, templated landing page experience, a Braze campaign may incorporate content that comprises multiple screens, modals, video, custom fonts, and support settings such as dark mode and accessibility built without code and deployed without app updates. Data from Braze may also be used to support personalized content in a Judo Experience. User events and data from the experience can feedback into Braze for attribution and targeting.

## Prerequisites

 Requirement | 
 Description | 

 Judo Account | 
 A Judo account is required to take advantage of this partnership. | 

 Judo SDK | 
 The Judo SDK must be integrated into your iOS and/or Android apps. | 

## Use cases

Onboarding: App publishers using Judo build and deploy rich, native onboarding experiences. These experiences can now be one element in a personalized cross-channel onboarding journey coordinated via Braze. Experiences may be personalized and quickly updated without any app updates to test the effectiveness of different in-app flows.

Conversion: App publishers can use data from Braze to create a personalized rich in-app experience to drive in-app purchases, paid subscriptions, or contextual merchandising using integration hooks in Judo. Access to these experiences may be triggered via engagement marketing campaigns created in Braze.

Event-Driven Content: A primary use for Judo in sports and entertainment is building rich experiences to preview, promote, and recap events. This capability has broad applications in other verticals for seasonal and news-driven content. Linking messaging to promote or highlight events in a timely manner to rich in-app experiences empowers publishers to drive engagement by being contextually relevant.

## Side-by-side SDK integration

Judo offers additional libraries that automate some of the effort necessary to integrate the Judo and Braze SDKs side-by-side in your mobile apps.

### Step 1: Install the Judo-Braze integration library

Install and set up the Judo-Braze integration library into your apps. This will automatically enable event tracking.

- iOS installation
instructions
 
- Android installation
instructions.

### Step 2: Configure in-app messaging

This step will involve creating custom ABKInAppMessageControllerDelegate and IInAppMessageManagerListener implementations for iOS and Android.

See the in-app message setup documentation bundled for each of the integration libraries:

- iOS In-App Messaging
Setup
 
- Android In-App Messaging
Setup.

## Using this integration

Once you have finished the app-side integration, you can test it by running a test Braze in-app message campaign for a Judo Experience to verify that it runs as expected.

### Step 1: Create a custom code in-app message campaign

From the Braze platform, create a Braze in-app message campaign with a Custom Code message type. Next, select HTML Upload as the custom type. Make sure to populate the content of the message with the base in-app messaging fields; this content will not be shown to the user.

Next, use the following minimal HTML snippet to satisfy the form validation:

```

1

```
 | 
```
<a href="appboy://close">X</a>

```
 | 

Note that this will not be displayed in production on your device as Judo will rewrite and replace this with a Judo Experience.

### Step 2: Set a key-value pair for Judo

Set a custom key-value pair on the campaign with a key of judo-experience. Provide the URL of the Judo Experience you’d like to show here. The Judo-Braze integration library will then detect this key-value pair in the handler and use it to inject your Judo Experience in place of the standard Braze in-app message UI.

### Step 3: Finishing the campaign

Lastly, complete the campaign, setting up a trigger for the campaign and selecting users via Segments in the Delivery and Target User sections. Visit our in-app message article on the different components of a Braze in-app message.

- 

New Stuff!
