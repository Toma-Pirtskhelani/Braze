---
url: https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/decisioning_studio
slug: docs__user_guide__data__unification__cloud_ingestion__decisioning_studio
title: "Sync BrazeAI Decisioning Studio data"
description: "Learn how to sync data warehouse tables to BrazeAI Decisioning Studio using Cloud Data Ingestion."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Sync BrazeAI Decisioning Studio data

This page covers how to sync data from your data warehouse directly to BrazeAI Decisioning Studio™ using Cloud Data Ingestion (CDI).

With CDI’s Decisioning Studio destination, CDI can also sync warehouse data directly to BrazeAI Decisioning Studio. Data from these syncs is made available to Decisioning Studio for activation, but your user profiles and Braze workspaces remain unchanged.

important

This feature is in early access. Contact your customer success manager or account manager for access.

## How it works

When you create a sync, choose Decisioning Studio as the destination and write a SQL query that returns the data you want to sync. CDI runs that query on the schedule you set and delivers the results as a Decisioning Studio asset. Each sync maps to a single asset, so you can’t point more than one sync at the same asset.

Unlike syncs to the Braze Data Platform, Decisioning Studio syncs don’t map your data to user profiles, events, or catalogs.

For the other ways to make data available to Decisioning Studio, see Connect your data.

## Prerequisites

- Access to Braze and BrazeAI Decisioning Studio.
 
- An active Cloud Data Ingestion data warehouse source. If you haven’t set one up, see Data warehouse integrations.
 
- The table or view you want to sync.
 
- A column (or columns) in that table to use as the primary key, and a timestamp column CDI can use for incremental syncing.

## Create a Decisioning Studio sync

### Step 1: Create the sync and select the destination

- Go to Data Settings > Cloud Data Ingestion > Syncs.
 
- Select Create data sync.
 
- Enter an Integration Name, then select your source under Data sources.
 
- Under Destination, set Data destination to BrazeAI Decisioning Studio™.
 
- Under Data category, select the Decisioning Studio data type that best matches your table. Choose from Customer profile, Message engagement events, Conversion events, or Other. This tags the data for Decisioning Studio and doesn’t change how CDI processes your rows.

### Step 2: Write your SQL query

On the Data definition step, write a SQL query that returns the data from the table or view you want to sync. The query result becomes the schema for your sync.

You can use the Source Explorer to browse available tables and views, or the AI SQL generator to get help writing your query.

Your query must return an UPDATED_AT column as CDI uses UPDATED_AT for incremental syncing and change tracking. On each sync run, CDI syncs only rows where UPDATED_AT is later than the last synced value. If the timestamp column you identified isn’t already named UPDATED_AT, you can alias it in your query:

```

1

```
 | 
```
SELECT *, LAST_MODIFIED AS UPDATED_AT FROM my_table

```
 | 

For more on how UPDATED_AT controls incremental syncing, including what happens when you move it backward, see Understanding the UPDATED_AT column.

note

Only single-statement, read-only queries are supported, including JOIN clauses. CDI runs read-only queries and doesn’t modify your underlying tables.

### Step 3: Preview and validate your query

Select Preview and validate to run your query. The Query preview (first 10 rows) section shows the first 10 rows returned from your source, along with each column’s detected data type, so you can confirm the data looks correct before continuing.

### Step 4: Select a primary key

Every Decisioning Studio sync needs a primary or composite key, one or more columns that uniquely identify each row. After validation succeeds, open the Primary key dropdown and select a column to serve as the primary key. Selecting multiple columns forms a composite key.

tip

A good primary key is unique for every row, never empty, and stable across sync runs. Avoid values generated at query time, such as UUID() or CURRENT_TIMESTAMP, as they can cause duplicate or dropped rows.

### Step 5: Set notifications, schedule, and create the sync

- On the Notifications step, enter one or more Contact Email(s) to receive sync error notifications. You can also turn on Row Error and Sync success notifications.
 
- On the Schedule step, turn on Recurring sync to run the sync automatically on a schedule. With Recurring sync off, the sync runs only when you trigger it, either manually from the dashboard or through the Trigger a sync endpoint.
 
- Review the Summary, then create the sync.

## Editing a sync

When you edit an existing sync, any change to your SQL query requires revalidation before you can save. Primary and composite keys cannot be changed and must still return.

Valid changes take effect on the next sync run.

## Handling schema changes

CDI handles source schema changes additively. On every sync run, CDI compares your source schema to the existing Decisioning Studio asset and adds any new columns while preserving the ones already there.

 Change in your source table | 
 Sync behavior | 

 A new column is added | 
 CDI adds the column to the Decisioning Studio asset. Rows delivered before the column existed show null for it. | 

 A column is removed | 
 CDI stops updating that column, but the column and its existing data remain in the asset. The other columns keep syncing. | 

 A column is renamed | 
 Treated as a removed column plus a new column. The original column stays in the asset, and the new column is added. | 

 A column’s data type changes | 
 CDI converts values where it can. Rows it can’t convert are reported as row errors in the sync’s run details. | 

When CDI detects a schema change, it’s shown in the sync’s run details and on the edit sync page, and your notification contacts receive an email alert. To change which columns are delivered, update your SQL query and revalidate.

- 

New Stuff!
