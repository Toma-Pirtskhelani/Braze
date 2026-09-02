---
url: https://www.braze.com/docs/user_guide/analytics/dashboards/api_usage
slug: docs__user_guide__analytics__dashboards__api_usage
title: "API usage dashboard"
description: "This article provides an overview of the API usage dashboard."
section: user_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# API usage dashboard

The API usage dashboard lets you monitor your incoming REST API traffic into Braze to understand your trends within your usage of our REST APIs and to troubleshoot any potential issues.

## About the API usage dashboard

To view your API usage dashboard, go to Settings > APIs and Identifiers, then select Dashboard.

The default dashboard is a view of all incoming REST API requests for your workspace over the last day (24 hours). Depending on your use case, you can adjust the dashboard controls to filter or group traffic and also configure the time range of the dashboard.

## Available metrics

The API usage dashboard includes the following statistics:

 Metric | 
 Description | 

 Total requests | 
 The total number of requests sent to Braze for your current workspace, given the filters and controls applied to the dashboard. | 

 Success rate | 
 The percentage of total requests where Braze issued a 2XX success response. | 

 Error rate | 
 The percentage of total requests where Braze issued a 4XX or 5XX error response. | 

## Using the dashboard

### Filters

Select Filters to apply filters to narrow the view of REST API traffic for your workspace, including:

- API key
 
- Endpoint
 
- Response code

### Group data

You can group data into various data series to explore different patterns in your usage, including:

- Response codes (default)
 
- API endpoint
 
- API key
 
- Success and failure only

### Date

Adjust the date filter to show a smaller or greater time range as needed. This includes:

- Today (default)
 
- Custom
 
- Last 3 Hours
 
- Last 6 Hours
 
- Last 12 Hours
 
- Last 24 Hours
 
- Yesterday
 
- Last 7 Days
 
- Last 14 Days
 
- Last 30 Days
 
- Last Month to Date

note

The Last 3 Hours and Last 6 Hours options will show traffic by minutes. Larger time periods will show traffic every five minutes, hour or day.

## Considerations

The API usage dashboard includes all REST API requests that Braze received and returned a 2XX, 4XX, or 5XX response for. This includes Data Transformation outputs and Cloud Data Ingestion syncs. SDK traffic and User Update steps are not included in this dashboard.

Data shown in the dashboard may have up to a short delay in showing recent traffic. During periods of high usage, you can refresh the dashboard up to 4 times per minute. You may need to wait a few minutes before refreshing the dashboard again.

### API keys in request body

When API keys are sent in the request body instead of the request header, some requests may not appear in the API usage dashboard. This can lead to incomplete data in the dashboard and make it difficult to accurately monitor API usage.

For the most accurate reporting in the API usage dashboard, include API keys in the request header rather than in the request body.

## Related articles

- API usage alerts
 
- Rate limits
 
- Bearer token authentication

- 

New Stuff!
