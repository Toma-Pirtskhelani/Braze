---
url: https://www.braze.com/docs/partners/data_and_analytics/loyalty/punchh/punchh
slug: docs__partners__data_and_analytics__loyalty__punchh__punchh
title: "Punchh"
description: "This reference article outlines the partnership between Braze and Punchh, a loyalty and engagement platform, enabling you to sync data across the two platforms. Data..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Punchh

Punchh is an industry-leading loyalty and engagement platform that enables brands to deliver omnichannel customer loyalty programs both in-store and digitally.

This integration is maintained by Punchh.

## About the integration

The Braze and Punchh integration allows you to sync data for gifting and loyalty purposes across the two platforms. Data published in Braze will be available for segmentation and can sync user data back into Punchh via Braze webhooks.

## What are the benefits?

- Ingest loyalty data from Punchh to Braze in real-time.
 
- Leverage and layer powerful audience data from Braze to deliver meaningful and dynamic cross-channel experiences (app, mobile, web, email, and SMS)

- Did customers open emails? Did customers open the app near a store?

- Standardize the look and feel of transactional emails sent through Braze.
 
- Create journeys that allow for A/B testing and optimization as you go.

## Prerequisites

 Requirement | 
 Description | 

 Punchh account | 
 You need an active Punchh account to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. | 

## What else should I know?

### Before integrating

- When utilizing the Braze integration, two campaigns will be required, one in Punchh and the second in Braze. For example, if you send a campaign with an offer attached, the gifting campaign will be configured within Punchh, and the notification can be sent from Braze.
 
- Guests should already exist in Punchh and Braze. Punchh will filter out any customer who is not already a loyalty guest.

### Important things to note

- Punchh has added the ability to disable the sending of default user attributes to Braze, so the customer does not incur data point overages. This is configured during the adapter setup.
 
- If using custom segments on recurring campaigns, the campaign name must be used instead of the campaign ID, as the IDs change each time the campaign runs.
 
- Communication channels available within each Punchh gifting campaign include rich messages, push notifications, SMS, and email.
 
- After users have been sent to a Punchh custom segment from Braze, they can’t be removed. Only new guests can be added to an existing custom segment. If guests need to be removed from an existing Punchh custom segment, a new webhook campaign will need to be created in Braze to send users to a new Punchh custom segment.

## Integration

Punchh offers several endpoints available to Braze customers to help add external IDs to the Punchh platform using the following Punchh API endpoints. After the external IDs have been added, create an adapter in Punchh, provide your Braze credentials, and select which events you’d like to sync. Next, you can take the Punchh segment ID and use it to build a Punchh webhook to trigger customer syncing in a Canvas journey.

Note that the Punchh user_id and Braze external_id need to be available in either platform for the integration to sync properly. 

- Events sent from Punchh to Braze will include the Braze external_id as the identifier. If Punchh is configured to use the external_source_id, that value will be set as the Braze external_id. Otherwise, the integration will default to setting the Punchh user_id as the Braze external_id.
 
- To send webhooks from Braze to Punchh, the Punchh user_id must be available on the Braze user profile. If Punchh user_id is not used as the Braze external_id, it should be set as a custom attribute “punchh_user_id”. 

### Step 1: Set up external ID ingestion endpoints (optional)

External IDs from Braze can be added using the following endpoints for new and existing Punchh users.

important

The external_source and external_source_id field values must be unique to Punchh and not associated with existing profiles.

- New Punchh users

Create new users in Punchh with a Punchh sign-up endpoint using the external_source and external_source_id fields. Punchh allows external identifiers to be sent with a user profile via one of the following sign-up endpoints:

- Mobile Signup API
 
- SSO Signup API

- Existing Punchh users 

Update external_source_id for existing Punchh users. Punchh allows external identifiers to be added to a profile via a user API update endpoint:

- Mobile User Update
 
- SSO User Update
 
- Dashboard User Update

- user sign-up api example
 
- user update api example

This example allows you to send external identifiers with a user profile at sign-up time. This is done by sending external_source as “customer_id” and external_source_id as “111111111111111111” as a string data type.

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

```
 | 
```
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
 "client":"CLIENT",
 "user" : {
 "email": "[email protected]",
 "password": "PASSWORD",
 "first_name":"FIRST_NAME",
 "last_name":"LAST_NAME",
 "terms_and_conditions":"true",
 "anniversary":"2014-02-02",
 "zip_code":"94497",
 "birthday":"2004-02-02",
 "external_source":"customer_id",
 "external_source_id":"111111111111111111"
 }
}'

```
 | 

This example allows you to update external identifiers with a user profile. This is done by sending external_source as “customer_id” and external_source_id as “111111111111111111” as a string data type.

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

```
 | 
```
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
 "client":"CLIENT",
 "user": {
 "external_source":"customer_id",
 "external_source_id":"111111111111111111"
 }
}'

```
 | 

note

Platform configuration: To enable external identifiers in Punchh, from the Punchh dashboard, navigate to Cockpit > Dashboard > External User Identifier.

### Step 2: Braze adapter setup in Punchh

#### Available events to sync

- Guest: Triggered upon any signup, update to guest profile, deactivated or deleted
 
- Loyalty Check-in: Triggered for loyalty transactions or earning by scanning barcode from the receipt
 
- Gift Check-in: Triggered for points gifted from a campaign
 
- Redemption: Triggered in case of any reward redemption excluding Punchh coupons, as those would be sent separately as coupon events, including issuance as well as redemption
 
- Rewards: Triggered from rewards gifted from campaigns, activity, conversion from points to rewards, or admin gifting
 
- Transaction Notifications: Triggered upon transactional activity for a user within the Punchh system (for example, point expiration)
 
- Marketing Notifications: Triggered based on different campaign setups in Punchh for an associated segment of users

note

Reference Punchh documentation on what sample payloads for these available events may look like.

Work with your Punchh Implementation manager to set up this adapter.

To set up the Braze and Punchh integration, do the following:

- In the Punchh dashboard, navigate to Cockpit > Dashboard > Major Features > Enable Webhook Management and toggle on Enable Webhook Management.

- Next, enable adapters by navigating to Settings > Webhooks Manager > Configurations > Show Adapters Tab and toggle on Show Adapters Tab.

- Navigate to Webhooks Manager under the Settings tab, select the Adapters tab, and click Create Adapter. 

- Fill in the adapter name, description, and admin email. Select Braze as your adapter and provide your Braze REST API endpoint and Braze API key.

- Next, select the available events you would like to enable. A list of these events can be found in Available events to sync.

- Click Submit to enable the webhook.

## Create Punchh webhook in Braze

Braze can add users to a Punchh segment through webhooks utilizing Punchh Custom Segments.

- 
 
Create a custom segment in Punchh and note the custom_segment_id present in the Punchh segment dashboard URL as shown in the following example. Both classic or beta segment builders can be used. However, beta is recommended as classic will eventually be deprecated.

In the Punchh platform, navigate to Guest > Segment > Custom List > New Custom List.

- 
 
Create a webhook campaign in Braze using the Punchh endpoint for adding a user to a custom segment as the webhook URL. Here, you can provide the custom_segment_id pulled from the URL and user_id as key-value pairs.

- 
 
This webhook can be set up as a singular campaign or as a step within a Canvas. Alternatively, if the webhook adding users to this specific Punchh segment will be used in multiple campaigns or Canvases, it can be set up as a template.

The user_id key within the webhook maps to the Punchh user ID. This identifier will need to be added to all webhooks created in Braze to add users to a Punchh custom segment. The punch_user_id custom attribute can be dynamically populated as the value for the user_id key using Liquid. You can insert the punchh_user_id custom attribute variable using the blue “plus” icon in the templated text field toolbar.

- 
 
After the webhook is saved, it can be used to sync users. For example, 136 guests would be added to the Punch custom segment when this Braze webhook campaign is launched.

For more information on how webhooks are used at Braze, check out Create a webhook.

## Use case campaigns

### Campaign and Canvas configuration

#### Triggering

Use cases for Braze messaging triggered by Punchh events being sent to Braze, such as reward events or guest events, can be created as action-based campaigns or Canvases triggered by the relevant Punchh event.

Adding a trigger will pull up the list of events created in Braze. Choose the event that should trigger your campaign or Canvas to be sent to the user who logged the event.

Property filters can be added to further filter the triggering event. For example, the message should only be triggered when a customer triggers the “checkins_gift” event where the approved event property is true. This is an optional feature that may not be applicable to all use cases.

#### Segmentation

In many cases, Braze campaigns and Canvases being triggered by Punchh events can be set to an “All Users” audience because the segmentation of users triggering these events is determined within Punchh. However, customers looking to further refine the audience of users who will receive the Braze messaging triggered by the event can do so by adding additional filters and segments in the Target Audiences section of the campaign composer or the Entry Audience of the Canvas composer.

### Use cases

- signup
 
- braze welcome
 
- mass offer
 
- recurring mass offer
 
- post check-in offer with notification
 
- post check-in offer without notification
 
- anniversary
 
- recall

#### Sign-up campaign

When utilizing the Braze configuration for a sign-up campaign with an offer attached, a sign-up gifting campaign will need to be configured within Punchh and a welcome message in Braze.

Punchh recommends that an execution delay be added to the sign-up campaign, so Braze can first trigger the welcome message based on the guest event. If you want to send a follow-up message informing the user that they have been gifted, you can trigger this based on the reward event.

In the case of a sign-up campaign, all signed up can be used for the segment; therefore, a custom Braze segment will not be required.

Punchh configurations required:

- Campaign: Sign-up
 
- Segment: All signed up
 
- Reward: Customer choice
Events required:
 
- Reward event
 
- Guest event
Considerations:
 
- Execution delay, recommend that the guest add a 5-10-minute delay

#### Braze welcome campaign

When a new user signs up, Punchh sends Braze a Guest event that creates the user and sends a custom attribute signup_channel, which you can use to trigger the Braze welcome campaign.

To set up the Braze welcome campaign, follow these steps:

- In Braze, create an action-based campaign.
 
- For the trigger, select Change Custom Attribute Value with the custom attribute signup_channel set to Any new value.
 
- Continue creating your campaign, then send when ready!

#### Mass offer campaign

When utilizing a mass offer campaign for gifting, a mass offer campaign will need to be configured within Punchh and a messaging campaign in Braze.

If you want to use a Braze segment for your campaign or send communication from Braze before gifting guests in the Punchh platform, then a custom Punchh segment will be required for the Punchh gifting campaign.

Creating the segment of users to receive this offer in Braze is only recommended when using attributes unavailable within Punchh. Otherwise, Punchh segmentation can be used, and the Braze messaging campaign will be created as an action-based campaign triggered by the users receiving their reward (the reward event triggered by Punchh).

Punchh configurations required:

- Campaign: Mass offer
 
- Segment: Custom list or customer choice
 
- Reward: Customer choice

Using Punchh for segmentation and gifting, and Braze for messaging:

For example, a $2 off reward is sent to a segment configurable within Punchh with messaging sent through Braze.

Using Braze segmentation and messaging, and Punchh for gifting:

For example, a $2 off reward and messaging sent to a segment with attributes not available in Punchh.

Using Braze segmentation and Punchh for gifting or messaging, or both:

For example, a $2 off reward is sent to a segment with attributes not available in Punchh, but no messaging is required, or the messaging can be sent through Punchh (note that all guests must be present in Punchh).

#### Recurring mass offer campaign

When utilizing a recurring mass offer campaign for gifting, a mass offer campaign will need to be configured within Punchh and a messaging campaign set up in Braze. A Punchh custom segment will be required if the customer wants to use Braze segmentation (only recommended if utilizing attributes unavailable within Punchh). Otherwise, Punchh segmentation can be used, and the Braze messaging campaign will be triggered based on the reward event.

Punchh configurations required:

- Campaign: Recurring mass offer
 
- Segment: Custom list or customer choice
 
- Reward: Customer choice
Considerations:
 
- Campaign IDs and campaign names are sent to Braze as an event property on the event. If you want to use a Punchh campaign identifier in Braze to further filter the audience receiving the campaign, you must use the campaign name because the campaign IDs change daily.

#### Post check-in offer campaign with notification

When utilizing a post check-in offer campaign, Braze will send the notification regarding the gifting, and when the guest makes a check-in, they will then be gifted from the Punchh post check-in campaign. Therefore, a post check-in offer campaign will need to be configured within Punchh and a messaging campaign in Braze (if notifying the customers of the campaign).

Punchh configurations required:

- Campaign: Post check-in offer
 
- Segment: Custom list
 
- Reward: Customer choice

For example, an email notifying guests to visit this weekend for double points to a segment with attributes not available in Punchh. Punchh will gift this segment points after a qualifying check-in and optional messaging from Braze.

#### Post check-in offer campaign without notification

When utilizing a post check-in offer campaign that does not first notify customers, the campaign will gift (optional messaging) and trigger any notification within Braze. Therefore, a post check-in offer campaign must be configured within Punchh; however, a custom list is not required. Instead, you can choose the segment you would like within Punchh.

Punchh configurations required:

- Campaign: Post check-in offer
 
- Segment: Customer choice
 
- Reward: Customer choice

For example, a surprise and delight Braze campaign is sent to a segment available in Punchh, thanking guests for visiting and rewarding them with $2 off their next visit.

#### Anniversary campaign

When utilizing an anniversary campaign, a user will first be gifted for their anniversary from the Punchh campaign. This gifting (reward event) will trigger the messaging campaign within Braze that notifies the user of the gifting. Therefore, a custom list is not required. Instead, you can choose the segment and anniversary setting within Punchh.

Punchh configurations required:

- Campaign: Anniversary campaign
 
- Segment: Customer choice
 
- Reward: Customer choice
Considerations:
 
- Gifting month of sign-up
 
- Lifespan duration (How long is the birthday reward valid?)
 
- Recurring campaigns, schedule required

#### Recall campaign

When targeting users based on inactivity, a recall campaign can be used. The customer can create the segment and campaign within Punchh but use Braze for messaging.

If you want to use segmentation created in Braze, a custom Punchh segment based on inactivity can be attached to a recurring mass offer campaign.

Punchh configurations required:

- Campaign: Recall campaign
 
- Segment: Customer choice
 
- Reward: Customer choice
Considerations:
 
- Campaign runs on a schedule

- 

New Stuff!
