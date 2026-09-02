---
url: https://www.braze.com/docs/user_guide/channels/in_app_messages/best_practices/ios_app_rating_prompt
slug: docs__user_guide__channels__in_app_messages__best_practices__ios_app_rating_prompt
title: "In-app rating prompt for iOS"
description: "This article describes approaches and implications for using Braze to ask users to review your app."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# In-app rating prompt for iOS

This article describes approaches and implications for using Braze to ask users to review your app. For tips on how to make an effective app rating campaign, check out The Do’s and Don’ts of Customer App Ratings.

Apple offers a native prompt, introduced with iOS 10.3, that lets users rate apps from within the app itself. If you want to request app ratings from users using an in-app message on iOS, you must use the native prompt, as Apple disallows custom review prompts (see App Store Review Guidelines, section 5.6.1).

Per Apple guidelines, app review prompts can be displayed to a user up to three times a year, so any app review campaigns should take advantage of rate limiting. Users can also opt out of seeing app review prompts entirely in their app settings. For more on App Store ratings, refer to Apple’s article on Ratings, Reviews, and Responses.

## Using Braze to ask users for app reviews

While Apple requires you to use the native prompt, you can still take advantage of Braze campaigns to ask users to rate and review your app at the right moment. There are two main approaches you can take.

### Approach 1: Deep linking to the App Store

With this approach, you want to encourage users to visit the App Store to add a review. To do so, create an in-app message campaign that deep links to the App Store.

### Approach 2: Soft priming

If you don’t want users to leave your app, you can first prime users with a separate in-app message. Priming is a way of asking users for permission before you send them the native App Store review prompt. To do so, create an in-app message campaign and add a custom deep link that calls the requestReview method when clicked.

For detailed steps, refer to Custom App Store review prompt.

Users will submit a rating through the native App Store review prompt, and can write and submit a review without leaving the app.

### Considerations

As an alternative to soft priming, you could also display the iOS app rating prompt directly without any Braze soft primer message displayed before. The advantage of this is if the user is opted-out of app review prompts, there wouldn’t be the suboptimal user experience of trying to rate the application but no prompt appearing to do so.

important

Do not create custom HTML in-app messages that mimic a native iOS app rating prompt, as this violates Apple’s guidelines.

- 

New Stuff!
