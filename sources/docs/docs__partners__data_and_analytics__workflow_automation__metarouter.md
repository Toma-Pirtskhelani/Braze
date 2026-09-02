---
url: https://www.braze.com/docs/partners/data_and_analytics/workflow_automation/metarouter
slug: docs__partners__data_and_analytics__workflow_automation__metarouter
title: "MetaRouter"
description: "Elevate your customer data management in Braze, with MetaRouter. This high-performance, server-side tag management solution offers maximum compliance and control with seamless deployment options, whether..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# MetaRouter

MetaRouter elevates your Braze experience by seamlessly integrating as a powerful server-side tag management platform. It empowers you to orchestrate a complete customer data journey within Braze, from reliable fully first-party data collection enriched by up to 30%, to real-time event stream activation for personalized journeys. Additionally, MetaRouter streamlines implementation by eliminating the need for Braze tags or other third-party tags, granting you granular, parameter-by-parameter control over the data flowing into Braze.

This integration is maintained by Metarouter.

## Supported features

- Retries can be built in.
 
- Requests are batched.
 
- Rate limiting issues are handled with a retry.
 
- External ID and PII are supported. MetaRouter passes their anonymous ID and any PII (email, phone number, name) that clients want.
 
- You can send Braze purchases and custom events data.

- Event properties are supported.
 
- Nested event properties are not supported.

## Prerequisites

Before you start, you’ll need the following:

 Requirement | 
 Description | 

 A MetaRouter account | 
 A MetaRouter Enterprise account. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. To create one go to Settings > API Keys. | 

 A Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

## Setting up MetaRouter

To set up MetaRouter for your Braze integration:

- Go to MetaRouter and create a new cluster.
 
- Choose which events you’d like to track.
 
- Install a MetaRouter SDK and integrate events into your website.
 
- Connect your cluster to your website’s UI.
 
- Create a new pipeline.
 
- Verify your website is sending events to MetaRouter.

## Integrating Braze

### Step 1: Add the Braze integration

In Enterprise MetaRouter, select Integrations > New Integration > Braze, then name your integration. Next enter your instance URL and API key, then select Apply Changes.

### Step 2: Add event mapping

Add event mapping for each identity output, then configure the events you want to send to Braze. When you’re finished, select Save as New Revision.

- 

New Stuff!
