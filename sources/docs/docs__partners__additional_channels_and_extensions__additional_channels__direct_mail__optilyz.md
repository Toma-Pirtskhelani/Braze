---
url: https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz
slug: docs__partners__additional_channels_and_extensions__additional_channels__direct_mail__optilyz
title: "optilyz"
description: "This reference article outlines the partnership between Braze and optilyz, which enables you to run more customer-centric, sustainable, and profitable direct mail campaigns."
section: partners/additional_channels_and_extensions
fetched: 2026-09-02
evidence: company-own (technical)
---
# optilyz

optilyz is a direct mail automation platform that enables you to run more customer-centric, sustainable, and profitable direct mail campaigns.

This integration is maintained by optilyz.

## About the integration

Use the optilyz and Braze webhook integration to send your customers direct mail such as letters, postcards, and self-mailers.

## Prerequisites

 Requirement | 
 Description | 

 optilyz account | 
 An optilyz account is required to take advantage of this partnership. | 

 optilyz API key

<OPTILYZ_API_KEY> | 
 Your optilyz customer success manager will provide you with your optilyz API key.

This API key will enable you to connect your Braze and optilyz accounts. | 

 optilyz automation ID

<OPTILYZ_AUTOMATION_ID> | 
 The automation ID can be found in a box on the page header.

When logged into optilyz, you can navigate to the automation you want to send data into.
The automation must be activated first. | 

## Use cases

Running direct mail like a digital channel means moving away from mass mailings and leveraging the channel as part of your (digital) customer journeys. The benefits of a modern approach to direct mail are:

- Increased conversion rates via increased relevance, additional use cases, easier A/B testing, and cross-channel effects
 
- Reduced effort via automation and an end-to-end solution
 
- Reduced cost via frame contracts and cost transparency

## Integration

To integrate with optilyz, use the optilyz API to send recipient data to the Braze webhook.

### Step 1: Create your Braze webhook template

To create an optilyz webhook template to use in future campaigns or Canvases, go to Content > Webhook in the Braze platform. Then, select Create webhook template.

If you would like to create a one-off optilyz webhook campaign or use an existing template, select Webhook in Braze when creating a new campaign.

In your new Webhook template, fill out the following fields:

- Webhook URL: The Webhook URL is unique to each customer and your optilyz customer success manager will provide it to you.
 
- Request Body: Raw Text

#### Request headers and method

optilyz also requires an HTTP Header for authorization and an HTTP method. The following will already be included within the template as a key-value pair, but in the Settings tab, you must replace the <OPTILYZ_API_KEY> with your optilyz API key. This key must include a “:” directly after the key and be encoded in base 64.

- HTTP Method: POST
 
- Request Headers:

- Authorization: {{ '<OPTILYZ_API_KEY>:' | base64_encode }}
 
- Content-Type: application/json

#### Request body

In the following request body, you can use any Liquid personalization tags and build a custom request template according to optilyz’ API documentation.

The variation field is optional and can define which design inside the automation should be used. If a variation is omitted, optilyz will assign one of the defined variations randomly.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14

```
 | 
```
{
 "address": {
 "title": "{{custom_attribute.${salutation}}}",
 "firstName": "{{${first_name}}}",
 "lastName": "{{${last_name}}}",
 "street": "{{custom_attribute.${street}}}",
 "houseNumber": "{{custom_attribute.${houseNumber}}}",
 "address2": "{{custom_attribute.${address2}}}",
 "zipCode": "{{custom_attribute.${zipCode}}}",
 "city": "{{custom_attribute.${city}}}",
 "country": "{{custom_attribute.${country}}}"
 },
 "variation": {{custom_attribute.${designVariation}}}
}

```
 | 

### Step 2: Preview your request

Next, preview your request in the Preview panel or navigate to the Test tab, where you can select a random user, an existing user, or customize your own to test your webhook. Remember to save your template before leaving the page!

important

Remember to save your template before leaving the page! 
Updated webhook templates can be found in the Saved Webhook Templates list when creating a new webhook campaign.

- 

New Stuff!
