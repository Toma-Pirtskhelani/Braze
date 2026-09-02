---
url: https://www.braze.com/docs/user_guide/get_started/b2b_use_cases/b2b_salesforce_sales_cloud
slug: docs__user_guide__get_started__b2b_use_cases__b2b_salesforce_sales_cloud
title: "Manage leads with Salesforce Sales Cloud"
description: "Learn how to use Braze webhooks to create and update leads in Salesforce Sales Cloud through the Salesforce sobjects/Lead endpoint."
section: user_guide/get_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# Manage leads with Salesforce Sales Cloud

Salesforce is one of the world’s leading cloud-based Customer Relationship Management (CRM) platforms designed to help businesses manage their entire sales process, including lead generation, opportunity tracking, and account management.

This page demonstrates how to use Braze webhooks to create and update leads in Salesforce Sales Cloud through a community-submitted integration.

important

This is a community-submitted integration and isn’t directly supported by Braze. Only official Braze-provided webhook templates are supported by Braze.

## How it works

The Braze and Salesforce Sales Cloud integration uses Braze webhooks to create and update leads in Salesforce Sales Cloud through the Salesforce sobjects/Lead endpoint.

Braze currently offers two integrations to Salesforce Sales Cloud for the following use cases:

- Creating a lead in Salesforce Sales Cloud
 
- Updating a lead in Salesforce Sales Cloud

note

This integration is purely to update Salesforce from Braze as part of your lead acquisition and nurturing efforts. For syncing data from Salesforce back to Braze, check out B2B data model or connect with one of our technology partners.

## Prerequisites

Before you can proceed with this integration, Salesforce Support must give you the ability to create connected apps. You can request this by submitting a Salesforce Support request.

After Salesforce Support grants you the ability to create a connected app in Salesforce Sales Cloud, follow the steps in the Salesforce documentation: Configure a Connected App for the OAuth 2.0 Client Credentials Flow.

When you configure the necessary OAuth settings for the connected app, keep all oAuth settings with their default values and selections except for the following:

- Select Enable for device flow. You can leave Callback URL blank, as it will default to a placeholder.
 
- For selected OAuth Scopes, add Manage user data via APIs (api).
 
- Select Enable Client Credentials Flow.

## Creating a lead in Salesforce Sales Cloud

As your customer engagement platform, Braze can generate new leads based on user flows such as filling out a form on a landing page. When that happens, you can use a Braze Salesforce Sales Cloud webhook to create a corresponding lead in Salesforce.

### Step 1: Collect your client_id and client_secret

- In Salesforce, go to Platform Tools > Apps > App Manager.
 
- Find your newly created Braze App and select View.
 
- Under Consumer Key and Secret, select Manage Consumer Details.
 
- On the resulting page, take note of your Consumer Key and Consumer Secret. The Consumer Key is your client_id, and the Consumer Secret is your client_secret.

### Step 2: Set up your webhook template

Use templates to quickly reuse this webhook across the Braze platform.

- In Braze, go to Templates, select Webhook Templates, then select + Create Webhook Template.
 
- Provide a name for the template, such as “Salesforce Sales Cloud > Create Lead”.
 
- In the Compose tab, enter the following details:

#### Compose webhook

 Field | 
 Details | 

 Webhook URL | 
 https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/ | 

 HTTP method | 
 POST | 

 Request Body | 
 JSON Key/Value Pairs | 

#### Body property key values

Select + Add New Body Property for each of the key/value pairs you want to map over from Braze to Salesforce. You can map over any field you want, so the following table is just one example.

 Key | 
 Value | 

 firstName | 
 {{${first_name}}} | 

 lastName | 
 {{${last_name}}} | 

 email | 
 {{${email_address}}} | 

 company | 
 {{custom_attribute.${company}}} | 

#### Request headers

Select + Add New Header for each of the following request headers.

 Key | 
 Value | 

 Authorization | 
 {% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token :method post :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials :save result %}Bearer {{result.access_token}} | 

 Content-Type | 
 application/json | 

- Select Save Template.

## Updating a lead in Salesforce Sales Cloud

To set up a Braze Salesforce Sales Cloud webhook that updates leads in Salesforce, you need a common identifier between Salesforce Sales Cloud and Braze. The example in the following section uses the Salesforce lead_id as the Braze external_id, but you can also accomplish this by using a user_alias. For details on this, refer to B2B Data

This example specifically demonstrates how to update a lead’s lead stage to “MQL” (Marketing Qualified Lead) after a lead crosses a certain lead threshold. This is a core part of our B2B lead scoring workflow use case.

### Step 1: Collect your client_id and client_secret

- In Salesforce, go to Platform Tools > Apps > App Manager.
 
- Find your newly created Braze App and select View.
 
- Under Consumer Key and Secret, select Manage Consumer Details.
 
- On the resulting page, take note of your Consumer Key and Consumer Secret.

- The Consumer Key is your client_id, and the Consumer Secret is your client_secret.

### Step 2: Set up your webhook template

- In Braze, go to Templates, select Webhook Templates, then select + Create Webhook Template.
 
- Provide a name for the template, such as “Salesforce Sales Cloud > Update Lead to MQL”.
 
- In the Compose tab, enter the following details:

#### Compose webhook

 Field | 
 Details | 

 Webhook URL | 
 https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}} | 

 HTTP method | 
 PATCH | 

 Request Body | 
 JSON Key/Value Pairs | 

#### Body property key values

Select + Add New Body Property for the following key/value pair. Note that Lead_Stage__c is an example name. The custom field you use to track MQLs in Salesforce may have a different name, so make sure that they match.

 Key | 
 Value | 

 Lead_Stage__c | 
 MQL | 

#### Request headers

Select + Add New Header for each of the following request headers.

 Key | 
 Value | 

 Authorization | 
 {% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token :method post :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials :save result %}Bearer {{result.access_token}} | 

 Content-Type | 
 application/json | 

- Select Save Template.

## Using these webhooks in an operational workflow

You can quickly add your templates to your operational workflows in Braze, such as:

- Part of a new user campaign that creates a lead in Salesforce
 
- Part of a lead scoring Canvas that updates users who have crossed your MQL threshold to “MQL”, and that updates Salesforce Sales Cloud with the same information

### New lead campaign

To create a lead in Salesforce when a user provides their email address, you can create a campaign that uses the “Update Lead” webhook template and triggers when a user adds their email address (for example, fills out a web form).

### Lead scoring Canvas for crossing the Marketing Qualified Lead (MQL) threshold

This webhook is covered in the lead scoring use case, but you can also check for MQLs and directly update Salesforce within the lead scoring Canvas (as opposed to creating a separate webhook campaign):

Add a subsequent step to your user update to check if a user has crossed your defined MQL threshold. If they have crossed, update the user’s status to “MQL”, and then update Salesforce with the same “MQL” status by using this webhook template. Salesforce takes care of the rest by routing this lead to the appropriate sales teams using your defined lead routing rules.

#### Adding Canvas step to check for users who passed the MQL threshold

- Add an Audience Path step with two groups: “MQL Threshold” and “Everyone Else”.
 
- In the “MQL Threshold” group, look for any users who currently don’t have a status of “MQL” (for example, lead_stage equals “Lead”), but have a lead score that is over your defined threshold (for example, lead_score greater than 50). If so, they move forward to the next step, if not, they exit.

- Add a User Update step that updates the user’s lead_stage attribute value to “MQL”.

- Add a webhook step that updates Salesforce with the new MQL stage.

Now your Canvas flow will update users who’ve crossed your MQL threshold!

## Troubleshooting

These workflows have limited debugging capability within Salesforce, so we recommend referring to the Braze Message Activity Log to find out why a Webhook failed and if any errors occurred.

For example, an error caused by an invalid URL used for oAuth token retrieval would display as https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL.

- 

New Stuff!
