---
url: https://www.braze.com/docs/user_guide/messaging/templates/in_app_message_templates/seasonal_promo
slug: docs__user_guide__messaging__templates__in_app_message_templates__seasonal_promo
title: "Seasonal promotion with background image"
description: "This page covers how to use the in-app message drag-and-drop editor to promote a seasonal offer or deal to drive user engagement."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Seasonal promotion with background image

Use the in-app message drag-and-drop editor to promote a seasonal offer or deal to drive user engagement.

## Prerequisites

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. For more information, see Creating an in-app message with drag-and-drop: Prerequisites.

   Swift: 5.0.0+     Web: 2.5.0+     Android: 8.0.0+  

### SDK versions for text links

To include text links that do not dismiss the message, the following minimum SDK versions are required:

   Swift: 6.2.0+     Android: 26.0.0+  

warning

If you include a link in your in-app message that redirects to a URL and the user isn’t on the minimum SDK versions specified, clicking on the link will close the message, and the user won’t be able to return to the message to submit the form.

## Creating a seasonal promotion with a background image

### Step 1: Choose your template

When creating a drag-and-drop in-app message, select Seasonal promotion with background image for your template, then select Build message. This template supports both mobile apps and web browsers.

### Step 2: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

### Step 3: Customize your button component

To get started building your seasonal promotion, select the button component in the editor. Then, use the side menu to select where users are taken when they select the button. The template default is to close the message, but you can choose to navigate to a specific page in your app (such as the product you’re promoting).

You can also add additional messages to your seasonal promotion in the Pages section, and then link them together for a sequential flow. For example, you can put together a sequence of messages that briefly describe the product’s capabilities and end with a button that takes users to the product page. Learn how to do that in Connect pages together.

### Step 4: Style your message

Customize the look and feel of your seasonal promotion using the drag-and-drop in-app message components. Add your own background image by replacing the default background image URL in the Message container menu or remove the URL and select your image from the Media Library.

## Analyzing the results

After your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, you can create a segment of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

- 

New Stuff!
