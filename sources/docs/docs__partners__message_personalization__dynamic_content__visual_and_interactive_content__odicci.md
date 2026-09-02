---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/odicci
slug: docs__partners__message_personalization__dynamic_content__visual_and_interactive_content__odicci
title: "Integrate Odicci with Braze"
description: "Step-by-step guide to integrating Odicci with Braze for personalized marketing campaigns"
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Integrate Odicci with Braze

Learn how to integrate Braze with Odicci, a platform that empowers businesses to acquire, engage and retain customers through loyalty driven omnichannel experiences.

tip

Refer to the Odicci Help Center for additional resources and FAQs.

## Use cases

You can connect the Odicci platform with Braze for seamless data sharing and campaign management, which includes:

- Automatically sending audience data collected in Odicci experiences to Braze.
 
- Triggering personalized marketing campaigns based on user interactions.
 
- Mapping fields between Odicci and Braze to ensure accurate data synchronization.

## Example

A retailer uses Odicci’s gamified experiences to collect email addresses for a marketing campaign.

- A customer completes a game in Odicci, providing their email address.
 
- Odicci automatically syncs this data to Braze.
 
- Braze triggers a personalized “Thank You” email and includes a discount code.

## Prerequisites

Before you start, you’ll need the following:

 Requirements | 
 Description | 

 An Odicci account | 
 An Odicci account with access to the Integrations section is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with the users.track and ‘campaigns.list’ permissions. | 

## Integrating Odicci

### Step 1: Enable the Integration in Odicci

- Log in to your Odicci account.
 
- Navigate to the Settings > Integrations section.
 
- 
 
Find the Braze integration and click Connect.

- Enter your Braze REST API Key into the provided field.
 
- Save the settings to activate the integration at the account level.

### Step 2: Obtain Your Braze REST API Key

- Log in to your Braze account.
 
- Go to Developer Console > REST API Keys.
 
- Create a new API Key or copy an existing one with the users.track permission.

### Step 3: Activate the Integration at the Experience Level

- Create or open an Experience in Odicci Studio.
 
- Navigate to Studio > Settings > Integrations.
 
- Locate the Braze checkbox and tick it to activate the integration for the experience.
 
- Save your changes.

### Step 4: Map Fields

- After activating the integration, remain in the Studio > Settings > Integrations section.
 
- Map the fields from your Odicci experience (e.g., Email, Name) to their corresponding fields in Braze.
 
- 
 
Save your configuration.

### Step 5: Test the Integration

- Run the experience in Odicci to collect test data.
 
- Verify that the data syncs correctly to Braze by checking the Braze dashboard or data logs.
 
- Ensure the mapped fields are correctly populated in Braze.

## Troubleshooting

If you experience issues with the integration, consider the following solutions. For further assistance, contact Odicci Support.

### API Key Not Valid

Double-check your Braze API Key and ensure it has the necessary permissions. Then, re-enter the API Key in the Odicci integration settings.

### Data Not Syncing

Verify that the fields in the Field Mapping section are correctly configured. Then, ensure the API Key has permissions for user data imports.

### Campaign Not Triggering

Check the Braze campaign settings to ensure the correct audience or trigger conditions are set.

- 

New Stuff!
