---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/storyly
slug: docs__partners__message_personalization__dynamic_content__visual_and_interactive_content__storyly
title: "Storyly"
description: "This reference article outlines the partnership between Braze and Storyly, a lightweight SDK, that allows app owners to target their segments and feed Braze with..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Storyly

Storyly is a lightweight SDK that brings stories to your app or website. With an intuitive design studio, insightful analytics, and seamless connectivity, Storyly is a powerful tool for enriching the audience experience.

This integration is maintained by Storyly.

## About the integration

The Braze and Storyly integration allows you to use your segments in Braze as an audience in the Storyly platform. With this integration, you can:

- Target your segments with specific stories
 
- Use user attributes to personalize your story contents

## Prerequisites

 Requirement | 
 Description | 

 Storyly account | 
 A Storyly account is required to take advantage of this partnership. | 

 Storyly SDK | 
 You must install the Storyly SDK. | 

 Braze REST API key | 
 A Braze REST API key with the following permissions 

 users.export.ids
 users.export.segments
 segments.list
 segments.details 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

## Use cases

With the Braze and Storyly integration, app owners can show stories to all segments in Braze and personalize the stories with user attributes.

Some common use cases include:

Target Braze segments in Storyly
After the integration is finished, you can create an Storyly audience based on your Braze segments. This could be a demographic or behavioral segment. For example, target users who live in a specific location, those who take a specific action on your app, or those interested in specific products with specific stories to increase conversion.

Personalized stories with user attributes
Braze user attributes are also usable in Storyly to generate dynamic stories. This could include a user’s name, products in a basket, or even favorited products, providing users unique personalized stories. Personalization helps increase conversion rates on stories and the overall story engagement rate.

## Data export integration

The Braze Storyly integration is explained in the following video:

Make sure that your Storyly integration holds custom parameters. These parameters will be matched to the Braze external id user property. Custom parameter implementation is explained here for iOS, Android, React Native, Flutter, and Web .

You can also refer to the Storyly documentation for more information.

### Step 1: Set the integration on Storyly dashboard

An integration be created within the Storyly Dashboard > Settings > Integrations > Connect with Braze. Here, you will need your Braze REST API key and Braze REST endpoint.

### Step 2: Get your segments

Next, you can use Braze segments to create a Storyly audience. This can be created within the Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze.

Here, there will be two syncing options. Select One-time sync for specific campaign stories, or Daily Sync for long-term stories.

- 

New Stuff!
