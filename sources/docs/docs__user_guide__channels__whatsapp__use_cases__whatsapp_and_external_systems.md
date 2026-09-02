---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems
slug: docs__user_guide__channels__whatsapp__use_cases__whatsapp_and_external_systems
title: "Integrate Braze and WhatsApp with an external AI or communication system"
description: "This reference article provides a step-by-step guide for integrating the Braze and WhatsApp integration with an external AI or communication system."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Integrate Braze and WhatsApp with an external AI or communication system

Leverage the power of AI chatbots and live agent hand-offs on the WhatsApp channel to streamline your customer support operations. By automating routine inquiries and seamlessly transitioning to human agents when needed, you can significantly improve response times and enhance the overall customer experience.

## Prerequisites

 Requirements | 
 Description | 

 External system | 
 A third-party AI or communication system capable of building and managing chatbots, automated client service systems using APIs, or both. | 

 Braze and WhatsApp integration | 
 A WhatsApp number managed by Braze | 

 Braze REST API Key | 
 A REST API key with campaigns.trigger.send permissions. This can be created in the Braze dashboard by going to Settings > API Keys. | 

## How it works

The integration between Braze and the external AI or communication system works as a two-way street, where Braze is the communication channel and the external system is the “intelligence” that processes messages and formulates responses.

The integration workflow can be divided into two key flows:
Inbound flow: A user’s message arrives in Braze and is then forwarded to your external system for processing.
Outbound flow: After processing the message, your external system sends a response to Braze, which then delivers the message to the end-user.

To efficiently automate this communication, this integration uses two key Braze features: webhook campaigns and API-triggered campaigns.

## Configuring the integration

### Step 1: Create a webhook campaign for inbound messages

First, create a webhook campaign to establish a way to send WhatsApp messages received by Braze to your external system.

- In Braze, create a webhook campaign.
 
- In the webhook composer, select Compose webhook.
 
- In the Webhook URL field, enter the API endpoint (URL) for the external system that will receive the message.
 
- Select Raw text for the request body and enter a payload with personalization that contains the user’s external_id and phone number, the message content, and other relevant information, such as:

```

1
2
3
4
5

```
 | 
```
{
 "user_id": "{{${user_id}}}",
 "phone_number": "{{${phone_number}}}",
 "message": "{{whats_app.${inbound_message_body}}}"
}

```
 | 

- In the Schedule Delivery step of your campaign composer, select Action-Based for the delivery type and Send a WhatsApp inbound message for the campaign trigger.

- Finish composing your campaign, then save and launch the campaign. After you launch the campaign, every time a message is received, Braze sends a webhook to your external system.

### Step 2: Create an API-triggered campaign for outbound messages

Next, create an API-triggered campaign to establish a way for your external system to send messages back to users through WhatsApp.

- In Braze, create a WhatsApp campaign.
 
- In the message composer, select either WhatsApp Template Message or Response Message, then select the template or response message layout. You can select any response message layout because the inbound message opened the 24-hour WhatsApp window.

- Add the API trigger property to the message body, such as {{api_trigger_properties.${external_system_msg+body}}}. This allows your AI system to populate the message that will be sent.

- In the Schedule Delivery step of your campaign composer, select Action-Based for the delivery type.
 
- Save the campaign, then take a note of the unique campaign_id that Braze generates for this campaign. You’ll need the ID for the next step.

### Step 3: Connect the external system to the API-triggered campaign

Lastly, configure your external system to call Braze and send the response.

- In your external system’s code, after processing the received message and generating the response, make a POST request to the Braze /messages/send endpoint.
 
- In the /messages/send request body, include the campaign_id from Step 2, the user’s external_id, and the content of the external system’s response.
 
- Use the API trigger property from Step 2 to insert the external system’s response, and don’t forget to include your API Key in the request header for authentication, such as in this cURL example:

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
15

```
 | 
```
curl -X POST \
 -H 'Content-Type:application/json' \
 -H 'Authorization: Bearer a valid rest API key' \
 -d '{
 "campaign_id": "campaign_id",
 "recipients": [
 {
 "external_user_id": "external_id",
 "trigger_properties": {
 "external_system_msg_body": "your external system message" 
 }
 }
 ]
 }' \
 {{Braze endpoint}}/campaigns/trigger/send

```
 | 

Now you have a solid foundation for building an AI chatbot workflow!

### Customizing your workflow

You can expand your integration logic to:

- Use different keywords to trigger distinct webhook campaigns.
 
- Create more complex conversation flows with multi-step API-triggered campaigns.
 
- Record chat information in Braze as custom attributes to enrich the user profile and segment future campaigns.

- 

New Stuff!
