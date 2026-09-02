---
url: https://www.braze.com/docs/partners/data_and_analytics/cohort_import/treasuredata
slug: docs__partners__data_and_analytics__cohort_import__treasuredata
title: "Treasure Data cohort import"
description: "This reference article outlines the cohort import functionality of Treasure Data."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Treasure Data cohort import

This article describes how to import user cohorts from Treasure Data to Braze so you can send targeted campaigns based on data that may only exist in your warehouse.

important

This feature is currently in beta. For more information, contact your Treasure Data and Braze representatives.

## Prerequisites

 Requirement | 
 Description | 

 Treasure Data account | 
 A Treasure Data account is required to take advantage of this partnership. | 

 Braze Data Import key | 
 This can be captured in the Braze dashboard from Partner Integrations > Technology Partners and then select Treasure Data. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

 Static IP Address of Treasure Data | 
 The static IP address of Treasure Data is the access point and source of the linkage for this Integration. To determine the static IP address, contact your Treasure Data Customer Success representative or Treasure Data Technical support. | 

## Data import integration

### Step 1: Get your Braze data import key

In Braze, navigate to Partner Integrations > Technology Partners and select Treasure Data. Here, you will find your REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one.

### Step 2: Create a data connection

Before you create your data connection within Treasure Data, you’ll need to authenticate. First, select Integrations Hub, then Catalog.

Search for the Braze Integration in the Catalog, then hover over the icon and select Create Authentication. Enter your credentials, name your authentication, then select Done.

### Step 3: Define your cohort Audience

Sync your cohorts to Braze through an activation in the Audience Studio or by executing a query in the Data Workbench.

important

Only users who already exist within Braze are added or removed from a cohort. Cohort Import will not create new users in Braze.

- data workbench
 
- audience studio

#### Step 3.1: Define your query

note

Query columns must be specified with the exact column names and data type. The query columns must include at least one of the columns: user_ids, device_ids, or braze alias column match with configuration on the UI. Only user profiles that exist within Braze will be added to a cohort. Cohort Import will not create new user profiles.

- Navigate to Data Workbench > Queries.
 
- Select New Query.
 
- Run the query to validate the result set.

##### Use case: Syncing cohorts by identifier

- syncing external ids
 
- syncing user aliases
 
- syncing device ids

Here’s an example table in Treasure Data:

 external_id | 
 email | 
 device_ids | 

 TDCohort1 | 
 [email protected] | 
 1a2b3c | 

 TDCohort2 | 
 [email protected] | 
 4d5f6g | 

 TDCohort3 | 
 [email protected] | 
 7h8j9k | 

 TDCohort4 | 
 [email protected] | 
 1ab2cd | 

warning

The column name must be user_ids or the sync will fail.

To sync cohorts using the external ID, run the following query:

```

1
2
3
4

```
 | 
```
SELECT
 external_id as user_ids
FROM
 example_cohort_table

```
 | 

After running the query, these user aliases will be added to the cohort in Braze:

- TDCohort1
 
- TDCohort2
 
- TDCohort3
 
- TDCohort4

Here’s an example table in Treasure Data:

 external_id | 
 email | 
 device_ids | 

 TDCohort1 | 
 [email protected] | 
 1a2b3c | 

 TDCohort2 | 
 [email protected] | 
 4d5f6g | 

 TDCohort3 | 
 [email protected] | 
 7h8j9k | 

 TDCohort4 | 
 [email protected] | 
 1ab2cd | 

To sync cohorts using the user alias, run the following query:

```

1
2
3
4

```
 | 
```
SELECT
 email
FROM
 example_cohort_table

```
 | 

After running the query, these user aliases will be added to the cohort in Braze:

- "alias_label":"email", "alias_name":"[email protected]"
 
- "alias_label":"email", "alias_name":"[email protected]"
 
- "alias_label":"email", "alias_name":"[email protected]"
 
- "alias_label":"email", "alias_name":"[email protected]"

Here’s an example table in Treasure Data:

 external_id | 
 email | 
 device_ids | 

 TDCohort1 | 
 [email protected] | 
 1a2b3c | 

 TDCohort2 | 
 [email protected] | 
 4d5f6g | 

 TDCohort3 | 
 [email protected] | 
 7h8j9k | 

 TDCohort4 | 
 [email protected] | 
 1ab2cd | 

warning

The column name must be device_ids or the sync will fail.

To sync cohorts using the device ID, run the following query:

```

1
2
3
4

```
 | 
```
SELECT
 device_ids
FROM
 example_cohort_table

```
 | 

After running the query, these device IDs will be added to the cohort in Braze:

- 1a2b3c
 
- 4d5f6g
 
- 7h8j9k
 
- 1ab2cd

#### Step 3.2: Specify the result export target

Once the query has been built, select Export Results. You can select an existing authentication, such as the one created in the last steps, or create a new authentication to be used for output.

 Export Result Mapping | 
 Description | 

 Cohort ID | 
 This is the backend cohort identifier that will be sent to Braze. | 

 Cohort Name (Optional) | 
 This is the name that will appear within the Cohort Filter in the Braze segmentation tool. If this is not set, the Cohort ID will be used as the Cohort Name. | 

 Operation | 
 Used to determine whether the query should add or remove profiles from the cohort in Braze. | 

 Aliases (Optional) | 
 When defined, the name of the corresponding column within your query will be sent as the alias_label, and the values of each row in the column will be sent as the alias_name. | 

 Thread Count | 
 Number of concurrent API calls. | 

Follow Treasure Data’s steps for configuring your export to meet your use case.

#### Step 3.3: Execute the query

Save the query with a name and run, or just run the query. Upon successful completion of the query, the query result is automatically exported to Braze.

#### Step 3.1: Create an activation

Create a new segment or choose an existing segment to sync to Braze as a cohort. Within the segment, choose Create activation.

#### Step 3.2: Fill out your activation details

 Activation Detail Setting | 
 Description | 

 Activation Name | 
 The name of your activation. | 

 Activation Description | 
 A brief description of the activation. | 

 Authentication | 
 Choose the Braze cohort authentication created in step 2. | 

 Cohort ID | 
 This is the backend cohort identifier that will be sent to Braze. | 

 Cohort Name (Optional) | 
 This is the name that will appear within the Cohort Filter in the Braze segmentation tool. If this is not set, the Cohort ID will be used as the Cohort Name. | 

 Operation | 
 Used to determine whether the query should add or remove profiles from the cohort in Braze. | 

 Aliases (Optional) | 
 When defined, the name of the corresponding column within your query will be sent as the alias_label, and the values of each row in the column will be sent as the alias_name. | 

 Thread Count | 
 Number of concurrent API calls. | 

#### Step 3.3: Set up output mapping

 Activation Output Mapping | 
 Description | 

 Attribute Columns | 
 Determine the columns from your segment database that will be mapped as identifiers when syncing profiles to a Braze cohort. | 

 String Builder | 
 The string builder is not necessary for the Braze integration. | 

important

- When using device_id as the identifier, the Output Column Name must be named device_ids.
 
- When using aliases as the identifier, the Output Column Name must be the name of the corresponding column within your query will be sent as the alias_label, and the values of each row in the column will be sent as the alias_name.
 
- When using external_id as the identifier, the Output Column Name must be named user_ids.

All non-relevant or misnamed column names will be ignored. You may choose to use more than one identifier in your syncs.

#### Step 3.4: Define your activation schedule

Define your desired sync schedule and save your activation.

### Step 4: Create a Braze segment from the Treasure Data Export

In Braze, navigate to Segments, create a new segment, and select Treasure Data Cohorts as your filter. From here, you can choose which Treasure Data cohort you wish to include. After your Treasure Data cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.

## User Matching

Identified users can be matched by either their external_id or alias. Anonymous users can be matched by their device_id. Identified users who were originally created as anonymous users can’t be identified by their device_id, and must be identified by their external_id or alias.

- 

New Stuff!
