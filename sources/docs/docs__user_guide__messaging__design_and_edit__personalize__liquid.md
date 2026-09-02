---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid
slug: docs__user_guide__messaging__design_and_edit__personalize__liquid
title: "Liquid reference"
description: "This landing page covers all things Liquid, such as supported personalization tags, filters, setting default values, and more."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Liquid reference 

Liquid is an open-source template language created by Shopify and used by Braze to power dynamic personalization. Instead of sending a static message to everyone, Liquid lets you create templates that change their content based on each recipient’s profile data, behavior, or language. Use the articles in this section for supported tags, filters, conditional logic, default values, and common personalization patterns.

## Section articles 

- 

 Use Liquid

- 

 Supported personalization tags

- 

 Operators

- 

 Filters

- 

 Advanced filters

- 

 Set default values

- 

 Conditional messaging logic

- 

 Abort messages

- 

 Liquid use cases

- 

 Tutorials

- 

 Frequently asked questions

## About Liquid

Liquid acts as a bridge between your message and your user data. When you send a message, Braze scans the text for Liquid syntax. When it finds Liquid, it pulls the relevant data for that specific user and replaces the code with the actual value before the message is sent.

For example, you can retrieve a custom attribute from a user profile that is an integer data type and round that value to the nearest whole number. For more on Liquid syntax and usage, refer to Supported personalization tags.

Liquid templating language supports the use of objects, tags, and filters.

- Objects allow you to insert personalized attributes into your messages.
 
- Tags allow you to insert data into messaging and use conditional logic to send messages if certain conditions are met. For example, you can use tags to include intelligent logic, such as “if” statements, in your campaigns.
 
- Filters allow you to reformat personalized attributes and dynamic content. For example, you could use the date filter to convert a timestamp, such as 2016-09-07 08:43:50 UTC, into a date, such as September 7, 2016.

warning

Braze currently doesn’t support 100% of Shopify’s Liquid, only certain portions which we have attempted to outline in our documentation. We highly recommend testing all messages using Liquid before sending them to reduce the risk of errors or using unsupported Liquid.

### Liquid 5 support

Braze supports Liquid up to and including Liquid 5 from Shopify. Liquid implementation supports syntax personalization tag types and whitespace control. For more information on specific tags, refer to syntax tags.

The following new array and math filters are available for use in your Liquid as you build your messaging.

- at_least
 
- at_most
 
- compact
 
- concat
 
- sort_natural
 
- where

Refer to Filters for definitions.

## Terms to know

These terms are reinterpreted from Shopify’s documentation based on our level of support.

 Term | 
 Definition | 
 Example | 

 Liquid | 
 A commonly-used, customer-facing template language created by Shopify and written in Ruby that is used to load and pull dynamic content. | 
 {{${first_name}}} will insert a user’s first name into a message. | 

 Object | 
 A denotation of a variable and location of the intended variable name that tells Liquid where to show content in the message. | 
 {{${city}}} will insert a user’s city into a message. | 

 Conditional logic tag | 
 Used to create logic and control the flow of message content. In Braze, conditional logic tags are used to create exceptions and variations in messages based on certain, predefined criteria. | 
 {% if ${language} == 'en' %} will trigger your message in a designated way in the event that a user has designated “English” as their language. | 

 Filters | 
 Used to change, narrow, or reformat the output of the Liquid object. It’s often used to create mathematical operations. | 
 {{"Big Sale" | upcase}} will cause the words “Big Sale” to appear as “BIG SALE” in the message. | 

 Operators | 
 Used in messages to create dependencies or criteria that can affect which message your user receives. | 
 If a user meets the defined criteria in a message tagged with {% custom_attribute.${Total_Revenue} > 0%}, they will receive the message. If not, they will receive another designated message (or not), depending on what you set. | 

- 

New Stuff!
