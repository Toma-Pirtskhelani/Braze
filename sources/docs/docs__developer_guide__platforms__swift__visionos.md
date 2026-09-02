---
url: https://www.braze.com/docs/developer_guide/platforms/swift/visionos
slug: docs__developer_guide__platforms__swift__visionos
title: "visionOS support"
description: "This article covers the features supported on visionOS."
section: developer_guide/platforms
fetched: 2026-09-02
evidence: company-own (technical)
---
# visionOS support

Starting with Braze Swift SDK 8.0.0, you can leverage Braze with visionOS, Apple’s spacial-computing platform for the Apple Vision Pro. For a sample visionOS app using Braze, see Sample Apps.

## Fully supported features

Most features available on iOS are also available on visionOS, including:

- Analytics (sessions, custom events, purchases, etc.)
 
- In-App Messaging (data models and UI)
 
- Content Cards (data models and UI)
 
- Push Notifications (user-visible with action buttons and silent notifications)
 
- Feature Flags
 
- Location Analytics

## Partially supported features

Some features are only partially supported on visionOS, but Apple is likely to address these in the future:

- Rich Push Notifications

- Images are supported.
 
- GIFs and videos display the preview thumbnail, but cannot be played.
 
- Audio playback is not supported.

- Push Stories

- Scrolling and selecting the Push Story page is supported.
 
- Navigating between Push Story pages using Next is not supported.

## Unsupported features

- Geofences Monitoring is not supported. Apple has not made the Core Location APIs for region monitoring available on visionOS.
 
- Live Activities are not supported. Currently, ActivityKit is only available on iOS and iPadOS.

- 

New Stuff!
