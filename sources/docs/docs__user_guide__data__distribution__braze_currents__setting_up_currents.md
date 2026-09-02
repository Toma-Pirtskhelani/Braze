---
url: https://www.braze.com/docs/user_guide/data/distribution/braze_currents/setting_up_currents
slug: docs__user_guide__data__distribution__braze_currents__setting_up_currents
title: "Set up Currents"
description: "This how-to article walks you through the process for integrating and configuring Braze Currents."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Set up Currents

This page outlines and describes the generic process for integrating and configuring Braze Currents.

important

Currents are included with certain Braze packages. Contact your Braze representative if you have any questions or want to gain access.

## Troubleshooting

### Cannot add a new Currents integration

If you see “You do not have any remaining Currents integrations” when adding a new integration, or if the button to add a new Currents connector is greyed out, common causes are:

- No Currents entitlement has been purchased for this workspace.
 
- The Currents entitlement is available in a different workspace in your company.

To resolve this, check other workspaces within your company. A different workspace may show an available Currents entitlement. If you need to request an entitlement or adjust your configuration, contact your Braze account manager.

### Cannot enable additional event tracking

If you can create or edit a connector but can’t enable one of the optional tracking switches, your workspace may have reached an entitlement limit for that event category.

- Track Customer Behavior and User Events requires available Customer Behavior Events entitlements.
 
- Track user profiles and attributes requires available User Profiles and Attributes entitlements.

If you need additional entitlements or help adjusting your configuration, contact your Braze account manager.

## Requirements

Using Currents with any of our partners requires the same basic parameters and connection methodology.

Each partner requires that Braze has permission to write and send data files to them, and Braze asks for the location they should write those files to, specifically bucket names or keys.

The following requirements are the basic, minimum requirements to integrate with most of our partners. Some partners will require additional parameters, which are listed in their respective partner documentation along with any nuances associated with these basic requirements.

 Requirement | 
 Origin | 
 Access | 
 Description | 

 Account with partner | 
 Arrange account with that partner or contact your Braze account manager for suggestions. | 
 Check that partner’s site or contact that partner to sign up. | 
 Braze will not send data to a partner if you don’t have access to that data through your company’s account. | 

 Partner API Key or Token | 
 Usually the partner’s dashboard. | 
 Copy and paste it into the designated Braze field. | 
 Braze has a designated field for this in the integrations page for that partner. We need this to map where we send your data. Keep your Partner Keys or Tokens up to date; invalid credentials may disable your connector and drop events. | 

 Authentication Code/Key, Secret Key, Certification File | 
 Contact a representative for your account with that partner. May also exist in the partner’s dashboard. | 
 Copy and paste keys into the designated Braze field. Generate and upload .json or other certification files into the appropriate place in Braze. | 
 Braze has a designated field for this in the integrations page for that partner. This gives Braze credentials and authorizes us to write files to your partner account. It’s important to keep your authentication details up to date; invalid credentials may result in disabling your connector, and dropping events. | 

 Bucket, Folder Path | 
 Some partners organize and sort data by buckets. This should be found in the partner’s dashboard. | 
 If this is required, copy the bucket name or file path exactly into the designated space in Braze. | 
 Though this is required for some partners, it’s important to get right when you do need it. | 

important

It’s important to keep your Partner Keys, Partner Tokens, and authentication details updated; if your connector’s credentials expire, the connector will stop sending events. If this persists for more than 5 days, the connector’s events will be dropped and data will be permanently lost.

## Setting up Currents

### Step 1: Choose your partner

Braze Currents allows you to integrate through Data Storage using flat files or to our behavioral analytics and customer data partners using a batched JSON payloads to a designated endpoint.

Before you begin your integration, it’s best to decide which integration is best for your purposes. For example, if you already use mParticle and Segment and would like Braze data to stream there, it would be best to use a batched JSON payload. If you would prefer to manipulate the data on your own or have a more complex system of data analysis, it might be best to use Data Storage (Braze uses this method!)

### Step 2: Open Currents

To get started, go to Partner Integrations > Currents. You’ll be taken to the Currents integration management page.

### Step 3: Add your partner

Add a partner, sometimes called a “Currents connector,” by selecting the dropdown at the top of the screen.

Each partner requires a different set of configuration steps. To enable each integration, refer to our list of available partners and follow the instructions on their respective pages.

Provide a contact email for integration error notifications. Braze sends notifications to this address if the integration encounters errors, such as credential issues or connectivity problems. To help ensure the right people receive alerts, use a distribution list or group email address.

### Step 4: Configure your events

Choose the events you wish to pass to that partner by checking from the available options. You can find listings of these events in our Customer Behavior Events and Message Engagement Events libraries.

If needed, you can learn more about our events in our event delivery semantics article.

### Step 5: Set up field transformations

You can use Currents field transformations to remove or hash a string field.

- Remove: Replaces the string field with [REDACTED]. This is helpful if your partner rejects events with missing or empty fields.
 
- Hash: Applies an SHA-256 hashing algorithm to the string field.

Selecting a field for one of these transformations will apply that transformation to all events in which that field appears. For example, selecting email_address for hashing will hash the email_address field in Email Send, Email Open, Email Bounce, and Subscription Group State Change events.

### Step 6: Test your integration

important

Currents will drop events with excessively large payloads of greater than 900 KB.

Before you test, consider checking out our sample Currents data in GitHub. When you’re ready to test, you choose an option in the following section:

#### Sending test events

To test your integration, you can select Send Test Events to send one event from each of your selected event types to this Current. For detailed information about each event type, refer to our Customer Behavior Events and Message Engagement Events libraries.

#### Testing Currents connectors

Test Currents connectors are free versions of our existing connectors that can be used for testing and trying out different destinations. Test Currents have:

- Up to 10 Test Currents connectors per workspace.
 
- An aggregate maximum of 1,500 events per fixed 24-hour period, resetting at midnight UTC. This event total is updated hourly on the dashboard.

After your Test Currents connectors reach the sending limit, your connector will not send events until the next day (at midnight UTC).

To upgrade your Test Currents connector, edit the integration in the dashboard and select Upgrade Test Integration.

## Updating Currents

To update your Currents connector after launching, do the following:

- In Braze, navigate to Partner Integrations > Data Export.
 
- Locate and your Currents connector in the list.
 
- Select  Edit.
 
- Make your changes.
 
- Select Update Current.

This will not stop your existing export and will begin sending events according to your new selection.

note

It may take some time for your changes to take effect.

## IP allowlisting

Braze will send Currents data from the listed IPs:

- united states (us)
 
- european union (eu)
 
- australia (au)
 
- indonesia (id)
 
- japan (jp)
 
- south korea (kr)

For instances US-01, US-02, US-03, US-04, US-05, US-06, US-07, these are the relevant IP addresses:

- 23.21.118.191
 
- 34.206.23.173
 
- 50.16.249.9
 
- 52.4.160.214
 
- 54.87.8.34
 
- 54.156.35.251
 
- 52.54.89.238
 
- 18.205.178.15

For instance US-08, these are the relevant IP addresses:

- 52.151.246.51
 
- 52.170.163.182
 
- 40.76.166.157
 
- 40.76.166.170
 
- 40.76.166.167
 
- 40.76.166.161
 
- 40.76.166.156
 
- 40.76.166.166
 
- 40.76.166.160
 
- 40.88.51.74
 
- 52.154.67.17
 
- 40.76.166.80
 
- 40.76.166.84
 
- 40.76.166.85
 
- 40.76.166.81
 
- 40.76.166.71
 
- 40.76.166.144
 
- 40.76.166.145

For instance US-10, these are the relevant IP addresses:

- 100.25.232.164
 
- 35.168.86.179
 
- 52.7.44.117
 
- 3.92.153.18
 
- 35.172.3.129
 
- 50.19.162.19

For instances EU-01 and EU-02, these are the relevant IP addresses:

- 52.58.142.242
 
- 52.29.193.121
 
- 35.158.29.228
 
- 18.157.135.97
 
- 3.123.166.46
 
- 3.64.27.36
 
- 3.65.88.25
 
- 3.68.144.188
 
- 3.70.107.88

For instance AU-01, these are the relevant IP addresses:

- 13.210.1.145
 
- 13.211.70.159
 
- 13.238.45.54
 
- 52.65.73.167
 
- 54.153.242.239
 
- 54.206.45.213

For instance ID-01, these are the relevant IP addresses:

- 108.136.157.246
 
- 108.137.30.207
 
- 16.78.128.71
 
- 16.78.14.134
 
- 16.78.162.208
 
- 43.218.73.35

For instance JP-01, these are the relevant IP addresses:

- 13.159.155.212
 
- 54.199.221.241
 
- 13.192.23.16
 
- 54.250.120.139
 
- 18.181.114.232
 
- 3.114.38.100

For instance KR-01, these are the relevant IP addresses:

- 43.200.215.4
 
- 52.79.67.175
 
- 52.79.113.60
 
- 3.34.212.92
 
- 54.116.134.231
 
- 3.37.197.225

- 

New Stuff!
