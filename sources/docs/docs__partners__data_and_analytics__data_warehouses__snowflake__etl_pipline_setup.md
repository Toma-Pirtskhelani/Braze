---
url: https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup
slug: docs__partners__data_and_analytics__data_warehouses__snowflake__etl_pipline_setup
title: "ETL event pipeline setup"
description: "This partner page offers an example set up for an Email Clicks query to reference when setting up your own queries."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# ETL event pipeline setup

This partner page offers an example set up for an email clicks query to reference when setting up your own queries.

You can use this email clicks query to analyze the interactions with specific emails in your Braze campaigns and Canvases.

## Set up this query

Create a database for BRAZE, then create a database if none exists for BRAZE_CURRENTS;:

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
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;

```
 | 

Use the following command to create your table:

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

```
 | 
```
CREATE TABLE
 braze_currents.public.users_messages_email_click (
 id STRING,
 user_id STRING,
 external_user_id STRING,
 time INT,
 timezone STRING,
 campaign_id STRING,
 campaign_name STRING,
 message_variation_id STRING,
 canvas_id STRING,
 canvas_name STRING,
 canvas_variation_id STRING,
 canvas_step_id STRING,
 send_id STRING,
 dispatch_id STRING,
 email_address STRING,
 url STRING,
 sending_ip STRING,
 user_agent STRING
 );

```
 | 

Use the following command to create or replace your pipe:

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

```
 | 
```
CREATE OR REPLACE PIPE
 pipe_users_messages_email_click
 auto_ingest=true AS

COPY INTO
 braze_currents.public.users_messages_email_click
 FROM
 (select
 $1:id::STRING,
 $1:user_id::STRING,
 $1:external_user_id::STRING,
 $1:time::INT,
 $1:timezone::STRING,
 $1:campaign_id::STRING,
 $1:campaign_name::STRING,
 $1:message_variation_id::STRING,
 $1:canvas_id::STRING,
 $1:canvas_name::STRING,
 $1:canvas_variation_id::STRING,
 $1:canvas_step_id::STRING,
 $1:send_id::STRING,
 $1:dispatch_id::STRING,
 $1:email_address::STRING,
 $1:url::STRING,
 $1:sending_ip::STRING,
 $1:user_agent::STRING

 FROM
 @braze_currents.public.braze_data/currents/dataexport.prod-03.S3.integration.YOUR_INTEGRATION_ID_HERE/event_type=users.messages.email.click/);

show pipes;

```
 | 

## Do more with this query example

Copy the notification_channel from the output of the preceding command and use that when configuring S3 bucket notifications.

Manually sync from S3 to Snowflake for the following pipe name given:

```

1
2
3

```
 | 
```
ALTER PIPE
 pipe_users_messages_email_click
 refresh ;

```
 | 

Check the pipe status, which will show when the message was forwarded from S3 into Snowflake:

```

1
2
3
4

```
 | 
```
SELECT
 SYSTEM$PIPE_STATUS(
 'pipe_users_messages_email_click'
 )

```
 | 

Finally, show the copy history for the table by selecting * from:

```

1

```
 | 
```
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));

```
 | 

- 

New Stuff!
