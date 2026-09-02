---
url: https://www.braze.com/docs/partners/message_personalization/location/infillion
slug: docs__partners__message_personalization__location__infillion
title: "Infillion"
description: "This reference article outlines the partnership between Braze and Infillion, which enables you to perfect your marketing relevance using location data."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Infillion

Infillion enables you to perfect your marketing relevance using location data. Their location SDK paired with geofencing software and beacons power relevant, personalized, proximity-aware mobile experiences.

Combine your beacon or geofence support with Braze targeting and messaging features to learn more about your user’s physical actions and message them accordingly. This partnership integration opens up an array of use cases for:

- Marketing: Send contextually relevant messaging and build experiential consumer journeys.
 
- Competitive Analysis: Set up triggers around competitive locations to understand consumer trends and patterns.
 
- Audience Insights: Understand your users’ visitation behaviors and further segment based on those learnings.

note

This integration works the same for Infillion beacons and Infillion geofence solutions.

## Prerequisites

 Requirement | 
 Description | 

 Infillion manager account | 
 A Infillion manager account is required to take advantage of this partnership. | 

 Infillion Location SDK | 
 The Infillion Location SDK powers macro and micro location-based mobile experiences using proximity beacons and geofences that allow you to communicate more effectively with your app users. You must have the SDK implemented, and geofences (or beacons) set up. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

## SDK integration

To integrate Braze and Infillion, you must implement the Infillion Location SDK and create a Infillion manager account. The following integrations for Android, FireOS, and iOS will create a unique custom event for each new place a user enters, these events can then be used for triggering and retargeting in your campaigns and Canvases.

If you anticipate creating more than 50 places, we recommend creating a generic Places Entered custom event and adding the place name as an event property.

- Integrate the Infillion SDK for Android and iOS into your app by following the instructions in the Infillion documentation.
 
- Use Infillion’s place REST API to get user places.
 
- Link your Infillion account to Braze by entering the Braze REST API key.
 
- Set up custom events in the Braze SDK. You can integrate Infillion with Braze for Android and FireOS and iOS.
 
- Log properties for these events (Place Name, Dwell Time).
 
- Use these properties and events for triggering campaigns and Canvases in Braze.

- 

New Stuff!
