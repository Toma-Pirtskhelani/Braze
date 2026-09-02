---
url: https://www.braze.com/docs/user_guide/get_started/braze_pilot
slug: docs__user_guide__get_started__braze_pilot
title: "Braze Pilot"
description: "Check out the different ways you can use Braze to launch messages from the Braze dashboard to your phone."
section: user_guide/get_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# Braze Pilot 

Braze Pilot is a mobile app that is designed to connect seamlessly with your Braze dashboard. This empowers you to launch campaigns and Canvases to the app, bringing Braze messages to life on your own phone. Braze Pilot includes a library of app simulations for fictional brands representing different industries, allowing you to experience how your messaging might look from your customers’ perspective.

## Section articles 

- 

 Getting Started with Braze Pilot

- 

 Data Dictionary

- 

 Deep Links

## Pilot app simulations

The core of Braze Pilot is its library of app simulations. Each app is a realistic simulation of an industry-specific fictional brand, instrumented to log a rich assortment of events and attributes that create endless opportunities for powering common Braze use cases.

- fitness
 
- ecommerce
 
- streaming

### Steppington

Steppington is a fitness app with workouts, exercise goals, and a Steppington+ premium service. It offers several places to demonstrate Content Cards, a section that can be revealed with feature flags, and a robust library of custom event logging that make it possible to illustrate many customer journeys for this industry.

### PantsLabyrinth

PantsLabyrinth is an eCommerce app that sells (you guessed it) pants! The PantsLabyrinth app includes full shopping cart checkout experience, an optional wishlist feature that can be enabled with a feature flag, and many opportunities for sly jokes with friends from the UK.

### MovieCanon

MovieCanon is a streaming service perfectly designed to illustrate common Braze use cases around content engagement.

## How Pilot connects with your Braze dashboard

The Braze SDK is a code package that collects data from your users once it’s integrated with your app or website. When you connect Pilot to your dashboard, you initialize this connection between the Pilot app on your phone and the Braze SDK, and establish a unique connection with your Braze instance by giving Pilot your API key identifier for your dashboard.

After Pilot connects to your Braze dashboard, the Braze SDK functions in the app just as it will once you integrate the SDK with your own app or website. This means that Braze will:

- Store data on your user activity in Pilot, including custom data specific to the fictional brands in the app.
 
- Automatically collect session data, device info, and push tokens.
 
- Power push notifications, in-app messages, and Content Card messaging channels that require SDK integration to function.

For more on the Braze SDK, check out Integration.

## User profiles in Braze

Every piece of data sent to Braze is stored in a user profile dedicated to a particular user of your app or website. Once you connect Pilot with your Braze dashboard, Braze will start logging data about you as the user of Pilot. There are two types of users that could be created for you through this connection: anonymous and identified.

### Anonymous

This connection status represents the experience of a guest of your app or website who hasn’t logged in yet. If you initialize Pilot as an anonymous user, Braze creates an anonymous user profile for you and logs data about your activity there. Anonymous users can still be targeted with campaigns, but you won’t be able to look up their user profile directly in your Braze dashboard.

### Identified

This connection status means Braze recognizes your user profile through a unique identifier assigned to you, known as an external identifier. You can search for this external identifier in the User Search page of your dashboard to locate your user profile, which stores all user attributes and events logged from Pilot based on your activity in the app. In the Braze dashboard, go to Audience > User Search, enter your Pilot external ID, and open the profile to inspect attributes and events.

### Connection type

To check what type of connection you have, check the connection status indicator at the top end of the Pilot app.

- anonymous user
 
- identified user
 
- not connected

Anonymous indicates you’re logging data as an anonymous user. The status area shows an Anonymous label (for example, a mask or incognito-style badge).

If you’re logging data as an identified user, the status area shows Identified user and your external ID.

Not connected indicates you haven’t yet initialized the Braze SDK connection with Pilot. The status area calls out that Pilot is not connected to your Braze workspace yet.

## Campaigns and Canvases

Campaigns and Canvases are how you send messages to your users.

- Campaigns are best for single messages sent to a specific audience segment across various channels.
 
- Canvases are advanced campaign workflows that allow you to automate and orchestrate personalized customer journeys across multiple channels. Within a Canvas, you can set up branching logic, delays, decision points, and conversion events to guide customers through a series of interactions. Canvases help ensure consistent and seamless communication across different touch points, increasing the chances of customer engagement and conversion.

## Supported messaging channels

Braze Pilot currently supports in-app messages, which appear in your app, delivering timely messaging while the user is actively engaging.

- 

New Stuff!
