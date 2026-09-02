---
url: https://www.braze.com/docs/user_guide/messaging/campaigns/creating_campaign
slug: docs__user_guide__messaging__campaigns__creating_campaign
title: "Create a campaign"
description: "Learn how to create a Braze messaging campaign from compose through launch—including multichannel sends—and how to schedule delivery, target audiences, assign conversion events, send tests,..."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create a campaign

Use campaigns when you want to reach consumers with a single messaging step across one or more supported channels. For multi-step journeys, use Canvas.

## Prerequisites

To create and launch a campaign, you need “Edit Campaigns” and “Launch Campaigns” permissions. For a full list of workspace permissions and how they appear in the dashboard, refer to Permissions.

### Before you begin

- Build or choose the segments that define who should receive your messages.
 
- Review Campaign basics so messaging channels, delivery types, and conversion goals align with your use case.
 
- For a guided walkthrough of delivery, targeting, and conversions, take the Campaign Setup Braze Learning course.
 
- Ask Operator to help draft your campaign from a brief, or refine targeting and delivery choices. For details, see What you can do with Operator.

## Campaign composer

The campaign composer is where you define delivery, audiences, conversions, and launch settings. Decide whether you’re creating a single-channel or multichannel campaign before you continue.

- single channel
 
- multichannel

A single-channel campaign reaches users through one messaging channel per launch.

### What’s different

#### Conversions and reporting

For single-channel campaigns, Braze tracks conversion events you assign to the campaign against sends from that channel. For attribution windows and counting rules, see Conversion tracking rules.

Workspace frequency capping and send limits still apply.

### Create a single-channel campaign

To create a campaign:

- Go to Messaging > Campaigns.
 
- Select Create campaign.
 
- Select the channel that fits your use case.
 
- On the Compose step, write and preview copy for that channel.

Each campaign uses one channel type at a time. Add variants when you want to compare creative splits or run A/B testing.

A multichannel campaign reaches users through more than one messaging channel in a single launch. For example, send an email and push notification together.

note

In-app messages aren’t available in multichannel campaigns. Create a single-channel campaign or Canvas instead.

### What’s different

#### Control groups

Campaign control groups compare variants within one channel (for example, Email A versus Email B). They aren’t used to compare entire channels inside one multichannel campaign. To test channels, creative, or timing together across a journey, use Canvas.

#### Conversions and reporting

For multichannel campaigns, Braze tracks conversion events per channel. When a user converts after receiving messages on more than one channel, Braze can attribute that conversion across those channels. Conversion counts may exceed Unique Users, and rates may exceed 100%. For full rules, see Conversion tracking rules.

Rate limits for sends that span channels are described in Multichannel campaigns and Canvases. For workspace-wide rules (including how multichannel sends count toward caps), refer to Frequency capping.

### Create a multichannel campaign

- Go to Messaging > Campaigns.
 
- Select Create campaign.
 
- Select Multichannel.
 
- On the Compose step, select Add channel and choose each channel you need. Select the channel icons to switch between composers while you write copy for each channel.

## Step 1: Compose messages

### Campaign details

Use the following fields to record metadata that helps your team find and manage the campaign.

 Field | 
 Purpose | 

 Name | 
 Use a clear name that reflects the campaign goal. | 

 Description | 
 Optional. Explain intent or links to briefs for collaborators. | 

 Team | 
 Optional. Assign Teams so the right groups can edit or report on this send. | 

 Tags | 
 Optional. Add tags to filter in lists and tools such as Report Builder. | 

 Campaign ID | 
 Where shown in the composer or summary, copy this identifier for API calls, reporting, and integrations that reference a specific campaign. | 

### Channels and editors

Compose channel-specific content in this step. For detailed guidance, see Channels and open the article for the channel you selected.

### Variants

Add variants when you want to compare creative or delivery splits. For background on experiments and controls, see Multivariate and A/B testing.

tip

When each variant uses similar body content, compose the message before you add extra variants. Then use Copy from Variant from the Add Variant menu to reuse work across variants or channels.

## Step 2: Schedule delivery

Choose when users become eligible to receive the campaign:

 Delivery type | 
 Summary | 

 Scheduled delivery | 
 Send at a specified time or cadence. | 

 Action-based delivery | 
 Send when users perform behaviors or meet conditions you define. | 

 API-triggered delivery | 
 Send when your systems call Braze to trigger the campaign for eligible users. | 

For scheduling concepts across Braze, see Schedule your campaign.

### Delivery controls

Depending on delivery type, you can adjust re-eligibility (whether users may enter the campaign again) and respect workspace frequency capping rules. You may also configure quiet hours so messages don’t send during restricted windows.

## Step 3: Target audiences

On Target Audiences, define who is eligible to receive the campaign. For full targeting options, UI walkthroughs, and screenshots, see Target users.

### Targeting options

In this section, you can target users by choosing segments or filters to narrow down your audience. Eligible users still need to meet the trigger or criteria you define in the Schedule Delivery step. The target audience is like a waiting room—only people already inside can move forward when the next action happens.

Workspace suppression lists automatically exclude listed users unless you allow an exception for this campaign.

### Audience summary

After adding segments or filters, the Audience Summary gives preview of what that segment population looks like, including how many users within that segment are reachable through your selected channels. Reachable counts reflect your workspace data, channel setup, and filters. Keep in mind that exact segment membership is always calculated before the message is sent. For very large audiences, Braze may show estimates until you calculate exact statistics.

note

If you have a Global Control Group set up, the reachable user count shown in your campaign target audience is smaller than the reachable user count shown for the same segment. This is because the campaign excludes users in the global control group, while the segment count does not.

### User Lookup

After adding segments or filters, you can test if your audience is set up as expected by looking up a user to confirm if they match the segment criteria. To do so, search for a user’s external_id or braze_id in the User Lookup section. You can’t search by email address here. See Testing segments for more.

When a user matches the segment, filter, and app criteria, an alert states so. When a user doesn’t match part or all of the segment, filter, or app criteria, the missing criteria is listed for troubleshooting purposes.

### Send to these users

For subscription-based channels (email, SMS, and similar), use Send to these users to only send your campaign to users who have a specific subscription status, such as those who are subscribed and opted in to email.

### Limit send volume

You can limit the total number of users that receive your message. This serves as a check that is independent of your campaign filters. For details, refer to Setting a maximum user cap.

### Limit the rate at which this campaign sends

If you anticipate large campaigns driving a spike in user activity and overloading your servers, you can specify a per-minute rate limit for sending messages, which means Braze sends no more than your rate-limited setting within a minute. For details, refer to Delivery speed rate limiting

### A/B testing

You can create a multivariate or A/B test for any campaign that targets a single channel, even if the single channel includes multiple devices. For example, if you want to use multivariate or A/B testing for a push campaign, you can target only iOS devices or only Android devices—not both device types in the same campaign.

For supported single-send and multi-send campaigns, turn on Optimize with BrazeAI™ to automatically optimize your variant distribution.

## Step 4: Assign conversion events

Conversion events measure outcomes after a user receives your campaign (or enters the control group). Braze defaults to Starts Session within a short window (three days). You can define conversion events that match your KPIs, up to four events per campaign.

After you launch, use the Conversions dashboard to analyze conversion trends across multiple campaigns or Canvases, compare channels, and adjust date ranges, attribution methods, and breakdowns in one place.

important

You can’t add or remove conversion events after the campaign launches. Confirm events before you launch.

## Step 5: Review summary and launch

The Review Summary step shows scheduling, audience, variants, and messaging choices. Before you launch your campaign:

- Confirm segments, variants, and delivery settings match your intent.
 
- Send test messages to validate rendering and behavior on your test devices or internal recipients.

When you’re ready, select Launch Campaign.

### Approvals

If your workspace uses approvals, a teammate with permission to approve campaigns must approve before launch. For more information, see Approvals for campaigns and Canvases.

## Related articles

- Design and edit
 
- A/B tests
 
- Know before you send
 
- Campaign analytics

- 

New Stuff!
