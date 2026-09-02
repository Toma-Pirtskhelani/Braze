---
url: https://www.braze.com/docs/user_guide/channels/push/create_a_push_message/push_stories
slug: docs__user_guide__channels__push__create_a_push_message__push_stories
title: "Push Stories"
description: "This reference article covers what Push Stories are, how to create one, as well as some frequently asked questions."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Push Stories

Push Stories take the photo carousel functionality popularized in Instagram and Facebook and allow marketers to create a carousel of pages within a push that tells a rich, cohesive story. These pages consist of an image, click action, title, and description. Your users can swipe through these pages and view the story—as told by you.

 Android Example (Expanded) | 
 IOS Example (Expanded) | 

 | 
 | 

note

On iOS SDK versions 3.13.0+, due to a change in how the SDK downloads images, a thumbnail of the first image will not show on the condensed view of the push. Ensure that your message copy prompts users to expand the push to see the images.

## Prerequisites

The following SDK versions are required to receive Push Stories:

   Swift: 5.0.0+     Android: 2.2.0+  

## How to use Push Stories

To use Push Stories, do the following:

- Create a push campaign.
 
- For your Notification Type, select Push Stories.
 
- Select iOS or Android. Note that if you select both for a push message, the option to create a Push Story won’t appear.

### Push Story composer

To create a page, perform the following steps:

- Select Add new page from the main composer.
 
- Insert an image for each page, along with the click behavior for that image.
 
- If desired, add a Title and Description for each page. If you use a title and description for one page, they must be inserted for all pages.

The previews will be reflected and are interactive.

important

If you are pulling in images with Connected Content, ensure that your image URL begins with https://. Using http:// will crash your app.

### Image and text specifications

The following image and text specifications apply to the photo carousel portion of Push Stories. For information on the basic push that users interact with to activate the Push Story, refer to Push message and image formats.

- images
 
- text

- Image ratio: 2:1 (required)
 
- Recommended image size: 500 KB
 
- Maximum image size: 5 MB
 
- File types: PNG, JPEG

- Title: 30 characters (recommended)
 
- Description: 30 characters (recommended)

note

While there may be some variance in character length from device to device, the title and description for Push Stories are limited to one line each. The remainder of your message will be truncated. Always test your message on a real device.

### Push Story segmentation

When you create a campaign or Canvas, you can filter which users you want to target based on whether they have clicked on a Push Story page. Then, select the campaign and the page you want to use to target your users.

### Push Stories analytics

The analytics will look very similar to the current analytics section for push notifications. For Push Stories analytics, you can open the Direct Opens metric to view the clicks per page.

## Troubleshooting

### iOS

#### I sent myself a Push Story but didn’t receive the notification

Apple has specific rules in place that will prevent certain types of notifications from being sent to a device based on a number of different factors. This includes evaluating the customers’ data plan, notification size, and the customers’ storage capacity. As a result, sometimes no notification will be sent to your customers.

These are limitations imposed by Apple that should be considered when designing your Push Story.

#### I sent myself a Push Story but saw the condensed view instead

In certain situations where all the pages do not load, for example, due to a loss of data connection, the Push Story will only show the condensed notification.

### Android

#### Push Story doesn’t dismiss after clicking the image

By default, Push Stories are not dismissed on Android after a user clicks on the image. If you’d like to dismiss the notification, call cancelNotification.

- 

New Stuff!
