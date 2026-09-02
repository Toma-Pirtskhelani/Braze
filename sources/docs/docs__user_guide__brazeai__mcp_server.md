---
url: https://www.braze.com/docs/user_guide/brazeai/mcp_server
slug: docs__user_guide__brazeai__mcp_server
title: "The Braze MCP server"
description: "Learn about the Braze MCP server, a secure connection that lets AI tools like Claude and Cursor access non-PII Braze data to answer questions,."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# The Braze MCP server

Learn about the Braze MCP server, a secure remote connection that lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, provide insights, and create content.

## What is Model Context Protocol (MCP)?

​​Model Context Protocol, or MCP, is a standard that lets AI agents connect to and work with data from another platform. It has two main parts:

- MCP client: The application where the AI agent runs, such as Cursor or Claude.
 
- MCP server: A service provided by another platform, like Braze, that defines which tools the AI can use and what data it can access.

## About the Braze MCP server

After setting up the Braze MCP server, you can connect AI tools like agents, assistants, and chatbots directly to Braze, allowing them to read aggregated data such as Canvas and Campaign analytics, custom attributes, segments, and more. The Braze MCP server is great for:

- Building AI-powered tools that need Braze context.
 
- CRM engineers creating multi-step agent workflows.
 
- Technical marketers experimenting with natural language queries.

The Braze MCP server includes both read and write tools. These tools do not return data from Braze user profiles. Your agents inherit your Braze dashboard user permissions. For the full list of available tools, see Available API functions.

warning

Tools that expose user-level PII are not available.

Use the MCP server to ask questions about campaign and Canvas performance, explore your segments and custom attributes, generate reports, and create content such as email templates, content blocks, and media library assets through natural language.

## Is the beta MCP server deprecated?

Yes. The locally hosted MCP server released in August 2025 is deprecated and will not receive additional updates. You can continue using it, but Braze recommends migrating to the remote-hosted version.

### How is the remote server different?

The previous Braze MCP server ran locally on your machine. You needed to install a package, manage a config file, and create a Braze API key with the right permissions. The remote MCP server removes that local setup.

Connect from a supported MCP client in under a minute. Authentication uses OAuth. Access is tied to your Braze dashboard user account, not a shared API key, so what an agent can see and do mirrors your dashboard permissions. If a dashboard user loses access in Braze, the client loses access too.

The key differences are:

- Setup: Paste a Braze URL instead of installing a package and editing config files.
 
- Auth: Sign in with your Braze account instead of creating an API key.
 
- Permissions: Access is based on your dashboard user account instead of API key permissions.
 
- Workspace targeting: Workspace context is passed per request instead of being fixed in local config.

## Frequently Asked Questions (FAQ)

### Which MCP clients are supported?

Any MCP client that supports remote MCP servers with OAuth can work. Braze has verified:

- Claude through custom connectors
 
- ChatGPT through custom connectors
 
- Cursor
 
- OpenAI Codex
 
- Claude Code
 
- Visual Studio Code

### What Braze data can my MCP client access?

MCP clients can access tools that do not return user-level PII.

### Can my MCP client change Braze data?

Yes, if your dashboard user has those permissions.

### Do I still need a Braze API key?

Not for MCP. API keys still work for the REST API and are not being deprecated.

### Which regions are supported?

Both Braze clusters are supported. Two endpoints are available today:

- https://mcp.braze.com/mcp (US)
 
- https://mcp.braze.eu/mcp (EU)

Either endpoint can reach any Braze cluster.

### Can I use the Braze remote MCP server with tools other than the verified list?

You can try, but authentication may be blocked. Braze currently maintains an allowlist of supported domains for security. Want support for your MCP client? Consider leaving product feedback.

### Does the remote server support multiple workspaces?

Yes. Specify the workspace per conversation or per request. One connection covers all workspaces you are authorized to access.

### Can my agent access user-level PII?

No. As of now, tools that expose PII are not available.

### What happens when my permissions change?

Agent access changes with the dashboard user. Permission changes apply on the next request. Deactivated dashboard users lose MCP access.

### Why do I not see the Braze connector in my client’s directory?

Directory listings may not be available in every MCP client yet. You can always connect manually using the Braze MCP URL.

### My company uses IP allowlisting. Can we use the remote MCP server?

Not right now. If you use IP Allowlisting, you cannot use the remote MCP server.

## Legal disclaimer

### How instructions and responses are handled

The Braze MCP server receives instructions from your Third-Party Provider MCP client, such as Claude, ChatGPT, Copilot, Gemini CLI, Codex, or Cursor, exactly as that provider’s underlying AI model formulates them. When you type a request in natural language, the AI model interprets your request and translates it into one or more specific tool calls to Braze. Braze receives and executes the tool call as sent. Braze does not see your original natural-language prompt and cannot verify that the generated tool call fully or accurately reflects your intended request.

When Braze returns data or a result, that response is sent back to your Third-Party Provider MCP client, which then interprets, formats, and presents it to you. Braze does not control how the AI model presents, summarizes, or describes returned information.

Braze is not liable for instructions generated by, or responses conveyed through, any Third-Party Provider MCP client. Braze recommends not using “auto-mode” if your Third-Party Provider MCP client offers it for automatic action implementation. Review AI-generated summaries against source data in your Braze dashboard and review any AI-proposed action before implementing it through your Third-Party Provider MCP client.

- 

New Stuff!
