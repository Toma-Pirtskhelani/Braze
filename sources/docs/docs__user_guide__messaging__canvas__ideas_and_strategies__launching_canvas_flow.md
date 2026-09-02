---
url: https://www.braze.com/docs/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow
slug: docs__user_guide__messaging__canvas__ideas_and_strategies__launching_canvas_flow
title: "Launch with Canvas Flow"
description: "This reference article covers how to prepare and test a Canvas built with Canvas Flow before launch."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Launch with Canvas Flow

This reference article covers how to prepare and test a Canvas built using Canvas Flow before launch. This includes identifying important Canvas checkpoints such as Canvas entry conditions, audience summaries, and user segments.

As you prepare to launch your Canvas, Braze recommends that you check your Canvas at each stage of the Canvas builder for settings that can impact your message sending, including:

- Race conditions
 
- Delivery times
 
- User segments

## Race conditions

Consider the race conditions that may be occur before launching your Canvas.

To enter a Canvas, users must be in the entry audience before the entry schedule occurs regardless of whether the Canvas is scheduled, action-based, or API-triggered.

Note that users who qualify for your entry audience after the Canvas launches will not enter the Canvas.

tip

Check out Entry schedule types for guidance and details for when to use scheduled, action-based, or API-triggered delivery for your Canvas!

### Review entry audience filters

In general, avoid configuring an action-based or API-triggered Canvas with the same trigger as the audience filter. For example, after a Canvas is launched, users who perform a specific action will be included in the entry audience, so there’s no need to add the event as an audience filter.

For more details on available segmentation filters to target your audience, see Segmentation Filters.

### Batch multiple API requests

Make your requests in the same API call, rather than multiple calls, to confirm that the user profile is created or updated first. Refer to Using multiple endpoints for more examples.

### Add a delay

Another option to avoid race conditions is to use the Delay step (ideally set for 5 minutes) as the first step of your Canvas.

This allows time for attributes, email addresses, and push tokens to be processed to new user profiles before they’re targeted for the following Canvas steps. Without this Delay step, it’s possible for an email to be sent to a user whose email hasn’t been updated yet.

## Delivery times

Setting a Canvas delivery time in real-time can lead to increasing engagement and conversion rates. Take note of which delivery time you’ve set for your Canvas. To help increase engagement and conversion rates, it’s best to trigger Canvases in real-time instead of on a scheduled, recurring basis.

If you selected a scheduled delivery for your Canvas, Braze recommends scheduling your Canvas at least 24 hours before you want it to launch to allow for any adjustments to your Canvas.

## User segments

Before oversaturating your Canvas Flow user journey with components, consider how you might keep a user journey simple. Use the simplified view in the Canvas editor to get a better idea of how your user journey branches.

There are four main components you can use to segment your users in a simple, effective manner:

- Audience Paths
 
- Decision Split
 
- Action Paths
 
- Experiment Paths

### Audience Paths

Use Audience Paths steps to segment users within the Canvas based on custom attributes, custom events, and previous message engagement data from user profiles.

### Decision Split

The Decision Split step allows you to send your users to different user journey paths based on their answers to a polar question.

### Action Paths

Action Paths focus on segmenting users based on real-time behaviors such as custom events, purchase events, and custom attribute changes.

### Experiment Paths

Similar to Action Paths, you can leverage Experiment Paths steps in your Canvas to test multiple Canvas paths against each other, along with a control group. This tracks path performance, allowing you to make informed decisions when building your Canvas journey.

## Testing before launch

After reviewing the finer details of your Canvas, check out Sending test Canvases for different methods you can leverage to test your Canvas with test users.

## Launch checklist

### Check user availability

- Make sure your users meet your segmentation criteria.
 
- Confirm their subscription state is “subscribed” or “opted-in” and their Push token exists. If you added these as Canvas entry rules, it’s possible that the users were unsubscribed between entering your Canvas and receiving the Message step.
 
- Confirm they match your Canvas send settings. (If users are “subscribed” but the settings are “Opted-in”, users won’t be enabled for the channel.)
 
- If global frequency capping is enabled for your Canvas, check if your rules are limiting how many times each user can receive a message from a specific channel.
 
- If Quiet Hours are enabled, your message send time could be affected, meaning that your message may be sent at the next available time (when the Quiet Hours end) or cancelled entirely.
 
- Check user availability for additional filters in your Canvas step.

### Confirm that they performed the prerequisite custom event or purchase

- Check if there’s a race condition, which impacts the messages users receive if they trigger multiple actions at the same time.
 
- Make sure there aren’t specific filters in the step that could have blocked users from receiving the message.
 
- Search for conflicts between different steps within the same Canvas. For example, users who didn’t receive the message might be stopped by a filter that requires the completion of another step on a different branch.
 
- Confirm that users meet additional validation rules.
 
- Confirm that the Canvas step was connected to the preceding step at the time of send.

### Confirm your Canvas saves correctly and all steps are valid

If your Canvas isn’t loading and won’t progress, this can be caused when a previous version of the Canvas wasn’t saved properly and contains invalid steps. You can duplicate the Canvas from the dashboard. If the issue persists, open a support ticket.

## Troubleshooting

Why are my users not receiving my Canvas messages?

Check user availability

- Make sure they meet your segmentation criteria.
 
- Confirm their push subscription state is “subscribed” or “opted-in” and their Push Enabled status is set to “true”. If you added these as Canvas entry rules, it’s possible that the users were unsubscribed between entering your Canvas and receiving the Message step.
 
- Confirm they match your Canvas send settings. (If users are “subscribed” but the settings are “Opted-in”, users won’t be enabled for the channel.)
 
- If global frequency capping is enabled for your Canvas, check if your rules are limiting how many times each user can receive a message from a specific channel.
 
- If Quiet Hours are enabled, your message send time could be affected, meaning that your message may be sent at the next available time (when the Quiet Hours end) or cancelled entirely.

Check user availability for additional filters in your Canvas step

- Confirm that they performed the prerequisite custom event or purchase.
 
- Check if there’s a race condition, which impacts the messages users receive if they trigger multiple actions at the same time.
 
- Make sure there aren’t specific filters in the step that could have blocked users from receiving the message.
 
- Search for conflicts between different steps within the same Canvas. For example, users who didn’t receive the message might be stopped by a filter that requires the completion of another step on a different branch.
 
- Confirm that users meet additional validation rules.
 
- Confirm that the Canvas step was connected to the preceding step at the time of send.

- 

New Stuff!
