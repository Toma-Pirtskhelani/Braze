---
url: https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/user_update
slug: docs__user_guide__messaging__canvas__canvas_components__user_update
title: "User Update"
description: "This reference article covers the User Update component and how to use it in your Canvases."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# User Update

The User Update component allows you to update a user’s attributes, events, and purchases in a JSON editor, so there’s no need to include sensitive information like API keys.

## How this component works

When using this component in your Canvas, updates don’t count toward your /users/track requests per minute rate limit. Instead, these updates are batched so Braze can process them more efficiently than a Braze-to-Braze webhook. Note that this component doesn’t log data points when being used to update non-billable data points (such as subscription groups).

After users enter the User Update step and it completes processing, they advance to the next step. This means any subsequent messaging that relies on these user updates is up-to-date when the next step is run.

## Creating a user update

Drag and drop the component from the sidebar, or select the plus button at the bottom of the variant or step and select User Update.

There are three options that allow you to update existing user profile information, add new information, or remove user profile information. All combined, the User Update steps in a workspace can update up to 200,000 user profiles per minute.

tip

You can also test the changes made with this component by searching for a user and applying the change to them. This will update the user.

## Updating custom attributes

To update or remove a custom attribute, select an attribute name from your list of attributes and enter the value.

## Removing custom attributes

To remove a custom attribute, select an attribute name using the dropdown. You can switch to the advanced JSON editor to further edit.

### Increasing and decreasing values

The User Update step can increase or decrease an attribute value. Select the attribute, select Increment By or Decrement By, and enter a number.

#### Track weekly progress

By incrementing a custom attribute that tracks an event, you can track the number of classes that a user has taken in a week. Using this component, the class count can reset at the start of the week and begin tracking again.

### Updating an array of objects

An array of objects is a data-rich custom attribute stored on a user’s profile. You can use it to create a history of the user’s interactions with your brand and to create segments based on a calculated field, such as purchase history or total lifetime value.

Using the Advanced JSON Editor option, you can insert JSON to add items to or remove items from this array of objects.

#### Use case: Updating a user’s wishlist

Track a user’s wishlist so you can segment or personalize based on their saved items.

- Create a custom attribute that is an array of objects, for example wishlist. Each object can include fields such as product_id, product_name, and added_at.
 
- In the User Update step, select Advanced JSON Editor. Then, in the Compose section, use the $add operation to append an item or the $remove operation to remove an item by value.

The following is an example of adding an item to the wishlist:

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
{
 "attributes": [
 {
 "wishlist": {
 "$add": [
 {
 "product_id": "SKU-123",
 "product_name": "Wireless Headphones",
 "added_at": "{{$isoTimestamp}}"
 }
 ]
 }
 }
 ]
}

```
 | 

To remove an item, use "wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] } with the same object structure so Braze can match and remove it.

#### Use case: Calculating the shopping cart total

Track when a user has items in their shopping cart, when they add new items or remove items, and what the total shopping cart value is.

- Create a custom array of objects called shopping_cart. The following example shows what this attribute may look like. Each item has a unique product_id that has additional data in its own nested array of objects, including price.

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
{
 "attributes": [
 {
 "shopping_cart": [
 {
 "total_cart_value": number,
 "shipping": number,
 "items_in_cart": number,
 "product_id": array,
 "gift": boolean,
 "discount_code": "enum",
 "timestamp": {"$time" : "{{$isoTimestamp}}"},
 }
 ]
 }
 ]
}

```
 | 

- Create a custom event named add_item_to_cart that is logged when a user adds an item to the basket.
 
- Create a Canvas that targets users who perform this custom event. Now, when a user adds an item to their cart, this Canvas is triggered. You can then target messaging directly to that user, offering coupon codes when they’ve reached a certain spend, abandoned their cart for a certain amount of time, or anything else that aligns with your use case.

The shopping_cart attribute carries the total of many custom events: the total cost of all the items, the total number of items in the cart, if the shopping cart contains a gift, and so on. This can look something like the following:

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
{
 "attributes": [
 {
 "shopping_cart": [
 {
 "total_cart_value": 22.99,
 "shipping": 4.99,
 "items_in_cart": 2,
 "product_id": ["1001", "1002"],
 "gift": true,
 "discount_code": "flashsale1000",
 "timestamp": {"$time" : "{{$isoTimestamp}}"},
 }
 ]
 }
 ]
}

```
 | 

## Setting Canvas entry property as an attribute

You can use the user update step to persist a canvas_entry_property. Let’s say you have an event that triggers when an item is added to a cart. You can store the ID of the most recent item added to cart and use that for a remarketing campaign. Use the personalization feature to retrieve a Canvas entry property and store it in an attribute.

### Personalization

To store the property of the trigger event for a Canvas as an attribute, use the personalization modal to extract and store the Canvas entry property. User Update also supports the following personalization features:

- Connected Content
 
- Content Blocks
 
- Entry properties
 
- Liquid logic (including aborting messages)
 
- Multiple attribute or event updates per object

warning

We recommend careful use of Connected Content Liquid personalization in User Update steps, as this step type has a rate limit of 200,000 requests per minute. This rate limit overrides the Canvas rate limit.

## Advanced JSON editor

Add an attribute, event, or purchase JSON object up to 65,536 characters to the JSON editor. A user’s global subscription and subscription group state can also be set.

Using the JSON editor, you can also preview and test that the user profile is updated with your changes in the Preview and test tab. You can either select a random user or search for a specific user. Then, after sending a test to a user, view the user profile using the generated link.

### Considerations

You don’t need to include sensitive data like your API key while using the JSON editor, as this is automatically provided by the platform. The following fields should not be included in the JSON editor:

- External user ID
 
- API key
 
- Braze cluster URL
 
- Fields related to push token imports

important

Canvas properties (such as the canvas_id, canvas_name, and canvas_variant_name Liquid tags) are not supported in User Update steps.

### Log custom events

Using the JSON editor, you can also log custom events. Note that this requires a timestamp in ISO format, so assigning a time and date with Liquid at the beginning is needed. Consider this example that logs an event with a time.

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
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
 "events": [
 {
 "name": "logged_user_event",
 "time": "{{timestamp}}"
 }
 ]
}

```
 | 

This next example links an event to a specific app using a custom event with optional properties and the app_id.

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
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
 "events": [
 {
 "app_id": "insert_app_id",
 "name": "rented_movie",
 "time": "{{timestamp}}",
 "properties": {
 "release": {
 "studio": "FilmStudio",
 "year": "2022"
 },
 "cast": [
 {
 "name": "Actor1"
 },
 {
 "name": "Actor2"
 }
 ]
 }
 }
 ]
}

```
 | 

### Edit subscription state

Within the JSON editor, you can also edit a user’s subscription state. For example, the following shows a user’s subscription state updated to opted_in.

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
{
 "attributes": [
 {
 "email_subscribe": "opted_in"
 }
 ]
}

```
 | 

### Update subscription groups

You can also update subscription groups using this Canvas step. The following example shows how to update one or more subscription groups.

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
{
 "attributes": [
 {
 "subscription_groups": [
 {
 "subscription_group_id": "subscription_group_identifier_1",
 "subscription_state": "subscribed"
 },
 {
 "subscription_group_id": "subscription_group_identifier_2",
 "subscription_state": "subscribed"
 },
 {
 "subscription_group_id": "subscription_group_identifier_3",
 "subscription_state": "subscribed"
 }
 ]
 }
 ]
}

```
 | 

- 

New Stuff!
