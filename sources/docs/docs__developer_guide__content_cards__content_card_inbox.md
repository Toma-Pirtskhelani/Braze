---
url: https://www.braze.com/docs/developer_guide/content_cards/content_card_inbox
slug: docs__developer_guide__content_cards__content_card_inbox
title: "Tutorial: Making an Inbox with Content Cards"
description: ""
section: developer_guide/content_cards
fetched: 2026-09-02
evidence: company-own (technical)
---
# Tutorial: Making an Inbox with Content Cards

Follow along with the sample code in this tutorial to build an inbox with Braze Content Cards.

- android
 
- swift
 
- web

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK.

## Making an inbox with Content Cards for Android (Compose)

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 2. Build a UI view

For Jetpack Compose, use a LazyColumn to display Content Cards in a scrollable list.

#### 3. Subscribe to Content Card updates

Use a DisposableEffect to manage the subscription lifecycle, ensuring proper cleanup when the composable leaves the composition.

#### 4. Build a custom inbox UI

Using the content card attributes such as title, description, and url allows you to build Content Cards to match your specific UI requirements. In this case, we’re building an inbox with Jetpack Compose’s Card and Column composables.

#### 5. Track impressions and clicks

You can log impressions and clicks using the logImpressions and logClick methods available for Content Cards.

Impressions should only be logged once when a card is viewed by the user. Use LaunchedEffect to log impressions when a card becomes visible. Note that you may need to consider the view lifecycle of your app, as well as use case, to ensure impressions are logged correctly.

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

## Making an inbox with Content Cards for Android (RecyclerView)

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 2. Build a UI view

In this tutorial, we use Android’s RecyclerView to display Content Cards, but we recommend building a UI with classes and components that suits your use case. Braze provides the UI by default, but this tutorial guides you to create a custom view to customize the appearance and behavior.

#### 3. Subscribe to Content Card updates

Use subscribeToContentCardsUpdates to allow your UI to respond when new Content Cards are available. Here, subscribers are registered and removed within the activity lifecycle hooks.

#### 4. Build a custom inbox UI

Using the Content Card attributes such as title, description, and url allows you to build Content Cards to match your specific UI requirements. In this case, we’re building an inbox with Android’s native RecyclerView.

#### 5. Track impressions and clicks

You can log impressions and clicks using the logImpressions and logClick methods available for Content Cards.

Impressions should only be logged once when a card is viewed by the user. Here, we use a naive mechanism to guard against duplicate logs with a per-card flag. Note that you may need to consider the view lifecycle of your app, as well as use case, to ensure impressions are logged correctly.

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

Before you can use this feature, you’ll need to integrate the Swift Braze SDK. You’ll also need to enable in-app messages for Swift.

## Making an inbox with Content Cards for Swift

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 2. Build a UI View

In this tutorial, we use Swift’s UITableViewController, but we recommend building a UI with classes and components that suits your use case.

#### 3. Subscribe to Content Card updates

Subscribe to the Content Cards listener to receive the latest updates, and then call requestRefresh() to request the latest Content Cards for that user.

#### 4. Build a custom inbox UI

Using the Content Card attributes such as title, description, and imageUrl allows you to build Content Cards to match your specific UI requirements. In this case, we’re building an inbox with Swift’s native table APIs.

#### 5. Track impressions and clicks

You can log impressions and clicks using the logClick(using:) and logImpression(using:) methods available for a content card.

Additionally, you can use logDismissed(using:) for dismissals.

Impressions should only be logged once when viewed by the user. Here, a naive mechanism using a Set and willDisplay is used to achieve this. Note that you may need to consider the UI lifecycle of your app, as well as use case, to ensure impressions are logged correctly.

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

Before you can use this feature, you’ll need to integrate the Web Braze SDK. However, no additional setup is required.

## Making an inbox with Content Cards for Web

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging. Optionally, you can also run Braze Web SDK methods in the console.

#### 2. Build the UI

Create a UI for the inbox page. Here, we’re building a basic HTML page, which includes a div with the id cards-list. This is used as the target container for rendering Content Cards.

#### 3. Subscribe to Content Card updates

Subscribe to the Content Cards listener to receive the latest updates, and then call requestContentCardsRefresh() to request the latest Content Cards for that user. Alternatively, call the subscriber before openSession() for an automatic refresh on session start.

#### 4. Build the inbox elements

Using the Content Card attributes such as title, description, and url allows you to display Content Cards to match your specific UI requirements.

#### 5. Track impressions and clicks

You can log impressions and clicks using the logContentCardImpressions and logContentCardClick methods available for Content Cards.

Additionally, you can use logCardDismissal for dismissals.

Impressions should only be logged once when viewed by the user. Here, an IntersectionObserver plus a Set keyed by card.id prevents duplicate logs. Note that you may need to consider the UI lifecycle of your app, as well as use case, to ensure impressions are logged correctly.

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

- 

New Stuff!
