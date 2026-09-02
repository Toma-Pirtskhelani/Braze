---
url: https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger
slug: docs__partners__additional_channels_and_extensions__additional_channels__instant_chat__messenger
title: "Facebook Messenger"
description: "This reference article outlines the partnership between Braze and Facebook Messenger, one of the world's most popular instant messaging platforms."
section: partners/additional_channels_and_extensions
fetched: 2026-09-02
evidence: company-own (technical)
---
# Facebook Messenger

Facebook Messenger is one of the world’s most popular instant messaging platforms, used by nearly one billion monthly active users. Through this platform, brands can create engaging chatbots to interact intelligently and automatically with their customers.

The Braze and Facebook integration leverages Braze webhooks, segmentation, personalization, and triggering features to message your users in Facebook Messenger through the Messenger Platform API. A custom Facebook Messenger webhook template is included in our platform under Content > Webhook.

The Facebook Messenger platform is intended for “non-promotional messages that facilitate a pre-existing transaction, provide other customer support actions, or deliver content requested by a person.” To read more, see Facebook’s platform guidelines and examples of acceptable use cases.

## Prerequisites

Acknowledge the following before proceeding with integration:

- Facebook does not allow the usage of the Messenger platform to send marketing messages.
 
- You will need the user’s explicit permission for messages from your page.
 
- To send messages to users who are not test users of your Facebook App, your app will need to pass Facebook’s app review.

 Requirement | 
 Origin | 
 Access | 
 Description | 

 Facebook Messenger page | 
 Facebook | 
 https://www.facebook.com/pages/create | 
 A Facebook page will be used as the identity of your bot. When people chat with your app, they will see the page name and profile picture. | 

 Facebook Messenger app | 
 Facebook | 
 https://developers.facebook.com/apps | 
 The Facebook app contains the settings for your Messenger bot, including access tokens. | 

 App bot review and approval | 
 Facebook | 
 https://developers.facebook.com/docs/messenger-platform/app-review | 
 When you are ready to release your bot to the public, you must submit it to Facebook for review and approval. This review process allows us to ensure your Messenger bot abides by our policies and functions as expected before making it available to everyone on Messenger. | 

 Page-scope IDs (PSIDs) | 
 Facebook | 
 https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages | 
 You need to have users PSIDs to send messages on Facebook Messenger. When a user interacts with your app via Messenger, Facebook will create a PSID. This PSID can be sent to Braze as a string custom attribute. | 

 Page access token | 
 Facebook | 
 https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token | 
 These access tokens are similar to user access tokens, except that they provide permission to APIs that read, write or modify the data belonging to a Facebook Page. To obtain a page access token, you need to obtain a user access token and ask for the manage_pagespermission. After you have the user access token, you then get the page access token via the Graph API. | 

## Integration

The following shows how to set up a Braze Facebook Messenger webhook. 
For those who require additional help getting your bot set up, a full Messenger bot tutorial and example code can be found in the Braze GitHub repository!

### Step 1: Collect your PSIDs

To send messages on Facebook Messenger, you need to collect your users’ page-specific IDs (PSIDs) to identify your user and interact with them consistently. PSIDs are not the same as the user’s Facebook ID. Facebook creates this identifier any time you message a customer or when a customer messages you.

PSIDs can be found using one of the various entry points Facebook offers. After the user messages your app or takes an action in a conversation, such as tapping a button or sending a message, their PSID will be included in the sender.id property of the webhook event, so your bot can identify who took the action.

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

```
 | 
```
{
 "sender":{
 "id":"<PSID>"
 },
 "recipient":{
 "id":"<PAGE_ID>"
 },
 "timestamp":1458692752478,
 "message":{
 "mid":"mid.1457764197618:41d102a3e1ae206a38",
 "text":"hello, world!",
 "quick_reply": {
 "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
 }
 }
}

```
 | 

Whenever you send a message, their PSID will be included in the recipient.id property of the request to identify who should receive the message.

### Step 2: Send to Braze as a custom attribute

Once you are confident that you are receiving PSIDs, coordinate and share this with your developers to send the PSIDs to Braze as a custom attribute. PSIDs are strings that can be accessed by making an API call.

### Step 3: Set up your webhook template

To create a Facebook Messenger webhook template:

- Go to Content > Webhook and select Create webhook template.
 
- Select Templates > Braze templates.
 
- Find and select the “Facebook Messenger” template.
 
- 
 
Select Select template.

- Provide a template name and add teams and tags, as necessary.
 
- Enter your message or choose a message template from those made available by Facebook. You can also choose your message type or tag.
 
- Include the PSID as a custom attribute. This can be done by using the blue and white + button in the corner of the Request Body box.
 
- Add your page access token in the webhook URL by replacing FACEBOOK_PAGE_ACCESS_TOKEN with your token.

#### Previewing and testing your webhook

Before you send your message, test your webhook. Make sure your Messenger ID is saved in Braze (or find it and test as a customized user), and use the preview to send the test message:

If you receive the message successfully, you can configure its delivery settings.

## Using this integration

Once set up, use this integration to target Facebook Messenger users. If you are not sending messages using users’ phone numbers and plan on sending Messenger messages repeatedly, you should create a segment for all users for whom the Messenger ID exists as a custom attribute and turn on analytics tracking to track your Messenger subscription rates over time.

If you choose not to create a specific segment for Messenger subscribers, make sure to include a filter for Messenger ID existing to avoid errors.

You may also use other segmentation to target your Messenger campaigns, and the rest of the campaign creation process, as is with any other campaign.

- 

New Stuff!
