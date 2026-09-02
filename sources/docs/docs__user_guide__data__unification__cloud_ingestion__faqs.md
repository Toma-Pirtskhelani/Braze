---
url: https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs
slug: docs__user_guide__data__unification__cloud_ingestion__faqs
title: "Frequently asked questions"
description: "This page answers frequently asked questions about Cloud Data Ingestion."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Frequently asked questions

This page contains answers to some frequently asked questions for Cloud Data Ingestion.

## Why was I emailed: “Error in CDI Sync”?

This type of email usually means there’s an issue with your CDI setup. Here are some common issues and how to fix them:

### CDI can’t access the data warehouse or table using your credentials

This could mean the credentials in CDI are incorrect or are misconfigured on the data warehouse. For more information, refer to Data Warehouse Integrations.

### The table cannot be found

Try updating your integration with the correct database configuration or create matching resources on the data warehouse, such as database/table.

### The catalog cannot be found

The catalog set up in the integration doesn’t exist in the Braze catalog. A catalog can be removed after the integration was set up. To resolve the issue, either update the integration to use a different catalog or create a new catalog that matches the catalog name in the integration.

## Why was I emailed: “Row errors in your CDI sync”?

This type of email means that some of your data could not be processed during the sync. To find out the specific error, you can review the logs in Braze by going to CDI > Sync Log.

## How do I fix “Time must be string in ISO8601 Format” in CDI setup?

This error means the event time value in your CDI payload is not in a supported datetime format.

For event and purchase payloads, format time as:

- An ISO 8601 string, or
 
- yyyy-MM-dd'T'HH:mm:ss:SSSZ

If time is omitted, Braze uses UPDATED_AT as the event time.

For full payload requirements, refer to Table setup for Cloud Data Ingestion.

## How do I fix errors for Test Connection and support emails?

- snowflake
 
- redshift
 
- bigquery
 
- databricks

### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### Error connecting to Snowflake instance: Incoming request with IP is not allowed to access Snowflake

Try adding the official Braze IPs to your IP allowlist. For more information, refer to Data Warehouse Integrations, or allow the relevant IPs:

- united states (us)
 
- european union (eu)
 
- australia (au)
 
- indonesia (id)
 
- japan (jp)
 
- south korea (kr)

For instances US-01, US-02, US-03, US-04, US-05, US-06, US-07, these are the relevant IP addresses:

- 23.21.118.191
 
- 34.206.23.173
 
- 50.16.249.9
 
- 52.4.160.214
 
- 54.87.8.34
 
- 54.156.35.251
 
- 52.54.89.238
 
- 18.205.178.15

For instance US-08, these are the relevant IP addresses:

- 52.151.246.51
 
- 52.170.163.182
 
- 40.76.166.157
 
- 40.76.166.170
 
- 40.76.166.167
 
- 40.76.166.161
 
- 40.76.166.156
 
- 40.76.166.166
 
- 40.76.166.160
 
- 40.88.51.74
 
- 52.154.67.17
 
- 40.76.166.80
 
- 40.76.166.84
 
- 40.76.166.85
 
- 40.76.166.81
 
- 40.76.166.71
 
- 40.76.166.144
 
- 40.76.166.145

For instance US-10, these are the relevant IP addresses:

- 100.25.232.164
 
- 35.168.86.179
 
- 52.7.44.117
 
- 3.92.153.18
 
- 35.172.3.129
 
- 50.19.162.19

For instances EU-01 and EU-02, these are the relevant IP addresses:

- 52.58.142.242
 
- 52.29.193.121
 
- 35.158.29.228
 
- 18.157.135.97
 
- 3.123.166.46
 
- 3.64.27.36
 
- 3.65.88.25
 
- 3.68.144.188
 
- 3.70.107.88

For instance AU-01, these are the relevant IP addresses:

- 13.210.1.145
 
- 13.211.70.159
 
- 13.238.45.54
 
- 52.65.73.167
 
- 54.153.242.239
 
- 54.206.45.213

For instance ID-01, these are the relevant IP addresses:

- 108.136.157.246
 
- 108.137.30.207
 
- 16.78.128.71
 
- 16.78.14.134
 
- 16.78.162.208
 
- 43.218.73.35

For instance JP-01, these are the relevant IP addresses:

- 13.159.155.212
 
- 54.199.221.241
 
- 13.192.23.16
 
- 54.250.120.139
 
- 18.181.114.232
 
- 3.114.38.100

For instance KR-01, these are the relevant IP addresses:

- 43.200.215.4
 
- 52.79.67.175
 
- 52.79.113.60
 
- 3.34.212.92
 
- 54.116.134.231
 
- 3.37.197.225

### Error executing SQL due to customer config: 002003 (42S02): SQL compilation error: does not exist or not authorized

If the table doesn’t exist, create the table. If the table does exist, verify that the user and role have permissions to read from the table.

### Could not use schema

If you receive this error, grant access to that schema for the specified user or role.

### Could not use role

If you receive this error, allow that user to use the specified role.

### User access disabled

If you receive this error, allow that user access to your Snowflake account.

### Error connecting to Snowflake instance with current and old key

If you receive this error, make sure the user is using the current public key as displayed in your Braze dashboard.

### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### Permission denied for relation {table_name}

If you receive this error:

- Grant the usage permission on the schema for that user.
 
- Grant the select permission on the table for that user.

### Create Connection Error

If you receive this error, verify the Redshift endpoint and port are correct.

### Create SSH Tunnel Error

If you receive this error:

- Verify the public key on your braze dashboard is on ec2 host used for SSH tunneling.
 
- Verify your username is correct.
 
- Verify the SSH Tunnel is correct.

### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### User does not have permission to query table

If you receive this error, add user permissions to query the table.

### Your usage exceeded the custom quota

If you receive this error, your quota needs to be updated so you can continue syncing at your current rate.

### Table was not found in location {region} Location

If you receive this error, verify your table is in the correct project and dataset.

### Invalid JWT Signature

If you receive this error, check that the BigQuery API service is enabled for your account.

### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. For Databricks, there may be two to five minutes of warm-up time when Braze connects to Classic and Pro SQL instances, which will lead to delays during connection setup and testing, as well as at the beginning of scheduled syncs. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### Command failed because warehouse was stopped

If you receive this error, ensure Databricks warehouse is running.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

If you receive this error, see Databricks: Forbidden error while accessing S3 data.

## How do I update my email alert preferences for CDI integrations?

Each integration has its own notification preference. Go to the CDI page and select the integration name you want to update. In the Notification preferences section you can update how you receive alerts regarding the selected integration.

## What happens if a future UPDATED_AT gets synced with an integration?

CDI uses UPDATED_AT to decide what data is new. After a future UPDATED_AT is synced, any data prior to that future date and time will not be processed. To fix this:

- Correct UPDATED_AT.
 
- Remove any old data that’s already synced with Braze
 
- Create a new integration to process that table again.

## Why doesn’t “Rows Synced” match the number in my warehouse?

CDI uses UPDATED_AT to decide which records to pick up during a sync. Check out this illustration to see how it works. At the beginning of a sync run, CDI queries your warehouse to get all records with UPDATED_AT later than the previously processed UPDATED_AT value. Records at the exact boundary timestamp may also be re-synced if new rows share that timestamp. Any record picked up at the time when the query executes is synced into Braze. Here are common cases when a record might not be synced:

- You’re adding records to the table with an UPDATED_AT value that has already been processed.
 
- You’re updating record values after they have been processed by a sync, but leaving UPDATED_AT unchanged.
 
- You’re adding or updating records while a sync is in progress. Depending on when the CDI query executes, there could be race conditions that lead to records not being picked up.

tip

To avoid these behaviors in the future, we recommend using monotonically increasing UPDATED_AT values and not updating the table during your scheduled sync run.

## Do I need mostly distinct UPDATED_AT values for large CDI imports?

Yes. For high-volume runs (for example, more than approximately 10 million rows), make sure your source data has mostly distinct UPDATED_AT values. If too many rows share the same timestamp, CDI is more likely to re-select rows at boundary timestamps in later runs. This can increase duplicate syncs and data point consumption.

For more information about CDI boundary behavior, see Avoid resyncing rows with duplicate timestamps.

### Where do I run these SQL checks?

Run the checks directly in your data warehouse SQL editor, against the same table or view used by your CDI integration:

- Snowflake: Projects > Worksheets (for more information, see Snowflake Worksheets)
 
- Redshift: Query Editor v2 (for more information, see Using Amazon Redshift Query Editor v2)
 
- BigQuery: BigQuery Studio SQL workspace (for more information, see BigQuery Studio introduction)
 
- Databricks: SQL editor (SQL warehouse) (for more information, see Databricks SQL editor)
 
- Fabric: SQL query editor

Use this process before enabling or scaling a large sync:

- Identify the exact CDI source table or view and the sync window you want to validate.
 
- Open your warehouse SQL editor and select the same database and schema used by CDI, then use a role with read access to the source table or view.
 
- Run the distinct timestamp count query to measure how many distinct UPDATED_AT values exist in that window.
 
- Run the query that groups by UPDATED_AT and counts rows to find timestamps with unusually high row counts.
 
- If many rows share identical timestamps, adjust your ingestion process so consecutive batches use progressively newer UPDATED_AT values, or increase timestamp precision so rows are more distributed.
 
- Re-run both queries until concentration is reduced, then launch or scale your sync.
 
- After launch, monitor CDI > Sync Log for unexpected re-sync volume at boundary timestamps.

Use checks like these in your warehouse:

```

1
2
3
4
5
6
7

```
 | 
```
SELECT
 COUNT(*) AS total_rows,
 COUNT(DISTINCT UPDATED_AT) AS distinct_timestamps,
 ROUND(COUNT(*) * 1.0 / NULLIF(COUNT(DISTINCT UPDATED_AT), 0), 2) AS avg_rows_per_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
 AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP);

```
 | 

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

```
 | 
```
SELECT
 UPDATED_AT,
 COUNT(*) AS rows_at_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
 AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP)
GROUP BY UPDATED_AT
ORDER BY rows_at_timestamp DESC
LIMIT 20;

```
 | 

If your warehouse doesn’t support LIMIT (for example, Fabric), use an equivalent syntax such as TOP.

## Why can a CDI sync with a small number of rows still take several minutes?

A CDI sync includes a fixed startup period before row processing begins. Because this startup time is similar across sync sizes, a small sync can still take several minutes and may appear slower in rows per minute. Total sync time still depends on your source query complexity, data shape, and available capacity in your data warehouse. For more information, see Data warehouse integrations.

## During a sync, is the order preserved if multiple records share the same ID?

The processing order is not 100% predictable. For example, if there are multiple rows with the same EXTERNAL_ID in the table during a sync, we cannot guarantee which value will end up in the final profile. If you’re updating the same EXTERNAL_ID with different attributes in the payload column, all changes are reflected when the sync is completed.

## Why are new users not being created from my CDI sync?

If your CDI integration has the Update existing users only option enabled, only users who already exist in Braze are updated, and new users are not created. This means that if a row in your sync table references an EXTERNAL_ID that doesn’t match any existing Braze user, that row is skipped.

To create new users through CDI, turn off the Update existing users only toggle in your integration settings. Go to Data Settings > Cloud Data Ingestion and select an integration.

## What are the security measures for CDI?

### Our measures

Braze has the following measures in place for CDI:

- All credentials are encrypted within our database, and only certain employees have authenticated access to them.
 
- We use encrypted connections to get data to customer warehouses.
 
- We make requests to the Braze API endpoints using the same API keys and TLS connections that we recommend our customers use.
 
- We regularly update our libraries and get any security patches.

### Your measures

We recommend you and your team set up the following security measures on your side:

- Restrict credential access to the minimum required for CDI to operate. This is because we need to be able to run select (and count) on the specific tables and views.
 
- Restrict the IPs that can access the tables to officially published Braze IPs.

- 

New Stuff!
