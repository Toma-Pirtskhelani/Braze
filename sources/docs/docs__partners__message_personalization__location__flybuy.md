---
url: https://www.braze.com/docs/partners/message_personalization/location/flybuy
slug: docs__partners__message_personalization__location__flybuy
title: "Flybuy"
description: "This reference article outlines the partnership between Braze and Flybuy, a location services platform, to add location intelligence to your operations and marketing capabilities."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Flybuy

Flybuy by Radius Networks is the leading omnichannel location platform leveraging AI-powered technology to optimize speed of service across pickup, delivery, drive-thru, and dine-in. Through its integrated Marketing Suite, Flybuy also enables brands to deliver hyper-targeted, moment-based messages, helping to drive engagement, increase check size, and support broader loyalty initiatives.

This integration is maintained by Flybuy.

## About the integration

Flybuy delivers rich user-intelligence events into Braze, empowering brands to send hyper-relevant, location-aware messages with the highest level of personalization. When a user generates an event in Flybuy, custom events with rich user attributes are delivered to Braze. These events and attributes can be used to power omnichannel operations and trigger proximity-based messages.

## Prerequisites

The following is required before you enable the integration:

 Requirement | 
 Description | 

 Flybuy account | 
 A Flybuy account with at least one project. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. | 

## Integration

To enable the integration, complete the following steps:

- In the Flybuy Merchant portal, navigate to the Project Info and click Events Engine.
 
- Click Add a Destination and then select Braze.
 
- Add your Braze API Key and Endpoint, and select the events you want enabled.
 
- Click Finish Setup.

important

Flybuy maps loyalty_id to the Braze external_id for logged-in users.

## Use cases

- Pickup
 
- Delivery
 
- Drive-Thru
 
- Table Service
 
- Hotel Mobile Check-In and Ordering
 
- Marketing Suite

## Event- and attribute-based trigger examples

Custom events and custom attributes can be used to power a variety of personalized experiences.

### Build an audience segment of customers who had a bad pickup experience

For example, target any customer who rated their pickup experience less than 5 stars.

### Trigger an alert when a customer enters a virtual pickup area

Send a personalized SMS targeting customers without a loyalty account to download the app and create a loyalty account.

### Build an audience segment of customers who had a long wait time

For example, target any customer who had a wait time of over two minutes upon exiting a virtual store premise.

### Trigger a course correction alert when a customer is headed to the wrong location

Send a push notification to customers when they are headed or have arrived at a location different from where they placed their order.

### Deliver special offers based on trip milestones

For example, send a special offer when a VIP customer arrives at their favorite locations.

### Build an audience segment of customers who were missing items in their order

For example, target any customer who commented that items were missing in their digital order.

For more details on APIs and SDKs, see the Flybuy Developer Documentation.

- 

New Stuff!
