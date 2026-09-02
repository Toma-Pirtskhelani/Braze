---
url: https://www.braze.com/docs/user_guide/channels/push/create_a_push_message/push_action_buttons
slug: docs__user_guide__channels__push__create_a_push_message__push_action_buttons
title: "Push action buttons"
description: "This reference article covers what push action buttons are and the difference across iOS and Android platforms."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Push action buttons

Push action buttons allow you to set content and actions for buttons when using Braze iOS and Android push notifications. With action buttons, your users can interact directly with your app from a notification without needing to click into an app experience.

## Creating action buttons

Each interactive button can link to a web page or a deep link or open the app.

- For standard push campaigns, you can specify your push action buttons in the On-Click Behavior section of the push message composer in the dashboard.
 
- For multiple platform push campaigns, action buttons can be configured separately for each platform under the Settings tab.

- ios
 
- android

### iOS

To use action buttons in your iOS push messages, do the following:

- Turn on action buttons in the Compose tab
 
- Select your iOS Notification Category from the following available button combinations:

- Accept / Decline
 
- Yes / No
 
- Confirm / Cancel
 
- More
 
- Pre-registered custom iOS Category

note

Due to iOS’s handling of buttons, you need to perform additional integration steps when setting up push action buttons, which are outlined in our developer documentation. In particular, you need to either configure iOS Categories or select from certain default button options. For Android integrations, these buttons will work automatically.

Preset pairs such as Yes / No map the second button to a dismissive (CLOSE) action by default, so it doesn’t open the app the same way as the first button. Direct Opens doesn’t include that kind of tap, but Push Notification Open data in Currents or Snowflake may still log it with button_action_type and button_string. For more information, see Push action buttons and reporting.

### Android

To use action buttons in your Android push messages, do the following:

- Turn on action buttons in the Compose tab
 
- Select Add Button and specify your button text and On-Click Behavior. You can select from the following available actions:

- Open App
 
- Redirect to Web URL
 
- Deep Link Into Application

You can add up to three buttons in your push.

#### Android character limits

Unlike iOS buttons, which are stacked, Android buttons are displayed side-by-side in a row. This means that the more buttons you add (up to three), the less space you have for button copy.

The following table outlines how many characters you can add before your button copy is truncated, depending on how many buttons you have:

 Number of Buttons | 
 Maximum characters per button | 

 1 | 
 46 characters | 

 2 | 
 20 characters | 

 3 | 
 11 characters | 

- 

New Stuff!
