---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/catalog
slug: docs__user_guide__messaging__design_and_edit__personalize__sources__catalog
title: "Catalog"
description: "Learn how to use catalogs as a data source for personalizing your Braze messages with non-user data like product details, content feeds, and pricing."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Catalog

Reference non-user data in your messages by connecting to catalogs. Catalogs store structured datasets — such as product information, restaurant listings, or content feeds — that you can access through Liquid to personalize any message.

## How it works

After importing data into a catalog (through CSV or API), reference catalog items in your messages using the items Liquid tag. For example, to pull a product name from a catalog called products:

```

1
2

```
 | 
```
{% catalog_items products {{${product_id}}} %}
{{items[0].name}} is back in stock!

```
 | 

Catalogs support up to 1,000 fields per item and can store millions of rows, making them suitable for large product inventories and content libraries.

## Common use cases

 Use case | 
 Description | 

 Product details | 
 Insert names, descriptions, prices, and images from a product catalog | 

 Restaurant or store listings | 
 Personalize messages with location-specific details | 

 Content recommendations | 
 Reference articles, videos, or other media items | 

 Event information | 
 Pull event dates, venues, and descriptions into messages | 

 Tier-based offers | 
 Match promotions to a user’s membership level or segment | 

## Catalog triggers

Catalogs also power automated messaging through catalog triggers. Set up back-in-stock notifications and price drop notifications to automatically message users when catalog items change.

For more information, see Catalog triggers.

## Selections

Use selections to group catalog items by filters you define. For example, create a selection of items under $20 or items in a specific category, then reference the filtered set in your messages.

For more information, see Selections.

## Getting started

To create and manage catalogs, see Catalogs. To learn how to reference catalog data in your messages, see Using catalogs in a message.

- 

New Stuff!
