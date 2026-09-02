---
url: https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/slideup
slug: docs__user_guide__channels__in_app_messages__message_types__slideup
title: "Slideup in-app messages"
description: "This reference article covers the message and design requirements of slideup in-app messages."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Slideup in-app messages

Our slideups typically appear at the top or bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information. These are non-obtrusive and allow your users to continue to interact with your app while the message displays.

This message type is available in the traditional editor.

## Image and copy behavior

Slideup messages can contain up to three lines of copy before truncation with ellipses. Images in slideups will never be cropped or clipped—they will always scale down to fit within the 50 x 50 pixel image container.

- All images must be less than 5 MB.
 
- We accept only PNG, JPEG, and GIF file types.
 
- We recommend that your images be 500 KB.

tip

Create assets with confidence! Our in-app message image templates and safe zone overlays are designed to play nicely with devices of all sizes. Download Design Templates ZIP

 Layout | 
 Asset Size | 
 Notes | 

 Image + Text | 
 1:1 aspect ratio
High-res 150 x 150 px
 Minimum 50 x 50 px | 
 Images of various aspect ratios will fit into a square image container, without cropping. | 

You should always preview and test your messages on a variety of devices to ensure that the most important areas of your image and message appear as expected. Note that when previewing your message on the composer, the actual rendering on devices may differ.

## Hyperlinks and anchor text

To add a link in a slideup, enter the message copy in the Body field and set the destination in On-click behavior (for example, Redirect to URL). When On-click behavior is configured, taps anywhere on the message except the close control trigger that action.

For custom HTML in-app messages, you can use HTML links directly. See Custom HTML in-app messages.

## Mobile devices

On mobile devices, slideups appear at the top or bottom of the app screen. You can specify this when you create your message. Users can swipe to dismiss the slideup, or tap to open it if a click action is included. If a click action is added to the slideup, a chevron “>” is shown.

## Larger screens

- desktop
 
- tablet

On a desktop browser, a slideup in-app message will sit in the corner of the screen as shown in the following screenshot (unless designated otherwise when creating the in-app message). Users can click the close “X” button to dismiss the slideup.

On a tablet, a slideup in-app message appears on the bottom of the screen. Similar to on mobile devices, users can swipe to dismiss the slideup, or tap to open it if a click action is included. If a click action is added to the slideup, a chevron “>” is shown. A close “X” button is not shown by default.

- 

New Stuff!
