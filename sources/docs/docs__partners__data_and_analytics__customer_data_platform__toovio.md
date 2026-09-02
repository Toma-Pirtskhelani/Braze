---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/toovio
slug: docs__partners__data_and_analytics__customer_data_platform__toovio
title: "Toovio"
description: "This reference article outlines the partnership between Braze and Toovio, a data-as-a-service company, that helps you discover your actionable data and use the most important..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Toovio

Toovio is a data-as-a-service company powered by artificial intelligence that helps you discover your actionable data and use the most critical elements to drive incremental results based on pre-defined objectives.

This integration is maintained by Toovio.

## About the integration

The Braze and Toovio partnership provides near real-time message triggering, the tools to drive incremental performance, and access to Toovio’s advanced campaign measurement tools.

## Prerequisites

 Requirement | 
 Description | 

 Toovio account | 
 A Toovio account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze Currents | 
 Braze Currents allows Braze clients to stream event or behavior data to a Braze data partner (AWS S3, Google Cloud Storage, or Microsoft Azure Blob Storage) for processing external to the Braze platform. | 

## Integration

The following integration allows Toovio to generate triggers targeting specific customers and communicate near real-time. Triggers determined by Toovio will transmit to Braze via the Braze /users/track endpoint.

### Step 1: Define data partner

A drop location for the Currents feed must be shared with Toovio; this allows Toovio to gain access and process user event and behavior data.

### Step 2: Set up a triggered campaign

Create a Braze API triggered campaign based on the customer events that Toovio will target. Additionally, target user attributes and values that will trigger the campaign should be defined.

### Step 3: Set up your Toovio account

Contact Toovio at [email protected] with the subject “New Customer Request” to set up an account. Toovio will work with clients to set up triggers and underlying models.

- 

New Stuff!
