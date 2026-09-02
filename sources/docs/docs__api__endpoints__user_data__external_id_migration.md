---
url: https://www.braze.com/docs/api/endpoints/user_data/external_id_migration
slug: docs__api__endpoints__user_data__external_id_migration
title: "External ID Migration"
description: "This landing page explains and lists the Braze external ID migration feature."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# External ID Migration 

The External ID Migration API allows you to rename existing external IDs (creating a new primary ID and deprecating the existing ID) and remove deprecated IDs post-migration. 

 We’ve designed this solution to allow multiple external IDs in order to support a migration period whereby older versions of your apps still in the wild that use the previous external ID naming schema don’t break. We highly recommend removing deprecated external IDs when your old naming schema is no longer in use.

## External ID Migration Endpoints 

- 

 POST: Rename External IDs

- 

 POST: Remove Deprecated External IDs

- 

New Stuff!
