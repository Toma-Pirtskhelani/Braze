---
url: https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts
slug: docs__user_guide__administer__global__workspace_settings__logs_and_alerts__api_usage_alerts
title: "API usage alerts"
description: "This article provides an overview of the API usage alerts, which allows you to proactively detect unexpected traffic."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# API usage alerts

API usage alerts provide critical visibility into your API usage, allowing you to proactively detect unexpected traffic. By setting up these alerts to track key API request volumes, you can receive real-time notifications and address problems before they impact your marketing campaigns.

## About API usage alerts

You can use API usage alerts to monitor request volumes for the following categories:

 API Category | 
 Details | 

 REST API Endpoints | 
 Tracks usage of all REST API calls made to Braze’s backend, such as sending messages, creating campaigns, or exporting users. | 

 SDK API Requests | 
 Tracks API requests made from Braze SDKs in client apps, such as triggering in-app messages or syncing user data.

*Only available to customers who have purchased Monthly Active Users – CY 24-25. | 

## Creating an API usage alert

To create an API usage alert:

- Go to Settings > APIs and Identifiers > API Usage Alerts, then create a new alert.
 
- Enter a name for your alert and choose the REST API endpoints and API keys you’d like to be alerted for.
 
- Define your alert criteria by choosing one or more response codes and specifying the alert thresholds.
 
- When you’re finished, toggle Alert enabled.

## Alert thresholds

When you define your alert criteria you can adjust the following thresholds:

 Alert thresholds

 Field | 
 Description | 

 Threshold condition | 
 
 Defines the conditions leading up to the threshold volume that you’d like to be alerted on. The following are supported:

- Increased by or Decreased by: Compares requests against the previous time window.
 
- Increased by percentage or Decreased by percentage: Compares the percentage change in requests against the previous time window.
 
- Greater than or equal, or less than or equal: Counts requests in a time window.
 
 | 

 Threshold volume | 
 Used in conjunction with threshold condition. | 

 Within | 
 The time window for alert evaluation. | 

## Setting up alert notifications

You can set up an email alert, a webhook alert or both. Webhook alerts can be very useful for use cases such as sending an alert to external platforms, such as a Slack channel. For an example, see our documentation on integrating alerts with Slack for our notification preferences.

### Sample payload

The following is a sample payload for the body of an API Usage Alert webhook.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

```
 | 
```
{
 "text": "Your My First API Usage Alert alert has triggered. Please note that this alert is reset every 8 hours, and only one notification will be sent per reset period. You can view your alert and usage here: <link>.",
 "data": {
 "alert_name": "My First API Usage Alert",
 "alert_type": "API Usage Alert",
 "app_group_name": "My Workspace",
 "alert_criteria": {
 "response_codes": "201, 202 and 203",
 "threshold_condition": "increase by",
 "threshold_volume": "50%",
 "within": "1 hour"
 },
 "timeframe_start": "2025-03-20 15:35:00",
 "timeframe_end": "2025-03-20 16:35:00",
 "volume": 1500,
 "previous_timeframe_start": "2025-03-20 14:35:00",
 "previous_timeframe_end": "2025-03-20 15:35:00",
 "previous_volume": 1000
 }
}

```
 | 

note

The previous_timeframe_start, previous_timeframe_end, and previous_volume fields are optional and only appear when the alert uses a comparative threshold condition (increase by, decrease by). These fields are omitted for greater than or equal or less than or equal alerts.

#### Payload field details

 Field | 
 Type | 
 Description | 

 text | 
 string | 
 Human-readable alert message. | 

 data.alert_name | 
 string | 
 Name of the alert. | 

 data.alert_type | 
 string | 
 Type of alert (always "API Usage Alert"). | 

 data.app_group_name | 
 string | 
 Workspace name. | 

 data.alert_criteria.response_codes | 
 string | 
 Response codes selected for the alert. Returns "all response codes" if none are selected, a single code like "201", or multiple codes like "201, 202 and 203". | 

 data.alert_criteria.threshold_condition | 
 string | 
 Condition type: "increase by", "decrease by", "greater than or equal", or "less than or equal". | 

 data.alert_criteria.threshold_volume | 
 string or number | 
 Threshold value. When the condition uses a percentage, this is a string ending in % (for example, "50%"). When the condition uses a numeric value, this is a number (for example, 50). | 

 data.alert_criteria.within | 
 string | 
 Time window for alert evaluation (for example, "1 day"). | 

 data.timeframe_start | 
 string | 
 Start of the alert timeframe in UTC format YYYY-MM-DD HH:MM:SS. | 

 data.timeframe_end | 
 string | 
 End of the alert timeframe in UTC format YYYY-MM-DD HH:MM:SS. | 

 data.volume | 
 number | 
 Request volume during the alert timeframe. | 

 data.previous_timeframe_start | 
 string | 
 (Optional) Start of the previous timeframe. Only present for comparative threshold conditions. | 

 data.previous_timeframe_end | 
 string | 
 (Optional) End of the previous timeframe. Only present for comparative threshold conditions. | 

 data.previous_volume | 
 number | 
 (Optional) Request volume during the previous timeframe. Only present for comparative threshold conditions. | 

### Example alerts

Here are some ways to set up your API usage alert configurations to be notified in the following scenarios.

- api health
 
- endpoint rate limit
 
- api-triggered campaigns
 
- partner integrations

You can set up alerts to monitor the general health of your API. For example, you can set up these alerts when API errors increase drastically, such as 20% from the previous hour.

 Endpoint | 
 API key | 
 Response code | 
 Threshold condition | 
 Threshold volume | 
 Within | 

 All endpoints | 
 All API keys | 
 4XX and 5XX | 
 Increased by 10% | 
 10 | 
 1 hour | 

Be alerted when your workspace reaches its rate limit for /users/track endpoint. You can also apply this configuration for other Braze endpoints.

 Endpoint | 
 API key | 
 Response code | 
 Threshold condition | 
 Threshold volume | 
 Within | 

 /users/track | 
 All API keys | 
 429 | 
 Greater than or equal to | 
 100 | 
 1 hour | 

This alert configuration notifies you when errors occur for API triggered campaigns and Canvases, some of which may be high-priority.

 Endpoint | 
 API key | 
 Response code | 
 Threshold condition | 
 Threshold volume | 
 Within | 

- /campaigns/trigger/send
- /canvas/trigger/send
- /messages/send | 
 All API keys | 
 4XX and 5XX | 
 Greater than or equal to | 
 1 | 
 1 hour | 

Use the following alert configuration to be alerted when a partner integration stops sending data to Braze.

 Endpoint | 
 API key | 
 Response code | 
 Threshold condition | 
 Threshold volume | 
 Within | 

 All endpoints | 
 The API key used for your partner integration | 
 All response codes | 
 Less than or equal to | 
 0 | 
 1 day | 

## Considerations

- Each active alert will only send an email or webhook notification once every 8 hours. This is to prevent too many notifications from a single alert. If your alert is notifying you prematurely, consider editing the alert criteria to better match your use case.
 
- You can have up to 10 alerts per workspace.

- 

New Stuff!
