---
url: https://www.braze.com/docs/api/objects_filters/trigger_properties_object
slug: docs__api__objects_filters__trigger_properties_object
title: "Trigger properties object"
description: "This reference article explains the different components of the trigger properties object."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# Trigger properties object

When using one of the endpoints for sending a campaign with API-triggered delivery, you may provide a map of keys and values to customize your message.

If you make an API request that contains an object in trigger_properties, the values in that object can then be referenced in your message template under the api_trigger_properties namespace. For example, a request with the following could add the word "shoes" to a message by adding {{api_trigger_properties.${product_name}}}.

Note that while trigger properties can be templated into messages, they aren’t automatically stored in the user profile by default.

note

The trigger_properties object and api_trigger_properties.${product_name} syntax is only supported in campaigns. To customize messages with keys and values from an API trigger request for Canvas, use the Canvas entry properties object. The trigger_properties object has a maximum size limit of 50 KB.

## Object body

The trigger_properties object supports strings, numbers, booleans, dates, objects, and arrays as data types.

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
 "trigger_properties" : {
 "product_name" : "shoes",
 "product_price" : 79.99,
 "details" : {
 "color" : "red",
 "size" : {
 "numerical" : 10,
 "country" : "US"
 }
 },
 "related_skus": ["123", "456", "789"]
 }
}

```
 | 

## Liquid templating examples

Reference trigger properties in your message templates using the api_trigger_properties namespace:

- Strings: {{api_trigger_properties.${product_name}}} returns "shoes"
 
- Numbers: {{api_trigger_properties.${product_price}}} returns 79.99
 
- Nested objects: {{api_trigger_properties.${details}.${color}}} returns "red"
 
- Array elements: {{api_trigger_properties.${related_skus}[0]}} returns "123"

- 

New Stuff!
