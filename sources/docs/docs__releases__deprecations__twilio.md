---
url: https://www.braze.com/docs/releases/deprecations/twilio
slug: docs__releases__deprecations__twilio
title: "Twilio"
description: "This article outlines the partnership between Braze and Twilio."
section: releases/deprecations
fetched: 2026-09-02
evidence: company-own (technical)
---
# Twilio

warning

Note that support for the Twilio Webhook Integration will be discontinued on January 31, 2020. If you wish to still access SMS services with Braze, see our SMS documentation.

For this example, we’ll configure the Braze webhook channel to send SMS and MMS to your users, via Twilio’s message sending API. For your convenience, a Twilio webhook template is included on the dashboard.

## HTTP URL

The Webhook URL is provided by Twilio in your dashboard. This URL is unique to your Twilio account since it contains your Twilio account ID (TWILIO_ACCOUNT_SID).

In our Twilio example, the webhook URL is https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json. You can find this URL in the Getting Started section of the Twilio console.

## Request Body

The Twilio API expects the request body to be URL-encoded, so we have to start by changing the request type in the Braze webhook composer to Raw Text. The required parameters for the body of the request are To, From, and Body.

The following screenshot is an example of what your request might look like if you are sending an SMS to each user’s phone number, with the body “Hello from Braze!”.

- You’ll need to have valid phone numbers on each user profile in your target audience.
 
- To meet Twilio’s request format, use the url_param_escape Liquid filter on your message contents. This filter encodes a string so all the characters are allowed in an HTML request; for example, the plus character (+) in the phone number +12125551212 is forbidden in URL-encoded data and will be converted to %2B12125551212.

## Request Headers and Method

Twilio requires two request headers, the request Content-Type and an HTTP Basic Authentication header. Add them to your webhook by clicking the gear icon on beside the webhook composer, then clicking Add New Pair twice.

 Header Name | 
 Header Value | 

 Content-Type | 
 application/x-www-form-urlencoded | 

 Authorization | 
 Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }} | 

Be sure to replace TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN with values from your Twilio dashboard. Lastly, Twilio’s API endpoint is expecting an HTTP POST request, so choose that option in the dropdown for HTTP Method.

## Preview Your Request

Use the webhook composer to preview the request for a random user, or for a user with particular credentials, to ensure that the request is rendering properly.

- 

New Stuff!
