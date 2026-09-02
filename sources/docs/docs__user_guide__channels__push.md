---
url: https://www.braze.com/docs/user_guide/channels/push
slug: docs__user_guide__channels__push
title: "Push"
description: "Send time-sensitive calls to action through mobile and web push notifications to re-engage users and drive action."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Push

Push notifications send time-sensitive calls to action to mobile and web devices and re-engage users who have not opened your app recently. They open directly to relevant content and demonstrate ongoing value from your product. This hub covers push integration, opt-in strategy, message types, best practices, and platform-specific settings for iOS, Android, and Web. Consider push primer messages before you request system permission. See the integration guides for iOS, Android, and Web to get started.

## Prerequisites

Before you start, make sure you have the following:

- Push integrated into your app or website. Work with your developers to set this up. For detailed steps, refer to the integration guides for iOS, Android, and Web.
 
- A push opt-in strategy. Users must grant push permission on their device. Consider using push primer messages to explain the value before prompting.

## Use cases

 Use case | 
 Explanation | 

 Initial onboarding | 
 Until users take the initial steps toward using your app (such as registering an account), their value is severely limited. Use push notifications to urge users to complete these steps so they can begin using your app in full. | 

 First purchases | 
 After users are comfortable using your app, you can use push notifications to help convert them into in-app purchasers. | 

 New features | 
 Push notifications can be effective in notifying disengaged users about new features that might attract them back to your app. | 

 Time-sensitive offers | 
 If you have a clock ticking on an offer, push is a great way to let your users know about it before it expires. These messages generally carry a high sense of urgency and are optimal for reminding recently-lapsed users about your app. For example, if your app is a game and you offer an in-game currency bonus for a daily play streak, alerting a user that their streak is at risk can be an effective push after they’ve reached a certain number of days. | 

## Push message regulations

Push reaches your customer’s device directly, so app and store policies restrict how you use it.

important

Your push messages must follow the Apple App Store Review Guidelines and Google Play policies. That includes rules on using push for ads, spam, promotions, and related topics.

 Policy source | 
 Summary | 

 Apple 3.2.2 | 
 Unacceptable uses include creating an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection. | 

 Apple 4.5.4 | 
 Push must not be required for the app to function and must not carry sensitive personal or confidential information. Don’t use push for promotions or direct marketing unless customers explicitly opt in via consent language in your app’s UI and can opt out in the app. | 

 Apple 4.10 | 
 You may not monetize built-in capabilities such as Push Notifications, the camera, or the gyroscope, or Apple services such as Apple Music or iCloud. | 

 Google Play — Unauthorized use or imitation of system functionality | 
 Apps must not mimic or interfere with system notifications. System-level notifications are only for integral app features (for example, an airline app notifying users of deals, or a game notifying users of in-game promotions). | 

## Frequently asked questions

### When does Braze record a successful Send for push?

Braze typically logs a Send once the message is dispatched from Braze toward Apple, Google, or your web push service. Delivered, opens, bounces, and uninstall signals are tracked separately and may arrive later. Use step- and campaign-level analytics together with push troubleshooting when Sends and downstream metrics look misaligned.

## Next steps

- Push setup
 
- Create a push message

- 

New Stuff!
