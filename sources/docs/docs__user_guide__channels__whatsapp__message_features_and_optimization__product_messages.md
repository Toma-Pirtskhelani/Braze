---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/product_messages
slug: docs__user_guide__channels__whatsapp__message_features_and_optimization__product_messages
title: "Product messages"
description: "This page covers how to use WhatsApp product messages to send interactive WhatsApp messages that showcase products from your Meta catalog."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Product messages

Product messages empower you to send interactive WhatsApp messages that showcase products directly from your Meta catalog.

When you send a WhatsApp product message to a user, the user goes on the following customer journey:

- The user receives your product or catalog message in WhatsApp.
 
- The user adds products to their cart directly from WhatsApp.
 
- The user taps Place order in WhatsApp.
 
- Your website or app receives the cart data from Braze and generates a checkout link.
 
- The user is directed to your website or app to complete their checkout.

When users add items to their cart through catalog messages, Braze receives webhook data for follow-up actions.

## Requirements

 Requirement | 
 Description | 

 WhatsApp Business Account | 
 To use WhatsApp product messages, you must have a WhatsApp Business Account connected with Braze. | 

 Meta catalog | 
 You need to set up a Meta catalog in your Commerce Manager. | 

 Term compliance | 
 Comply with the Meta Commerce Terms and Policies. | 

## Product message types

note

Enhance your product message experience with the integrated product selector, which is accessed during step 4 of Setting up product messages.

- catalog messages
 
- multi-product messages
 
- single product

Catalog messages display your entire product catalog in an interactive format. They are available as template and response messages.

If you’ve enabled catalog permissions to Braze during setup, you can select which thumbnail is visible to users.

note

You don’t need to make additional product selections in Braze, as the catalog connection is managed by Meta and thus is inherited into your product catalog.

Multi-product messages highlight specific products from your catalog, with up to 30 highlighted items per message. They are available as template and response messages.

You can either select the products manually with IDs or, if you’ve enabled catalog permissions during setup, use the dropdown product selector.

important

There’s a known header display issue with multi-product message templates on Meta. Meta is aware of the issue and working on a fix.

Single product messages highlight one specific product from your product catalog. They are available as response messages.

You can either select the products manually with IDs or, if you’ve enabled catalog permissions during setup, use the dropdown product selector.

## Setting up product messages

- In the Meta Commerce Manager, follow Meta’s instructions to create your Meta catalog. Make sure you’re in the same Meta Business Portfolio where your Braze-connected WhatsApp Business Account resides.
 
- Follow Meta’s instructions to connect your Meta catalog to your Braze-connected WhatsApp Business Account by assigning the “Manage Catalog” permission in Meta Business Manager.

Make sure to use the Braze Business Manager ID, 332231937299182, as the partner business ID.

- Select your Meta catalog settings. You must select Show catalog icon in chat header to send catalog messages.

- In Braze, go through the embedded signup process to provide permissions. Be sure to select all the catalogs you want to provide permissions for. This will unlock the Braze integrated product selector.

tip

For best practices to follow when creating Meta catalogs, refer to Tips for building a high-quality catalog in Commerce Manager.

## Building a product message

You can build a product message by using a WhatsApp template message or response message.

- whatsapp message template
 
- response message

- In your Meta Business manager, go to Message Templates.
 
- Select Catalog as a format, and then choose between Catalog message (displays full catalog) and Multi-product catalog message (highlights specific items).
 
- In Braze, create a WhatsApp campaign or Canvas Message step.
 
- Select the subscription group that matches where you submitted the template.
 
- Select WhatsApp Template Message.
 
- Select the template you’d like to use.

- If you select a multi-product template, provide the section title and content IDs for the products to highlight. You can either copy the Content ID directly from your Meta Commerce Manager or, if you enabled the permissions for the integrated product selector, select the items.

- Continue building your message.

- In Braze, create a WhatsApp campaign or Canvas Message step.
 
- Select a subscription group.
 
- Select Response Message.
 
- Select Meta Product Messages.

- Select the message type you’d like to use.

- Continue building your message.

## Managing products

### Accessing Commerce Manager

In your Meta Business Manager, go to Commerce Manager and select your organization. Here, you can manage your catalog assets, such as:

- Create new catalogs
 
- Add products to existing catalogs
 
- Update product information
 
- Remove discontinued items

important

If you remove referenced products from your catalog, the associated messages will fail to send.

## Receiving inbound product questions

Users can respond to your product or catalog message with product questions. These arrive as inbound messages, which can then be sorted with an Action Path.

Additionally, Braze extracts the product ID and catalog ID from these questions, so if you wish to automate responses or send questions to another team (such as customer support), you can include those details. For example, you could personalize responses with the WhatsApp properties of inbound_product_id or inbound_catalog_id.

## Checkout: Cart processing and webhooks

When users interact with your WhatsApp product messages, they can browse products and add items to their cart. However, currently there is no built-in checkout functionality for shipping information or payment processing. Instead, we encourage you to create a cart within your own app or website and direct users to that cart using a custom link.

### Considerations

- No in-app checkout: Users can’t complete purchases directly within WhatsApp. All transactions must be redirected to your website or app.
 
- Custom link required: You need to create a custom link that directs users to their cart on your platform.
 
- Manual setup: The setup process requires manual configuration of your cart and messaging workflows.

note

We currently don’t support payments directly occurring in WhatsApp, and future support will be country-specific (currently, Meta offers it only for companies based in and working directly with users in India, Brazil, and Singapore).

### Setting up cart event triggers

When a customer places an order in WhatsApp, Braze automatically:

- Receives the cart contents from WhatsApp (product IDs, quantities, and other order data).
 
- Creates an ecommerce.cart_update eCommerce event with all relevant data, including source = whats_app.
 
- Triggers a response, allowing you to set up automated campaigns to respond to the order.

The ecommerce.cart_update eCommerce event only appears listed in Braze after an event has been sent, which can be done by generating a test product message from Braze and submitting a cart event.
The cart event includes:

- Cart ID: Unique identifier for the cart
 
- Products: List of items with product IDs, quantities, and prices
 
- Total Value: Sum of all items
 
- Currency: The cart’s currency
 
- Source: Marked as “whats_app”
 
- Metadata: Additional data like catalog ID and message text

You can find additional Braze cart event information in Types of eCommerce recommended events.

### Setting up a triggered response

- Create a custom event trigger for ecommerce.cart_updated.
 
- Add a property filter for source = "whats_app".

- Configure follow-up actions based on cart data.

### Recommended checkout implementations

- simple liquid-based cart links
 
- connected content
 
- webhook and custom events

Use Liquid to build cart URLs directly in your response message. This is best if you have consistent product IDs between WhatsApp and your eCommerce platform.

#### Example Liquid

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
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
 {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
 {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}

```
 | 

#### Setup

- Create a WhatsApp response message campaign with the trigger of an ecommerce.cart_update eCommerce event.
 
- Create a subsequent message with the cart URL.
 
- Build your cart URL with Liquid. If you use Shopify, you can create a cart permalink with the prior example Liquid.

Make an API call to your eCommerce system to generate a personalized checkout URL. This is best if you need dynamic cart URL generation or complex product mapping.

#### Setup

- Create a webhook campaign or Canvas step triggered by the ecommerce.cart_update eCommerce event, which will send the cart data to your eCommerce system.
 
- Create a WhatsApp campaign or Canvas Message step triggered by the same eCommerce event to send a WhatsApp response message with the cart URL to the user. Follow the direction in the subsequent response message to use Connected Content.

Use webhooks to send cart data to your system, then trigger follow-up messages through custom events. This is best for complex integrations requiring extensive cart processing or multi-step workflows.

#### Setup

Create a webhook campaign or Canvas step triggered by the ecommerce.cart_update eCommerce event, which will send the cart data to your eCommerce system. Your API will then:

- Receive cart data
 
- Create a cart in your system
 
- Generate the checkout URL
 
- Send a checkout_started event to Braze, triggering your WhatsApp message to send with the checkout link

## Testing and validation

### Test message requirements

Cart functionality carries over between test messages, but processing of the inbound result doesn’t carry over.

### Message preview

- Product images and details are pulled from your Meta catalog.
 
- Interactive preview shows placeholders until integration is complete.

### Error codes

- If a product ID doesn’t exist in the catalog, you’ll receive the error product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359.
 
- If a catalog is disconnected from the WABA, you’ll receive the error Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings.

- 

New Stuff!
