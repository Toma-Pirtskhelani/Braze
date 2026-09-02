---
url: https://www.braze.com/docs/user_guide/channels/push/create_a_push_message/message_and_image_formats
slug: docs__user_guide__channels__push__create_a_push_message__message_and_image_formats
title: "Push message and image formats"
description: "This article describes message and image formats for push notifications."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Push message and image formats

This reference article describes message and image formats for push notifications.

For best results, refer to the following image size and message length guidelines when crafting your push messages. There may be some variance depending on the presence of an image, the notification state (iOS) and display setting of the user’s device, as well as the size of the device. When in doubt, keep your copy short and sweet.

## iOS and Android push

- images
 
- text
 
- payload size
 
- image example
 
- text example

 Image Type | 
 Recommended Image Size | 
 Max Image Size | 
 File Types | 

 (iOS) 2:1 Recommended | 
 500 KB | 
 5 MB | 
 PNG, JPEG, GIF | 

 (Android) Push icon | 
 500 KB | 
 5 MB | 
 PNG, JPEG | 

 (Android) Expanded notification | 
 500 KB | 
 5 MB | 
 PNG, JPEG | 

note

GIFs are not supported in Android push notifications. This is an Android platform limitation, not a Braze limitation.

- For in-app messages and Content Cards on Android, you can support GIFs by integrating a third-party image library, such as Glide or Fresco. 

- On iOS, push notifications support GIFs. In-app messages and Content Cards require a custom GIF image provider.

 Message Type | 
 Recommended Message Length (Text only) | 
 Recommended Message Length (Rich) | 

 (iOS) Lock Screen | 
 160 characters | 
 130 characters | 

 (iOS) Notification Center | 
 160 characters | 
 130 characters | 

 (iOS) Banner Alert | 
 80 characters | 
 65 characters | 

 (Android) Lock Screen | 
 49 characters | 
 N/A | 

 (Android) Notification Drawer | 
 597 characters | 
 N/A | 

Wondering how many characters you can use in an iOS push notification without it being truncated? Check out our iOS character count guidelines.

 Platform | 
 Size | 

 pre iOS 8 | 
 0.256 KB | 

 post iOS 8 | 
 2 KB | 

 Android (FCM) | 
 4 KB | 

- ios
 
- android

note

Large image notifications display best when using an image of at least 600x300 pixels.

- ios
 
- android

## Web push

- images
 
- text

| Browser | Recommended Icon Size
| — | —

Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Icons are configurable on a per-campaign basis with Safari 16+ on macOS 13+)
Opera | 192x192 ≥

| Browser | Platform | Large Image Size
| — | — | —

Chrome | Android | 2:1 aspect ratio
Firefox | Android | N/A
Chrome | Windows | 2:1 aspect ratio
Edge | Windows | 2:1 aspect ratio
Firefox | Windows | N/A
Firefox | Windows | 2:1 aspect ratio
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A

| Browser | Platform | Maximum Title Length | Maximum Message Body Length
| — | — | — | —

Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42

- 

New Stuff!
