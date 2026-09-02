---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/blueconic
slug: docs__partners__data_and_analytics__customer_data_platform__blueconic
title: "BlueConic"
description: "This reference article outlines the partnership between Braze and BlueConic, a leading pure-play customer data platform, allowing you to unify data across persistent, individual profiles..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# BlueConic

BlueConic, the leading pure-play customer data platform, liberates companies’ first-party data from disparate systems and makes it accessible wherever and whenever it is required to transform customer relationships and drive business growth.

This integration is maintained by Blueconic.

## About the integration

The Braze and BlueConic integration allows users to unify data across persistent, individual profiles and then sync it across the two systems for import goals via an Amazon Web Services S3 server. Potential goals include growth-focused initiatives, customer lifecycle orchestration, modeling and analytics, digital products and experiences, audience-based monetization, and more. This integration supports both scheduled batch import and export.

important

When using the integration, BlueConic will send deltas (changing data) on each sync. This includes any profiles that have changed since the last send and all attributes of that profile. Monitor data point usage accordingly.

## Prerequisites

 Requirement | 
 Description | 

 BlueConic account | 
 A BlueConic account is required to take advantage of this partnership. You will need access to view and edit connections within your BlueConic account to access the plugins. | 

 Braze REST API key | 
 A Braze REST API key with users.track, users.export.segment, campaigns.list, campaigns.details, segments.lists, and segments.details permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

 S3 authentication | 
 You will need access to an Amazon Web Services (S3) server to export and import the data. | 

 Access key ID
Secret access key | 
 The access key ID and secret access key will allow you to authenticate your S3 server for importing and exporting. | 

 AWS bucket | 
 You will need to connect to S3 within the plugin. After authentication, the available buckets will show in a dropdown menu. This is where files to be imported or exported are stored. | 

## Integration

### Step 1: Creating a Braze connection

In BlueConic, select Connections in the navigation bar, and then Add Connection. In the prompt that appears, search Braze and select Braze connection.

Expand or collapse available metadata fields in the connection by clicking the gray chevron icon. Within these fields, you can favorite this connection, name your connection, add labels, include a description, and choose to get email notifications if the connection runs or fails to run.

Save your settings.

### Step 2: Configuring a Braze connection

To configure the connection between BlueConic and Braze, you must add your Braze account credentials and Amazon Web Services (S3) account information to authenticate the connection.

- In BlueConic, select Set up and run in the Setup section.

- In the Braze authentication page that opens, enter your Braze REST API endpoint and Braze API key.

- In the S3 setup and authentication section, enter these credentials: Amazon Web Services (S3) access key ID, secret access key, and S3 bucket. They need to be the same credentials you configured when setting up your Braze and Amazon S3 integration. Save your settings. 

### Step 3: Creating import or export goals (import mapping)

Once the authentication is complete, you must create at least one import or export goal, turn the connection on, and schedule or run the connection.

- import
 
- export

- Select Import data into BlueConic in the Setup section to open the Braze data configuration page.

- Select the location of the data in Braze. Here, you can tell BlueConic where to find the data to be imported by selecting your Braze audience.

- Next, map identifiers between Braze and BlueConic. 

 To link the customer data between the two systems, enter one or more customer identifiers.
Use the Allow creation… checkbox to allow BlueConic to create new profiles for data that does not match an existing BlueConic profile.

- Next, match the BlueConic data fields you are exporting to Braze fields. Use the first dropdown to select either the BlueConic profile identifier or a profile property, then select the corresponding Braze profile identifier in the matching dropdown. Next, use the dropdown menu to specify how imported content should be added to existing values: added, summed, set only if the profile property is empty, or set to clear (if the Braze field is empty).

Use the Add Mapping button to create additional mapping rows as needed. You can add multiple mapping rows with the Add remaining fields option. BlueConic detects the remaining Braze fields and matches them with BlueConic profile properties. You can set the merge strategy for imports (set, add, sum, set if empty or clear) and provide a custom prefix to the names of BlueConic profile properties.

- Lastly, select Run the connection to start the connection. Visit BlueConic to learn more about scheduling and running connections.

- Select Export data to Braze in the Setup section to configure your data export from BlueConic to Braze.

- Choose a BlueConic segment for the export. Only profiles in this segment with matching identifiers in Braze will be exported.

- Next, link identifiers between BlueConic profiles and Braze fields. You can optionally choose to let BlueConic create new records if no existing match is found.

- Next, match the BlueConic data fields you are exporting to Braze fields. Use the dropdown menu from the BlueConic icon to choose the type of information you want to export. Available information includes profile properties, BlueConic profile identifiers, associated segments, all viewed interactions, permission levels, and a static text value.

- Lastly, select Run the connection to start the connection. Visit BlueConic to learn more about scheduling and running connections.

## Step 4: Toggle connection on

Use the toggle next to the Braze connection title to toggle the connection on and off. A connection must be on to run during scheduled times.

- 

New Stuff!
