---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/growthloop
slug: docs__partners__data_and_analytics__customer_data_platform__growthloop
title: "GrowthLoop"
description: "This reference article outlines the partnership between Braze and GrowthLoop, a platform that allows you to segment customer data directly from data warehouses and send..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# GrowthLoop

GrowthLoop helps marketing teams activate customer data from the cloud data warehouse to Braze and other channels. Automate, scale, and measure marketing programs from your cloud data warehouse, keeping the data in a single, centralized location.

This integration is maintained by GrowthLoop.

## About the integration

The Braze and GrowthLoop integration allows you to segment customer data directly from data warehouse and send it to Braze–ensuring that users can optimize the deep feature set of Braze in tandem with their single source of truth. Streamline marketing efforts for customer segmentation and activation, reducing the time it takes to segment, launch, test, and measure the results of targeted campaigns sent to Braze.

## Prerequisites

 Requirement | 
 Description | 

 GrowthLoop growth or enterprise account | 
 A GrowthLoop account is required to take advantage of this partnership. | 

 Braze Rest API key | 
 A Braze REST API key with all permissions.

This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

## Use cases

Send customer lists from your data warehouse to Braze, targeting email and push notification campaigns in one click, and always keep them in sync.

- Emails based on sign-up activation — send emails to help users that fall off in your sign-up flow and convert them to active users.
 
- Emails based on any user behavior — send emails based on user behavior, such as “Add to Cart.”
 
- Emails to churned customers — re-engage churned customers via email with an offer.

## Integration

### Configure Braze connection in GrowthLoop

When you sign into the Segmentation Platform within GrowthLoop, navigate to the Destinations tab in the navigation sidebar and click New Destination in the action bar.

Scroll until you can find Braze, and click Add Braze.

A popup will appear to configure the connection to the destination.

- Destination name: This is how the destination will be named and referred to in the app going forward
 
- Sync frequency: Select Daily or Hourly; this will control how often GrowthLoop exports audiences to Braze
 
- API key: API key created in the requirements, with the necessary permissions
 
- API URL: URL as defined in the requirements

Click Create, and you can export your first audience to Braze! To create an audience in GrowthLoop, visit Create an Audience.

### Post export

Once your audience has been exported, every 15 minutes, GrowthLoop will generate an updated version of your customer lists and send it to Braze.

At the same time, GrowthLoop will remove users from your audience that no longer qualify and add newly qualified users to your audience.

Braze will match users and create a flag, signifying they are part of a GrowthLoop audience.

When you create a campaign in Braze, you can select customers in that GrowthLoop audience.

## Troubleshooting

Contact the GrowthLoop team at [email protected] for additional information or support.

- 

New Stuff!
