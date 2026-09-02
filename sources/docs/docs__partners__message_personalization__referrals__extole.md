---
url: https://www.braze.com/docs/partners/message_personalization/referrals/extole
slug: docs__partners__message_personalization__referrals__extole
title: "Extole"
description: "This article outlines the partnership between Braze and Extole, a referral marketing company, that allows you to pull customer events and attributes from refer-a-friend and..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Extole

Extole, a SaaS company, is an industry leader in refer-a-friend marketing, helping create and optimize effective referral marketing programs to increase customer acquisition.

This integration is maintained by Extole.

## About the integration

With the Braze and Extole integration, you can pull customer events and attributes from Extole refer-a-friend and growth programs into Braze, empowering you to create more personalized marketing campaigns that boost customer acquisition, engagement, and loyalty. You can also dynamically pull Extole content attributes, such as personalized share codes and links, into Braze communications.

## Prerequisites

 Requirement | 
 Description | 

 Extole account | 
 An Extole account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with the users.track permission. This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze API URL | 
 Your Braze API URL is specific to your Braze instance. | 

## Use cases

The following use cases showcase a few ways to use Extole’s integration with Braze. Work with your Extole implementation and customer success managers to develop an option that fits your company’s specific needs.

- Use custom events from your referral and engagement programs to trigger a Braze campaign or Canvas
 
- Create custom segments, dashboards, and reporting using data from your Extole-powered programs
 
- Automatically unsubscribe or subscribe users to your marketing list in Braze

## Integration

Complete the following steps to quickly get your integration up and running. Your Extole implementation and customer success managers will support you through this process and answer any questions you may have.

### Connect to your Braze account

- Select the Braze integration on the Partners page of your My Extole account.
 
- In the Braze integration, select Install to initiate the connection between Extole and Braze.
 
- Fill out the required fields, starting with your Braze REST API key.
 
- Enter your Braze API URL. This URL depends on which instance your Braze account is provisioned to.
 
- Add any Extole events you’d like to send to Braze. The default events, event properties, and user attributes are described in the Extole Events table.
 
- Add any reward states you’d like to send to Braze other than the FULFILLED state. Refer to the Extole Rewards table for descriptions of the available reward states.
 
- Select your Braze external ID key mapping. This is how Extole updates user profiles in Braze. You can map the Braze external ID key to Extole’s email_address or partner_user_id for the user. We recommend using external_id instead of email_address as it is more secure.
 
- Save your settings to complete the connection. Now, Extole events can flow to your Braze account.

### Extole program events

The following are the default events, event properties, and user attributes Extole will send to Braze. Contact your Extole implementation or customer success managers to identify and add additional Extole events to your integration.

 Event | 
 Description | 
 Event Properties | 
 User Attributes | 

 extole_created_share_link | 
 A participant creates their share link by entering their email in the Extole Share Experience. | 
 Event name 
Event time 
Partner (Extole) 
Funnel (advocate or friend) 
Program | 
 
External ID 
Email 
Share link | 

 extole_shared | 
 A participant shares their referral link with a friend. | 
 Event name 
Event time 
Partner (Extole) 
External ID 
Funnel (advocate or friend) 
Program 
Share channel | 
 Email 
First name 
Last Name | 

 outcome - The outcome is dynamic based on the configuration of your program (such as extole_shipped, extole_converted) | 
 A participant has converted or completed the desired outcome event configured for the program. | 
 Dynamic per program | 
 Email 
First name 
Last Name | 

### Extole subscription states

 Subscription State | 
 Description | 
 Event Properties | 
 User Attributes | 

 subscribed | 
 A participant has opted-in to receive marketing messages. | 
 N/A | 
 Email 
List type 
External ID 
Email subscribe (opted in) | 

 unsubscribed | 
 A participant has opted-out of receiving Extole email communications. | 
 Email 
External ID 
Subscription state (unsubscribed) 
Subscription group ID | 
 List type | 

### Extole rewards

By default, Extole will send reward events in the FULFILLED state to Braze so you can trigger reward notifications via a Braze campaign or Canvas. Refer to the following table for additional reward states.

 Reward State | 
 Description | 
 Event Properties | 
 User Attributes | 

 FULFILLED | 
 The default state. The reward has been assigned a value (such as coupon or gift card) by an Extole reward supplier. | 
 Email 
Face value 
Coupon code 
Face value type | 
 Email 
First name 
Last name | 

 EARNED | 
 A reward has been created and associated with a person. | 
 Email 
Face value 
Coupon code 
Face value type | 
 Email 
First name 
Last name | 

 SENT | 
 The reward has been fulfilled and has been sent either via email or on a device to the recipient. | 
 Email 
Face value 
Coupon code 
Face value type | 
 Email 
First name 
Last name | 

 REDEEMED | 
 The reward has been used by the recipient, as evidenced in a conversion or redemption event sent to Extole. | 
 Email 
Face value 
Coupon code 
Face value type | 
 Email 
First name 
Last name | 

 FAILED | 
 An issue has prevented the reward from being issued or sent, requiring attention. | 
 Email 
Face value 
Coupon code 
Face value type | 
 Email 
First name 
Last name | 

 CANCELED | 
 The reward has been deactivated and will return to inventory. | 
 Email 
Face value 
Face value type | 
 Email 
First name 
Last name | 

 REVOKED | 
 The fulfilled reward has been invalidated. For example, Extole requested a supplier gift card and then determined that the card was sent in error. If the supplier supports revoking the reward, Extole will request the funds back, and the reward will no longer be valid. | 
 Email 
Face value 
Face value type | 
 Email 
First name 
Last name | 

## Customization

### Find and create users in Braze

For certain use cases, such as a new email or SMS subscription where Extole does not have an external ID (user ID), Extole can check for the user’s identifier using the Braze Export user profile by identifier endpoint. Extole will add and update any profile attributes if the user exists in Braze. If the request does not return a user profile, Extole will use the /users/track endpoint to create a user alias with the user’s email address as the alias name.

## Using this integration

After connecting your accounts, events will automatically begin flowing from Extole to Braze without any action on your part. A live view of events being sent to Braze can be found in Extole’s Outbound Webhook Center for troubleshooting.

- 

New Stuff!
