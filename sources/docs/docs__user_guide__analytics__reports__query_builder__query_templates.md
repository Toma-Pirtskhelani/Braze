---
url: https://www.braze.com/docs/user_guide/analytics/reports/query_builder/query_templates
slug: docs__user_guide__analytics__reports__query_builder__query_templates
title: "Query Builder templates"
description: "This reference article lists the types of reports you can create using Braze data from Snowflake in the Query Builder."
section: user_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Query Builder templates

Access Query Builder templates by selecting Query Template when creating a report. All templates surface data from up to the last 60 days, but you can directly edit that and other values in the editor.

For definitions of the metrics that may appear in your Query Builder reports, refer to the Report Metrics Glossary and filter by the respective channel.

## Channel templates

 Query name | 
 Description | 

 Channel engagement and revenue | 
 This report shows, for each channel, all engagement metrics (such as opens and clicks), revenue, number of transactions, and average price. 
- Number of transactions: Number of purchase events 
- Average price: Revenue divided by transactions | 

 Purchases and revenue by segment | 
 This report shows metrics for the messages sent for a specific segment. 

 Purchase metrics are unique throughout the reporting period. One user can generate at most one purchase. Revenue takes into account every purchase from the reporting period. | 

 Purchases and revenue for variants or steps, by segment | 
 This report shows metrics for the variants or Canvas steps of the messages sent to each segment. 

 Purchase metrics are unique throughout the reporting period. One user can generate at most one purchase. Revenue takes into account every purchase from the reporting period. | 

 Top/bottom messaging for purchases | 
 This report shows purchase metrics for the top or bottom campaigns, Canvases, or Canvas steps. Each row is a campaign, Canvas, or Canvas step. You must specify whether to display the top or bottom performers, and the specific metric to run this analysis for (such as Unique purchases upon receipt, Revenue upon receipt, Unique recipients). 

 The rows in top performer reports will be ordered from best to worst, while the rows in bottom performer reports will be ordered from worst to best. | 

## Campaign templates

 Query name | 
 Description | 

 Campaign revenue by country | 
 This report shows revenue per country for a specific campaign. To run this report, you must specify the API identifier for a campaign. You can find a campaign’s API identifier at the bottom of that campaign’s details page. 

 This report shows, for each country, the amount of revenue generated, number of orders, number of returns, net revenue, and gross revenue.

- Orders: Number of purchase events 
- Returns: Number of purchase events with negative revenue values 
- Net revenue: Revenue of all non-returns 
- Gross revenue: Revenue that includes the value of returns | 

## Canvas templates

 Query name | 
 Description | 

 Canvas revenue by country | 
 This report shows revenue per country for a specific Canvas. To run this report, you must specify the API identifier for a Canvas. You can find the Canvas API identifier under Analyze Variants. 

 This report shows, for each country, the amount of revenue generated, number of orders, number of returns, net revenue, and gross revenue.

- Orders: Number of purchase events 
- Returns: Number of purchase events with negative revenue values 
- Net revenue: Revenue of all non-returns 
- Gross revenue: Revenue that includes the value of returns | 

## Email templates

 Query name | 
 Description | 

 Email bounces per domain | 
 The number of bounces per email domain, broken down into total bounces, hard bounces, and soft bounces. 
 | 

 Email delivery metrics by day | 
 This report shows metrics for the messages sent on each day, such as how many emails were sent, delivered, soft bounced, and hard bounced. 

 All metrics are unique throughout the reporting period. For example, if a welcome email soft bounced one time on November 21, two times on November 22, and was never delivered: 
- The Soft Bounces metric for November 21 increases by one.
- The Soft Bounces metric for November 22 is not affected. | 

 Email engagement metrics by segment | 
 This report shows metrics for the messages sent to each segment, such as how many emails were sent, delivered, soft bounced, and hard bounced. 

 All metrics are unique throughout the reporting period. For example, if a welcome email soft bounced one time on November 21, two times on November 22, and was never delivered: 
- The Soft Bounces metric for November 21 increases by one. 
- The Soft Bounces metric for November 22 is not affected. | 

 Email engagement metrics for variants or steps, by segment | 
 This report shows metrics for the variants or Canvas steps of the messages sent to each segment. These metrics include how many emails were sent, delivered, soft bounced, and hard bounced. 

 All metrics are unique throughout the reporting period. For example, if a welcome email soft bounced one time on November 21, two times on November 22, and was never delivered: 
- The Soft Bounces metric for November 21 increases by one. 
- The Soft Bounces metric for November 22 is not affected. | 

 Email performance by country | 
 This report shows the following metrics for each country: sends, indirect open rate, and direct open rate. Country is the country of the user at the time of push send. 

 | 

 Email Subscription Change Logs | 
 This report shows the metrics that were logged about each user’s subscription change, such as their email address, subscription status, the time their status was changed, and the associated Canvas or campaign. | 

 Email subscription group opt-ins and opt-outs | 
 This report shows the number of unique user opt-ins and opt-outs for any email subscription group for each week. You must have at least one email subscription group in the workspace to run this query. 

 | 

 Email URLs clicked | 
 This report shows the number of clicks each link in an email had. To run this report, you’ll need to specify the API identifier for a campaign or Canvas. You can find a campaign’s API identifier at the bottom of that campaign’s details page and the Canvas API identifier under Analyze Variants. 

 This report shows de-personalized links and a count of clicks for each link. Your CSV download will include the user IDs of all users that clicked, the link they clicked on, and a timestamp of when they clicked. 

 De-personalized URLs: URLs that are stripped of Liquid tags. 

 | 

 Top/bottom messaging for email engagement | 
 This report shows email engagement metrics for the top or bottom campaigns, Canvases, or Canvas steps. You must specify whether to display the top or bottom performers, and the specific metric to run this analysis for (such as Sent, Soft Bounces, and Unique Opens). 

 The rows in top performer reports will be ordered from best to worst, while the rows in bottom performer reports will be ordered from worst to best. 

 | 

## Mobile templates

 Query name | 
 Description | 

 Device carriers | 
 The number of users per device carrier, such as Verizon and T-Mobile. 

 | 

 Device models | 
 The number of users per device model, such as iPhone 15 Pro and Pixel 7. 

 | 

 Device operating systems | 
 The number of users per operating system, such as 17.4 and Android 14. 

 | 

 Device screen resolutions | 
 The number of users per device screen resolution, such as 1179x2556 and 750x1334. 

 | 

 SMS Error Codes | 
 This report shows the error type and number of errors for each SMS error code. 

 | 

 SMS Provide Errors by User | 
 This report shows SMS error codes for a specific user. | 

## Push templates

 Query name | 
 Description | 

 Push performance by country | 
 This report shows the following metrics for each country: deliveries, open rate, and click rate. Country is the country of the user at the time of email send. 

 | 

## Segment breakdown

 Query name | 
 Description | 

 Email engagement metrics by segment | 
 This report shows email performance metrics broken down by segment at the campaign or Canvas level. | 

 Purchases and revenue by segment | 
 This report shows purchase and revenue metrics broken down by segment for a specific campaign or Canvas. | 

 Top/bottom messaging for email engagement | 
 This report shows the campaigns, Canvases, or Canvas steps that were the highest or lowest performers for a specified email engagement metric. | 

 Top/bottom messaging for purchases | 
 This report shows the campaigns, Canvases, or Canvas steps that were the highest or lowest performers for a specified purchase or revenue metric. | 

 Push performance by segment | 
 This report shows push metrics broken down by segments. | 

- 

New Stuff!
