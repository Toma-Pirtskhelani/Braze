---
url: https://www.braze.com/docs/developer_guide/banners/migrating_from_content_cards
slug: docs__developer_guide__banners__migrating_from_content_cards
title: "Migrate from Content Cards to Banners"
description: "Learn how to migrate from Content Cards to Banners, including code examples for all supported SDKs, limitations, and benefits."
section: developer_guide/banners
fetched: 2026-09-02
evidence: company-own (technical)
---
# Migrate from Content Cards to Banners

This guide helps you migrate from Content Cards to Banners for banner-style messaging use cases. Banners are ideal for inline, persistent in-app and web messages that appear at specific placements in your application.

## Why migrate to Banners?

- If your engineering team is building or maintaining custom Content Cards, migrating to Banners can reduce that ongoing investment. Banners let marketers control the UI directly, freeing developers for other work.
 
- If you’re launching new homepage messages, onboarding flows, or persistent announcements, start with Banners rather than building on Content Cards. You can benefit from real-time personalization, no 30-day expiration, no size limit, and native prioritization from day one.
 
- If you’re working around the 30-day expiration limit, managing complex re-eligibility logic, or frustrated by stale personalization, Banners solves these problems natively.

Banners offer several advantages over Content Cards for banner-style messaging:

### Accelerated production

- Reduced on-going engineering support required: Marketers can build custom messages using a drag-and-drop editor and custom HTML without requiring developer assistance for customization
 
- Flexible customization options: Design directly in the editor, use HTML or leverage existing data models with custom properties

### Better UX

- Dynamic content updates: Banners refresh Liquid logic and eligibility on every refresh, ensuring users always see the most relevant content
 
- Native placement support: Messages appear in specific contexts rather than a feed, providing better contextual relevance
 
- Native prioritization: Control over display order without custom logic, making it easier to manage message hierarchy

### Persistence

- No expiration limit: Banner campaigns do not have a 30-day expiration limit like Content Cards, allowing for true persistence of messages

## When to migrate

Consider migrating to Banners if you’re using Content Cards for:

- Homepage heroes, product page promotions, checkout offers
 
- Persistent navigation announcements or sidebar messages
 
- Always-on messages running longer than 30 days
 
- Messages where you want real-time personalization and eligibility

## When to keep Content Cards

Continue using Content Cards if you need:

- Feed experiences: Any use case involving multiple scrollable messages or a card-based “Inbox”.
 
- Specific features: Messages that require promotional codes, as Banners do not support these natively. Banners support Connected Content in early access.
 
- Triggered delivery: Use cases strictly requiring API-triggered or action-based delivery. While Banners don’t support API-triggered or action-based delivery, real-time eligibility evaluation means users instantly qualify or disqualify based on segment membership at each refresh.

## Migration guide

### Prerequisites

Before migrating, ensure your Braze SDK meets the minimum version requirements:

   Swift: 13.1.0+     Web: 6.4.0+     Android: 38.0.0+  Flutter: 16.0.0+  React Native: 17.0.1+  

Dismissals and re-eligibility require the following minimum SDK versions:

   Swift: 14.1.0+     Web: 6.7.1+     Android: 42.1.0+  

### Subscribe to updates

#### Content Cards approach

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
8

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
 // Handle array of cards
 cards.forEach(card => {
 console.log("Card:", card.id);
 });
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

```
 | 
```
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
 // Handle array of cards
 cards.forEach { card ->
 Log.d(TAG, "Card: ${card.id}")
 }
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

```
 | 
```
braze.contentCards.subscribeToUpdates { cards in
 // Handle array of cards
 for card in cards {
 print("Card: \(card.id)")
 }
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

```
 | 
```
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
 const cards = update.cards;
 // Handle array of cards
 cards.forEach(card => {
 console.log("Card:", card.id);
 });
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

```
 | 
```
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
 // Handle array of cards
 for (final card in contentCards) {
 print("Card: ${card.id}");
 }
});

```
 | 

#### Banners approach

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
8
9

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
 // Get banner for specific placement
 const banner = braze.getBanner("sample_placement_id");
 if (banner) {
 console.log("Banner received for placement:", banner.placementId);
 }
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

```
 | 
```
Braze.getInstance(context).subscribeToBannersUpdates { update ->
 // Get banner for specific placement
 val banner = Braze.getInstance(context).getBanner("sample_placement_id")
 if (banner != null) {
 Log.d(TAG, "Banner received for placement: ${banner.placementId}")
 }
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
braze.banners.subscribeToUpdates { banners in
 // Get banner for specific placement
 braze.banners.getBanner(for: "sample_placement_id") { banner in
 guard let banner = banner else { return }

 print("Banner received for placement: \(banner.placementId)")
 }
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
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
 const banners = data.banners;
 // Get banner for specific placement
 Braze.getBanner("sample_placement_id").then(banner => {
 if (banner) {
 console.log("Banner received for placement:", banner.placementId);
 }
 });
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

```
 | 
```
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
 // Get banner for specific placement
 braze.getBanner("sample_placement_id").then((banner) {
 if (banner != null) {
 print("Banner received for placement: ${banner.placementId}");
 }
 });
});

```
 | 

### Display content

note

Content Cards can be manually rendered with custom UI logic, whereas Banners can only be rendered with the out-of-the-box SDK methods.

#### Content Cards approach

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
8
9
10
11

```
 | 
```
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
 // Custom rendering logic
 if (card instanceof braze.ClassicCard) {
 // Render classic card
 }
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
11
12
13
14
15

```
 | 
```
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
 .replace(R.id.content_cards_container, fragment)
 .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
 when (card) {
 is ClassicCard -> {
 // Render classic card
 }
 }
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

```
 | 
```
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
 switch card {
 case let card as Braze.ContentCard.Classic:
 // Render classic card
 default:
 break
 }
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

```
 | 
```
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getCachedContentCards();
cards.forEach(card => {
 if (card.type === 'CLASSIC') {
 // Render classic card
 }
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
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
 if (card.type == 'CLASSIC') {
 // Render classic card
 }
}

```
 | 

#### Banners approach

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
braze.subscribeToBannersUpdates((banners) => {
 const banner = braze.getBanner("sample_placement_id");
 if (!banner) {
 return;
 }

 const container = document.getElementById("global-banner-container");
 braze.insertBanner(banner, container);

 if (banner.isControl) {
 container.style.display = "none";
 }
});

braze.requestBannersRefresh(["sample_placement_id"]);

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

```
 | 
```
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
// android:id="@+id/banner_view"
// android:layout_width="match_parent"
// android:layout_height="wrap_content"
// app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
 placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))

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

```
 | 
```
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
 placementId: "sample_placement_id",
 braze: braze,
 processContentUpdates: { result in
 switch result {
 case .success(let updates):
 if let height = updates.height {
 // Update height constraint
 }
 case .failure:
 break
 }
 }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])

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

```
 | 
```
// Using BrazeBannerView component
<Braze.BrazeBannerView
 placementId='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
 // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);

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

```
 | 
```
// Using BrazeBannerView widget
BrazeBannerView(
 placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
 // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);

```
 | 

### Log analytics (custom implementations)

note

Both Content Cards and Banners automatically track analytics when using their default UI components. The following examples are for custom implementations where you’re building your own UI.

#### Content Cards approach

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
// Manual impression logging required for custom implementations
cards.forEach(card => {
 braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();

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

```
 | 
```
// Manual impression logging required for custom implementations
cards.forEach { card ->
 card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()

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

```
 | 
```
// Manual impression logging required for custom implementations
for card in cards {
 card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()

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

```
 | 
```
// Manual impression logging required for custom implementations
cards.forEach(card => {
 Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);

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

```
 | 
```
// Manual impression logging required for custom implementations
for (final card in cards) {
 braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);

```
 | 

#### Banners approach

- web
 
- android
 
- swift
 
- react native
 
- flutter

important

Analytics are automatically tracked when using insertBanner(). Manual logging should not be used when using insertBanner().

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
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);

```
 | 

important

Analytics are automatically tracked when using BannerView. Manual logging should not be used when using BannerView.

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
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);

```
 | 

important

Analytics are automatically tracked when using BannerUIView. Manual logging should not be used for default BannerUIView.

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

```
 | 
```
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
 guard let banner = banner else { return }

 // Log impression
 banner.context?.logImpression()

 // Log click (with optional buttonId)
 banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView

```
 | 

important

Analytics are automatically tracked when using BrazeBannerView. No manual logging required.

```

1
2
3
4
5

```
 | 
```
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView

```
 | 

important

Analytics are automatically tracked when using BrazeBannerView. No manual logging required.

```

1
2
3
4
5

```
 | 
```
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView

```
 | 

### Getting properties

#### Content Cards approach

- web
 
- android
 
- swift
 
- react native
 
- flutter

```

1
2
3

```
 | 
```
cards.forEach(card => {
 console.log("Card id:", card.id, "Extras:", card.extras);
});

```
 | 

```

1
2
3

```
 | 
```
cards.forEach { card ->
 Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}

```
 | 

```

1
2
3

```
 | 
```
for card in cards {
 print("Card id: \(card.id) Extras: \(card.extras)")
}

```
 | 

```

1
2
3

```
 | 
```
cards.forEach(card => {
 console.log("Card id:", card.id, "Extras:", card.extras);
});

```
 | 

```

1
2
3

```
 | 
```
for (final card in cards) {
 print("Card id: ${card.id} Extras: ${card.extras}");
}

```
 | 

#### Banners approach

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

```
 | 
```
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
 return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);

```
 | 

```

1
2
3
4

```
 | 
```
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
 Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}

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
braze.banners.getBanner(for: "sample_placement_id") { banner in
 guard let banner = banner else { return }

 print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}

```
 | 

```

1
2
3
4

```
 | 
```
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
 console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}

```
 | 

```

1
2
3
4

```
 | 
```
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
 print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}

```
 | 

### Handling control groups

#### Content Cards approach

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
cards.forEach(card => {
 if (card.isControl) {
 // Logic for control cards ie. don't display but log analytics
 } else {
 // Logic for cards ie. render card
 }
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

```
 | 
```
cards.forEach { card ->
 if (card.isControl) {
 // Logic for control cards ie. don't display but log analytics
 } else {
 // Logic for cards ie. render card
 }
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

```
 | 
```
for card in cards {
 if card.isControl {
 // Logic for control cards ie. don't display but log analytics
 } else {
 // Logic for cards ie. render card
 }
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

```
 | 
```
cards.forEach(card => {
 if (card.isControl) {
 // Logic for control cards ie. don't display but log analytics
 } else {
 // Logic for cards ie. render card
 }
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

```
 | 
```
for (final card in cards) {
 if (card.isControl) {
 // Logic for control cards ie. don't display but log analytics
 } else {
 // Logic for cards ie. render card
 }
}

```
 | 

#### Banners approach

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
8
9
10
11
12
13
14
15
16

```
 | 
```
braze.subscribeToBannersUpdates((banners) => {
 const banner = braze.getBanner("sample_placement_id");
 if (!banner) {
 return;
 }

 const container = document.getElementById("global-banner-container");

 // Always call insertBanner to track impression (including control)
 braze.insertBanner(banner, container);

 // Hide if control group
 if (banner.isControl) {
 container.style.display = "none";
 }
});

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
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
 placementId = "sample_placement_id"
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

```
 | 
```
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
 placementId: "sample_placement_id",
 braze: braze
)

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
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
 placementId='sample_placement_id'
/>

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
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
 placementId: "sample_placement_id",
)

```
 | 

## Limitations

When migrating from Content Cards to Banners, be aware of the following limitations:

### Migrating triggered messages

Banners only support scheduled delivery campaigns. To migrate a message that was previously API-triggered or action-based, convert it to segment-based targeting:

- Example: Instead of triggering a “Complete Profile” card with the API, create a segment for users who signed up in the last 7 days but have not completed their profile.
 
- Real-time eligibility: Users qualify or disqualify for the Banner instantly at each refresh based on their segment membership.

### Feature differences

 Feature | 
 Content Cards | 
 Banners | 

 Content Structure | 
   | 
   | 

 Multiple cards in feed | 
 ✅ Supported | 
 ✅ Can create multiple placements to achieve carousel-like implementation. Only one banner is returned per placement. | 

 Multiple placements | 
 N/A | 
 ✅ Multiple placements supported | 

 Card types (Classic, Captioned, Image Only) | 
 ✅ Multiple predefined types | 
 ✅ Single HTML-based banner (more flexible) | 

 Content Management | 
   | 
   | 

 Drag-and-drop editor | 
 ❌ Requires developer for customization | 
 ✅ Marketers can create/update without engineering | 

 Custom HTML/CSS | 
 ❌ Limited to card structure | 
 ✅ Full HTML/CSS support | 

 Key-value pairs for customization | 
 ✅ Required for advanced customization | 
 ✅ Strongly-typed key-value pairs called “properties” for advanced customization | 

 Message extras | 
 ✅ Supported | 
 ❌ Not currently supported | 

 Persistence & Expiration | 
   | 
   | 

 Card expiration | 
 ✅ Supported (30-day limit) | 
 ✅ Supported (no expiration limit) | 

 True persistence | 
 ❌ 30-day maximum | 
 ✅ Unlimited persistence | 

 Display & Targeting | 
   | 
   | 

 Feed UI | 
 ✅ Default feed available | 
 ❌ Placement-based only | 

 Context-specific placement | 
 ❌ Feed-based | 
 ✅ Native placement support | 

 Prioritization | 
 ❌ Requires custom logic | 
 ✅ Native prioritization | 

 User Interaction | 
   | 
   | 

 Manual dismissal | 
 ✅ Supported | 
 ✅ Supported | 

 Re-eligibility after dismissal | 
 ❌ Requires custom filters or campaign logic | 
 ✅ Default waiting period | 

 Pinned cards | 
 ✅ Supported | 
 N/A | 

 Analytics | 
   | 
   | 

 Automatic analytics (default UI) | 
 ✅ Supported | 
 ✅ Supported | 

 Priority Sorting | 
 ❌ Not supported | 
 ✅ Supported | 

 Content Updates | 
   | 
   | 

 Liquid templating refresh | 
 ❌ Once per card at send/launch | 
 ✅ Refreshes on every refresh | 

 Eligibility refresh | 
 ❌ Once per card at send/launch | 
 ✅ Refreshes on every session | 

### Product limitations

- Up to 25 active messages per placement.
 
- Up to 10 placement IDs per refresh request; requests beyond this are truncated.

### SDK limitations

- Banners are not currently supported on .NET MAUI (Xamarin), Cordova, Unity, Vega, or TV platforms.
 
- Make sure you’re using the minimum SDK versions listed in the prerequisites.

## Related articles

- Banner placements
 
- Tutorial: Displaying a Banner by Placement ID
 
- Banner analytics
 
- Banner FAQ

- 

New Stuff!
