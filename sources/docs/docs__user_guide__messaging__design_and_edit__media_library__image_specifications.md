---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library/image_specifications
slug: docs__user_guide__messaging__design_and_edit__media_library__image_specifications
title: "Image specifications"
description: "This reference article describes the recommended image sizes and specifications for each channel type."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Image specifications

In general, smaller and high-quality images will load faster, so we recommend using the smallest asset possible to achieve your desired output. To maximize your image use in specific channels, refer to the details in this article.

You should always preview and test your messages on a variety of devices to confirm that the most important areas of your image and message appear as expected.

## Image behavior

 Layout | 
 Behavior | 

 Image and text | 
 Tall or narrow images will scale down and be horizontally centered. Wide images will be clipped on the horizontal edges. | 

 Image only | 
 The message will resize to fit images of most aspect ratios. | 

## Video

Videos uploaded to the media library can only be used in WhatsApp messages. For more information, refer to Creating a WhatsApp message.

## GIFs

GIFs are supported in iOS push, in-app messages, email, Content Cards, and MMS or RCS messages. GIFs with very elongated shapes (for example, 3000 x 2 pixels) or 300 or more frames may fail to upload, even if the total file size is small.

note

GIFs are not supported in Android push notifications. This is an Android platform limitation, not a Braze limitation.

- For in-app messages and Content Cards on Android, you can support GIFs by integrating a third-party image library, such as Glide or Fresco. 

- On iOS, push notifications support GIFs. In-app messages and Content Cards require a custom GIF image provider.

## Channel guidance

### Content Cards

 Card type | 
 Aspect ratio | 
 Image quality | 

 Classic | 
 1:1 aspect ratio | 
 60 x 60 px | 

 Captioned | 
 4:3 aspect ratio | 
 600 px minimum width | 

 Banner | 
 Any aspect ratio | 
 600 px minimum width | 

For more information, refer to Content Card creative details.

### Email

 Email type | 
 Recommended maximum properties | 

 Text only | 
 25 KB | 

 Text with images | 
 60 KB | 

 Email width | 
 600 px | 

 Image specifications | 
 Recommended maximum properties | 

 Size | 
 5 MB | 

 Width | 
 Header: 600 px
Body: 480 px | 

 File types | 
 PNG, JPEG, GIF

 WebP image support varies across email clients. For reliable rendering, convert WebP images to PNG or JPEG before adding them to email messages.

SVG images are not recommended for email messages due to compatibility issues with Gmail and other major email clients. Use PNG, JPEG, or GIF instead. | 

 Text specifications | 
 Recommended maximum properties | 

 Subject line length | 
 35 characters
6 to 10 words | 

 "From: Name" length | 
 25 characters | 

 Pre-header length | 
 85 characters | 

### In-app messages

Modal in-app messages are designed to fit the device at the best and most filling ratios possible, while staying true to the size and ratios of your chosen image or copy for your message.

While there are no limits to how many text characters you can include in an in-app message (as well as buttons, headline, main body, and others), we moderate how many text characters you use. Too much text will require users to expand and scroll the message.

All in-app messages have a recommended image size of 500 KB, maximum image size of 5 MB, and support PNG, JPEG, and GIF file types. WebP images aren’t supported across all devices or browsers; we suggest converting WebP images to PNG or JPEG before adding them to in-app messages.

note

SVG images are not supported for in-app messages because they do not render reliably across all platforms. Use PNG, JPEG, or GIF instead.

- portrait
 
- landscape
 
- slideup
 
- modal

 Type | 
 Aspect ratio | 
 Image quality | 
 Notes | 

 Portrait full screen with text | 
 6:5 | 
 High resolution 1200 x 1000 px 
Minimum resolution 600 x 500 px | 
 Cropping can occur on all sides, but the image will always fill the top 50% of the viewport. | 

 Portrait full screen (image only, with or without buttons) | 
 3:5 | 
 High resolution 1200 x 2000 px 
 Minimum resolution 600 x 1000 px | 
 Cropping can occur on the horizontal edges on taller devices. | 

 Type | 
 Aspect ratio | 
 Image quality | 
 Notes | 

 Landscape full screen with text | 
 10:3 | 
 High resolution 2000 x 600 px 
Minimum resolution 1000 x 300 px | 
 Cropping can occur on all sides, but the image will always fill the top 50% of the viewport. | 

 Landscape full screen (image only, with or without buttons) | 
 5:3 | 
 High resolution 2000 x 600 px 
 Minimum resolution 1000 x 600 px | 
 Cropping can occur on the horizontal edges on taller devices. | 

 Type | 
 Aspect ratio | 
 Image quality | 
 Notes | 

 Slideup | 
 1:1 | 
 High resolution 150 x 150 px 
 Minimum resolution 50 x 50 px | 
 Images of various aspect ratios will fit into a square image container, without cropping. | 

 Type | 
 Aspect ratio | 
 Image quality | 
 Notes | 

 Modal (image only) | 
 1:1 | 
 Maximum recommended resolution: 1200 x 2000 px 
 Minimum resolution: 600 x 600 px | 
 The message will resize to fit images of most aspect ratios. The recommended maximum resolution has a 3:5 aspect ratio, which may not provide optimal results. While larger images are usable, they may lead to longer load times. 
 The ideal aspect ratio for images is 1:1, and not meeting this ratio may trigger a warning during upload. This warning is a suggestion for best results and does not prevent the upload of larger images. | 

 Modal with text | 
 29:10 | 
 High resolution 1450 x 500 px 
 Minimum resolution 600 x 205 px | 
 Tall images will scale down and be horizontally centered. Wide images will be clipped on the horizontal edges. | 

tip

In-app message rendering on Web SDK may be affected by custom browser text-size settings. Users with custom text-size scaling may experience minor rendering issues, such as a 1px gap along the edge of a modal image. When previewing and testing in-app messages, we recommend using default browser text-size settings for the most accurate representation.

tip

Create assets with confidence! Our in-app message image templates and safe-zone overlays are designed to play nicely with devices of all sizes. Download Design Templates ZIP.

For more information, refer to In-app message creative details.

#### Font Awesome

Braze supports using Font Awesome v4.3.0 for modal in-app message icons.

### Push notifications

We recommend the following payload sizes:

 Messaging system | 
 Recommended payload | 

 iOS (pre-iOS 8) | 
 0.256 KB | 

 iOS (post-iOS 8) | 
 2 KB | 

 Android (FCM) | 
 4 KB | 

 Message type | 
 Maximum message length | 
 Maximum title length | 

 iOS lock screen | 
 175 characters | 
 43 characters | 

 iOS notification | 
 175 characters | 
 43 characters | 

 iOS banner alert | 
 85 characters | 
 43 characters | 

 Android lock screen | 
 49 characters | 
 43 characters | 

 Android notification drawer | 
 597 characters | 
 43 characters | 

The recommended image size for all push images is 500 KB.

 Image type | 
 Aspect ratio | 
 Maximum pixels | 
 Maximum image size | 
 File types | 
 Notes | 

 iOS | 
 2:1 (recommended) | 
 1038 x 1038 | 
 5 MB | 
 PNG, JPEG, GIF | 
 As of January 2020, iOS rich push notifications can handle images 1038 x 1038 px as long as they are under 10 MB, but we recommend using as small a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.

For more information, see iOS rich notifications. | 

 Android push icon | 
 1:1 | 
 N/A | 
 500 KB | 
 PNG, JPEG | 
 | 

 Android expanded notification image | 
 2:1 | 
 Small:
512 x 256

Medium:
1024 x 512

Large:
2048 x 1024 | 
 500 KB | 
 PNG, JPEG | 
 Used in Android rich notifications. | 

 Android incline image | 
 3:2 | 
 N/A | 
 N/A | 
 PNG, JPEG | 
 For more details, see Android inline image push. | 

#### Recommended message lengths

For best results, refer to the following message length guidelines when crafting push messages. There may be some variance depending on the presence of an image, the notification state (iOS) and display setting of the user’s device, as well as the size of the device.

 Message type | 
 Recommended length (text only) | 
 Recommended length (rich) | 

 iOS lock screen | 
 160 characters | 
 130 characters | 

 iOS Notification Center | 
 160 characters | 
 130 characters | 

 iOS banner alert | 
 80 characters | 
 65 characters | 

 Android lock screen | 
 49 characters | 
 N/A | 

 Android notification drawer | 
 597 characters | 
 N/A | 

For more information about iOS character counts, see iOS character count guidelines.

#### Web push

- images
 
- text

 Browser | 
 Recommended icon size | 

 Chrome | 
 192 x 192 px or larger | 

 Firefox | 
 192 x 192 px or larger | 

 Safari | 
 192 x 192 px or larger (configurable per campaign with Safari 16 on macOS 13+) | 

 Opera | 
 192 x 192 px or larger | 

 Browser | 
 Platform | 
 Large image size | 

 Chrome | 
 Android | 
 2:1 aspect ratio | 

 Firefox | 
 Android | 
 N/A | 

 Chrome | 
 Windows | 
 2:1 aspect ratio | 

 Edge | 
 Windows | 
 2:1 aspect ratio | 

 Firefox | 
 Windows | 
 N/A | 

 Opera | 
 Windows | 
 2:1 aspect ratio | 

 Chrome | 
 macOS | 
 N/A | 

 Safari | 
 macOS | 
 N/A | 

 Firefox | 
 macOS | 
 N/A | 

 Opera | 
 macOS | 
 N/A | 

 Browser | 
 Platform | 
 Maximum title length | 
 Maximum body length | 

 Chrome | 
 Android | 
 35 | 
 50 | 

 Firefox | 
 Android | 
 35 | 
 50 | 

 Chrome | 
 Windows | 
 50 | 
 120 | 

 Edge | 
 Windows | 
 50 | 
 120 | 

 Firefox | 
 Windows | 
 54 | 
 200 | 

 Opera | 
 Windows | 
 50 | 
 120 | 

 Chrome | 
 macOS | 
 35 | 
 50 | 

 Safari | 
 macOS | 
 38 | 
 84 | 

 Firefox | 
 macOS | 
 38 | 
 42 | 

 Opera | 
 macOS | 
 38 | 
 42 | 

#### Push notification examples

- ios
 
- android

note

Large image notifications display best when using an image of at least 600 x 300 pixels.

For additional resources, see Push image and text specifications.

### SMS and MMS

MMS messages support a single image per message. Only MMS-enabled subscription groups can send images.

 Property | 
 Recommendation | 

 Size | 
 600 KB or smaller for reliable carrier delivery. The composer blocks uploads larger than 1 MB. | 

 File types | 
 PNG, JPEG, GIF | 

For carrier file size limits and throughput, refer to MMS message limits and throughput.

For composing MMS messages, refer to Create an SMS, MMS, or RCS message.

- 

New Stuff!
