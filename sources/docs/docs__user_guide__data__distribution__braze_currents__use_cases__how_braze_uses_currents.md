---
url: https://www.braze.com/docs/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents
slug: docs__user_guide__data__distribution__braze_currents__use_cases__how_braze_uses_currents
title: "How Braze uses Currents"
description: "This Currents how-to article will walk you through the basic process for setting up proper intakes for event data, as well as moving it into..."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# How Braze uses Currents

Braze uses Currents internally with selected partners.

We filter our data from email and push campaigns into a business insights tool, Looker, but it takes a slightly different route to get there. We use an inverted version of the Extract, Transform, Load (ETL) methodology—switching the order to Extract, Load, Transform (ELT).

## Step 1: Intake and aggregate event data

After launching campaigns using any of our engagement tools (like campaigns or Canvas), we track event data using our own system as well as some from our email partners. Some of this data is aggregated and shown in the dashboard, but we’re interested in diving deeper!

## Step 2: Send event data to a data storage partner

We set up Currents to send Braze event data to Amazon S3 for storage and extraction. Now, we do know that you can use Athena to sit on top of S3 and run queries. It’s a great short-term solution. But we wanted a long-term solution using a Relational Database and a Business Intelligence/Analytics tool. (We recommend that same for you.)

S3 provides flexible storage and routing options for moving, pivoting, and analyzing data. We do not transform data in S3 because we maintain a specific structure for it.

## Step 3: Transform event data with a relational database

From S3, we choose a warehouse (Snowflake Data Sharing or Snowflake Reader Accounts, in our case). We transform it there, then move it to Looker, where we have blocks set up that will structure and organize our data.

Snowflake isn’t the only warehouse option. Other options include Redshift, Google BigQuery, and more!

### Snowflake Reader Accounts

Snowflake Reader Accounts offer users access to the same data and functionality as Snowflake Data Sharing, all without requiring a Snowflake account or customer relationship with Snowflake. With Reader Accounts, Braze will create and share your data into an account and provide you credentials to log in and access your data. This will result in all data sharing and usage billing being handled entirely by Braze.

To learn more, contact your customer success manager.

#### Additional resources

For helpful usage monitoring resources, check out Snowflake’s Resource Monitors and Viewing Warehouse Credit Usage articles.

## Step 4: Use a Business Intelligence (BI) tool to manipulate your data

Finally, we use a BI tool to analyze our data, turn it into charts and other visual tools, and more using Looker and Looker Blocks so we don’t have to ETL or ELT data every time it moves from Currents.

Feeling inspired to do the same? Check out the following docs to get more information on these and how you can use them to build your database!

- User Behavior Block
 
- Message Engagement Block

- 

New Stuff!
