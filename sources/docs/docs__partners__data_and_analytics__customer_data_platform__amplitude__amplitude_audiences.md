---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences
slug: docs__partners__data_and_analytics__customer_data_platform__amplitude__amplitude_audiences
title: "Amplitude"
description: "This reference article outlines the partnership between Braze and Amplitude, a product analytics and business intelligence platform."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Amplitude

Amplitude is a product analytics and business intelligence platform.

The Braze and Amplitude bi-directional integration allows you to import your Amplitude Cohorts, user traits, and events into Braze, as well as create segments that can target users in future campaigns or Canvases. You can also leverage Braze Currents to export your Braze events to Amplitude to perform deeper analytics of your product and marketing data.

## Prerequisites

 Requirement | 
 Description | 

 Amplitude account | 
 An Amplitude account is required to take advantage of this partnership. | 

 Currents | 
 In order to export data back into Amplitude, you need to have Braze Currents set up for your account. | 

## Choose an integration

Amplitude and Braze offer two different integration methods. Read through the following documentation to decide which methods will fit your needs:

- Braze Event Streaming: An integration that allows you to forward raw Amplitude event data straight to Braze.
 
- Cohort import: An integration that allows you to forward Amplitude cohorts to Braze.

## Braze Event Streaming

### Prerequisites

 Requirement | 
 Description | 

 Braze REST API key | 
 A Braze REST API key with the all permissions.

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. | 

 Braze app identifier | 
 The identifier for the app that will receive Amplitude events. This can be found within the Braze Dashboard > Developer Console > Settings. | 

### Amplitude Setup

- In Amplitude, navigate to Data Destinations then look up “Braze - Event Stream”.
 
- Enter a sync name and then click Create Sync.
 
- Click Edit and provide your Braze REST API endpoint, REST API key, and Braze app identifier.
 
- Use the send events filter to select the events to send. You can send all events, but Amplitude recommends choosing the most important ones.
 
- When finished, enable the destination and save.

Refer to Braze Event Streaming for more information on this integration.

## Sync user traits and computations

Use Audiences to send user properties and computations to Braze as custom attributes. You will be able to sync user properties or computed properties for users who have been active in the last 90 days.

When a user’s property or a computation updates, Amplitude will update a custom attribute in Braze with the same name as that user property or computation.

User trait and computation syncs will create new users for user identifiers that do not yet exist within Braze. Computations and user traits can only be synced using user identifiers. A user identifier can be any of the following:

- External ID
 
- Braze ID
 
- User alias
 
- Email address

Refer to Amplitude’s documentation to learn more about syncing properties, recommendations, and cohorts to third-party destinations.

### How to sync user properties and computations

In Amplitude Audiences, select Syncs > Create Sync.

Next, choose to sync a user property, computation, cohort, or recommendation.

- syncing user property
 
- syncing computation

Select User Property and then the desired user property to sync.

Next, select a destination to sync your user property to.

Lastly, define the frequency of your sync.

Select Computation and then the desired computation to sync

Next, select a destination to sync your computation to.

Lastly, define the frequency of your sync.

## Troubleshooting

### “We do not have enough data yet for this filter” when syncing a cohort

If you get this error when importing an Amplitude cohort into Braze, try the following:

- Confirm user ID alignment. The User ID in Amplitude (not the Amplitude ID) must match the External User ID in Braze (not the Braze or BSON ID) exactly. For example, User ID 12345 in Amplitude must match External User ID 12345 in Braze.
 
- Regenerate your Braze API key. In the Braze dashboard, go to Partner Integrations > Technology Partners > Amplitude and select Generate New Key. Then retry the Amplitude cohort sync using the new API key.
 
- Confirm the cohort synced in Amplitude. Contact Amplitude support to confirm that the cohort was successfully synced on Amplitude’s side before troubleshooting further in Braze.

## Amplitude user profile API endpoints

To check out some of the common Amplitude API endpoints that can be used with Connected Content, view our dedicated Amplitude API documentation.

- 

New Stuff!
