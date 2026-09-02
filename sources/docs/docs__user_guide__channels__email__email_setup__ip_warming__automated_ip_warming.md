---
url: https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming
slug: docs__user_guide__channels__email__email_setup__ip_warming__automated_ip_warming
title: "Automated IP warming"
description: "This reference article covers automated IP warming and how to monitor your IP warming."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Automated IP warming

Use automated IP warming to gradually ramp email volume from new dedicated IPs to build sender reputation with inbox providers. For common questions, see the Automated IP warming FAQ.

## How it works

You can use automated IP warming to gradually increase your daily send volume, allowing inbox providers to learn and trust your sending patterns. When you add a domain to your workspace, you can select the Automated IP Warming tile in the Pick up where you left off section of your home dashboard. This tile remains for 60 days while your workspace is in the new-sender onboarding window, and is hidden after you complete at least one plan.

Each automated IP warming plan is tied to one from address. That from address maps to a sending subdomain and an IP pool. If the pool contains multiple dedicated IPs, Braze warms them together in a single plan.

Braze sends to your most engaged subscribers first, which allows daily volume to grow at a pace that matches best practices. Then, Braze tracks engagement and deliverability signals. If Braze detects any issues, the system adjusts your schedule automatically.

After you complete at least one plan, you can view completed plans at Settings > Email Preferences > Automated IP warming.

## Prerequisites

To perform automated IP warming, you must have the following:

- Verified subdomain and active IP addresses
 
- Permissions to view and set up a plan:

- “View Email Settings” to view IP warming plans and the home dashboard widget
 
- “View Email Templates” to select email templates
 
- “View Segments” to select segments

- Permissions to launch a plan:

- “Edit Email Settings”
 
- “Edit Campaigns”
 
- “Launch Campaigns”
 
- “Approve Campaigns”

note

If the campaign approval workflow is turned on, Braze automatically approves campaigns created by automated IP warming on your behalf.

## Set up an automated IP warming plan

### Step 1: Set a schedule

- Enter a unique Plan name. Plan names may contain letters, numbers, hyphens, and underscores only, and must be unique in your workspace. A plan name is required before you can launch.
 
- In the Sending information section, select the From address to warm IP addresses for. Braze displays the associated IP pool and the number of IP addresses in pool for that from address.
 
- Enter the Current daily send volume and Target send volume. Braze suggests a target send volume of up to 2 million sends per IP in the selected pool. If your current daily send volume is 0, the first day of your schedule starts at up to 50 sends per IP, capped at 500 total.
 
- Select the start date for automated IP warming. This date must be at least one day after the plan is launched.
 
- Enter the send time. This sends the messages in the workspace time zone (or company time zone if the workspace has no override).
 
- Select Next: Segments to continue the setup.

### Step 2: Select and rank segments

- Next, select the segments to target. During IP warming, Braze starts sending to your highest engaged users and gradually increases send volume over time and slowly adds in segments with less engagement.
 
- Then, drag and drop the segments to rank them from high to low engagement. High engagement includes recipients who consistently open and click on your emails. Low engagement includes recipients who are inconsistent in their engagement with your emails or haven’t engaged with your emails in a very long time.
 
- Select Next: Messages to continue the setup.

### Step 3: Select the messages to send

- Select Select email templates.
 
- Choose the email templates for the messages to send. The content you send during IP warming should encourage opens and clicks. We recommend choosing content that has had good reception in the past. For example, you can use promotional offers to encourage immediate engagement and purchases.
 
- Select Select templates. Braze calculates the number of required templates before you can launch. We recommend providing more templates than the minimum required to allow the system to adjust for deliverability issues without stopping.
 
- After adding the required number of templates, select Next: Summary.

important

Changes made to the campaigns created from the IP warming tool (such as changing the scheduled date, segment, volume) are not reflected on the IP warming Summary page.

### Step 4: Select conversion events

You can define up to four of the following conversion events to track. These conversion events cannot be updated after the automated IP warming plan has launched.

- Starts session
 
- Places order
 
- Performs custom event
 
- Upgrade app
 
- Opens email
 
- Clicks email

Next, select the conversion deadline, which is the maximum time that can pass between a user entering a campaign and the conversion event.

### Step 5: Review and launch

Review the details of your IP warming plan. Then, select Launch.

## Multiple IP warming

Use multiple automated IP warming plans when you need to warm more than one from address or IP pool.

 Scenario | 
 Recommendation | 

 Multiple dedicated IPs in one IP pool | 
 Create one plan and select the from address for that pool | 

 Multiple IP pools or from addresses | 
 Create a separate plan for each from address | 

### Warm multiple IPs in one pool

When you select a from address in Step 1: Set a schedule, Braze shows the associated IP pool and IP addresses in pool. Braze uses the IP count when it builds your ramp schedule and suggests your target send volume.

If your Current daily send volume is 0, the first scheduled day starts at up to 50 sends per IP in the pool, capped at 500 total. Braze suggests a Target send volume of up to 2 million sends per IP in the pool.

### Warm multiple IP pools

To warm more than one from address or IP pool:

- Go to Settings > Email Preferences > Automated IP warming.
 
- Select New IP warming plan.
 
- Enter a unique Plan name.
 
- Complete the setup for that from address.
 
- Repeat for each additional from address or IP pool you need to warm.

Track each plan from the Automated IP warming table. Each plan has its own schedule, segments, templates, campaigns, and tracker. Plans can be in Draft, In progress, Completed, or Stopped status.

important

Avoid sending large non-warming campaigns from the same from address or IP pool while an automated IP warming plan is active. Additional sends during warming can affect deliverability signals and make it challenging to isolate issues.

## During active IP warming

IP warming campaigns are created at midnight in the effective time zone for the current day and the next day (0 to 1 days before send). Launching a plan also creates upcoming campaigns immediately. These campaigns are automatically named with the following format: IP Warming Day [X] - [Date] - [Template Name].

When the targeted daily send goal is reached, the system stops sending for that day to protect your reputation.

Braze evaluates deliverability for campaigns that sent between 12 and 20 hours ago. If any of the following thresholds are crossed, Braze holds volume for the next send day instead of increasing it:

- Delivered rate below 90%
 
- Open rate below 10%
 
- Bounce rate above 5%
 
- Spam complaint rate above 0.04%

For what happens when volume is held, see What happens when volume is held?.

## Stop an IP warmup plan

You can stop an IP warming plan to prevent creation of future campaigns. Stopping a plan also disables all associated campaigns. After you stop a plan, you can’t resume it. Set up a new plan to pick up from where you left off by:

- Downloading the existing data for your stopped plan to keep for your record
 
- Updating the Current daily send volume to the most recent volume
 
- Adding a filter to a segment if you plan to use the same segment from the last IP warmup by excluding users that have already received previous campaigns

## When an IP warming completes

IP warming is marked as completed when the last day of IP warming ends at midnight in your workspace time zone (or company time zone if the workspace has no override). For example, if the last campaign in the plan sends at 8 pm, the plan is marked complete at midnight four hours later.

Completed plans remain available from Settings > Email Preferences > Automated IP warming. The tracker also stays on the home dashboard for 90 days after the plan ends. After 90 days, the home dashboard tracker is removed.

Downloading the data includes these standard email metrics:

- Sent
 
- Delivered
 
- Bounces
 
- Spam reports
 
- Total opens
 
- Unique opens
 
- Clicked
 
- Unsubscribed

If a day includes multiple campaigns used to meet volume requirements, these are aggregated in the daily view.

- 

New Stuff!
