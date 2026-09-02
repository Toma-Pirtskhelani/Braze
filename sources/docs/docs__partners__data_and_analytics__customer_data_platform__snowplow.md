---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/snowplow
slug: docs__partners__data_and_analytics__customer_data_platform__snowplow
title: "Snowplow"
description: "This reference article outlines the partnership between Braze and Snowplow, a data infrastructure platform, that allows you to forward Snowplow events to Braze in real..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Snowplow

Snowplow is a scalable, open-source platform for rich, high-quality, low-latency data collection. Snowplow is designed to collect high-quality, complete behavioral data for enterprise businesses.

This integration is maintained by Snowplow.

## About the integration

The Braze and Snowplow integration enables you to forward Snowplow events to Braze in real time using Snowplow’s Event Forwarding solution. This integration lets you send events to Braze while offering flexibility and control. Specifically, you can:

- Filter and transform events before sending to Braze.
 
- Map Snowplow event data to Braze user attributes, custom events, and purchases.
 
- Retain all data in your private cloud until you choose to forward it.
 
- Deploy the solution yourself within your existing Snowplow cloud account.

Snowplow’s Event Forwarding is a paid add-on feature available to Snowplow customers. To forward events to Braze without this add-on, use Snowplow’s Google Tag Manager Server-Side integration.

Leverage Snowplow’s rich behavioral data to drive powerful customer-centric interactions in Braze and deliver personalized messages in real time.

## Prerequisites

 Requirement | 
 Description | 

 Snowplow pipeline | 
 You need a Snowplow pipeline up and running. | 

 Snowplow Console access | 
 You must have access to Snowplow Console to configure event forwarders. | 

 Braze REST API key | 
 A Braze REST API key with the following permissions: users.track, users.alias.new, users.identify, users.export.ids, users.merge, users.external_ids.rename, and users.alias.update. 

 You can create this in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. | 

## Use cases

### Personalized, action-based delivery

Use any of the large number of rich events that Snowplow collects by default, or define your custom events to shape even more granular customer journeys that make sense for your business. Leverage Snowplow’s rich behavioral data to design customer funnels and unlock value for your marketing and product teams, helping them to maximize conversion and product usage through Braze.

### Dynamic segmentation

Create dynamic audiences in Braze based on Snowplow’s high-quality behavioral data: As users take actions in your product, app, or website, you can leverage the real-time behavioral data that Snowplow collects to automatically add or remove users from relevant segments in Braze.

## Integration

### Step 1: Configure the destination in Snowplow Console

To create the event forwarder:

- In Snowplow Console, navigate to Destinations and select Create new destination.
 
- When configuring the connection, select Braze for the connection type.
 
- Enter your Braze API key and REST API endpoint.
 
- Save the connection.

### Step 2: Configure the event forwarder

When configuring the forwarder, you can choose which Snowplow events to forward and map them to Braze object types:

- User attributes: Update user profile data and custom user properties.
 
- Custom events: Send user actions and behaviors.
 
- Purchases: Send transaction data with product details.

For each object type, you can configure field mappings to specify how Snowplow event data maps to Braze fields. See Snowplow’s Creating forwarders documentation for detailed setup instructions and field mapping configuration.

### Step 3: Validate the integration

Confirm events are reaching Braze by checking the following pages in your Braze account:

- Query Builder: In Braze, navigate to Analytics > Query Builder. You can write queries on the following tables to preview the data forwarded from Snowplow: USER_BEHAVIORS_CUSTOMEVENT_SHARED and USERS_BEHAVIORS_PURCHASE_SHARED.
 
- API Usage Dashboard: In Braze, navigate to Settings > APIs and Identifiers to see a chart of API usage over time. You can filter specifically for the API key Snowplow uses and see both successes and failures.

## Sending custom properties

You can send custom properties beyond the standard fields. The structure depends on which Braze object type you’re using:

- User attributes: Add as top-level fields (for example, subscription_tier, loyalty_points)
 
- Event properties: Nest under properties object (for example, properties.plan_type, properties.feature_flag)
 
- Purchase properties: Nest under properties object (for example, properties.color, properties.size)

For property names containing spaces, use bracket notation (for example, ["account type"] or properties["campaign source"]).

See the Event Object documentation for details on supported data types, property naming requirements, and payload size limits.

## Limitations

Rate limits: Braze enforces a rate limit of 3,000 API calls every three seconds for the Track Users API. Because Snowplow doesn’t support batching for event forwarders, this API rate limit also functions as the event rate limit. If your input throughput exceeds 3,000 events per three seconds, you may experience increased latency.

- 

New Stuff!
