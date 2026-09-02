---
url: https://www.braze.com/docs/user_guide/messaging/campaigns/test_campaigns/triggered_action_based
slug: docs__user_guide__messaging__campaigns__test_campaigns__triggered_action_based
title: "API-triggered and action-based campaigns"
description: "This reference article explains how to test API-triggered and action-based campaigns."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# API-triggered and action-based campaigns

When setting up campaigns, it is always a good practice to test your messages before launching. This reference article covers creating a test user segment that will allow you to inspect API requests, payloads, and view deliverability logs.

## Step 1: Create a test user segment

The only way to test the triggering of a campaign with the API or custom event is to push the campaign live. As part of rolling out a new campaign, we strongly recommend adding a test user segment to campaigns when testing triggering deliverability. This will provide a safety net, ensuring that even if a campaign is accidentally sent, it will only go to internal users.

- Import test users
Test users can be imported to Braze through a CSV or a one-off batched request through Postman. When importing these users, we recommend setting a custom attribute on their profiles (such as internal_test_user: true) that can be used to build a test group segment. 

- Add test users as Braze-recognized test users
Marking your test users as Braze-recognized test users in the dashboard gives you access to verbose logging for each user, allowing you to inspect API requests, their payloads, and view deliverability logs. These logs can help you determine if there were any issues delivering campaigns to end users. 

- Create segment
To create a test user segment, create a segment of users with the internal_test_user custom attribute set to true. This segment can be removed when the campaign goes live.

## Step 2: Testing sends

Next, you can do a test send from the Braze dashboard or use Inbox Vision (email only) to see what the layout will look like while the campaign is still in draft mode. You can then send the campaign to your test user segment to verify it is behaving as expected. Regardless of whether the campaign is API-triggered or action-based, use Postman to send a one-off request to the Braze API, triggering the campaign.

## Step 3: Use Braze logging to inspect inbound results

Use Braze logging to troubleshoot triggering, sending, and event problems.

- The event user log will show you the raw payload of the API-trigger request, the custom event triggering the campaign, and any associated trigger or event properties.
 
- The message activity log will log any errors and help you understand why a particular message may not have been delivered.

## Step 4: Remove the test segment and roll out the campaign

Once the message is triggering and rendering properly with all clicked links registered, you can remove the segment and update the campaign. If you prefer to start the campaign from scratch so that the few test user impressions are not included, you can duplicate the campaign and restart it without the test user segment.

- 

New Stuff!
