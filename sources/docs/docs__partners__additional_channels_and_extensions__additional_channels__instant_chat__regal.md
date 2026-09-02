---
url: https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/instant_chat/regal
slug: docs__partners__additional_channels_and_extensions__additional_channels__instant_chat__regal
title: "Regal"
description: "This reference article outlines the partnership between Braze and Regal, a Voice AI agent platform that helps you orchestrate personalized, omnichannel customer journeys using Braze..."
section: partners/additional_channels_and_extensions
fetched: 2026-09-02
evidence: company-own (technical)
---
# Regal

Regal.io is a Voice AI agent platform that helps enterprises drive better customer experiences through intelligent, real-time conversations across channels.

This integration is maintained by Regal.

By integrating Regal with Braze, you can unify behavioral data and conversational AI to orchestrate personalized, omnichannel customer journeys. Braze captures signals across the customer lifecycle, which Regal uses to power AI agent conversations, routing, and real-time decisions.

Use Braze data to shape what your AI agents say, how they respond, and when to engage. Send conversation outcomes and insights back to Braze to improve targeting and lifecycle marketing. Trigger AI-powered calls and SMS at key moments in the customer journey, and follow up in Braze based on what happens in each conversation.

## Prerequisites

 Requirement | 
 Description | 

 Regal account | 
 A Regal account is required to take advantage of this partnership. | 

 Regal API key | 
 A Regal API key allows you to send events from Braze to Regal.

Email [email protected] to get this key. | 

 Braze Data Transformation | 
 A Data Transformation is required to receive data from Regal. | 

## Integration: Sending data from Braze to Regal

Use Braze Canvas or campaign webhooks to send customer profile and event data from Braze to Regal.

### Step 1: Create new contacts in Regal

Create a Canvas or campaign that sends webhooks to Regal whenever you create a new Braze profile that should be available for calls and texts in Regal.

- 
 
Create a Canvas or campaign titled “Create New Contact for Regal” and select Action-Based as the entry type.

- 
 
Set the trigger logic to Custom Event, then select the event that fires when a profile with a phone number is created. Regal also recommends adding a filter to confirm the phone field is set.

- 
 
In your new webhook template, fill out the following fields:

- Webhook URL: https://events.regalvoice.com/events
 
- Request Body: Raw Text

#### Request headers and method

Regal also requires an HTTP header for authorization and an HTTP method. The following are included in the template as key-value pairs in the Settings tab:

- HTTP Method: POST
 
- Request Headers:

- Authorization: {{<REGAL_API_KEY>}}
 
- Content-Type: application/json

#### Request body

The only required identifier is a phone number inside traits.phones. Use the traits.phones object to associate one or more phone numbers with a contact. Each phone number can store its own label, primary designation, and voice and SMS opt-in status. This structure is especially useful when a contact has multiple phone numbers.

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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49

```
 | 
```
{
 "userId": "<uniqueIdentifier>",
 "traits": {
 "phones": {
 "<primaryPhoneNumber>": {
 "label": "Mobile",
 "isPrimary": true,
 "voiceOptIn": {
 "subscribed": true,
 "ip": "<ipAddress>",
 "source": "<leadSource>",
 "text": "<voiceOptInText>",
 "timestamp": "<timestamp>"
 },
 "smsOptIn": {
 "subscribed": true,
 "ip": "<ipAddress>",
 "source": "<leadSource>",
 "text": "<smsOptInText>",
 "timestamp": "<timestamp>"
 }
 },
 "<secondaryPhoneNumber>": {
 "label": "Home",
 "isPrimary": false,
 "voiceOptIn": {
 "subscribed": false,
 "ip": "<ipAddress>",
 "source": "<leadSource>",
 "text": "<voiceOptInText>",
 "timestamp": "<timestamp>"
 },
 "smsOptIn": {
 "subscribed": false,
 "ip": "<ipAddress>",
 "source": "<leadSource>",
 "text": "<smsOptInText>",
 "timestamp": "<timestamp>"
 }
 }
 },
 "email": "<email>",
 "firstName": "<firstName>",
 "lastName": "<lastName>",
 "custom1": "<custom1>",
 "custom2": "<custom2>"
 },
 "eventSource": "braze"
}

```
 | 

This payload example assumes the listed phone numbers include current voice and SMS consent status. If that’s not true, you can omit voiceOptIn and smsOptIn when creating the contact and set up a separate Canvas or campaign to update consent on the relevant phone number when opt-in is collected.

### Step 2: Update opt-in information

If opt-in and opt-out can occur at different points in your app, update Regal when users change their subscription status.

Regal recommends using the traits.phones schema so you can manage opt-in and opt-out per phone number, rather than at the contact level.

Use the following Canvas setup to send up-to-date opt-in information to Regal.

- 
 
Create a new Canvas or campaign titled “Send Opt In or Out to Regal”.

- Select one of the following trigger options, then select the field that represents the user’s opt-in status:

- User Profile Field Updated
 
- Update Subscription Group Status
 
- Subscription Status

- In your new webhook template, fill out the following fields:

- Webhook URL: https://events.regalvoice.com/events
 
- Request Body: Raw Text

#### Request headers and method

Regal also requires an HTTP header for authorization and an HTTP method. The following are included in the template as key-value pairs in the Settings tab:

- HTTP Method: POST
 
- Request Headers:

- Authorization: {{<REGAL_API_KEY>}}
 
- Content-Type: application/json

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24

```
 | 
```
{
 "userId": "<uniqueIdentifier>",
 "traits": {
 "phones": {
 "<phoneNumber>": {
 "voiceOptIn": {
 "subscribed": "<voice_optin_subscribed>",
 "ip": "<ipAddress>",
 "source": "<optInSource>",
 "text": "<voiceOptInText>",
 "timestamp": "<timestamp>"
 },
 "smsOptIn": {
 "subscribed": "<sms_optin_subscribed>",
 "ip": "<ipAddress>",
 "source": "<optInSource>",
 "text": "<smsOptInText>",
 "timestamp": "<timestamp>"
 }
 }
 }
 },
 "eventSource": "braze"
}

```
 | 

You can also include additional user profile attributes in this payload to keep other attributes up to date at the same time.

### Step 3: Send custom events

Set up a Canvas or campaign for each key event you want to send to Regal.

These events do more than trigger outreach (for example, a confirmation text when a lead completes sign-up). They provide the real-time context that powers how Regal AI agents speak, make decisions, and route conversations throughout the customer journey. By sending event data and attributes from Braze, you enable AI agents to adapt conversations based on each user’s behavior, preferences, and lifecycle stage.

For example, Braze events and attributes can be used in Regal to:

- Personalize AI agent speech: Reference recent behavior or product interest directly in conversations.

- Example: If a user explored life insurance options, the agent can reference contact.firstName and contact.brazeProductInterest in the conversation.

- Drive dynamic conversation logic: Adjust what the agent prioritizes in real time.

- Example: If contact.brazeAge is greater than 65, prioritize Medicare coverage; otherwise, focus on ACA plans and current insurance status.

- Enable intelligent routing and escalation: Route conversations based on value or intent.

- Example: If contact.brazeLeadTier is “High Value”, transfer to a senior agent after qualification; otherwise, continue with the AI agent.

- Align messaging and offers: Tailor what the agent presents based on campaign context.

- Example: If contact.brazeCampaignName is “Spring Mortgage Promo”, highlight the promotional offer during the conversation.

Create a new Canvas or campaign titled “Send Product Interest Event to Regal.”

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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59

```
 | 
```
{
 "userId": "<uniqueIdentifier>",
 "traits": {
 "phones": {
 "<primaryPhoneNumber>": {
 "label": "Mobile",
 "isPrimary": true,
 "voiceOptIn": {
 "subscribed": true,
 "ip": "<ipAddress>",
 "source": "<optInSource>",
 "text": "<voiceOptInText>",
 "timestamp": "<timestamp>"
 },
 "smsOptIn": {
 "subscribed": true,
 "ip": "<ipAddress>",
 "source": "<optInSource>",
 "text": "<smsOptInText>",
 "timestamp": "<timestamp>"
 }
 },
 "<secondaryPhoneNumber>": {
 "label": "Home",
 "isPrimary": false,
 "voiceOptIn": {
 "subscribed": false,
 "ip": "<ipAddress>",
 "source": "<optInSource>",
 "text": "<voiceOptInText>",
 "timestamp": "<timestamp>"
 },
 "smsOptIn": {
 "subscribed": false,
 "ip": "<ipAddress>",
 "source": "<optInSource>",
 "text": "<smsOptInText>",
 "timestamp": "<timestamp>"
 }
 }
 },
 "email": "<email>",
 "firstName": "<firstName>",
 "lastName": "<lastName>",
 "brazeProductInterest": "Life Insurance",
 "brazeAge": 68,
 "brazeLeadTier": "High Value",
 "brazeCampaignName": "Spring Insurance Promo"
 },
 "name": "Product Interest Captured",
 "properties": {
 "action": "Viewed Product Comparison",
 "productCategory": "Life Insurance",
 "intentScore": "High",
 "lastPage": "Compare Life Insurance Plans",
 "readyToCommit": true
 },
 "eventSource": "braze"
}

```
 | 

#### Up-to-date contact attributes

Regal also recommends sending key user profile attributes on event payloads so Regal has up-to-date contact attributes when key events occur.

note

If you have questions about which events to send to Regal or how to set up these Canvases and campaigns, email [email protected].

## Integration: Sending data from Regal to Braze

Use Regal Reporting Webhooks and Braze Data Transformation to send Regal reporting events (such as SMS.sent and call.completed) to Braze. After you map these events, they appear on user profiles and are available for segmentation, Canvas, and campaigns.

### Step 1: Create a Data Transformation in Braze

Create one Data Transformation for each Regal webhook you plan to send to Braze.

To create a Data Transformation:

- Navigate to the Transformations page in your Braze dashboard.
 
- Give your transformation a name and click Create transformation.
 
- From the list of transformations, select View actions and select Copy webhook URL.

### Step 2: Enable reporting webhooks in Regal

To set up reporting webhooks:

- 
 
Go to the Regal app and open the Settings page.

- 
 
In the Reporting Webhooks section, click Create Webhooks.

- 
 
In the webhook endpoint input, add the Braze Data Transformation webhook URL for the associated Data Transformation.

#### Updating an endpoint

When you edit an endpoint, it can take up to 5 minutes for the cache to refresh and send events to your new endpoint instead.

#### Retries

Currently, Regal does not retry these events. If Braze does not respond within 5 seconds, Regal drops the event. Regal plans to add retries in a future release.

#### Events

For the complete list of reporting events, property definitions, and sample payloads, see Regal’s Reporting Webhooks guide.

### Step 3: Transform Regal events into Braze events

The Braze Data Transformation feature allows you to map incoming Regal events into the format necessary to be added as attributes, events, or purchases in Braze.

- 
 
Name your Data Transformation. It is recommended to set up a Data Transformation per event webhook.

- 
 
To test the connection, create an outbound call from the Regal Agent Desktop to your phone and submit the Conversation Summary form to create a call.completed event.

- 
 
Determine what identifiers you will use to map your Regal contacts to your Braze profiles. The available identifiers in Regal events include:

- userId - only set on events if you’ve previously sent this identifier for a contact
 
- traits.phone
 
- traits.email - only set on events if you’ve previously sent this identifier for a contact

In Braze-to-Regal event payloads, Regal recommends using traits.phones to support multiple phone numbers and phone-level consent. In Regal reporting events sent back to Braze, traits.phone may still appear as an identifier in event payloads.

#### Braze-supported identifiers

- Braze does not support phone numbers as an identifier. To use this as an identifier, the phone number can be set as a user alias in Braze.
 
- When using Braze Data Transformation, email address can be used as an identifier. If the email address exists as a profile within Braze, the existing profile will be updated. If the email address does not yet exist within Braze, an email-only profile will be created.

## Use cases

- trigger an email
 
- update profile attributes
 
- keep your experiments in sync
 
- unsubscribe a contact
 
- trigger follow-up from call analysis
 
- store call transcript links

Trigger an email from Braze based on a call disposition in Regal

The following sample payload shows a call.completed event in Regal.

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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35

```
 | 
```
{
 "userId": "123",
 "traits": {
 "phone": "+15555550123",
 "email": "[email protected]"
 },
 "name": "call.completed",
 "properties": {
 "agent_firstname": "Alex",
 "agent_fullname": "Alex Lee",
 "agent_id": "[email protected]",
 "direction": "OUTBOUND",
 "regal_voice_phone": "+15555550200",
 "regal_voice_phone_internal_name": "Sales Line",
 "contact_phone": "+15555550123",
 "call_id": "WTxxxxx9",
 "type": "Outbound Call",
 "disposition": "Converted During Convo",
 "notes": null,
 "objections": null,
 "campaign_name": "Life Insurance Quote Follow Up",
 "campaign_friendly_id": "445",
 "started_at": 1657855046,
 "ended_at": 1657855053,
 "completed_at": 1657855059,
 "talk_time": 7,
 "wrapup_time": 6,
 "handle_time": 13,
 "journey_uuid": null,
 "journey_name": null,
 "journey_friendly_id": null
 },
 "originalTimestamp": "1657855059",
 "eventSource": "Regal Voice"
}

```
 | 

The following sample Data Transformation maps this to a custom event in Braze.

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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48

```
 | 
```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
 {
 "external_id": payload.userId,
 "name": "Call Completed",
 "time": isoString,
 "_update_existing_only": false,
 "properties": {
 "agent_firstname": payload.properties.agent_firstname,
 "agent_fullname": payload.properties.agent_fullname,
 "agent_id": payload.properties.agent_id,
 "direction": payload.properties.direction,
 "regal_voice_phone": payload.properties.regal_voice_phone,
 "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
 "contact_phone": payload.properties.contact_phone,
 "call_id": payload.properties.call_id,
 "type": payload.properties.type,
 "disposition": payload.properties.disposition,
 "notes": payload.properties.notes,
 "objections": payload.properties.objections,
 "campaign_name": payload.properties.campaign_name,
 "campaign_friendly_id": payload.properties.campaign_friendly_id,
 "started_at": payload.properties.started_at,
 "ended_at": payload.properties.ended_at,
 "completed_at": payload.properties.completed_at,
 "talk_time": payload.properties.talk_time,
 "wrapup_time": payload.properties.wrapup_time,
 "handle_time": payload.properties.handle_time,
 "journey_uuid": payload.properties.journey_uuid,
 "journey_name": payload.properties.journey_name,
 "journey_friendly_id": payload.properties.journey_friendly_id
 }
 }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
 | 

Update profile attributes in Braze based on contact.attribute.edited events from Regal

The following sample payload shows a contact.attribute.edited event in Regal. Regal sends this event when an agent updates an attribute on a contact’s profile during a conversation.

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
16
17
18
19
20
21
22
23

```
 | 
```
{
 "userId": "123",
 "traits": {
 "phone": "+15555550123",
 "email": "[email protected]"
 },
 "name": "contact.attribute.edited",
 "properties": {
 "agent_email": "[email protected]",
 "contact_phone": "+15555550123",
 "changes": {
 "custom_properties": {
 "annual_income": {
 "old_value": "150,000",
 "new_value": "300,000"
 }
 }
 },
 "created_at": "1657855462"
 },
 "originalTimestamp": "1657855462",
 "eventSource": "Regal Voice"
}

```
 | 

The following sample Data Transformation maps the new custom property values to the relevant attributes on your Braze profiles:

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
16
17
18
19
20
21
22
23
24
25
26

```
 | 
```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
 {
 "external_id": payload.userId,
 "_update_existing_only": false,
 ...attributes
 }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
 | 

Keep your experiments in Braze and Regal in sync using contact.experiment.assigned events

The following sample payload shows a contact.experiment.assigned event in Regal.

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
16
17
18

```
 | 
```
{
 "userId": "123",
 "traits": {
 "phone": "+15555550123",
 "email": "[email protected]"
 },
 "name": "contact.experiment.assigned",
 "properties": {
 "experiment_name": "Post Call Offer Test",
 "experiment_id": "xxxx-xxxx-xxxx-xxxx",
 "experiment_variant": "Aggressive Offer - 50%",
 "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
 "journey_friendly_id": 220,
 "journey_name": "Post Call Follow Up"
 },
 "originalTimestamp": "1657855118",
 "eventSource": "Regal Voice"
}

```
 | 

The following sample Data Transformation maps this to a custom event in Braze.

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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

```
 | 
```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
 {
 "external_id": payload.userId,
 "_update_existing_only": false,
 "name": "Contact Experiment Assigned",
 "time": isoString,
 "properties": {
 "experiment_name": payload.properties.experiment_name,
 "experiment_id": payload.properties.experiment_id,
 "experiment_variant": payload.properties.experiment_variant,
 "journey_uuid": payload.properties.journey_uuid,
 "journey_friendly_id": payload.properties.journey_friendly_id,
 "journey_name": payload.properties.journey_name
 }
 }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
 | 

Unsubscribe a contact in Braze based on contact.unsubscribed events from Regal

The following sample payload shows a contact.unsubscribed event in Regal.

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
16
17
18
19

```
 | 
```
{
 "userId": "123",
 "traits": {
 "phone": "+15555550123",
 "email": "[email protected]",
 "ip": "78.97.213.166"
 },
 "name": "contact.unsubscribed",
 "properties": {
 "new_subscription": true,
 "channel": "voice",
 "text": null,
 "ip": "207.38.149.143",
 "source": "regalvoice.agent_desktop",
 "timestamp": "1657855229"
 },
 "originalTimestamp": "1657855230",
 "eventSource": "Regal Voice"
}

```
 | 

The following sample Data Transformation unsubscribes the contact in Braze.

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
16
17
18
19
20

```
 | 
```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
 {
 "external_id": payload.userId,
 "_update_existing_only": true,
 "subscription_groups" : [{
 "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
 "subscription_state": "unsubscribed"
 }]
 }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
 | 

Trigger tailored follow-up journeys in Braze based on call.analysis.available events from Regal

Use Regal’s call.analysis.available event to identify the main reason a customer did not convert and trigger a tailored follow-up journey in Braze.

For example:

- When the primary objection is price, send a value-oriented follow-up email.
 
- When the primary objection is timing, place the user into a nurture sequence for later reconsideration.
 
- When the primary objection is trust, send testimonials, ratings, or compliance reassurance.
 
- When needs_human_agent is true, notify a sales or support team and suppress further automated messaging.

The following sample payload shows a call.analysis.available event in Regal.

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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46

```
 | 
```
{
 "traits": {
 "phone": "+1XXXXXXXXXX",
 "email": "[email protected]"
 },
 "name": "call.analysis.available",
 "brand": "circle-bank",
 "contact_email": "[email protected]",
 "contact_phone": "+1XXXXXXXXXX",
 "created_at": "1754079836",
 "entity_type": "event",
 "event_id": "9f5d8dbb2973b0e2359c6fd34111111",
 "event_type": "regal_voice_event",
 "external_id": "41dd1aa2-1111-f011-a2d5-00505611111",
 "original_timestamp": "1754079835",
 "profile_id": "62653af1111111173af128291e92",
 "properties": {
 "agent_email": "[email protected]",
 "call_analysis": {
 "purchase_intent": "medium",
 "primary_objection": "price",
 "secondary_objection": "needs_to_compare",
 "product_interest": "Life Insurance",
 "follow_up_required": true,
 "follow_up_email_text": "Thanks for speaking with us today. I know cost is top of mind, so I wanted to send over a simple summary of the life insurance options we discussed and what may fit your budget.",
 "recommended_next_action": "send_value_oriented_follow_up",
 "needs_human_agent": false,
 "customer_sentiment_label": "interested_but_hesitant"
 },
 "contact_phone": "+1XXXXXXXXXX",
 "incoming_sip_headers": {
 "Via": "SIP/2.0/UDP srv1.example.com;branch=z9hG4bK776asdhds",
 "From": "<sip:[email protected]>;tag=1928301774",
 "Call-ID": "a84b4c76e66710"
 },
 "is_ai_agent": true,
 "outgoing_sip_headers": {
 "Via": "SIP/2.0/TCP srv2.example.com;branch=z9hG4bKgsdh7723",
 "To": "<sip:[email protected]>",
 "User-Agent": "RegalVoiceAI/1.0"
 },
 "task_id": "WT7f3ea47fa6e6055aa847f0a62111111"
 },
 "originalTimestamp": "1754079835",
 "source": "Regal Voice"
}

```
 | 

Use a Data Transformation to map call_analysis fields (such as primary_objection and needs_human_agent) to Braze custom events or profile attributes. Then build Canvas or campaign logic in Braze that branches on those values.

Update profile attributes with transcript links from call.transcript.available events

Use the call.transcript.available event to send a link to the full call transcript to Braze. Map the transcript URL to a Braze user profile attribute with Data Transformation so your team can access and review conversations from the user profile.

The following sample payload shows a call.transcript.available event in Regal.

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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44

```
 | 
```
{
 "userId": "123",
 "traits": {
 "phone": "+15555550123",
 "email": "[email protected]"
 },
 "name": "call.transcript.available",
 "properties": {
 "agent_email": "[email protected]",
 "task_id": "WT953358e8822dd9333fc38dfbac25e1e1",
 "call_summary": "The agent Yuri explained insurance options to Alex and he said he'll need to think about it before moving forward Agent politely ended the call.",
 "contact_name": "Alex Smith",
 "contact_phone": "+15555550123",
 "is_voicemail": false,
 "moments_count": 18,
 "recording_id": "RE0118052841b7299d0630d1dff610c1fb",
 "recording_link": "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Recordings/xxx.mp3",
 "recording_duration": 78.75987,
 "request_timestamp": 1657799128,
 "response_timestamp": 1657799136,
 "sentiments": {
 "contact_sentiment": 70,
 "agent_sentiment": 75,
 "agent_sentiment_reason": "Yuri was polite and attentive, effectively gathering information and providing a resource, which contributed to a positive interaction.",
 "contact_sentiment_reason": "Alex was satisfied with the information provided but may have wanted more assistance regarding insurance options."
 },
 "trackers": [
 {
 "tracker_id": "4be87957-9140-4451-894a-bdbaed1f2460",
 "tracker_name": "Refinance"
 },
 {
 "tracker_id": "eb2577c6-5e23-4c65-9e04-5cc5d49eee7e",
 "tracker_name": "High Intent"
 }
 ],
 "transcript": "[handling agent]: Hi Alex, this is Yuri with BrightCover Insurance. I'll be going over some insurance options with you today. [contact]: Sounds good. [handling agent]: Before we start, I'm going to transfer you to a specialist for a moment. One sec. [transfer agent]: Hi Alex, this is Lee. Just verifying a few details before sending you back to Yuri. [contact]: Okay. [handling agent]: Thanks, Alex. Based on what you shared, here are some plan options... [contact]: I'll need to think about it. [handling agent]: Totally understandable. Feel free to reach out anytime. Have a great day! END OF TRANSCRIPT",
 "transcript_is_truncated": false,
 "transcript_url": "https://app.regalvoice.com/transcripts/WT953358e8822dd9333fc38dfbac25e1e1"
 },
 "originalTimestamp": "1657843308",
 "eventSource": "Regal Voice",
 "eventId": "f49a3cf9cb1336683bd5f19dwe4c61147"
}

```
 | 

- 

New Stuff!
