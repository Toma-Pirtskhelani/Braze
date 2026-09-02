---
url: https://www.braze.com/docs/user_guide/analytics/reports/query_builder
slug: docs__user_guide__analytics__reports__query_builder
title: "Query Builder"
description: "This reference article describes how to build reports using Braze data from Snowflake in the Query Builder."
section: user_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Query Builder

The Query Builder generates reports using Braze data in Snowflake. The Query Builder comes with pre-built SQL query templates to get you started, or you can write your own custom SQL queries to unlock even more insights.

Because the Query Builder allows direct access to some customer data, you can only access the Query Builder if you have the “View PII” permission.

## Available data tables

Query Builder uses the same Snowflake SQL tables as SQL Segment Extensions and Snowflake Data Sharing. For a complete list of available tables and their columns, refer to the SQL table reference.

### User profile attribute views

Query Builder and SQL Segment Extensions include most user profile attribute views, such as periodic snapshots and default-attribute history.

Two views of custom attribute are available only through Snowflake Data Sharing:

- USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED
 
- USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED

Braze excludes these views from Query Builder and SQL Segment Extensions because they are slow to query at workspace scale and often time out. Use USER_CUSTOM_ATTRIBUTES_VIEW_SHARED for custom attribute snapshots in Query Builder. If you need historical or near-real-time custom attribute data, query the excluded views through Snowflake Data Sharing instead.

## Running reports in the Query Builder

To run a Query Builder report:

- Go to Analytics > Query Builder.
 
- Select Create SQL Query. If you need inspiration or help in crafting your query, select Query Template and choose a template from the list. Otherwise, select SQL Editor to head straight to the editor.
 
- Your report is automatically given a name with the current date and time. Hover over the name and select to give your SQL query a meaningful name.
 
- Write your SQL query in the editor or get help from AI from the AI Query Builder tab. If writing your own SQL, see Writing custom SQL queries for requirements and resources.
 
- Select Run Query.
 
- Save your query.
 
- To download a CSV of your report, select Export.

Results from each report can be generated once a day. If you run the same report more than once in one calendar day, you’ll see the same results in both reports.

### Query templates

Access query templates by selecting Create SQL Query > Query Template when first creating a report.

See Query templates for a list of available templates.

### Data timeframe

Queries return data from the past 60 days. If you use Currents or Snowflake Data Sharing, you may be able to query up to two years of data, which is how long your data is retained in Snowflake. For more details about extended data retention, contact your customer success manager.

### Query Builder time zone

The default time zone for querying our Snowflake database is UTC. As a result, there may be some data discrepancies between your Email Channel Engagement page (which follows your company’s time zone) and your Query Builder results.

To convert the time zone in your query results, add the following SQL to your query and customize it for your company’s time zone:

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
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;

```
 | 

### Query history

The Query history section in Query Builder displays your previously run queries to help you track and reuse your work. Query history is retained for seven days, meaning that queries older than seven days are automatically removed.

If you need to audit query usage for longer periods or maintain records beyond seven days, we recommend exporting or saving important query results before they expire.

### Comparing Query Builder with other reporting sources

Query Builder results may differ from other reporting tools because they use different data sources and processing methods.

For example, soft bounce counts in Query Builder may be higher than in SendGrid Deliverability reports. Query Builder counts all occurrences of soft bounces without deduplication. If a user soft bounces multiple times before eventual delivery (or after extended retries), each soft bounce attempt is counted. SendGrid Deliverability uses its own data and logic, which Braze doesn’t have visibility into, so counts between the two reports may not match.

For more information about how soft bounces are tracked across different reporting sources, refer to Soft bounce in the Email analytics glossary.

## Generating SQL with the AI Query Builder

The AI Query Builder leverages GPT, powered by OpenAI, to recommend SQL for your query.

To generate SQL with the AI Query Builder:

- After creating a report in the Query Builder, select the AI Query Builder tab.
 
- Type in your prompt or select a sample prompt and select Generate to translate your prompt into SQL.
 
- Review the generated SQL to make sure it looks correct, and then select Insert into Editor.

### Tips

- Familiarize yourself with the available tables and columns in the SQL table reference. Asking for data that doesn’t exist in these tables may result in ChatGPT making up a fake table.
 
- Familiarize yourself with the SQL writing rules for this feature. Not following these rules will cause an error.
 
- You can send up to 20 prompts per minute with the AI Query Builder.

### How is my data used and sent to OpenAI?

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per OpenAI’s API platform commitments, data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

## Writing custom SQL queries

Write your SQL query using Snowflake syntax. Consult the table reference for a full list of tables and columns available to be queried.

To view table details within the Query Builder:

- From the Query Builder page, open the Reference panel and select Available Data Tables to view available data tables and their names.
 
- Select See Details to view the table description and information about the table columns, such as data types.
 
- To insert the table name in your SQL, select Copy table name to SQL editor.

To use pre-written queries provided by Braze, select Query Template when first creating a report in the Query Builder.

Restricting your query to a specific time period will help you generate results quicker. The following is an example query that gets the number of purchases and the revenue generated for the last hour.

```

1
2
3

```
 | 
```
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));

```
 | 

This query retrieves the number of email sends in the last month:

```

1
2
3

```
 | 
```
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));

```
 | 

If you query for the CANVAS_ID, CANVAS_VARIATION_API_ID, or CAMPAIGN_ID, their associated name columns will automatically be included in the results table. You don’t need to include them in the SELECT query itself.

 ID name | 
 Associated name column | 

 CANVAS_ID | 
 Canvas Name | 

 CANVAS_VARIATION_API_ID | 
 Canvas Variant Name | 

 CAMPAIGN_ID | 
 Campaign Name | 

This query retrieves all three IDs and their associated name columns with a maximum of 100 rows:

```

1
2
3

```
 | 
```
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100

```
 | 

### Automatically populate the campaign variant name

If you want the campaign variant name to automatically populate, include the column name MESSAGE_VARIATION_API_ID in your query, such as in this example:

```

1
2
3

```
 | 
```
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100

```
 | 

### Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
 
- Processing timeout (after 6 minutes)

- Reports that take longer than 6 minutes to run will time out.
 
- If a report times out, try to limit the time range in which you are querying data or query a more specific set of data.

## Using variables

Use variables to use predefined variable types in SQL to reference values without needing to manually copy the value. For example, instead of manually copying a campaign’s ID to the SQL editor, you can use {{campaign.${My campaign}}} to directly select a campaign from a dropdown in the Variables tab.

After a variable is created, it will appear in the Variables tab of your Query Builder report. Benefits of using SQL variables include:

- Save time by creating a campaign variable to select from a list when creating your report, instead of pasting in campaign IDs.
 
- Swap in values by adding variables that allow you to reuse the report for slightly different use cases in the future (such as a different custom event).
 
- Reduce user error when editing your SQL by reducing the amount of editing needed for each report. Teammates that are more comfortable with SQL can create reports that less technical teammates can then use.

### Guidelines

Variables must adhere to the following Liquid syntax: {{ type.${name}}}, where type must be one of the accepted types and name can be anything you choose. The labels for these variables default to the variable name.

By default, all variables are mandatory (and your report will not run unless variable values are selected) except for the date range, which defaults to the past 30 days when the value isn’t provided.

### Variable types

The following variable types are accepted:

- Number
 
- Date range
 
- Messaging
 
- Products
 
- Custom events
 
- Custom events properties
 
- Workspace
 
- Catalogs
 
- Catalog fields
 
- Options
 
- Segments
 
- String
 
- Tags

#### Number

- Replacement value: The provided value, such as 5.5
 
- Usage example: some_number_column < {{number.${some name}}}

#### Date range

If using both start_date and end_date, they must have the same name so you can use them as a date range.

##### Example values

The date range type can be relative, start date, end date, or date range.

All four types are shown if both start_date and end_date are used with the same name. If only one is used, then only the relevant types will show.

 Date range type | 
 Description | 
 Required values | 

 Relative | 
 Specifies the past X days | 
 Requires start_date | 

 Start date | 
 Specifies a start date | 
 Requires start_date | 

 End date | 
 Specifies an end date | 
 Requires end_date | 

 Date range | 
 Specifies both a start and end date | 
 Requires both start_date and end_date | 

- Replacement value: Replaces start_date and end_date with a Unix timestamp in seconds for a specified date in UTC, such as 1696517353.
 
- Usage example: For all of relative, start date, end date, and date range variables:

- time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}

- You can use either start_date or end_date if you don’t want a date range.

#### Messaging

All messaging variables must share the same identifier when you want to tie together their state in one group.

##### Canvas

For selecting one Canvas. Sharing the same name with a campaign will result in a radio button within the Variables tab that for selecting either Canvas or campaign.

- Replacement value: Canvas BSON ID
 
- Usage example: canvas_id = ‘{{canvas.${some name}}}’

##### Canvases

For selecting multiple Canvases. Sharing the same name with a campaign will result in a radio button within the Variables tab for selecting either Canvas or campaign.

- Replacement value: Canvases BSON IDs
 
- Usage example: canvas_id IN ({{canvases.${some name}}})

##### Campaign

For selecting one campaign. Sharing the same name with a Canvas will result in a radio button within the Variables tab that for selecting either Canvas or campaign.

- Replacement value: Campaign BSON ID
 
- Usage example: campaign_id = ‘{{campaign.${some name}}}’

##### Campaigns

For multi-selecting campaigns. Sharing the same name with a Canvas will result in a radio button within the Variables tab for selecting either Canvas or campaign.

- Replacement value: Campaigns BSON IDs
 
- Usage example: campaign_id IN ({{campaigns.${some name}}})

##### Campaign variants

For selecting campaign variants that belong to the selected campaign. It must be used in conjunction with a campaign or campaigns variable.

- Replacement value: Campaign variants API IDs, strings delimited by commas such as api-id1, api-id2.
 
- Usage example: message_variation_api_id IN ({{campaign_variants.${some name}}})

##### Canvas variants

For selecting Canvas variants that belong to a chosen Canvas. It must be used with a Canvas or Canvases variable.

- Replacement value: Canvas variants API IDs, strings delimited by commas such as in api-id1, api-id2.
 
- Usage example: canvas_variation_api_id IN ({{canvas_variants.${some name}}})

##### Canvas step

For selecting a Canvas step that belongs to a chosen Canvas. It must be used with a Canvas variable.

- Replacement value: Canvas step API ID
 
- Usage example: canvas_step_api_id = ‘{{canvas_step.${some name}}}’

##### Canvas steps

For selecting Canvas steps that belong to chosen Canvases. It must be used with a Canvas or Canvases variable.

- Replacement value: Canvas steps API IDs
 
- Usage example: canvas_step_api_id IN ({{canvas_steps.${some name}}})

- 

New Stuff!
