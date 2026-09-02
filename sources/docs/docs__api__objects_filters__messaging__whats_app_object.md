---
url: https://www.braze.com/docs/api/objects_filters/messaging/whats_app_object
slug: docs__api__objects_filters__messaging__whats_app_object
title: "WhatsApp object"
description: "This reference article explains the different components of the Braze WhatsApp object."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# WhatsApp object

The whats_app object allows you to modify or create WhatsApp messages via our messaging endpoints.

## WhatsApp object

```

1
2
3
4
5
6
7

```
 | 
```
{
 "app_id": (required, string) see App Identifier,
 "subscription_group_id": (required, string) the ID of your subscription group,
 "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
 "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message | list_response_message | flow_response_message),
 "message": (required, object) The message object that must include the required fields based on the selected `message_type`. Below are the specific message structures for each type. Refer to the relevant message type for the required fields and their format.
}

```
 | 

- App identifier

### Message Types

#### template_message

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
{
 "template_name": (required, string) the WhatsApp template name for the message,
 "template_language_code": (required, string) the language code of the WhatsApp template for the message,
 "header_variables": (optional, header variables object) an object to specify header variable values for specified template_name, required if the header has variables; see object specification below,
 "body_variables": (optional, body variable object) an object to specify body variable values for specified template_name, required if the body has variables; see object specification below,
 "button_variables": (optional, button variables object) an object to specify button variable values for specified template_name, required if buttons have variables; see object specification below,
 "header_media_uri": (optional, string) URI to the header media, if the header is of type IMAGE in specified template_name. Only IMAGE and TEXT header types are supported by the messages/send API.
}

```
 | 

important

Media send limitations: Media sends (documents, videos, and other media types) are not supported by the messages/send API. Only TEXT and IMAGE header types are supported for template messages sent through the API. If your WhatsApp template uses a DOCUMENT, VIDEO, or other media type header, you cannot send it using the messages/send API. Use the Campaigns Triggered API or the Braze dashboard to send templates with media headers.

##### Header variables object

The header_variables object lets you specify values for header variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.

note

You can use header_variables only with templates that have TEXT-type headers. For IMAGE headers, use header_media_uri instead. DOCUMENT, VIDEO, and other media header types are not supported by the messages/send API.

header_image_uri is used only for response message types (such as quick_reply_response_message), not template messages.

```

1
2
3

```
 | 
```
{
 "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}

```
 | 

Currently, only zero or one header variables can be specified.

###### Example

```

1
2
3

```
 | 
```
{
 "0": "Check it out!"
}

```
 | 

##### Body variables object

The body_variables object lets you specify values for body variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.

```

1
2
3
4

```
 | 
```
{
 "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
 "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}

```
 | 

###### Example

```

1
2
3
4

```
 | 
```
{
 "0": "Check it out!",
 "1": "It's pretty neat."
}

```
 | 

##### Button variables object

The button_variables object lets you specify values for button variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.

```

1
2
3

```
 | 
```
{
 "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}

```
 | 

Currently, only one button variable can be specified, which is the path component of a call-to-action URL. The variable index must match the CTA URL button index in the template. For example, if your CTA button is the second button in your template, use variable index “1”.

###### Example

```

1
2
3

```
 | 
```
{
 "1": "/marketing/promotion123"
}

```
 | 

### Response Messages

#### text_response_message

```

1
2
3
4

```
 | 
```
{
 "body": (required, string) the body of the message to send,
 "preview_url": (optional, boolean) whether WhatsApp should render a preview of links included in body
}

```
 | 

##### Example

```

1
2
3
4

```
 | 
```
{
 "body": "Check out our new deals at https://braze.com",
 "preview_url": true
}

```
 | 

#### text_image_response_message

```

1
2
3
4

```
 | 
```
{
 "image_uri": (required, string) the uri of the image to send,
 "caption": (optional, string) the caption for the image being sent
}

```
 | 

##### Example

```

1
2
3
4

```
 | 
```
{
 "image_uri": "https://braze.com/promotion.jpg",
 "caption": "This won't last for long, check it out!"
}

```
 | 

#### quick_reply_response_message

```

1
2
3
4
5
6
7

```
 | 
```
{
 "body": (required, string) the body of the message to send,
 "header_image_uri": (optional, string) the URI of the image to send as the message header (only valid if header_text not present),
 "header_text": (optional, string) the text to send as the message header (only valid if header_image_uri not present),
 "footer": (optional, string) the footer of the message to send,
 "buttons": (required, array) array of Button objects. Will render in message based on order in array.
}

```
 | 

##### Button object

```

1
2
3

```
 | 
```
{
 "text": (required, string) the text of the button
}

```
 | 

###### Example

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
{
 "body": "Want to keep hearing from us?",
 "buttons": [
 {
 "text": "Yes!"
 },
 {
 "text": "No thanks"
 }
 ]
}

```
 | 

#### list_response_message

The list_response_message type allows you to send a list-based message in WhatsApp. This message type includes a list of items that the recipient can interact with.

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
{
 "header": (optional, string) the header of the message to send,
 "body": (required, string) the body of the message to send,
 "footer": (optional, string) the footer of the message to send,
 "list": (required, object) the list object that contains:
 "list_button_text": (required, string) the text that will appear on the list button,
 "list_sections": (required, array) an array of List Section Objects
}

```
 | 

#### List Section Object

```

1
2
3
4

```
 | 
```
{
 "section_title": (required, string) The title of the section,
 "list_rows": (required, array) An array of List Row Objects
}

```
 | 

#### List Row Object

```

1
2
3
4

```
 | 
```
{
 "row_title": (required, string) The title of the row,
 "row_description": (optional, string) The description for the row
}

```
 | 

##### Constraints

- list_sections: Must have at least one section.
 
- list_rows: A maximum of 10 rows can be included across all sections.
 
- row_description: Optional for each row.

##### Example

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
25
26
27
28
29
30
31
32
33
34

```
 | 
```
{
 "body": "Here is a list of options to choose from:",
 "list": {
 "list_button_text": "Choose an option",
 "list_sections": [
 {
 "section_title": "Section 1",
 "list_rows": [
 {
 "row_title": "Option 1"
 },
 {
 "row_title": "Option 2",
 "row_description": "Description for Option 2"
 }
 ]
 },
 {
 "section_title": "Section 2",
 "list_rows": [
 {
 "row_title": "Option 3"
 },
 {
 "row_title": "Option 4"
 },
 {
 "row_title": "Option 5"
 }
 ]
 }
 ]
 }
}

```
 | 

#### flow_response_message

The flow_response_message type allows you to send a flow-based message in WhatsApp. This message type includes an interactive flow that the recipient can complete.

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

```
 | 
```
{
 "header_text": (optional, string) the header text of the message to send,
 "body": (required, string) the body of the message to send,
 "footer": (optional, string) the footer of the message to send,
 "flow_button": (required, object) the flow button object that contains:
 "caption": (required, string) the text that will appear on the flow button,
 "flow_id": (required, string) the unique identifier of the WhatsApp Flow,
 "generate_custom_attribute": (optional, boolean) whether to save flow response on the user profile and generate a custom attribute upon responding to this flow message
}

```
 | 

##### Flow Button Object

```

1
2
3
4

```
 | 
```
{
 "caption": (required, string) The text displayed on the button,
 "flow_id": (required, string) The ID of the flow
}

```
 | 

##### Constraints

- flow_button: Must include both caption and flow_id.
 
- caption: Maximum 20 characters.
 
- flow_id: Must be a valid published Flow ID.

##### Example

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
{
 "body": "Please complete your order details",
 "flow_button": {
 "caption": "Start Order",
 "flow_id": "594425479261596"
 },
 "generate_custom_attribute": true
}

```
 | 

- 

New Stuff!
