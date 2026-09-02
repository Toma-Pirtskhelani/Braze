---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content
slug: docs__user_guide__messaging__design_and_edit__personalize__connected_content__troubleshooting_webhooks_and_connected_content
title: "Troubleshoot webhook and Connected Content requests"
description: "Diagnose webhook and Connected Content errors using a symptom index, HTTP error tables, and unhealthy host detection guidance."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Troubleshoot webhook and Connected Content requests

Use this page to troubleshoot common error codes for webhooks and Connected Content. For setup, see Creating a webhook and Making an API call. To inspect a Connected Content request in preview, see Connected Content Debugger.

## Start here: Match your symptom

Match your symptom in the table to navigate to the relevant section.

 Symptom | 
 Go to | 

 4XX client error in Message Activity Log | 
 4XX errors | 

 5XX server error or timeout | 
 5XX errors | 

 598 Host Unhealthy or requests halted briefly | 
 Unhealthy host detection | 

 Connected Content renders blank in preview or send | 
 Connected Content returns no response body | 

 Need to inspect a Connected Content request in preview | 
 Connected Content Debugger | 

 Automated error email from Braze | 
 Automated emails and Message Activity Log entries | 

 Need webhook failure events in Currents | 
 Additional failure insights in Braze Currents | 

## Standard investigation path

Use this workflow when a webhook or Connected Content request fails or renders incorrectly. Start at step 1.

- Open the Message Activity Log and note the error code, timestamp, and endpoint URL.
 
- For 4XX errors, verify request syntax, authentication headers, URL path, and HTTP method against the endpoint documentation.
 
- For 5XX errors, check endpoint health, rate limits, and whether Braze flagged the host as unhealthy.
 
- For Connected Content, preview the message for a test user. Use the Connected Content Debugger to inspect the request and response, and confirm Liquid doesn’t resolve to blank or JSON-breaking values.
 
- If unhealthy host detection may be involved, review Unhealthy host detection before contacting Braze Support.

## 4XX errors

4XX errors indicate that there’s an issue with the request sent to the endpoint. These errors are typically caused by erroneous requests, including malformed parameters, missing authentication headers, or incorrect URLs. Note that these errors also apply to the Report Builder.

Refer to the following table for error code details and steps to resolve:

 Error code | 
 What it means | 
 Steps to resolve | 

 400 Bad Request | 
 There's invalid syntax in the request. | 

- Check the request payload for any syntax errors.
 
- Confirm that all required fields are included and correctly formatted.
 
- If you're sending a JSON payload, validate the JSON structure.
 
- If you're using Liquid to template in personalization tags in the webhook request, verify that the Liquid does not resolve to a blank value or produce JSON-breaking characters (such as unescaped quotes). Preview the message for a test user to confirm the rendered output is valid.
 
 | 

 401 Unauthorized | 
 The request requires user authentication. | 

- Verify that the correct authentication credentials (such as API keys or tokens) are included in the request headers.
 
- Confirm that you have the user permissions to access the endpoint.
 
 | 

 403 Forbidden | 
 The endpoint understands the request but refuses to authorize it. | 

- Check if the API key or token has the required permissions.
 
- Confirm that you have the user permissions to access the endpoint.
 
- If requests consistently return 403 and authentication looks correct, your server, API gateway, or WAF may be blocking Braze's outbound IP addresses. Allowlist the IPs for your Braze cluster. For webhooks, see IP allowlisting. For Connected Content, see Connected Content IP allowlisting.
 
 | 

 404 Not Found | 
 The endpoint cannot find the requested resource. | 

- Check the endpoint URL for any typos or incorrect paths.
 
- Confirm that the resource you're trying to access exists.
 
 | 

 405 Method Not Allowed | 
 The request method is known by the endpoint but is not supported by the target resource. | 

- Check the HTTP method (DELETE, GET, POST, PUT) used in the request.
 
- Confirm that the endpoint supports the method you're using.
 
 | 

 408 Request Timeout | 
 The endpoint timed out processing the request. | 

- Check the HTTP method (DELETE, GET, POST, PUT) used in the request.
 
- Confirm that the endpoint supports the method you're using.
 
 | 

 409 Conflict | 
 The request is incomplete because of a conflict with the current state of the resource. | 

- Check the HTTP method (DELETE, GET, POST, PUT) used in the request.
 
- Confirm that the endpoint supports the method you're using.
 
 | 

 429 Too Many Requests | 
 There are too many requests sent in a given amount of time. | 

- Lower the rate limit on your campaign or Canvas step.
 
 | 

## 5XX errors

5XX errors indicate that there’s an issue with the endpoint. These errors are typically caused by server-side issues.

 Error code | 
 What it means | 

 500 Internal Server Error | 
 The endpoint encountered an unexpected condition that prevented it from completing the request. | 

 502 Bad Gateway | 
 The endpoint received an invalid response from the upstream server. | 

 503 Service Unavailable | 
 The endpoint is currently unable to handle the request due to a temporary overload or maintenance. | 

 504 Gateway Timeout | 
 The endpoint didn’t receive a timely response from the upstream server. | 

 529 Host Overloaded | 
 The endpoint host is overloaded and could not respond. | 

 598 Host Unhealthy | 
 Braze simulated the response because the endpoint host temporarily is marked as unhealthy. For more information, see Unhealthy host detection. | 

 599 Connection Error | 
 Braze experienced a network connect timeout error while trying to establish a connection to the endpoint, meaning the endpoint may be unstable or down. | 

### Resolving 5XX errors

Here are tips for troubleshooting common 5XX errors:

- Review the error message for specific details available in the Message Activity Log. For webhooks, go to the Performance Over Time section on the Braze home page and select the statistics for webhooks. From here, you can find the timestamp that indicates when the errors occurred.
 
- Make sure you’re not sending too many requests that overload the endpoint. You can send in batches or adjust the rate limit to check if this reduces any errors.

## Unhealthy host detection

Braze webhooks and Connected Content employ an unhealthy host detection mechanism to detect when the target host experiences a high rate of significant slowness or overload resulting in timeouts, too many requests, or other outcomes that prevent Braze from successfully communicating with the target endpoint. It acts as a safeguard to reduce unnecessary load that may be causing the target host to struggle. It also serves to stabilize Braze infrastructure and maintain fast messaging speeds.

The detection thresholds differ between webhooks and Connected Content:

- For webhooks: If the number of failures exceeds 3,000 in any one-minute moving time window (per unique combination of host name and app group— not per endpoint path), Braze temporarily halts requests to the target host for one minute.
 
- For Connected Content: If the number of failures exceeds 3,000 AND the error rate exceeds 90% in any one-minute moving time window (per unique combination of host name and app group— not per endpoint path), Braze temporarily halts requests to the target host for one minute.

When requests are halted, Braze simulates responses with a 598 error code to indicate the poor health. After one minute, Braze resumes requests at full speed if the host is found to be healthy. If the host is still unhealthy, Braze waits another minute before trying again.

The following error codes contribute to the unhealthy host detector failure count: 408, 429, 502, 503, 504, 529.

For webhooks, Braze automatically retries HTTP requests that were halted by the unhealthy host detector. This automatic retry uses exponential backoff and retries only a few times before failing. For more information on webhook errors, refer to Errors, retry logic, and timeouts.

For Connected Content, if requests to the target host are halted by the unhealthy host detector, Braze continues to render messages and follow your Liquid logic as if it received an error response code. If you want to ensure these Connected Content requests are retried when they’re halted by the unhealthy host detector, use the :retry option. For more information on the :retry option, see Connected Content retries.

If you believe the unhealthy host detection may be causing issues, contact Braze Support.

### Connected Content returns no response body

Symptom: A Connected Content call renders as blank in your message preview or send.

If a Connected Content call renders as blank in your message preview or send, use the Connected Content Debugger to inspect the request and response, then check:

- Non-breaking spaces in the URL: Braze strips non-breaking spaces (&nbsp; or Unicode U+00A0) from Connected Content URLs before making the request. If your URL was copied from a document or dashboard field that inserted non-breaking spaces between characters, the request may fail or return no usable body. Re-type the URL in plain text or remove hidden spaces, then preview again.
 
- Redirect responses (3xx): Connected Content does not follow redirects. Only 2xx responses are treated as successful, so a 301 or 302 can render blank even when the same URL works in Postman. Use the final destination URL, or configure the endpoint to return a 2xx response (typically 200) at the URL Braze calls. See Why does Connected Content fail when my endpoint returns a redirect?.
 
- HTTP errors and empty bodies: For status codes outside the 2xx range or blocked hosts, Connected Content can render an empty string. See Making an API call and review failures in the Message Activity Log.

## Automated emails and Message Activity Log entries

### Setting up automated emails

If you experience more than 100,000 webhook or Connected Content endpoint errors (including retries) in a workspace in a 24-hour period, Braze sends you an email that includes the following information on how to resolve the errors.

- Name of the workspace
 
- A link to the Canvas or campaign
 
- Endpoint URL
 
- Error code
 
- Time the error was last observed
 
- Links to the Message Activity Log and related documentation

note

You can configure the error threshold per workspace. To adjust this threshold, contact Braze Support.

The endpoint errors are:

- 4XX: 400, 401, 403, 404, 405, 408, 409, 429
 
- 5XX: 500, 502, 503, 504, 598, 599

These emails are only sent once per day at the workspace level. If no users sign up for these emails, Braze notifies all company administrators.

To sign up to receive these emails, do the following:

- Go to Settings > Admin Settings > Notification Preferences.
 
- Select Connected Content Errors and Webhook Errors in the Canvas & Campaigns section.

### Message Activity Log entries

If a failure occurs, there is at least one entry in the Message Activity Log related to it. If the request is retried and eventually succeeds, those details are available in Currents and Snowflake Data Share. Note that even if a request eventually succeeds after a retry, the errors can still trigger the automated email.

### Additional failure insights in Braze Currents

To increase transparency into webhook-related issues, Braze streams detailed webhook failure events to Currents and Snowflake Data Sharing. These events include failed webhook requests (such as HTTP 4xx or 5xx responses), providing more observability into how webhook issues may impact message delivery. Note that failure events include terminal errors as well as errors that are being retried.

note

Connected Content requests are not included in these webhook failure events.

For more information, refer to the Message engagement events glossary.

- 

New Stuff!
