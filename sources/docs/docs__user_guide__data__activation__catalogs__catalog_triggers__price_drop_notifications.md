---
url: https://www.braze.com/docs/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications
slug: docs__user_guide__data__activation__catalogs__catalog_triggers__price_drop_notifications
title: "Price drop notifications"
description: "This reference article describes how to create price drop notifications in Braze catalogs."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Price drop notifications

This page covers how price drop notifications work and how you can set up and use them. With a combination of price drop notifications through Braze catalogs and a Canvas, you can notify customers when an item’s price has decreased.

## How it works

When a user triggers a custom event for an item, we’ll automatically subscribe them to receive price drop notifications for that item. When the item’s price meets your inventory rule (such as a drop larger than 50%), all subscribers will be eligible for notifications through a campaign or Canvas. However, only users who opted into notifications will receive notifications.

## Setting a custom event for price drop notifications

You’ll set up a custom event to use as a subscription event, such as a product_clicked event. This event must contain a property of the item ID (catalog item IDs). We recommend including a catalog name, but this isn’t required. You’ll also provide the name of a price field, which must be a number data type.

You can create a price drop subscription for a user and a catalog item when the following occurs:

- A selected custom event is performed by a user
 
- The custom event has a type property that includes price_drop (type must be an array)

To set both price-drop and back-in-stock notifications in the same event, you can use the type property, which must be an array. When an item has a price change that meets your price rule, we’ll look up all your users who are subscribed to that item (users who did the subscription event) and send a Braze custom event that you can use to trigger a campaign or Canvas.

The event properties are sent alongside your user, so you can template in the item details into the campaign or Canvas that sends.

## Setting up price drop notifications

Follow these steps to set up price drop notifications in a specific catalog.

- Go to your catalog and select the Settings tab.
 
- Select the Price Drop toggle.
 
- If the global catalog settings have not been configured, you’ll be prompted to set up the custom events and properties that will be used to trigger notifications. 

 Field | 
 Description | 

 Fallback catalog | 
 The catalog used for the subscription if there isn’t a catalog_name property in the custom event. | 

 Custom event for subscribing | 
 The custom event used to subscribe a user for catalog notifications. When this event occurs, the user who performed the event will be subscribed. | 

 Custom event for unsubscribing | 
 The custom event used to unsubscribe a user from notifications. This event is optional. If the user doesn’t perform this event, they’ll be unsubscribed after 90 days or when the price drop event triggers, whichever occurs first. | 

 Item ID event property | 
 The property on the earlier in this section custom event used to determine the item for a subscription or unsubscription. This property on the custom event should contain an item ID that exists in a catalog. The custom event must contain a catalog_name property to specify which catalog this item is in. | 

Here’s an example custom event:

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
{
 "events": [
 {
 "external_id": "<external_id>",
 "name": "subscription",
 "time": "2024-04-15T19:22:28Z",
 "properties": {
 "id": "shirt-xl",
 "catalog_name": "on_sale_products",
 "type": ["price_drop", "back_in_stock"]
 }
 }
 ]
}

```
 | 

- Select Save, and continue to the next section to set up notification rules.

### Setting up notification rules

- Go to your catalog’s Settings page.
 
- 
 
For Notification rules, select from the following options:

- Notify all subscribed users: Notify all customers who are waiting when the item’s price drops.
 
- Set notification limits: Notify a specified number of customers per your configured notification period. Braze will notify the specified numbers of customers in increments until there are no more customers to notify, or until the item’s price goes back up. Your notification rate cannot exceed notifying 10,000 users per minute.

- Set the Price field in catalog. This is the catalog field that will be used to determine the item’s price. It must be a number type.
 
- Set the Price drop rule. This is the logic used to determine if a notification should be sent. A price drop can be configured as a percentage price change or by the change in value for the price field.
 
- Select Save settings.

important

Notification rules in these settings do not replace Canvas notification settings, such as Quiet Hours.

## Using price drop notifications in a Canvas

After setting up the price drop notifications in a catalog, follow these steps to use these notifications for a Canvas.

- Set up an action-based Canvas.
 
- Select Perform Price Drop Event as the trigger.
 
- Select the name of the catalog with the price drop notifications.
 
- Continue setting up your Canvas as you would.

Now, your customers will be notified when an item’s price drops.

### Using Liquid

To template in details about the catalog item that has dropped in price, you can use the context Liquid tag to access the item_id.

Using {{context.${catalog_update}.item_id}} will return the ID of the item that dropped in price. {{context.${catalog_update}.previous_value}} will return the price value of the item before the update, and {{context.${catalog_update}.new_value}} will return the new price value after the update.

Use the Liquid tag {% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %} at the top of your message, then use {{items[0].<field_name>}} to access data about that item throughout the message.

important

Canvas entry properties are part of Canvas context variables. This means canvas_entry_properties is referenced as context. Each context variable includes a name, data type, and a value that can include Liquid. Currently, canvas_entry_properties are backwards compatible. For more details, see Context and Canvas context object.

tip

To pull in images for catalog trigger items, your catalog must include a field named image_url. You can then reference it using {{ items[0].image_url }}.

## Considerations

- Users are subscribed for 90 days. If an item does not drop in price in 90 days, the user is removed from the subscription.
 
- When using the Notify all subscribed users notification rule, Braze will notify 100,000 users over 10 minutes.
 
- Braze supports up to 50,000 updated items daily that are eligible for triggering price drop notifications. You can have up to 100 million active subscriptions at a given time, where each subscription represents a user profile subscribed to watch a catalog item.

- 

New Stuff!
