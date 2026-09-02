---
url: https://www.braze.com/docs/partners/data_and_analytics/leads_capture/outgrow
slug: docs__partners__data_and_analytics__leads_capture__outgrow
title: "Outgrow"
description: "This article provides a comprehensive guide on configuring a native integration between Outgrow and Braze for enhanced user data synchronization and personalized campaigns."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Outgrow

Outgrow is an interactive content platform that empowers you to create quizzes, calculators, surveys, and other types of engaging content to collect user data and insights. The Braze and Outgrow integration lets you automatically transfer user data from Outgrow into Braze, enabling highly personalized and targeted campaigns.

When you use the Braze and Outgrow integration for interactive content, the benefits you get include:

- Enhanced personalization: Collect data from Outgrow quizzes, surveys, and calculators that can be mapped to custom attributes in Braze. This data allows for precise segmentation and personalized campaigns.
 
- Real-time data sync: Receive Outgrow data in Braze in real-time, allowing you to act on user insights immediately. This allows for timely follow-ups or personalized messages based on users’ most recent interactions.
 
- Streamlined data management: Automate data transfer between Outgrow and Braze, eliminating manual data exports and imports, reducing data discrepancies, and saving time.
 
- Improved user experience: Leverage user insights to create more relevant experiences, leading to higher satisfaction, retention, and lifetime value.
 
- Flexible targeting and segmentation: Refine segmentation in Braze using Outgrow data, allowing you to target users based on specific interactions (such as quiz scores or survey responses) to create campaigns that resonate with your users.

## Prerequisites

Before setting up the Outgrow and Braze integration, confirm you have the following:

 Requirement | 
 Description | 

 Outgrow account | 
 A registered Outgrow account to configure and manage interactive content and data transfer settings | 

 Braze account | 
 A Braze account with access to REST API credentials | 

 API key | 
 An API key from Braze with the users.track permission to enable user data transfer | 

 Custom attributes in Braze | 
 Custom attributes set up in Braze to capture Outgrow responses (such as quiz scores, segments, and others) | 

## Integration

Follow these steps to configure the Braze and Outgrow integration:

### Step 1: Generate Braze API key

- In your Braze account, go to Developer Console > API Settings.
 
- Select Create New API Key.
 
- Name your API key, turn on the users.track permission, and save the API key.

### Step 2: Configure the Braze integration in Outgrow

- Log into your Outgrow account.
 
- In the dashboard, go to Integrations.
 
- From the list of available integrations, select Braze.
 
- Enter your Braze API Key and REST API Endpoint URL:

- API Key: Enter the API key that was generated in Braze
 
- REST Endpoint URL: Enter the endpoint for your Braze instance (for example, https://rest.iad-01.braze.com)

- Select Save to turn on the integration.

### Step 3: Map Outgrow data to Braze attributes

In Outgrow, you can map responses from interactive content (such as quiz results, custom segments, or engagement scores) to Braze custom attributes.

- In the Outgrow Integration Settings for Braze, define which Outgrow responses to map to Braze attributes.
 
- Make sure that each selected response aligns with a custom attribute in Braze. For example:

- Quiz score maps to outgrow_quiz_score.
 
- Custom segment maps to outgrow_custom_segment.

- Save your mapping settings.

### Step 4: Test the integration

After configuring the integration, run a test to confirm data is properly transferring from Outgrow to Braze.

- Publish an Outgrow experience (such as a quiz or calculator) and complete it as a test user.
 
- In your Braze account, go to the User Profile section and check for updated attributes (such as outgrow_quiz_score or outgrow_custom_segment).
 
- Verify that the data is correctly populated under the appropriate custom attributes.

## Using Outgrow data in Braze for segmentation and targeting

### Creating segments in Braze with Outgrow data

With the integration, you can create Braze segments based on custom attributes populated from Outgrow responses.

- In Braze, go to Engagement > Segments and select Create New Segment.
 
- Name your segment and set filters based on Outgrow data. For example:

- Filter by outgrow_quiz_score to target users whose score is greater than a specific threshold.
 
- Filter by outgrow_custom_segment to target users who belong to a particular Outgrow-defined segment.

- Save your segment for use in campaigns and Canvases.

### Launching campaigns with Outgrow-defined segments

You can use the custom segments created from Outgrow data to personalize your Braze campaigns and target users based on their responses to interactive content. To do so and create a more personalized user experience, follow these steps:

- In Braze, go to Engagement > Campaigns.
 
- Select Create Campaign and choose your campaign type (email, push, in-app message, or others).
 
- In the audience targeting step, select the segment created from Outgrow attributes (such as users with specific quiz scores or segments).
 
- Customize your campaign content and settings, and then launch.

## Troubleshooting common issues

 Issue | 
 Solution | 

 Data isn’t transferring to Braze | 
 Verify that the API key and endpoint URL are correct in your Outgrow integration settings. Make sure the API key has the users.track permission turned on. | 

 Incorrect data mapping | 
 Make sure that each mapped Outgrow response corresponds to a valid Braze custom attribute and that the attribute names match exactly. | 

 Segment not filtering correctly | 
 Make sure that custom attributes in Braze are properly set up and receiving data. Re-check your segment filter logic. | 

## Additional considerations

- Data privacy: Comply with data privacy regulations (such as GDPR and CCPA) when transferring user data between platforms.
 
- Rate limits: Outgrow data is sent to Braze in real-time, but Braze API rate limits may apply for large volumes of data. Plan accordingly for high-traffic experiences.
 
- Custom attribute configuration: Verify that the Braze custom attributes used in this integration are correctly configured to capture data sent from Outgrow.

For additional assistance, refer to Outgrow documentation or contact Outgrow Support.

- 

New Stuff!
