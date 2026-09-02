---
url: https://www.braze.com/docs/api/errors
slug: docs__api__errors
title: "API errors and responses"
description: "This reference article covers the various errors and server responses that can come up while using the Braze API and how to troubleshoot them."
section: api/errors
fetched: 2026-09-02
evidence: company-own (technical)
---
# API errors and responses

This reference article covers the various errors and server responses that can come up while using the Braze API and how to troubleshoot them.

## Server responses

If your POST payload was accepted by our servers, then successful messages are met with the following response:

```

1
2
3

```
 | 
```
{
 "message" : "success"
}

```
 | 

Note that success means only that the RESTful API payload was correctly formed and passed to our push notification or email or other messaging services. It does not mean that the messages were actually delivered, as additional factors could prevent the message from being delivered (for example, a device could be offline, the push token could be rejected by Apple’s servers, or you may have provided an unknown user ID).

### Why does my request return success when no message was delivered?

A message: success or 2XX response means Braze accepted and queued the request for the endpoints involved—not that every recipient received a message. For messaging, delivery still depends on channel eligibility, tokens, provider errors, and content validation. See the fatal errors table for HTTP errors that block sends, and to your campaign or Canvas analytics for downstream delivery metrics.

For endpoints like /users/identify, which don’t send messages, a success message means only that Braze received the request for processing. If there is no match for the alias after processing, the request is stopped.

If your message is successful but has non-fatal errors, you receive the following response:

```

1
2
3

```
 | 
```
{
 "message" : "success", "errors" : [<minor error message>]
}

```
 | 

In the case of a success, any messages that were not affected by an error in the errors array are still delivered. If your message has a fatal error you receive the following response:

```

1
2
3

```
 | 
```
{
 "message" : <fatal error message>, "errors" : [<minor error message>]
}

```
 | 

## Responses for tracked send IDs

Analytics are always available for campaigns. In addition, analytics are available for a specific campaign send instance when the campaign is sent as a broadcast. When tracking is available for a specific campaign send instance, you receive the following response:

```

1
2
3

```
 | 
```
{
 "message": "success", "send_id" : "example_send_id"
}

```
 | 

The provided send id can be used as a parameter for the /send/data_series endpoint to pull back send specific analytics.

## Errors

The status code element of a server response is a 3-digit number where the first digit of the code defines the class of response.

- The 2XX class of status code (non-fatal) indicates that your request was successfully received, understood, and accepted.
 
- The 4XX class of status code (fatal) indicates a client error. See the fatal errors chart for a full list of 4XX error codes and descriptions.
 
- The 5XX class of status code (fatal) indicates a server error. There are several potential causes, for example, the server you’re trying to access is unable to execute the request, the server is undergoing maintenance making it unable to execute the request, or the server is experiencing high levels of traffic. When this happens, we recommend you retry your request with exponential backoff. In the event of an incident or outage, Braze is not able to replay any REST API call that failed during the incident window. You must retry any calls that failed during the incident window.

- A 502 error is a failure before it reaches the destination server.
 
- A 503 error means that the request made it to the destination server, but we can’t complete the request because there isn’t enough capacity, or there is a network issue, or similar.
 
- A 504 error indicates a server didn’t receive a response from another server upstream.

### Fatal errors

The following status codes and associated error messages are returned if your request encounters a fatal error.

warning

All of the following error codes indicate that no messages are sent.

 Error Code | 
 Description | 

 5XX Internal Server Error | 
 Retry your request with exponential backoff. | 

 400 Bad Request | 
 Bad syntax. Invalid JSON returns HTTP 400. The error field may include a message that you must pass valid application/json in the request body, or Error while parsing request body. Please check your syntax. See Error while parsing request body. | 

 400 No Recipients | 
 There are no external IDs or segment IDs, or no push tokens in the request. | 

 400 Invalid Campaign ID | 
 No messaging API campaign was found for your provided campaign ID. | 

 400 Message Variant Unspecified | 
 You provide a campaign ID but no message variation ID. | 

 400 Invalid Message Variant | 
 You provided a valid campaign ID, but the message variation ID doesn’t match any of that campaign’s messages. | 

 400 Mismatched Message Type | 
 You provided a message variation of the wrong message type for at least one of your messages. | 

 400 Invalid Extra Push Payload | 
 You provide the extra key for either apple_push or android_push but it is not a dictionary. | 

 400 Max Input Length Exceeded | 
 For /users/track, this error is caused by exceeding the maximum number of objects allowed in a single request. The limit depends on the rate-limit model: for most customers, each request supports up to 75 total objects combined across attributes, events, and purchases. For customers on legacy rate limits, each array supports up to 75 objects independently. For more information, see POST: Create and update users. | 

 400 The max number of external_ids and aliases per request was exceeded | 
 Caused by calling more than 50 external IDs. | 

 400 The max number of ids per request was exceeded | 
 Caused by calling more than 50 external IDs. | 

 400 No message to send | 
 No payload is specified for the message. | 

 400 Slideup Message Length Exceeded | 
 Slideup message contains more than 140 characters. | 

 400 Apple Push Length Exceeded | 
 JSON payload is more than 1,912 bytes. | 

 400 Android Push Length Exceeded | 
 JSON payload is more than 4,000 bytes. | 

 400 Bad Request | 
 Cannot parse send_at datetime. | 

 400 Bad Request | 
 In your request, in_local_time is true but time has passed in your company’s time zone. | 

 401 Unauthorized | 
 Invalid API key. Common causes include:

- Missing or malformed Authorization header. The header value must be Bearer followed by a space and then your API key: Authorization: Bearer YOUR-API-KEY. Common mistakes include omitting Bearer, omitting the key after Bearer, or wrapping the value in quotes.
- Wrong REST endpoint. You’re sending the request to the incorrect instance. For example, if your account is on our EU instance (https://dashboard-01.braze.eu), the request should be sent to https://rest.fra-01.braze.eu.
- Insufficient permissions. Each API key is scoped to a specific workspace and set of permissions. Verify the key’s permissions under Settings > API Keys in the dashboard.
- Wrong API key. API keys are workspace-specific. A key from one workspace cannot be used to authenticate requests for a different workspace. | 

 403 Forbidden | 
 The rate plan doesn’t support, or the account is otherwise inactivated. | 

 403 Access Denied | 
 The REST API key you are using does not have sufficient permissions. Common causes include: 
- API key predates the feature. If the API key was created before a feature was launched (such as subscription groups or catalogs), the key doesn't automatically inherit those permissions. Create a new API key with the required permissions under Settings > API Keys.
- Missing endpoint-specific permission. Each API endpoint requires a specific permission scope (for example, users.track or email.status). Verify the key's permissions match the endpoint you're calling.
- Trailing slash or typo in the URL. For example, /users/track/ (with a trailing slash) instead of /users/track can produce unexpected errors. | 

 404 Not Found | 
 Invalid URL. | 

 415 Unsupported Media Type | 
 The Content-Type request header is missing or incorrect. In the Settings page, add Content-Type with a value of application/json. | 

 429 Rate Limited | 
 Over rate limit. | 

### Error while parsing request body

Braze returns HTTP 400 when the request body is not valid JSON. This applies to REST endpoints that accept a JSON body, such as POST, PUT, and PATCH.

The error field includes a message that you must pass valid application/json in the request body. You may also see Error while parsing request body. Please check your syntax.

Common causes include trailing commas, comments inside JSON, single-quoted strings, an extra opening { before the payload, or sending a concatenated string instead of a JSON-encoded object.

Before you retry:

- Validate the payload with a JSON linter.
 
- Set Content-Type: application/json and send UTF-8 encoded JSON.
 
- Confirm your HTTP client JSON-encodes the object rather than concatenating raw strings.

For /users/track payload size and per-request object limits, see Why do I get 400 Bad Request with a bad syntax or parse error?.

- 

New Stuff!
