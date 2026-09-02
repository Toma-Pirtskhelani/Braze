---
url: https://www.braze.com/docs/partners/data_and_analytics/loyalty/antavo
slug: docs__partners__data_and_analytics__loyalty__antavo
title: "Antavo Loyalty Cloud"
description: "This reference article outlines the partnership between Braze and Antavo, a next-gen loyalty program that goes beyond rewarding purchases."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Antavo Loyalty Cloud

Antavo is an enterprise-grade SaaS loyalty technology provider that builds comprehensive loyalty programs to foster brand love and change customer behavior.

This integration is maintained by Antavo.

## About the integration

The Antavo and Braze integration allows you to use loyalty program-related data to build personalized campaigns to enhance the customer experience. Antavo supports loyalty data synchronization between the two platforms—this is a one-way data synchronization only, from Antavo to Braze. The integration supports the external_id Braze field, which Antavo uses to synchronize the loyalty member ID.

## Prerequisites

 Requirement | 
 Description | 

 Antavo account | 
 An Antavo account with the Braze integration enabled is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with the following permissions: users.track, events.list, events.data_series, and events.get.

This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

 Braze app identifier | 
 Your app identifier key. 

To locate this key in the Braze dashboard, go to Settings > API Keys and find the Identification section. | 

## Integration

### Step 1: Connect Braze in Antavo

In Antavo, go to Modules > Braze and click Configure. When first navigating to the Braze integration configuration page in Antavo, the interface will prompt you to connect the two systems.

Provide the following credentials:

- Instance URL: The Braze REST endpoint of the instance you are provisioned to.
 
- API Token (Identifier): The Braze REST API key that Antavo should use when sending requests to Braze.
 
- App Identifier: The Braze app identifier.

After you enter the credentials, click Connect.

### Step 2: Configure field mapping

After the connection is established, you’ll be redirected to the Sync Fields page automatically in Antavo to configure the field synchronization between the two systems. You can reach this page at any time through Modules > Braze.

To configure field mapping in Antavo:

- Click Add new field .
 
- Use the dropdown field to select the Antavo Loyalty field that you want to synchronize to Braze.
 
- Enter the Remote field that represents the equivalent custom attribute in Braze to which the data will be populated.

note

You can find your list of custom attributes in Braze under Data Settings > Custom Attributes. If the field you enter is not defined in Braze, a new field will automatically be generated with the first sync.

- To add additional field pairings, repeat steps 1-3.
 
- To remove a field from the list of synchronized data, click at the end of the row.
 
- Click Save.

When any value of the configured fields changes in Antavo, not only the synchronization of that single value is triggered, but every field added to the field mapping is included in the request.

important

To minimize data point usage, we recommend only mapping the fields that will be actioned on within Braze.

#### Supported data types

The integration supports all Braze custom attribute data types, namely: number (integer, float), string, array, boolean, object, array of objects, and date.

The data fields are populated based on the configured field mapping.

## Triggers

In addition to configuring field mapping, the integration provides further capabilities through features built into Antavo’s Workflows tool. All Braze custom attribute data types and custom event property data types can be synchronized through workflows as well.

### Synchronizing loyalty data occasionally

Use this option if the data is not stored in loyalty fields in Antavo or if the data is not added to the list of mapped fields. The synchronization of requested data is triggered when the configured workflow criteria are met.

Visit the step-by-step guide to learn how to configure the synchronization of loyalty data related to the last purchase.

### Synchronizing loyalty program events

Use events synchronized from Antavo to enter loyalty members in action-based Braze Canvases. The integration can synchronize any Antavo event (including purchase events) that appears in Braze as custom events.

Visit the step-by-step guide to learn how to configure the synchronization of the loyalty program enrollment event and the synchronization of the loyalty program benefit earning event.

- 

New Stuff!
