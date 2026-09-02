---
url: https://www.braze.com/docs/user_guide/channels/push/platform_specific_resources/ios/rich_notifications
slug: docs__user_guide__channels__push__platform_specific_resources__ios__rich_notifications
title: "Create rich push notifications for iOS"
description: "This tutorial covers the requirements and steps on how to create iOS Rich Notifications for your Braze campaigns."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create rich push notifications for iOS

Rich Notifications allow for more customization in your push notifications by adding additional content beyond copy. Android notifications have included images in push notifications for some time now, messaged as an ‘Expanded Notification Image’. Starting with iOS 10, your customers will be able to receive iOS push notifications that include GIFs, images, videos, or audio.

## Prerequisites

Before you create a rich push notification for iOS, note the following details:

- To ensure your app can send rich notifications, follow the iOS push integration instructions, as your developer will need to add a service extension to your app.
 
- File types that we currently support for direct uploading within our dashboard include JPEG, PNG, or GIF. These files can also be entered into the templatable URL field along with these additional file types: AIF, M4A, MP3, MP4, or WAV.
 
- Reference Apple’s documentation for media limitations and specs.
 
- iOS will scale images to fit in the screen and will scale rich images for the active or locked view.

note

As of January 2020, iOS rich push notifications can handle images 1038x1038 that are under 10 MB, but we recommend using as small a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.

important

Push notification images may not show as expected if the file size for the image is too big, the aspect ratio is incorrect, the text exceeds the maximum message length, or the title text exceeds the maximum title length.

### Character count

While we can’t provide a hard and fast rule for the precise number of characters to include in a push, we provide some guidelines to consider while designing iOS messages. There may be some variance depending on the presence of an image, the notification state and display setting of the user’s device, and the size of the device. When in doubt, keep it short and sweet.

As a best practice, Braze recommends keeping each line of text for both the optional title and message body to approximately 30-40 characters in a mobile push notification.

#### Notification states

Your users may view push notifications in a variety of different situations, and could see different lengths of text as follows.

 Notification states

 Lock screen or Notification Center | 
 Expanded | 
 Device active | 

 This is the most common scenario.

Title: 1 line of text
Body: 4 lines of text
Image: square thumbnail | 
 When a user long-presses a message.

Title: 1 line of text
Body: 7 lines of text
Image: 2:1 aspect ratio (recommended, see following note) | 
 When a user receives a push while their phone is unlocked and active.

Title: 1 line of text
Body: 2 lines of text | 

note

While we recommend a 2:1 aspect ratio for expanded push notifications, nearly any aspect ratio is supported. Images will always span the full width of the notification, and the height will adjust accordingly.

#### Variables in text truncation

When creating content, consider the following scenarios that may impact how much text is displayed.

- timing
 
- images
 
- interruption level
 
- more

Depending on when a user engages with a push notification, the timestamp can shorten the title text.

Title character count: 35

Title character count: 33

Title character count: 22

Body text is shortened by about 10 characters per line when an image is present.

Body character count: 179

Body character count: 154

For iOS 15, Time Sensitive and Critical denotations push the title down to a new line without the timestamp, giving it a little more space.

Title character count: 35

Title character count: 39

The following details can also impact text truncation:

- Phone display settings: a user can increase or decrease the global UI font size on their phone, typically for accessibility reasons.
 
- Device width: the message could be displayed on a small phone, or a wide iPad.
 
- Content types: emojis and wide characters like “m” and “w” take up more space than “i” or “t”, and longer words like “engagement” may line-wrap more abruptly than shorter words.

## Setting up your iOS rich notification

### Step 1: Create a push campaign

Follow the campaign steps to compose a push notification for iOS. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

### Step 2: Add media

Add your image, GIF, audio, or video file in the iOS Notification Image field in the composer of the message. Refer to the requirements on how to add your content files.

You can also limit this message to only send to users who have a device that runs on iOS 10. For users who have not upgraded to iOS 10, it will appear as text-only notifications without the rich content if you leave the Only send to devices with Rich Notification support unchecked.

### Step 3: Continue creating your campaign

Once your rich notification content is uploaded to the dashboard, you can continue scheduling your campaign.

When a user receives the push notification, they can hard press on the push message to expand the image.

- 

New Stuff!
