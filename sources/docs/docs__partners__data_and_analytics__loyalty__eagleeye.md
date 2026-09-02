---
url: https://www.braze.com/docs/partners/data_and_analytics/loyalty/eagleeye
slug: docs__partners__data_and_analytics__loyalty__eagleeye
title: "Eagle Eye"
description: "Learn how to integrate Eagle Eye with Braze."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Eagle Eye

Eagle Eye is a leading SaaS and AI technology company enabling retail, travel and hospitality brands to earn the loyalty of their end customers by powering their real-time, omnichannel and personalized consumer marketing activities, at scale.

This integration is maintained by Eagle Eye.

## Overview

The Eagle Eye Connect is a bi-directional integration between Braze and AIR that enables brands to activate loyalty and promotional data directly in Braze. Clients can issue rewards in AIR to consumers entering an audience in AIR. This allows marketers to personalize customer engagement using real-time data such as point balances, promotions, and reward activities.

## Use Cases

- Trigger Braze campaigns based on loyalty events like point thresholds or rewards earned.
 
- Enrich Braze user profiles with real-time loyalty data to enable more personalized targeting.
 
- Track and report on campaign effectiveness tied to reward redemptions.
 
- Issue rewards in AIR when users enter campaigns in Braze.

## Prerequisites

 Requirement | 
 Description | 

 Eagle Eye AIR account | 
 You need an active Eagle Eye AIR account to take advantage of this partnership. To get started, contact Eagle Eye’s Partnerships team at [email protected]. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. | 

## Outbound vs. inbound

The following tables outline the two types of integrations supported between Braze and Eagle Eye AIR. Eagle Eye Connect is the middleware that enables data exchange between AIR and partner systems like Braze. To learn more, refer to Eagle Eye’s Braze documentation.

- outbound
 
- inbound

 Outbound vs. inbound

 Direction | 
 Initiated By | 
 Data Flow | 
 Purpose | 
 Example | 

 Eagle Eye → Braze | 
 Eagle Eye | 
 To Braze API | 
 
 Send loyalty data into Braze user profiles as custom attributes via custom events. Within Braze, the ingested data can be used to:

- segment users, trigger campaigns
 
- personalize messages
 
 | 

- Sending loyalty points or tier status into Braze (ee_loyalty.points.current, ee_loyalty.tier.tierId)
 
- Updating a user's profile when they receive or redeem a coupon.
 
 | 

 Outbound vs. inbound

 Direction | 
 Initiated By | 
 Data Flow | 
 Purpose | 
 Example | 

 Braze → Eagle Eye | 
 Braze | 
 To Eagle Eye API via webhook | 
 
 When a consumer enters an audience in Braze from any source, Braze can trigger a Braze webhook to EE Connect, allowing EE to issue a reward (coupon or points)

 Upon completion of the action in AIR, Braze would receive an outbound event from AIR.
 | 

- Rewards (Coupon or points) are issued to a consumer for joining the loyalty program
 
- Rewards are issued to a consumer that had a late delivery
 
- Birthday Rewards
 
 | 

tip

To learn more about the custom data that can you can send to Braze as custom attributes or events, refer to Eagle Eye’s Braze documentation.

## Integration Overview

Currently, inbound and outbound connectors can only be set up via API with direct support from the Eagle Eye team—however, a self-serve option within the AIR dashboard is on the way!

When working with your Eagle Eye team, you’ll complete the following:

### Step 1: Provide configuration details

First, you’ll provide the following details to your Eagle Eye team:

 You Provide | 
 Description | 

 Braze API credentials | 
 Share your Braze REST endpoint, App Identifier, and API Key securely with your Eagle Eye contact. | 

 Identifier matching | 
 Determine and share the primary user identifier for profile updates that is common in AIR and Braze, such as External ID or Email. | 

 Auth key | 
 Determine and share a secret auth key for each inbound and outbound connector. | 

 Currency code | 
 Share the 3-digit currency code for displaying monetary purchase amounts (e.g., USD). | 

### Step 2: Configure Eagle Eye Connect

Your Eagle Eye team will configure Eagle Eye Connect using your provided details along with unique AIR API credentials and outbound events for the connectors.

### Step 3: Configure Social Behavioral Actions in AIR

Next, you’ll set up one or more Social Behavioral Actions in AIR with unique action references to issue points or coupons.

### Step 4: Configure Braze

In Braze, you’ll complete the following:

- Set up Campaigns in Braze to issue rewards in AIR
 
- Set up any communications to consumers when AIR events are received

### Step 5: Test your integration

Make API calls in AIR and observe event data flow into your Braze workspace.Validate data received from AIR and confirm attributes are updating as expected.

Also, add users to audiences and confirm rewards are issued in AIR.

### Step 6: Launch to production

After testing is successful, the integration can go live to continuously send data to Braze. The same configuration steps are required for production environments in AIR and Braze

Contact your Eagle Eye Customer Success Manager to have a resource assigned to you, to set up EE Connect.

## Support

For integration support or troubleshooting, please contact the Eagle Eye support team at [email protected].

- 

New Stuff!
