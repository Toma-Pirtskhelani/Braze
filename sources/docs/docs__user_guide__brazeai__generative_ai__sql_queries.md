---
url: https://www.braze.com/docs/user_guide/brazeai/generative_ai/sql_queries
slug: docs__user_guide__brazeai__generative_ai__sql_queries
title: "Query Builder"
description: "This reference article describes how to build reports using Braze data from Snowflake in the Query Builder."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Query Builder

Learn how to use the Query Builder, so you can generate reports using Braze data in Snowflake. The Query Builder comes with pre-built SQL query templates to get you started, or you can write your own custom SQL queries to unlock even more insights.

## Prerequisites

You’ll need “View PII” permissions to use Query Builder, since it allows direct access to some customer data.

## Using the Query Builder

### Step 1: Create an SQL query

To create a new query, go to Analytics > Query Builder, then select Create SQL Query.

If you need inspiration or help in crafting your query, choose Query Template and select a pre-made template. To start with a blank query, select SQL Editor.

Your report is automatically given a name with the current date and time. Hover over the name and select to give your SQL query a meaningful name.

### Step 2: Build your query

When building your query, you can choose to get help from AI or build it on your own.

- using brazeai
 
- on my own

The AI Query Builder leverages GPT, powered by OpenAI, to recommend SQL for your query. To generate SQL with the AI Query Builder:

- After creating a report in the Query Builder, select the AI Query Builder tab.
 
- Type in your prompt or select a sample prompt and select Generate to translate your prompt into SQL.
 
- Review the generated SQL to make sure it looks correct, and then select Insert into Editor.

#### Tips

- Familiarize yourself with the available Snowflake data tables. Asking for data that doesn’t exist in these tables may result in ChatGPT making up a fake table.
 
- Familiarize yourself with the SQL writing rules for this feature. Not following these rules will cause an error.
 
- You can send up to 20 prompts per minute with the AI Query Builder.

#### How is my data used and sent to OpenAI?

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per OpenAI’s API platform commitments, data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

Write your SQL query using Snowflake syntax. Consult the table reference for a full list of tables and columns available to be queried.

To view table details within the Query Builder:

- From the Query Builder page, open the Reference panel and select Available Data Tables to view available data tables and their names.
 
- Select See Details to view the table description and information about the table columns, such as data types.
 
- To insert the table name in your SQL, select .

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

#### Troubleshooting

Your query may fail for any of the following reasons:

- Syntax errors in your SQL query
 
- Processing timeout (after 6 minutes)

- Reports that take longer than 6 minutes to run will time out.
 
- If a report times out, try to limit the time range in which you are querying data or query a more specific set of data.

### Step 3: Generate your report

When you’re finished building your query, select Run Query. If there’s no errors or report timeouts, a CSV file will be generated from the query.

To download the CSV report, select Export.

important

Each report can only generate results once per day. If you run the same report multiple times in a single calendar day, you’ll see the same results in each report.

## Report timeouts

Reports that take longer than six minutes to run will time out. If this is the first query you’re running in some time, it may take longer to process and therefore has a higher likelihood of timing out. If this happens, try running the report again.

If your report continues to time out after multiple attempts, contact Support.

## Querying abort reasons

You can query the ABORT_TYPE column on any USERS_MESSAGES_*_ABORT_SHARED table to analyze why messages were not sent. The ABORT_TYPE field contains a string value describing the specific reason for the abort, and the companion ABORT_LOG field contains additional details (such as the frequency capping rule that was triggered).

For example, to count email aborts by type in the last 30 days:

```

1
2
3
4
5

```
 | 
```
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC

```
 | 

For the full list of ABORT_TYPE values and their descriptions, see Abort types.

## Data and results

All queries surface data from the last 60 days. When you export your results, it will only contain up to 1,000 rows. For reports that require larger amounts of data, you can use tools such as Currents or the export API endpoint.

## Snowflake credits

Each company has 5 Snowflake credits available per month, shared across all workspaces. A small portion of a Snowflake credit is used whenever you run a query or preview a table.

note

Snowflake credits are not shared between features. For example, credits across SQL Segment Extensions and Query Builder are independent of each other.

Credit usage is correlated to the run time of your SQL query. The longer the run time is, the higher the portion of a Snowflake credit a query will cost. Run time can vary depending on the complexity and size of your queries over time. The more complex and frequent queries you run, the larger your resource allocation and the faster your run time becomes.

Credits are not used when writing, editing, or saving reports within the Braze SQL editor. Your credits will reset to 5 on the first of each month at 12 am UTC. You can monitor your monthly credit usage at the top of the Query Builder page.

When you reach the credit cap, you cannot run queries, but you can create, edit, and save SQL reports. If you want to purchase more Query Builder credits, please get in touch with your account manager.

- 

New Stuff!
