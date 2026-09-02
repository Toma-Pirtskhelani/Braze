---
url: https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step
slug: docs__user_guide__messaging__canvas__canvas_components__message_step
title: "Message"
description: "This reference article covers how to create a stand-alone message using the Message step."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Message

Message steps allow you to add a standalone message where you want in your Canvas.

## Create a message

To create a Message component, first add a step to your Canvas. Drag and drop the component from the sidebar, or select the plus button at the bottom of a step and select Message.

### Step 1: Select your messaging channel

You can select from the following messaging channels:

- Banners
 
- Content Cards
 
- Email
 
- LINE
 
- Push notifications
 
- SMS/MMS/RCS
 
- In-app messages
 
- Webhook
 
- WhatsApp

### Step 2: Edit delivery settings

Next, you can edit settings for Intelligent Delivery, Quiet Hours overrides, and delivery validation.

#### Intelligent Timing

You can enable Intelligent Timing with a fallback option when a user’s profile does not have enough data to calculate an optimal time. We recommend enabling Intelligent Timing and rate limiting as an additional check for any delays between users entering the Message step and the actual message sending.

Select Using Intelligent Timing in the Delivery Settings tab. Here, you can select either the most popular time or a specific fallback time. If Quiet Hours are enabled, the Message step also allows you to override this setting.

#### Delivery validations

Delivery validations provide an additional check at message send to confirm your audience still meets your criteria. We recommend using it when Quiet Hours, Intelligent Timing, or rate limiting are enabled. Select Validate audience at message send, then add a segment or additional filters. If a user doesn’t meet the validations, choose whether they exit the Canvas or advance to the next step.

Delivery validations evaluate user profile criteria at send time. App-related filters check whether a user recently used or ever used a specific app, but they don’t confirm which app a user is using in their current session.

If your workspace has multiple apps and a Message step should target a specific app, use one of the following approaches instead:

- When composing the message, specify your delivery platforms, such as Mobile Apps or Web Browsers.
 
- Use Liquid to check the targeted device or app at send time:

- {{targeted_device.${platform}}} evaluates the platform for the user’s current session. For more information, see Targeted device information.
 
- {{app.${api_id}}} evaluates which app is requesting the message. Combine this tag with abort_message() to prevent sends to the wrong app. For more information, see Targeted app information.

## How users advance

All users who enter the Message step advance to the next step when any one of the following conditions is met:

- Any message is sent
 
- A message is frequency capped and not sent
 
- A message is aborted
 
- A user is not reachable by channel, so the message is not sent
 
- A user does not meet the criteria in Delivery validations

If an action-based Canvas is triggered by an inbound SMS message, you can reference SMS properties in the first step (Message step) or a Message step that is nested under an Action Path step. For example, in the Message step, you could use {{sms.${inbound_message_body}}} or {{sms.${inbound_media_urls}}}.

## Reference context properties

important

Canvas entry properties are part of Canvas context variables. This means canvas_entry_properties is referenced as context. Each context variable includes a name, data type, and a value that can include Liquid. Currently, canvas_entry_properties are backwards compatible. For more details, see Context and Canvas context object.

Entry properties are configured in the Entry Schedule step of creating a Canvas and will indicate the trigger that enters a user into a Canvas. These properties can also access the properties of entry payloads in API-triggered Canvases. Note that the context object has a maximum size limit of 50 KB.

Entry properties can be used in Liquid in any Message step. Use the following Liquid when referencing these entry properties: {context.${property_name}}. Events must be custom events or purchase events to be used this way.

note

For in-app message channels specifically, context can only be referenced in Canvas.

Use the following Liquid when referencing these entry properties: context.${property_name}. Note that the events must be custom events or purchase events to be used this way.

For example, consider the following request: \"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}. You could add the word “shoes” to a message with the Liquid {{context.${product_name}}}.

You can also leverage persistent entry properties in any Message step to guide your users through personalized steps throughout your Canvas workflow.

### Event properties

Event properties refer to the properties that you set for custom events and purchase events. These event properties can be used in campaigns with action-based delivery as well as Canvases.

In Canvas, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. For example, when referencing event_properties, use this Liquid snippet: {{event_properties.${property_name}}}

important

event_properties can’t be used independently of Action Paths steps.

In the first Message step following an Action Path, you can use event_properties related to the event referenced in that Action Path. You can have other steps (that are not another Action Paths or Message step) in between this Action Paths step and the Message step. Note that you’ll only have access to event_properties if your Message step can be traced back to a non-Everyone Else path in an Action Path step.

important

You can’t use event_properties in the lead Message step. Instead, you must use context or add an Action Paths step with the corresponding event before the Message step that includes event_properties.

Expand for original Canvas editor

You can no longer create or duplicate Canvases using the original editor. This section is available for reference only.

- event_properties can’t be used in scheduled full steps. However, you can use event_properties in the first full step of an action-based Canvas, even if the full step is scheduled.
 
- context can be referenced only in the first full step of a Canvas.
 
- For in-app message channels specifically, context can be referenced in the original Canvas editor if you have persistent entry properties enabled as part of the previous early access.

## Analytics

Refer to the following table for definitions of Message component metrics:

 Metric | 
 Description | 

 Entries | 
 The number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Message step twice, two entries will be recorded. | 

 Proceeded to Next Step | 
 The number of entries that proceeded to the next step in the Canvas. | 

 Sends | 
 The total number of messages the step has sent. If your Canvas re-eligibility and a user enters a Message step twice, two entries will be recorded. | 

 Unique Recipients | 
 The number of users who have received messages from this step. | 

 Primary Conversion Event | 
 The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. You define this event when building the campaign. | 

 Revenue | 
 The total revenue in dollars from campaign recipients within the set primary conversion window. | 

- 

New Stuff!
