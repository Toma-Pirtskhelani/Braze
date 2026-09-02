---
url: https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas
slug: docs__user_guide__messaging__canvas__create_a_canvas__canvas_by_channel__in-app_messages_in_canvas
title: "In-app messages in Canvas"
description: "This reference article describes features and nuances specific to in-app messages that you can add to your Canvas to show rich messaging."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# In-app messages in Canvas

You can add in-app messages as part of your Canvas journey to show rich messaging when your customer engages with your app.

## How it works

Before you can use in-app messages in your Canvas, be sure to have a Canvas set up with delay and audience options.

In the Canvas builder, add a Message step and select In-App Message as your Messaging Channel. You can customize when your message expires and which advancement behavior it has.

If your workspace has multiple apps, target the correct app using delivery platforms, {{targeted_device.${platform}}}, or {{app.${api_id}}} Liquid tags—not delivery validations. In-app messages display only when the user opens the targeted app and meets the step’s trigger criteria. For more information, see Delivery validations.

## Adding an in-app message to your user journey

To add an in-app message to your Canvas, do the following:

- Add a Message step to your user journey.
 
- Select In-App Message for your Messaging Channel.
 
- Determine when your message will expire and which advancement behavior it will have.

## Triggered in-app messages

You can select a trigger for your in-app messages to be triggered on session start, or by custom events and purchases.

After any delays pass and the audience options are checked, in-app messages are set to live when a user reaches the Message step. If a user starts a session and performs the trigger event for the in-app message, the user will see the in-app message.

For Canvas steps that have action-triggered entry, users can enter the Canvas mid-session. In-app messages aren’t set to live until a session starts, so if a user is in the middle of a session when they reach the Message step, they won’t receive the in-app message until they start another session and perform the relevant trigger.

## In-app message expiration

You can choose when the in-app message will expire. During this time, the in-app message will sit and wait to be viewed until it has reached the expiry date. After the in-app message is sent, it can be viewed one time.

 Option | 
 Description | 
 Example | 

 A duration after the step is available | 
 Sets the in-app message to expire relative to when the step becomes available to the user. | 
 An in-app message with a two-day expiration would become available when the user enters the Message step and audience options are checked. Any delays before reaching this step would come from preceding Delay steps in your Canvas. The in-app message would then be available for 2 days (48 hours) from when the user enters the step, and during those two days, users may see the in-app message if they open the app. | 

 On a specific date and time | 
 Select a specific date and time when the in-app message will be no longer available. | 
 If you have a sale that ends on November 30, 2024, select this option so that users no longer see the associated in-app message when the sale ends. | 

When a user starts a session, Braze checks whether their eligibility or expiration for in-app messages has changed and sends updated expiration information to their device.

If an in-app message is set to expire on a specific date and time that has already passed when the user reaches the Message step, that user does not receive the in-app message. They will continue through the Canvas according to your advancement behavior for that step.

This often happens when a preceding step, such as a Delay step, keeps users on a longer path. For example, if you launch a Canvas on May 22 with a 72-hour delay followed by an in-app message that expires on May 23 at midnight, users reach the Message step after the expiration time and do not see the in-app message.

### Control groups and A/B testing

When you use Canvas A/B testing with variant paths and a control path, keep in-app message expiry duration settings aligned across paths. If the control path uses a shorter expiry duration than the variant paths, control users may reach the step after expiration, which can lower control impressions compared to variant impressions and skew your test results.

## Use cases

Braze recommends that you consider using this feature in your promotional and onboarding Canvases.

- promotional
 
- user onboarding

Promotions, coupons, and sales often have hard expiration dates. The following Canvas should alert your users at the most opportune times that there is a promotion they may use, and perhaps influence a purchase. This promotion expires on February 28, 2019, at 11:15 am in your company’s time zone.

 Use cases

 Canvas Step | 
 Delay | 
 Audience | 
 Channel | 
 Expiration | 
 Advancement | 
 Details | 

 Day 1: 50% off | 
 None | 
 All from entry | 
 Push | 
 N/A | 
 Advance Audience After Delay | 
 Initial push that alerts your users of the promotion. This is meant to drive users to your app to take advantage of the promotion. | 

 In-app: 50% off | 
 None | 
 All from entry | 
 In-app message | 
 Expires by: 2/28/2019 11:15 AM Company Time | 
 In-App Message Viewed | 
 The user has now opened the app and will receive this message whether or not that was because of the push message before. | 

 50% off reminder | 
 1 day after the user receives the previous step | 
 All from entry 

Filter: Last made a purchase more than one week ago | 
 In-app message | 
 Expires by: 2/28/2019 11:15 AM Company Time | 
 None (last message in Canvas) | 
 The user has received the in-app message in the previous step but has not made a purchase despite being in the app. 

This message is meant to further draw the user to make a purchase using the promotion. | 

The in-app messages expire when the promotion expires to prevent any discrepancies between the messaging and the customer experience.

Your first impression with a user is, perhaps, your most critical one. It can make or break future visits to your app. Your initial communications with your user should be sensibly timed and encourage frequent visits to your app to promote usage.

 Use cases

 Canvas Step | 
 Delay | 
 Audience | 
 Channel | 
 Expiration | 
 Advancement | 
 Details | 

 Welcome email | 
 None | 
 All from entry | 
 Email | 
 N/A | 
 Advance Audience after Delay | 
 Initial email that welcomes your users to a project, membership, or other onboarding program. 

This is intended to drive users to your app to begin their onboarding. | 

 Day 3-6 in-app message | 
 3 days after the user receives the previous step | 
 All from entry | 
 In-app message | 
 Expires: 3 days after the step becomes available | 
 In-App Message Live | 
 If the user has acted upon the email and been driven to the app, they will receive the desired in-app message to continue or remind them of their onboarding and any requirements associated with it. | 

 Day 5 push | 
 2 days after the user receives the previous step | 
 All from entry | 
 Push | 
 N/A | 
 Message Sent | 
 After users have received their in-app message, they will receive a follow-up push to continue their onboarding. | 

These push messages are spaced around an in-app message to make sure the user has visited the app and started their onboarding. This helps prevent any spam or out-of-order messaging that could dissuade users from visiting your app, and instead create a flowing, sensible order to their initial experiences with your app.

## Prioritizing in-app messages

A user can trigger two in-app messages within your Canvas at the same time. When this happens, Braze will adhere to the following priority order to determine which in-app message is displayed.

Select Set exact priority and drag different Canvas steps to reorder their priority for the Canvas. By default, steps earlier in a Canvas variant will display before later steps. After your steps are in your preferred order of prioritization, select Apply sort.

### Making changes to drafts of active Canvases

If you make changes to the in-app message priority in Send Settings of a draft of an active Canvas, these changes are applied directly to the active Canvas when the priority sorter is closed. However, in a Message step, the priority sorter will be updated when the draft is launched since Canvas step settings apply at a step level.

## Advancement behavior

Message steps automatically advance all users who enter the step. Note that it doesn’t wait for the in-app message to trigger or display. There is no requirement to specify message advancement behavior, making configuring the overall step simpler.

When a user enters an in-app message step, they advance out of it immediately instead of being held for the expiration window. In this case, having a Delay step in your user journey can be helpful.

To use the Advance when message sent option, add a separate audience path to filter users who didn’t receive the previous step.

Original Canvas editor

You can no longer create or duplicate Canvases using the original editor. This section is available for reference when understanding how advancement behavior works for steps with in-app messages.

Canvases created in the original editor need to specify an advancement behavior—the criteria for advancement through your Canvas component. Steps with only in-app messages have different advancement options than steps with multiple message types (such as push or email). For in-app messages in the current Canvas workflow, this option is set to always immediately advance the audience.

Action-based delivery is not available for Canvas steps with in-app messages. Canvas steps with in-app messages must be scheduled. Instead, Canvas in-app messages will appear the first time that your user opens the app (triggered by the start session) after the scheduled message in the Canvas component has been sent to them.

If you have multiple in-app messages within one Canvas, a user must start multiple sessions to receive each of those individual messages.

important

When Advance When In-App Message Live is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you do not want the in-app message to be live when the next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.

### Steps with multiple channels

Steps with an in-app message and another channel have the following advancement options:

 Option | 
 Description | 

 Advance When Message Sent | 
 Users must be sent an email, webhook, or push notification, or view the in-app message to advance to subsequent steps in the Canvas. 
 
 If the in-app message expires and the user hasn’t been sent the email, webhook, or push, or hasn’t viewed the in-app message, they will exit the Canvas and will not advance to subsequent steps. | 

 Immediately Advance Audience | 
 Everyone in the step’s audience advances to the next steps after the delay elapses, whether they have seen the noted message or not. 
 
 Users must match the step’s segment and filter criteria to advance to the next steps. | 

important

When Entire Audience is selected, the in-app message will be available until it expires, even if the user has moved to subsequent steps. If you don’t want the in-app message to be live when the next steps in the Canvas are delivered, check that the expiration is shorter than the delay on subsequent steps.

## Trigger actions

You can choose from the following trigger actions to target your users:

- Make Purchase: Target users who make any purchase or a specific purchase
 
- Start Session: Target users who start a session in any app or a specific app
 
- Perform Custom Event: Target users who perform the selected custom event (the custom event must be sent using the SDK).

A user has to enter the Canvas step, start a session, and then perform the trigger to receive an in-app message. This means mid-session updates aren’t supported. For example, if the trigger is to start a session, the user only needs to enter the Canvas step and start a session to receive the in-app message. If the trigger is not to start a session, the user has to enter the Canvas step, start a session, and then perform the trigger to receive the in-app message.

The following Canvas features aren’t available with in-app messages, so they won’t be applied to your in-app messages even if they’re turned on.

- Intelligent Timing
 
- Rate limiting
 
- Frequency capping
 
- Exit criteria
 
- Quiet hours

## Custom event properties in a Canvas

Custom event properties in in-app messages for Canvas are supported. However, these properties are from the custom event or purchase triggering the in-app message, which is located in the Message step, not the preceding action path.

## Considerations

Here are some considerations when sending in-app messages in a Canvas.

- If the user never restarts the app or never starts a session, the app won’t be able to find out if the user is eligible for the in-app message, meaning an in-app message won’t be sent.
 
- When the first click occurs and there is a Canvas context variable (Canvas entry properties), and a user re-enters a Canvas five times, Braze will take the fifth entry and use that context variable in the in-app message.
 
- A user can be eligible for up to 10 in-app messages within the same Canvas step. For example, if a Canvas allows re-entry and a user enters the Canvas 11 times, they will only be sent 10 in-app messages if none have expired.

- 

New Stuff!
