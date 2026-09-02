---
url: https://www.braze.com/docs/partners/data_and_analytics/loyalty/openloyalty
slug: docs__partners__data_and_analytics__loyalty__openloyalty
title: "Open Loyalty"
description: "The Braze and Open Loyalty integration allows you to sync loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Open Loyalty

Open Loyalty is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user’s loyalty status changes.

This integration is maintained by Open Loyalty

## About the integration

This integration uses Braze Data Transformations to capture webhooks from Open Loyalty and map them to Braze user profiles.

- Real-time Updates: Push loyalty events (points earned, tier upgrades) to Braze.
 
- Personalization: Use loyalty attributes (current balance, next tier name) in your Braze templates.
 
- Bi-directional: Update Open Loyalty customer custom attributes based on Braze engagement data.

## Use cases

This integration covers the following data flows:

- Syncing Events to Braze (Inbound): Track point changes, tier upgrades, or reward redemptions by sending data from Open Loyalty to Braze. Data Transformation converts this data into a User Event.
 
- Modifying Open Loyalty Members (Outbound): Automatically update member data in Open Loyalty based on user behavior in Braze, such as adding “VIP” labels or updating custom attributes.

## Prerequisites

Before you start, you need the following:

 Requirement | 
 Description | 

 Open Loyalty account | 
 You need an Admin account on an Open Loyalty Tenant to take advantage of this partnership. | 

 Open Loyalty REST API Key | 
 An Open Loyalty REST API Key (for integrations that send data from Braze to Open Loyalty). 

 Create this in Settings > Admins > API Keys. | 

 Braze REST API Key | 
 A Braze REST API key with users.track permissions. 

 Create this key in the Braze dashboard from Settings > API Keys. | 

 Braze Data Transformation | 
 You need access to the “Data Settings” tab in Braze to configure webhook listeners. | 

 Matching IDs | 
 The user’s external_id in Braze must match their loyaltyCardNumber (or another default identifier) in Open Loyalty. | 

 Tenant ID | 
 Your Open Loyalty Tenant ID (required for Outbound updates). | 

## Integration

The primary integration syncs Open Loyalty webhook events to Braze using Data Transformation.

### Step 1: Generate the Webhook URL in Braze

First, create a data transformation in Braze to generate a unique URL for receiving data.

- In Braze, open Data Settings > Data Transformation.
 
- Click Create Transformation.
 
- Complete the following fields:

- Transformation name: Provide a descriptive name (for example, “Open Loyalty Point Update Events”).
 
- Select destination: Choose POST: Track users.

- Click Create Transformation.
 
- Locate the Webhook URL in the details panel and click Copy.

important

Keep this URL safe; you need it for the next step.

### Step 2: Create the Webhook Subscription in Open Loyalty

Tell Open Loyalty to send specific events to the URL you just generated.

- Log in to your Open Loyalty Admin Panel.
 
- Navigate to General > Webhooks.
 
- Click Add new webhook and configure the subscription:

- eventName: Select the event you want to track (for example, AvailablePointsAmountChanged, CustomerLevelChanged, or CampaignEffectWasApplied).
 
- url: Paste the Braze Webhook URL from Step 1.
 
- Add the following headers:

- Content-Type: application/json
 
- User-Agent: partner-OpenLoyalty

- Save the webhook subscription.

### Step 3: Configure the Data Transformation

Write the JavaScript logic in Braze to map the incoming Open Loyalty payload to Braze properties.

- In Braze, open the data transformation you created in Step 1.
 
- Trigger the event in Open Loyalty (for example, change a member’s points or assign a tier) to generate a sample payload in the Webhook details pane.
 
- In the Transformation code editor, write a script to map the incoming data. Use the following example as a guide:

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

```
 | 
```
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
 "events": [
 {
 // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
 "external_id": data.customer.loyaltyCardNumber,
 
 // Define the Event Name (what you see in Braze)
 "name": "Loyalty Event Triggered",
 
 // timestamp
 "time": new Date().toISOString(),
 
 // Map specific properties you want to use in emails/segments
 "properties": {
 "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
 "new_balance": data.amount,
 "change_amount": data.amountChange,
 "tier_name": data.tier ? data.tier.name : null
 }
 }
 ]
};

return brazecall;

```
 | 

- Click Validate to ensure the code runs against your sample payload, then click Activate.

## Using Open Loyalty with Braze

After you complete the inbound integration, configure Outbound Updates to modify Open Loyalty members based on Braze behavior.

### Step 1: Configure Braze Webhook Campaign

This process uses Braze Webhooks to send a PATCH request to the Open Loyalty Member API (for example, to add a “VIP” label).

- In Braze, create a new Webhook Campaign (or use a Webhook within a Canvas).
 
- Click Compose Webhook.
 
- Webhook URL: Construct the URL using your Open Loyalty instance, Tenant ID, and the Braze Liquid variable for the user ID.

- 
 
Format:

https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}

- Complete the following fields:

- Request Method: PATCH
 
- Request Headers:

- Content-Type: application/json
 
- X-AUTH-TOKEN: <YOUR_PERMANENT_TOKEN>
 
- User-Agent: Braze

- Request Body: Select Raw text and paste the payload:

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
 "customer": {
 "labels": [
 {
 "key": "braze_vip_segment",
 "value": "optedIn"
 }
 ]
 }
}

```
 | 

### Step 2: Configure the Trigger

- Navigate to the Delivery or Entry Schedule tab.
 
- Complete the following fields:

- Delivery Method: Action-Based.
 
- Trigger: Define the relevant trigger (for example, a user enters a specific Segment in Braze).
 
- Launch: Activate the campaign.

## Troubleshooting

### Verify Inbound Events

When the Data Transformation is active, data appears in Braze as a custom event. Verify this by creating a campaign with a Perform Custom Event trigger and checking if your defined event (for example, Loyalty Event Triggered) is available.

### Verify Outbound Webhooks

Check the Message Activity Log in Braze to ensure the webhook returned a 200 OK status.

- 401 Error: Check your Open Loyalty API Token.
 
- 404 Error: The user ID in Braze does not exist in Open Loyalty.

- 

New Stuff!
