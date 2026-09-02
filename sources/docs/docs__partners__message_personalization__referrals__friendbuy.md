---
url: https://www.braze.com/docs/partners/message_personalization/referrals/friendbuy
slug: docs__partners__message_personalization__referrals__friendbuy
title: "Friendbuy"
description: "Learn how to integrate Friendbuy with Braze."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Friendbuy

Use the integration between Friendbuy and Braze to expand your email and SMS capabilities while effortlessly automating your referral and loyalty program communications. Braze will generate customer profiles for all the opted-in phone numbers collected via Friendbuy.

This integration is maintained by Friendbuy.

## Prerequisites

Before you start, you’ll need the following:

 Requirements | 
 Description | 

 A Friendbuy account | 
 A Friendbuy account is required to take advantage of this partnership. | 

 A Braze REST API key | 
 A Braze REST API key with users.track permissions. This can be created in the Braze dashboard from Settings > API Keys. | 

 A Braze REST endpoint | 
 Your REST endpoint URL, which depends on the URL for your Braze instance. | 

## Integrating Friendbuy

In Friendbuy, go to Developer Center > Integrations, then on the Braze integration card select Add integration.

In the form, enter your REST endpoint and API Key, then select Install Integration.

Go to back to your Friendbuy account and refresh the page. If your integration was successful, you’ll see a message similar to the following:

### Custom attributes

 Custom Attribute Name | 
 Definition | 
 Data Type | 

 Friendbuy Referral Status | 
 Referrers are categorized as Advocate and referees are categorized as Referred Friend | 
 String | 

 Friendbuy Customer Name | 
 The name the customer entered when submitting their info through a referral widget | 
 String | 

 Friendbuy Referral Link | 
 A personal referral link (PURL) generated for an Advocate. For example, https://fbuy.io/EzcW | 
 String | 

 Friendbuy Date of Last Share | 
 The date and time the Advocate last shared with a Friend via any share channel. If the Advocate has not shared yet, the property won’t be visible. | 
 Time | 

 Friendbuy Campaign ID | 
 The Campaign ID associated with the personal referral link generated for an Advocate | 
 String | 

 Friendbuy Campaign Name | 
 The Campaign Name associated with the personal referral link generated for an Advocate | 
 String | 

 Friendbuy Coupon Code | 
 The most recent Referral coupon code distributed to the customer. Note: only one code will be displayed | 
 String | 

 Friendbuy Coupon Value | 
 The currency value of the most recent coupon code distributed to the customer. | 
 Number | 

 Friendbuy Coupon Status | 
 The status of the most recent coupon code distributed to the customer. Note: status will be ‘distributed’ or ‘redeemed’ | 
 String | 

 Friendbuy Coupon Currency | 
 Currency code (USD, CAD, etc.) or percent (%) associated with the most recent coupon code distributed to the customer. | 
 String | 

 Friendbuy Coupon Campaign ID | 
 The Campaign ID associated with the coupon code generated for a customer. | 
 String | 

## Default behavior

Before customer data can be sent to Braze, customers must opt-in through the referral widget by checking one or more boxes of the following boxes:

note

Friendbuy uses the international standard (E.164) to verify real phone numbers. Invalid numbers, such as 555-555-5555, will not be sent to Braze.

### Checkbox behavior

 Checkbox selected | 
 Behavior | 

 Email only | 
 Only the customer’s email address is sent to Braze. | 

 Phone only | 
 Only the customer’s phone number is sent to Braze. | 

 Neither | 
 No customer data is sent to Braze. | 

 Both | 
 The customer’s email address and phone number is sent to Braze. | 

- 

New Stuff!
