---
url: https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments
slug: docs__user_guide__audience__segments__segment_extension__sql_segments
title: "SQL Segment Extensions"
description: "This article describes how to create a SQL Segment Extension using Snowflake queries."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# SQL Segment Extensions

You can generate a Segment Extension using Snowflake SQL queries of Snowflake data. SQL can help you unlock new segment use cases because it offers the flexibility to describe the relationships between data in ways that aren’t achievable through other segmentation features.

Like standard Segment Extensions, you can query events from up to the past two years (730 days) in your SQL Segment Extension. Unlike standard Segment Extensions, SQL Segment Extensions consume credits.

## Prerequisites

Because it’s possible to access PII data through this feature, you must have PII permissions to run SQL segment queries.

## Creating a Segment Extension

### Step 1: Choose an editor

There are two types of SQL editors to choose from when creating your SQL Segment Extension: the SQL Editor, and the Incremental SQL Editor.

- Full Refresh: Each time your segment refreshes, Braze will query all available data to update your segment, which will use more credits than incremental refreshes. Full refresh extensions can automatically regenerate membership daily, but can’t be refreshed using incremental refresh.
 
- Incremental refresh: Incremental refresh is a more cost-efficient way to set up your query, although the setup involves a few more steps. If you can complete these additional steps when constructing your segment, then it’s worth choosing this option because your query will run using fewer credits.
 
- AI SQL generator: The AI SQL Generator lets you write a prompt in plain language and turns it into a SQL query for your segment. It’s a quick way to get started without needing to write the SQL yourself.

tip

You can do a manual full refresh on all SQL Segments created in either SQL editor.

- full refresh
 
- incremental refresh
 
- ai sql generator

To create a full refresh SQL Segment Extension:

- Go to Audience > Segment Extensions.
 
- Select Create New Extension, then select Full refresh.

- Add a name for your Segment Extension and input your SQL. Refer to Step 2 for requirements and resources.

- Save your Segment Extension.

To create an incremental refresh SQL Segment Extension:

- Go to Audience > Segment Extensions.
 
- Select Create New Extension and select Incremental refresh.

- Add a name for your Segment Extension and input your SQL. Refer to the section Writing SQL for requirements and resources.

- If desired, select Regenerate Extension Daily.

When selected, Braze will update segment membership each day automatically. This means that each day at midnight in your company’s time zone (with a potential delay of an hour), Braze will check for new users in your segment and automatically add them to your segment. If a Segment Extension has not been used in 7 days, Braze will automatically pause daily regeneration. An unused Segment Extension is one that is not part of a campaign or Canvas (the campaign or Canvas doesn’t need to be active for the extension to be considered “used”).

- Save your Segment Extension.

note

The AI SQL generator is currently available as a beta feature. Contact your customer success manager if you’re interested in participating in this beta trial.

The AI SQL generator leverages GPT, powered by OpenAI, to recommend SQL for your SQL segment.

To use the AI SQL generator, do the following:

- Select Launch AI SQL Generator after creating a SQL segment using either full or incremental refresh.
 
- Type your prompt and select Generate to translate your prompt into SQL.
 
- Review the generated SQL to make sure it looks correct, and then save your segment.

#### Example prompts

- Users who received an email in the last month
 
- Users who made less than five purchases in the last year

#### Tips

- Familiarize yourself with the available Snowflake data tables. Asking for data that doesn’t exist in these tables may result in ChatGPT making up a fake table.
 
- Familiarize yourself with the SQL writing rules for this feature. Not following these rules will cause an error. For example, your SQL code must select the user_id column. Starting your prompt with “users who” can help.
 
- You can send up to 20 prompts per minute with the AI SQL Generator.

#### How is my data used and sent to OpenAI?

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per OpenAI’s API platform commitments, data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

note

SQL queries that take longer than 20 minutes to run will time out.

When the extension finishes processing, you can create a segment using your Segment Extension and target this new segment with your campaigns and Canvases.

### Step 2: Write your SQL

Your SQL query should be written using Snowflake syntax. Consult the table reference for a full list of tables and columns available to be queried.

important

Note that the tables available to query contain only event data. If you wish to query for user attributes, you should combine your SQL segment with custom attribute filters from the classic segmenter.

- sql editor
 
- incremental sql editor

Your SQL must additionally adhere to the following rules:

- Write a single SQL statement. Do not include any semicolons.
 
- Your SQL must select only one column: the user_id column. This means your SQL must contain:

```

1

```
 | 
```
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"

```
 | 

- It isn’t possible to query for users with zero events, which means any query for users that have done an event less than X times would need to follow this workaround:

- Write a query to select users who have the event MORE than X times.
 
- When referencing your Segment Extension in your segment, select doesn't include to invert the result.

#### Additional rules

Additionally, your standard SQL query must adhere to the following rules:

- You cannot use DECLARE statements.

All incremental refresh queries consist of two parts: a query, and schema details.

- In the editor, write a query that selects user_ids from your desired table.
 
- Add schema details by selecting an Operator, Number of times, and Time period from the fields at the top of the editor. The query will check if the sum of the aggregate column meets a certain condition specified by the {{operator}} and {{number of times}} placeholders. This functions similarly to the workflow for creating classic Segment Extensions.

- Operator: Indicate if the event has happened more than, less than, or equal to a number of occurrences.

- Number of times: How many times you would like to evaluate the event in relation to the operator.

- Time period: Number of days from 1 to 730 in which you want to check instances of the event. This time period refers to past days relative to the current day. The following example shows querying for users that performed the event more than 5 times in the past 365 days.

In the following example, the resulting segment would contain users that performed the favorited event more than 3 times during the last 30 days, after a specified date.

tip

Incremental refresh segments take into account late events, which are events that occurred more than 2 days ago (for example, SDK events that weren’t sent at the time they were captured).

#### Additional rules

Additionally, your incremental refresh query must adhere to the following rules:

- Write a single SQL statement. Do not include any semicolons.
 
- Your incremental SQL segment would be able to refer to just one single event. Your dropdowns for date and count are in reference to your chosen event.
 
- Your SQL must have the following columns: user_id, $start_date, and an aggregation function (such as COUNT). Any SQL saved without these three fields will result in an error.
 
- You cannot use DECLARE statements.

note

If you’re creating a SQL segment that uses the table CATALOGS_ITEMS_SHARED, you must specify a catalog ID. For example:

```

1
2
3

```
 | 
```
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10

```
 | 

### Step 3: Preview the query

Before saving, you can run a preview of your query. Query previews are automatically limited to 100 rows and will timeout after 60 seconds. The user_id column requirement does not apply when running a preview.

For incremental SQL Segment Extensions, the preview will not include the additional criteria from your operator, number of times, and time period fields.

### Step 4: Determine if you need to invert SQL

Next, determine if you need to invert SQL. While it’s not possible to directly query for users with zero events, you can use Invert SQL to target these users.

note

By default, Invert SQL is not toggled on. However, if you use the AI SQL generator to generate a SQL statement that needs to be negated, ChatGPT could return an output that automatically toggles this feature on.

For example, to target users who have fewer than three purchases, first write a query to select users who have three or more purchases. Then, select the Invert SQL to target users with fewer than three purchases (including those with zero purchases).

important

Unless you’re specifically aiming to target users with zero events, you won’t need to invert SQL. If Invert SQL is selected, confirm that the feature is needed and that the segment matches your desired audience. For example, if a query targets users with at least one event, it will only target users with zero events when inverted.

## Refreshing segment membership

To refresh the segment membership of any Segment Extension created using SQL, open the Segment Extension and select Refresh.

tip

If you created a segment where you expect users to enter and exit regularly, manually refresh the Segment Extension it uses before targeting that segment in a campaign or Canvas.

## Managing your Segment Extensions

On the Segment Extensions page, segments generated using SQL are denoted with next to their name.

Select a SQL Segment Extension to view where the extension is being used, archive the extension, or manually refresh the segment membership.

### Designating refresh settings

If you don’t need your extension to refresh on a regular schedule, you can save it without using refresh settings, and Braze will default to generating your Segment Extension based on your user membership at that moment. Use the default behavior if you only want to generate the audience once and then target it with a one-off campaign.

Your segment will always begin processing after the initial save. Whenever your segment refreshes, Braze will re-run the segment and update segment membership to reflect the users in your segment at the time of refresh. This can help your recurring campaigns reach the most relevant users.

#### Setting up a recurring refresh

To set up a recurring schedule by designating refresh settings, select Enable refresh. The option to designate refresh settings is available for all types of Segment Extensions, including SQL segments, CDI Segment Extensions, and simple form-based Segment Extensions.

important

To optimize your data management, refresh settings are automatically turned off for unused Segment Extensions. Segment Extension are considered unused when they’re:

- Not used in any active or inactive (draft, stopped, archived) campaigns, Canvases, or segments; or
 
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension if this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.

#### Selecting your refresh settings

Within the Refresh Interval Settings panel, you can select the frequency at which this segment extension will refresh: hourly, daily, weekly, or monthly. You’ll also be required to select the specific time (which is in your company’s time zone) the refresh would occur, such as:

- If you have an email campaign that is sent every Monday at 11 am company time, and you want to ensure your segment is refreshed right before it’s sent, you should choose a refresh schedule of weekly at 10 am on Mondays.
 
- If you’d like your segment to refresh every day, select the daily refresh frequency and then choose the time of day to refresh.

note

The ability to set an hourly refresh schedule isn’t available for form-based Segment Extensions (but you can set daily, weekly, or monthly schedules).

#### Credit consumption and additional costs

Because refreshes re-run your segment’s query, each refresh for SQL segments will consume SQL segment credits, and each refresh for CDI Segment Extensions will incur a cost within your third-party data warehouse.

note

Segments could require up to 60 minutes to refresh because of data processing times. Segments that are currently in the process of refreshing will have a “Processing” status within your Segment Extensions list. This has a couple of implications:

- To finish processing your segment before a specific time, choose a refresh time that is 60 minutes earlier.
 
- Only one refresh can occur at a time for a specific Segment Extension. If there is a conflict where a new refresh is initiated when an existing refresh has already begun processing, Braze will cancel the new refresh request and continue the in-progress processing.

#### Criteria to automatically disable stale extensions

Scheduled refreshes are automatically disabled once a Segment Extension is stale. A Segment Extension is stale if it meets the following criteria:

- Not used in any active campaigns or Canvases
 
- Not used in any segment that is in an active campaign or Canvas
 
- Not used in any segment that has analytics tracking turned on
 
- Hasn’t been modified in over seven days
 
- Hasn’t been added to a campaign or Canvas (including drafts), or segment in over seven days

If the scheduled refresh is disabled for a Segment Extension, that extension will have a notification that says so.

When you’re ready to use a stale Segment Extension, review the refresh settings, select the refresh schedule that matches your use case, and then save any modifications.

## Snowflake credits

Each Braze workspace has 5 Snowflake credits available per month. If you need more credits, contact your account manager. Credits are used whenever you refresh, or save and refresh, a SQL Segment’s membership. Credits are not used when you run previews within a SQL Segment or save or refresh a classic Segment Extension.

note

Snowflake credits are not shared between features. For example, credits across SQL Segment Extensions and Query Builder are independent of each other.

Credit usage is correlated to the run time of your SQL query. The longer the run time is, the more credits a query will cost. Run time can vary depending on the complexity and size of your queries over time. The more complex and frequent queries you run, the larger your resource allocation and the faster your run time becomes.

To save on credits, preview your query to ensure it is correct before saving the SQL Segment Extension.

Your credits will reset to 5 on the first of each month at 12 am UTC. You can monitor your credit usage throughout the month within the credits usage panel. From the Segment Extensions page, click View SQL Credit Usage.

The following will happen when your credits reach zero:

- Any SQL Segment Extensions set up to automatically refresh stop refreshing, impacting the membership of these segments and any campaigns or Canvases that target these segments.
 
- You can only save new SQL Segment Extensions as drafts for the remainder of the month.

All company users who created a SQL Segment and your company admins will receive a notification email when you have used up 50%, 80%, and 100% of your credits. After your credits reset at the start of the next month, you can create more SQL Segments, and automatic refreshes will resume.

If you want to purchase more SQL Segment credits or additional Segment Extensions, please contact your account manager.

- 

New Stuff!
