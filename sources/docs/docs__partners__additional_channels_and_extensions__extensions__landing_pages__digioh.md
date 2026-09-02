---
url: https://www.braze.com/docs/partners/additional_channels_and_extensions/extensions/landing_pages/digioh
slug: docs__partners__additional_channels_and_extensions__extensions__landing_pages__digioh
title: "Digioh"
description: "This reference article outlines the partnership between Braze and Digioh, a survey platform for creating pop-ups, forms, surveys, and communication preference centers that drive engagement..."
section: partners/additional_channels_and_extensions
fetched: 2026-09-02
evidence: company-own (technical)
---
# Digioh

Digioh supports list growth, first-party data capture, and use of that data in Braze campaigns.

This integration is maintained by Digioh.

## About the integration

The Braze and Digioh integration lets you use a drag-and-drop builder to create on-brand forms, pop-ups, preference centers, landing pages, and surveys that connect you with your customers. Digioh assists with integration setup and can build, design, and launch your first campaign.

## Prerequisites

 Requirement | 
 Description | 

 Digioh account | 
 A Digioh account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze API /users/track/ endpoint | 
 Your REST endpoint URL with the /users/track/ details appended to it. Your endpoint will depend on the Braze URL for your instance.

For example, if your REST API endpoint is https://rest.iad-01.braze.com your /users/track/ endpoint will be https://rest.iad-01.braze.com/users/track/. | 

## Integration

To integrate Digioh, you must first configure the Braze connector. When completed, you will need to apply the integration to a lightbox (widget). Visit Digioh to read more about integration basics.

### Step 1: Create Digioh integration

In Digioh, click the Integrations tab and then the New Integration button. Select Braze from the Integration dropdown and name the integration.

Next, enter the Braze REST API key and your Braze API /users/track/ endpoint.

Lastly, use the map fields section to map additional custom fields beyond email and name. The following code snippet shows an example payload. When completed, select Create Integration.

```

1
2
3
4
5
6
7
8

```
 | 
```
{
 "attributes" : [
 {
 "external_id": "[EMAIL_MD5]",
 "email" : "[EMAIL]"
 }
 ]
}

```
 | 

### Step 2: Create a Digioh lightbox

Use the Digioh design editor to build a lightbox (widget). 

Interested in seeing a gallery of ways to leverage the design editor? Visit the Digioh theme gallery.

### Step 3: Apply integration

To apply this integration to a Digioh lightbox, navigate to the Boxes page and select Add or Edit link in the Integrations column. This can also be added from the Integration section of the editor.

Here, select Add Integration, choose your desired integration, and Save. Digioh will now pass your captured leads to Braze in real-time.

- 

New Stuff!
