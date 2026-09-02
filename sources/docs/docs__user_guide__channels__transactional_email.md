---
url: https://www.braze.com/docs/user_guide/channels/transactional_email
slug: docs__user_guide__channels__transactional_email
title: "Transactional email"
description: "Send transactional emails for critical, time-sensitive notifications triggered by API calls in Braze."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Transactional email

Transactional emails are purpose-built for sending automated, non-promotional messages to facilitate an agreed-upon transaction between you and your customers. Use transactional email campaigns in Braze to send critical, time-sensitive notifications triggered by API calls, such as order confirmations, password resets, and shipping updates.

## Prerequisites

Transactional email is only available as part of select Braze packages. Contact your Braze customer success manager or open a support ticket for more details.

Before you start, make sure you have the following:

- Completed email setup, including IP and domain configuration, authentication, and IP warming
 
- A Braze REST API key with the transactional.send permission

## Use cases

Transactional email is designed for sending non-promotional, service-triggered messages. Common use cases include the following:

 Use case | 
 Explanation | 

 Order confirmations | 
 Confirm that a customer’s purchase has been received and is being processed. | 

 Password resets | 
 Deliver secure, time-sensitive links for customers to reset their account credentials. | 

 Shipping notifications | 
 Notify customers when their order has shipped, including tracking information and estimated delivery dates. | 

 Account alerts | 
 Send critical account-related notifications, such as payment failures, subscription changes, or security alerts. | 

## How transactional email differs from marketing email

Transactional emails are sent through a dedicated Braze transactional HTTP API, which is optimized for speed and reliability. Unlike marketing emails, transactional emails:

- Don’t require a user to be opted in to marketing communications
 
- Are triggered by API calls rather than scheduled or action-based triggers
 
- Support near-real-time delivery for time-sensitive content

## Next steps

- Create a transactional email
 
- Tracking

- 

New Stuff!
