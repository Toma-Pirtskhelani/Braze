---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/otherlevels
slug: docs__partners__message_personalization__dynamic_content__otherlevels
title: "OtherLevels"
description: "This article covers the integration between OtherLevels Experience Platform and Braze."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# OtherLevels

The OtherLevels Experience Platform uses GenAI to transform how sports brands, publishers, and operators connect with their customers by transforming traditional content into on-brand personalised video and rich media experiences at scale.

This integration is maintained by OtherLevels.

## Overview

The Braze and OtherLevels integration allows you to create custom GenAI videos through API calls to the OtherLevels Experience Platform, and then send these videos to your users as iOS push videos through Braze Connected Content.

Give your users a better experience with OtherLevels AI-powered experiences. Transform existing and third-party content into highly-scalable video and rich media for audiences that already consume content differently and respond strongly to contextually personalized experiences.

## Prerequisites

Before you start, you’ll need the following:

 Requirements | 
 Description | 

 An OtherLevels account | 
 An OtherLevels account is required to take advantage of this partnership. | 

 A Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 A Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

This integration requires calling the OtherLevels Experience Platform API as part of the video generation process before messages can be sent to your users from Braze. cURL examples are provided as part of this documentation, however we recommend using API clients like Postman to automate the API calls.

## Use cases

Use GenAI videos created with the OtherLevels Experience Platform to:

- Create better experiences for sports owners and leagues, fan engagement, sports books, iGaming, and lotteries.
 
- Amplify your customer marketing by transforming text-based content into rich media and video, creating human and engaging experiences.
 
- Lift outcomes from acquisition to retention by extending, not retooling, your existing Braze integration.

## Integrating the OtherLevels Experience Platform

### Step 1: Call the OtherLevels Experience Platform API to generate a video

The first step of the integration involves calling the OtherLevels Experience Platform API to generate a new video. Note that video generation is not instantaneous. Depending on the length and complexity of the video, the content may take up to half an hour to generate. Plan your messaging schedules and API calls accordingly so that the API calls to generate videos are made sufficiently ahead of when your Braze messages are scheduled to send.

important

The following request uses cURL. For more efficient API request management, we recommend using an API client like Postman.

Refer to the following example for how to structure your API call. For more information about customizing the video specifics and structuring your API call, refer to Customizing the GenAI video.

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
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65

```
 | 
```
curl --request POST \
 --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
 --header 'Content-Type: application/json' \
 --header 'User-Agent: insomnia/10.3.0' \
 --data '{
 "task": {
 "type": "tasks",
 "tasks": {
 "image_video_overlay": {
 "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
 "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
 "color": "255,255,255,0",
 "y_pos": "0",
 "x_pos": "0",
 "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
 "video_input": "= tasks.talking_talent_replace_bg.mp4",
 "type": "compose.ImageVideoOverlay"
 },
 "resize_image": {
 "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
 "type": "compose.MediaResize",
 "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
 "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
 },
 "bg_image": {
 "type": "load",
 "url": "BACKGROUND_IMAGE_URL",
 "refresh_interval": "12h"
 },
 "talking_head": {
 "test": false,
 "title": "INSERT_TITLE",
 "caption": false,
 "templateId": "TALENT_TEMPLATE",
 "type": "TALENT_MODEL",
 "variables": {
 "script": {
 "name": "script",
 "properties": {
 "content": "= tasks.translate_text.text"
 },
 "type": "text"
 }
 }
 },
 "translate_text": {
 "type": "translate_text",
 "source": "en",
 "target": "en",
 "text": "INSERT_SCRIPT"
 },
 "talking_talent_speed": {
 "type": "compose.VideoSetSpeed",
 "speed": "1.0",
 "video_input": "= tasks.talking_head.mp4"
 },
 "talking_talent_replace_bg": {
 "type": "compose.VideoReplaceBg",
 "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
 "video_input": "= tasks.talking_talent_speed.mp4"
 }
 },
 "output": "image_video_overlay"
 }
}'

```
 | 

Replace the following:

 Placeholder | 
 Description | 

 OTHERLEVELS_PROJECT_KEY | 
 An OtherLevels project key will be provided when you are provisioned with an OtherLevels Account. | 

 BACKGROUND_IMAGE_URL | 
 An HTTPS URL for the background of the video. | 

 INSERT_TITLE | 
 The title of the video, this is an internal reference and will not be displayed in the video. | 

 TALENT_TEMPLATE | 
 A Talent Template ID. OtherLevels will work with you during account provisioning to create a talent (avatar). You will be provided one or multiple Talent IDs that can be used. | 

 TALENT_MODEL | 
 A Talent Model ID. OtherLevels will work with you during account provisioning to create a talent (avatar). You will be provided one or multiple Talent Models that can be used. | 

 INSERT_SCRIPT | 
 The exact script that you would like the talent to say during the video. | 

As part of the API response, OtherLevels will return a JSON payload indicating a successful API call. The JSON will contain a unique recipe_id to identify the generated video. The recipe_id will be required in the next step.

Here is an example response from the API:

```

1

```
 | 
```
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}

```
 | 

### Step 2: Setting the recipe_id as a custom attribute

The recipe_id you receive from Step 1 is now set as a Braze custom attribute for the user(s) that you wish to send the videos to.

Depending on your use case, you may have generated a single video that is intended for a large audience, in which case this same recipe_id can be set for multiple users. Alternatively, you may have generated multiple unique videos each targeting a different user, in which case each user should have their custom recipe_id set as Braze custom attributes.

important

The following request uses cURL. For more efficient API request management, we recommend using an API client like Postman.

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

```
 | 
```
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
 "attributes": [
 {
 "external_id": "USER_ID",
 "olxpmedia": "RECIPE_ID"
 }
 ]
}'

```
 | 

Replace the following:

 Placeholder | 
 Description | 

 BRAZE_API_ENDPOINT | 
 The Braze REST endpoint URL of your current Braze instance. For more information, refer to REST API keys. | 

 BRAZE_API_KEY | 
 Your Braze REST API key with the users.track permission. | 

 USER_ID | 
 The User ID who will be receiving this particular video. For more examples of the identifiers which can be used, refer to /users/track. | 

 RECIPE_ID | 
 The recipe_id received from the OtherLevels API response in Step 1. | 

### Step 3: Sending through Braze Connected Content

To send the GenAI videos as iOS push messages to your users, follow these steps:

- Create a Braze iOS push notification campaign.
 
- While composing your campaign, go to the Assets section and paste the following Connected Content syntax into the Add from URL field.

```

1

```
 | 
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}

```
 | 

Next, replace OTHERLEVELS_PROJECT_KEY with the project key provided by OtherLevels.

- In the dropdown for URL file format, select MP4.
 
- Configure the rest of the campaign (such as message content, sending schedule, and target audience) based on your desired preferences.

## Customizing the GenAI video

### Video size and attributes

The video background can be specified within the bg_image key.

 Parameter | 
 Description | 

 url | 
 HTTPS url for the background image. | 

The video background size can be specified within the resize_image key. We recommend that the background image is sized the same as what is configured here.

 Parameter | 
 Description | 

 width | 
 Width of the background image, with options for both portrait and landscape modes. | 

 height | 
 Height of the background image, with options for both portrait and landscape modes. | 

Video Overlay Options can be specified within the image_video_overlay key.

 Parameter | 
 Description | 

 width | 
 Width of the overlay, with options for both portrait and landscape modes. | 

 height | 
 Height of the overlay, with options for both portrait and landscape modes. | 

 color | 
 Color of the overlay specified in RGB along with transparency video. | 

 y_pos | 
 Y-axis offset from center. | 

 x_pos | 
 X-axis offset from center. | 

### Talent and script

As part of provisioning, OtherLevels will work with you to generate one or multiple talents (sometimes referred to as avatars) for use in your videos. Depending on your use case and brand, this may be made in the form of one of your existing brand ambassadors or a unique creation.

After these are created, you will be provided with usable TALENT_TEMPLATE and TALENT_MODEL IDs to use with our API.

The voice model used to process input scripts works best when providing a natural script that a human would read. In most cases, you don’t need extra punctuation to manually guide the script. However, we recommend testing all your scripts before sending to a real audience. The speed at which the talent reads the script can be specified within the talking_talent_speed key.

 Parameter | 
 Description | 

 speed | 
 Specify the speed at which the talent will read the script. For example, 1.5. | 

## Additional considerations

- Only the iOS push notification platform natively supports video media. Android push notifications do not natively support videos, so this integration can only be used with your iOS audience.
 
- When receiving video push notifications on iOS devices, users need to press and hold the push notification for the video to load and play. This is standard behaviour on the iOS platform and cannot be customized.

- 

New Stuff!
