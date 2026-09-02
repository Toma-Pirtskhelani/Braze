---
url: https://www.braze.com/docs/partners/message_orchestration/retargeting/quikly
slug: docs__partners__message_orchestration__retargeting__quikly
title: "Quikly"
description: "This reference article outlines the partnership between Braze and Quickly, a urgency marketing platform, that allows you to accelerate conversions on events within a Braze..."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Quikly

Quikly, an urgency marketing platform, uses psychology to motivate consumers, so brands can immediately increase response around their key marketing initiatives.

This integration is maintained by Quikly.

## About the integration

The Braze and Quikly partnership allows you to accelerate conversions on events within a Braze customer journey. Quikly does this by using urgency psychology to motivate consumers in fun — and instant — ways. For example, brands can use Quikly to immediately acquire new email and SMS subscribers directly into Braze or to motivate other key marketing objectives like downloading your mobile app.

## Prerequisites

 Requirement | 
 Description | 

 Quikly account | 
 A Quikly brand partner account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with users.track, subscription.status.set, users.export.ids, and subscription.status.get permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

 Quikly API key (optional) | 
 A Quikly API key provided by your client success manager (webhook only). | 

## Use cases

Quikly allows brands to accelerate email or SMS acquisition and motivates subscribers to provide first-party data directly within Braze. You can also use Braze to target lapsed customers with a Quikly activation that will reactivate and retain that audience. Additionally, marketers can use this integration to incentivize specific customer journey events with unique reward structures.

For example:

- Build anticipation and engagement over days as consumers opt-in for a chance to claim exciting rewards with Quikly Hype. First-party data is automatically pushed to Braze.
 
- Accelerate acquisition of new email and SMS subscribers using unique, real-time offers based on a consumer’s speed of response, rank against others, randomly, or before time or quantities run out with Quikly Swap.
 
- Motivate specific steps in the customer journey with unique reward structures using webhooks.
 
- Apply custom attributes or events to the user’s profile upon participating in a Quikly activation.

## Integration

This section outlines four different integrations: email acquisition, SMS acquisition, custom attributes, and webhooks. The integration you choose will depend on your Quikly activation and use case.

- email acquisition
 
- sms acquisition
 
- custom attributes
 
- webhooks

### Email Acquisition

If your Quikly activations collect customer email addresses or profile data, the only required step is to provide Quikly with your REST API key and endpoint. Quikly will configure your brand account to pass this data to Braze. If there are additional user attributes you’d like included, mention this when you provide the API credentials to Quikly.

Here is an outline of how Quikly executes this workflow.

- Upon participating in a Quikly activation, Quikly schedules a user lookup using the export API to see if a user exists with a given email_address.
 
- Log or update the user.

- If the user exists:

- Do not create a new profile.
 
- If desired, Quikly can log a custom attribute on the user’s profile to indicate that the user participated in the activation.
 - If the user does not exist:
 
- Quikly creates an alias-only profile via the Braze /users/track endpoint, setting the user’s email as the user alias to reference that user in the future (as the user won’t have an external ID).
 
- If desired, Quikly can log custom events to indicate this profile participated in Quikly activation.

/users/track request

#### Request headers

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY

```
 | 

#### Request body

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

```
 | 
```
{
 "attributes": [{
 "_update_existing_only": false,
 "user_alias:": {
 "alias_name": "[email protected]",
 "alias_label: "email"
 },
 "email": "[email protected]"
 }]
}

```
 | 

### SMS subscriptions

Quikly activations can collect mobile phone numbers directly from customers and initiate a new SMS subscription. To enable this integration, provide your Quikly client success manager with the subscription_group_id. You can access a subscription group’s subscription_group_id by navigating to the Subscription Group page.

Quikly will perform a subscription lookup using the customer’s phone number and automatically credit them in the activation if an SMS subscription already exists. Otherwise, a new subscription will be initiated, and after the subscription status is verified, the customer will be credited.

Here is the complete workflow when a customer provides their mobile number and consent via Quikly:

- Quikly performs a subscription lookup using the subscription group status to see if a given phone is subscribed to a subscription_group_id. If a subscription exists, credit the user in the Quikly activation. No further action is necessary.
 
- Quikly performs a user lookup using the Export user profile by identifier endpoint to see if a user profile exists with a given email_address. If no user exists, create an alias-only profile via the Braze /users/track endpoint, setting the user’s email as the user alias to reference that user in the future (as the user won’t have an external ID).
 
- Update the subscription status using the Update user’s subscription group status endpoint.

To support existing double opt-in SMS subscription workflows, Quikly can send a custom event to Braze rather than the standard workflow in this section. In that case, rather than updating the subscription status directly, the custom event triggers the double opt-in process and the subscription status is periodically monitored to verify the user has fully opted-in before crediting them in the Quikly activation.

important

Braze advises that when creating new users via the /users/track endpoint, there should be a delay of about 2 minutes before adding users to the relevant subscription group to allow Braze time to fully create the user profile.

Detailed /subscription/status/set request

#### Request headers

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY

```
 | 

#### Request body

```

1
2
3
4
5
6

```
 | 
```
{
 "subscription_group_id": "the-id-of-the-subscription-group",
 "subscription_status": "subscribed",
 "phone": "+13135551212"
 }]
}

```
 | 

### Custom attributes

Depending on your Braze implementation, you may want events within Quikly activation to cascade through Braze for further processing. For example, you may wish to apply a custom user attribute based on what level or incentive was achieved in Quikly activation, allowing you to display the relevant Content Card when they open your app or log in to your website. Quikly will work with you directly to implement these integrations.

### Webhooks

Use webhooks to trigger incentives for specific events in the customer journey. For example, if you have a Braze event for when a user logs into your app, turns on push notifications, or uses your store locator, you can use a webhook to trigger a custom offer to that user based on the configuration of a specific Quikly activation. Example tactics include rewarding the first X number of users who perform an action (such as logging into your app) with a custom offer or providing an offer that decreases in value as more time elapses to motivate an immediate response.

### Create a Quikly webhook in Braze

To create a Quikly webhook template for future campaigns or Canvases, navigate to Content > Webhook in the Braze platform. Then, select Create webhook template.

If you would like to create a one-off Quikly webhook campaign or use an existing template, select Webhook in Braze when creating a new campaign.

Select Blank Template, and enter the following for the webhook URL and request body:

- Webhook URL: https://api.quikly.com/webhook/braze
 
- Request body: JSON key/value pairs

#### Request headers and method

Quikly requires an HTTP Header for authorization.

- HTTP Method: POST
 
- Request Header:

- Authorization: Bearer [PARTNER_AUTHORIZATION_HEADER]
 
- Content-Type: application/json

#### Request body

Select JSON key/value pairs and add the following pairs:

```

1
2
3

```
 | 
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}

```
 | 

### Preview your request

Preview your request in the Preview panel or navigate to the Test tab, where you can select a random user, an existing user, or customize your own to test your webhook.

important

Remember to save your template before leaving the page! 
Updated webhook templates can be found in the Saved Webhook Templates list when creating a new webhook campaign.

## Support

Contact your client success manager at Quikly with any questions.

- 

New Stuff!
