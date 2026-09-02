---
url: https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables
slug: docs__user_guide__audience__segments__segment_extension__sql_segments__sql_segments_tables
title: "SQL table reference"
description: "This page is a reference of the Snowflake SQL tables and columns used across the Query Builder, SQL Segment Extensions, and Snowflake Data Sharing."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# SQL table reference

This page is a reference of the Snowflake SQL tables and columns available across the following Braze tools:

- Query Builder
 
- SQL Segment Extensions
 
- Snowflake Data Sharing

Most tables are available in all three tools. Tables marked Snowflake Data Sharing only are exclusive to Snowflake Data Sharing and are not accessible in Query Builder or SQL Segment Extensions.

tip

These SQL tables correspond to the events documented in the Currents event glossary. For example, the SQL table USERS_MESSAGES_EMAIL_SEND_SHARED corresponds to the Currents event users.messages.email.Send. If you need JSON event schemas or partner-specific formats (Amplitude, Mixpanel, Segment), refer to the Currents glossary.

## Table of contents

 Table | 
 Description | 

 AGENTCONSOLE_AGENTEXECUTED_SHARED | 
 When an Agent Console agent is executed (Snowflake Data Sharing only) | 

 AGENTCONSOLE_RAWLLMREQUEST_SHARED | 
 Raw information from each LLM call (Snowflake Data Sharing only) | 

 AGENTCONSOLE_TOOLINVOCATION_SHARED | 
 When a tool is executed (Snowflake Data Sharing only) | 

 USER_CUSTOM_ATTRIBUTES_VIEW_SHARED | 
 Periodic snapshot of custom profile attributes per user | 

 USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED | 
 Historical default profile attributes with effective date ranges | 

 USER_DEFAULT_ATTRIBUTES_VIEW_SHARED | 
 Periodic snapshot of default profile attributes per user | 

 USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED | 
 Near real-time default profile attributes per user | 

 USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED | 
 Historical custom profile attributes with effective date ranges (Snowflake Data Sharing only) | 

 USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED | 
 Near real-time custom profile attributes per user (Snowflake Data Sharing only) | 

 CATALOGS_ITEMS_SHARED | 
 Non-deleted catalog items | 

 CHANGELOGS_CAMPAIGN_SHARED | 
 When a campaign is changed (Snowflake Data Sharing only) | 

 CHANGELOGS_CANVAS_SHARED | 
 When a Canvas is changed (Snowflake Data Sharing only) | 

 CHANGELOGS_GLOBALCONTROLGROUP_SHARED | 
 When the Global Control Group is changed | 

 USERS_BEHAVIORS_CUSTOMEVENT_SHARED | 
 When a user performs a custom event | 

 USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED | 
 When a user installs an app and we attribute it to a partner | 

 USERS_BEHAVIORS_LOCATION_SHARED | 
 When a user records a location | 

 USERS_BEHAVIORS_PURCHASE_SHARED | 
 When a user makes a purchase | 

 USERS_BEHAVIORS_UNINSTALL_SHARED | 
 When a user uninstalls an app | 

 USERS_BEHAVIORS_UPGRADEDAPP_SHARED | 
 When a user upgrades the app | 

 USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED | 
 When a user has their first session | 

 USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED | 
 When a user views the News Feed | 

 USERS_BEHAVIORS_APP_SESSIONEND_SHARED | 
 When a user ends a session on an app | 

 USERS_BEHAVIORS_APP_SESSIONSTART_SHARED | 
 When a user begins a session on an app | 

 USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED | 
 When a user triggers a geofenced area—for example, by entering or exiting a geofence. This event is batched with other events and received through the standard events endpoint, so it may not appear in real time.

To log geofence activity in this table, select Enable Analytics for Enter and Enable Analytics for Exit in the advanced settings for each geofence. See step 3 in Manually create geofences for details. | 

 USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED | 
 When a user triggers a geofenced area (for example, when they enter or exit a geofence). This event was received through the dedicated geofence endpoint and is therefore received in real-time as soon as a user’s device detects that it has triggered a geofence. 

In addition, due to rate limiting on the geofence endpoint, it is possible that some geofence events are not reflected as a RecordEvent. All geofence events, however, are represented by DataEvent (but potentially with some delay due to batching). | 

 USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED | 
 When a Live Activity push-to-start token changes | 

 USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED | 
 When a Live Activity update token changes | 

 USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED | 
 When a push notification token state changes | 

 USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED | 
 When a user is subscribed or unsubscribed globally from a channel such as email | 

 USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED | 
 When a user is subscribed or unsubscribed to or from a subscription group | 

 USERS_CAMPAIGNS_CONVERSION_SHARED | 
 When a user converts for a campaign | 

 USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED | 
 When a user is enrolled in the control group for a campaign | 

 USERS_CAMPAIGNS_FREQUENCYCAP_SHARED | 
 When a user gets frequency capped for a campaign | 

 USERS_CAMPAIGNS_REVENUE_SHARED | 
 When a user generates revenue within the primary conversion period | 

 USERS_CANVASSTEP_PROGRESSION_SHARED | 
 When a user progresses to a Canvas step | 

 USERS_CANVAS_CONVERSION_SHARED | 
 When a user converts for a Canvas conversion event | 

 USERS_CANVAS_ENTRY_SHARED | 
 When a user enters a Canvas | 

 USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED | 
 When a user exits a Canvas because they match audience exit criteria | 

 USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED | 
 When a user exits a Canvas because they performed an exception event | 

 USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED | 
 When a user converts for a Canvas Experiment step | 

 USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED | 
 When a user enters an Experiment step path | 

 USERS_CANVAS_FREQUENCYCAP_SHARED | 
 When a user gets frequency capped for a Canvas step | 

 USERS_CANVAS_REVENUE_SHARED | 
 When a user generates revenue within the primary conversion event period | 

 USERS_MESSAGES_BANNER_ABORT_SHARED | 
 An originally scheduled banner message was aborted for some reason | 

 USERS_MESSAGES_BANNER_CLICK_SHARED | 
 When a user clicks a banner | 

 USERS_MESSAGES_BANNER_IMPRESSION_SHARED | 
 When a user views a banner | 

 USERS_MESSAGES_CONTENTCARD_ABORT_SHARED | 
 An originally scheduled Content Card message was aborted for some reason. | 

 USERS_MESSAGES_CONTENTCARD_CLICK_SHARED | 
 When a user clicks a Content Card | 

 USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED | 
 When a user dismisses a Content Card | 

 USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED | 
 When a user views a Content Card | 

 USERS_MESSAGES_CONTENTCARD_SEND_SHARED | 
 When we send a Content Card to a user | 

 USERS_MESSAGES_EMAIL_ABORT_SHARED | 
 An originally scheduled email message was aborted for some reason. | 

 USERS_MESSAGES_EMAIL_BOUNCE_SHARED | 
 An Email Service Provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure. | 

 USERS_MESSAGES_EMAIL_CLICK_SHARED | 
 When a user clicks a link in an email | 

 USERS_MESSAGES_EMAIL_DEFERRAL_SHARED | 
 When an email is deferred | 

 USERS_MESSAGES_EMAIL_DELIVERY_SHARED | 
 When an email is delivered | 

 USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED | 
 When an email is marked as spam | 

 USERS_MESSAGES_EMAIL_OPEN_SHARED | 
 When a user opens an email | 

 USERS_MESSAGES_EMAIL_SEND_SHARED | 
 When we send an email to a user | 

 USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED | 
 When an email soft bounces | 

 USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED | 
 When a user unsubscribes from email | 

 USERS_MESSAGES_EMAIL_RETRY_SHARED | 
 When an email message is retried after being deprioritized or frequency capped (Snowflake Data Sharing only) | 

 USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED | 
 When a user views a feature flag | 

 USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED | 
 An originally scheduled in-app message was aborted for some reason. | 

 USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED | 
 When a user clicks an in-app message | 

 USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED | 
 When a user views an in-app message | 

 USERS_MESSAGES_LINE_ABORT_SHARED | 
 When a scheduled LINE message cannot be delivered, before sending to LINE | 

 USERS_MESSAGES_LINE_CLICK_SHARED | 
 When a user clicks a link in a LINE message | 

 USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED | 
 When a LINE message is received from a user | 

 USERS_MESSAGES_LINE_SEND_SHARED | 
 When a LINE message is sent to LINE | 

 USERS_MESSAGES_LINE_RETRY_SHARED | 
 When a LINE message is retried after being deprioritized or frequency capped (Snowflake Data Sharing only) | 

 USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED | 
 When a Live Activity has an outcome event | 

 USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED | 
 When a Live Activity message is sent | 

 USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED | 
 An originally scheduled News Feed card message was aborted for some reason | 

 USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED | 
 When a user clicks a News Feed card | 

 USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED | 
 When a user views a News Feed card | 

 USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED | 
 An originally scheduled push notification message was aborted for some reason. | 

 USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED | 
 When a push notification bounces | 

 USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED | 
 When a user opens the app after receiving a notification without clicking on the notification | 

 USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED | 
 When a user receives a push notification while the app is open. 

This event is not supported by the Swift SDK and is deprecated in the Obj-C SDK. | 

 USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED | 
 When a user opens a push notification or clicks a push notification button (including a CLOSE button that does NOT open the app). 

 Push button actions have multiple outcomes. No, Decline, and Cancel actions are “clicks”, and Accept actions are “opens”. Both are represented in this table, but they can be distinguished in the BUTTON_ACTION_TYPE column. For example, a query can be used to group by a BUTTON_ACTION_TYPE that is not No, Decline, or Cancel. | 

 USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED | 
 When we send a push notification to a user | 

 USERS_MESSAGES_RCS_ABORT_SHARED | 
 When an RCS send is interrupted due to an error detected within Braze and the message is dropped | 

 USERS_MESSAGES_RCS_CLICK_SHARED | 
 When the end user interacts with an RCS message by tapping or clicking on a UI element | 

 USERS_MESSAGES_RCS_DELIVERY_SHARED | 
 When an RCS message is successfully delivered to an end user’s mobile device | 

 USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED | 
 When Braze receives an RCS message that originates from the end user | 

 USERS_MESSAGES_RCS_READ_SHARED | 
 When the end user opens an RCS message on their device | 

 USERS_MESSAGES_RCS_REJECTION_SHARED | 
 When an RCS message fails to be delivered due to intervention by the carrier | 

 USERS_MESSAGES_RCS_SEND_SHARED | 
 When an RCS message is sent out of Braze’s systems to last-mile delivery partners | 

 USERS_MESSAGES_SMS_ABORT_SHARED | 
 An originally scheduled SMS message was aborted for some reason. | 

 USERS_MESSAGES_SMS_CARRIERSEND_SHARED | 
 When an SMS message is sent to the carrier | 

 USERS_MESSAGES_SMS_DELIVERY_SHARED | 
 When an SMS message is delivered | 

 USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED | 
 When Braze is unable to deliver the SMS message to the SMS service provider | 

 USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED | 
 When an SMS message is received from a user | 

 USERS_MESSAGES_SMS_REJECTION_SHARED | 
 When an SMS message is not delivered to a user | 

 USERS_MESSAGES_SMS_SEND_SHARED | 
 When an SMS message is sent | 

 USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED | 
 When a user clicks a Braze shortened URL included in an SMS message | 

 USERS_MESSAGES_SMS_RETRY_SHARED | 
 When an SMS message is retried after being deprioritized or frequency capped (Snowflake Data Sharing only) | 

 USERS_MESSAGES_WEBHOOK_ABORT_SHARED | 
 An originally scheduled webhook message was aborted for some reason | 

 USERS_MESSAGES_WEBHOOK_FAILURE_SHARED | 
 When a webhook message is delivered but fails with an error response from the endpoint | 

 USERS_MESSAGES_WEBHOOK_SEND_SHARED | 
 When we send a webhook for a user | 

 USERS_MESSAGES_WEBHOOK_RETRY_SHARED | 
 When a webhook message is retried after being deprioritized or frequency capped (Snowflake Data Sharing only) | 

 USERS_MESSAGES_WHATSAPP_ABORT_SHARED | 
 An originally scheduled WhatsApp message was aborted for some reason | 

 USERS_MESSAGES_WHATSAPP_CLICK_SHARED | 
 When a user clicks a link or button in a WhatsApp message | 

 USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED | 
 When a WhatsApp message is delivered | 

 USERS_MESSAGES_WHATSAPP_FAILURE_SHARED | 
 When a WhatsApp message is not delivered to a user | 

 USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED | 
 When a WhatsApp message is received from a user | 

 USERS_MESSAGES_WHATSAPP_READ_SHARED | 
 When a user opens a WhatsApp message | 

 USERS_MESSAGES_WHATSAPP_SEND_SHARED | 
 When we send a WhatsApp message for a user | 

 USERS_MESSAGES_WHATSAPP_RETRY_SHARED | 
 When a WhatsApp message is retried after being deprioritized or frequency capped (Snowflake Data Sharing only) | 

 USERS_RANDOMBUCKETNUMBERUPDATE_SHARED | 
 When a user’s random bucket number is changed | 

 USERS_USERDELETEREQUEST_SHARED | 
 When a user is deleted by a customer request | 

 USERS_USERORPHAN_SHARED | 
 When a user is merged with another user’s profile and the original profile is orphaned | 

 SNAPSHOTS_APP_SHARED | 
 App snapshots (Snowflake Data Sharing only) | 

 SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED | 
 Campaign message variation snapshots (Snowflake Data Sharing only) | 

 SNAPSHOTS_CANVAS_FLOW_STEP_SHARED | 
 Canvas Flow step snapshots (Snowflake Data Sharing only) | 

 SNAPSHOTS_CANVAS_STEP_SHARED | 
 Canvas step snapshots (Snowflake Data Sharing only) | 

 SNAPSHOTS_CANVAS_VARIATION_SHARED | 
 Canvas variation snapshots (Snowflake Data Sharing only) | 

 SNAPSHOTS_EXPERIMENT_STEP_SHARED | 
 Experiment step snapshots (Snowflake Data Sharing only) | 

## Agent Console

note

Agent Console tables are available in Snowflake Data Sharing only.

### AGENTCONSOLE_AGENTEXECUTED_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 invocation_id | 
 string | 
 Globally unique ID for this message | 

 request_id | 
 string | 
 Unique ID for this overall LLM request and complete execution | 

 duration | 
 int | 
 Duration of the session in seconds | 

 prompt_tokens | 
 int | 
 How many prompt tokens this request used | 

 completion_tokens | 
 int | 
 How many completion tokens this request used | 

 total_tokens | 
 int | 
 How many total tokens this request used | 

 cache_tokens | 
 int | 
 How many cached tokens this request used | 

 reasoning_tokens | 
 int | 
 How many reasoning tokens this request used | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 agent_id | 
 string | 
 BSON ID of the CustomerDefinedAgent | 

 agent_name | 
 string | 
 Name of the CustomerDefinedAgent | 

 model_provider | 
 string | 
 Name of the LLM model provider | 

 model_name | 
 string | 
 Name of the LLM model used in this request | 

 provider_request_id | 
 string | 
 Any request ID given by the model provider for the API call | 

 cache_hit | 
 boolean | 
 Whether this request hit the cache to return the response | 

 llm_owned_by_customer | 
 boolean | 
 If true, the customer’s API key was used; if false, Braze’s key was used | 

 is_error | 
 boolean | 
 Whether this request errored out | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 user_id | 
 string | 
 [PII] Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 input | 
 null, string | 
 [PII] Input to the LLM | 

 output | 
 null, string | 
 [PII] Response from the LLM | 

 invocation_source | 
 null, string | 
 Which ruby object invoked the LLM request | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### AGENTCONSOLE_RAWLLMREQUEST_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 invocation_id | 
 string | 
 Globally unique ID for this message | 

 request_id | 
 string | 
 Unique ID for this overall LLM request and complete execution | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this event belongs to | 

 agent_id | 
 string | 
 BSON ID of the CustomerDefinedAgent | 

 agent_name | 
 string | 
 Name of the CustomerDefinedAgent | 

 model_provider | 
 string | 
 Name of the LLM model provider | 

 model_name | 
 string | 
 Name of the LLM model used in this request | 

 duration | 
 int, null | 
 Duration of the session in seconds | 

 request | 
 string | 
 [PII] Prompt used in the request | 

 http_status_code | 
 int, null | 
 HTTP status code of the response | 

 response_body | 
 string, null | 
 [PII] Response from the LLM | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### AGENTCONSOLE_TOOLINVOCATION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 tool_call_id | 
 string | 
 Globally unique ID for this tool call | 

 duration | 
 int | 
 Duration of the session in seconds | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 agent_id | 
 string | 
 BSON ID of the CustomerDefinedAgent | 

 agent_name | 
 string | 
 Name of the CustomerDefinedAgent | 

 is_error | 
 boolean | 
 Whether this request errored out | 

 tool_name | 
 string | 
 Name of the tool | 

 tool_arguments | 
 null, string | 
 [PII] JSON of the tool arguments | 

 invocation_source | 
 null, string | 
 Which ruby object invoked the LLM request | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

## User profile attribute views

### USER_CUSTOM_ATTRIBUTES_VIEW_SHARED

 Field | 
 Type | 
 Description | 

 app_group_id | 
 string | 
 BSON ID of the workspace | 

 app_id | 
 string | 
 BSON ID of the app | 

 user_id | 
 string | 
 [PII] Braze user ID | 

 time | 
 int | 
 UNIX timestamp in seconds of the profile update (for backfilled rows, the time of the backfill) | 

 time_ms | 
 int | 
 UNIX timestamp in milliseconds of the profile update (for backfilled rows, the time of the backfill) | 

 update_source | 
 string | 
 Source of the update to the profile | 

 sf_updated_at | 
 timestamp | 
 When this row was updated in Snowflake | 

 custom_attributes | 
 variant | 
 [PII] Custom attributes as a JSON object | 

### USER_DEFAULT_ATTRIBUTES_VIEW_SHARED

 Field | 
 Type | 
 Description | 

 app_group_id | 
 string | 
 BSON ID of the workspace | 

 app_id | 
 string | 
 BSON ID of the app | 

 user_id | 
 string | 
 [PII] Braze user ID | 

 time | 
 int | 
 UNIX timestamp in seconds of the profile update (for backfilled rows, the time of the backfill) | 

 time_ms | 
 int | 
 UNIX timestamp in milliseconds of the profile update (for backfilled rows, the time of the backfill) | 

 update_source | 
 string | 
 Source of the update to the profile | 

 sf_updated_at | 
 timestamp | 
 When this row was updated in Snowflake | 

 external_user_id | 
 string | 
 [PII] External ID for the user | 

 first_name | 
 string | 
 [PII] First name | 

 last_name | 
 string | 
 [PII] Last name | 

 email_address | 
 string | 
 [PII] Email address | 

 gender | 
 string | 
 [PII] Gender | 

 phone_number | 
 string | 
 [PII] Phone number | 

 dob | 
 string | 
 [PII] Date of birth | 

 TIME_ZONE | 
 string | 
 [PII] Time zone | 

 home_city | 
 string | 
 [PII] Home city | 

 country | 
 string | 
 [PII] Country | 

 language | 
 string | 
 [PII] Language | 

### USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED

 Field | 
 Type | 
 Description | 

 app_group_id | 
 string | 
 BSON ID of the workspace | 

 user_id | 
 string | 
 [PII] Braze user ID | 

 app_id | 
 string | 
 BSON ID of the app | 

 time | 
 int | 
 UNIX timestamp in seconds of the profile update (for backfilled rows, the time of the backfill) | 

 time_ms | 
 int | 
 UNIX timestamp in milliseconds of the profile update (for backfilled rows, the time of the backfill) | 

 update_source | 
 string | 
 Source of the update to the profile | 

 sf_updated_at | 
 timestamp | 
 When this row was updated in Snowflake | 

 external_user_id | 
 string | 
 [PII] External ID for the user | 

 first_name | 
 string | 
 [PII] First name | 

 last_name | 
 string | 
 [PII] Last name | 

 email_address | 
 string | 
 [PII] Email address | 

 gender | 
 string | 
 [PII] Gender | 

 phone_number | 
 string | 
 [PII] Phone number | 

 dob | 
 string | 
 [PII] Date of birth | 

 TIME_ZONE | 
 string | 
 [PII] Time zone | 

 home_city | 
 string | 
 [PII] Home city | 

 country | 
 string | 
 [PII] Country | 

 language | 
 string | 
 [PII] Language | 

 eff_dt | 
 timestamp | 
 Start of the interval when this attribute state was current | 

 end_dt | 
 timestamp | 
 End of that interval | 

### USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED

 Field | 
 Type | 
 Description | 

 app_group_id | 
 string | 
 BSON ID of the workspace | 

 app_id | 
 string | 
 BSON ID of the app | 

 user_id | 
 string | 
 [PII] Braze user ID | 

 time | 
 int | 
 UNIX timestamp in seconds of the profile update (for backfilled rows, the time of the backfill) | 

 time_ms | 
 int | 
 UNIX timestamp in milliseconds of the profile update (for backfilled rows, the time of the backfill) | 

 update_source | 
 string | 
 Source of the update to the profile | 

 sf_updated_at | 
 timestamp | 
 When this row was updated in Snowflake | 

 external_user_id | 
 string | 
 [PII] External ID for the user | 

 first_name | 
 string | 
 [PII] First name | 

 last_name | 
 string | 
 [PII] Last name | 

 email_address | 
 string | 
 [PII] Email address | 

 gender | 
 string | 
 [PII] Gender | 

 phone_number | 
 string | 
 [PII] Phone number | 

 dob | 
 string | 
 [PII] Date of birth | 

 home_city | 
 string | 
 [PII] Home city | 

 country | 
 string | 
 [PII] Country | 

 language | 
 string | 
 [PII] Language | 

 TIME_ZONE | 
 string | 
 [PII] Time zone | 

### USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

 Column name | 
 Data type | 
 Description | 

 APP_GROUP_ID | 
 VARCHAR | 
 Your Braze workspace identifier | 

 USER_ID | 
 VARCHAR | 
 The unique Braze user identifier | 

 APP_ID | 
 VARCHAR | 
 The specific app within your workspace | 

 EXTERNAL_USER_ID | 
 VARCHAR | 
 Your own user identifier (if set) | 

 TIME | 
 NUMBER | 
 Unix timestamp (seconds) of the profile update | 

 TIME_MS | 
 NUMBER | 
 Unix timestamp (milliseconds) of the profile update | 

 UPDATE_SOURCE | 
 VARCHAR | 
 The source of the attribute update (API, SDK, dashboard, etc.) | 

 SF_UPDATED_AT | 
 TIMESTAMP_NTZ | 
 When the data was last updated in Snowflake | 

 CUSTOM_ATTRIBUTES | 
 VARIANT | 
 JSON object containing all custom attributes (key-value pairs) | 

 ARCHIVED | 
 BOOLEAN | 
 Whether the user profile is archived | 

 EFF_DT | 
 TIMESTAMP_NTZ | 
 Effective date: when this attribute state began | 

 END_DT | 
 TIMESTAMP_NTZ | 
 End date: when this attribute state ended (NULL for current state) | 

For usage guidance and example queries, see Snowflake user attributes.

### USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

 Column name | 
 Data type | 
 Description | 

 APP_GROUP_ID | 
 VARCHAR | 
 Your Braze workspace identifier | 

 USER_ID | 
 VARCHAR | 
 The unique Braze user identifier | 

 EXTERNAL_USER_ID | 
 VARCHAR | 
 Your own user identifier (if set) | 

 TIME | 
 NUMBER | 
 Unix timestamp (seconds) of the profile update | 

 TIME_MS | 
 NUMBER | 
 Unix timestamp (milliseconds) of the profile update | 

 UPDATE_SOURCE | 
 VARCHAR | 
 The source of the attribute update (API, SDK, dashboard, etc.) | 

 ARCHIVED | 
 BOOLEAN | 
 Whether the user profile is archived | 

 SF_UPDATED_AT | 
 TIMESTAMP_NTZ | 
 When the data was last updated in Snowflake | 

 APP_ID | 
 VARCHAR | 
 The specific app within your workspace | 

 CUSTOM_ATTRIBUTES | 
 OBJECT | 
 JSON object containing all custom attributes (key-value pairs) | 

note

This view uses OBJECT type for CUSTOM_ATTRIBUTES instead of VARIANT. Use the same JSON accessor syntax (:attribute_name::TYPE) to query individual attributes.

For usage guidance and example queries, see Snowflake user attributes.

## Catalogs

### CATALOGS_ITEMS_SHARED

 Field | 
 Type | 
 Description | 

 catalog_id | 
 string | 
 BSON ID of the catalog | 

 item_id | 
 string | 
 BSON ID of the catalog item | 

 app_group_id | 
 null, string | 
 BSON ID of the app group | 

 app_group_api_id | 
 null, string | 
 API ID of the app group | 

 field_name | 
 null, string | 
 Name of the field | 

 field_value | 
 null, string | 
 Value of the field | 

## Changelogs

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 random_bucket_number | 
 null, int | 
 New random bucket number | 

 global_control_group | 
 null, boolean | 
 With this change, the bucket number is included as global control group | 

 previous_global_control_group | 
 null, boolean | 
 Before this change the bucket number was included as global control group but it no longer is | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### CHANGELOGS_CAMPAIGN_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 api_id | 
 string | 
 API ID of the campaign | 

 name | 
 null, string | 
 Name of the campaign | 

 conversion_behaviors | 
 null, string | 
 Conversion behaviors for the campaign | 

 actions | 
 null, string | 
 Actions for the campaign | 

### CHANGELOGS_CANVAS_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 api_id | 
 string | 
 API ID of the Canvas | 

 name | 
 null, string | 
 Name of the Canvas | 

 conversion_behaviors | 
 null, string | 
 Conversion behaviors for the Canvas | 

 variations | 
 null, string | 
 Variations for the Canvas | 

## Behaviors

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed the event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this action occurred | 

 time | 
 int | 
 Unix timestamp at which the user performed the event | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the custom event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 name | 
 string | 
 Name of the custom event | 

 properties | 
 string | 
 Custom properties of the event stored as a JSON encoded string | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that installed | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the user installed | 

 source | 
 string | 
 the source of the attribution | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_LOCATION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that records the location | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this location was recorded | 

 time | 
 int | 
 Unix timestamp at which the location was recorded | 

 latitude | 
 float | 
 [PII] Latitude of recorded location | 

 longitude | 
 float | 
 [PII] Longitude of recorded location | 

 altitude | 
 null, float | 
 [PII] altitude of recorded location | 

 ll_accuracy | 
 null, float | 
 latitude and longitude accuracy of recorded location | 

 alt_accuracy | 
 null, float | 
 altitude accuracy of recorded location | 

 device_id | 
 null, string | 
 ID of the device on which the location was recorded | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use when the location was recorded | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_PURCHASE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that made a purchase | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which the purchase occurred | 

 time | 
 int | 
 Unix timestamp at which the user made the purchase | 

 device_id | 
 null, string | 
 ID of the device on which the purchase occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the purchase | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 product_id | 
 string | 
 ID of the product purchased | 

 price | 
 float | 
 Price of the purchase | 

 currency | 
 string | 
 Currency of the purchase | 

 properties | 
 string | 
 Custom properties of the purchase stored as a JSON encoded string | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_UNINSTALL_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that uninstalled | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app that was uninstalled | 

 time | 
 int | 
 Unix timestamp at which the user uninstalled | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that upgraded the app | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app the user upgraded | 

 time | 
 int | 
 Unix timestamp at which the user upgraded the app | 

 device_id | 
 null, string | 
 ID of the device on which the user upgraded the app | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 old_app_version | 
 null, string | 
 Old version of the app | 

 new_app_version | 
 null, string | 
 New version of the app | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performs this action | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this session occurred | 

 time | 
 int | 
 Unix timestamp at which the session started | 

 session_id | 
 string | 
 UUID of the session | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the session occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the session | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performs this action | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this session occurred | 

 time | 
 int | 
 Unix timestamp at which the session ended | 

 duration | 
 null, float | 
 Duration of the session in seconds | 

 session_id | 
 string | 
 UUID of the session | 

 device_id | 
 null, string | 
 ID of the device on which the session occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the session | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performs this action | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_api_id | 
 null, string | 
 API ID of the app on which this session occurred | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the session started | 

 session_id | 
 string | 
 UUID of the session | 

 device_id | 
 null, string | 
 ID of the device on which the session occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the session | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed the event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this action occurred | 

 time | 
 int | 
 Unix timestamp at which the user performed the event | 

 device_id | 
 null, string | 
 ID of the device on which the custom event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 event_type | 
 string | 
 What kind of geofence event was triggered. (for example, ‘enter’ or ‘exit’) | 

 location_set_id | 
 string | 
 The ID of the location set of the geofence that was triggered | 

 geofence_id | 
 string | 
 The ID of the geofence that was triggered | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed the event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this action occurred | 

 time | 
 int | 
 Unix timestamp at which the user performed the event | 

 device_id | 
 null, string | 
 ID of the device on which the custom event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 event_type | 
 string | 
 What kind of geofence event was triggered. (for example, ‘enter’ or ‘exit’) | 

 location_set_id | 
 string | 
 The ID of the location set of the geofence that was triggered | 

 geofence_id | 
 string | 
 The ID of the geofence that was triggered | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 activity_attributes_type | 
 null, string | 
 Live Activity attribute type | 

 push_to_start_token | 
 null, string | 
 Live Activity push to start token | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 ios_push_token_apns_gateway | 
 null, int | 
 APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production | 

 push_token_state_change_type | 
 null, string | 
 A description of the push token state change type | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 activity_id | 
 null, string | 
 Live Activity identifier | 

 update_token | 
 null, string | 
 Live Activity update token | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 ios_push_token_apns_gateway | 
 null, int | 
 APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production | 

 push_token_state_change_type | 
 null, string | 
 A description of the push token state change type | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 time_ms | 
 int | 
 Time in milliseconds when the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 push_token | 
 null, string | 
 Push token of the event | 

 push_token_created_at | 
 null, int | 
 UNIX timestamp at which the push token was created | 

 push_token_updated_at | 
 null, int | 
 UNIX timestamp at which the push token was last updated | 

 push_token_foreground_push_disabled | 
 null, boolean | 
 Foreground push disabled flag of the push token | 

 push_token_device_id | 
 null, string | 
 Device id of the push token | 

 push_token_provisionally_opted_in | 
 null, boolean | 
 Provisionally opted in flag of the push token | 

 ios_push_token_apns_gateway | 
 null, int | 
 APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production | 

 web_push_token_public_key | 
 null, string | 
 Public key of the push token, only applies to web push tokens | 

 web_push_token_user_auth | 
 null, string | 
 User auth of the push token, only applies to web push tokens | 

 web_push_token_vapid_public_key | 
 null, string | 
 VAPID public key of the push token, only applies to web push tokens | 

 push_token_state_change_type | 
 null, string | 
 A description of the push token state change type | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user affected | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 email_address | 
 null, string | 
 [PII] email address of the user | 

 state_change_source | 
 null, string | 
 source of the state change (REST, SDK, Dashboard, etc) | 

 subscription_status | 
 string | 
 Subscription status: ‘Subscribed’, ‘Unsubscribed’ or ‘Opted In’ | 

 channel | 
 null, string | 
 Channel of the global subscription state such as email | 

 time | 
 int | 
 Unix timestamp at which the subscription state changed | 

 timezone | 
 null, string | 
 Time zone of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app the event belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this event belongs to | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 send_id | 
 null, string | 
 Message send ID this subscription state change action originated from | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 channel_identifier | 
 null, string | 
 [PII] The user’s identifier on the channel the event is for. | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user affected | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 email_address | 
 null, string | 
 [PII] email address of the user | 

 phone_number | 
 null, string | 
 [PII] phone number of the user in e164 format | 

 app_api_id | 
 null, string | 
 API ID of the app the event belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this event belongs to | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 channel | 
 null, string | 
 Channel: ‘email’ or ‘sms’, depending on the channel type of the subscription group | 

 subscription_status | 
 string | 
 Subscription status: ‘Subscribed’, ‘Unsubscribed’ or ‘Opted In’ | 

 time | 
 int | 
 Unix timestamp at which the subscription state changed | 

 timezone | 
 null, string | 
 Time zone of the user | 

 send_id | 
 null, string | 
 Message send ID this subscription state change action originated from | 

 state_change_source | 
 null, string | 
 Source of the state change (REST, SDK, Dashboard, etc) | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 channel_identifier | 
 null, string | 
 [PII] The user’s identifier on the channel the event is for. | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

## Campaigns

### USERS_CAMPAIGNS_CONVERSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 conversion_behavior_index | 
 null, int | 
 Index of the conversion behavior | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 channel | 
 null, string | 
 Channel this event belongs to | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_CAMPAIGNS_REVENUE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 revenue | 
 long | 
 The amount of USD revenue in cents generated | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 device_id | 
 string, null | 
 ID of the device that is tied to this user, if the user is anonymous | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 progression_type | 
 string, null | 
 Type of step progression event | 

 is_canvas_entry | 
 boolean, null | 
 Whether this is entry into a first step in a Canvas | 

 exit_reason | 
 string, null | 
 If this is an exit, the reason a user exited the canvas during the step | 

 canvas_entry_id | 
 string, null | 
 Unique identifier for this instance of a user in a Canvas | 

 next_step_id | 
 string, null | 
 BSON ID of the next step in the canvas | 

 next_step_api_id | 
 string, null | 
 API ID of the next step in the Canvas | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_CANVAS_CONVERSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 device_id | 
 string, null | 
 ID of the device that is tied to this user, if the user is anonymous | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 string, null | 
 API ID of the app on which this event occurred | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 string, null | 
 API ID of the Canvas step message variation this user received | 

 conversion_behavior_index | 
 int, null | 
 Type of conversion event the user performed where “0” is a primary conversion and “1” is a secondary conversion | 

 gender | 
 string, null | 
 [PII] Gender of the user | 

 country | 
 string, null | 
 [PII] Country of the user | 

 timezone | 
 string, null | 
 Time zone of the user | 

 language | 
 string, null | 
 [PII] Language of the user | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_CANVAS_ENTRY_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 device_id | 
 string, null | 
 ID of the device that is tied to this user, if the user is anonymous | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 [Deprecated] API ID of the Canvas step this event belongs to | 

 gender | 
 string, null | 
 [PII] Gender of the user | 

 country | 
 string, null | 
 [PII] Country of the user | 

 timezone | 
 string, null | 
 Time zone of the user | 

 language | 
 string, null | 
 [PII] Language of the user | 

 in_control_group | 
 boolean, null | 
 True if the user was enrolled in the control group | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 string, null | 
 API ID of the app on which this event occurred | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 experiment_step_api_id | 
 string, null | 
 API ID of the Experiment step this event belongs to | 

 conversion_behavior_index | 
 int, null | 
 Type of conversion event the user performed where “0” is a primary conversion and “1” is a secondary conversion | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 experiment_split_api_id | 
 string, null | 
 API ID of the experiment split the user enrolled in | 

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 experiment_step_api_id | 
 string, null | 
 API ID of the Experiment step this event belongs to | 

 in_control_group | 
 boolean, null | 
 True if the user was enrolled in the control group | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 experiment_split_api_id | 
 string, null | 
 API ID of the experiment split the user enrolled in | 

### USERS_CANVAS_FREQUENCYCAP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 device_id | 
 string, null | 
 ID of the device that is tied to this user, if the user is anonymous | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 string, null | 
 API ID of the Canvas step message variation this user received | 

 channel | 
 string, null | 
 Messaging Channel this event belongs to (email, push, etc.) | 

 gender | 
 string, null | 
 [PII] Gender of the user | 

 country | 
 string, null | 
 [PII] Country of the user | 

 timezone | 
 string, null | 
 Time zone of the user | 

 language | 
 string, null | 
 [PII] Language of the user | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_CANVAS_REVENUE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 device_id | 
 string, null | 
 ID of the device that is tied to this user, if the user is anonymous | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 canvas_id | 
 string, null | 
 (For Braze use only) ID of the Canvas this event belongs to | 

 canvas_api_id | 
 string, null | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 string, null | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 string, null | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 string, null | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 string, null | 
 [PII] Gender of the user | 

 country | 
 string, null | 
 [PII] Country of the user | 

 timezone | 
 string, null | 
 Time zone of the user | 

 language | 
 string, null | 
 [PII] Language of the user | 

 revenue | 
 int, null | 
 Amount of revenue generated in USD, displayed as cents | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 app_api_id | 
 string, null | 
 API ID of the app on which this event occurred | 

## Messages

### USERS_MESSAGES_BANNER_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Device browser - extracted from user_agent - on which the open occurred | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of [‘ios_idfa’, ‘google_ad_id’, ‘windows_ad_id’, ‘roku_ad_id’] | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (up to 128 chars) | 

 banner_placement_id | 
 null, string | 
 Customer specified banner placement ID | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_BANNER_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Device browser - extracted from user_agent - on which the open occurred | 

 button_id | 
 null, string | 
 ID of the button clicked, if this click represents a click on a button | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of [‘ios_idfa’, ‘google_ad_id’, ‘windows_ad_id’, ‘roku_ad_id’] | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 banner_placement_id | 
 null, string | 
 Customer specified banner placement ID | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_BANNER_IMPRESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Device browser - extracted from user_agent - on which the open occurred | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of [‘ios_idfa’, ‘google_ad_id’, ‘windows_ad_id’, ‘roku_ad_id’] | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 banner_placement_id | 
 null, string | 
 Customer specified banner placement ID | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (maximum of 2,000 characters) | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 content_card_id | 
 string | 
 ID of the card that generated this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Browser of the device | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 content_card_id | 
 string | 
 ID of the card that generated this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Browser of the device | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 content_card_id | 
 string | 
 ID of the card that generated this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Browser of the device | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 content_card_id | 
 string | 
 ID of the card that generated this event | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during liquid rendering | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (maximum of 2,000 characters) | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 sending_ip | 
 null, string | 
 IP address from which the email send was made | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 bounce_reason | 
 null, string | 
 [PII] The SMTP reason code and user friendly message received for this bounce event | 

 esp | 
 null, string | 
 ESP related to the event (SparkPost, SendGrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 is_drop | 
 null, boolean | 
 Indicates that this event counts as a drop event | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

note

You may see multiple rows for the same user around a single hard bounce. That can happen when events are processed asynchronously or when related sends have different dispatch_id values. When deduplicating or analyzing exports, consider dispatch_id, time, and id together.

### USERS_MESSAGES_EMAIL_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 url | 
 null, string | 
 URL that the user clicked on | 

 user_agent | 
 null, string | 
 User agent on which the click occurred | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 link_id | 
 null, string | 
 Unique ID for the link which was clicked, as created by Braze | 

 link_alias | 
 null, string | 
 Alias associated with this link ID | 

 esp | 
 null, string | 
 ESP related to the event (SparkPost, SendGrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 is_amp | 
 null, boolean | 
 Indicates that this is an AMP event | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 is_suspected_bot_click | 
 null, boolean | 
 Whether this event was processed as a bot event | 

 suspected_bot_click_reason | 
 null, object | 
 Why this event was classified as a bot | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 email_address | 
 null, string | 
 [PII] Email address of the user | 

 recipient_domain | 
 null, string | 
 Receipient’s email domain | 

 esp | 
 null, string | 
 ESP related to the event (Sparkpost or Sendgrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 ip_pool | 
 null, string | 
 IP pool from which the email send was made | 

 sending_ip | 
 null, string | 
 IP address from which the email send was made | 

 timezone | 
 null, string | 
 Time zone of the user | 

 deferral_reason | 
 null, string | 
 [PII] The SMTP reason code and user friendly message received for this deferral event | 

 attempt_count | 
 null, int | 
 Number of attempts made to send the message | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 sending_ip | 
 null, string | 
 IP address from which the email was sent | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 esp | 
 null, string | 
 ESP related to the event (SparkPost, SendGrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 user_agent | 
 null, string | 
 User agent on which the spam report occurred | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 esp | 
 null, string | 
 ESP related to the event (SparkPost, SendGrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_OPEN_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 user_agent | 
 null, string | 
 User agent on which the open occurred | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 machine_open | 
 null, string | 
 Populated to ‘true’ if the open event is triggered without user engagement, for example, by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity. | 

 esp | 
 null, string | 
 ESP related to the event (SparkPost, SendGrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 is_amp | 
 null, boolean | 
 Indicates that this is an AMP event | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_SEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during Liquid rendering | 

 esp | 
 null, string | 
 ESP related to the event (SparkPost, SendGrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 sending_ip | 
 null, string | 
 IP address from which the email send was made | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 bounce_reason | 
 null, string | 
 [PII] The SMTP reason code and user friendly message received for this bounce event | 

 esp | 
 null, string | 
 ESP related to the event (SparkPost, SendGrid, or Amazon SES) | 

 from_domain | 
 null, string | 
 Sending domain for the email | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED

This table logs message-level email unsubscribes from the recipient’s side: clicking an unsubscribe link, the email client’s one-click List-Unsubscribe, preference center submissions, and ESP-reported unsubscribes. Unsubscribes made through the REST API are not included; those emit users.behaviors.subscriptiongroup.StateChange or users.behaviors.subscription.GlobalStateChange events instead.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 string | 
 [PII] email address of the user | 

 ip_pool | 
 null, string | 
 IP Pool from which the email send was made | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_EMAIL_RETRY_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

This event occurs when a message is deprioritized or frequency capped and is retried later within the configured retry window.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 [PII] Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 retry_type | 
 null, string | 
 Type of retry | 

 retry_log | 
 null, string | 
 Log message describing retry details | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 email_address | 
 null, string | 
 [PII] Email address of the user | 

 ip_pool | 
 null, string | 
 IP pool from which the email send was made | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 feature_flag_id_name | 
 null, string | 
 The Feature Flag Rollout identifier | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 browser | 
 null, string | 
 Device browser - extracted from user_agent - on which the open occurred | 

 carrier | 
 null, string | 
 Carrier of the device | 

 country | 
 null, string | 
 [PII] Country of the user | 

 device_model | 
 null, string | 
 Model of the device | 

 language | 
 null, string | 
 [PII] Language of the user | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 platform | 
 null, string | 
 Platform of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 timezone | 
 null, string | 
 Time zone of the user | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 card_api_id | 
 null, string | 
 API ID of the card | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Browser of the device | 

 version | 
 string | 
 Which version of in-app message, legacy or triggered | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (maximum of 2,000 characters) | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 card_api_id | 
 null, string | 
 API ID of the card | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 resolution of the device | 

 carrier | 
 null, string | 
 carrier of the device | 

 browser | 
 null, string | 
 browser of the device | 

 version | 
 string | 
 which version of in-app message, legacy or triggered | 

 button_id | 
 null, string | 
 ID of the button clicked, if this click represents a click on a button | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 card_api_id | 
 null, string | 
 API ID of the card | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 resolution of the device | 

 carrier | 
 null, string | 
 carrier of the device | 

 browser | 
 null, string | 
 browser of the device | 

 version | 
 string | 
 which version of in-app message, legacy or triggered | 

 ad_id | 
 null, string | 
 [PII] Advertising identifier | 

 ad_id_type | 
 null, string | 
 One of ios_idfa, google_ad_id, windows_ad_id, OR roku_ad_id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether advertising tracking is enabled for the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during liquid rendering | 

 locale_key | 
 null, string | 
 [PII] The key corresponding to the translations (for example ‘en-us’) used to compose this message (null for default). | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_LINE_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (up to 128 chars) | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 line_channel_id | 
 null, string | 
 The LINE Channel ID the message was sent to or received from | 

 line_channel_name | 
 null, string | 
 The LINE Channel Name the message was sent to or received from | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 native_line_id | 
 null, string | 
 [PII] The user’s Line ID from which the message was sent to or received from | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 timezone | 
 null, string | 
 Time zone of the user | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_LINE_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 timezone | 
 null, string | 
 Time zone of the user | 

 native_line_id | 
 null, string | 
 [PII] The user’s Line ID from which the message was sent to or received from | 

 line_channel_id | 
 null, string | 
 The LINE Channel ID the message was sent to or received from | 

 line_channel_name | 
 null, string | 
 The LINE Channel Name the message was sent to or received from | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 is_suspected_bot_click | 
 null, boolean | 
 Whether this event was processed as a bot event | 

 short_url | 
 null, string | 
 Shortened url that was clicked | 

 url | 
 null, string | 
 URL that the user clicked on | 

 user_agent | 
 null, string | 
 User agent on which the spam report occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 line_channel_id | 
 null, string | 
 The LINE Channel ID the message was sent to or received from | 

 line_channel_name | 
 null, string | 
 The LINE Channel Name the message was sent to or received from | 

 media_id | 
 null, string | 
 The LINE-generated ID which can be used to retrieve inbound media from LINE | 

 message_body | 
 null, string | 
 Typed response from the user | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 native_line_id | 
 null, string | 
 [PII] The user’s Line ID from which the message was sent to or received from | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 timezone | 
 null, string | 
 Time zone of the user | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_LINE_SEND_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 line_channel_id | 
 null, string | 
 The LINE Channel ID the message was sent to or received from | 

 line_channel_name | 
 null, string | 
 The LINE Channel Name the message was sent to or received from | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during liquid rendering | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 native_line_id | 
 null, string | 
 [PII] The user’s Line ID from which the message was sent to or received from | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 timezone | 
 null, string | 
 Time zone of the user | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_LINE_RETRY_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

This event occurs when a message is deprioritized or frequency capped and is retried later within the configured retry window.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 [PII] Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 retry_type | 
 null, string | 
 Type of retry | 

 retry_log | 
 null, string | 
 Log message describing retry details | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 line_channel_id | 
 null, string | 
 The LINE Channel ID the message was sent to or received from | 

 line_channel_name | 
 null, string | 
 The LINE Channel Name the message was sent to or received from | 

 native_line_id | 
 null, string | 
 [PII] The user’s Line ID from which the message was sent to or received from | 

 subscription_group_api_id | 
 null, string | 
 Subscription group API ID | 

 timezone | 
 null, string | 
 Time zone of the user | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 activity_id | 
 null, string | 
 Live Activity identifier | 

 activity_attributes_type | 
 null, string | 
 Live Activity attribute type | 

 push_to_start_token | 
 null, string | 
 Live Activity push to start token | 

 update_token | 
 null, string | 
 Live Activity update token | 

 live_activity_event_type | 
 null, string | 
 Event type of Live Activity. One of [‘start’, ‘update’, ‘end’] | 

 live_activity_event_outcome | 
 null, string | 
 Outcome of Live Activity event | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 activity_id | 
 null, string | 
 Live Activity identifier | 

 activity_attributes_type | 
 null, string | 
 Live Activity attribute type | 

 push_to_start_token | 
 null, string | 
 Live Activity push to start token | 

 update_token | 
 null, string | 
 Live Activity update token | 

 live_activity_event_type | 
 null, string | 
 Event type of Live Activity. One of [‘start’, ‘update’, ‘end’] | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 card_api_id | 
 null, string | 
 API ID of the card | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Device browser - extracted from user_agent - on which the open occurred | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (up to 128 chars) | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 card_api_id | 
 null, string | 
 API ID of the card | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Device browser - extracted from user_agent - on which the open occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 card_api_id | 
 null, string | 
 API ID of the card | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Device browser - extracted from user_agent - on which the open occurred | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that we made a delivery attempt to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 platform | 
 string | 
 Platform of the device | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (maximum of 2,000 characters) | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 push_token | 
 null, string | 
 Push token that bounced | 

 device_id | 
 null, string | 
 device_id that we made a delivery attempt to that bounced | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 platform | 
 null, string | 
 Platform of the device | 

 ad_id | 
 null, string | 
 [PII] advertising ID of the device that we made a delivery attempt to | 

 ad_id_type | 
 null, string | 
 Type of the advertising id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether or not tracking is enabled for advertising | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Browser of the device | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED

important

This event is not supported by the Swift SDK and is deprecated in the Obj-C SDK.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Browser of the device | 

 ad_id | 
 null, string | 
 [PII] advertising ID of the device that we made a delivery attempt to | 

 ad_id_type | 
 null, string | 
 Type of the advertising id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether or not tracking is enabled for advertising | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 sdk_version | 
 null, string | 
 Version of the Braze SDK in use during the event | 

 platform | 
 null, string | 
 Platform of the device | 

 os_version | 
 null, string | 
 Version of the operating system of the device | 

 device_model | 
 null, string | 
 Model of the device | 

 resolution | 
 null, string | 
 Resolution of the device | 

 carrier | 
 null, string | 
 Carrier of the device | 

 browser | 
 null, string | 
 Browser of the device | 

 button_string | 
 null, string | 
 Identifier (button_string) of the push notification button clicked. null if not from a button click | 

 button_action_type | 
 null, string | 
 Action type of the push notification button. One of [URI, DEEP_LINK, NONE, CLOSE]. null if not from a button click | 

 slide_id | 
 null, string | 
 Slide identifier of the push carousel slide user clicks on | 

 slide_action_type | 
 null, string | 
 Action type of the push carousel slide | 

 ad_id | 
 null, string | 
 [PII] advertising ID of the device that we made a delivery attempt to | 

 ad_id_type | 
 null, string | 
 Type of the advertising id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether or not tracking is enabled for advertising | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 push_token | 
 null, string | 
 Push token that we made a delivery attempt to | 

 device_id | 
 null, string | 
 device_id that we made a delivery attempt to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 app_api_id | 
 null, string | 
 API ID of the app on which this event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 platform | 
 string | 
 Platform of the device | 

 ad_id | 
 null, string | 
 [PII] advertising ID of the device that we made a delivery attempt to | 

 ad_id_type | 
 null, string | 
 Type of the advertising id | 

 ad_tracking_enabled | 
 null, boolean | 
 Whether or not tracking is enabled for advertising | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during liquid rendering | 

 is_sampled | 
 null, string | 
 Indicates whether the push send was sampled and expected a delivery event | 

 locale_key | 
 null, string | 
 [PII] The key corresponding to the translations (for example ‘en-us’) used to compose this message (null for default). | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_RCS_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (up to 128 chars) | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_name | 
 null, string | 
 Name of the Canvas variation this user received | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_RCS_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 is_suspected_bot_click | 
 null, boolean | 
 Whether this event was processed as a bot event | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 short_url | 
 null, string | 
 Shortened url that was clicked | 

 suspected_bot_click_reason | 
 null, string | 
 Why this event was classified as a bot | 

 user_agent | 
 null, string | 
 User agent on which the spam report occurred | 

 user_phone_number | 
 null, string | 
 [PII] The user’s phone number from which the message was received | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 interaction_type | 
 null, string | 
 The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL | 

 element_label | 
 null, string | 
 Optional details about the clicked element, such as the text of a suggested reply or button | 

 element_type | 
 null, string | 
 Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 url | 
 null, string | 
 URL that the user clicked on | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 canvas_variation_name | 
 null, string | 
 Name of the Canvas variation this user received | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_RCS_DELIVERY_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_name | 
 null, string | 
 Name of the Canvas variation this user received | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 to_phone_number | 
 null, string | 
 [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671) | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 from_rcs_sender | 
 null, string | 
 The RCS sender ID or agent name used to send the message | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 action | 
 null, string | 
 Action taken in response to this message. (for example Subscribed, Unsubscribed or None). | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 media_urls | 
 null, string | 
 Media URLs from the user | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 user_phone_number | 
 null, string | 
 [PII] The user’s phone number from which the message was received | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 message_body | 
 null, string | 
 Typed response from the user | 

 to_rcs_sender | 
 null, string | 
 The inbound RCS sender that the message was sent to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_RCS_READ_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_name | 
 null, string | 
 Name of the Canvas variation this user received | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 to_phone_number | 
 null, string | 
 [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671) | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_RCS_REJECTION_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_name | 
 null, string | 
 Name of the Canvas variation this user received | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 error | 
 null, string | 
 Error name | 

 from_rcs_sender | 
 null, string | 
 The RCS sender ID or agent name used to send the message | 

 is_sms_fallback | 
 null, boolean | 
 Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 provider_error_code | 
 null, string | 
 Error code from the provider | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 to_phone_number | 
 null, string | 
 [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671) | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_RCS_SEND_SHARED

 Field | 
 Type | 
 Description | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 canvas_variation_name | 
 null, string | 
 Name of the Canvas variation this user received | 

 category | 
 null, string | 
 Keyword category name, only populated for auto-reply messages: ‘opt-in’, ‘opt-out’, ‘help’, or custom value | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 from_rcs_sender | 
 null, string | 
 The RCS sender ID or agent name used to send the message | 

 message_extras | 
 null, string | 
 A JSON string of the tagged key-value pairs during liquid rendering | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 to_phone_number | 
 null, string | 
 [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671) | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

## SMS message events and deleted user profiles

note

For USERS_MESSAGES_SMS_* shared tables (including USERS_MESSAGES_SMS_REJECTION_SHARED, USERS_MESSAGES_SMS_DELIVERY_SHARED, and USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED), Braze writes a row only when the Braze user profile still exists in the workspace when the event is processed for Snowflake Data Sharing and Currents. If that user was deleted before processing completes, the event doesn’t appear in Snowflake or your Currents export, even when SMS workspace metrics in the dashboard still reflect aggregate counts from Braze’s reporting path. For the corresponding Currents behavior, see SMS Rejection events and related SMS event types in the same glossary.

### USERS_MESSAGES_SMS_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 subscription_group_api_id | 
 null, string | 
 External ID of the subscription group | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (maximum of 2,000 characters) | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 from_phone_number | 
 null, string | 
 phone number from which the SMS message was sent | 

 subscription_group_api_id | 
 null, string | 
 external ID of the subscription group | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_DELIVERY_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 from_phone_number | 
 null, string | 
 Phone number from which the SMS message was sent | 

 subscription_group_api_id | 
 null, string | 
 External ID of the subscription group | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 is_sms_fallback | 
 null, boolean | 
 Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 subscription_group_api_id | 
 null, string | 
 external ID of the subscription group | 

 error | 
 null, string | 
 error name | 

 provider_error_code | 
 null, string | 
 error code from SMS service provider | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 is_sms_fallback | 
 null, boolean | 
 Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 null, string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace associated with the inbound phone number | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 user_phone_number | 
 string | 
 [PII] the user’s phone number from which the message was received | 

 subscription_group_id | 
 null, string | 
 ID of the subscription group targeted for this SMS message | 

 subscription_group_api_id | 
 null, string | 
 API ID of the subscription group targeted for this SMS message | 

 inbound_phone_number | 
 string | 
 The inbound number that the message was sent to | 

 action | 
 string | 
 Action taken in response to this message. For example, Subscribed, Unsubscribed, or None. | 

 message_body | 
 string | 
 Response from the user | 

 media_urls | 
 null, {"type"=>"array", "items"=>["null", "string"]} | 
 Media URLs from the user | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this event belongs to | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this event belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_REJECTION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 from_phone_number | 
 null, string | 
 phone number from which the SMS message was sent | 

 subscription_group_api_id | 
 null, string | 
 external ID of the subscription group | 

 error | 
 null, string | 
 error name | 

 provider_error_code | 
 null, string | 
 error code from SMS service provider | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 is_sms_fallback | 
 null, boolean | 
 Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_SEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 subscription_group_api_id | 
 null, string | 
 external ID of the subscription group | 

 category | 
 null, string | 
 Keyword Category Name, only populated for auto-reply messages: ‘Opt-in’, ‘Opt-out’, ‘Help’, or custom value | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during liquid rendering | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 null, string | 
 Braze ID of the user targeted by short_url, null if short_url did not use user click tracking | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user targeted by short_url if one exists, null if short_url did not use user click tracking | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace used to generate short_url | 

 time | 
 int | 
 Unix timestamp at which short_url was clicked | 

 timezone | 
 null, string | 
 Time zone of the user | 

 campaign_id | 
 null, string | 
 Braze ID of the campaign short_url was generated for, null if not from a campaign | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign short_url was generated for, null if not from a campaign | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation short_url was generated for, null if not from a campaign | 

 canvas_id | 
 null, string | 
 Braze ID of the Canvas short_url was generated for, null if not from a Canvas | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas short_url was generated for, null if not from a Canvas | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation short_url was generated for, null if not from a Canvas | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step short_url was generated for, null if not from a Canvas | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation short_url was generated for, null if not from a Canvas | 

 url | 
 string | 
 original URL contained in message that is redirected to by short_url | 

 short_url | 
 string | 
 shortened URL that was clicked | 

 user_agent | 
 null, string | 
 user agent requesting short_url | 

 user_phone_number | 
 string | 
 [PII] the user’s phone number | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 is_suspected_bot_click | 
 null, boolean | 
 Whether this event was processed as a bot event | 

 suspected_bot_click_reason | 
 null, object | 
 Why this event was classified as a bot | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_SMS_RETRY_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

This event occurs when a message is deprioritized or frequency capped and is retried later within the configured retry window.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 [PII] Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 subscription_group_api_id | 
 null, string | 
 Subscription group API ID | 

 retry_type | 
 null, string | 
 Type of retry | 

 retry_log | 
 null, string | 
 Log message describing retry details | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (maximum of 2,000 characters) | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED

 Field | 
 Type | 
 Description | 

 http_status_code | 
 null, int | 
 HTTP status code of the response | 

 endpoint_url | 
 null, string | 
 The endpoint url being requested | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 content_length | 
 null, int | 
 Content length of the response | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 host | 
 null, string | 
 The host for the request | 

 id | 
 string | 
 Globally unique ID for this event | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 raw_response | 
 null, string | 
 Truncated raw response from endpoint | 

 retry_count | 
 null, int | 
 The number of retries attempted | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 url_path | 
 null, string | 
 The path of the url being requested | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 webhook_duration | 
 null, int | 
 Total duration of this request in milliseconds | 

 webhook_failure_source | 
 null, string | 
 To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable | 

 is_terminal | 
 null, boolean | 
 Whether this event was the terminal attempt in a send | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_WEBHOOK_SEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 campaign_name | 
 null, string | 
 Name of the campaign | 

 message_variation_name | 
 null, string | 
 Name of the message variation | 

 canvas_name | 
 null, string | 
 Name of the Canvas | 

 canvas_variation_name | 
 null, string | 
 Name of the Canvas variation this user received | 

 canvas_step_name | 
 null, string | 
 Name of the Canvas step | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during liquid rendering | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

This event occurs when a message is deprioritized or frequency capped and is retried later within the configured retry window.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 [PII] Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 gender | 
 null, string | 
 [PII] Gender of the user | 

 country | 
 null, string | 
 [PII] Country of the user | 

 timezone | 
 null, string | 
 Time zone of the user | 

 language | 
 null, string | 
 [PII] Language of the user | 

 retry_type | 
 null, string | 
 Type of retry | 

 retry_log | 
 null, string | 
 Log message describing retry details | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 timezone | 
 null, string | 
 Time zone of the user | 

 app_group_id | 
 null, string | 
 ID of the workspace this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 abort_type | 
 null, string | 
 Type of abort. For a list of values, see Abort types. | 

 abort_log | 
 null, string | 
 [PII] Log message describing abort details (maximum of 2,000 characters) | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_MESSAGES_WHATSAPP_CLICK_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 timezone | 
 null, string | 
 Time zone of the user | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 url | 
 null, string | 
 URL that the user clicked on | 

 short_url | 
 null, string | 
 Shortened url that was clicked | 

 user_agent | 
 null, string | 
 User agent on which the spam report occurred | 

 user_phone_number | 
 null, string | 
 [PII] The user’s phone number from which the message was received | 

 sf_created_at | 
 timestamp, null | 
 when this event was picked up by the Snowpipe | 

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 timezone | 
 null, string | 
 Time zone of the user | 

 from_phone_number | 
 null, string | 
 Phone number from which the WhatsApp message was sent | 

 app_group_id | 
 null, string | 
 ID of the workspace this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 flow_id | 
 null, string | 
 The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow. | 

 template_name | 
 null, string | 
 [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message | 

 message_id | 
 null, string | 
 The unique ID generated by Meta for this message | 

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 timezone | 
 null, string | 
 Time zone of the user | 

 from_phone_number | 
 null, string | 
 Phone number from which the WhatsApp message was sent | 

 app_group_id | 
 null, string | 
 ID of the workspace this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 provider_error_code | 
 null, string | 
 Error code from WhatsApp | 

 provider_error_title | 
 null,  string | 
 Error title from WhatsApp | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 message_id | 
 null, string | 
 The unique ID generated by Meta for this message | 

 template_name | 
 null, string | 
 [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message | 

 flow_id | 
 null, string | 
 The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow. | 

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 user_phone_number | 
 string | 
 [PII] the user’s phone number from which the message was received | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 inbound_phone_number | 
 string | 
 The inbound number that the message was sent to | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 timezone | 
 null, string | 
 Time zone of the user | 

 app_group_id | 
 null, string | 
 ID of the workspace this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 message_body | 
 string | 
 Response from the user | 

 quick_reply_text | 
 string | 
 Text of button pressed by the user | 

 media_urls | 
 null, {"type"=>"array", "items"=>["null", "string"]} | 
 Media URLs from the user | 

 action | 
 string | 
 Action taken in response to this message. For example, Subscribed, Unsubscribed, or None. | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 catalog_id | 
 null, string | 
 Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty. | 

 product_id | 
 null, string | 
 ID of the product purchased | 

 flow_id | 
 null, string | 
 The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow. | 

 flow_response_json | 
 null, string | 
 [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow. | 

 message_id | 
 null, string | 
 The unique ID generated by Meta for this message | 

 in_reply_to | 
 null, string | 
 The message_id of the message this message was replying to | 

### USERS_MESSAGES_WHATSAPP_READ_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 timezone | 
 null, string | 
 Time zone of the user | 

 from_phone_number | 
 null, string | 
 Phone number from which the WhatsApp message was sent | 

 app_group_id | 
 null, string | 
 ID of the workspace this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 template_name | 
 null, string | 
 [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message | 

 message_id | 
 null, string | 
 The unique ID generated by Meta for this message | 

 flow_id | 
 null, string | 
 The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow. | 

### USERS_MESSAGES_WHATSAPP_SEND_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 Unix timestamp at which the event happened | 

 to_phone_number | 
 null, string | 
 [PII] phone number of the recipient | 

 user_id | 
 string | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 null, string | 
 [PII] External user ID of the user | 

 device_id | 
 null, string | 
 device_id that is tied to this user if user is anonymous | 

 timezone | 
 null, string | 
 Time zone of the user | 

 from_phone_number | 
 null, string | 
 phone number from which the WhatsApp message was sent | 

 app_group_id | 
 null, string | 
 ID of the workspace this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the workspace this user belongs to | 

 subscription_group_api_id | 
 string | 
 Subscription group API ID | 

 campaign_id | 
 null, string | 
 Internal-use Braze ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 Internal-use Braze ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 message_extras | 
 null, string | 
 [PII] A JSON string of the tagged key-value pairs during Liquid rendering | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

 send_id | 
 null, string | 
 Message send ID this message belongs to | 

 flow_id | 
 null, string | 
 The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow. | 

 template_name | 
 null, string | 
 [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message | 

 message_id | 
 null, string | 
 The unique ID generated by Meta for this message | 

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED

note

This table is available only through Snowflake Data Sharing. It is not accessible in Query Builder or SQL Segment Extensions.

This event occurs when a message is deprioritized or frequency capped and is retried later within the configured retry window.

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 user_id | 
 string | 
 [PII] Braze user ID of the user who performed this event | 

 external_user_id | 
 null, string | 
 [PII] External ID of the user | 

 app_group_id | 
 null, string | 
 BSON ID of the app group this user belongs to | 

 app_group_api_id | 
 null, string | 
 API ID of the app group this user belongs to | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 to_phone_number | 
 null, string | 
 [PII] Phone number of the user receiving the message in e.164 format | 

 device_id | 
 null, string | 
 ID of the device on which the event occurred | 

 timezone | 
 null, string | 
 Time zone of the user | 

 subscription_group_api_id | 
 null, string | 
 Subscription group API ID | 

 campaign_id | 
 null, string | 
 BSON ID of the campaign this event belongs to | 

 campaign_api_id | 
 null, string | 
 API ID of the campaign this event belongs to | 

 message_variation_api_id | 
 null, string | 
 API ID of the message variation this user received | 

 canvas_id | 
 null, string | 
 BSON ID of the Canvas this event belongs to | 

 canvas_api_id | 
 null, string | 
 API ID of the Canvas this event belongs to | 

 canvas_variation_api_id | 
 null, string | 
 API ID of the Canvas variation this event belongs to | 

 canvas_step_api_id | 
 null, string | 
 API ID of the Canvas step this event belongs to | 

 canvas_step_message_variation_api_id | 
 null, string | 
 API ID of the Canvas step message variation this user received | 

 dispatch_id | 
 null, string | 
 ID of the dispatch this message belongs to | 

 retry_type | 
 null, string | 
 Type of retry | 

 retry_log | 
 null, string | 
 Log message describing retry details | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

## Users

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 user_id | 
 string, null | 
 Braze ID of the user that performed this event | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 time | 
 int, null | 
 Unix timestamp at which the event happened | 

 random_bucket_number | 
 int, null | 
 Current random bucket number assigned to the user | 

 prev_random_bucket_number | 
 int, null | 
 Previous random bucket number assigned to the user | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_USERDELETEREQUEST_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that was deleted | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 time | 
 int, null | 
 Unix timestamp at which the user delete request was processed | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

### USERS_USERORPHAN_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string, null | 
 Globally unique ID for this event | 

 user_id | 
 string, null | 
 Braze ID of the user that was orphaned | 

 external_user_id | 
 string, null | 
 [PII] External user ID of the user | 

 device_id | 
 string, null | 
 ID of the device that is tied to this user, if the user is anonymous | 

 app_group_id | 
 string, null | 
 Braze ID of the workspace this user belongs to | 

 app_group_api_id | 
 string, null | 
 API ID of the workspace this user belongs to | 

 app_api_id | 
 string, null | 
 API ID of the app the orphaned user belonged to | 

 time | 
 int, null | 
 Unix timestamp at which the user was orphaned | 

 orphaned_by_id | 
 string, null | 
 Braze ID of the user whose profile was merged with the orphaned user’s profile | 

 sf_created_at | 
 timestamp, null | 
 When this event was picked up by the Snowpipe | 

## Snapshots

note

Snapshot tables are available in Snowflake Data Sharing only.

### SNAPSHOTS_APP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 api_id | 
 string | 
 API ID of the app | 

 name | 
 null, string | 
 Name of the app | 

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 api_id | 
 string | 
 API ID of the campaign message variation | 

 name | 
 null, string | 
 Name of the campaign message variation | 

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 type | 
 null, string | 
 Type of the Canvas Flow step | 

 api_step_id | 
 string | 
 API ID of the Canvas step | 

 experiment_splits | 
 null, string | 
 Experiment splits for the step | 

 conversion_behaviors | 
 null, string | 
 Conversion behaviors for the step | 

 name | 
 null, string | 
 Name of the Canvas Flow step | 

### SNAPSHOTS_CANVAS_STEP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 api_id | 
 string | 
 API ID of the Canvas step | 

 name | 
 null, string | 
 Name of the Canvas step | 

 actions | 
 null, string | 
 Actions for the Canvas step | 

### SNAPSHOTS_CANVAS_VARIATION_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 api_id | 
 string | 
 API ID of the Canvas variation | 

 name | 
 null, string | 
 Name of the Canvas variation | 

### SNAPSHOTS_EXPERIMENT_STEP_SHARED

 Field | 
 Type | 
 Description | 

 id | 
 string | 
 Globally unique ID for this event | 

 time | 
 int | 
 UNIX timestamp at which the event happened | 

 app_group_id | 
 string | 
 BSON ID of the app group this user belongs to | 

 type | 
 null, string | 
 Type of the Experiment step | 

 api_step_id | 
 string | 
 API ID of the Experiment step | 

 experiment_splits | 
 null, string | 
 Experiment splits for the step | 

 conversion_behaviors | 
 null, string | 
 Conversion behaviors for the step | 

 name | 
 null, string | 
 Name of the Experiment step | 

## Abort types

The following table lists the possible abort_type values. An abort type describes the specific reason a message was not sent.

### General

These abort types can occur on any messaging channel.

 abort_type value | 
 Description | 

 liquid_abort_message | 
 The abort_message Liquid tag was called, so the send was canceled. | 

 template_parse_error | 
 The message template could not be parsed due to a syntax or rendering error, so the send was canceled. | 

 rate_limit | 
 The message was aborted because it exceeded the configured rate limit. | 

 campaign_disabled | 
 The campaign was disabled before the message could be sent. | 

 campaign_does_not_exist | 
 The campaign associated with this message no longer exists. | 

 campaign_action_does_not_exist | 
 The campaign action associated with this message no longer exists. | 

 message_variation_does_not_exist | 
 The message variation assigned to this user no longer exists. | 

 user_not_in_segment | 
 The user is not in the target segment, so the message was not sent. | 

 trigger_event_blacklisted | 
 The trigger event is blocklisted, so the message was not sent. | 

 exhausted_retries | 
 The message could not be sent after the maximum number of retry attempts. | 

 frequency_capped | 
 The user already received the maximum number of messages allowed by your workspace’s frequency capping rules. | 

### Content and rendering

 abort_type value | 
 Description | 

 exhausted_cc_retries | 
 Connected Content failed after the maximum number of retries, so the message was aborted. | 

 connected_content_not_supported | 
 Connected Content is not supported in this context, so the message was aborted. | 

 promo_codes_not_supported | 
 Promotion codes are not supported in this context, so the message was aborted. | 

 catalog_items_rerender_not_supported | 
 Catalog item re-rendering is not supported in this context, so the message was aborted. | 

 blacklisted_media_url | 
 The media URL is blocklisted and cannot be used in messages. | 

 blocked_media_url | 
 The media URL was blocked by security policies. | 

 invalid_media_url | 
 The media URL is not valid or could not be resolved. | 

 ssl_error | 
 An SSL error occurred while making a request. | 

 invalid_http_status | 
 An HTTP request returned a non-successful status code. | 

 http_timeout | 
 An HTTP request timed out before receiving a response. | 

 missing_hostname | 
 The request URL is missing a hostname. | 

### Email

 abort_type value | 
 Description | 

 exhausted_link_shortening_retries | 
 Link shortening failed after the maximum number of retries. | 

 missing_email | 
 The user does not have an email address on their profile. | 

 invalid_domain | 
 The email address has an invalid domain. | 

### Push

 abort_type value | 
 Description | 

 invalid_push_payload | 
 The push notification payload is invalid or malformed. | 

 sdk_not_supported | 
 The SDK version on the user’s device does not support this type of push notification. | 

### SMS/MMS

 abort_type value | 
 Description | 

 exhausted_link_shortening_retries | 
 Link shortening failed after the maximum number of retries. | 

 sms_empty_payload | 
 The SMS message body is empty. | 

 sms_no_sending_numbers | 
 No sending phone numbers are available for this subscription group. | 

 sms_fatal_provider_error | 
 A fatal error occurred with the SMS provider, preventing message delivery. | 

 sms_gateway_domain_not_allowed | 
 The SMS gateway domain is not on the allowlist. | 

 blocked_recipient_country | 
 The recipient’s phone number is in a country that is blocked by your geographic permissions. | 

 mms_not_supported | 
 MMS is not supported for this recipient or sending number. | 

 no_current_messaging_service | 
 No active messaging service is configured for this subscription group. | 

### WhatsApp

 abort_type value | 
 Description | 

 whats_app_no_sending_numbers | 
 No sending phone numbers are available for this WhatsApp subscription group. | 

 whats_app_invalid_template_message | 
 The WhatsApp template message is invalid or not approved. | 

 whats_app_invalid_response_message | 
 The WhatsApp response message is invalid. | 

 whats_app_fatal_provider_error | 
 A fatal error occurred with the WhatsApp provider, preventing message delivery. | 

### LINE

 abort_type value | 
 Description | 

 line_fatal_provider_error | 
 A fatal error occurred with the LINE provider, preventing message delivery. | 

### Kakao

 abort_type value | 
 Description | 

 kakao_fatal_provider_error | 
 A fatal error occurred with the Kakao provider, preventing message delivery. | 

### Content Cards

 abort_type value | 
 Description | 

 content_card_size_exceeded | 
 The Content Card payload exceeds the maximum size limit (2 KB). | 

 content_card_content_invalid | 
 The Content Card content is invalid or contains unsupported characters. | 

 content_card_expiration_invalid | 
 The Content Card expiration date is invalid. | 

 content_card_general | 
 The Content Card could not be created due to a general error. | 

### In-app messages

 abort_type value | 
 Description | 

 no_longer_in_availability_window | 
 The message could not be sent within the configured availability window, so it was aborted. | 

 maximum_impressions_reached | 
 The in-app message has already reached its maximum number of impressions. | 

### Webhooks

 abort_type value | 
 Description | 

 blocked_webhook_url | 
 The webhook URL was blocked by security policies. | 

- 

New Stuff!
