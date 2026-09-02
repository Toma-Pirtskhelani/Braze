---
url: https://www.braze.com/docs/partners/message_personalization/location/loplat
slug: docs__partners__message_personalization__location__loplat
title: "loplat"
description: "This reference article outlines the partnership between Braze and loplat, an offline location-based marketing platform, to allow you to execute proximity marketing campaigns by adding..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# loplat

Loplat is the leading offline location-based platform. Use loplat SDK to increase your store’s footfall smartly and execute marketing campaigns that encourage in-store purchases. You can measure the store performance through footfall analysis after the campaign ends.

This integration is maintained by Loplat.

## About the integration

The Braze and loplat integration allows you to use loplat’s location services (store POI and custom geofence) to trigger geo-contextual marketing campaigns and create custom events using offline segmentation. When users visit the targeted location you set in loplat X, the campaign and location information are sent immediately to Braze.

## Prerequisites

 Requirement | 
 Description | 

 loplat X account | 
 A loplat X account is required to take advantage of this integration.

Email [email protected] to request a loplat X account. | 

 loplat SDK | 
 loplat SDK recognizes users’ store visits, processes location events, and distinguishes whether users are staying at a place or moving. You can use loplat SDK to analyze your store’s footfall, send push messages when users enter your store, etc.

Note that the SDK is only available for Android and iOS. | 

 Braze REST API key | 
 A Braze REST API key with the following permissions:
- users.track
- campaigns.trigger.send
- campaigns.list
- canvas.trigger.send
- canvas.list

This can be created in the Braze dashboard from Settings > API Keys. | 

## Use cases

The custom event location information provided by loplat can be used in your campaigns to achieve use cases like:

- Duty-free promotion alert

- Send duty-free shop discount coupons to the users who are near the boarding gates at the airport.

- Electric vehicle (EV) charging station location push

- Set geofences around EV charging stations and notify users when they are nearby the station and encourage them to charge.

## Integration

### Step 1: Integrate the SDKs

Integrate the loplat SDK and the Braze SDK in your app using the steps provided in the loplat-Braze integration documentation.

### Step 2: Sync the Braze and loplat X dashboards and create a campaign

Create a new API key in the Braze dashboard. Copy the API key and paste it at Settings > API Settings in the loplat X dashboard. See the loplat X user’s guide for more details.

#### API-triggered delivery

- Create a Braze campaign or Canvas that sends with API-Triggered Delivery, and copy the campaign ID.
 
- Launch the campaign in Braze after completing all steps.
 
- Go to loplat X and create a campaign following the instructions in the loplat X user’s guide.
 
- Paste the Braze campaign ID under the Campaign Message Settings, and launch the campaign.

#### Action-based delivery

With the integration, you can apply location conditions by sending geofence information, region, brand name, or store name. In addition, you can add segments or assign conversion with the custom event you created.

- Create a loplat X campaign following the instructions in the loplat X user’s guide.
 
- Add a custom event under the Campaign Message Settings and launch the campaign.
 
- Go to the Braze dashboard and create a campaign or Canvas that sends with Action-Based Delivery.
 
- Select the custom event you created in loplat X to set a location trigger action.

- 

New Stuff!
