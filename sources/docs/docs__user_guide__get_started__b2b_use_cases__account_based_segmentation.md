---
url: https://www.braze.com/docs/user_guide/get_started/b2b_use_cases/account_based_segmentation
slug: docs__user_guide__get_started__b2b_use_cases__account_based_segmentation
title: "Set up account-based segmentation"
description: "Learn how to use various Braze features to power your B2B account-based segmentation use cases."
section: user_guide/get_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# Set up account-based segmentation

This page shows how to use various Braze features to power your B2B account-based segmentation use cases.

You can do B2B account-based segmentation in two ways, depending on how you set up your B2B data model:

- When using catalogs for your business objects
 
- When using connected sources for your business objects

## Setting up B2B account-based segmentation

### Option 1: When using catalogs for your business objects

#### Basic SQL template segmentation

To help you get started, we created basic SQL templates for simple account-based segmentation.

Let’s say you want to segment users who are employees of a target enterprise account.

- Go to Audience > Segment Extensions > Create New Extension > Start with a template and select the template Catalog segment for events. 

The SQL editor automatically populates with a template that joins user event data with catalog data to segment users who engage with certain catalog items. 

- Use the Variables tab to provide the necessary fields for your template before generating your segment.

For Braze to identify users based on their engagement with catalog items, you need to do the following:

- Select a catalog that contains a catalog field
 
- Select a custom event that contains an event property
 
- Match your catalog field and event property values

##### Variables guidelines for B2B use cases

Select the following variables for a B2B account-based segmentation use case:

 Variable | 
 Property | 

 Catalog | 
 Account Catalog | 

 Catalog field | 
 Id | 

 Custom event | 
 account_linked | 

 Custom event property | 
 account_id | 

 (Under Filter SQL Results) Catalog Field | 
 Classification | 

 (Under Filter SQL Results) Value | 
 Enterprise | 

#### Sophisticated SQL segmentation

For more sophisticated or complex segmentation, refer to SQL Segment Extensions. To help you get started, here are a few SQL templates you can use to help you get a head start with B2B account-based segmentation:

- Create a segment comparing two filters in a single catalog (such as users who work in the restaurant industry for an enterprise-level account). You must include the catalog ID and item ID.

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
WITH salesforce_accounts AS (
 SELECT
 ITEM_ID as id,
 MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
 MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
 FROM CATALOGS_ITEMS_SHARED
 WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
 GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
; 

```
 | 

- Create a segment comparing two filters across two separate catalogs (such as users associated with enterprise-target accounts that have an open “Stage 3” opportunity).

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
18
19
20
21
22
23
24
25
26
27
28
29

```
 | 
```
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
 SELECT
 ITEM_ID as id,
 MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
 MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
 FROM CATALOGS_ITEMS_SHARED
 WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
 GROUP BY ITEM_ID
),
salesforce_opportunities AS (
 SELECT
 ITEM_ID as id,
 MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
 MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
 FROM CATALOGS_ITEMS_SHARED
 WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
 GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;

```
 | 

### Option 2: When using connected sources for your business objects

For the basics on how to use connected sources in segmentation, refer to CDI Segment Extensions. Use the templates covered in When using catalogs for inspiration on how to format the source tables, as you can format them any way you want.

## Using your account-based extension in a segment

After you’ve created your account-level segmentation in the earlier in this section steps, you can directly pull those Segment Extensions into your targeting criteria. It’s also easy to layer on incremental user demographic criteria such as role, engagement with previous campaigns, and more. For more information, refer to Using your extension in a segment.

- 

New Stuff!
