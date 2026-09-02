---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid
slug: docs__user_guide__messaging__design_and_edit__personalize__liquid__using_liquid
title: "Use Liquid"
description: "This reference article provides an overview of common Liquid use cases and how to include Liquid tags into your messaging."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Use Liquid

This article shows how you can use a variety of user attributes to dynamically insert personal information into your messaging.

Liquid is an open-source template language developed by Shopify and written in Ruby. You can use it in Braze to pull user profile data into your messages and customize that data. For example, you can use Liquid tags to create conditional messages, such as sending different offers based on a user’s subscription anniversary date. Additionally, filters can manipulate data, like formatting a user’s registration date from a timestamp into a more readable format, such as “January 15, 2022.” For further details on Liquid syntax and its capabilities, refer to Supported personalization tags.

## How it works

Liquid tags act as placeholders in your messages that can pull in consented information from your user’s account and enable personalization and relevant messaging practices.

In the following block, you can see that a dual usage of a Liquid tag to call the user’s first name, as well as a default tag in the event that a user would not have their first name registered.

```

1

```
 | 
```
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!

```
 | 

To a user named Janet Doe, the message would appear to the user as either:

```

1

```
 | 
```
Hi Janet, thanks for using the App!

```
 | 

Or…

```

1

```
 | 
```
Hi Valued User, thanks for using the App!

```
 | 

important

HTML comments (<!-- -->) are removed before any Liquid is read, so Liquid tags within HTML comments do not render in your message. For proper rendering, make sure all the Liquid tags you want to use are outside of HTML comments.

## Supported values to substitute

The following values can be substituted into a message, depending on their availability:

- Basic user information (for example, first_name, last_name, email_address)
 
- Custom attributes

- Nested custom attributes

- Custom event properties
 
- Most recently used device information
 
- Target device information

You can also pull content directly from a web server through Braze Connected Content.

important

Braze currently supports Liquid up to and including Liquid 5 from Shopify.

## Using Liquid

Using Liquid tags, you can elevate the quality of your messages by enriching them with a personal touch.

### Liquid syntax

Liquid follows a specific structure, or syntax, that you’ll need to keep in mind as you’re crafting dynamic personalization. Here are a few basic rules to keep in mind:

- Use straight quotes in Braze: There is a difference between curly quotes (’ ‘) and straight quotes (' '). Use straight quotes (' ') in your Liquid in Braze. You may see curly quotes when copying and pasting from certain text editors, which can cause issues in your Liquid. If you’re inputting quotes directly into the Braze dashboard, you’ll be fine.
 
- Brackets come in pairs: Every bracket must both open and close { }. Make sure to use curly brackets.
 
- If statements come in pairs: For every if, you need an endif to indicate the if statement has ended.
 
- Case statements come in pairs: For every case, you need an endcase to close the block.
 
- Variable names must use ASCII characters: Liquid variable names (created with assign or capture) support only ASCII letters, digits, and underscores. Braze personalization attribute names (inside custom_attribute.${...} or event_properties.${...}) can include non-ASCII characters.
 
- Wrap Braze Liquid variables in multi-line assign tags: Use double curly braces ({{ }}) around Braze Liquid variables when an assign spans multiple lines.

#### Multi-line assign tags

You can split an assign across multiple lines (for example, by continuing filters with | before the closing tag) as long as you wrap all Braze Liquid variables with double curly braces ({{ }}). Without those braces, multi-line assign statements can cause unexpected rendering, including custom attributes that fail to template. The following example shows a working multi-line assign:

```

1
2
3
4

```
 | 
```
{%- assign color = {{custom_attribute.${favorite_color}}}
| default: {{custom_attribute.${fav_color}}}
| default: 'blue'
%}

```
 | 

You can also write the full assign on one line:

```

1

```
 | 
```
{%- assign color = custom_attribute.${favorite_color} | default: custom_attribute.${fav_color} | default: 'blue' %}

```
 | 

#### Where to use operators and filters

Operators (such as ==, !=, >, and, or) and filters (such as | size, | plus) can each be used only in specific Liquid contexts.

 Context | 
 Operators | 
 Filters | 

 assign | 
 Not supported | 
 Supported | 

 if, elsif, unless | 
 Supported | 
 Not supported | 

 case, when | 
 Equality matching only1 | 
 Not supported | 

 for | 
 Not supported | 
 Not supported | 

 Array access ([ ]) | 
 Not supported | 
 Not supported | 

When you need a filtered value in a context that doesn’t support filters, assign the result to a variable first.

##### Use a filter result in a conditional

You can’t use a filter directly in a conditional statement. This is incorrect:

```

1
2
3

```
 | 
```
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}

```
 | 

Instead, assign the filter result to a variable:

```

1
2
3
4

```
 | 
```
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}

```
 | 

##### Use a filter result in a for loop

You can’t apply a filter to the iterable in a for loop. This is incorrect:

```

1
2
3

```
 | 
```
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}

```
 | 

Instead, assign the filtered value to a variable:

```

1
2
3
4

```
 | 
```
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}

```
 | 

##### Use a filter result for array access

You can’t use a filter inside square brackets. This is incorrect:

```

1

```
 | 
```
{{ my_array[my_var | minus: 1] }}

```
 | 

Instead, assign the filtered value first:

```

1
2

```
 | 
```
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}

```
 | 

##### Store a comparison result in a variable

You can’t use an operator in an assign statement. This is incorrect:

```

1
2
3
4

```
 | 
```
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}

```
 | 

Instead, use a conditional to set the variable:

```

1
2
3
4
5
6
7
8

```
 | 
```
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}

```
 | 

#### Default attributes and custom attributes

If you include the following text in your message: {{${first_name}}}, the user’s first name (pulled from the user’s profile) will be substituted when the message is sent. You can use the same format with other default user attributes.

If you would like to use the value of a custom attribute, you must add the namespace “custom_attribute” to the variable. For example, to use a custom attribute named “zip code”, you would include {{custom_attribute.${zip code}}} in your message.

### Inserting tags

You can insert tags by typing two open curly brackets {{ in any message, which will trigger an auto-completion feature that will continue to update as you type. You can even select a variable from the options that appear as you type.

If you’re using a custom tag, you can copy and paste the tag into whatever message you desire.

#### Exceptions for double brackets

If using a tag within another Liquid tag, such as {{ in any message, which will trigger an auto-completion feature that will continue to update as you type. You can even select a variable from the options that appear as you type.

If you’re using a custom tag, you can copy and paste the tag into whatever message you desire.

#### Exceptions for double brackets

If using a tag within another Liquid tag, such as {% assign %} or {% if %}, you can use either double brackets or no brackets. It is only when the tag stands alone that it has to be encased in double brackets. For simplicity, you can always use double brackets.

The following tags are all correct:

```

1
2
3
4
5

```
 | 
```
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}

```
 | 

note

If you use Liquid in your email messages, be sure to:

- Insert it using the HTML editor as opposed to the classic editor. The classic editor may parse the Liquid as plaintext. For example, the Liquid would parse as Hi {{ ${first_name} }}, thanks for using our service! instead of templating in the user’s first name.
 
- Place Liquid code within the <body> tag only. Placing it outside this tag may cause inconsistent rendering upon delivery.

### Switching between HTML and Classic editors

When you switch between the HTML and Classic editors, Liquid snippets and Content Blocks can shift position in your message. Review your template after you switch editors. If you need more predictable layout control, use the Drag-and-Drop Editor.

### Inserting pre-formatted variables

You can insert pre-formatted variables with defaults through the Add Personalization modal located near any templated text field.

The modal will insert Liquid with your specified default value at the point where your cursor was. The insertion point is also specified by the preview box, which has the before and after text. If a block of text is highlighted, the highlighted text will be replaced.

- 
 
In case and when tags, Liquid compares the case expression to each when value using equality (similar to chaining if and elsif with ==). You can’t use arbitrary comparison or logical operators inside a when clause the way you do with if and elsif. For examples, see Conditional messaging logic. ↩

- 

New Stuff!
