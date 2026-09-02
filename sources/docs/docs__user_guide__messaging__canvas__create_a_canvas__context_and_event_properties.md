---
url: https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties
slug: docs__user_guide__messaging__canvas__create_a_canvas__context_and_event_properties
title: "Context and event properties"
description: "This reference article describes the differences between context and event properties, and when to use each property."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Context and event properties

This reference article covers information about context and event_properties, including when to use each property and the differences in behavior. 

 For information about custom event properties in general, check out Custom events properties.

important

Canvas entry properties are part of Canvas context variables. This means canvas_entry_properties is referenced as context. Each context variable includes a name, data type, and a value that can include Liquid. Currently, canvas_entry_properties are backwards compatible. For more details, see Context and Canvas context object.

Context properties and event properties function differently within your Canvas workflows. Properties of events or API calls that trigger a user’s entry into a Canvas are known as context. Properties of events that occur as a user moves within a Canvas journey are known as event_properties. The key difference is context focuses on more than just events by also accessing the properties of entry payloads in API-triggered Canvases.

Refer to the following table for a summary of differences between context and event properties.

   | 
 Context properties | 
 Event properties | 

 Liquid | 
 context | 
 event_properties | 

 Persistence | 
 Can be referenced by all Message steps for the duration of a Canvas built using Canvas. | 
 - Can only be referenced once. 
 - Cannot be referenced by any subsequent Message steps. | 

 Canvas behavior | 
 Can reference context in any step of a Canvas. For post-launch behavior, refer to Editing Canvases after launch. | 
 - Can reference event_properties in the first Message step after an Action Paths step where the action taken is a custom event or purchase event. 
 - Cannot be after the Everyone Else path of the Action Paths step. 
 - Can have other non-Message components in between the Action Paths and Message steps. If one of these non-Message components is an Action Paths step, the user can go through that action path’s Everyone Else path. | 

Original Canvas editor details

You can no longer create or duplicate Canvases using the original editor. Note that Canvas Context is not supported in the original Canvas editor, so this section is available for reference when using Canvas entry properties and event properties for the previous Canvas workflow.

Canvas entry properties:

- Must have persistent entry properties turned on.
 
- Can only reference canvas_entry_properties in the first full step of a Canvas. The Canvas must be action-based or API triggered.

Entry properties:

- Can reference event_properties in any full step that uses action-based delivery in a Canvas.
 
- Cannot be used in scheduled full steps other than the first full step of an action-based Canvas. However, if a user is using a Canvas component, the behavior follows the current Canvas workflow rules for event_properties.

Event properties:

- Cannot use event_properties in the lead Message step. Instead, you must use canvas_entry_properties or add an Action Paths step with the corresponding event before the Message step that includes event_properties.

## Things to know

- Context is only available for reference in Liquid. To filter on the properties within the Canvas, use event property segmentation instead.
 
- For in-app message channels, you can reference context and event_properties in a Canvas. event_properties can be accessed when included in the first Canvas step because it’s trigger-based.
 
- You can’t use event_properties in the lead Message step. Instead, you can use context or add an Action Paths step with the corresponding event before the Message step that includes event_properties.
 
- When an Action Path step contains a “Sent an SMS Inbound Message” or “Sent a WhatsApp Inbound Message” trigger, the subsequent Canvas steps can include an SMS or WhatsApp Liquid property. This mirrors how event properties work in Canvases. This way you can leverage your messages to save and reference first-party data on user profiles and conversational messaging.

note

Audience eligibility is evaluated once at Canvas entry. If a user is merged during entry, the identified user continues through the Canvas and is not re-evaluated against the Canvas segment criteria.

tip

You don’t need a Context step to reference properties from the triggering event in Audience Paths or Decision Split steps. You can reference the properties directly in the filter groups with the Context Variable filter. Make sure to select the correct data type.

### Timestamps for triggers

If you’re using timestamps with a datetime type from events that trigger action-based Canvases, which are referenced using context, timestamps are normalized to UTC.

Given this behavior, Braze strongly recommends you use a Liquid timezone filter like the following example to guarantee that your messages are sent with your preferred timezone.

```

1

```
 | 
```
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}

```
 | 

## Use case

To further understand the differences for context and event_properties, let’s consider this scenario where users enter an action-based Canvas if they perform the custom event “add item to wishlist”.

Context is configured in the Entry Schedule step of creating a Canvas and correspond to when a user enters a Canvas. Context can also be referenced in any Message step.

In this Canvas, we have a user journey that begins with an Action Paths step to determine if a user has added an item to their wishlist. From here, if the user has added an item, they experience a delay before receiving a message “New item in your wishlist!” from the Message step.

The first Message step in a user journey has access to the custom event_properties from your Action Paths step. In this case, we’re able to include {{event_properties.${property_name}}} in this Message step as part of our message content. If a user doesn’t add an item to their wishlist, they go through the Everyone Else path, meaning the event_properties can’t be referenced and reflects an invalid settings error.

Note that you’ll only have access to event_properties if your Message step can be traced back to a non-Everyone Else path in an Action Paths step. If the Message step is connected to an Everyone Else path but can be traced back to an Action Paths step in the user journey, then you also still have access to event_properties. For more information on these behaviors, see Message step.

- 

New Stuff!
