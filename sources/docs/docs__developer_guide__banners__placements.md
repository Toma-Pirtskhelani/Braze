---
url: https://www.braze.com/docs/developer_guide/banners/placements
slug: docs__developer_guide__banners__placements
title: "Manage Banner placements"
description: "Learn how to create and manage Banner placements in the Braze SDK, including accessing their unique properties and logging impressions."
section: developer_guide/banners
fetched: 2026-09-02
evidence: company-own (technical)
---
# Manage Banner placements

Learn how to create and manage Banner placements in the Braze SDK, including accessing their unique properties and logging impressions. For more general information, see About Banners.

## About placement requests

When you create placements in your app or website, your app sends a request to Braze to fetch Banner messages for each placement.

- You can request up to 10 placements per refresh request.
 
- For each placement, Braze returns the highest-priority Banner the user is eligible to receive.
 
- If more than 10 placements are requested in a refresh, only the first 10 are returned; the rest are dropped.

For example, an app might request three placements in a refresh request: homepage_promo, cart_abandonment, and seasonal_offer. Each request returns the most relevant Banner for that placement.

#### Rate limiting for refresh requests

If you’re on older SDK versions (before Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0, and Flutter 15.0.0), only one refresh request is permitted per user session.

If you’re on newer minimum SDK versions (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+, and Flutter 15.0.0+), refresh requests are controlled by a token bucket algorithm to prevent excessive polling:

- Each user session begins with five refresh tokens.
 
- Tokens refill at a rate of one token every 180 seconds (3 minutes).

Each explicit call to requestBannersRefresh consumes one token. The automatic refresh that occurs at the start of a new session or when changeUser is called does not consume a token, as this refresh is a publishing of the last cached Banner for that user. If you attempt a refresh when no tokens are available, the SDK doesn’t make the request and logs an error until a token refills. This is important for mid-session and event-triggered updates. To implement dynamic updates (for example, after a user completes an action on the same page), call the refresh method after the custom event is logged, but note the necessary delay for Braze to ingest and process the event before the user qualifies for a different Banner campaign.

## Create a placement

### Prerequisites

These are the minimum SDK versions needed to create Banner placements:

   Swift: 13.1.0+     Web: 6.4.0+     Android: 38.0.0+  Flutter: 16.0.0+  React Native: 17.0.1+  

### Step 1: Create placements in Braze

If you haven’t already, you’ll need to create Banner placements in Braze that are used to define the locations in your app or site can display Banners. To create a placement, go to Settings > Banners Placements, then select Create Placement.

Give your placement a name and assign a Placement ID. Be sure you consult other teams before assigning an ID, as it’ll be used throughout the card’s lifecycle and shouldn’t be changed later. For more information, see Placement IDs.

### Step 2: Refresh placements in your app

To refresh placements, call the refresh method for your SDK (requestBannersRefresh() on Web and Android, or requestRefresh() on Swift).

Banner refresh behavior has two paths:

- Explicit refresh: You can call the refresh method at any point during an active session.
 
- Automatic refresh on a new session: After you make at least one explicit refresh request, the SDK can re-request the most recently requested placement IDs when a new Braze session starts (for example, after changeUser() or after a session timeout).

The role of subscribeToBannersUpdates() differs by platform:

- iOS and Android: subscribeToBannersUpdates() (or subscribeToUpdates() on Swift) registers an update callback. The automatic session-start refresh is not dependent on the subscription being active.
 
- Web: The automatic session-start refresh is tied to subscribeToBannersUpdates() being registered. Without an active subscription, the SDK does not automatically repeat the refresh on a new session.

In all cases, you must make at least one explicit refresh request per app lifecycle so the SDK knows which placement IDs to keep updated. Banners are not fetched automatically on first launch without that initial call, and the tracked placement IDs reset after the app restarts.

Automatic session-start refreshes do not consume a rate limiting token.

tip

Refresh placements as soon as possible to avoid delays in downloading or displaying Banners.

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

```

1
2
3

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

```
 | 

```

1

```
 | 
```
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])

```
 | 

- java
 
- kotlin

```

1
2
3
4

```
 | 
```
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);

```
 | 

```

1

```
 | 
```
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))

```
 | 

```

1

```
 | 
```
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Unity.

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Cordova.

```
 | 

```

1

```
 | 
```
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Roku.

```
 | 

### Step 3: Listen for updates

tip

If you insert Banners using the SDK methods in this guide, all analytics events (such as impressions and clicks) are handled automatically, and impressions are only logged when the banner is in view.

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

- javascript
 
- react

If you’re using vanilla JavaScript with the Web Braze SDK, use subscribeToBannersUpdates to listen for placement updates and then call requestBannersRefresh to fetch them.

```

1
2
3
4
5
6
7
8

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
 console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

```
 | 

If you’re using React with the Web Braze SDK, set up subscribeToBannersUpdates inside a useEffect hook and call requestBannersRefresh after registering your listener.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

```
 | 
```
import * as braze from "@braze/web-sdk";

useEffect(() => {
 const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
 console.log("Banners were updated");
 });

 // always refresh after your subscriber function has been registered
 braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

 // cleanup listeners
 return () => {
 braze.removeSubscription(subscriptionId);
 }
}, []);

```
 | 

note

Your banner update listener reflects the SDK’s in-memory banner state. A single update can include placements that were already cached (for example, from an earlier refresh, another screen, or automatic SDK work), not only the placement IDs from your most recent requestRefresh call. If you care only about certain placements, check each banner’s placement ID in your listener and skip the rest. When you’ve registered your listener, call requestRefresh for the placements you want to sync from Braze.

```

1
2
3
4
5
6
7
8

```
 | 
```
let placementIds = ["global_banner", "navigation_square_banner"]
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
 banners.forEach { placementId, banner in
 print("Received banner: \(banner) with placement ID: \(placementId)")
 }
}
// Always refresh after your subscriber is registered
brazeClient.braze()?.banners.requestRefresh(placementIds: placementIds)

```
 | 

note

Your banner update listener reflects the SDK’s in-memory banner state. A single update can include placements that were already cached (for example, from an earlier refresh, another screen, or automatic SDK work), not only the placement IDs from your most recent requestBannersRefresh call. If you care only about certain placements, check each banner’s placement ID in your listener and skip the rest. When you’ve registered your listener, call requestBannersRefresh for the placements you want to sync from Braze.

- java
 
- kotlin

```

1
2
3
4
5
6
7
8
9
10

```
 | 
```
ArrayList<String> placementIds = new ArrayList<>();
placementIds.add("global_banner");
placementIds.add("navigation_square_banner");
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
 for (Banner banner : banners.getBanners()) {
 Log.d(TAG, "Received banner: " + banner.getPlacementId());
 }
});
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds);

```
 | 

```

1
2
3
4
5
6
7
8

```
 | 
```
val placementIds = listOf("global_banner", "navigation_square_banner")
Braze.getInstance(context).subscribeToBannersUpdates { update ->
 for (banner in update.banners) {
 Log.d(TAG, "Received banner: " + banner.placementId)
 }
}
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds)

```
 | 

```

1
2
3
4
5
6
7
8
9
10

```
 | 
```
const bannerCardsSubscription = Braze.addListener(
 Braze.Events.BANNER_CARDS_UPDATED,
 (data) => {
 const banners = data.banners;
 console.log(
 `Received ${banners.length} Banner Cards with placement IDs:`,
 banners.map((banner) => banner.placementId)
 );
 }
);

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Unity.

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Cordova.

```
 | 

```

1
2
3
4
5

```
 | 
```
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
 for (final banner in banners) {
 print("Received banner: " + banner.toString());
 }
});

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Roku.

```
 | 

### Step 4: Insert using the placement ID

tip

For a complete step-by-step tutorial, check out Displaying a Banner by Placement ID.

- web
 
- swift
 
- android
 
- react native
 
- unity
 
- cordova
 
- flutter
 
- roku

Create a container element for the Banner. Be sure to set its width and height.

```

1

```
 | 
```
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

```
 | 

- javascript
 
- react

If you’re using vanilla JavaScript with the Web Braze SDK, call the insertBanner method to replace the inner HTML of the container element.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
 baseUrl: "sdk-base-url",
 allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
 // get this placement's banner. If it's `null` the user did not qualify for one.
 const globalBanner = braze.getBanner("global_banner");
 if (!globalBanner) {
 return;
 }

 // choose where in the DOM you want to insert the banner HTML
 const container = document.getElementById("global-banner-container");

 // Insert the banner which replaces the innerHTML of that container
 braze.insertBanner(globalBanner, container);

 // Special handling if the user is part of a Control Variant
 if (globalBanner.isControl) {
 // hide or collapse the container
 container.style.display = "none";
 }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

```
 | 

If you’re using React with the Web Braze SDK, call the insertBanner method with a ref to replace the inner HTML of the container element.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17

```
 | 
```
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
 const bannerRef = useRef<HTMLDivElement>(null);

 useEffect(() => {
 const globalBanner = braze.getBanner("global_banner");
 if (!globalBanner || globalBanner.isControl) {
 // hide the container
 } else {
 // insert the banner to the container node
 braze.insertBanner(globalBanner, bannerRef.current);
 }
 }, []);
 return <div ref={bannerRef}></div>
}

```
 | 

tip

To track impressions, be sure to call insertBanner for isControl. You can then hide or collapse your container afterwards.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47

```
 | 
```
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
 self.globalBanner = banner
})

// UIKit implementation:
// If you simply want the Banner view, initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
 let bannerUIView = BrazeBannerUI.BannerUIView(
 placementId: "global_banner",
 braze: braze,
 // iOS does not perform automatic resizing or visibility changes.
 // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
 processContentUpdates: { result in
 switch result {
 case .success(let updates):
 if let height = updates.height {
 // Adjust the visibility and/or height.
 }
 case .failure(let error):
 // Handle the error.
 }
 }
 )
}

// SwiftUI implementation:
// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
 let bannerView = BrazeBannerUI.BannerView(
 placementId: "global_banner",
 braze: braze,
 // iOS does not perform automatic resizing or visibility changes.
 // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
 processContentUpdates: { result in
 switch result {
 case .success(let updates):
 if let height = updates.height {
 // Adjust the visibility and/or height according to your parent controller.
 }
 case .failure(let error):
 // Handle the error.
 }
 }
 )
}

```
 | 

- java
 
- kotlin

To get the Banner in Java code, use:

```

1

```
 | 
```
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");

```
 | 

You can create Banners in your Android views layout by including this XML:

```

1
2
3
4
5

```
 | 
```
<com.braze.ui.banners.BannerView
 android:id="@+id/global_banner_id"
 android:layout_width="match_parent"
 android:layout_height="wrap_content"
 app:placementId="global_banner" />

```
 | 

If you’re using Android Views, use this XML:

```

1
2
3
4
5

```
 | 
```
<com.braze.ui.banners.BannerView
 android:id="@+id/global_banner_id"
 android:layout_width="match_parent"
 android:layout_height="wrap_content"
 app:placementId="global_banner" />

```
 | 

To use Jetpack Compose, add the com.braze:android-sdk-jetpack-compose artifact to your app module. Use the same version as your other Braze Android SDK dependencies. This module is separate from android-sdk-ui and ships the Banner composable under com.braze.jetpackcompose.banners.

note

Some Compose UI libraries define their own Banner composable. Import com.braze.jetpackcompose.banners.Banner explicitly so you call Braze’s API.

```

1
2
3
4
5
6

```
 | 
```
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
 Banner(placementId = "global_banner")
}

```
 | 

Optionally pass heightCallback to receive the rendered height in dp when the banner size changes. For reference, see the KDoc for Banner.

If you don’t add the Jetpack Compose module, wrap BannerView in AndroidView:

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

```
 | 
```
import android.view.ViewGroup
import androidx.compose.runtime.Composable
import androidx.compose.ui.viewinterop.AndroidView
import com.braze.ui.banners.BannerView

@Composable
fun myBannerSlot() {
 AndroidView(
 factory = { context ->
 BannerView(context, "global_banner").apply {
 layoutParams = ViewGroup.LayoutParams(
 ViewGroup.LayoutParams.MATCH_PARENT,
 ViewGroup.LayoutParams.WRAP_CONTENT
 )
 }
 },
 update = { it.placementId = "global_banner" }
 )
}

```
 | 

To get the Banner in Kotlin, use:

```

1

```
 | 
```
val banner = Braze.getInstance(context).getBanner("global_banner")

```
 | 

If you’re using React Native’s New Architecture, you need to register BrazeBannerView as a Fabric component in your AppDelegate.mm.

```

1
2
3
4
5
6
7
8

```
 | 
```
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
 NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
 dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
 return dictionary;
}
#endif

```
 | 

For the simplest integration, add the following JavaScript XML (JSX) snippet into your view hierarchy, providing just the placement ID.

```

1
2
3

```
 | 
```
<Braze.BrazeBannerView
 placementId='global_banner'
/>

```
 | 

To get the Banner’s data model in React Native, or to check for the presence of that placement in your user’s cache, use:

```

1

```
 | 
```
const banner = await Braze.getBanner("global_banner");

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Unity.

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Cordova.

```
 | 

For the simplest integration, add the following widget into your view hierarchy, providing just the placement ID.

```

1
2
3
4

```
 | 
```
BrazeBannerView(
 placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:

```
 | 

You can use the getBanner method to check for the presence of that placement in your user’s cache.

```

1
2
3
4
5
6
7

```
 | 
```
braze.getBanner("global_banner").then((banner) {
 if (banner == null) {
 // Handle null cases.
 } else {
 print(banner.toString());
 }
});

```
 | 

```

1

```
 | 
```
This feature is not currently supported on Roku.

```
 | 

### Step 5: Send a test Banner (optional)

Before you launch a Banner campaign, you can send a test Banner to verify your integration. Test Banners are stored in a separate in-memory cache and don’t persist across app restarts. While no extra setup is needed, your test device must be capable of receiving foreground push notifications so it can display the test.

note

Test Banners are like any other banners, except they’re removed at the next app session.

## Log impressions

Braze automatically logs impressions for Banners that are in view when you use SDK methods to insert a Banner—so no need to track impressions manually.

## Logging clicks

The method used to log Banner clicks depends on how your Banner is rendered and where your click handler is located.

### Standard Banner content (automatic)

If you’re using default, out-of-the-box SDK methods to insert Banners, and your Banner uses standard editor components (images, buttons, text), clicks are tracked automatically. The SDK attaches click listeners to these elements, and no additional code is needed.

### Custom Code Blocks

If your Banner uses the Custom Code editor block in the Braze dashboard, you must use brazeBridge.logClick() to log clicks from within that custom HTML. This applies even when using SDK methods to render the Banner, because the SDK cannot automatically attach listeners to elements inside your custom code.

```

1
2
3

```
 | 
```
<button onclick="brazeBridge.logClick()">
 Click me
</button>

```
 | 

For the full reference, see Custom code and JavaScript bridge for Banners. The brazeBridge provides a communication layer between the Banner’s internal HTML and the parent Braze SDK.

### Custom UI implementations (headless)

If you’re building a fully custom UI using the Banner’s custom properties rather than rendering the Banner HTML, you must manually log clicks and impressions from your application code. Because the SDK is not rendering the Banner, it has no way to automatically track interactions with your custom UI elements.

For method signatures and full details, see the Braze SDK reference documentation.

#### Logging impressions

Call the platform’s Banner impression method when your custom UI considers the Banner “viewed.” Build robust logic for what counts as an impression to avoid duplicate events—for example, log only when the Banner enters the viewport (or equivalent), and do not log again when the same Banner is scrolled back into view or when your component re-renders without a new view event.

- web
 
- android
 
- swift
 
- react native
 
- flutter

```

1
2
3
4
5
6
7

```
 | 
```
import * as braze from "@braze/web-sdk";

// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
const banner = braze.getBanner("placement_id_homepage_top");
if (banner) {
 braze.logBannerImpressions([banner]);
}

```
 | 

Web SDK reference

- kotlin
 
- java

```

1
2

```
 | 
```
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top")

```
 | 

```

1
2

```
 | 
```
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top");

```
 | 

Android SDK reference

```

1
2
3
4

```
 | 
```
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
 banner?.context.logImpression()
}

```
 | 

Swift SDK reference

```

1
2

```
 | 
```
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");

```
 | 

See the React Native SDK repository for the latest method signatures.

```

1
2

```
 | 
```
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");

```
 | 

Flutter SDK reference

#### Logging clicks

Call the platform’s Banner click method when the user taps your custom Banner (or a specific button). Pass the optional buttonId when the click is on a specific button so analytics can attribute the click correctly.

- web
 
- android
 
- swift
 
- react native
 
- flutter

```

1
2
3
4

```
 | 
```
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId); // buttonID is optional

```
 | 

Web SDK reference

- kotlin
 
- java

```

1
2

```
 | 
```
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId) // buttonID parameter can be null

```
 | 

```

1
2

```
 | 
```
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId); // buttonID parameter can be null

```
 | 

Android SDK reference

```

1
2
3
4

```
 | 
```
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
 banner?.context.logClick(buttonId: buttonId) // buttonID is optional
}

```
 | 

Swift SDK reference

```

1
2

```
 | 
```
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId); // buttonID is optional

```
 | 

See the React Native SDK repository for the latest method signatures.

```

1
2

```
 | 
```
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId); // buttonID parameter can be null

```
 | 

Flutter SDK reference

## Log dismissals

Banner dismissals programmatically remove a Banner from a placement when a user actively dismisses it. When dismissed, the Banner is suppressed for that user. The next time the list of placements is refreshed, a new banner is returned if the user is eligible for one.

### Prerequisites

These are the minimum SDK versions required to log Banner dismissals:

   Swift: 14.1.0+     Web: 6.7.1+     Android: 42.1.0+  

### Integrations

#### Standard Banner integrations (drag-and-drop editor)

If your Banner uses the drag-and-drop editor and includes a dismiss button component, no additional code is required. When a user clicks the dismiss button, the message is hidden, triggers a dismissal, and then records a dismissal event for analytics.

#### Custom Code Blocks

If your Banner uses the Custom Code editor block, you can trigger a dismissal directly from within the Banner’s HTML using brazeBridge.closeMessage().

```

1
2
3

```
 | 
```
<button onclick="brazeBridge.closeMessage()">
 Dismiss
</button>

```
 | 

#### Dismiss a banner programmatically

If you’re using the standard BrazeBannerView with the dismiss button created in the drag-and-drop editor, no additional code is required; dismissal is handled automatically.

For custom UI integrations, you can call the dismiss method directly on your Braze instance to programmatically dismiss a banner and log a dismissal event. The dismiss method is safe to call multiple times—the SDK ignores duplicate calls for the same banner.

These are the minimum SDK versions required to dismiss a banner programmatically:

   Swift: 15.1.0+     Web: 6.9.0+     Android: 42.3.0+  Flutter: 20.0.0+  React Native: 22.0.0+  

- web
 
- android
 
- swift
 
- react native
 
- flutter

Pass the Banner object to braze.dismissBanner(). You can get the Banner object from braze.getAllBanners() or from a subscribeToBannersUpdates callback.

- javascript
 
- react

```

1
2
3
4
5
6
7
8

```
 | 
```
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
 braze.dismissBanner(banner);
}

```
 | 

```

1
2
3
4
5
6
7
8

```
 | 
```
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
 braze.dismissBanner(banner);
}

```
 | 

- java
 
- kotlin

```

1

```
 | 
```
Braze.getInstance(context).dismissBanner("your-placement-id");

```
 | 

```

1

```
 | 
```
Braze.getInstance(context).dismissBanner("your-placement-id")

```
 | 

Use dismiss() on the banner’s context when available. This method is idempotent and fires the onDismiss callback automatically. If the context is unavailable, call dismiss(using:) directly on the banner. Both methods must be called from the main thread.

```

1
2
3
4
5

```
 | 
```
// Preferred: dismiss via context.
banner.context?.dismiss()

// Fallback: if context is unavailable.
banner.dismiss(using: braze)

```
 | 

In Objective-C, these are available as [banner.context dismiss] and [banner dismissUsing:braze].

```

1

```
 | 
```
Braze.dismissBanner("your-placement-id");

```
 | 

```

1

```
 | 
```
braze.dismissBanner("your-placement-id");

```
 | 

### Log custom analytics on banner dismissal

To run custom logic when a banner is dismissed—such as logging analytics—use the dismiss callback for your SDK. The callback receives an event object with the banner’s placementId, stableKey, and trackingId.

- web
 
- android
 
- swift
 
- react native
 
- flutter

Use Banner.subscribeToDismissedEvent() to run custom logic when a specific banner is dismissed. Subscribe to the event before displaying the banner.

note

Banner.subscribeToDismissedEvent() requires Web SDK 6.9.0 or later. On earlier versions, use braze.subscribeToBannersUpdates() and detect dismissal by checking whether the banner is no longer present in the updated banners map.

- javascript
 
- react

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
 const banner = banners["global_banner"];

 if (banner) {
 banner.subscribeToDismissedEvent(() => {
 // Run any custom logic here, such as logging custom analytics
 console.log("Banner was dismissed");
 });
 }
});

braze.requestBannersRefresh(["global_banner"]);

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

```
 | 
```
import { useEffect } from "react";
import * as braze from "@braze/web-sdk";

useEffect(() => {
 const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
 const banner = banners["global_banner"];

 if (banner) {
 banner.subscribeToDismissedEvent(() => {
 // Run any custom logic here, such as logging custom analytics
 console.log("Banner was dismissed");
 });
 }
 });

 braze.requestBannersRefresh(["global_banner"]);

 return () => {
 braze.removeSubscription(subscriptionId);
 };
}, []);

```
 | 

Set the optional onDismissCallback property on BannerView.

- java
 
- kotlin

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14

```
 | 
```
import android.util.Log;
import com.braze.ui.banners.BannerView;
import kotlin.Unit;

// After obtaining your BannerView instance (for example from XML via findViewById, or `new BannerView(context, "global_banner")`)

bannerView.setOnDismissCallback((snapshot) -> {
 Log.d(TAG, "placementId: " + snapshot.getPlacementId()
 + ", stableKey: " + snapshot.getStableKey()
 + ", trackingId: " + snapshot.getTrackingId());

 // Run any custom logic here, such as logging custom analytics
 return Unit.INSTANCE;
});

```
 | 

```

1
2
3
4
5
6
7
8
9
10

```
 | 
```
import android.util.Log
import com.braze.ui.banners.BannerView

// After obtaining your BannerView instance (for example via findViewById or `BannerView(context, "global_banner")`)

bannerView.onDismissCallback = { snapshot ->
 Log.d(TAG, "placementId: ${snapshot.placementId}, stableKey: ${snapshot.stableKey}, trackingId: ${snapshot.trackingId}")

 // Run any custom logic here, such as logging custom analytics
}

```
 | 

```

1
2
3
4
5
6
7
8
9

```
 | 
```
// After initializing your banner view instance using UIKit or SwiftUI

bannerView.onDismiss = { event in
 print("Banner dismissed — placementId: \(event.placementId ?? "unknown")")
 print(" stableKey: \(event.stableKey ?? "unknown")")
 print(" trackingId: \(event.trackingId ?? "unknown")")

 // Run any custom logic here, such as logging custom analytics
}

```
 | 

Set the onDismiss prop on Braze.BrazeBannerView to run custom logic when a banner is dismissed.

```

1
2
3
4
5
6
7
8
9

```
 | 
```
import Braze from "@braze/react-native-sdk";

<Braze.BrazeBannerView
 placementId="global_banner"
 onDismiss={(event) => {
 console.log("placementId:", event.placementId, "stableKey:", event.stableKey, "trackingId:", event.trackingId);
 // Run any custom logic here, such as logging custom analytics
 }}
/>

```
 | 

Set the onDismiss parameter on BrazeBannerView to run custom logic when a banner is dismissed.

```

1
2
3
4
5
6
7

```
 | 
```
BrazeBannerView(
 placementId: 'global_banner',
 onDismiss: (BrazeBannerDismissEvent event) {
 print('placementId: ${event.placementId}, stableKey: ${event.stableKey}, trackingId: ${event.trackingId}');
 // Run any custom logic here, such as logging custom analytics
 },
)

```
 | 

### Pending dismissal storage cap

Dismissal events are stored locally as pending entries until they can be synced to the Braze server on the next requestBannersRefresh call.

warning

In rare cases where a large number of dismissals accumulate without a successful sync, older pending dismissals may be dropped. If this occurs, previously-dismissed Banners may reappear until the next successful sync completes. To minimize this risk, call requestBannersRefresh whenever your app regains network connectivity.

## Dimensions and sizing

Here’s what you need to know about Banner dimensions and sizing:

- While the composer allows you to preview Banners in different dimensions, that information isn’t saved or sent to the SDK.
 
- The HTML will take up the full width of the container it’s rendered in.
 
- We recommend making a fixed dimension element and testing those dimensions in composer.

## Custom properties

You can use custom properties from your Banner campaign to retrieve key–value data through the SDK and modify your app’s behavior or appearance. For example, you could:

- Send metadata for your third-party analytics or integrations.
 
- Use metadata such as a timestamp or JSON object to trigger conditional logic.
 
- Control the behavior of a Banner based on included metadata like ratio or format.

### Prerequisites

You must add custom properties to your Banner campaign. Additionally, these are the minimum SDK versions required to access custom properties:

   Swift: 13.1.0+     Web: 6.1.0+     Android: 38.0.0+  Flutter: 15.1.0+  React Native: 17.0.0+  

### Access custom properties

To access a banner’s custom properties, use one of the following methods based on the property’s type defined in the dashboard. If the key doesn’t match a property of that type or does not exist, the method returns null.

- web
 
- swift
 
- android
 
- react native
 
- flutter

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

```
 | 
```
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

 // Returns the string property
 const stringProperty = banner.getStringProperty("color");

 // Returns the boolean property
 const booleanProperty = banner.getBooleanProperty("expanded");

 // Returns the number property
 const numberProperty = banner.getNumberProperty("height");

 // Returns the timestamp property (as a number)
 const timestampProperty = banner.getTimestampProperty("account_start");

 // Returns the image URL property as a string of the URL
 const imageProperty = banner.getImageProperty("homepage_icon");

 // Returns the JSON object property
 const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

```
 | 
```
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
 // Returns the string property
 let stringProperty: String? = banner.stringProperty(key: "color")

 // Returns the boolean property
 let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

 // Returns the number property as a double
 let numberProperty: Double? = banner.numberProperty(key: "height")

 // Returns the Unix UTC millisecond timestamp property as an integer
 let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

 // Returns the image property as a String of the image URL
 let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

 // Returns the JSON object property as a [String: Any] dictionary
 let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}

```
 | 

- java
 
- kotlin

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23

```
 | 
```
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
 // Returns the string property
 String stringProperty = banner.getStringProperty("color");
 
 // Returns the boolean property
 Boolean booleanProperty = banner.getBooleanProperty("expanded");
 
 // Returns the number property
 Number numberProperty = banner.getNumberProperty("height");
 
 // Returns the timestamp property (as a Long)
 Long timestampProperty = banner.getTimestampProperty("account_start");
 
 // Returns the image URL property as a String of the URL
 String imageProperty = banner.getImageProperty("homepage_icon");
 
 // Returns the JSON object property as a JSONObject
 JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

```
 | 
```
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

```
 | 
```
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

```
 | 
```
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
 // Get the string property
 final String? stringProperty = banner?.getStringProperty('color');
 
 // Get the boolean property
 final bool? booleanProperty = banner?.getBooleanProperty('expanded');
 
 // Get the number property
 final num? numberProperty = banner?.getNumberProperty('height');
 
 // Get the timestamp property
 final int? timestampProperty = banner?.getTimestampProperty('account_start');
 
 // Get the image URL property
 final String? imageProperty = banner?.getImageProperty('homepage_icon');
 
 // Get the JSON object property
 final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');
 
 // Use these properties as needed in your UI or logic
});

```
 | 

- 

New Stuff!
