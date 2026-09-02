---
url: https://www.braze.com/docs/partners/data_and_analytics/business_intelligence/clarisights
slug: docs__partners__data_and_analytics__business_intelligence__clarisights
title: "Clarisights"
description: "This reference article outlines the partnership between Braze and Clarisights, a self-serve performance marketing reporting platform, allowing you to import data from Braze campaigns and..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Clarisights

Clarisights is a self-serve performance marketing reporting platform for data-driven organizations. It automatically integrates, processes, and visualizes all your data from marketing, analytical and attribution sources.

This integration is maintained by Clarisights.

## About the integration

The Braze and Clarisights integration allows you to import data from Braze campaigns and Canvases to help achieve a unified reporting interface of performance and CRM/retention marketing.

## Prerequisites

 Requirement | 
 Description | 

 Clarisights account | 
 A Clarisights workspace is required to take advantage of this partnership | 

 Braze REST API key | 
 A Braze REST API key with the following permissions: 
 - campaigns.list 
 - campaigns.details
 - campaigns.data_series 
 - canvas.details
 - canvas.list 
 - canvas.data_series 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

 Braze workspace name | 
 The name of the workspace associated with the Braze API key. This name will be used to identify the workspace integration on Clarisights. | 

## Use cases

With the Braze and Clarisights integration, users can create different visualizations and tables to gain insights from the campaigns they have created. Popular use cases include:

- better visibility
 
- granular reporting
 
- unified dashboards

Better visibility on overall campaigns and Canvases performance.

Granular reporting for campaigns and Canvases.

Unified dashboards for CMOs and CXOs.

## Integration

To sync Braze data to Clarisights, you must build a Braze connector and connect Braze workspaces.

- In Clarisights, navigate to the Integrations page, locate the Braze connector, and select + Connect.

- Next, using the integration flow, connect your Clarisights account to Braze. This can be done by providing your Braze REST API key, Braze workspace name, and Braze REST endpoint.

Before successful integration, users will see the connected workspaces on the same page.

## Using this integration

To include Braze as a data source in your Clarisights reports, navigate to Create New Report. Name your report and select Braze as a data source in the prompt that appears. You can also choose the metrics and dimensions to include in the report. When completed, select Create Report.

The data from Braze will start flowing from the time of the next scheduled data import. Contact your Clarisights customer success manager to request backfills for longer durations.

Visit Clarisights for more information on available metrics and dimensions or report creation.

- 

New Stuff!
