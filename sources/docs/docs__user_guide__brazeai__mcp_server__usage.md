---
url: https://www.braze.com/docs/user_guide/brazeai/mcp_server/usage
slug: docs__user_guide__brazeai__mcp_server__usage
title: "Using the Braze MCP server"
description: "Learn how to interact with your Braze data using natural-language tools like Claude and Cursor."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Using the Braze MCP server

Learn how to interact with your Braze data through natural language after connecting to the remote Braze MCP server. For more information, see Braze MCP server.

important

The locally hosted Braze MCP server (beta) is deprecated and doesn’t receive additional updates.

## Prerequisites

Before you can use this feature, you’ll need to set up the Braze MCP server.

## Best practices

When using the Braze MCP server through natural-language tools, keep these tips in mind:

- Confirm the workspace in your prompt, especially when you have access to multiple workspaces.
 
- Be specific about date ranges and metrics when requesting analytics.
 
- Ask the agent to confirm which tools it used when validating outputs.
 
- Compare high-impact recommendations against source data in the Braze dashboard.

## Usage examples

After setting up the Braze MCP server, you can interact with Braze through natural language. Here are examples to get started.

### Which workspaces can I access?

- example prompt
 
- example response

Show my available Braze workspaces and tell me which one to use for production campaign analytics.

I called get_workspaces and found these workspaces:

- Marketing - Production (app_group_id: YOUR-APP-GROUP-ID-1)
 
- Marketing - Staging (app_group_id: YOUR-APP-GROUP-ID-2)

Use Marketing - Production for production campaign analytics prompts.

For more information, see Available API functions.

### Show me campaign performance for last week

- example prompt
 
- example response

In the Marketing - Production workspace, show campaign performance for the last seven days, including sends, opens, clicks, and top performers.

I used get_campaign_list and get_campaign_dataseries for the requested workspace and date range.

Summary:

- Total sends: YOUR-TEST-SENDS
 
- Total opens: YOUR-TEST-OPENS
 
- Total clicks: YOUR-TEST-CLICKS
 
- Top campaign by opens: YOUR-TEST-CAMPAIGN-NAME

I can break this down by campaign, channel, or day if needed.

For more information, see Available API functions.

### Create an email template

- example prompt
 
- example response

In the Marketing - Production workspace, create an onboarding email template named "YOUR-TEST-TEMPLATE-NAME".

I used create_email_template and created your template.

- Template ID: YOUR-TEST-TEMPLATE-ID-123
 
- Template name: YOUR-TEST-TEMPLATE-NAME
 
- Workspace: Marketing - Production

For more information, see Available API functions.

## Example workflows

These examples combine multiple tools to complete a task from start to finish.

### Report across multiple workspaces

- example prompt
 
- example response

Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.

I called get_workspaces to confirm access, then ran get_campaign_dataseries for each workspace over the past seven days.

- US Prod: YOUR-TEST-SENDS sends, YOUR-TEST-OPEN-RATE open rate
 
- EU Prod: YOUR-TEST-SENDS sends, YOUR-TEST-OPEN-RATE open rate

US Prod sent more messages this week, while EU Prod had the higher open rate. I can break either workspace down by campaign or channel.

### Copy templates from staging to production

- example prompt
 
- example response

Copy the email templates from my Staging workspace to my Production workspace.

I used get_email_templates and get_email_template_info to read the templates in Staging, then create_email_template to recreate each one in Production.

- YOUR-TEST-TEMPLATE-NAME-1: created in Production (YOUR-TEST-TEMPLATE-ID-1)
 
- YOUR-TEST-TEMPLATE-NAME-2: created in Production (YOUR-TEST-TEMPLATE-ID-2)

I skipped drag-and-drop editor templates, which get_email_template_info doesn’t support. Let me know if you’d like me to review the copied templates.

### Summarize weekly campaign health

- example prompt
 
- example response

Give me a weekly campaign health summary for the Production workspace.

I used get_campaign_list and get_campaign_dataseries to pull the past seven days of activity in Production.

- Total sends: YOUR-TEST-SENDS
 
- Open rate: YOUR-TEST-OPEN-RATE
 
- Click rate: YOUR-TEST-CLICK-RATE
 
- Top campaign by conversions: YOUR-TEST-CAMPAIGN-NAME

Sends were up week over week. I can add a channel breakdown or flag any campaigns with declining engagement.

## How the remote MCP server works

When you send a request, a few steps happen behind the scenes:

- You prompt your client. You type a request in natural language, such as asking for last week’s campaign performance.
 
- The client’s model selects tools. The AI model in your client interprets your request and translates it into one or more Braze tool calls, such as get_campaign_list and get_campaign_dataseries.
 
- Braze runs the tool call. The remote MCP server receives each tool call over your authenticated OAuth session, applies the workspace you specified, and runs it against the matching Braze REST API endpoint.
 
- Braze returns the result. The server sends the data back to your client, which formats and presents it to you.

Your access is the intersection of two things:

- The scopes granted when you authorized the connection, such as mcp:tools.
 
- Your own dashboard user permissions. If you can’t view campaigns in the dashboard, your agent can’t either. If you can create email templates, your agent can too. An agent can never exceed your own access.

Workspace context is passed with each request rather than stored in a local config file, so one connection can work across every workspace you’re authorized to access.

## Legal disclaimer

### How instructions and responses are handled

The Braze MCP server receives instructions from your Third-Party Provider MCP client, such as Claude, ChatGPT, Copilot, Gemini CLI, Codex, or Cursor, exactly as that provider’s underlying AI model formulates them. When you type a request in natural language, the AI model interprets your request and translates it into one or more specific tool calls to Braze. Braze receives and executes the tool call as sent. Braze does not see your original natural-language prompt and cannot verify that the generated tool call fully or accurately reflects your intended request.

When Braze returns data or a result, that response is sent back to your Third-Party Provider MCP client, which then interprets, formats, and presents it to you. Braze does not control how the AI model presents, summarizes, or describes returned information.

Braze is not liable for instructions generated by, or responses conveyed through, any Third-Party Provider MCP client. Braze recommends not using “auto-mode” if your Third-Party Provider MCP client offers it for automatic action implementation. Review AI-generated summaries against source data in your Braze dashboard and review any AI-proposed action before implementing it through your Third-Party Provider MCP client.

- 

New Stuff!
