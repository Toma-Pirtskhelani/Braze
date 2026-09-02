---
url: https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed
slug: docs__developer_guide__content_cards__customizing_cards__feed
title: "Customize the feed for Content Cards"
description: "This article covers Content Card feed customization options."
section: developer_guide/content_cards
fetched: 2026-09-02
evidence: company-own (technical)
---
# Customize the feed for Content Cards

A Content Card feed is the sequence of Content Cards in your mobile or web applications. This article covers configuring when the feed is refreshed, the order of the cards, managing multiple feeds, and “empty feed” error messages. For the full list of content card types, see About Content Cards.

## About the session lifecycle

A session refers to the period of time the Braze SDK tracks user activity in your app after it’s launched. You can also force a new session by calling the changeUser() method.

- web
 
- android
 
- swift

By default, a session starts when you first call braze.openSession(). The session will remain active for up to 30 minutes of inactivity (unless you change the default session timeout or the user closes the app.

note

If you’ve set up the activity lifecycle callback for Android, Braze will automatically call openSession() and closeSession() for each activity in your app.

By default, a session starts when openSession() is first called. If your app goes to the background and then returns to the foreground, the SDK will check if more than 10 seconds have passed since the session started (unless you change the default session timeout). If so, a new session will begin. Keep in mind that if the user closes your app while it’s in the background, session data may not be sent to Braze until they reopen the app.

Calling closeSession() will not immediately end the session. Instead, it will end the session after 10 seconds if openSession() isn’t called again by the user starting another activity.

By default, a session starts when you call Braze.init(configuration:). This occurs when the UIApplicationWillEnterForegroundNotification notification is triggered, meaning the app has entered the foreground.

If your app goes to the background, UIApplicationDidEnterBackgroundNotification is triggered. The app does not remain in an active session while in the background. When your app returns to the foreground, the SDK compares the time elapsed since the session started against the session timeout (unless you change the default session timeout). If the time since the session started exceeds the timeout period, a new session begins.

## Refreshing the feed

### Automatic refresh

By default, the Content Card feed will automatically refresh when:

- A new session is started
 
- The default Content Card feed is closed and reopened after more than 60 seconds have passed since the last refresh.

tip

To dynamically show up-to-date Content Cards without manually refreshing, select At first impression during card creation. These cards will be refreshed when they are available.

### Manual refresh

To manually refresh the feed at a specific time:

- web
 
- android
 
- swift

Request a manual refresh of Braze Content Cards from the Web SDK at any time by calling requestContentCardsRefresh().

You can also call getCachedContentCards to get all currently available cards from the last Content Cards refresh.

```

1
2
3
4
5

```
 | 
```
import * as braze from "@braze/web-sdk";

function refresh() {
 braze.requestContentCardsRefresh(); 
}

```
 | 

To open Content Card links in a new browser tab instead of the same tab, set openCardsInNewTab: true in your Web SDK initialization options. For more information about initialization options, see Web SDK repository guide.

Request a manual refresh of Braze Content Cards from the Android SDK at any time by calling requestContentCardsRefresh.

- java
 
- kotlin

```

1

```
 | 
```
Braze.getInstance(context).requestContentCardsRefresh();

```
 | 

```

1

```
 | 
```
Braze.getInstance(context).requestContentCardsRefresh()

```
 | 

Request a manual refresh of Braze Content Cards from the Swift SDK at any time by calling the requestRefresh method on the Braze.ContentCards class:

- swift
 
- objective-c

In Swift, Content Cards can be refreshed either with an optional completion handler or with an asynchronous return using the native Swift concurrency APIs.

#### Completion handler

```

1
2
3

```
 | 
```
AppDelegate.braze?.contentCards.requestRefresh { result in
 // Implement completion handler
}

```
 | 

#### Async/Await

```

1

```
 | 
```
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()

```
 | 

```

1
2
3

```
 | 
```
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
 // Implement completion handler
}];

```
 | 

### Full sync vs. partial sync

The Braze SDK uses two types of sync when retrieving Content Cards from the server:

- Full sync: Pulls down all Content Cards a user is eligible for. Full syncs occur automatically every 7 days or whenever changeUser() is called.
 
- Partial sync: Pulls down only new Content Cards since the last request. If the user isn’t eligible for any new cards, the response returns zero cards. Partial syncs occur each time requestContentCardsRefresh() is called (unless 7 days have passed since the last full sync, in which case a full sync is triggered instead).

Partial syncs reduce server load and device battery usage. Content Cards that have already been received are stored locally on the SDK, so users will continue to see their available cards even when a partial sync returns zero new cards.

### Rate limit

Braze uses a token bucket algorithm to enforce the following rate limits:

- Up to 5 refresh calls per device, shared across users and calls to openSession()
 
- After reaching the limit, a new call becomes available every 180 seconds (3 minutes)
 
- The system will hold up to five calls for you to use at any time
 
- subscribeToContentCards() will still return cached cards even when rate-limited

important

The Braze SDK also applies rate limits for performance and reliability. Keep this in mind when running automated tests or performing manual QA. See Braze SDK rate limits for more information.

## Customizing displayed card order

You can change the order in which your Content Cards are displayed. This allows you to fine tune the user experience by prioritizing certain types of content, such as time-sensitive promotions.

- web
 
- android
 
- swift

Customize the display order of Content Cards in your feed by using the filterFunction param of showContentCards():. For example:

```

1
2
3

```
 | 
```
braze.showContentCards(null, (cards) => {
 return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});

```
 | 

- android view controller
 
- jetpack compose

The ContentCardsFragment relies on a IContentCardsUpdateHandler to handle any sorting or modifications of Content Cards before they are displayed in the feed. A custom update handler can be set via setContentCardUpdateHandler on your ContentCardsFragment.

The following is the default IContentCardsUpdateHandler and can be used as a starting point for customization:

Show Java example

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
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63

```
 | 
```
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

 // Interface that must be implemented and provided as a public CREATOR
 // field that generates instances of your Parcelable class from a Parcel.
 public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
 public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
 return new DefaultContentCardsUpdateHandler();
 }

 public DefaultContentCardsUpdateHandler[] newArray(int size) {
 return new DefaultContentCardsUpdateHandler[size];
 }
 };

 @Override
 public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
 List<Card> sortedCards = event.getAllCards();
 // Sort by pinned, then by the 'updated' timestamp descending
 // Pinned before non-pinned
 Collections.sort(sortedCards, new Comparator<Card>() {
 @Override
 public int compare(Card cardA, Card cardB) {
 // A displays above B
 if (cardA.getIsPinned() && !cardB.getIsPinned()) {
 return -1;
 }

 // B displays above A
 if (!cardA.getIsPinned() && cardB.getIsPinned()) {
 return 1;
 }

 // At this point, both A & B are pinned or both A & B are non-pinned
 // A displays above B since A is newer
 if (cardA.getUpdated() > cardB.getUpdated()) {
 return -1;
 }

 // B displays above A since A is newer
 if (cardA.getUpdated() < cardB.getUpdated()) {
 return 1;
 }

 // At this point, every sortable field matches so keep the natural ordering
 return 0;
 }
 });

 return sortedCards;
 }

 // Parcelable interface method
 @Override
 public int describeContents() {
 return 0;
 }

 // Parcelable interface method
 @Override
 public void writeToParcel(Parcel dest, int flags) {
 // No state is kept in this class so the parcel is left unmodified
 }
}

```
 | 

Show Kotlin example

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
48
49
50
51
52
53
54
55

```
 | 
```
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
 override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
 val sortedCards = event.allCards
 // Sort by pinned, then by the 'updated' timestamp descending
 // Pinned before non-pinned
 sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
 // A displays above B
 if (cardA.isPinned && !cardB.isPinned) {
 return@sort -1
 }

 // B displays above A
 if (!cardA.isPinned && cardB.isPinned) {
 return@sort 1
 }

 // At this point, both A & B are pinned or both A & B are non-pinned
 // A displays above B since A is newer
 if (cardA.updated > cardB.updated) {
 return@sort -1
 }

 // B displays above A since A is newer
 if (cardA.updated < cardB.updated) {
 return@sort 1
 }
 0
 })
 return sortedCards
 }

 // Parcelable interface method
 override fun describeContents(): Int {
 return 0
 }

 // Parcelable interface method
 override fun writeToParcel(dest: Parcel, flags: Int) {
 // No state is kept in this class so the parcel is left unmodified
 }

 companion object {
 // Interface that must be implemented and provided as a public CREATOR
 // field that generates instances of your Parcelable class from a Parcel.
 val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
 override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
 return DefaultContentCardsUpdateHandler()
 }

 override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
 return arrayOfNulls(size)
 }
 }
 }
}

```
 | 

tip

The ContentCardsFragment source can be found on GitHub.

To filter and sort Content Cards in Jetpack Compose, set the cardUpdateHandler parameter. For example:

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
ContentCardsList(
 cardUpdateHandler = {
 it.sortedWith { cardA, cardB ->
 // A displays above B
 if (cardA.isPinned && !cardB.isPinned) {
 return@sortedWith -1
 }
 // B displays above A
 if (!cardA.isPinned && cardB.isPinned) {
 return@sortedWith 1
 }
 // At this point, both A & B are pinned or both A & B are non-pinned
 // A displays above B since A is newer
 if (cardA.updated > cardB.updated) {
 return@sortedWith -1
 }
 // B displays above A since A is newer
 if (cardA.updated < cardB.updated) {
 return@sortedWith 1
 }
 0
 }
 }
)

```
 | 

- swift
 
- objective-c

Customize the card feed order by directly modifying the static Attributes.defaults variable.

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
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
 cards.sorted {
 if $0.pinned && !$1.pinned {
 return true
 } else if !$0.pinned && $1.pinned {
 return false
 } else {
 return $0.createdAt > $1.createdAt
 }
 }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)

```
 | 

Customization via BrazeContentCardUI.ViewController.Attributes is not available in Objective-C.

## Customizing “empty feed” message

When a user does not qualify for any Content Cards, the SDK displays an “empty feed” error message stating: “We have no updates. Please check again later.” You can customize this “empty feed” error message similar to the following:

- web
 
- android
 
- swift

The Web SDK does not support replacing the “empty feed” language programmatically. You can opt to replace it each time the feed is shown, but this is not recommended because the feed may take some time to refresh and the empty feed text won’t display immediately.

- android view system
 
- jetpack compose

If the ContentCardsFragment determines that the user does not qualify for any Content Cards, it displays the empty feed error message.

A special adapter, the EmptyContentCardsAdapter, replaces the standard ContentCardAdapter to display this error message. To set the custom message itself, override the string resource com_braze_feed_empty.

The style used to display this message can be found via Braze.ContentCardsDisplay.Empty and is reproduced in the following code snippet:

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
<style name="Braze.ContentCardsDisplay.Empty">
 <item name="android:lineSpacingExtra">1.5dp</item>
 <item name="android:text">@string/com_braze_feed_empty</item>
 <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
 <item name="android:textSize">18.0sp</item>
 <item name="android:gravity">center</item>
 <item name="android:layout_height">match_parent</item>
 <item name="android:layout_width">match_parent</item>
</style>

```
 | 

For more information on customizing Content Card style elements, see Customizing style.

To customize the “empty feed” error message with Jetpack Compose, you can pass in an emptyString to ContentCardsList. You can also pass in emptyTextStyle to ContentCardListStyling to further customize this message.

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
ContentCardsList(
 emptyString = "No messages today",
 style = ContentCardListStyling(
 emptyTextStyle = TextStyle(...)
 )
)

```
 | 

If you have a Composable you would like to display instead, you can pass in emptyComposable to ContentCardsList. If emptyComposable is specified, the emptyString will not be used.

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
ContentCardsList(
 emptyComposable = {
 Image(
 painter = painterResource(id = R.drawable.noMessages),
 contentDescription = "No messages"
 )
 }
)

```
 | 

- swift
 
- objective-c

Customize the view controller empty state by setting the related Attributes.

```

1
2
3
4

```
 | 
```
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel

```
 | 

Change the language that appears automatically in empty Content Card feeds by redefining the localizable Content Card strings in your app’s ContentCardsLocalizable.strings file.

note

If you want to update this message in different locale languages, find the corresponding language in the Resources folder structure with the string ContentCardsLocalizable.strings.

## Implementing multiple feeds

Content Cards can be filtered on your app so that only specific cards are displayed, enabling you to have multiple Content Card feeds for different use cases. For example, you can maintain both a transactional feed and a marketing feed. To accomplish this, create different categories of Content Cards by setting key-value pairs in the Braze dashboard. Then, create feeds in your app or site that treat these types of Content Cards differently, filtering out some types and displaying others.

### Step 1: Set key-value pairs on cards

When creating a Content Card campaign, set key-value pair data on each card. You will use this key-value pair to categorize cards. Key-value pairs are stored in the extras property in the card’s data model.

For this example, we’ll set a key-value pair with the key feed_type that will designate which Content Card feed the card should be displayed in. The value will be whatever your custom feeds will be, such as home_screen or marketing.

### Step 2: Filter Content Cards

Once key-value pairs have been assigned, create a feed with logic that will display the cards you wish to display and filter cards of other types. In this example, we will only display cards with a matching key-value pair of feed_type: "Transactional".

- web
 
- android
 
- swift

The following example will show the Content Cards feed for Transactional type cards:

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

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
 braze.showContentCards(null, function(cards) {
 return cards.filter((card) => card.extras["feed_type"] === feed_type);
 });
}

```
 | 

Then, you can set up a toggle for your custom feed:

```

1
2
3
4

```
 | 
```
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
 showCardsByFeedType("Transactional"); 
};

```
 | 

For more information, see the SDK method documentation.

- android view system
 
- jetpack compose

By default, the Content Card feed is displayed in a ContentCardsFragment and IContentCardsUpdateHandler returns a list of cards to display after receiving a ContentCardsUpdatedEvent from the Braze SDK. However, it only sorts cards and doesn’t handle any filtering directly.

#### Step 2.1: Create a custom handler

You can filter out Content Cards by implementing a custom IContentCardsUpdateHandler using the key-value pairs set by Card.getExtras() in the dashboard, then modifying it to remove any cards from the list that don’t match the value for feed_type you set earlier.

Show Java example

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

```
 | 
```
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
 return new IContentCardsUpdateHandler() {
 @Override
 public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
 // Use the default card update handler for a first
 // pass at sorting the cards. This is not required
 // but is done for convenience.
 final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

 final Iterator<Card> cardIterator = cards.iterator();
 while (cardIterator.hasNext()) {
 final Card card = cardIterator.next();

 // Make sure the card has our custom KVP
 // from the dashboard with the key "feed_type"
 if (card.getExtras().containsKey("feed_type")) {
 final String feedType = card.getExtras().get("feed_type");
 if (!desiredFeedType.equals(feedType)) {
 // The card has a feed type, but it doesn't match
 // our desired feed type, remove it.
 cardIterator.remove();
 }
 } else {
 // The card doesn't have a feed
 // type at all, remove it
 cardIterator.remove();
 }
 }

 // At this point, all of the cards in this list have
 // a feed type that explicitly matches the value we put
 // in the dashboard.
 return cards;
 }
 };
}

```
 | 

Show Kotlin example

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

```
 | 
```
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
 return IContentCardsUpdateHandler { event ->
 // Use the default card update handler for a first
 // pass at sorting the cards. This is not required
 // but is done for convenience.
 val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

 val cardIterator = cards.iterator()
 while (cardIterator.hasNext()) {
 val card = cardIterator.next()

 // Make sure the card has our custom KVP
 // from the dashboard with the key "feed_type"
 if (card.extras.containsKey("feed_type")) {
 val feedType = card.extras["feed_type"]
 if (desiredFeedType != feedType) {
 // The card has a feed type, but it doesn't match
 // our desired feed type, remove it.
 cardIterator.remove()
 }
 } else {
 // The card doesn't have a feed
 // type at all, remove it
 cardIterator.remove()
 }
 }

 // At this point, all of the cards in this list have
 // a feed type that explicitly matches the value we put
 // in the dashboard.
 cards
 }
}

```
 | 

#### Step 2.2: Add it to a fragment

After you’ve created a IContentCardsUpdateHandler, create a ContentCardsFragment that uses it. This custom feed can be used like any other ContentCardsFragment. In the different parts of your app, display different Content Card feeds based on the key provided on the dashboard. Each ContentCardsFragment feed will have a unique set of cards displayed thanks to the custom IContentCardsUpdateHandler on each fragment.

Show Java example

```

1
2
3

```
 | 
```
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));

```
 | 

Show Kotlin example

```

1
2
3

```
 | 
```
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")

```
 | 

To filter which content cards are shown in this feed, use cardUpdateHandler. For example:

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
ContentCardsList(
 cardUpdateHandler = {
 it.filter { card ->
 card.extras["feed_type"] == "Transactional"
 }
 }
 )

```
 | 

The following example will show the Content Cards feed for Transactional type cards:

- swift
 
- objective-c

```

1
2

```
 | 
```
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }

```
 | 

To take it a step further, the cards presented in the view controller can be filtered by setting the transform property on your Attributes struct to display only the cards filtered by your criteria.

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
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
 cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)

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
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
 if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
 [transactionalCards addObject:card];
 }
}

```
 | 

- 

New Stuff!
