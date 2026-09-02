---
url: https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties
slug: docs__user_guide__messaging__canvas__create_a_canvas__context_and_event_properties__canvas_persistent_entry_properties
title: "Persistent entry properties"
description: "This reference article describes how to use persistent entry properties in your Canvas to send more curated messages, and create a highly refined end-user experience...."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Persistent entry properties

When a Canvas is triggered by a custom event, purchase, or an API call, you can use metadata from the API call, custom event, or purchase event for personalization in each step in your Canvas workflow. You can use these properties to send more curated messages.

important

Persistent entry properties are an artifact of the original Canvas editor, so there are deprecated references to terms like Canvas entry properties that remain for historical reference. For the current Canvas editor, refer to Context and event properties.

To use persistent entry properties in the current Canvas editor, you must either create a new Canvas or clone an existing one to the current editor.

## Using entry properties

Entry properties can be used in action-based and API-triggered Canvases. These entry properties are defined when a Canvas is triggered by a custom event, purchase, or API call. Refer to the following articles for more information:

- Canvas entry properties object
 
- Event properties object
 
- Purchase object

Properties passed in from these objects can be referenced by using the canvas_entry_properties Liquid tag. For example, a request with "canvas_entry_properties": {"product_name": "shoes", "product_price": 79.99} could add the word “shoes” to a message by adding the Liquid {{canvas_entry_properties.${product_name}}}.

When a Canvas includes a message with the canvas_entry_properties Liquid tag, the values associated with those properties will be saved for the duration of a user’s journey in the Canvas and deleted when the user exits the Canvas. Note that Canvas entry properties are only available for reference in Liquid. To filter on the properties within the Canvas, use event property segmentation instead.

note

The Canvas entry properties object has a maximum size limit of 50 KB.

## Updating Canvas to use entry properties

If an active Canvas that previously did not include any messages that use canvas_entry_properties is edited to include canvas_entry_properties, the value corresponding to that property will not be available for users who entered the Canvas before canvas_entry_properties was added to the Canvas. The values will only be saved for users that enter the Canvas after the change is made.

For example, if you initially launched a Canvas that did not use any entry properties on November 3, then added a new property product_name to the Canvas on November 11, values for product_name would only be saved for users that entered the Canvas on November 11 onward.

In the case that a Canvas entry property is null or blank, you can abort messages using conditionals. The following code snippet is an example of how you could use Liquid to abort a message.

```

1
2
3

```
 | 
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}

```
 | 

To read more about aborting messages with Liquid, check out our Liquid documentation.

## Global Canvas entry properties

With canvas_entry_properties, you can set global properties that apply to all users or user-specific properties that only apply to the specified user. The user-specific property will supersede the global property for that user.

### Example request

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
curl -X POST \
-H 'Content-Type: application/json' \
-d '{
 "api_key": "a valid rest api key",
 "canvas_id": "the ID of your Canvas",
 "canvas_entry_properties": {
 "food_allergies": "none"
 },
 "recipients": [
 {
 "external_user_id": "Customer_123",
 "canvas_entry_properties": {
 "food_allergies": ["dairy", "soy"],
 "nutrition": {
 "calories_per_serving": 200,
 "serving_size_in_ounces": 4
 }
 }
 }
 ]
 }'

```
 | 

In this request, the global value for “food allergies” is “none”. For Customer_123, the value is “dairy”. Messages in this Canvas containing the Liquid snippet {{canvas_entry_properties.${food_allergies}}} will template with “dairy” for Customer_123 and “none” for everyone else.

## Use case

If you have a Canvas that is triggered when a user browses an item in your eCommerce site but does not add it to their cart, the first step of the Canvas might be a push notification asking if they are interested in purchasing the item. You could reference the product name by using {{canvas_entry_properties.${product_name}}}

The second step may send another push notification prompting the user to checkout if they added the item to their cart but have not purchased it yet. You can continue to reference the product_name entry property by using {{canvas_entry_properties.${product_name}}}.

## Troubleshooting

### Entry properties are blank with multiple entry triggers

Braze stores canvas_entry_properties from the trigger that entered this user, not from every trigger configured on the Canvas. If that trigger has no event or API payload—for example Start Session or Change Custom Attribute Value—Liquid canvas_entry_properties is blank for that journey. Users who enter the same Canvas from a custom event, purchase, or API call still have the properties from that payload.

To keep entry properties populated for every user, use only entry types that pass those properties (custom event, purchase, or API-triggered). For personalization in the current Canvas editor, use context and event properties. To filter on properties, use event property segmentation instead of Liquid canvas_entry_properties.

- 

New Stuff!
