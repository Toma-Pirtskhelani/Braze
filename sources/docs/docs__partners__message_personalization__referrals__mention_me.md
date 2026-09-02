---
url: https://www.braze.com/docs/partners/message_personalization/referrals/mention_me
slug: docs__partners__message_personalization__referrals__mention_me
title: "Mention Me"
description: "Mention Me Integration Setup Guide"
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Mention Me

Together, Mention Me and Braze can be your gateway to attracting premium customers and fostering unwavering brand loyalty. By seamlessly integrating first-party referral data into Braze, you can deliver highly-personalized omnichannel experiences targeted at your brand fans.

This integration is maintained by Mention Me.

## Prerequisites

Before you start, you’ll need the following:

 Requirements | 
 Description | 

 A Mention Me account | 
 A Mention Me account is required to take advantage of this partnership. | 

 A Braze REST API key | 
 A Braze REST API key with users.track and templates.email.create permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 A Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

## Use cases

- Send contact data and opt-ins from Mention Me referred customers to Braze in real time
 
- Use referral data to create coupon email reminders
 
- Enhance the performance of other marketing channels by using referral data to segment and target high value customers

## What data is sent from Mention Me to Braze?

When you set up this integration, Mention Me will automatically create your customer attributes and events—so no need to do this beforehand.

Your customer’s email addresses in Braze will be used to link relevant events and custom attributes. Mention Me will send events and contact profile attributes for any prospect or existing customer who triggers this event via Mention Me, regardless of their opt-in status.

For more details, refer to Contact profile attributes and events.

## Integrating Mention Me

tip

For a full step-by-step walkthrough, refer to Mention Me’s Braze setup documentation.

To integrate Mention Me with Braze:

- In Mention Me, go to the Braze integration page, then select Connect.
 
- Select Create New Authorization, then add the API key you previously created and select your Braze instance.
 
- Choose one or more countries you’d like to sync with.
 
- When you’re finished, select Connect.

- 

New Stuff!
