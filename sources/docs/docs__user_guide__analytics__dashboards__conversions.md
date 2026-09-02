---
url: https://www.braze.com/docs/user_guide/analytics/dashboards/conversions
slug: docs__user_guide__analytics__dashboards__conversions
title: "Conversions dashboard"
description: "The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods."
section: user_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Conversions dashboard

The conversions dashboard analyzes conversions across campaigns, Canvases, and channels, by using various attribution methods. When measuring your conversions, you can specify the time frame, conversion event, and conversion window.

## Setting up your report

To set up your conversions dashboard report:

- Go to Analytics > Conversions.
 
- Select a Date Range for your report, up to a 90-day window.
 
- Select the campaigns or Canvases (or both) to analyze.

- (optional) Filter campaigns and Canvases by selecting a tag.

- Select the Channel(s) to analyze for your messages.
 
- Select a Breakdown by layer to view different dimensions of data, such as by variant, Canvas step, country, or language.
 
- (Optional) If you want to calculate conversions of an event that wasn’t set up as a conversion event on the campaign or Canvas, turn on Use custom events.
 
- Select an attribution method through which to analyze the selected messages.

note

If you’re analyzing conversions for multiple channels, your Attribution Method will default to Last-Touch Attribution.

- Select Create to run the report.

After the page loads, select a Conversion Event to filter the report for conversion data. The available selections will include the events that were pre-configured on the Canvases and campaigns. If you selected a custom event when setting up your report (step 6), this option isn’t available.

### Using custom events

For custom event metrics to appear on the conversions dashboard, you must have a conversion event and a Canvas entry event in the date range specified on the page.

To calculate conversions of an event that wasn’t set up as a conversion event on the campaign or Canvas, select a specific custom event to use as a conversion event.

- When setting up your report, turn on Use custom events.
 
- Select a custom event to use as the conversion event.
 
- Select the conversion window within which that event should have occurred to be counted as a conversion.

note

If you select a custom event, you won’t see the Conversion Event dropdown on the page and will have to re-run to report to view conversions for different custom events.

### Considerations

For a user to be counted in the report, they must meet the following criteria within the selected date range:

- Enter the Canvas or campaign.
 
- Log an attribution method.
 
- Perform the conversion event.

For example, let’s say a user does the following:

- Enters the Canvas on September 30.
 
- Logs an attribution method on October 1.
 
- Performs the conversion event on October 2.

This user will not appear in a report with a date range of October 1 to October 7. This is because the user entered the Canvas before the reporting period, even though the conversion event occurred within the defined date range. For the user to appear in a report, the date range must include September 30.

## Understanding your report

Your report is split into three sections:

- Conversion details
 
- Conversion funnel
 
- Conversions over time

### Conversion details

The conversion details table always shows one column for Recipients and another for Conversions (rate and total). The remaining two table columns that appear depend on the options you selected when setting up your report.

The following table describes possible metrics.

 Metric shown | 
 Description | 

 Recipients | 
 The number of users who received a message through the selected channel within the report’s date range | 

 Conversion Rate (Recipients) | 
 Calculated as: (Number of conversions) / (Number of recipients) | 

 Attribution method | 
 Defined by the attribution method you selected when you set up the report. For Last Touch attribution or if multiple channels are selected, this appears as Touches. | 

 Conversion Rate (Attribution method) | 
 Defined by the attribution method you selected when you set up the report. If multiple channels are selected, this defaults to last-touch attribution. | 

If you selected breakdown-level details for campaigns or Canvases when setting up your report (step 5), you can select Expand to expand the table.

### Conversion funnel

This bar graph shows the absolute counts for each engagement event based on the selected channel. The conversions count will be defined as per the selected attribution method.

By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, select the name of the campaign or Canvas that you’d like to exclude. For additional details on the engagement event, you can hover over each bar.

To download the time series data, select a download option: PNG, JPEG, PDF, SVG, or CSV.

note

This graph only shows data for a single channel at a time. Use the Channel dropdown on the chart to select a single channel.

### Conversions over time

This time series graph includes a representation of the conversions per campaign or Canvas over time. By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you’d like to exclude.

To download the time series data, select Chart context menu and then select your download option. Available options are PNG, JPEG, PDF, SVG, or CSV.

### Attribution methods

 Attribution method | 
 Definition | 
 Rate calculation | 
 Channel-specific options | 

 Upon Receipt | 
 Total number of conversions that occurred after message receipt | 
 Calculated as (Unique Received Conversions) / (Unique Recipients) | 
 
- Upon email delivery
- Upon SMS delivery | 

 Upon Send | 
 Total number of conversions that occurred after message send | 
 Calculated as (Unique Send Conversions) / (Unique Recipients) | 
 
- Upon push send
- Upon Content Card send
- Upon SMS send | 

 Upon Open | 
 Total number of conversions that occurred after message open | 
 Calculated as (Unique Open Conversions) / (Unique Recipients) | 
 
- Upon email open
- Upon push open | 

 Upon Click | 
 Total number of conversions that occurred message click | 
 Calculated as (Unique Click Conversions) / (Unique Recipients) | 
 
- Upon email click
- Upon Content Card click
- Upon IAM click | 

 Upon Impression | 
 Total number of conversions that occurred after an impression | 
 Calculated as (Unique Impression Conversions) / (Unique Recipients) | 
 
- Upon IAM impression
- Upon Content Card impression | 

 Upon Last-Touch | 
 Conversions that give all credit to the last-touched or clicked message during the conversion window. | 
 Calculated as (Number of Touches) / (Unique Recipients) | 
 Last-touch attribution is automatically selected if multiple channels are added to the report. | 

## Terms to know

 Term | 
 Definition | 

 Touch | 
 A physical interaction or touchpoint with a message.

Touches can include:

- Email Click
- Push Open
- Content Card Click
- In-App Message Click
- SMS Click | 

## Troubleshooting

### Why do I have low campaign or Canvas conversions?

Your conversions might not be as high as you expect them to be when compared to previous campaigns or your expectations. Conversions depend on two key functions: event tracking and conversion deadlines.

To troubleshoot, check your event tracking and conversion deadlines.

#### Event tracking

When a campaign triggers a session start or custom event, you want to ensure that this event, or session, is happening frequently enough to trigger the message. Check the home dashboard for session data, or your custom events report.

#### Conversion deadlines

For each conversion event that you select per campaign, you set the deadline. This means you are setting a time limit within which a conversion must happen in order for it to count toward each respective campaign.

Review information on conversion tracking rules to understand your campaign metrics. For user conversions in Canvas, refer to Canvas FAQ.

### Why don’t email open totals match Campaign Analytics?

Campaign Analytics and Report Builder count machine opens in Unique Opens. See Does the Unique Opens metric include Machine Opens? in the email FAQ for details.

On the Conversion Dashboard, Upon Email Open attribution counts only human opens. Machine opens are not included in the open count used for that attribution method.

Because of that difference, open totals in Campaign Analytics can be higher than open counts used in Conversion Dashboard attribution for the same campaigns. Compare metrics within the same surface, or use Other Opens in Campaign Analytics when you want human engagement without machine opens.

- 

New Stuff!
