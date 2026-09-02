---
url: https://www.braze.com/docs/user_guide/brazeai/item_recommendations/using_recommendations
slug: docs__user_guide__brazeai__item_recommendations__using_recommendations
title: "Use item recommendations in your messaging"
description: "This article describes how to use item recommendations in your message."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Use item recommendations in your messaging

After your recommendation is trained, you can use Liquid to fetch and display recommended items in your messages by working directly with the product_recommendation Liquid object.

tip

For a step-by-step walkthrough, check out our Braze Learning course: Crafting Personalized Experiences with AI.

## Prerequisites

Before you can use recommendations in your messaging, you’ll need to create and train a recommendation engine. Training can take anywhere between 10 minutes and 36 hours—you’ll receive an email when it’s finished or if an error has occurred.

## Using recommendations in your messaging

### Step 1: Add Liquid code

After your recommendation is finished training, you can personalize your messages with Liquid to insert the most popular products in that catalog.

- pre-formatted code
 
- custom code

You can generate Liquid from the Add personalization section in your message composer:

- In any message composers that support personalization, select Add personalization to open the personalization window.
 
- For Personalization Type, select Item Recommendation.
 
- For Item Recommendation Name, select the recommendation you just created.
 
- For Number of Predicted Items, enter how many top products you’d like to be inserted. For example, you can display the top three most purchased items.
 
- For Information to Display, select which fields from the catalog should be included for each item. The values for these fields for each item will be drawn from the catalog associated with this recommendation.
 
- Select the Copy icon and paste the Liquid wherever it needs to go in your message.

You can write custom Liquid code by referencing a catalog’s product_recommendation object. It contains all the dynamically-generated product recommendation data for that catalog, structured as an array of objects, where each object represents a recommended item.

 Specification | 
 Details | 

 Structure | 
 Each item is accessed as items[index], where index starts at 0 (for the first item) and increments for subsequent items. | 

 Catalog fields | 
 Each item in the array contains key-value pairs corresponding to fields (columns) in the catalog. For example, common catalog fields for product recommendations include:
- name or title
- price
- image_url | 

Use the assign tag to fetch the product_recommendation data and assign it to a variable.

```

1

```
 | 
```
{% assign items = {{product_recommendation.${recommendation_name}}} %}

```
 | 

Replace the following:

 Placeholder | 
 Description | 

 recommendation_name | 
 The name of the AI recommendation you created in Braze. | 

 items | 
 The variable storing the recommended items array. | 

Next, reference specific items and their fields using array indexing and dot notation:

```

1
2

```
 | 
```
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}

```
 | 

To include multiple items, reference each item individually by its index. .name and .price pull the corresponding field from the catalog.

```

1
2
3
4

```
 | 
```
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}

```
 | 

AI recommendations return multiple products as an array, where items[0] is the first item, items[1] is the second, and so on. If a recommendation only returns one item, attempting to reference items[1] will result in an empty field.

### Step 2: Reference an image (optional)

If the catalog your recommendation includes image links, you can reference them in your message.

- drag-and-drop
 
- html

In the email drag-and-drop editor, add an image block to your email, then select the image block to open Image properties.

Toggle Image with Liquid, then add the following to the Dynamic URL field (the URL field does not support newlines, so make sure the code appears on one line):

```

1

```
 | 
```
{% assign items = {{product_recommendation.${recommendation_name}}} %}{{ items[0].image_url_field }}

```
 | 

Replace the following:

 Placeholder | 
 Description | 

 recommendation_name | 
 The name of your recommendation. | 

 image_url_field | 
 The name of the field in your catalog that contains image URLs. | 

To include a placeholder image in your preview and test emails, select Choose image then either choose an image from your media library or enter the URL of an image from your hosting site.

For HTML image references, set the image src attribute to the image URL field in the catalog. You might want to use another field, such as a product name or description, as the alt text.

```

1
2

```
 | 
```
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">

```
 | 

Replace the following:

 Placeholder | 
 Description | 

 recommendation_name | 
 The name of your recommendation. | 

 image_url_field | 
 The name of the field in your catalog that contains image URLs. | 

- 

New Stuff!
