---
url: https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context
slug: docs__user_guide__messaging__canvas__canvas_components__context
title: "Context"
description: "This reference article covers how to create and use Context steps in your Canvas."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Context

Context steps let you create and update one or more variables for a user as they move through a Canvas. For example, if you have a Canvas that manages seasonal discounts, you can use a context variable to store a different discount code each time a user enters the Canvas.

## How it works

Context steps allow you to create and use temporary data during a user’s journey through a specific Canvas. This data exists only within that Canvas journey and doesn’t persist across different Canvases or outside the session.

Context variables exist only for that specific Canvas journey. They don’t change the user’s profile permanently and don’t appear in other Canvases. This makes them ideal for temporary information that’s relevant only to a specific campaign or workflow.

tip

For a full reference on context variables, including data types, usage, and best practices, see the Context variables reference.

Within a Context step, you can define or update up to 10 context variables. These variables can be used to personalize delays, segment users dynamically, and enrich messaging throughout the Canvas. For example, you could create a context variable for a user’s scheduled flight time, then use it to set personalized delays and send reminders.

You can set context variables in two ways:

- At Canvas entry: Properties from the custom event or API trigger are automatically populated as context variables.
 
- In a Context step: Define or update context variables manually by adding a Context step.

Each context variable requires a name, a data type, and a value (set using Liquid or the Add Personalization tool). When defined, you can reference context variables throughout the Canvas using Liquid, such as {{context.${flight_time}}}. In the Context variable name field, you can also enter the context variable name or select it from the dropdown in the step editor. For details, see Context variables reference.

Each Canvas entry redefines context variables based on the latest entry data and Canvas setup, allowing users to have multiple active journeys with their own context. For example, if a customer has two upcoming flights, they’ll have two separate journey states running simultaneously—each with its own flight-specific context variables like departure time and destination. This allows you to send personalized reminders about their 2 pm flight to New York while sending different updates about their 8 am flight to Los Angeles tomorrow, so that each message stays relevant to the specific booking.

### User processing and batching

Context steps process users in batches to optimize performance. When users enter a Context step, Braze processes them in batches of 1,000 users by default. These batches are processed in parallel, but within each batch, users are processed sequentially.

This means:

Example: If 3,500 users enter a Context step with Connected Content that takes 650ms per user:

- Braze creates 4 batches of users (1,000, 1,000, 1,000, and 500 users in this example).
 
- Each batch processes users sequentially, so a batch of 1,000 users takes approximately 10.8 minutes (650 seconds; 1,000 × 650ms).
 
- Batches complete at different times, so users trickle into the next step as their batch finishes.
 
- The first users may reach the next step several minutes before the last users, depending on batch size and Connected Content response times.

Without Connected Content, Context steps process much faster because there are no external API calls to wait for.

## Considerations

- You can define up to 10 context variables per Context step.
 
- Each variable requires a unique name (letters, numbers, underscores only, up to 100 characters).
 
- The total size of all variables in a step cannot exceed 50 KB.
 
- Variables passed in using API triggers share the same namespace as those created in Context steps; redefining a variable in a Context step overrides the API value.

For more details and advanced usage, see Context variables reference.

## Creating a Context step

tip

You don’t need a Context step to reference properties from the triggering event in Audience Paths or Decision Split steps. You can reference the properties directly in the filter groups with the Context Variable filter. Make sure to select the correct data type.

### Step 1: Add a step

Add a step to your Canvas, then drag and drop the component from the sidebar, or select the plus button and select Context.

### Step 2: Define the variables

note

You can define up to 10 context variables for each Context step.

To define a context variable:

- Give your context variable a name.
 
- Select a data type.
 
- Write a Liquid expression manually or use Add Personalization to create a Liquid snippet from pre-existing attributes.
 
- Select Preview to check the value of your context variable.
 
- (Optional) To add additional variables, select Add Context variable and repeat steps 1-4.
 
- When you’re finished, select Done.

Now you can use your context variable anywhere you use Liquid, such as in Message and User Update steps, by selecting Add Personalization. In the Context variable name field, you can also enter the context variable name or select it from the dropdown in the step editor. For a full walkthrough, see Context variables reference.

important

When referencing context variables, always use the format {{context.${variable_name}}}.

### Context variable filters

You can create filters using context variables in Audience Paths and Decision Split steps.

To route users based on an Agent step response, add the Agent step before your Audience Paths or Decision Split step. The Agent step stores its output in Canvas context, which you can evaluate with context variable filters in those branching steps.

If the agent returns an object and you want to filter on a nested property, enter the path in the Context variable name field using dot notation instead of only the top-level variable name (for example, intent_agent.persona when persona is nested under intent_agent).

For filter setup, comparison logic, and advanced examples, see Context variables reference.

important

Choosing between “Day of year” and “Time” filter types: When filtering context variables that contain dates, choose the correct comparison type based on whether the date repeats every year. Use “Day of year” only when the year is not included in the value the context variable produces.

- Use “Day of year” when the date repeats every year (for example, birthdays, anniversaries, or holidays like Christmas). This comparison type calculates based on the day of the year (1-365/366), ignoring the year component.
 
- Use “Time” when the date is an absolute date that doesn’t repeat (for example, contract end dates, appointment dates, or subscription renewal dates). This comparison type calculates based on the full timestamp, including the year.

Using “Day of year” for absolute dates can produce incorrect or unexpected results because the calculation ignores the year component. For example, if you’re comparing a future contract end date in April to determine if it’s within 63 days, using “Day of year” may incorrectly match dates because it only compares day numbers (119 vs 359) without considering that April is actually 188 days away.

## Previewing user paths

We recommend testing and previewing your user paths to make sure your messages are sent to the right audience and context variables are evaluated to the expected outcomes.

note

If you’re previewing your Canvas in the Preview & Test Send section of the editor, the timestamp in the test message preview does not standardize to UTC because this panel generates previews as strings. This means if a Canvas is set up to accept a time object, the message preview does not accurately preview what occurs when the Canvas is live. To test your Canvas most accurately, we recommend previewing user paths instead.

Be sure to observe any common scenarios that create invalid context variables. When previewing your user path, you can view the outcomes of personalized Delay steps using context variables, and any audience or decision step comparisons that match users to any context variables.

If the context variable is valid, you can reference the variable throughout your Canvas. However, if the context variable wasn’t created correctly, future steps in your Canvas won’t perform correctly either. For example, if you create a Context step to assign users an appointment time and set the appointment time’s value to a past date, the reminder email in your Message step does not send.

## Converting Connected Content strings to JSON

When making a Connected Content call in a Context step, JSON returned from the call is evaluated as a string data type for consistency and error prevention. If you want to convert this string into JSON, convert it by using as_json_string. For example:

```

1
2

```
 | 
```
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}

```
 | 

## Troubleshooting

### Invalid context variables

A context variable is considered invalid when:

- A call to an embedded Connected Content fails.
 
- The Liquid expression at runtime returns a value that doesn’t match the data type or is empty (null).

For example, if the context variable data type is Number but the Liquid expression returns a string, it is invalid.

In these circumstances:

- The user advances to the next step.
 
- The Canvas step analytics counts this as Not Updated.

When troubleshooting, monitor the Not Updated metric to check that your context variable is updating correctly. If the context variable is invalid, your users can continue in your Canvas past the Context step, but may not qualify for later steps.

Refer to Data types for the example setups for each data type.

### Delays in sending with Connected Content

All users in a batch are processed before any users advance. After batch processing completes, successful users move to the next step, while failed users are retried separately—successful users don’t wait for retry attempts to succeed before advancing.

#### Retry behavior

In Canvas steps (including Context steps), Braze uses Canvas-specific retry mechanisms rather than the standard Connected Content retry behavior. If a Connected Content call fails:

- For Message steps, Connected Content calls can retry up to five times.
 
- For all other steps, Braze retries the step approximately 13 times with exponential backoff.

If all retries fail, the user exits the Canvas.

The :retry tag used in standard Connected Content doesn’t apply to Connected Content calls made within Canvas steps. Canvas steps have their own retry logic optimized for Canvas workflows.

The time it takes to process all users through a Context step depends on:

- The number of users entering the step
 
- Whether Connected Content is used (and its response time)
 
- The batch size (default 1,000 users per batch)

If your Connected Content endpoint has rate limits, consider that Context steps process users sequentially within each batch, which helps respect rate limits naturally. However, multiple batches are processed in parallel, so ensure your endpoint can handle concurrent requests from multiple batches.

## Time zone consistency standardization

With Canvas Context generally available, all default timestamp event properties in action-based Canvases are in UTC. This change is part of a broader effort to ensure a more predictable and consistent experience when editing Canvas steps and messages. Note that this change impacts all action-based Canvases, whether the specific Canvas is using a Context step or not.

important

In all circumstances, we strongly recommend using Liquid time_zone filters for timestamps to be represented in the desired time zone. You can reference this frequently asked question for an example.

## Frequently asked questions

### What has changed since Canvas Context became generally available?

Now that Canvas Context is generally available, the following details apply:

- All timestamps with a datetime type from trigger event properties in action-based Canvases are in UTC.
 
- This change impacts all action-based Canvases, whether the specific Canvas is using a Context step or not.

#### What is the reason for this change?

This change is part of a broader effort to create a more predictable and consistent experience when editing Canvas steps and messages.

#### Are API-triggered or scheduled Canvases impacted by this change?

No.

#### Does this change impact Canvas entry properties?

Yes, this impacts canvas_entry_properties if the canvas_entry_property is being used in an action-based Canvas and the property type is time. In all circumstances, we recommend using Liquid time_zone filters for timestamps to be represented in the desired time zone.

Here’s an example of how to do this:

 Liquid in Message step | 
 Output | 
 Is this the way to represent time zones correctly in Liquid? | 

 {{canvas_entry_properties.${timestamp_property}}} | 
 2025-08-05T08:15:30:250-0800 | 
 No | 

 {{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}} | 
 2025-08-05 4:15pm | 
 No | 

 {{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}} | 
 2025-08-05 8:15am | 
 Yes | 

#### What is a practical example of how the new timestamp behavior might affect my messages?

Let’s say we have an action-based Canvas that has the following content in a Message step:

```

1

```
 | 
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!

```
 | 

This results in the following message:

```

1

```
 | 
```
Your appointment is scheduled for 2025-08-05 4:15 PM, we’ll see you then!

```
 | 

Because no time zone is specified using Liquid, the timestamp here is in UTC.

To specify a time zone clearly, we can use Liquid time_zone filters like this:

```

1

```
 | 
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!

```
 | 

This results in the following message:

```

1

```
 | 
```
Your appointment is scheduled for 2025-08-05 8:15 AM, we'll see you then!

```
 | 

Because the America/Los Angeles time zone is specified using Liquid, the timestamp here is in PST.

The preferred time zone can also be sent in the event properties payload and used in Liquid logic:

```

1
2
3
4

```
 | 
```
{
 "appointment_time": "2025-08-05T08:15:30:250-0800"
 "user_timezone": "America/Los_Angeles"
}

```
 | 

### How do context variables differ from Canvas entry properties?

Canvas entry properties are included as Canvas context variables. This means you can send Canvas entry properties using the Braze API and reference them in other steps, similar to using a context variable with the Liquid snippet.

### Can variables reference each other in a singular Context step?

Yes. All variables in a Context step are evaluated in a sequence, meaning you could have the following context variables set up:

 Context variable | 
 Value | 
 Description | 

 favorite_cuisine | 
 {{custom_attribute.${Favorite Cuisine}}} | 
 A user’s favorite type of cuisine. | 

 promo_code | 
 EATFRESH | 
 The available discount code for a user. | 

 personalized_message | 
 "Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!" | 
 A personalized message that combines the previous variables. In a Message step, you could use the Liquid snippet {{context.${personalized_message}}} to reference the context variable to deliver a personalized message to each user. You could also use a Context step to save the promo code value and template it in other steps throughout a Canvas. | 

This also applies across multiple Context steps. For example, imagine this sequence:

- An initial Context step creates a variable called JobInfo with the value job_title.
 
- A Message step references {{context.${JobInfo}}} and displays job_title to the user.
 
- Later, a Context step updates the context variable, changing the value of JobInfo to job_description.
 
- All subsequent steps that reference JobInfo now use the updated value job_description.

Context variables use their most recent value throughout the Canvas, with each update affecting all following steps that reference that variable.

- 

New Stuff!
