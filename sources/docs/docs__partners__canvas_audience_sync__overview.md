---
url: https://www.braze.com/docs/partners/canvas_audience_sync/overview
slug: docs__partners__canvas_audience_sync__overview
title: "About Audience Sync"
description: "This reference article covers how to use Braze Audience Sync to Facebook, to deliver advertisements based upon behavioral triggers, segmentation,."
section: partners/canvas_audience_sync
fetched: 2026-09-02
evidence: company-own (technical)
---
# About Audience Sync

The Braze Audience Sync feature helps you extend the reach of your campaigns to many of the top social and advertising technologies. Through Braze Canvas, brands can dynamically and securely sync first-party user data into the advertising ecosystem to drive marketing and operational efficiencies.

## Feature availability

All Braze customers immediately have access to Audience Sync to Google and Facebook, but customers on Action Credits can access all Audience Sync partners. To unlock additional Audience Sync destinations for customers not on Action Credits, purchase Audience Sync Pro. Contact your Braze account manager for more details.

## Use cases

- Targeting high-value users using owned and paid channels to drive incremental purchases or engagement.
 
- Creating lookalike audiences of your high-value users to optimize new user acquisition costs and conversions.
 
- Retargeting users with ads who are less responsive to other marketing channels.
 
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand.

## Overview

 Destination | 
 Time for destination to match audience members | 
 Rate limit | 
 Lookalike or actalike | 
 Tips | 

 Criteo | 
 Up to 24 hours | 
 250,000 requests per minute. Batched every 5 seconds with an auto-retry. | 
 Yes | 
 
- Criteo supports up to 1,000 ad audiences.
- The minimum audience size is 500, and the recommend is over 20,000. | 

 Facebook or Instagram | 
 Up to 24 hours | 
 190,000 ad accounts per hour | 
 Yes | 
 
- Facebook supports up to 500 ad audiences.
- Facebook requires audiences to be at least 1,000 users. | 

 Google Ads or YouTube | 
 Between 6 to 12 hours | 
 Batched every 5 seconds with an auto-retry based on Google feedback | 
 No | 
 
- Customer match: Use either mobile ad, or email address or phone number.
- Google Audiences require at least 5,000 users to start serving ads.
- The audience size will show as zero until there are at least 1,000 users. | 

 LinkedIn | 
 48 hours | 
 LinkedIn processes 10 queries per second and 100,000 users per request. Braze batches users every 5 seconds. | 
 AI predictive audiences | 
 
- The minimum audience size is 300 members with location targeting taken into consideration.
- LinkedIn shows match the rate in the Braze dashboard. | 

 Pinterest | 
 Between 24 and 48 hours | 
 Pinterest processes 7 queries per second and 1,900 users per request. Braze batches users every 5 seconds. | 
 Yes | 
 Pinterest audiences require at least 100 users. | 

 Snapchat | 
 N/A | 
 Snapchat processes 10 queries per second and 100,000 users per request. Braze batches users every 5 seconds. | 
 Yes | 
 Snapchat supports up to 1,000 ad audiences. | 

 The Trade Desk | 
 Up to 24 hours | 
 N/A | 
 Yes | 
 
- There is no minimum audience size for CRM audiences in The Trade Desk.
- There is no limit for how many audiences The Trade Desk supports.
- If you sync to an audience with a region set to the EU, phone number is not supported. | 

 TikTok | 
 Between 24 and 48 hours | 
 TikTok processes 50 queries per second and 10,000 users per request. Braze batches users every 5 seconds. | 
 Yes | 
 
- TikTok supports up to 400 ad audiences.
- TikTok audiences require at least 1,000 users to start serving ads. | 

When the rate limit is reached, Braze retries syncs for 13 hours.

## How it works

To use Audience Sync to Google or Facebook, connect your ad account by searching for the partner on the Technology Partners page.

After connecting your ad account, you can create a Canvas with an Audience Sync step.

Next, select the partner to sync audiences.

For each partner, you’ll need to configure the following as part of your Audience Sync step:

- Ad account
 
- Audience
 
- Action to either add or remove users
 
- Fields to match

Keep in mind that Braze syncs users as soon as they enter the Audience Sync step within your Canvas.

For each Audience Sync destination, the partner may have different requirements for which fields Braze can send. Refer to the specific partner documentation for more details.

### Audience Sync Pro

To use an Audience Sync Pro partner including TikTok, Pinterest, Snapchat, or Criteo, you can select your partners based on your Audience Sync Pro purchase allotments in the Audience Sync Pro section on the Technology Partners page.

First, select the partners you intend to use. Each purchase of Audience Sync Pro provides you 3 allotted Audience Sync Pro destinations, which are available within each of your workspaces within your dashboard.

After selecting your Audience Sync Pro destinations, connect your selected partner ad account by clicking the partner tile.

Lastly, create your Audience Sync step in Canvas using this Audience Sync Pro destination.

### Batching and latency

When users enter an Audience Sync step in Canvas, Braze enqueues them into a batching system that aggregates user updates before dispatching to the partner API. A batch is sent when one of the following occurs:

- The batch reaches its size limit. This varies by partner:

- Default supports up to 2,000 users
 
- Google Ads supports up to 10,000 users
 
- Facebook and TikTok support up to 2,000 users

- The batch latency timer expires. The default is one hour, but this is configurable per partner. For example, The Trade Desk uses 10 minutes.

High-volume Canvases may dispatch sooner because batches fill faster. Lower-volume Canvases wait until the latency timer expires. Braze doesn’t guarantee a fixed dispatch time; the timing depends on batch size and the configured latency window.

Braze records dispatch activity in internal logs for monitoring and troubleshooting, but these timestamps are not exposed as queryable fields. After Braze dispatches a batch to the partner API, the partner processes the audience update according to their own Service Level Agreements—typically 6–48 hours.

Braze doesn’t receive confirmation from partners that individual users have been matched or synced. Partner responses are HTTP acknowledgments of receipt, not match confirmations. To verify that an audience has been populated, check the partner’s ad platform (such as Google Ads Audience Manager or Meta Business Manager).

### Audience Sync error emails

If the error is related to the overall partner integration (such as an authorization issue), an email is sent to the user who connected the integration. If that user no longer exists, then the administrators receive the emails.

If the error is related to issues with the Audience Sync component (such as “Audience Does Not Exist”) in Canvas, an email is sent to the user who set up the Canvas. If that user no longer exists, then it falls back to the company administrator.

To configure who receives these emails, contact your customer success manager to add recipients under Notification Preferences. This preference covers both integration errors and Audience Sync component errors. Recipients you add receive these emails in addition to the user associated with the error.

## Data privacy considerations

important

This documentation is not intended to provide, nor may it be relied upon as providing legal advice. The use of Audience Sync is subject to specific legal requirements. To ensure that you are using it in compliance with all applicable laws, you should seek the advice of your legal counsel.

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and to comply with privacy laws, such as the “Do Not Sell or Share” right under the CCPA. Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. The following options can help.

If you have collected the iOS IDFA through the Braze SDK, you will be able to use the “Ads Tracking Enabled” filter. Select the value as true to only send users into Audience Sync destinations where they have opted in.

If you are collecting opt-ins, opt-outs, Do Not Sell Or Share, or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

To learn more on how to comply with these Data Protection laws within the Braze platform, see Data Protection Technical Assistance.

## Managing consent for ad targeting

As the advertiser, it is your responsibility to manage consent for ad tracking or targeting of your users.

To send ads to your users, you must comply with all applicable laws and regulations, and the ad platform’s policies and requirements. Only use Braze to target and sync users where you have obtained their consent.

To keep your audience lists in these ad platforms up-to-date and remove users who have revoked their consent, set up a Canvas to remove users from these existing audience lists using an Audience Sync step.

- 

New Stuff!
