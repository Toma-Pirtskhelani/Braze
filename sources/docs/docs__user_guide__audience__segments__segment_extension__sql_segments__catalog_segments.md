---
url: https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments/catalog_segments
slug: docs__user_guide__audience__segments__segment_extension__sql_segments__catalog_segments
title: "Catalog segments"
description: "This article describes how to create catalog segments, which use catalog data in SQL Segment Extensions to build audiences of users."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Catalog segments

Catalog segments are a type of SQL Segment Extension that is created by combining catalog data with data from custom events or purchases. They can be referenced in a segment and then targeted by campaigns and Canvases.

Catalog segments use SQL to join data from catalogs and data from custom events or purchases. To do so, you must have a common identifier field across your catalogs and your custom events or purchases. For example, the value of an item ID in a catalog must match the value of a property in a custom event.

## Creating a catalog segment

- Go to Segment Extensions > Create New Extension > Start With Template and select a template. 

- 
 
The SQL editor automatically populates with a template. 

This template joins user event data with catalog data to segment users who engaged with certain catalog items.

- 
 
Use the Variables tab to provide the necessary fields for your template before generating your segment. 
For Braze to identify users based on their engagement with catalog items, you need to do the following: 
 - Select a catalog that contains a catalog field 
 - Select a custom event that contains an event property 
 - Match your catalog field and event property values

Here are guidelines to select the variables:

 Variable field | 
 Description | 

 Catalog | 
 The name of the catalog you’re using to target users. | 

 Catalog field | 
 The field in your catalog that contains the same values as your Custom event property. This is often a type of ID. In the eCommerce use case, this would be shopify_id. | 

 Custom event | 
 The name of your custom event, which is the same event that contains a property with values matching your Catalog field. In the eCommerce use case, this would be Made Order. | 

 Custom event property | 
 The name of your custom event property, which matches values with your Catalog field. In the eCommerce example use case, this would be Shopify_ID. | 

- If needed, fill in additional optional fields for your use case to segment by a particular field value within your catalog:

- Catalog field: A particular field (column name) within this catalog
 
- Value: A specific value within that field or column 

 Using the health app as an example, let’s say that within the catalog for each doctor you could book, there’s a field called specialty that contains a value such as vision or dental. To segment users who have visited any doctors with the value dental, you can select specialty as the Catalog field, and select dental as the Value.

- After creating a SQL Segment, we recommend clicking Run Preview to see if your query returns users or if there are errors. For more information about previewing query results, managing SQL Segment Extensions, and more, check out SQL Segment Extensions.

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

### Determining if you need to invert SQL

While it’s not possible to directly query for users with zero events, you can use Invert SQL to target these users.

For example, to target users who have fewer than three purchases, first write a query to select users who have three or more purchases. Then, select Invert SQL to target users with fewer than three purchases (including those with zero purchases).

important

Unless you’re specifically aiming to target users with zero events, you won’t need to invert SQL. If Invert SQL is selected, confirm that the feature is needed and that the segment matches your desired audience. For example, if a query targets users with at least one event, it will only target users with zero events when inverted.

## Refreshing segment membership

To refresh the segment membership of any catalog segment, open the catalog segment and select Actions > Refresh > Yes, Refresh.

tip

If you created a segment where you expect users to enter and exit regularly, manually refresh the catalog segment it uses before targeting that segment in a campaign or Canvas.

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

## Use cases

- health
 
- saas

### Health app

Let’s say you have a health app and want to segment users who have booked a visit for the dentist. You also have the following:

- A catalog Doctors that contains the different doctors a patient can book, each assigned with a doctor ID
 
- A custom event Booked Visit with a doctor ID property that shares the same values as the doctor ID field in your catalog
 
- A speciality field within your catalog that contains the dental value

You would set up a catalog segment by using the following variables:

 Variable | 
 Property | 

 Catalog | 
 Doctors | 

 Catalog field | 
 doctor ID | 

 Custom event | 
 Booked Visit | 

 Custom event property | 
 doctor ID | 

 (Under Filter SQL Results) Catalog field | 
 Specialty | 

 (Under Filter SQL Results) Value | 
 Dental | 

### SaaS platform

Let’s say you have B2B SaaS platform and want to segment users who are employees of an existing customer. You also have the following:

- A catalog Accounts that contains the different accounts that are currently using your SaaS platform, each assigned with an account ID
 
- A custom event Event Attendance with an “account ID” property that shares the same values as the “account ID” field in your catalog
 
- A Classification field within your catalog that contains the enterprise value

You would set up a catalog segment by using the following variables:

 Variable | 
 Property | 

 Catalog | 
 Accounts | 

 Catalog field | 
 account ID | 

 Custom event | 
 Event Attendance | 

 Custom event property | 
 account ID | 

 (Under Filter SQL Results) Catalog field | 
 Classification | 

 (Under Filter SQL Results) Value | 
 Enterprise | 

## Frequently asked questions

### Does running a catalog segment consume SQL Segment Extension credits?

Yes, catalog segments are powered by SQL and consume SQL Segment Extension credits. To learn more, check out SQL Segments usage.

### Does creating a catalog segment consume SQL Segment Extension allotments?

Yes. In the same way SQL Segment Extensions count toward your Segment Extension allotment, catalog segments also count toward that allotment.

### I have a catalog segment use case that the current template doesn’t serve. How should I set that up?

Contact your customer support manager or Braze Support for additional guidance.

- 

New Stuff!
