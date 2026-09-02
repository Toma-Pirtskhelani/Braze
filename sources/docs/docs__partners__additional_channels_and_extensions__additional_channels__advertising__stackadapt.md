---
url: https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/advertising/stackadapt
slug: docs__partners__additional_channels_and_extensions__additional_channels__advertising__stackadapt
title: "StackAdapt"
description: "This reference article outlines the partnership between Braze and StackAdapt."
section: partners/additional_channels_and_extensions
fetched: 2026-09-02
evidence: company-own (technical)
---
# StackAdapt

StackAdapt is the leading AI-powered marketing platform used by digital marketers to deliver targeted performance-driven advertising.

This integration is maintained by StackAdapt.

The Braze and StackAdapt integration allows you to sync user profile data from Braze into the StackAdapt Data Hub. By connecting the two platforms, you can create a unified view of your customers and activate first-party data to improve ad performance.

## Use cases

- Re-engage lapsed users: Identify users who have unsubscribed from email marketing lists in Braze and target them with programmatic ads on StackAdapt to re-engage them through a different channel.
 
- Create multi-channel experiences: Extend a user’s journey beyond email. For example, if a user clicks on an email campaign in Braze, you can use StackAdapt to show them a complementary programmatic ad, reinforcing the message and driving further action.
 
- Personalize at scale: Leverage granular data points from Braze, such as “Home City” or “Language”, to serve highly relevant, localized, and language-specific ads and emails.
 
- Deepen understanding of your audience: By syncing profile attributes, you can create richer audience segments in StackAdapt, enabling more precise targeting and personalized ad experiences.

## Prerequisites

 Requirement | 
 Description | 

 StackAdapt Account | 
 You need an active StackAdapt account with permissions to manage Data Hub integrations. | 

 Braze REST API key | 
 A Braze REST API key with the following permissions: 
- users.export.ids
- users.export.segment
- email.unsubscribe
- email.hard_bounces
- messages.schedule_broadcasts
- campaigns.list
- campaigns.details
- canvas.list
- canvas.details
- segments.list
- segments.details
- purchases.product_list
- events.list
- feed.list
- feed.details
- templates.email.info
- templates.email.list
- subscription.status.get
- subscription.groups.get

This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. | 

## How it works

The StackAdapt Data Hub connects directly to your Braze account to pull user profile attributes. This allows you to leverage your Braze customer data directly within StackAdapt for advanced audience segmentation and activation.

### Data flow

- StackAdapt initiates a secure connection to your Braze instance using the provided API credentials.
 
- StackAdapt retrieves user profile data and specifically the properties you have selected and mapped.
 
- The data is normalized and ingested into your StackAdapt Data Hub, becoming available for segmentation and use in your campaigns.
 
- The integration allows for scheduled data syncs (for example, daily) to keep your StackAdapt audiences up-to-date with the latest profile data from Braze.

## Fields synced

StackAdapt can sync a variety of Braze profile fields, including, but not limited to:

- standard attributes
 
- custom attributes
 
- attribution data
 
- subscription status

- Email
 
- Date of Birth
 
- First Name
 
- Last Name
 
- Phone
 
- Home City
 
- Country
 
- Gender
 
- Time Zone
 
- Created At
 
- External ID
 
- Language

Attributes that are specific to your app or business, defined based on your specific business needs.

- Attributed Ad
 
- Attributed Adgroup
 
- Attributed Campaign
 
- Attributed Source

- Email Subscription Status
 
- Push Subscription Status

It is crucial to accurately map fields in Braze that reflect user consent for marketing communications (for example, email subscription status) so that your advertising efforts remain compliant with user preferences and privacy regulations.

## Setting up the integration

Follow these steps to import your Braze user profiles:

- Log into your StackAdapt account.
 
- In the navigation menu, select Data Hub.
 
- Select Import Profiles, then select Braze from the list of available integrations.
 
- Enter your Braze API credentials when prompted.

- Braze REST API Key: Located in Braze by going to Settings > API Keys. As a security best practice, we recommend creating a dedicated API key for your StackAdapt integration.
 
- Braze App Key: Located in Braze by going to Settings > API Keys or Manage Apps.
 
- Braze REST Endpoint URL: The base URL for your Braze instance (for example, https://rest.iad-01.braze.com).

- Select Connect to verify the credentials.

- Choose your connection and select your StackAdapt advertiser.
 
- Configure your Property Mappings. Review and confirm the default mappings and pre-selected properties that StackAdapt suggests.
 
- (Optional) If you want to import additional properties, select them by checking the respective checkboxes and specify if they contain PII and their data type.

- Add your profiles to a List or create a new one so you can group and segment your profiles
 
- Select Activate Integration to start the initial data sync.

## Considerations

- Importing custom events and properties: This feature is not yet supported.
 
- Data latency: It can take up to 24 hours to import all of the user profile data.
 
- Consent management: Confirm that your data collection practices in Braze align with privacy regulations and that you have the necessary consent to use customer data for advertising purposes. StackAdapt relies on the consent status passed from your source systems.
 
- Attribute consistency: To maximize the effectiveness of your data, maintain consistency in how attributes are named and populated in Braze before syncing them to StackAdapt.

- 

New Stuff!
