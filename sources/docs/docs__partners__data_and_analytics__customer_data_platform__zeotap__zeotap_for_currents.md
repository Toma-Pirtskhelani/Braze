---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/zeotap/zeotap_for_currents
slug: docs__partners__data_and_analytics__customer_data_platform__zeotap__zeotap_for_currents
title: "Zeotap for Currents"
description: "This reference article outlines the partnership between Braze Currents and Zeotap, a next-generation customer data platform that helps you discover and understand your mobile audience..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Zeotap for Currents

Zeotap is a next-generation customer data platform that helps you discover and understand your mobile audience by providing identity resolution, insights, and data enrichment.

The Braze and Zeotap integration empowers you to extend the scale and reach of your campaigns by syncing Zeotap customer segments to Braze user profiles. With Currents, you can also connect data to Zeotap to make it actionable across the entire growth stack.

## Prerequisites

 Requirement | 
 Description | 

 Zeotap account | 
 A Zeotap account is required to take advantage of this partnership. | 

 Currents | 
 To export data back into Zeotap, you need to have Braze Currents set up for your account. | 

## Implementation

### Step 1: Create a Currents source

- In Zeotap, go to Sources under Integrate.
 
- Select Create Source.
 
- Select Customer Engagement Channels as the category.

- Select Braze as the data source.
 
- Enter a source name.
 
- Select your region.

- Select Create Source.
 
- Go to the Implementation Details tab and take note of the API URL and Write Key.

### Step 2: Configure data streaming in Currents

- In Braze, go to Partner Integrations > Data Export.
 
- Select Create New Current and Custom Currents Export.

- Enter an integration name and email to be contacted if errors occur with the integration.
 
- Under Credentials, enter the following information you noted from Step 1:

- The API URL as the Endpoint
 
- The Write Key as the Bearer Token

- Select the message engagement events that you want to send to Zeotap.

- Select Launch Current to save the changes and start sending events to Zeotap.

important

The Currents connector doesn’t support anonymous users (users without an external_id).

- 

New Stuff!
