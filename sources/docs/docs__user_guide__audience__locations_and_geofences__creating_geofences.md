---
url: https://www.braze.com/docs/user_guide/audience/locations_and_geofences/creating_geofences
slug: docs__user_guide__audience__locations_and_geofences__creating_geofences
title: "Geofences"
description: "Learn how to set up location permissions, create a location permission primer, and build geofences for location-based campaigns."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Geofences

A geofence is a virtual geographic area, represented as latitude and longitude combined with a radius, forming a circle around a specific global position. Geofences can vary from the size of a building to the size of an entire city. You can use geofences to trigger campaigns in real-time as users enter and exit their borders, or send follow-up campaigns hours or days later.

tip

For a guided walkthrough, refer to the Braze Learning course Create a Geofence.

## How it works

Geofences are organized into geofence sets—a group of geofences that you can use to segment or engage users throughout the platform. Each geofence set can hold a maximum of 10,000 geofences. You can create or upload an unlimited number of geofences.

Users who enter or exit your geofences add a new layer of user data that you can use for segmentation and re-targeting.

Keep the following device limits in mind:

- Android apps may store up to 100 geofences locally at a time. Braze is configured to store only up to 20 geofences locally per app.
 
- iOS devices may monitor up to 20 geofences at a time per app. Braze monitors up to 20 locations if space is available.
 
- If the user is eligible to receive more than 20 geofences, Braze downloads the maximum number of locations based on proximity to the user at session start.
 
- For geofences to work correctly, ensure that your app is not using all available geofence spots.

The following table describes common geofence terms:

 Term | 
 Description | 

 Latitude and longitude | 
 The geographic center of the geofence. | 

 Radius | 
 The radius of the geofence in meters, measured from the geographic center. Set a minimum radius of 100 meters to 150 meters for all geofences. | 

 Cooldown | 
 Users receive geofence-triggered notifications after performing enter or exit transitions on individual geofences. After a transition occurs, there is a pre-defined period during which that user can’t perform the same transition on that individual geofence again. This “cooldown” is pre-defined by Braze and its main purpose is to prevent unnecessary network requests. | 

## Prerequisites

### SDK and platform requirements

Geofence-triggered campaigns are available on iOS and Android. To support geofences, the following is required:

- Braze geofences or location collection must be enabled.
 
- The user must grant “Always Allow” location access.

important

Braze location collection is disabled by default. To verify that it’s enabled on Android, confirm that com_braze_enable_location_collection is set to true in your braze.xml.

For platform-specific setup instructions, see Geofences in the developer guide.

### Location permissions

Before your geofences can function, users must grant your app permission to access their location. Understanding the different permission levels and their impact on geofencing is critical to building an effective location-based strategy.

## Understanding location permissions

Both iOS and Android offer multiple levels of location access. The permission level a user grants directly affects whether geofencing works and how accurate the location data is.

### Permission levels

- ios
 
- android

 Permission | 
 Description | 
 Geofencing support | 

 Allow Once | 
 Grants location access for a single session. The prompt reappears the next time the user opens the app. | 
 No. Background tracking is disabled, so the device only receives location updates when the app is open. | 

 Allow While Using the App | 
 Grants location access whenever the app is in the foreground. After this is granted, iOS may present a follow-up prompt asking the user to upgrade to “Always Allow”. | 
 Yes. iOS enables background location monitoring, including geofence transitions, for apps with this permission. | 

 Always Allow | 
 Grants continuous location access, including in the background and when the app is closed. | 
 Yes. This provides the most reliable geofence monitoring. | 

 Don’t Allow | 
 Denies all location access. | 
 No. | 

 Permission | 
 Description | 
 Geofencing support | 

 While Using the App | 
 Grants location access while the app is in the foreground. | 
 No. On Android, background location access is required for geofence monitoring. | 

 Always Allow | 
 Grants continuous location access, including in the background. On Android 10 and later, this requires a separate prompt after the initial “While Using the App” permission is granted. | 
 Yes. This is required for geofencing on Android. | 

 Don’t Allow | 
 Denies all location access. On Android 13 and later, if a user denies the location prompt twice, the OS blocks further in-app prompts. | 
 No. | 

### Precise versus approximate location

On iOS 14+ and Android 12+, users can choose between precise and approximate location.

 Setting | 
 Accuracy | 
 Impact on geofencing | 

 Precise location (on) | 
 Accuracy in the 5 meter to 50 meter range, using GPS, Wi-Fi, and cellular triangulation. | 
 Geofences function as expected. Recommended for all geofence-based use cases. | 

 Approximate location (off) | 
 Accuracy around 3 square kilometers (approximately 1 square mile). The device returns a general area rather than exact coordinates. | 
 Geofences don’t trigger reliably. The device can’t accurately determine whether a user is inside or outside a geofence boundary. | 

important

For geofencing to work reliably, users must enable precise location. Include this guidance in your location permission primer messaging so users understand why precise location matters.

## Setting up a location permission primer

A location permission primer is an in-app message that explains the value of sharing location data before the user sees the native OS permission prompt. Because the native location prompt can only be shown once (on iOS) or a limited number of times (on Android), priming users in advance increases opt-in rates.

### Step 1: Work with your development team

Because Braze in-app messages don’t include a built-in button action to invoke the native location permission prompt, your development team needs to handle location permissions on the device side. Before building the in-app message in Braze, coordinate with your development team to set up deep links that your in-app message can call. The specific implementation depends on your app’s architecture, but common approaches include:

- A deep link that triggers the native location permission prompt from within your app.
 
- A deep link that opens the app’s location settings page in the device’s OS settings, which is useful for re-prompting users who previously denied or limited their permissions.

For more information about deep links, see Deep linking to in-app content. For platform-specific guidance on location and geofence integration, see Geofences in the developer guide.

### Step 2: Build the location primer in-app message

Create an in-app message campaign that explains the value of location access. All in-app message types support this opt-in, including drag-and-drop.

- Go to Messaging > Campaigns, then select Create Campaign > In-App Message.
 
- Choose a message type and layout. A Modal or Full layout gives you more space to articulate the benefits.
 
- Write messaging that clearly explains why location access benefits the user. For example:

- “Enable location to get notified about deals near you.”
 
- “Turn on location so we can let you know when your order is ready for pickup at your nearest store.”

- Add a primary call-to-action button (such as Turn On Location) and set its on-click behavior to Deep Link into App, using the deep link your development team created to trigger the native location prompt.
 
- Add a secondary button (such as Not Now) that closes the message.

### Step 3: Target the right audience

For best results, show the location primer when users are engaged and likely to see value in sharing their location.

- Target users who haven’t granted location access yet. Work with your development team to determine the best way to track and segment users based on their location permission status.
 
- Time the primer after a high-value action, such as completing a purchase, saving a store as a favorite, or browsing nearby events. Users are more likely to opt in when they understand the benefit.
 
- Avoid showing the primer on first launch. Wait until users have experienced enough value from the app to want a more personalized experience.

### Step 4: Encourage the recommended permission level

Your primer messaging should encourage users to grant the permission level that enables geofencing:

- On iOS, encourage users to select Allow While Using the App at minimum. iOS may later prompt the user to upgrade to Always Allow on its own. You can also follow up with a separate campaign to explain why “Always Allow” provides the best experience.
 
- On Android, encourage users to grant Always Allow. On Android 10 and later, the user must first grant “While Using the App”, then grant “Always Allow” in a separate follow-up prompt. Guide them through both steps.

In both cases, remind users to keep Precise Location turned on for the best experience.

## Redirecting users to OS settings

If a user previously denied location access or selected a limited permission, you can’t trigger the native prompt again from within the app on most OS versions. Instead, direct them to update their permissions in device settings.

Use a deep link inside a custom in-app message to navigate the user to the app’s location settings page in the OS. Your development team can set up a deep link for this as part of your app’s location permission handling (refer to Step 1).

When building this in-app message, consider the following:

- When to show: Target users who have “While Using the App” permission when you need “Always Allow”, or users who previously denied location access.
 
- Messaging example: “To get the most out of location-based features, update your location settings to ‘Always Allow’. Tap to go to Settings.”

tip

You can trigger this in-app message at any point in the user journey—after a purchase, when browsing nearby content, or as part of a Canvas flow. Be selective when re-prompting: limit these campaigns to loyal or highly engaged users to avoid opt-in fatigue.

## Example location priming strategies

### “While Using the App” primer

A retail app displays a modal in-app message after a user saves a store as a favorite:

- Heading: “Get notified about in-store deals”
 
- Body: “Turn on location so we can send you exclusive offers when you’re near your favorite stores. Your location is only accessed when using the app.”
 
- CTA: Turn On Location deep links to the native location permission prompt
 
- Dismiss: Maybe Later closes the message

This approach is effective because the user has already expressed interest in a specific store, creating a natural context for the location permission request.

### “Always Allow” follow-up

After a user grants “While Using the App” permission, show a follow-up in-app message during the next session:

- Heading: “Never miss a nearby deal”
 
- Body: “Update your location settings to ‘Always’ so we can notify you about offers even when you’re not browsing the app. We’ll only send relevant alerts when you’re near participating locations.”
 
- CTA: Update Settings deep links to the app’s location settings page in the OS
 
- Dismiss: Keep Current Settings closes the message

This follow-up gives the user context for why upgrading to “Always Allow” provides additional value beyond the initial permission level.

## Manually create geofences

### Step 1: Create a geofence set

To create a geofence, create a geofence set first.

- Go to Audience > Locations in the Braze dashboard.
 
- Select Create Geofence Set.
 
- For Set name, enter a name for your geofence set.
 
- (Optional) Add tags to filter your set.

### Step 2: Add the geofences

Next, add geofences to your geofence set.

- Select Draw Geofence to click and drag the circle on the map. Repeat to add more geofences to your set as needed.
 
- (Optional) Select Edit and replace the geofence description with a name.
 
- (Optional) Select Show Advanced Settings, then use these settings to control how geofence analytics are recorded:

- Select Enable Analytics for Enter and Enable Analytics for Exit to log enter and exit activity in the USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED SQL table for reporting and analysis.
 
- Configure a cooldown period to set how many seconds must pass before the same user can trigger another enter or exit event for that geofence. If you don’t set a cooldown, the default is six hours.
 
- Use Android Notification Responsiveness to set the maximum delay, in seconds, that Android devices use when delivering enter or exit events to your app.

- Select Save Geofence Set to save.

tip

Create geofences with a radius of at least 200 meters for optimal functionality. For more information, refer to Geofence best practices.

## Bulk upload geofences

You can upload geofences in bulk as a GeoJSON object of type FeatureCollection. Each geofence is a Point geometry type in the feature collection. The properties for each feature require a radius key and an optional name key for each geofence.

To upload your JSON file, select More > Upload JSON.

When creating your geofences, consider the following details:

- The coordinates value in the GeoJSON is formatted as [Longitude, Latitude].
 
- The maximum geofence radius that may be uploaded is 10,000 meters (about 10 kilometers or 6.2 miles).

### Example

The following example shows the correct GeoJSON format for specifying two geofences: one for Braze headquarters in NYC, and one for the Statue of Liberty south of Manhattan.

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

```
 | 
```
{
 "type": "FeatureCollection",
 "features": [
 {
 "type": "Feature",
 "geometry": {
 "type": "Point",
 "coordinates": [-73.9853689, 40.7434683]
 },
 "properties": {
 "radius": 200,
 "name": "Braze HQ"
 }
 },
 {
 "type": "Feature",
 "geometry": {
 "type": "Point",
 "coordinates": [-74.044468, 40.689225]
 },
 "properties": {
 "radius": 100,
 "name": "Statue of Liberty"
 }
 }
 ]
}

```
 | 

## Using geofence events

After you configure your geofences, you can use them to enhance and enrich how you communicate with your users.

### Triggering campaigns and Canvases

To use geofence data as part of campaign and Canvas triggers, choose Action-Based Delivery for the delivery method. Next, add a trigger action of Trigger a Geofence. Finally, choose the geofence set and geofence transition event types for your message. You can also advance users through a Canvas using geofence events.

### Personalizing messages

To use geofence data to personalize a message, you can use the following Liquid personalization syntax:

- {{event_properties.${geofence_name}}}
 
- {{event_properties.${geofence_set_name}}}

## Updating geofence sets

The Braze SDK requests geofences only once per day on session start. If you make changes to the geofence sets after session start, you need to wait 24 hours from the time the sets are first pulled down to receive the updated set.

note

If the geofences aren’t loaded onto the device locally, the user can’t trigger the geofence even if they enter the area.

## Geofence best practices

### Geofence configuration

- Use a radius of 200 meters or more for reliable triggering.
 
- Avoid setting up geofences that overlap or are nested inside each other, as this can cause problems with triggering.
 
- A geofence can trigger an enter event only once every six hours. This cooldown period is enforced locally. If a user uninstalls the app or clears app data, all cooldowns reset.
 
- No more than 20 geofences in total can be stored on a device. If the user is eligible for more than 20, Braze downloads the closest locations based on proximity at session start.
 
- Braze sends only geofences within a 2,000 kilometer radius of the user to the device.

### Device requirements

- Your application’s users must grant location permissions, see the Location permissions section for more information.

note

Basic SDK integration enables location tracking only. Geofencing requires additional setup steps for both iOS and Android. For details, see Geofences in the developer guide.

You can also use geofences with Braze Technology Partners, such as Radar and Foursquare.

## Differences between geofences and location tracking

In Braze, geofences and location tracking serve different purposes:

   | 
 Location tracking | 
 Geofences | 

 Purpose | 
 Segment users based on where they were | 
 Trigger messaging when users enter or exit an area | 

 Typical use | 
 Most Recent Location and related filters | 
 Real-time campaigns on geofence enter or exit | 

 When location is evaluated | 
 Updated when the app is open (session start); reflects the user’s last known location | 
 Monitored by the OS when location permissions allow, including when the app is in the background or closed | 

- Location tracking: Collect and store each user’s most recent location on their profile. You use this data for backward-looking segmentation—for example, the Most Recent Location filter targets users based on where they last opened your app, not necessarily where they are in real time.
 
- Geofences: Define virtual boundaries around a latitude, longitude, and radius. When a user enters or exits a boundary, Braze can trigger actions such as sending a campaign. Geofences require additional SDK setup beyond basic location tracking.

Both features require users to grant location permissions. If a user opts out of location tracking, previously stored location data isn’t automatically removed from their profile, but new location data isn’t collected.

## Frequently asked questions

### How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user’s location, including Wi-Fi, GPS, and cellular towers.

Typical accuracy is in the 20 meter to 50 meter range, and best-case accuracy is in the 5 meter to 10 meter range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Create geofences with larger radii in rural locations.

Accuracy also depends on whether the user has precise location enabled. With approximate location only, accuracy drops to around 3 square kilometers, making geofences unreliable. For more information, see Precise versus approximate location.

### How do geofences affect battery life?

Braze geofencing uses the native geofence system service on iOS and Android. It’s tuned to intelligently trade off accuracy and power, saving battery life and improving performance as the underlying service improves.

### When are geofences active?

Braze geofences work at all hours of the day, even when your app is closed. They become active as soon as they are defined and uploaded to the Braze dashboard. However, geofences can’t function if a user has disabled location tracking.

For geofences to work, users must have location services enabled on their device and must have granted your app the required location permission level. For more information, see Understanding location permissions.

### Is geofence data stored in user profiles?

No, Braze doesn’t store geofence data on user profiles. Geofences are monitored by Apple and Google location services, and Braze only gets notified when a user triggers a geofence. At that point, Braze processes any associated trigger campaigns.

### Can I set up a geofence within a geofence?

As a best practice, avoid setting up geofences that overlap with each other, as this may cause issues with triggering notifications.

### What if a user denies location access?

Your development team can set up a deep link that opens the app’s location settings page in the OS, where users can update their permissions. You can use this deep link inside a custom in-app message at any point in the user journey. Be selective about when you show this message—target users who are engaged or who have performed a high-value action to increase the chance of an opt-in. For more information, see Redirecting users to OS settings.

- 

New Stuff!
