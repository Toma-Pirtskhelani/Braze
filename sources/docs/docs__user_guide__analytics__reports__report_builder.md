---
url: https://www.braze.com/docs/user_guide/analytics/reports/report_builder
slug: docs__user_guide__analytics__reports__report_builder
title: "Report Builder"
description: "This reference article describes the Report Builder feature."
section: user_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Report Builder

This page covers how to use Report Builder to create and view granular reports using Braze data, and how to add reports to dashboards.

The following video provides an overview of how to create and customize reports in Report Builder.

## Using a report template

- Go to Analytics > Report Builder (New).
 
- Select the More options arrow next to the Create New Report button, and then select Use a report template.

- Select one of the report templates from the Braze template library.

- Use the Row items and Tags dropdown to find relevant reports to your use cases.

- Follow step 3 and onward in Creating a report to further customize the report to fit your use case.

## Creating a report

- Go to Analytics > Report Builder (New).
 
- Select Create New Report.
 
- In the Rows dropdown, select what you’d like to report on:

- Campaigns
 
- Canvases
 
- Campaigns and Canvases
 
- Channels
 
- Tags

Note that your Rows selection impacts the metrics that you can view. For example, you can view multivariate metrics only if you report on Canvases, or Campaigns with a Variant drilldown. You can’t view those metrics when reporting on Campaigns and Canvases, even if those campaigns and Canvases have multivariate tests.

- (Optional) Select Add drilldown to break down your data into more granular views:

- Channels
 
- Date

- Use this to split your data into smaller time ranges. For example, if you’re interested in how your campaigns performed by day, select the following configuration:

- Rows: Campaigns
 
- Grouping: Date
 
- Interval: Days

- Variants
 
- Campaigns and Canvases

tip

Try out different configurations of drilldown options to explore the many ways you can break down your data.

- In the Columns section, select Customize Metrics.

- Browse metrics by category and select the corresponding checkbox to add a metric to your report.

- Reorder the metrics and columns by dragging the dotted icon up or down.

- In Report content, configure the date range for which you’d like to include data in your report.
 
- Then, depending on your selections in step 3, choose to manually or automatically add campaigns, Canvases, or both to your report.

- Add manually: Choose each campaign or Canvas to include in the report by using the filters for Last Sent dates and tags or channels, or searching the campaign or Canvas name.

- Add automatically: Set rules for which campaigns or Canvases to include in the report. You’re only required to select one field on this page.

- Note that as additional campaigns or Canvases satisfy the conditions you set on this screen, they are automatically added to future runs of your report.
 
- Banners isn’t an option in the Channel dropdown, so you can’t use channel rules to automatically add Banner campaigns or Canvases. You can still include Banner KPIs in your report metrics.

- Run the report by selecting Save & Run.

note

The report may take up to a few minutes to run, depending on the date range and number of campaigns or Canvases you selected in the configuration stage.

## Metrics availability

Your selection for Rows affects the metrics you can select.

tip

If you want to report on Canvas variants or steps, select Canvases for rows and either leave the field empty or select Date as the drilldown. After running the report, a Canvas View dropdown appears on the results page to view metrics for the Canvas only, or group metrics by variant, step, or message.

 When editing your report, the preview table shows a maximum of 50 rows. Run the report to view all rows on the results page with pagination (100 rows per page) or export the full dataset as a CSV.

 Metric | 
 Description | 

 Conversion metrics | 
 Available for Campaigns, Canvases, Campaigns and Canvases. | 

 Entries | 
 Available for Campaigns, Canvases, Campaigns and Canvases, Tags. | 

 Last Sent Date | 
 Available for Campaigns, Canvases, Campaigns and Canvases. Only displays for scheduled campaigns—does not populate for action-based or API-triggered campaigns. | 

 Sends | 
 Available for each relevant channel. | 

 Messages Sent | 
 Available for Campaigns, Canvases, Campaigns and Canvases, Tags. | 

 Subject line | 
 Available for email Campaigns with Variant drilldown, Canvases, and Canvases with Variant drilldown. | 

 Total Revenue | 
 Available for Campaigns, Canvases, Campaigns and Canvases, Tags. Unavailable with Channels drilldown. | 

 Unique Impressions | 
 Available for Campaigns, Canvases, Campaigns and Canvases, Tags. | 

 Unique Recipients | 
 Available for Campaigns, Canvases, Campaigns and Canvases, Tags. Unavailable with Channels drilldown. | 

### Deleted message variants

Statistics for deleted message variants are not displayed when you break down your report by campaigns or Canvases. However, channel-level totals include all statistics regardless of whether the variant was deleted. For example, Sends for email include all email sends, but if you break down those statistics by campaign, the numbers may be lower because sends for deleted message variants are filtered out.

In the same report, Unique Recipients can be higher than Unique Impressions when a message variant was deleted after send. Campaign-level Unique Recipients can still include users who received the deleted variant, while Unique Impressions omit stats from deleted variants in message-level aggregations.

## Viewing a report

After running your report, you can view your results in table format on the report results page.

### Creating a report chart

At the bottom of the page you can create a chart of your data by selecting a Chart type and configuring the chart metrics. By default, you’ll see the first metric.

note

To create a line chart, select Date as a drilldown option when configuring the report. This displays trends over time.

#### Downloading a report chart

To download an image of the report chart, select the dotted icon then choose a download option.

## Sharing a report

You can share a dashboard link to the report by selecting Share and one of these options:

- Share a link: Copy and share the link.
 
- Send or schedule an email: Send an email immediately or at a designated time that contains a download link that expires after one hour. You can select recipients from the company users listed in the Email Recipients dropdown or enter any other email address.

note

The Email Recipients dropdown lists Braze company users only, and saves their email addresses across report schedules. External email addresses must be manually entered each time you create a new report schedule. If you frequently send reports to external recipients, such as a partner contact, consider adding them as a company user with appropriate permissions so their address appears in the dropdown.

- Download CSV: Download a CSV of the report.

## Adding a report to a dashboard

- Select the dotted icon at the top of the report table.
 
- Select Add to dashboard.
 
- Select whether you want to create a new dashboard or add to an existing dashboard.

- Follow the steps in Dashboard Builder to learn more about building a dashboard.

## Team permissions

Report Builder reports don’t support team assignment like campaigns or Canvases. You can’t limit a saved report to a specific team when you create it.

Users with team-level “View Dashboard Reports” permission (rather than workspace-level) can still use Report Builder, but report visibility is limited:

- These users only see reports where every selected campaign and Canvas is assigned to their teams.
 
- Reports with Channels as rows are hidden.
 
- Reports that use automatic selection to add campaigns or Canvases are hidden, because Braze can’t verify team access for messages that may be added when the report runs.

Report Builder (legacy) scopes which campaigns and Canvases you can add to a report by team, but saved reports are not filtered from the list the same way as in Report Builder (New). For permission setup, see Setting user permissions and Teams.

## Troubleshooting

### Report shows no sends for a campaign or Canvas

A campaign or Canvas appears in the report when its Last sent date falls in the Last sent window you configured. Sends and other metrics only populate for activity inside the Show data for date range. If the message didn’t send during Show data for, the row can still list the campaign or Canvas with zero sends.

For example, suppose Last sent is January 1, 2025–April 14, 2025, so a campaign is included, but Show data for is December 1, 2024–January 14, 2025. If that campaign had no sends in December or January, it still appears in the table with no send metrics.

### Download link has expired

Report download links expire after one hour. If your link has expired, generate a new report and download it within the hour. There is no way to extend the expiry time.

If you have an Amazon S3 bucket connected in Partner Integrations, you may be able to retrieve data from older reports by browsing your S3 bucket directly.

- 

New Stuff!
