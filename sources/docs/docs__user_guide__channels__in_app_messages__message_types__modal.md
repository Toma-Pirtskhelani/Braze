---
url: https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/modal
slug: docs__user_guide__channels__in_app_messages__message_types__modal
title: "Modal in-app messages"
description: "This reference article covers the message and design requirements of modal in-app messages."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Modal in-app messages

Modals appear in the center of the device’s screen with a screen overlay that helps it stand out from your app in the background. These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

This message type is available in both the drag-and-drop and traditional editor.

## Image specifications

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

## Larger screens

On a tablet or desktop browser, a modal in-app message will still sit in the center of the app screen as shown in the following screenshot.

- 

New Stuff!
