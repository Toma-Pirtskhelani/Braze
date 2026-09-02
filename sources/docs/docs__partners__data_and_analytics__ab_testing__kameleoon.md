---
url: https://www.braze.com/docs/partners/data_and_analytics/ab_testing/kameleoon
slug: docs__partners__data_and_analytics__ab_testing__kameleoon
title: "Kameleoon"
description: "Learn how to integrate Kameleoon with Braze"
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Kameleoon

Kameleoon is an optimization solution with experiment, AI-powered personalization, and feature management capabilities in a single unified platform.

## Prerequisites

Before you start, you’ll need the following:

 Requirement | 
 Description | 

 Kameleoon account | 
 A Kameleoon account is required to take advantage of this partnership. | 

 Braze account | 
 An active Braze account with the Braze Web SDK integrated on your webpage. You’ll also need event property segmentation enabled. To request it, refer to Considerations. | 

## Use cases

Kameleoon sends custom events to Braze to identify users participating in experimentation and personalization campaigns, enabling more precise targeting and personalized messaging.

## Integrating Kameleoon

This integration runs as a JavaScript tracker through Kameleoon’s engine.js. It can be quickly enabled from within Kameleoon’s platform.

### Step 1: Go to the Kameleoon Integrations page

In your Kameleoon app, select Admin and then Integrations on the sidebar.

### Step 2: Install the Braze tool

By default, the Braze tool isn’t installed. Look for the Braze icon, then select Install the tool. 

Select the projects for which you want to activate the Braze tool, so that Kameleoon data will correctly report to Braze.

After configuring the tool, select Validate, which will close the configuration panel. You will then see an ON toggle next to the Braze tool’s icon, including the number of projects the tool is configured on.

important

This feature is in beta. Join the Kameleoon Beta Program to start using this integration.

### Step 3: Associate Braze with Kameleoon campaigns

#### In the Graphic/Code editor

To finalize your experiment, select the Integrations step to configure Braze as a tracking tool, then select Braze.

Braze will be mentioned in the summary before going live. Kameleoon will automatically transmit the data to Braze, and you’ll be able to use it for analysis and segmentation directly in Braze.

##### Personalization creation

On the Personalization Creation page, you can select Braze among the reporting tools to personalize your reporting.

##### Feature flag creation

Set up the integration in the feature flag environment in the Integrations section. Enable it for the environments where you want it active.

##### Results page

After Braze is set as a reporting tool for an experiment, you can select (or unselect) it on the Kameleoon results page in the Experiment configuration menu.

note

This integration requires a hybrid implementation and is only compatible with web SDKs.

The reporting tools associated with the experiment will display. Select Edit to edit this selection.

### Step 4: Analyze and Leverage Your Kameleoon Data in Braze

After the integration is set up, Kameleoon will send custom events called kameleoon_exposure with properties such as Experiment name, Experiment ID, Variation name, Variation ID to Braze.

You can then view this data in the Custom Events, create custom event reports to identify Kameleoon campaign exposure, and enable segmentation based on event properties. You can use custom events when creating subsequent or linked campaigns and Canvases through Action Paths, action-based triggers or creating segments

Furthermore, these events will be accessible through Currents custom event objects to allow for comprehensive reporting and analysis.

## Considerations

### Request event property segmentation

Before you can use event property segmentation, you’ll need it enabled in Braze. Use the following template to contact your Braze CSM or the support team for access.

 Request event property segmentation

 Field | 
 Details | 

 Subject | 
 Request to Enable Event Property Segmentation for Kameleoon Integration | 

 Body | 
 
 Hello Braze Team,

 We would like to enable event property segmentation for events sent from our Kameleoon<>Braze integration. Here are the details:

 - Event Name: Kameleoon

 - Event Properties: kameleoon_campaign_name, kameleoon_variation_name

 Please confirm once the properties have been enabled in our account.

 Thank you.
 | 

### Braze data points

The custom event sent from Kameleoon to Braze—including any event properties enabled for segmentation—will log data points in your Braze instance.

- 

New Stuff!
