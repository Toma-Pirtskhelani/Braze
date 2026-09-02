---
url: https://www.braze.com/docs/partners/ecommerce/shopify/multiple_stores
slug: docs__partners__ecommerce__shopify__multiple_stores
title: "Connect multiple Shopify stores"
description: "This reference article covers how to connect and configure multiple Shopify stores to a single workspace."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Connect multiple Shopify stores

Connect multiple Shopify store domains to a single workspace to have a holistic view of your customers across all markets. Build and launch automation programs and journeys in a single workspace without duplicating efforts across regional stores.

important

This feature doesn’t support Shopify Markets or Markets Pro. If you’re interested in Shopify Markets or Markets Pro support, submit product feedback.

## Requirements

 Requirement | 
 Description | 

 Set up a Shopify store | 
 Be sure that you’ve already set up at least one Shopify store with Braze. | 

 Unique Shopify storefront domains for each region | 
 Multiple store support is intended for use with unique Shopify store domains for different regional storefronts. 

If you want to connect multiple sub-brands to Braze, we recommend creating separate workspaces for each sub-brand. | 

## Connecting an additional store

After you install the Braze app to your Shopify store and install your first store, select + Connect New Store.

For your additional Shopify regional store, select Begin setup.

Like your first Shopify store integration, you can choose either between a standard or custom setup.

Choose the option that best fits your needs:

- standard
 
- custom

The standard integration is tailored for Shopify online stores, providing a seamless and straightforward setup process. This option allows you to quickly connect your Shopify store to Braze, empowering you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

To use the standard Shopify integration, refer to Shopify standard integration setup.

The custom integration offers a more flexible and composable solution if you use Shopify Hydrogen or support a headless store. This option empowers you to implement Braze SDKs directly into your Shopify environment, enabling deeper integration and tailored functionalities. Whether you’re looking to create unique customer experiences or optimize specific workflows, the custom integration provides the tools necessary to fully leverage Braze’s capabilities in a headless setup.

To use the custom Shopify integration, refer to Shopify custom integration setup.

To view each store integration and configure advanced settings, select a store in the dropdown menu.

## Syncing users across stores

### Shopify alias

When you connect multiple stores, synced Shopify users who have logged in or placed an order will receive a new alias in the format: shopify_customer_id_{{storename}}.

### Braze external ID

You can choose from the following options for your Braze external ID:

 Option | 
 Description | 

 Shopify Customer ID | 
 If you use Shopify’s customer ID as your Braze external ID, each store will generate a unique customer ID for each user. This means that if a user interacts with multiple stores, they will have separate profiles in Braze. | 

 Email, Hashed Email, or Custom External ID | 
 If you use the email, hashed email, or custom external ID types, users who engage with multiple stores will have their profiles merged into a single consolidated profile when they log in or place an order. | 

### Merged fields

When a user profile is synced, the following fields will be merged. For full details on merging behavior, refer to Merge behavior.

- Device information
 
- Total session count (combined from both profiles)
 
- Custom event and purchase data
 
- Custom event properties for segmentation (for example, “X times in Y days” where X ≤ 50 and Y ≤ 30)
 
- Event count (combined from both profiles)
 
- Dates of first and last events (Braze selects the earliest and most recent dates)
 
- Campaign interaction data (most recent date fields)
 
- Workflow summaries (most recent date fields)
 
- Message and engagement history
 
- Subscription groups

### Collecting subscribers (optional)

You can choose to collect subscribers directly through Braze (in your Shopify connector settings) or through API and SDK alternatives that sync data from Shopify.

- shopify connector
 
- braze api or sdks

In the Manage users step of your Shopify connector settings, you can use Braze to collect email and SMS subscriber opt-ins and organize them into a dedicated subscription group:

- Create a unique subscription group for each store you connect. This helps you maintain accurate data about where subscribers are coming from.
 
- Enable email and SMS subscriber collection.

Alternatively, you can sync email and SMS marketing opt-in information directly from Shopify using the Braze API or SDKs.

 Option | 
 Resources | 

 API | 
 - Subscription group endpoints to directly replace what is supported by the integration
- Users/track endpoint to set subscription group data or the global email subscription state
- Braze preference center for more customized marketing opt-in collection options | 

 SDKs | 
 - NotificationSubscriptionTypes
- addToSubscriptionGroup
- removeFromSubscriptionGroup
- setEmailNotificationSubscriptionType | 

## Shopify data

### Synced attributes

When you connect more than one store, the following attributes will be synced with the most recent state of the Shopify profile:

- First Name
 
- Last Name
 
- Email
 
- Gender
 
- Date of Birth
 
- Country
 
- City
 
- Last Used App
 
- Language
 
- Time Zone
 
- Shopify Tags
 
- Shopify Order Count
 
- Shopify Total Spent

### Supported events

#### eCommerce recommended events

When you connect multiple stores, incoming eCommerce recommended events will include a source event property. This property identifies which storefront URL the event originated from, allowing you to use this information for segmentation or triggering specific use cases.

The supported eCommerce recommended events within the Shopify integration are:

- ecommerce.product_viewed
 
- ecommerce.cart_updated
 
- ecommerce.checkout_started
 
- ecommerce.order_placed
 
- ecommerce.order_cancelled
 
- ecommerce.order_refunded

#### Shopify custom events

Incoming Shopify custom events include an event property called shopify_storefront. This property indicates which storefront URL the event came from, allowing you to leverage it for segmentation or triggering use cases.

Supported Shopify custom events include:

- shopify_fulfilled_order
 
- shopify_partially_fulfilled_order
 
- shopify_paid_order
 
- shopify_account_login

For a complete overview of all event payloads, refer to Shopify data features.

### Shopify product sync

When you connect and configure each Shopify store in Braze, you can optionally enable the Shopify product sync as part of the integration.

If you activate the product sync for each store, Braze includes the name of your Shopify store in the catalog name. This distinguishes products from different stores.

- 

New Stuff!
