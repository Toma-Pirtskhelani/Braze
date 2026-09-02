---
url: https://www.braze.com/docs/partners/message_personalization/location/radar
slug: docs__partners__message_personalization__location__radar
title: "Radar"
description: "This reference article outlines the partnership between Braze and Radar, a geofencing platform, to add location context and tracking to your iOS and Android apps...."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Radar

Radar is the leading geofencing and location tracking platform. The Radar platform has three core products: Geofences, Trip Tracking, and Geo APIs. Combining the Braze industry-leading engagement platform and Radar’s industry-leading geofencing capabilities allows you to drive revenue and loyalty through a wide range of location-based product and service experiences. These include pickup and delivery tracking, location-triggered notifications, contextual personalization, location verification, store locators, address autocomplete, and more.

This integration is maintained by Radar.

## About the integration

The Braze and Radar integration allows you to access sophisticated location-based campaign triggers and user profile enrichment with rich, first-party location data. When Radar geofence or trip tracking events are generated, custom events and user attributes are sent to Braze in real-time. These events and attributes can then be used to trigger location-based campaigns, power last-mile pickup and delivery operations, monitor fleet and shipping logistics, or build user segments based on location patterns.

Additionally, Radar Geo APIs can be used to enrich or personalize your marketing campaigns through Connected Content.

## Prerequisites

 Requirement | 
 Description | 

 Radar account | 
 A Radar account is required to take advantage of this partnership. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 App identifier | 
 Your app identifier can be found can be found within the Braze dashboard from Settings > API Keys. | 

 iOS API key
Android API key | 
 These API keys can be found within the Braze dashboard from Settings > App Settings. | 

## Integration

To map data between the Braze and Radar SDKs, you must set the same user IDs or user aliases in both systems. This can be done using the changeUser() method in the Braze SDK and the setUserId() method in the Radar SDK.

To enable the integration:

- In Radar on the Integrations page, locate Braze.
 
- Set Enabled to Yes.
 
- Paste in your app identifier and API keys.

note

You can set separate API keys for test and live environments.

- Select your Braze endpoint.
 
- Input any event or event attribute filtering to ensure only relevant data is sent to Braze for engagement marketing. Whenever Radar events are generated, Radar will send custom events and user attributes to Braze. Events from iOS devices will be sent using your iOS API keys; events and user attributes from Android devices will be sent using your Android API keys.

note

By default, Radar userId maps to Braze external_id for logged in users. However, you can track logged out users or specify custom mappings by setting Radar metadata.brazeAlias or metadata.brazeExternalId. If you set metadata.brazeAlias, you must also add a matching alias in Braze with label radarAlias.

## Event and attribute-based use cases

You can use custom events and user attributes to build location-based segments or trigger location-based campaigns.

### Trigger a store arrival notification for curbside pickup

Send a push notification to the user with arrival instructions as they arrive at your store for a curbside pickup.

### Build an audience segment of recent store visitors

For example, target any users who have visited your store within the past 7 days, whether they made a purchase or not.

## Connected Content

The following example shows how to run a promotion to drive nearby users in-store with a digital offer.

To get started, you’ll need to have your Radar publishable API key on hand to use within your request URLs.

Next, within a connected_content tag, make a GET request to the Search Places API. The search places API returns nearby locations based on Radar Places: a database of locations for places, chains, and categories that provides a comprehensive view of the world.

The following code snippet is an example of what Radar will return as a JSON object from the API call:

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46

```
 | 
```
{
 "meta": {
 "code": 200
 },
 "places": [
 {
 "_id": "5dc9b0fd2004860034bf2b06",
 "name": "Target",
 "location": {
 "type": "Point",
 "coordinates": [
 -74.42653983613333,
 40.548302893822985
 ]
 },
 "categories": [
 "shopping-retail",
 "department-store"
 ],
 "chain": {
 "slug": "target",
 "name": "Target",
 "domain": "target.com"
 }
 },
 {
 "_id": "5dc9b3d82004860034bfec54",
 "name": "Walmart",
 "location": {
 "type": "Point",
 "coordinates": [
 -74.44121885326864,
 40.554603296187224
 ]
 },
 "categories": [
 "shopping-retail"
 ],
 "chain": {
 "slug": "walmart",
 "name": "Walmart",
 "domain": "walmart.com"
 }
 }
 ]
}

```
 | 

To construct the Connected Content targeted and personalized Braze message, you can use the Braze most_recent_location attribute as an input for the near parameter in the API request’s URL. The most_recent_location attribute is collected via the Radar event integration or directly through the Braze SDK.

In the following example, the Radar chain filtering is applied for Target and Walmart locations, and the search radius for nearby locations is set to 2 km.

```

1

```
 | 
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}

```
 | 

As you can see from the connect_content tag, the JSON object is stored into the local variable nearbyplaces by adding :save nearbyplaces after the URL.
You can test what the output should be by referencing {{nearbyplaces.places}}.

Bringing our use-case together, here is what the syntax of the campaign would look like. The following code iterates through the nearbyplaces.places object, extracting unique values and concatenating them with proper human-readable delimiters for the message.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30

```
 | 
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and " | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!

```
 | 

tip

Visit Radar documentation for all the Radar APIs that can be used in Connected Content.

- 

New Stuff!
