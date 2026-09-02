---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/lemnisk
slug: docs__partners__data_and_analytics__customer_data_platform__lemnisk
title: "Lemnisk"
description: "This reference article details the partnership between Braze and Lemnisk, an AI-enabled customer data platform-led Marketing Automation platform, allowing you to stream user data collected..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Lemnisk

Lemnisk, is an AI-powered Customer Data Platform (CDP) and marketing automation solution that enables real-time capture, unification, and activation of customer data from diverse, siloed sources. It seamlessly delivers this unified data across various MarTech and business platforms, while offering robust, real-time analytics to track every stage of the customer data lifecycle.

This integration is maintained by Lemnisk.

## About the integration

The Lemnisk and Braze integration allows brands and enterprises to unlock the full potential of Braze by acting as a CDP-led intelligence layer that unifies user data across platforms in real time, and sending the user’s information and behaviors collected to Braze in real-time. Lemnisk delivers enriched customer profiles directly into Braze by blending behavioral signals and personal attributes that let you personalize your messaging with deeper context.

## Prerequisites

 Requirement | 
 Description | 

 Lemnisk accounts | 
 A Lemnisk account is required to take advantage of this partnership. | 

 External API in Lemnisk | 
 Contact your Lemnisk CSM to get External API enabled for your account. | 

 Braze REST API key | 
 A Braze REST API key with users.track permission. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your account. | 

## Integrating Lemnisk

### Step 1: Create a Braze External API

In Lemnisk, go to the External API channel. Select Add New External API. We’ll now set up the Track Users endpoint as an External API.

Under Basic Details, enter a name, description, channel, and channel identifier.

Under External API details, enter the relevant details for your users.track endpoint. You can define multiple engagement-level fields using {{}}, which lets you set different values for different campaigns.

To finish setting up your Track Users configuration, select Save. You’ll automatically be redirected to the Test API page.

### Step 2: Test the configuration

On the Test API page, enter some test values for the API parameters in your JSON tree view, then select Test Configuration.

If your credentials and API definitions are correct, Braze will return a success response.

Next, you’ll verify that your events are being sent to Braze successfully. In the Braze dashboard, go to Audience > Search Users, then enter one of the identifiers from your External API configuration (such as a user email address). If everything is working correctly, the profile that received your test API trigger will be listed.

### Step 3: Trigger user events in Braze

- On Lemnisk, create a new segment. For example, you could create a segment that sends information to Braze as soon as users submit a lead form.
 
- In your new segment, go to External API > Add Engagement.
 
- Under Engagement Creation, enter the basic details and select the configuration you created previously.
 
- Under Configure Parameters, you’ll find the inputs for the Braze parameters you chose to expose at engagement level. In the following example, it shows Name of the User, Product ID, and Event Time.

- Enter the relevant personalization variables for our chosen parameters, then select Save.
 
- When you’re finished, activate the Engagement.

- 

New Stuff!
