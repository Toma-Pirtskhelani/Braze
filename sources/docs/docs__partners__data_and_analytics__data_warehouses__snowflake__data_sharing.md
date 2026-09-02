---
url: https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake/data_sharing
slug: docs__partners__data_and_analytics__data_warehouses__snowflake__data_sharing
title: "Snowflake Data Sharing"
description: "This reference article covers the Snowflake Secure Data Sharing integration, which allows you to access Braze engagement and campaign data directly in your Snowflake instance...."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Snowflake Data Sharing

Snowflake Secure Data Sharing allows Braze to give you secure access to data on our Snowflake portal without worrying about workflow friction or slowdown, failure points, and unnecessary costs that come with typical data provider relationships. Data sharing can be set up through the following integration or through Snowflake Reader Accounts.

Snowflake Data Sharing is part of Braze Data Distribution. For a full overview of Data Distribution options, see Data Distribution.

tip

Interested in having access to Snowflake-level data without the need for a Snowflake account?
Check out Snowflake Reader Accounts. With Reader Accounts, Braze will create and share your data into an account and provide you credentials to log in and access your data. This will result in all data sharing and usage billing being handled entirely by Braze.

## Data Distribution entitlements

Your Data Distribution entitlement determines which event types are available in your data share. Braze organizes events into the following categories:

 Entitlement | 
 Event category | 
 Description | 
 Event glossary reference | 

 Engagement Events | 
 Message engagement events | 
 Events related to message sends, deliveries, opens, clicks, bounces, and other messaging channel interactions | 
 Message engagement events | 

 Customer Behavior Events | 
 Message engagement events and customer behavior events | 
 Includes all Message Engagement Events, plus events related to purchases, custom events, sessions, attribution, and in-app user actions | 
 Message engagement events, Customer behavior and user events | 

 User Profiles and Attributes | 
 Message engagement events, customer behavior events, and user profile events | 
 Includes Message Engagement Events and Customer Behavior Events, plus events related to changes in user profiles and attributes | 
 Message engagement events, Customer behavior and user events, User profile events | 

For questions about which events are included in your entitlement, contact your Braze account or customer success manager.

## About Secure Data Sharing

With data sharing, no actual data is copied or transferred between accounts. All sharing is accomplished through Snowflake’s unique services layer and metadata store. This is an important concept because shared data does not take up any storage in your account and, therefore, does not contribute to your monthly data storage charges. The only charges are for the computing resources (such as virtual warehouses) used to query the shared data.

Additionally, using Snowflake’s built-in roles and permissions capabilities, access to data shared from Braze can be controlled and governed using the access controls already in place for your Snowflake account and the data therein. Access can be restricted and monitored the same way as your own data.

- Reduce time to insights
Say goodbye to ETL processes that take weeks to build out. Braze and Snowflake’s unique architectures make all customer engagement and campaign data immediately accessible and queryable from the instant it arrives in the data lake. No data is copied or moved, so you can deliver customer experiences based on only the most relevant, up-to-date information.
 
- Break down data silos
Create a holistic view of your customers across channels and platforms. Data sharing makes joining your Braze customer engagement data with all of your other Snowflake data easier than ever—creating richer insights across a single, reliable source of truth.
 
- See how your engagement stacks up
Optimize your customer engagement strategies with Braze Benchmarks. This interactive tool, powered by Braze and Snowflake, allows you to compare your brand’s engagement data to benchmarks across channels, industry, and device platforms.

To learn more about Snowflake’s data sharing, see Introduction to Secure Data Sharing.

## Prerequisites

 Requirement | 
 Description | 

 Braze access | 
 Contact your Braze account or customer success manager to set up Data Sharing. | 

 Snowflake account | 
 A Snowflake account with admin permissions. | 

## Setting up Secure Data Sharing

For Snowflake, data sharing happens between a data provider and data consumer. Within this context, your Braze account is the data provider because it creates and sends the datashare—whereas your Snowflake account is the data consumer because it uses the datashare to create a database. For more details, see Snowflake: Consuming Shared Data.

### Step 1: Send the datashare from Braze

- In Braze, go to Partner Integrations > Data Sharing.
 
- Enter your Snowflake account details and locator. To get your account locator, run SELECT CURRENT_ACCOUNT() in the destination account.
 
- If you’re using a CRR share, specify the cloud provider and region.
 
- When you’re finished, select Create Datashare. This will send the datashare to your Snowflake account.

### Step 2: Create the database in Snowflake

- After a few minutes, you should receive the inbound datashare in your Snowflake account.
 
- 
 
Using the inbound datashare, create a database to view and query the tables. For example:

```

1

```
 | 
```
 CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>

```
 | 

- Grant privileges to query the new database.

warning

If you delete and recreate a share in the Braze dashboard, you must drop the previously-created database and recreate it using CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name> to query the inbound share.
If you have multiple workspaces sharing data to the same Snowflake account, see the Snowflake Data Sharing FAQs for guidance on managing multi-workspace configurations.

## Usage and visualization

After the data share is provisioned, create a database from the incoming data share, making all the tables shared appear in your Snowflake instance and be queryable just like any other data you’re storing in your instance. However, keep in mind that the shared data is read-only and can only be queried but not modified or deleted in any way.

Similar to Currents, you can use your Snowflake Secure Data Sharing to:

- Create complex reports
 
- Perform attribution modeling
 
- Secure sharing within your own company
 
- Map raw event or user data to a CRM (like Salesforce)
 
- And more

Download the raw table schemas.

### User ID schema

Note the following differences between Braze and Snowflake naming conventions for user IDs.

 Braze schema | 
 Snowflake schema | 
 Description | 

 braze_id | 
 "USER_ID" | 
 The unique identifier that is automatically assigned by Braze. | 

 external_id | 
 "EXTERNAL_USER_ID" | 
 The unique identifier of a user’s profile that is set by the customer. | 

## Important information and limitations

### Breaking versus non-breaking changes

#### Non-breaking changes

Non-breaking changes can happen at any time and generally provide additional functionality. Examples of non-breaking changes:

- Adding a new table or view
 
- Adding a column to an existing table or view

important

Because new columns are considered non-breaking, Braze strongly recommends explicitly listing the columns of interest in each query instead of using SELECT * queries. Alternately, you might want to create views that explicitly name columns and then query those views instead of the tables directly.

#### Breaking changes

When possible, breaking changes are preceded by an announcement and a migration period. Examples of breaking changes include:

- Removing a table or view
 
- Removing a column from an existing table or view
 
- Changing the type or nullability of an existing column

### Snowflake regions

Braze currently hosts all user-level data in these Snowflake AWS regions:

- US East-1
 
- EU-Central (Frankfurt)
 
- AP-Northeast-1 (Tokyo)
 
- AP-Southeast-2 (Sydney)
 
- AP-Southeast-3 (Jakarta)

For users outside those regions, Braze can provide data sharing to joint customers who are hosting their Snowflake infrastructure across any AWS, Azure, or GCP region.

### Data retention

#### Retention policy

Any data older than two years will be archived and moved to long-term storage. As part of the archival process, all events are anonymized and any personally identifiable information (PII) sensitive fields are stripped out (this includes optionally PII fields like properties). Archived data still contains the user_id field, which allows for per-user analytics across all events data.

You will be able to query against the most recent two years of data for each event in the corresponding USERS_*_SHARED view. Additionally, each event will have a USERS_*_SHARED_ALL view which can be queried against to return both anonymized and non-anonymized data.

#### Historical data

The archive of historical event data in Snowflake goes back to April 2019. In the first few months of Braze storing data in Snowflake, product changes were made that may have resulted in some of that data looking slightly different or having some null values (as we weren’t passing data into every available field at this time). It’s best to assume that any results that include data before August 2019 may look slightly different from expectations.

### General Data Protection Regulation (GDPR) compliance

Nearly every event record Braze stores includes a few fields representing users’ personally identifiable information (PII). Some events may include email address, phone number, device ID, language, gender, and location information. If a user’s request to be forgotten is submitted to Braze, we will null out those PII fields for any event belonging to those users. This way, we’re not removing the historical record of the event, but now the event can never be tied back to a specific individual.

### Speed, performance, cost of queries

The speed, performance, and cost of any query run on top of the data are determined by the warehouse size you use to query the data. In some cases, depending on how much data you’re accessing for analytics, you may find that you need to use a larger warehouse size for the query to be successful. Snowflake has excellent resources available about how to best determine which size to use including Overview of warehouses and Warehouse considerations

tip

For a set of example queries to reference when setting up Snowflake, check out our sample queries and ETL event pipeline setup examples.

- 

New Stuff!
