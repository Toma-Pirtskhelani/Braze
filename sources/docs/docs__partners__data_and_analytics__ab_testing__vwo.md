---
url: https://www.braze.com/docs/partners/data_and_analytics/ab_testing/vwo
slug: docs__partners__data_and_analytics__ab_testing__vwo
title: "VWO"
description: "Learn how to integrate VWO with Braze."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# VWO

VWO is a powerful experimentation platform that helps brands enhance key business metrics by enabling teams to run conversion optimization programs backed by customer behavior data. With VWO, you can unify customer data, gain behavioral insights, build hypotheses, run A/B tests across multiple platforms (server, web, and mobile), roll out features, personalize experiences, and optimize the entire customer journey.

By integrating VWO with Braze, you can leverage VWO experiment data to create targeted segments and deliver personalized campaigns.

## Prerequisites

 Requirement | 
 Description | 

 VWO account | 
 A VWO account with access to experimentation data. | 

 Braze account | 
 An active Braze account with the Braze Web SDK integrated on your webpage. You’ll also need event property segmentation enabled. To request it, see Considerations. | 

## Integrating VWO with Braze

### Step 1: Enable the Braze integration in VWO

- Log in to your VWO account.
 
- 
 
In the VWO dashboard, go to Configurations > Integrations. Here, you can enable integrations at the workspace level, which applies the integration to all future test campaigns by default.

- Select the Braze integration to enable it.
 
- 
 
Optionally, you can enable the Braze integration for any existing campaigns. To do so, select a campaign, then go to Configuration > Integrations, and enable Braze.

- After you’ve enabled the integration, VWO will start sending experiment data to Braze at the campaign level.

### Step 2: Create a segment in Braze with VWO event properties

- In the Braze dashboard, select Segments > + Create Segment.
 
- In the Create Segment window, enter a name for the segment, then Create Segment.
 
- In your newly-created segment, select Filters > Add Filter, then choose Custom Event as the filter type.
 
- In the filter dropdown, search for VWO.
 
- Select the relevant VWO property and specify the required value.
 
- 
 
If needed, configure the number of visits and time frame. When you’re finished, select Save.

- 
 
To view the number of users that match your segment criteria, select Calculate Exact Statistics.

## Data flow

VWO sends the campaign experiment data to Braze as a custom event using the following format:

- Event Name: VWO
 
- Event Properties: vwo_campaign_name, vwo_variation_name

tip

These custom event properties can also be used for segmentation and targeting.

## Considerations

### Request event property segmentation

Before you can use event property segmentation, you’ll need it enabled in Braze. Use the following template to contact your Braze CSM or the support team for access.

 Request event property segmentation

 Field | 
 Details | 

 Subject | 
 Request to Enable Event Property Segmentation for VWO Integration | 

 Body | 
 
 Hello Braze Team,

 We would like to enable event property segmentation for events sent from our VWO<>Braze integration. Here are the details:

 - Event Name: VWO

 - Event Properties: vwo_campaign_name, vwo_variation_name

 Please confirm once the properties have been enabled in our account.

 Thank you.
 | 

### Braze data points

The custom event sent from VWO to Braze—including any event properties enabled for segmentation—will log data points in your Braze instance.

### Considerations

Currently, this integration doesn’t support real-time sync of test data. There may be a delay of up to 15 minutes for test data to appear in Braze.

## Troubleshooting

If you’re not seeing VWO data in Braze:

- Right-click on the page, where your test campaign is running and select Inspect Element.
 
- Under the Network tab, search for Braze to filter the network calls for Braze.
 
- The network calls get populated as the page loads. You may reload the page to view the network calls.
 
- Select a network call to view further details.
 
- Go to the Request Payload section in the Payload tab, where you can find events: that has name: ce, indicating Custom Event.
 
- Expand 0: and data: to see n: “VWO” (name of the Custom Event) and p: {vwo_campaign_name: “”, vwo_variation_name: “”}. These indicate that the values are being pushed by VWO to Braze.

For additional support, contact your VWO customer success manager.

- 

New Stuff!
