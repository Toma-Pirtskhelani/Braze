---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/stayfilm
slug: docs__partners__message_personalization__dynamic_content__visual_and_interactive_content__stayfilm
title: "Stayfilm"
description: "Learn how to integrate Stayfilm personalized video rendering with Braze using webhook campaigns, Connected Content, and Data Transformation."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Stayfilm

Stayfilm is a REST API for automated, personalized video production at scale. The platform integrates data, images, text, soundtracks, narration, and visual effects to generate customized video content for eCommerce, marketplaces, CRM workflows, and marketing campaigns.

This integration sends render jobs from Braze to the Stayfilm API, receives callbacks when videos are ready, and stores video URLs and status on user profiles for use in campaigns and Canvases.

This integration is maintained by Stayfilm.

## Use cases

Stayfilm supports personalized video delivery across the customer lifecycle, including:

- Onboarding and welcome journeys: Welcome new users with videos personalized to their profile or signup context
 
- Product and marketplace content: Generate product-focused videos from catalog or user-supplied media
 
- Conversion and activation: Reinforce key actions with contextual video messaging
 
- Loyalty and upsell: Highlight personalized offers or usage milestones in video format
 
- Win-back and churn prevention: Re-engage inactive users with tailored video content

## Prerequisites

Before you begin, confirm you have the following:

 Requirement | 
 Description | 

 Stayfilm API access | 
 Contact Stayfilm to obtain your project credentials, including idproject, Subscription-Key, OAuth client credentials, and the Stayfilm API base URL. For authentication and endpoint details, see the Stayfilm API documentation. | 

 Braze Data Transformation | 
 Use Braze Data Transformation to receive Stayfilm callbacks and map them to Braze user profiles through the /users/track endpoint. | 

 Braze user identifier | 
 This walkthrough uses external_id to correlate Stayfilm jobs with Braze user profiles. The value you pass in CallbackRelayData must match the user’s external_id in Braze. | 

 Braze sandbox (recommended) | 
 Test the integration in a Braze sandbox workspace before deploying to production. | 

## How the integration works

This integration uses a bidirectional webhook flow:

- Outbound: A Braze webhook campaign sends a render job to the Stayfilm POST /Job endpoint. The request includes user media, template configuration, and CallbackRelayData set to the Braze user’s external_id.
 
- Inbound: When Stayfilm finishes rendering, it sends a callback to your Braze Data Transformation webhook URL. The transformation maps the response to custom attributes and custom events on the matching user profile.
 
- Delivery: Use the stored stayfilm_video_url attribute in messaging channels, such as an in-app message with custom HTML.

The Data Transformation in this walkthrough writes the following custom attributes:

 Attribute | 
 Description | 

 stayfilm_video_status | 
 ready when rendering succeeds, or failed when Stayfilm reports an error | 

 stayfilm_video_url | 
 URL of the rendered MP4 video | 

 stayfilm_job_id | 
 Stayfilm job identifier | 

 stayfilm_render_error | 
 Error message when rendering fails | 

 stayfilm_callback_received_at | 
 ISO timestamp of the callback | 

The transformation also records custom events named stayfilm_video_ready or stayfilm_video_failed.

## Integration

The following steps walk through a proof of concept. After you validate the flow, adapt the job payload, attributes, and messaging to your use case.

### Step 1: Create a test user

Create a test user profile to use while you build and validate the integration. For more information, see Import users.

- Go to Audience > Import Users.
 
- Select Quick User Add.
 
- Enter an external_id and any other required fields, then select Create new user.

important

Do not use personal data—such as email, phone number, full name, government ID, address, or order details—as an external_id. Treat external_id as case-sensitive throughout this integration.

This walkthrough uses stayfilm-poc-001 as the example external_id. Note the value you choose because you use it in later steps.

### Step 2: Create a Data Transformation

Create a Data Transformation to receive Stayfilm callbacks and update user profiles.

- Go to Data Settings > Data Transformation.
 
- Select Create transformation.
 
- Enter a name, such as Stayfilm Callback Data Transformation.
 
- Under Editing experience, select Start from scratch.
 
- Under Select destination > Destination, select POST: Track users.
 
- Select Create transformation.
 
- Replace the default transformation code with the following:

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

```
 | 
```
const brazeExternalId = payload.RelayedData;
if (!brazeExternalId) {
 throw new Error("Missing RelayedData. Expected Stayfilm callback to relay the Braze external_id from CallbackRelayData.");
}

const idJob = payload.IdJob || null;
const producedFiles = payload.ProducedFiles || {};
const videoUrl = producedFiles?.Videos?.VideoMP4?.Url || null;
const errorMessage = payload.ErrorMessage || null;
const hasError = payload.HasError === true || Boolean(errorMessage);
const isReady = !hasError && Boolean(videoUrl);
const now = new Date().toISOString();

let brazecall = {
 attributes: [
 {
 external_id: brazeExternalId,
 _update_existing_only: true,
 stayfilm_video_status: isReady ? "ready" : "failed",
 stayfilm_video_url: videoUrl || null,
 stayfilm_job_id: idJob,
 stayfilm_render_error: errorMessage,
 stayfilm_callback_received_at: now
 }
 ],
 events: [
 {
 external_id: brazeExternalId,
 _update_existing_only: true,
 name: isReady ? "stayfilm_video_ready" : "stayfilm_video_failed",
 time: now,
 properties: {
 stayfilm_job_id: idJob,
 stayfilm_video_url: videoUrl || null,
 stayfilm_render_error: errorMessage,
 stayfilm_status: payload.Status || payload.status || null
 }
 }
 ]
};

return brazecall;

```
 | 

- Select Save, then copy the generated webhook URL.
 
- Send a test POST request to the webhook URL with the following sample Stayfilm callback JSON. Set RelayedData to the external_id of the test user you created in step 1.

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
{
 "IdJob": "debug-job-001",
 "HasError": false,
 "Status": "DRAFT_DONE",
 "ProducedFiles": {
 "Videos": {
 "VideoMP4": {
 "Url": "https://example.com/stayfilm-poc-video.mp4"
 }
 }
 },
 "RelayedData": "stayfilm-poc-001"
}

```
 | 

Send the request with cURL, Postman, or a similar tool. A successful response returns HTTP status 201 with {"message": "success"}.

- Go to Data Settings > Data Transformation and reload the page if your transformation does not appear in the list.
 
- Open the transformation and select Validate. Confirm that validation succeeds in Output.
 
- Select Activate.
 
- Provide the copied webhook URL to Stayfilm as your callback URL.

note

If you store more than the Braze external_id in CallbackRelayData, update the transformation code to parse RelayedData accordingly.

### Step 3: Create a webhook campaign to send jobs to Stayfilm

Create a webhook campaign that submits render jobs to Stayfilm.

important

Before you test the campaign, confirm Stayfilm has configured your project with the Data Transformation callback URL from step 2.

- Go to Messaging > Campaigns.
 
- Select Create campaign > Webhook.
 
- Enter a campaign name, such as Stayfilm Webhook Integration.
 
- Select Compose webhook > Start from scratch.
 
- Under Compose Webhook > Webhook URL, enter the Stayfilm POST /Job endpoint URL provided by Stayfilm. Replace {BASE_URL} in the following example: https://{BASE_URL}/stg/v3/job
 
- Set HTTP method to POST.
 
- Under Request Body, select Raw Text, then paste the job payload Stayfilm provides. You can use Connected Content to make the body dynamic.

Include CallbackRelayData set to the Braze user’s external_id. Stayfilm returns this value in the callback as RelayedData.

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
{
 "SmartTags": ["Setup-Template"],
 "Medias": [
 {
 "Group": "userMedia",
 "URL": "https://{BASE_URL}/some_media.png"
 }
 ],
 "Videos": [{}],
 "CallbackRelayData": "stayfilm-poc-001"
}

```
 | 

Add the following request headers:

 Key | 
 Value | 

 idproject | 
 The idproject value provided by Stayfilm | 

 Subscription-Key | 
 The Subscription-Key provided by Stayfilm | 

 Content-Type | 
 application/json | 

 Authorization | 
 OAuth bearer token retrieved through Connected Content (see the following example) | 

In the following Connected Content block, replace {TENANT_ID}, {CLIENT_ID}, {CLIENT_SECRET_URL_ENCODED}, and {SCOPE_URL_ENCODED} with the values Stayfilm provides. URL-encode {CLIENT_SECRET_URL_ENCODED} and {SCOPE_URL_ENCODED} before you paste them into the block. For OAuth requirements, see the Stayfilm API documentation.

```

1
2
3
4
5
6
7

```
 | 
```
{% connected_content https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
 :method post
 :body grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET_URL_ENCODED}&scope={SCOPE_URL_ENCODED}
 :content_type application/x-www-form-urlencoded
 :cache_max_age 3000
 :save stayfilm_auth
%}Bearer {{stayfilm_auth.access_token}}

```
 | 

- Select Save Draft.

note

If you leave the campaigns page and return, set Status to All to find campaigns that are still in Draft.

### Step 4: Test the webhook campaign

- From the webhook composer, select the Test tab.
 
- Under Preview message as user, select Select existing user, then search for your test user (for example, stayfilm-poc-001).
 
- Select Send test.

A successful response returns HTTP status 201 with a JSON body similar to the following:

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
{
 "IdJob": "4557a77e-f56c-48be-81f7-2d8c5e558cb1",
 "Videos": [
 {
 "IdVideo": "87287b25-7814-4fa1-ad1a-f2ea89822d0f",
 "IdGenre": "f07a1334-5904-420a-9f31-92644f245c5a",
 "IdVideoTemplate": "7b77c3df-12a1-4636-a9b4-bc227f4c233f",
 "IdProject": "73ea3e73-b41e-4676-b674-51731d3bf49c",
 "Status": "DRAFT_RENDERING_PENDING",
 "DurationInSeconds": null,
 "URL": null,
 "ErrorMessage": null,
 "CreatedAt": "2026-06-16T00:35:28.7736263Z",
 "UpdatedAt": "2026-06-16T00:35:28.7736264Z",
 "IdVideoFather": null,
 "IdVideoSon": null,
 "ProducingStatus": "PENDING"
 }
 ],
 "Images": []
}

```
 | 

### Step 5: Confirm the Stayfilm callback

Stayfilm renders the video asynchronously and sends a callback to your Data Transformation when processing completes. Monitor job status through the Stayfilm API endpoints described in the Stayfilm API documentation.

- Go to Data Settings > Data Transformation.
 
- Select the Logs tab for your transformation.
 
- Confirm a callback appears with a Success status.

### Step 6: Display the video in an in-app message

After stayfilm_video_url is populated on the user profile, display the rendered video in a campaign or Canvas.

- Go to Messaging > Campaigns.
 
- Select Create campaign > In-app message.
 
- Enter a campaign name, such as Stayfilm Video Show.
 
- In the message composer, select the Traditional Editor.
 
- Under Send To, select Web Browsers.
 
- Set Message Type to Custom Code.
 
- Paste the following HTML into the HTML field:

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

```
 | 
```
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<div id="stayfilm-video-url" style="display: none;">{{custom_attribute.${stayfilm_video_url}}}</div>
<video id="stayfilm-video" controls preload="metadata" playsinline style="width: 100%; max-width: 420px; border-radius: 12px; background: #000;">
Your browser does not support HTML5 video.
</video>
<script>
(function () {
 var urlElement = document.getElementById("stayfilm-video-url");
 var video = document.getElementById("stayfilm-video");
 var videoUrl = urlElement ? urlElement.textContent.trim() : "";
 if (!videoUrl || videoUrl.indexOf("http") !== 0) {
 return;
 }
 var source = document.createElement("source");
 source.src = videoUrl;
 source.type = "video/mp4";
 video.appendChild(source);
 video.load();
})();
</script>
</body>
</html>

```
 | 

- Select Save Draft.
 
- Select the Test tab.
 
- Under Preview message as user, select Select existing user, then search for your test user’s external_id.

The rendered video appears and plays in the preview when stayfilm_video_url is set on the profile.

## Extend the integration

This walkthrough covers a subset of the Stayfilm API. To adapt job templates, media inputs, or downstream messaging, see the Stayfilm API documentation and update your webhook payload, Data Transformation mapping, and campaign logic accordingly.

## Considerations

- Asynchronous rendering: Video generation is not immediate. Trigger follow-up messaging from the stayfilm_video_ready custom event or segment on stayfilm_video_status instead of sending the in-app message in the same flow as the webhook.
 
- Identifier consistency: The value in CallbackRelayData must match the Braze user’s external_id exactly.
 
- OAuth token caching: The Connected Content example caches the OAuth token for 3000 seconds. Adjust cache_max_age if Stayfilm changes token lifetime requirements.
 
- Sandbox testing: Validate the full callback loop in a Braze sandbox before production launch.
 
- Custom attribute capacity: Confirm your workspace has capacity for the Stayfilm custom attributes and events this integration creates.

## Troubleshooting

Refer to the following table if you experience issues with the Stayfilm integration.

 Issue | 
 Resolution | 

 Data Transformation validation fails | 
 Confirm RelayedData in your test payload matches a valid Braze external_id, then reload the Data Transformation page before selecting Validate. | 

 Webhook test returns a non-201 response | 
 Verify Stayfilm credentials in your request headers, confirm the OAuth Connected Content block uses URL-encoded values, and check that your POST /Job URL is correct. | 

 Callback does not appear in transformation logs | 
 Confirm Stayfilm has your active Data Transformation webhook URL and allow time for video rendering to complete. | 

 In-app preview does not show the video | 
 Confirm stayfilm_video_url is set on the test user profile and that the in-app message targets Web Browsers with Custom Code. | 

- 

New Stuff!
