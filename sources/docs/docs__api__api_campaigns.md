---
url: https://www.braze.com/docs/api/api_campaigns
slug: docs__api__api_campaigns
title: "API campaigns"
description: "This reference article covers how to generate a campaign_id to include in your API calls and how to configure that campaign."
section: api/api_campaigns
fetched: 2026-09-02
evidence: company-own (technical)
---
# API campaigns

This reference article covers how to generate a campaign_id to include in your API calls and how to configure that campaign.

API campaigns are typically used for transactional messaging. When creating API campaigns (not API-triggered campaigns), the Braze dashboard is only used to generate a campaign_id, which lets you track analytics for campaign reporting. You can also generate a message variation ID, which is different for each variant in your campaign.

Send that information to your development team to use in the API request, along with:

- Campaign copy
 
- Audience membership
 
- Assets

After the campaign begins, you can view the results in the dashboard. API campaigns use the Braze messaging APIs, which have the same detailed reporting and retargeting options as campaigns created completely through the dashboard.

Because API campaigns always include a campaign_id, their sends are reflected in dashboard stats. If you call /messages/send without a campaign_id, Braze doesn’t increment those metrics—sends still appear in the Message Activity Log, but not in email performance metrics in the dashboard.

warning

Because API campaigns are typically transactional, all users are eligible for API campaigns, even those in your Global Control Group. A one-click list-unsubscribe header is not added to these sends by default. To add a one-click list-unsubscribe header to an API campaign, see Add one-click list-unsubscribe to API campaigns. To add a one-click list-unsubscribe header to all API campaigns, contact your customer success manager.

## Create a new campaign

Go to Messaging > Campaigns and select Create Campaign, then select API Campaigns. Now, you can move on to configuring your API campaign.

An API-triggered campaign is different from an API campaign.

## Configure your campaign

To configure your campaign, perform the following steps:

- Add a descriptive title so you can find the results on the campaigns page after you send your messages.
 
- Select Add Message and add the message types included in your API campaign. This allows you to generate a campaign_id and a message variation ID, which differs for each channel you include.
 
- Optionally, you can add a conversion event to track user conversions on a specific action or campaign goal.
 
- Select Save Campaign to begin your API campaign.

## API calls

After you save your API campaign, include the following in your API request:

- The generated campaign_id fields with your API request where noted in the Send Messages Endpoints.
 
- A message object for each platform included in the campaign. In the message object, provide the message variation ID. This specifies that statistics should be collected and displayed under that variant. The following message objects are supported: Android, Content Cards, email, iOS, Kindle, SMS/MMS, web push, and webhook.

## Add one-click list-unsubscribe to API campaigns

By default, Braze does not add the one-click list-unsubscribe header to API campaigns. You can add this header to individual API campaign sends by including the {{${set_user_to_one_click_list_unsubscribe}}} Liquid tag in the email headers field of your API request.

To comply with RFC 8058 for one-click list-unsubscribe, include both the List-Unsubscribe and List-Unsubscribe-Post headers in your API request:

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
{
 "external_user_ids": ["user_id"],
 "messages": {
 "email": {
 "app_id": "your_app_id",
 "subject": "Your Subject",
 "from": "Sender Name <[email protected]>",
 "body": "<p>Email body content</p>",
 "headers": {
 "List-Unsubscribe": "<{{${set_user_to_one_click_list_unsubscribe}}}>",
 "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
 }
 }
 }
}

```
 | 

note

The inclusion of these headers does not guarantee that the email client displays an unsubscribe button. Email clients decide whether to show the unsubscribe option based on factors such as sender reputation and message content.

### Add email attachments

To add attachments to API campaign emails, include an attachments array in the email object. You can reference an email template created in the drag-and-drop or HTML editor by providing its email_template_id in the email object, then add attachments through the API call.

For attachment details, size limits, and best practices, see Example email object with attachment.

- 

New Stuff!
