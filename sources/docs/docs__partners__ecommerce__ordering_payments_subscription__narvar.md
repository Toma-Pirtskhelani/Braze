---
url: https://www.braze.com/docs/partners/ecommerce/ordering_payments_subscription/narvar
slug: docs__partners__ecommerce__ordering_payments_subscription__narvar
title: "Narvar"
description: "Learn how to integrate Narvar with Braze."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Narvar

Narvar is a post-purchase platform that enhances customer loyalty through order tracking, delivery updates, and returns management. The Braze and Narvar integration enables brands to leverage Narvar’s notification events to trigger messages directly from Braze, keeping customers informed with timely updates.

## Prerequisites

 Requirement | 
 Description | 

 Narvar Account | 
 A Narvar account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with messages.send permission. This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL, which depends on the URL for your Braze instance. | 

## Supported features

 Type | 
 Supported features | 

 Notifications | 
 - Delivery Anticipation
- Carrier Delay
- Delivered Standard | 

 Channels | 
 Push Notifications | 

note

If you’re interested in additional notification types or channels, please contact your Braze and Narvar CSM.

## Integration Details

For each notification event, Narvar initiates a request to the Braze /messaging/send endpoint to deliver a push message to each opted-in consumer.

Narvar is responsible for configuring the push notification payloads for each message. Currently, Narvar does not have a built-in design interface for push notifications, so their team will collaborate with your team to determine and define payload requirements. These payloads can be customized to the same extent as those sent through your own system, including support for variable content placeholders, such as order data and consumer details.

## Getting Started with the Braze-Narvar Integration

- Contact your Narvar CSM to express interest in the integration.
 
- Designate Braze environments for staging and production.
 
- Generate API Key in Braze for Narvar’s use.
 
- Generate Campaign Key(s) in Braze as needed.
 
- Provide API and Campaign keys to Narvar through a secure one-time link.
 
- Share Push Notification Payload Details to finalize setup.

- 

New Stuff!
