---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/wsc_sports
slug: docs__partners__message_personalization__dynamic_content__visual_and_interactive_content__wsc_sports
title: "WSC Sports"
description: "This reference article outlines the partnership between Braze and WSC Sports, a sports video platform that allows you to include rich and robust sports media..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# WSC Sports

The WSC Sports platform generates personalized sports videos for every digital platform and every sports fan - automatically and in real-time.

This integration is maintained by WSC Sports.

## About the integration

The Braze and WSC Sports integration allows you to include rich and robust sports media in your Braze push notifications.

## Prerequisites

 Requirement | 
 Description | 

 WSC account | 
 A WSC account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with Messages, Segments, Campaigns and Canvas permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

## Integration

The WSC Sports application handles the end-to-end process, from selecting the video to the arrival of the push notification on the end user’s device.

### Step 1: Select send settings

Before starting the integration, make sure you have your desired campaign and user segments built in Braze. When completed, in the WSC Sports platform, select your desired video, and in the send settings, select Braze user segment and campaign ID you would like to use. Lastly, choose the time you would like your push message sent out.

#### API call

Once sent, WSC Sports will deliver the push notification to the chosen user segments, using the following Braze endpoints, based on the options selected:

- /messages/schedule/create
 
- /messages/send

The resulting body of the message is as follows:

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

```
 | 
```
{
 "apple_push": {
 "alert": {
 "body": "Push Message Title"
 },
 "asset_url": "internalURI.mp4",
 "asset_file_type": "mp4"
 }
}

```
 | 

### Step 2: Test send

At this point, your campaign should be ready to test and send. Check the Braze error message logs if you run into errors.

- 

New Stuff!
