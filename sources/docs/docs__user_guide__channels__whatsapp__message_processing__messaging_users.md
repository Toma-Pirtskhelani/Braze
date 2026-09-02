---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/messaging_users
slug: docs__user_guide__channels__whatsapp__message_processing__messaging_users
title: "User messages"
description: "This reference article covers how Braze will go about handling user messages."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# User messages

WhatsApp is a two-way communication channel. Not only can your brand send users messages, but they can engage in conversations using templated campaigns and Canvases. There are various ways to do this, including WhatsApp quick replies, list messages, and trigger words. Quick reply and list message calls-to-action (CTAs) are a great way to encourage user engagement with your WhatsApp messaging.

## Action-based triggers

Both campaigns and Canvases can start, branch, and have mid-journey changes from an inbound WhatsApp message (a user messaging your WhatsApp), such as a trigger word.

Ensure that your trigger word matches what you are expecting from users.

Things to know:

- Each letter of your trigger word must be capitalized when configured. Braze does not require inbound trigger words sent by users to be capitalized. For example, messaging “jOin2023” will still trigger the Canvas or campaign.
 
- If no trigger word is specified on the entry schedule action-based trigger, the campaign or Canvas will run for ALL inbound WhatsApp messages. This includes messages that have matched phrases across active campaigns and Canvases, in which case the user will receive two WhatsApp messages.

- campaign
 
- canvas

## Unrecognized responses

We recommend that you include an option for unrecognized responses on interactive Canvases. This guides users to understand what are available prompts and sets expectations for the channel. Expectation management can be especially helpful if you have WhatsApp channels with live agent chat.

- In the action step, after creating the action groups for the custom filter phrases, add an additional action group for “Send WhatsApp message”, but do not check Where the message body. This will catch all unrecognized user responses, similar to an “else” clause.
 
- We recommend following up with a WhatsApp message informing the user that this channel is not manned and guiding them to a support channel if needed.

## Quick replies

Quick replies appear as clickable button options within the conversation but act as if a user replied with text. Braze then processes these as inbound messages, and can send back set responses based on the button clicked. Use the “Inbound WhatsApp message action” step when creating and filtering responses from your users.

### Configure the quick reply experience in Canvas

#### Step 1: Build out CTAs

First, build out your Quick Reply CTAs in the WhatsApp Message Template Manager within a message template.

Once your template has been submitted and approved by WhatsApp, you can use it to build a Canvas within Braze.

tip

You can build the Canvas before receiving the approval on your message template.

#### Step 2: Build your Canvas

Next, build a Canvas with a message step that includes your created template.

Create an action step that follows the message step. Create one group per quick reply option in this action step.

For each quick reply option group, specify the exact text as the button you are matching. Note that the keywords must be in uppercase.

If you would like a default response for users who respond to the message with text instead of quick replies, create an additional group with no matching message body.

Continue building the Canvas as you would otherwise from this point forward.

### Responses

You will most likely want a reply message for each response. We recommend having a catch-all option for responses outside the bounds of quick replies (such as for customers who respond with a general message rather than a predetermined prompt). For example, “We’re sorry, we didn’t recognize your response. For support issues, please message ."

Note that you can use any subsequent actions that the Braze Canvas offers, such as messages in response, user profile updates, or Braze-to-Braze webhooks.

## List messages

List messages appear as a body message with a list of clickable options. Each list can have multiple sections, and each list can have up to 10 rows.

### Configure the list message experience in Canvas

#### Step 1: Create or edit an existing action-based Canvases

You can only add WhatsApp list messages to Canvases that are action-based, as they need to be in response to a user message.

#### Step 2: Create a WhatsApp Message step

Add a WhatsApp Message step, and then select the response message layout of List Message.

Add a List button name that users will select to display your list. Then, use the fields in List content to create your list:

- Section: Add up to 10 sections to group and organize your list items. For example, a clothing retailer could use sections to organize by seasonal styles (like spring, summer, autumn, and winter) or clothing items (like tops, bottoms, and shoes).
 
- Row: Add up to 10 rows, or list items, across all sections.
 
- Row description (optional): Add an optional description to all rows (list items).

Change the order of sections and rows by selecting and dragging the icon next to their names.

Back in the Canvas composer, add an Action path after the Message step that has a group for each list response. In each group:

- Add a trigger for Sent inbound WhatsApp subscription group and select the respective WhatsApp subscription group.
 
- Check the Where the message body checkbox.
 
- Specify the content for one row (or list item).

Continue to build out your Canvas.

### Creating actions paths for long descriptions

If you have row descriptions, you must use Matches regex to specify a row. For example, if you want to specify a row with the description, “Our new style that fits over your favorite pair of ankle boots”, you could use regex with “ankle boots”.

## Considerations

### Timing requirements for response messages

Response messages need to be sent within 24 hours of receiving a user’s message. To help build successful experiences, Braze checks the message logic to confirm there is an upstream inbound user message that unblocks the response message.

For sub-minute replies in two-way Canvas flows, minimize steps between the inbound trigger and the response message send. Canvas architecture, webhook round trips, and User Update batching can add latency. See Minimize response latency for two-way flows.

The following events unblock response messages:

- Inbound message

- Action Path or action-based entry with the trigger Send a WhatsApp inbound message.

- API-triggered entry
 
- Inbound product message

- ecommerce.cart_updated event

### Quick replies and inbound messages outside the 24-hour window

When a user interacts with your business on WhatsApp—including by tapping a quick reply button on an older template message—their action counts as an inbound message. That inbound message opens a new 24-hour customer service window, even if the original template was sent more than 24 hours ago.

In a Canvas with quick reply buttons, users can tap a button days after receiving the welcome template and still enter the correct Action Path. Braze evaluates the Action Path when the inbound message arrives; you don’t need to extend the Action Path duration beyond the default to capture late replies.

The following diagram shows a common quick-reply flow:

```
sequenceDiagram
 participant Brand
 participant User
 Brand->>User: Template message (quick reply buttons)
 Note over User: More than 24 hours pass
 User->>Brand: Taps quick reply (inbound message)
 Note over Brand,User: New 24-hour customer service window opens
 Brand->>User: Response message (within Action Path)

```

#### Things to know

- The response message step must still fall within 24 hours of the user’s inbound message. In most Canvas flows, the response sends immediately after the Action Path evaluates, so this isn’t an issue.
 
- The 24-hour customer service window is different from Canvas conversion events, which can use a window of up to 30 days. Conversion windows control attribution; they don’t affect whether a response message can send.
 
- For billing, see Are WhatsApp response messages free?.

### Filtering by a custom time attribute

If your action-based WhatsApp campaign or Canvas audience depends on a custom time attribute falling within a relative window (for example, between now and the next 24 hours), combine two filters as described in Time.

### Inbound media storage and URL expiration

When a user sends a WhatsApp message that contains media (such as an image, audio file, or document), Braze stores that media in Amazon S3 for 30 days from the time the message is received.

However, the inbound_media_urls Liquid field, which references the URL of that media, is valid for seven days from the time Braze receives the inbound message. Because the URL is generated once at receipt and not regenerated, the seven-day window applies regardless of when you access the field. The shorter of the two limits applies, so in practice, inbound_media_urls should be treated as valid for up to seven days.

note

If you save an inbound_media_urls value to a user custom attribute for later use, be aware of this seven-day expiration. Attempting to access the URL after it has expired results in a broken link.

### Inbound profile name

When Meta includes a display name on an inbound WhatsApp message, Braze exposes it as the {{whats_app.${inbound_profile_name}}} Liquid attribute on that inbound event. This value reflects the name the user set in WhatsApp and may not match CRM profile data. Validate the data before using it in user copy, or use a Canvas User Update step to save it to a profile field for later use. For a full list of WhatsApp Liquid attributes, see Supported personalization tags.

- 

New Stuff!
