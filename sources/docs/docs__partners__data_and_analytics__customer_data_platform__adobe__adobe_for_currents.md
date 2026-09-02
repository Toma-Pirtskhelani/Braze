---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents
slug: docs__partners__data_and_analytics__customer_data_platform__adobe__adobe_for_currents
title: "Adobe for Currents"
description: "This reference article outlines the partnership between Braze Currents and Adobe, a customer data platform that allows brands to connect and map their Adobe data..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Adobe for Currents

Adobe is a customer data platform that allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real time.

The Braze and Adobe integration allows you to seamlessly control the flow of information between the two systems. With Currents, you can also connect data to Adobe to make it actionable across the entire growth stack.

## Prerequisites

 Requirement | 
 Description | 

 Currents | 
 To export data back into Adobe, you need to have Braze Currents set up for your account. | 

 Adobe Experience Platform account | 
 An Adobe Experience Platform account is required to take advantage of this partnership. | 

 Permission to create a connector | 
 You need permissions to create a streaming source connection to use this integration. | 

## Integration

### Step 1: Create an XDM schema in Adobe

- In Adobe Experience Platform, go to Schemas > select Create schema > select Experience Event > select Next.

- Provide a name and description for your schema.
 
- In the Composition panel, configure your schema attributes:

- In Field groups, select Add and then add the Braze Currents User Event field group.
 
- Select Save.

For more information on schemas, refer to Adobe’s documentation on creating schemas.

### Step 2: Connect Braze to the Adobe Experience Platform

- In Adobe Experience Platform, go to Sources > Catalog > Marketing automation.
 
- Select Add data for Braze Currents.
 
- Upload the Braze Currents sample file.

- After your file is uploaded, provide your dataflow details, including information about your dataset and the schema that you are mapping to.

- If this is your first time connecting a Braze Currents source, create a new dataset and make sure to use the schema you created in Step 1.
 
- If this isn’t your first time, use any existing dataset that references the Braze schema.

- Configure mapping for your data and resolve the issues.

- Change the mapping for id from to _braze.appID to _id at the root level of the schema.
 
- Make sure properties.is_amp is mapped to _braze.messaging.email.isAMP.
 
- Delete the time and timestamp mapping, then select the add icon > Add calculated field and enter time * 1000. Select Save.
 
- Select Map target field next to the new source field and map it to timestamp at the root level of the schema. 

- Select Validate to confirm you resolved the issues.

important

Braze timestamps are expressed in seconds. To accurately reflect timestamps in Adobe Experience Platform, your calculated fields need to be in milliseconds. To convert seconds to milliseconds, use the calculation time * 1000.

- Select Next, review your dataflow details, and then select Finish.

### Step 3: Gather credentials

Collect the following credentials to input into Braze, which will allow Braze to send data to Adobe Experience Platform.

 Field | 
 Description | 

 Client ID | 
 The client ID associated with your Adobe Experience Platform source. | 

 Client Secret | 
 The client secret associated with your Adobe Experience Platform source. | 

 Tenant ID | 
 The tenant ID associated with your Adobe Experience Platform source. | 

 Sandbox Name | 
 The sandbox associated with your Adobe Experience Platform source. | 

 Dataflow ID | 
 The dataflow ID associated with your Adobe Experience Platform source. | 

 Streaming Endpoint | 
 The streaming endpoint associated with your Adobe Experience Platform source. Braze automatically converts this to the batch streaming endpoint. | 

### Step 4: Configure Currents to stream data to your data source

- In Braze, go to Partner Integrations > Data Export, and then select Create New Current.
 
- Provide the following:

- A name for the connector
 
- Contact information for notifications about the connector
 
- The credentials from Step 3

- Select the events you want to receive.
 
- Optionally configure any desired field exclusions or transformations.
 
- Select Launch Current.

- 

New Stuff!
