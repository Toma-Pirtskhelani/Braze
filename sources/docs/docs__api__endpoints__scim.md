---
url: https://www.braze.com/docs/api/endpoints/scim
slug: docs__api__endpoints__scim
title: "SCIM Endpoints"
description: "This landing page lists the Braze SCIM endpoints."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# SCIM Endpoints 

The System for Cross-domain Identity Management (SCIM) specification is designed to make managing user identities in cloud-based applications and services easier by providing a defined schema for representing users and groups. Use the Braze SCIM endpoints to manage automated user provisioning.

## 

- 

 POST: Create Dashboard User Account

- 

 GET: Look Up Existing Dashboard User Account by Resource ID

- 

 GET: Search Existing Dashboard User Account by Email

- 

 PUT: Update Dashboard User Account

- 

 DELETE: Remove Dashboard User Account

important

These SCIM API endpoints require the custom SCIM integration. If you set up an identity provider (IdP) integration (Okta or Entra ID), you can’t use these endpoints; only one SCIM bridge can be set up per company. The IdP integrations create and delete user accounts automatically but don’t manage permissions or workspace assignments. You must set those manually in the Braze dashboard.

## How to export a list of users with dashboard access

Use this workflow to audit users who have access to your Braze dashboard.

- Download the Security Event report from Settings > Admin Settings > Security Settings > Security Event Download.
 
- Extract the user emails from the report.
 
- For each email, use GET: Search Existing Dashboard User Account by Email to retrieve the user details.
 
- If needed, use the returned resource id with GET: Look Up an Existing Dashboard User Account by Resource ID for additional user details.

For the full SCIM endpoint list, see SCIM Endpoints. For more information about the report source, see Downloading a security event report.

- 

New Stuff!
