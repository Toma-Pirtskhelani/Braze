---
url: https://www.braze.com/docs/user_guide/audience/segments/segment_extension
slug: docs__user_guide__audience__segments__segment_extension
title: "Segment Extensions"
description: "This how-to article will walk you through how to set up and use a Segment Extension to enhance your segmentation capabilities."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Segment Extensions

Segment Extensions allow you to build very precise segments over an extended period of a user’s history. For example, using Segment Extensions you can target users who have purchased a particular product in the last sixteen months or have spent a certain amount of money with your service. Refine this audience by using event properties to make targeting even more granular.

Braze segmentation allows you to target users based on custom event or purchase behavior. Segment Extensions enhances this capacity, letting you draw on historic data saved on the user profile. Using Segment Extensions, you can identify and reach users who have completed any custom event or purchase event any number of times in the past two years (730 days).

## Why use Segment Extensions?

Braze segments give you powerful targeting tools to create dynamic groups of users. For most use cases, this is enough to reach your audience effectively. Segment Extensions are designed for advanced use cases where you need to analyze behaviors from up to two years ago or apply complex logic—without compromising data retention or system performance. You can use SQL queries (SQL Segment Extensions) or data from your own data warehouse to refine your audience further.

For example, Braze default segmentation will find users that fit specific criteria you define, such as identifying a user who recently purchased one of your products. Segment Extensions let you go deeper—like identifying users who bought a particular color of a specific product at least twice between 18 to 24 months ago. Segment Extensions are an enhancement, not a requirement. If you need more advanced filters or a longer lookback window, they’re a great tool to help while keeping your data usage optimized.

note

There is a default allotment of 50 active Segment Extensions per workspace at a particular time. If you need to increase this limit, contact your Braze customer success manager to discuss your use case.

## Creating a Segment Extension

To create a Segment Extension, you will create a filter to refine a segment of your users based on custom event properties. When creating a Segment Extension, you will choose whether the segment will be static or dynamically refreshed at a set interval.

### Step 1: Navigate to Segment Extensions

Go to Audience > Segment Extensions.

From the Segment Extensions table, select Create New Extension, then select your Segment Extension creation experience:

- Simple extension: Create a Segment Extension focused on a single event by using a guided form.
Best for when you don’t want to use SQL.
 
- Start with a template: Create a SQL segment with a customizable template using Snowflake data.
 
- Incremental refresh: Write a Snowflake SQL segment that automatically refreshes the last 2 days of data or manually refresh as needed. Best for balancing accuracy and cost-efficiency.
 
- Full refresh: Write a SQL segment with Snowflake data or any CDI connected source that recalculates the entire audience upon manual refresh. Best for when you need a complete, up-to-date view of your audience.

If you select an experience that uses SQL, refer to SQL Segment Extensions for further information. If you select Simple extension, continue to step 2.

#### SQL credit usage

The following Segment Extension types consume SQL credits:

- SQL Segment Extensions (both incremental and full refresh)
 
- Catalog Segments
 
- CDI Segments

- Credits are consumed within your own data warehouse

### Step 2: Name your Segment Extension

Name your Segment Extension by describing the type of users you intend to filter for. This will ensure that this extension can be easily and accurately discovered when applying it as a filter in your segment.

### Step 3: Choose your criteria

Select between purchase, message engagement, eCommerce recommended event, or custom event criteria for targeting. After you’ve selected the desired event type criteria, choose which purchased item, message interaction, eCommerce recommended event, or custom event you’d like to target for your user list. Then choose how many times (more than, less than, or equal to) the user would need to have completed the event, and the time period—for Segment Extensions specifically, you can go back up to the past 730 days (2 years).

Segmentation based on event data from more than 730 days can be done using other filters located in Segments. When choosing your time period, you can specify a relative date range to select the past X number of days, a start date, an end date, or an exact date range (date A to date B).

If you are creating a Segment Extension using an eCommerce recommended event, first select eCommerce Recommended Event as your criterion, then select an event from the dropdown.

#### Event property segmentation

To increase targeting precision, select the Add Property Filters checkbox. This will enable you to drill down based on the specific properties of your purchase or custom event. We support event property segmentation based on string, numeric, boolean, and time objects.

For string properties, you can enter in multiple values at once. In the following example, this filter looks for users with a status equal to any of the following: gold, silver, or bronze.

If you are using eCommerce recommended events and add an event property, the property dropdown will automatically populate with the properties available for that specific eCommerce recommended event.

We also support segmentation based on nested event properties. In the comparison dropdown, select the comparison that matches your nested property’s data type. You can use the same nested event property syntax to add nested properties for any eCommerce recommended events that contain nested properties. For info on the different nested properties available, see Types of eCommerce recommended events. To generate the necessary schema for your Segment Extension’s property name, follow the steps in Nested objects in custom events.

Segment Extensions rely on long term storage of event properties and don’t have a time-stamped property storage limit. You can look back on event properties tracked within the past two years. Using event properties within Segment Extensions does not impact data point usage.

note

You don’t need Segment Extensions to use event properties or nested custom attributes in your segment. Segment Extensions just extend the historic window used to create a default segment. You can create a real-time default segment that uses event properties from the past 30 days or uses nested custom attributes. Similarly, you can schedule your message to trigger in real time based on an event property—no Segment Extension required.

### Step 4: Designate refresh settings (optional)

If you don’t need your extension to refresh on a regular schedule, you can save it without using refresh settings, and Braze will default to generating your Segment Extension based on your user membership at that moment. Use the default behavior if you only want to generate the audience once and then target it with a one-off campaign.

Your segment will always begin processing after the initial save. Whenever your segment refreshes, Braze will re-run the segment and update segment membership to reflect the users in your segment at the time of refresh. This can help your recurring campaigns reach the most relevant users.

#### Setting up a recurring refresh

To set up a recurring schedule by designating refresh settings, select Enable refresh. The option to designate refresh settings is available for all types of Segment Extensions, including SQL segments, CDI Segment Extensions, and simple form-based Segment Extensions.

important

To optimize your data management, refresh settings are automatically turned off for unused Segment Extensions. Segment Extension are considered unused when they’re:

- Not used in any active or inactive (draft, stopped, archived) campaigns, Canvases, or segments; or
 
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension if this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.

#### Selecting your refresh settings

Within the Refresh Interval Settings panel, you can select the frequency at which this segment extension will refresh: hourly, daily, weekly, or monthly. You’ll also be required to select the specific time (which is in your company’s time zone) the refresh would occur, such as:

- If you have an email campaign that is sent every Monday at 11 am company time, and you want to ensure your segment is refreshed right before it’s sent, you should choose a refresh schedule of weekly at 10 am on Mondays.
 
- If you’d like your segment to refresh every day, select the daily refresh frequency and then choose the time of day to refresh.

note

The ability to set an hourly refresh schedule isn’t available for form-based Segment Extensions (but you can set daily, weekly, or monthly schedules).

#### Credit consumption and additional costs

Because refreshes re-run your segment’s query, each refresh for SQL segments will consume SQL segment credits, and each refresh for CDI Segment Extensions will incur a cost within your third-party data warehouse.

note

Segments could require up to 60 minutes to refresh because of data processing times. Segments that are currently in the process of refreshing will have a “Processing” status within your Segment Extensions list. This has a couple of implications:

- To finish processing your segment before a specific time, choose a refresh time that is 60 minutes earlier.
 
- Only one refresh can occur at a time for a specific Segment Extension. If there is a conflict where a new refresh is initiated when an existing refresh has already begun processing, Braze will cancel the new refresh request and continue the in-progress processing.

#### Criteria to automatically disable stale extensions

Scheduled refreshes are automatically disabled once a Segment Extension is stale. A Segment Extension is stale if it meets the following criteria:

- Not used in any active campaigns or Canvases
 
- Not used in any segment that is in an active campaign or Canvas
 
- Not used in any segment that has analytics tracking turned on
 
- Hasn’t been modified in over seven days
 
- Hasn’t been added to a campaign or Canvas (including drafts), or segment in over seven days

If the scheduled refresh is disabled for a Segment Extension, that extension will have a notification that says so.

When you’re ready to use a stale Segment Extension, review the refresh settings, select the refresh schedule that matches your use case, and then save any modifications.

### Step 5: Save your Segment Extension

After you select Save, your Segment Extension will begin processing. The length of time it takes to generate your Segment Extension depends on how many users you have, how many custom events or purchase events you’re capturing, and how many days you’re looking back in history.

While your Segment Extension is processing, you will see a small animation next to the name of the Segment Extension, and the word “Processing” in the Last Processed column on the Segment Extension list. Note that you will not be able to edit a Segment Extension while it is processing.

When a Segment Extension is processing, Braze will continue to use the version history of the default segment from before the processing began for audience segmentation purposes. Processing takes place each time a save or refresh occurs, and involves querying and updating user profiles—in other words, your default segment’s membership does not update instantaneously. This means that unless a user’s action is performed before the refresh begins processing, we can’t guarantee that the user will be included in the Segment Extension once that particular refresh is complete. Conversely, users who were in the Segment Extension before the refresh that no longer meet the criteria will continue to match your default segment until the refresh process is complete and updates are applied.

### Step 6: Use your extension in a segment

After you have created a Segment Extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. Start by choosing Braze Segment Extension from the filter list under the User Attributes section.

From the Braze Segment Extension filter list, choose the Segment Extension you wish to include or exclude in this segment.

To view the Segment Extension criteria, select View Extension Details to show the details in a new window.

Now you can proceed as usual with creating your segment.

## Frequently asked questions

### Can I create a Segment Extension that uses multiple custom events?

Yes. You can add multiple events or reference multiple Snowflake tables when using SQL Segment Extensions.

When using Simple extension Segment Extensions, you can select one custom event, one purchase event, or one channel interaction. However, you can combine multiple Segment Extensions with an AND or OR when creating the default segment.

### Can I archive Segment Extensions if they exist in an active campaign?

No. Before you can archive a Segment Extension, you need to remove it from all active messaging.

### Can I use arrays in Segment Extensions?

Yes. To use arrays, append brackets ([]) to your property name. If your property is location_code, you would enter location_code[].

Braze uses [] to traverse arrays and check if any item in the traversed array matches the event property. For example, you could create a Segment Extension of users who match at least one value of an array property.

### How does Braze calculate the time period for a relative time period of “last __ days”?

When Segment Extensions calculates the relative time period (“last X days”), the start time is set to midnight UTC. For example, for a Segment Extension that refreshes at 2024-09-16 21:00 UTC and specifies 10 days, the start time is set to 2024-09-06 00:00 UTC, not 2024-09-06 21:00 UTC.

However, you can specify the time zones by using SQL segments to identify users who performed the custom event 10 days ago based on midnight in company time, or users who performed the event 10 days ago based on the current time.

- 

New Stuff!
