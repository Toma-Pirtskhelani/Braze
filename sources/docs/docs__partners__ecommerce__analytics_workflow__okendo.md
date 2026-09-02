---
url: https://www.braze.com/docs/partners/ecommerce/analytics_workflow/okendo
slug: docs__partners__ecommerce__analytics_workflow__okendo
title: "Okendo"
description: "Learn how to integrate Okendo with Braze."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Okendo

Okendo is a unified customer marketing platform that provides tools to cultivate advocacy, scale word-of-mouth, and maximize lifetime value to mobilize your customers for faster, more efficient growth.

This integration is maintained by Okendo.

## About the integration

The Braze integration with Okendo works across multiple products in Okendo’s platform, including Reviews, Loyalty, Referrals, Surveys, and Quizzes. Okendo sends custom events and user attributes to Braze, which can be used to personalize and trigger messages.

## Prerequisites

 Requirement | 
 Description | 

 Okendo account | 
 An Okendo account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. | 

## Integration

### Step 1: Set up Braze Connector in Okendo

- In Okendo, go to Settings > Integrations > Email & SMS > Braze
 
- Add the API endpoint and API key to the Integration settings.

### Step 2: Configure your identifier

The external_id field is used to identify the user associated with each event. Toggle on Use Shopify Customer ID for Braze user identification to associate the field with Shopify Customer IDs. Otherwise, toggle it off to associate it with each user’s email address.

## Syncing Okendo events and attributes to Braze

### Custom events

note

For sample event data, refer to Okendo’s documentation.

#### Review events

- Okendo Review Created
 
- Okendo Review Request

#### Referral events

- Sent Okendo Referral
 
- Opted In to Okendo Referrals
 
- Okendo Referral Invitation
 
- Received Okendo Referral Coupon
 
- Redeemed Okendo Referral Coupon
 
- Okendo Referral Rejected

#### Loyalty events

- Enrolled in Okendo Loyalty
 
- Okendo Loyalty Points Awarded
 
- Okendo Loyalty Points Redeemed
 
- Okendo Loyalty Tier Changed
 
- Okendo Loyalty Points Adjusted

#### Survey event

- Submitted Okendo Survey

#### Quiz event

- Submitted Okendo Quiz

### Custom attributes

Okendo sends user profile data as custom attributes in Braze, which can be used to create audience segments. Examples include:

- Profile questions asked in surveys and during a review submission, such as age, birthday, skin type, and hair color
 
- Review metrics such as Average Review Rating and Average Review Sentiment
 
- Loyalty metrics such as Points Balance and VIP Tier
 
- Referrals metrics such as the Number of Successful Referrals and Total Referral Revenue
 
- NPS score collected from a survey

## Using Braze with Okendo products

Depending on the Okendo product, you must complete additional steps to use Braze and Okendo together. Refer to the following articles for more details:

- Integrating Reviews with Braze
 
- Integrating Loyalty with Braze
 
- Integrating Referrals with Braze
 
- Integrating Surveys with Braze
 
- Integrating Quizzes with Braze

note

For assistance with configuring the integration, contact the Okendo support team.

- 

New Stuff!
