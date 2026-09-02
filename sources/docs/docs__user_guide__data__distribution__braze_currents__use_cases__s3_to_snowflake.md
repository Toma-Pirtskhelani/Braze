---
url: https://www.braze.com/docs/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake
slug: docs__user_guide__data__distribution__braze_currents__use_cases__s3_to_snowflake
title: "Transfer data from Amazon S3 to Snowflake"
description: "This how-to article will walk you through transferring data from cloud storage (like Amazon S3) to a warehouse (like Snowflake) using the Extract, Transform, Load..."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Transfer data from Amazon S3 to Snowflake

If your data currently sits in Amazon S3, you can transfer it to Snowflake or another relational data warehouse using the Extract, Load, Transform (ELT) process. This page covers how to do so.

note

If you have more specific use cases and would like Braze to service your Currents instance, contact your Braze account manager and ask them about Braze Data Professional Services.

## How it works

The Extract, Load, Transform (ELT) process is an automated process that moves data into Snowflake, which will allow you to use the Braze Looker Blocks to visualize that data in Looker to help drive insights and feedback into your campaigns, Canvases, and segments.

After you have a Currents to S3 export set up and are receiving live events data, you can configure your live ELT pipeline in Snowflake by configuring the following components:

- AWS SQS queues
 
- Auto-Ingest Snowpipes

## Configuring AWS SQS queues

Auto-ingest Snowpipes rely on SQS queues for sending notification from S3 to Snowpipe. This process is managed by Snowflake after configuring SQS.

### Step 1: Configure the external S3 stage

note

Tables in your database are created in this stage.

- 
 
When you set up Currents in Braze, specify a folder path for your Currents files to follow into your S3 bucket. Here we use currents, the default folder path.

- 
 
Create the following in the listed order:
 2.1 In AWS, create a new public-private key pair for the desired S3 bucket, with grants according to your organization’s security requirements.
 2.2. In Snowflake, create a database and schema of your choice (named currents and public in the following example).
 2.3. Create a Snowflake S3 Stage (called braze_data):

```

1
2
3
4
5

```
 | 
```
CREATE OR REPLACE STAGE
 currents.public.braze_data
 url='s3://snowpipe-demo/'
 credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;

```
 | 

- Define the AVRO file format for your stage.

```

1
2
3
4

```
 | 
```
CREATE FILE FORMAT
 currents.public.currents_avro
 type = 'avro'
 compression = 'auto';

```
 | 

```

1
2
3
4

```
 | 
```
ALTER STAGE
 currents.public.braze_data
SET
 file_format = currents.public.currents_avro;

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
30
31
32

```
 | 
```
CREATE OR REPLACE PIPE
 pipe_users_messages_pushnotification_open
 auto_ingest=true AS

COPY INTO
 users_messages_pushnotification_open
 FROM
 (SELECT
 $1:id::STRING,
 $1:user_id::STRING,
 $1:external_user_id::STRING,
 $1:time::INT,
 $1:timezone::STRING,
 $1:app_id::STRING,
 $1:campaign_id::STRING,
 $1:campaign_name::STRING,
 $1:message_variation_id::STRING,
 $1:canvas_id::STRING,
 $1:canvas_name::STRING,
 $1:canvas_variation_id::STRING,
 $1:canvas_step_id::STRING,
 $1:canvas_step_message_variation_id::STRING,
 $1:platform::STRING,
 $1:os_version::STRING,
 $1:device_model::STRING,
 $1:send_id::STRING,
 $1:device_id::STRING,
 $1:button_action_type::STRING,
 $1:button_string::STRING

 FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);

```
 | 

- Finally, use the show pipes; command to show your SQS information. The name of the SQS queue will be visible in a new column called NOTIFICATION_CHANNEL because this pipe was created as an auto-ingest pipe.

### Step 2: Create bucket events

- In AWS, navigate to the corresponding bucket of the new Snowflake stage. Then, under the Properties tab, go to Events.

- Create new events for each set of Currents Data, as needed (Messaging, User Behavior), or both.

- Check the appropriate box for the object create notifications, as well as the ARN on the bottom of the form (from the notification channel column in Snowflake).

## Configuring auto-ingest Snowpipes

For the AWS SQS configuration to produce the correct tables, you must define the structure of the incoming data properly by using the following examples and schemas determined in our Currents documentation for Message Engagement or Messaging Events, User or Customer Behavior Events, or both.

It is critical to structure your tables in accordance with the Braze Currents schemas, as Braze Currents will continuously load data into them through specific fields with specific data types. For example, a user_id will be loaded as a string and called a user_id in Currents data.

note

Depending on your Currents integration, you may have different events you must set up (such as Message Engagement or Messaging Events and User or Customer Behavior Events). You can also write a script for some or all of this process.

- user behavior events
 
- messaging events

- Create a table INTO which we will continuously load using the following structure from the Currents schema:

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
CREATE TABLE
 users_behaviors_app_firstsession (
 id STRING,
 user_id STRING,
 external_user_id STRING,
 app_id STRING,
 time INT,
 session_id STRING,
 gender STRING,
 country STRING,
 timezone STRING,
 language STRING,
 device_id STRING,
 sdk_version STRING,
 platform STRING,
 os_version STRING,
 device_model STRING
 );

```
 | 

- Create the auto_ingest pipe and specify:
 2.1. Which table to load
 2.2 How to load the following table

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

```
 | 
```
CREATE OR REPLACE PIPE
 pipe_users_behaviors_app_firstsession
 auto_ingest=true AS

COPY INTO
 users_behaviors_app_firstsession
 FROM
 (SELECT
 $1:id::STRING,
 $1:user_id::STRING,
 $1:external_user_id::STRING,
 $1:app_id::STRING,
 $1:time::INT,
 $1:session_id::STRING,
 $1:gender::STRING,
 $1:country::STRING,
 $1:timezone::STRING,
 $1:language::STRING,
 $1:device_id::STRING,
 $1:sdk_version::STRING,
 $1:platform::STRING,
 $1:os_version::STRING,
 $1:device_model::STRING

 FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);

```
 | 

warning

You must repeat the CREATE TABLE and CREATE PIPE commands for every event type.

- Create a table INTO which we will continuously load using the following structure from the Currents schema:

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

```
 | 
```
CREATE TABLE
 public_users_messages_pushnotification_open (
 id STRING,
 user_id STRING,
 external_user_id STRING,
 time INT,
 timezone STRING,
 app_id STRING,
 campaign_id STRING,
 campaign_name STRING,
 message_variation_id STRING,
 canvas_id STRING,
 canvas_name STRING,
 canvas_variation_id STRING,
 canvas_step_id STRING,
 canvas_step_message_variation_id STRING,
 platform STRING,
 os_version STRING,
 device_model STRING,
 send_id STRING,
 device_id STRING,
 button_action_type STRING,
 button_string STRING
 );

```
 | 

- Create the AUTO continuous load pipe and specify:
 2.1. Which table to load
 2.2 How to load the following table

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
30
31
32

```
 | 
```
CREATE OR REPLACE PIPE
 pipe_users_messages_pushnotification_open
 auto_ingest=true AS

COPY INTO
 users_messages_pushnotification_open
 FROM
 (SELECT
 $1:id::STRING,
 $1:user_id::STRING,
 $1:external_user_id::STRING,
 $1:time::INT,
 $1:timezone::STRING,
 $1:app_id::STRING,
 $1:campaign_id::STRING,
 $1:campaign_name::STRING,
 $1:message_variation_id::STRING,
 $1:canvas_id::STRING,
 $1:canvas_name::STRING,
 $1:canvas_variation_id::STRING,
 $1:canvas_step_id::STRING,
 $1:canvas_step_message_variation_id::STRING,
 $1:platform::STRING,
 $1:os_version::STRING,
 $1:device_model::STRING,
 $1:send_id::STRING,
 $1:device_id::STRING,
 $1:button_action_type::STRING,
 $1:button_string::STRING

 FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);

```
 | 

warning

You must repeat the CREATE TABLE and CREATE PIPE commands for every event type.

To see the types of analytics you can perform using Braze Currents, consult our Looker Blocks.

note

Contact your Braze account manager if you have any questions or if you’re interested in having Braze guide you through this process.

- 

New Stuff!
