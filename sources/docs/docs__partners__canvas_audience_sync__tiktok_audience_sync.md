---
url: https://www.braze.com/docs/partners/canvas_audience_sync/tiktok_audience_sync
slug: docs__partners__canvas_audience_sync__tiktok_audience_sync
title: "Audience Sync to TikTok"
description: "This reference article will cover how to use Braze Audience Sync to TikTok to deliver advertisements based upon behavioral triggers, segmentation, and more."
section: partners/canvas_audience_sync
fetched: 2026-09-02
evidence: company-own (technical)
---
# Audience Sync to TikTok

Using the Braze Audience Sync to TikTok, brands can elect to add user data from their own Braze integration to TikTok Audiences to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas.

Common use cases for Audience Syncing include:

- Targeting high-value users via multiple channels to drive purchases or engagement
 
- Retargeting users who are less responsive to other marketing channels
 
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand
 
- Creating lookalike audiences to acquire new users more efficiently

This feature lets brands control what specific first-party data is shared with TikTok. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our privacy policy.

important

Audience Sync Pro disclaimer

Braze Audience Sync to TikTok is an Audience Sync Pro integration. For more information on this integration, contact your Braze account manager.

## Prerequisites

You must ensure the following items are created, completed, and/or accepted before setting up your TikTok Audience Step in Canvas.

 Requirement | 
 Origin | 
 Description | 

 TikTok for Business Center Account | 
 TikTok | 
 A centralized tool to manage your brand’s TikTok assets (such as ad accounts, pages, apps). | 

 TikTok Ad Account | 
 TikTok | 
 An active TikTok ad account tied to your brand’s Business Center account.

Ensure that your TikTok Business Center manager admin has granted you admin permissions to the TikTok ad accounts you plan to use with Braze. | 

 TikTok terms & policies | 
 TikTok | 
 Agree to comply with any of TikTok’s required terms, policies, guidelines, and documentation related to your use of the TikTok Audience Sync, including any terms, policies, guidelines, and documentation incorporated by reference therein, which may include: the Commercial Terms of Service, Advertising Terms, Privacy Policy, Custom Audience Terms, Developer Terms of Service, Developer Data Sharing Agreement, Advertising Policies, Brand Guidelines, and Community Guidelines. | 

## Integration

### Step 1: Connect to TikTok

important

You must have the “Admin” permission to connect TikTok to your Braze account.

In the Braze dashboard, go to Partner Integrations > Technology Partners and select TikTok. Under TikTok Audience Sync, select Connect TikTok.

You’ll then be redirected to the TikTok OAuth page to authorize Braze for ad account management and Audience Management. After you have selected Confirm, you’ll be redirected back into Braze to select which TikTok ad accounts you wish to sync to.

Once successfully connected, you will return to the partner page. Here, you can view which accounts are connected and disconnect existing accounts.

Your TikTok connection will be applied at the Braze workspace level. If your TikTok admin removes you from your TikTok Business Center or access to the connected TikTok accounts, Braze will detect an invalid token. As a result, your active Canvases using TikTok Audience components will show errors, and Braze will not be able to sync users.

### Step 2: Add a TikTok Audience component in Canvas

Add a component in your Canvas and select Audience Sync.

### Step 3: Sync setup

Click on the Custom Audience button to open the component editor.

Select TikTok as the desired Audience Sync partner.

Then select the desired TikTok ad account. Under the Choose a New or Existing Audience dropdown, type in the name of a new or existing audience.

- create a new audience
 
- sync with an existing audience

Create a New Audience

Enter a name for the new audience, select Add Users to Audience, and select which fields you would like to sync with TikTok. Next, save your audience by clicking the Create Audience button at the bottom of the step editor.

Braze displays a notification at the top of the step editor if the audience is created successfully or if errors arise. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the audience step.

Sync with an Existing Audience

Braze also offers the ability to add users to existing TikTok audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and Add to the Audience. Braze will then add users in near real-time as they enter the TikTok Audience step.

### Step 4: Launch Canvas

After you configure your TikTok Audience component, launch the Canvas! A new audience is created, and users who flow through the TikTok Audience component are passed into this audience on TikTok. If your Canvas contains subsequent components, your users advance to the next step in their user journey.

You can view the audience in TikTok by entering your Ads Manager Account and selecting Audiences from the Assets dropdown. From the Audience page, you can see the size of each audience after it reaches ~1,000.

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze syncs them in near real time while respecting TikTok’s Marketing API rate limits. Braze batches and processes as many users as possible every 5 seconds before sending them to TikTok.

TikTok’s Segment API rate limit allows no more than 50 queries per second and 10k users per request. If a customer reaches this limit, Braze retries the sync for up to ~13 hours. If the sync is still not possible, Braze lists these users under the Users Errored metric.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

 Metric | 
 Description | 

 Entered | 
 Number of users who entered this component to be synced to TikTok. | 

 Proceeded to Next Step | 
 Number of users that advanced to the next component if one exists. All users will auto-advance if this is the last step in the Canvas branch. | 

 Users Synced | 
 Number of users who have successfully been synced to TikTok. Note that this does not equate to users matched on TikTok. | 

 Users Not Synced | 
 Number of users that have not been synced due to missing fields to match. | 

 Users Pending | 
 Number of users currently being processed by Braze to sync into TikTok. | 

 Users Errored | 
 Number of users who were not synced to TikTok due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid TikTok token or if the audience was deleted on TikTok. | 

 Exited Canvas | 
 Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience sync component. | 

important

Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.

## Frequently asked questions

### What should I do next if I receive an invalid token error?

You can disconnect and reconnect your TikTok account on the TikTok partner page. Ensure with your TikTok Business Center admin that you have the appropriate permissions to the ad account you wish to sync.

### Why is my Canvas not allowed to launch?

Confirm that your TikTok account successfully connects to Braze on the TikTok partner page. Next, make sure you’ve selected an ad account, entered a name for the new audience, and selected fields to match.

### How do I know if users have matched after passing users to TikTok?

TikTok does not provide this information for their data privacy policies.

### How long will it take for my audiences to populate in TikTok?

The audience size will update within 24-48 hours on the Audiences page in TikTok’s Ads Manager.

### What is the maximum number of audiences I can have in my TikTok ad account?

You can have up to 400 audiences per TikTok ad account.

### Why is my audience size or match rate in TikTok higher than the users synced in Braze with Audience Sync?

This is because in TikTok, one ID may be associated with multiple TikTok users. This occurs most often when clients use mobile ad IDs (iOS IDFA and Android GAID) because one device may have multiple TikTok users logged in.

Additionally, TikTok also counts Pangle users as matched users, which in some cases can result in an elevated match rate. However, when you use the audience for ad delivery, the actual deliverable audience size may not be as high as the matched user size as it depends on placement and other influencing factors.

### Why am I receiving an email with the subject “Audience Does Not Exist For Canvas”?

This can occur if the audience you chose to sync to is not a streaming audience (for example, if it’s a lookalike audience or a user file audience). Try creating a new audience through the Braze Audience Sync Canvas step.

- 

New Stuff!
