---
url: https://www.braze.com/docs/partners/canvas_audience_sync/criteo_audience_sync
slug: docs__partners__canvas_audience_sync__criteo_audience_sync
title: "Audience Sync to Criteo"
description: "This reference article will cover how to use Braze Audience Sync to Criteo, to deliver advertisements based upon behavioral triggers, segmentation, and more."
section: partners/canvas_audience_sync
fetched: 2026-09-02
evidence: company-own (technical)
---
# Audience Sync to Criteo

Using the Braze Audience Sync to Criteo, brands can elect to add user data from their own Braze integration to Criteo customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based on your user data can now be used to trigger an ad to that user in your Criteo customer lists.

Common use cases for audience syncing include:

- Targeting high-value users via multiple channels to drive purchases or engagement
 
- Retargeting users who are less responsive to other marketing channels
 
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand
 
- Creating lookalike audiences to acquire new users more efficiently

This feature gives brands the option to control what specific first-party data is shared with Criteo. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our privacy policy.

important

Audience Sync Pro disclaimer

Braze Audience Sync to Criteo is an Audience Sync Pro integration. For more information on this integration, contact your Braze account manager. 

## Prerequisites

You must ensure that you have the following items created and/or completed prior to setting up your Audience Sync to Criteo.

 Requirement | 
 Origin | 
 Description | 

 Criteo ad account | 
 Criteo | 
 An active Criteo ad account tied to your brand.

Ensure that your Criteo admin has granted you the appropriate permissions to access Audiences. | 

 Criteo Advertising Guidelines
and
Criteo Brand Safety Guidelines | 
 Criteo | 
 As an active Criteo customer, you must ensure that you can comply with Criteo’s Advertising and Brand Safety Guidelines prior to launching any Criteo campaigns. | 

## Integration

### Step 1: Connect to Criteo

important

You must have the “Admin” permission to connect Criteo to your Braze account.

In the Braze dashboard, go to Partner Integrations > Technology Partners and select Criteo. Under Criteo Audience Export, select Connect Criteo.

A Criteo oAuth page appears to authorize Braze for the permissions related to your Audience Sync integration.

Once you have selected confirm, you’ll then be redirected back into Braze to select which Criteo ad accounts you wish to sync to.

After you have successfully connected, you are taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.

Your Criteo connection will be applied at the Braze workspace level. If your Criteo admin removes you from your Criteo ad account, Braze will detect an invalid token. As a result, your active Canvases using Criteo will show errors, and Braze will not be able to sync users.

### Step 2: Configure your Canvas entry criteria

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the CCPA. Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. The following options can help.

If you have collected the iOS IDFA through the Braze SDK, you will be able to use the Ads Tracking Enabled filter. Select the value as true to only send users into Audience Sync destinations where they have opted in.

If you are collecting opt-ins, opt-outs, Do Not Sell Or Share, or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

To learn more on how to comply with these Data Protection laws within the Braze platform, see Data Protection Technical Assistance.

### Step 3: Add an Audience Sync Step with Criteo

Add a component in your Canvas and select Audience Sync.

### Step 4: Sync setup

Click on the Custom Audience button to open the component editor.

Select Criteo as the desired Audience Sync partner.

Then select your desired Criteo ad account. Under the Choose a New or Existing Audience dropdown, type in the name of a new or existing audience.

- create a new audience
 
- sync with an existing audience

Create a New Audience

Enter a name for the new audience, select Add Users to Audience, and select which fields you would like to sync with Criteo. Next, save your audience by clicking the Create Audience button at the bottom of the step editor.

Braze displays a notification at the top of the step editor if the audience is created successfully or if errors arise. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync component.

Sync with an Existing Audience

Braze also offers the ability to add users to existing Criteo audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and Add to the Audience. Braze will then add users in near real-time as they enter the Audience Sync component.

### Step 5: Launch Canvas

After you configure your Audience Sync to Criteo, launch the Canvas! The new audience is created, and users who go through the Audience Sync step are passed into this audience on Criteo. If your Canvas contains subsequent components, your users advance to the next step in their user journey.

You can view the audience in Criteo by going into your ads manager account and then selecting Segments from the Audience Library of the navigation. From the Segments page, you can see the size of each audience after it reaches ~1,000.

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze syncs them in near real time while respecting Criteo’s API rate limits. Braze batches and processes as many users as possible every five seconds before sending them to Criteo.

Criteo’s API rate limit allows no more than 250 requests per minute. If a customer reaches this limit, Braze retries the sync for up to ~13 hours. If the sync is still not possible, Braze lists these users under the Users Errored metric.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

 Metric | 
 Description | 

 Entered | 
 Number of users who entered this component to be synced to Criteo. | 

 Proceeded to Next Step | 
 How many users advanced to the next component if there is one. All users will auto-advance if this is the last step in the Canvas branch. | 

 Users Synced | 
 Number of users who have successfully been synced to Criteo. | 

 Users Not Synced | 
 Number of users that have not been synced due to missing fields to match. | 

 Users Pending | 
 Number of users currently being processed by Braze to sync into Criteo. | 

 Users Errored | 
 Number of users who were not synced to Criteo due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Criteo token or if the audience was deleted on Criteo. | 

 Exited Canvas | 
 Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. | 

important

Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.

## Frequently asked questions

### What should I do next if I receive an invalid token error?

You can simply disconnect and reconnect your Criteo account on the Criteo partner page. Ensure with your Criteo admin that you have the appropriate permissions to the ad account you wish to sync with.

### Why is my Canvas not allowed to launch?

Confirm that your Criteo ad account has successfully connected to Braze on the Criteo partner page. Next, check that you’ve selected an ad account, entered a name for the new audience, and selected fields to match.

### How do I know if users have matched after passing users to Criteo?

Criteo does not provide this information for their own data privacy policies.

### How many audiences can Criteo support?

At this time, you can only have 1,000 audiences within your Criteo account. If you’re exceed this limit, Braze will notify you that we are unable to create new audiences. You’ll need to remove audiences that you’re no longer using in your Criteo ad account.

- 

New Stuff!
