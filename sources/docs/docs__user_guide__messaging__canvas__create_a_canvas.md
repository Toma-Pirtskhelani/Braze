---
url: https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas
slug: docs__user_guide__messaging__canvas__create_a_canvas
title: "Create a Canvas"
description: "Learn how to create and launch a Canvas: set up basics, entry schedule, target audience, send settings, build your journey, and more."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create a Canvas

This reference article covers the necessary steps involved in creating, maintaining, and testing a Canvas. Follow this guide, or check out our Canvas Braze Learning course. You can also start from a Braze Canvas template to speed up your setup. For more information, see Canvas templates. To draft a Canvas from a natural-language description, ask Operator.

Expand for original Canvas editor details

You can no longer create or duplicate Canvases using the original Canvas experience. Braze recommends cloning your Canvases to the most current editor.

## Step 1: Set up a new Canvas

First, go to Messaging > Canvas, then select Create Canvas.

The Canvas builder will guide you step-by-step through setting up your Canvas—everything from naming it to setting conversion events and bringing the intended users into your customer journey. Select each of the following tabs to view which settings you can adjust for each builder step.

- basics
 
- entry schedule
 
- target audience
 
- send settings
 
- build canvas
 
- summary

Here, you will set up the basics of your Canvas:

- Name your Canvas
 
- Add teams
 
- Add tags
 
- Assign conversion events, and choose their event types and deadlines

Learn more about the Basics step.

Here, you will decide how and when your users will enter your Canvas:

- Scheduled: This is a time-based Canvas entry
 
- Action-Based: Your user will enter your Canvas after they perform a defined action
 
- API-Triggered: Use an API request to enter users into your Canvas

Learn more about the Entry Schedule step.

Here, you will select your target audience:

- Create your audience by adding segments and filters
 
- Fine-tune Canvas re-entry and entry limits
 
- See a summary of your target audience

Learn more about the Target Audience step.

Here, you will select your Canvas Send Settings:

- Select your subscription settings
 
- Set a send rate limit for your Canvas messages
 
- Enable and set Quiet Hours

Learn more about the Send Settings step.

Here, you will build your Canvas.

Learn how to build your Canvas using the Canvas builder.

Here, you will find the summary of your Canvas details. If you have the Canvas approval workflow turned on, you can approve the listed Canvas details before launching.

### Step 1.1: Start with your Canvas basics

Here, you’ll name your Canvas, assign Teams, and create or add Tags. You can also assign conversion events for the Canvas.

tip

Tag your Canvases so they’re easy to find and build reports out of. For instance, when using Report Builder, you can filter by particular tags.

#### Choose conversion events

Choose your conversion event type, then select the conversions to record. These conversion events will measure the efficiency of your Canvas.

If your Canvas has multiple variants or a control group, Braze will use this conversion event to determine the best variation for achieving this conversion goal. Using the same logic, you can create multiple conversion events.

### Step 1.2: Determine your Canvas entry schedule

You can choose one of three ways in which users can enter your Canvas.

#### Entry schedule types

- scheduled delivery
 
- action-based delivery
 
- api-triggered delivery

With scheduled delivery, users will enter on a time schedule, similarly to how you would schedule a campaign. You can enroll users in a Canvas as soon as it is launched, enter them into your journey at some point in the future, or on a recurring basis (daily, weekly, or monthly).

If you select a monthly recurring schedule, note that some months may not have the selected day. For example, let’s say you set a Canvas to send monthly on the 31st day. In this scenario, Braze sends on the last day of that month, such as April 30, because April 31 doesn’t exist.

In this example, based on the time-based options, users enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

When using local time zone delivery, Braze evaluates entry eligibility twice: first at Samoa time (UTC+13) on the scheduled day, and again at the user’s local time. A user must be eligible for both checks to enter the Canvas. If your entry filters use relative time windows (for example, “more than 2 days ago”), the 24-hour period may not have elapsed at the time of the first check, causing users to enter one day late. To avoid this, use a broader time window, such as at least two days. For more details, see When does Braze evaluate users for local time zone delivery?

With action-based delivery, users will enter the Canvas and begin receiving messages when they take particular actions, such as opening your app, making a purchase, or triggering a custom event.

You can control other aspects of the Canvas behavior from the Entry Audience window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

note

Interact with Canvas Step is not available as an action-based entry trigger for Canvases. It can only be used as a trigger for campaigns. To trigger one Canvas from another, use the Send to Destination Canvas component, or create a Braze-to-Braze webhook that calls the /canvas/trigger/send endpoint.

important

If your action-based Canvas sends messages earlier than expected, check that your custom event timestamp is sent with the current time instead of a backdated time. For example, if an action-based Canvas has a three-hour delay after a user performs a custom event, Braze uses the timestamp sent with the custom event to evaluate that delay. If the timestamp is backdated by more than three hours, Braze treats the delay as already elapsed and sends the message immediately.

With API-triggered delivery, users will enter your Canvas and begin receiving messages after they have been added using the /canvas/trigger/send endpoint via the API. In the dashboard, you can find an example cURL request that does this as well as assign optional context using the context object.

You can use the following endpoints for API-triggered delivery:

- POST: Send Canvas Messages via API-Triggered Delivery
 
- POST: Schedule API-Triggered Canvases
 
- POST: Update Scheduled API-Triggered Canvases

After selecting your delivery method, adjust the settings to match your use case, then continue to setting your target audience.

Deduplicate behavior for Canvases using the original editor

Should the window of re-eligibility be less than the maximum duration of the Canvas, a user will be allowed to re-enter and receive more than one component’s messages. In the edge case where a user’s re-entry reaches the same component as its previous entry, Braze will deduplicate that component’s messages.

If a user re-enters the Canvas, reaches the same component as their previous entry, and is eligible for an in-app message for each entry, the user will get the message twice (depending on in-app message priority) as long as they re-open a session two times.

### Step 1.3: Set your target entry audience

Only the users who match your defined criteria can enter the journey in the Target Audience step, meaning Braze evaluates the target audience for eligibility first before users enter the Canvas journey. For example, if you want to target new users, you can select a segment of users who first used your app less than a week ago.

important

In workspaces with multiple apps, Canvas entry audience eligibility (including segments and filters) is evaluated only when users enter the Canvas, not at individual Message steps. If your workspace has multiple apps and you need to ensure message steps target only users of a specific app, use one of the following approaches in each Message step:

- Turn on Validate audience at message send in the Message step delivery validations and add app-specific segments or filters.
 
- Use Liquid to check the targeted device or app at send time.

Without these safeguards, users who qualified for the journey in one app may receive messages intended for another app if they also use other apps in your workspace.

In Entry Controls, you can limit the number of users every time the Canvas is scheduled to run. For API trigger-based and action-based Canvases, this limit occurs at every UTC hour.

warning

Avoid configuring an action-based campaign or Canvas with the same trigger as the audience filter (such as a changed attribute or performed a custom event). A race condition may occur in which the user is not in the audience at the time they perform the trigger event, which means they won’t receive the campaign or enter the Canvas.

#### Testing your audience

After adding segments and filters to your target audience, you can test if your audience is set up as expected by looking up a user to confirm if they match the audience criteria.

#### Selecting entry controls

Entry controls determine if users are allowed to re-enter a Canvas. You can also limit the number of people who would potentially enter this Canvas by a selected cadence depending on your entry schedule type:

- Scheduled: Lifetime of the Canvas or every time the Canvas is scheduled
 
- Action-Based: Hourly, daily, or the lifetime of the Canvas
 
- API-Triggered: Hourly, daily, or the lifetime of the Canvas

For example, if you have a scheduled Canvas and select Limit entrance volume and set the Maximum entries field to 500,000 users with Every time Canvas is scheduled as the limit cadence, then the Canvas only sends to 500,000 users per scheduled send.

tip

Braze does not recommend selecting Every time the Canvas is scheduled for IP warming as this may lead to increased send volumes.

#### Setting exit criteria

Setting the exit criteria determines which users you want to exit a Canvas. If a user performs the exception event or matches the segments and filters, they won’t receive any further messages.

#### Calculating target population

In the Target Population section, you can view a summary of your audience, such as your selected segments and additional filters, and a breakdown of how many users are reachable per messaging channel. To calculate the exact number of reachable users in your target audience instead of the default estimation, select Calculate exact statistics.

Note that:

- Calculating exact statistics can take a few minutes to run. This function only calculates the exact statistics at the segment level, not at the filter or filter group level.
 
- While exact statistics are loading, a rounded estimate may appear. The exact figure appears in the Reachable Users section when loaded. You can select Show Additional Stats for a detailed breakdown.
 
- For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

To view additional statistics, such as the average lifetime revenue for targeted users, select Show Additional Statistics.

#### Why the target audience count could differ from the reachable users count

The target population size that is displayed in a campaign or Canvas may differ from the reachable audience size for a segment, even if you’re directly adding that segment into your campaign or Canvas without additional filters. 
This may happen for several reasons:

- When a Global Control Group applies to a campaign or Canvas, users in that Global Control Group are excluded in the reachable users count.
 
- The target population size on a campaign or Canvas excludes users that aren’t contactable through various message channels; the behavior differs from channel to channel. For example, the reachable audience for a campaign or Canvas excludes users who are unsubscribed, marked as spam (for emails), or hard bounced (for emails). The segment itself, however, only excludes opt-outs when showing the estimated number of email reachable users.
 
- Braze only sends SMS messages to users within the selected subscription group, so the SMS target population for a campaign or Canvas will also exclude any users who aren’t part of your selected subscription group.

### Step 1.4: Select your send settings

Select Send Settings to edit your subscription settings, turn on rate limiting, and to turn on quiet hours. By turning on rate limiting or frequency capping, you can ease the marketing pressure placed on your users and ensure you aren’t over-messaging them.

For Canvases targeting email and push channels, you may want to limit your Canvas so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in status:

- User A is subscribed to email and is push enabled. This user doesn’t receive the email but will receive the push.
 
- User B is opted-in to email but is not push enabled. This user will receive the email but doesn’t receive the push.
 
- User C is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, set the Subscription Settings to send this Canvas to “opted-in users only”. This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default.

These subscription settings are applied on a per-step basis, meaning that there is no effect on the entry audience. So, this setting is used to evaluate a user’s eligibility to receive each Canvas step.

important

With this configuration, do not include any filters in the Target Audience step that limit the audience to a single channel (for example, Foreground Push Enabled = True or Email Subscription = Opted-In).

You can choose to specify quiet hours (the time during which your messages are not sent) for your Canvas. Check Enable Quiet Hours in your Send Settings. Then, select your quiet hours in your user’s local time and whether the message should abort or send at the next available time.

When Send at next available time is selected, quiet hours suppress the message and send it at the next available time outside quiet hours. For example, let’s say quiet hours are set up to prevent messages from being sent between 11:30 am and 2:30 pm in the user’s local time, and a user enters a Message step at 11:35 am. Because this time is within quiet hours, the message is not sent yet, and the user receives the Message step at 2:30 pm, which is after quiet hours.

## Step 2: Build your Canvas

tip

Save time and streamline your Canvas creation by using Braze Canvas templates! Browse our library of pre-built templates to find one that fits your use case and customize it to meet your specific needs. For more information, see Canvas templates.

### Step 2.1: Add a variant

Select Add Variant, then add a new variant to your Canvas. Variants represent a journey that your users will take and can contain multiple steps and branches.

You can add additional variants by selecting the plus button. When you add new variants, you’ll be able to adjust how your users will be distributed between them so that you can cross-compare and analyze the efficacy of different engagement strategies.

tip

By default, Canvas variant assignment is determined by a deterministic hash of the user ID and Canvas ID (not a user’s random bucket number), meaning that a given user is consistently assigned to the same variant on re-entry, as long as the variant distribution percentages remain unchanged. If you adjust the variant distribution after launch, users may be assigned to different variants when they re-enter the Canvas. 

If you need assignment that stays fixed when distribution percentages change, use a single Canvas variant and route users with an Audience Paths step. At the start of the journey, use a User Update step to store a random number in a custom attribute, then filter on that attribute in Audience Paths.

Expand for steps

- Create a Number custom attribute to store your random number. Name it something easy to locate, like lottery_number or random_assignment. In your dashboard, go to Data Settings > Custom Attributes.

- Use a single Canvas variant (or add the same User Update step to each variant). Add a User Update step at the beginning of the journey. This step generates and stores the random number before users reach your Audience Paths step.

- In the User Update step, select the Advanced JSON Editor. Use the {% random %} tag to generate the number. For details, see Send messages with a random number. For example, {% random 10 %} returns an integer from 0 through 9. Set the custom attribute from step 1 using JSON like this:

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

```
 | 
```
{% if {{custom_attribute.${lottery_number}}} == blank %}
{% capture lottery_number_str %}{% random 10 %}{% endcapture %}
{
 "attributes": [
 {
 "lottery_number": {{ lottery_number_str | plus: 0 }}
 }
 ]
}
{% endif %}

```
 | 

The {% if %} block sets the number only when the attribute is blank, so users keep the same assignment when they re-enter the Canvas.

- Add an Audience Paths step after the User Update step. In each audience group, add filters based on your custom attribute instead of using variant distribution percentages.

For example, if you used {% random 10 %}, one group might use lottery_number is less than 4, another is more than 3 and less than 7, and a third is more than 6 and less than 10.

### Step 2.2: Add Canvas steps

You can add more steps to your Canvas workflow by dragging and dropping components from the Components sidebar. Or, select the plus button to add a component with the popover menu.

tip

As you begin to add more steps, you can switch up the zoom level to focus in on details or take in the entire user journey. Zoom in with Shift + + or zoom out with Shift + -.

important

You can add up to 200 steps in a Canvas. If your Canvas exceeds 200 steps, loading issues may occur.

#### Maximum duration

As your Canvas journey increases in steps, the maximum duration is the longest possible time a user can take to complete this Canvas. This is calculated by adding the delays and trigger windows of each step for each variant for the longest path. For example, if your Canvas has a Delay step with a delay of 3 days and a Message step, the maximum duration of your Canvas will be 3 days.

#### Editing a step

Looking to edit a step in your user journey? Check out how to do this depending on your Canvas workflow!

You can edit any step in your Canvas workflow by selecting any of the components. For example, let’s say you want to edit your first step, a Delay component, in your workflow to a specific day. Select the step to view its settings and adjust your delay to March 1. This means on March 1, your users will move to the next step in your Canvas.

Or you can quickly edit and adjust the Action Settings of your Action Paths step to hold users for a window of time. This prioritizes their next path based on the actions during this evaluation period.

The lightweight components in Canvas allow for a simple editing experience, so adjusting the finer details of your Canvas is made easier.

#### Messages in Canvas

Edit the messages in a Canvas component to control messages that a particular step will send. Canvas can send email, mobile, and web push messages, and webhooks to integrate with other systems. Similar to campaigns, you can use certain Liquid templating to personalize your messages.

tip

Did you know you can include Canvas component names in your messages and link templates?

Use the campaign.${name} Liquid tag in Canvas to display the current Canvas component name.

The Message component manages the messages sent to users. You can select your Messaging Channels and adjust Delivery Settings to optimize your Canvas messaging. For more details on this component, check out Message.

Select Done after you’ve finished configuring your Canvas component.

- canvas entry properties
 
- event properties

The context object is configured in the Entry Schedule step of creating a Canvas and indicates the trigger that enters a user into a Canvas. These properties can also access the properties of entry payloads in API-triggered Canvases. Note that the context object can be up to 50 KB.

Use the following Liquid when referencing these properties created upon entering the Canvas: context.${property_name} . Note that the events must be custom events or purchase events to be used this way.

For example, consider the following request: \"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}. You could add the word “shoes” to a message with this Liquid {{context.${product_name}}}.

Event properties are the properties set by you on custom events and purchases. These event_properties can be used in campaigns with action-based delivery as well as Canvases.

In Canvas, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. Use this Liquid {{event_properties.${property_name}}} when referencing these event_properties. These events must be custom events or purchase events to be used this way in the Message component.

In the first Message step following an Action Path, you can use event_properties related to the event referenced in that Action Path. You can have other steps (that are not another Action Paths or Message step) in between this Action Paths step and the Message step. Note that you’ll only have access to event_properties if your Message step can be traced back to a non-Everyone Else path in an Action Path step

### Step 2.3: Edit connections

To move a connection between steps, select the arrow connecting the two components and select a different component. To remove the connection, select the arrow followed by Cancel Connection in the footer of the Canvas composer.

If a single variant has multiple branches with the same audience and send time, Braze does not guarantee an even split across those branches. Distribution may favor the branch that was created first. For an even split, use Random Bucket Number filters on each branch. For more information, see What happens if the audience and send time are identical for a Canvas that has one variant, but multiple branches?.

## Step 3: Add a control group

You can add a control group to your Canvas by selecting the plus button to add a new variant.

Braze will track the conversions for users who are placed into the control group, although they will not receive any messages. To preserve an accurate test, we will track the number of conversions for your variants and the control group for exactly the same amount of time, as shown on the conversion event selection screen.

You can adjust the distribution between your messages by double-clicking the Variant Name headers.

In this example, we have our Canvas divided into two variants. Variant 1 has 70% of the users. The second variant is a control group with the remaining 30% of users.

### Optimize Canvas variants with BrazeAI

For a Canvas with multiple top-level variants, turn on Optimize with BrazeAI™ to automatically adjust the percentage of users entering each variant. BrazeAI™ uses variant performance to maximize the expected number of conversions.

Add at least two variants and one conversion event. Then, select a variant percentage to open Edit Variant Distribution and turn on Optimize with BrazeAI™.

After the initial conversion deadline, BrazeAI™ reviews performance every 12 hours and shifts more users toward the variant that drives the most conversions. When the optimization identifies a decisive winner, all future eligible users enter that variant.

This optimization works best for Canvases that have new users entering frequently.

## Step 4: Save and launch

After you’re done creating your Canvas, select Launch Canvas to save and launch your Canvas. After you’ve launched your Canvas, you’ll be able to view analytics for your journey as they come in on the Canvas Details page.

You can also save your Canvas as a draft if you need to come back to it.

tip

Need to make edits to your Canvas after launch? Well, you can! Check out Editing Canvases after launch for more information.

- 

New Stuff!
