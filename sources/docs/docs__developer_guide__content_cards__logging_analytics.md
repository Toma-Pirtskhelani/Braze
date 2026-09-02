---
url: https://www.braze.com/docs/developer_guide/content_cards/logging_analytics
slug: docs__developer_guide__content_cards__logging_analytics
title: "Log analytics"
description: "This article covers how to manually log impressions, clicks, dismissals, and handle on-click behavior for your customized Content Cards."
section: developer_guide/content_cards
fetched: 2026-09-02
evidence: company-own (technical)
---
# Log analytics

When building a custom UI for Content Cards, you must manually log analytics like impressions, clicks, and dismissals, as this is only handled automatically for default card models. Logging these events is a standard part of a Content Card integration and is essential for accurate campaign reporting and billing. To do this, populate your custom UI with data from the Braze data models and then manually log the events. Once you understand how to log analytics, you can see common ways Braze customers create custom Content Cards.

## Logging analytics

When implementing your custom Content Cards, you can parse the Content Card objects and extract their payload data such as title, cardDescription, and imageUrl. Then, you can use the resulting model data to populate your custom UI.

To obtain the Content Card data models, subscribe to Content Card updates. There are two properties to pay particular attention to:

- id: Represents the Content Card ID string. This is the unique identifier used to log analytics from custom Content Cards.
 
- extras: Encompasses all the key-value pairs from the Braze dashboard.

All properties outside of id and extras are optional to parse for custom Content Cards. For more information on the data model, see each platform’s integration article: Android, iOS, Web.

- web
 
- android
 
- swift
 
- react native

Register a callback function to subscribe for updates when cards are refreshed.

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
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
 const cards = updates.cards;
// For example:
 cards.forEach(card => {
 if (card.isControl) {
 // Do not display the control card, but remember to call `logContentCardImpressions([card])`
 }
 else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
 // Use `card.title`, `card.imageUrl`, etc.
 }
 else if (card instanceof braze.ImageOnly) {
 // Use `card.imageUrl`, etc.
 }
 })
});

braze.openSession();

```
 | 

note

Content Cards will only refresh on session start if a subscribe request is called before openSession(). You can always choose to manually refresh the feed as well.

- java
 
- kotlin

### Step 1: Create a private subscriber variable

To subscribe to card updates, first declare a private variable in your custom class to hold your subscriber:

```

1
2

```
 | 
```
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;

```
 | 

### Step 2: Subscribe to updates

Next, add the following code to subscribe to Content Card updates from Braze, typically inside of your custom Content Cards activity’s Activity.onCreate():

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

```
 | 
```
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
 @Override
 public void trigger(ContentCardsUpdatedEvent event) {
 // List of all Content Cards
 List<Card> allCards = event.getAllCards();

 // Your logic below
 }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();

```
 | 

### Step 3: Unsubscribe

We also recommend unsubscribing when your custom activity moves out of view. Add the following code to your activity’s onDestroy() lifecycle method:

```

1

```
 | 
```
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);

```
 | 

### Step 1: Create a private subscriber variable

To subscribe to card updates, first declare a private variable in your custom class to hold your subscriber:

```

1

```
 | 
```
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null

```
 | 

### Step 2: Subscribe to updates

Next, add the following code to subscribe to Content Card updates from Braze, typically inside of your custom Content Cards activity’s Activity.onCreate():

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
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
 // List of all Content Cards
 val allCards = event.allCards

 // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)

```
 | 

### Step 3: Unsubscribe

We also recommend unsubscribing when your custom activity moves out of view. Add the following code to your activity’s onDestroy() lifecycle method:

```

1

```
 | 
```
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)

```
 | 

To access the Content Cards data model, call contentCards.cards on your braze instance.

- swift
 
- objective-c

```

1

```
 | 
```
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards

```
 | 

note

Reading contentCards.cards, contentCards.unviewedCards, or contentCards.lastUpdate blocks the calling thread until the SDK has completed its post-initialization operations. Use the non-blocking getters in Non-blocking snapshot accessors for main-thread or latency-sensitive contexts.

Additionally, you can also maintain a subscription to observe for changes in your Content Cards. You can do so in one of two ways:

- Maintaining a cancellable; or
 
- Maintaining an AsyncStream.

### Cancellable

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
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
 // Implement your completion handler to respond to updates in `contentCards`.
}

```
 | 

### AsyncStream

```

1

```
 | 
```
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream

```
 | 

### Non-blocking snapshot accessors

Use these methods to read the current cached state without blocking the calling thread. Each completion handler is always delivered on the main thread.

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
// All cached cards.
AppDelegate.braze?.contentCards.getCachedContentCards { cards in
 // Use `cards` here.
}

// Unviewed cards only (excludes control cards).
AppDelegate.braze?.contentCards.getUnviewedCards { cards in
 // Use `cards` here.
}

// Date of the last server sync for the current user (nil until the first sync completes).
AppDelegate.braze?.contentCards.getLastUpdate { date in
 // Use `date` here.
}

```
 | 

```

1

```
 | 
```
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;

```
 | 

Additionally, if you wish to maintain a subscription to your content cards, you can call subscribeToUpdates:

```

1
2
3
4

```
 | 
```
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
 // Implement your completion handler to respond to updates in `contentCards`.
}];

```
 | 

To read the current cached state without blocking the calling thread, use the following methods. Each completion handler is delivered on the main thread.

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
// All cached cards.
[AppDelegate.braze.contentCards getCachedContentCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
 // Use `cards` here.
}];

// Unviewed cards only (excludes control cards).
[AppDelegate.braze.contentCards getUnviewedCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
 // Use `cards` here.
}];

// Date of the last server sync for the current user (nil until the first sync completes).
[AppDelegate.braze.contentCards getLastUpdateWithCompletion:^(NSDate * _Nullable date) {
 // Use `date` here.
}];

```
 | 

To listen for updates, subscribe to Content Card update events:

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
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
 const cards = update.cards;
 cards.forEach(card => {
 if (card.isControl) {
 // Do not display the control card, but remember to log an impression
 } else {
 // Use card.title, card.cardDescription, card.image, etc.
 }
 });
});

```
 | 

To get the most recently cached Content Card data:

```

1
2
3

```
 | 
```
import Braze from "@braze/react-native-sdk";

const cachedCards = await Braze.getCachedContentCards();

```
 | 

To request a manual refresh of Content Cards from Braze servers:

```

1

```
 | 
```
Braze.requestContentCardsRefresh();

```
 | 

## Logging events

Logging valuable metrics like impressions, clicks, and dismissals is quick and simple. Set a custom click listener to manually handle these analytics.

- web
 
- android
 
- swift
 
- react native

Log impression events when cards are viewed by users using logContentCardImpressions:

```

1
2
3

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);

```
 | 

Log card click events when users interact with a card using logContentCardClick:

```

1
2
3

```
 | 
```
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);

```
 | 

The BrazeManager can reference Braze SDK dependencies such as the Content Card objects array list to get the Card to call the Braze logging methods. Use the ContentCardable base class to easily reference and provide data to the BrazeManager.

To log an impression or click on a card, call Card.logClick() or Card.logImpression() respectively.

You can manually log or set a Content Card as “dismissed” to Braze for a particular card with isDismissed. If a card is already marked as dismissed, it cannot be marked as dismissed again.

To create a custom click listener, create a class that implements IContentCardsActionListener and register it with BrazeContentCardsManager. Implement the onContentCardClicked() method, which will be called when the user clicks a Content Card. Then, instruct Braze to use your Content Card click listener.

- java
 
- kotlin

For example:

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
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
 @Override
 public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
 return false;
 }

 @Override
 public void onContentCardDismissed(Context context, Card card) {

 }
});

```
 | 

For example:

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
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
 override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
 return false
 }

 override fun onContentCardDismissed(context: Context, card: Card) {

 }
}

```
 | 

important

To handle control variant Content Cards in your custom UI, pass in your com.braze.models.cards.Card object, then call the logImpression method as you would with any other Content Card type. The object will implicitly log a control impression to inform our analytics of when a user would have seen the control card.

Implement the BrazeContentCardUIViewControllerDelegate protocol and set your delegate object as the delegate property of your BrazeContentCardUI.ViewController. This delegate will handle passing the data of your custom object back to Braze to be logged. For an example, see Content Cards UI tutorial.

- swift
 
- objective-c

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
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
 _ controller: BrazeContentCardUI.ViewController,
 shouldProcess clickAction: Braze.ContentCard.ClickAction,
 card: Braze.ContentCard
 ) -> Bool {
 // Intercept the content card click action here.
 return true
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
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
 shouldProcess:(NSURL *)url
 card:(BRZContentCardRaw *)card {
 // Intercept the content card click action here.
 return YES;
}

```
 | 

important

To handle control variant Content Cards in your custom UI, pass in your Braze.ContentCard.Control object, then call the logImpression method as you would with any other Content Card type. The object will implicitly log a control impression to inform our analytics of when a user would have seen the control card.

Log impression events when cards are viewed by users:

```

1

```
 | 
```
Braze.logContentCardImpression(card.id);

```
 | 

Log card click events when users interact with a card:

```

1

```
 | 
```
Braze.logContentCardClicked(card.id);

```
 | 

Log dismissal events when a user dismisses a card:

```

1

```
 | 
```
Braze.logContentCardDismissed(card.id);

```
 | 

## Handling on-click behavior

- web
 
- android
 
- swift
 
- react native

When a user clicks a Content Card in a custom feed, the on-click behavior (such as navigating to a URL, deep linking, or logging a custom event) is not handled automatically. Use handleBrazeAction to process the card’s URL and execute the configured on-click action, including Braze actions (brazeActions:// URLs).

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
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
 // Log the click
 braze.logContentCardClick(card);

 // Handle the on-click behavior
 if (card.url) {
 braze.handleBrazeAction(card.url);
 }
}

```
 | 

 Parameter | 
 Description | 

 url | 
 A valid URL, or a valid Braze action URL with the scheme brazeActions://. | 

 openLinkInNewTab | 
 (Optional) Whether the URL should open in a new tab. Defaults to false. | 

important

If you don’t call handleBrazeAction(), on-click behaviors configured in the Braze dashboard (such as “Log Custom Event” or “Navigate to URL”) won’t execute for cards displayed in a custom feed.

On-click behavior is handled automatically by the default Content Cards UI. For custom implementations, use the IContentCardsActionListener interface described in Logging analytics.

On-click behavior is handled automatically by the default Content Cards UI. For custom implementations, use the BrazeContentCardUIViewControllerDelegate protocol described in Logging analytics.

When a user clicks a Content Card in a custom feed, the on-click behavior is not handled automatically. After logging the click with Braze.logContentCardClicked(cardId), call Braze.processContentCardClickAction(cardId) to process deep links, URLs, and brazeActions:// actions. For method reference, see React Native Content Cards.

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

function onCardPress(card) {
 Braze.logContentCardClicked(card.id);

 if (card.url) {
 Braze.processContentCardClickAction(card.id);
 }
}

```
 | 

important

If you don’t call processContentCardClickAction(), on-click behaviors configured in the Braze dashboard won’t execute for cards in a custom feed.

## Unique dismissals higher than unique impressions

If Unique Dismissals exceeds Unique Impressions, your custom Content Card integration logged dismissals without logging impressions for those same cards. Braze’s default Content Card UI logs both automatically, so this mismatch appears only when you use a custom UI.

Log an impression each time you display a card, and log a dismissal when the user dismisses it. For method names and examples, see the following platform sections.

## Missing Content Cards analytics

If Content Cards appear correctly in your app but you consistently do not receive any analytics (impressions, clicks, and so on), it is likely an SDK integration issue.

- Custom Content Card views (Android, iOS, Web): The default Braze UI logs impressions and clicks automatically on all platforms. If you are using a custom Content Card view or implementation, you must call the appropriate logging methods explicitly within your application. See Log analytics for your platform. For custom Web implementations specifically, ensure the Braze Web SDK is loaded, check the browser console for errors, and verify that card data is being received.
 
- SDK initialization and user identification: Ensure the SDK is fully initialized before displaying cards. Events are silently dropped (not queued) if the SDK is uninitialized, in delayed initialization mode, or GDPR-disabled. The SDK does log analytics for anonymous users, but dashboard metrics like “unique daily impressions” require a resolved user identity, so call changeUser before cards are displayed where possible.

## Content Card ID

Each campaign send to a recipient generates a new Content Card ID. If the same user receives the campaign again on a later send, Braze assigns a new ID. Reference the card id when logging impressions, clicks, and dismissals in custom implementations.

- 

New Stuff!
