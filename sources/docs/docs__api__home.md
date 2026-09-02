---
url: https://www.braze.com/docs/api/home
slug: docs__api__home
title: "Braze API Guide"
description: "Browse Braze REST API endpoints by type, with links to authentication, rate limits, and object reference documentation."
section: api/home
fetched: 2026-09-02
evidence: company-own (technical)
---
# Braze API Guide 

Braze provides a high-performance REST API to track users, send messages, export data, and manage campaigns, Canvases, catalogs, and more. Use this glossary to browse endpoints by type, open reference articles for request and response details, and find links to authentication, rate limits, and object documentation.

 API Overview

 API Identifier Types

 Objects & Filters

 Errors & Responses

 Data Retention

 Rate Limits

 Endpoint Search 
 Search endpoints
 Results update automatically as you type.
 
Select endpoint type to narrow the glossary:

 Apps

 Campaigns

 Canvas

 Catalogs

 Content Blocks

 Custom Events

 Data Objects

 Email List

 Email Templates

 Webhook Templates

 KPI

 Media Library

 Device Messaging API

 Purchases

 Preference Center

 Schedule Messages

 SCIM

 SDK Authentication

 Segments

 Send Messages

 SMS

 Subscription Groups

 User Data

 Live Activity

 Cloud Data Ingestion

Endpoint
 
Description

/v1/device-messaging/banners/sync 

Retrieve eligible Banners for a user and a set of placements.

/v1/device-messaging/banners/track 

Record impression and click events for Banners.

/apps/push_credential/update 

Update the push credentials for a single app.

/catalogs/{catalog_name}/fields/{field_name} 

Delete a field from a catalog.

/catalogs/{catalog_name}/fields/ 

Create multiple fields in a catalog.

/catalogs/{catalog_name}/items 

Delete multiple items in your catalog.

/catalogs/{catalog_name}/items 

Edit multiple items in your catalog.

/catalogs/{catalog_name}/items 

Create multiple items in your catalog.

/catalogs/{catalog_name}/items/ 

Replace multiple items in a catalog.

/catalogs/{catalog_name}/items/{item_id} 

Delete an item in a catalog.

/catalogs/{catalog_name}/items/{item_id} 

List a catalog item and its details.

/catalogs/{catalog_name}/items 

Return multiple catalog items and their content.

/catalogs/{catalog_name}/items/{item_id} 

Edit an item in a catalog.

/catalogs/{catalog_name}/items/{item_id} 

Create an item in a catalog.

/catalogs/{catalog_name}/items/{item_id} 

Replace an item in a catalog.

/catalogs/{catalog_name} 

Delete a catalog.

/catalogs 

List the catalogs in a workspace.

/catalogs 

Create a catalog.

/catalogs/{catalog_name}/selections/{selection_name} 

Delete a catalog selection.

/catalogs/{catalog_name}/selections 

Create a selection in a catalog.

/cdi/integrations 

Return a list of existing integrations.

/cdi/integrations/{integration_id}/job_sync_status 

Return a list of sync statuses.

/cdi/integrations/{integration_id}/sync 

Trigger a sync for a given integration.

/data_objects/* 

View the full Data Objects endpoint reference, including object types, objects, and relationship endpoints.

/data_objects/objects/{type_name}/{external_id}/object_relationships 

List, create, replace, update, and delete object-to-object relationships.

/data_objects/objects/{type_name}/{external_id} 

Get one data object, or replace, update, and delete it.

/data_objects/objects/{type_name} 

List data objects for a type.

/data_objects/types/{type_name} 

Get one data object type and its schema definition.

/data_objects/types 

List data object types in the workspace.

/data_objects/types/{type_name}/object_relationship_types 

List object relationship kinds for a data object type.

/data_objects/types/{type_name}/user_relationship_types 

List user relationship kinds for a data object type.

/data_objects/objects/{type_name}/{external_id}/user_relationships 

List user relationships for a data object.

/data_objects/objects/{type_name}/{external_id}/users 

Create, replace, update, and delete user-to-object relationships.

/email/hard_bounces 

Pull a list of email addresses that have "hard bounced" your email messages within a certain time frame.

/email/unsubscribes 

Return emails that have unsubscribed during the time period from start_date to end_date.

/email/blacklist 

Unsubscribe a user from email and mark them as hard bounced.

/email/status 

Set the email subscription state for your users.

/email/bounce/remove 

Remove email addresses from your Braze bounce list.

/email/spam/remove 

Remove email addresses from your Braze spam list.

/campaigns/data_series 

Retrieve a daily series of various stats for a campaign over time.

/campaigns/details 

Retrieve relevant information on a specified campaign.

/campaigns/list 

Export a list of campaigns, each of which includes its name, campaign API identifier, whether it is an API campaign, and tags associated with the campaign.

/sends/data_series 

Retrieve a daily series of various stats for a tracked send_id.

/canvas/data_series 

Export time series data for a Canvas.

/canvas/data_summary 

Export rollups of time series data for a Canvas, providing a concise summary of a Canvas' results.

/canvas/details 

Export metadata about a Canvas, such as the name, time created, current status, and more.

/canvas/list 

Export a list of Canvases, including the name, Canvas API identifier and associated tags.

/custom_attributes 

Export a list of custom attributes including the name, description, data type, array length (if applicable), status, and associated tags.

/events/list 

Export a list of names of custom events recorded for your app.

/events/data_series 

Retrieve a series of the number of occurrences of a custom event in your app over a designated time period.

/events 

Export a list of custom events including the name, description, status, associated tags, and analytics report inclusion.

/kpi/new_users/data_series 

Retrieve a daily series of the total number of new users on each date.

/kpi/dau/data_series 

Retrieve a daily series of the total number of unique active users on each date.

/kpi/mau/data_series 

Retrieve a daily series of the total number of unique active users over a 30-day rolling window.

/kpi/uninstalls/data_series 

Retrieve a daily series of the total number of uninstalls on each date.

/purchases/product_list 

Return a paginated lists of product IDs.

/purchases/quantity_series 

Return the total number of purchases in your app over a time range.

/purchases/revenue_series 

Return the total money spent in your app over a time range.

/segments/list 

Export a list of segments, each of which includes its name, Segment API identifier, and whether it has analytics tracking enabled.

/segments/data_series 

Retrieve a daily series of the estimated size of a segment over time.

/segments/details 

Retrieve relevant information on a segment.

/export/segment/cancel 

Cancel exports for the provided segment ID.

/sessions/data_series 

Retrieve a series of the number of sessions for your app over a designated time period.

/users/export/global_control_group 

Export all users within a Global Control Group.

/users/export/ids 

Export data from any user profile by specifying a user identifier.

/users/export/segment 

Export all the users within a segment.

/media_library/create 

Upload an asset to the media library.

/messages/live_activity/update 

Update an iOS Live Activity.

/messages/scheduled_broadcasts 

Return a JSON list of information about scheduled campaigns and entry Canvases between now and a designated end_time specified in the request.

/messages/schedule/delete 

Cancel a message that you previously scheduled before it has been sent.

/canvas/trigger/schedule/delete 

Cancel a Canvas message that you previously scheduled via API-triggered before it has been sent.

/campaigns/trigger/schedule/delete 

Cancel API-triggered campaign messages that you previously scheduled before it has been sent.

/messages/schedule/create 

Schedule a campaign, Canvas, or other message to be sent at a designated time.

/campaigns/trigger/schedule/create 

Send dashboard created campaign messages through API-triggered delivery.

/canvas/trigger/schedule/create 

Schedule Canvas messages through API-triggered delivery.

/messages/schedule/update 

Update scheduled messages. This endpoint accepts updates to either the schedule or messages parameter or both.

/campaigns/trigger/schedule/update 

Update scheduled API-triggered campaigns created in the dashboard.

/canvas/trigger/schedule/update 

Update scheduled API-triggered Canvases you created in the dashboard.

/sends/id/create 

Create send IDs to use for sending messages and tracking message performance programmatically, without campaign creation for each send.

/messages/send 

Send immediate, one-off messages to designated users through the Braze API.

/transactional/v1/campaigns/{CAMPAIGN_ID}/send 

Send immediate, one-off transactional messages to a designated user.

/campaigns/trigger/send 

Send immediate, one-off messages to designated users through API-triggered delivery. - Send Messages

/canvas/trigger/send 

Send Canvas messages through API-Triggered delivery. - Send Messages

/preference_center/v1/{preferenceCenterExternalId}/url/{userId} 

Create a URL for a preference center.

/preference_center/v1/list 

List available preference centers.

/preference_center/v1/{preferenceCenterExternalId} 

View the details for your preference center, including when it was created and updated.

/preference_center/v1 

Create a preference center to allow users to manage their notification preferences for email campaigns.

/preference_center/v1/{preferenceCenterExternalId} 

Update a preference center.

/app_group/sdk_authentication/delete 

Delete an SDK Authentication key for your app.

/app_group/sdk_authentication/keys 

List SDK Authentication keys for your app.

/app_group/sdk_authentication/create 

Create a new SDK Authentication key for your app.

/app_group/sdk_authentication/primary 

Set an SDK Authentication key as the primary key for your app.

/sms/invalid_phone_numbers 

Pull a list of phone numbers that Braze marked as "invalid" within a certain time frame.

/sms/invalid_phone_numbers/remove 

Remove "invalid" phone numbers from the invalid list in Braze. Use this to re-validate phone numbers after Braze marks them as invalid.

/subscription/status/get 

Get the subscription state of a user in a subscription group.

/subscription/user/status 

List and get the subscription groups of a certain user.

/subscription/status/set 

Batch update the subscription state of up to 50 users on the Braze dashboard.

/v2/subscription/status/set 

Batch update the subscription state of up to 50 users on the Braze dashboard.

/content_blocks/list 

List your existing Content Blocks information.

/content_blocks/info 

Call information for your existing email Content Block.

/content_blocks/create 

Create an email Content Block.

/content_blocks/update 

Update an email Content Block.

/templates/email/list 

Get a list of available email templates in your Braze account.

/templates/email/info 

Get information on your email templates.

/templates/email/create 

Create email templates on the Braze dashboard.

/templates/email/update 

Update email templates on the Braze dashboard.

/templates/webhook/translations/source 

View the default source translations for a webhook template.

/templates/webhook/translations 

View translations for a webhook template.

/templates/webhook/translations 

Update translations for a webhook template.

/users/external_ids/remove 

Remove your users' old deprecated external IDs.

/users/external_ids/rename 

Rename your users' external IDs.

/users/alias/new 

Add new user aliases for existing identified users, or to create new unidentified users.

/users/delete 

Delete any user profile by specifying a known user identifier.

/users/identify 

Identify an unidentified (alias-only) user.

/users/track 

Record custom events, purchases, and update user profile attributes.

/users/alias/update 

Update existing user alias names to new user alias names.

/users/merge 

Merge a user profile into another user.

/scim/v2/Users/{id} 

Permanently delete an existing dashboard user.

/scim/v2/Users?filter={[email protected]} 

Look up an existing dashboard user account by specifying their email.

/scim/v2/Users/{id} 

Look up an existing dashboard user account by specifying their resource ID.

/scim/v2/Users 

Create a new dashboard user account by specifying email, given and family names, permissions (for setting permissions at the company, workspace, and team level).

/scim/v2/Users/{id} 

Update an existing dashboard user account by specifying email, given and family names, permissions (for setting permissions at the company, workspace, and team level).

- 

New Stuff!
