---
url: https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/fullscreen
slug: docs__user_guide__channels__in_app_messages__message_types__fullscreen
title: "Fullscreen in-app messages"
description: "This reference article covers the message and design requirements of fullscreen in-app messages."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Fullscreen in-app messages

Fullscreen messages take up the whole screen of the device! This message type is great when you really need your user’s attention, like for mandatory app updates.

This message type is available in both the drag-and-drop and traditional editor.

- portrait
 
- landscape

## Images

Fullscreen in-app messages will fill the entire height of a device and crop horizontally (left and right sides) as needed. Image and text fullscreen messages will fill 50% of the height of a device. All fullscreen in-app messages will fill the status bar on “notched” devices.

- All images must be less than 5 MB.
 
- We accept only PNG, JPEG, and GIF file types.
 
- We recommend that your images be 500 KB.

tip

Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. Download Design Templates ZIP

### Portrait

 layout | 
 asset size | 
 notes | 

 Image and text | 
 6:5 aspect ratio
 High-res 1200 x 1000 px
 Minimum 600 x 500 px | 
 Cropping can occur on all sides, but the image will always fill the top 50% of the viewport | 

 Image only | 
 3:5 aspect ratio
 High-res 1200 x 2000 px
 Minimum 600 x 1000 px | 
 Cropping can occur on the primary side and right edges on taller devices | 

### Landscape

 layout | 
 asset size | 
 notes | 

 Image and text | 
 10:3 aspect ratio
 High-res 2000 x 600px
 Minimum 1000 x 300 px | 
 Cropping can occur on all sides, but the image will always fill the top 50% of the viewport | 

 Image only | 
 5:3 aspect ratio
 High-res 2000 x 1200px
 Minimum 1000 x 600 px | 
 Cropping can occur on the primary side and right edges on taller devices | 

### Image safe zone

When previewing a fullscreen in-app message in the Braze platform, you can enable the Image Safe Zone to protect a message area from cropping when displayed across devices. The safe zone impacts only the image; the close button is always visible to users, even if it appears outside the safe zone in the preview.

In addition to testing the Image Safe Zone in the preview pane, we always recommend you test your message.

## Larger screens

On a tablet or desktop browser, a fullscreen in-app message will sit in the center of the app screen, as shown in the following screenshot.

- portrait
 
- landscape

- 

New Stuff!
