---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/merkury
slug: docs__partners__data_and_analytics__customer_data_platform__merkury
title: "Merkury"
description: "This reference article outlines the partnership between Braze and Merkury, an enterprise identity platform for your apps, that allows you to leverages the `MerkuryID` to..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Merkury

Merkury is Merkle’s enterprise identity platform that helps brands maximize consumer engagement, experience, and revenue through first-party cookieless identity capabilities. The MerkuryID unifies a brand’s known and unknown customer and prospects records, site/app visits, and consumer data to a single, persistent person ID.

This integration is maintained by Merkury.

## About the integration

The Braze and Merkury integration allows you to leverages the MerkuryID to increase site visitor recognition rates for Braze customers. Upon recognizing visitors that are brand email subscribers, Merkury updates the Braze profile to include the subscribers email address. The increased recognition capabilities of MerkuryID improves engagement and personalization opportunities and immediately increases site abandonment email send quantities and associated revenue.

## Prerequisites

 Requirement | 
 Description | 

 Merkle account | 
 A Merkle account is required to take advantage of this partnership. | 

 Merkle Client ID | 
 Obtain your Client ID from your Merkle representative. | 

 Merkury tag | 
 Place Merkle’s Merkury tag on your website. | 

 Braze REST and SDK endpoint | 
 Your REST or SDK endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

 Braze REST API key | 
 A Braze REST API key with users.track, users.export.ids, users.export.segment, and segments.list permissions. 

This can be created within Braze Dashboard > Developer Console > REST API Key > Create New API Key. | 

important

The Merkury identity connector requests to Braze operate within Braze API rate limit specifications. Contact Braze or your Merkle account manager if you have any questions.

Merkury sends at least one request at the end of a qualified session.

## Side-by-side SDK integration

Uses Merkle’s client-side Merkury tag to capture Braze devices and forwards them to the Merkury identity connector endpoint for identification.

### Step 1: Setup Braze web SDK tag

You must have the Braze Web SDK deployed on your website to use this integration.

### Step 2: Deploy Merkle’s Merkury tag

Deploy the Merkury tag on your website to make the Merkury identity connector available on your website. Your Merkle account manager will provide you with a detailed guide with instructions.

### Step 3: Create custom attributes

The Merkury identity connector populates the following fields, which you must create in Braze as custom attributes.

 Attribute name | 
 Data type | 
 Description | 

 hmid | 
 String | 
 Merkle’s Merkury ID | 

 confidence_score | 
 Number | 
 How confident Merkury was able to identify (1-8, lower is better) | 

### Step 4: Provide Merkle with user email universe

Merkle recommends a segmentation export of your permissible email universe. This can be followed up with daily exports of active permissible users.

The following fields are required:

- braze_id
 
- external_id
 
- email address

See your Braze representative for further information.

- 

New Stuff!
