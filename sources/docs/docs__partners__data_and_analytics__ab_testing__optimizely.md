---
url: https://www.braze.com/docs/partners/data_and_analytics/ab_testing/optimizely
slug: docs__partners__data_and_analytics__ab_testing__optimizely
title: "Optimizely"
description: "This reference article outlines the partnership between Braze and Optimizely that allows you to sync your Braze customer segments, events, and Currents events to Optimizely..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Optimizely

Optimizely is a leading digital experience platform that offers experimentation and content management tools for digital products and marketing campaigns.

The Braze and Optimizely integration is a two-way integration that allows you to:

- Sync your Braze customer segments and events to Optimizely Data Platform (ODP) nightly to enrich Optimizely customer profiles, reports, and segmentation.
 
- Send Braze Currents events from Braze to Optimizely’s reporting tool.
 
- Sync ODP customer data and events to Braze to enrich your Braze customer data and trigger Braze messaging based on customer events in ODP.

## Prerequisites

 Requirement | 
 Description | 

 Optimizely Data Platform account | 
 An Optimizely Data Platform (ODP) account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with the following permissions: users.track,users.export.segments,segments.list,campaigns.trigger.send, and canvas.trigger.send. | 

 Currents | 
 To export data back into Optimizely, you need to have Braze Currents set up for your account. | 

 Optimizely URL and Token | 
 This can be obtained by navigating to your Optimizely dashboard and copying the ingestion URL and token. | 

## Integration

### Step 1: Configure the integration

- In the App Directory of Optimizely Data Platform (ODP), select the Braze app and then select Install App.
 
- Go to the Settings tab. In the Authorization section, do the following:

- Enter Braze REST API Key.
 
- Select your Braze Instance URL.
 
- Select Verify API Key.

- In Braze, go to Currents.
 
- Select Create New Current > Custom Currents Export.
 
- Configure the Current using the endpoint and token provided in ODP. This is required to sync Braze events to ODP.

- In ODP, expand the Segments section and select specific segments from the Segments to Sync list, or select Import All Customers to sync all segments.
 
- Add any additional field mappings you want between Braze and ODP.
 
- Select Save.

tip

You must select segments to import Braze customer profiles. If you don’t select any segments, the integration won’t import any customer profiles.

### Step 2: Map data fields

The integration has default data field mappings between Braze and ODP. For example, the Email field in Braze is mapped to the Last Seen Email field in ODP.

#### Map additional fields (optional)

If there are additional data fields in Braze that you want to map to ODP, do the following in ODP:

- In the Segments section of the app, select the Braze field from the Braze User Data Fields drop-down list.
 
- Select the ODP field from the ODP Customer Fields drop-down list.
 
- Select Save Field Map.

#### Delete non-required field mappings (optional)

You can also delete any data field mappings that aren’t required. Do the following in ODP:

- In the Segments section of the app, select the field mapping you want to delete from the Field Map drop-down list.
 
- Select Delete Field Map.

### Step 3: Sync data from Optimizely Data Platform (ODP) to Braze

After you configure the integration, you can set up an activation in ODP to sync your ODP customer data to Braze.

- Go to Activation > Engage and select Create New Campaign.
 
- Select Behavioral to set up an automated, recurring sync.
 
- Select Create From Scratch, then enter a name for your activation that represents the data you are syncing to Braze (such as Braze Data Sync).
 
- In the Enrollment section, you can sync data for customers that match a segment or sync data for customers that trigger an event (like when ODP registers that a customer opens an email):

- Customers that match a segment: Select your desired segment, then select Next.

- Customers that trigger an event: Expand the Filter drop-down list and select the ODP event to use as the trigger for this data sync to Braze. Then, expand Automation Rules and adjust as desired. 

- Expand Touchpoints, select to edit Touchpoint 1, then select Braze.
 
- Expand the Targeting section, then select the Target Identifier.
 
- Select one of the following options for Add Users To in the Configure section:

- Campaign: Add customers to a specific campaign in Braze. After choosing this option, you must select the Braze campaign.
 
- Canvas: Add customers to a specific canvas in Braze. After choosing this option, you must select the Braze canvas.
 
- Profile Update Only: Update only the Braze customer profile.

- (Optional) Select the Number of Additional Fields you want to sync to Braze (up to 20).

 Then, select the following for each additional field’s drop-down list and input field that:

- In each Field # drop-down list, select the Braze field you want to populate.
 
- In each corresponding Field # Value, enter the ODP field you want to send to the selected Braze field. For example, if you selected Company Name from the Field # drop-down list, enter `` for the corresponding Field # Value.

- Select Save, then select your activation name in the breadcrumb trail.
 
- Select Select start time and schedule in the Touchpoints section if you selected Customers that match a segment for the enrollment.
 
- Complete the following settings:

- Recurring or Continuous: Select Recurring.
 
- Start Date: Enter the date you want to send the data to Braze.
 
- End: Defaults to Never. If you want to end the Braze data sync on a specific date, set that here.
 
- Repeats: Set to Daily.
 
- Repeat Every – Set to 1 day.
 
- Timing: Enter the time you want to send the data to Braze.
 
- Time Zone: Select the time zone in which you want to send this data.

- Select Apply, Save, then Go Live. Your sync starts at your designated start date and time (or when the trigger event occurs).

## Troubleshooting

### Inspect events

To verify that data is properly syncing from ODP to Braze, you can inspect events in ODP.

- In ODP, go to Account Settings > Event Inspector.
 
- Select Start Inspector.
 
- When data is available in the inspector, a number displays next to Refresh. Select to view the data.
 
- The raw data that ODP and Braze sends back and forth displays. Select View Details to see the formatted version of that raw data.
 
- Data fields sent from Braze back to ODP start with _braze.

### Check activity logs

Each data sync is also logged in the ODP activity log:

- Go to Account Settings > Activity Log.
 
- Filter the categories by braze.
 
- Select View Details for a formatted view of the log details, including the number of matches.

- 

New Stuff!
