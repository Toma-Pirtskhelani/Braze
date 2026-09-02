---
url: https://www.braze.com/docs/partners/data_and_analytics/cohort_import/kubit
slug: docs__partners__data_and_analytics__cohort_import__kubit
title: "Kubit cohort import"
description: "This reference article outlines the cohort import functionality of Kubit, a no-code, self-service analytics platform that delivers instant product insights, allowing you to import Kubit..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Kubit cohort import

This article describes how to import user cohorts from Kubit to Braze. For more information on integrating Kubit and its other functionalities, see the main Kubit article.

## Data import integration

### Step 1: Get the Braze data import key

In Braze, navigate to Partner Integrations > Technology Partners and select Kubit. Here, you will find the REST endpoint and generate your Braze data import key.

Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Kubit’s dashboard.

### Step 2: Configure Braze in Kubit

Provide the Braze data import key and Braze REST endpoint to your Kubit support contact. They will configure the integration on their side and let you know when the integration is live.

### Step 3: Import Cohorts to Braze

#### Create a cohort in Kubit

Create a cohort in Kubit and define the criteria of your target users.

#### Import users to Braze

Once you have saved your cohort, you can import them to Braze to be used in Braze segments. These segments can then be used to create targeted email or push campaigns and Canvases.

To do this, navigate to your existing cohort and under Cohort Control select Import to Braze.

Next, select the desired import cadence. One-time imports allow you to import once now. Scheduled imports allow you to import daily, weekly, or monthly at a specific time. Note that each cohort can only have one live import schedule.

important

Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.

#### Verify import status

Once an import has been completed, an email notification will be sent to the recipients(s) specified in the import schedule. You can also check a cohort’s import status under Schedule in Kubit. The schedule history will display every import execution time, outcome, and the total number of users in the cohort who were imported to Braze.

You can manually trigger an import by clicking on Import to Braze icon for that import schedule.

### Step 4: Create Braze segments with Kubit cohorts

After importing cohorts to Braze, you can use them as filters to create Braze segments and include them in Braze campaigns or Canvas. Visit our segment documentation to learn more about how to create Braze segments.

## User Matching

Identified users can be matched by either their external_id or alias. Anonymous users can be matched by their device_id. Identified users who were originally created as anonymous users can’t be identified by their device_id, and must be identified by their external_id or alias.

- 

New Stuff!
