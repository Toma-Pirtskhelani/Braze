---
url: https://www.braze.com/docs/partners/data_and_analytics/workflow_automation/airbyte
slug: docs__partners__data_and_analytics__workflow_automation__airbyte
title: "Airbyte"
description: "This reference article covers the Braze and Airbyte integration. Airbyte is an open-source data integration engine that helps you consolidate your data in your data..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Airbyte

Airbyte is an open-source data integration engine that helps you consolidate your data in your data warehouses, lakes, and databases.

This integration is maintained by Airbyte.

## About the integration

The Braze and Airbyte integration allows users to create a data pipeline to collect and analyze Braze data by connecting all of your applications and databases to a central warehouse. After data has been collected in the central warehouse, data teams can explore Braze data effectively using their preferred business intelligence tools.

## Prerequisites

 Requirement | 
 Description | 

 Airbyte Cloud account | 
 An Airbyte Cloud account is required to take advantage of this integration. | 

 Braze REST API key | 
 A Braze REST API key with all permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your endpoint will depend on the Braze URL for your instance. | 

## Integration

- In your Airbyte Cloud account, navigate to Sources > + New Source > Set up the Source.
 
- Enter “Braze” as the source name and select Braze from the source dropdown.
 
- Provide your endpoint URL, Braze REST API key, and start date. Click Set up Source.

### Supported sync modes

Airbyte’s Braze source connector supports the following sync modes:

- 

 **Full Refresh | 
 Overwrite**: sync all records from the source and replace data in the destination by overwriting it. | 

- 

 **Incremental Sync | 
 Append**: Sync new records from the source and add them to the destination without deleting any data. | 

### Supported streams

- campaigns
 
- campaigns_analytics
 
- canvases
 
- canvases_analytics
 
- events
 
- events_analytics
 
- kpi_daily_new_users
 
- kpi_daily_active_users
 
- kpi_daily_app_uninstalls
 
- cards
 
- cards_analytics
 
- segments
 
- segments_analytics

note

Rate limits differ depending on the stream. Visit the rate limits table for more information.

- 

New Stuff!
