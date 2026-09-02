---
url: https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/target_users
slug: docs__user_guide__messaging__messaging_fundamentals__target_users
title: "Target users"
description: "This reference article covers how to target your audience in your campaign and Canvas editors."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Target users

Determining how to target your users is one of the most crucial steps when creating a campaign or Canvas. By understanding how to segment your audience based on their behaviors, preferences and demographics, you can tailor and personalize your messaging.

## Creating a target audience

### Step 1: Choose users

Under Targeting Options, you can use the following options to choose which users you’d like to target for your campaign or Canvas. Only the users who match your defined criteria will receive the message. Keep in mind that exact segment membership is always calculated just before the message is sent.

- single segment
 
- multiple segments
 
- multiple filters
 
- segments & filters
 
- specific apps

To target members of a previously created segment, select one segment from the dropdown under Target Users by Segment.

To target users that fall into multiple previously created segments, add multiple segments from the dropdown under Target Users by Segment. The resulting target audience will be users both in the first segment and the second segment and the third segment, etc.

To target users without adding a segment, you can use a series of filters. This is an impromptu audience during message creation and allows you to skip segment creation when sending to one-off audiences.

You can also target users of one or more previously created segments that also fall under additional filters. After first selecting your segments, you can further refine your audience under the Additional Filters section. This is demonstrated in the following screenshot, which targets users that are in the “Daily Active Users” segment, “Never opened email” segment, and made a purchase more than 30 days ago.

You can deliver a campaign message or Canvas step to specific apps, such as sending an in-app message or push notification to only Android or iOS apps.

However, remember that it’s possible for one user to use multiple apps. The “Has app” filter identifies all users who have the selected app, but doesn’t control which apps receive messages. For example, if you apply a segment filter where “Has app” is set to Android, any users who also have the iOS app will also receive the message on their iOS app.

Let’s say you want to send an in-app message only to Android apps.

- Create a segment and set Apps and websites targeted to Users from specific apps, then select your Android app.

- In the Target Audiences step, confirm that your segment is added in the Target Users By Segment section.

note

This won’t work if you add your segment in the Additional Filters section through a segment membership filter. You must directly reference your segment in Target Users By Segment to deliver your message only to that app.

tip

For email campaigns, you can target Seed Groups under the Seed Groups section. Note that Seed Groups aren’t available for API campaigns, although you can include Seed Groups via an API-triggered entry in a campaign. For more information, see Seed Groups.

### Step 2: Test your audience

After adding segments and filters to your audience, you can test if your audience is set up as expected by looking up a user to confirm if they match the audience criteria.

#### Audience summary

The Audience Summary will show an overview of who is in your target audience. Here, you can further limit your audience by setting a maximum user cap or rate-limiting delivery speed.

#### A/B testing

In the A/B Testing section, you can set up a test to compare users’ responses to multiple versions of the same marketing campaign. These versions share similar marketing goals but differ in wording and style. The objective is to identify the version of the campaign that best accomplishes your marketing goals.

For more information and best practices, refer to Multivariate & A/B Testing.

#### Audience statistics

Braze provides detailed audience statistics of the targeted channels in the footer. The larger your user base is, the more likely the Reachable Users amount is a rough estimate. The number of reachable users may decrease if you use a Global Control Group or set up message eligibility.

- To determine an accurate number for your reachable users, select Calculate exact statistics, as this will search through every user in your user base.
 
- To see what percentage of your user base is being targeted or the Lifetime Value (LTV) for this segment, select Show Additional Statistics.

##### Why the target audience count could differ from the reachable users count

The target population size that is displayed in a campaign or Canvas may differ from the reachable audience size for a segment, even if you’re directly adding that segment into your campaign or Canvas without additional filters. 
This may happen for several reasons:

- When a Global Control Group applies to a campaign or Canvas, users in that Global Control Group are excluded in the reachable users count.
 
- The target population size on a campaign or Canvas excludes users that aren’t contactable through various message channels; the behavior differs from channel to channel. For example, the reachable audience for a campaign or Canvas excludes users who are unsubscribed, marked as spam (for emails), or hard bounced (for emails). The segment itself, however, only excludes opt-outs when showing the estimated number of email reachable users.
 
- Braze only sends SMS messages to users within the selected subscription group, so the SMS target population for a campaign or Canvas will also exclude any users who aren’t part of your selected subscription group.

note

Calculating exact statistics can take a few minutes to run. This function only calculates the exact statistics at the segment level, not at the filter or filter group level.

For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

## How target audience and entry criteria work together

When you build a campaign or Canvas in Braze, targeting happens in two parts:

- Target audience: Who qualifies
 
- Entry criteria: What triggers delivery

Order matters: Braze checks whether someone is in the target audience before the entry criteria is evaluated. If a user doesn’t already qualify for the audience at that moment, they won’t enter the campaign or Canvas—even if they later trigger the entry event. Think of the target audience as a waiting room: only users who are already inside when the trigger occurs can move forward.

### Example 1

You want to send a push message during a user’s first session.

You set:

- Target audience: Users with session count = 0
 
- Entry event: Session start

When the user opens your app, Braze sees their session count is now 1—and they no longer qualify for the audience. The entry event happens after they’re eligible, so the message won’t send.

To make this work, the user needs to qualify for the audience before the session begins (flip the target audience and entry trigger).

### Example 2

You want to send an email to users who’ve spent more than $10 in the last 7 days.

You set:

- Target audience: Users who spent more than $10 in the last 7 days
 
- Entry event: Any purchase

Now imagine a user spends $12 today. That doesn’t trigger the message—it only makes them eligible to enter the audience. They won’t receive the email unless they make another purchase later.

A better approach would be to use a broader audience and shift the filter into the entry criteria:

- Audience: All users (or your base audience)
 
- Entry event: Make a purchase
 
- Entry filter: Total spend in last 7 days > $10

This way, a qualifying purchase both meets the filter and triggers the message—no second action required.

## Best practices

- Make sure the audience segment includes users before the entry criteria occurs.
 
- Avoid using audience filters that only apply after your event. If a filter depends on something that happens at the time of the trigger (like “session count = 0”), the user may no longer qualify by the time Braze checks.
 
- Use time-based logic thoughtfully. For example, if you want to target new users:

- Set your target audience to “first used app within the last 7 days”.
 
- Set your entry event to “session start”.
 
- That way, only users who are still within their first week will qualify and enter when they start a session.

- 

New Stuff!
