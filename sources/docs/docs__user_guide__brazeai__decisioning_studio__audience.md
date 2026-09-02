---
url: https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/audience
slug: docs__user_guide__brazeai__decisioning_studio__audience
title: "Define your audience"
description: "Learn how to define and configure the audience for your BrazeAI Decisioning Studio agent, including treatment groups and platform-specific setup steps."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Define your audience

Use case audiences are typically defined in a Customer Engagement Platform (such as Braze or Salesforce Marketing Cloud), then sent to the Decisioning Studio agent. The agent then divides customers into treatment groups in order to conduct randomized controlled trials.

## Treatment groups

 Group | 
 Description | 

 Decisioning Studio | 
 Customers who receive AI-optimized recommendations | 

 Random Control | 
 Customers who receive randomly selected options (baseline comparison) | 

 Business-as-Usual (optional) | 
 Customers who receive the current marketing journey (for comparing against existing performance) | 

 Holdout (optional) | 
 Customers who receive no communications (to measure overall campaign impact) | 

## Configure your audience

- braze
 
- salesforce marketing cloud
 
- other platforms

- Create a segment for the audience you want to target.
 
- Provide the Segment ID to your AI Decisioning Services team.

note

For Braze, we can ingest multiple segments and combine them to create the audience. Decisioning Studio can ingest a segment for a Business-as-Usual comparator campaign. All of these patterns are acceptable.

- Configure an SFMC Data Extension for your audience and provide the data extension ID
 
- Set up SFMC Installed Package for API integration with the appropriate permissions required by Decisioning Studio
 
- Confirm this data extension is refreshed daily, as Decisioning Studio pulls from the latest incremental data available

Provide the extension ID and API key to our AI Decisioning Services team, who will assist with next steps in ingesting customer data.

### Google Cloud Storage

If the audience is not currently stored in Braze or Salesforce Marketing Cloud, then the next best step is to configure an automated export directly to a Braze-controlled Google Cloud Storage (GCS) bucket.

To determine whether this is feasible, refer to the documentation for your platform. For example, mParticle offers a native integration with Google Cloud Storage. If this is the case, we can provide a GCS bucket to export audience data to.

### Additional resources

- Twilio Segment
 
- Treasure Data
 
- ActionIQ
 
- Adobe Experience Platform

## Next steps

After defining your audience, proceed to set up orchestration:

- Set up orchestration

- 

New Stuff!
