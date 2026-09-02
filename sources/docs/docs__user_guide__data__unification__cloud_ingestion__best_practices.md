---
url: https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/best_practices
slug: docs__user_guide__data__unification__cloud_ingestion__best_practices
title: "Best practices"
description: "This page provides an overview of Cloud Data Ingestion, best practices, and product limitations."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Best practices

Braze Cloud Data Ingestion allows you to set up a direct connection from your data warehouse or file storage system to Braze to sync relevant user or catalog data. When you sync this data to Braze, you can leverage it for use cases such as personalization, triggering, or segmentation.

## Understanding the UPDATED_AT column

note

UPDATED_AT is relevant for data warehouse integrations only, not for S3 syncs.

When a sync runs, Braze directly connects to your data warehouse instance, retrieves all new data from the specified table, and updates the corresponding data on your Braze dashboard. Each time the sync runs, Braze reflects any updated data.

important

Braze CDI will sync rows strictly based on the UPDATED_AT value, regardless of whether the row content is the same as what’s currently in Braze. Given that, we recommend using UPDATED_AT properly to only sync new or updated data to avoid unnecessary data point usage.

### Example: Recurring sync

To illustrate how UPDATED_AT is used in a CDI sync, consider this example recurring sync for updating user attributes:

- File storage sources

- Amazon S3

## Supported data types

Cloud Data Ingestion supports the following data types:

- User attributes, including:

- Nested custom attributes
 
- Arrays of objects
 
- Subscription statuses

- Custom events
 
- Purchase events
 
- Catalog items
 
- User delete requests

### Avoiding data type issues

When using CDI to sync data from external sources (such as Databricks or Snowflake), ensure your source columns use the correct data types before syncing. Common issues include:

- Timestamps stored as strings: Make sure your date columns use a timestamp or datetime type in your source database, not a varchar or string.
 
- Numbers stored as strings: Cast numeric columns to integer or float types in your source query before syncing.
 
- Inconsistent types across syncs: If a column type changes between syncs, Braze may reject the new data. Verify your source schema remains consistent.

For forcing or changing data types for custom attributes in the Braze dashboard, see Manage custom data.

You can update user data by external ID, user alias, Braze ID, email, or phone number. You can delete users by external ID, user alias, or Braze ID.

## What gets synced

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the UPDATED_AT column in your table or view. Braze selects and imports any rows where UPDATED_AT is later than the last synced UPDATED_AT value. Rows at the exact boundary timestamp may also be re-synced if new rows are added at that same timestamp between runs.

important

CDI tracks the number of rows at the last synced UPDATED_AT value. If new rows are added with that same timestamp between runs, CDI switches to an inclusive boundary (>=) and re-syncs all rows at that timestamp, including ones already processed. To avoid duplicate syncs and unnecessary data point consumption, use unique UPDATED_AT values across sync runs. For more information, see Avoid resyncing rows with duplicate timestamps.

In your data warehouse, add the following users and attributes to your table, setting the UPDATED_AT time to the time you add this data:

 UPDATED_AT | 
 EXTERNAL_ID | 
 PAYLOAD | 

 2022-07-17 08:30:00 | 
 customer_1234 | 

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
{
 "attribute_1":"abcdefg",
 "attribute_2": {
 "attribute_a":"example_value_1",
 "attribute_b":"example_value_1"
 },
 "attribute_3":"2019-07-16T19:20:30+1:00"
}

```
 | 

 | 

 2022-07-18 11:59:23 | 
 customer_3456 | 

```

1
2
3
4
5
6

```
 | 
```
{
 "attribute_1":"abcdefg",
 "attribute_2":42,
 "attribute_3":"2019-07-16T19:20:30+1:00",
 "attribute_5":"testing"
}

```
 | 

 | 

 2022-07-19 09:07:23 | 
 customer_5678 | 

```

1
2
3
4
5

```
 | 
```
{
 "attribute_1":"abcdefg",
 "attribute_4":true,
 "attribute_5":"testing_123"
}

```
 | 

 | 

During the next scheduled sync, Braze syncs all rows with an UPDATED_AT timestamp later than the most recent synced timestamp. Braze updates or adds fields, so you do not need to sync the full user profile each time. After the sync, user profiles reflect the new updates:

Recurring sync, second run on July 20, 2022 at 12 pm

 UPDATED_AT | 
 EXTERNAL_ID | 
 PAYLOAD | 

 2022-07-17 08:30:00 | 
 customer_1234 | 

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
{
 "attribute_1":"abcdefg",
 "attribute_2": {
 "attribute_a":"example_value_2",
 "attribute_b":"example_value_2"
 },
 "attribute_3":"2019-07-16T19:20:30+1:00"
}

```
 | 

 | 

 2022-07-18 11:59:23 | 
 customer_3456 | 

```

1
2
3
4
5
6

```
 | 
```
{
 "attribute_1":"abcdefg",
 "attribute_2":42,
 "attribute_3":"2019-07-16T19:20:30+1:00",
 "attribute_5":"testing"
}

```
 | 

 | 

 2022-07-19 09:07:23 | 
 customer_5678 | 

```

1
2
3
4
5

```
 | 
```
{
 "attribute_1":"abcdefg",
 "attribute_4":true,
 "attribute_5":"testing_123"
}

```
 | 

 | 

 2022-07-16 00:25:30 | 
 customer_9012 | 

```

1
2
3
4
5

```
 | 
```
{
 "attribute_1":"abcdefg",
 "attribute_4":false,
 "attribute_5":"testing_123"
}

```
 | 

 | 

A new row was added for customer_9012, but its UPDATED_AT value (2022-07-16 00:25:30) is earlier than the stored timestamp (2022-07-19 09:07:23), so it won’t be synced. However, the existing row for customer_5678 has an UPDATED_AT value equal to the stored timestamp, so it is re-synced due to the inclusive boundary. For more details about this behavior, refer to Make sure the UPDATED_AT time isn’t the same time as your sync. The stored UPDATED_AT remains 2022-07-19 09:07:23.

Recurring sync, third run on July 21, 2022 at 12 pm

 UPDATED_AT | 
 EXTERNAL_ID | 
 PAYLOAD | 

 2022-07-17 08:30:00 | 
 customer_1234 | 

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
{
 "attribute_1":"abcdefg",
 "attribute_2": {
 "attribute_a":"example_value_1",
 "attribute_b":"example_value_1"
 },
 "attribute_3":"2019-07-16T19:20:30+1:00"
}

```
 | 

 | 

 2022-07-18 11:59:23 | 
 customer_3456 | 

```

1
2
3
4
5
6

```
 | 
```
{
 "attribute_1":"abcdefg",
 "attribute_2":42,
 "attribute_3":"2019-07-16T19:20:30+1:00",
 "attribute_5":"testing"
}

```
 | 

 | 

 2022-07-19 09:07:23 | 
 customer_5678 | 

```

1
2
3
4
5

```
 | 
```
{
 "attribute_1":"abcdefg",
 "attribute_4":true,
 "attribute_5":"testing_123"
}

```
 | 

 | 

 2022-07-16 00:25:30 | 
 customer_9012 | 

```

1
2
3
4
5

```
 | 
```
{
 "attribute_1":"xyz",
 "attribute_4":false,
 "attribute_5":"testing_123"
}

```
 | 

 | 

 2022-07-21 08:30:00 | 
 customer_1234 | 

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
{
 "attribute_1":"abcdefg",
 "attribute_2": {
 "attribute_a":"example_value_2",
 "attribute_b":"example_value_2"
 },
 "attribute_3":"2019-07-20T19:20:30+1:00"
}

```
 | 

 | 

In this third run, another new row was added for customer_1234 with an UPDATED_AT value (2022-07-21 08:30:00) later than the stored timestamp. This new row and the existing row for customer_5678 (which has an UPDATED_AT equal to the stored timestamp) are both synced. The stored UPDATED_AT is now set as 2022-07-21 08:30:00.

note

UPDATED_AT values are allowed to be even later than the run start time for a given sync. However, this is not recommended as it pushes the last UPDATED_AT timestamp “into the future” and subsequent syncs will not sync earlier values.

## Use a UTC timestamp for the UPDATED_AT column

The UPDATED_AT column should be in UTC to prevent issues with daylight savings time. Prefer UTC-only functions, such as SYSDATE() instead of CURRENT_DATE() whenever possible.

## Avoid resyncing rows with duplicate timestamps

CDI tracks the number of rows at the last synced UPDATED_AT timestamp. If CDI detects that new rows have been added with that same timestamp since the last run, it uses an inclusive boundary (>=) to re-select all rows at that timestamp, including ones already processed. Otherwise, CDI uses an exclusive boundary (>) and only selects rows strictly later than the last synced value.

For example, if a sync processes five rows at UPDATED_AT = 2025-04-01 00:00:00, and a sixth row is later added with the same timestamp, the next sync detects the count change and re-syncs all six rows. This can result in duplicate data and unnecessary data point consumption.

To avoid this:

- If you’re setting up a sync against a VIEW, don’t use CURRENT_TIMESTAMP as the default value. This causes all data to sync every time the sync runs because the UPDATED_AT field evaluates to the time the query runs.
 
- If you have long-running pipelines or queries writing data to your source table, avoid running these concurrently with a sync, or avoid using the same timestamp for every row inserted.
 
- Use a transaction to write all rows that share the same timestamp.
 
- Use unique, monotonically increasing UPDATED_AT values to prevent rows from being re-selected after they’ve been processed.

### Example: Managing subsequent updates

This example shows the general process for syncing data for the first time, then only updating changing data (deltas) in the subsequent updates. Let’s say we have a table EXAMPLE_DATA with some user data. On day 1, it has the following values:

 Example: Managing subsequent updates

 external_id | 
 attribute_1 | 
 attribute_2 | 
 attribute_3 | 
 attribute_4 | 

 12345 | 
 823 | 
 blue | 
 380 | 
 FALSE | 

 23456 | 
 28 | 
 blue | 
 823 | 
 TRUE | 

 34567 | 
 234 | 
 blue | 
 384 | 
 TRUE | 

 45678 | 
 245 | 
 red | 
 349 | 
 TRUE | 

 56789 | 
 1938 | 
 red | 
 813 | 
 FALSE | 

To get this data into the format that CDI expects, you could run the following query:

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

```
 | 
```
SELECT
 CURRENT_TIMESTAMP AS UPDATED_AT,
 EXTERNAL_ID AS EXTERNAL_ID,
 TO_JSON(
 OBJECT_CONSTRUCT(
 'attribute_1', attribute_1,
 'attribute_2', attribute_2,
 'attribute_3', attribute_3,
 'attribute_4', attribute_4
 )
 ) AS PAYLOAD
FROM EXAMPLE_DATA;

```
 | 

None of this has synced to Braze before, so add all of it to the source table for CDI:

 UPDATED_AT | 
 EXTERNAL_ID | 
 PAYLOAD | 

 2023-03-16 15:00:00 | 
 12345 | 
 { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} | 

 2023-03-16 15:00:00 | 
 23456 | 
 { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"} | 

 2023-03-16 15:00:00 | 
 34567 | 
 { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"} | 

 2023-03-16 15:00:00 | 
 45678 | 
 { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"} | 

 2023-03-16 15:00:00 | 
 56789 | 
 { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} | 

A sync runs, and Braze records that you synced all available data up until “2023-03-16 15:00:00”. Then, on the morning of day 2, you have an ETL that runs and some fields in your users table are updated (marked with *):

 Example: Managing subsequent updates. * indicates a field updated since the last sync.

 external_id | 
 attribute_1 | 
 attribute_2 | 
 attribute_3 | 
 attribute_4 | 

 12345 | 
 145* | 
 red* | 
 380 | 
 TRUE* | 

 23456 | 
 15* | 
 blue | 
 823 | 
 TRUE | 

 34567 | 
 234 | 
 blue | 
 495* | 
 FALSE* | 

 45678 | 
 245 | 
 green* | 
 349 | 
 TRUE | 

 56789 | 
 1938 | 
 red | 
 693* | 
 FALSE | 

Now you need to add only the changed values into the CDI source table. These rows can be appended rather than updating the old rows. That table now looks like this:

 UPDATED_AT | 
 EXTERNAL_ID | 
 PAYLOAD | 

 2023-03-16 15:00:00 | 
 12345 | 
 { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} | 

 2023-03-16 15:00:00 | 
 23456 | 
 { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"} | 

 2023-03-16 15:00:00 | 
 34567 | 
 { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"} | 

 2023-03-16 15:00:00 | 
 45678 | 
 { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"} | 

 2023-03-16 15:00:00 | 
 56789 | 
 { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} | 

 2023-03-17 09:30:00 | 
 12345 | 
 { "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"} | 

 2023-03-17 09:30:00 | 
 23456 | 
 { "ATTRIBUTE_1": "15"} | 

 2023-03-17 09:30:00 | 
 34567 | 
 { "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"} | 

 2023-03-17 09:30:00 | 
 45678 | 
 { "ATTRIBUTE_2":"green"} | 

 2023-03-17 09:30:00 | 
 56789 | 
 { "ATTRIBUTE_3":"693"} | 

CDI will only sync the new rows, so the next sync that runs will only sync the last five rows.

## Additional tips

### Only write new or updated attributes to minimize consumption

Each time a sync runs, Braze looks for rows that have not previously been synced. We check this using the UPDATED_AT column in your table or view. Braze selects and imports any rows where UPDATED_AT is later than the last synced UPDATED_AT value, regardless of whether they are the same as what’s currently on the user profile. Rows at the boundary timestamp may also be re-synced if new rows share that timestamp. Given that, we recommend only syncing attributes you want to add or update.

Data point usage is identical using CDI as for other ingestion methods like REST APIs or SDKs, so it is up to you to make sure that you’re only adding new or updated attributes into your source tables.

### Separate EXTERNAL_ID from PAYLOAD column

The PAYLOAD object should not include an external ID or other ID type.

### Remove an attribute

You can set it to null if you want to omit an attribute from a user’s profile. If you want an attribute to remain unchanged, don’t send it to Braze until it’s been updated. To completely remove an attribute, use TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...)).

### Make incremental updates

Make incremental updates to your data so you can prevent unintentional overwrites when simultaneous updates are made.

important

- Updates to different attributes: In the vast majority of cases, if two updates don’t impact the same attributes on a user, they have entirely independent results. For example, if you update a user’s Color attribute and separately update their Size attribute, both updates should be applied correctly, even if they occur within seconds of each other.
 
- Updates to the same attribute: Race conditions can occur when multiple updates target the same attribute within a single sync run. In these rare cases, one update may overwrite another. The best way to prevent this behavior is to ensure that the source data for your CDI sync reflects only the latest state of each user, or that all updates for a given user or user+attribute pairing are contained in a single row.
 
- Object array operators: The only exceptions to independent updates are with the $add, $remove, and $update operators for object arrays, where updates to the same array may interact with each other.
 
- Events: Race conditions don’t affect events because each event is unique and has a timestamp associated with it.

The best way to prevent this behavior is to ensure that the source data for your CDI sync reflects only the latest state of each user, or that all updates for a given user or user+attribute pairing are contained in a single row.

### Create a JSON string from another table

If you prefer to store each attribute in its own column internally, you need to convert those columns to a JSON string to populate the sync with Braze. To do that, you can use a query like:

- snowflake
 
- redshift
 
- bigquery
 
- databricks
 
- microsoft fabric

Use this query in Snowflake to format source columns into CDI fields.

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

```
 | 
```
CREATE TABLE "EXAMPLE_USER_DATA"
 (attribute_1 string,
 attribute_2 string,
 attribute_3 number,
 my_user_id string);

SELECT
 CURRENT_TIMESTAMP as UPDATED_AT,
 my_user_id as EXTERNAL_ID,
 TO_JSON(
 OBJECT_CONSTRUCT (
 'attribute_1',
 attribute_1,
 'attribute_2',
 attribute_2,
 'yet_another_attribute',
 attribute_3)
 )as PAYLOAD FROM "EXAMPLE_USER_DATA";

```
 | 

Use this query in Redshift to format source columns into CDI fields.

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

```
 | 
```
CREATE TABLE "EXAMPLE_USER_DATA"
 (attribute_1 string,
 attribute_2 string,
 attribute_3 number,
 my_user_id string);

SELECT
 CURRENT_TIMESTAMP as UPDATED_AT,
 my_user_id as EXTERNAL_ID,
 JSON_SERIALIZE(
 OBJECT (
 'attribute_1',
 attribute_1,
 'attribute_2',
 attribute_2,
 'yet_another_attribute',
 attribute_3)
 ) as PAYLOAD FROM "EXAMPLE_USER_DATA";

```
 | 

Use this query in BigQuery to format source columns into CDI fields.

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

```
 | 
```
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
 attribute_2 STRING,
 attribute_3 NUMERIC,
 my_user_id STRING);

SELECT
 CURRENT_TIMESTAMP as UPDATED_AT,
 my_user_id as EXTERNAL_ID,
 TO_JSON(
 STRUCT(
 'attribute_1' AS attribute_1,
 'attribute_2'AS attribute_2,
 'yet_another_attribute'AS attribute_3
 )
 ) as PAYLOAD 
 FROM BRAZE.EXAMPLE_USER_DATA;

```
 | 

Use this query in Databricks to format source columns into CDI fields.

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

```
 | 
```
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
 attribute_1 string,
 attribute_2 STRING,
 attribute_3 NUMERIC,
 my_user_id STRING
);

SELECT
 CURRENT_TIMESTAMP as UPDATED_AT,
 my_user_id as EXTERNAL_ID,
 TO_JSON(
 STRUCT(
 attribute_1,
 attribute_2,
 attribute_3
 )
 ) as PAYLOAD 
 FROM BRAZE.EXAMPLE_USER_DATA;

```
 | 

Use this query in Microsoft Fabric to format source columns into CDI fields.

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

```
 | 
```
CREATE TABLE [braze].[users] (
 attribute_1 VARCHAR,
 attribute_2 VARCHAR,
 attribute_3 VARCHAR,
 attribute_4 VARCHAR,
 user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
 user_id as EXTERNAL_ID,
 CURRENT_TIMESTAMP as UPDATED_AT,
 JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;

```
 | 

### Use the UPDATED_AT timestamp

Braze uses the UPDATED_AT timestamp to track what data has been synced successfully. CDI also tracks the number of rows at the last synced timestamp. If new rows are added with that same timestamp between runs, CDI re-syncs all rows at that timestamp, which can lead to duplicate data. For more details and tips, see Avoid resyncing rows with duplicate timestamps.

### Table configuration

We have a public GitHub repository for customers to share best practices or code snippets. To contribute your own snippets, create a pull request!

### Data formatting

Cloud Data Ingestion table setup requirements and payload formatting requirements are documented on Table setup for Cloud Data Ingestion.

Use that page to distinguish:

- Source table requirements (required columns, identifier columns, and UPDATED_AT behavior)
 
- Payload requirements (which fields must match the /users/track object format for each data type)

### Avoid timeouts for data warehouse queries

We recommend that queries be completed within one hour for optimal performance and to avoid potential errors. If queries exceed this timeframe, consider reviewing your data warehouse configuration. Optimizing resources allocated to your warehouse can help improve query execution speed.

## Product limitations

 Limitation | 
 Description | 

 Number of integrations | 
 There is no limit on how many integrations you can set up. However, you will only be able to set up one integration per table or view. | 

 Number of rows | 
 By default, each run can sync up to 500 million rows. Braze stops any syncs with more than 500 million new rows. If you need a higher limit than this, contact your Braze customer success manager or Braze Support. | 

 Attributes per row | 
 Each row should contain a single user ID and a JSON object with up to 250 attributes. Each key in the JSON object counts as one attribute (that is, an array counts as one attribute). | 

 Payload size | 
 Each row can contain a payload of up to 1 MB. Braze rejects payloads greater than 1 MB and logs the error “Payload was greater than 1MB” to the sync log along with the associated external ID and truncated payload. | 

 Data type | 
 You can sync user attributes, events, and purchases through Cloud Data Ingestion. | 

 Braze region | 
 This product is available in all Braze regions. Any Braze region can connect to any source data region. | 

 Source region | 
 Braze will connect to your data warehouse or cloud environment in any region or cloud provider. | 

- 

New Stuff!
