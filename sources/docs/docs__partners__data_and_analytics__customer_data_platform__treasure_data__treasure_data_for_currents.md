---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents
slug: docs__partners__data_and_analytics__customer_data_platform__treasure_data__treasure_data_for_currents
title: "Treasure Data for Currents"
description: "This reference article outlines the partnership between Braze Currents and Treasure Data, an enterprise customer data platform that streams Braze event data into Treasure Data..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Treasure Data for Currents

Treasure Data is a customer data platform (CDP) that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and Treasure Data integration lets you control the flow of information between the two systems. With Currents, you can stream Braze event data into Treasure Data and make it actionable across your growth stack.

The recommended method is the Braze Currents Streaming connector in Treasure Data, paired with a Custom Currents Export in Braze. This approach provides:

- Real-time event streaming from Braze into Treasure Data
 
- Optional automatic table routing by event type
 
- A flat, SQL-queryable schema that doesn’t require JSON parsing

note

The Braze Currents Streaming connector is available by request. Contact Treasure Data support to enable it on your Treasure Data account. For partner-side setup details, see Treasure Data’s Braze Currents Import Integration.

## Prerequisites

 Requirement | 
 Description | 

 Treasure Data account | 
 An active Treasure Data account is required to take advantage of this partnership. | 

 Currents | 
 To export data to Treasure Data, you need Braze Currents set up for your account. | 

 Braze Currents Streaming connector | 
 Contact Treasure Data support to enable the Braze Currents Streaming connector on your Treasure Data account. | 

 Treasure Data Write API key | 
 A Treasure Data Write API key authenticates the inbound stream from Braze. | 

## Integration

### Step 1: Configure the connector in Treasure Data

- In the Treasure Data console, go to Connections > New Connection.
 
- Select Braze Currents Streaming.
 
- Under Authentication, enter your Treasure Data Write API key.
 
- Under Source Settings, configure the following:

 Field | 
 Description | 

 Source Name | 
 A descriptive name for this connection | 

 Datastore | 
 Select Plazma | 

 Database | 
 The Treasure Data database where events are stored | 

 Table | 
 The default destination table | 

 Multiple Tables | 
 Select to route each Braze event type to its own table | 

- After you’ve saved, copy the Unique ID (task_id). You need this value in the next step.

### Step 2: Create a Custom Currents Export in Braze

The Treasure Data Export option in the Braze Currents UI uses the legacy Postback API method and is no longer recommended. Use Custom Currents Export instead.

- In Braze, go to Partner Integrations > Data Export.
 
- Select Create New Current > Custom Currents Export.
 
- Enter an integration name and a contact email for error notifications.
 
- Under Credentials, enter the endpoint URL for your Treasure Data region. Enter your Treasure Data Write API key as the Bearer Token.

 Region | 
 Endpoint URL | 

 US | 
 https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID} | 

 EU | 
 https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID} | 

 AP02 | 
 https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID} | 

 Tokyo | 
 https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID} | 

Replace {TASK_ID} with the Unique ID you copied in Step 1.

- Select the event types you want to export. Custom Currents connections can send events for identified users and for users without an external_user_id. Treasure Data ingests both.
 
- Select Launch Current.

warning

Keep your Treasure Data Write API key and endpoint URL up to date. If the endpoint is unreachable for more than 5 days, Braze drops the connector’s events and the data is permanently lost.

## Query your data

After events are flowing, query them with SQL. Treasure Data flattens the payload, so you don’t need to parse JSON.

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
 id AS event_id,
 event_type,
 user_external_user_id,
 properties_campaign_name,
 properties_email_address,
 time
FROM your_database.your_table
WHERE TD_INTERVAL(time, '-1d', 'JST')

```
 | 

note

The time field in Treasure Data is the timestamp when Treasure Data received and processed the event, not the original event occurrence time in Braze.

If you selected Multiple Tables, each event type lands in its own table (for example, users_message_email_open or users_behaviors_purchase).

To confirm data is arriving, run a count query a few minutes after you launch the Current:

```

1
2
3

```
 | 
```
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')

```
 | 

## Data schema

Treasure Data flattens nested JSON up to two levels deep:

 JSON type | 
 Treasure Data column type | 

 string | 
 string | 

 number | 
 long | 

 boolean | 
 string | 

 array | 
 JSON string | 

 object (level 1) | 
 field_name | 

 object (level 2) | 
 parent_field_name_field_name | 

 null | 
 omitted | 

Column names use lowercase letters and underscores only.

## Limits

 Item | 
 Limit | 

 Maximum payload size | 
 1 MB per request | 

 Batch size | 
 100 events per batch (default) | 

## Integration details

Braze supports exporting all data listed in the Currents event glossaries to Treasure Data. That includes all properties in both message engagement and customer behavior events.

The payload structure for exported data matches the payload structure for custom HTTP connectors. You can review sample payloads in the examples repository for custom HTTP connectors.

## Migrate from the legacy Postback method

If you previously used Treasure Data Export (Postback) in Braze:

- Complete the Custom Currents Export setup in this article.
 
- Confirm events are flowing to the new table.
 
- Disable the old Postback-based Current in Braze.

Legacy data stored as raw JSON arrays can still be queried with JSON_PARSE and UNNEST. New data ingested through the streaming connector uses the flat schema described in Data schema.

- 

New Stuff!
