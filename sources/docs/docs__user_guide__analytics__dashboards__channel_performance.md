---
url: https://www.braze.com/docs/user_guide/analytics/dashboards/channel_performance
slug: docs__user_guide__analytics__dashboards__channel_performance
title: "Channel performance dashboards"
description: "This reference article covers the channel performance dashboard, which allows you to view performance metrics for entire channels across both campaigns and Canvases."
section: user_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Channel performance dashboards

Channel performance dashboards show aggregate performance metrics for an entire channel, from both campaigns and Canvases. These dashboards are currently available for email, push, and SMS.

## Dashboards

Select a tab to view details for available channel performance dashboards.

- email performance
 
- email insights
 
- sms performance
 
- push performance

### Email performance dashboard

View your email performance dashboard by going to Analytics > Email Performance, and selecting the date range for the period you want to view data. Your date range can be up to one year in the past.

note

To view the Email Performance dashboard, you need the “View Usage Data” or “View Dashboard Reports” permission.

#### How metrics are calculated

The calculations for different metrics in the email performance dashboard are the same as those on an individual message level (such as campaign analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you’ve selected. To learn more about these definitions, refer to Email metrics.

Each tile shows the rate metric first, followed by the count metric (with the exception of Sends, which displays the count metric followed by the average per day). For example, the unique clicks tile contains the Unique click rate from your selected time period and the count of the total number of unique clicks from that time period. Each tile also shows the comparison to the last period.

 Metric | 
 Type | 
 Calculation | 

 Sends | 
 Count | 
 Total number of sends across each day in the date range | 

 Delivery rate | 
 Rate | 
 (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) | 

 Bounce rate | 
 Rate | 
 (Total number of bounces across each day in the date range) / (Total number of sends across each day in the date range) | 

 Unsubscribe rate | 
 Rate | 
 (Total number of unique unsubscribes across each day in the date range) / (Total number of deliveries for a date range)

This uses unique unsubscribes, which is also used in Campaign Analytics, Overview, and Report Builder. These unsubscribes are logged across all sources (such as the , REST API, CSV imports, emails, and list unsubscribes). The unsubscribe rates in Campaign and Canvas analytics are unsubscribes that occur as a result of an unsubscribe click on a Braze-delivered email. | 

 Unique open rate | 
 Rate | 
 (Total number of unique opens across each day in the date range) / (Total number of deliveries for a date range) | 

 Other opens rate | 
 Rate | 
 (Total number of total other opens across each day in the date range) / (Total number of deliveries for date range)

Other opens includes emails that haven’t been identified as machine opens, such as when a user opens an email. This metric is non-unique and is a sub-metric of total opens. | 

 Unique click rate | 
 Rate | 
 (Total number of unique clicks across each day in the date range) / (Total number of deliveries for a date range) | 

 Unique click to open rate | 
 Rate | 
 (Total number of unique clicks across each day in the date range) / (Total number of unique opens across each day in the date range) | 

### Email insights dashboard

The email insights dashboard tracks where and when your customers are interacting with your emails. These reports can provide rich and granular data on how to optimize your emails to drive greater engagement. The email insights dashboard includes up to the last six months of data. To access the dashboard, go to Analytics > Email Performance > Email Insights.

#### Engagement by Device

The Engagement by Device report provides a breakdown of what devices your users are using to engage with your email. This data tracks email engagement across mobile, desktop, tablet, and other device types. This data is based on the user agent string passed from your users’ devices.

note

If you use CloudFront as your CDN, make sure your users’ user agent is passed along to the ESP. Otherwise, every user agent will be “Amazon Cloudfront”.

The “Other” category includes any user string that cannot be identified as desktop, mobile, or tablet. For example, television, car, video game console, OTT (over-the-top or streaming), and similar. This may also include null or empty values.

To better understand what is in this “Other” category, you can extract the user agents using either of these options:

- Currents will send you the exact user agent string that was retrieved from your users’ devices.
 
- Leverage our Query Builder to use SQL or our AI Query Builder to view the user agents.

For email opens, Braze will separate Google Image Proxy, Apple Image Proxy, and Yahoo Mail Proxy. These services will cache and load all embedded images in an email before it’s delivered to the recipient. As a result, this will trigger an email open from the mailbox provider’s servers rather than the recipient’s server, which can lead to inflated email opens. These services are meant to enhance privacy, security, performance, and efficiency when loading images. This can also contain real opens from recipients, as these proxy services mask the user agent, and Braze categorizes proxy data using the user agent.

#### Engagement by Mailbox Provider

The Engagement by Mailbox Provider report displays the top mailbox providers contributing to your clicks or opens. You can click into specific premier mailbox providers to drill down into specific receiving domains. For example, if Microsoft is listed on this report as one of your top mailbox provider metrics, you can further view details for their receiving domains, such as “outlook.com”, “hotmail.com”, “live.com”, and more.

#### Time of Engagement

The Time of Engagement report displays data on when users are engaging with your emails. This can help answer questions such as which weekday or what time sees the highest engagement from your customers. With these insights, you can experiment with the best day or time to send your messages to drive higher engagement. Note that these times are based on your company’s time zone.

The Day of the week engagement report breaks down opens or clicks by day of the week.

The Time of the day engagement report breaks down opens or clicks by each hour in a 24-hour time window.

For more information on analytics for your emails, check out Email reporting.

### SMS performance dashboard

To use your SMS performance dashboard, go to Analytics > SMS Performance, and select the date range for the period you want to view data. Your date range can be up to one year in the past.

#### How metrics are calculated

The calculations for different metrics in the SMS performance dashboard are the same as those on an individual message level (such as campaign analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you’ve selected. To learn more about these definitions, refer to SMS metrics.

Each tile shows the rate metric first, followed by the count metric (with the exception of Sends, which displays the count metric followed by the average per day). Each tile also shows the comparison to the last period.

 Metric | 
 Type | 
 Calculation | 

 Sends | 
 Count | 
 Total number of sends across each day in the date range | 

 Confirmed deliveries rate | 
 Rate | 
 (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) | 

 Delivery failures rate | 
 Rate | 
 (Total number of failures across each day in the date range) / (Total number of sends across each day in the date range) | 

 Rejections rate | 
 Rate | 
 (Total number of rejections across each day in the date range) / (Total number of sends across each day in the date range) | 

 Click rate | 
 Rate | 
 (Total number of clicks across each day in the date range) / (Total number of deliveries across each day in the date range) | 

 Total opt-ins | 
 Rate | 
 Total number of inbound message opt-ins across each day in the date range | 

 Total opt-outs | 
 Rate | 
 Total number of inbound message opt-outs across each day in the date range | 

### Push performance dashboard

The Push Performance dashboard gives you a single, channel-level view of push engagement, including sends, bounces, deliveries, and direct, influenced, and total open rates over a configurable time window. Use it to understand the overall health of your push channel without rolling up data from individual campaigns or Canvases.

To open the dashboard, go to Analytics > Dashboard Builder, then select Push Channel Dashboard. Your date range can be up to one year in the past.

#### How metrics are calculated

The calculations for different metrics in the push performance dashboard are the same as those on an individual message level (such as campaign analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you’ve selected. For metric definitions, refer to Report Metrics Glossary and filter by Push. For more information about influenced opens, see Influenced opens.

Each tile shows the rate metric first, followed by the count metric (with the exception of Sends, which displays the count metric only). Each tile also shows the comparison to the last period.

 Metric | 
 Type | 
 Calculation | 

 Sends | 
 Count | 
 Total number of sends across each day in the date range | 

 Bounce rate | 
 Rate | 
 (Total number of bounces across each day in the date range) / (Total number of sends across each day in the date range) | 

 Delivery rate | 
 Rate | 
 (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) | 

 Direct open rate | 
 Rate | 
 (Total number of direct opens across each day in the date range) / (Total number of deliveries across each day in the date range) | 

 Influenced open rate | 
 Rate | 
 (Total number of influenced opens across each day in the date range) / (Total number of deliveries across each day in the date range) | 

 Total open rate | 
 Rate | 
 (Total number of total opens across each day in the date range) / (Total number of deliveries across each day in the date range)

Total opens includes both direct opens and influenced opens. | 

## Dashboard filters

You can filter the data on your dashboard using the following filter options:

- Tag: Choose one tag. When applied, your dashboard will show metrics for only your selected tag.
 
- Platforms: (Push performance dashboard only) Choose a push platform, such as All Push, Android, iOS, Mobile combined, Kindle, or Web. When applied, your dashboard displays metrics for only your selected platform.
 
- Canvas: Choose up to 10 Canvases. When applied, your dashboard will show metrics for only your selected Canvases. If you select a tag filter first, then your options for Canvas filters will only include Canvases that have your selected tag.
 
- Campaign: Choose up to 10 campaigns. When applied, your dashboard will show metrics for only your selected campaigns. If you select a tag filter first, then your options for campaign filters will only include campaigns that have your selected tag.

## Comparing time periods

The channel performance dashboard automatically compares the time period you have selected in the date range versus the prior time period, totaling the same number of days. For example, if you choose “Last 7 Days” as your date range in the dashboard, the comparison to the last period will compare the metrics from the last seven days against the seven days prior. If you select a custom date range—let’s say May 10 to May 15, which is six days’ worth of data—the dashboard will compare the metrics from across those days to the metrics from May 4 to May 9.

The comparison is the percentage change between the last and current periods, calculated by taking the difference between the two periods and dividing it by the metric from the last period.

### Viewing changes in total counts and rates

You can switch between Show Change in Totals—which compares the total counts (such as the number of emails delivered) between the two periods—and Show Change in Rates—which compares the rates (such as the delivery rate).

## Frequently asked questions

### Why is my dashboard displaying empty values?

There are a few scenarios that could lead to empty values for a metric:

- Braze recorded zeros for that particular metric in your selected date range.
 
- You haven’t sent any messages during the selected date range.
 
- While there were metrics such as opens, clicks, or unsubscribes for a selected date range, there were no deliveries or sends. In this case, Braze will not calculate a rate metric.

To see more metrics, try expanding the date range.

### Why does my email dashboard display more Other Opens than Unique Opens?

For the Unique Opens metric, Braze will deduplicate any repeat opens registered by a given user (whether they include Machine Opens or Other Opens) so that only a single Unique Open is incremented if a user opens multiple times. For Other Opens, Braze does not de-deduplicate.

- 

New Stuff!
