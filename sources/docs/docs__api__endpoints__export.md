---
url: https://www.braze.com/docs/api/endpoints/export
slug: docs__api__endpoints__export
title: "Export endpoints"
description: "This reference article explains the Braze export endpoints, including prerequisites, what you can export, how data is delivered, and a full list."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export endpoints

With this collection of endpoints, you can access and export various levels of details on your KPIs, app sessions, users, segments, campaigns, and Canvases. Make sure you know your Braze instance, API key, and API identifier when building your parameters and request bodies.

## Prerequisites

Before you begin, make sure you have the following:

 Requirement | 
 Description | 

 Braze REST API key | 
 A REST API key with the appropriate export permissions for the endpoints you plan to call. API keys are scoped to specific endpoints, and permissions can’t be changed after creation. For details, refer to REST API key. | 

 Relevant identifiers | 
 The identifiers for the data you want to export, such as a campaign ID, segment ID, or Canvas ID. You can find these on the Braze dashboard. For a full list, refer to API identifier types. | 

 Cloud storage credentials (optional) | 
 If you’re exporting large datasets, connect an Amazon S3, Microsoft Azure Blob Storage, or Google Cloud Storage bucket to have export files written directly to your storage. | 

note

If you’re a marketer or team member without API access, coordinate with a developer or admin in your organization to set up API keys and integrations.

## What you can export

The following table summarizes the categories of data available through the export APIs.

 Category | 
 What it includes | 
 API reference | 

 Campaigns | 
 Performance analytics, campaign details, campaign lists, and send analytics | 
 Campaign endpoints | 

 Canvases | 
 Data series analytics, analytics summaries, Canvas details, and Canvas lists | 
 Canvas endpoints | 

 Segments | 
 Segment lists, segment analytics, and segment details | 
 Segment endpoints | 

 User data | 
 Full user profiles by identifier or by segment, and users by global control group | 
 User data endpoints | 

 KPIs | 
 Daily active users, monthly active users, daily new users, and uninstalls by date | 
 KPI endpoints | 

 Sessions | 
 App session time-series data | 
 Sessions endpoint | 

 Custom events | 
 Event names, event lists, and event analytics over time | 
 Custom events endpoints | 

 Custom attributes | 
 Attribute names | 
 Custom attributes endpoint | 

 Purchases | 
 Revenue data by time, product ID lists, and purchase counts | 
 Purchase endpoints | 

## How export data is delivered

API exports return data in JSON format, unlike the CSV files you download from the dashboard. The delivery method depends on whether you have cloud storage connected:

- Without cloud storage: Braze writes the export files to its own S3 bucket and includes a temporary download URL in the API response. This URL expires after four hours, and the export is packaged as a compressed archive (ZIP or GZIP, depending on the output_format parameter) containing JSON files. Each line in the JSON files represents one data object.
 
- With cloud storage connected: Braze writes the export files directly to your configured bucket. The API response doesn’t include a download URL. Files follow your own retention policies and are typically more reliable for large exports.

tip

“Cloud storage” means your own storage bucket (for example, Amazon S3, Microsoft Azure Blob Storage, or Google Cloud Storage). You can connect your bucket in Partner Integrations > Technology Partners so Braze can write export files directly to it.

For more details on export delivery and troubleshooting, refer to Export troubleshooting.

## Export endpoints

The following table lists all export APIs available.

 Category | 
 Method | 
 Endpoint | 

 Campaigns | 
 GET | 
 Campaign Analytics | 

 Campaigns | 
 GET | 
 Campaign Details | 

 Campaigns | 
 GET | 
 Campaigns List | 

 Campaigns | 
 GET | 
 Send Analytics | 

 Canvases | 
 GET | 
 Canvas Data Series Analytics | 

 Canvases | 
 GET | 
 Canvas Analytics Summary | 

 Canvases | 
 GET | 
 Canvas Details | 

 Canvases | 
 GET | 
 Canvas List | 

 Custom events | 
 GET | 
 Custom Events | 

 Custom events | 
 GET | 
 Custom Events List | 

 Custom events | 
 GET | 
 Custom Event Analytics | 

 Custom attributes | 
 GET | 
 Custom Attributes | 

 KPIs | 
 GET | 
 KPIs for Daily New Users by Date | 

 KPIs | 
 GET | 
 KPIs for Daily Active Users by Date | 

 KPIs | 
 GET | 
 KPIs for Monthly Active Users Over Last 30 Days | 

 KPIs | 
 GET | 
 KPIs for Uninstalls by Date | 

 Purchases | 
 GET | 
 Product IDs List | 

 Purchases | 
 GET | 
 Number of Purchases | 

 Purchases | 
 GET | 
 Revenue Data by Time | 

 Segments | 
 GET | 
 Segment List | 

 Segments | 
 GET | 
 Segment Analytics | 

 Segments | 
 GET | 
 Segment Details | 

 Sessions | 
 GET | 
 App Sessions Time-Series Data | 

 User data | 
 POST | 
 User Data by Identifier | 

 User data | 
 POST | 
 User Data by Segment | 

 User data | 
 POST | 
 User Data by Global Control Group | 

## Related articles

For one-off exports from the dashboard, refer to these articles:

- Export campaign data
 
- Export Canvas data
 
- Export segment data to CSV

- 

New Stuff!
