---
url: https://www.braze.com/docs/api/api_limits
slug: docs__api__api_limits
title: "Rate limits"
description: "This reference article covers API rate limits for the Braze API infrastructure."
section: api/api_limits
fetched: 2026-09-02
evidence: company-own (technical)
---
# Rate limits

The Braze API infrastructure is designed to handle high volumes of data across our customer base. To this end, we enforce API rate limits per workspace.

A rate limit is the number of requests the API can receive in a given time period. Many load-based denial-of-service incidents in large systems are unintentional—caused by errors in software or configurations—not malicious attacks. Rate limits check that such errors don’t deprive our customers of Braze API resources. If too many requests are sent in a given time frame, you may see error responses with a status code of 429, which indicates the rate limit has been hit.

warning

API rate limits are subject to change depending on the proper usage of our system. We encourage sensible limits when making an API call to prevent damage or misuse.

## Rate limits by request type

Refer to the following for the default API rate limits of different request types. These default limits can be increased upon request. Contact your customer success manager for more information.

### Requests with different rate limits

 Request Type | 
 Default API Rate Limit | 

 /users/track | 
 Requests: Rate limits vary depending on your contract. For customers with data points in their pricing, Braze applies a burst limit of 3,000 requests per three seconds. For all other customers, limits are configured according to your contract terms. Contact Braze Support or your customer success manager for questions about your limits.

Batching: Up to 75 total objects combined across attributes, events, and purchases per API request. Customers on legacy rate limits can include up to 75 objects per array independently. For more information, see Batching User Track requests.

Limits for Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU: See Monthly Active Users CY 24-25 limits. | 

 /users/export/ids | 
 If you onboarded on or after August 22, 2024: 250 requests per minute. 

 If you onboarded before August 22, 2024: 2,500 requests per minute. | 

 /users/delete
/users/alias/new
/users/alias/update
/users/identify
/users/merge | 
 20,000 requests per minute, shared between the endpoints. | 

 /users/external_id/rename | 
 1,000 requests per minute. | 

 /users/external_id/remove | 
 1,000 requests per minute. | 

 /events/list | 
 1,000 requests per hour, shared with the /purchases/product_list endpoint. | 

 /purchases/product_list | 
 1,000 requests per hour, shared with the /events/list endpoint. | 

 /campaigns/data_series | 
 50,000 requests per minute. | 

 /messages/send
/campaigns/trigger/send
/canvas/trigger/send
/campaigns/trigger/schedule/create
/canvas/trigger/schedule/create | 
 For broadcast calls (when broadly targeting segments, filters, or a connected audience), 250 requests per minute across all audiences, and 10 requests per minute per unique audience (whichever limit hits first).

Otherwise, when targeting individual recipients, the request is included in the 250,000 requests per hour shared rate limit. | 

 /sends/id/create | 
 100 requests per day. | 

 /subscription/status/set | 
 5,000 requests per minute. | 

 /preference_center/v1/{preferenceCenterExternalId}/url/{userId}
/preference_center/v1/list
/preference_center/v1/{preferenceCenterExternalId} | 
 1,000 requests per minute. | 

 /preference_center/v1
/preference_center/v1/{preferenceCenterExternalId} | 
 10 requests per minute. | 

 /catalogs/{catalog_name}
/catalogs
/catalogs | 
 50 requests per minute shared between the endpoints. | 

 /catalogs/{catalog_name}/items
/catalogs/{catalog_name}/items
/catalogs/{catalog_name}/items | 
 16,000 requests per minute shared between the endpoints. | 

 /catalogs/{catalog_name}/items/{item_id}
/catalogs/{catalog_name}/items/{item_id}
/catalogs/{catalog_name}/items
/catalogs/{catalog_name}/items/{item_id}
/catalogs/{catalog_name}/items/{item_id} | 
 50 requests per minute shared between the endpoints. | 

 /catalogs/{catalog_name}/fields/{field_name}
/catalogs/{catalog_name}/fields
/catalogs/{catalog_name}/selections/{selection_name}
/catalogs/{catalog_name}/selections | 
 50 requests per minute shared between the endpoints. | 

 /scim/v2/Users/{id}
/scim/v2/Users?filter={[email protected]}
/scim/v2/Users/{id}
/scim/v2/Users/{id}}
/scim/v2/Users/ | 
 5,000 requests per day, per company, shared between the endpoints. | 

 /cdi/integrations | 
 50 requests per minute. | 

 /cdi/integrations/{integration_id}/sync | 
 20 requests per minute. | 

 /cdi/integrations/{integration_id}/job_sync_status | 
 100 requests per minute. | 

 /media_library/create | 
 100 requests per hour. | 

 /media_library/replace_file | 
 100 requests per hour. | 

### Requests with shared rate limits

The following requests have a rate limit of 250,000 requests per hour, shared between them.

- /app_group/sdk_authentication/create
 
- /app_group/sdk_authentication/keys
 
- /app_group/sdk_authentication/delete
 
- /app_group/sdk_authentication/primary
 
- /campaigns/details
 
- /campaigns/list
 
- /campaigns/trigger/send (only for non-broadcast calls—those that specify external_user_ids or aliases)
 
- /campaigns/trigger/schedule/create (only for non-broadcast calls)
 
- /campaigns/trigger/schedule/delete
 
- /campaigns/trigger/schedule/update
 
- /canvas/data_series
 
- /canvas/data_summary
 
- /canvas/details
 
- /canvas/list
 
- /canvas/trigger/send (only for non-broadcast calls)
 
- /canvas/trigger/schedule/create (only for non-broadcast calls)
 
- /canvas/trigger/schedule/delete
 
- /canvas/trigger/schedule/update
 
- /content_blocks/create
 
- /content_blocks/info
 
- /content_blocks/list
 
- /content_blocks/update
 
- /email/blocklist
 
- /email/blacklist
 
- /email/bounce/remove
 
- /email/hard_bounces
 
- /email/spam/remove
 
- /email/status
 
- /email/unsubscribes
 
- /events/data_series
 
- /kpi/dau/data_series
 
- /kpi/mau/data_series
 
- /kpi/new_users/data_series
 
- /kpi/uninstalls/data_series
 
- /messages/live_activity/start
 
- /messages/live_activity/update
 
- /messages/send (only for non-broadcast calls)
 
- /messages/schedule/create
 
- /messages/schedule/delete
 
- /messages/schedule/update
 
- /messages/scheduled_broadcasts
 
- /segments/data_series
 
- /segments/details
 
- /segments/list
 
- /sends/data_series
 
- /sessions/data_series
 
- /sms/invalid_phone_numbers
 
- /sms/invalid_phone_numbers/remove
 
- /subscription/status/get
 
- /subscription/user/status
 
- /templates/email/create
 
- /templates/email/info
 
- /templates/email/list
 
- /templates/email/update
 
- /users/export/global_control_group
 
- /users/export/segment

### What counts as the same unique audience?

This applies to the following endpoints: /messages/send, /campaigns/trigger/send, /canvas/trigger/send, /campaigns/trigger/schedule/create, and /canvas/trigger/schedule/create.

For these endpoints, broadcast requests are considered to target the same unique audience when all of the following match:

- The campaign or Canvas being triggered (the campaign_id or canvas_id in your API request, if specified)
 
- The audience being targeted (the segments or filters, or for API campaigns, the segment_id in your API request)
 
- The connected audience filters (the audience object in your API request, if specified)

Each unique combination of these attributes counts as a distinct audience, so the additional rate limit for each unique audience applies to each combination independently.

## Batching API requests

Braze APIs are built to support batching. With batching, Braze can take in as much data as possible in a single API call so that you don’t need to make a lot of API calls. It’s more efficient for Braze to process data in batches than to process data one call at a time. For example, handling 1,000 batched API calls requires less resources than handling 75,000 individual calls. Batching is extremely important for any application that may require more than 75,000 calls per hour.

note

REST API rate limit increases are considered based on need for customers who are making use of the API batching capabilities.

### Batching requests for the Create and update users endpoint

Each /users/track request can contain up to 75 total objects combined across attributes, events, and purchases. Each object can update one user. A single user profile can be updated by multiple objects.

Legacy rate limits

For customers on legacy rate limits, each array (attributes, events, and purchases) can contain up to 75 objects independently, for a combined maximum of up to 225 objects per request.

For more information about /users/track rate limits, see POST: Create and update users.

Requests made to this endpoint generally begin processing in this order:

- Attributes
 
- Events
 
- Purchases

### Batching Messaging endpoint requests

A single request to the Messaging endpoints can reach any one of the following:

- Up to 50 specific external_ids, each with individual message parameters
 
- A segment of any size created in the Braze dashboard, specified by its segment_id
 
- Users who match additional audience filters of any size, defined in the request as a connected audience object

### Example batch request

The following example uses external_id to make one API call for email and SMS.

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "subscription_groups":[
 {
 "subscription_group_id":"subscription_group_identifier",
 "subscription_state":"subscribed",
 "external_ids":["example-user","[email protected]"]
 },
 {
 "subscription_group_id":"subscription_group_identifier",
 "subscription_state":"subscribed",
 "external_ids":["example-user","[email protected]"]
 }
 ]
}

```
 | 

## Monitoring your rate limits

Every single API request sent to Braze returns the following information in the response headers:

 Header Name | 
 Description | 

 X-RateLimit-Limit | 
 The maximum number of requests that you can make in a specified interval (your rate limit). | 

 X-RateLimit-Remaining | 
 The number of requests remaining in the current rate limit window. | 

 X-RateLimit-Reset | 
 The time at which the current rate limit window resets in UTC epoch seconds. | 

This information is intentionally included in the header of the response to the API request rather than the Braze dashboard. This allows your system to better react in real time as you’re interacting with our API. For example, if the X-RateLimit-Remaining value drops below a certain threshold, you might want to slow sending to make sure all transactional emails go out. Or, if it reaches zero, you might want to pause all sending until the time specified in X-RateLimit-Reset elapses.

note

HTTP headers will be returned in all lowercase characters. This behavior aligns with the HTTP/2 protocol that mandates all header field names must be lowercase. This differs from HTTP/1.X where header names were case-insensitive but were commonly written in various capitalizations.

If you have questions about API limits, contact your customer success manager or open a support ticket.

tip

You can use the API usage dashboard to view and compare incoming traffic against your rate limits.

### Optimal delay between endpoints

note

We recommend that you allow for a 5-minute delay between consecutive endpoint calls to minimize errors.

Understanding the optimal delay between endpoints is crucial when making consecutive calls to the Braze API. Problems arise when endpoints depend on the successful processing of other endpoints, and if called too soon, could raise errors. For example, if you’re assigning users an alias through our /user/alias/new endpoint, and then hitting that alias to send a custom event through our /users/track endpoint, how long should you wait?

Under normal conditions, the time for our data eventual consistency to occur is 10-100ms (1/10 of a second). However, there can be some cases where it takes longer for that consistency to occur, so we recommend that you allow for a 5-minute delay between making subsequent calls to minimize the probability of error.

## Payload size limits

Braze API requests are subject to payload size limits, separate from rate limits. Most endpoints accept request bodies up to 4 MB. When a request exceeds the applicable limit, Braze may reject it with HTTP 413 Request Entity Too Large or HTTP 400 Bad Request, depending on the endpoint.

The /users/track/bulk endpoint has a 2 MB payload limit and returns HTTP 400 when the request body exceeds that limit. For endpoint-specific limits and error handling, see User data endpoints.

### Rate limit reset

Rate limits reset on the clock hour, not on a rolling window. For example, if the limit is 250,000 requests per hour, you could make 50,000 requests between 10:00 PM and 10:59 PM and another 250,000 requests between 11:00 PM and 11:59 PM, because the counter resets at the top of each hour.

- 

New Stuff!
