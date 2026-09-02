---
url: https://www.braze.com/docs/partners/message_orchestration/templates/smartersends
slug: docs__partners__message_orchestration__templates__smartersends
title: "SmarterSends"
description: "This reference article outlines the partnership between Braze and SmarterSends, an easy-to-use interface designed for non-marketers to create, schedule, and deploy brand compliant emails campaigns...."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# SmarterSends

SmarterSends drives personalization with marketing campaigns that businesses can create, schedule, and deploy to enforce brand and legal compliance with control over the content and data used.

This integration is maintained by SmarterSends.

## About the integration

The Braze and SmarterSends partnership allows you to combine the power of Braze with the hyper-localized content owned by your distributed users to elevate your marketing campaigns.

## Prerequisites

 Requirement | 
 Description | 

 SmarterSends account | 
 A SmarterSends account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with these permissions: 
- users.track
- users.export.ids
- messages.schedule.create
- messages.schedule.update 
- messages.schedule.delete
- sends.id.create
- segments.list
- segments.data_series
- segments.details
- sends.data_series This can be created in the Braze dashboard from Settings > API Keys. For additional security, allowlist the SmarterSends IP address (available in your instance). | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

 Braze API campaign ID | 
 The Braze API campaign ID is the unique identifier for all campaigns sent through SmarterSends. This can be created in the Braze dashboard at Messaging > Campaigns. | 

## Use cases

With the Braze and SmarterSends integration, you can take advantage of distributed marketing by creating and executing marketing campaigns across multiple channels and locations. These advantages include:

- Increased reach: Using multiple channels and locations to reach a wider audience and target customers in different locations, resulting in increased brand exposure.
 
- Targeted messaging: Tailoring messaging across channels and locations to resonate with local audiences for more effective communication and engagement with customers.
 
- Improved brand consistency: Aligning your brand messaging and image across all channels and locations, which is important for building a strong and recognizable brand.
 
- Better insights: Collecting data from various channels and locations, providing valuable insights into customer behavior and preferences, which can be used to refine marketing strategies and tactics both on the local and global levels.
 
- Increased efficiency: Leveraging the strengths of different channels and locations, which can result in more efficient use of resources while still achieving the desired marketing goals.

## Integration

### Step 1: Create a REST API key

- In Braze, go to Settings > API Keys and click Create New API Key.
 
- Enter a name for the API key.
 
- Select the following permissions for this key to allow SmarterSends to interact with your Braze workspace.

- users.track
 
- users.export.ids
 
- messages.schedule.create
 
- messages.schedule.update
 
- messages.schedule.delete
 
- sends.id.create
 
- segments.list
 
- segments.data_series
 
- segments.details
 
- sends.data_series

- Add the SmarterSends IP address to the Whitelist IPs section.
 
- Click Save API Key.
 
- Copy and paste the API key with the appropriate permissions to the Braze Email Service Provider settings in SmarterSends.

### Step 2: Create or copy an application ID

- In your Braze workspace, go to Settings > App Settings.
 
- Set up a new app or use the application ID from an existing application within your workspace. Note the application ID is labeled as the API Key.
 
- Copy and paste this ID into the App ID field in SmarterSends.

### Step 3: Create an API campaign

An API campaign allows tracking metrics for all SmarterSends mail within Braze and enables SmarterSends to trigger these API-based campaigns.

- In Braze, create an API campaign.
 
- Click Email under Select Message Channel to add a messaging channel to begin tracking metrics.
 
- Next, copy and paste the campaign ID from Braze to the Campaign ID field in SmarterSends.
 
- Copy and paste the message variation ID from Braze to the Message Variant ID field in SmarterSends. This will be the default message ID used if you decide not to create a message ID for each group in SmarterSends.
 
- For each group you create in SmarterSends, add a message variant to your API campaign in Braze. Then, copy the message variant ID to the group’s message variant ID in SmarterSends.

tip

Create a message variant ID for each group you create in SmarterSends to view metrics for each group’s sends separately in your Braze workspace. This can be helpful to identify trends across groups when building reports in Braze.

## Customization

Each SmarterSends instance is fully customizable with your brand’s logo colors and custom domain name, creating a familiar environment. Additionally, for further personalization, you can define the attributes and custom attributes to target users in campaigns based on the segments within your Braze workspace.

- 

New Stuff!
