---
url: https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data
slug: docs__user_guide__data__unification__cloud_ingestion__sync_catalogs_data
title: "Sync and delete catalog data"
description: "This page provides an overview of how to sync catalog data."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Sync and delete catalog data

This page discusses how to sync catalog data.

## Step 1: Create a new catalog

Before creating a new Cloud Data Ingestion (CDI) integration for catalogs, you need to create a new catalog or identify an existing catalog you want to use for the integration. There are a few ways to create a new catalog and any of these will work for the CDI integration:

- Upload a CSV
 
- Create a catalog in the Braze dashboard or during CDI setup.
 
- Create a catalog using the Create catalog endpoint

Any changes to the catalog schema (for example, adding new fields or changing field type) must be made through the catalog dashboard before updated data is synced through CDI. We recommend making these updates when the sync is paused or not scheduled to run to avoid conflicts between your data warehouse data and the schema in Braze.

## Step 2: Integrate Cloud Data Ingestion with catalog data

The setup for a catalog sync closely follows the process for user-data CDI integrations.

- snowflake
 
- redshift
 
- bigquery
 
- databricks
 
- microsoft fabric
 
- s3

- Set up a source table in Snowflake. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.

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

```
 | 
```
 CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
 CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
 CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
 UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
 --ID of the catalog item to be created or updated
 ID VARCHAR(16777216) NOT NULL,
 --Catalog fields and values that should be added or updated
 PAYLOAD VARCHAR(16777216) NOT NULL,
 --The catalog item associated with this ID should be deleted
 DELETED BOOLEAN
 );

```
 | 

- Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.

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

```
 | 
```
 CREATE ROLE BRAZE_INGESTION_ROLE;

 GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
 GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
 GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

 CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
 GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

 CREATE USER BRAZE_INGESTION_USER;
 GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```
 | 

- If your Snowflake account has network policies, allowlist the Braze IPs so the CDI service can connect. For a list of IPs, refer to the Cloud Data Ingestion.
 
- In the Braze dashboard, navigate to Technology Partners > Snowflake, and create a new sync.
 
- Enter connection details (or reuse existing credentials) and the source table.
 
- Proceed to step 2 of the setup flow, select the “Catalogs” sync type, and input the integration name and schedule. Note that the name of the integration should exactly match the name of the catalog you previously created.
 
- Choose a sync frequency and proceed to the next step.
 
- Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake. To complete this step, you will need someone with SECURITYADMIN access or higher in Snowflake.
 
- Select Test Connection so that everything works as expected.
 
- Save the sync, and use the synced catalog data for all your personalization use cases.

- Set up a source table in Redshift. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.

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

```
 | 
```
 CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
 CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
 CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
 updated_at timestamptz default sysdate not null,
 --ID of the catalog item to be created or updated
 id varchar not null,
 --Catalog fields and values that should be added or updated
 payload varchar(max),
 --The catalog item associated with this ID should be deleted
 deleted boolean
 )

```
 | 

- 
 
Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.

```

1
2
3

```
 | 
```
 CREATE USER braze_user PASSWORD '{password}';
 GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
 GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;

```
 | 

- If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. Allow access from the following IPs corresponding to your Braze dashboard’s region. For a list of IPs, refer to the Cloud Data Ingestion.

- Optionally, set up a new project or dataset to hold your source table.

```

1

```
 | 
```
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;

```
 | 

Create one or more tables to use for your CDI integration with the following fields:

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
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
 updated_at TIMESTAMP DEFAULT current_timestamp,
 id STRING,
 payload JSON,
 deleted BOOLEAN
);

```
 | 

 FIELD NAME | 
 TYPE | 
 MODE | 

 UPDATED_AT | 
 TIMESTAMP | 
 REQUIRED | 

 PAYLOAD | 
 JSON | 
 REQUIRED | 

 ID | 
 STRING | 
 REQUIRED | 

 DELETED | 
 BOOLEAN | 
 OPTIONAL | 

- Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse those—but make sure to extend access to the catalog source table. 
The service account should have the in the following section permissions:

- BigQuery Connection User: This will allow Braze to make connections.
 
- BigQuery User: This will provide Braze access to run queries, read dataset metadata, and list tables.
 
- BigQuery Data Viewer: This will provide Braze access to view datasets and their contents.
 
- BigQuery Job User: This will provide Braze access to run jobs

After creating the service account and granting permissions, generate a JSON key. Refer to Keys create and delete for more information. You’ll update this to the Braze dashboard later.

- If you have network policies in place, you must give Braze network access to your BigQuery instance. For a list of IPs, refer to the Cloud Data Ingestion.

- Set up a source table in Databricks. You can use the names in the following example or choose your catalog, schema, and table names. You can also use a view or a materialized view instead of a table.

```

1

```
 | 
```
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;

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

```
 | 
```
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
 updated_at TIMESTAMP DEFAULT current_timestamp(),
 id STRING,
 deleted BOOLEAN,
 payload STRING, STRUCT, or MAP
);

```
 | 

 FIELD NAME | 
 TYPE | 
 MODE | 

 UPDATED_AT | 
 TIMESTAMP | 
 REQUIRED | 

 PAYLOAD | 
 STRING, STRUCT, or MAP | 
 REQUIRED | 

 ID | 
 STRING | 
 REQUIRED | 

 DELETED | 
 BOOLEAN | 
 NULLABLE | 

- Create a personal access token in your Databricks workspace.

- a. Select your Databricks username, then select User Settings from the dropdown menu.
 
- b. On the Access tokens tab, select Generate new token.
 
- c. Enter a comment that helps you to identify this token, such as “Braze CDI”.
 
- d. Change the token’s lifetime to no lifetime by leaving the Lifetime (days) box blank. Select Generate.
 
- e. Copy the displayed token, and then select Done.
 
- f. Keep the token in a safe place until you need to enter it during the credential creation step in the Braze dashboard.

- If you have network policies in place, you must give Braze network access to your Databricks instance. For a list of IPs, see the Cloud Data Ingestion page.

Create one or more tables to use for your CDI integration with the following fields:

```

1
2
3
4
5
6
7
8

```
 | 
```
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
 UPDATED_AT DATETIME2(6) NOT NULL,
 PAYLOAD VARCHAR NOT NULL,
 ID VARCHAR NOT NULL,
 DELETED BIT
)
GO

```
 | 

- Set up a service principal and grant proper permissions. If you already have credentials from an existing sync, you can reuse those—just make sure to extend access to the catalog source table. To learn more about how to create a new service principal and credentials, see the Cloud Data Ingestion page.

- If you have network policies in place, you must give Braze network access to your Microsoft Fabric instance. For a list of IPs, see the Cloud Data Ingestion.

Create source files in S3 using JSON or CSV format. Each file must include the following fields:

 Field | 
 Required? | 
 Description | 

 ID | 
 Yes | 
 The ID of the catalog item to create or update. | 

 PAYLOAD | 
 Yes | 
 A JSON string of the fields to sync to the catalog item in Braze. | 

 DELETED | 
 Optional | 
 When set to true, the corresponding catalog item is removed from the catalog. | 

 UPDATED_AT | 
 Unsupported | 
 File storage doesn’t support UPDATED_AT columns. | 

note

Filenames must follow AWS rules and be unique. Append timestamps to help ensure uniqueness.

The complete S3 setup requires an S3 bucket, an Amazon SQS queue, and an AWS IAM role and policy. Braze only processes files uploaded after the sync is created, so re-upload existing files you want to ingest.

For the full S3 setup flow, see File storage integrations, especially:

- Setting up Cloud Data Ingestion in AWS
 
- Setting up Cloud Data Ingestion in Braze
 
- Troubleshooting

For common AWS-side notification and permission issues, refer to Granting permissions to publish event notification messages to a destination.

The following examples show valid JSON and CSV formats for syncing catalog data from file storage.

- json catalogs
 
- csv catalogs with delete
 
- csv catalogs without delete

```
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}

```

important

Each line in your source file must contain valid JSON or the file is skipped.

```

1
2
3
4

```
 | 
```
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true

```
 | 

```

1
2
3

```
 | 
```
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"

```
 | 

For additional file examples, see File storage integrations.

## How the integration works

note

The sync views in this section apply to data warehouse integrations only. For S3 file storage, Braze processes new files as they’re uploaded to your bucket. See File storage integrations for details.

Each time the sync runs, Braze pulls in all rows where UPDATED_AT is later than the last synced value. Rows at the exact boundary timestamp may be re-synced if new rows share that same timestamp. We recommend creating a view in your data warehouse from your catalog data to set up a source table that will fully refresh each time a sync runs. With views, you won’t need to rewrite the query each time.

For example, if you have a table of product data (product_catalog_1) with product_id and three additional attributes, you could sync the following view:

- snowflake
 
- redshift
 
- bigquery
 
- databricks
 
- microsoft fabric

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

```
 | 
```
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS 
SELECT
 CURRENT_TIMESTAMP as UPDATED_AT,
 product_id as id,
 TO_JSON(
 OBJECT_CONSTRUCT (
 'attribute_1',
 attribute_1,
 'attribute_2',
 attribute_2,
 'attribute_3',
 attribute_3)
 )as PAYLOAD FROM "product_catalog_1";

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
10
11
12
13

```
 | 
```
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
 CURRENT_TIMESTAMP as UPDATED_AT,
 Product_id as id,
 JSON_SERIALIZE(
 OBJECT (
 'attribute_1',
 attribute_1,
 'attribute_2',
 attribute_2,
 'attribute_3',
 attribute_3)
 ) as PAYLOAD FROM "product_catalog_1";

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
10
11

```
 | 
```
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
 last_updated as UPDATED_AT,
 product_id as ID,
 TO_JSON(
 STRUCT(
 attribute_1,
 attribute_2,
 attribute_3,
 )
 ) as PAYLOAD 
 FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);

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
10
11

```
 | 
```
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
 last_updated as UPDATED_AT,
 product_id as ID,
 TO_JSON(
 STRUCT(
 attribute_1,
 attribute_2,
 attribute_3,
 )
 ) as PAYLOAD 
 FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);

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

```
 | 
```
CREATE VIEW [braze].[user_update_example]
AS SELECT 
 id as ID,
 CURRENT_TIMESTAMP as UPDATED_AT,
 JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;

```
 | 

- The data fetched from the integration will be used to create or update items in the target catalog based on the id provided.
 
- If DELETED is set to true, the corresponding catalog item will be deleted.
 
- The sync won’t log data points, but all data synced will count toward your total catalog usage; this usage is measured based on the total data stored, so you don’t need to worry about only syncing changed data.

- 

New Stuff!
