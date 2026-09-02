---
url: https://www.braze.com/docs/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import
slug: docs__partners__data_and_analytics__reverse_etl__hightouch__hightouch_cohort_import
title: "Hightouch cohort import"
description: "This reference article outlines the cohort import functionality of Hightouch, a platform to sync your customer data from your warehouse to business tools."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Hightouch cohort import

This article describes how to import user cohorts from Hightouch to Braze so you can send targeted campaigns based on data that may only exist in your warehouse. For more information on integrating Hightouch and its other functionalities, see the main Hightouch article.

## Data import integration

### Step 1: Get the Braze data import Key

In Braze, navigate to Partner Integrations > Technology Partners and select Hightouch.

Here, you will find your REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one.

### Step 2: Add Braze cohorts as a Destination in Hightouch

Navigate to the Destination page in your Hightouch workspace, search for Braze Cohorts, and click Continue. From there, take your REST endpoint and data import key and click Continue.

### Step 3: Sync a model (or audience) into Braze Cohorts

In Hightouch, using your created model or audience, create a new sync. Next, select the Braze Cohorts destination you created in the previous step. Lastly, in the Braze Cohorts destination configuration, select the identifier you want to match against and decide whether or not you want Hightouch to create a new Braze Cohort or update an existing one.

important

Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.

### Step 4: Create a Braze segment from the Hightouch custom audience

In Braze, navigate to Segments, create a new segment, and select Hightouch Cohorts as your filter. From here, you can choose which Hightouch cohort you wish to include. After your Hightouch cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.

### Using this integration

To use your Hightouch segment, create a Braze campaign or Canvas and select the segment as your target audience.

## User Matching

Identified users can be matched by either their external_id or alias. Anonymous users can be matched by their device_id. Identified users who were originally created as anonymous users can’t be identified by their device_id, and must be identified by their external_id or alias.

- 

New Stuff!
