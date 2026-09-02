---
url: https://www.braze.com/docs/user_guide/example_library/personalize/test_messages_with_mock_json
slug: docs__user_guide__example_library__personalize__test_messages_with_mock_json
title: "Test messages with mock JSON in preview"
description: "Use Liquid capture and json_parse to mock Connected Content or entry-style JSON in the message composer preview without launching a campaign or sending test messages...."
section: user_guide/example_library
fetched: 2026-09-02
evidence: company-own (technical)
---
# Test messages with mock JSON in preview

Mock API or entry-style JSON inside your message with capture and json_parse so you can validate Liquid and layout in the composer preview before you launch a campaign, trigger a Canvas, or call Connected Content live.

## About this example

Flash & Thread, a fictional clothing retail brand, builds messages that depend on Connected Content responses, Canvas context variables, or array of objects profile data. Triggering real API calls or launching campaigns for every iteration slows development.

This pattern embeds a mock JSON payload in the message body, stores it with capture, then parses it with json_parse so Liquid can reference structured fields in the Preview section—without a live Connected Content call, API-triggered Canvas entry, or test send.

Use this during message development. It does not replace end-to-end testing with real triggers, test sends, or preview user paths in Canvas.

## Considerations

- This approach supports composer preview during development. Run test sends and live-path checks before you launch to customers.
 
- A capture block alone stores JSON as a string. Reference fields only after you apply json_parse—otherwise preview output can be blank.
 
- Mock JSON must be valid. Invalid JSON causes json_parse to fail or return unexpected structures.
 
- Replace or remove mock blocks before launch, or guard production Liquid so mock data is used only in preview (for example with a comment flag you delete before go-live).
 
- The Liquid snippets in this article are examples. Test in your channels and with your real payload shapes.
 
- For Connected Content in production, remove the mock block and use your live URL tag. See Making an API call.

## Setup

This example mocks a Connected Content–style product listing response for an email that loops over listings.

### Step 1: Capture mock JSON in the message

Use capture to hold the JSON string. Use valid JSON syntax inside the block (double quotes on keys and string values).

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
{% capture mock_response %}
{
 "success": true,
 "listings": [
 {
 "id": 45731,
 "name": "Summit Trail Jacket",
 "image_url": "https://example.com/images/trail-jacket.png",
 "price": {
 "actual": "89.00",
 "currency": "USD"
 },
 "link": "https://example.com/products/trail-jacket",
 "product_category": "Outerwear",
 "properties": {
 "size": "L",
 "colour": "Navy",
 "limited_edition": false
 },
 "out_of_stock": false
 }
 ]
}
{% endcapture %}

```
 | 

### Step 2: Parse JSON with json_parse

Assign the parsed structure to a variable you reference in the rest of the message.

```

1

```
 | 
```
{% assign response_json = mock_response | json_parse %}

```
 | 

Without json_parse, dot notation on the captured string (for example {{ mock_response.listings }}) typically renders blank in preview.

### Step 3: Reference parsed fields in Liquid

Loop over the parsed array and render fields as you would for a live API response.

```

1
2
3

```
 | 
```
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}

```
 | 

Go to the Preview section in the message composer and confirm fields render.

### Step 4: Apply the same pattern to other JSON shapes

Use the same capture + json_parse flow to mock:

 Data you want to test | 
 Mock JSON shape | 

 Canvas context variables | 
 Object with the property keys your message expects | 

 Array of objects on a profile | 
 JSON array of objects with the same keys as your custom attribute | 

 Connected Content response | 
 Sample API JSON saved from a prior successful call | 

Swap mock variables for production Liquid (Canvas context variables, custom attributes, or Connected Content tags) before you launch.

## Related articles

- Send test messages
 
- Preview user paths in Canvas
 
- Advanced Liquid filters (json_parse)
 
- Connected Content
 
- Array of objects
 
- Context variables

- 

New Stuff!
