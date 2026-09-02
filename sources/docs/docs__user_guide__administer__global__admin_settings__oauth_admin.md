---
url: https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin
slug: docs__user_guide__administer__global__admin_settings__oauth_admin
title: "Manage OAuth settings"
description: "Learn how to manage MCP OAuth access for the Braze MCP server."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# Manage OAuth settings

OAuth settings manage company-wide access to the Braze MCP server.

OAuth settings apply to your entire company. The permissions assigned to each user determine which workspaces and features they can access through the MCP server.

## Requirements

 Requirement | 
 Description | 

 “Admin” permission | 
 You must have the company-level “Admin” permission to view OAuth settings or turn MCP OAuth access on or off. | 

 “Use MCP Server” permission | 
 Users must have this permission for each workspace they want to access through the MCP server. This permission is separate from the “Admin” permission used to manage OAuth settings. | 

For more information about assigning permissions, see User permissions.

## How OAuth access works

OAuth settings and user permissions work together:

- Company-wide OAuth settings determine whether users can connect MCP clients to Braze.
 
- The “Use MCP Server” permission determines whether an individual user can use the MCP server in a workspace.
 
- The user’s existing dashboard permissions determine which Braze data and features an MCP client can access.
 
- One OAuth connection can access only the workspaces that the user is authorized to access.

Turning on MCP OAuth access doesn’t grant users new workspace permissions. Similarly, removing a dashboard permission removes that capability from the user’s connected MCP client.

## Company and workspace controls

OAuth policy is stored at the company level. Workspace admins can’t override MCP OAuth access for a single workspace.

 Control | 
 Where you configure it | 
 Scope | 

 MCP OAuth access | 
 Settings > Admin Settings > OAuth | 
 Entire company. When this is off, MCP OAuth is denied in every workspace. | 

 “Use MCP Server” permission | 
 Settings > User Management | 
 Per workspace. Users need this permission in each workspace they access through the MCP server. | 

Only users with the “Admin” permission can change MCP OAuth access. For how workspace permissions interact with this company setting, see OAuth and MCP access.

## Turn MCP OAuth access on or off

To update MCP OAuth access for your company:

- Go to Settings > Admin Settings > OAuth.
 
- In Global access controls, turn MCP OAuth access on or off.

When MCP OAuth access is on, users with the “Use MCP Server” permission can authorize approved MCP clients.

When it’s off, OAuth access to the MCP server is denied for all users and workspaces in your company. Existing MCP connections stop working the next time they use or refresh their OAuth access token.

If Braze has turned off the remote MCP server for your environment, the MCP OAuth access toggle is disabled and a message explains that the company setting has no effect until the remote MCP server is turned on again.

## Audit OAuth activity

Braze records OAuth connections to the MCP server in the security event report. Use this report to audit when users connect through OAuth.

To revoke one user’s MCP access, remove the “Use MCP Server” permission from that user. For setup and troubleshooting guidance, see Setting up the Braze MCP server.

- 

New Stuff!
