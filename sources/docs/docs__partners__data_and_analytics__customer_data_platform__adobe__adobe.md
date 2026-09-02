---
url: https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/adobe/adobe
slug: docs__partners__data_and_analytics__customer_data_platform__adobe__adobe
title: "Adobe"
description: "This page outlines the partnership between Braze and Adobe, a customer data platform, that allows brands to connect and map their Adobe data (custom attributes..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Adobe

Built on the Adobe Experience Platform, Adobe’s real-time customer data platform brings together known and anonymous data from multiple enterprise sources to create customer profiles. These profiles can then be used to provide personalized experiences across all channels and devices in real-time.

The Braze and Adobe CDP integration connects and maps your brand’s Adobe data (custom attributes and segments) to Braze in real-time. You can then act on this data, delivering personalized, targeted experiences to your users. With Adobe, the integration is intuitive. Simply take any Adobe identity, map it to a Braze external ID, and send it off to the Braze platform. All data sent will be accessible in Braze through a new AdobeExperiencePlatformSegments attribute.

important

The Adobe Experience Platform integration currently doesn’t support dynamic audience membership. This means it can only add values to user profiles, not remove them.

## Prerequisites

 Requirement | 
 Description | 

 Adobe account | 
 An Adobe account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze instance | 
 Your Braze instance can be obtained from your Braze onboarding manager or can be found on the API overview page. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint will depend on the Braze URL for your instance. | 

important

The sending of additional custom attributes will increase your data point usage. We suggest speaking with your customer success manager to better understand this potential data point increase.

## Integration

### Step 1: Configure Braze destination

From the Adobe Settings page, select Destinations under Collections. From there, locate the Braze tile and select Configure.

note

If a connection with Braze already exists, you’ll see an Activate button on the destination card. For more information about the difference between activate and configure, refer to the catalog section of the Adobe destination workspace documentation.

### Step 2: Provide Braze token

In the Account step, provide your Braze API key and select Connect to destination.

### Step 3: Authentication

Next, in the Authentication step, enter your Braze connection details:

- Name: Enter the name you’d like to recognize this destination by in the future.
 
- Destination: Enter a description that will help you identify this destination.
 
- Endpoint instance: Enter your Braze endpoint instance.
 
- Marketing use case: Marketing use cases indicate the intent for which data will be exported to the destination. You can select from Adobe-defined marketing use cases or create your own marketing use case. To read more about Adobe marketing use cases, visit Data governance in Adobe Experience Platform.

### Step 4: Create destination

Select Create destination. Your destination has been created. You can select Save & Exit to activate segments later or Next to continue the workflow and select segments to activate.

### Step 5: Activate segments

Activate the data you have in the Adobe real-time CDP by mapping segments to the Braze destination.

The following list highlights the general steps required to activate a segment. For thorough guidance on Adobe segments and the segment activation workflow, visit Adobe.

- Select and activate the Braze destination.
 
- Select applicable segments.
 
- Configure scheduling and file names for each segment you export.
 
- Select attributes to send to Braze.
 
- Review and verify activation.

### Step 6: Field mapping

To correctly send your audience data from the Adobe Experience Platform to Braze, you must complete the field mapping step. Mapping creates a link between the Adobe Experience data model fields and the corresponding Braze platform fields.

- In the mapping step, select Add new mapping.

- In the source field section, select the arrow button next to the empty field to open the select source field window.

- In the window, select Adobe attributes to map to your Braze attributes. 

Next, select the identity namespace. This option is used to map a platform identity namespace to a Braze namespace.

 Choose your source fields, then select Select.

- In the target field section, select the mapping icon beside the field.

- In the select target field window, you can choose between three categories of target fields:

• Select identity namespace: Use this option to map Platform identity namespaces to Braze identity namespaces.
• Select custom attributes: Use this option to map Adobe XDM attributes to custom Braze attributes that you defined in your Braze account. 

You can also use this option to rename existing XDM attributes into Braze. For example, mapping a lastname XDM attribute to a custom Last_Name attribute in Braze, will create the Last_Name attribute in Braze if it doesn’t already exist, and map the lastname XDM attribute to it. 

 Choose your target fields, then select Select.

- Your field mapping should appear in the list.

- To add more mappings, repeat steps 1 through 6, as necessary.

## Use case

Let’s say your XDM profile schema and your Braze instance contains the following attributes and identities:

   | 
 XDM profile schema | 
 Braze instance | 

 Attributes | 
 - person.name.firstname
- person.name.lastname
- mobilePhone.number | 
 - FirstName
- LastName
- PhoneNumber | 

 Identities | 
 - Email
- Google Ad ID (GAID)
- Apple ID For Advertisers (IDFA) | 
 - external_id | 

The correct mapping would look like this:

## Exported data

To verify if data has been exported successfully to Braze, check your Braze account. Adobe Experience Platform segments are exported to Braze under the AdobeExperiencePlatformSegments attribute.

## Data usage and governance

All Adobe Experience Platform destinations are compliant with data usage policies when handling your data. See Data governance in real-time CDP for detailed information on how the Adobe Experience Platform enforces data governance.

- 

New Stuff!
