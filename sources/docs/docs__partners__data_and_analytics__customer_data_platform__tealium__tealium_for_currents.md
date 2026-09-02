---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents
slug: docs__partners__data_and_analytics__customer_data_platform__tealium__tealium_for_currents
title: "Tealium for Currents"
description: "This reference article outlines the partnership between Braze Currents and Tealium, a customer data platform that collects and routes information between sources in your marketing..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Tealium for Currents

Tealium is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and Tealium integration allows you to seamlessly control the flow of information between the two systems. With Currents, you can also connect data to Tealium to make it actionable across the entire growth stack.

## Prerequisites

 Requirement | 
 Description | 

 Tealium EventStream or Tealium AudienceStream | 
 A Tealium account is required to take advantage of this partnership. | 

 Currents | 
 In order to export data back into Tealium, you need to have Braze Currents set up for your account. | 

 Tealium URL | 
 These can be obtained by navigating to your Tealium dashboard and copying the ingestion URL. | 

## Integration

### Step 1: Create a data source for Braze within Tealium

Instructions for creating a data source can be found on the Tealium site. When completed, Tealium will provide a data source URL to copy, which you will use in the next step.

### Step 2: Create Current

In Braze, navigate to Currents > + Create Current > Tealium Export. Provide an integration name, contact email, and your Tealium URL.

Next, select what you want to track from the list of available events. By default, all events sent to Tealium include the user’s external_user_id. However, you can select the Include events from anonymous users checkbox to also send events that do not have an external_user_id to Tealium.

After setting up your integration, select Launch Current.

important

It’s important to keep your Tealium URL up to date. If your connector’s URL is incorrect, Braze will be unable to send events. If this persists for more than 5 days, the connector’s events will be dropped, and data will be permanently lost.

## Integration details

Braze supports exporting all data listed in the Currents event glossaries (including all properties in both message engagement and customer behavior events) to Tealium.

The payload structure for exported data is the same as the payload structure for custom HTTP connectors, which can be viewed in the examples repository for custom HTTP connectors.

- 

New Stuff!
