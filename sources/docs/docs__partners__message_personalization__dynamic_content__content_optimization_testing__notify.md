---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/content_optimization_testing/notify
slug: docs__partners__message_personalization__dynamic_content__content_optimization_testing__notify
title: "Notify"
description: "This reference article outlines the partnership between Braze and Notify, a real-time, omnichannel personalization solution that offers personalization across the customer lifecycle."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Notify

Notify is an AI-driven software solution that seamlessly integrates with customer relationship management tools to enhance marketing strategies and facilitate engagement across multiple channels.

The Braze and Notify integration empowers marketers to effectively drive engagement across various platforms. Instead of relying on traditional marketing methods, a Braze API-triggered campaign can use Notify’s capabilities to deliver personalized messaging through multiple channels, including email, SMS, push notifications, and more.

## Prerequisites

Before you start, you’ll need the following:

 Requirement | 
 Description | 

 Braze REST API key | 
 A Braze REST API key with users.export.segment and campaigns.trigger.send permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 CNAME configuration | 
 A subdomain must be created for the tracking pixel used in the email for Notify to track user engagement with messaging to further inform the model. Share the subdomain URL with Notify after it’s created. | 

 Database opt-in export | 
 Send the campaign and purchase data from the past year (12 months) to Notify. ​This export will be used to train Notify predictive model. 

 Fields: 

 Email: A SHA256 hash of the email, converted to lowercase and with any leading or trailing spaces removed.

Segment: The segment information defining the level of activity (active or inactive).

Sub-segment: Any other relevant activity information such as purchase activity level. | 

## Integration

### Step 1: Create your campaign

Create an API triggered campaign in Braze. Then, share the campaign api_identifier with Notify.

### Step 2: Create your segment in Braze

Next, create the segment of users that they would like to target with the campaign created in Step 1. Then, share the segment ID with Notify.

### Step 3: Fetch your segment

Then, Notify will export the users in the segment attached to the campaign.

### Step 4: Notify triggers the campaign

Using the /campaigns/trigger/send endpoint, Notify’s AI triggers the Braze campaign created in Step 1 to send to users at the time they deem most likely to engage.

- 

New Stuff!
