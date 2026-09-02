---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/dynamics_365_customer_insights
slug: docs__partners__data_and_analytics__customer_data_platform__dynamics_365_customer_insights
title: "Dynamics 365 Customer Insights"
description: "This reference article outlines the partnership between Braze and Dynamics 365 Customer Insights, a leading enterprise customer data platform, that allows you export customer segments..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Dynamics 365 Customer Insights

Dynamics 365 Customer Insights is a leading enterprise customer data platform that delivers personalized customer experiences with a 360-degree view of your customers.

This integration is maintained by Dynamics 365 Customer Insights.

## About the integration

The Braze and Dynamics 365 Customer Insights integration allows you to export customer segments to Braze to use in campaigns or Canvases.

## Prerequisites

 Requirement | 
 Description | 

 Dynamics 365 Customer Insights account | 
 A Dynamics 365 Customer Insights account is required to take advantage of this partnership. You will need access as an administrator to view and edit connections within your Dynamics 365 Customer Insights account to access the necessary plugins. | 

 Braze REST API key | 
 A Braze REST API key is required with users.track and users.export.segment permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Matching profile identifiers | 
 Unified customer profiles in the exported segments contain a field representing an email address and a Braze external_id. | 

## Integration

### Step 1: Set up Braze connection

In Customer Insights, navigate to Admin > Connections. Next, select Add connections and choose Braze to configure the connection.

- Give your connection a recognizable name in the Display name field.
 
- Choose who can use this connection. If you leave this field blank, the default will be Administrators. For more information, refer to Allow contributors to use a connection for exports.
 
- Provide your Braze API key and REST endpoint in the format rest.iad-03.braze.com.
 
- Select I agree to confirm the data and privacy compliance.
 
- Select Connect to initialize the connection to Braze.
 
- Select Add yourself as export user and provide your Customer Insights credentials.
 
- Select Save to complete the connection.

### Step 2: Create a Braze Segment

- In Braze, go to Audience > Segments.
 
- Create a segment of the users you want Microsoft to update through Dynamics 365 Customer Insights.
 
- Capture the segment’s API Identifier

### Step 3: Configure an export

You can configure this export if you have access to a connection of this type. For more information, refer to Exports overview.

- In Customer Insights, go to Data > Exports. To create a new export, select Add destination.
 
- In the Connection for export field, select a connection for the Braze section. If you don’t see this section name, there are no connections of this type available to you.
 
- Provide the segment API identifier of the segment in Braze.
 
- In the Data matching section, in the Email field, select the field that represents a customer’s email address. Next, in the Braze Customer ID field, select the field that represents the customer’s Braze ID. You can also select an additional, optional field for matching data.
 a. If you map the external_id in Braze to the Braze customer ID field in Customer Insights, the existing records will be updated in Braze when exporting.
 b. If you map a different ID field that doesn’t represent the external_id of a record in Braze, or an empty field, new records will be created in Braze when exporting.
 
- Finally, select the segments you want to export and select Save.

Note that saving an export does not run the export immediately. This export will run with every scheduled refresh. You can also export data on demand.

### Using this integration

After your segments are successfully exported to Braze, you can find them as custom attributes on user profiles. The custom attribute will be named with the Braze segment API identifier that was entered while configuring the export connection. For example, "Segment_API_Identifier": "0000-0000-0000"

To create a segment of these users in Braze, navigate to Segments, create a new segment, and select Custom Attributes as your filter. From here, you can choose the Dynamics 365 synced custom attribute. After the segment is created, you can select it as an audience filter when creating a campaign or Canvas.

note

For more information on this integration, visit Microsoft’s Braze integration article.

- 

New Stuff!
