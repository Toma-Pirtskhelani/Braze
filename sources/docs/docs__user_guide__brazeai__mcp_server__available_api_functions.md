---
url: https://www.braze.com/docs/user_guide/brazeai/mcp_server/available_api_functions
slug: docs__user_guide__brazeai__mcp_server__available_api_functions
title: "Braze MCP server functions"
description: "List of read and write Braze API functions accessible through the Braze MCP server."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Braze MCP server functions

The Braze MCP server exposes read and write tools that map to specific Braze REST API endpoints. For more information, see Braze MCP server.

important

The locally hosted Braze MCP server (beta) is deprecated and doesn’t receive additional updates.

note

The Braze MCP server includes tools that are only available to customers participating in beta programs. If you try to access a tool that is part of a beta program and your account does not have the feature enabled, you may receive an error response. To join a beta program, contact your account manager.

## Prerequisites

Before you can use this feature, you’ll need to set up the Braze MCP server.

## Available Braze API functions

Your MCP client references these tools to interact with the Braze MCP server.

### Workspaces

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_workspaces | 
 N/A | 
 read | 
 Discover which Braze workspaces the current OAuth access token can reach. Call this first: each returned workspace id is the app_group_id every other tool requires. | 

### Campaigns

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_campaign_list | 
 /campaigns/list | 
 read | 
 Export a list of campaigns with name, campaign API identifier, API-campaign flag, and tags. | 

 get_campaign_details | 
 /campaigns/details | 
 read | 
 Retrieve relevant information on a specified campaign by campaign_id. | 

 get_campaign_dataseries | 
 /campaigns/data_series | 
 read | 
 Daily series of campaign stats over time (sends, opens, clicks, conversions by channel). | 

 duplicate_campaign | 
 /campaigns/duplicate | 
 create | 
 Duplicate an existing campaign. | 

 create_campaign* | 
 N/A | 
 create | 
 Create a new campaign. | 

 edit_campaign* | 
 N/A | 
 update | 
 Edit an existing campaign. | 

 launch_campaign* | 
 N/A | 
 update | 
 Launch a campaign. | 

 stop_campaign* | 
 N/A | 
 update | 
 Stop a running campaign. | 

 archive_campaign* | 
 N/A | 
 update | 
 Archive a campaign. | 

 unarchive_campaign* | 
 N/A | 
 update | 
 Unarchive a campaign. | 

 get_campaign_draft* | 
 N/A | 
 read | 
 Retrieve draft campaign details. | 

 get_campaign_live_details* | 
 N/A | 
 read | 
 Retrieve live campaign details. | 

 create_campaign_message* | 
 N/A | 
 create | 
 Create a message within a campaign. | 

 update_campaign_message* | 
 N/A | 
 update | 
 Update a campaign message. | 

 delete_campaign_message* | 
 N/A | 
 delete | 
 Delete a campaign message. | 

 create_campaign_message_variation* | 
 N/A | 
 create | 
 Create a message variation within a campaign. | 

 update_campaign_message_variation* | 
 N/A | 
 update | 
 Update a campaign message variation. | 

 delete_campaign_message_variation* | 
 N/A | 
 delete | 
 Delete a campaign message variation. | 

 update_campaign_distribution* | 
 N/A | 
 update | 
 Update campaign distribution settings. | 

* This tool is only available to customers participating in the campaign APIs beta program. If your account does not have this feature enabled, you may receive an error when attempting to use it. To join the beta program, contact your account manager.

### Canvases

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_canvas_list | 
 /canvas/list | 
 read | 
 Export a list of Canvases with name, Canvas API identifier, and tags. | 

 get_canvas_details | 
 /canvas/details | 
 read | 
 Export Canvas metadata: name, time created, current status, and more. | 

 get_canvas_data_series | 
 /canvas/data_series | 
 read | 
 Export time series data for a Canvas. | 

 get_canvas_data_summary | 
 /canvas/data_summary | 
 read | 
 Export rollups of Canvas time series data for a concise results summary. | 

### Catalogs

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_catalogs | 
 /catalogs | 
 read | 
 List catalogs in a workspace. | 

 get_catalog_items | 
 /catalogs/{catalog_name}/items | 
 read | 
 Return multiple catalog items and their content. | 

 get_catalog_item | 
 /catalogs/{catalog_name}/items/{item_id} | 
 read | 
 Return a single catalog item and its content. | 

 create_catalog | 
 /catalogs | 
 create | 
 Create a catalog. | 

 delete_catalog | 
 /catalogs/{catalog_name} | 
 delete | 
 Delete a catalog. | 

 create_catalog_fields | 
 /catalogs/{catalog_name}/fields | 
 create | 
 Create multiple fields in a catalog. | 

 delete_catalog_field | 
 /catalogs/{catalog_name}/fields/{field_name} | 
 delete | 
 Delete a catalog field. | 

 create_catalog_items | 
 /catalogs/{catalog_name}/items | 
 create | 
 Create multiple items in a catalog. Up to 50 items per request. | 

 edit_catalog_items | 
 /catalogs/{catalog_name}/items | 
 update | 
 Edit multiple existing items in a catalog. Up to 50 items per request. | 

 replace_catalog_items | 
 /catalogs/{catalog_name}/items | 
 update | 
 Replace multiple items in a catalog. Creates items if they don’t exist. Up to 50 items per request. | 

 delete_catalog_items | 
 /catalogs/{catalog_name}/items | 
 delete | 
 Delete multiple items in a catalog. Up to 50 items per request. | 

 create_catalog_selection | 
 /catalogs/{catalog_name}/selections | 
 create | 
 Create a selection in a catalog. | 

 delete_catalog_selection | 
 /catalogs/{catalog_name}/selections/{selection_name} | 
 delete | 
 Delete a catalog selection. | 

### Custom attributes

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_custom_attributes | 
 /custom_attributes | 
 read | 
 Export custom attributes recorded for your app, in groups of 50, alphabetical. | 

### Custom events

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_events | 
 /events | 
 read | 
 Export custom events recorded for your app, in groups of 50, alphabetical (cursor pagination). | 

 get_events_list | 
 /events/list | 
 read | 
 Export custom event names, in groups of 250, alphabetical (page pagination). | 

 get_events_data_series | 
 /events/data_series | 
 read | 
 Occurrences of a custom event over a designated time period. | 

### CDI integrations

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 list_integrations | 
 /cdi/integrations | 
 read | 
 List existing Cloud Data Ingestion integrations, 10 per call. | 

 get_integration_job_sync_status | 
 /cdi/integrations/{integration_id}/job_sync_status | 
 read | 
 Past sync statuses for a given CDI integration, 10 per call. | 

 trigger_integration_sync | 
 /cdi/integrations/{integration_id}/sync | 
 write | 
 Trigger a sync for a given CDI integration. | 

### KPI

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_dau_data_series | 
 /kpi/dau/data_series | 
 read | 
 Daily series of unique active users per date. | 

 get_mau_data_series | 
 /kpi/mau/data_series | 
 read | 
 Daily series of unique active users over a 30-day rolling window. | 

 get_new_users_data_series | 
 /kpi/new_users/data_series | 
 read | 
 Daily series of total new users per date. | 

 get_uninstalls_data_series | 
 /kpi/uninstalls/data_series | 
 read | 
 Daily series of total uninstalls per date. | 

### Media library

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 create_media_library_asset | 
 /media_library/create | 
 create | 
 Upload an asset to the Braze media library through external URL or base64 file content. Exactly one upload mode must be provided. | 

### Purchases

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_product_list | 
 /purchases/product_list | 
 read | 
 Paginated list of product IDs. | 

 get_quantity_series | 
 /purchases/quantity_series | 
 read | 
 Total number of purchases in your app over a time range. | 

 get_revenue_series | 
 /purchases/revenue_series | 
 read | 
 Total money spent in your app over a time range. | 

### Segments

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_segment_list | 
 /segments/list | 
 read | 
 Export segments with name, Segment API identifier, and analytics-tracking flag. | 

 get_segment_details | 
 /segments/details | 
 read | 
 Retrieve relevant information on a segment by segment_id. | 

 get_segment_data_series | 
 /segments/data_series | 
 read | 
 Daily series of a segment’s estimated size over time. | 

 get_segment_filters* | 
 N/A | 
 read | 
 Retrieve segment filter definitions. | 

 create_segment* | 
 N/A | 
 create | 
 Create a new segment. | 

 edit_segment* | 
 N/A | 
 update | 
 Edit an existing segment. | 

* This tool is only available to customers participating in the segment APIs beta program. If your account does not have this feature enabled, you may receive an error when attempting to use it. To join the beta program, contact your account manager.

### Sends

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_send_data_series | 
 /sends/data_series | 
 read | 
 Daily stats for a tracked send_id (API campaigns). Braze stores send analytics for 14 days after the send. | 

### Sessions

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_session_data_series | 
 /sessions/data_series | 
 read | 
 Number of sessions for your app over a designated time period. | 

### Templates

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_email_templates | 
 /templates/email/list | 
 read | 
 List available email templates in your Braze account. | 

 get_email_template_info | 
 /templates/email/info | 
 read | 
 Get information for a specific email template. Drag-and-drop editor templates are not accepted. | 

 create_email_template | 
 /templates/email/create | 
 create | 
 Create an email template on the Braze dashboard. | 

 update_email_template | 
 /templates/email/update | 
 update | 
 Update an existing email template. | 

### Content blocks

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 get_content_blocks | 
 /content_blocks/list | 
 read | 
 List existing content block information. | 

 get_content_block_info | 
 /content_blocks/info | 
 read | 
 Get information for an existing content block, optionally with campaign or Canvas inclusion data. | 

 create_content_block | 
 /content_blocks/create | 
 create | 
 Create a content block. | 

 update_content_block | 
 /content_blocks/update | 
 update | 
 Update a content block. | 

### Operator

 Tool | 
 API endpoint | 
 Access | 
 Description | 

 send_operator_prompt | 
 N/A | 
 update | 
 Send a natural-language prompt to the BrazeAI Operator. Submits a background job and returns a job_id. | 

 get_operator_result | 
 N/A | 
 read | 
 Poll for the result of a submitted Operator job using its job_id. | 

 cancel_operator_job | 
 N/A | 
 update | 
 Cancel a running Operator job. | 

important

These tools are only available to customers participating in the Operator beta program. If your account does not have this feature enabled, you may receive an error when attempting to use it. To join the beta program, contact your account manager.

## Legal disclaimer

### How instructions and responses are handled

The Braze MCP server receives instructions from your Third-Party Provider MCP client, such as Claude, ChatGPT, Copilot, Gemini CLI, Codex, or Cursor, exactly as that provider’s underlying AI model formulates them. When you type a request in natural language, the AI model interprets your request and translates it into one or more specific tool calls to Braze. Braze receives and executes the tool call as sent. Braze does not see your original natural-language prompt and cannot verify that the generated tool call fully or accurately reflects your intended request.

When Braze returns data or a result, that response is sent back to your Third-Party Provider MCP client, which then interprets, formats, and presents it to you. Braze does not control how the AI model presents, summarizes, or describes returned information.

Braze is not liable for instructions generated by, or responses conveyed through, any Third-Party Provider MCP client. Braze recommends not using “auto-mode” if your Third-Party Provider MCP client offers it for automatic action implementation. Review AI-generated summaries against source data in your Braze dashboard and review any AI-proposed action before implementing it through your Third-Party Provider MCP client.

- 

New Stuff!
