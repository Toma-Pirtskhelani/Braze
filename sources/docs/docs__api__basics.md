---
url: https://www.braze.com/docs/api/basics
slug: docs__api__basics
title: "API overview"
description: "This reference article covers the API basics including what a REST API is, the terminology, and an overview of API keys."
section: api/basics
fetched: 2026-09-02
evidence: company-own (technical)
---
# API overview

This reference article covers the API basics, including common terminology and an overview of REST API keys, permissions, and how to keep them secure.

## Braze REST API collection

 Collection | 
 Purpose | 

 Catalogs | 
 Create and manage catalogs and catalog items to reference in your Braze campaigns. | 

 Cloud Data Ingestion | 
 Manage your data warehouse integrations and syncs. | 

 Email lists and addresses | 
 Set up and manage bi-directional sync between Braze and your email systems. | 

 Export | 
 Access and export various details of your campaigns, Canvases, KPIs, and more. | 

 Media Library | 
 Manage assets within Braze. | 

 Messages | 
 Schedule, send, and manage your campaigns and Canvases. | 

 Preference center | 
 Build your preference center and update the styling of it. | 

 SCIM | 
 Manage user identities in cloud-based applications and services. | 

 SMS | 
 Manage your users’ phone numbers in your subscription groups. | 

 Subscription groups | 
 List and update both SMS and email subscription groups stored in the Braze dashboard. | 

 Templates | 
 Create and update templates for email messaging and Content Blocks. | 

 User data | 
 Identify, track, and manage your users. | 

## API definitions

The following is an overview of terms you may see in the Braze REST API documentation.

### Endpoints

Braze manages a number of different instances for our dashboard and REST endpoints. When your account is provisioned, you log in to one of the following URLs. Use the correct REST endpoint based on which instance you are provisioned to. If you are unsure, open a support ticket or use the following table to match the URL of the dashboard you use to the correct REST Endpoint.

To find your REST endpoint in Braze:

- Log in to Braze and go to Settings > APIs and Identifiers > API Keys.
 
- Select an existing API key, or select Create API Key to make a new key.
 
- Copy the REST endpoint shown on this tab and use that endpoint for your API requests.

important

When using endpoints for API calls, use the REST endpoint.

For SDK integration, use the SDK endpoint, not the REST endpoint.

 Instance | 
 URL | 
 REST Endpoint | 
 SDK Endpoint | 

 US-01 | 
 https://dashboard-01.braze.com | 
 https://rest.iad-01.braze.com | 
 sdk.iad-01.braze.com | 

 US-02 | 
 https://dashboard-02.braze.com | 
 https://rest.iad-02.braze.com | 
 sdk.iad-02.braze.com | 

 US-03 | 
 https://dashboard-03.braze.com | 
 https://rest.iad-03.braze.com | 
 sdk.iad-03.braze.com | 

 US-04 | 
 https://dashboard-04.braze.com | 
 https://rest.iad-04.braze.com | 
 sdk.iad-04.braze.com | 

 US-05 | 
 https://dashboard-05.braze.com | 
 https://rest.iad-05.braze.com | 
 sdk.iad-05.braze.com | 

 US-06 | 
 https://dashboard-06.braze.com | 
 https://rest.iad-06.braze.com | 
 sdk.iad-06.braze.com | 

 US-07 | 
 https://dashboard-07.braze.com | 
 https://rest.iad-07.braze.com | 
 sdk.iad-07.braze.com | 

 US-08 | 
 https://dashboard-08.braze.com | 
 https://rest.iad-08.braze.com | 
 sdk.iad-08.braze.com | 

 US-10 | 
 https://dashboard.us-10.braze.com | 
 https://rest.us-10.braze.com | 
 sdk.us-10.braze.com | 

 EU-01 | 
 https://dashboard-01.braze.eu | 
 https://rest.fra-01.braze.eu | 
 sdk.fra-01.braze.eu | 

 EU-02 | 
 https://dashboard-02.braze.eu | 
 https://rest.fra-02.braze.eu | 
 sdk.fra-02.braze.eu | 

 AU-01 | 
 https://dashboard.au-01.braze.com | 
 https://rest.au-01.braze.com | 
 sdk.au-01.braze.com | 

 ID-01 | 
 https://dashboard.id-01.braze.com | 
 https://rest.id-01.braze.com | 
 sdk.id-01.braze.com | 

 JP-01 | 
 https://dashboard.jp-01.braze.com | 
 https://rest.jp-01.braze.com | 
 sdk.jp-01.braze.com | 

 KR-01 | 
 https://dashboard.kr-01.braze.com | 
 https://rest.kr-01.braze.com | 
 sdk.kr-01.braze.com | 

### API limits

For most APIs, Braze has a default rate limit of 250,000 requests per hour. However, certain request types have their own rate limit applied to better handle high volumes of data across the customer base. For details, refer to API rate limits

### User IDs

- External user ID: The external_id serves as a unique user identifier for whom you are submitting data. This identifier should be the same as the one you set in the Braze SDK in order to avoid creating multiple profiles for the same user.
 
- Braze user ID: braze_id serves as a unique user identifier that Braze sets. You can use this identifier to delete users through the REST API in addition to external_ids.

For more information, refer to the following articles based on your platform: iOS, Android, and Web.

## About REST API keys

A REST Application Programming Interface key (REST API key) is a unique code that you pass into an API to authenticate the API call and identify the calling application or user. You access the API using HTTPS web requests to your company’s REST API endpoint. REST API keys work in tandem with App Identifier keys to track, access, send, export, and analyze data to help ensure everything is running smoothly.

Workspaces and API keys go hand in hand at Braze. Workspaces are designed to house versions of the same application across multiple platforms. Many customers also use workspaces to contain free and premium versions of their applications on the same platform. As you may notice, these workspaces are also making use of the REST API and have their own REST API keys. These keys can be individually scoped to include access to specific endpoints on the API. Each call to the API must include a key with access to the endpoint hit.

We refer to both the REST API key and workspace API key as the api_key. The api_key is included in each request as a request header and acts as an authentication key that allows you to use our REST APIs. These REST APIs are used to track users, send messages, export user data, and more. When you create a new REST API key, you must give it access to specific endpoints. By assigning specific permissions to an API key, you can limit exactly which calls an API key can authenticate.

tip

In addition to REST API keys, there also exists a type of key called Identifier keys that can be used to reference specific things like apps, templates, Canvases, campaigns, Content Cards, and segments from the API. For more information, refer to API identifier types.

### Creating REST API keys

To create a new REST API key:

- Go to Settings > APIs and Identifiers.
 
- Select Create API Key.
 
- Give your new key a name for identification at a glance.
 
- Specify allowlisted IP addresses and subnets for the new key.
 
- Select which permissions you want to be associated with your new key.

important

Keep in mind that after you create a new API key, you cannot edit the scope of permissions or the allowlisted IPs. This limitation is in place for security reasons. If you need to change the scope of a key, create a new key with the updated permissions and implement that key in place of the old one. After you’ve completed your implementation, you can delete the old key.

### REST API key permissions

API key permissions are permissions you can assign a user or group to limit their access to certain API calls. To view your list of API key permissions, go to Settings > APIs and Identifiers, and select your API key.

- user data
 
- email
 
- messages
 
- campaigns
 
- canvas
 
- segments
 
- purchases
 
- events
 
- sessions
 
- kpis
 
- templates
 
- sso
 
- content blocks
 
- preference center
 
- subscription
 
- sms
 
- catalogs
 
- sdk authentication

 Permission | 
 Endpoint | 
 Description | 

 users.track | 
 /users/track | 
 Record user attributes, custom events, and purchases. | 

 users.delete | 
 /users/delete | 
 Delete any user. | 

 users.alias.new | 
 /users/alias/new | 
 Create a new alias for an existing user. | 

 users.identify | 
 /users/identify | 
 Identify an alias-only user with an external ID. | 

 users.export.ids | 
 /users/export/ids | 
 Query for user profile information by user ID. | 

 users.export.segment | 
 /users/export/segment | 
 Query for user profile information by segment. | 

 users.merge | 
 /users/merge | 
 Merges two existing users into each other. | 

 users.external_ids.rename | 
 /users/external_ids/rename | 
 Change the external ID for an existing user. | 

 users.external_ids.remove | 
 /users/external_ids/remove | 
 Remove the external ID for an existing user. | 

 users.alias.update | 
 /users/alias/update | 
 Update an alias for an existing user. | 

 users.export.global_control_group | 
 /users/export/global_control_group | 
 Query for user profile information in the Global Control Group. | 

 Permission | 
 Endpoint | 
 Description | 

 email.unsubscribe | 
 /email/unsubscribes | 
 Query for unsubscribed email addresses. | 

 email.status | 
 /email/status | 
 Change email address status. | 

 email.hard_bounces | 
 /email/hard_bounces | 
 Query for hard bounced email addresses. | 

 email.bounce.remove | 
 /email/bounce/remove | 
 Remove email addresses from your hard bounce list. | 

 email.spam.remove | 
 /email/spam/remove | 
 Remove email addresses from your spam list. | 

 email.blacklist | 
 /email/blacklist | 
 Blocklist email addresses. | 

 Permission | 
 Endpoint | 
 Description | 

 messages.send | 
 /messages/send | 
 Send an immediate message to specific users. | 

 messages.schedule.create | 
 /messages/schedule/create | 
 Schedule a message to be sent at a specific time. | 

 messages.schedule.update | 
 /messages/schedule/update | 
 Update a scheduled message. | 

 messages.schedule.delete | 
 /messages/schedule/delete | 
 Delete a scheduled message. | 

 messages.schedule_broadcasts | 
 /messages/scheduled_broadcasts | 
 Query all scheduled broadcast messages. | 

 messages.live_activity.update | 
 /messages/live_activity/update | 
 Update an iOS Live Activity. | 

 Permission | 
 Endpoint | 
 Description | 

 campaigns.trigger.send | 
 /campaigns/trigger/send | 
 Trigger the sending of an existing campaign. | 

 campaigns.trigger.schedule.create | 
 /campaigns/trigger/schedule/create | 
 Schedule a send of a campaign with API-triggered delivery. | 

 campaigns.trigger.schedule.update | 
 /campaigns/trigger/schedule/update | 
 Update a campaign scheduled with API-triggered delivery. | 

 campaigns.trigger.schedule.delete | 
 /campaigns/trigger/schedule/delete | 
 Delete a campaign scheduled with API-triggered delivery. | 

 campaigns.list | 
 /campaigns/list | 
 Query for a list of campaigns. | 

 campaigns.data_series | 
 /campaigns/data_series | 
 Query for campaign analytics over a time range. | 

 campaigns.details | 
 /campaigns/details | 
 Query for details of a specific campaign. | 

 sends.data_series | 
 /sends/data_series | 
 Query for message send analytics over a time range. | 

 sends.id.create | 
 /sends/id/create | 
 Create send ID for message blast tracking. | 

 campaigns.url_info.details | 
 /campaigns/url_info/details | 
 Query for URL details of a specific message variation within a campaign. | 

 transactional.send | 
 /transactional/v1/campaigns/{campaign_id}/send | 
 Allows for ability to send transactional messaging using the Transactional messaging endpoint. | 

 Permission | 
 Endpoint | 
 Description | 

 canvas.trigger.send | 
 /canvas/trigger/send | 
 Trigger the sending of an existing Canvas. | 

 canvas.trigger.schedule.create | 
 /canvas/trigger/schedule/create | 
 Schedule a send of a Canvas with API-triggered delivery. | 

 canvas.trigger.schedule.update | 
 /canvas/trigger/schedule/update | 
 Update a Canvas scheduled with API-triggered delivery. | 

 canvas.trigger.schedule.delete | 
 /canvas/trigger/schedule/delete | 
 Delete a Canvas scheduled with API-triggered delivery. | 

 canvas.list | 
 /canvas/list | 
 Query for a list of Canvases. | 

 canvas.data_series | 
 /canvas/data_series | 
 Query for Canvas analytics over a time range. | 

 canvas.details | 
 /canvas/details | 
 Query for details of a specific Canvas. | 

 canvas.data_summary | 
 /canvas/data_summary | 
 Query for rollups of Canvas analytics over a time range. | 

 canvas.url_info.details | 
 /canvas/url_info/details | 
 Query for URL details of a specific message variation within a Canvas step. | 

 Permission | 
 Endpoint | 
 Description | 

 segments.list | 
 /segments/list | 
 Query for a list of segments. | 

 segments.data_series | 
 /segments/data_series | 
 Query for segment analytics over a time range. | 

 segments.details | 
 /segments/details | 
 Query for details of a specific segment. | 

 Permission | 
 Endpoint | 
 Description | 

 purchases.product_list | 
 /purchases/product_list | 
 Query for a list of products purchased in your app. | 

 purchases.revenue_series | 
 /purchases/revenue_series | 
 Query for total money spent per day in your app over a time range. | 

 purchases.quantity_series | 
 /purchases/quantity_series | 
 Query for the total number of purchases per day in your app over a time range. | 

 Permission | 
 Endpoint | 
 Description | 

 events.list | 
 /events/list | 
 Query for a list of custom events. | 

 events.data_series | 
 /events/data_series | 
 Query occurrences of a custom event over a time range. | 

 Permission | 
 Endpoint | 
 Description | 

 sessions.data_series | 
 /sessions/data_series | 
 Query for sessions per day over a time range. | 

 Permission | 
 Endpoint | 
 Description | 

 kpi.dau.data_series | 
 /kpi/dau/data_series | 
 Query for unique active users per day over a time range. | 

 kpi.mau.data_series | 
 /kpi/mau/data_series | 
 Query for total unique active users over a 30-day rolling window over a time range. | 

 kpi.new_users.data_series | 
 /kpi/new_users/data_series | 
 Query for new users per day over a time range. | 

 kpi.uninstalls.data_series | 
 /kpi/uninstalls/data_series | 
 Query for app uninstalls per day over a time range. | 

 Permission | 
 Endpoint | 
 Description | 

 templates.email.create | 
 /templates/email/create | 
 Create a new email template on the dashboard. | 

 templates.email.info | 
 /templates/email/info | 
 Query for information of a specific template. | 

 templates.email.list | 
 /templates/email/list | 
 Query for a list of email templates. | 

 templates.email.update | 
 /templates/email/update | 
 Update an email template stored on the dashboard. | 

 Permission | 
 Description | 

 sso.saml.login | 
 Set up identity provider-initiated login. For more information, refer to Service Provider (SP) initiated login. | 

 Permission | 
 Endpoint | 
 Description | 

 content_blocks.info | 
 /content_blocks/info | 
 Query for information of a specific template. | 

 content_blocks.list | 
 /content_blocks/list | 
 Query for a list of Content Blocks. | 

 content_blocks.create | 
 /content_blocks/create | 
 Create a new Content Block on the dashboard. | 

 content_blocks.update | 
 /content_blocks_update | 
 Update an existing Content Block on the dashboard. | 

 Permission | 
 Endpoint | 
 Description | 

 preference_center.get | 
 /preference_center/v1/{preferenceCenterExternalId} | 
 Get a preference center. | 

 preference_center.list | 
 /preference_center/v1/list | 
 List preference centers. | 

 preference_center.update | 
 /preference_center/v1

/preference_center/v1/{preferenceCenterExternalID} | 
 Create or update a preference center. | 

 preference_center.user.get | 
 /preference_center/v1/{preferenceCenterExternalId}/url/{userId} | 
 Get a preference center link for a user. | 

 Permission | 
 Endpoint | 
 Description | 

 subscription.status.set | 
 /subscription/status/set | 
 Set subscription group status. | 

 subscription.status.get | 
 /subscription/status/get | 
 Get subscription group status. | 

 subscription.groups.get | 
 /subscription/user/status | 
 Get status of subscription groups that specific users are explicitly subscribed and unsubscribed to. | 

 Permission | 
 Endpoint | 
 Description | 

 sms.invalid_phone_numbers | 
 /sms/invalid_phone_numbers | 
 Query for invalid phone numbers. | 

 sms.invalid_phone_numbers.remove | 
 /sms/invalid_phone_numbers/remove | 
 Remove the invalid phone number flag from users. | 

 Permission | 
 Endpoint | 
 Description | 

 catalogs.add_items | 
 /catalogs/{catalog_name}/items | 
 Add multiple items to an existing catalog. | 

 catalogs.update_items | 
 /catalogs/{catalog_name}/items | 
 Update multiple items in an existing catalog. | 

 catalogs.delete_items | 
 /catalogs/{catalog_name}/items | 
 Delete multiple items from an existing catalog. | 

 catalogs.get_item | 
 /catalogs/{catalog_name}/items/{item_id} | 
 Get a single item from an existing catalog. | 

 catalogs.update_item | 
 /catalogs/{catalog_name}/items/{item_id} | 
 Update a single item in an existing catalog. | 

 catalogs.create_item | 
 /catalogs/{catalog_name}/items/{item_id} | 
 Create a single item in an existing catalog. | 

 catalogs.delete_item | 
 /catalogs/{catalog_name}/items/{item_id} | 
 Delete a single item from an existing catalog. | 

 catalogs.replace_item | 
 /catalogs/{catalog_name}/items/{item_id} | 
 Replace a single item from an existing catalog. | 

 catalogs.create | 
 /catalogs | 
 Create a catalog. | 

 catalogs.get | 
 /catalogs | 
 Get a list of catalogs | 

 catalogs.delete | 
 /catalogs/{catalog_name} | 
 Delete a catalog. | 

 catalogs.get_items | 
 /catalogs/{catalog_name}/items | 
 Get items preview from an existing catalog. | 

 catalogs.replace_items | 
 /catalogs/{catalog_name}/items | 
 Replace items in an existing catalog. | 

 Permission | 
 Endpoint | 
 Description | 

 sdk_authentication.create | 
 /app_group/sdk_authentication/create | 
 Create a new SDK Authentication key for your app. | 

 sdk_authentication.primary | 
 /app_group/sdk_authentication/primary | 
 Mark an SDK Authentication key as the primary key for your app. | 

 sdk_authentication.delete | 
 /app_group/sdk_authentication/delete | 
 Delete an SDK Authentication key for your app. | 

 sdk_authentication.keys | 
 /app_group/sdk_authentication/keys | 
 Get all SDK Authentication keys for your app. | 

### Managing REST API keys

You can view details for or delete existing REST API keys from Settings > APIs and Identifiers > API Keys tab. Note that you cannot edit REST API keys after you create them.

The API Keys tab includes the following information for each key:

 Field | 
 Description | 

 API Key Name | 
 The name given to the key upon creation. | 

 Identifier | 
 The API key. | 

 Created By | 
 The email address of the user who created the key. This field shows as “N/A” for keys created before June 2023. | 

 Date Created | 
 The date this key was created. | 

 Last Seen | 
 The date this key was last used. This field shows as “N/A” for keys that have never been used. | 

To view the details of an API key, hover over the key and select View. This includes all the permissions this key has, whitelisted IPs (if any), and if this key is opted into Braze IP whitelisting.

Note when deleting a user, Braze does not delete the associated API keys that user created. To delete a key, hover over the key and select Delete.

### REST API key security

API keys are used to authenticate an API call. When you create a new REST API key, you need to give it access to specific endpoints. By assigning specific permissions to an API key, you can limit exactly which calls an API key can authenticate.

Given that REST API keys allow access to potentially sensitive REST API endpoints, secure these keys and only share them with trusted partners. They should never be publicly exposed. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.

A good security practice is to assign a user only as much access as is necessary to complete their job: this principle can also be applied to API keys by assigning permissions to each key. These permissions give you better security and control over the different areas of your account.

warning

Given that REST API keys allow access to potentially sensitive REST API endpoints, make sure they are stored and used securely. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.

If you accidentally expose a key, you can delete it from the Developer Console. For help with this process, open a support ticket.

### Security of REST API keys and SDK API keys

REST API keys and SDK API keys have different security profiles.

   | 
 REST API keys | 
 SDK API keys | 

 Purpose | 
 Server-side authentication for the REST API (sending messages, exporting data, managing users) | 
 Client-side identification for the Braze SDK (data ingestion, in-app messages, Content Cards) | 

 Visibility | 
 Must remain private. Never expose in client-side code, public repositories, or user applications. | 
 Designed to be public. Bundled inside your app binary or visible in web browser JavaScript, similar to a Google Analytics tracking ID. | 

 Solution if exposed | 
 Immediately revoke the key and create a replacement in Settings > APIs and Identifiers > API Keys. An exposed REST API key can be used to send messages, export user data, or modify account settings. | 
 No action required. An SDK API key can only ingest data and retrieve client-side messaging (such as in-app messages and Content Cards). It cannot export user data, send messages on your behalf, or modify campaigns. | 

### API IP allowlisting

For additional security, you can specify a list of IP addresses and subnets which are allowed to make REST API requests for a given REST API key. This is referred to as allowlisting, or whitelisting. To allow specific IP addresses or subnets, add them to the Whitelist IPs section when creating a new REST API key:

If you don’t specify any, requests can be sent from any IP address.

tip

If you’re making a Braze-to-Braze webhook and using allowlisting, see the list of IPs to whitelist.

## API authentication and security

### Bearer token authentication

Braze authenticates REST API requests using the REST API key passed as a Bearer token in the Authorization request header. When you send a request, include your API key in the following format:

```

1

```
 | 
```
Authorization: Bearer YOUR_REST_API_KEY

```
 | 

On each request, Braze performs the following server-side validation checks:

- Token validity: Verifies that the REST API key exists in Braze and is active (for example, not revoked or disabled).
 
- Token authorization: Confirms the API key has the required permissions for the requested endpoint.

If authentication fails, the API returns an error response with an HTTP status code. For example, 401 Unauthorized indicates an invalid or missing key, while 403 Forbidden indicates the key doesn’t have permission for the requested endpoint. For more information, see API errors.

### Request header casing

HTTP header names are case-insensitive, so Authorization and authorization are equivalent. The same applies to other standard request headers, such as Content-Type. Send whichever casing your HTTP client produces.

Braze also accepts any casing of the Bearer scheme (Bearer, bearer, or BEARER). Send the REST API key itself exactly as it was issued.

### Network-level security

REST API requests to Braze are protected by Transport Layer Security (TLS) encryption across the full request path. The following table describes the network flow for an API request from your server to Braze:

 Step | 
 Component | 
 Description | 

 1 | 
 Your server | 
 Initiates an HTTPS request with TLS encryption. | 

 2 | 
 Cloudflare | 
 Terminates the client TLS connection and applies network-level protections. | 

 3 | 
 Network Load Balancer (NLB) | 
 Forwards packets to the application infrastructure. NLBs operate at Layer 4, meaning there’s no Layer 7 proxying. Packets are forwarded without HTTP-level inspection or modification. | 

 4 | 
 NGINX ingress | 
 Terminates the internal TLS connection and routes the request. | 

 5 | 
 Unicorn (application server) | 
 Processes the authenticated request. | 

TLS encryption covers every link in the chain. Your server connects to Cloudflare over TLS, and Cloudflare establishes a separate TLS connection through the NLB to the NGINX ingress, so your API key and request data remain encrypted in transit.

## Additional resources

### Ruby client library

If you’re implementing Braze using Ruby, you can use the Ruby client library to reduce your data import time. A client library is a collection of code specific to one programming language—in this case, Ruby—that makes it easier to use an API.

The Ruby client library supports the User endpoints.

important

This client library is in beta. To help make this library better, send feedback to [email protected].

- 

New Stuff!
