---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents
slug: docs__partners__data_and_analytics__customer_data_platform__mparticle__mparticle_for_currents
title: "mParticle for Currents"
description: "This reference article outlines the partnership between Braze Currents and mParticle, a customer data platform that collects and routes information between sources in your marketing..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# mParticle for Currents

mParticle is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and mParticle integration allows you to seamlessly control the flow of information between the two systems. With Currents, you can also connect data to mParticle to make it actionable across the entire growth stack.

## Prerequisites

 Requirement | 
 Description | 

 Currents | 
 In order to export data back into mParticle, you need to have Braze Currents set up for your account. | 

 mParticle account | 
 An mParticle account is required to take advantage of this partnership. | 

 mParticle server-to-server key and secret | 
 These can be obtained by navigating to your mParticle dashboard and creating the necessary feeds that allow mParticle to receive Braze interaction data for iOS, Android, and Web platforms. | 

## About mParticle credentials

mParticle has app-level and workspace-level credentials which impact how your events are sent.

- App-level: mParticle will separate events by each individual app, meaning the app-level credentials you give to your iOS app can only be used to send iOS-specific events.
 
- Workspace-level: mParticle groups all events together (that are not app-specific), meaning the workspace-level credentials you give your app group will be used to send all of your non-app-specific events.

You can think of this as mParticle ingesting a “feed” based on each individual app. For example, if you have one app for iOS, one for Android, and one for Web, your events will be disjointed. This means if you provide the same credentials for each app, then one mParticle feed will be used to receive all data for all of your apps, with no duplication.

## Integration

### Step 1: Create feeds

From your mParticle admin account, navigate to Setup > Inputs. Locate Braze in the mParticle Directory and add the feed integration.

The Braze feed integration supports four separate feeds: iOS, Android, Web, and Unbound. The unbound feed can be used for events such as emails that are not connected to a platform. You will need to create an input for each main platform feed. You can create additional inputs from Setup > Inputs, on the Feed Configurations tab.

For each feed, under Act as Platform select the matching platform from the list. If you do not see an option to select an act-as feed, the data will be treated as unbound, but can still be forwarded to data warehouse outputs.

As you create each input, mParticle will provide you with a key and secret. Copy these credentials, making sure to note which feed each pair of credentials is for.

### Step 2: Create Current

In Braze, navigate to Currents > + Create Current > Create mParticle Export. Provide an integration name, contact email and the mParticle API key and mParticle secret key for each platform. Next, select the events you want to track; a list of available events is provided. Lastly, click Launch Current

important

It’s important to keep your mParticle API Key and mParticle Secret Key up to date; if your connector’s credentials expire, the connector will stop sending events. If this persists for more than 5 days, the connector’s events will be dropped and data will be permanently lost.

All events sent to mParticle will include the user’s external_user_id as the customerid. At this time, Braze does not send event data for users who do not have their external_user_id set. If you’d like to map the external_user_id to a different ID in mParticle that is not the default customerid, please contact your Braze CSM.

## Supported Currents events

Braze supports exporting the following events to mParticle:

- Message engagement events
 
- Customer behavior events

For the payload structure of each event, select the mParticle tab in the message engagement events glossary and customer behavior events glossary.

To read more about the mParticle integration, visit the mParticle documentation.

- 

New Stuff!
