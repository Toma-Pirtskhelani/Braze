---
url: https://www.braze.com/docs/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook
slug: docs__user_guide__channels__webhooks__use_case_create_a_braze_to_braze_webhook
title: "Create a Braze-to-Braze webhook"
description: "This reference article covers when to use User Update versus Braze-to-Braze webhooks and how to create a Braze-to-Braze webhook."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create a Braze-to-Braze webhook

Braze-to-Braze webhooks let you call the Braze REST API from within Braze using a Webhook in a Campaign or Canvas. Use this for orchestration tasks like triggering an API-triggered Canvas. For updating User attributes, Custom events, or Purchases from Canvas, use User Update instead. It’s designed for user profile changes and processes updates more efficiently.

To get the most out of this article, you should be familiar with how webhooks work and how to create a webhook in Braze.

## Use Send to Destination for triggering another Canvas

To trigger a second Canvas from within a Canvas, use Send to Destination instead of a Braze-to-Braze webhook. This Canvas component is designed specifically for connecting Canvas journeys and provides a simpler, more efficient way to send users from one Canvas to another.

Send to Destination evaluates users against the destination Canvas entry and audience criteria when they reach the step, without requiring webhook configuration or API keys. Users who meet the criteria enter the destination Canvas and can continue their journey in the source Canvas if additional steps follow.

tip

Add Send to Destination to your Canvas to send users to another Canvas journey without configuring webhooks or API calls.

## Use User Update for user data changes

To update user profiles from within a Canvas, including modifying Custom attributes, recording Custom events, or recording Purchases, use User Update instead of a Braze-to-Braze webhook.

User Update groups multiple changes together and sends them in batches, making it faster than webhooks. It’s easier to set up than a webhook and supports complex updates through its Advanced JSON composer. For example, to count how many times a user has seen a message, use User Update’s Increment and decrement feature rather than a Braze-to-Braze webhook.

tip

Add User Update to your Canvas to update a user’s attributes, events, and purchases using a JSON composer.

## When to use a Braze-to-Braze webhook

User Update can handle nearly all the same tasks as a Braze-to-Braze webhook for updating user profiles. For complex updates beyond simple custom attributes, you can use the Advanced JSON composer.

Send to Destination provides a simpler way to trigger a second Canvas from within Canvas without needing webhook configuration.

You can use a Braze-to-Braze webhook when you need to call Braze’s REST API from within Braze for scenarios that don’t have a dedicated Canvas component. Common examples include:

- Triggering an API-triggered Campaign from a Canvas
 
- Calling other Messaging endpoints for orchestration patterns where one workflow in Braze needs to invoke an API that doesn’t have a dedicated Canvas component

For user updates inside Canvas, use User Update. For triggering another Canvas, use Send to Destination.

## Prerequisites

To create a Braze-to-Braze webhook, you need an API key with permissions for the endpoint you want to reach. For example, to trigger an API-triggered Canvas, you need an API key with the canvas.trigger.send permission.

## Setting up your Braze-to-Braze webhook

The general workflow for creating a Braze-to-Braze webhook follows these steps:

- Create a webhook as a campaign or Canvas component.
 
- Choose Blank Template.
 
- In the Compose tab, specify the Webhook URL and Request Body for your API use case.
 
- In the Settings tab, specify your HTTP Method and Request Headers as required by the endpoint.
 
- Configure any additional delivery settings (for example, triggering from a custom event) and build out the rest of your campaign or Canvas.

## Trigger a second Canvas from an initial Canvas

In this use case, you create two Canvases and use a Braze-to-Braze webhook to trigger the second Canvas from the first. This acts like an entry trigger for when a user reaches a certain point in another Canvas.

note

The Interact with Canvas Step trigger is only available for campaigns, not for action-based Canvas entry. If you need to trigger a Canvas based on a user reaching a specific step in another Canvas, use this Braze-to-Braze webhook approach or the Send to Destination Canvas component.

- Start by creating your second Canvas—the Canvas that should be triggered by your initial Canvas.
 
- For the Canvas Entry Schedule, select API-Triggered.
 
- Make note of your Canvas ID. You need this in a later step.
 
- Continue building out the steps of your second Canvas, then save the Canvas.
 
- Finally, create your first Canvas. Find the step where you want to trigger the second Canvas and create a new step with a webhook.

Refer to the following when configuring your webhook:

- Webhook URL: Your REST endpoint URL followed by /canvas/trigger/send. For example, for the US-06 instance, the URL would be https://rest.iad-06.braze.com/canvas/trigger/send.
 
- Request Body: Raw Text

### Request headers and method

Braze requires an HTTP header for authorization that includes your API key and another that declares your content type.

- Request Headers:

- Authorization: Bearer YOUR_API_KEY
 
- Content-Type: application/json

- HTTP Method: POST

Replace YOUR_API_KEY with a Braze API key that has canvas.trigger.send permissions. You can create an API key in the Braze dashboard by going to Settings > API Keys.

#### Request body

Add your /canvas/trigger/send request in the text field. For details, see Sending Canvas messages via API-triggered delivery. The following is an example of the request body for this endpoint, where your_canvas_id is the Canvas ID from your second Canvas:

```

1
2
3
4
5
6
7
8

```
 | 
```
{
 "canvas_id": "your_canvas_id",
 "recipients": [
 {
 "external_user_id": "{{${user_id}}}"
 }
 ]
}

```
 | 

When a user reaches this webhook step in the first Canvas, Braze triggers the second Canvas for that user via the API.

## Considerations

- User updates: For updating user profiles from Canvas (attributes, events, purchases), use User Update instead of Braze-to-Braze webhooks for better efficiency and cost-effectiveness.
 
- Braze-to-Braze webhooks are subject to endpoint Rate limits.
 
- Updates to the user profile incur Data points that count toward your overall consumption, while triggering another message through the messaging endpoints does not.
 
- To target Anonymous users, use braze_id instead of external_id in the request body of your webhook.
 
- You can save your Braze-to-Braze webhook as a webhook template for reuse.
 
- You can check the Message Activity Log to view and troubleshoot webhook failures.

- 

New Stuff!
