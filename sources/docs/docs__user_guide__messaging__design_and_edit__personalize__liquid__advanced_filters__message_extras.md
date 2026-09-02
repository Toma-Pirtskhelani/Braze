---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras
slug: docs__user_guide__messaging__design_and_edit__personalize__liquid__advanced_filters__message_extras
title: "Message extras Liquid tag"
description: "This article explains how to use the message extras Liquid tag and how to check for syntax."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Message extras Liquid tag

Use the message_extras Liquid tag to annotate your send events with dynamic data from Connected Content, Catalogs, custom attributes (such as language, country), Canvas entry properties, or other data sources.

The message_extras Liquid tag appends key-value pairs to the corresponding send event in Currents and Snowflake Data Sharing.

To send dynamic or extra data back to your Currents or Snowflake Data Sharing send event, insert the proper Liquid tag into your message body.

Here’s an example of the standard Liquid tag format for message_extras:

```

1

```
 | 
```
{% message_extras :key test :value 123 %}

```
 | 

You can add these tags as needed for your key-value pairs in the message body. However, the length of all keys and values should not exceed 1,000 bytes (1 KB). In Currents and Snowflake Data Sharing, you can see a new event field called message_extras for your send events. This generates a JSON-serialized string in one field.

note

Email extras send metadata to email service providers and are not published to Currents or Snowflake. To add metadata or dynamic values to Currents or Snowflake send events, use the message_extras Liquid tag.

## How message extras data is sent using Currents

Message extras are key-value pairs attached at send time. Configuration depends on the channel. For email, they are added using headers. For iOS push, they are included in the push payload. All supported send events surface the same message_extras field in Currents (and Snowflake) once the message is sent.

## Supported channels

The message_extras tag is supported for all message types with a send event, along with in-app message impression events. Using message_extras with in-app messages requires certain minimum SDK versions to be met.

## How to use the message_extras tag

- In the message body for the channel, enter the message_extras Liquid tag. Or, you can use the Add Personalization modal and select Message Extras for the personalization type.

- Enter the key-value pair for each message_extras tag.

- After your campaign or Canvas has been sent, Braze attaches the dynamic data at send time to the message_extras field in Currents or Snowflake Data Sharing send events.

## Checking syntax

Any other input that doesn’t match the tag standard discussed earlier in this section may fail to pass to Currents or Snowflake. Check that your syntax or formatting doesn’t include any of the following:

- Non-existent, empty, or mistyped delimiters
 
- Duplicate keys (Braze defaults to sending the key-value pair that is encountered first)
 
- Extra text before keys or values are defined
 
- Out of order keys and values

- For example, {% message_extras :value 123 :key test %}

## Sending promotion code information to Currents

You can combine message_extras with promotion codes to send promotion code information to Currents. Use the capture tag to store the promotion code in a variable, then reference that variable in message_extras:

```

1
2
3
4
5

```
 | 
```
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}

```
 | 

## Considerations

- Key-values that exceed 1,000 bytes (1 KB) are truncated.
 
- Whitespace counts toward the character count. Note that Braze omits the leading and trailing whitespaces.
 
- The resulting JSON outputs string values only.
 
- You can include Liquid variables as a key or value, but you cannot nest additional Liquid tags inside message_extras.

- For example, you can use the following Liquid: {% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}

## Frequently asked questions

### How can I associate the message_extras field in the send events to my engagement events like opens and clicks?

A dispatch_id is generated and provided in your send events, which you can use as a unique identifier to tie to specific click, open, or delivered events. Query this field in Currents or Snowflake. For more information, see Dispatch ID behavior.

#### Can I use message_extras with in-app messages?

Yes, you can use message_extras in your in-app messages as long as your users’ devices are on the following minimum SDK versions:

   Swift: 8.4.0+     Web: 5.2.0+     Android: 30.4.0+  

- 

New Stuff!
