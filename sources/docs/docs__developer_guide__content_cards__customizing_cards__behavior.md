---
url: https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/behavior
slug: docs__developer_guide__content_cards__customizing_cards__behavior
title: "Customize the behavior of Content Cards"
description: "This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations."
section: developer_guide/content_cards
fetched: 2026-09-02
evidence: company-own (technical)
---
# Customize the behavior of Content Cards

This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations. For the full list of content card types, see About Content Cards.

## Key-value pairs

Braze enables you to send extra data payloads through Content Cards to user devices using key-value pairs. These can help you track internal metrics, update app content, and customize properties. Add key-value pairs using the dashboard.

note

We do not recommend sending nested JSON values as key-value pairs. Instead, flatten the JSON before sending it.

- web
 
- android
 
- swift

Key-value pairs are stored on card objects as extras. These can be used to send data down along with a card for further handling by the application. Call card.extras to access these values.

Key-value pairs are stored on card objects as extras. These can be used to send data down along with a card for further handling by the application. Call card.extras to access these values.

Key-value pairs are stored on card objects as extras. These can be used to send data down along with a card for further handling by the application. Call card.extras to access these values.

tip

It’s important that your marketing and developer teams coordinate on which key-value pairs will be used (for example, feed_type = brand_homepage), as any key-value pairs marketers input into the Braze dashboard must exactly match the key-value pairs that developers build into the app logic.

## Content Cards as supplemental content

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

The accompanying example shows a feed with a hybrid list of items that are populated using local data and Content Cards powered by Braze. With this, Content Cards can be indistinguishable alongside existing content.

### API-triggered key-value pairs

API-triggered campaigns are a good strategy to employ when a card’s values depend on external factors to determine what content to display to the user. For example, to display supplemental content, set key-value pairs using Liquid. Note that class_type should be known at set-up time.

## Content Cards as interactive content

Content Cards can be leveraged to create dynamic and interactive experiences for your users. In the accompanying example, a Content Card pop-up appears at checkout to provide users with last-minute promotions. Well-placed cards like this are a great way to give users a “nudge” toward specific user actions.

The key-value pairs for this use case include a discount_percentage set as the desired discount amount and class_type set as coupon_code. These key-value pairs allow you to filter and display type-specific Content Cards on the checkout screen. For more information on using key-value pairs to manage multiple feeds, see Customizing the default Content Card feed. 

## Content Card badges

Badges are small icons that are ideal for getting a user’s attention. Using badges to alert the user about new Content Card content can attract users back to your app and increase sessions.

### Displaying the number of unread Content Cards as a badge

You can display the number of unread Content Cards your user has as a badge on your app’s icon.

- web
 
- android
 
- swift

You can request the number of unread cards at any time by calling:

```

1

```
 | 
```
braze.getCachedContentCards().getUnviewedCardCount();

```
 | 

You can then use this information to display a badge signifying how many unread Content Cards there are. See the SDK reference docs for more information.

You can request the number of unread cards at any time by calling:

- java
 
- kotlin

```

1

```
 | 
```
Braze.getInstance(context).getContentCardUnviewedCount();

```
 | 

```

1

```
 | 
```
Braze.getInstance(context).contentCardUnviewedCount

```
 | 

You can then use this information to display a badge signifying how many unread Content Cards there are. See the SDK reference docs for more information.

The following sample uses braze.contentCards to request and display the number of unread Content Cards. After the app is closed and the user’s session ends, this code requests a card count, filtering the number of cards based on the viewed property.

Apps that have adopted the UIScene life cycle (required for apps built with Xcode 27 and later) should implement this in SceneDelegate.swift’s sceneDidEnterBackground(_:) rather than AppDelegate.swift’s applicationDidEnterBackground(_:).

- swift
 
- objective-c

```

1

```
 | 
```
func sceneDidEnterBackground(_ scene: UIScene)

```
 | 

Within this method, implement the following code, which actively updates the badge count while the user views cards during a given session:

```

1
2

```
 | 
```
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0

```
 | 

```

1

```
 | 
```
(void)sceneDidEnterBackground:(UIScene *)scene

```
 | 

Within this method, implement the following code, which actively updates the badge count while the user views cards during a given session:

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
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
 if (card.viewed == NO) {
 unreadCardCount += 1;
 }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;

```
 | 

- 

New Stuff!
