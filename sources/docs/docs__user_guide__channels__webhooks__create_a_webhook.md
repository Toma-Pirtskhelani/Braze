---
url: https://www.braze.com/docs/user_guide/channels/webhooks/create_a_webhook
slug: docs__user_guide__channels__webhooks__create_a_webhook
title: "Create a webhook campaign"
description: "This reference article covers how to create and configure a webhook campaign."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create a webhook campaign

Creating a webhook campaign or including a webhook in a multichannel campaign allows you to trigger non-app actions by providing other systems and applications with real-time information.

You can use webhooks to send information to systems, such as Salesforce or Marketo, or to your backend systems. For example, you might want to credit your customers’ accounts with a promotion after they’ve performed a custom event a certain number of times.

tip

To learn more about what webhooks are and how you can use them in Braze, check out Webhooks before proceeding.

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.

- campaign
 
- canvas

Steps:

- Go to Messaging > Campaigns and select Create Campaign.
 
- Select Webhook, or, for campaigns targeting multiple channels, select Multichannel.
 
- Name your campaign something clear and meaningful.
 
- (Optional) Add a description to describe how this campaign will be used.
 
- Add teams and tags as needed.

- Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by particular tags.

- Add and name as many variants as you need for your campaign. You can choose different webhook templates for each of your added variants. For more on this topic, refer to Multivariate and A/B testing.

tip

If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose Copy from Variant from the Add Variant dropdown.

Steps:

- Create your Canvas using the Canvas composer.
 
- After you’ve set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
 
- Choose a step schedule and specify a delay as needed.
 
- Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
 
- Choose your advancement behavior.
 
- Choose any other messaging channels which you would like to pair with your message.

## Step 2: Build your webhook

You can choose to create a webhook from scratch, use an existing template, or use one of our existing templates. Then, build your webhook in the Compose tab of the editor.

The Compose tab consists of the following fields:

- Language
 
- Webhook URL
 
- HTTP method
 
- Request body

### Language

Internationalization is supported in the URL and the request body. To internationalize your message, select Add languages and fill out the required fields.

We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. For our full list of available languages you can use, refer to Languages supported.

If you’re adding copy in a language that is written right-to-left, note that the final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to Creating right-to-left messages.

### Webhook URL

The webhook URL, or HTTP URL, specifies your endpoint. The endpoint is the place where you’ll be sending the information that you’re capturing in the webhook.

If you’d like to send information to a vendor, the vendor should provide this URL in their API documentation. If you’re sending information to your own systems, check with your development or engineering team to confirm you’re using the correct URL.

Braze only allows URLs that communicate over standard ports 80 (HTTP) and 443 (HTTPS).

#### Using Liquid

You can personalize your webhook URLs using Liquid. At times, certain endpoints may require you to identify a user or provide user-specific information as part of your URL. When using Liquid, make sure to include a default value for each piece of user-specific information that you use in your URL.

### HTTP method

The HTTP method you should use varies depending on the endpoint to which you are sending information. In most cases, you’ll use POST.

 HTTP method | 
 Description | 

 POST | 
 Writes new information on the receiving server. This is the most common method used when sending data. | 

 GET | 
 Retrieves existing information, as opposed to writing new information. By definition, a GET request does not support a request body. | 

 PUT | 
 Updates information on the endpoint, replacing any existing information with what’s in the request body. | 

 DELETE | 
 Deletes the resource in the HTTP URL. | 

### Request body

The request body is the information that will be sent to the URL that you specified. You can create the body of your webhook request with JSON key-value pairs or raw text.

#### JSON key-value pairs

JSON key-value pairs allow you to easily write a request for an endpoint that expects a JSON format. You can only use this with an endpoint that expects a JSON request. For example, if your key is message_body, the corresponding value might be Your order just arrived!. After you’ve entered your key-value pair, the composer will configure your request in JSON syntax, and a preview of your JSON request will automatically populate.

You can personalize your key-value pairs using Liquid, such as including any user attribute, custom attribute, or event property in your request. For example, you can include a customer’s first name and email in your request. Be sure to include a default value for each attribute.

#### Raw text

The raw text option gives you the flexibility to write a request for an endpoint that expects a body of any format. For example, you might use this to write a request for an endpoint that expects your request to be in XML format.

Both personalization and internationalization using Liquid is supported in raw text.

If you set the Content-Type request header to application/x-www-form-url-encoded, the request body must be formatted as a URL-encoded string. For example:

```

1

```
 | 
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived

```
 | 

## Step 3: Configure additional settings

### Request headers (optional)

Certain endpoints may require that you include headers in your request. In the Compose section of the composer, you can add as many headers as needed.

Common request headers are Content-Type specifications (which describe what type of data to expect in the body, such as XML or JSON) and Authorization headers that contain your credentials with your vendor or system.

note

HTTP header names are case-insensitive per RFC 7230, section 3.2 (“Each header field consists of a case-insensitive field name”). If your receiving endpoint or any intermediate services (such as CDNs) transform header casing, this won’t affect header processing—Content-Type, content-type, and CONTENT-TYPE are all treated identically.

Content type specifications must use the key Content-Type. Common values are application/json or application/x-www-form-urlencoded.

Authorization headers must use the key Authorization. Common values are Bearer {{YOUR_TOKEN}} or Basic {{YOUR_TOKEN}} where YOUR_TOKEN is the credentials provided by your vendor or system.

## Step 4: Test send your message

Before making your campaign go live, Braze recommends that you test the webhook to make sure the request is formatted properly.

To do so, switch to the Test tab and send a test webhook. You can test the webhook as a random user, a specific user (by entering their email address of external user ID), or a customized user with attributes of your choosing.

After sending the test webhook, a dialog will appear with the response message. If the webhook request is unsuccessful, refer to the error message for assistance in troubleshooting your webhook. The following example details the response of a webhook with an invalid webhook URL.

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
404 Not Found

{
 "error": {
 "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at [email protected].",
 "status_code": 404
 }
}

```
 | 

For more information, see Send test messages.

## Step 5: Build the remainder of your campaign or Canvas

- campaign
 
- canvas

Next, build the remainder of your campaign. See the following sections for further details on how to best use our tools to build webhooks.

### Choose delivery schedule or trigger

Webhooks can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to Scheduling your campaign.

For action-based delivery, you can also set the campaign’s duration and Quiet hours.

This step is also where you can specify delivery controls, such as allowing users to become re-eligible to receive the campaign, or enabling frequency capping rules.

### Choose users to target

Next, you must target users by choosing segments or filters to narrow down your audience. In this step, you select the larger audience from your segments, and narrow that segment further with our filters, if you choose. You automatically receive a preview of what that approximate segment population looks like. Keep in mind that exact segment membership is always calculated before the message is sent.

important

Your message will only be sent to users who already match the conditions you set in the Target Audience step. After that, they still need to meet the trigger you define in the Schedule Delivery step. Think of the target audience as a waiting room—only people already inside can move forward when the next action happens.

### Choose conversion events

Braze allows you to track how often users perform specific actions, conversion events, after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

If you haven’t done so already, complete the remaining sections of your Canvas step. For details about building the rest of your Canvas, including multivariate testing and Optimize with BrazeAI™, see Build your Canvas.

## Step 6: Review and deploy

After you’ve finished building the last of your campaign or Canvas, review its details, test it, then send it!

## Things to know

### Errors, retry logic, and timeouts

Webhooks rely on Braze servers making requests to an external endpoint, and errors can occasionally occur. The most common errors include syntax errors, expired API keys, rate limits, and unexpected server-side issues. Before sending a webhook campaign:

- Test your webhook for syntax errors
 
- Ensure personalized variables have default values

If your webhook fails to send, an error message gets logged to the Message Activity Log, and includes details like the error timestamp, app name, and details about the error.

If the error message is not clear enough regarding the source of the error, you should check the documentation of the API endpoint you’re using. These typically provide an explanation of the error codes the endpoint uses as well as what they’re typically caused by.

#### Response codes and retry logic

When the webhook request is sent, the receiving server will return a response code indicating what happened with the request. The following table summarizes the different responses the server may send, how they impact campaign analytics, and whether, in the case of errors, Braze will try to redeliver the campaign:

 Response code | 
 Marked as received? | 
 Retries? | 

 20x (success) | 
 Yes | 
 N/A | 

 30x (redirection) | 
 No | 
 No | 

 408 (request timeout) | 
 No | 
 Yes | 

 429 (rate limited) | 
 No | 
 Yes | 

 Other 4XX (client error) | 
 No | 
 No | 

 5XX (server error) | 
 No | 
 Yes | 

note

Braze retries the earlier in this section status codes up to five times within 30 minutes using exponential backoff. If we can’t reach your endpoint, retries may be spread over a 24-hour period.

Each webhook is allowed 90 seconds before it times out.

Retry-After and rate-limit response headers can affect how long Braze waits before a retriable attempt (for example, after 408, 429, or 5XX). They do not make non-retriable responses, such as 401, eligible for retry.

note

If webhook sends appear to be missing from analytics, open the Message Activity Log for the campaign or Canvas step. Braze retries only certain responses (for example 408, 429, and 5XX)—most other 4XX client errors, including 401 Unauthorized, are not retried. For the full response table, see Response codes and retry logic.

#### 403 Forbidden and IP allowlisting

403 Forbidden responses means your endpoint received the request but refused it. Common causes include invalid or missing authentication, insufficient API permissions, and network rules (such as a firewall or web application firewall) that block Braze’s outbound IP addresses.

If webhook requests consistently return 403 and your authentication headers are correct, allowlist the Braze IPs for your cluster on the server that receives the webhook. See IP allowlisting. Connected Content requests use the same outbound IPs; see Connected Content IP allowlisting.

For other 4XX troubleshooting steps, refer to Troubleshoot webhook and Connected Content requests.

#### Authentication and Connected Content credentials

The outbound webhook HTTP request does not support attaching Connected Content credentials (:basic_auth or :auth_credentials) to authenticate against your endpoint. Set authentication using Request headers on the webhook instead. To fetch a token or secret at send time, you can place a {% connected_content %} tag in a header or body field so Liquid resolves it before the webhook is sent.

#### Saved webhook templates and campaign usage

Braze does not provide a built-in report that lists every campaign or Canvas step that references a given saved webhook template. To audit usage, review webhook steps that use the same URL and HTTP method, or contact Braze Support.

#### Troubleshooting and additional error details

For detailed explanations, troubleshooting steps, and guidance on resolving specific webhook errors, refer to Troubleshoot webhook and Connected Content requests. You’ll also find more explanations on how our unhealthy host detection system works and how Braze provides error notifications through automated emails and additional logging in Braze Currents.

### IP allowlisting

When a webhook is sent from Braze, the Braze servers make network requests to our customers or third-party servers. With IP allowlisting, you can verify that webhook requests are coming from Braze, adding a layer of security.

Braze will send webhooks from the following IPs. The listed IPs are automatically and dynamically added to any API keys that have been opted-in for allowlisting.

important

If you’re making a Braze-to-Braze webhook and using allowlisting, you should allowlist all the following IPs, including 127.0.0.1.

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

### Delete users

To delete an individual user or a segment of users, go to Audience > Manage Audience > Delete Users. The dashboard supports bulk segment deletion (up to 10 million profiles), includes a 7-day cancellation window, and doesn’t consume shared REST API rate limits. For steps, limits, and permissions, see Delete users.

For programmatic deletion in smaller batches, use the /users/delete endpoint instead of a webhook campaign.

- 

New Stuff!
