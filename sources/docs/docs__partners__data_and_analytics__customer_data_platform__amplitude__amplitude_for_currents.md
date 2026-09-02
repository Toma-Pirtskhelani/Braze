---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents
slug: docs__partners__data_and_analytics__customer_data_platform__amplitude__amplitude_for_currents
title: "Amplitude for Currents"
description: "This reference article outlines the partnership between Braze Currents and Amplitude, a product analytics and business intelligence platform."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Amplitude for Currents

Amplitude is a product analytics and business intelligence platform.

The Braze and Amplitude bi-directional integration allows you to sync your Amplitude Cohorts, user traits, and events into Braze as well as leverage Braze Currents to export your Braze events to Amplitude to perform deeper analytics of your product and marketing data.

## Prerequisites

 Requirement | 
 Description | 

 Amplitude account | 
 An Amplitude account is required to take advantage of this partnership. | 

 Currents | 
 In order to export data back into Amplitude, you need to have Braze Currents set up for your account. | 

## Data export integration

A full list of the events and event properties that can be exported from Braze to Amplitude can be found in the following sections. All events sent to Amplitude will include the user’s external_user_id as the Amplitude user ID. Braze-specific event properties will be sent under the event_properties key in the data sent to Amplitude.

important

To use this feature, your Amplitude user ID must match the Braze external ID.

Braze will only send event data for users who have their external_user_id set or anonymous users who have their device_id set. For the anonymous users, you will need to sync your Amplitude device ID with the Braze device ID in the SDK. For example:

```

1

```
 | 
```
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)

```
 | 

You can export two types of events to Amplitude: Message Engagement Events consisting of the Braze Events directly related to message sending, and Customer Behavior Events, including other app or website activity such as sessions, custom events, and purchases tracked through the platform. All regular events are prefixed with [Appboy], and all custom events are prefixed with [Appboy] [Custom Event]. Custom event and purchase event properties are prefixed with [Custom event property] and [Purchase property], respectively.

note

Braze Currents applies the [Appboy] prefix when exporting events to Amplitude. The label references Braze’s legacy product name. This is expected behavior and does not indicate an SDK or integration issue.

All cohorts named and imported into Braze will be prefixed with [Amplitude] and suffixed with their cohort_id. This means that a cohort named “TEST_COHORT” with the cohort_id “abcd1234” will be titled [Amplitude] TEST_COHORT: abcd1234 in Braze filters.

Contact your account manager or open a support ticket if you need access to additional event entitlements.

### Step 1: Configure Amplitude Integration in Braze

In Amplitude, locate your Amplitude export API key.

warning

Keep your Amplitude API Key up to date. If your connector’s credentials expire, the connector will stop sending events. If this persists for more than 48 hours, the connector’s events will be dropped, and data will be permanently lost.

### Step 2: Create Braze Current

In Braze, navigate to Currents > + Create Current > Create Amplitude Export. Provide an integration name, contact email, Amplitude export API key, and Amplitude region in the listed fields. Next, select the events you want to track; a list of available events is provided. Lastly, click Launch Current

note

Events sent from Braze Currents to Amplitude will count toward your Amplitude event volume quota.

tip

If you receive an “Invalid API key” error when pasting your Amplitude API key, try manually typing the key instead. Some browsers may add hidden characters when copying and pasting that can cause validation errors.

For more information, see Amplitude’s Appboy Amplitude Integration.

## Rate limits

Currents connect to Amplitude’s HTTP API, which has a rate limit of 30 events/second per device and an undocumented limit of 500K events/day per device. If these thresholds are exceeded, Amplitude will throttle events logged through Currents. If a device in your integration exceeds this rate limit, you may experience a delay in when events from all devices will appear in Amplitude.

Devices should not report more than 30 events/second or 500K events/day under normal circumstances, and this event pattern should only occur due to a misconfigured integration. To avoid this type of delay, ensure that your SDK integration reports events at a normal rate as specified in our SDK integration instructions and refrain from running automated tests that generate many events for a single device.

## Supported Currents events

Braze supports exporting the following events to Amplitude:

- Message engagement events
 
- Customer behavior events

For the payload structure of each event, select the Amplitude tab in the message engagement events glossary and customer behavior events glossary.

- 

New Stuff!
