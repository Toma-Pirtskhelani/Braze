---
url: https://www.braze.com/docs/developer_guide/banners/tutorial_displaying_banners
slug: docs__developer_guide__banners__tutorial_displaying_banners
title: "Tutorial: Displaying a Banner by Placement ID"
description: "New to Banners in the Braze SDK? Start with this tutorial on displaying Banners by placement ID."
section: developer_guide/banners
fetched: 2026-09-02
evidence: company-own (technical)
---
# Tutorial: Displaying a Banner by Placement ID

Follow along with the sample code in this tutorial to display Banners using their placement ID. For more general information, see Banners.

- web
 
- android
 
- swift

## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

   Swift: 11.3.0+     Web: 5.8.1+     Android: 33.1.0+  Flutter: 13.0.0+  React Native: 14.0.0+  

## Displaying banners for the Web SDK

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

### 2. Subscribe to Banner updates

Use subscribeToBannersUpdates() to register a handler that runs whenever a Banner is updated. Inside the handler, call braze.getBanner("global_banner") to get the latest placement.

### 3. Insert the Banner and handle control groups

Use braze.insertBanner(banner, container) to insert a Banner when it’s returned. To ensure keep your layout clean, hide or collapse Banners that are apart of a control group (for example, when isControl is true).

### 4. Refresh your Banners

After initializing the SDK, call requestBannersRefresh(["global_banner", ...]) to ensure that Banners are refreshed at the start of each session.

You can also call this function at any time to refresh Banner placements later.

### 5. Add a container for your Banner

In your HTML, add a new <div> element and give it a short, Banner-related id, such as global-banner-container. Braze will use this <div> to insert your Banner into the page.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

```

```

## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

   Swift: 11.3.0+     Web: 5.8.1+     Android: 33.1.0+  Flutter: 13.0.0+  React Native: 14.0.0+  

## Displaying banners for the Android SDK

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

### 2. Subscribe to Banner updates

Use subscribeToBannersUpdates() to register a handler that runs whenever a Banner is updated.

### 3. Refresh your placements

After initializing the Braze SDK, call requestBannersRefresh(["PLACEMENT_ID"]) to fetch the latest Banner content for that placement.

### 4. Define BannerView in your banners.xml

In banners.xml, declare a <com.braze.ui.banners.BannerView> element with app:placementId="PLACEMENT_ID". Braze will use this element to insert your Banner into your UI.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

```

```

```

```

## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

   Swift: 11.3.0+     Web: 5.8.1+     Android: 33.1.0+  Flutter: 13.0.0+  React Native: 14.0.0+  

## Displaying banners for the Swift SDK

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

- uikit
 
- swiftui

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

### 2. Refresh your placements

After initializing the Braze SDK, call requestBannersRefresh(placementIds: ["PLACEMENT_ID"]) to refresh Banner content at the start of each session.

### 3. Initialize the Banner and provide a callback

Create a BrazeBannerUI.BannerUIView instance with your Braze object and placement ID, and provide a processContentUpdates callback to unhide the Banner and update its height constraint based on the provided content height.

### 4. Enable Auto Layout constraints

Hide the Banner view by default, then disable autoresizing mask translation to enable Auto Layout constraints.

### 5. Anchor content and set height constraints

Anchor your main content to the top using Auto Layout, and place the Banner view after it. Pin the Banner’s leading, trailing, and bottom edges to the safe area, and set an initial height constraint of 0 that will be updated when content loads.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

```

```

```

```

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

### 2. Refresh your placements

After initializing the Braze SDK, call requestBannersRefresh(placementIds: ["PLACEMENT_ID"]) to refresh Banner content at the start of each session.

### 3. Create a view component

Create a reusable SwiftUI view component that displays available Banners and contains your main app content if needed.

### 4. Only display available Banners

Only attempt to show BrazeBannerUI.BannerView if the SDK is initialized and Banner content exists for that user. In .onAppear, call getBanner(for:placementID) to set the state of hasBannerForPlacement.

### 5. Only show BannerView after it loads

To avoid blank space in your UI, only show BrazeBannerUI.BannerView if a Banner is present and the SDK is initialized.

### 6. Dynamically update Banner height

Use the processContentUpdates callback to fetch the Banner’s content height as soon as it loads. Update your SwiftUI state (contentHeight) and apply a .frame(height:) constraint using the provided height.

### 7. Limit the Banner height

To ensure your Banner never exceeds the maximum height, apply a .frame(height: min(contentHeight, 80)) modifier. This will keep your UI visually balanced regardless of the Banner’s content.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

```

```

```

```

- 

New Stuff!
