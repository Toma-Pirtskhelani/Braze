---
url: https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/instant_chat/sendbird
slug: docs__partners__additional_channels_and_extensions__additional_channels__instant_chat__sendbird
title: "Sendbird"
description: "This reference article outlines the partnership between Braze and Sendbird, a leading in-app messaging solution that allows users to receive in-app notifications on the Sendbird..."
section: partners/additional_channels_and_extensions
fetched: 2026-09-02
evidence: company-own (technical)
---
# Sendbird

Sendbird Notifications offers marketers and product managers a powerful new channel to communicate with their customers in-app with persistent, interactive one-way messages. These messages can be used for any communication and are most commonly used for promotional and transactional purposes.

This integration is maintained by Sendbird.

## About the integration

The Braze and Sendbird integration allows company users to:

- Use Braze segmentation and triggering capabilities to initiate personalized in-app notifications.
 
- Create tailored in-app notifications on the Sendbird Notifications platform, which are then delivered within the app environment, enhancing user engagement.

By harnessing the joint capabilities of Braze and Sendbird Notifications, businesses can elevate customer engagement and drive higher conversion rates through effective in-app notification strategies.

## Prerequisites

 Requirement | 
 Description | 

 Sendbird account | 
 A Sendbird account is required to take advantage of this partnership. | 

 Sendbird UIKit | 
 You must have the Sendbird UIKit installed in your iOS or Android app. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

## Use cases

The Braze and Sendbird Notifications integration offers a range of use cases to boost customer engagement and deliver an exceptional user experience:

- Marketing: Enhance targeted campaigns with personalized promotions and recommendations tailored to users’ preferences, such as exclusive discounts based on browsing history or past purchases.
 
- Transactional: Elevate customer communication through real-time updates on orders, deliveries, billing, and payments, including notifications regarding order status, shipping details, and estimated delivery times.

## Integration

### Step 1: Create a notification template

Sendbird templates allow you to send personalized in-app notifications by building and using multiple templates for each channel. Templates can be created and customized on Sendbird Dashboard without writing code.

### Step 2: Set up the Braze integration on Sendbird dashboard

From Sendbird Dashboard, select your application, navigate to Notifications > Integrations, and click Add under the Braze section. Here, you will need your Braze REST API key and Braze REST endpoint.

Once you have provided all fields, click Save to complete the integration and access the integration endpoints and API token.

### Step 3: Install Sendbird Notification Builder

Next, you must install Sendbird Notification Builder. This Google Chrome extension lets you send customized notifications through Sendbird on the Braze Dashboard.

#### Add Sendbird credentials to the extension

Once the extension is installed, click the Sendbird icon in your browser’s toolbar and select Settings. Here, provide your app ID and API token found in the Sendbird Notification Builder.

### Step 4: Map Sendbird user ID to Braze user ID

A Sendbird user ID must be added to a Braze user profile as a custom attribute for the integration to be used. You can upload and update user profiles via CSV files from the User import page. Alternatively, you can use the Braze user ID as the Sendbird user ID.

### Step 5: Set up your webhook template

In Braze, from Templates & Media, go to Webhook Templates and choose the Sendbird Webhook Template. Note that this template will only be available if you have installed the Sendbird Notification Builder extension.

- Provide a template name and add teams and tags as necessary.
 
- Copy a real-time or batch endpoint from the Sendbird dashboard into the Webhook URL.
 
- In the Receiver field, click the icon and insert the user attribute mapped to the Sendbird user ID.

- {{ '{{' }}custom_attribute.${sendbird_id}}} if you are using a custom attribute sendbird_id as the Sendbird user ID.
 
- {{ '{{' }}${user_id}}} if you are using Braze user ID as the Sendbird user ID.

- In the Settings tab, replace SENDBIRD_API_TOKEN with the notifications API token from the Sendbird dashboard.
 
- Save the template.

## Using this integration

### Campaigns

- In the Braze dashboard, on the Campaigns page, click Create Campaign > Webhook.
 
- Select the webhook template you created in this section. It’s highly recommended you use the Batch endpoint for campaigns.
 
- Customize the template by editing its variables in the Compose tab.

### Canvas

- From a new or existing Canvas, add a Message component.
 
- Open the component and select Webhook from the Messaging Channels.
 
- Select the webhook template you created in this section. It’s highly recommended you use the Real-time endpoint for Canvases.
 
- Customize the template by editing its variables in the Compose tab.

## Customization

### Track delivery and open status

To integrate the notifications’ delivery and open status event with a campaign’s conversion metric, add a custom event on the Braze dashboard.

- From the Braze dashboard, go to Settings > Manage Settings > Custom Events, and click + Add Custom Event.
 
- After you’ve created a custom event, click Manage Properties, add a property named “status”, and choose “String” as the property type.
 
- When you compose a notification in campaigns or Canvases, enter the name of the custom event into the Event Name field.

This custom event will be triggered twice for each notification, when a message is sent and when a user opens the message.

- When a message is sent, a custom event is triggered with SENT status.
 
- When a message is read, a custom event is triggered with READ status.

- 

New Stuff!
