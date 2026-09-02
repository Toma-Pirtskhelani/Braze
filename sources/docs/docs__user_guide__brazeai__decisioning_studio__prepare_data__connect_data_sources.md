---
url: https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources
slug: docs__user_guide__brazeai__decisioning_studio__prepare_data__connect_data_sources
title: "Connect your data"
description: "Learn how to connect customer data sources to BrazeAI Decisioning Studio for personalized AI decisioning."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Connect your data

BrazeAI Decisioning Studio™ agents need to fully understand customer context in order to make effective decisions. This article explains how to connect customer data sources to Decisioning Studio.

tip

Your AI Decisioning Services team will support you in configuring data connections for optimal performance.

## Supported integration patterns

Decisioning Studio supports multiple integration patterns for connecting customer data:

 Integration pattern | 
 Best for | 
 Setup complexity | 

 Braze Data Platform | 
 Customers already using Braze | 
 Low | 

 Braze Cloud Data Ingestion (CDI) | 
 Connecting external data warehouses | 
 Medium | 

 Cloud Storage (GCS, AWS, Azure) | 
 Direct data exports from other platforms | 
 Medium | 

 CEP integrations | 
 SFMC, Klaviyo data extensions | 
 Medium | 

## Customer data types

The following customer data assets help agents personalize more effectively:

 Data type | 
 Description | 
 Examples | 

 Customer profile | 
 Static and slowly-changing attributes | 
 Years as customer, geography, acquisition channel, satisfaction level, lifetime value estimate | 

 Customer behavior | 
 Activity and engagement patterns | 
 Account logins, device type, customer service interactions, product usage | 

 Transaction history | 
 Purchase and conversion data | 
 Products purchased, transaction amounts, payment methods, purchase channels | 

 Marketing engagement | 
 Responses to communications | 
 Email opens/clicks, SMS engagement, web and mobile activity, survey responses | 

tip

The more information agents have about your customers, the better they will perform. Consider including data on any insights that would be particularly important to your business (for example, do you want to see how AI treats your loyalty customers differently? Make sure loyalty status is in the customer data).

## Connect data by platform

- braze
 
- sfmc
 
- klaviyo
 
- cloud storage

### Send customer data through Braze

BrazeAI Decisioning Studio can use all data that you are already sending to the Braze Data Platform.

For customer data that isn’t on the user profile or custom attributes, you have two ways to bring it in with Braze Cloud Data Ingestion:

- Ingest into the Braze Data Platform. Sync warehouse data into Braze user profiles, custom attributes, or events. Choose this when you also want the data available in Braze for segmentation and messaging. Supports Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric, AWS S3, and Google Cloud Storage.
 
- Send directly to Decisioning Studio (Early Access). Sync warehouse data straight to Decisioning Studio, without adding them to the Braze user profile or custom attributes. Choose this for data you want Decisioning Studio to use but don’t need elsewhere in Braze. This option is in early access, see Cloud Data Ingestion: Sync Decisioning Studio data to set it up.

Once you are satisfied with the data you are sending into the Braze Data Platform, contact your AI Decisioning Services team to discuss which fields on the user profile or custom attributes should be used for AI Decisioning.

To streamline this process, create a list of Braze user profile attributes that you think best represent your customers’ behaviors that should be used in Decisioning Studio (see the list of available fields). Your services team can also help you conduct discovery sessions to decide which fields are most appropriate for AI Decisioning.

Other options for sending data include:

- Sending Braze custom events via the SDK
 
- Sending events using the REST endpoint (/users/track)

These patterns require more engineering effort, but are sometimes preferable depending on your current Braze configuration. Reach out to the AI Decisioning Services team to learn more.

### Send customer data through SFMC

For Salesforce Marketing Cloud integrations:

- Configure SFMC Data Extension(s) for your customer data
 
- Set up SFMC Installed Package for API integration with the appropriate permissions required by Decisioning Studio
 
- Ensure that data extensions are refreshed daily, as Decisioning Studio will pull from the latest incremental data available

Provide the extension ID and API key to your AI Decisioning Services team. They will assist with next steps in ingesting customer data.

### Send customer data through Klaviyo

For Klaviyo integrations:

- Confirm customer profile data is available in Klaviyo profiles
 
- Generate a private API key with Full Access to Profiles
 
- Provide the API key to your AI Decisioning Services team

See the Klaviyo documentation for more information on API key setup.

### Other cloud solutions (Google Cloud Storage, Azure, AWS)

If customer data is not currently stored in Braze, SFMC, or Klaviyo, the next best step is to configure an automated export directly to a Braze-controlled Google Cloud Storage bucket. We can also support export to AWS or Azure (although GCS is preferable). For these platforms, export to their internal cloud storage in those cloud platforms and Braze can then pull that data.

To determine whether this is feasible, refer to the documentation for your Martech platform. For example:

- mParticle offers a native integration with Google Cloud Storage
 
- Twilio Segment
 
- Treasure Data
 
- ActionIQ
 
- Adobe Experience Platform

If this is feasible, we can provide a GCS bucket to export customer data to that is isolated to Decisioning Studio.

## Best practices

- Descriptive column names: Customer data should have clear, descriptive column names. Ideally, a data dictionary should be provided.
 
- Incremental updates: Incremental files are preferable versus snapshots of the whole customer history every day
 
- Consistent identifiers: Each record must contain a unique customer identifier that is consistent across all data assets
 
- Include timestamps: Records should have associated timestamps for accurate attribution and agent training

## Custom integrations

Other options or completely custom data pipelines are possible. These may require additional Services work or Engineering work from your team. To determine what is feasible and optimal, work with your AI Decisioning Services team.

important

This guide explains the most common integration patterns. Information Security will still need to vet all connection points and Solutions Consultants will be available to advise on the implementation.

## Next steps

After connecting your data sources, proceed to set up orchestration:

- Set up orchestration

- 

New Stuff!
