---
url: https://www.braze.com/docs/developer_guide/changelogs
slug: docs__developer_guide__changelogs
title: "Braze SDK changelogs"
description: "This reference page includes the changelogs for each Braze SDK and a link to the changelog in their public GitHub repository."
section: developer_guide/changelogs
fetched: 2026-09-02
evidence: company-own (technical)
---
# Braze SDK changelogs

This reference page includes the changelogs for each Braze SDK and a link to the changelog in their public GitHub repository. For the full list of resources, see References, Repositories, and Sample Apps.

- web
 
- android
 
- swift
 
- cordova
 
- flutter
 
- react native
 
- roku
 
- unity
 
- .net maui (xamarin)

tip

You can also find a copy of the Web Braze SDK changelog on GitHub.

## 6.11.0

##### Added

- Added braze.registerPush(), which performs the same push registration steps as braze.requestPushPermission() but never prompts the user for permission. It no-ops if push permission has not already been granted.

##### Fixed

- Fixed an issue where some SDK data could remain in storage after calling braze.logout().
 
- Fixed a bug where in-app message click events could be logged twice on iOS under certain circumstances.
 
- Fixed a bug where in-app message impression events could be logged twice under certain circumstances.

## 6.10.2

##### Fixed

- Fixed a scenario where rate-limiting would not work as intended for the push unregistration endpoint.

## 6.10.1

##### Fixed

- Fixed an issue where subscribing to Banner or Content Card updates after a session had already started could trigger redundant refresh requests.

## 6.10.0

##### Added

- Added braze.logout(), which unregisters push for the current browser and, on success, wipes locally stored SDK data and disables the SDK.

##### Fixed

- Fixed an issue where unregisterPush() invoked the errorCallback instead of the successCallback when push notifications are not supported in the browser.

## 6.9.0

##### Added

- Added braze.dismissBanner(), which can be used to programmatically dismiss a banner and log a dismissal event.
 
- Added Banner.subscribeToDismissedEvent(), which can be used to subscribe to dismissal events for a Banner.
 
- Added optional subtotal_value, tax, and shipping fields on the ecommerce.order_placed, ecommerce.cart_updated, and ecommerce.checkout_started eCommerce events.

##### Fixed

- Fixed an issue where the optional type field for the ecommerce.product_viewed eCommerce event was on the metadata object instead of the root object. The metadata object still accepts the type field, but integrators will need to move it to the root object in order for back-in-stock notifications to work properly.
 
- Fixed an issue where validation for the discounts field on the ecommerce.order_placed eCommerce event allowed non-array values.
 
- Improved crawler bot detection.

## 6.8.0

##### Added

- Added braze.logEcommerceEvent() to log eCommerce lifecycle events such as product viewed, cart updated, checkout started, and order placed.

##### Fixed

- Fixed an issue where a new Banner impression would not be logged for a placement ID if the underlying Banner changed mid-session.

## 6.7.1

##### Fixed

- Fixed an issue where Braze pushes were not displayed properly.

## 6.7.0 - DEPRECATED

##### Added

- Added brazeBridge.closeMessage() support for Banners. Calling this method will remove the Banner from the page and log a dismissal event.
 
- braze.requestBannersRefresh() no longer requires the allowUserSuppliedJavascript initialization option to be enabled.

##### Fixed

- Fixed an issue with the CDN integration on Safari 26+ that could cause messaging sync requests to fail in certain scenarios.
 
- Fixed an issue where the Braze SDK would attempt to display push notifications sent from other push providers

## 6.6.0

##### Added

- Added a cookieExpiryInDays initialization option to configure cookie duration from the default of 400 days.

## 6.5.0

##### Added

- Added the Banner.html property to support manually injecting HTML for cases where insertBanner is not appropriate.

##### Fixed

- Improved request retry timing to prefer server-configurable values for resiliency and consistency with other Braze SDKs

## 6.4.0

##### Added

- Added methods braze.logBannerImpressions() and braze.logBannerClick() to allow integrators to manually log both the banner impression and click events. These methods should only be called if you’re bypassing insertBanner and building custom UI for banners similar to other channels.

##### Fixed

- Fixed an issue where In-App Messages for the previous user were still displayed after changing users.

## 6.3.1

##### Fixed

- Fixed an issue where banner impressions were not cleared from local storage when a new session was opened.

## 6.3.0

##### Added

- Exposed NotificationSubscriptionTypes in brazeBridge.
 
- Added support for detection of ChatGPT Atlas browser.
 
- Improved crawler bot detection.

## 6.2.0

##### Added

- Updated platform detection for the Coolita and WhaleTV Smart TV platforms, which are now classified as Other Smart TV.

## 6.1.0

##### Added

- Added support for Banner properties.

##### Changed

- The default client-side rate limiting value for Banners refresh has been increased. For more information on SDK rate limiting, please refer to the Braze Developer Guide

##### Fixed

- Fixed an issue where Banner serialization keys were inconsistent between SDK versions, which could cause Banners to display incorrectly until the first Banners refresh after a version upgrade.
 
- Fixed an issue where PetalBot and Meta web crawlers were not properly detected.

## 6.0.0

##### ⚠️ Breaking

- Removed the Banner.html property, logBannerClick, and logBannerImpressions methods. Instead, use insertBanner which automatically handles impression and click tracking.
 
- Removed support for the legacy News Feed feature.
This includes removal of the Feed class, and the following associated methods:

- destroyFeed()
 
- getCachedFeed()
 
- logFeedDisplayed()
 
- requestFeedRefresh()
 
- showFeed()
 
- subscribeToFeedUpdates()
 
- toggleFeed()
 
- logCardClick() (replaced by logContentCardClick())
 
- logCardImpressions() (replaced by logContentCardImpressions())

- The created and categories fields that were used by legacy News Feed cards have been removed from Card subclasses.
 
- The linkText field was also removed from the ImageOnly Card subclass and its constructor.
 
- Clarified definitions and updated types to note that certain SDK methods explicitly return undefined when the SDK is not initialized, aligning the typings with actual runtime behavior. This could introduce new TypeScript errors in projects that relied on the previous (incomplete) typings.
 
- The images of In-App Messages with cropType of CENTER_CROP (e.g. FullScreenMessage by default) are now rendered via an <img> tag instead of <span> for improved accessibility. This may break existing CSS customizations for the .ab-center-cropped-img class or its children.

##### Added

- Added imageAltText and language fields to the following classes:

- Cards: CaptionedImage, ImageOnly, and [ClassicCard]
 
- In-App Messages: ModalMessage, FullScreenMessage, and SlideUpMessage

- When available, the default UI will use these fields to set the alternate text of images and the lang attribute, respectively, of In-App Messages and Cards.
 
- Improved the accessibility of In-App Messages and Content Cards when displayed by the default UI.

##### Changed

- Any new session subscriptions now immediately invoke the callback if a new session has already started.

##### Fixed

- Subscription methods now correctly trigger refreshes when openSession() is called, even if changeUser() was called first.
 
- Fixed an issue where Banners could display with a small amount of whitespace at the bottom.
 
- Fixed an issue where the messageExtras field was missing from the type definitions of InAppMessage classes.

## 5.9.1

##### Fixed

- Fixed an issue where rate limit state persisted across users and sessions causing requests to be incorrectly rate limited at session start.

## 5.9.0

##### Added

- Added brazeBridge.setBannerHeight() to allow Banners to resize dynamically.

##### Fixed

- Fixed an edge case with retry logic for Feature Flags, Content Cards and Banners network requests.

## 5.8.1

##### Fixed

- Fixed an issue with the npm version of the Web SDK that prevented Banner clicks from being logged.

## 5.8.0

##### Changed

- The insertBanner method now accepts a null or undefined banner argument.
 
- requestBannersRefresh now waits for the initial response from the backend and tries again if Banners are enabled.

##### Fixed

- Fixed a race condition causing “not enabled” messages to be logged for Banners and Feature Flags methods on the user’s first session.

## 5.7.0

##### Added

- Added a method User.setLineId used to set the user’s LINE User ID.

##### Fixed

- Fixed an issue where the chevron icon pointed in the wrong direction on SlideUp in-app messages when using RTL languages.

##### Changed

- The SDK now respects the retry-after header returned by the Braze platform when determining how long to wait before retrying a request.

## 5.6.1

##### Fixed

- Fixed an issue where the Tizen operating system was not accurately reported in device properties.

## 5.6.0

##### Added

- Added support for the Banners campaign type.

##### Fixed

- Fixed an issue where the SDK could erroneously request a triggers refresh even if no session is started.
 
- Fixed an issue where ControlMessage instances would allow multiple impressions.

## 5.5.0

##### Changed

- The SDK now rate limits Content Cards impressions to correspond to expected human behavior.

## 5.4.0

##### Added

- Added support for right-to-left languages to the built-in UI for In-App Messages and Content Cards.
 
- Introduced a new initialization option serviceWorkerScope that can be used to override the default scope of the service worker.
 
- Added a method braze.isInitialized() that returns whether the SDK has been initialized.
 
- Added a new custom event named braze.initialized that is dispatched on the window object when the Braze initialization completes.

## 5.3.2

##### Fixed

- Fixed a regression introduced in 5.2.0 that could cause HTML In-App Messages to render incorrectly when an external script is loaded synchronously.

## 5.3.1

##### Fixed

- Fixed an issue where a custom serviceWorkerLocation was not used when calling unregisterPush.

## 5.3.0

##### Added

- Added the following methods to the FeatureFlag class to support the upcoming expansion of feature flag property types:

- getJsonProperty()
 
- getImageProperty()
 
- getTimestampProperty()

##### Fixed

- Fixed an issue where e.preventDefault() could be called on events that were not cancelable.

## 5.2.0

##### Added

- Added a deviceId initialization option. This can be used to set device ID of the user that would be used after initialization.
 
- Added support for the message_extras liquid tag for in-app messages.

##### Changed

- The SDK will now persist and send the user’s alias in all backend requests if it has been set, until the user is identified via an external ID. This alias will no longer be sent in requests once the user is identified and is not compatible with SDK authentication.
 
- The SDK will now check for existing permissions before requesting push permissions.

##### Fixed

- Fixed an issue where unregisterPush() failed to invoke the successCallback() function in some cases where the user has already unsubscribed to push.
 
- Fixed an issue where characters | and : were not supported in the userId.
 
- Fixed an issue where HTML In-App Messages that used module script tags were not supported.

## 5.1.1

##### Fixed

- Fixed an issue where content cards sync request count persisted across users causing requests to be incorrectly rate limited.

## 5.1.0

##### Changed

- The subscribeToFeatureFlagsUpdates() callback will be triggered first with cached feature flags only if this cache is from the current session.

##### Fixed

- Fixed an issue where in-app messages failed to render a transparent background when using color-scheme.
 
- Fixed an issue where impressions for a given feature flag ID were limited to once-per-user instead of once-per-session.

## 5.0.1

##### Fixed

- Fixed a bug where toggling noCookies initialization option from true to false did not create all the necessary cookies.
 
- Fixed an issue where user attributes could not be nulled out by setting a specific null value.

## 5.0.0

##### ⚠️ Breaking

- The subscribeToFeatureFlagsUpdates() callback will now always be called, regardless of refresh success/failure. If there is a failure in receiving updates, the callback will be called with currently cached feature flags.
 
- The getFeatureFlag() method now returns a null if the feature flag does not exist, or if feature flags are disabled.
 
- Removed logContentCardsDisplayed() method that was previously deprecated in 4.0.4.
 
- Removed the deprecated initialization option enableHtmlInAppMessages. This should be replaced with the allowUserSuppliedJavascript option instead.
 
- Removed Banner class that was previously deprecated in 4.9.0 in favor of ImageOnly.
 
- Removed ab-banner CSS classname as part of Banner class removal. CSS customizations should instead target the ab-image-only class.
 
- The SDK no longer throws runtime errors anywhere. If Braze methods are called prior to initialization, a warning will be logged to the console instead.
 
- The SDK no longer adds default Braze in-app message styles to custom HTML in-app messages. These styles were previously used by legacy in-app message types.

## 4.10.2

##### Fixed

- Fixed a CSS templating issue in the npm version of the SDK introduced in 4.10.1 that caused in-app messages to display without the expected styles when using Braze built-in UI.

## 4.10.1

##### Fixed

- Fixed an issue where user attributes could not be nulled out by setting a specific null value.

## 4.10.0

##### Added

- Added a new appVersionNumber initialization option for targeting via numerical comparison.

##### Changed

- The SDK now ensures that cached messages for user (content cards, deferred in-app message, and feature flags) are cleared upon changeUser().
 
- getDeviceId and getUserId now return results directly. Their callback parameters are deprecated and will be removed in a future major version.

## 4.9.0

##### Added

- Introduced a new ImageOnly Card subclass, which has the same functionality as the Banner class.
 
- Added a new ab-image-only CSS class to Banner and ImageOnly cards when displayed through the built-in UI. New CSS customizations should target this class. The ab-banner classname will remain on both card types until the Banner class is removed in a future release.
 
- Introduced two new methods deferInAppMessage() and getDeferredInAppMessage() that can be used together to delay the display of an in-app message for a future pageload.

- [deferInAppMessage()] method defers the given in-app message.
 
- The deferred in-app message can be retrieved by calling the [getDeferredInAppMessage] method.

##### Changed

- Deprecated the Banner class.

##### Fixed

- Fixed an issue where in-app messages with images would fail to display when a parent node is supplied to showInAppMessage() and the parent node has not been attached to the DOM before the display callback is invoked.
 
- Fixed an issue where the callbacks passed to requestContentCardsRefresh() were sometimes not triggered when this call was queued behind another requestContentCardsRefresh() or subscribeToContentCardsUpdates() request.
 
- Fixed an issue where dismissCard() did not work as expected on cached content cards.
 
- Fixed an issue where calling destroy() soonafter wipeData() incorrectly created a device ID cookie.

## 4.8.3

##### Fixed

- Fixed an issue where manageServiceWorkerExternally initialization option failed to register service-worker when trying to register from a path higher than the service-worker location.

## 4.8.2

##### Fixed

- Fixed an issue where slow / failed image loading prevents subsequent in-app messages from displaying.
 
- Fixed a regression introduced in 4.8.0 where push notifications failed to display in Safari versions <= 15.

## 4.8.1

##### Fixed

- Fixed an issue where content cards were sometimes not marked as read upon card impression.
 
- Improved the typings for the isControl field on In-App Message and Card classes.

## 4.8.0

##### Changed

- The subscribeToFeatureFlagsUpdates callback will now always be called first with the currently cached feature flags, and when feature flag updates are available.

##### Fixed

- Fixed the return type for subscribeToContentCardsUpdates().
 
- Fixed the return type for subscribeToFeatureFlagsUpdates().
 
- Improved type definitions in Card, InAppMessage and InAppMessageButton classes:

- Fixed return types for Card.subscribeToClickedEvent() and Card.subscribeToDismissedEvent().
 
- Fixed return types for InAppMessage.subscribeToClickedEvent() and InAppMessage.subscribeToDismissedEvent().
 
- Fixed return type for InAppMessageButton.subscribeToClickedEvent().
 
- Fixed type definition of InAppMessage.extras.

## 4.7.2

##### Fixed

- Fixed a regression with the noCookies option which caused some localStorage keys to be persisted in cookie storage.

## 4.7.1

##### Fixed

- Improved the type definition of Card.extras.
 
- Fixed a regression introduced in 4.0.0 where the manageServiceWorkerExternally and disablePushTokenMaintenance initialization options could not work as expected.

## 4.7.0

##### Added

- User.setCustomUserAttribute now accepts nested custom attributes and arrays of objects.

- Adds a merge parameter that specifies whether the value should be merged with the existing value on the backend. If false (default), any existing attribute will be overwritten. If true, existing objects and arrays of objects will be merged. To update an array of objects, follow the guidelines in our public docs.

##### Fixed

- Fixed an issue where requestPushPermission did not call the deniedCallback if the SDK encountered certain errors when registering push.
 
- Fixed an issue where requestPushPermission did not log a message if push is not supported on the user’s browser.
 
- Fixed an incorrect typing in subscribeToSdkAuthenticationFailures.

## 4.6.3

##### Fixed

- Fixed an issue preventing Feature Flags refreshes when SDK Authentication errors occur.

## 4.6.2

##### Changed

- Removed legacy email capture CSS. This is not a breaking change, as all existing web email capture campaigns have been migrated to the new universal email capture type on the Braze backend. This change results in ~1KB size reduction for those using the built-in In-App Message UI.

## 4.6.1

##### Fixed

- Improved the type definition of FeatureFlag.properties.

## 4.6.0

##### Added

- Added a method braze.logContentCardClick() to log that the user clicked on the given Content Card. This method is equivalent to calling braze.logCardClick() with parameter forContentCards = true.
 
- Added support for the upcoming Braze Feature Flags product.

##### Changed

- Improved the check for duplicate in-app messages at display time.

## 4.5.1

##### Fixed

- Fixed an issue where sites with globally-scoped svg and img CSS caused certain elements of the built-in UI to display incorrectly.

## 4.5.0

##### Added

- Added isControl property to ContentCard base model, to easily determine whether the card is a control card.
 
- Added isControl property to InAppMessage base model, to easily determine whether the message is a control in-app-message.

##### Changed

- Improved the reliability of in-app message impression logging in edge cases.

## 4.4.0

##### Added

- A message is now logged if an IAM is triggered but not displayed because neither automaticallyShowInAppMessages() nor subscribeToInAppMessage() were called.

##### Changed

- IndexedDB connections now close after a transaction has been completed.

##### Fixed

- Fixed an issue introduced in 4.0.0 where In-App Message closing animations did not work as expected.

## 4.3.0

##### Added

- Added brazeBridge.changeUser(id: string, sdkAuthSignature?: string) to HTML In-App Messages.
 
- Added the ability to include a custom pathname in the baseUrl initialization option.

## 4.2.1

##### Fixed

- Fixed an issue introduced in 4.0.3, where IAM displays could sometimes fail due to an internal race condition.

## 4.2.0

##### Added

- Added support for Content Cards to evaluate Retry-After headers.

## 4.1.0

##### Added

- Added a method braze.logContentCardImpressions() to log that the user saw the given Content Cards. This method is equivalent to calling braze.logCardImpressions() with parameter forContentCards = true.

##### Fixed

- Fixed an issue where calling unregisterPush() when the user is already unregistered would fail to execute the success callback function.

## 4.0.6

##### Fixed

- Fixed an issue introduced in 4.0.0 that incorrectly failed to display valid IAMs with an unknown Braze Action type error.

## 4.0.5

##### Fixed

- Fixed an issue introduced in 4.0.0 that prevented the SDK from running with certain rollup.js configurations.

## 4.0.4

##### Changed

- Deprecated and changed the obsolete logContentCardsDisplayed method to a no-op. Card impressions should be logged using logCardImpressions.

##### Fixed

- Fixed an issue introduced in 4.0.0 that prevented control in-app message impressions from being logged.

## 4.0.3

##### Fixed

- Fixed an issue introduced in 4.0.0 where Safari push did not work unless the full baseUrl (e.g. https://sdk.iad-01.braze.com/api/v3) was specified in the initialization options.
 
- The SDK will now ignore In-App Messages containing a push prompt Braze Action for users who have already registered for push or whose browser does not support push.

## 4.0.2

##### Changed

- Cookies set by the Braze Web SDK now expire after 400 days per the recommendation of the HTTP Working Group’s draft RFC 6265

##### Fixed

- Removed usages of the nullish coalescing operator for better compatibility with various webpack configurations.

## 4.0.1

##### Fixed

- The created field is now set for Card objects when using Content Cards.
 
- Added "type": "module" to the package.json so frameworks like Next.js recognize the SDK as an ES Module.

## 4.0.0

##### ⚠️ Breaking

- See our upgrade guide for more information on how to migrate from v3.
 
- The appboy-web-sdk, @braze/web-sdk-core, and @braze/web-sdk-no-amd npm packages are deprecated in favor of the @braze/web-sdk package and will no longer receive updates.
 
- The SDK’s exported object has been renamed from appboy to braze. CDN users must update their loading snippet when upgrading to 4.0.
 
- The file name for the bundled version of the SDK has changed to braze.min.js. CDN users must ensure that the URL points to this new file name when upgrading to 4.0.
 
- The Braze Web SDK now supports importing individual features and methods as native ES Modules that can be tree-shaken. For example, if you only use In-App Messages with a custom UI, you can now import our InAppMessage classes and subscribeToInAppMesssage() and Javascript module bundlers such as webpack will remove any unused code. If you prefer to continue using a compiled version of the SDK, it can be found through our CDN.
 
- The prefix for SDK logs has changed from Appboy to Braze. If you use the Appboy prefix as a filter in your logging tools, you should update it to include Braze.
 
- As a result of the above changes, many of our method signatures have changed. See our upgrade guide for more information on how to migrate.
 
- Dropped support for Internet Explorer.

##### Changed

- Updated default z-index of InAppMessage to 9001. This can be still be overwritten using the inAppMessageZIndex initialization option.

##### Added

- Introduced support for the new Braze Actions feature. When displaying In-App Messages and Content Cards through our built-in UI, this feature requires no additional code.
 
- Added braze.handleBrazeAction() to handle Braze Action URLs when using a custom UI.

## 3.5.1

##### Changed

- Added Shopify to BrazeSdkMetadata

## 3.5.0

##### Added

- Added appboy.addSdkMetadata() to allow self reporting of SDK Metadata fields via the appboy.BrazeSdkMetadata enum.
 
- Deprecated the appboy.stopWebTracking() method in favor of using appboy.disableSDK(), which has the same functionality.
 
- Deprecated the appboy.resumeWebTracking() method in favor of using appboy.enableSDK(), which has the same functionality.
 
- Added getter method appboy.isDisabled() to determine if SDK has been disabled via appboy.disableSDK().
 
- Accessibility improvements to in-app messages with scrollable text.

##### Changed

- Calling changeUser() with an SDK Authentication signature will now update the signature when it is called with the current user’s ID.

##### Fixed

- Fixed an issue where removing the ab-pause-scrolling class was not sufficient to allow scrolling on touchscreen devices during the display of an in-app message.

## 3.4.1

##### Fixed

- Fixed an issue introduced in 3.3.0 where event timestamps could become incorrect when a network request fails and the event is placed back in the queue.

## 3.4.0

##### Added

- Added User.addToSubscriptionGroup() and User.removeFromSubscriptionGroup() to manage SMS/Email Subscription Groups.

##### Changed

- Cards with subclass ControlCard are no longer counted in Feed.getUnreadCardCount or ContentCards.getUnviewedCardCount.

##### Fixed

- Fixed an issue where globally-scoped CSS could cause the text and close button of In-App Messages to display incorrectly when using the built-in UI.
 
- Fixed an accessibility issue with Content Cards where some feed children did not have the article role.
 
- Fixed an issue where service worker network requests, including push click analytics, could not be made when SDK Authentication is enabled. If SDK Authentication is enabled and the service worker does not have a valid authentication signature, push click analytics will now be sent to the backend on the user’s next session.
 
- Fixed an issue where network requests that failed due to SDK Authentication errors did not use exponential backoff for retries.
 
- Fixed an issue where iPads would be detected as Mac devices when using the “Request Desktop Site” iOS feature.
 
- Fixed an issue where aspectRatio had an incorrect type in Card subclasses.

## 3.3.0

##### Added

- Introduced support for new SDK Authentication feature.
 
- Introduced an inAppMessageZIndex initialization option that allows you to easily customize the z-index of In-App Messages displayed by the built-in UI.
 
- Added successCallback and errorCallback parameters to requestContentCardsRefresh.
 
- The SDK now logs deprecation warnings for deprecated methods and initialization options when logging is enabled.
 
- Added support for brazeBridge, which has the same API as appboyBridge. appboyBridge is now deprecated but will continue to function.
 
- Introduced support for the upcoming nested properties feature in appboy.logCustomEvent and appboy.logPurchase.

##### Changed

- Removed appboyQueue replay snippet from the npm publication of the SDK. This avoids possible race conditions when referencing the SDK simultaneously from npm and the CDN, and removes use of eval from the npm package
 
- appboy.logCustomEvent and appboy.logPurchase now impose a 50KB limit on custom properties. If the supplied properties are too large, the event is not logged.
 
- Deprecated the trackLocation method in favor of using the native Geolocation API and passing the location data to ‘User.setLastKnownLocation`. See our public docs for more information.
 
- Deprecated the enableHtmlInAppMessages initialization option in favor of allowUserSuppliedJavascript. These options are functionally equivalent and no other changes are required.

##### Fixed

- Fixed incorrect typing for User.setCountry.
 
- Added missing dismissed property to TypeScript definition and docs for Card subclasses.

## 3.2.0

##### Added

- Added an optional parentNode parameter to appboy.display.hideContentCards that allows you to specify a particular Content Cards feed to hide.

##### Changed

- Cookies set by the SDK are now renewed when a new session is started. This fixes an issue where the SDK would stop setting cookies that had been deleted or expired when identification information existed in localStorage, preventing cross-subdomain identification from functioning in certain circumstances.
 
- Increased clickable area of all buttons in the built-in UI to be at least 45x45px to comply with mobile accessibility best-practices. This includes some minor changes to the Content Cards and News Feed UI to accommodate the larger buttons.

##### Fixed

- Fixed an issue where some network requests fail on websites using certain libraries that overwrite the native Promise object.

## 3.1.2

##### Fixed

- Added default alt text to In-App Message and Content Card images to improve screen-reader experience.
 
- Improved the display of different aspect ratios for ClassicCard images when using the built-in UI.
 
- Fixed a regression introduced in 3.1.0 where the SDK would sometimes make multiple network requests when starting a new session.
 
- Fixed an issue where globally-scoped float CSS caused certain elements of the built-in UI to display incorrectly.
 
- Fixed an incorrect TypeScript definition for DeviceProperties.

## 3.1.1

##### Fixed

- Fixed an issue where a javascript error could be thrown when showing Content Cards or In-App Messages in certain environments where this is undefined.

## 3.1.0

##### Added

- Added a devicePropertyAllowlist initialization option. This new initialization option has the same functionality as devicePropertyWhitelist, which is now deprecated and will be removed in a future release.

##### Changed

- Relaxed the email address validation used by the SDK in favor of the more accurate Braze backend validation. Valid addresses with unusual structures or international characters which were previously rejected will now be accepted.

##### Fixed

- Fixed an issue where the SDK was improperly handling session starts when switching between subdomains, causing a short delay in triggering in-app messages.

## 3.0.1

##### Fixed

- Fixed incorrect type definitions for the extras property of Card and In-App Message classes.
 
- Fixed a regression introduced in 2.5.0 where the functionality of the manageServiceWorkerExternally and disablePushTokenMaintenance initialization options were swapped.

## 3.0.0

##### ⚠️ Breaking

- The Braze Web SDK now comes bundled with TypeScript definitions in the @braze NPM packages. The TypeScript defintions include documentation and autocomplete in IDEs that support it, even if your project does not use TypeScript.
 
- The following breaking changes have been made to allow for a better TypeScript experience:

- The ab namespace has been removed. To migrate from previous integrations, you can simply find and replace all references to appboy.ab with appboy.
 
- InAppMessage.Button has been renamed to InAppMessageButton. To migrate from previous integrations, you can simply find and replace all references to InAppMessage.Button with InAppMessageButton.

- Due to the above changes, the SDK loading snippet has been updated. If you integrate the Braze Web SDK using the CDN, you must update the loading snippet when upgrading to 3.0.
 
- The baseUrl option to appboy.initialize is now required to initialize the SDK. If your integration did not already provide the baseUrl option, it should now be set to the previous default value of sdk.iad-01.braze.com (e.g, appboy.initialize('YOUR-API-KEY', { baseUrl: 'sdk.iad-01.braze.com' });).
 
- Removed the messagingReadyCallback from openSession and changeUser. Since 2.3.1, the SDK handles events that occur during the asynchronous portion of these calls gracefully, and ensures internally that only the latest messaging will be triggered. Any code previously being invoked inside this callback may be safely placed directly after the openSession or changeUser call.

##### Changed

- The Braze Web SDK has brand new docs, which can be found here. Any URLs from the previous docs will redirect to the appropriate location.

##### Fixed

- Fixed an issue where browser version was incorrectly reported in Android Webview.

## 2.7.1

##### Fixed

- Fixed a regression introduced in 2.5.0 where the functionality of the manageServiceWorkerExternally and disablePushTokenMaintenance initialization options were swapped.

## 2.7.0

##### Added

- Added appboyBridge.getUser().addAlias(alias, label) to HTML In-App Messages.

##### Changed

- The Braze Web SDK now uses User-Agent Client Hints for device detection when available. When using User-Agent Client Hints, browser version detection is limited to the significant version (e.g., 85 instead of 85.0.123.0). Note that this upgrade will be necessary to ensure accurate operating system detection in upcoming versions of Chromium-based browsers.
 
- Cards received from the Content Cards test send feature of the Braze dashboard are no longer removed when the SDK receives an update to the user’s Content Cards.

##### Fixed

- Removed code that could result in javascript errors in certain webpack configurations where the global object is not accessible by the SDK.
 
- Fixed an issue where the ab.Card methods removeAllSubscriptions, removeSubscription, subscribeToClickedEvent, and subscribeToDismissedEvent were minified, resulting in undefined when called.

## 2.6.0

##### Added

- Introduced new NPM packages under the @braze scope. The core and full versions of the SDK as well as the service worker are now published in their own packages, resulting in a drastically reduced install size compared to the appboy-web-sdk package. This is not a breaking change for existing NPM integrations and we will continue to publish the appboy-web-sdk package to maintain backwards compatibility. See the README for integration details.
 
- Added appboyBridge.getUser().setLanguage(language) to HTML In-App Messages.

##### Changed

- The new HTML In-App Message type now allows multiple clicks to be logged for a given message.

##### Fixed

- Made push-related methods more defensive against edge-cases where Notification is not defined.
 
- Fixed an issue where unexpected backend responses could result in a javascript error.
 
- Fixed an issue in recent versions of Safari where calling appboy.registerAppboyPushMessages would throw a javascript error if the user did not allow websites to ask for permission to send notifications.

## 2.5.2

##### Fixed

- Fixed an issue that could cause some prerender user agents to fail to be appropriately recognized as a web crawler.

##### Changed

- Data will now be flushed to the Braze backend every 3 seconds on Safari (down from 10 seconds) due to new privacy features that clear localStorage after 7 days of inactivity.

## 2.5.1

##### Fixed

- Fixed an issue in Content Cards where getUnviewedCardCount() returns undefined. This issue was introduced in 2.5.0.

## 2.5.0

##### Added

- Introduced support for upcoming HTML In-App Message templates.
 
- Added appboyBridge.logClick() to HTML In-App Messages.
 
- Expanded browser detection to include UC Browser and newer versions of Microsoft Edge that are based on Chromium.
 
- Added a new variant of the SDK that allows sites using RequireJS to load the SDK through another method, such as NPM or a <script> tag. See the README for more information.
 
- Added an optional callback to appboy.requestImmediateDataFlush that is invoked when the flush is complete.
 
- Added Czech and Ukrainian language support for Braze UI elements.

##### Changed

- Decreased the size of the service worker by 20%.

##### Fixed

- Fixed an issue where refreshing Content Cards or News Feed while the feed is showing could cause multiple impressions to be logged for the same card.
 
- Fixed a bug where calling setEmail with an email address containing capital letters could sometimes be incorrectly rejected.
 
- Fixed a bug where refreshing Content Cards would incorrectly set the clicked attribute of the cards to false.
 
- Fixed a bug where providing serviceWorkerLocation with an absolute URL containing a protocol and hostname would result in an error being logged when calling appboy.registerAppboyPushMessages.
 
- Fixed an issue where calling appboy.registerAppboyPushMessages in recent versions of Firefox would not show the notification prompt.
 
- Fixed a timing issue where creating a reference to window.appboy and then using that reference asynchronously could sometimes cause javascript errors when using the default integration snippet.

## 2.4.3

##### Fixed

- Fixed a bug that would cause appboy.registerAppboyPushMessages to fail when called immediately on a user’s first session.
 
- Fixed an issue where using both the manageServiceWorkerExternally and serviceWorkerLocation initialization options would cause the SDK to not register for push if the provided service worker location was in a sub-directory.
 
- Fixed an issue where appboy.registerAppboyPushMessages could throw an exception if an error occured while updating a previously registered service worker.

## 2.4.2

##### Fixed

- Fixed a bug introduced in 2.4.1 that would focus inline feeds, causing the page to scroll when content cards are shown out of view.

## 2.4.1

#### Breaking

- Accessibility updates in this release have changed headers to use h1 tags and close buttons to use button tags (instead of div and span respectively). As a result, any CSS customizations which rely upon div or span elements within .ab-feed or .ab-in-app-message should be updated to use classes instead.

##### Added

- Introduced a dismissCard method that can be used to dismiss a card programmatically.
 
- Improved accessibility throughout the SDK:

- Used h1 tags for headers and button tags for close buttons
 
- Added ARIA attributes
 
- Improved the experience when tabbing through elements
 
- We now restore the user’s previously focused element after closing In-App Messages

##### Fixed

- Fixed a bug introduced in 2.4.0 that could cause a javascript error in integrations that only include the core library. This error would occur when a Content Card with a URL is received.

## 2.4.0

##### Breaking

- Removed the Feedback feature and appboy.submitFeedback method from the SDK.

##### Added

- Improved browser detection to account for the Smart TV landscape.
 
- Added logic to automatically renew push subscriptions when they are expired or older than 6 months.
 
- Introduced a contentSecurityNonce initialization option for sites with a Content Security Policy. See the appboy.initialize documentation for more info.
 
- Introduced a disablePushTokenMaintenance initialization option for sites that have users with Web Push permission granted, but do not wish to use Web Push with Braze. See the appboy.initialize documentation for more info.
 
- Introduced a manageServiceWorkerExternally initialization option for sites that have their own service worker already. See the appboy.initialize documentation for more info.
 
- Deprecated the subscribeToNewInAppMessages method in favor of the new subscribeToInAppMessage method, which has a simpler interface.

##### Fixed

- Improved support for In-App Messages on “notched” devices (for example, iPhone X, Pixel 3XL).
 
- The logic that prevents the page behind a modal or fullscreen In-App Message from scrolling now functions correctly on iOS.
 
- Fixed a caching bug that could cause In-App Messages, Content Cards, and News Feed Cards received by one instance of the Braze SDK to not be seen by another simultaneously running instance of the Braze SDK.
 
- Fixed a bug that would cause redundant network activity for new users on their first session ever.
 
- Fixed a bug that would cause push registration that occurs immediately on a user’s first session to fail.
 
- Introduced the allowUserSuppliedJavascript initialization option, which is an alias for the existing enableHtmlInAppMessages option, and disabled the ability to use javascript: URIs in In-App Message and Content Card click actions unless one of these options is provided.

##### Changed

- Improved the look and feel of Content Card dismissals and Content Card and News Feed animations to match the latest In-App Message styles.
 
- The baseUrl configuration option for appboy.initialize is now more flexible in the values that it can accept.
 
- Cookies set by the Braze Web SDK now expire after 1 year.

## 2.3.4

##### Fixed

- Fix regression introduced in 2.3.3 that could prevent analytics from being logged from the service worker.

## 2.3.3

##### Fixed

- Improved some In-App Message CSS styles to be more resilient against conflicts with any page-wide CSS.
 
- Improved the resiliency of the code that allows body content to scroll again when modal or fullscreen in-app messages are dismissed.

## 2.3.2

##### Added

- Added support for an improved integration snippet which is capable of stubbing the interface before the SDK loads in Google Tag Manager.

## 2.3.1

##### Added

- Introduced new closeMessage method on ab.InAppMessage objects to enable integrations to programmatically close messages if desired.
 
- The Braze Web SDK now automatically enqueues trigger events that occur while triggers are being synced with the Braze backend, and replays them when the sync is complete. This fixes a race condition that could cause users to inadvertantly miss messages when trigger events occur directly after calling openSession or changeUser. This change obsoletes usage of the messagingReadyCallback, which is now deprecated (but will continue to function).

##### Fixed

- Fixed an issue which prevented tall ab.HtmlMessage objects from scrolling on iOS.
 
- Fixed “Object doesn’t support this action” error in Internet Explorer 11 or older when showing ab.HtmlMessage objects.

## 2.3.0

##### Added

- Improved the look and feel of In-App Messages to adhere to the latest UX and UI best practices. Changes affect font sizes, padding, and responsiveness across all message types. Now supports button border styling.

##### Fixed

- This feature, which regressed in 2.1.0, has been restored: when you call appboy.openSession, if the user has previously granted the site permission to send push, Braze will now automatically send the user’s push token to Braze backend. This will allow users to continue to receive push messages if they manually remove push permission and then subsequently manually reenable it - and will also cause user push tokens to automatically migrate to Braze over time when moving to Braze from a previously-integrated third-party push provider.

## 2.2.7

##### Added

- HTML In-App Messages now emit an ab.BridgeReady event when the appboyBridge variable is available for use inside your HTML, allowing you to use appboyBridge immediately when an in-app message is shown. To utilize this event in your HTML In-App Messages, use window.addEventListener('ab.BridgeReady', function() {/*Use appboyBridge here*/}, false);.

##### Changed

- Changed usages of Date.now() to new Date().valueOf() to allow the Braze SDK to sit side-by-side with legacy 3rd party libraries that monkey-patched Date.now() before ECMASCRIPT 5 defined it.

## 2.2.6

##### Added

- Added clicked property to Content Cards which returns true if this card has ever been clicked on this device.

##### Changed

- Improved in-app message triggering logic to fall back to lower priority messages when the Braze server aborts templating (e.g. from a Connected Content abort in the message body, or because the user is no longer in the correct Segment for the message)
 
- Improved in-app message triggering logic to retry user personalization when communication with the Braze server fails due to network connectivity issues.
 
- The Braze Web SDK now only stores cookies for the most recently-used API Key (app). This reduces cookie storage usage for domains that are configured against many Braze apps.

## 2.2.5

##### Added

- Added devicePropertyWhitelist property to the options for appboy.initialize(), which can be used to filter what device properties get collected.

## 2.2.4

##### Added

- Added support for richer custom styling through CSS in in-app messages.

##### Changed

- Subtle visual polish to the News Feed and Content Cards

## 2.2.3

##### Added

- Added support for tracking custom location attributes. See the ab.User.setCustomLocationAttribute documentation for more information.
 
- When calling appboy.registerAppboyPushMessages with a deniedCallback, that deniedCallback will now be invoked (with a temporary parameter of true) for temporary denials, where the browser has automatically denied permission on behalf of the user after multiple ignored attempts to register for push, but will allow attempts again in the future - probably in about a week.
 
- Added appboyBridge.web.trackLocation() in HTML in-app messages. This enables HTML in-app message soft location tracking prompts.

##### Fixed

- News Feed and Content Cards clicks and impressions will now be logged multiple times for a given card (if they in fact occur multiple times). Impressions will still only be logged for a given card once per viewing of the feed (regardless of how many times it scrolls in and out of view).
 
- Improved logic around IndexedDB to better catch and log errors (prevents security errors with disabled cookies on certain browsers, or from Safari’s “Intelligent Tracking Prevention” when integrated in an iFrame).
 
- Worked around this Chrome Bug which could cause device detection to throw “Unsupported time zone specified undefined” on Linux-based systems with certain settings.
 
- Fixed an issue where the messagingReadyCallback would not get fired if changeUser was called with an empty ID.

##### Changed

- Data will now be flushed to the Braze backend every three seconds when localStorage is not available.
 
- Improved triggered in-app message re-eligibility logic to better handle templating failures.

## 2.2.2

##### Added

- Updated push token handling to automatically remove blocked users from the pushable audience on session start.

##### Fixed

- Fixed issue in Content Cards where the getUnviewedCardCount method on ab.ContentCards could not be invoked properly.
 
- Fixed a bug where the addAlias method was returning an object instead of a boolean value.
 
- Fixed issue which could prevent Content Cards from syncing properly on IE 11 and Safari.

##### Changed

- Various user attribute methods now support setting null (setFirstName, setLastName, setCountry, setHomeCity, setPhoneNumber, setEmail, setGender, setLanguage, and setDateOfBirth) by passing in an explicit null value.

## 2.2.1

##### Fixed

- Prevent push received/clicked analytics from being sent to the Braze backend when appboy.stopWebTracking has been called.

## 2.2.0

##### Added

- Introduced support for Content Cards, which will eventually replace the existing News Feed feature and adds significant capability.
 
- Added support for web push on Accelerated Mobile Pages (AMP). See https://www.braze.com/documentation/Web/#amp-support for setup information.

##### Fixed

- Fixed an issue where in-app messages triggered on session start could potentially be templated with the old user’s attributes.

##### Removed

- Removed appboy.requestInAppMessageRefresh() and support for legacy in-app messages - these were long-deprecated and have been supplanted by triggered in-app messages.

## 2.1.1

##### Fixed

- Prevent push received/clicked analytics from being sent to the Braze backend when appboy.stopWebTracking has been called.

## 2.1.0

##### Added

- Added appboy.wipeData() to allow deletion of locally stored SDK data. After calling this method, users will appear as a new anonymous user on a new device.

##### Fixed

- Improved push registration and unregistration

- appboy.registerAppboyPushMessages will now set the user’s subscription status to “OPTED_IN” only at times when they’ve just accepted the permission prompt.
 
- appboy.unregisterAppboyPushMessages will now persist across sessions and user changes (until appboy.registerAppboyPushMessages is called again).
 
- appboy.registerAppboyPushMessages will cause push prompts to be shown shown more reliably in situations where the user has ignored them in the past. Logging around dismissing (as opposed to accepting or blocking) push prompts has been improved.

- Fixed a bug with appboy.changeUser where messagingReadyCallback would not fire when the supplied userId was the current user.

##### Changed

- Updated from FontAwesome 4.3.0 to FontAwesome 4.7.0. Integrations that wish to maintain older versions should pass in doNotLoadFontAwesome as true during initialization and load their desired version.
 
- The Braze SDK will automatically load FontAwesome unless doNotLoadFontAwesome is explicitly passed in as true during initialization, regardless of whether fontawesome.css or fontawesome.min.css are already on the page.

## 2.0.9

##### Fixed

- Prevent push received/clicked analytics from being sent to the Braze backend when appboy.stopWebTracking has been called.

## 2.0.8

##### Added

- Added defensive guards against any possibility of sessions expiring in less than 1 second or of creating multiple session events in rapid succession if scripted in parallel across many open tabs.

## 2.0.7

##### Added

- Added support for Voluntary Application Server Identification (VAPID) for Web Push:

- Will be required for Microsoft Edge’s upcoming Web Push support, and possibly other browsers in the future.
 
- Allows importing of VAPID-enabled push tokens generated by other push providers, given the corresponding keypair. Contact Braze Technical Support for assistance.
 
- Happens transparently in the background and does not require an integration update.
 
- Once the browser landscape has sufficiently matured, this will eventually obviate the need to supply a gcm_sender_id in your site’s manifest.json.

##### Changed

- appboy.unregisterAppboyPushMessages now accepts optional successCallback and errorCallback arguments to signal completion, as it functions asynchronously.

## 2.0.6

##### Fixed

- Fixed a javascript error introduced in 2.0.5 when logging in the service worker.

## 2.0.5

##### Added

- Added Location Tracking - See appboy.trackLocation() for more information.
 
- appboy.user.setGender now supports more gender options. See the Genders enum documentation for more information.
 
- Added appboy.stopWebTracking() and appboy.resumeWebTracking() to allow user opt-outs.
 
- Improved accessibility for in-app messages and news feed by focusing on elements where appropriate, allowing users to tab through various buttons, and adding labels where appropriate.

##### Fixed

- Fixed a bug that caused appboy.display.automaticallyShowNewInAppMessages() not to function correctly when called after calling appboy.destroy() and then calling appboy.initialize() a second time.
 
- The openSession and changeUser methods now take a messagingReadyCallback that executes when the Braze Web SDK is ready to show messaging data to this user. This fixes a race condition where custom events could be logged before in-app messages had been fetched from the Braze backend and users would not see intended messaging.

##### Changed

- Deprecated the submitFeedback method. The feedback feature is disabled for new accounts, and will be removed in a future SDK release.

## 2.0.4

##### Changed

- Renamed documentation references from Appboy to Braze. This is not a breaking change.

## 2.0.3

##### Fixed

- Fixed a null reference error when replaying calls made using the new integration snippet on IE 11.

## 2.0.2

##### Fixed

- Fixed an issue with our minification that would cause the Braze Web SDK to leak polyfill functions into the global namespace.

## 2.0.1

##### Fixed

- Fixed automatic css loading when used in combination with the doNotLoadFontAwesome initialization option.

## 2.0.0

##### Breaking

- Braze now automatically loads required CSS styles. You must remove all references to appboy.min.css from your site.
 
- The getUserId method now takes a callback which it invokes with the userId, instead of returning a value directly. This is necessary to ensure the proper replaying of calls made to appboy before the SDK has fully loaded. Where before, you would do var userId = appboy.getUser().getUserId();, now do appboy.getUser().getUserId(function(userId) { console.log(userId); }) See the getUserId method documentation for more information.
 
- The getDeviceId method now takes a callback which it invokes with the deviceId, instead of returning a value directly. This is necessary to ensure the proper replaying of calls made to appboy before the SDK has fully loaded. See the getDeviceId method documentation for more information.

##### Changed

- The default Braze integration snippet has been updated for best-practices compliance, resilience, and performance. Using this new snippet, calls may be made to appboy before the SDK has fully loaded, and will be replayed automatically when the SDK loads. We recommend that you update your site’s integration to the new snippet for optimal behavior, but this is not a breaking change, and is not required.

##### Added

- If you are using a front-end packager such as Browserify or Webpack, the NPM integration instructions have been updated to meet your use-case.

## 1.6.14

##### Added

- Added the user agent for the https://prerender.io/ crawler to the list of known web crawlers.
 
- Added ab.User.setLanguage method to allow explicit control over the language you use in the Braze dashboard to localize your messaging content.

##### Fixed

- Fixed array validation on pages where the Array type has been modified by other scripts.

##### Changed

- Marked the ‘touchstart’ listener in in-app messages as ‘passive’ for performance and PWA compliance.

## 1.6.13

##### Added

- Contains service-worker support for Web Push notifications that require user interaction to be dismissed.

##### Fixed

- Improved time zone recognition on modern browsers to prevent possible ambiguity between different zones with similar UTC offsets.
 
- Broadened detection of the Android OS to better recognize newer hardware and as-of-yet unreleased hardware on an ongoing basis.
 
- Fixed data-formation error when pending additions or removals to a custom attribute array were re-enqueued following a Braze backend outage or otherwise failed data flush.

##### Changed

- We now allow a value of 0 for the minimumIntervalBetweenTriggerActionsInSeconds option for appboy.initialize

## 1.6.12

##### Added

- Introduced noCookies option. By default, the Braze SDK will store small amounts of data (user ids, session ids), in cookies. This is done to allow Braze to recognize users and sessions across different subdomains of your site. If this presents a problem for you, pass true for this option to disable cookie storage and rely entirely on HTML 5 localStorage to identify users and sessions. The downside of this configuration is that you will be unable to recognize users across subdomains of your site.
 
- Added user aliasing capability. Aliases can be used in the API and dashboard to identify users in addition to their ID. See the addAlias method documentation for more information.

##### Fixed

- Fixed issue in which the local cache of seen in-app messages and news feed cards was being cleared when the anonymous user was identified, allowing certain items to be retriggered or appear unread.

## 1.6.11

##### Added

- When you call appboy.openSession, if the user has previously granted the site permission to send push, Braze will now automatically send the user’s push token to Braze backend. This will allow users to continue to receive push messages if they manually remove push permission and then subsequently manually reenable it - and will also cause user push tokens to automatically migrate to Braze over time when moving to Braze from a previously-integrated third-party push provider.

##### Fixed

- IMPORTANT: Due to a behavioral change in Chrome 59, to reliably receive notifications, you must update the service worker from https://js.appboycdn.com/web-sdk/1.6/service-worker.js.
 
- appboy.display.automaticallyShowNewInAppMessages() may now be safely called multiple times on the same appboy instance.

## 1.6.10

##### Fixed

- A bug in our documentation for soft push prompts could cause Control Group stats to fail. If you previously implemented soft push prompts, please refer to the latest version of our documentation: https://www.braze.com/documentation/Web/#soft-push-prompts

## 1.6.9

##### Added

- Added support for appboyBridge.web.registerAppboyPushMessages to allow HTML in-app messages to request push permission from the user.

## 1.6.8

##### Fixed

- Fixed “Notification is not defined” error when calling appboy.isPushPermissionGranted/appboy.isPushBlocked on Chrome versions prior to 46.

## 1.6.7

##### Added

- The Braze Web SDK now supports HTML content in-app messages. For your security, these must be enabled by supplying the enableHtmlInAppMessages configuration option when calling appboy.initialize.

##### Fixed

- The News Feed css is now defensive against any global box-sizing css rules that may exist on your site, and handles classic card image styling more gracefully.
 
- On mobile devices, Fullscreen in-app messages’ close buttons are sized relative to the entire device - this ensures touchable targets on high-resolution phones.
 
- Improved positioning of Modal in-app messages to ensure visibility and attractive positioning across all browsers.

## 1.6.6

##### Fixed

- Fixed a data-storage issue where a small number of users impacted by the issue fixed in 1.6.5 may record a new session on page load after upgrading to 1.6.5.

## 1.6.5

##### Fixed

- Cookies are now stored with path=/ for sitewide accessibility, ensuring that identification persists sitewide in all situations. This fixes an issue introduced in 1.6.0.

## 1.6.4

##### Added

- The Braze Web SDK now ignores web crawler activity by default - this saves datapoints, makes analytics more accurate, and may improve page rank (this change can be reversed with the allowCrawlerActivity initialization option).

##### Fixed

- Fixed an issue where in-app messages triggered off of push clicks wouldn’t fire because the push click happened before the in-app message configuration was synced to the device.
 
- Increased defensiveness against corrupted localStorage or cookie data.

##### Changed

- Increased the size of in-app message close buttons on mobile browsers slightly to make an easier touch target.
 
- Updated appboy.registerAppboyPushMessages to flush subscriptions to the server immediately.

## 1.6.3

##### Changed

- Further improved the layout of Fullscreen in-app messages on short desktop screens.

## 1.6.2

##### Changed

- Deprecated the appboy.isPushGranted method in favor of the new appboy.isPushPermissionGranted. The old method was inappropriately testing whether the browser has an active push subscription, and not doing the intended test of whether the user has granted push permission. The old method will be removed in an upcoming release.

## 1.6.1

##### Fixed

- Improved Modal in-app message layout to prevent text-view scrolling until necessary.

##### Changed

- Deprecated the safariWebsitePushId parameter to appboy.registerAppboyPushMessages and appboy.isPushGranted in favor of the new safariWebsitePushId option to appboy.initialize. If you implement Safari push, you should convert your integration to use the new initialization option - support for the parameters will be removed in a future release. This is not yet a breaking change.
 
- Polished Fullscreen in-app message display on desktop browsers to reduce unused whitespace when the content is small enough not to scroll.

## 1.6.0

##### Fixed

- Fixed an edge-case that could cause SlideUp in-app messages to appear offscreen if many were triggered in rapid succession.

##### Changed

- Improved ability to consistently identify users, devices, and sessions across subdomains by preferring domain-wide cookies for ID storage (over the previously-preferred localStorage).

## 1.5.1

##### Fixed

- Fixed a rendering issue that could cause FullScreen in-app messages to appear partially off-screen on very short browser windows.

## 1.5.0

##### Added

- Added support for upgraded in-app messages including image-only messages, improved image sizing/cropping, text scrolling, text alignment, configurable orientation, and configurable frame color.
 
- Added support for in-app messages triggered on custom event properties, purchase properties, and in-app message clicks.
 
- Improved support for templated in-app messages.
 
- Added appboy.isPushGranted() method, useful for migrating existing push subscriptions from another third-party provider to Braze.
 
- Added language localization - language is detected automatically from the browser or can be specified explicitly via the language initialization option.

## 1.4.2

##### Added

- Added additional logging information for Safari push.

## 1.4.1

##### Added

- Added a more explicit error when attempting to call registerAppboyPushMessages on Safari without supplying a safariWebsitePushID.

## 1.4.0

##### Added

- Added support for Safari push messages.
 
- If you version your website, you may now optionally pass the version to Braze via the new appVersion initialization option.
 
- The News Feed now displays a timed-out message to users if the refresh fails (due to network or back end outages).
 
- Browser version will now be reported as part of the user’s device information along with browser.
 
- Added ability to specify on a message-by-message basis whether in-app message clicks should open in a new tab or same tab.

##### Fixed

- Fixed an issue which caused emoji in web push messages to be broken on Firefox.

##### Changed

- Overhauled the browser detection code for improved reliability.

## 1.3.3

##### Added

- Added a new serviceWorkerLocation initialization option. See JSDocs for more information.

## 1.3.2

##### Added

- Added support for Braze Feedback through the new appboy.submitFeedback method.

##### Fixed

- In-App Messages now track click analytics even when the click action is “None.”
 
- Prevent Mobile Safari in Private Browsing mode from throwing an exception. This issue was introduced in 1.3.0.

## 1.3.1

##### Fixed

- Prevent Firefox from throwing an exception when in Private Browsing mode. This issue was introduced in 1.3.0.

## 1.3.0

##### Breaking

- The inAppMessages parameter to appboy.subscribeToNewInAppMessages subscribers may now contain ab.ControlMessage objects.

##### Added

- Adds support for triggered in-app messages.

##### Fixed

- Fixed a bug where news feed cards weren’t always immediately being marked as read during scrolling.

##### Changed

- All iOS devices will now report their OS as “iOS” instead of “iPhone/iPod” or “iPad”.

## 1.2.2

##### Fixed

- Fixed a javascript error that could occur when attempting to showFeed before the body has loaded.
 
- Made in-app message buttons explicitly display:inline-block so that they still display correctly if the site is styling buttons as display:block.

## 1.2.1

##### Fixed

- The service worker now reads Braze’s backend URL from IndexedDB, which allows web push to function for clients with custom Braze endpoints.
 
- isPushBlocked now returns false when isPushSupported is false instead of erroring.

## 1.2.0

##### Breaking

- Restyled the news feed for improved legibility with a wider variety of card content. If you have existing news feed css customization this may be a breaking change.

##### Added

- Supports web push (on browsers implementing the w3c spec, with or without payloads - i.e. Chrome, Firefox).
 
- Introduced appboy.toggleFeed as a convenience method - it simply calls appboy.showFeed or appboy.destroyFeed based on whether there’s currently a feed showing.

##### Fixed

- Buttonless FullScreen and Modal messages now respect body click actions from the dashboard.

##### Changed

- To reduce the datapoint impact of the high number of anonymous users on the web, in-app messages are no longer. automatically refreshed for new, anonymous users on their first openSession call. You can override this behavior and force an in-app message refresh by manually calling appboy.requestInAppMessageRefresh.
 
- In-App Messages may now be dismissed with a click on the greyed-out background of the page. This behavior may be prevented by passing requireExplicitInAppMessageDismissal:true to appboy.initialize.

## 1.1.1

##### Added

- Expanded browser detection to recognize more niche browsers.

##### Fixed

- Fixed an issue which would cause some Android devices to be detected as Linux.

## 1.1.0

##### Added

- Introduced appboy.logFeedDisplayed, which is called automatically when using appboy.display.showFeed.

##### Fixed

- Fixed a race condition which could cause events to be double-counted if the user had the site open in very many tabs at once.

##### Changed

- News feed and in-app message links now open in the same tab.

## 1.0.1

##### Fixed

- The SDK now logs correctly to the console when enableLogging is true (or toggleAppboyLogging has been called) and no custom logger has been specified.

## 1.0.0

##### Added

- Respect blacklisted custom events, attributes, and purchases.

##### Removed

- Removed the setBio method on ab.User in accordance with the deprecation of that user property across the Braze platform.

## 0.2.4

##### Fixed

- Fixed an issue which was causing the in-app message refresh throttle not to persist beyond a single page load.

## 0.2.3

##### Added

- Introduce appboy.display.destroyFeed method to allow integrators to implement a toggle feed button or otherwise hide the feed from code.

##### Fixed

- Prevent potential race condition which could cause news feed cards to not be marked as read for a short amount of time.

##### Removed

- Remove the news feed z-index. If necessary, the z-index can be set manually via CSS: .ab-feed { z-index: }.

## 0.2.2

##### Fixed

- Fix issue where already-cached news feed cards were not properly having impressions logged when the news feed was first shown.

##### Changed

- Minor improvements to In-App Message styling.

## 0.2.1

##### Added

- Give the news feed a z-index just below bootstrap modal backdrops.

##### Fixed

- Support legacy Internet Explorer (complete IE9 support, generally functional IE8 support).

##### Changed

- Ignore in-app messages with an unknown type (prevents future message types from be inappropriately displayed on versions of the sdk which don’t yet support them).

## 0.2.0

##### Added

- Added Braze news feed support.

## 0.1.5

##### Fixed

- Correctly identify IE11.

## 0.1.4

##### Fixed

- Fixed issue where SlideUp message clicks with a clickAction of URI were not being respected.
 
- Fixed issue where Date custom attributes, custom event properties, and purchase properties were not being recognized as Dates by the Braze platform.

## 0.1.3

##### Added

- Add support for more purchase currencies, allow lowercase currencies.

##### Changed

- Use millisecond precision when logging events.

## 0.1.2

##### Changed

- Introduce optional doNotLoadFontAwesome initialization option and additionally don’t load FontAwesome if fontawesome.css or fontawesome.min.css are already on the page.
 
- More minor improvements to In-App Message styling.

## 0.1.1

##### Changed

- Various minor improvements to SlideUp styling.

## 0.1.0

##### Added

- Support in-app messages.

## 0.0.5

##### Fixed

- Fixed critical issue which caused browser tabs to become unresponsive with no network connection.

## 0.0.4

##### Fixed

- Defend against NS_ERROR_FILE_CORRUPTED (corrupted browser SQLite database) and more generally against inability to use localStorage.

## 0.0.3

##### Changed

- Provide better backend error messages.

## 0.0.2

##### Fixed

- Fixed a bug where due to minification, locally stored data was version-specific.

## 0.0.1

##### Fixed

- Fixed bug where multibyte UTF-8 characters were being rejected for various attributes.
 
- Harden usage of localStorage slightly.

##### Changed

- Allow setLogger to be called before initialize.

## 0.0.0

- Initial release with core functionality.

tip

You can also find a copy of the Android Braze SDK changelog on GitHub.

## 43.1.1

Release Date

##### Fixed

- Fixed published AAR metadata requiring consuming apps to compile against API 37. Consuming projects may use compileSdk 21 or later.

## 43.1.0

Release Date

##### Fixed

- Fixed an issue where BannerView could call WebView APIs after destroy() when async banner HTML loading ran after an embedder tore down the view (e.g. Flutter or React Native platform views).
 
- Fixed a potential ANR when setting BannerView.placementId (including during Compose AndroidView composition). Banner resolution via Braze.getBanner now runs off the main thread; WebView updates still apply on the main thread.
 
- Fixed Braze.unregisterPush hanging when local SDK request rate limiting denied a send. Local rate-limit denial rejects enqueue (retriable failure, no HTTP status) instead of waiting for a token.
 
- Fixed an issue where Back callbacks from an In-App Message could remain registered after transitioning through a blocklisted Activity, causing Back navigation to be intercepted after the message was no longer visible.
 
- Fixed an issue where Banner test sends from the dashboard were not included in BannersUpdatedEvent published to Braze.subscribeToBannersUpdates() subscribers.
 
- Fixed an issue where sse connections wouldn’t check for expired auth tokens and could reconnect with a cached token that had already expired.
 
- Fixed an issue in the sse stream reader where a closed socket could cause heavy CPU usage until the stream timeout fired.
 
- Fixed an issue where a Content Cards full sync with only malformed cards could clear the local card cache. Cached cards are now preserved when a full sync contains no processable cards.
 
- Fixed Push Story left/right navigation failing when Push Max attached a push dedupe id (br_p_id).

##### Changed

- Updated the Android Gradle Plugin from 8.12.3 to 9.2.1.
 
- Migrated to AGP 9 built-in Kotlin and removed the separate kotlin-android / org.jetbrains.kotlin.android plugin.

## 43.0.0

Release Date

#### Breaking

- Renames ProductViewedEvent.typeIdentifiers to type.
 
- Added support for registering for Firebase Cloud Messaging using the Firebase Installation ID in version 25.1.0 and higher of the firebase-messaging library.

- To disable this feature, set com_appboy_firebase_cloud_messaging_registration_enabled to false in your appboy.xml file.
 
- The Braze SDK will automatically enable Firebase Cloud Messaging auto-initialization via the Firebase Installation ID. To disable this set <meta-data android:name="firebase_messaging_installation_id_enabled" android:value="false" tools:replace="android:value" /> in your AndroidManifest.xml file.
 
- If you are using a custom FirebaseMessagingService implementation, you will need to override the onRegistered method to handle the Firebase Installation ID and then call Braze.getInstance(context).registeredPushToken = installationId to register it with the Braze SDK.

##### Fixed

- Fixed an issue where setting a custom attribute with an array of JSON objects via the HTML In-App Message or Banner JS bridge would incorrectly store the elements as strings instead of structured objects. Arrays of objects passed to brazeBridge.getUser().setCustomUserAttribute() are now routed to the native setCustomUserAttribute(key, JSONArray) API, matching the behavior of the iOS SDK.
 
- Fixed a potential ANR in Card.logImpression() and Card.logClick() where synchronous disk I/O on the calling thread could block the main thread. Both operations are now dispatched asynchronously via BrazeCoroutineScope.
 
- Fixed an issue where HTML In-App Messages did not render correctly in edge-to-edge host activities when BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled() was enabled, leaving visible gaps around the WebView. When this setting is disabled, the SDK now injects system safe-area insets into the WebView as CSS custom properties (--braze-safe-area-inset-*) so HTML content can respect status bar, navigation bar, and display cutout areas. See #90 for details.
 
- Fixed an issue where HTML Full In-App Messages used WRAP_CONTENT height when added to the host view, preventing them from filling the screen.
 
- Fixed an issue where IInAppMessageManagerListener.beforeInAppMessageViewOpened() was not called after beforeInAppMessageDisplayed() when Braze.changeUser() and in-app message display overlapped.

##### Added

- Added Braze.unregisterPush / IBraze.unregisterPush to unregister this device’s push token with Braze.

- The API sends a single request to the push/unregister endpoint with no retry logic, adhering to global and per-endpoint rate limits.
 
- On success, the push token is cleared both locally and on the server.
 
- On failure, a BrazePushUnregistrationException is surfaced carrying an error message and an isRetriable flag so integrators can implement their own retry behavior.
 
- Both a suspending variant (suspend fun unregisterPush(), which throws BrazePushUnregistrationException on failure) and a callback variant (unregisterPush { result: Result<Unit> -> }) are available.

- Added Braze.logout / IBraze.logout to perform a full device logout.

- Flushes pending requests, unregisters push, then calls Braze.wipeData() and Braze.disableSdk() on success.
 
- On failure, a BrazePushUnregistrationException is surfaced and local data is not wiped nor the SDK disabled, so integrators can implement their own retry behavior.
 
- Both suspending and callback variants are available.

- Added optional subtotalValue, tax, and shipping fields to CartUpdatedEvent, CheckoutStartedEvent, and OrderPlacedEvent.

##### Changed

- Upgraded a broad set of third-party and AndroidX dependencies to their latest minSdkVersion 21-compatible releases, including Google Play Services, AndroidX (Core, Annotation, WebKit, Activity, DataStore, Navigation, Lifecycle), Jetpack Compose (BOM and runtime), Kotlin Coroutines, Robolectric, Mockito, and various utility libraries. These are maintenance updates that do not change the public API or the minimum supported SDK.
 
- Push notification image downloads now retry with exponential backoff (up to 3 attempts) using the SDK request-backoff settings when available. In-app message, Content Card, and other non-push image loads remain single-attempt. Failed push large-icon URL downloads now fall back to the configured drawable resource instead of setting a null bitmap.

## 42.3.1

Release Date

##### Fixed

- Fixed an issue where HTML In-App Messages displayed during an Activity transition could remain visible but not dismissable after carryover.

## 42.3.0

Release Date

#### Breaking

- BannerView: BannerDismissSnapshot fields passed to onDismissCallback are now non-null. If the SDK cannot resolve placementId, stableKey, or trackingId, the callback is skipped and a warning is logged.

##### Fixed

- Fixed the android-sdk-jetpack-compose Maven metadata to publish BOM-managed Compose dependencies, including androidx.compose.material:material, so ContentCardsList can resolve Material pull refresh classes without requiring apps to add Material 2 manually.
 
- Fixed a potential ANR when backgrounding the app while a default HTML In-App Message WebView is visible (for example when using BrazeActivityLifecycleCallbackListener with the default persist-WebView-on-background behavior). WebView.onPause() is now deferred until after onActivityPaused returns.

##### Added

- Banners: Added Braze.dismissBanner(placementId) / IBraze.dismissBanner to dismiss a Banner by placement ID programmatically.
 
- Added structured eCommerce event logging via IBraze.logEcommerceEvent / Braze.logEcommerceEvent with eCommerceEvent: EcommerceEvent. Includes EcommerceEvent, EcommerceProduct, and concrete events CheckoutStartedEvent, CartUpdatedEvent, OrderPlacedEvent, and ProductViewedEvent, with built-in field validation, ISO 4217 currency enforcement, and automatic serialization.

## 42.2.0

Release Date

##### Changed

- BannerView: onDismissCallback is now invoked with a single BannerDismissSnapshot argument (placementId, stableKey, and trackingId, each nullable when unknown) instead of a no-argument callback. Integrators must update assignments to use the new signature.
 
- Removed the hardcoded Toast shown by ContentCardsFragment when the network is unavailable, aligning with ContentCardsList (Jetpack Compose) which only logs. The empty-state view is still displayed. Integrators that want to surface a custom network-error UI should handle it at the app layer using their own connectivity signals.

## 42.1.0

Release Date

##### Added

- Added support for Android 17 (API 37).
 
- Added support for Banner Dismissal events.
 
- Added BannerView.onDismissCallback for integrators to run custom logic when a Banner is dismissed.

## 42.0.0

Release Date

#### Breaking

- Updated Kotlin from 2.0.20 to 2.2.20.

- Updated Kotlin Coroutines from 1.8.1 to 1.10.2.
 
- Updated Kotlin Serialization from 1.8.0 to 1.9.0.

##### Fixed

- Fixed an issue where non-HTML In-App Message view creation was dispatched to a background thread, causing an IllegalArgumentException when image loaders like Glide require the main thread. See #102 for details.
 
- Fixed an issue where in-app messages from a previous user session could be presented after changeUser() is called. On user change, the in-app message stack, event map, and any carryover or unregistered messages are now unconditionally cleared.
 
- Fixed an issue on API 36+ where pressing the Back button to dismiss an in-app message could also close the app or navigate back.
 
- Fixed an issue where expired Banners would be returned in Braze.subscribeToBannersUpdates().
 
- Fixed R8 optimized resource shrinking stripping custom res/values that Braze requires to operate when android.r8.optimizedResourceShrinking is enabled (Gradle 9.x). See #84 for details.
 
- Fixed an issue where setDateOfBirth accepted out-of-range or negative date values instead of rejecting them.
 
- Fixed a potential ANR when registering for Braze updates during Activity lifecycle (for example when using BrazeActivityLifecycleCallbackListener). That registration no longer blocks the UI thread.

##### Added

- Added a config field BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled() to configure the SDK to automatically apply window insets to HTML In-App messages.

- By default, this value is true.

- Added support for dismissing slideup in-app messages by vertical swipes. Slideups from the bottom can be dismissed by swiping down and slideups from the top can be dismissed by swiping up.

## 41.1.1

Release Date

##### Fixed

- Fixed an issue where calling wipeData() could result in SDK read/writes not working until the app was restarted.

- All data would still be properly wiped from storage after calls to wipeData().
 
- This issue would manifest as CancellationException or StorageException in logs and would not result in an app crash.

## 41.1.0

Release Date

##### Changed

- Updated the Coil library from 3.1.0 to 3.2.0.

## 41.0.0

Release Date

#### Breaking

- Renamed BrazeConfig.Builder.setIsLocationCollectionEnabled() to setIsAutomaticLocationCollectionEnabled().
 
- Renamed BrazeConfig.isLocationCollectionEnabled to isAutomaticLocationCollectionEnabled.
 
- Renamed BrazeConfigurationProvider.isLocationCollectionEnabled to isAutomaticLocationCollectionEnabled.

##### Fixed

- Fixed an issue where manual location tracking was being blocked by automatic location tracking.

- BrazeUser.setLastKnownLocation() now works independently of the automatic location collection setting. Customers can use automatic collection, manual tracking, both, or neither.

- Fixed a memory leak in the data persistence layer.

##### Changed

- Updated Coil library to Coil3.

## 40.2.0

Release Date

##### Fixed

- Fixed a potential memory leak in the activity lifecycle. See #86 for details.
 
- Fixed an issue when pressing the Back button from the Accessibility menu to dismiss an in-app message, occurring on Samsung devices running on Android 16 or higher.

## 40.1.1

Release Date

##### Fixed

- Fixed a potential memory leak in session management. See #86 for details.
 
- Fixed an issue with multiple sessions being opened when transparent activities are present.

## 40.1.0

Release Date

##### Fixed

- Fixed an error that could occur when a WebView failed to render correctly.
 
- Fixed an issue with location collection on pre-Android 11 devices.
 
- Fixed an issue that could cause an IAM with a deeplink click action to become unresponsive after being clicked.

##### Added

- Added the ability to call setGoogleAdvertisingId with null or a blank string in order to completely opt out users from ad tracking.

## 40.0.2

Release Date

##### Fixed

- Fixed an issue with com.braze.Braze.Companion#disableDelayedInitialization on low end devices.

## 40.0.1

Release Date

##### Changed

- Improved state management of the networking stack to be more efficient with requests after the app is resumed.

## 40.0.0

Release Date

#### Breaking

- Removed InAppMessageCloser.

- Use BrazeInAppMessageManager.hideCurrentlyDisplayingInAppMessage() to hide in-app messages and IInAppMessage#setAnimateOut() for controlling exit animations.

##### Fixed

- Fixed an issue where calls to wipeData() followed by enableSdk() could result in certain SDK data being unusable until the app was restarted.

- All data would still be properly wiped from storage after calls to wipeData().
 
- This issue would manifest as IllegalStateException: There are multiple DataStores active for the same file in logcat and would not result in an app crash.
 
- This issue does not result in any data loss.

- Fixed an issue where anonymous user transitions to identified users could cause SDK Auth errors when push token data was present.
 
- Fixed an issue where BrazeInAppMessageManager could misreport incoming in-app messages as not belonging to the current user after disabling and re-enabling the SDK.

##### Added

- Added IBraze.subscribeToChangeUserEvents().

##### Changed

- Removes DeviceKey.RESOLUTION.

## 39.0.0

Release Date

#### Breaking

- Changed the behavior of Braze.subscribeToContentCardsUpdates() to immediately return cached Content Cards after registering the subscriber.

##### Fixed

- Fixed a race condition in BrazeBootReceiver which could cause a crash upon SDK initialization.

##### Changed

- Increased the socket read timeout for all network requests to 25 seconds.

## 38.0.0

Release Date

#### Breaking

- Removed News Feed.

- Removed BrazeImageSwitcher, CardKey.Provider, and CardCategory.
 
- Card objects now only represent Content Cards.
 
- Removed Card.updated.
 
- Removed IBraze.logFeedDisplayed(), IBraze.requestFeedRefreshFromCache(), IBraze.requestFeedRefresh(), IBraze.subscribeToFeedUpdates(subscriber), IBraze.logFeedCardImpression(cardId), and IBraze.logFeedCardClick(cardId).
 
- Removed BrazeConfig.isNewsFeedVisualIndicatorOn.

##### Added

- Added support for delayed SDK initialization.

- To enable delayed initialization, call Braze.enableDelayedInitialization(context, analyticsBehavior).
 
- To disable delayed initialization, call Braze.disableDelayedInitialization(context).

- Added predictive back animations to full view in-app messages on gesture navigation modes on API 34+, and 3-button navigation modes on API 36+. See the Android 16 Documentation for more details.
 
- Moved the method internals of BrazeFirebaseMessagingService.onNewToken() to the companion object for easier behavior overriding.
 
- Added support for new Banner properties by adding the following methods:

- banner.getStringProperty(key) for accessing String properties.
 
- banner.getNumberProperty(key) for accessing Number properties.
 
- banner.getBooleanProperty(key) for accessing Boolean properties.
 
- banner.getJSONProperty(key) for accessing JSONObject properties.
 
- banner.getImageProperty(key) for accessing image URL properties as Strings.
 
- banner.getTimestampProperty(key) for accessing Unix UTC millisecond timestamp properties as Longs.

##### Changed

- Changed the behavior of templated In-App Messages to not automatically retry on endpoint errors to match the behavior of the iOS and Web SDKs.
 
- The default client-side rate limiting values for Banners refresh has been increased. For more information on SDK rate limiting, please refer to the Braze Developer Guide.

## 37.0.0

Release Date

#### Breaking

- Removed the config field BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled() and defaulted its behavior to true. The SDK will now unconditionally apply window insets to all HTML In-App Messages.
 
- Removed IBraze.requestContentCardsRefresh(boolean). Please instead use IBraze.requestContentCardsRefresh() and IBraze.requestContentCardsRefreshFromCache().
 
- Removed BrazeConfig.Builder.setDeviceObjectWhitelist(). Please use BrazeConfig.Builder.setDeviceObjectAllowlist() instead.
 
- Removed BrazeConfig.Builder.setDeviceObjectWhitelistEnabled(). Please use BrazeConfig.Builder.setDeviceObjectAllowlistEnabled() instead.
 
- Removed ContentCardsUpdatedEvent.getLastUpdatedInSecondsFromEpoch. Please instead use getTimestampSeconds()(Java) or timestampSeconds(Kotlin).
 
- Removed FeatureFlag.getTimestamp(key). Please use FeatureFlag.getTimestampProperty(key) instead.
 
- Removed BrazeWebViewClient.shouldInterceptRequest(view, url). Please use BrazeWebViewClient.shouldInterceptRequest(view, request) instead.
 
- Removed IBraze.getInstallTrackingId(). Please use IBraze.deviceId instead.

##### Fixed

- Fixed an issue where a LeakedClosableViolation would occur when disabling and re-enabling the SDK.
 
- Fixed an issue with Android TalkBack announcing “double tap to activate” on header and body text in In-App Messages.

##### Added

- Added support for Android 16 (API 36).

- Note that apps targeting API 36 should update to this SDK version.

- Added shutdown() to IBrazeImageLoader to allow for cleanup of resources.
 
- Improved accessibility support across In-App Messages and Content Cards by introducing alt text for images (by setting their content description).
 
- Added the ability to pass null to BrazeUser.setGender(gender) in order to unset the gender value.

##### Changed

- UriAction.openUriWithActionViewFromPush, UriAction.openUriWithWebViewActivity, and UriAction.openUriWithWebViewActivityFromPush are marked as open and can now be overridden.

## 36.0.0

Release Date

[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. Note that while we are re-introducing the ability to compile, we are not reintroducing formal support for <API 25, and cannot guarantee that the SDK will work as intended on devices running those versions.

If your app supports those versions, you should:

- Validate your integration of the SDK works as intended on physical devices (not just emulators) for those API versions.
 
- If you cannot validate expected behavior, you must either call disableSDK, or not initialize the SDK on those versions. Otherwise, you may cause unintended side effects or degraded performance on your end users’ devices.

#### Breaking

- Fixed an issue where In-App Messages would cause a read on the main thread.

- BrazeInAppMessageManager.displayInAppMessage is now a Kotlin suspend function.
 
- If you do not call this function directly, you do not need to make any changes.

- AndroidX Compose BOM updated to 2025.04.01 to handle updates in the Jetpack Compose APIs.

##### Fixed

- Fixed a potential issue where the SDK could incorrectly calculate in-flight In-App Message requests and prevent new In-App Messages from being triggered.
 
- Ensured that Content Cards, In-App Messages, Feature Flags, and Banners are cleared when calling Braze.wipeData().
 
- Set default background of BannerView to transparent.
 
- Fixed an issue where BrazeInAppMessageManager.activity would point to the previous activity when an Activity on the blocklist was active.
 
- Fixed an issue where In-App Messages would continue consuming predictive back callbacks after the message was dismissed/closed.

- For more detail: The predictive back callback not removed when the In-App Message was closed via the close button (or any other non-back dismissal method). This caused two back button invocations to be needed to trigger the host Activity/Fragment’s predictive back callback.

##### Added

- Added a parameter enablePullToRefresh to ContentCardsList in Jetpack Compose to allow for disabling pull-to-refresh behavior.

##### Changed

- Removed the deprecated announceForAccessibility in favor of accessibilityLiveRegion and contentDescription for accessibility TalkBack.
 
- Removed any displayed In-App Messages when calling Braze.changeUser().
 
- Modified BrazeActivityLifecycleCallbackListener to keep track of the latest activity in use.

- This is used to handle push permission prompts for various channels (ie. In-App Messages, Banners, etc).
 
- If you plan on using push permission prompts from a channel other than In-App Messages, you should make sure you’re registering BrazeActivityLifecycleCallbackListener in your Application class.

- Set allowFileAccess to false in BannerView.

## 35.0.0

Release Date

#### Breaking

- HTML In-App Messages will now persist the WebView when the app is put in the background.

- To disable this feature, use <bool name="com_braze_persist_webview_when_backgrounding_app">false</bool> in your braze.xml file.

- Removes the ability to control whether the SDK prevents showing In-App Messages to different users in certain edge cases.

- Removes the option to configure via braze.xml through <bool name="com_braze_prevent_in_app_message_display_for_different_user">true</bool>.
 
- Removes the option to configure via runtime configuration through BrazeConfig.setShouldPreventInAppMessageDisplayForDifferentUsers().
 
- The SDK will now always behave as if this configuration option were set to true.

##### Fixed

- Control banners will invoke bannerView.heightCallback with a value of 0.0. Previously it was not being called for control banners.
 
- Fixed an issue where sending a test banner from the dashboard would not update immediately.

##### Added

- Added the ability to get success and failure callbacks for BrazeUser.requestBannersRefresh().
 
- Allows user to subscribe to Banner update errors with Braze.subscribeToBannersErrors().

## 34.0.0

Release Date

#### Breaking

- Updated the minimum SDK version from 21 (Lollipop) to 25 (Nougat).

##### Added

- Adds BrazeNotificationPayload.isSilentPush to check if a notification payload is a silent push.
 
- Adds BrazeUser.setLineId(String) to set the LINE ID of a user.

- Adds brazeBridge.getUser().setLineId(String) to the javascript interface for HTML In-App Messages and Banners.

- Added the ability to forcibly pad In-App Messages with the height of the status bar.

- Configured via braze.xml through <bool name="com_braze_in_app_message_add_status_bar_padding">true</bool>.
 
- Can also be configured via runtime configuration through BrazeConfig.setShouldAddStatusBarPaddingToInAppMessages().
 
- Defaults to false. You should not change this value unless you’re seeing issues with In-App Messages close button being obscured by the status bar when using a cross-platform framework like React Native or Flutter.

- Added a callback in BannerJavascriptInterface for dynamically setting the height of a Banner.

#### Fixed

- Fixed an issue where automatic location collection being disabled would also disable Geofences.

## 33.1.0

Release Date

##### Fixed

- Fixed an issue where ContentCardsFragment would not show the empty state if the user had only control cards.

##### Added

- Adds support for the Braze Banner Cards product.
 
- Added BrazeWebViewClient to facilitate the creation of WebViewClients in Banners and In-App Messages.

- Added BannerWebViewClient, which extends BrazeWebViewClient.
 
- InAppMessageWebViewClient now extends BrazeWebViewClient.

- Added JavascriptInterfaceBase to simplify the creation of JavaScript interfaces for Banners and In-App Messages.

- Added BannerJavascriptInterface, which extends JavascriptInterfaceBase.
 
- InAppMessageJavascriptInterface now extends JavascriptInterfaceBase.

- Added IBannerWebViewClientListener interface for Banner WebViewClient listeners.
 
- Added an optional button id parameter to IInAppMessage.logClick.

##### Changed

- Changed the location of brazeBridge to be located in file braze-html-bridge.js. brazeBridge is now accessible in both Banners and In-App Messages.

- braze-html-in-app-message-bridge.js is now deprecated and will be removed in a future version of the SDK, in favor of braze-html-bridge.js.

- Changed properties in AttributionData from non-nullable to nullable to allow for optional values.

## 33.0.0

Release Date

##### Breaking

- Updated Kotlin from 1.8 to Kotlin 2.0.

##### Fixed

- Braze HTML In-App Message bridge method incrementCustomUserAttribute() will use the provided value as the increment amount instead of always incrementing by 1.
 
- Fixed an issue where In-App Message text alignments would not match what was set in the dashboard in some cases.

- Removed android:supportsRtl="true" from android-sdk-ui AndroidManifest.xml. You should have this in your application AndroidManifest.xml.
 
- Removed android:textAlignment="viewStart" from the In-App Message layouts, since this is sent by the server.

- Fixed an issue where Content Cards and Feature Flags were not refreshing after a session started due to a session timeout.
 
- Fixed an issue with SDK Authentication where tokens that expired and refreshed mid session would be treated as failed.

##### Changed

- Braze HTML In-App Message bridge method will now also accept strings for incrementCustomUserAttribute(), setDateOfBirth(), setCustomLocationAttribute(), and logPurchase().

## 32.1.0

Release Date

##### Fixed

- Fixed an issue where geofence events could not be sent when the app is in the background.
 
- Fixed an issue where In-App Messages would fail to be dismissed when the host app is using the predictive back gesture.

##### Added

- Added support for an upcoming Braze SDK Debugging tool.
 
- Added the ability to prevent certain edge cases where the SDK could show In-App Messages to different users than the one that triggered the In-App Message.

- Configured via braze.xml through <bool name="com_braze_prevent_in_app_message_display_for_different_user">true</bool>.
 
- Can also be configured via runtime configuration through BrazeConfig.setShouldPreventInAppMessageDisplayForDifferentUsers().
 
- Defaults to false. Note that even when false, the SDK will still prevent most cases of showing In-App Messages to different users. This configuration option is designed to prevent edge cases such as when the user changes while on a BrazeActivityLifecycleCallbackListener blocked Activity or when a mismatched message is still in the stack.

##### Changed

- Changed the behavior of the Braze.getDeviceId() method to return a different device ID based on the API key used to initialize the SDK.

## 32.0.0

Release Date

##### Breaking

- Fixed issue where cards with duplicate IDs would cause a crash in Jetpack Compose Content Cards.

- If you manually add cards, please ensure that they have unique IDs.

##### Fixed

- Fixed an issue where closing an In-App Message could throw an error if the previously focused View was removed.
 
- Fixed an issue where some In-App Messages could display after their expiration time.
 
- Fixed an issue with In-App Message and Content Cards not displaying RTL language properly.
 
- Fixed an issue where logging In-App Message impression or clicks could result in blocking the main thread.

##### Added

- Added support for Android 15 (API 35).

- Note that apps targeting API 35 should update to this SDK version.

##### Changed

- Changed the behavior of Braze.wipeData() to retain external subscriptions (like Braze.subscribeToContentCardsUpdates()) after being called.

## 31.1.0

Release Date

##### Fixed

- Added getTimestampProperty(key) to FeatureFlag and deprecated getTimestamp(key) for consistency.

##### Added

- Added Azerbaijani language translations for Braze UI elements.

## 31.0.0

Release Date

#### Breaking

- BrazeImageUtils::getBitmap now returns a BitmapAndHeaders object instead of just a Bitmap. This object contains the Bitmap and headers from the image download network request.

- Custom Image Loaders that have used code from DefaultBrazeImageLoader may need to update their code to handle the new return type.

##### Fixed

- Fixed the potential for ViewUtils.removeViewFromParent to cause a crash.
 
- Fixed an issue where an HTML In-App Message could crash if a bad external link had a query parameter of target="_blank". Thanks to @chenxiangcxc for finding the issue.
 
- Fixed an issue where images would be cached when the HTTP headers indicated they shouldn’t be cached.
 
- Fixed an issue where some liquid templated images would not have the proper aspect ratio.

##### Added

- Added support for new Feature Flag property types by adding getJsonProperty(key), getImageProperty(key), and getTimestampProperty(key) to FeatureFlag.

##### Changed

- Removed @Synchronized from Brazelogger in order to eliminate noisy thread deadlock logs.

## 30.4.0

Release Date

##### Fixed

- Fixed an issue with com.braze.support.DateTimeUtils.nowInMilliseconds() where, in the event of the device network time clock not being available, the SDK would continually log about the error.

##### Added

- Adds support for the message_extras Liquid tag for in-app messages.

## 30.3.0

Release Date

##### Added

- Added the fields responseCode, responseHeaders, requestUrl to BrazeNetworkFailureEvent.

## 30.2.0

Release Date

##### Added

- Introduces out-of-the-box Jetpack Compose support for Content Cards. Add the com.braze:android-sdk-jetpack-compose module to your build.gradle if you would like to use this feature.

## 30.1.1

Release Date

##### Fixed

- Fixed an issue where the SDK would fail to unregister session seal broadcast receivers.

- The intent action is suffixed with .intent.BRAZE_SESSION_SHOULD_SEAL.

## 30.1.0

Release Date

##### Added

- Added the ability to configure whether SDK created Activities (such as ContentCardsActivity, BrazeWebViewActivity, etc.) use the WindowManager.LayoutParams.FLAG_SECURE to prevent screen capturing.

- Configured via braze.xml through <bool name="com_braze_use_activity_window_flag_secure">true</bool>.
 
- Can also be configured via runtime configuration through BrazeConfig.setShouldUseWindowFlagSecureInActivities().
 
- Defaults to false.

## 30.0.0

Release Date

#### Breaking

- WebViews used for In-App Messages have been updated to use WebViewAssetLoader.

- WebSettings.allowFileAccess is now set to false in InAppMessageHtmlBaseView and BrazeWebViewActivity.
 
- If you are overriding InAppMessageWebViewClient and/or InAppMessageHtmlBaseView, please compare against the original classes to make sure your implementation is correctly loading the assets.
 
- If you are not overriding InAppMessageWebViewClient or InAppMessageHtmlBaseView, everything will work as before.
 
- If you are not using custom classes, everything will work as before.

##### Fixed

- Fixed an issue where ImageView.setBitmap was being called on a non-UI thread, causing CalledFromWrongThreadException.
 
- Fixed an issue where a StrictMode DiskReadViolation would occur when displaying an In-app Message. Thanks to @auxDK for finding the issue.

##### Added

- Added BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(Context, BrazePushEvent) to process events when using Braze.subscribeToPushNotificationEvents.

- See /samples/firebase-push.

- Added the ability to configure whether a user’s notification subscription state should automatically be set to OPTED_IN when push permissions are granted.

- Configured via braze.xml through <bool name="com_braze_optin_when_push_authorized">true</bool>.
 
- Can also be configured via runtime configuration through BrazeConfig.setOptInWhenPushAuthorized().
 
- Defaults to true. This was the previous behavior.

## 29.0.1

Release Date

##### Fixed

- Fixed an issue where Content Cards saved directly to storage via API triggered campaigns could be purged after syncs.
 
- Fixed an issue with the default Content Card feed where images provided without default aspect ratios would display with the wrong dynamic aspect ratio.

## 29.0.0

Release Date

##### Breaking

- Renamed BannerImageCard, BannerImageCardView, and BannerImageContentCardView to ImageOnlyCard, ImageOnlyCardView, and ImageOnlyContentCardView.
 
- All styles used for Banner Cards have been updated to Image Only Cards. All keys with the word banner should be replaced with image_only.
 
- Device brand information is now sent. If you want to block this, see Blocking data collection.

##### Fixed

- Fixed an issue where NotificationTrampolineActivity would sometimes appear in the list of recent tasks.

##### Added

- Braze HTML In-App Message bridge method setCustomUserAttribute() will now accept a JSON Object as the value.

- When passing a JSON Object, you can pass a third parameter of ‘true’ that will merge the JSON Object with the existing value.

- Adds a new option REENQUEUE to enum InAppMessageOperation.

- Return this option in IInAppMessageManagerListener.beforeInAppMessageDisplayed to ensure that an in-app message is not displayed and is simply re-enqueued.
 
- This option will reset any trigger times and re-eligibility rules as if it was never triggered. It will not add the message to the In-App Message stack.

## 28.0.0

Release Date

#### Breaking

- Updated minimum SDK version to 21 (Lollipop).
 
- Feature Flags functions have been modified.

- Braze.getFeatureFlag(id) will now return null if the feature flag doesn’t exist.
 
- Braze.subscribeToFeatureFlagsUpdates() will only callback when a refresh request completes, and initially if previously cached data exists. It will also be called with cached feature flags for any refresh failures.

- If you want the cached value immediately at app startup, use Braze.getFeatureFlag(id).

- Refactored DefaultInAppMessageViewWrapper.createButtonClickListener() into DefaultInAppMessageViewWrapper.createButtonClickListeners().

##### Fixed

- Fixed an issue where Firebase fallback service had a null Context.
 
- Fixed an issue where calling requestPushPermission() before closeMessage() in the HTML bridge could result in the HTML IAM remaining in the view hierarchy.
 
- Fixed an issue where Braze.removeSingleSubscription() wouldn’t remove synchronous subscriptions, resulting in memory leaks with ContentCardsFragment.

##### Changed

- DefaultContentCardHandler will sort by Card.id if both Card.isPinned and Card.created are equal.

## 27.0.1

##### Fixed

- Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on openSession calls. Customers on v27.0.0 are strongly encouraged to upgrade.

## 27.0.0

Release Date

⚠️ This version has a known issue. Please upgrade to v33.0.0.

#### Breaking

- Removed IInAppMessage.logDisplayFailure().

##### Fixed

- Fixed the behavior of HTML In-App messages to restrict remote navigation inputs to their display WebView during message display on non touch-mode devices.

## 26.3.2

##### Fixed

- Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on openSession calls. Customers on v26.3.0 and v26.3.1 are strongly encouraged to upgrade.

## 26.3.1

Release Date

⚠️ This version has a known issue. Please upgrade to v33.0.0.

##### Fixed

- Internal bug fixes for an upcoming Braze push feature.

## 26.3.0

Release Date

⚠️ This version has a known issue. Please upgrade to v33.0.0.

##### Added

- Added the ability to forward Firebase push notifications to FirebaseMessagingService implementations if that push notification is not a Braze notification.

- Configured via runtime configuration through BrazeConfig.setFallbackFirebaseMessagingServiceEnabled() and BrazeConfig.setFallbackFirebaseMessagingServiceClasspath()
 
- Can also be configured via braze.xml through <bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool> and <string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>.
 
- Defaults to false.

## 26.2.1

⚠️ This version has a known issue. Please upgrade to v33.0.0.

##### Fixed

- Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on openSession calls. Customers on v26.2.0 are strongly encouraged to upgrade.

## 26.2.0

Release Date

⚠️ This version has a known issue. Please upgrade to v33.0.0.

##### Fixed

- Fixed an issue with Unity not properly forwarding messages to the Braze Unity internal layer for In-App Message events.
 
- Fixed an issue on Android 13+ devices where push subscriptions would be set to OPTED_IN on every session after the user granted push permissions. Now, the SDK sets the user to OPTED_IN only once immediately after the user grants push permissions.

##### Changed

- Deprecated IBraze.requestContentCardsRefresh(boolean) in favor of IBraze.requestContentCardsRefresh() and IBraze.requestContentCardsRefreshFromCache().

## 26.1.1

⚠️ This version has a known issue. Please upgrade to v33.0.0.

##### Fixed

- Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on openSession calls. Customers on v26.1.0 are strongly encouraged to upgrade.

## 26.1.0

Release Date

⚠️ This version has a known issue. Please upgrade to v33.0.0.

##### Important

- This release includes support for Android 14 (Upside Down Cake / API 34).

##### Added

- Added verticalAccuracy to location information.

- BrazeUser.setLastKnownLocation now accepts verticalAccuracy.
 
- Updates through Braze location APIs will automatically include verticalAccuracy if the device supports it.

##### Changed

- Changed target API for the SDK to 34.

## 26.0.0

Release Date

#### Breaking

- Added the ability to configure link target behavior for HTML In-App Messages through BrazeConfig.setIsHtmlInAppMessageHtmlLinkTargetEnabled() or via adding <bool name="com_braze_html_in_app_message_enable_html_link_target">true</bool> to your braze.xml. Defaults to enabled.

- When enabled, a link in an In-App Message that has the link target set (e.g. <a HREF="https://www.braze.com" target="_blank">Please Read</a>) will open the link in a browser, but will not close the In-App Message.

##### Fixed

- Fixed an issue where a slideup In-App Message would not be auto-dismissed if the user interacted with it.
 
- Fixed an issue where a user’s push subscription state changed to “subscribed” instead of “opted in” upon accepting the Android 13+ push prompt.

## 25.0.0

Release Date

### Important

Our SDK is now hosted in Maven Central. You can remove https://braze-inc.github.io/braze-android-sdk/sdk from your build.gradle and make sure you have mavenCentral() as a repository.

##### Added

- Added BrazeLogger.enableVerboseLogging() to more easily enable verbose logs.
 
- Added Braze.getDeviceIdAsync() which allows for asynchronously retrieving the Braze device identifier.
 
- Added com.braze.events.IFireOnceEventSubscriber to provide the ability to listen to Braze updates with a fire-only-once guarantee.

```

1
2
3

```
 | 
```
Braze.getInstance(context).subscribeToContentCardsUpdates(IFireOnceEventSubscriber {
 // Only fires once
})

```
 | 

- Updated BrazeUser.setCustomUserAttribute() to now accept nested custom attributes and arrays of objects. Please see our public docs for more information.

## 24.3.0

Release Date

##### Fixed

- Fixed an issue where the SDK would attempt to to access the visual service WindowManager from non-visual contexts, resulting in benign StrictMode errors.
 
- Added @JvmStatic to com.braze.push.BrazeHuaweiPushHandler.handleHmsRemoteMessageData().
 
- Fixed an issue where notification extra data was not being passed along in Push Story main image clicks.
 
- Fixed an issue where ContentCardAdapter was not properly handling bad indexes being passed in.
 
- Fixed an issue where a user’s push subscription state would not change to “opted in” upon accepting the Android 13+ push prompt.

##### Added

- Added the ability to configure dismissal of Push Stories on click by adding BrazeConfig.setDoesPushStoryDismissOnClick() or <bool name="com_braze_does_push_story_dismiss_on_click">true</bool> to your braze.xml. Defaults to true.

## 24.2.0

Release Date

##### Added

- Added support for the upcoming Braze Feature Flags product.

##### Changed

- Changed the default behavior for images to more aggressively sample large images.

- Images will be sampled until their effective bitmap size (i.e. W x H x 4 bytes) is below 16 MB.
 
- Images will be sampled until both (and not either) the half-width and half-height of the image is less than or equal to the image destination dimensions.

- Changed the behavior of failed Content Card requests to automatically retry on server 500 errors and SDK Authentication errors.

## 24.1.0

Release Date

##### Added

- Added BrazeActivityLifecycleCallbackListener.registerOnApplication() which allows for registering the lifecycle callback listener from any Context.

## 24.0.0

Release Date

#### Breaking

- Location and geofence functionality has moved to a new module called com.braze:android-sdk-location. Add this module to your build.gradle if you are using Braze location functionality.
 
- Deprecated classes starting with Appboy have now been removed.
 
- Moved com.appboy packages to com.braze.
 
- All xml classes and values in them have been changed from appboy to braze. All custom code should be updated accordingly.
 
- BrazeNotificationUtils.isAppboyPushMessage() removed. Please use instead:

- Java: BrazeNotificationUtils.isBrazePushMessage(Intent)
 
- Kotlin: Intent.isBrazePushMessage()

- APPBOY_NOTIFICATION_OPENED_SUFFIX, APPBOY_NOTIFICATION_RECEIVED_SUFFIX, and APPBOY_NOTIFICATION_DELETED_SUFFIX are removed.

- Instead, please use Braze.getInstance(context).subscribeToPushNotificationEvents()

- Updated the minimum version of com.google.android.gms:play-services-location required for Braze Geofences to 20.0.0.

##### Added

- Added the ability to optionally pipe Braze logcat from BrazeLogger to a custom callback via BrazeLogger.onLoggedCallback.

```

1
2
3

```
 | 
```
 BrazeLogger.onLoggedCallback = fun(priority: BrazeLogger.Priority, message: String, throwable: Throwable?) {
 // Custom callback logic here
 }

```
 | 

```

1
2
3
4

```
 | 
```
 BrazeLogger.setOnLoggedCallback((priority, s, throwable) -> {
 // Custom logic here
 return null;
 });

```
 | 

##### Changed

- Removed BrazeUser.setFacebookData() and BrazeUser.setTwitterData().
 
- Changed the default behavior of DefaultContentCardsUpdateHandler to use the creation time vs last update time when sorting Content Cards.

## 23.3.0

Release Date

##### Fixed

- Fixed the behavior of the Braze HTML In-App Message bridge method requestPushPermission() to not cause the in-app message to reload.
 
- Fixed com.braze.ui.inappmessage.views.InAppMessageImageView to guard against null values of InAppMessageImageView.inAppRadii.

##### Changed

- Removed com.appboy.ui.inappmessage.IInAppMessageViewWrapperFactory. Please use com.braze.ui.inappmessage.IInAppMessageViewWrapperFactory.
 
- Changed com.braze.ui.inappmessage.views.InAppMessageFullView.getMessageClickableView to be nullable.

## 23.2.1

Release Date

##### Fixed

- Fixed the fields of DefaultInAppMessageViewWrapper to be open, allowing them to be subclassed in Kotlin properly.

## 23.2.0

Release Date

##### Fixed

- Fixed the fields of DefaultInAppMessageViewWrapper to be protected, allowing them to be subclassed.
 
- Fixed BrazeNotificationPayload and BrazePushReceiver to not hold onto an Activity context for longer than needed.

##### Added

- Added a config field BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled() to configure the SDK to automatically apply window insets to HTML In-App messages.

- By default, this value is false.

- Added subscribeToNoMatchingTriggerForEvent which is called if no Braze in-app message was triggered for a given event.

##### Changed

- Removed com.appboy.ui.inappmessage.listeners.IInAppMessageWebViewClientListener. Please use com.braze.ui.inappmessage.listeners.IInAppMessageWebViewClientListener.
 
- Removed AppboyInAppMessageHtmlBaseView.APPBOY_BRIDGE_PREFIX. Please use InAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX.

## 23.1.2

Release Date

##### Changed

- Removed the use of the Kotlin Coroutines method limitedParallelism().

## 23.1.1

Release Date

##### Fixed

- Fixed the DefaultInAppMessageViewWrapper to be Kotlin open, allowing it to be subclassed.

## 23.1.0

Release Date

##### Added

- Added more reliable HTML In-App Message focusing specifically for TV environments. To use this behavior please set com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages to false.
 
- Added BrazeNotificationPayload.extras as a Map<String, String> to easily retrieve dashboard provided KVPs for push notification data.
 
- Added support for Content Cards to evaluate Retry-After headers.

## 23.0.1

Release Date

##### Fixed

- Fixed an issue where BaseCardView would sometimes have the wrong size for a given image.

##### Changed

- Added proguard rules to keep enum.values() and enum.valueOf(String) for users who don’t use the default Android proguard rules.

## 23.0.0

Release Date

#### Breaking

- BaseContentCardView.bindViewHolder() now takes Card instead of generic type.

##### Fixed

- Fixed an issue where apps with a target of Android 12 running on Android 13 devices would not automatically create a default notification channel upon a push notification being received.

##### Added

- Added ability to retrieve deeplinks from BrazeNotificationPayload objects via BrazeNotificationPayload().deeplink.

## 22.0.0

Release Date

#### Breaking

- Appboy.java is now Braze.kt. Kotlin clients will need to update their code to support the use of Kotlin properties on the Braze singleton where needed.

- Braze.registerPushToken()/Braze.getRegisteredPushToken() is now Braze.setRegisteredPushToken()/Braze.getRegisteredPushToken(). If using Kotlin, use the property Braze.registeredPushToken.
 
- Braze.getDeviceId is now just Braze.deviceId for Kotlin.
 
- Braze.enableMockNetworkAppboyRequestsAndDropEventsMode is now Braze.enableMockNetworkRequestsAndDropEventsMode().
 
- Appboy.java has been removed. For example, calls like Appboy.getInstance() will need to be Braze.getInstance() moving forward.
 
- Replaced setCustomAppboyNotificationFactory() with setCustomBrazeNotificationFactory() / customBrazeNotificationFactory.
 
- Renamed enableMockAppboyNetworkRequestsAndDropEventsMode to enableMockNetworkRequestsAndDropEventsMode.

- Moved com.appboy.IBrazeEndpointProvider to com.braze.IBrazeEndpointProvider.
 
- Renamed com.appboy.events.IEventSubscriber to com.braze.events.IEventSubscriber.
 
- Removed Appboy.registerAppboyPushMessages() / Appboy.getAppboyPushMessageRegistrationId(). Replaced with getRegisteredPushToken() / setRegisteredPushToken().
 
- Replaced IAppboyNotificationFactory with IBrazeNotificationFactory.

##### Fixed

- Fixed an issue in BrazePushReceiver where eager In-App Message test displays and Content Card serializations from push notifications wouldn’t work unless notifications were enabled on the device.
 
- Fixed an issue where devices between the API 19 up to API 29 would not perform automatic data syncs in some cases.
 
- Fixed an issue where carryover in-app messages wouldn’t display on subsequent Views on new Activities.
 
- Fixed an issue where some long running In-App Message HTML WebViews would call View methods on non UI threads.

##### Added

- Added IBraze.subscribeToPushNotificationEvents() to allow for subscriptions to push notification events without the use of a BroadcastReceiver.

- Recommended to be placed in your Application.onCreate().

##### Changed

- Changed com.braze.models.outgoing.BrazeProperties.clone() to return BrazeProperties?.

## 21.0.0

Release Date

##### Important

- This release includes support for Android 13 (Tiramisu / API 33).

#### Breaking

- Removed IAppboy.logContentCardsDisplayed. This method was not part of the recommended Content Cards integration and can be safely removed.

##### Changed

- Changed target API for the SDK to 33.

## 20.0.0

Release Date

#### Breaking

- Changed BrazeNotificationStyleFactory to remove deprecated functions.

- Removed BrazeNotificationStyleFactory.getBigNotificationStyle(Context, Bundle, Bundle, NotificationCompat.Builder). Use BrazeNotificationStyleFactory.getNotificationStyle(NotificationCompat.Builder, BrazeNotificationPayload) instead.
 
- Removed BrazeNotificationStyleFactory.getBigTextNotificationStyle(BrazeConfigurationProvider, Bundle). Use BrazeNotificationStyleFactory.getBigTextNotificationStyle(BrazeNotificationPayload) instead.
 
- Removed BrazeNotificationStyleFactory.getStoryStyle(Context, Bundle, Bundle, NotificationCompat.Builder). Use BrazeNotificationStyleFactory.getStoryStyle(NotificationCompat.Builder, BrazeNotificationPayload) instead.

- Changed BrazeNotificationActionUtils to remove deprecated functions.

- Removed BrazeNotificationActionUtils.addNotificationActions(Context, NotificationCompat.Builder, Bundle). Use BrazeNotificationActionUtils.addNotificationActions(NotificationCompat.Builder, BrazeNotificationPayload) instead.
 
- Removed BrazeNotificationActionUtils.addNotificationAction(Context, NotificationCompat.Builder, Bundle, Int). Use BrazeNotificationActionUtils.addNotificationAction(BrazeNotificationPayload.ActionButton) instead.
 
- Removed AppboyNotificationActionUtils. Use BrazeNotificationActionUtils instead.

- Removed AppboyHuaweiPushHandler. Use BrazeHuaweiPushHandler instead.
 
- Removed AppboyFirebaseMessagingService. Use BrazeFirebaseMessagingService instead.
 
- Removed AppboyAdmReceiver. Use BrazeAmazonDeviceMessagingReceiver instead.
 
- BrazeFirebaseMessagingService.handleBrazeRemoteMessage() and BrazeFirebaseMessagingService.isBrazePushNotification() now require non-null parameters.
 
- UriAction.channel is now Channel.CONTENT_CARD for actions that originate from a Content Card instead of Channel.NEWS_FEED.

##### Fixed

- Fixed an issue that would prevent SDK Authentication errors from being retried.

##### Added

- Modified BrazeProperties.addProperties() to allow adding nested properties via JSONObject or Map<String, *>.
 
- Added support for Braze Action Deeplink Click Actions.

##### Changed

- Slideup messages now have a maximum width of 450dp. This can be adjusted by modifying @dimen/com_braze_inappmessage_slideup_max_width.
 
- Added com.braze.Constants with constants starting with “BRAZE_” that replace the corresponding “APPBOY_” constants in com.appboy.Constants. The “APPBOY_” constants are deprecated and will be removed in a future release.

## 19.0.0

##### Important

- It is highly recommended to include the compiler flag -Xjvm-default=all in your Gradle build options due to the new use of default arguments in the SDK. Without this flag, you may see a compiler warning about “Inheritance from an interface with ‘@JvmDefault’ members”. An example is included below:

```

1
2
3
4
5
6

```
 | 
```
 android {
 kotlinOptions {
 freeCompilerArgs = ['-Xjvm-default=all']
 jvmTarget = "1.8"
 }
 }

```
 | 

Release Date

##### ⚠ Breaking

- Modified behavior of BrazeProperties(JSONObject) when Date is part of JSONObject.

- Previously, Date objects in the JSONObject would be converted with the Date.toString() (e.g. “Thu Jan 01 03:15:33 CST 1970”).
 
- Date objects in the JSONObject are now converted to BrazeDateFormat.LONG (e.g. “1970-01-01 09:15:33”). This behavior is consistent with BrazeProperties.addProperty(Date).

- Converted IInAppMessage to Kotlin and changed several methods to no longer allow for null inputs or return boolean statuses on field setters.

- IInAppMessage.setClickAction() is renamed to setClickBehavior() and now returns void.
 
- MessageButton.setClickAction() is renamed to setClickBehavior() and now returns void.
 
- InAppMessageImmersiveBase.setMessageButtons() no longer accepts null. Pass in an empty list to clear.

- Converted Card to Kotlin, so JVM signatures may have changed.

- Removed Card.isEqualToCard(). Please use card.equals(otherCard) instead.
 
- Removed Card.isRead() and Card.setIsRead(). Please use Card.isIndicatorHighlighted (Kotlin) or Card.isIndicatorHighlighted() and Card.setIndicatorHighlighted() (Java).

- Removed com.appboy.AnimationUtils, com.appboy.ViewUtils, com.appboy.UriUtils, com.appboy.IAction, com.appboy.NewsfeedAction and com.appboy.UriAction classes. The Braze namespaced classes remain.
 
- BrazeDeeplinkHandler.createUriActionFromUrlString() and BrazeDeeplinkHandler.createUriActionFromUri() now require non-null values for uri/url and channel.

- AppboyNavigator has been removed in favor of BrazeDeeplinkHandler.

- Removed AppboyNotificationUtils in favor of BrazeNotificationUtils.
 
- Removed AppboyLifecycleCallbackListener. Please use BrazeActivityLifecycleCallbackListener.

- Removed BrazeLifecycleCallbackListener.setInAppMessagingRegistrationBlacklist() in favor of BrazeLifecycleCallbackListener.setInAppMessagingRegistrationBlocklist(). Removed BrazeLifecycleCallbackListener.setSessionHandlingBlacklist() in favor of BrazeLifecycleCallbackListener.setSessionHandlingBlocklist().

- Removed AppboyContentCardsManager. Please use BrazeContentCardsManager instead.
 
- Removed AppboyEmptyContentCardsAdapter. Please use EmptyContentCardsAdapter instead.
 
- Removed BrazeUser.setAvatarImageUrl(String).

##### Fixed

- Fixed the startup behavior of the SDK to not perform caller thread blocking operations when setting up SharedPreferences and other disk reading I/O.
 
- Fixed a potential issue where the default implementation of Webview.onRenderProcessGone() could lead to app crashes. Thanks to @ankitsingh08 for finding the issue.

##### Changed

- Added BrazeProperties(Map<String, *>) constructor.
 
- Changed Appboy.getConfiguredApiKey() to accept a BrazeConfigurationProvider instead of a Context object.
 
- Deprecated AppboyBootReceiver. Please use BrazeBootReceiver instead.
 
- Deprecated APPBOY_WEBVIEW_URL_EXTRA. Please use BRAZE_WEBVIEW_URL_EXTRA instead.
 
- Changed the SDK to not wake the screens of Configuration.UI_MODE_TYPE_TELEVISION devices when receiving push notifications.

- These screen types will not be awoken even if isPushWakeScreenForNotificationEnabled() is true and the permission Manifest.permission.WAKE_LOCK is granted.
 
- Special thanks to @IanGClifton for https://github.com/braze-inc/braze-android-sdk/pull/213.

## 18.0.1

Release Date

##### Fixed

- Fixed an issue introduced in 17.0.0 where some HTML In-App Message zip asset files containing hidden __MACOSX folders without a corresponding entry for that folder would cause the in-app message to fail to display.

## 18.0.0

##### Important

- It is highly recommended to include the compiler flag -Xjvm-default=all in your Gradle build options due to the new use of default arguments in the SDK. Without this flag, you may see a compiler warning about “Inheritance from an interface with ‘@JvmDefault’ members”. An example is included below:

```

1
2
3
4
5
6

```
 | 
```
 android {
 kotlinOptions {
 freeCompilerArgs = ['-Xjvm-default=all']
 jvmTarget = "1.8"
 }
 }

```
 | 

Release Date

This version has a known issue with HTML In-App Message which was fixed in v18.0.1

##### ⚠ Breaking

- Removed AppboyLruImageLoader in favor of DefaultBrazeImageLoader.

- com.appboy.lrucache.AppboyLruImageLoader -> com.braze.images.DefaultBrazeImageLoader.
 
- com.appboy.Appboy.getAppboyImageLoader -> com.appboy.Appboy.getImageLoader.
 
- com.appboy.Appboy.setAppboyImageLoader -> com.appboy.Appboy.setImageLoader.

- Removed IAppboyEndpointProvider in favor of IBrazeEndpointProvider.

- If using Braze.setAppboyEndpointProvider() please use Braze.setEndpointProvider().

##### Fixed

- Fixed an issue introduced in 15.0.0 where Full in-app messages on tablets may have had an incorrect background color.

##### Added

- Added the ability to change SDK authentication signature with Braze.changeUser() when the current user id and a new signature is passed in.

- Previously, Braze.changeUser() would not change the SDK authentication signature if the current user id was used.

##### Changed

- InAppMessageCloser is deprecated.

- Use BrazeInAppMessageManager.hideCurrentlyDisplayingInAppMessage() to hide currently displayed in-app messages.
 
- Use IInAppMessage.setAnimateOut() to set whether your in-app message should animate on close.
 
- New version of IInAppMessageManagerListener.onInAppMessageClicked() and IInAppMessageManagerListener.onInAppMessageButtonClicked() that don’t use InAppMessageCloser have been added.

- If you override the deprecated functions that use InAppMessageCloser, those will be called.
 
- If you override the new functions and don’t override the deprecated functions, the new functions will be called.

- Deprecated ContentCardsUpdatedEvent.getLastUpdatedInSecondsFromEpoch.

- Use getTimestampSeconds() (Java) or timestampSeconds (Kotlin).

## 17.0.0

Release Date

:warning: This version has a known issue with HTML In-App Message which was fixed in v18.0.1

##### ⚠ Breaking

- BrazeLogger.setLogLevel() replaced with direct property setter BrazeLogger.logLevel for Kotlin.
 
- Removed AppboyLogger, com.appboy.IntentUtils, com.appboy.StringUtils class. The Braze namespaced classes remain.
 
- Removed com_braze_locale_api_key_map as a configuration option and BrazeConfig.setLocaleToApiMapping(). If you need to change your API key based on locale, please use BrazeConfig at runtime instead.

##### Added

- Added Braze.isDisabled() to determine whether the SDK is disabled.
 
- Added Braze.addSdkMetadata() to allow self reporting of SDK Metadata fields via the BrazeSdkMetadata enum.

- Fields may also be added via a string-array to your braze.xml with the key com_braze_sdk_metadata. The allowed items are the same as the keys found in the BrazeSdkMetadata enum. For example when using Branch:

```

1
2
3

```
 | 
```
<string-array name="com_braze_sdk_metadata">
 <item>BRANCH</item>
</string-array>

```
 | 

- Fields are additive across all reporting methods.

## 16.0.0

Release Date

##### ⚠ Breaking

- Removed AppboyConfigurationProvider in favor of BrazeConfigurationProvider.

- Any deprecated usages, such as in the IBrazeNotificationFactory have also been removed.

##### Fixed

- Fixed an issue introduced in 13.1.0 where session start location updates would fail to update on pre API 30 devices.
 
- Fixed an issue introduced in 13.1.0 where geofence update events would fail to update properly.

##### Added

- Added the ability to namespace all braze.xml configurations to be able to use braze in place of appboy. The Braze namespaced configuration keys will take precedence over the appboy keys.

- For example, com_appboy_api_key can be replaced with com_braze_api_key.
 
- Be sure to look for and update any API keys in your build variants as the com_braze_api_key from your default variant might take precedence unexpectedly.
 
- All com_appboy_* configuration keys in XML will be removed in a future release so it is advised to migrate these configuration keys to their com_braze_* counterparts.

##### Changed

- Changed target API for the SDK to 31.

## 15.0.0

Release Date

##### Important

- It is highly recommended to do extensive QA after updating to this release, especially for clients doing any amount of Content Card or In-App Message customizations.

##### ⚠ Breaking

- All Content Cards layout/drawables/colors/dimens identifiers containing com_appboy_content_cards/com_appboy_content_card were replaced with com_braze_content_cards/com_braze_content_card respectively.

- Content Card drawables icon_pinned, icon_read, icon_unread are now com_braze_content_card_icon_pinned, com_braze_content_card_icon_read, com_braze_content_card_icon_unread.

- All In-App Message layout/drawables/colors/dimens identifiers containing com_appboy_inappmessage/com_appboy_in_app_message replaced with com_braze_inappmessage.
 
- All styles under namespace Appboy.* moved to Braze.*.

- Any Appboy.* style overrides must be migrated to Braze.* as there is no backwards compatibility.
 
- For example, a style override for Appboy.Cards.ImageSwitcher must be renamed to Braze.Cards.ImageSwitcher.

- Several classes/interfaces have been moved to a Braze namespace/package.

- In-App Messages

- In-App Message classes under com.appboy.models.* moved to com.braze.models.inappmessage
 
- Class com.appboy.ui.inappmessage.InAppMessageCloser -> com.braze.ui.inappmessage.InAppMessageCloser
 
- Enum com.appboy.ui.inappmessage.InAppMessageOperation -> com.braze.ui.inappmessage.InAppMessageOperation
 
- Enums in package com.appboy.enums.inappmessage.* moved to com.braze.enums.inappmessage

- Content Cards

- Interface IContentCardsUpdateHandler moved to com.braze.ui.contentcards.handlers.IContentCardsUpdateHandler
 
- Interface IContentCardsViewBindingHandler moved to com.braze.ui.contentcards.handlers.IContentCardsViewBindingHandler
 
- Interface AppboyContentCardsActionListener moved to com.braze.ui.contentcards.listeners.DefaultContentCardsActionListener
 
- Classes in package com.appboy.ui.contentcards.view.* moved to com.braze.ui.contentcards.view.*

- This is the package containing all Content Card default views.

- Class com.appboy.events.ContentCardsUpdatedEvent -> com.braze.events.ContentCardsUpdatedEvent

- Miscellaneous

- Class AppboyBaseFragmentActivity moved to com.braze.ui.activities.BrazeBaseFragmentActivity

- Removed deprecated IInAppMessageManagerListener#onInAppMessageReceived from IInAppMessageManagerListener.
 
- Removed AppboyUser in favor of BrazeUser.

- Note that for Kotlin consumers, Appboy.currentUser? and Braze.currentUser? are valid due to the removal of generics on the Braze.getCurrentUser() method.

##### Added

- Added support for Conversational Push.
 
- Added the ability for custom broadcast receivers to not require the host package name as a prefix when declaring intent filters in your app manifest.

- <action android:name="${applicationId}.intent.APPBOY_PUSH_RECEIVED" /> should be replaced with <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
 
- <action android:name="${applicationId}.intent.APPBOY_NOTIFICATION_OPENED" /> should be replaced with <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
 
- <action android:name="${applicationId}.intent.APPBOY_PUSH_DELETED" /> should be replaced with <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
 
- The appboy intents have been deprecated but are still available. They will be removed in a future release so migrating early is highly recommended.
 
- Both the appboy and braze intents are sent for backwards compatibility so only one set should be registered at a time.

- Added BrazeUser.addToSubscriptionGroup() and BrazeUser.removeFromSubscriptionGroup() to add or remove a user from an email or SMS subscription group.

- Added brazeBridge.getUser().addToSubscriptionGroup() and brazeBridge.getUser().removeFromSubscriptionGroup() to the javascript interface for HTML In-App Messages.

##### Changed

- Several classes in the android-sdk-ui artifact have been renamed to the Braze namespace/package. Whenever possible, the original classes are still available. However, they will be removed in a future release so migrating early is highly recommended.

- Classes in package com.appboy.push.* moved to com.braze.push.*
 
- Classes in package com.appboy.ui.inappmessage.views moved to com.braze.ui.inappmessage.views
 
- Classes in package com.appboy.ui.inappmessage.listeners moved to com.braze.ui.inappmessage.listeners
 
- Interfaces in com.appboy.ui.inappmessage.* moved to com.braze.ui.inappmessage.*
 
- Class com.appboy.AppboyFirebaseMessagingService -> com.braze.push.BrazeFirebaseMessagingService
 
- Class com.appboy.AppboyAdmReceiver -> com.braze.push.BrazeAmazonDeviceMessagingReceiver
 
- Class com.appboy.ui.AppboyContentCardsFragment -> com.braze.ui.contentcards.ContentCardsFragment
 
- Class com.appboy.ui.activities.AppboyContentCardsActivity -> com.braze.ui.activities.ContentCardsActivity
 
- Class com.appboy.ui.AppboyWebViewActivity -> com.braze.ui.BrazeWebViewActivity
 
- Class com.appboy.ui.inappmessage.AppboyInAppMessageManager -> com.braze.ui.inappmessage.BrazeInAppMessageManager
 
- Class com.appboy.ui.inappmessage.DefaultInAppMessageViewWrapper -> com.braze.ui.inappmessage.DefaultInAppMessageViewWrapper
 
- Class com.appboy.AppboyLifecycleCallbackListener -> com.braze.BrazeActivityLifecycleCallbackListener

- Changed the ContentCardsFragment and BrazeInAppMessageManager to clear their respective caches of messages after wipeData() is called.

## 14.0.1

Release Date

##### Fixed

- Fixed an issue with BrazeProperties not being kept via proguard rules.
 
- Fixed an issue on TV integrations where in app messages wouldn’t properly be given focus when visible.

##### Added

- Added close icon highlighting for TV integrations when selecting the close button in In App Messages.

## 14.0.0

Release Date

##### ⚠ Breaking

- Interface IInAppMessageViewWrapperFactory changed to use BrazeConfigurationProvider.
 
- Interface IAppboyImageLoader/IBrazeImageLoader changed to use com.braze.enums.BrazeViewBounds.
 
- Class com.appboy.configuration.AppboyConfig is now com.braze.configuration.BrazeConfig. The original class has been removed and old usages should be updated.
 
- Class com.appboy.enums.AppboyViewBounds is now com.braze.enums.BrazeViewBounds. The original class has been removed and old usages should be updated.
 
- Removed com.appboy.push.AppboyNotificationUtils#bundleOptString.
 
- Braze.logPurchase() and Braze.logEvent() now impose a 50KB limit on event properties. If the supplied properties are too large, the event is not logged.

- See BrazeProperties.isInvalid().

- HTML In-App Messages rendered via the default AppboyHtmlViewFactory now require the device to be in touch mode to display.

- See getIsTouchModeRequiredForHtmlInAppMessages() in the #added section for configuration on disabling this behavior.

- For Kotlin consumers, Appboy.currentUser? calls must be migrated to Braze.getCurrentUser<BrazeUser>() due to updated generics resolution.

##### Changed

- Several classes in the base artifact have been renamed to the Braze namespace/packages. Whenever possible, the original classes are still available. However, they will be removed in a future release so migrating early is highly recommended.

- com.appboy.Appboy -> com.braze.Braze
 
- com.appboy.configuration.AppboyConfig -> com.braze.configuration.BrazeConfig
 
- com.braze.AppboyUser -> com.braze.BrazeUser
 
- com.appboy.lrucache.AppboyLruImageLoader -> com.braze.images.DefaultBrazeImageLoader
 
- com.appboy.configuration.AppboyConfigurationProvider -> com.braze.configuration.BrazeConfigurationProvider
 
- com.appboy.models.outgoing.AppboyProperties -> com.braze.models.outgoing.BrazeProperties
 
- com.appboy.support.AppboyImageUtils -> com.braze.support.BrazeImageUtils
 
- com.appboy.support.AppboyFileUtils -> com.braze.support.BrazeFileUtils

- Changed the behavior of In-App Message Accessibility Exclusive mode to save and reset the accessibility flags of views after display.
 
- Changed the AppboyInAppMessageWebViewClientListener to use an Activity context when following a deeplink in IInAppMessageWebViewClientListener.onOtherUrlAction.
 
- Deprecated AppboyInAppMessageHtmlBaseView.APPBOY_BRIDGE_PREFIX.

##### Added

- Added Braze.registerPushToken() and Braze.getRegisteredPushToken().

- Note that these methods are the functional equivalents of Appboy.registerAppboyPushMessages() and Appboy.getAppboyPushMessageRegistrationId().

- Exposed brazeBridge which replaces appboyBridge to be used as the javascript interface for HTML In-App Messages. appboyBridge is deprecated and will be removed in a future version of the SDK.
 
- Added AppboyInAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX.
 
- Added the ability to configure whether View#isInTouchMode() is required to show HTML In-App Messages via BrazeConfig.setIsTouchModeRequiredForHtmlInAppMessages().

- Can also be configured via boolean com_braze_require_touch_mode_for_html_in_app_messages in your braze.xml.
 
- Defaults to true.

- Added support for new SDK Authentication feature.

##### Fixed

- Fixed an issue with setIsInAppMessageAccessibilityExclusiveModeEnabled() not being respected if set via runtime configuration. Setting this value via XML was unaffected.
 
- Fixed an issue with the SDK repeatedly failing to initialize when not properly setting a Braze API key.

## 13.1.2

Release Date

##### Changed

- Changed the NotificationTrampolineActivity to always call finish() regardless of any eventual deeplink handling by the host app or SDK.

## 13.1.1

Release Date

##### Fixed

- Fixed an issue with the NotificationTrampolineActivity being opened on notification delete intents.

## 13.1.0

Release Date

##### Changed

- All notifications now route through NotificationTrampolineActivity to comply with Android 12 notification trampoline restrictions.
 
- Inline Image push is now compatible with the Android 12 notification area changes.
 
- Automatic Firebase Messaging registration will now use FirebaseMessaging.getInstance().getToken() directly if available.
 
- Removed usage of Intent.ACTION_CLOSE_SYSTEM_DIALOGS with push notifications.

##### Added

- Added getInAppMessageStack(), getCarryoverInAppMessage(), and getUnregisteredInAppMessage() to AppboyInAppMessageManager.

## 13.0.0

Release Date

##### ⚠ Breaking

- Moved all In-App Message buttons from Button to com.appboy.ui.inappmessage.views.InAppMessageButton.

- This ensures that the MaterialComponentsViewInflater does not interfere with standard In-App Message display when using a MaterialComponents theme.
 
- Apps extending a Material theme should test to ensure their In-App Messages appear as expected.

- Moved com.appboy.ui.inappmessage.AppboyInAppMessageImageView to com.appboy.ui.inappmessage.views.InAppMessageImageView.
 
- Removed all getter methods from AppboyConfig. Access to the underlying data is now directly possible via the variables of the object, e.g. appboyConfig.getApiKey() is now appboyConfig.mApiKey.

##### Added

- Added getEmptyCardsAdapter(), getContentCardUpdateRunnable(), getNetworkUnavailableRunnable() to protected methods in AppboyContentCardsFragment for easier customizability.
 
- Changed the max content line length to 2 lines for Inline Image Push.

- This style can be found via "Appboy.Push.InlineImage.TextArea.TitleContent.ContentText"

##### Fixed

- Changed the AppboyContentCardsFragment.ContentCardsUpdateRunnable to determine network unavailability and feed emptiness based on the filtered list of cards and not the original input list of cards.
 
- Fixed an issue with IAM display where a deleted local image would result in a failed image display.

## 12.0.0

Release Date

##### ⚠ Breaking

- Added getIntentFlags to the IAppboyNavigator interface to more easily allow for customizing Activity launch behavior.

- A default implementation is available below:

```

1
2
3
4

```
 | 
```
@Override
public int getIntentFlags(IntentFlagPurpose intentFlagPurpose) {
 return new AppboyNavigator().getIntentFlags(intentFlagPurpose);
}

```
 | 

- Renamed firebase_messaging_service_automatically_register_on_new_token to com_appboy_firebase_messaging_service_automatically_register_on_new_token in appboy.xml configuration.

##### Fixed

- Fixed an issue with the default image loader not properly setting image bitmaps on API 23 and below devices.
 
- Fixed an issue where the AppboyInAppMessageManager.ensureSubscribedToInAppMessageEvents() method wouldn’t properly resubscribe after disabling and re-enabling the SDK.

##### Changed

- Changed Push Stories in AppboyNotificationStyleFactory to use BrazeNotificationPayload.

## 11.0.0

Release Date

##### ⚠ Breaking

- Changed the behavior of new beta HTML In-App Messages with dashboard preview support (i.e. those with MessageType.HTML and not MessageType.HTML_FULL) to not automatically log analytics clicks on url follows in IInAppMessageWebViewClientListener.

- Body click analytics will no longer automatically be collected. To continue to receive body click analytics, you must log body clicks explicitly from your message via Javascript using appboyBridge.logClick().

- IContentCardsUpdateHandler and IContentCardsViewBindingHandler interfaces now extend android.os.Parcelable.

- This ensures that these handlers properly transition across instance state saves and reads.
 
- Examples on how to extend Parcelable can be found in DefaultContentCardsUpdateHandler and DefaultContentCardsViewBindingHandler.

- Renamed AppboyFcmReceiver to BrazePushReceiver.

##### Added

- Added AppboyInAppMessageManager.getIsCurrentlyDisplayingInAppMessage().
 
- Added ability to configure whether the AppboyFirebaseMessagingService will automatically register tokens in its onNewToken method.

- Defaults to whether FCM automatic registration is enabled. Note that FCM automatic registration is a separate configuration option and is not enabled by default.
 
- Configured by changing the boolean value for firebase_messaging_service_automatically_register_on_new_token in your appboy.xml, or at runtime by setting AppboyConfig.setIsFirebaseMessagingServiceOnNewTokenRegistrationEnabled().
 
- Note that the Sender ID used to configure tokens received in onNewToken() is based on the app’s default Firebase Project rather than the explicitly configured Sender ID on the Braze SDK. These should generally be the same value.

##### Changed

- Deprecated AppboyLifecycleCallbackListener.setInAppMessagingRegistrationBlacklist() in favor of AppboyLifecycleCallbackListener.setInAppMessagingRegistrationBlocklist().
 
- Deprecated AppboyConfig.Builder.setDeviceObjectWhitelist() in favor of AppboyConfig.Builder.setDeviceObjectAllowlist().
 
- Deprecated AppboyConfig.Builder.setDeviceObjectWhitelistEnabled() in favor of AppboyConfig.Builder.setDeviceObjectAllowlistEnabled().

##### Fixed

- Fixed an issue where the AppboyContentCardsFragment would not transition a custom IContentCardsUpdateHandler or IContentCardsViewBindingHandler implementation in onSaveInstanceState(), which caused the defaults for both to be used instead.
 
- Fixed an issue with deeplink handling where push action button deeplinks would only work once throughout the lifetime of the application.

## 10.1.0

Release Date

##### Changed

- Changed AppboyWebViewActivity to extend FragmentActivity for better fragment management.

- Note that AppboyWebViewActivity now no longer performs session and in-app message registration on its own.
 
- Clients using AppboyLifecycleCallbackListener will see no effect.
 
- Clients performing manual session integration should override AppboyWebViewActivity to add back this registration and set the new Activity via AppboyConfig.Builder#setCustomWebViewActivityClass() or com_appboy_custom_html_webview_activity_class_name in the appboy.xml file.

##### Added

- Added support for receiving messages via the Huawei Messaging Service.

##### Fixed

- Fixed minor display issues with Inline Image Push.

## 10.0.0

Release Date

##### ⚠ Breaking

- The Android SDK has now fully migrated to AndroidX dependencies. No backwards compatibility is possible with the no longer maintained Android Support Library.

- See https://developer.android.com/jetpack/androidx for more information on AndroidX, including migration steps.
 
- Braze Android 9.0.0 is the last SDK version compatible with the Android Support Library.

- Added a new interface method, IAppboyNotificationFactory.createNotification(BrazeNotificationPayload).

- The BrazeNotificationPayload is a data object that performs the task of extracting and surfacing values from the Braze push payload in a far more convenient way.
 
- Integrations without a custom IAppboyNotificationFactory will have no breaking changes.
 
- Integrations with a custom IAppboyNotificationFactory are recommended to switchover to their non-deprecated counterparts in AppboyNotificationUtils.java.

##### Added

- Added support for com_appboy_inapp_show_inapp_messages_automatically boolean configuration for Unity.

##### Fixed

- Fixed support for dark mode in HTML in-app messages and remote urls opened in AppboyWebViewActivity for deeplinks via the prefers-color-scheme: dark css style.

- The decision to display content in dark mode will still be determined at display time based on the device’s state.

- Fixed an issue where the card parameter in com.appboy.IAppboyImageLoader.renderUrlIntoCardView() was null for Content Cards.

##### Removed

- Removed com.appboy.push.AppboyNotificationUtils.handleContentCardsSerializedCardIfPresent().

## 9.0.0

Release Date

##### ⚠ Breaking

- The Android SDK now has a source and target build compatibility set to Java 8.

##### Changed

- Simplified the email regex used in the SDK to centralize most validation on the server.

- The original email validation used is reproduced below:

```

1

```
 | 
```
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])

```
 | 

##### Fixed

- Fixed an issue where in-app message icon TextViews could throw a ClassCastException on certain devices and prevent display.

##### Removed

- Removed com.appboy.support.AppboyImageUtils.getBitmap(android.net.Uri) in favor of com.appboy.support.AppboyImageUtils.getBitmap(android.content.Context, android.net.Uri, com.appboy.enums.AppboyViewBounds).
 
- Removed com.appboy.AppboyAdmReceiver.CAMPAIGN_ID_KEY.

- Use Constants.APPBOY_PUSH_CAMPAIGN_ID_KEY instead.

- Removed com.appboy.push.AppboyNotificationUtils.isValidNotificationPriority().

## 8.1.0

Release Date

##### Added support for Android 11 R (API 30).

- Note that apps targeting API 30 should update to this SDK version.

##### Changed

- Changed Content Card subscriptions to automatically re-fire when silent push syncs or test send cards are received via push.
 
- Improved several accessibility features of In-App Messages and Content Cards as per Principles for improving app accessibility.

- Changed non-informative accessibility content descriptions for in-app message and Content Card images to @null.
 
- Content Cards now have content descriptions on their views that incorporate the title and description.

- Changed the AppboyFirebaseMessagingService to override the onNewToken() method to register a Firebase push token when automatic Firebase registration enabled.

##### Added

- Added appboyBridge.getUser().addAlias() to the javascript interface for HTML In-App Messages.
 
- Added Appboy.getConfiguredApiKey() to aid in determining if the SDK has an API key properly configured.
 
- Added an overload for IAppboy.getCurrentUser() that adds an asynchronous callback for when the current user is available instead of blocking on the caller thread.

- The following is an example of the full interface:
 
- 

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

```
 | 
```
Appboy.getInstance(mContext).getCurrentUser(new IValueCallback<AppboyUser>() {
 @Override
 public void onSuccess(@NonNull AppboyUser currentUser) {
 currentUser.setFirstName("Jared");
 }

 @Override
 public void onError() {}
});

```
 | 

- A convenience class is also provided with SimpleValueCallback:
 
- 

```

1
2
3
4
5
6

```
 | 
```
Appboy.getInstance(mContext).getCurrentUser(new SimpleValueCallback<AppboyUser>() {
 @Override
 public void onSuccess(@NonNull AppboyUser currentUser) {
 currentUser.setFirstName("Julian");
 }
});

```
 | 

- Added AppboyInAppMessageManager.setClickOutsideModalViewDismissInAppMessageView() allow for the dismissal of a Modal In-App Message when tapping on the frame behind the message itself.

- The default (and historical) value is false, meaning that clicks outside the modal do not close the modal.
 
- To toggle the feature on, call: AppboyInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)

##### Fixed

- Fixed behavior of the com.appboy.ui.AppboyContentCardsFragment to not assign margin of the first card in the feed from the top of the feed.
 
- Fixed an issue with Content Card test sends where the test send wouldn’t be visible in some conditions.
 
- Fixed an issue with regex based event property triggers not working as expected. Previously they had to match the entire string, now they will search for matches as expected. The regex is now also case-insensitive.
 
- Fixed an issue with resolveActivity() in the default UriAction logic not returning a valid Activity to handle external deeplinks on Android 11 devices without the QUERY_ALL_PACKAGES permission.
 
- Fixed an issue introduced in 4.0.1 where upgrading the SDK could result in server configuration values getting removed until the next session start.

##### Removed

- Removed AppboyConfig.Builder.setNotificationsEnabledTrackingOn().
 
- Removed AppboyImageUtils.getPixelsFromDp().
 
- Removed ViewUtils.getDisplayHeight().

## 8.0.1

Release Date

##### Fixed

- Fixed an Activity resolution issue in com.appboy.ui.AppboyWebViewActivity by removing a call to setDownloadListener().
 
- Fixed an implementation issue in 8.0.0 related to setting runtime configuration after stopping the SDK.

## 8.0.0

Release Date

##### ⚠ Breaking

- Integrators note: most of the changes listed below are on lightly used interfaces that do no affect most clients.
 
- Moved InAppMessageHtmlBase.getAssetsZipRemoteUrl(), InAppMessageHtmlBase.setAssetsZipRemoteUrl() to InAppMessageZippedAssetHtmlBase.java.
 
- Moved AppboyInAppMessageHtmlFullView.APPBOY_BRIDGE_PREFIX to AppboyInAppMessageHtmlBaseView.APPBOY_BRIDGE_PREFIX
 
- Renamed IInAppMessage.getRemoteAssetPathForPrefetch to IInAppMessage.getRemoteAssetPathsForPrefetch and changed signature to List.
 
- Renamed IInAppMessage.setLocalAssetPathForPrefetch to IInAppMessage.setLocalAssetPathsForPrefetch and changed signature to Map<String, String>.
 
- Created In-App Message interface IInAppMessageWithImage for slideup, modal, and fulls to hold image based methods. These methods have been refactored out of the IInAppMessage interface.

- These methods are getImageUrl(), getRemoteImageUrl(), getLocalImageUrl(), getBitmap(), getImageDownloadSuccessful(), setImageUrl(), setLocalImageUrl(), setImageDownloadSuccessful(), setRemoteImageUrl(), and setBitmap().

- Content Card backgrounds (in the default UI), now have their colors set via /android-sdk-ui/src/main/res/drawable-nodpi/com_appboy_content_card_background.xml.
 
- Several Content Cards related style values are now fully decoupled from News Feed values and are enumerated below.
 
- The color @color/com_appboy_card_background_border is now @color/com_appboy_content_card_background_border for Content Cards.
 
- The color @color/com_appboy_card_background_shadow is now @color/com_appboy_content_card_background_shadow for Content Cards.
 
- The color @color/com_appboy_card_background is now @color/com_appboy_content_card_background for Content Cards.
 
- The color used for the text in the empty AppboyContentCardsFragment, @color/com_appboy_title is now @color/com_appboy_content_card_empty_text_color.
 
- Several News Feed dimensions values also used in Content Card styles now have Content Card specific values, enumerated below. Note that if these values were overridden in your styles for use in Content Cards, they will have to be updated to the new keys.
 
- The dimension @dimen/com_appboy_card_background_border_left is now @dimen/com_appboy_content_card_background_border_left.
 
- The dimension @dimen/com_appboy_card_background_border_right is now @dimen/com_appboy_content_card_background_border_right.
 
- The dimension @dimen/com_appboy_card_background_border_top is now @dimen/com_appboy_content_card_background_border_top.
 
- The dimension @dimen/com_appboy_card_background_border_bottom is now @dimen/com_appboy_content_card_background_border_bottom.
 
- The dimension @dimen/com_appboy_card_background_shadow_bottom is now @dimen/com_appboy_content_card_background_shadow_bottom.
 
- The dimension @dimen/com_appboy_card_background_corner_radius is now @dimen/com_appboy_content_card_background_corner_radius.
 
- The dimension @dimen/com_appboy_card_background_shadow_radius is now @dimen/com_appboy_content_card_background_shadow_radius.
 
- Removed AppboyInAppMessageHtmlJavascriptInterface(Context) in favor of AppboyInAppMessageHtmlJavascriptInterface(Context, IInAppMessageHtml).
 
- Removed IAppboy.logPushDeliveryEvent() and AppboyNotificationUtils.logPushDeliveryEvent().

##### Added

- Added support for upcoming HTML In-App Message templates.
 
- Added appboyBridge.logClick(String), appboyBridge.logClick() and appboyBridge.getUser().setLanguage() to the javascript interface for HTML In-App Messages.
 
- Added support for dark mode in HTML in-app messages and remote urls opened in AppboyWebViewActivity for deeplinks via the prefers-color-scheme: dark css style.

- The decision to display content in dark mode will be determined at display time based on the device’s state.

- Added support for dark mode in the default Content Cards UI.

- This feature is enabled by default. To disable or change, override the values present in android-sdk-ui/src/main/res/values-night/colors.xml and android-sdk-ui/src/main/res/values-night/dimens.xml.

- Added IAppboy.subscribeToSessionUpdates() which allows for the host app to be notified when a session is started or ended.
 
- Added the ability to optionally set a custom list of location providers when obtaining a single location, such as on session start. See AppboyConfig.Builder.setCustomLocationProviderNames() for more information.

- The following example showcases instructing the SDK to use LocationManager.GPS_PROVIDER and LocationManager.NETWORK_PROVIDER.

```

1
2

```
 | 
```
 new AppboyConfig.Builder()
 .setCustomLocationProviderNames(EnumSet.of(LocationProviderName.GPS, LocationProviderName.NETWORK));

```
 | 

- In xml:

```

1
2
3
4

```
 | 
```
 <string-array translatable="false" name="com_appboy_custom_location_providers_list">
 <item>GPS</item>
 <item>NETWORK</item>
 </string-array>

```
 | 

- By default, only the passive and network providers are used when obtaining a single location from the system.
 
- This change does not affect Braze Geofences.

##### Fixed

- Fixed an issue where the pending intent flags on a push story only allowed for the main deeplink to be fired once.
 
- Fixed behavior of the com.appboy.ui.AppboyContentCardsFragment to not double the margin of the first card in the feed from the top of the feed.
 
- Fixed an issue where calling wipeData() or disableSdk() could result in not being able to set runtime configuration afterwards.

##### Changed

- Deprecated com.appboy.models.IInAppMessageWithImage#setImageUrl() in favor of com.appboy.models.IInAppMessageWithImage#setRemoteImageUrl(String).

## 7.0.0

Release Date

##### ⚠ Breaking

- Made several changes to the default Content Card views to more easily customize and apply ImageView styling.

- Changed Appboy.ContentCards.BannerImage.ImageContainer.Image to Appboy.ContentCards.BannerImage.Image.

- Removed com.appboy.ui.contentcards.view.ContentCardViewHolder.createCardImageWithStyle().

##### Added

- Added Czech and Ukrainian language translations for Braze UI elements.
 
- Added android-sdk-base-jetified and android-sdk-ui-jetified to reference jetified SDK AAR artifacts from the artifact repository.

- This is a direct replacement for android-sdk-ui-x and is a more complete integration path for using the Braze SDK with AndroidX.
 
- Usage as follows:

```

1
2
3

```
 | 
```
dependencies {
implementation "com.appboy:android-sdk-ui-jetified:${BRAZE_SDK_VERSION}"
}

```
 | 

- If previously using the android-sdk-ui-x module, you must replace any imports under the com.appboy.uix.push package to be under com.appboy.ui.push.
 
- The gradle properties android.enableJetifier=true and android.useAndroidX=true are no longer required when using androidX libraries with the Braze SDK.

- Added Material Design Button class names to exported consumer proguard rules.

```

1
2

```
 | 
```
-keepnames class android.support.design.button.MaterialButton
-keepnames class com.google.android.material.button.MaterialButton

```
 | 

##### Fixed

- Fixed issue in AppboyCardAdapter where a card index could be out of bounds when marking a card as seen.

##### Changed

- In-App Message “test sends” from the dashboard now display automatically if your app is in the foreground.

- Backgrounded apps will continue to receive a push notification to display the message.
 
- You can disable this feature by changing the boolean value for com_appboy_in_app_message_push_test_eager_display_enabled in your appboy.xml, or at runtime by setting AppboyConfig.setInAppMessageTestPushEagerDisplayEnabled() to false.

- Changed UriAction to be more easily customizable.

##### Removed

- Removed the android-sdk-ui-x module. See the Added section for more information.
 
- Removed the China Push Sample app.

## 6.0.0

Release Date

##### ⚠ Breaking

- Slideup and HTML Full In-App Messages now require the device to be in touch mode at the time of display. This is enforced in their respective IInAppMessageViewFactory default implementations.

- See https://developer.android.com/reference/android/view/View.html#isInTouchMode().

- Removed ViewUtils.setFocusableInTouchModeAndRequestFocus().
 
- AppboyUnityPlayerNativeActivity, AppboyOverlayActivity, AppboyUnityNativeInAppMessageManagerListener, AppboyUnityPlayerNativeActivity, AppboyUnityPlayerNativeActivity, and IAppboyUnityInAppMessageListener have been removed from the android-sdk-unity project.

- UnityPlayerNativeActivity was deprecated in 2015. See https://unity3d.com/unity/beta/unity5.4.0b1.

##### Added

- Added proper support for navigating and closing Braze In-App Messages with directional-pads/TV remote input devices.
 
- Added the ability to customize the in-app message button border radius via @dimen/com_appboy_in_app_message_button_corner_radius.
 
- Added the ability to customize the in-app message button border color stroke width via @dimen/com_appboy_in_app_message_button_border_stroke.

- The stroke width used when an in-app message button border is focused is set via @dimen/com_appboy_in_app_message_button_border_stroke_focused.

##### Fixed

- Fixed an issue where Content Cards syncs were suppressed too often.
 
- Fixed an issue where in-app messages could not be closed on TVs or other devices without touch interactions.

##### Changed

- Changed in-app messages to return focus back to the view that previously held focus before a message is displayed as given via Activity#getCurrentFocus().

## 5.0.0

Release Date

##### ⚠ Breaking

- Added IInAppMessageView.hasAppliedWindowInsets().

##### Added

- Added appboyBridge.logClick() and appboyBridge.getUser().setLanguage() to the javascript interface for HTML In-App Messages.
 
- Added Appboy.requestGeofences() to request a Braze Geofences update for a manually provided GPS coordinate. Automatic Braze Geofence requests must be disabled to properly use this method.

- Braze Geofences can only be requested once per session, either automatically by the SDK or manually with the above method.

- Added the ability to disable Braze Geofences from being requested automatically at session start.

- You can do this by configuring the boolean value for com_appboy_automatic_geofence_requests_enabled in your appboy.xml.
 
- You can also configure this at runtime by setting AppboyConfig.setAutomaticGeofenceRequestEnabled().

##### Fixed

- Fixed an issue where multiple calls to ViewCompat.setOnApplyWindowInsetsListener() could result in in-app messages margins getting applied multiple times instead of exactly once.
 
- Fixed an issue where pure white #ffffffff in a dark theme in-app message would not be used when the device was in dark mode.

- In this case, the original non-dark theme color would be used by the in-app message instead.

## 4.0.2

Release Date

##### Fixed

- Fixed an issue introduced in 4.0.0 where Content Card clicks wouldn’t get forwarded to the parent RecyclerView based on its View’s clickable status.

- This would result in clicks not being handled or logged for Content Cards.

## 4.0.1

Release Date

##### Fixed

- Fixed an issue where in-app messages could display behind translucent status and navigation bars.

## 4.0.0

Release Date

##### Known Issues with version 4.0.0

- Content Card clicks are not handled or logged for Content Cards due to the "Appboy.ContentCards" style containing the "clickable=true" style. This is fixed in SDK version 4.0.2.

##### ⚠ Breaking

- Added beforeInAppMessageViewOpened(), afterInAppMessageViewOpened(), beforeInAppMessageViewClosed(), afterInAppMessageViewClosed() to the IInAppMessageManagerListener interface.

- These methods are intended to help instrument each stage of the In-App Message View gaining and losing visibility status.

- Renamed Card.getIsDismissible() to Card.getIsDismissibleByUser().

##### Added

- Added the ability to more easily test In-App Messages from the dashboard when sending a test push by bypassing the need to click the test push notification and instead directly display the test In-App Message when the app is in the foreground.

- A push notification will still display if a test In-App Message push is received and the app is in the background.
 
- You can enable this feature by configuring the boolean value for com_appboy_in_app_message_push_test_eager_display_enabled in your appboy.xml. The default value is false.
 
- You can also enable this feature at runtime by setting AppboyConfig.setInAppMessageTestPushEagerDisplayEnabled() to true. The default value is false.

- Added the ability to customize how In-App Messages views are added to the view hierarchy with a custom IInAppMessageViewWrapperFactory.

- See AppboyInAppMessageManager.setCustomInAppMessageViewWrapperFactory().
 
- For lightweight customizations, consider extending DefaultInAppMessageViewWrapper and overriding getParentViewGroup(), getLayoutParams(), and addInAppMessageViewToViewGroup().
 
- Addresses https://github.com/braze-inc/braze-android-sdk/issues/138.

- Added Card.setIsDismissibleByUser() to allow for integrators to disable the default swipe-to-dismiss behavior on a per-card basis.
 
- Added the ability to set the initial AppboyLogger log level via appboy.xml.

- In your appboy.xml, set an integer value for com_appboy_logger_initial_log_level. The integer should correspond to a constant in Log, such as Log.VERBOSE which is 2.
 
- Values set via AppboyLogger.setLogLevel() take precedence over values set in appboy.xml.

- Added the ability to use a custom Activity when opening deeplinks inside the app via a WebView. This Activity will be used in place of the default AppboyWebViewActivity.

- You can do this by configuring the string value for com_appboy_custom_html_webview_activity_class_name in your appboy.xml. Note that the class name used appboy.xml must be the exact class name string as returned from YourClass.class.getName().
 
- You can also configure this at runtime by setting AppboyConfig.setCustomWebViewActivityClass().
 
- To retrieve the url in your custom WebView:

```

1
2
3
4

```
 | 
```
final Bundle extras = getIntent().getExtras();
if (extras.containsKey(Constants.APPBOY_WEBVIEW_URL_EXTRA)) {
String url = extras.getString(Constants.APPBOY_WEBVIEW_URL_EXTRA);
}

```
 | 

##### Fixed

- Fixed the inability to scroll through Content Cards when not using standard input mechanisms, aiding accessibility.

- All Content Card views now have selectable and focusable attributes set to true.
 
- Amazon Fire TV integrators should update to this version.

- Changed AppboyInAppMessageHtmlUserJavascriptInterface.setCustomAttribute() in the HTML javascript bridge to not coerce Double into Float.
 
- Fixed default Content Card rendering on low screen density devices. Previously, Content Cards could render without a margin and overflow off screen.

- @dimens/com_appboy_content_cards_max_width now accurately sets the maximum possible width of a Content Card.
 
- @dimens/com_appboy_content_cards_divider_left_margin and @dimens/com_appboy_content_cards_divider_right_margin are now used to provide a margin for Content Cards when the width of the Content Card does not exceed the max width of @dimens/com_appboy_content_cards_max_width.

- Fixed an issue where images in Content Cards could be resized before they had finished a layout, resulting in an 0 width/height ImageView.

##### Changed

- InAppMessageImmersiveBase.getMessageButtons() is now guaranteed to be non-null. When buttons are not set on the message, this list will be non-null and empty.

- Calling InAppMessageImmersiveBase.setMessageButtons() with null will instead clear the MessageButton list

- Changed the SDK to compile against the 18.0.0 version of the Firebase Cloud Messaging dependency.
 
- Updated the exported android-sdk-ui consumer proguard rules to keep javascript interface methods.
 
- Changed the WebView used in HTML In-App Messages to have DOM storage enabled via setDomStorageEnabled(true).
 
- Changed Content Cards to allow for blank or empty values for the title or description. In these situations, the TextView’s visibility is changed to GONE in the view hierarchy.

##### Removed

- Removed Constants.APPBOY_WEBVIEW_URL_KEY.

## 3.8.0

Release Date

##### ⚠ Breaking

- Added renderUrlIntoInAppMessageView(), renderUrlIntoCardView(), getPushBitmapFromUrl(), and getInAppMessageBitmapFromUrl() to the IAppboyImageLoader interface. These methods provide more information about the rendered object. For example, renderUrlIntoCardView() provides the Card object being rendered in the feed.

- IAppboyImageLoader.renderUrlIntoView() and IAppboyImageLoader.getBitmapFromUrl() have been removed.
 
- For maintaining behavioral parity, renderUrlIntoInAppMessageView() and renderUrlIntoCardView() can reuse your previous IAppboyImageLoader.renderUrlIntoView() implementation while getPushBitmapFromUrl() and getInAppMessageBitmapFromUrl() can reuse your previous IAppboyImageLoader.getBitmapFromUrl() implementation.
 
- The Glide IAppboyImageLoader implementation has been updated and can be found here.

- Removed MessageButton#getIsSecondaryButton() and MessageButton#setIsSecondaryButton().

##### Added

- Added support for the upcoming feature, In-App Messages in Dark Mode.

- Dark Mode enabled messages must be created from the dashboard. Braze does not dynamically theme In-App Messages for Dark Mode.
 
- Added IInAppMessageThemeable interface to In-App Messages, which adds enableDarkTheme() to In-App Messages.
 
- To configure/disable Braze from automatically applying a Dark Theme (when available from Braze’s servers), use a custom IInAppMessageManagerListener.

- 

```

1
2
3

```
 | 
```
 if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(AppboyInAppMessageManager.getInstance().getApplicationContext())) {
 ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
 }

```
 | 

- Added Card.isContentCard().
 
- Added the ability to use an existing color resource for com_appboy_default_notification_accent_color in your appboy.xml.

- For example: <color name="com_appboy_default_notification_accent_color">@color/my_color_here</color>.

##### Fixed

- Fixed an edge case where the AppboyInAppMessageManager could throw an NullPointerException if an in-app message was in the process of animating out while AppboyInAppMessageManager.unregisterInAppMessageManager() was called.
 
- Fixed an issue where multiple subscribers to Content Cards updates could cause a ConcurrentModificationException if they simultaneously attempted to mutate the list returned in ContentCardsUpdatedEvent.getAllCards().

- ContentCardsUpdatedEvent.getAllCards() now returns a shallow copy of the list of Content Cards model objects.

- Fixed an issue (introduced in 3.7.0) where the background color for fullscreen in-app messages was not set.
 
- Fixed an issue (introduced in 3.7.0) were images for fullscreen in-app messages would not appear on API 21 and below devices.

## 3.7.1

Release Date

##### Added

- Added IInAppMessage.setExtras() to set extras on In-App Messages.

##### Fixed

- Fixed an issue where a slow loading HTML In-App Message could throw an exception if the Activity changed before onPageFinished() was called.
 
- Removed FEATURE_INDETERMINATE_PROGRESS and FEATURE_PROGRESS from AppboyWebViewActivity.

## 3.7.0

Release Date

##### Known Issues

- This release introduced issues with in-app message unregistration (AppboyInAppMessageManager.unregisterInAppMessageManager()) and fullscreen in-app messages. These issues have been fixed in version 3.8.0 of the SDK.

##### Breaking

- Added the applyWindowInsets() method to IInAppMessageView interface. This allows for granular customization at the in-app message view level with respect to device notches.
 
- The old configuration key used in appboy.xml for disabling location collection com_appboy_disable_location_collection is now deleted. This key is replaced by com_appboy_enable_location_collection. The default value of com_appboy_disable_location_collection is false. Braze location collection is disabled by default starting with Braze SDK version 3.6.0.
 
- Removes the Feedback feature from the SDK. All Feedback methods on the SDK, including Appboy.submitFeedback() and Appboy.logFeedbackDisplayed(), are removed.

##### Fixed

- Changed the behavior of In-App Messages to allow analytics to be logged again when the same In-App Message is displaying a new time.

##### Changed

- Improves support for in-app messages on “notched” devices (for example, iPhone X, Pixel 3XL). Full-screen messages now expand to fill the entire screen of any phone, while covering the status bar.
 
- Changed the behavior of HTML In-App Messages to not display until the content has finished loading as determined via WebViewClient#onPageFinished() on the in-app message’s WebView.

## 3.6.0

Release Date

##### Breaking

- External user ids (provided via Appboy.changeUser()), are now limited to 997 bytes in UTF-8 encoding.

- Existing user IDs will be truncated to 997 bytes in UTF-8 encoding.
 
- New user IDs (via Appboy.changeUser()) will be rejected if too long.
 
- This byte limit can be read in code via Constants#USER_ID_MAX_LENGTH_BYTES.

- Added IInAppMessage.getMessageType() to return the MessageType enum for easier in-app message type checking.
 
- Braze location collection is disabled by default. If you choose to use our location services, you must explicitly enable location services.

- You can do this by configuring the boolean value for com_appboy_enable_location_collection in your appboy.xml. The default value is false.
 
- You can also enable location collection at runtime by setting AppboyConfig.setIsLocationCollectionEnabled() to true.
 
- The old configuration value com_appboy_disable_location_collection in appboy.xml is deprecated. It should be replaced with new configuration value of com_appboy_enable_location_collection.

##### Added

- Added AppboyContentCardsFragment.getContentCardsRecyclerView() to obtain the RecyclerView associated with the Content Cards fragment.
 
- Added AppboyInAppMessageManager.getDefaultInAppMessageViewFactory() to simplify most custom implementations of IInAppMessageViewFactory.

##### Changed

- Changed the click target area of in-app message close buttons to 48dp. The close button drawable was increased to 20dp from 14dp.

- The width/height in dp of this click target can be configured with a dimens override for com_appboy_in_app_message_close_button_click_area_width and com_appboy_in_app_message_close_button_click_area_height respectively.

- Changed UriUtils.getQueryParameters() to handle the parsing of an opaque/non-hierarchical Uri such as mailto: or tel:.

## 3.5.0

##### Breaking

- Removed IAppboyUnitySupport interface from Appboy singleton object. Its methods have been added to the IAppboy interface.
 
- The IAction in IContentCardsActionListener.onContentCardClicked() is now annotated as @Nullable. Previously, this field was always non-null.
 
- Fixed an issue where FLAG_ACTIVITY_NEW_TASK was not added to configured back stack Activities when opening push. This resulted in push notifications failing to open deep links in that situation.

- Custom push back stack Activities are set via AppboyConfig.setPushDeepLinkBackStackActivityClass().

##### Added

- Added Appboy.getCachedContentCards() to provide an easier way to obtain the cached/offline list of Content Cards on the device.
 
- Added Appboy.deserializeContentCard() to allow for the deserialization of a Content Card. Useful for custom integrations that store the Content Cards data models in their own storage and recreate the Content Card afterwards.

##### Changed

- Deprecated Card.isEqualTo() in favor of using Card.equals().

##### Fixed

- Fixed behavior in Content Cards and News Feed where cards without a click action wouldn’t have their client click listeners called.

## 3.4.0

##### Added

- Added support for Android 10 Q (API 29).

- With the addition of the android.permission.ACCESS_BACKGROUND_LOCATION permission in Android Q, this permission is now required for Braze Geofences to work on Android Q+ devices. Please see the documentation for more information.
 
- The AppboyNotificationRoutingActivity class is now sent with the Intent.FLAG_ACTIVITY_NO_HISTORY Intent flag. This is not expected to be a user visible change nor will require any integration changes.

- Added the ability to enable Braze Geofences without enabling Braze location collection. Set AppboyConfig.setGeofencesEnabled() or com_appboy_geofences_enabled in your appboy.xml to enable Braze Geofences.

- Note that Braze Geofences will continue to work on existing integrations if location collection is enabled and this new configuration is not present. This new configuration is intended for integrations that want Braze Geofences, but not location collection enabled as well.

- Added Appboy.setGoogleAdvertisingId() to pass a Google Advertising ID and Ad Tracking Limiting enabled flag back to Braze. Note that the SDK will not automatically collect either field.

##### Fixed

- Fixed in-app message buttons not properly respecting colors when using a Material Design style theme.

##### Breaking

- Geofences on Android Q+ devices will not work without the android.permission.ACCESS_BACKGROUND_LOCATION permission.
 
- Changed the signature of IInAppMessageManagerListener.onInAppMessageButtonClicked() to include the in-app message of the clicked button.
 
- Removed the deprecated AppboyWebViewActivity.URL_EXTRA. Please use Constants.APPBOY_WEBVIEW_URL_EXTRA instead.

## 3.3.0

##### Known Issues

- If using a defined back stack Activity (set via AppboyConfig.setPushDeepLinkBackStackActivityClass()), then push notifications containing deep links won’t be opened. This behavior is fixed in 3.4.1.

##### Changed

- Changed the behavior of push deep links to not restart the launcher activity of the app when clicked.
 
- Changed the broadcast receiver responsible for sealing sessions after the session timeout to use goAsync to lower the occurrence of ANRs on certain devices.

- This ANR would contain the constant APPBOY_SESSION_SHOULD_SEAL in the Google Play Console.

- Changed the default video poster (the large black & white play icon) used by default in HTML in-app messages to be transparent.

##### Added

- Added support for long type event properties.

##### Fixed

- Fixed fullscreen in-app messages on notched devices rendering with a gap at the top of the in-app message.
 
- Fixed behavior of in-app messages where modal display would take up the entire screen after successive rotations on older devices.

## 3.2.2

##### Changed

- Improved the reliability of the session start location logic when location collection is enabled.
 
- Changed the in-app message trigger behavior to not perform custom event triggering until any pending server trigger requests have finished.

##### Fixed

- Fixed a bug in AppboyInAppMessageImageView that made images loaded with Glide appear blurry or not appear when setting an aspect ratio.

## 3.2.1

##### Added

- Added AppboyFirebaseMessagingService.handleBrazeRemoteMessage() to facilitate forwarding a Firebase RemoteMessage from your FirebaseMessagingService to the AppboyFirebaseMessagingService.

- AppboyFirebaseMessagingService.handleBrazeRemoteMessage() will return false if the argument RemoteMessage did not originate from Braze. In that case, the AppboyFirebaseMessagingService will do nothing.
 
- A helper method AppboyFirebaseMessagingService.isBrazePushNotification() will also return true if the RemoteMessage originated from Braze.

#### Fixed

- Fixed an issue with AppboyInAppMessageBoundedLayout having a custom styleable attribute that collided with a preset Android attribute.

## 3.2.0

##### Important

- Please note the breaking push changes in release 3.1.1 regarding the AppboyFirebaseMessagingService before upgrading to this version.

##### Fixed

- Fixed an issue where a filename’s canonical path was not validated during zip file extraction.
 
- Fixed an issue where the SDK setup verification would erroneously always log a warning that the AppboyFcmReceiver was registered using the old com.google.android.c2dm.intent.RECEIVE intent-filter.

##### Changed

- Improved the look and feel of in-app messages to adhere to the latest UX and UI best practices. Changes affect font sizes, padding, and responsiveness across all message types. Now supports button border styling.

##### Added

- Added collection of ActivityManager.isBackgroundRestricted() to device collection information.

## 3.1.1

##### Breaking

- Added AppboyFirebaseMessagingService to directly use the Firebase messaging event com.google.firebase.MESSAGING_EVENT. This is now the required way to integrate Firebase push with Braze. The AppboyFcmReceiver should be removed from your AndroidManifest and replaced with the following:

- 

```

1
2
3
4
5

```
 | 
```
<service android:name="com.appboy.AppboyFirebaseMessagingService">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT" />
 </intent-filter>
</service>

```
 | 

- Also note that any c2dm related permissions should be removed from your manifest as Braze does not require any extra permissions for AppboyFirebaseMessagingService to work correctly.

- Changed signature of Appboy.logPushNotificationActionClicked().

##### Added

- Added ability to render HTML elements in push notifications via AppboyConfig.setPushHtmlRenderingEnabled() and also com_appboy_push_notification_html_rendering_enabled in your appboy.xml.

- This allows the ability to use “multicolor” text in your push notifications.
 
- Note that html rendering be used on all push notification text fields when this feature is enabled.

##### Fixed

- Fixed behavior where the app would be reopened after clicking notification action buttons with a “close” button.
 
- Fixed behavior where in-app messages would not apply proper margins on devices with notched displays and would appear obscured by the notch.
 
- Fixed an issue that caused the enum DeviceKey to be unavailable in our public API.
 
- Fixed an issue in the AppboyFcmReceiver where the “is uninstall tracking push” method was looking for the extras bundle before its preprocessing into a bundle. This would result in uninstall tracking push being forwarded to your broadcast receiver as a silent push when it should not.
 
- Fixed an issue in the AppboyLruImageLoader where very large bitmaps stored in the cache could throw OutOfMemoryError when retrieving them from the cache.

##### Changed

- Changed behavior of the Feed and Content Cards image loader to always resize images to their true source aspect ratio after download.

## 3.1.0

##### Breaking

- Renamed AppboyNotificationUtils.wakeScreenIfHasPermission() to AppboyNotificationUtils.wakeScreenIfAppropriate(). Wakelocks can now be configured to not wake the device screen for push notifications.

- This can be set via AppboyConfig.setIsPushWakeScreenForNotificationEnabled() and also com_appboy_push_wake_screen_for_notification_enabled in your appboy.xml.

##### Added

- A drop-in AppboyContentCardsActivity class has been added which can be used to display Braze Content Cards.
 
- Added an appboyBridge ready event to know precisely when the appboyBridge has finished loading in the context of an HTML in-app message.

- Example below:

```

1
2
3
4
5
6

```
 | 
```
 <script type="text/javascript">
 function logMyCustomEvent() {
 appboyBridge.logCustomEvent('My Custom Event');
 }
 window.addEventListener('ab.BridgeReady', logMyCustomEvent, false);
 </script>

```
 | 

- Added Constants.TRAFFIC_STATS_THREAD_TAG to identify the Braze network traffic with the TrafficStats API.
 
- Added the ability to configure a blacklist of Activity classes to disable automatic session handling and in-app message registration in the AppboyLifecycleCallbackListener. See AppboyLifecycleCallbackListener.setActivityClassInAppMessagingRegistrationBlacklist(), AppboyLifecycleCallbackListener.setActivityClassSessionHandlingBlacklist(), and constructor AppboyLifecycleCallbackListener(boolean, boolean, Set<Class>, Set<Class>).

##### Changed

- Deprecated the Feedback feature. This feature is disabled for new accounts, and will be removed in a future SDK release.
 
- Changed the deprecated status of the AppboyNotificationUtils.isUninstallTrackingPush() method. Note that uninstall tracking notifications will not be forwarded to registered receivers.
 
- Improved in-app message triggering logic to fall back to lower priority messages when the Braze server aborts templating (e.g. from a Connected Content abort in the message body, or because the user is no longer in the correct segment for the message)

## 3.0.1

##### Changed

- Deprecated Card.isRead() and Card.setIsRead(). Please use Card.isIndicatorHighlighted() and Card.setIndicatorHighlighted() instead.

##### Added

- Added Card.isClicked(). Clicks made through Card.logClick() are now saved locally on the device for Content Cards.
 
- Added AppboyConfig.setIsInAppMessageAccessibilityExclusiveModeEnabled() which forces accessibility readers to only be able to read currently displaying in-app messages and no other screen contents.

- This can also be set via com_appboy_device_in_app_message_accessibility_exclusive_mode_enabled in your appboy.xml.

## 3.0.0

##### Breaking

- From AppboyConfig, removed getEnableBackgroundLocationCollection(), getLocationUpdateTimeIntervalSeconds(), and getLocationUpdateDistance() and their respective setters in AppboyConfig.Builder.
 
- Removed AppboyInAppMessageImmersiveBaseView.getMessageButtonsView().
 
- Removed the Fresco image library from the SDK. To displaying GIFs, you must use a custom image library. Please see IAppboy#setAppboyImageLoader(IAppboyImageLoader).

- We recommend the Glide Image Library as a Fresco replacement.
 
- AppboyConfig.Builder.setFrescoLibraryEnabled() has been removed.
 
- AppboyConfigurationProvider.getIsFrescoLibraryUseEnabled() has been removed.

##### Fixed

- Fixed a NPE issue with the RecyclerView while saving the instance state in the AppboyContentCardsFragment.

##### Added

- Added the ability to set location custom attributes on the html in-app message javascript interface.
 
- Added compatibility with androidX dependencies.

- This initial release adds direct compatibility for classes found under the com.appboy.push package. These classes are commonly used in conjunction with an IAppboyNotificationFactory. To use these compatible classes, add the following gradle import: implementation 'com.appboy:android-sdk-ui-x:VERSION' and replace your imports to fall under the com.appboy.uix.push package.
 
- The gradle properties android.enableJetifier=true and android.useAndroidX=true are required when using androidX libraries with the Braze SDK.

- Added nullability annotation to Appboy and AppboyUser for better Kotlin interoperability.
 
- Added the ability to optionally whitelist keys in the device object. See AppboyConfig.Builder.setDeviceObjectWhitelistEnabled() and AppboyConfig.Builder.setDeviceObjectWhitelist() for more information.

- The following example showcases whitelisting the device object to only include the Android OS version and device locale in the device object.

```

1
2
3

```
 | 
```
 new AppboyConfig.Builder()
 .setDeviceObjectWhitelistEnabled(true)
 .setDeviceObjectWhitelist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));

```
 | 

##### Removed

- Removed the ability to optionally track locations in the background.
 
- Removed Cross Promotion cards from the News Feed.

- Cross Promotion cards have also been removed as a card model and will thus no longer be returned.

##### Changed

- Updated the Baidu China Push sample to use the version 2.9 Baidu JNI libraries and version 6.1.1.21 of the Baidu jar.

## 2.7.0

##### Breaking

- Renamed AppboyGcmReceiver to AppboyFcmReceiver. This receiver is intended to be used for Firebase integrations and thus the com.google.android.c2dm.intent.REGISTRATION intent-filter action in your AndroidManifest should be removed.
 
- Removed AppboyConfigurationProvider.isGcmMessagingRegistrationEnabled(), AppboyConfigurationProvider.getGcmSenderId(), AppboyConfig.Builder.setGcmSenderId(), and AppboyConfig.Builder.setGcmMessagingRegistrationEnabled().

##### Changed

- Changed custom event property values validation to allow for empty strings.

## 2.6.0

##### Added

- Introduced support for the Content Cards feature, which will eventually replace the existing News Feed feature and adds significant capability.

##### Breaking

- Updated the minimum SDK version from 14 (Ice Cream Sandwich) to 16 (Jelly Bean).

##### Added

- Added AppboyUser.setLocationCustomAttribute() and AppboyUser.unsetLocationCustomAttribute().

## 2.5.1

##### Changed

- Changed the behavior of push stories to ensure that after the story initially appears in the notification tray, subsequent page traversal clicks don’t alert the user again.

##### Added

- The Braze SDK now automatically records when the user has disabled notifications at the app level.

- The appboy.xml com_appboy_notifications_enabled_tracking_on boolean attribute and AppboyConfig.Builder.setNotificationsEnabledTrackingOn() have been deprecated and are no longer used.
 
- This allows users to more effectively opt-out of push and leads to a more accurate push notification reachable audience.

##### Fixed

- Fixed an issue where, when the lock screen was present, notification action button and push story body clicks would not open the application immediately. Added AppboyNotificationRoutingActivity for handling notification action button and push story body clicks.
 
- Fixed an issue where, for non fullscreen activities targeting API 27, requesting an orientation on activities would throw an exception.

## 2.5.0

##### Breaking

- Added isControl() to the IInAppMessage interface.
 
- Added logDisplayFailure() to the IInAppMessage interface. In-app message display failures may affect campaign statistics so care should be taken when logging display failures.
 
- Added the InAppMessageControl class to represent control in-app messages. Control in-app messages should not be displayed to users and should only call logImpression() at render time.

- Requesting in-app message display, even if the stack is non-empty, may potentially lead to no in-app message displaying if the in-app message is a control in-app message.

- Added AppboyInAppMessageManager.setCustomControlInAppMessageManagerListener() to modify the lifecycle behavior for control in-app messages.
 
- Removed logInAppMessageClick, logInAppMessageButtonClick, and logInAppMessageImpression from Appboy Unity player subclasses and AppboyUnityActivityWrapper.
 
- Removed AppboyConfigurationProvider.getIsUilImageCacheDisabled() and AppboyConfig.Builder.setDisableUilImageCache().

##### Fixed

- Fixed the issue where in-app messages triggered on session start could potentially be templated with the old user’s attributes.
 
- Fixed a bug where calling Appboy.wipeData() or Appboy.disableSdk() could potentially lead to null instances being returned from Appboy.getInstance().
 
- Fixed the issue where push deep links did not respect the back stack behavior when instructed to open inside the app’s WebView.
 
- Fixed a bug where the push received broadcast action contained the host package name twice.

## 2.4.0

##### Fixed

- Fixed a bug where calling Appboy.wipeData() would throw an uncaught exception when the Google Play location services library was not present.

##### Added

- Added the ability to listen for notification deleted intents from the AppboyGcmReceiver via the action suffix AppboyNotificationUtils.APPBOY_NOTIFICATION_DELETED_SUFFIX.
 
- Added a notification creation timestamp to notifications built from the AppboyGcmReceiver. This allows for calculating the duration of a notification. Intents will contain Constants.APPBOY_PUSH_RECEIVED_TIMESTAMP_MILLIS in the intent extras bundle.

##### Changed

- Deprecated AppboyNotificationUtils.isUninstallTrackingPush() to always return false. Uninstall tracking no longer requires sending a silent push notification to devices.

## 2.3.0

##### Known Issues with version 2.3.0

- If the Google Play location services library is not present, calls to Appboy.wipeData() will throw an uncaught exception.

##### Breaking

- Removed the appboyInAppMessageCustomFontFile custom xml attribute. Custom font typefaces must now be located in the res/font directory.

- To override a Braze style, both android:fontFamily and fontFamily style attributes must be set to maintain compatibility across all SDK versions. Example below:
```
 
 @font/YOUR_CUSTOM_FONT_FAMILY
 @font/YOUR_CUSTOM_FONT_FAMILY
 
```

- See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html for more information.

- Removed AppboyInAppMessageButtonView.java and AppboyInAppMessageTextView.java.
 
- Removed the AppboyGeofenceService. Geofence integration no longer requires a manifest registration. Any reference to AppboyGeofenceService can safely be removed from your manifest.
 
- Renamed AppboyUnityPlayerNativeActivityWrapper to AppboyUnityActivityWrapper.

##### Fixed

- Fixed a bug where sessions could be opened and closed with a null activity.

##### Added

- Added the ability to have the Braze SDK automatically register for Firebase Cloud Messaging.

- Enabled via com_appboy_firebase_cloud_messaging_registration_enabled boolean attribute in XML or via AppboyConfig.Builder.setIsFirebaseCloudMessagingRegistrationEnabled().
 
- The Firebase Cloud Messaging Sender ID is set via com_appboy_firebase_cloud_messaging_sender_id string attribute in XML or via AppboyConfig.Builder.setFirebaseCloudMessagingSenderIdKey().
 
- The Firebase Cloud Messaging dependencies must still be compiled into your project. The Braze SDK does not compile any Firebase Cloud Messaging dependencies as part of this release.

- Added UnityPlayerActivity support to AppboyUnityActivityWrapper. Previously only UnityPlayerNativeActivity was supported.
 
- Added a AppboyUnityPlayerActivity class for the UnityPlayerActivity for both prime31 and non-prime31 integrations.

## 2.2.5

##### Added

- Added support for wiping all customer data created by the Braze SDK via Appboy.wipeData().
 
- Added Appboy.disableSdk() to disable the Braze SDK.
 
- Added Appboy.enableSdk() to re-enable the SDK after a call to Appboy.disableSdk().

##### Changed

- Changed AppboyInAppMessageWebViewClientListener to call onDismissed() when onCloseAction() gets called for HTML in-app messages.

##### Fixed

- Fixed an issue where internal thread pool executors could get blocked on a long running task and throw RejectedExecutionException.

## 2.2.4

##### Added

- Added AppboyConfig.Builder.setIsSessionStartBasedTimeoutEnabled() which optionally sets the session timeout behavior to be either session-start or session-end based. The default behavior is to be session-end based.

- The use of this flag is recommended for long (30 minutes or longer) session timeout values.
 
- This value can also be configured via appboy.xml with the boolean com_appboy_session_start_based_timeout_enabled set to true.

## 2.2.3

##### Added

- Added support for any custom image library to work with in-app messages and the news feed, including the Glide Image Library.

- Please see IAppboy#setAppboyImageLoader(IAppboyImageLoader) for how to set a custom image library.

- Added the Glide Image Integration sample app, showcasing how to use the Glide Library.

#### Changed

- Updated the proguard rules for Fresco and Notification Enabled Tracking.

## 2.2.2

##### Added

- The Braze SDK may now optionally record when the user has disabled notifications at the app level.

- Enabled via appboy.xml using the com_appboy_notifications_enabled_tracking_on boolean attribute or via AppboyConfig.Builder.setNotificationsEnabledTrackingOn().
 
- If using proguard in your app and Braze SDK v2.2.2 or below, please add -keep class android.support.v4.app.NotificationManagerCompat { *; } to your proguard rules.
 
- (Update) Note that starting with Braze Android SDK Version 2.5.1, this feature is now automatically enabled.

## 2.2.1

##### Added

- Added Other, Unknown, Not Applicable, and Prefer not to Say options for user gender.

## 2.2.0

##### Breaking

- Removed Appboy.requestInAppMessageRefresh() and removed support for Original in-app messages. Note that all customers on version 2.2.0 and newer should use triggered in-app messages.
 
- Changed the signature of most methods on the IAppboy interface. Methods that logged values now return void instead of boolean.

- IAppboy.openSession() now returns void.
 
- IAppboy.closeSession now returns void.
 
- IAppboy.changeUser() now returns void. To get the current user, please call IAppboy.getCurrentUser().
 
- IAppboy.logCustomEvent() and all method overloads now return void.
 
- IAppboy.logPurchase() and all method overloads now return void.
 
- IAppboy.submitFeedback() now returns void.
 
- IAppboy.logPushNotificationOpened() now returns void.
 
- IAppboy.logPushNotificationActionClicked() now returns void.
 
- IAppboy.logFeedDisplayed() now returns void.
 
- IAppboy.logFeedbackDisplayed() now returns void.

- Removed AppboyFeedbackFragment.FeedbackResult.ERROR.
 
- Changed AppboyFeedbackFragment.FeedbackFinishedListener to AppboyFeedbackFragment.IFeedbackFinishedListener.
 
- Changed AppboyFeedbackFragment.FeedbackResult.SENT to AppboyFeedbackFragment.FeedbackResult.SUBMITTED.
 
- Removed Appboy.fetchAndRenderImage(). Please use getAppboyImageLoader().renderUrlIntoView() instead.
 
- Removed AppboyFileUtils.getExternalStorage().

##### Added

- Added Push Stories, a new push type that uses DecoratedCustomViewStyle to display multiple images in a single notification. We recommend posting push stories to a notification channel with vibration disabled to avoid repeated vibrations as the user navigates through the story.

##### Changed

- The Braze singleton now internally performs most actions on a background thread, giving a very substantial performance boost to all actions on the Appboy singleton.

#### Fixed

- Reduced the number of connections made when the Braze SDK downloads files and images. Note that the amount of data downloaded has not changed.

## 2.1.4

##### Added

- Added a check on Braze initialization for the “Calypso AppCrawler” indexing bot that disables all Braze network requests when found. This prevents erroneous Braze data from being sent for Firebase app indexing crawlers.
 
- Added the ability to disable adding an activity to the back stack when automatically following push deep links. Previously, the app’s main activity would automatically be added to the back stack.

- Enabled via appboy.xml using the com_appboy_push_deep_link_back_stack_activity_enabled boolean attribute or via AppboyConfig.Builder.setPushDeepLinkBackStackActivityEnabled().

- Added the ability to specify a custom activity to open on the back stack when automatically following push deep links. Previously, only the app’s main activity could be used.

- The custom activity is set via appboy.xml using the com_appboy_push_deep_link_back_stack_activity_class_name string attribute or via AppboyConfig.Builder.setPushDeepLinkBackStackActivityClass(). Note that the class name used in the appboy.xml must be the exact class name string as returned from YourClass.class.getName().

- Added the setLanguage() method to AppboyUser to allow explicit control over the language you use in the Braze dashboard to localize your messaging content.

##### Changed

- Added support for acquiring wake locks on Android O using the notification channel importance instead of the individual notification’s priority.

## 2.1.3

##### Fixed

- Fixed a bug where implicit intents for custom push broadcast receivers would be suppressed in devices running Android O.
 
- Updated the Braze ProGuard configuration to ensure Google Play Services classes required by Geofencing aren’t renamed.

## 2.1.2

##### Fixed

- Fixed a bug where sealed session flushes would not be sent on apps with long session timeouts due to Android O background service limitations.

## 2.1.1

##### Added

- Added the ability to set a custom API endpoint via appboy.xml using the com_appboy_custom_endpoint string attribute or via AppboyConfig.Builder.setCustomEndpoint().

##### Fixed

- Fixed a bug where date custom attributes were formatted in the device’s locale, which could result in incorrectly formatted dates. Date custom attributes are now always formatted in Locale.US.

## 2.1.0

##### Breaking

- Updated the minimum SDK version from 9 (Gingerbread) to 14 (Ice Cream Sandwich).

- We recommend that session tracking and in-app messages registration be done via an AppboyLifecycleCallbackListener instance using Application.registerActivityLifecycleCallbacks().

- Removed the deprecated field: AppboyLogger.LogLevel. Please use AppboyLogger.setLogLevel() and AppboyLogger.getLogLevel() instead.
 
- Updated the v4 support library dependency to version 26.0.0. To download Android Support Libraries versions 26.0.0 and above, you must add the following line to your top-level build.gradle repositories block:

```

1
2
3

```
 | 
```
maven {
 url "https://maven.google.com"
}

```
 | 

##### Added

- Added support for Android O notification channels. In the case that a Braze notification does not contain the id for a notification channel, Braze will fallback to a default notification channel. Other than the default notification channel, Braze will not create any channels. All other channels must be programatically defined by the host app.

- Note that default notification channel creation will occur even if your app does not target Android O. If you would like to avoid default channel creation until your app targets Android O, do not upgrade to this version.
 
- To set the user facing name of the default Braze notification channel, please use AppboyConfig.setDefaultNotificationChannelName().
 
- To set the user facing description of the default Braze notification channel, please use AppboyConfig.setDefaultNotificationChannelDescription().

##### Changed

- Updated the target SDK version to 26.

## 2.0.5

##### Fixed

- Fixed a bug where relative links in href tags in HTML in-app messages would get passed as file Uris to the AppboyNavigator.

##### Added

- Added Double as a valid value type on AppboyUser.setCustomUserAttribute().
 
- Added user aliasing capability. Aliases can be used in the API and dashboard to identify users in addition to their ID. See the addAlias method on AppboyUser for more information.

## 2.0.4

##### Changed

- Made further improvements to Braze singleton initialization performance.

## 2.0.3

##### Changed

- Enabled TLS 1.2 for Braze HTTPS connections running on API 16+ devices. Previously, for devices running on API 16-20, only TLS 1.0 was enabled by default.
 
- Improved Braze singleton initialization performance.

## 2.0.2

##### Fixed

- Fixed a bug where identifying a user while a request was in flight could cause newly written attributes on the old user to be orphaned in local storage.

## 2.0.1

##### Added

- Added support for displaying Youtube videos inside of HTML in-app messages and the Braze Webview. For HTML in-app messages, this requires hardware acceleration to be enabled in the Activity where the in-app message is being displayed, please see https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling. Please note that hardware acceleration is only available on API versions 11 and above.
 
- Added the ability to access Braze’s default notification builder instance from custom IAppboyNotificationFactory instances. This simplifies making small changes to Appboy’s default notification handling.
 
- Improved AppboyImageUtils.getBitmap() by adding the ability to sample images using preset view bounds.

## 2.0.0

##### Breaking

- Removed the following deprecated methods and fields:

- Removed the unsupported method Appboy.logShare().
 
- Removed Appboy.logPurchase(String, int).
 
- Removed Appboy.logFeedCardImpression() and Appboy.logFeedCardClick(). Please use Card.logClick() and Card.logImpression() instead.
 
- Removed the unsupported method Appboy.getAppboyResourceEndpoint().
 
- Removed IAppboyEndpointProvider.getResourceEndpoint(). Please update your interface implementation if applicable.
 
- Removed Appboy.registerAppboyGcmMessages(). Please use Appboy.registerAppboyPushMessages() instead.
 
- Removed AppboyInAppMessageBaseView.resetMessageMargins(). Please use AppboyInAppMessageBaseView.resetMessageMargins(boolean) instead.
 
- Removed com.appboy.unity.AppboyUnityGcmReceiver. To open Braze push deep links automatically in Unity, set the boolean configuration parameter com_appboy_inapp_show_inapp_messages_automatically to true in your appboy.xml.
 
- Removed the unsupported method AppboyUser.setBio().
 
- Removed AppboyUser.setIsSubscribedToEmails(). Please use AppboyUser.setEmailNotificationSubscriptionType() instead.
 
- Removed Constants.APPBOY_PUSH_CUSTOM_URI_KEY. Please use Constants.APPBOY_PUSH_DEEP_LINK_KEY instead.
 
- Removed Constants.APPBOY_CANCEL_NOTIFICATION_TAG.
 
- Removed com.appboy.ui.actions.ViewAction and com.appboy.ui.actions.WebAction.
 
- Removed CardCategory.ALL_CATEGORIES. Please use CardCategory.getAllCategories() instead.
 
- Removed AppboyImageUtils.storePushBitmapInExternalStorage().
 
- Removed AppboyFileUtils.canStoreAssetsLocally() and AppboyFileUtils.getApplicationCacheDir().
 
- Removed InAppMessageModal.getModalFrameColor() and InAppMessageModal.setModalFrameColor(). Please use InAppMessageModal.getFrameColor() and InAppMessageModal.setFrameColor() instead.
 
- Removed com.appboy.enums.SocialNetwork.
 
- Removed AppboyNotificationUtils.getAppboyExtras(). Please use AppboyNotificationUtils.getAppboyExtrasWithoutPreprocessing() instead.
 
- Removed AppboyNotificationUtils.setLargeIconIfPresentAndSupported(Context, AppboyConfigurationProvider, NotificationCompat.Builder). Please use AppboyNotificationUtils.setLargeIconIfPresentAndSupported(Context, AppboyConfigurationProvider, NotificationCompat.Builder, Bundle) instead.
 
- Removed AppboyInAppMessageManager.hideCurrentInAppMessage(). Please use AppboyInAppMessageManager.hideCurrentlyDisplayingInAppMessage() instead.

- Changed method signatures for gotoNewsFeed() and gotoURI() in IAppboyNavigator. Please update your interface implementation if applicable.
 
- Removed Appboy.unregisterAppboyPushMessages(). Please use AppboyUser.setPushNotificationSubscriptionType() instead.
 
- Moved getAppboyNavigator() and setAppboyNavigator() from Appboy.java to AppboyNavigator.java.
 
- The Braze Baidu China Push integration now uses the Baidu channelId as the push token. Please update your push token registration code to pass channelId instead of userId into Appboy.registerAppboyPushMessages(). The China Push sample has been updated.
 
- Removed the wearboy and wear-library modules. Android Wear 1.0 is no longer supported. Please remove AppboyWearableListenerService from your AndroidManifest.xml if applicable.

##### Added

- Added a javascript interface to HTML in-app messages with ability to log custom events, purchases, user attributes, navigate users, and close the messaage.
 
- Added the ability to set a single delegate object to custom handle all Uris opened by Braze across in-app messages, push, and the news feed. Your delegate object should implement the IAppboyNavigator interface and be set using AppboyNavigator.setAppboyNavigator().

- See https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomAppboyNavigator.java for an example implementation.
 
- You must also provide instructions for Braze to navigate to your app’s (optional) news feed implementation. To use Braze’s default handling, call AppboyNavigator.executeNewsFeedAction(context, uriAction);.
 
- Note: Previously, AppboyNavigator was only used when opening in-app messages.

##### Changed

- Removed the need to manually add declarations for Braze’s news feed and in-app message activities (AppboyFeedActivity and AppboyWebViewActivity) to the app AndroidManifest.xml. If you have these declarations in your manifest, they can be safely removed.
 
- Push notifications with web url click actions now open in an in-app webview instead of the external mobile web browser when clicked.

## 1.19.0

##### Added

- Added support for registering geofences with Google Play Services and messaging on geofence events. Please reach out to [email protected] for more information about this feature.

##### Removed

- Support for share type notification action buttons and custom notification action buttons was removed.

##### Changed

- Push deep links that can be handled by the current app are automatically opened using the current app. Previously, if another app could handle the deep link as well, a chooser dialog would open.

- Thanks to catacom
 
- See https://github.com/braze-inc/braze-android-sdk/pull/71

- AppboyImageUtils.storePushBitmapInExternalStorage() has been deprecated.

## 1.18.0

##### Breaking

- Renamed the android-sdk-jar artifact in the gh-pages branch to android-sdk-base and changed its format from jar to aar. Most integrations depend on android-sdk-ui and won’t need to take any action.

- Note: If you were compiling android-sdk-jar in your build.gradle, you must now compile android-sdk-base.

##### Added

- Added the ability to set custom read and unread icons for News Feed cards. To do so, override the Appboy.Cards.ImageSwitcher style in your styles.xml and add appboyFeedCustomReadIcon and appboyFeedCustomUnReadIcon drawable attributes.
 
- Added a sample app showcasing the FCM + Braze push integration. See /samples/firebase-push.
 
- Added a sample app for manual session integration. See /samples/manual-session-integration.

##### Removed

- Removed the -dontoptimize flag from Braze’s UI consumer proguard rules. See https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/appboy-proguard-rules.pro for the latest Proguard config.

- Thanks to mnonnenmacher
 
- See https://github.com/braze-inc/braze-android-sdk/pull/69

##### Changed

- Updated the Droidboy project to use the conventional Android Build System folder structure.

## 1.17.0

##### Breaking

- Added the ability to configure Braze completely at runtime using Appboy.configure(). Values set at runtime take precedence over their counterparts in appboy.xml. A complete example of Braze runtime configuration is available in our Hello Appboy sample app’s application class.

- Renamed com.appboy.configuration.XmlAppConfigurationProvider to com.appboy.configuration.AppboyConfigurationProvider.
 
- Appboy.configure(String) changed to Appboy.configure(Context, AppboyConfig). To maintain parity, replace your current usage with the following equivalent snippit:

```

1
2
3
4

```
 | 
```
AppboyConfig appboyConfig = new AppboyConfig.Builder()
 .setApiKey("your-api-key")
 .build();
Appboy.configure(this, appboyConfig);

```
 | 

##### Fixed

- Fixed an issue where in-app messages triggered off of push clicks wouldn’t fire because the push click happened before the in-app message configuration was synced to the device.

##### Changed

- Updated Appboy.registerAppboyPushMessages() to flush the subscription to the server immediately.
 
- Improved the accessibility-mode behavior of in-app messages.

## 1.16.0

##### Added

- Added the ability to toggle outbound network requests from the Braze SDK online/offline. See Appboy.setOutboundNetworkRequestsOffline() for more details.

##### Fixed

- Fixed a bug that caused session sealed automatic data flushes to not occur.

##### Removed

- Removed Braze notification action button icons and icon constants.

## 1.15.3

##### Fixed

- Fixed a bug where in-app messages triggered while no activity was registered with AppboyInAppMessageManager would be dropped.

## 1.15.2

##### Fixed

- Fixed a bug where in-app messages triggered while no activity was registered with AppboyInAppMessageManager would be displayed without assets.

## 1.15.1

##### Added

- Added Hebrew localization strings.

##### Changed

- Improved the initialization time of the Braze SDK.

##### Removed

- Removed fetching of the device hardware serial number as part of device metadata collection.

## 1.15.0

##### Breaking

- Deprecated AppboyInAppMessageManager.hideCurrentInAppMessage(). Please use AppboyInAppMessageManager.hideCurrentlyDisplayingInAppMessage() instead.

##### Added

- Added the option to handle session tracking and InAppMessageManager registration automatically on apps with a minimum supported SDK of API level 14 or above. This is done by registering an AppboyLifecycleCallbackListener instance using Application.registerActivityLifecycleCallbacks(). See the Hello Appboy sample app’s application class for an example.
 
- Added support for upgraded in-app messages including image-only messages, improved image sizing/cropping, text scrolling, text alignment, configurable orientation, and configurable frame color.
 
- Added support for in-app messages triggered on custom event properties, purchase properties, and in-app message clicks.
 
- Added support for templating event properties within in-app messages.
 
- Added the ability to optionally open deep links and the main activity of the app automatically when a user clicks a push notification, eliminating the need to write a custom BroadcastReceiver for Braze push. To activate, set the boolean property com_appboy_handle_push_deep_links_automatically to true in your appboy.xml. Note that even when automatic deep link opening is enabled, Braze push opened and received intents will still be sent. To avoid double opening, remove your custom BroadcastReceiver or modify it to not open deep links.

## 1.14.1

##### Fixed

- Fixed a bug where images in short news and cross promotion News Feed cards would appear too small on high resolution devices. This bug did not affect Fresco users.

##### Changed

- Updated Baidu push service jar from v4.6.2.38 to v5.1.0.48.

## 1.14.0

##### Breaking

- Renamed disableAllAppboyNetworkRequests() to enableMockAppboyNetworkRequestsAndDropEventsMode() and fixes a bug where calling Appboy.changeUser() would cause a network request even in disabled/mocked mode. Note that enableMockAppboyNetworkRequestsAndDropEventsMode should only be used in testing environments.

##### Added

- Added the ability to log negatively-priced purchases.
 
- Added the option to sort News Feed cards based on read/unread status.
 
- Added a custom News Feed click delegate. To handle News Feed clicks manually, implement IFeedClickActionListener and register an instance using AppboyFeedManager.getInstance().setFeedCardClickActionListener(). This enables use-cases such as selectively using the native browser to open web links.

##### Changed

- Added the ability to include file separators in User Ids.
 
- Changes Braze’s default Log Level from VERBOSE to INFO. Previously disabled debug log statements are enabled and available for debugging. To change Braze’s Log Level, update the value of AppboyLogger.LogLevel, e.g. AppboyLogger.LogLevel = Log.VERBOSE.

##### Removed

- Removed keep rules from consumerProguardFiles automatic Proguard configuration for potentially improved optimization for client apps. Note that client apps that Proguard Braze code must now store release mapping files for Braze to interpret stack traces. If you would like to continue to keep all Braze code, add -keep class bo.app.** { *; } and -keep class com.appboy.** { *; } to your Proguard configuration.

- See https://github.com/braze-inc/braze-android-sdk/issues/54

- Removed onRetainInstance() from the Braze News Feed fragment. As a result, the News Feed may be used in nested fragments.

## 1.13.5

##### Added

- Defined com_appboy_card_background to provide simpler control of news feed card background color.
 
- Added a convenience method to Month to allow direct instantiation from a month integer.

##### Fixed

- Fixed a database access race condition in changeUser code.

- See https://github.com/braze-inc/braze-android-sdk/issues/52 and https://github.com/braze-inc/braze-android-sdk/issues/39

##### Removed

- Removed optimizations from the private library’s Proguard configuration to allow dexing Braze with Jack and Android Gradle Plugin 2.2.0+.

## 1.13.4

##### Added

- Added ability to set push and email subscription state from Droidboy.

##### Changed

- Open sourced Braze’s Unity plugin library code.

## 1.13.3

##### Added

- Added the ability to set the large notification icon from within the GCM payload.
 
- Added consumerProguardFiles automatic Proguard configuration.

##### Fixed

- Fixed a bug where triggered HTML in-app messages would not always send button analytics.

##### Changed

- Updated Baidu push service jar from v4.3.0.4 to v4.6.2.38.
 
- Updated to log analytics for in-app messages and in-app message buttons with ‘NONE’ click actions.
 
- Updated the Droidboy sample app to use material design.
 
- Updated the Hello Appboy sample app to use Proguard.

## 1.13.2

##### Fixed

- Fixed bug where passing a JSONObject with multiple invalid keys or values to the AppboyProperties constructor would cause a ConcurrentModificationException.

## 1.13.1

##### Fixed

- Added handling to a case where certain devices were returning null Resources for GCM BroadcastReceiver onReceive contexts.

## 1.13.0

##### Added

- Added support for action-based, locally triggered in-app messages. In-app messages are now sent to the device at session start with associated trigger events. The SDK will display in-app messages in near real-time when the trigger event associated with a message occurs. Trigger events can be app opens, push opens, purchases, and custom events.

##### Changed

- Deprecated the old system of requesting in-app message display, now collectively known as ‘original’ in-app messaging, where messages were limited to displaying at app start.

##### Removed

- Removed Iab billing example code from Droidboy.

## 1.12.0

##### Breaking

- Removed the deprecated method Appboy.requestSlideupRefresh(). Please use Appboy.requestInAppMessageRefresh() instead.
 
- Removed the deprecated class AppboySlideupManager. Please use AppboyInAppMessageManager instead.

##### Changed

- HTML in-app message WebViews now use wide viewport mode and load pages in overview mode.
 
- Moved AppboyImageUtils to the private library with an updated api.
 
- Moved WebContentUtils to the private library.
 
- Renamed IInAppMessageHtmlBase to InAppMessageHtmlBase.
 
- Method count of the private Braze library has decreased by over 600 since version 1.11.0.

##### Removed

- Removed the partial duplicate of the private library’s StringUtils from the ui project.

## 1.11.2

##### Fixed

- Fixed bug where large and small icons both rendered at full size in notification remoteviews for Honeycomb/ICS. Now, if a large icon is available, only the large icon is shown. Otherwise, the small icon is used.
 
- Fixed bug where push open logs were under-reported under certain device conditions.

## 1.11.1

- Placeholder for Unity release.

## 1.11.0

##### Added

- Creates Activity based Unity in-app messages (fixing an issue where touches on in-app messages were hitting the game behind the in-app message) and removes redundant Unity permissions.
 
- Added a method for setting modal frame color on in-app messages, no longer displays in-app messages on asset download failure and adds robustness.
 
- Added deep link support to AppboyUnityGcmReceiver.

##### Changed

- Makes the WebView background for HTML in-app messages transparent. Ensure your HTML in-app messages expect a transparent background.
 
- Updated Google Play Services from to 7.5.0 to 8.3.0 and Play Services Support from 1.2.0 to 1.3.0.

- See https://github.com/braze-inc/braze-android-sdk/issues/45

- Updated Braze WebView to support redirects to deep links and enables DOM storage.

## 1.10.3

##### Added

- Added Android M Support. Under the runtime permissions model introduced in Android M, location permission must be explicitly obtained from the end user by the integrating app. Once location permission is granted, Braze will resume location data collection on the subsequent session.

## 1.10.2

##### Added

- Added the ability to log a custom event from an HTML in-app message. To log a custom event from an HTML in-app message, navigate a user to a url of the form appboy://customEvent?name=customEventName&p1=v2, where the name URL parameter is the name of the event, and the remaining parameters are logged as String properties on the event.

## 1.10.1

##### Changed

- Enabled javascript in HTML in-app messages.
 
- Deprecated logShare() and setBio() in the public interface as support in the Braze dashboard has been removed.

## 1.10.0

##### Fixed

- Fixed an issue where applications in extremely resource starved environments were seeing ANRs from the periodic dispatch BroadcastReceiver. This was not a bug in the Braze code, but a symptom of a failing application. This updates our periodic dispatch mechanism so it won’t have this symptomatic behavior, which in some cases should help developers track down the source of the actual issue (depending on the bug). Apps that only use the Braze jar file will now have to register <service android:name="com.appboy.services.AppboyDataSyncService"/> in their AndroidManifest.xml to enable Braze to periodically flush data.
 
- Fixed a very rare issue where calling Context.checkCallingOrSelfPermission() would cause an exception to be thrown on certain custom Android builds.

##### Changed

- Updated the News Feed to not show cards in the local cache that have expired.

## 1.9.2

##### Fixed

- Fixed bug triggered when AppboyWearableListenerService was not registered.

## 1.9.0

##### Breaking

- All users must add the line -dontwarn com.google.android.gms.** to their proguard config file if using proguard.

- See https://github.com/braze-inc/braze-android-sdk/issues/43

##### Added

- Added support for analytics from Android Wear devices.
 
- Added support for displaying notification action buttons sent from the Braze dashboard. To allow image sharing on social networks, add the <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" /> permission to your AndroidManifest.xml.
 
- Added delegate to FeedbackFinishedListener enabling modification of feedback messages before they are sent to Appboy. Also adds a disposition parameter to onFeedbackFinished().
 
- Added support for GIF images in the News Feed and in in-app messages via the Facebook Fresco image library (version 0.6.1) as a provided library. If found in the parent app (your app), images and GIFs will be loaded using views from the Fresco library. In order to display GIFs, Fresco must be added as a dependency in the parent app. If not found in the parent app, News Feed cards and in-app messages will not display GIFs. To disable use of the Fresco library in the UI project, set the value of com_appboy_enable_fresco_library_use to false (or omit it) in your appboy.xml; to enable Fresco use set com_appboy_enable_fresco_library_use to true in your appboy.xml. ImageView specific attributes for News Feed cards and in-app messages, such as scaleType, must now be applied programmatically instead of being applied from styles.xml. If using Fresco and proguarding your app, please include http://frescolib.org/docs/proguard.html with your proguard config. If you are not using Fresco, add the dontwarn com.appboy.ui.** directive. Note: to use Fresco with Braze it must be initialized when your application launches.
 
- Added explicit top and bottom padding values for in-app message buttons to improve button rendering on some phones. See the Appboy.InAppMessage.Button style in styles.xml.
 
- Added HTML in-app message types. HTML in-app messages consist of html along with an included zipped assets file to locally reference images, css, etc. See CustomHtmlInAppMessageActionListener in our Droidboy sample app for an example listener for the callbacks on the actions inside the WebView hosting the HTML in-app message.
 
- Added a setAttributionData() method to AppboyUser that sets an AttributionData object for the user. Use this method with attribution provider SDKs when attribution events are fired.

##### Changed

- Removed the need for integrating client apps to log push notifications inside their activity code. Please remove all calls to Appboy.logPushNotificationOpened() from your app as they are now all handled automatically by Braze. Otherwise, push opens will be incorrectly logged twice.
 
- In-app message views are now found in the com.appboy.ui.inappmessage.views package and in-app message listeners are now found in the com.appboy.ui.inappmessage.listeners package.

## 1.8.2

##### Added

- Added the ability to specify custom fonts for in-app message ui elements via the appboyInAppMessageCustomFontFile custom xml attribute.
 
- Increases the number of supported currency codes from 22 to 171. All common currency codes are now supported. The full list of supported codes is available at our Javadoc.
 
- Added the method isUninstallTrackingPush() to AppboyNotificationUtils to be able to detect background push sent for Braze uninstall tracking.

##### Changed

- Updated BigPictureStyle to show message in expanded view if summary is not present (after 1.7.0 a summary was required in expanded view to have text appear).

## 1.8.1

- Internal release for Xamarin, adds AppboyXamarinFormsFeedFragment.

## 1.8.0

##### Breaking

- Updated the minimum sdk version from 8 (froyo) to 9 (gingerbread).

##### Added

- Added an opt-in location service that logs background location events.

##### Fixed

- Fixed an in-app message lifecycle listener bug where certain lifecycle events could be fired twice.

## 1.7.3

##### Added

- Added Braze logging configurability by setting the AppboyLogger.LogLevel. This is intended to be used in development environments and should not be set in a released application as logging statements are essential for debugging.

- See https://github.com/braze-inc/braze-android-sdk/issues/38

- Added getAppboyPushMessageRegistrationId() to the Braze interface to enable retrieval of the GCM/ADM/Baidu registration ID Braze has set for the device.

##### Changed

- Updated our libraries to build against API level 22.
 
- Blacklisted custom attributes may no longer be incremented.

## 1.7.2

##### Added

- Introduced AppboyNotificationUtils.getAppboyExtrasWithoutPreprocessing() to parse Braze extras from GCM/ADM intent extras directly rather than requiring Braze extras to be parsed into a Bundle before being passed into AppboyNotificationUtils.getAppboyExtras().
 
- Added the ability to send and retrieve extra key-value pairs via a News Feed card.
 
- Added the ability to define custom key-value properties on a custom event or purchase. Property keys are strings and values may be strings, doubles, ints, booleans, or java.util.Date objects.

##### Removed

- Removed DownloadUtils.java from com.appboy.ui.support. The downloadImageBitmap() function has been moved to com.appboy.support.AppboyImageUtils.

## 1.7.1

##### Added

- Upgrades Droidboy’s custom user attributes and purchases capability and refactors the settings page.

##### Removed

- Removed requirement to manually integrate Font Awesome into the client app’s /assets folder for in-app messages with icons.

## 1.7.0

##### Breaking

- Added summary subtext in BigView style notifications. This is a breaking change in BigView style notification display. Previously the summary text in BigView style notifications was set to the bundle/dashboard summary text if it was present, or the alert message otherwise. Now the bundle/dashboard summary text is used to set the message subtext, which results in the bundle/dashboard summary text being shown in both the collapsed and expanded views. See our updated push previews for a visualization of this change.

##### Added

- Added the ability to set a custom IAppboyNotificationFactory to customize push using Appboy.setCustomAppboyNotificationFactory().
 
- Added the ability to override title and summary in BigView push notifications.
 
- Added the ability to set a default large icon for push messages by adding the com_appboy_push_large_notification_icon drawable resource to your appboy.xml.
 
- Added support for modal and full screen style in-app messages. Also adds support for including fontawesome icons and images with in-app messages, changing colors on in-app message UI elements, expanded customization options, and message resizing for tablets. Please visit our documentation for more information.
 
- Added a sample application (China Sample App) which integrates Baidu Cloud Push and Braze for sending push messages through Braze to devices without Google Services installed.
 
- Added AppboyNotificationUtils.logBaiduNotificationClick(), a utility method for logging push notification opens from push messages sent via Baidu Cloud Push by Braze.

##### Changed

- Refactors AppboyNotificationUtils into multiple classes in the com.appboy.push package and the AppboyImageUtils class in com.appboy.

## 1.6.2

##### Added

- Added a major performance upgrade that reduces CPU usage, memory footprint, and network traffic.
 
- Added 26 additional languages to localization support for Braze UI elements.
 
- Added local blocking for blacklisted custom attributes, events, and purchases. However, blacklisted attributes may still be incremented (removed in release 1.7.3).
 
- Added the ability to set the accent color for notification in Android Lollipop and above. This can be done by setting the com_appboy_default_notification_accent_color integer in your appboy.xml.
 
- Updated the News Feed to render wider on tablet screens.
 
- Added swipe handling for in-app messages on APIs <= 11.

##### Changed

- Updated our UI library to build against API level 21.

## 1.6.1

##### Fixed

- Fixed a timezone bug where short names were used for lookup, causing the default timezone (GMT) to be set in cases where the short name was not equal to the time zone Id.
 
- Fixed a bug where multiple pending push intents could override each other in the notification center.

## 1.6.0

##### Fixed

- Fixed News Feed swipe-refresh CalledFromWrongThreadException.

##### Changed

- Updated the android-L preview support from version 1.5.2 to support the public release of Android 5.0. Updates the v4 support library dependency to version 21.0.0.
 
- android.permission.GET_ACCOUNTS is no longer required during initial GCM registration for devices running Jelly Bean and higher. However, use of this permissions is recommended so that pre-Jelly Bean devices can register with GCM.
 
- android.permission.WAKE_LOCK is no longer required during initial GCM registration. However, use of this permissions is recommended to allow notifications to wake the screen and engage users when the notification arrives.
 
- No longer overwrite messages in the notification center based on collapse key (GCM) or consolidation key (ADM). Instead, overwrite based on message title and message alert, or, if specified, a custom notification id.
 
- Updated Droidboy to use the most recent Google IAB helper classes.

## 1.5.5

##### Added

- Added support for displaying Kindle notifications with images.

##### Changed

- Notifications with a minimum priority specified no longer trigger the device wakelock because Android does not display them in the status bar (they appear silently in the drawer).

##### Removed

- Removed styleable elements from the UI project. This should have no impact on consuming projects.

## 1.5.4

##### Added

- Incubates a feature to allow for runtime changes to be made to the API key. Please contact [email protected] if you want to test this feature.
 
- Added support for Big View text summaries, allowing summary text to be displayed under the main text in a notification.
 
- Added support for custom URIs to open when a notification is clicked.
 
- Added support for notification duration control. When specified, sets an alarm to remove a notification from the notification center after the specified duration.
 
- Added support for notification sounds. Users can specify a notification sound URI to play with the notification.
 
- Added support for changing in-app message duration from the client app. To do this, you can modify the slideup object passed to you in the onReceive() delegate using the new setter method IInAppMessage.setDurationInMilliseconds().

##### Changed

- Updated AppboyWebViewActivity to always fill the parent view. This forces some previously problematic websites to render at the correct size.

## 1.5.3

##### Added

- Added the ability to turn off Braze’s automatic location collection using the com_appboy_disable_location_collection boolean in appboy.xml.
 
- Added the ability to send location tracking events to Braze manually using setLastKnownLocation on the AppboyUser. This is intended to be used with com_appboy_disable_location_collection set to true so that locations are only being recorded from a single source.

## 1.5.2

##### Added

- Added support for GCM and ADM messages without collapse keys.
 
- Added support for GCM and ADM messages with notification priorities.
 
- Enabled setting a registration ID without a full push setup; registerAppboyGcmMessages() and registerAppboyPushMessages() no longer throw null pointer exceptions if Braze isn’t correctly configured to display push messages.
 
- Enabled AppboyWebViewActivity to download items.
 
- Added support for apps built targeting android-L. Braze’s process for registering push notifications had previously used an implicit service intent which caused a runtime error. Any apps built against android-L will need to upgrade to this version. However, apps with Braze that are/were built against any other versions of Android will run without issue on android-L. Thus, this is not an urgent upgrade unless you’re working with android-L.

##### Removed

- Removed extraneous features from Droidboy so it’s more easily digestible as a sample application.

## 1.5.1

##### Removed

- Removed obfuscation from parameter names on public models.

## 1.5.0

##### Added

- Added Kindle Fire support and ADM support.
 
- Added read/unread visual indicators to newsfeed cards. Use the configuration boolean com_appboy_newsfeed_unread_visual_indicator_on in appboy.xml to enabled the indicators. Additionally, moved the logFeedCardImpression() and logFeedCardClick() methods to the card objects themselves.
 
- Added support to image loading in CaptionedImage and Banner cards for dynamic resizing after loading the image url; supports any aspect ratio.
 
- Added Hello Appboy sample project that shows a minimal use case of the Braze SDK.
 
- Added wake lock to AppboyGcmReceiver in the UI project. When the WAKE_LOCK permission is set, the screen will be turned on when a notification is received.

##### Changed

- Moved constants from AppboyGcmReceiver (ie: APPBOY_GCM_NOTIFICATION_TITLE_ID, etc.) into new AppboyNotificationUtils class.
 
- Restricted productId to 255 characters for Appboy.logPurchase().

## 1.4.3

##### Removed

- Removed org.json classes from appboy.jar.

## 1.4.2

##### Added

- Added summary text for push image notifications.
 
- Added a new constant, APPBOY_LOG_TAG_PREFIX, for logging which includes the sdk version number.

## 1.4.1

##### Added

- Added automatic tests to verify that the sdk has integrated correctly.
 
- Added an optional quantity amount to in-app-purchases.

##### Changed

- Changed the device identifier from the device persistent ANDROID_ID to a non device persistent identifier for compliance with the new Google Play Terms of Service.

##### Removed

- Removed default max length and ellipsize properties in the styles.xml. The old defaults were set to 5 for maxLines for newsfeed cards and ellipsize ‘end’.

## 1.4.0

##### Added

- Added categories.
 
- Added swipe to refresh functionality to the newsfeed. The swipe to refresh colors are configurable in the colors xml file.
 
- Added configurable session timeout to the appboy xml.
 
- Added images to GCM push notifications.
 
- Added email and push notification subscription types for a user. Subscription types are explicitly opted in, subscribed, and unsubscribed. The old email boolean subscribe method has been deprecated.

##### Changed

- The feedback form now displays error popups to the user on invalid fields.

##### Removed

- Removed click logging on slideups when action is None.

## 1.3.4

##### Changed

- Minor changes to address some Lint issues in the UI project.
 
- Updated the open source AppboyGcmReceiver to use references to R.java for resource identifiers. This became possible when we moved AppboyGcmReceiver.java into the android-sdk-ui project (from the base library JAR).

## 1.3.3

##### Fixed

- Minor bug fix for a crash that occurred in certain conditions where the News Feed cards were replaced with a smaller set of cards.

## 1.3.2

##### Fixed

- Fixed a few minor style issues to be closer in line with Eclipse’s preferences.
 
- Fixed a potential synchronization issue with the AppboyListAdapter.
 
- Added the ability to set the avatar image URL for your users.
 
- Fixed support for protocol URLs and adds an ActivityAction overload that streamlines the use of deep link and web link actions.

##### Changed

- Minor update to Chinese language translation.
 
- Moved com.appboy.AppboyGcmReceiver to the open source android-sdk-ui project. Also moves some of the constants previously available as AppboyGcmReceiver.* to com.appboy.constants.APPBOY_GCM_*. The CAMPAIGN_ID_KEY previously used in our sample app is still available in com.appboy.AppboyGcmReceiver, but if you were using other constants, you’ll have to move the references.
 
- Removed input validation on custom attribute key names so that you can use foreign characters and spaces to your heart’s desire. Just don’t go over the max character limit.

## 1.3.1

##### Changed

- Updated to version 1.9.1 of Android-Universal-Image-Loader.
 
- Added Chinese language translations.
 
- Minor cleanup to imports.

## 1.3

Braze version 1.3 provides a substantial upgrade to the slideup code and reorganization for better flexibility moving forward, but at the expense of a number of breaking changes. We’ve detailed the changes in this changelog and hope that you’ll love the added power, increased flexibility, and improved UI that the new Braze slideup provides. If you have any trouble with these changes, feel free to reach out to [email protected] for help, but most migrations to the new code structure should be relatively painless.

##### Breaking

New AppboySlideupManager

- The AppboySlideupManager has moved to com.appboy.ui.slideups.AppboySlideupManager.java.
 
- An ISlideupManagerListener has been provided to allow the developer to control which slideups are displayed, when they are displayed, as well as what action(s) to perform when a slideup is clicked or dismissed.

- The slideup YOUR-APPLICATION-PACKAGE-NAME.intent.APPBOY_SLIDEUP_CLICKED event has been replaced by the ISlideupManagerListener.onSlideupClicked(Slideup slideup, SlideupCloser slideupCloser) method.

- Added the ability to use a custom android.view.View class to display slideups by providing an ISlideupViewFactory.
 
- Default handling of actions assigned to the slideup from the Braze dashboard.
 
- Slideups can be dismissed by swiping away the view to either the left or the right. (Only on devices running Honeycomb Android 3.1 or higher).

- Any slideups that are created to be dismissed by a swipe will automatically be converted to auto dismiss slideups on devices that are not running Android 3.1 or higher.

Slideup model

- A key value extras java.util.Map has been added to provide additional data to the slideup. Extras can be on defined on a per slideup basis via the dashboard.
 
- The SlideFrom field defines whether the slideup originates from the top or the bottom of the screen.
 
- The DismissType property controls whether the slideup will dismiss automatically after a period of time has lapsed, or if it will wait for interaction with the user before disappearing.

- The slideup will be dismissed automatically after the number of milliseconds defined by the duration field have elapsed if the slideup’s DismissType is set to AUTO_DISMISS.

- The ClickAction field defines the behavior after the slideup is clicked: display a news feed, redirect to a uri, or nothing but dismissing the slideup. This can be changed by calling any of the following methods: setClickActionToNewsFeed(), setClickActionToUri(Uri uri), or setClickActionToNone().
 
- The uri field defines the uri string that the slide up will open when the ClickAction is set to URI. To change this value, use the setClickActionToUri(Uri uri) method.
 
- Convenience methods to track slideup impression and click events have been added to the com.appboy.models.Slideup class.

- Impression and click tracking methods have been removed from IAppboy.java.

- A static createSlideup method has been added to create custom slideups.

IAppboyNavigator

- A custom IAppboyNavigator can be set via IAppboy.setAppboyNavigator(IAppboyNavigator appboyNavigator) which can be used to direct your users to your integrated Braze news feed when certain slideups are clicked. This provides a more seamless experience for your users. Alternatively, you can choose not to provide an IAppboyNavigator, but instead register the new AppboyFeedActivity class in your AndroidManifest.xml which will open a new Braze news feed Activity when certain slideups are clicked.

Other

- A new base class, AppboyBaseActivity, has been added that extends android.app.Activity and integrates Braze session and slideup management.
 
- A drop-in AppboyFeedActivity class has been added which can be used to display the Braze News Feed.

## 1.2.1

##### Fixed

- Fixed a ProGuard issue.

## 1.2

##### Added

- Introduced two new card types (Banner card and Captioned Image card).
 
- Added support for sending down key/value pairs as part of a GCM message.

##### Fixed

- Minor bug fixes.

## 1.1

##### Added

- Added support for reporting purchases in multiple currencies.

##### Fixed

- Fixed a bug in caching custom events to a SQLite database.
 
- Fixed a validation bug when logging custom events.

##### Changed

- Deprecated IAppboy.logPurchase(String, int).

## 1.0

- Initial release

tip

You can also find a copy of the Swift Braze SDK changelog on GitHub.

## 18.2.0

##### Added

- Adds the following public protocols that mirror each module’s public API:

- Braze.CoreModule - the top-level Braze instance.
 
- Braze.UserModule - Braze.User
 
- Braze.NotificationsModule - Braze.Notifications
 
- Braze.LiveActivitiesModule - Braze.LiveActivities
 
- Braze.FeatureFlagsModule - Braze.FeatureFlags
 
- Braze.ContentCardsModule - Braze.ContentCards
 
- Braze.BannersModule - Braze.Banners
 
- These public modules support both Swift and Objective-C, except for Braze.LiveActivitiesModule which is Swift-only.

##### Deprecated

- Deprecates all public symbols in BrazeKitCompat and BrazeUICompat, which will be removed in a future major release. Use BrazeKit (and BrazeUI for UI components) instead.

## 18.1.0

##### Fixed

- Fixes an issue where ImageOnly Content Cards with a blank (but present) image url would be discarded as invalid.

- These cards are now displayed as blank cards, matching the Android SDK’s behavior.

- Fixes an issue where aliases and other events could be dropped if logged before a session started.
 
- Fixes an issue where device info (timezone, locale, model, OS version) could be missing on new profiles if it was sent before a session started. The SDK now waits and sends that info with the session.

##### Added

- Adds @MainActor annotation to Braze.Notifications.subscribeToUpdates(_:) closure parameter to properly enforce Swift 6 strict concurrency checking.
 
- Adds Braze.Banner.RemovalReason.expired, passed to BrazeBannerPlacement.removeBannerContent(reason:) when a banner is removed from the local cache after expiring.

##### Deprecated

- Deprecates Braze.Configuration.useUUIDAsDeviceId, which will be removed in a future major release (20.0.0). Once removed, the SDK will always use a randomly generated UUID as the device ID.

- After configuration is removed, device IDs previously persisted from the identifierForVendor (IDFV) continue to be respected until local persistence is cleared and device ID becomes UUID-based.

- Deprecates Braze.Configuration.DeviceProperty.resolution (and its Objective-C equivalent BRZDeviceProperty.resolution), which will be removed in a future major release (20.0.0). This field is not used by the SDK or Braze backend.

## 18.0.0

##### Breaking

- Renames Braze.Ecommerce.ProductViewedEvent.typeIdentifiers to type on Swift and Objective-C API surfaces.
 
- Renames Live Activities push-to-start update events on Braze.LiveActivities.UpdateEvent.ActivityType, which are emitted when using Braze.LiveActivities.subscribeToStateUpdates(_:):

- pushToStartOptedOut → pushToStartUnregistered
 
- pushToStartOptOutFlushed → pushToStartUnregisterFlushed

##### Fixed

- Fixes the touch target size on in-app message close buttons to match the minimum recommended size in the Apple Human Interface Guidelines.
 
- Fixes a bug that prevented geofences from being registered with CLLocationManager when automaticLocationCollection was disabled.

##### Added

- Adds two new APIs to unregister the device’s push token or push-to-start tokens from the current user’s profile.

- braze.notifications.unregisterPush(completion:) removes the standard push token. This is also available as unregisterPush() async throws and in Objective-C.
 
- braze.liveActivities.unregisterPushToStart(types:completion:) removes Live Activities push-to-start tokens for the given activity attribute types (default: remove all push-to-start tokens). This is also available as unregisterPushToStart(types:) async throws but supports Swift only.

- Adds a new logout method to unregister the device’s push token and push-to-start tokens.

- braze.logout(completion:) removes the push token and push-to-start tokens (if available), and then wipes all local data and disables the SDK on success. This is also available as logout() async throws and in Objective-C.

##### Deprecated

- Deprecates braze.liveActivities.optOutPushToStart(type:) in favor of braze.liveActivities.unregisterPushToStart(types:completion:).

## 17.0.0

##### Breaking

- Braze.init and changeUser(userId:) no longer block the calling thread.
 
- The following properties now block the calling thread until the SDK has settled, ensuring they reflect the latest user state immediately after changeUser or Braze.init:

- braze.user.id
 
- braze.deviceId
 
- braze.contentCards.cards
 
- braze.contentCards.unviewedCards
 
- braze.contentCards.lastUpdate
 
- braze.featureFlags.featureFlags
 
- braze.featureFlags.featureFlag(id:)
 
- For UI and other latency-sensitive code paths, prefer the asynchronous getters (getCachedContentCards(_:), getUnviewedCards(_:), getLastUpdate(_:), getAllFeatureFlags(_:)).

- braze.user.id now returns nil after calling wipeData().

- Previously, braze.user.id continued to return the last user ID after wipeData().
 
- This matches the Swift SDK’s behavior with that of the Android SDK.

- changeUser now notifies Braze.ContentCards.subscribeToUpdates(_:) subscribers after a user switch, matching the existing Android SDK behavior.

- Previously, subscribers were not notified until the next Content Cards sync.

- Removes the deprecated push-to-start token update API on Braze.LiveActivities.

- Removes the deprecated Braze.LiveActivities.PushToStartTokenUpdate enum and the pushToStartTokenUpdatesStream property.
 
- Use subscribeToStateUpdates(_:) instead, which delivers the push-to-start token lifecycle events (UpdateEvent.ActivityType.pushToStartTokenRead, .pushToStartTokenFlushed, .pushToStartOptedOut, .pushToStartOptOutFlushed) as part of the complete Live Activities lifecycle in a single subscription.

##### Added

- Adds non-blocking asynchronous accessors for user and device identifiers:

- Braze.User.getId(_:) and Braze.User.getId() async — deliver on the main thread.
 
- Braze.getDeviceId(_:) and Braze.getDeviceId() async — deliver on the main thread.
 
- ObjC bridges: getIdWithCompletion: and getDeviceIdWithCompletion:.
 
- Prefer these over the synchronous properties on the main thread or in @MainActor contexts.

- Adds an sdkDisabled error on Braze.ContentCards.requestRefresh(_:), Braze.FeatureFlags.requestRefresh(_:), and Braze.Banners.requestBannersRefresh(_:). When the SDK is disabled, these now invoke their completion handler with .sdkDisabled instead of leaving it uncalled.

## 16.0.0

##### Breaking

- Updates to Content Cards behavior and reliability

- braze.contentCards.cards is now immediately updated after a card is marked as viewed, dismissed, or clicked via its context.

- Previously, these mutations were only visible in braze.contentCards.cards after the next server sync.

- Disabling Content Cards via Braze.Configuration now immediately clears braze.contentCards.cards and notifies subscribeToUpdates subscribers with an empty list.

- Previously, braze.contentCards.cards retained its last value and subscribers were not notified.

##### Added

- Adds Braze.FeatureFlags.getAllFeatureFlags(_:) — an asynchronous, callback-based getter that delivers cached feature flags on the main thread without blocking the calling thread.

## 15.2.0

##### Added

- Adds optional subtotalValue, tax, and shipping fields to Braze.Ecommerce.OrderPlacedEvent, all Braze.Ecommerce.CartUpdated variants (Replace / Add / Remove), and Braze.Ecommerce.CheckoutStartedEvent.

- Available in Objective-C on BRZEcommerceOrderPlacedEvent, BRZEcommerceCartUpdatedEvent, and BRZEcommerceCheckoutStartedEvent.

##### Fixed

- Fixes a video player configuration error for embedded YouTube videos in HTML in-app messages.

## 15.1.0

##### Added

- Adds dismiss() to Braze.Banner.Context and dismiss(using:) to Braze.Banner to dismiss a banner when using a custom UI.

- Recommended to use Braze.Banner.Context.dismiss.
 
- Both methods must be called from the main thread.
 
- Calling either method fires the onDismiss callback on any registered BrazeBannerPlacement for that placement ID.
 
- Available in Objective-C as -[BRZBannerContext dismiss] and -[BRZBanner dismissUsing:].

- Adds example implementations for building a custom UI with banners.

- See Support/Examples/Swift/Sources/Banners-Custom-UI/ for a Swift example.
 
- See Support/Examples/ObjC/Sources/Banners-Custom-UI/ for an Objective-C example.

- Adds Braze.ContentCards.getCachedContentCards(_:), Braze.ContentCards.getUnviewedCards(_:), and Braze.ContentCards.getLastUpdate(_:) — asynchronous, callback-based getters that deliver on the main thread.

##### Fixed

- Fixes a bug in the default Content Cards UI that would prevent image loading if multiple cards contained the same remote image URL. (#176)

- If multiple cards contained the same image URL, only the first card to finish loading would display the image, whereas all others would indefinitely display the loading spinner.

## 15.0.1

##### Fixed

- Improves the stability of the SDK’s internal state management, resolving a crash that would occur under low memory conditions.
 
- getBanner now returns the cached banner immediately even when the SDK is rate limited.

## 15.0.0

##### Breaking

- Banners: onDismiss now receives Braze/BannerDismissalEvent instead of Braze/Banner.
 
- Raises the Xcode version to 26.0 (17A324).
 
- Raises the minimum Mac Catalyst deployment target from iOS 13 (macOS 10.15 Catalina) to iOS 16 (macOS 13 Ventura).

- Mac Catalyst users on macOS 12 Monterey or earlier are no longer supported.

- Removes the ability to control whether the SDK prevents showing in-app messages to different users in certain edge cases.

- Removes the option to configure through Braze.Configuration.preventInAppMessageDisplayForDifferentUser.
 
- The SDK will now always behave as if this configuration option were set to true.

- Updates the Braze.WebViewBridge.ScriptMessageHandler and Braze.WebViewBridge.SchemeHandler init to have non-optional channel parameter.

##### Added

- Logs configuration validation messages when Braze.Configuration.devicePropertyAllowList omits pushEnabled or pushAuthStatus.

- Both are required for push token registration and for push notifications to behave correctly.

- Adds support for logging Braze eCommerce recommended events.

- Creates the following new event types:

- Braze.Ecommerce.ProductViewedEvent
 
- Braze.Ecommerce.CartUpdated.Replace — full cart snapshot
 
- Braze.Ecommerce.CartUpdated.Add — incremental add
 
- Braze.Ecommerce.CartUpdated.Remove — incremental remove
 
- Braze.Ecommerce.CheckoutStartedEvent
 
- Braze.Ecommerce.OrderPlacedEvent

- Adds the following API: Braze.logEcommerceEvent(_:)
 
- Adds Objective-C compatible APIs:

- -[Braze logEcommerceProductViewed:]
 
- -[Braze logEcommerceCartUpdated:]
 
- -[Braze logEcommerceCheckoutStarted:]
 
- -[Braze logEcommerceOrderPlaced:]

##### Fixed

- Fixes a rare race condition where the app would become unresponsive when calling changeUser or wipeData while an HTML in-app message or banner was in the middle of displaying.

## 14.2.1

##### Fixed

- Improves the reliability of resuming the SDK’s tracking of Live Activities when there are multiple active activity types.

- This improves the tracking of Live Activities when relaunching the app after it has been terminated.

- Fixes a compilation issue introduced in 14.2.0 on Mac Catalyst targets caused by ActivityKit imports.

## 14.2.0

##### Added

- Adds methods to observe all key events and errors in the ActivityKit API, enabling observation of real-time state and error events from the SDK’s Live Activity lifecycle.

- Adds Braze.LiveActivities.UpdateEvent, a new enum covering activity and token lifecycle events (e.g. started, active, dismissed, stale, ended, contentUpdated, pushTokenUpdated) as well as Braze SDK operation events (trackingStarted, trackingResumed, pushTokenFlushed).
 
- Adds Braze.LiveActivities.ErrorEvent, a new enum covering observation failures, token registration failures (with isTransient for retry logic), activityNotFound, and invalidPushTokenTag.
 
- Adds subscribeToStateUpdates(_:) and subscribeToErrors(_:) methods on Braze.LiveActivities to register callbacks for the above events. Both return a Braze.Cancellable to remove the subscription.
 
- For detailed usage, refer to the Braze developer guide or the Live Activities tutorial.

##### Deprecated

- Deprecates the push-to-start token update API on Braze.LiveActivities in favor of the new subscribeToStateUpdates(_:) API.

- Deprecates the Braze.LiveActivities.PushToStartTokenUpdate enum and the pushToStartTokenUpdatesStream property.
 
- Use subscribeToStateUpdates(_:) instead, which delivers the push-to-start token lifecycle events (UpdateEvent.ActivityType.pushToStartTokenRead, .pushToStartTokenFlushed, .pushToStartOptedOut, .pushToStartOptOutFlushed) as part of the complete Live Activities lifecycle in a single subscription, covering the same information as the deprecated PushToStartTokenUpdate cases without the need to maintain a separate subscription.

##### Fixed

- Improves reliability of Live Activity push token updates during app background and foreground transitions, including cold start scenarios where push-to-start activities may not have received token updates.
 
- Content cards now filter out invalid cards so users can still view remaining valid cards.

- Previously, if any of the cards were invalid in the content card sync, the entire sync would be dropped and no cards would be added.
 
- This update brings parity with the behavior on Android and Web.

## 14.1.0

##### Added

- Adds support for Banner dismissal events.

- Adds an optional onDismiss closure to both BrazeBannerUI.BannerUIView (UIKit) and BrazeBannerUI.BannerView (SwiftUI) for integrators to run custom logic when a banner is dismissed.

- By default, this closure is a no-op.

- Improves the robustness of the SDK’s internal state management.

- This release includes an internal refactor intended to make SDK behavior more consistent. No external API changes.

- Adds error logging for Banners operations, providing actionable diagnostics for persistence failures and invalid banner states.

##### Fixed

- Improves robustness around push notification and deep link handling during delayed SDK initialization.
 
- Fixes an issue where Braze.FeatureFlags.subscribeToUpdates would not trigger the update closure upon all refresh completions.

- All refresh completions, regardless of a success or error result, will now trigger the update closure. This change brings parity with the Android and Web SDKs.
 
- Previously, the update closure would not always trigger upon the completion of a refresh request, depending on whether the cached data had previously been reported.

## 14.0.4

##### Fixed

- Fixes an issue where the configuration of push notification automation would be dropped upon every other re-initialization of the Braze instance.

## 14.0.3

##### Fixed

- Push Stories now filter out invalid pages so users can still navigate through remaining valid pages.

## 14.0.2

##### Fixed

- Fixes the SwiftUI implementation of BannerView to update Banner contents in-place whenever a refresh has succeeded.
 
- Re-exposes the public initializer of BrazeInAppMessageUI.HtmlView as a designated init instead of a convenience init, which was introduced in version 14.0.0

- This allows subclasses of HtmlView to access the public initializer.

- Improves robustness of internal SDK logic around dictionary access to prevent potential crashes.

## 14.0.1

##### Fixed

- Resolves an issue where the handling of universal links defaulted to the UIApplicationDelegate implementation instead of the UISceneDelegate implementation when the app was not in foreground.

- This would occur even if there was no UIApplicationDelegate implementation, resulting in dropped universal link handling under such scenarios.

- Fixes a memory leak where base64-encoded tracking IDs in in-app messages would accumulate on background threads.
 
- Resolves an issue where in-app messages were not dismissed when the user is changed, resulting in the user seeing incorrect content.

- This change also adds changeUser dismissal reason for in-app messages.

## 14.0.0

##### Breaking

- Removes News Feed.

- This fully removes all UI elements, data models, and actions associated with News Feed.

##### Added

- Remote configuration now automatically refetches after SDK upgrades, keeping server defaults in sync and improving reliability after version changes.

##### Fixed

- Resolves an issue where long text in in-app message buttons would wrap to multiple lines.

- These messages will now match the dashboard preview behavior of truncating long text.

- Push Stories now fail gracefully when receiving null/empty deeplink values.

- Previously, an invalid deeplink would cause the Push Story’s content to appear blank.
 
- StoryPage safely trims and percent-encodes deeplink strings, dropping invalid values instead of throwing an error.
 
- StoryView only scrolls when pages exist, preventing the “Next” action from crashing when the carousel is empty.

- HTML in-app messages now reuse cached payloads to mitigate app hangs that occur in rare situations during presentation.
 
- Templated in-app messages with delayed presentation will now request templated values only after completion of the delay.

- This ensures that templated values are most up-to-date with the display of the message.
 
- Previously, the request for templated values would occur at trigger time, prior to the delay.

## 13.3.0

##### Added

- Improves reliability when sending the push token and push authorization status to the backend.

- This change ensures that push authorization status changes will be flushed immediately as soon as they are read.

## 13.2.1

##### Fixed

- Resolves an issue where an accumulation of Banners pending requests could cause the host application to hang at app startup.

- This fix performs additional cleanup to any existing requests that were accumulated from previous versions, so you do not need to do any manual cleanup.

## 13.2.0

##### Added

- Adds support for compilation with Xcode 26.0 and its corresponding operating system runtimes on all platforms supported by the Braze Swift SDK.

## 13.1.0

##### Added

- Adds support for Banner properties via new public methods on Braze.Banner instances.

- banner.stringProperty(key:) for accessing String properties.
 
- banner.numberProperty(key:) for accessing Double properties.
 
- banner.timestampProperty(key:) for accessing Int Unix millisecond timestamp properties.
 
- banner.booleanProperty(key:) for accessing Bool properties.
 
- banner.imageProperty(key:) for accessing image URL properties as Strings.
 
- banner.jsonProperty(key:) for accessing JSON properties as [String:Any] dictionaries.
 
- banner.jsonProperty<T: Decodable>(key:type:decoder:) for accessing JSON properties as values of any custom Decodable type.

- The default client-side rate limiting values for Banners refresh has been increased. For more information on SDK rate limiting, please refer to the Braze Developer Guide

##### Fixed

- Improves the behavior of VoiceOver for assets that are missing an imageAltText for Content Card and In-App Message campaigns created via the Traditional editor.

- These assets will no longer be selectable or narrated by VoiceOver. Previously, the asset would be selectable and VoiceOver would read gibberish.
 
- Drag-and-drop campaigns are not affected by this issue.
 
- Campaigns created using the Traditional editor should always have the Alt text field populated for accessible users.

## 13.0.0

##### Breaking

- Extends the functionality of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:) to be triggered for “Optional” authentication errors.

- The delegate method BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:) will now be triggered for both “Required” and “Optional” authentication errors.
 
- If you want to only handle “Required” SDK authentication errors, add a check ensuring that BrazeSDKAuthError.optional is false inside your implementation of this delegate method.

- Fixes the usage of Braze.Configuration.sdkAuthentication to take effect when enabled.

- Previously, the value of this configuration was not consumed by the SDK and the token was always attached to requests if it was present.
 
- Now, the SDK will only attach the SDK authentication token to outgoing network requests when this configuration is enabled.

- The setters for all properties of Braze.FeatureFlag and all properties of Braze.Banner have been made private. The properties of these classes are now read-only.
 
- Removes the banner.id property, which was deprecated in version 11.4.0.

- Instead, use banner.trackingId to read a banner’s campaign tracking ID.

##### Added

- Adds the boolean field optional to BrazeSDKAuthError to indicate if it is an optional authentication error.

## 12.1.0

##### Added

- Adds optional imageAltText and language fields to UI classes and structs associated with Content Card and In-App Message campaigns for improved accessibility.

- The imageAltText field contains the image accessibility alt text (if any) for the image or icon in a given campaign. The SDK’s default UI will use this field to inform how VoiceOver narrates the image portion of a campaign
 
- The optional language field is a BCP 47 tag. If it is present, VoiceOver will use the corresponding language narrator when reading the campaign. Otherwise, the user system default settings will be used.
 
- These are the classes and structs with imageAltText and language:

- Braze.ContentCard.ClassicImage
 
- Braze.ContentCard.ImageOnly
 
- Braze.ContentCard.CaptionedImage
 
- Braze.ContentCardRaw (BRZContentCardRaw in Objective-C)
 
- Braze.InAppMessage.Slideup
 
- Braze.InAppMessage.Modal
 
- Braze.InAppMessage.ModalImage
 
- Braze.InAppMessage.Full
 
- Braze.InAppMessage.FullImage
 
- Braze.InAppMessageRaw (BRZInAppMessageRaw in Objective-C)
 
- Braze.ContentCard.Classic has the language field only

- Adds provisional support for Xcode 26 Beta via the braze-inc/braze-swift-sdk-xcode-26-preview repository.

- Full support will be added to the main repository closer to the public release of Xcode 26.
 
- For any compatibility issues discovered while using the Xcode 26 Beta, submit a GitHub issue on the main repository.

## 12.0.3

##### Fixed

- Fixes the Banner rendering incompatibility with iOS 18.5+ while maintaining the correct URL redirect behavior.

- Banners can now successfully render on iOS 18.5+ without compromising click action functionality.
 
- See the changelog entries for versions 12.0.1 and 12.0.2 for further details.

## 12.0.2

⚠️ Important: This version has a known issue preventing Banners from rendering on iOS 18.5+.

##### Fixed

- Reverts Banners to the behavior found in versions 12.0.0 and prior.

- Banners remain unusable on iOS 18.5+. A future release will address this issue.

## 12.0.1

⚠️ Important: This version has a known issue in Drag-and-Drop in-app messages and Banners, preventing certain URLs from redirecting properly. Update to a newer version if you are using this feature.

##### Fixed

- Fixes an issue where setting configuration.forwardUniversalLinks = true would not properly forward universal links to the system APIs in some cases.

- The SDK now verifies that the system APIs are implemented (either in your UIApplicationDelegate or SceneDelegate) before forwarding the universal link.
 
- When multiple implementations are found, the SDK favors the SceneDelegate implementation over the UIApplicationDelegate implementation.

- Fixes an issue when configuring Braze.Configuration.Push.Automation.authorizationOptions with the .provisional option.

- Previously, the .provisional option was also applied for push primer in-app messages. This resulted in no push notification permission prompt being shown to the user.
 
- With this change, push primer in-app messages will request push notification permissions using only the .alert, .badge, and .sound options, ensuring that the system prompt is presented to the user.

- Fixes an incompatibility with iOS 18.5 where Banners would not render.

- Previously, the Banner view would be added to the view hierarchy with a height of 0 but never successfully load the HTML content.
 
- Banner views will no longer trigger superfluous about:blank URLs upon initial load.

## 12.0.0

##### Breaking

- The distributed static XCFrameworks now include their resources directly instead of relying on external resources bundles.

- When manually integrating the static XCFrameworks, you must select the Embed & Sign option for each XCFramework in the Frameworks, Libraries, and Embedded Content section of your target’s General settings.
 
- No changes are required for Swift Package Manager or CocoaPods integrations.

##### Fixed

- Fixes an App Store validation issue where Braze’s libraries privacy manifests would fail to be detected when integrating the SDK as static XCFrameworks.
 
- Fixes BrazeKitCompat ABKContentCard.expiresAt to return the correct expiration date.

- Previously, ABKContentCard.expiresAt would always return 0.

- Fixes an issue where the Braze.FeatureFlags.subscribeToUpdates(_:) update closure was being called immediately after calling changeUser(userId:) instead of waiting for the next feature flags sync result.
 
- Fixes an issue where Braze.ContentCards.subscribeToUpdates(_:) would not call the update closure whenever a sync occurred without any changes in the Content Cards data.

- Previously, the update closure would only be called when the sync resulted in a change.

- Fixes the Braze.User.set(dateOfBirth:) method to report dates using the Gregorian calendar instead of the device’s current calendar setting.

- Previously, the SDK would override input dates and formats if the device’s calendar settings were non-Gregorian.
 
- With this change, you will still need to ensure that dates provided to set(dateOfBirth:) are generated with the Gregorian calendar, but the Braze SDK will no longer override their formats inadvertently.

- Enhances the ⁠braze.wipeData() function to send a final update to all registered channel subscribers, notifying them of the data wipe.

- This update ensures that any UI components utilizing the channel’s data are properly dismissed and cleaned up.
 
- For instance, if an in-app message is currently displaying as braze.wipeData() is called, the message will be removed from display.

- Fixes braze.user.id not resetting to nil after calling braze.wipeData().

- Internally, the user identifier was properly reset, but the public braze.user.id property was not updated to reflect this change.

##### Added

- Adds the BrazeInAppMessagePresenter.dismiss(reason:) optional protocol method.

- This method enables the SDK to inform the in-app message presenter when an in-app message should be dismissed due to an internal SDK state change.
 
- Currently, this method is triggered only by calling ⁠braze.wipeData().
 
- BrazeInAppMessageUI implements this optional method and dismisses the in-app message when triggered.

## 11.9.0

##### Added

- Adds Braze.LiveActivities.pushToStartTokenUpdatesStream: AsyncStream<Braze.LiveActivities.PushToStartTokenUpdate>, an asynchronous stream which publishes updates pertaining to the Live Activities push-to-start token lifecycle.

- See Braze.LiveActivities.PushToStartTokenUpdate for all varieties of update events published by the stream.

- Adds dSYM files to the dynamic and mergeable variants of the Braze SDK XCFrameworks.

- This addresses an App Store submission validation warning when using Xcode 16.0 or later.

##### Fixed

- The SDK Debugger tool will now capture logs even when Braze.configuration.logger.level is .disabled and no SDK logging occurs locally.

- This aligns the Braze Swift SDK Debugger Tool behavior with that of the Debugger Tool on the Braze Android SDK.

- Sets the default background of BannerUIView to be transparent.
 
- Renames the VisibilityTracker.displayLinkTick method to VisibilityTracker.brazeDisplayLinkTick in BrazeUI to avoid potential naming conflicts with private system methods.

## 11.8.0

##### Added

- Network requests made by the SDK to the Braze Live Activities /push_token_tag endpoint will now be retried in the case of a request failure.
 
- Expands customizability options of custom endpoints passed when initializing a Braze instance.

- You can now specify a base path to be used for SDK network requests (i.e. “example.com/mockServer”).
 
- http schemes are now supported for use by custom endpoints (i.e. http://example.com). Previously, only https schemes were supported.

##### Fixed

- Fixes an issue where in-app messages would not always be triggered when sending Braze requests to the tracking endpoint. This occurred when both of the following conditions are true:

- The Braze.Configuration.Api.trackingPropertyAllowList did not include the .everything type.
 
- All other Braze.Configuration.TrackingProperty types were manually listed in the trackingPropertyAllowList.

- Improves the rendering behavior of Banner Cards embedded in a scroll view on hybrid development frameworks.
 
- Fixes the Banner Card view to prevent drag gestures from exposing the background of the HTML content.
 
- Fixes an issue on the Braze web view bridge where numeric values of 1 or 0 would be incorrectly reported as true or false, respectively.

## 11.7.0

##### Added

- Adds the ability for a banner container to resize when the banner content changes height.

## 11.6.1

##### Fixed

- Improves the reliability of collecting Live Activity push-to-start tokens on calling registerPushToStart:

- Push-to-start tokens will now flush to the server immediately as soon as they are retrieved.
 
- Push-to-start tokens will now be read immediately from the pushToStartToken property as soon as registerPushToStart is called, in addition to the existing behavior where an observable is set up to monitor new tokens.

- Resolves issues with the SDK’s internal state for devices that were previously affected after restoring from another device’s iCloud or iTunes backup.

- Previously, these devices would incorrectly inherit the device ID from the original device.
 
- With this update, the SDK now generates a unique device ID for each restored device, ensuring proper identification and functionality.
 
- This update follows up on the 11.6.0 fix, which prevented the issue from occurring on future backups.

## 11.6.0

##### Fixed

- Fixes the behavior in the Braze-provided UI for Banner Cards where content would not automatically be cleared from the UI when changing to a user that was not eligible for that campaign.
 
- Changes the behavior of Braze.Banners.subscribeToUpdates(_:) to match behavior of the corresponding API on the Braze Android SDK.

- Upon calling Braze.Banners.subscribeToUpdates(_:), the update handler closure will only be called if a banners sync has succeeded during the current user session.

- Previously, calling Braze.Banners.subscribeToUpdates(_:) would always result in the update handler being called one time immediately.

- Upon successfully completing a banners sync, Braze.Banners.subscribeToUpdates(_:) will call its registered update handler even if the sync result is identical to the last successful sync.

- Changes the behavior of Braze.Banners.bannersStream to match behavior of the corresponding API on the Braze Android SDK.

- Braze.Banners.bannersStream will now only emit an update immediately upon access if a banners sync has succeeded during the current user session.

- Previously, accessing Braze.Banners.bannersStream would always emit one update immediately.

- Upon successfully completing a banners sync, Braze.Banners.bannersStream will emit an update even if the sync result is identical to the last successful sync.

- JavaScript bridge methods expecting number arguments now also accept string representations of numbers.

- This change aligns the behavior of the Swift SDK with the behavior of the Web SDK.

##### Added

- Adds an optional method removeBannerContent to the BrazeBannerPlacement protocol.
 
- Locally persisted Braze SDK data will no longer transfer during OS backups. This resolves an issue introduced in 6.2.0.

## 11.5.0

##### Fixed

- Braze.banners.getBanner(for:_:) now successfully returns a cached Banner object for the requested placement ID as long as a Banner Cards sync has ever succeeded for the current user.

- Previously, it would log a warning and pass nil to the completion handler if a Banner Cards sync had not been completed for the current user during the current session specifically.
 
- This change aligns behavior with the Android SDK.

- Fixes an issue where images with the "JPEG" image type would sometimes not display in Push Stories.
 
- Fixes an issue where an in-app message in a Braze-provided UI can be displayed for an ineligible user under rare conditions.

- This may occur if the in-app message was in the process of being displayed in the UI at the same time that the user was changed to a different user.

##### Added

- Adds Braze.User.id to access the current user identifier synchronously.

- Deprecates Braze.User.id() async and Braze.User.id(queue:completion:) in favor of Braze.User.id.

- These methods will be removed fully in a future update.

- Adds the optional parameter userIDMatchBehavior to the initializers of Braze.InAppMessageRaw.Context. This determines the behavior in the UI when the current identified user is different from the one that triggered the in-app message.

- The default for Braze-provided UIs (.enforce) will enforce that the user ID matches the user ID that triggered the in-app message. If there is a mismatch, the in-app message will not be displayed.
 
- For custom UIs, the default is .ignore and a mismatch will still display the in-app message.

## 11.4.0

##### Fixed

- Fixes an issue where the SDK could hang during initialization if previous sessions generated a large number of geofence refreshes. This hang could sometimes lead to a crash by blocking the main thread for an extended period.
 
- Fixes an issue where the triggering of in-app messages could be delayed in cases where requests for updated in-app message triggers are also delayed due to rate limiting.
 
- Adds additional safeguards to ensure that ongoing network requests are dropped when changing users mid-flight.

##### Added

- When Content Cards, Feature Flags, or Banner Cards go from enabled to disabled, the stored data is removed from cache.
 
- Adds banner.trackingId to distinguish between banner objects.

- Deprecates banner.id in favor of banner.trackingId.

## 11.3.0

##### Fixed

- Fixes a behavior where calling the logClick bridge method in HTML in-app messages with "" as the button ID would log an error.

- Instead, this would log an in-app message body click to match other platforms.

##### Added

- Adds support for the Braze Banner Cards product.

- For usage details, refer to our tutorial here.

## 11.2.0

##### Fixed

- Fixes the Objective-C Braze.delegate declaration to be weak like the Swift variant.

##### Added

- Braze.prepareForDelayedInitialization now takes an optional parameter analyticsBehavior: PushEnqueueBehavior.

- Braze uses this value to determine whether any Braze push payloads received before initialization should be processed once initialization is complete.
 
- PushEnqueueBehavior.queue will enqueue received push payloads to be processed upon initialization. This option is selected by default.
 
- PushEnqueueBehavior.drop will drop received push payloads, ignoring them.

- Adds configuration properties to customize the lineSpacing, maxLineHeight, minLineHeight, and lineHeightMultiple for the header and message texts in full and modal in-app messages.
 
- Updates BrazeContentCardUI.ViewController.Attributes.defaults to be a var to allow directly editing the property for convenience.

## 11.1.1

##### Fixed

- Fixes an issue introduced in 11.0.0 where the push subscription status would be sent to the backend with an inaccurate value at startup, causing an unexpected subscription state. The SDK now sends up the accurate subscription status at each startup.

## 11.1.0

⚠️ Important: This version has a known issue related to push subscription status. Upgrade to version 11.1.1 instead.

##### Fixed

- Fixes an issue introduced in 11.0.0 where the push token status would not always be reported in all circumstances.
 
- Fixes a display bug where an in-app message would appear truncated after certain keyboard dismissal scenarios.
 
- Fixes a reference cycle in Braze.NewsFeedCard.Context that could prevent the card from being deallocated.

##### Added

- Adds a public initializer for Braze.Notifications.Payload.

## 11.0.1

##### Fixed

- Fixes an issue introduced in 11.0.0 where the push subscription status would be sent to the backend with an inaccurate value at startup, causing an unexpected subscription state. The SDK now sends up the accurate subscription status at each startup.

## 11.0.0

⚠️ Important: This version has a known issue related to push subscription status. Upgrade to version 11.1.1 instead.

##### Breaking

- Adds support for Swift 6 strict concurrency checking.

- Relevant public Braze classes and data types now conform to the Sendable protocol and can be safely used across concurrency contexts.
 
- Main thread-only APIs are now marked with the @MainActor attribute.
 
- We recommend using Xcode 16.0 or later to take advantage of these features while minimizing the number of warnings generated by the compiler. Previous versions of Xcode may still be used, but some features may generate warnings.

- When integrating push notification support manually, you may need to update the UNUserNotificationCenterDelegate conformance to use the @preconcurrency attribute to prevent warnings.

- Applying the @preconcurrency attribute on protocol conformance is only available in Xcode 16.0 or later. Reference our sample integration code here.
 
- As of Xcode 16.0, Apple has not yet audited the UNUserNotificationCenterDelegate protocol for Swift concurrency.

```

1
2
3

```
 | 
```
extension AppDelegate: @preconcurrency UNUserNotificationCenterDelegate {
// Your existing implementation
}

```
 | 

- Updates the SDWebImage dependency in BrazeUICompat and sample apps to 5.19.7+ to support Swift 6 strict concurrency checking.

#### Fixed

- Fixes the push authorization status reporting to display the proper push token status on the Dashboard when a user has not explicitly accepted or declined push permissions.

## 10.3.1

##### Fixed

- Improves the reliability of sending updates to Live Activities that were launched via a push-to-start notification to an app in the terminated state.

## 10.3.0

##### Fixed

- Fixes the in-app message orientation validation logic, which prevented certain device classes from displaying messages under certain orientation configurations.
 
- Fixes the default behavior on full-screen in-app messages to display as modals only on tablet screen sizes.

- Previously, full-screen messages would erroneously default to modal presentations on some larger phones.

- Fixes a crash when dismissing a slideup in-app message before it has finished presenting.
 
- Fixes an issue on iOS 18.0+ where the in-app message UI would persist on the screen when attempting to dismiss the message before it has finished presenting.
 
- Updates custom attribute value, custom event, and purchase string validation to use a 255 character maximum instead of a 255 byte maximum.

##### Added

- The Braze.set(identifierForAdvertiser:) and Braze.set(identifierForVendor:) methods now accept a nil parameter value to remove the identifiers from the user profile.
 
- Adds additional safeguards to Braze.Notifications.subscribeToUpdates to ensure the same Push notification can’t trigger the update closure multiple times.

## 10.2.0

##### Fixed

- Updates the content card image background color to be clear.

##### Added

- Adds support for an upcoming Braze SDK Debugging tool.

## 10.1.0

##### Fixed

- Fixes an issue affecting the Objective-C variants of BrazeDelegate, BrazeContentCardUIViewControllerDelegate and BrazeInAppMessageUIDelegate.

- When setting these delegates in Objective-C a second time, the delegate would end up being set to nil.
 
- This issue has been resolved and the delegates can now be set multiple times without issue.

##### Added

- Adds support for delayed SDK initialization, allowing you to create the Braze instance outside of application(_:didFinishLaunchingWithOptions:).

- The SDK can now be initialized asynchronously, while conserving the ability to process incoming Braze push notifications.
 
- Symbol documentation: Braze.prepareForDelayedInitialization(pushAutomation:)
 
- Integration documentation: Delayed Initialization
 
- Sample app: PushNotifications-DelayedInitialization.

- Adds the ability to prevent showing an in-app message to a different user than the one that triggered the in-app message.

- To enable this feature, set Braze.Configuration.preventInAppMessageDisplayForDifferentUser to true (default: false).

## 10.0.0

##### Breaking

- The following changes have been made when subscribing to Push events with Braze.Notifications.subscribeToUpdates(payloadTypes:_:):

- The update closure will now be triggered by both “Push Opened” and “Push Received” events by default. Previously, it would only be triggered by “Push Opened” events.

- To continue subscribing only to “Push Opened” events, pass in [.opened] for the parameter payloadTypes. Alternatively, implement your update closure to check that the type from the Braze.Notifications.Payload is .opened.

- When receiving a push notification with content-available: true, the Braze.Notifications.Payload.type will now be .received instead of .opened.

- Marks the following deprecated APIs as unavailable:

- Braze.Configuration.Api.Flavor
 
- Braze.Configuration.Api.flavor
 
- Braze.Configuration.Api.SdkMetadata
 
- Braze.Configuration.Api.addSdkMetadata(_:)
 
- Braze.ContentCard.ClickAction.uri(_:useWebview:)
 
- Braze.ContentCard.ClickAction.uri
 
- Braze.InAppMessage.ClickAction.uri(_:useWebview:)
 
- Braze.InAppMessage.ClickAction.uri
 
- Braze.InAppMessage.ModalImage.imageUri
 
- Braze.InAppMessage.Full.imageUri
 
- Braze.InAppMessage.FullImage.imageUri
 
- Braze.InAppMessage.Themes.default
 
- Braze.deviceId(queue:completion:)
 
- Braze._objc_deviceId(completion:)
 
- Braze.deviceId()
 
- Braze.User.setCustomAttributeArray(key:array:fileID:line:)
 
- Braze.User.addToCustomAttributeArray(key:value:fileID:line:)
 
- Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)
 
- Braze.User._objc_addToCustomAttributeArray(key:value:)
 
- Braze.User._objc_removeFromCustomAttributeArray(key:value:)
 
- gifViewProvider
 
- GifViewProvider.default

- Removes the deprecated APIs:

- Braze.Configuration.DeviceProperty.pushDisplayOptions
 
- Braze.InAppMessageRaw.Context.Error.extraProcessClickAction

- Removes the deprecated BrazeLocation class in favor of BrazeLocationProvider.

##### Fixed

- Fixes a crash when handling a scheme-based deep link containing a registered applink domain (e.g. applinks:example.com with a deep link to app://example.com/path).

##### Added

- Adds support to subscribe to “Push Received” events via Braze.Notifications.subscribeToUpdates(payloadTypes:_:).

- The following notifications will trigger this subscription:

- Notifications received in the foreground
 
- Notifications with the field content-available: true received in the foreground or background

- The following notifications will not trigger this subscription:

- Notifications received while terminated
 
- Notifications received in the background without the field content-available: true

- The new parameter payloadTypes will allow you to subscribe to “Push Opened” events, “Push Received” events, or both. If the parameter is omitted, it will subscribe to both by default.
 
- If you are using manual push integration, you will need to first implement UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:), and make sure to call Braze.Notifications.handleForegroundNotification(notification:) within your implementation. Then, use subscribeToUpdates as noted above. See our guide on push notification integration for more info.

- Adds the public property Braze.Notifications.Payload.type.
 
- Adds the Braze.WebViewBridge.ScriptMessageHandler.init(braze:) initializer enabling a simpler way to initialize the ScriptMessageHandler for adding it to user-provided web views.

## 9.3.1

##### Fixed

- Fixes an issue where the Braze.FeatureFlag.subscribeToUpdates(_:) callback was not triggered at app launch when the cached feature flags matched the remote feature flags.
 
- Fixes an issue in Objective-C projects where the return value of Braze.FeatureFlag.jsonProperty(key:) would incorrectly encode any entry value equal to null under certain conditions.

- [String: Any] dictionaries returned by the Swift API will now drop null values.
 
- NSDictionary objects returned by the Objective-C API will now encode null values as NSNull.

## 9.3.0

##### Added

- Adds Objective-C support for the BrazeInAppMessageUIDelegate.inAppMessage(_:prepareWith:) method.

- Customization of ViewAttributes via the attributes property is not available in the Objective-C version of PresentationContextRaw.

- Adds Braze.FeatureFlag.jsonProperty(key:type:decoder:) to decode jsonobject type Feature Flag properties into custom Decodable types.
 
- Deprecates the existing Feature Flag APIs, to be removed in a future version:

- Braze.FeatureFlag.jsonStringProperty(key:) has been deprecated.
 
- Braze.FeatureFlag.jsonObjectProperty(key:) has been deprecated in favor of Braze.FeatureFlag.jsonProperty(key:).

##### Fixed

- Fixes an issue where the preferredOrientation on the presentation context of an in-app message would not be respected.

## 9.2.0

##### Added

- Adds the openNewWindowLinksInBrowser configuration (default: false) to Braze.ModalContext.

- Set this value in the braze(_:willPresentModalWithContext:) method of your BrazeDelegate to specify whether to launch the device browser to open web view hyperlinks that normally open a new tab or window.

##### Fixed

- Fixes an issue with the automatic push integration feature that could cause the SDK not to send the device token to Braze.
 
- Fixes an issue that prevented external links, which open in a new tab, from being activated in presented web views.

## 9.1.0

##### Added

- Adds support for 3 new Feature Flag property types and various APIs for accessing them:

- Braze.FeatureFlag.timestampProperty(key:) for accessing Int Unix millisecond timestamps.
 
- Braze.FeatureFlag.imageProperty(key:) for accessing image URLs as Strings.
 
- Braze.FeatureFlag.jsonObjectProperty(key:) for accessing JSONs as [String:Any] dictionaries.
 
- Braze.FeatureFlag.jsonStringProperty(key:) for accessing JSONs as Strings.

- Adds safeguards when reading the device model.

##### Fixed

- Fixes the duplicate symbols compilation errors and runtime warnings that may occur under specific conditions when integrating BrazeKit and either BrazeNotificationService or BrazePushStory via CocoaPods.

## 9.0.0

##### Breaking

- Removes the default privacy tracking domains from the BrazeKit privacy manifest.

- If you are using the Braze data tracking features, you will need to manually add your tracking endpoint to your app-level privacy manifest.
 
- Refer to the updated tutorial for integration guidance.

- Removes the deprecated BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError).

- This method was originally deprecated in release 5.14.0.
 
- Failing to switch to the new delegate method will not trigger a compiler error; instead, the BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method you define will simply not be called.

##### Fixed

- Adds the missing NSPrivacyCollectedDataTypes key to the BrazePushStory privacy manifest.

## 8.4.0

##### Added

- Expands Geofences behavior in the background while “When In Use” authorization is selected:

- Adds the Braze.Location.Configuration.allowBackgroundGeofenceUpdates property to toggle whether geofences should be updated in the background.

- When using this setting, verify that you have enabled the Location updates background mode.

- Adds the Braze.Location.Configuration.distanceFilter property to configure the minimum distance sensitivity for triggering a location update.

- Adds support for the message_extras Liquid tag for in-app messages.

## 8.3.0

##### Added

- Adds early access for a third alternative repository which provides all Braze modules as mergeable XCFrameworks. For instructions on how to leverage it, refer to the repository README:

- braze-inc/braze-swift-sdk-prebuilt-mergeable

##### Fixed

- Adds a missing privacy manifest for BrazePushStory.
 
- Fixes an invalid privacy manifest warning in BrazeLocation when submitting to the App Store as a dynamic XCFramework.
 
- Fixes an issue where already enqueued in-app messages would not be removed from the stack after subsequent .reenqueue and .discard display actions.
 
- Fixes an issue preventing retried requests from using an updated SDK authentication token until a new request was scheduled for processing.
 
- Purchases, custom events, and nested custom user attributes can now include properties with values of any type conforming to BinaryInteger (Int64, UInt16, etc).

- All values will be cast to Int before being logged.
 
- This resolves an issue with a bugfix in 7.6.0.

## 8.2.1

##### Fixed

- Fixes App Store validation issues when archiving with Xcode 15.3.

## 8.2.0

##### Added

- Adds support for remotely starting Live Activities via push notifications.

- Adds the following methods to the liveActivities module:

- registerPushToStart(forType:name:) -> Task<Void, Never>
 
- optOutPushToStart(type:)

- This feature requires iOS 17.2 or higher.
 
- For usage details, refer to the updated Live Activities tutorial here.

- Adds return values for existing liveActivities methods:

- launchActivity(pushTokenTag:activity:) now returns a discardable Task<Void, Never>?.

- Adds pushToStartTokens as a new tracking property type.

## 8.1.0

##### Added

- Adds the is_test_send boolean value in the in-app message JSON representation.
 
- Adds the Braze.subscribeToSessionUpdates(_:) method and Braze.sessionUpdatesStream property to subscribe to the session updates events generated by the SDK.
 
- Adds public APIs to access BrazeKit, BrazeLocation and BrazeUI resources bundles:

- Braze.Resources.bundle
 
- BrazeLocationResources.bundle
 
- BrazeUIResources.bundle

- BrazeKit.overrideResourceBundle and BrazeUI.overrideResourceBundle have been deprecated in favor of BrazeKit.overrideResourcesBundle and BrazeUI.overrideResourcesBundle.
 
- Re-enables visionOS sample apps requiring SDWebImage in Examples-CocoaPods.xcworkspace. SDWebImage for visionOS is now supported when using CocoaPods.
 
- Updated SDWebImage dependency in BrazeUICompat to 5.19.0+.

##### Fixed

- Fixes multiple issues on visionOS:

- Sessions now properly start as expected.
 
- The click behavior Open Web URL Inside App now properly opens the URL in a modal web view. Previously, the URL would always be opened using the default web browser.
 
- Braze.Notifications.Payload.targetScene is now defined.
 
- Braze.URLContext.targetScene is now properly set by the SDK for in-app messages click actions.
 
- Braze.WebViewBridge.ScriptMessageHandler.init(logClick:logError:showNewsFeed:closeMessage:braze:) is now defined.
 
- [BrazeDelegate.braze(:willPresentModalWithContext:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(:willpresentmodalwithcontext:)-1fj41) now has a default implementation.
 
- Handling network requests and persisting data properly extend the lifetime of the application for processing.

## 8.0.1

##### Fixed

- Fixes the reported SDK version, see 8.0.0.
 
- Removes crash data from the BrazeKit privacy manifest. This data type is not collected by Braze.

## 8.0.0

##### ⚠️ Warning

- This release reports the SDK version as 7.7.0 instead of 8.0.0.

##### Breaking

- Compiles the SDK using Xcode version 15.2 (15C500b).

- This also raises the minimum deployment targets to iOS 12.0 and tvOS 12.0.

- The BrazeLocation class is now marked as unavailable. It was previously deprecated in favor of BrazeLocationProvider in 5.8.1.

##### Added

- Adds support for visionOS 1.0.

- ⚠️ Rich push notifications and Push Stories may not display as expected on visionOS 1.0. We are monitoring the latest versions for potential fixes.
 
- ⚠️ CocoaPods is not yet supported by SDWebImage for visionOS. visionOS sample apps requiring SDWebImage have been disabled in the Examples-CocoaPods.xcworkspace. Refer to the SwiftPM or manual integration Xcode project instead.

## 7.7.0

##### Added

- Updates the prebuilt release assets to include the privacy manifest for manual integrations of SDWebImage.

- Follow the manual integration guide to add the SDWebImage.bundle to your project for static XCFrameworks.

- Enhances support for language localizations.

- Introduces a localization for Azerbaijani strings.
 
- Updates Ukrainian localization strings for accuracy.

##### Fixed

- Fixes the default button placement for full in-app message views.
 
- Fixes an issue where setting Braze.Configuration.Api.endpoint to a URL with invalid characters could cause a crash.

- If the SDK is given an invalid endpoint, it will no longer attempt to make network requests and will instead log an error.

- Fixes an issue preventing BrazeLocation from working correctly when using the dynamic XCFrameworks.

## 7.6.0

##### Added

- Adds the Braze.InAppMessage.Data.isTestSend property, which indicates whether an in-app message was triggered as part of a test send.
 
- Adds logic to separate Braze data into tracking and non-tracking requests.

- Adds the following methods to set and edit the allow list for properties that will be used for tracking:

- Braze.Configuration.Api.trackingPropertyAllowList: Set the initial allow list before initializing Braze.
 
- Braze.updateTrackingAllowList(adding:removing:): Update the existing allow list during runtime.

- For full usage details on these configurations, refer to our tutorial here.

##### Fixed

- Adds safeguards to prevent a rare race condition occuring in the SDK network layer.
 
- Prevents in-app message test sends from attempting re-display after being discarded by a custom in-app message UI delegate.
 
- Fixes an issue in the default Braze in-app message UI where some messages were not being removed from the stack after display.
 
- Fixes the compilation of BrazeKitCompat and BrazeUICompat in Objective-C++ projects.
 
- Fixes an issue in BrazeUICompat where the header text in Full or Modal in-app messages would be duplicated in place of the body text under certain conditions.
 
- Fixes the encoding of values of types Float, Int8, Int16, Int32, Int64, UInt, UInt8, UInt16, UInt32 and UInt64. Those types were previously not supported in custom events and purchase properties.
 
- Fixes an issue preventing purchase events from being logged when the product identifier has a leading dollar sign.
 
- Fixes an issue preventing custom attributes from being logged when the attribute key has a leading dollar sign.

## 7.5.0

##### Added

- Adds privacy manifests for BrazeKit and BrazeLocation to describe Braze’s data collection policies. For more details, refer to Apple’s documentation on privacy manifests.

- More fine-tuned configurations to manage your data collection practices will be made available in a future release.

- Adds the optInWhenPushAuthorized configuration property to specify whether a user’s notification subscription state should automatically be set to optedIn when updating push permissions to authorized.
 
- The WebKit Inspector developer tool is now enabled by default for all instances of BrazeInAppMessagesUI.HtmlView. It can be disabled by setting BrazeInAppMessagesUI.HtmlView.Attributes.allowInspector to false.

##### Fixed

- Fixes an issue with the code signatures of XCFrameworks introduced in 7.1.0.
 
- Fixes a crash on tvOS devices running versions below 16.0, caused by the absence of the UIApplication.openNotificationSettingsURLString symbol in those OS versions.
 
- Fixes an issue where a content card would not display if the value under “Redirect to Web URL” was an empty string.
 
- Fixes incorrect behavior in BrazeUI where tapping the body of a Full or Modal in-app message with buttons and an “Image Only” layout would dismiss that message and process the button’s click action.

- Tapping the body will now be a no-op, bringing parity with other platforms.

## 7.4.0

##### Added

- Adds two alternative repositories to support specialized integration options. For instructions on how to leverage them, refer to their respective READMEs:

- braze-inc/braze-swift-sdk-prebuilt-static which provides all Braze modules as static XCFrameworks.
 
- braze-inc/braze-swift-sdk-prebuilt-dynamic which provides all Braze modules as dynamic XCFrameworks.

- In-App Message assets from URLs containing the query parameter cache=false will not be prefetched.

- Additionally, when presented as a part of In-App Messages or Content Cards, those URLs will be fetched using the URLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData caching policy, which always requests a fresh version from the source and ignores any cached versions.

##### Fixed

- Fixes XCFrameworks headers to use the #import syntax instead of @import for compatibility with Objective-C++ contexts.
 
- Fixes the push token tag validation during Live Activity registration, accepting strings up to 256 bytes instead of 255 bytes.
 
- Braze.ContentCards.unviewedCards no longer includes Control cards to bring parity with Android and Web.
 
- Fixes an Objective-C metaclass crash that occurs when initializing a custom subclass of certain BrazeUI views.

## 7.3.0

##### Added

- Adds support for Expo Notifications event listeners when using the automatic push integration.

##### Fixed

- Fixes a rare concurrency issue that might result in duplicated events when logging large amount of events.
 
- Fixes an issue where user.set(dateOfBirth:) was not setting the date of birth accurately due to variations in the device’s timezone.

## 7.2.0

##### Added

- Exposes the BrazePushStory.NotificationViewController.didReceive methods for custom handling of push story notification events.

##### Fixed

- Resolves an issue for in-app messages with buttons where tapping on the body would incorrectly execute the button’s click action.

- Now, when you tap on the body of an in-app message with buttons, no event should occur.

- Resolves a potential deadlock under rare circumstances in BrazeUI’s In-App messages presentation.
 
- Fixes the default implementation for the Objective-C representation of BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:url:buttonId:message:view:) to return the proper click action URL.
 
- Resolves an issue where the body of the modal in-app message may be displayed stretched on some device models.
 
- Resolves an issue where BrazeInAppMessageUI could fail to detect the correct application window for presenting its post-click webview.

- BrazeInAppMessageUI now prefers using the current key UIWindow instead of the first one in the application’s window stack.

##### Removed

- Braze.Configuration.DeviceProperty.pushDisplayOptions has been deprecated. Providing this value no longer has an effect.

## 7.1.0

##### Fixed

- Resolves an issue preventing templated in-app messages from triggering if a previous attempt to display the message failed within the same session.
 
- Fixes an issue that prevented custom events and nested custom attributes from logging if had a property with a value that was prefixed with a $.
 
- Fixes a bug in the Content Cards feed UI where the empty feed message would not display when the user only had control cards in their feed.
 
- Adds additional safeguards when reading the device model.

##### Added

- Adds a code signature to all XCFrameworks in the Braze Swift SDK, signed by Braze, Inc..
 
- BrazeInAppMessageUI.DisplayChoice.later has been deprecated in favor of BrazeInAppMessageUI.DisplayChoice.reenqueue.

## 7.0.0

##### Breaking

- The useUUIDAsDeviceId configuration is now enabled by default.

- For more details on the impacts, refer to this Collecting IDFV - Swift.

- The Banner Content Card type and corresponding UI elements have been renamed to ImageOnly. All member methods and properties remain the same.

- Braze.ContentCard.Banner → Braze.ContentCard.ImageOnly
 
- BrazeContentCardUI.BannerCell → BrazeContentCardUI.ImageOnlyCell

- Refactors some text layout logic in BrazeUI into a new Braze.ModalTextView class.
 
- Updates the behavior for Feature Flags methods.

- FeatureFlags.featureFlag(id:) now returns nil for an ID that does not exist.
 
- FeatureFlags.subscribeToUpdates(:) will trigger the callback when any refresh request completes with a success or failure.

- The callback will also trigger immediately upon initial subscription if previously cached data exists from the current session.

##### Fixed

- Fixes compiler warnings about Swift 6 when compiling BrazeUI while using Xcode 15.
 
- Exposes public imports for ABKClassicImageContentCardCell.h and ABKControlTableViewCell.h for use in the BrazeUICompat layer.
 
- Adds additional safeguards around invalid constraint values for BrazeInAppMessageUI.SlideupView.
 
- Resolves a Content Cards feed UI issue displaying a placeholder image in Classic cards without an attached image.

##### Added

- Adds the enableDarkTheme property to BrazeContentCardUI.ViewController.Attributes.

- Set this field to false to prevent the Content Cards feed UI from adopting dark theme styling when the device is in dark mode.
 
- This field is true by default.

## 6.6.2

##### Fixed

- Fixes an issue preventing purchase events from being logged when the product identifier has a leading dollar sign ($).
 
- Fixes an issue preventing custom attributes from being logged when the attribute key has a leading dollar sign ($).

## 6.6.1

##### Fixed

- Fixes a crash in the geofences feature that could occur when the number of monitored regions exceeded the maximum count.
 
- Fixes an issue introduced in 6.3.1 that would always update a user’s push subscription status to optedIn on app launch if push permissions were authorized on the device settings.

- The SDK now will only send the subscription status at app launch if the device notification settings goes from denied to authorized.

- Braze.ContentCard.logClick(using braze: Braze) will now log a click regardless of whether the ContentCard has a ClickAction.

- This behavior differs from the default API Braze.ContentCard.Context.logClick(), which has the safeguard of requiring a ClickAction to log a click.

## 6.6.0

##### Fixed

- Fixes an issue in HTML in-app messages where custom event and purchase properties would always convert values for 1 and 0 to become true and false, respectively.

- These property values will now respect their original form in the HTML.

- Prevents the default Braze UI from displaying in-app messages underneath the keyboard when Stage Manager is in use.

##### Added

- Adds the Braze.FeatureFlags.logFeatureFlagImpression(id: String) method.
 
- Adds the optional merge parameter to the Objective-C representation of the setCustomAttribute(key:dictionary:merge:) method.

## 6.5.0

##### Fixed

- Content card impressions can now be logged any number of times on a single card, bringing parity with Android and Web.

- This removes the limit introduced in 6.3.1 where a card impression could only be logged once per session.
 
- In the Braze-provided Content Cards feed UI, impressions will be logged once per feed instance.

##### Added

- Adds a simplified method for integrating push notification support into your application:

- Automatic push integration can be enabled by setting configuration.push.automation = true on your configuration object.

- This eliminates the need for the manual push integration outlined in the Implement the push notification handlers manually tutorial section.
 
- When enabled, the SDK will automatically implement the necessary system delegate methods for handling push notifications.
 
- Compatibility with other push providers, whether first or third party, is maintained. The SDK will automatically handle only Braze push notifications, while original system delegate methods will be executed for all other push notifications.

- Each automation step can be independently enabled or disabled. For example, configuration.push.automation.requestAuthorizationAtLaunch = false can be used to prevent the automatic request for push permissions at launch.
 
- Resources:

- Updated Standard Push Notifications tutorial.
 
- Braze.Configuration.Push.automation property.
 
- Braze.Configuration.Push.Automation type (provides details about the behavior of each automation step).

- Adds the Braze.Configuration.forwardUniversalLinks configuration. When enabled, the SDK will redirect universal links from Braze campaigns to the appropriate system methods.
 
- Adds the Braze.Notifications.subscribeToUpdates(_:) method to subscribe to the push notifications handled by the SDK.

- This method runs the provided closure with a Braze.Notifications.Payload class representing the processed push notification.

- Adds the Braze.Notifications.deviceToken property to access the most recent notification device token received by the SDK.

## 6.4.0

##### Fixed

- Fixes an issue preventing text fields from being selected in HTML IAMs for iOS 15.
 
- Fixes an issue where the device model was inaccurately reported as iPad on macOS (Mac Catalyst and Designed for iPad configurations).
 
- Fixes an issue where custom event and purchase properties would not accept an entry if its value was an empty string.
 
- Fixes a crash that occurred in the default UI for Content Cards when encountering a zero-value aspect ratio.
 
- Fixes an issue introduced in 6.0.0 where images in in-app messages would appear smaller than expected when using the compatibility UI (BrazeUICompat).

##### Added

- Adds the unviewedCards convenience property to the Braze.ContentCards class to get the unviewed content cards for the current user.

## 6.3.1

##### Fixed

- Fixes an issue where the previous user’s data would not be flushed after calling changeUser(userId:sdkAuthSignature:) when the SDK authentication feature is enabled.
 
- A content card impression can now be logged once per session. Previously, the Braze-provided Content Cards UI would limit to a single impression per card at maximum, irrespective of sessions.
 
- Fixes an issue that previously caused push notification URLs with percent-encoded characters to fail during decoding.
 
- Fixes a behavior to automatically set a user’s push subscription state to optedIn after push permissions have explicitly been authorized via the Settings app.
 
- Correctly hides shadows on in-app messages that are configured with a transparent background.
 
- Fixes a rare crash occurring when deinitializing the Braze instance.

##### Added

- Adds additional logging for network-related decoding errors.

## 6.3.0

##### Fixed

- “Confirm” and “Cancel” notification categories now show the correct titles on the action buttons.

##### Added

- Adds a new SDKMetadata option .reactnativenewarch for the React Native New Architecture.
 
- Adds public initializers for Braze.URLContext and Braze.ModalContext.

## 6.2.0

##### Fixed

- Fixes a crash introduced in 6.0.0 when displaying an HTML in-app message using the BrazeUICompat module.
 
- Removed a system call that is known to be slow on older versions of macOS. This resolves the SDK hanging during initialization on Mac Catalyst when running on affected macOS versions.

##### Added

- Adds support for target attributes on anchor tags in HTML in-app messages (e.g. <a href="..." target="_blank"></a>).

- Adding the target attribute to links will allow them to open in a new webview without dismissing the current in-app message.
 
- This behavior can be disabled via the linkTargetSupport property of the BrazeInAppMessageUI.HtmlView.Attributes struct.
 
- See our Custom HTML in-app messages documentation page for more details.

## 6.1.0

##### Fixed

- Fixes an issue that led to disproportionately large close buttons on in-app messages when the user has set a large font size in the device settings.
 
- Fixes an issue that would lock the screen in a specific orientation after the dismissal of an in-app message customized to be presented in that orientation.

- This issue only impacted iOS 16.0+ devices.

##### Added

- Adds new versions of setCustomAttribute to the User object to support nested custom attributes.

- Renames User.setCustomAttributeArray(key: String, array: [String]?) to setCustomAttribute(…) to align it with other custom attribute setters, and adds “string” to the addTo and removeFrom attribute array methods to clarify which custom attributes they’re used for.

## 6.0.0

##### Breaking

- The in-app message data models sent to BrazeInAppMessagePresenter.present(message:) now contain remote asset URLs. Previously, these data models would contain local asset URLs.

- This change is only breaking in two situations:

- When implementing a custom BrazeInAppMessagePresenter.
 
- When relying on asset URLs being local in the message provided by BrazeInAppMessageUIDelegate.inAppMessage(_:displayChoiceForMessage:)

- The in-app message data models available from the other BrazeInAppMessageUIDelegate methods remain unchanged and contain local asset URLs.

##### Added

- The in-app message context now provides two additional methods:

- getLocalAssets(urls:destinationURL:completionHandler:): Retrieves the local assets associated with the given remote asset URLs.
 
- withLocalAssets(message:destinationURL:completionHandler:): Returns a modified in-app message with all remote asset URLs replaced with local ones.

## 5.14.0

##### Fixed

- VoiceOver now correctly focuses on in-app message views when they are presented.
 
- Fixes an issue causing in-app messages with re-eligibility disabled to display multiple times under certain conditions.
 
- Fixes an issue where modal and full in-app message headers were truncated on devices running iOS versions lower than 16 when displaying non-ASCII characters.
 
- The dynamic variant of BrazeUI.framework in the release artifact braze-swift-sdk-prebuilt.zip is now an actual dynamic framework. Previously, this specific framework was mistakenly distributed as a static framework.

##### Added

- Adds the BrazeSDKAuthDelegate protocol as a separate protocol from BrazeDelegate, allowing for more flexible integrations.

- Apps implementing BrazeDelegate.braze(_:sdkAuthenticationFailedWithError:) should migrate to use BrazeSDKAuthDelegate and remove the old implementation. The BrazeDelegate method will be removed in a future major release.

## 5.13.0

##### Fixed

- Fixes an issue where the SDK would automatically track body clicks on non-legacy HTML in-app messages.

##### Added

- Adds the synchronous deviceId property on the Braze instance.

- deviceId(queue:completion:) is now deprecated.
 
- deviceId() async is now deprecated.

- Adds the automaticBodyClicks property to the HTML in-app message view attributes. This property can be used to enable automatic body clicks tracking on non-legacy HTML in-app messages.

- This property is false by default.
 
- This property is ignored for legacy HTML in-app messages.

## 5.12.0

Starting with this release, this SDK will use Semantic Versioning.

##### Added

- Adds json() and decoding(json:) public methods to the Feature Flag model object for JSON encoding/decoding.

## 5.11.2

##### Fixed

- Fixes a crash occurring when the SDK is configured with a flush interval of 0 and network connectivity is poor.

## 5.11.1

##### Fixed

- Fixes an issue preventing the correct calculation of the delay when retrying failed requests. This led to a more aggressive retry schedule than intended.
 
- Improves the performance of Live Activity tracking by de-duping push token tag requests.
 
- Fixes an issue in logClick(using:) where it would incorrectly open the url field in addition to logging a click for metrics. It now only logs a click for metrics.

- This applies to the associated APIs for content cards, in-app messages, and news feed cards.
 
- It is still recommended to use the associated Context object to log interactions instead of these APIs.

##### Added

- Adds BrazeKit.overrideResourceBundle and BrazeUI.overrideResourceBundle to allow for custom resource bundles to be used by the SDK.

- This feature is useful when your setup prevents you from using the default resource bundle (e.g. Tuist).

## 5.11.0

##### Added

- Adds support for Live Activities via the liveActivities module on the Braze instance.

- This feature provides the following new methods for tracking and managing Live Activities with the Braze push server:

- launchActivity(pushTokenTag:activity:)
 
- resumeActivities(ofType:)

- This feature requires iOS 16.1 and up.
 
- To learn how to integrate this feature, refer to the setup tutorial.

- Adds logic to re-synchronize Content Cards on SDK version changes.
 
- Adds provisional support for Xcode 14.3 Beta via the braze-inc/braze-swift-sdk-xcode-14-3-preview repository.

## 5.10.1

##### Changed

- Dynamic versions of the prebuilt xcframeworks are now available in the braze-swift-sdk-prebuilt.zip release artifact.

## 5.10.0

##### Fixed

- Fixes an issue where test content cards were removed before their expiration date.
 
- Fixes an issue in BrazeUICompat where the status bar appearance wasn’t restored to its original state after dismissing a full in-app message.
 
- Fixes an issue when decoding notification payloads where some valid boolean values weren’t correctly parsed.

##### Changed

- In-app modal and full-screen messages are now rendered with UITextView, which better supports large amounts of text and extended UTF code points.

## 5.9.1

##### Fixed

- Fixes an issue preventing local expired content cards from being removed.
 
- Fixes a behavior that could lead to background tasks extending beyond the expected time limit with inconsistent network connectivity.

##### Added

- Adds logImpression(using:) and logClick(buttonId:using:) to news feed cards.

## 5.9.0

##### Breaking

- Raises the minimum deployment target to iOS 11.0 and tvOS 11.0.
 
- Raises the Xcode version to 14.1 (14B47b).

##### Fixed

- Fixes an issue where the post-click webview would close automatically in some cases.
 
- Fixes a behavior where the current user messaging data would not be directly available after initializing the SDK or calling changeUser(userId:).
 
- Fixes an issue preventing News Feed data models from being available offline.
 
- Fixes an issue where the release binaries could emit warnings when generating dSYMs.

##### Changed

- SwiftPM and CocoaPods now use the same release assets.

##### Added

- Adds support for the upcoming Braze Feature Flags product.
 
- Adds the braze-swift-sdk-prebuilt.zip archive to the release assets.

- This archive contains the prebuilt xcframeworks and their associated resource bundles.
 
- The content of this archive can be used to manually integrate the SDK.

- Adds the Examples-Manual.xcodeproj showcasing how to integrate the SDK using the prebuilt release assets.
 
- Adds support for Mac Catalyst for example applications, available at Support/Examples/
 
- Adds support to convert from Data into an in-app message, content card, or news feed card via decoding(json:).

## 5.8.1

##### Fixed

- Fixes a conflict with the shared instance of ProcessInfo, allowing low power mode notifications to trigger correctly.

##### Changed

- Renames the BrazeLocation class to BrazeLocationProvider to avoid shadowing the module of the same name (SR-14195).

## 5.8.0

To help migrate your app from the Appboy-iOS-SDK to our Swift SDK, this release includes the Appboy-iOS-SDK migration guide:

- Follow step-by-step instructions to migrate each feature to the new APIs.
 
- Includes instructions for a minimal migration scenario via our compatibility libraries.

##### Added

- Adds compatibility libraries BrazeKitCompat and BrazeUICompat:

- Provides all the old APIs from Appboy-iOS-SDK to easily start migrating to the Swift SDK.
 
- See the migration guide for more details.

- Adds support for News Feed data models and analytics.

- News Feed UI is not supported by the Swift SDK. See the migration guide for instructions on using the compatibility UI.

## 5.7.0

##### Fixed

- Fixes an issue where modal image in-app messages would not respect the aspect ratio of the image when the height of the image is larger than its width.

##### Changed

- Changes modal, modal image, full, and full image in-app message view attributes to use the ViewDimension type for their minWidth, maxWidth and maxHeight attributes.

- The ViewDimension type enables providing different values for regular and large size-classes.

##### Added

- Adds a configuration to use a randomly generated UUID instead of IDFV as the device ID: useUUIDAsDeviceId.

- This configuration defaults to false. To opt in to this feature, set this value to true.
 
- Enabling this value will only affect new devices. Existing devices will use the device identifier that was previously registered.

## 5.6.4

##### Fixed

- Fixes an issue preventing the execution of BrazeDelegate methods when setting the delegate using Objective-C.
 
- Fixes an issue where triggering an in-app message twice with the same event did not place the message on the in-app message stack under certain conditions.

##### Added

- Adds the public id field to Braze.InAppMessage.Data.
 
- Adds logImpression(using:) and logClick(buttonId:using:) to both in-app messages and content cards, and adds logDismissed(using:) to content cards.

- It is recommended to continue using the associated Context to log impressions, clicks, and dismissals for the majority of use cases.

- Adds Swift concurrency to support async/await versions of the following public methods. These methods can be used as alternatives to their corresponding counterparts that use completion handlers:

- Braze.User.id()
 
- Braze.deviceId()
 
- ContentCards.requestRefresh()
 
- ContentCards.cardsStream as an alternative to ContentCards.subscribeToUpdates(_:)

## 5.6.3

##### Fixed

- Fixes the InAppMessageRaw to InAppMessage conversion to properly take into account the extras dictionary and the duration.
 
- Fixes an issue preventing the execution of the braze(_:sdkAuthenticationFailedWithError:) delegate method in case of an authentication error.

##### Changed

- Improves error logging descriptions for HTTP requests and responses.

## 5.6.2

##### Changed

- Corrected the version number from the previous release.

## 5.6.1

##### Added

- Adds the public initializers Braze.ContentCard.Context(card:using:) and Braze.InAppMessage.Context(message:using:).

## 5.6.0

##### Fixed

- The modal webview controller presented after a click now correctly handles non-HTTP(S) URLs (e.g. App Store URLs).
 
- Fixes an issue preventing some test HTML in-app messages from displaying images.

##### Added

- Learn how to easily customize BrazeUI in-app message and content cards UI components with the following documentation and example code:

- In-App Message UI Customization article
 
- Content Cards UI Customization article
 
- InAppMessageUI-Customization example scheme
 
- ContentCardUI-Customization example scheme

- Adds new attributes to BrazeUI in-app message UI components:

- cornerCurve to change the cornerCurve
 
- buttonsAttributes to change the font, spacing and corner radius of the buttons
 
- imageCornerRadius to change the image corner radius for slideups
 
- imageCornerCurve to change the image cornerCurve for slideups
 
- dismissible to change whether slideups can be interactively dismissed

- Adds direct accessors to the in-app message view subclass on the BrazeInAppMessageUI.messageView property.

- slideup, modal, modalImage, full, fullImage, html, control.

- Adds direct accessors to the content card title, description and domain when available.
 
- Adds Braze.Notifications.isInternalNotification to check if a push notification was sent by Braze for an internal feature.
 
- Adds brazeBridge.changeUser() to the HTML in-app messages JavaScript bridge.

##### Changed

- The applyAttributes() method for BrazeContentCardUI views now take the attributes explicitly as a parameter.

## 5.5.1

##### Fixed

- Fixes an issue where content cards would not be properly removed when stopping a content card campaign on the dashboard and selecting the option Remove card after the next sync (e.g. session start).

## 5.5.0

##### Added

- Adds support for host apps written in Objective-C.

- Braze Objective-C types start either with BRZ or Braze, e.g.:

- Braze
 
- BrazeDelegate
 
- BRZContentCardRaw

- See our Objective-C Examples project.

- Adds BrazeDelegate.braze(_:noMatchingTriggerForEvent:) which is called if no Braze in-app message is triggered for a given event.

##### Changed

- In Braze.Configuration.Api:

- Renamed SdkMetadata to SDKMetadata.
 
- Renamed addSdkMetadata(_:) to addSDKMetadata(_:).

- In Braze.InAppMessage:

- Renamed Themes.default to Themes.defaults.
 
- Renamed ClickAction.uri to ClickAction.url.
 
- Renamed ClickAction.uri(_:useWebView:) to ClickAction.url(_:useWebView:).

## 5.4.0

##### Fixed

- Fixes an issue where brazeBridge.logClick(button_id) would incorrectly accept invalid button_id values like "", [], or {}.

##### Added

- Adds support for Braze Action Deeplink Click Actions.

## 5.3.2

##### Fixed

- Fixes an issue preventing compilation when importing BrazeUI via SwiftPM in specific cases.
 
- Lowers BrazeUI minimum deployment target to iOS 10.0.

## 5.3.1

##### Fixed

- Fixes an HTML in-app message issue where clicking a link in an iFrame would launch a separate webview and close the message, instead of redirecting within the iFrame.
 
- Fixes the rounding of In-App Message modal view top corners.
 
- Fixes the display of modals and full screen in-app messages on iPads in landscape mode.

##### Added

- Adds two Example schemes:

- InAppMessage-Custom-UI:

- Demonstrates how to implement your own custom In-App Message UI.
 
- Available on iOS and tvOS.

- ContentCards-Custom-UI:

- Demonstrates how to implement your own custom Content Card UI.
 
- Available on iOS and tvOS.

- Adds Braze.InAppMessage.ClickAction.uri for direct access.
 
- Adds Braze.ContentCard.ClickAction.uri for direct access.
 
- Adds Braze.deviceId(queue:completion:) to retrieve the device identifier used by Braze.

## 5.3.0

##### Added

- Adds support for tvOS.

- See the schemes Analytics-tvOS and Location-tvOS in the Examples project.

## 5.2.0

##### Added

- Adds Content Cards support.

- See the Content Cards UI tutorial to get started.

##### Changed

- Raises BrazeUI minimum deployment target to iOS 11.0 to allow providing SwiftUI compatible Views.

## 5.1.0

##### Fixed

- Fixes an issue where the SDK would be unable to present a webview when the application was already presenting a modal view controller.
 
- Fixes an issue preventing a full device data update after changing the identified user.
 
- Fixes an issue preventing events and user attributes from being flushed automatically under certain conditions.
 
- Fixes an issue delaying updates to push notifications settings.

##### Added

- Adds CocoaPods support.

- Pods:

- BrazeKit
 
- BrazeUI
 
- BrazeLocation
 
- BrazeNotificationService
 
- BrazePushStory

- See Examples/Podfile for example integration.

- Adds Braze.UIUtils.activeTopmostViewController to get the topmost view controller that is currently being presented by the application.

## 5.0.1

##### Fixed

- Fixes a race condition when retrieving the user’s notification settings.
 
- Fixes an issue where duplicate data could be recorded after force quitting the application.

## 5.0.0 (Early Access)

We are excited to announce the initial release of the Braze Swift SDK!

The Braze Swift SDK is set to replace the current Braze iOS SDK and provides a more modern API, simpler integration, and better performance.

### Current limitations

The following features are not supported yet:

- Objective-C integration

- Added in 5.5.0

- tvOS integration

- Added in 5.3.0

- News Feed

- Added in 5.7.0

- Content Cards

- Added in 5.2.0

tip

You can also find a copy of the Cordova Braze SDK changelog on GitHub.

## 17.0.0

##### Breaking

- Updated the native Android bridge from Braze Android SDK 42.2.0 to 43.1.1.
 
- Updated the native iOS bridge from Braze Swift SDK 14.0.1 to 18.2.0.

- Braze.init and changeUser no longer block the calling thread. Refer to the full release notes for Swift SDK 17.0.0 for more details.

- Content Card extras on iOS is now a JavaScript object instead of a JSON-encoded string, matching Android. Integrators that called JSON.parse on extras should use the object directly.

##### Fixed

- Fixed an Android crash when an in-app message arrived while the Cordova WebView was torn down. JavaScript delivery is now skipped instead of throwing a NullPointerException. #109
 
- Fixed Android Gradle builds on cordova-android 14 and 15 failing with an inconsistent Java/Kotlin JVM target. The plugin no longer hardcodes Kotlin jvmTarget to 1.8 and now inherits the host project’s configured Java/Kotlin target.
 
- Fixed Android builds that do not use Firebase Cloud Messaging failing because google-services.json was missing. The Google Services Gradle plugin is now applied only when that file is present.

##### Changed

- Deprecated getContentCardsFromServer. This method will be removed in a future major version.

- Use requestContentCardsRefresh() to request a background refresh, then getContentCardsFromCache() to read the latest cached cards.
 
- The deprecated method now kicks a background refresh and immediately returns the cached cards on both platforms.

- getContentCardsFromCache on Android now returns the current cached cards immediately.
 
- com.braze.ios_use_uuid_as_device_id is now deprecated and will be removed in a future release. Once removed, the SDK will always use a randomly generated UUID as the device ID.

## 16.0.1

##### Fixed

- Fixed iOS initialization when using cordova-ios 8 with the Swift AppDelegate template, where plugins can load after UIApplicationDidFinishLaunchingNotification and Braze would never start.

## 16.0.0

##### Breaking

- Updated the native Android bridge from Braze Android SDK 41.1.1 to 42.2.0.

## 15.0.0

##### Breaking

- Updated the native Android bridge from Braze Android SDK 39.0.0 to 41.1.1.
 
- Updated the native iOS bridge from Braze Swift SDK 13.2.0 to 14.0.1.

##### Fixed

- Fixed subscribeToInAppMessage on both iOS and Android to properly invoke the success callback with in-app message data and correctly respect the useBrazeUI parameter. #103

## 14.0.0

##### Breaking

- Updated the native Android bridge from Braze Android SDK 37.0.0 to 39.0.0.

- The minimum required GradlePluginKotlinVersion is now 2.1.0.

- Updated the native iOS bridge from Braze Swift SDK 12.0.0 to 13.2.0.

- This includes Xcode 26 support.

- Removes support for News Feed. The following APIs have been removed:

- launchNewsFeed
 
- getNewsFeed
 
- getNewsFeedUnreadCount
 
- getNewsFeedCardCount
 
- getCardCountForCategories
 
- getUnreadCardCountForCategories

## 13.0.0

##### Breaking

- Updated the internal iOS implementation of enableSdk method to use setEnabled: instead of _requestEnableSDKOnNextAppRun, which was deprecated in the Swift SDK.

- Calling this method no longer requires the app to be re-launched to take effect. The SDK will now become enabled as soon as this method is executed.

- Updated the native Android bridge from Braze Android SDK 36.0.0 to 37.0.0.

## 12.0.0

[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for < API 25. Read more here.

##### Breaking

- Updated the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
 
- Updated the native iOS bridge from Braze Swift SDK 11.6.1 to 12.0.0.

##### Fixed

- Updated the internal iOS implementation of getUserId to braze.user.identifier instead of [braze.user idWithCompletion:], which was deprecated in Swift SDK 11.5.0. This deprecation does not have any impact to functionality.

##### Added

- Added support for the setSdkAuthenticationSignature method on Android.

## 11.0.0

##### Breaking

- Updated the native Android bridge from Braze Android SDK 32.1.0 to 35.0.0.

- The minimum required Android SDK version is 25. See more details here.

- Updated the native iOS bridge from Braze Swift SDK 10.1.0 to 11.6.1.

##### Fixed

- Updated automatic push integration on iOS to be fully compatible with Swift-based projects (e.g. Capacitor applications).

- Previously, the automatic push integration would not properly register the push token in Swift-based projects.

##### Added

- Added the ability to provide different API keys for Android and iOS in the config.xml file.

- To set the Android API key, add <preference name="com.braze.android_api_key" value="your-android-api-key" />.
 
- To set the iOS API key, add <preference name="com.braze.ios_api_key" value="your-ios-api-key" />.
 
- The preference <preference name="com.braze.api_key" value="your-api-key" /> is still supported for backwards compatibility and is used if no platform-specific API key is provided.

## 10.0.0

##### Breaking

- ⚠️ This version now requires Cordova Android 13.0.0. ⚠️

- Refer to the Cordova release announcement for a full list of project dependency requirements.

- Updated the native Android bridge from Braze Android SDK 30.3.0 to 32.1.0.
 
- Updated the native iOS bridge from Braze Swift SDK 9.2.0 to 10.1.0.

##### Fixed

- Fixed the native-to-JavaScript translation of in-app message strings, where nested escape characters were previously being removed.
 
- Fixed the subscribeToInAppMessage method on iOS to respect the useBrazeUI setting.

- Updated the Android implementation to match iOS by using the DISCARD option instead of DISPLAY_LATER if the default Braze UI is not used.

- Fixed the getContentCardsFromServer method to trigger an error callback on iOS when cards have failed to refresh.

##### Added

- Added the getUserId() method to get the ID of the current user. This method will return null if the current user is anonymous.
 
- Added support for new Feature Flag property types and APIs for accessing them:

- getFeatureFlagTimestampProperty(id, key) for accessing Int Unix UTC millisecond timestamps as numbers.
 
- getFeatureFlagImageProperty(id, key) for accessing image URLs as strings.
 
- getFeatureFlagJSONProperty(id, key) for accessing JSON objects as object types.

- Added setLocationCustomAttribute(key, latitude, longitude) to set a location custom attribute.

## 9.2.0

##### Added

- Updated the native iOS bridge from Braze Swift SDK 9.1.0 to 9.2.0.

## 9.1.0

##### Added

- Added the following properties to the Content Card model:

- isTest
 
- isControl (Note: If you’re implementing your own UI, Control Cards should not be rendered, but you should manually log analytics for them.)

- Updated the native iOS bridge from Braze Swift SDK 9.0.0 to 9.1.0.

## 9.0.0

##### Breaking

- Updated the native iOS bridge from Braze Swift SDK 7.7.0 to 9.0.0.

##### Added

- Added support to modify the allow list for Braze tracking properties via the following JavaScript properties and methods:

- TrackingProperty string enum
 
- TrackingPropertyAllowList object interface
 
- updateTrackingPropertyAllowList method
 
- For details, refer to the Braze iOS Privacy Manifest documentation.

- Added the setAdTrackingEnabled method to set adTrackingEnabled flag on iOS and both the adTrackingEnabled flag and the Google Advertising ID on Android.
 
- Added BrazePlugin.subscribeToInAppMessage() which allows you to listen for new in-app messages from the JavaScript plugin and choose whether or not to use the default Braze UI to display in-app messages.
 
- Added support for logging analytics and functionality for in-app messages.

- BrazePlugin.logInAppMessageImpression(message)
 
- BrazePlugin.logInAppMessageClicked(message)
 
- BrazePlugin.loginAppMessageButtonClicked(message, buttonId)
 
- BrazePlugin.hideCurrentInAppMessage()

- Added support for manually performing the action of an in-app message when using a custom UI.

- BrazePlugin.performInAppMessageAction(message)
 
- BrazePlugin.performInAppMessageButtonAction(message, buttonId)

- Updated the native Android bridge from Braze Android SDK 30.1.1 to 30.3.0.

## 8.1.0

##### Added

- Added new Android feature support that can be added in your config.xml:

- Ability to set the session timeout behavior to be based either on session start or session end events.

- <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />

- Ability to set the user-facing name as seen via NotificationChannel.getName for the Braze default NotificationChannel.

- <preference name="com.braze.default_notification_channel_name" value="name" />

- Ability to set the user-facing description as seen via NotificationChannel.getDescription for the Braze default NotificationChannel.

- <preference name="com.braze.default_notification_channel_description" value="description" />

- Ability to set whether a Push Story is automatically dismissed when clicked.

- <preference name="com.braze.does_push_story_dismiss_on_click" value="true" />

- Ability to set whether the use of a fallback Firebase Cloud Messaging Service is enabled.

- <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true" />

- Ability to set the classpath for the fallback Firebase Cloud Messaging Service.

- <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="your-classpath" />

- Ability to set whether the Content Cards unread visual indication bar is enabled.

- <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true" />

- Ability to set whether the Braze will automatically register tokens in com.google.firebase.messaging.FirebaseMessagingService.onNewToken.

- <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true" />

- Ability to set whether Braze will add an activity to the back stack when automatically following deep links for push.

- <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />

- Ability to set the activity that Braze will add to the back stack when automatically following deep links for push.

- <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="your-class-name" />

- Ability to set if Braze should automatically opt-in the user when push is authorized by Android.

- <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />

- Added new iOS feature support that can be added in your config.xml:

- Ability to set the minimum logging level for Braze.Configuration.Logger.

- <preference name="com.braze.ios_log_level" value="2" />

- Ability to set if a randomly generated UUID should be used as the device ID.

- <preference name="com.braze.ios_use_uuid_as_device_id" value="YES" />

- Ability to set the interval in seconds between automatic data flushes.

- <preference name="com.braze.ios_flush_interval_seconds" value="10" />

- Ability to set whether the request policy for Braze.Configuration.Api should be automatic or manual.

- <preference name="com.braze.ios_use_automatic_request_policy" value="YES" />

- Ability to set if a user’s notification subscription state should automatically be set to optedIn when push permissions are authorized.

- <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />

- Added BrazePlugin.setLastKnownLocation() to set the last known location for the user.
 
- Updated the native iOS bridge from Braze Swift SDK 7.6.0 to 7.7.0.
 
- Updated the native Android bridge from Braze Android SDK 30.0.0 to 30.1.1.

##### Fixed

- Fixed the getDeviceId method to return the value as a success instead of an error on iOS.

## 8.0.0

##### Breaking

- Updated the native Android bridge from Braze Android SDK 27.0.1 to 30.0.0.
 
- Updated the native iOS bridge from Braze Swift SDK 6.6.0 to 7.6.0.
 
- Renamed the Banner Content Card type to ImageOnly:

- ContentCardTypes.BANNER → ContentCardTypes.IMAGE_ONLY
 
- On Android, if the XML files in your project contain the word banner for Content Cards, it should be replaced with image_only.

- BrazePlugin.getFeatureFlag(id) will now return null if the feature flag does not exist.
 
- BrazePlugin.subscribeToFeatureFlagsUpdates(function) will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.
 
- Removed the deprecated method registerAppboyPushMessages. Use setRegisteredPushToken instead.

##### Added

- Added the ability to set a minimum trigger action time interval for Android and iOS.

- To enable this feature, add the line <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" /> in your config.xml.

- Added the ability to configure the app group ID for iOS push extensions.

- To enable this feature, add the line <preference name="com.braze.ios_push_app_group" value="your-app-group" /> in your config.xml.

- Added support for automatically forwarding universal links in iOS.

- To enable this feature, add the line <preference name="com.braze.ios_forward_universal_links" value="YES" /> in your config.xml.

## 7.0.0

##### Breaking

- Updated the native Android version from Braze Android SDK 26.3.2 to 27.0.1.

##### Added

- Added logFeatureFlagImpression(id).
 
- Updated the native iOS version from Braze Swift SDK 6.5.0 to 6.6.0.
 
- Added support for nested custom user attributes.

- The setCustomUserAttribute method now accepts objects and arrays of objects.
 
- Added an optional merge parameter to the setCustomUserAttribute method. This is a non-breaking change.
 
- Please see our public docs for more information.

- Exposed the braze instance as a convenience static property on iOS via BrazePlugin.braze.

- This makes it easier to work with tools such as Capacitor by Ionic.

## 6.0.1

##### Fixed

- Updated the native Android version from Braze Android SDK 26.3.1 to 26.3.2.

## 6.0.0

##### Breaking

- Updated the native iOS version from Braze Swift SDK 5.13.0 to 6.5.0.
 
- Updated the native Android version from Braze Android SDK 25.0.0 to 26.3.1.

##### Added

- Added support for Braze SDK Authentication.

- Enabled on Android via <preference name="com.braze.sdk_authentication_enabled" value="true" />.
 
- Enabled on iOS via <preference name="com.braze.sdk_authentication_enabled" value="YES" />.
 
- Updated changeUser() to accept an optional second parameter for an SDK Auth token, e.g. changeUser("user id here", "jwt token here").
 
- Added subscribeToSdkAuthenticationFailures() which listens for SDK authentication failures.
 
- Added setSdkAuthenticationSignature() to set a Braze SDK Authentication signature JWT token.

## 5.0.0

##### Breaking

- Updated these Feature Flag methods to return promises instead of using a callback parameter

- getAllFeatureFlags()
 
- getFeatureFlag(id)
 
- getFeatureFlagBooleanProperty(id, key)
 
- getFeatureFlagStringProperty(id, key)
 
- getFeatureFlagNumberProperty(id, key)
 
- To get a boolean property, for example, you can now use the following syntax:

```

1

```
 | 
```
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("feature-flag-id", "property-key");

```
 | 

- Changed subscribeToFeatureFlagUpdates to subscribeToFeatureFlagsUpdates.

## 4.0.0

##### Breaking

- Renamed instances of Appboy to Braze.

- To ensure that your project is properly migrated to the new naming conventions, note and replace the following instances in your project:

- The plugin has been renamed from cordova-plugin-appboy to cordova-plugin-braze.

- Ensure that you run cordova plugin remove cordova-plugin-appboy and then re-add the plugin using the instructions in the README.

- This GitHub repository has been moved to the URL https://github.com/braze-inc/braze-cordova-sdk.
 
- In your project’s config.xml file, rename instances of com.appboy to com.braze for each of your configuration property keys.
 
- The JavaScript class interface AppboyPlugin has been renamed to BrazePlugin.

- Updated to Braze Android SDK 25.0.0.
 
- Updated to Braze Swift SDK 5.13.0.

- This update fixes the iOS behavior introduced in version 2.33.0 when logging clicks for content cards. Calling logContentCardClicked now only sends a click event for metrics, instead of both sending a click event as well as redirecting to the associated url field.

- For instance, to log a content card click and redirect to a URL, you will need two commands:
```
BrazePlugin.logContentCardClicked(contentCardId);

// Your own custom implementation
YourApp.openUrl(contentCard[“url”]);
```

- This brings the iOS behavior to match pre-2.33.0 versions and bring parity with Android’s behavior.

##### Added

- Added property methods for Feature Flags: getFeatureFlagBooleanProperty(id, key), getFeatureFlagStringProperty(id, key), getFeatureFlagNumberProperty(id, key)

## 3.0.0

##### Added

- Added support for the upcoming Braze Feature Flags product with getFeatureFlag(), getAllFeatureFlags(), refreshFeatureFlags(), and subscribeToFeatureFlagUpdates().

##### Changed

- Updated to Braze Swift SDK 5.11.0.
 
- Removed automatic requests for App Tracking Transparency permissions on iOS.

## 2.33.0

##### Breaking

- Migrated the iOS plugin to use the new Braze Swift SDK (5.8.1).

- News Feed UI is no longer supported on iOS.
 
- This migration requires re-identifying users. To do so, you must call the changeUser method on the Braze instance for non-anonymous users. You can read more about it here.

## 2.32.0

##### Breaking

- Updated to Braze Android SDK 24.1.0.
 
- Updated the Android bridge to Kotlin.

- <preference name="GradlePluginKotlinEnabled" value="true" /> is now required in your config.xml.

- Removed setAvatarImageUrl().

##### Changed

- Added an main value to package.json.

##### Added

- Added setRegisteredPushToken() which replaces the deprecated registerAppboyPushMessages() method.

## 2.31.0

##### Breaking

- Updated to Braze Android SDK 23.0.1.

##### Added

- Added a method requestPushPermission() for Android API 33 to request push permission prompts from the system on Android 13 devices.

## 2.30.1

##### Added

- Added the ability to set the session timeout for iOS (String) in seconds.

- Add <preference name="com.appboy.com.appboy.ios_session_timeout" value="your_timeout" /> to your config.xml, replacing your_timeout with the desired number of seconds.

##### Fixed

- Fixed a bug where a Content Card without a key-value pair could cause a crash.

## 2.30.0

##### Breaking

- Updated to Braze Android SDK 21.0.0.
 
- Removed “logContentCardsDisplayed” from the javascript plugin.

## 2.29.0

##### Breaking

- Updated to Braze Android SDK 19.0.0.

##### Changed

- Updated to Braze iOS SDK 4.4.2.

## 2.28.0

##### Breaking

- Updated to Braze Android SDK 18.0.1.

##### Fixed

- Fixed an error around locating certain iOS resources when integrating the SDK.

## 2.27.0

##### Breaking

- Updated to Braze Android SDK 17.0.0.
 
- Updated to Braze iOS SDK 4.4.0.

##### Added

- Added addToSubscriptionGroup() and removeFromSubscriptionGroup().

## 2.26.0

##### Breaking

- Updated to Braze Android SDK 16.0.0.

##### Fixed

- Fixed an issue in pre Android P WebViews where the system WebView would not properly handle view focus being returned to it.

- https://issuetracker.google.com/issues/36915710 for more information.
 
- This fix is applied by default and can be disabled via com.braze.android_apply_cordova_webview_focus_request_fix in your config.xml.
 
- When enabled, this fix sets a custom In App Message view vrapper factory with the native Android SDK, potentially overriding any other custom set view factories.

## 2.25.0

##### Breaking

- Updated to Braze Android SDK 15.0.0.

##### Changed

- Updated to Braze iOS SDK 4.3.2.

##### Added

- Added Other, Unknown, Not Applicable, and Prefer not to Say options for user gender.

## 2.24.0

##### Breaking

- Updated to Braze Android SDK 14.0.1.
 
- Updated to Braze iOS SDK 4.3.0.

##### Changed

- (minor) Changed logcat tag for Android plugin to be BrazeCordova.

## 2.23.0

##### Breaking

- Updated to Braze Android SDK 13.1.2.

## 2.22.0

##### Breaking

- Updated to Braze Android SDK 13.0.0.

##### Added

- Added the ability to delay automatic session tracking for Android.

- <preference name="com.appboy.android_disable_auto_session_tracking" value="true" /> in your config.xml.

## 2.21.0

##### Breaking

- Updated to Braze iOS SDK 3.31.1.

##### Fixed

- Fixed an issue on iOS where the plugin was incompatible with other Cordova plugins that have the use_frameworks Cocoapods setting in their Podfile.

##### Added

- Added the ability to disable UNAuthorizationOptionProvisional on iOS. Within config.xml, set com.appboy.ios_disable_un_authorization_option_provisional to YES to disable UNAuthorizationOptionProvisional.

## 2.20.0

##### Added

- Added the method getDeviceId() to the javascript plugin.

## 2.19.0

##### Breaking

- Updated to Braze iOS SDK 3.29.1.
 
- Updated to Braze Android SDK 11.0.0.

##### Fixed

- Fixed an issue where the plugin would automatically add the In-app Purchase capability to XCode projects.

##### Added

- Added the methods addAlias() and setLanguage() to the javascript plugin.

## 2.18.0

##### Breaking

- Updated to Braze Android SDK 10.0.0.

## 2.17.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.27.0. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.

## 2.16.0

##### Changed

- Updated to Braze Android SDK 8.1.0.
 
- Updated to Braze iOS SDK 3.26.1.

##### Added

- Added the ability to display notifications while app is in the foreground in iOS. Within config.xml set com.appboy.display_foreground_push_notifications to "YES" to enable this.

## 2.15.0

##### Changed

- Updated to Braze iOS SDK 3.23.0.
 
- Updated to Braze Android SDK 8.0.1.

## 2.14.0

##### Changed

- Reverted iOS plugin to use framework tag in plugin.xml.
 
- Updated to Braze Android SDK 7.0.0.

## 2.13.0

##### Added

- Added the Content Cards methods requestContentCardsRefresh(), getContentCardsFromServer(), getContentCardsFromCache(), launchContentCards(), logContentCardsDisplayed(), logContentCardClicked(), logContentCardImpression(), logContentCardDismissed() to the javascript plugin.

- getContentCardsFromServer(), getContentCardsFromCache() both take a success and error callback to handle return values.

##### Changed

- Updated to Braze Android SDK 4.0.2.

## 2.12.0

##### Changed

- Updated to Braze Android SDK 3.8.0.
 
- Pinned Android Gradle plugin version to 3.5.1 in build-extras.gradle.

- Addresses https://github.com/braze-inc/braze-cordova-sdk/issues/46.

## 2.11.2

Important: This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the Braze iOS SDK Changelog for more information.

##### Changed

- Updated to Braze iOS SDK 3.20.2.

## 2.11.1

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 2.11.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 2.11.2 or above if you make use of HTML in-app messages.

##### Changed

- Updated to Braze iOS SDK 3.20.1.

## 2.11.0

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 2.11.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 2.11.2 or above if you make use of HTML in-app messages.

##### Breaking

- Updated to Braze iOS SDK 3.20.0.
 
- Important: Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to this version as soon as possible to ensure a smooth transition as devices upgrade to iOS 13.
 
- Removes the Feedback feature.

- submitFeedback() and launchFeedback() have been removed from the AppboyPlugin interface.

- Updated to Braze Android SDK 3.7.0.

##### Added

- Added ability to configure location collection in preferences. Braze location collection is now disabled by default.

- Set com.appboy.enable_location_collection to true/false on Android.
 
- Set com.appboy.enable_location_collection to YES/NO on iOS.

- Added ability to configure geofences in preferences. Note that the geofences branch is still required to use Braze Geofences out of the box.

- Set com.appboy.geofences_enabled to true/false on Android.
 
- Set com.appboy.geofences_enabled to YES/NO on iOS.

## 2.10.1

##### Fixed

- Fixed an issue in the iOS plugin where custom endpoints were not correctly getting substituted for the actual server endpoints.

## 2.10.0

##### Breaking

- Updated to Braze iOS SDK 3.14.1.

##### Added

- Added ability for plugin to automatically collect the IDFA information on iOS. To enable, set com.appboy.ios_enable_idfa_automatic_collection to YES in your config.xml project file.

- 

```

1
2
3

```
 | 
```
<platform name="ios">
 <preference name="com.appboy.ios_enable_idfa_automatic_collection" value="YES" />
</platform>

```
 | 

##### Fixed

- Fixed an issue in the Android plugin where the Braze SDK could be invoked before pluginInitialize was called by Cordova. The plugin now explicitly initializes the SDK before any SDK or Android lifecycle methods are called.

- Fixes https://github.com/braze-inc/braze-cordova-sdk/issues/38

## 2.9.0

##### Breaking

- Updated to Braze iOS SDK 3.14.0.
 
- Updated to Braze Android SDK 3.2.2.

##### Changed

- Changed the iOS plugin to use Cocoapods instead of a framework integration.
 
- Improved the look and feel of in-app messages to adhere to the latest UX and UI best practices. Changes affect font sizes, padding, and responsiveness across all message types. Now supports button border styling.

##### Fixed

- Fixed the Android plugin not respecting decimal purchase prices.

- Fixes https://github.com/braze-inc/braze-cordova-sdk/issues/36.

## 2.8.0

- Changed the iOS frameworks to be automatically embedded in the plugin.xml.

- This fixes the “dyld: Library not loaded” issue raised in XCode if the frameworks were not manually embedded.

- Adds method to immediately flush any pending data via requestImmediateDataFlush().

## 2.7.1

- Fixes an issue where sending push on Android resulted in a crash in version 2.7.0. Past versions (before 2.7.0) are unaffected.

## 2.7.0

- Updates Braze Android version to 3.0.0+

- Removes GCM push registration methods. In your config.xml com.appboy.android_automatic_push_registration_enabled and com.appboy.android_gcm_sender_id , now have no effect on push registration.

- Updates Braze iOS version to 3.9.0.

## 2.6.0

- Fixes an issue where the Cordova 8.0.0+ build system would convert numeric preferences in the config.xml to be floating point numbers.

- Numeric preferences, such as sender ids, now should be prefixed with str_ for correct parsing. I.e. <preference name="com.appboy.android_fcm_sender_id" value="str_64422926741" />.

- Updates Braze Android version to 2.6.0+

## 2.5.1

- Updates Braze Android version to 2.4.0+.
 
- Adds Firebase Cloud Messaging automatic registration support. GCM automatic registration should be disabled by setting the config value “com.appboy.android_automatic_push_registration_enabled” to “false”. See the Android sample-project’s config.xml for an example. FCM config.xml keys below.

- “com.appboy.firebase_cloud_messaging_registration_enabled” (“true”/”false”)
 
- “com.appboy.android_fcm_sender_id” (String)
 
- The Firebase dependencies firebase-messaging and firebase-core are now included automatically as part of the plugin.

## 2.5.0

- Updates Braze Android version to 2.2.5+.
 
- Updates Braze iOS version to 3.3.4.
 
- Adds wipeData(), enableSdk(), and disableSdk() methods to the plugin.

## 2.4.0

- Fixes a subdirectory incompatibility issue with Cordova 7.1.0

## 2.3.2

- Adds configuration for custom API endpoints on iOS and Android using the config.xml.

- Android preference: “com.appboy.android_api_endpoint”
 
- iOS preference: “com.appboy.ios_api_endpoint”

## 2.3.1

- Adds getter for all News Feed cards. Thanks to @cwelk for contributing.
 
- Adds a git branch geofence-branch for registering geofences with Google Play Services and messaging on geofence events. Please reach out to [email protected] for more information about this feature. The branch has geofences integrated for both Android and iOS.

## 2.3.0

- Fixes in-app messages display issue on iOS.
 
- Updates Appboy iOS version to 2.29.0
 
- Updates Appboy Android version to 2.0+
 
- Fixes original in-app messages not being requested on Android.

## 2.2.0

- Updates Appboy Android version to 1.18+
 
- Updates Appboy iOS version to 2.25.0
 
- Adds the ability to configure the Android Cordova SDK using the config.xml. See the Android sample-project’s config.xml for an example.

- Supported keys below, see the AppboyConfig.Builder javadoc for more details
 
- “com.appboy.api_key” (String)
 
- “com.appboy.android_automatic_push_registration_enabled” (“true”/”false”)
 
- “com.appboy.android_gcm_sender_id” (String)
 
- “com.appboy.android_small_notification_icon” (String)
 
- “com.appboy.android_large_notification_icon” (String)
 
- “com.appboy.android_notification_accent_color” (Integer)
 
- “com.appboy.android_default_session_timeout” (String)
 
- “com.appboy.android_handle_push_deep_links_automatically” (“true”/”false”)
 
- “com.appboy.android_log_level” (Integer) can also be configured here, for obtaining debug logs from the Appboy Android SDK

- Updates the Android Cordova SDK to use the Appboy Lifecycle listener to handle session and in-app message registration

## 2.1.0

- Adds support for iOS 10 push registration and handling using the UNUserNotificationCenter.
 
- Adds functionality for turning off automatic push registration on iOS. To disable, add the preference com.appboy.ios_disable_automatic_push_handling with a value of YES.

## 2.0.0

- Updates to add functionality for turning off automatic push registration on iOS. If you want to turn off iOS default push registration, add the preference com.appboy.ios_disable_automatic_push_registration with a value of YES.
 
- Includes patch for iOS 10 push open bug. See https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#2240 for more information.
 
- Updates Appboy iOS version to 2.24.2.
 
- Updates Appboy Android version to 1.15+.
 
- Updates plugin to configure Android via parameters to eliminate need for post-install modifications on Android. Ported from https://github.com/Appboy/appboy-cordova-sdk/tree/feature/android-variable-integration.

## 0.1

- Initial release. Adds support for Appboy Android version 1.12+ and Appboy iOS version 2.18.1.

tip

You can also find a copy of the Flutter Braze SDK changelog on GitHub.

## 22.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 42.3.1 to 43.0.0.
 
- Updates the native iOS bridge from Braze Swift SDK 17.0.0 to 18.0.0.

## 21.0.0

##### Breaking

- Updates the native iOS bridge from Braze Swift SDK 16.0.0 to 17.0.0.

- With this update, the native Braze.init and changeUser(userId:) no longer block the calling thread. Refer to the full release notes for Swift SDK 17.0.0 for more details.

- Removes the following deprecated methods:

- logCustomEventWithProperties(). Use logCustomEvent() instead.
 
- logPurchaseWithProperties(). Use logPurchase() instead.
 
- registerAndroidPushToken(). Use registerPushToken() instead.
 
- getInstallTrackingId(). Use getDeviceId() instead.
 
- setGoogleAdvertisingId(). Use setAdTrackingEnabled() instead.

##### Fixed

- Fixes an iOS race where a Braze method called immediately after initialize() was silently dropped because the native Braze instance had not been created yet. The instance is now created synchronously so calls made right after initialize() are applied to a valid instance.
 
- The native changeUser, enableSDK, and disableSDK handlers now return a completion result on both iOS and Android, so awaiting these method channel calls no longer hangs.

## 20.0.0

##### Breaking

- Updates the native iOS bridge from Braze Swift SDK 14.1.0 to 16.0.0.

- With this update, the underlying Content Cards list behind getCachedContentCards (including removed, viewed, and clicked states) is updated immediately when changes occur. This now matches the iOS behavior with Android.

##### Added

- Updates the native Android bridge from Braze Android SDK 42.2.0 to 42.3.1.

- Fixed an issue where HTML In-App Messages displayed during an Activity transition could remain visible but not dismissable after carryover.

- Adds support for banner dismissals.

- Adds stableKey field to the BrazeBanner model.
 
- Adds onDismiss callback to BrazeBannerView, invoked when the banner for that placement is dismissed.
 
- Adds BrazePlugin.dismissBanner(placementId) to programmatically dismiss the banner for a given placement.

## 19.0.0

##### Breaking

- The minimum supported Dart version is 2.17.0.
 
- SDK logging is now controlled on the Dart layer.
 
- Updates the native Android bridge from Braze Android SDK 41.1.1 to 42.2.0.

##### Fixed

- Fixes a crash on Android where setBrazePluginIsReady could throw a NullPointerException when replaying pending push events containing null entries.

- See #129.

##### Added

- Flutter-specific and native platform logs now print to the DevTools logging view.

- Logs use dart:developer’s log() function under the name BrazeFlutterSDK, making them visible in the Flutter DevTools Logging tab.
 
- Adds BrazeLogLevel with three levels:

- BrazeLogLevel.debug
 
- BrazeLogLevel.info
 
- BrazeLogLevel.error

- Adds BrazePlugin.logLevel to filter out logs below a given level.

- Accepts a BrazeLogLevel or a raw dart:developer integer.
 
- Defaults to BrazeLogLevel.info, which suppresses debug logs.

- Adds BrazePlugin.logger, an optional callback.

- When set, it replaces the default dart:developer output so you can route logs to your own logging infrastructure.

- On Android:

- The plugin now configures the native BrazeLogger when the Flutter engine attaches.
 
- Any log level or log callback set in your Application.onCreate will be overwritten.
 
- Use BrazePlugin.logLevel from Dart to control the log level instead.

- On iOS:

- If your AppDelegate already sets a custom configuration.logger.print closure, the plugin will not forward native logs to Dart and BrazePlugin.logLevel will only filter Dart-side logs.
 
- Otherwise, any log level set in configuration.logger.level will be overriden.
 
- BrazePlugin.logLevel will only take effect after BrazePlugin.initialize(apiKey, endpoint) is called and a new Braze instance is created.

- Updates the native iOS bridge from Braze Swift SDK 14.0.4 to 14.1.0.

## 18.0.1

##### Fixed

- Braze.registerPushToken() now explicitly enforces that the device token is a hex-encoded string for the iOS implementation.

- This addresses previously reported issues of tokens being improperly converted.

## 18.0.0

##### Breaking

- Streamlines the iOS integration process to not require writing native code to forward content cards, banners, feature flags, in-app messages, or push notification updates from the native SDK.

- The SDK will now automatically set up these subscriptions when the Braze instance is created.
 
- This matches the existing behavior on Android.
 
- To migrate, remove any manual calls to braze.contentCards.subscribeToUpdates(), braze.banners.subscribeToUpdates(), braze.notifications.subscribeToUpdates, braze.featureFlags.subscribeToUpdates and braze.inAppMessagePresenter in the AppDelegate.
 
- By default, in-app messages will be presented. To override this, set a custom in-app message presenter using the postInitialization closure in BrazePlugin.configure(_:postInitialization:).

##### Added

- Adds support for delayed SDK initialization. See full setup guide here.

- Adds initialize(apiKey, endpoint) method to create the Braze instance at runtime with the stored configuration. This method can be called multiple times to re-initialize the SDK with a different API key and endpoint mid-session.
 
- To enable delayed initialization on Android, add com_braze_enable_delayed_initialization set to true in your braze.xml.

- For iOS integrations only, adds BrazePlugin.configure(_:postInitialization:) to store configurations in your AppDelegate for later use by the new Dart initialize(apiKey, endpoint) method.

- BrazePlugin.initBraze() is deprecated. Use the configure + Dart initialize pattern instead.

##### Fixed

- Updates the native iOS bridge from Braze Swift SDK 14.0.1 to 14.0.4.

## 17.1.0

##### Added

- Adds support to import the Flutter iOS package via Swift Package Manager (SPM).

- The Braze Flutter SDK still supports CocoaPods integrations at this time.
 
- For instructions on how to migrate from CocoaPods to SPM, reference Flutter’s official docs.
 
- The minimum Flutter version of the Braze SDK remains unchanged, but integration with SPM requires Flutter version 3.24.0 or higher.

- The Flutter iOS sample app has been updated to use SPM to import the Braze SDK.

- This also removes all relevant files to the CocoaPods integration for the sample app.

- Updates the native Android bridge from Braze Android SDK 41.0.0 to 41.1.1.

## 17.0.0

##### Breaking

- Updates the native iOS bridge from Braze Swift SDK 13.3.0 to 14.0.1.
 
- Updates the native Android bridge from Braze Android SDK 40.0.0 to 41.0.0.

##### Added

- Adds support for logging banner analytics to Braze using BrazeBanner instances.

- See logBannerClicked(placementId:buttonId:) and logBannerImpression(placementId:) on the BrazePlugin interface.

## 16.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 39.0.0 to 40.0.0.

##### Fixed

- Banner views will no longer call setState extraneously if the view component is not mounted.

- Previously, this could cause an exception to occur if the Banner tried to update its height while the view was not mounted within the widget hierarchy.

- Fixes UI flickering and display issues with BrazeBannerView when navigating between screens on Android

##### Added

- Updates the native iOS bridge from Braze Swift SDK 13.2.0 to 13.3.0.

## 15.1.0

##### Added

- Adds support for Banner properties via new public methods for BrazeBanner.

- banner.getStringProperty(key:) for accessing String properties.
 
- banner.getNumberProperty(key:) for accessing num properties.
 
- banner.getTimestampProperty(key:) for accessing int Unix UTC millisecond timestamp properties.
 
- banner.getBooleanProperty(key:) for accessing bool properties.
 
- banner.getImageProperty(key:) for accessing image URL properties as Strings.
 
- banner.getJSONProperty(key:) for accessing JSON properties as Map<String, dynamic>.

## 15.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 36.0.0 to 39.0.0.
 
- Updates the native iOS bridge from Braze Swift SDK 12.0.0 to 13.2.0.

- This includes Xcode 26 support.

##### Added

- Adds the ability to unset the following user attributes by setting these values to null:

- First name
 
- Last name
 
- Phone number
 
- Email
 
- Gender
 
- Language
 
- Home city
 
- Country

## 14.0.3

##### Fixed

- Fixes missing Braze symbol error in BrazeBannerViewFactory when using dynamically-linked frameworks.

## 14.0.2

[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for < API 25. Read more here.

##### Fixed

- Fixes a display issue introduced in 14.0.1 when changing a Banner dynamically.
 
- The minSdk enforced by the Flutter Android layer is now downgraded from 25 to 21, matching the minSdk in the Android native layer.

## 14.0.1

##### Fixed

- Fixes a crash on iOS when the app is force-closed while a Banner is visible on the screen.

- Note: This fix may cause display issues when trying to change Banners dynamically. This will be addressed in a future patch.

## 14.0.0

⚠️ Important: This version has a known issue related to Banners. Upgrade to version 14.0.2 instead.

##### Breaking

- Updates the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
 
- Updates the native iOS bridge from Braze Swift SDK 11.9.0 to 12.0.0.

##### Fixed

- Fixes an issue on iOS where getUserId() would not return any value if the user was anonymous.

- This API will now return null if the user is anonymous.

- Fixes the iOS implementation of setDateOfBirth to correctly report dates using the Gregorian calendar instead of the user’s device calendar.

- Previously, the SDK would re-format the input date components with the device’s calendar settings if they were non-Gregorian.

- Fixes the in-app message data model to reflect the correct types under the following circumstances:

- HTML in-app messages will now reflect their correct type html, instead of the default slideup type.
 
- Full in-app messages will now reflect their correct type full, instead of incorrectly being marked as html_full. HTML full messages will still continue to work as expected.

## 13.0.0

⚠️ Important: This version has a known issue related to Banners. Upgrade to version 14.0.2 instead.

##### Breaking

- Updates the native Android bridge from Braze Android SDK 33.0.0 to 35.0.0.

- The minimum required Android SDK version is 25. See more details here.

##### Added

- Adds the BrazeBannerView widget to display a Banner Card directly in Dart.

- To use this feature, insert the widget BrazeBannerView(placementId:) into your Dart view hierarchy with the relevant placementId.
 
- Reference our integration in our sample app.

- Adds support for the Braze Banner Cards product and APIs to utilize them.

- BrazePlugin.requestBannersRefresh(List<String> placementIds) - to request a refresh of the banners associated with the provided placement IDs. This must be called at least once to set the list of banners to retrieve. On iOS only, failures will be logged if unsuccessful.
 
- BrazePlugin.getBanner(String placementId) - to get a banner with the provided placement ID if available in cache, otherwise returns null.
 
- BrazePlugin.subscribeToBanners(void Function(List<BrazeBanner>) onEvent) - to subscribe to the stream of banners and call [onEvent] when it receives the list of banners.

- Updates the native iOS bridge from Braze Swift SDK 11.6.1 to 11.9.0.

## 12.1.1

##### Added

- Updates the native iOS bridge from Braze Swift SDK 11.6.0 to 11.6.1.

## 12.1.0

##### Added

- Updates the native iOS bridge from Braze Swift SDK 11.3.0 to 11.6.0.

## 12.0.0

##### Breaking

- Updates the native iOS bridge from Braze Swift SDK 10.3.1 to 11.3.0.
 
- Updates the native Android bridge from Braze Android SDK 32.1.0 to 33.1.0.

## 11.1.0

##### Added

- Updates the native iOS bridge from Braze Swift SDK 10.2.0 to 10.3.1.

## 11.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 30.4.0 to 32.1.0.

- Changes the behavior of wipeData() on Android to retain external subscriptions (like subscribeToContentCards()) after being called.

- Updates the native iOS bridge from Braze Swift SDK 9.0.0 to 10.2.0.

##### Added

- Adds support for 3 new Feature Flag property types:

- featureFlag.getTimestampProperty(String key) for accessing Int Unix UTC millisecond timestamps as int?s.
 
- featureFlag.getJSONProperty(String key) for accessing JSON objects as Map<String, dynamic>? types.
 
- featureFlag.getImageProperty(String key) for accessing image URLs as String?s.

- Adds the getUserId() method to get the ID of the current user. This method will return null if the current user is anonymous.
 
- Adds the hideCurrentInAppMessage() method, which dismisses the currently displayed in-app message.

##### Fixed

- Fixes an issue on Android where push notification stream subscriptions were not receiving events after clicking on a push notification when the app was in a terminated state.

- Thank you @Neelansh-ns for the contribution!

## 10.1.0

##### Added

- Updated the Android Gradle plugin from 8.0.2 to 8.1.1.
 
- Updated the native Android bridge from Braze Android SDK 30.3.0 to 30.4.0.
 
- Adds the BrazeInAppMessage.isTestSend property, which indicates whether an in-app message was triggered as part of a test send.

## 10.0.0

##### Breaking

- Updates the native iOS bridge from Braze Swift SDK 8.4.0 to 9.0.0.

##### Added

- Adds the getDeviceId method to replace getInstallTrackingId, which is now deprecated.

##### Fixed

- Fixes an issue where StrictMode DiskReadViolation was triggered on Android.

- Thanks @radivojeostojic for pointing this out.

## 9.0.0

##### Breaking

- Updates the native iOS bridge from Braze Swift SDK 7.7.0 to 8.4.0.

- The minimum iOS deployment target has been updated to 12.0.
 
- The minimum supported Xcode version is 15.2.

- Updates the native Android bridge from Braze Android SDK 29.0.1 to 30.3.0.
 
- The minimum supported Dart version is 2.15.0.
 
- The minimum supported Swift Language Version is Swift 5.

##### Added

- Push notification payloads are now accessible in the Dart layer by calling subscribeToPushNotificationEvents(void Function(BrazePushEvent) onEvent). This allows you to run custom Dart code after a push is received or when a push is clicked.

- On iOS, this callback can only be triggered for push click events.
 
- Reference our Flutter Push Notification documentation with details on how to utilize this feature.
 
- This feature is compatible with the replayCallbacksConfigKey to replay the push event callback for any notifications that were received prior to calling subscribeToPushNotificationEvents.
 
- Due to an issue in the Flutter framework, this feature is not compatible with subscribing to iOS silent push notifications.

- Adds support for Braze tracking properties.

- Adds the updateTrackingPropertyAllowList(allowList) method to dynamically configure Braze tracking properties.
 
- For further usage details, refer to the Swift privacy manifest documentation.

- Deprecates setGoogleAdvertisingId(id, adTrackingEnabled) in favor of setAdTrackingEnabled(adTrackingEnabled, id).

## 8.2.0

##### Added

- Updates the native iOS bridge from Braze Swift SDK 7.3.0 to 7.7.0.
 
- Adds example integrations for Braze Rich Push Notifications and Braze Push Stories to the iOS sample app.

##### Fixed

- Removes the automatic assignment of BrazeDelegate in the iOS native layer, allowing for custom implementations to be assigned to the braze instance.

- The plugin now uses the sdkAuthDelegate property for the SDK Authentication feature instead.

## 8.1.0

##### Added

- Updates the native iOS bridge from Braze Swift SDK 7.2.0 to 7.3.0.

## 8.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 27.0.1 to 29.0.1.
 
- Updates the native iOS bridge from Braze Swift SDK 6.6.1 to 7.2.0.
 
- Modifies the behavior for Feature Flags methods.

- BrazePlugin.getFeatureFlagByID(String id) will now return null if the feature flag does not exist.
 
- BrazePlugin.subscribeToFeatureFlags(void Function(List<BrazeFeatureFlag>) onEvent)) will only trigger in the following situations:

- When a refresh request completes with success or failure.
 
- Upon initial subscription if there was previously cached data from the current session.

- The minimum supported Android SDK version is 21.

##### Fixed

- Moved the compileSDKVersion for Android down to 33 to match Flutter’s versioning.

## 7.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 26.1.1 to 27.0.1.
 
- Adds support for Gradle 8.

##### Added

- Updates the native iOS bridge from Braze Swift SDK 6.3.0 to 6.6.1.
 
- Adds BrazePlugin.logFeatureFlagImpression(String id) to log a Feature Flag impression.
 
- Adds support for custom user attributes to be nested objects.

- BrazeUser.setNestedCustomUserAttribute()
 
- BrazeUser.setCustomUserAttributeArrayOfObjects()
 
- You can specify that the Dictionary be merged with the existing value.

- BrazeUser.setNestedCustomUserAttribute(string, Map<string, dynamic>, true)

- See https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/ for more information.

- Adds BrazeUser.setCustomUserAttributeArrayOfStrings() to set arrays of strings as a custom attribute.
 
- Adds BrazePlugin.getCachedContentCards() to get the most recent content cards from the cache.
 
- Adds BrazePlugin.registerPushToken() to send a push token to Braze’s servers.

- Deprecates BrazePlugin.registerAndroidPushToken() in favor of this new method.

- Adds an example integration of iOS push notifications as well as custom scheme deep links, universal links (iOS), and app links (Android) to the Flutter sample app.

## 6.0.1

##### Fixed

- Updates the native Android bridge from Braze Android SDK 26.1.0 to 26.1.1.

## 6.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 25.0.0 to 26.1.0.

##### Fixed

- Fixes an issue where BrazeContentCard.imageAspectRatio would always return 1 for whole-number int values.

- The field imageAspectRatio is now a num type instead of a double type. No changes are required.

##### Added

- Added support for Braze Feature Flags.

- BrazePlugin.getFeatureFlagByID(String id) - Get a single Feature Flag
 
- BrazePlugin.getAllFeatureFlags() - Get all Feature Flags
 
- BrazePlugin.refreshFeatureFlags() - Request a refresh of Feature Flags
 
- BrazePlugin.subscribeToFeatureFlags(void Function(List<BrazeFeatureFlag>) onEvent)) - Subscribe to Feature Flag updates
 
- Feature Flag property getter methods for the following types:

- Boolean: featureFlag.getBooleanProperty(String key)
 
- Number: featureFlag.getNumberProperty(String key)
 
- String: featureFlag.getStringProperty(String key)

- Updates the native iOS bridge from Braze iOS SDK 6.0.0 to 6.3.0.

## 5.0.0

##### Breaking

- The native Android bridge uses Braze Android SDK 25.0.0.
 
- The native iOS bridge uses Braze iOS SDK 6.0.0.

- If you wish to access remote URLs for in-app messages instead of local URLs, replace your implementation of the BrazeInAppMessageUIDelegate method inAppMessage(_:willPresent:view:) with a custom implementation of BrazeInAppMessagePresenter or a BrazeInAppMessageUI subclass. This is relevant if you are caching asset URLs outside of the Braze SDK.
 
- For reference, see our sample code here.

## 4.1.0

##### Fixed

- Fixes an issue in 4.0.0 where the version in braze_plugin.podspec was not incremented correctly.

##### Changed

- The native iOS bridge uses Braze iOS SDK 5.12.0.

## 4.0.0

Starting with this release, this SDK will use Semantic Versioning.

##### Breaking

- Fixes the behavior in the iOS bridge introduced in version 3.0.0 when logging clicks for in-app messages and content cards. Calling logClick now only sends a click event for metrics, instead of both sending a click event as well as redirecting to the associated url field.

- For instance, to log a content card click and redirect to a URL, you will need two commands:
```
braze.logContentCardClicked(contentCard);

// Your own custom implementation
Linking.openUrl(contentCard.url);
```

- This brings the iOS behavior to match version 2.x and bring parity with Android’s behavior.

- Removes setBrazeInAppMessageCallback() and setBrazeContentCardsCallback() in favor of subscribing via streams.

- Reference our sample app for an example on how to use subscribeToInAppMessages() or subscribeToContentCards().

##### Changed

- The native Android bridge uses Braze Android SDK 24.3.0.
 
- The native iOS bridge uses Braze iOS SDK 5.11.2.
 
- Improves behavior when using replayCallbacksConfigKey alongside having subscriptions to in-app messages or content cards via streams.

## 3.1.0

##### Breaking

- The native Android bridge uses Braze Android SDK 24.2.0.
 
- The native iOS bridge uses Braze iOS SDK 5.9.0.
 
- The minimum iOS deployment target is 11.0.

## 3.0.1

##### Fixed

- Updates the braze_plugin.podspec file to statically link the iOS framework by default. This prevents the need to do a manual step when migrating to 3.x.x.
 
- Fixes an issue introduced in version 2.2.0 where the content cards callback was not being called when receiving an empty list of content cards.

## 3.0.0

##### Breaking

- The native iOS bridge now uses the new Braze Swift SDK, version 5.6.4.

- The minimum iOS deployment target is 10.0.

- During migration, update your project with the following changes:

- To initialize Braze, follow these integration steps to create a configuration object. Then, add this code to complete the setup:

```

1

```
 | 
```
let braze = BrazePlugin.initBraze(configuration)

```
 | 

- This migration requires re-identifying users. To do so, you must call the changeUser method on the Braze instance for non-anonymous users. You can read more about it here.
 
- To continue using SDWebImage as a dependency, add this line to your project’s /ios/Podfile:

```

1

```
 | 
```
pod 'SDWebImage', :modular_headers => true

```
 | 

- Then, follow these setup instructions.

- For guidance around other changes such as receiving in-app message and content card data, reference our sample AppDelegate.swift.

##### Added

- Adds the isControl field to BrazeContentCard.

##### Changed

- Updates the parameter syntax for subscribeToInAppMessages() and subscribeToContentCards().

## 2.6.1

##### Added

- Adds support to replay the onEvent method for queued in-app messages and content cards when subscribing via streams.

- This feature must be enabled by setting replayCallbacksConfigKey: true in customConfigs for the BrazePlugin.

##### Changed

- The native Android bridge uses Braze Android SDK 23.3.0.
 
- Updates the parameter type for subscribeToInAppMessages() and subscribeToContentCards() to accept a Function instead of a void.

## 2.6.0

##### Breaking

- The native Android bridge uses Braze Android SDK 23.2.0.
 
- The native iOS bridge uses Braze iOS SDK 4.5.1.
 
- process(inAppMessage) is renamed to processInAppMessage(inAppMessage) in the iOS layer.

##### Added

- Adds the ability to subscribe to data for in-app messages and content cards via streams.

- Use the methods subscribeToInAppMessages() and subscribeToContentCards(), respectively.

##### Changed

- Updates the iOS layer to use Swift. BrazePlugin.h and BrazePlugin.m are now consolidated to BrazePlugin.swift.
 
- Deprecates setBrazeInAppMessageCallback() and setBrazeContentCardsCallback() in favor of subscribing via streams.

## 2.5.0

##### Breaking

- The native Android bridge uses Braze Android SDK 21.0.0.
 
- Removes logContentCardsDisplayed(). This method was not part of the recommended Content Cards integration and can be safely removed.

##### Added

- Adds support for the SDK Authentication feature.

- To handle authentication errors, use setBrazeSdkAuthenticationErrorCallback(), and use setSdkAuthenticationSignature() to update the signature. When calling changeUser(), be sure to pass in the sdkAuthSignature parameter.
 
- Thanks @spaluchiewicz for contributing to this feature!

- Adds setLastKnownLocation() to set the last known location for the user.

## 2.4.0

##### Breaking

- The native Android bridge uses Braze Android SDK 20.0.0.
 
- Removes setAvatarImageUrl().

##### Changed

- The native iOS bridge uses Braze iOS SDK 4.4.3.

## 2.3.0

##### Breaking

- The native Android bridge uses Braze Android SDK 17.0.0.
 
- The minimum supported Android SDK version is 19.
 
- Removes support for Android V1 Embedding APIs. Please reference the Flutter migration guide to update to the V2 APIs.

##### Added

- Custom events and purchases now support nested properties.

- In addition to integers, floats, booleans, dates, or strings, a JSON object can be provided containing dictionaries of arrays or nested dictionaries. All properties combined can be up to 50 KB in total length.

- Adds the ability to restrict the Android automatic integration from natively displaying in-app messages.

- To enable this feature, add this to your braze.xml configuration:
```
 
 DISCARD
 
```

- The available options are DISPLAY_NOW or DISCARD. If this entry is ommitted, the default is DISPLAY_NOW.

##### Changed

- The native iOS bridge uses Braze iOS SDK 4.4.1.

## 2.2.0

##### Breaking

- The native Android bridge uses Braze Android SDK 16.0.0.
 
- The native iOS bridge uses Braze iOS SDK 4.4.0.
 
- Streamlines the Android integration process to not involve any manual writing of code to automatically register for sessions, in-app messages, or Content Card updates from the native SDK.

- To migrate, remove any manual calls to registerActivityLifecycleCallbacks(), subscribeToContentCardsUpdates(), and setCustomInAppMessageManagerListener().
 
- To disable this feature, set the boolean com_braze_flutter_enable_automatic_integration_initializer to false in your braze.xml configuration.

##### Added

- Adds the ability to set the in-app message callback and content cards callback in the constructor of BrazePlugin.
 
- Adds the option to store any in-app messages or content cards received before their callback is available and replay them once the corresponding callback is set.

- To enable this feature, add this entry into the customConfigs map in the BrazePlugin constructor:

```

1

```
 | 
```
replayCallbacksConfigKey : true

```
 | 

- Thank you @JordyLangen for the contribution!

- Adds BrazePlugin.addToSubscriptionGroup() and BrazePlugin.removeFromSubscriptionGroup() to manage SMS/Email Subscription Groups.

##### Fixed

- Fixes an issue in the iOS bridge where custom events without any properties would not be logged correctly.

## 2.1.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 4.3.2.
 
- The native Android bridge uses Braze Android SDK 15.0.0.

##### Added

- Adds logContentCardsDisplayed() to manually log an impression when displaying Content Cards in a custom UI.

## 2.0.0

##### Breaking

- Migrates the plugin to support null safety. All non-optional function parameters have been updated to be non-nullable unless otherwise specified. Read here for more information about null safety.

- Please reference the Dart documentation when migrating your app to null safety.
 
- Apps that have not yet migrated to null safety are compatible with this version as long as they are using Dart 2.12+.
 
- Thanks @IchordeDionysos for contributing!

- Passing through null as a value for user attributes is no longer supported.

- The only attribute that is able to be unset is email by passing in null into setEmail.

- The methods logEvent and logPurchase now take an optional properties parameter.
 
- The native Android bridge uses Braze Android SDK 14.0.0.
 
- The minimum supported Dart version is 2.12.0.

##### Changed

- logEventWithProperties and logPurchaseWithProperties are now deprecated in favor of logEvent and logPurchase.

## 1.5.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 4.0.2.
 
- The native Android bridge uses Braze Android SDK 13.1.2.
 
- The minimum supported Flutter version is 1.10.0.

##### Added

- Adds a public repository for the Braze Flutter SDK here: https://github.com/braze-inc/braze-flutter-sdk.

- We look forward to the community’s feedback and are excited for any contributions!

## 1.4.0

##### Breaking

- The native Android bridge uses Braze Android SDK 13.0.0.
 
- The native iOS bridge uses Braze iOS SDK 3.34.0.

##### Added

- Adds BrazePlugin.setGoogleAdvertisingId() to set the Google Advertising ID and the associated Ad-Tracking Enabled field for Android. This is a no-op on iOS.

##### Fixed

- Fixes an issue where the Braze Android SDK’s Appboy.setLogLevel() method wasn’t respected.

## 1.3.0

##### Breaking

- The native Android bridge uses Braze Android SDK 12.0.0.
 
- The native iOS bridge uses Braze iOS SDK 3.31.0.

##### Added

- Adds support for the Braze plugin to be used with Android V2 Embedding APIs. Integrations using V1 Embedding will also continue to work.
 
- Allows the Android Braze plugin to be used with multiple Flutter engines.

## 1.2.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.30.0.

##### Added

- Allows the iOS Braze plugin to be used with multiple Flutter engines.

## 1.1.0

##### Breaking

- The native Android bridge uses Braze Android SDK 11.0.0.
 
- The native iOS bridge uses Braze iOS SDK 3.29.1.

## 1.0.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.27.0. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.

## 0.10.1

##### Changed

- The native iOS bridge uses Braze iOS SDK 3.26.1.

## 0.10.0

##### Breaking

- The native Android bridge uses Braze Android SDK 8.1.0.
 
- The native iOS bridge uses Braze iOS SDK 3.26.0.

##### Fixed

- Fixed an issue where setBoolCustomUserAttribute always set the attribute to true on iOS.

## 0.9.0

##### Breaking

- The native Android bridge uses Braze Android SDK 7.0.0.
 
- The native iOS bridge uses Braze iOS SDK 3.22.0.

## 0.8.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.21.3.
 
- The native Android bridge uses Braze Android SDK 4.0.2.

- If you are using a custom IInAppMessageManagerListener, then you will need to define new methods added to that interface in Braze Android SDK 4.0.0. See the MainActivity.kt file of our sample app for a reference example.

## 0.7.0

##### Added

- Added BrazePlugin.launchContentCards() and BrazePlugin.refreshContentCards() to natively display and refresh Content Cards.
 
- Adds a Dart callback for receiving Braze Content Card data in the Flutter host app.

- Similar to in-app messages, you will need to subscribe to Content Card updates in your native app code and pass Content Card objects to the Dart layer. Those objects will then be passed to your callback within a List<BrazeContentCard> instance.
 
- To set the callback, call BrazePlugin.setBrazeContentCardsCallback() from your Flutter app with a function that takes a List<BrazeContentCard> instance.

- The BrazeContentCard object supports a subset of fields available in the native model objects, including description, title, image, url, extras, and more.

- On Android, you will need to register an IEventSubscriber<ContentCardsUpdatedEvent> instance and pass returned Content Card objects to the Dart layer using BrazePlugin.processContentCards(contentCards).

- See the MainActivity.kt file of our sample app for a reference example.

- On iOS, you will need to create an NSNotificationCenter listener for ABKContentCardsProcessedNotification events and pass returned Content Card objects to the Dart layer using BrazePlugin.processContentCards(contentCards).

- See the AppDelegate.swift file of our sample app for a reference example.

- Added support for logging Content Card analytics to Braze using BrazeContentCard instances. See logContentCardClicked(), logContentCardImpression(), and logContentCardDismissed() on the BrazePlugin interface.

## 0.6.1

##### Fixed

- Fixed an issue where the Braze Kotlin plugin file’s directory structure did not match its package structure.

## 0.6.0

##### Changed

- The native Android bridge uses Braze Android SDK 3.8.0.
 
- Updated the native iOS bridge to Braze iOS SDK 3.20.4.

## 0.5.2

Important: This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the Braze iOS SDK Changelog for more information.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.2.

## 0.5.1

Important This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 0.5.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 0.5.2 or above if you make use of HTML in-app messages.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.1.

## 0.5.0

Important This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 0.5.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 0.5.2 or above if you make use of HTML in-app messages.

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.20.0.
 
- Important: Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In application:didRegisterForRemoteNotificationsWithDeviceToken:, replace

```

1
2

```
 | 
```
[[Appboy sharedInstance] registerPushToken:
 [NSString stringWithFormat:@"%@", deviceToken]];

```
 | 
 
with

```

1

```
 | 
```
[[Appboy sharedInstance] registerDeviceToken:deviceToken]];

```
 | 

- registerPushToken() was renamed to registerAndroidPushToken() and is now a no-op on iOS. On iOS, push tokens must now be registered through native methods.

## 0.4.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.18.0.
 
- The native Android bridge uses Braze Android SDK 3.6.0.

##### Added

- Added the following new field to BrazeInAppMessage: zippedAssetsUrl.

- Note that a known issue in the iOS plugin prevents HTML in-app messages from working reliably with the Dart in-app message callback. Android is not affected.

## 0.3.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.15.0.
 
- The native Android bridge uses Braze Android SDK 3.5.0.
 
- Support for the Android configuration parameter com_appboy_inapp_show_inapp_messages_automatically has been removed.

- To control whether an in-app message object should be displayed natively or not, create and register an instance of IInAppMessageManagerListener in your native Android code and implement decisioning in the beforeInAppMessageDisplayed method. See MainActivity in our sample app for an example.

- On Android, in-app message objects are no longer sent automatically to the Dart in-app message callback after calling BrazePlugin.setBrazeInAppMessageCallback() in your Dart code.

- Similar to iOS, you will need to implement a delegate interface in your native app code and pass in-app message objects to the Dart layer for passing to the callback.
 
- On Android, the delegate interface is IInAppMessageManagerListener and the method for passing objects to Dart is BrazePlugin.processInAppMessage(inAppMessage).
 
- See the sample IInAppMessageManagerListener implementation in the MainActivity.kt file of our sample app for an example.
 
- This approach gives the integrator more flexibility in deciding when a message should be displayed natively, discarded, or passed into the Dart layer.

##### Added

- Added support for logging in-app message analytics to Braze using BrazeInAppMessage instances. See logInAppMessageClicked, logInAppMessageImpression, and logInAppMessageButtonClicked on the BrazePlugin interface.

## 0.2.1

##### Added

- Added the following new fields to BrazeInAppMessage: imageUrl, useWebView, duration, clickAction, dismissType, messageType
 
- Added the following new fields to BrazeButton: useWebView, clickAction.

## 0.2.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.14.0.
 
- The native Android bridge uses Braze Android SDK 3.2.1.

##### Added

- Adds addAlias() to the public API interface.
 
- Adds requestLocationInitialization() to the public API interface.
 
- Adds getInstallTrackingId() to the public API interface.
 
- Adds support for disabling native in-app message display on Android.

- To disable automatic in-app message display, create a boolean element named com_appboy_inapp_show_inapp_messages_automatically in your Android app’s appboy.xml and set it to false.
 
- Note: Disabling automatic in-app message display was already possible for iOS. For instructions, see README.md.

- Adds a Dart callback for receiving Braze in-app message data in the Flutter host app.

- Analytics are not currently supported on messages displayed through the callback.
 
- To set the callback, call BrazePlugin.setBrazeInAppMessageCallback() from your Flutter app with a function that takes a BrazeInAppMessage instance.

- The BrazeInAppMessage object supports a subset of fields available in the native model objects, including uri, message, header, buttons, and extras.

- The callback should begin to function on Android immediately after being set.
 
- On iOS, you will additionally need to implement the ABKInAppMessageControllerDelegate delegate as described in our public documentation. Your beforeInAppMessageDisplayed delegate implementation must call BrazePlugin.process(inAppMessage). For an example, see AppDelegate.swift in our example app.

## 0.1.1

- Formatted braze_plugin.dart.

## 0.1.0

- Removes the unused dart:async import in braze_plugin.dart.
 
- Makes _callStringMethod private in braze_plugin.dart.
 
- Adds basic dartdoc to the public API interface.

## 0.0.2

- Updates the version of Kotlin used by the Android plugin from 1.2.71 to 1.3.11.

## 0.0.1

- Initial release.
 
- The native iOS bridge uses Braze iOS SDK 3.12.0.
 
- The native Android bridge uses Braze Android SDK 3.1.0.

tip

You can also find a copy of the React Native Braze SDK changelog on GitHub.

## 23.0.0

##### Breaking

- Updates the native Swift SDK version bindings from Braze Swift SDK 16.0.0 to 18.2.0.

- Includes fixes for issues where native Swift calls to Braze.init and Braze.changeUser would block the calling thread. Refer to the linked release notes for further details.
 
- Includes fix for a bug that prevented geofences from being registered with CLLocationManager when automaticLocationCollection was disabled.

- Updates the native Android SDK version bindings from Braze Android SDK 42.3.1 to 43.1.1.

##### Fixed

- Fixes an iOS issue where Braze.subscribeToInAppMessage(false, callback) would fail to disable the default in-app message UI if another React Native event listener was registered first.
 
- Fixes an Android crash where Braze.requestPushPermission() could throw a NullPointerException while off the main thread.

## 22.0.0

##### Breaking

- Updates the native Swift SDK version bindings from Braze Swift SDK 15.1.0 to 16.0.0.

- With this update, the underlying Content Cards list behind getCachedContentCards (including removed, viewed, and clicked states) is updated immediately when changes occur. This now matches the iOS behavior with Android.

- Renames the Braze.BrazeBannerView placementID prop to placementId for consistency with other Banner APIs such as Braze.getBanner(placementId) and Braze.logBannerImpression(placementId).

- Update any usages of placementID={...} to placementId={...}.
 
- The onDismiss callback event payload field placementID has been renamed to placementId.

##### Added

- Adds Braze.dismissBanner(placementId) to programmatically dismiss a Banner by placement ID.
 
- Adds support for Banner dismissal events on Braze.BrazeBannerView.
 
- Adds onDismiss to Braze.BrazeBannerView for integrators to run custom logic when a Banner is dismissed.

##### Deprecated

- Deprecates getContentCards, which performs a network request before returning Content Cards.

- This method will be removed in a future major version.
 
- Use getCachedContentCards instead to retrieve the most recently cached Content Cards state, and requestContentCardsRefresh to manually trigger a background refresh.

## 21.1.0

##### Added

- Updates the native Swift SDK version bindings from Braze Swift SDK 15.0.1 to 15.1.0.

##### Fixed

- Fixes an Android issue where Braze.getInitialPushPayload() returned null on cold start when androidHandlePushDeepLinksAutomatically was enabled, due to a ClassCastException when reading the ab_use_webview notification extra as a String instead of a Boolean.

## 21.0.0

##### Breaking

- Updates the native Swift SDK version bindings from Braze Swift SDK 14.0.4 to 15.0.1.

- Raises the Xcode version to 26.0 (17A324).

##### Added

- Updates the Braze sample app to use React Native version 0.85.3. This change validates SDK compatibility with the latest version of React Native.

##### Fixed

- Updates the native Android SDK version bindings from Braze Android SDK 42.3.0 to 42.3.1.
 
- Corrects misleading JSDoc on logContentCardClicked. The method forwards the click and its validation to the native iOS and Android SDKs.
 
- Fixes an Android issue where in-app messages tied to session start could fail to appear on first launch when using runtime Braze.initialize() with the Expo plugin.

## 20.1.0

##### Added

- Updates the native Android SDK version bindings from Braze Android SDK 42.0.0 to 42.2.0.

##### Fixed

- Fixes an Android issue introduced in version 19.1.0 where a push notification containing a deep link would not navigate to the intended screen when the app was launched from a terminated state.

## 20.0.0

##### Breaking

- Updates the native Android SDK version bindings from Braze Android SDK 41.1.1 to 42.0.0.

##### Fixed

- Fixes an Android issue where getContentCards() could crash natively if its Promise was settled more than once. Also, the promise may now be rejected with no_active_react_instance when React is inactive.

## 19.2.0

##### Added

- Adds support for delayed SDK initialization via Braze.initialize(apiKey, endpoint) in JavaScript.

- On iOS, use BrazeReactInitializer.configure(_:postInitialization:) in your AppDelegate to register configuration and post-initialization closures before React Native starts, such as inside the didFinishLaunching. The closures are applied when Braze.initialize() is called from the JavaScript layer.
 
- On Android, set com_braze_enable_delayed_initialization to true in your braze.xml to prevent auto-initialization. SDK configuration values from braze.xml are applied automatically when Braze.initialize() is called.
 
- Deprecates BrazeReactBridge.initBraze(_:) on iOS. Use BrazeReactInitializer.configure(_:postInitialization:) in your AppDelegate and Braze.initialize(apiKey, endpoint) from JavaScript instead.

- Adds BrazeReactInitializer, a Swift-first helper class for configuring delayed initialization on iOS. This resolves a Swift type-resolution issue where Braze.Configuration was not directly usable from Swift in the Objective-C bridge.

##### Fixed

- Updates the native Swift SDK version bindings from Braze Swift SDK 14.0.1 to 14.0.4.

## 19.1.0

##### Added

- Updates the native Android SDK version bindings from Braze Android SDK 41.0.0 to 41.1.1.

##### Fixed

- Fixes an Android issue where getInitialPushPayload() would not return the push payload when the app was cold-started via a deep link routed through ACTION_VIEW instead of the direct Braze push intent.

## 19.0.0

##### Breaking

- Updates the native Swift SDK version bindings from Braze Swift SDK 13.3.0 to 14.0.1.
 
- Updates the native Android SDK version bindings from Braze Android SDK 40.0.2 to 41.0.0.

##### Added

- Adds Android support for Braze.getInitialPushPayload() to handle push notification deep links when the app is launched from a terminated state.

- This resolves an issue where deep links from push notifications were not handled on Android when the app was cold started.
 
- To use this feature, call BrazeReactUtils.populateInitialPushPayloadFromIntent(intent) in your MainActivity.onCreate() method before React Native initializes. See BrazeProject.tsx in the sample app for an example implementation.
 
- This provides feature parity with the existing iOS implementation added in version 13.1.0.

- Adds logBannerImpression(placementId) and logBannerClick(placementId, buttonId?) methods to manually log banner analytics for custom banner UI implementations.
 
- Updates the Braze sample app to use React Native version 0.83.0. This change validates SDK compatibility with the latest version of React Native.

## 18.0.0

##### Breaking

- Fixes the Typescript type for the callback of subscribeToInAppMessage and addListener for Braze.Events.IN_APP_MESSAGE_RECEIVED.

- These listeners now properly return a callback with the new InAppMessageEvent type. Previously, the methods were annotated to return a BrazeInAppMessage type, but it was actually returning a String.
 
- If you are using either subscription API, ensure that the behavior of your in-app messages are unchanged after updating to this version. See our sample code in BrazeProject.tsx.

- The APIs logInAppMessageClicked, logInAppMessageImpression, and logInAppMessageButtonClicked now accept only a BrazeInAppMessage object to match its existing public interface.

- Previously, it would accept both a BrazeInAppMessage object as well as a String.

- BrazeInAppMessage.toString() now returns a human-readable string instead of the JSON string representation.

- To get the JSON string representation of an in-app message, use BrazeInAppMessage.inAppMessageJsonString.

- On iOS, [[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:] has been moved to [BrazeReactDataTranslator formatPushPayload:withLaunchOptions:].

- This new method is a now a class method instead of an instance method.

- Adds nullability annotations to BrazeReactUtils methods.
 
- Removes the following deprecated methods and properties from the API:

- getInstallTrackingId(callback:) in favor of getDeviceId.
 
- registerAndroidPushToken(token:) in favor of registerPushToken.
 
- setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:) in favor of setAdTrackingEnabled.
 
- PushNotificationEvent.push_event_type in favor of payload_type.
 
- PushNotificationEvent.deeplink in favor of url.
 
- PushNotificationEvent.content_text in favor of body.
 
- PushNotificationEvent.raw_android_push_data in favor of android.
 
- PushNotificationEvent.kvp_data in favor of braze_properties.

- Updates the native Android SDK version bindings from Braze Android SDK 39.0.0 to 40.0.2.

##### Added

- Adds imageAltText and language fields to BrazeInAppMessage for accessibility features.
 
- Updates the native Swift SDK version bindings from Braze Swift SDK 13.2.0 to 13.3.0.

## 17.0.1

##### Fixed

- Fixes an iOS issue where existing Banner views would fail to re-display after navigating away and returning.
 
- Fixes an incompatibility with React Native 0.80+ where iOS Banner views would not be generated as Fabric components but as legacy RCTViews.

- This issue has no known impacts that are visible to the end user.

## 17.0.0

##### Breaking

- Updates the native Android SDK version bindings from Braze Android SDK 37.0.0 to 39.0.0.
 
- Removes support for News Feed. The following APIs have been removed:

- launchNewsFeed
 
- requestFeedRefresh
 
- getNewsFeedCards
 
- logNewsFeedCardClicked
 
- logNewsFeedCardImpression
 
- getCardCountForCategories
 
- getUnreadCardCountForCategories
 
- Braze.Events.NEWS_FEED_CARDS_UPDATED
 
- Braze.CardCategory

##### Fixed

- Fixes an issue where getDeviceID() did not return when an error occurred.
 
- Fixes the Android implementation of the FeatureFlag object to return the correct values for timestamp, image, and JSON objects. Prior to this change, the following APIs would return undefined on Android:

- Braze.getFeatureFlagTimestampProperty(id)
 
- Braze.getFeatureFlagJSONProperty(id)
 
- Braze.getFeatureFlagImageProperty(id)

- Fixes the FeatureFlagTimestampProperty object type to be datetime instead of timestamp.
 
- Fixes an issue where passing a null value for googleAdvertisingId to setAdTrackingEnabled() could cause a crash on Android.

##### Added

- Adds support for Banner properties via new public methods for Banner:

- banner.getStringProperty(key:) for accessing String properties.
 
- banner.getNumberProperty(key:) for accessing num properties.
 
- banner.getTimestampProperty(key:) for accessing int Unix UTC millisecond timestamp properties.
 
- banner.getBooleanProperty(key:) for accessing bool properties.
 
- banner.getImageProperty(key:) for accessing image URL properties as Strings.
 
- banner.getJSONProperty(key:) for accessing JSON properties as Map<String, dynamic>.

- Deprecates the following static methods in favor of new FeatureFlag instance methods:

- Braze.getFeatureFlagStringProperty(flagId, propertyKey), instead use flag.getStringProperty(key)
 
- Braze.getFeatureFlagBooleanProperty(flagId, propertyKey), instead use flag.getBooleanProperty(key)
 
- Braze.getFeatureFlagNumberProperty(flagId, propertyKey), instead use flag.getNumberProperty(key)
 
- Braze.getFeatureFlagTimestampProperty(flagId, propertyKey), instead use flag.getTimestampProperty(key)
 
- Braze.getFeatureFlagJSONProperty(flagId, propertyKey), instead use flag.getJSONProperty(key)
 
- Braze.getFeatureFlagImageProperty(flagId, propertyKey), instead use flag.getImageProperty(key)

## 16.1.0

##### Fixed

- Fixes a missing symbol error when compiling for Android on the React Native legacy bridge architecture on 0.81.

- This change is backwards compatible with prior versions of React Native.

##### Added

- Updates the native Swift SDK version bindings from Braze Swift SDK 13.0.0 to 13.2.0.

- This includes Xcode 26 support.

## 16.0.0

##### Breaking

- Updates the native Android SDK version bindings from Braze Android SDK 36.0.0 to 37.0.0.
 
- Updates the native Swift SDK version bindings from Braze Swift SDK 12.0.0 to 13.0.0.

- The "sdkAuthenticationError" event will now trigger for both “Required” and “Optional” authentication errors.

##### Fixed

- Fixes the iOS implementation of setDateOfBirth to correctly report dates using the Gregorian calendar instead of the user’s device calendar.

- Previously, the SDK would re-format the input date components with the device’s calendar settings if they were non-Gregorian.

##### Added

- Updates the Braze sample app to use React Native version 0.80.0. This change validates SDK compatibility with the latest version of React Native.
 
- Adds ability to unset user first name, last name, phone number, email, gender, language, home city, and country by setting these values to null.

## 15.0.1

##### Fixed

- Improves the TypeScript declarations in the following areas:

- Adds missing TypeScript definitions for the BrazeBannerView component and its children properties.
 
- Usage comments that were previously missing for properties on PushNotificationEvent and TrackingPropertyAllowList will now appear in the TypeScript auto-complete descriptions.

## 15.0.0

[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for < API 25. Read more here.

##### Breaking

- Updates the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
 
- Updates the native iOS version bindings from Braze Swift SDK 11.9.0 to 12.0.0.
 
- Updates the unit representation of PushNotificationEvent.timestamp to milliseconds on iOS.

- Previously, this value would be represented in seconds on iOS. This will now match the existing Android implementation.

## 14.1.0

##### Fixed

- Updates the internal implementations of the following methods to use non-deprecated methods from the native Swift SDK:

- getUserId now uses braze.user.identifier instead of [braze.user idWithCompletion:], which was deprecated in Swift SDK 11.5.0.
 
- Banner.trackingId now uses the underlying banner.trackingId instead of banner.identifier, which was deprecated in Swift SDK 11.4.0.
 
- These deprecations do not have any impacts to functionality.

- Fixes the callback signature of getInitialPushPayload to indicate that null can be returned when there is no payload object available.
 
- Fixes the relative path reference to various Braze data models in the NativeBrazeReactModuleSpec.
 
- Resolves a build failure in the BrazeBannerView class introduced in 14.0.0, which would occur under certain iOS project configurations.

##### Added

- Updates the native iOS version bindings from Braze Swift SDK 11.7.0 to 11.9.0.

## 14.0.0

##### Breaking

- Resolves an Android issue with setDateOfBirth(year, month, day) introduced in 1.38.0, where the month was indexed 0-11 instead of 1-12. The months are now indexed from 1-12 on both Android and iOS.

- The previous behavior on Android would assign setDateOfBirth(1970, 1, 1) to the month of February instead of the intended month of January, and setDateOfBirth(1970, 12, 1) to null instead of the intended month of December.
 
- Customers who wish to retroactively rectify this are recommended to ask their users to confirm their dates of birth and call setDateOfBirth with these values.

- Updates the native Android version bindings from Braze Android SDK 32.1.0 to 35.0.0.

- The minimum required Android SDK version is 25. See more details here.

- The NativeBrazeReactModule.ts file has been moved into a sub-directory called specs.

- If your project contains direct references to this file, you will need to update the relative path of your imports to /specs/NativeBrazeReactModule.
 
- For an example, refer to the sample test setup here.

##### Added

- Updates the native iOS version bindings from Braze Swift SDK 11.2.0 to 11.7.0.
 
- Adds support for the Braze Banner Cards product and APIs to utilize them.

- Braze.requestBannersRefresh(placementIds) - to request a refresh of the banners associated with the provided placement IDs. On iOS only, failures will be logged if unsuccessful.
 
- Braze.getBanner(placementId) - to get a banner with the provided placement ID if available in cache, otherwise returns null.
 
- Braze.Events.BANNER_CARDS_UPDATED event for Braze.addListener - to subscribe to banners updates.

- Adds the default UI components for Braze Banner Cards.

- To use this feature, insert the Braze.BrazeBannerView component into your view hierarchy with the required placementID property.

## 13.2.0

##### Added

- Updates the native iOS version bindings from Braze Swift SDK 11.1.1 to 11.2.0.
 
- Updates the Android bridge to add compatibility with React Native version 0.77.0.

- Updates the Braze sample app to use React Native version 0.77.0.

- Adds the setIdentifierForAdvertiser and setIdentifierForVendor methods to set the IDFA and IDFV, respectively (iOS only). This is a no-op on Android.

## 13.1.1

##### Fixed

- Resolves an iOS issue that would deallocate existing references of braze.delegate when performing a hot reload of the app.

## 13.1.0

##### Fixed

- Updates the iOS sample app to properly retain the BrazeReactDelegate instance. Internally, the Braze SDK uses a weak reference to the delegate, which could be deallocated if not retained by the app. This change ensures the delegate is retained for the lifecycle of the app.

##### Added

- Updates the native iOS version bindings from Braze Swift SDK 11.0.0 to 11.1.1.
 
- Adds the method Braze.getInitialPushPayload() to get the push notification payload when opening the app via notification click while the application was in a terminated state.

- Braze.getInitialURL() is now deprecated in favor of Braze.getInitialPushPayload(). To access the initial URL, use the new method to receive the push notification payload, and access the value of the url key.
 
- If you are using Braze.getInitialPushPayload(), add the following code to your application:didFinishLaunchingWithOptions:launchOptions::

```

1

```
 | 
```
[[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

```
 | 
 
This replaces populateInitialUrlFromLaunchOptions, which is now deprecated.

## 13.0.0

⚠️ Important: This version includes a Swift SDK version with a known issue related to push subscription status. Upgrade to version 13.1.0 instead.

##### Breaking

- Updates the native Android version bindings from Braze Android SDK 31.1.0 to 32.1.0.
 
- Updates the native iOS version bindings from Braze Swift SDK 10.3.0 to 11.0.0.

## 12.2.0

##### Added

- Updates the native iOS version bindings from Braze Swift SDK 10.1.0 to 10.3.0.
 
- Updates the Braze sample app to use React Native version 0.75.2.
 
- Updates the Braze sample app to show how to support GIFs in in-app messages and content cards on iOS.
 
- Adds the ability to conditionally import the android-sdk-location Braze library in gradle.properties via importBrazeLocationLibrary=true.

## 12.1.0

##### Added

- Updates the native iOS version bindings from Braze Swift SDK 10.0.0 to 10.1.0.

## 12.0.0

##### Breaking

- Updates the native iOS version bindings from Braze Swift SDK 9.0.0 to 10.0.0.

- When subscribing to push notification events, the subscription will be triggered on iOS for both "push_received" and "push_opened", instead of only for "push_opened" events.

##### Added

- Updates the Braze sample app to use React Native version 0.74.1.
 
- Adds support for 3 new Feature Flag property types and various APIs for accessing them:

- getFeatureFlagTimestampProperty(id, key) for accessing Int Unix UTC millisecond timestamps as numbers.
 
- getFeatureFlagImageProperty(id, key) for accessing image URLs as strings.
 
- getFeatureFlagJSONProperty(id, key) for accessing JSON objects as object types.

## 11.0.0

##### Breaking

- Updates the native Android version bindings from Braze Android SDK 30.4.0 to 31.1.0.

##### Fixed

- Fixes an issue on Android where the timestamp of a PushNotificationEvent was incorrectly translated from a long to a int. The value received by the JavaScript layer is now the same as the value sent from the Android code.

## 10.0.0

##### Breaking

- Updates the native iOS version bindings from Braze Swift SDK 8.4.0 to 9.0.0.

##### Added

- Updates the native Android version bindings from Braze Android SDK 30.3.0 to 30.4.0.

## 9.2.0

##### Fixed

- Fixes the Android implementation of Braze.setCustomUserAttribute() to correctly handle null values.

- Thanks @owonie for your contribution!

##### Added

- Updates the native iOS version bindings from Braze Swift SDK 8.2.1 to 8.4.0.

## 9.1.0

##### Fixed

- Fixes the iOS implementation of Braze.registerPushToken() to correctly pass the device token to the native SDK.

##### Added

- Adds the BrazeInAppMessage.isTestSend property, which indicates whether an in-app message was triggered as part of a test send.
 
- Updates the native iOS version bindings from Braze Swift SDK 8.1.0 to 8.2.1.
 
- Updates the native Android version bindings from Braze Android SDK 30.1.1 to 30.3.0.

## 9.0.0

##### Breaking

- Bumps React Native minimum requirement version to 0.71.0.

- For further details about levels of support for each React Native release, refer to Releases Support Policy in the React Working Group.

- Bumps the minimum required iOS version to 12.0.
 
- Updates the native iOS version bindings from Braze Swift SDK 7.5.0 to 8.1.0.
 
- Updates the native Android version bindings from Braze Android SDK 29.0.1 to 30.1.1.

## 8.4.0

##### Fixed

- Fixes the hasListeners property in the iOS native layer to prevent duplicate symbol errors with other libraries.
 
- Addresses redefinition build errors when using the iOS Turbo Module with statically linked frameworks.

##### Added

- Adds support to modify the allow list for Braze tracking properties via the following TypeScript properties and methods:

- TrackingProperty string enum
 
- TrackingPropertyAllowList object interface
 
- updateTrackingPropertyAllowList method
 
- For details, refer to the Braze iOS Privacy Manifest documentation.

- Deprecates the setGoogleAdvertisingId method in favor of setAdTrackingEnabled.

- This new method will now set adTrackingEnabled flag on iOS and both the adTrackingEnabled flag and the Google Advertising ID on Android.

- Exposes the ContentCardTypes enum through the public TypeScript interface in index.d.ts.
 
- Updates the native iOS bridge from Braze Swift SDK 7.5.0 to 7.7.0.

## 8.3.0

##### Added

- Adds example integrations for Braze Rich Push Notifications and Braze Push Stories to the iOS sample app.
 
- Updates the native iOS bridge from Braze Swift SDK 7.3.0 to 7.5.0.
 
- Adds support for React Native 0.73.

- Removes strict Java version dependencies in the build.gradle file of the Braze library.
 
- Updates the Braze sample app to use React Native version 0.73.1.

## 8.2.0

##### Fixed

- Adds a missing update from Braze Android SDK 29.0.0 to 29.0.1 in the 8.1.0 release.

##### Added

- Updates the native iOS bridge from Braze Swift SDK 7.1.0 to 7.3.0.

- This release includes compatibility with Expo Notifications. Refer to the push notification setup documentation for more details.

## 8.1.0

##### Fixed

- Fixes the setLastKnownLocation method to sanitize null inputs before calling the native layer.

- This previously caused an issue when calling this method on the legacy React Native architecture.

- Updates the native Android bridge from Braze Android SDK 29.0.0 to 29.0.1.

##### Added

- Push notification objects are now accessible in the JavaScript layer via new fields on the PushNotificationEvent interface.

- Deprecates the following fields from the PushNotificationEvent interface in favor of the new names that can be used on both iOS and Android:

- push_event_type -> Use payload_type instead.
 
- deeplink -> Use url instead.
 
- content_text -> Use body instead.
 
- raw_android_push_data -> Use the android object instead.
 
- kvp_data -> Use braze_properties instead.

- Adds iOS support for the listener event Braze.Events.PUSH_NOTIFICATION_EVENT.

- On iOS, only "push_opened" events are supported, indicating the user interacted with the received notification.
 
- The iOS event does not support the deprecated legacy fields mentioned above.

- Adds methods to manually perform the action of an In-App Message or Content Card when using a custom UI.

- Braze.performInAppMessageButtonAction(inAppMessage, buttonId)
 
- Braze.performInAppMessageAction(inAppMessage)
 
- Braze.processContentCardClickAction(id)

- Updates the native iOS bridge from Braze Swift SDK 7.0.0 to 7.1.0.

## 8.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 27.0.1 to 29.0.0.
 
- Updates the native iOS bridge from Braze Swift SDK 6.6.0 to 7.0.0.
 
- Renames the Banner Content Card type to ImageOnly:

- BannerContentCard → ImageOnlyContentCard
 
- ContentCardTypes.BANNER → ContentCardTypes.IMAGE_ONLY
 
- On Android, if the XML files in your project contain the word banner for Content Cards, it should be replaced with image_only.

- Braze.getFeatureFlag(id) will now return null if the feature flag does not exist.
 
- Braze.Events.FEATURE_FLAGS_UPDATED will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.

##### Added

- Adds Braze.getUserId() to get the ID of the current user.

## 7.0.0

##### Breaking

- Updates the native Android bridge from Braze Android SDK 26.3.2 to 27.0.1.

##### Fixed

- Fixes the Android layer to record date custom user attributes as ISO strings instead of integers.
 
- Fixes a bug introduced in 6.0.0 where Braze.getInitialUrl() may not trigger the callback on Android.

##### Added

- Updates the native iOS bridge from Braze Swift SDK 6.4.0 to 6.6.0.
 
- Adds support for nested custom user attributes.

- The setCustomUserAttribute now accepts objects and arrays of objects.
 
- Adds an optional merge parameter to the setCustomUserAttribute method. This is a non-breaking change.
 
- Reference our public docs for more information.

- Adds Braze.setLastKnownLocation() to set the last known location for the user.
 
- Adds Braze.registerPushToken() in the JavaScript layer to post a push token to Braze’s servers.

- Deprecates Braze.registerAndroidPushToken() in favor of Braze.registerPushToken().

- Adds Braze.getCachedContentCards() to get the most recent content cards from the cache, without a refresh.
 
- Adds support for the Feature Flag method logFeatureFlagImpression(id).

## 6.0.2

##### Fixed

- Updates the native Android bridge from Braze Android SDK 26.3.1 to 26.3.2.

## 6.0.1

##### Fixed

- Adds 'DEFINES_MODULE' => 'YES' to the iOS Podspec when compiling the Turbo Module to prevent the need for static framework linkage when using the Braze Expo plugin.

## 6.0.0

##### Breaking

- If you are using the New Architecture, this version requires React Native 0.70 or higher.
 
- Fixes the sample setup steps for iOS apps conforming to RCTAppDelegate.

- ⚠️ If your app conforms to RCTAppDelegate and was following our previous AppDelegate setup in the sample project or Braze documentation, you will need to reference our updated samples to prevent any crashes from occurring when subscribing to events in the new Turbo Module. ⚠️

- If your project contains unit tests that depend on the Braze React Native module, you will need to update your imports to the NativeBrazeReactModule file to properly mock the Turbo Module functions in Jest.

- For an example, refer to the sample test setup here.

- Updates the native Android bridge from Braze Android SDK 25.0.0 to 26.3.1.
 
- Fixes the presentation of in-app messages to match the documented behavior.

- Calling subscribeToInAppMessage or addListener in the Javascript layer will no longer cause a custom BrazeInAppMessageUIDelegate implementation on iOS to be ignored.
 
- Calling Braze.addListener for the inAppMessageReceived event will subscribe in both the Javascript and the native layers (iOS + Android). This means it is no longer required to call Braze.subscribeToInAppMessage.

- Per the Braze documentation, you do not need to explicitly call subscribeToInAppMessage to use the default In-App Message UI.

- See our documentation for more details around Advanced customization.

##### Added

- Migrates the Braze bridge to a backwards-compatible New Architecture Turbo Module.

- This is a non-breaking change to your existing imports of the Braze SDK if you are using React Native 0.70+.
 
- The Braze SDK continues to be compatible with both the New Architecture and old React Native architecture.

- Adds the getDeviceId method to replace getInstallTrackingId, which is now deprecated.
 
- Updates the native iOS bridge from Braze Swift SDK 6.3.1 to 6.4.0.
 
- Adds a conditional library namespace to the Android build.gradle file to prepare for React Native 0.73, which uses AGP 8.x.

- For more details, refer to this React Native announcement.

## 5.2.0

##### Fixed

- Fixes an issue on Android where push notifications wouldn’t be forwarded after the app was closed.
 
- Fixes an issue on iOS preventing in-app message subscription events from being sent if subscribeToInAppMessage is called prior to any Braze.addListener calls.
 
- Changed the Java compatibility version for the Android plugin to Java 11.

##### Added

- Updates the native iOS bridge from Braze Swift SDK 6.2.0 to 6.3.1.

## 5.1.0

##### Fixed

- Fixes an issue that occured whenever a custom event is logged with dictionary properties using a key named “type”.
 
- Removes the automatic assignment of BrazeDelegate in the iOS bridge, allowing for custom implementations to be assigned to the braze instance.

## 5.0.0

##### Breaking

- Updates the native iOS bridge from Braze Swift SDK 5.13.0 to 6.2.0.
 
- Removes setSDKFlavor and setMetadata, which were no-ops starting from version 2.0.0.

- On iOS, these fields must be set using the Braze.Configuration object at SDK initialization.
 
- On Android, these fields must be set via the braze.xml file.

##### Fixed

- Fixes an issue on Android with getNewsFeedCards() and getContentCards() where promises could be invoked more than once.

##### Added

- Updates the native Android bridge from Braze Android SDK 24.3.0 to 25.0.0.

## 4.1.0

##### Fixed

- Fixes an issue in the PushNotificationEvent object introduced in 2.0.1 where a field was named context_text instead of the correct value of content_text.

##### Added

- Adds support for the upcoming Braze Feature Flags product with the following methods:

- getFeatureFlag(id)
 
- getAllFeatureFlags()
 
- refreshFeatureFlags()
 
- getFeatureFlagBooleanProperty(id, key)
 
- getFeatureFlagStringProperty(id, key)
 
- getFeatureFlagNumberProperty(id, key)

- Adds the Braze Event key Braze.Events.FEATURE_FLAGS_UPDATED for subscribing to Feature Flags updates.

## 4.0.0

##### Breaking

- The iOS bridge now automatically attaches the default In-App Message UI with the braze instance, without needing to call subscribeToInAppMessage(). This updates the behavior from 2.0.0 to simplify integration.

- This change doesn’t affect integrations using custom UIs for in-app messages.

- Changes the returned value when subscribing to Braze.Events.CONTENT_CARDS_UPDATED to be a Braze.ContentCardsUpdatedEvent object instead of a boolean.

- Braze.ContentCardsUpdatedEvent contains a cards property which is an array of the Content Cards in the update.
 
- Thanks @Minishlink for your contribution!

##### Fixed

- Fixes an issue in the iOS bridge where getContentCards() and getNewsFeedCards() returned data in a different format than the Android bridge.
 
- Fixes the behavior when using the recommended iOS integration where the React Bridge delegate had conflicts with other dependencies. The updated sample app code can be found here.

##### Added

- Updates the native iOS bridge to Braze Swift SDK 5.13.0.
 
- Improves typescript definitions for addListener event types.

## 3.0.0

Starting with this release, this SDK will use Semantic Versioning.

##### ⚠ Breaking

- Fixes the behavior in the iOS bridge introduced in version 2.0.0 when logging clicks for in-app messages, content cards, and news feed cards. Calling logClick now only sends a click event for metrics, instead of both sending a click event as well as redirecting to the associated url field.

- For instance, to log a content card click and redirect to a URL, you will need two commands:
```
Braze.logContentCardClicked(contentCard.id);

// Your own custom implementation
Linking.openUrl(contentCard.url);
```

- This brings the iOS behavior to match version 1.x and bring parity with Android’s behavior.

##### Fixed

- Fixes an issue in the iOS bridge introduced in 2.0.0 where getContentCards() and getNewsFeedCards() would return an array of cards with the url and image fields as null.

##### Changed

- Updates the native iOS bridge to Braze Swift SDK 5.11.2.
 
- Updates the native Android bridge to Braze Android SDK 24.3.0.
 
- Updates getContentCards on the iOS bridge to initiate a refresh before returning the array of Content Cards. This brings parity with the Android bridge behavior.

## 2.1.0

##### Added

- Added 'DEFINES_MODULE' => 'YES' to the Cocoapod’s xcconfig to remove the need for static framework linkage on iOS when using the Braze Expo plugin.

## 2.0.2

##### Fixed

- Removes the usage of Objective-C modules when importing the Braze Swift SDK for improved compatibility with Objective-C++.

- When importing BrazeKit or BrazeLocation, you must use the #import <Module/Module-Swift.h> syntax:

- @import BrazeKit; → #import <BrazeKit/BrazeKit-Swift.h>
 
- @import BrazeLocation; → #import <BrazeLocation/BrazeLocation-Swift.h>

## 2.0.1

##### Fixed

- Fixes compatibility issues with newer versions of React Native introduced in 2.0.0.
 
- Fixes an issue where callbacks were not being executed for some user attribute methods.

## 2.0.0

##### ⚠ Breaking

- The Braze React Native SDK npm package has moved from react-native-appboy-sdk to @braze/react-native-sdk.
 
- Renames AppboyReactBridge and AppboyReactUtils to BrazeReactBridge and BrazeReactUtils, respectively.
 
- This version requires React Native 0.68 or higher.
 
- Updates the native iOS bridge to use the new Swift SDK version 5.9.1.
 
- During migration, update your project with the following changes in your iOS integration:

- To initialize Braze, follow these integration steps to create a configuration object. Then, add this code to complete the setup:

```

1

```
 | 
```
let braze = BrazePlugin.initBraze(configuration)

```
 | 

- This migration requires re-identifying users. To do so, you must call the changeUser method on the Braze instance for non-anonymous users. You can read more about it here.
 
- To continue using SDWebImage as a dependency, add this line to your project’s /ios/Podfile:

```

1

```
 | 
```
pod 'SDWebImage', :modular_headers => true

```
 | 

- Then, follow these setup instructions.

- To use the default In-App Message UI, make sure to call subscribeToInAppMessage() or else follow these instructions to add it to your app.
 
- For sample code to help with the migration, reference our sample app and AppDelegate.mm file.
 
- If you are integrating this SDK with an application that uses only Objective-C, create an empty Swift file to ensure that all the relevant Swift runtime libraries are linked. Reference this file from our sample app.

- The following methods for News Feed are now no-ops on iOS:

- Braze.launchNewsFeed()
 
- Braze.getCardCountForCategories()
 
- Braze.getUnreadCardCountForCategories()

- Updates the native Android bridge to Braze Android SDK 24.2.0.

##### Added

- Adds the following APIs to more easily interface with the News Feed product. Thanks @swissmanu for your contribution!

- Braze.getNewsFeedCards()
 
- Braze.logNewsFeedCardClicked()
 
- Braze.logNewsFeedCardImpression()

## 1.41.0

##### ⚠ Breaking

- Removed setFacebookData().
 
- Removed setTwitterData().

##### Changed

- Updated the native Android bridge to Braze Android SDK 23.3.0.
 
- Exposes isControl field for ContentCard.
 
- Removed kotlinVersion gradle template variable. To override the Kotlin version used, please use a Gradle dependency resolutionStrategy.

## 1.40.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 23.2.1.
 
- Updated the native iOS bridge to Braze iOS SDK 4.5.1.

##### Changed

- Updated the React podspec dependency to React-Core.

## 1.39.0

##### ⚠ Breaking

- Renamed the kotlin_version gradle template variable to kotlinVersion.
 
- Updated the native Android bridge to Braze Android SDK 23.2.0.

##### Fixed

- Fixed an issue that caused a NativeEventEmitter warning message to appear.

## 1.38.1

##### Fixed

- Fixed an issue introduced in 1.38.0 where setEmail did not work as expected on Android.

## 1.38.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 23.0.1.
 
- Updated the native iOS bridge to Braze iOS SDK 4.5.0.
 
- The Braze React Native Android SDK now requires Kotlin directly for compilation. An example is included below:

```

1
2
3
4
5
6
7

```
 | 
```
 buildscript {
 ext.kotlin_version = '1.6.0'

 dependencies {
 classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
 }
 }

```
 | 

##### Added

- Introduced Braze.Events.PUSH_NOTIFICATION_EVENT which can be used to listen for Braze Push Notification events on Android. See example below:

```

1
2
3
4
5

```
 | 
```
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, function(data) {
 console.log(`Push Notification event of type ${data.push_event_type} seen.
 Title ${data.title}\n and deeplink ${data.deeplink}`);
 console.log(JSON.stringify(data, undefined, 2));
});

```
 | 

- Added Braze.requestPushPermission() to request a permissions prompt for push notifications.

## 1.37.0

##### ⚠ Breaking

- The Braze React Native SDK now exports its default object as an ES Module. If you currently import the SDK using require(), you will need to now import it as a standard ES Module (e.g. import Braze from "react-native-appboy-sdk").

##### Added

- Introduced Braze.subscribeToInAppMessage() which publishes an event to the Javascript layer when an in-app message is triggered and allows you to choose whether or not to use the default Braze UI to display in-app messages.

## 1.36.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 21.0.0.
 
- Updated the native iOS bridge to Braze iOS SDK 4.4.4.
 
- Removed setAvatarImageUrl().
 
- Removed logContentCardsDisplayed. This method was not part of the recommended Content Cards integration and can be safely removed.

## 1.35.1

##### Fixed

- Fixed an issue where setMetadata did not have a method implementation for Android.

## 1.35.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 4.4.2.
 
- Drops support for iOS 9 and 10.

## 1.34.1

##### Fixed

- Fixed an issue where getInitialUrl would not resolve when there is no initial URL.

## 1.34.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 18.0.1.

##### Fixed

- Fixed an issue with Content Card types. Thanks @jtparret!

##### Changed

- Improved logging around getInitialUrl.

## 1.33.1

##### Fixed

- Fixed an issue introduced in 1.33.0 that caused a build error on iOS.

## 1.33.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 16.0.0.
 
- Updated the native iOS bridge to Braze iOS SDK 4.3.4.

##### Added

- Added ReactAppboy.addToSubscriptionGroup() and ReactAppboy.removeFromSubscriptionGroup() to manage SMS/Email Subscription Groups.
 
- Custom events and purchases now support nested properties. In addition to integers, floats, booleans, dates, or strings, a JSON object can be provided containing dictionaries of arrays or nested dictionaries. All properties combined can be up to 50 KB in total length.

## 1.32.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 15.0.0.
 
- Updated the native iOS bridge to Braze iOS SDK 4.3.2.

## 1.31.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 4.3.1.

##### Added

- Added support for new SDK Authentication feature to the Javascript layer. See setSdkAuthenticationSignature on the Appboy interface, as well as the optional signature parameter on ReactAppboy.changeUser.

## 1.30.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 4.3.0, which fixes a crashing issue with Content Cards when using the default UI.
 
- Updated the native Android bridge to Braze Android SDK 14.0.1.

## 1.29.1

##### ⚠️ Known Issues

- This release contains a known issue with the Content Cards default UI on iOS, where showing a “Classic” type card with an image causes a crash. If you are using the default Content Cards UI, do not upgrade to this version.

##### Fixed

- Fixed issue introduced in 1.29.0 where calling ReactAppboy.changeUser would cause an error on Android.

## 1.29.0

##### ⚠️ Known Issues

- This release contains a known issue with the Content Cards default UI on iOS, where showing a “Classic” type card with an image causes a crash. If you are using the default Content Cards UI, do not upgrade to this version.

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 14.0.0.
 
- Updated the native iOS bridge to Braze iOS SDK 4.2.0.

## 1.28.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 4.0.2.
 
- Updated the native Android bridge to Braze Android SDK 13.1.2, which contains support for Android 12.

##### Fixed

- Fixed an issue where calling getInstallTrackingId() while the SDK was disabled would cause a crash on iOS.

##### Added

- Added support for ReactAppboy.setGoogleAdvertisingId() to set the Google Advertising ID and associated ad-tracking enabled field for Android devices. This is a no-op on iOS.

## 1.27.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.33.1.
 
- Updated the native Android bridge to Braze Android SDK 13.0.0.

##### Added

- Added support for receiving iOS push action button deep links in ReactAppboy.getInitialURL(). If you are using ReactAppboy.getInitialURL() and implement iOS push action button categories, add the following code to the beginning of your userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler::

```

1

```
 | 
```
[[AppboyReactUtils sharedInstance] populateInitialUrlForCategories:response.notification.request.content.userInfo];

```
 | 

## 1.26.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.31.2.
 
- Updated the native Android bridge to Braze Android SDK 12.0.0.

## 1.25.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.29.1, which adds improved support for in-app message display on iPhone 12 models.
 
- Updated the native Android bridge to Braze Android SDK 11.0.0.

## 1.24.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.28.0.
 
- Updated the native Android bridge to Braze Android SDK 10.1.0. Please read the Braze Android SDK changelog for details.

## 1.23.0

##### ⚠ Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.27.0. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.

## 1.22.0

##### Changed

- Updated the native Android bridge to Braze Android SDK 8.1.0, which contains support for Android 11.
 
- Updated the native iOS bridge to Braze iOS SDK 3.26.1, which contains preliminary support for iOS 14.

## 1.21.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 8.0.1.
 
- Updated the native iOS bridge to Braze iOS SDK 3.26.0.

##### Added

- Added support for working with in-app messages in the JavaScript layer. In-App Messages can be instantiated using the BrazeInAppMessage class. The resulting object can be passed into the analytics methods: logInAppMessageClicked, logInAppMessageImpression, and logInAppMessageButtonClicked (along with the button index). See the README for additional implementation details or the AppboyProject sample app for an integration example.

##### Changed

- Improved Typescript definitions for setCustomUserAttribute and incrementCustomUserAttribute.

- Thanks @janczizikow!

##### Fixed

- Fixed incorrect TypeScript definition for ContentCard.

- Thanks @Hannes-Sandahl-Mpya!

## 1.20.0

##### ⚠ Breaking

- Updated the native Android bridge to Braze Android SDK 7.0.0.

##### Added

- Added ReactAppboy.requestGeofences() to request a Braze Geofences update for a manually provided GPS coordinate. Automatic Braze Geofence requests must be disabled to properly use this method.

## 1.19.0

##### Breaking

- Updated the native Android bridge to Braze Android SDK 5.0.0.
 
- Updated the native iOS bridge to Braze iOS SDK 3.21.3.

## 1.18.0

##### Breaking

- Updated the native Android bridge to Braze Android SDK 3.8.0.

##### Fixed

- Fixed an issue where ReactContext.getJSModule() could be called before the native module was initialized.

- Thanks @tszajna0!

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.4.

## 1.17.4

##### Fixed

- Removed a support library reference in AppboyReactBridge.java that caused Androidx compatibility issues.

## 1.17.3

##### Fixed

- Added SDWebImage and Headers pod directories to the AppboyReactBridge project’s Header Search Paths. Thanks @tomauty and @mlazari for your contributions! See https://github.com/braze-inc/braze-react-native-sdk/pull/70 and https://github.com/braze-inc/braze-react-native-sdk/pull/69.

##### Changed

- Updated the native Android bridge to Braze Android SDK 3.7.1.

## 1.17.2

Important: This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the Braze iOS SDK Changelog for more information.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.2.

## 1.17.1

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.17.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.17.2 or above if you make use of HTML in-app messages.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.1.

## 1.17.0

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.17.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.17.2 or above if you make use of HTML in-app messages.

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.20.0.
 
- Important: Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In application:didRegisterForRemoteNotificationsWithDeviceToken:, replace

```

1
2

```
 | 
```
[[Appboy sharedInstance] registerPushToken:
 [NSString stringWithFormat:@"%@", deviceToken]];

```
 | 
 
with

```

1

```
 | 
```
[[Appboy sharedInstance] registerDeviceToken:deviceToken];

```
 | 

- ReactAppboy.registerPushToken() was renamed to ReactAppboy.registerAndroidPushToken() and is now a no-op on iOS. On iOS, push tokens must now be registered through native methods.

## 1.16.0

Important This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.17.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.17.2 or above if you make use of HTML in-app messages.

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.19.0.
 
- Updated the native Android bridge to Braze Android SDK 3.7.0.
 
- Note: This Braze React Native SDK release updates to Braze Android SDK and Braze iOS SDK dependencies which no longer enable automatic Braze location collection by default. Please consult their respective changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.
 
- Removes the Feedback feature.

- submitFeedback() and launchFeedback() have been removed from the Appboy interface.

##### Added

- Added the ability to more easily create custom UIs for Content Cards from within the React Native layer by providing access to card data and analytics methods in Javascript.

- Added ReactAppboy.getContentCards for getting locally cached content cards data.

- To request a Content Cards update, use ReactAppboy.requestContentCardsRefresh().

- Added ReactAppboy.logContentCardsDisplayed for manually logging an impression for the content card feed.
 
- Added ReactAppboy.logContentCardClicked for manually logging a click to Braze for a particular card.
 
- Added ReactAppboy.logContentCardImpression for manually logging an impression to Braze for a particular card.
 
- Added ReactAppboy.logContentCardDismissed for manually logging a dismissal to Braze for a particular card.
 
- Added ReactAppboy.addListener for subscribing to ReactAppboy.Events.CONTENT_CARDS_UPDATED events.

- After a successful update, use getContentCards to retrieve updated cards.
 
- 

```

1
2
3
4

```
 | 
```
ReactAppboy.addListener(ReactAppboy.Events.CONTENT_CARDS_UPDATED, async function() {
 let cards = await ReactAppboy.getContentCards();
 console.log('Content Cards Updated.', cards);
})

```
 | 

- See https://github.com/braze-inc/braze-react-native-sdk/pull/58. Thanks @alexmbp!

## 1.15.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.17.0.
 
- Removed the NewsFeedLaunchOptions enum. Using these arguments with launchNewsFeed() had been a no-op since version 1.7.0.

## 1.14.0

##### Breaking

- Updated the native Android bridge to Braze Android SDK 3.5.0.

##### Fixed

- Fixed an issue where logging custom events or purchases without event properties would cause crashes on Android, for example logCustomEvent("event").

##### Added

- Added additional TypeScript definitions.

## 1.13.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.15.0.

- This release of the iOS SDK added support for SDWebImage version 5.0.
 
- Note that upgrading to SDWebImage 5.0 also removed the FLAnimatedImage transitive dependency.

## 1.12.0

##### Breaking

- Updated the native Android bridge to Braze Android SDK 3.3.0.

##### Added

- Added ReactAppboy.launchContentCards() for launching the content cards UI.

## 1.11.1

##### Added

- Added Typescript definitions for the Appboy interface.

- Thanks @ahanriat and @josin for your contributions! See https://github.com/braze-inc/braze-react-native-sdk/pull/57 and https://github.com/braze-inc/braze-react-native-sdk/pull/38.
 
- Note that certain less-used parts of the API were excluded. Please file an issue if you would like specific method(s) added.

## 1.11.0

##### Breaking

- Updated the native Android bridge to Braze Android SDK 3.2.0.

- Added AppboyFirebaseMessagingService to directly use the Firebase messaging event com.google.firebase.MESSAGING_EVENT. This is now the recommended way to integrate Firebase push with Braze. The AppboyFcmReceiver should be removed from your AndroidManifest and replaced with the following:

```

1
2
3
4
5

```
 | 
```
<service android:name="com.appboy.AppboyFirebaseMessagingService">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT" />
 </intent-filter>
</service>

```
 | 

- Also note that any c2dm related permissions should be removed from your manifest as Braze does not require any extra permissions for AppboyFirebaseMessagingService to work correctly.

- Updated the native iOS bridge to Braze iOS SDK 3.14.0.

- Dropped support for iOS 8.

##### Added

- Added support for sending JavaScript Date() type custom event and purchase properties through the Appboy interface.

## 1.10.0

##### Breaking

- Updated the native Android bridge to Braze Android SDK 3.1.0.

##### Added

- Added addAlias(aliasName, aliasLabel) to the Appboy interface to allow aliasing users.

- Thanks @alexmbp!

##### Changed

- Updated build.gradle to use project.ext config if available.

## 1.9.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.11.0.
 
- Updated the native Android bridge to Braze Android SDK 3.0.1.
 
- Updated the Android wrapper to use api and implementation syntax in it’s build.gradle instead of compile. As part of this work, the Android Gradle plugin version was updated to 3.2.1.

##### Fixed

- Fixed an issue where the Android wrapper would include an older version of React Native in test APK builds.

##### Added

- Added setUserAttributionData() to the Appboy interface to allow setting the attribution data for the current user.
 
- Added getInstallTrackingId() to the Appboy interface to allow getting the install tracking id. This method is equivalent to calling Appboy.getInstallTrackingId() on Android and returns the IDFV on iOS.
 
- Added setLanguage() to the Appboy interface to allow setting a language for the current user.
 
- Added hideCurrentInAppMessage() to the Appboy interface to allow hiding of the currently displayed in-app message.

##### Changed

- Updated our sample projects to use React Native 0.56.

## 1.8.1

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.8.4.

## 1.8.0

##### Breaking

- Updated the native Android bridge to Braze Android SDK 2.7.0.

- Important: Note that in Braze Android SDK 2.7.0, AppboyGcmReceiver was renamed to AppboyFcmReceiver. This receiver is intended to be used for Firebase integrations. Please update the AppboyGcmReceiver declaration in your AndroidManifest.xml to reference AppboyFcmReceiver and remove the com.google.android.c2dm.intent.REGISTRATION intent filter action.

- Updated the native iOS bridge to Braze iOS SDK 3.8.3.

##### Added

- Added setLocationCustomAttribute() to the Appboy interface to allow setting of custom location attributes.

## 1.7.3

##### Added

- Added requestLocationInitialization() to the Appboy interface. Calling this method is the equivalent of calling AppboyLocationService.requestInitialization() on the native Braze Android SDK. The method is a no-op on iOS.

## 1.7.2

##### Fixed

- Fixed an issue introduced in 1.7.0 where calling launchNewsFeed() would cause crashes in the Android bridge.

## 1.7.1

##### Fixed

- Updated the podspec to point to Braze iOS SDK version 3.5.1.

## 1.7.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.5.1.
 
- Updated the native Android bridge to Appboy Android SDK 2.4.0.

##### Added

- Added Other, Unknown, Not Applicable, and Prefer not to Say options for user gender.
 
- Updated the AppboyProject sample app to use FCM instead of GCM.
 
- Added toasts to provide feedback for user actions in the AppboyProject sample app.
 
- Implemented requiresMainQueueSetup in AppboyReactBridge.m to prevent warnings in React Native 0.49+.

- See https://github.com/braze-inc/braze-react-native-sdk/pull/39. Thanks @danieldecsi!

##### Changed

- Passing launch options into launchNewsFeed() is now a no-op.

## 1.6.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.3.3.
 
- Updated the native Android bridge to Braze Android SDK 2.2.5.

##### Added

- Added support for wiping all customer data created by the Braze SDK via Appboy.wipeData().

- Note that on iOS, wipeData() will disable the SDK for the remainder of the app run. For more information, see our iOS SDK’s documentation for disableSDK.

- Added Appboy.disableSDK() to disable the Braze SDK immediately.
 
- Added Appboy.enableSDK() to re-enable the SDK after a call to Appboy.disableSDK().

- Note that on iOS, enableSDK() will not enable the SDK immediately. For more information, see our iOS SDK’s documentation for requestEnableSDKOnNextAppRun.

##### Changed

- Removed allowBackup from the plugin AndroidManifest.xml.

- See https://github.com/braze-inc/braze-react-native-sdk/pull/34. Thanks @SMJ93!

## 1.5.2

##### Fixed

- Fixed a race condition between SDK flavor reporting and sharedInstance initialization on iOS.

## 1.5.1

##### Fixed

- Fixed a bug that caused opted-in subscription states to not be reflected on the user profile.

## 1.5.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.0.0 or later.
 
- Updated the native Android bridge to Braze Android SDK 2.2.4.
 
- Changed success callbacks on submitFeedback() on Android to always return true as submitFeedback() was changed to return void in the native SDK.

## 1.4.1

##### Added

- Added support for apps that use use_frameworks in Podfile.

- See https://github.com/braze-inc/braze-react-native-sdk/commit/6db78a5bbeb31457f8a1dcf988a3265d8db9a437 and https://github.com/braze-inc/braze-react-native-sdk/issues/29. Thanks @jimmy-devine and @sljuka.

## 1.4.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 2.31.0 or later.
 
- Updated the native Android bridge to Braze Android SDK 2.1.4.

##### Added

- Added ReactAppboy.registerPushToken() for registering push tokens with Braze.

- See https://github.com/braze-inc/braze-react-native-sdk/pull/13. Thanks @dcvz!

- Added the local react-native-appboy-sdk Podspec for integrating the React Native iOS bridge via Cocoapods.

- See https://github.com/braze-inc/braze-react-native-sdk/pull/15. Thanks @pietropizzi!

## 1.3.0

##### Breaking

- Updates the native iOS bridge to use Braze iOS SDK 2.29.0, which drops support for iOS 7.
 
- Updates the native Android bridge to use Braze Android SDK 2.0.0.

##### Added

- Adds ReactAppboy.requestImmediateDataFlush() for requesting an immediate flush of any data waiting to be sent to Braze’s servers.
 
- Adds ReactAppboy.requestFeedRefresh() for requesting a refresh of the News Feed.

- See https://github.com/braze-inc/braze-react-native-sdk/pull/12. Thanks @stief510!

- Added the ability to pass an optional dictionary of News Feed launch options to launchNewsFeed(). See NewsFeedLaunchOptions for supported keys.

- For more information on currently supported NewsFeedLaunchOptions keys, see the card width and card margin properties on ABKFeedViewController.
 
- See https://github.com/braze-inc/braze-react-native-sdk/pull/10. Thanks @mihalychk!

## 1.2.0

##### Breaking

- Updates the native iOS bridge to be compatible with React Native v0.40.0.

##### Changed

- Updates the AppboyProject sample project to React Native v0.41.1.

## 1.1.0

##### Breaking

- Update Required — Fixes a bug in the iOS bridge where custom attribute dates were converted incorrectly, causing incorrect date data to be sent to Braze. As a result of the fix, setDateCustomUserAttribute() in the iOS React bridge may now only be called with a double.

- Note: The default Javascript Braze interface has not changed, so for most integrations this just requires updating the SDK, unless you were manually calling our iOS bridge outside of our recommended integration.
 
- See https://github.com/braze-inc/braze-react-native-sdk/issues/7

## 1.0.0

##### Breaking

- Update Required — Updates iOS push handling in the AppboyProject sample project to be compatible with iOS 10. For more information, refer to the CHANGELOG for Braze iOS SDK v2.24.0.

##### Added

- Adds callbacks to the native bindings to provide function call results to React Native.
 
- Exposes ReactAppboy.getCardCountForCategories() and ReactAppboy.getUnreadCardCountForCategories() for retrieving News Feed card counts.

- See https://github.com/braze-inc/braze-react-native-sdk/issues/1

- Adds ReactAppboy.getInitialURL() for handling deep links when an iOS application is launched from the suspended state by clicking on a push notification with a deep link. See componentDidMount() in AppboyProject.js for a sample implementation.
 
- Exposes ReactAppboy.setTwitterData() and ReactAppboy.setFacebookData() for Twitter and Facebook integration.

- See https://github.com/braze-inc/braze-react-native-sdk/issues/4

##### Changed

- Targets Braze Android SDK version 1.15.3 and Braze iOS SDK version 2.24.2.
 
- Updates the AppboyProject sample application to React Native v0.33.0.
 
- Updates the AppboyProject sample project to integrate session handling and in-app message manager registration using an AppboyLifecycleCallbackListener, as introduced in Braze Android SDK v1.15.0.

##### Removed

- Removes AppboyBroadcastReceiver.java from the AppboyProject sample project, as Braze Android SDK v1.15.0 removes the need for a custom AppboyBroadcastReceiver for Braze push notifications.

## 0.3.0

##### Changed

- Renames Android module to conform to rnpm standard.

## 0.2.0

##### Changed

- Refactors Android module to have the source directly under the android folder.

## 0.1.0

- Initial release. Targets Braze Android SDK version 1.12.0 and Braze iOS SDK Version 1.18.4.

tip

You can also find a copy of the Roku Braze SDK changelog on GitHub.

## 2.2.1

##### Fixed

- Fixed a crash when processing a failed HTTP request for templated in-app messages while the device has intermittent or no connectivity.

## 2.2.0

##### Added

- Added support for new Feature Flag property types by adding getJSONProperty(key), getImageProperty(key), and getTimestampProperty(key) to FeatureFlag.
 
- Added support for adding user alias with m.Braze.addUserAlias(alias, label)
 
- Use SetMessagePort() instead of deprecated SetPort(). Thanks @chrisdp for pointing this out.

## 2.1.0

##### Added

- Added support for sending App Version information to Braze.

## 2.0.0

##### Breaking

- getFeatureFlag will return invalid when the flag does not exist.
 
- BrazeTask now observes BrazeFeatureFlagsUpdated to know when Feature Flags refreshes succeed or fail. Data values may not always be different.

- This will prevent you from being notified on the initial cache load. You can still observe BrazeFeatureFlags if you want to be notified of the cache load.

## 1.0.1

##### Fixed

- Fixed warning that occurs when Feature Flags are not enabled.

## 1.0.0

##### Added

- Support for Feature Flags.

- Get a single feature flag

```

1
2
3
4
5

```
 | 
```
ff = m.braze.getFeatureFlag("theme")
if ff <> invalid and ff.enabled 
 bgcolor = ff.getStringProperty("bgcolor")
 ...
end if

```
 | 

- Get all feature flags.

```

1

```
 | 
```
allFeatureFlags = m.braze.getAllFeatureFlags()

```
 | 

- Be notified when Feature Flags are updated. Data values may not always be different.

```

1

```
 | 
```
m.BrazeTask.ObserveField("BrazeFeatureFlagsUpdated", "onFeatureFlagChanges")

```
 | 

- Refresh feature flags.

```

1

```
 | 
```
m.braze.refreshFeatureFlags()

```
 | 

- If you want to not cache feature flags, you can put the following in your main.brs.

```

1

```
 | 
```
config[config_fields.FF_CACHE_DISABLED] = true

```
 | 

##### Fixed

- Fixed a circular reference between Braze and BrazeTask.

## 0.1.3

##### Fixed

- Fixed an issue where in-app messages might not filter properly on property criteria.
 
- Fixed an issue where very low opacity values would cause colors to have the wrong value.

##### Added

- Added a new sample app (TorchieTV) that more closely mimics the common Roku app.

## 0.1.2

##### Fixed

- Reduced the number of superfluous requests to Braze servers

## 0.1.1

##### Added

- Style data on buttons in In-App messages is now available. See README.md for more information.

##### Changed

- Get In-App Message triggers at the start of session to match other SDKs.

##### Fixed

- Fixed issues with messages that re-evaluate campaign eligibility before displaying.
 
- Fixed issues with users in the control group.
 
- Fixed issue where new session wasn’t started when changing users.

## 0.1.0

##### ⚠️ Known Issues

- This release contains a known issue with in-app message syncing. Do not use this version and upgrade to 0.1.1+ instead.

##### Added

- Added support for receiving In-App Messaging model data.
 
- Added field BrazeTask.BrazeInAppMessage for In-App Messages.
 
- Added LogInAppMessageImpression, LogInAppMessageButtonClick, and LogInAppMessageClick to BrazeSDK.

## 0.0.4

##### Changed

- Replaced the GetModel method with the more precise GetModelDetails().ModelNumber.

##### Fixed

- Replaced the deprecated GetVersion Roku API method with GetOSVersion.

## 0.0.3

##### Fixed

- Fixed the polarity on ad_tracking_enabled sent to Braze via device info.

## 0.0.2

##### Fixed

- Fixed an issue with device Id generation.

## 0.0.1

##### Added

- Initial release.
 
- Supports logging custom events, purchases, setting default and custom user attributes, session tracking, and user identity management.

tip

You can also find a copy of the Unity Braze SDK changelog on GitHub.

## 12.0.0

#### Breaking

- Updated the native iOS bridge from Braze Swift SDK 14.1.0 to 18.0.0.
 
- Updated the native Android bridge from Braze Android SDK 42.2.0 to 43.0.0.

#### Added

- Added support for custom user attributes to be double value.

- AppboyBinding.SetCustomUserAttribute(string key, double value);

## 11.0.0

#### Breaking

- Updated the native iOS bridge from Braze Swift SDK 13.2.0 to 14.1.0.
 
- Updated the native Android bridge from Braze Android SDK 36.0.0 to 42.2.0.

- The minimum required Android SDK version is 23. See more details here.

- Updated the minimum required Unity version to Unity 6 (6000.0.66f2 or later).
 
- Removed News Feed.

- Removed RequestFeedRefresh(), RequestFeedRefreshFromCache(), LogFeedDisplayed(), LogCardImpression(string), LogCardClicked(string).

#### Fixed

- Fixed AppboyBinding.RegisterAppboyPushMessages(string) throwing NoSuchMethodError on Android. See #109.

## 10.0.0

#### Breaking

- Updated the native iOS bridge from Braze Swift SDK 12.0.0 to 13.2.0.

- This includes Xcode 26 support.

## 9.0.0

#### Breaking

- Updated the native Android bridge from Braze Android SDK 35.0.0 to 36.0.0.
 
- Updated the native iOS bridge from Braze Swift SDK 11.9.0 to 12.0.0.

## 8.0.0

##### Breaking

- Updated the native iOS bridge from Braze Swift SDK 10.3.0 to 11.9.0.
 
- Updated the native Android bridge from Braze Android SDK 32.1.0 to 35.0.0.

- The minimum required Android SDK version is 25. See more details here.

##### Fixed

- Fixed a crash on iOS due to the completion handler for silent / background push notification being executed multiple times when Unity was configured to process remote notifications in addition to the Braze plugin (UNITY_USES_REMOTE_NOTIFICATIONS = 1).
 
- Fixed the Push Received Listener getting mistakenly called when a push was opened on iOS. The Push Opened Listener is now properly called instead.

##### Added

- Updated the version of SDWebImage from 5.19.0 to 5.19.7+ when automatically importing via “Braze Configuration”.

## 7.1.0

##### Added

- Updated the native iOS bridge from Braze Swift SDK 10.1.0 to 10.3.0.

## 7.0.0

##### Breaking

- Updated the native Android bridge from Braze Android SDK 30.3.0 to 32.1.0.
 
- Updated the native iOS bridge from Braze Swift SDK 9.0.0 to 10.1.0.

##### Fixed

- Fixed an issue on Android where the AndroidPushReceivedTimestamp of a PushNotification was incorrectly translated from a long to an int. The value received by the C# layer is now the same as the value sent in the JSON.

##### Added

- On the FeatureFlag object, added these APIs to get specific properties:

- featureFlag.GetTimestampProperty(string id) for accessing Int Unix UTC millisecond timestamps as long?s.
 
- featureFlag.GetJSONProperty(string id) for accessing JSON objects as JSONObject? types.
 
- featureFlag.GetImageProperty(string id) for accessing image URLs as string?s.

- Updated the following APIs to use Pascal case and deprecated the previous variant:

- featureFlag.GetStringProperty(string id), replacing getStringProperty
 
- featureFlag.GetIntegerProperty(string id), replacing getIntegerProperty
 
- featureFlag.GetDoubleProperty(string id), replacing getDoubleProperty
 
- featureFlag.GetBooleanProperty(string id), replacing getBooleanProperty

- Added the method AppboyBinding.SetUserLanguage(string) for setting the language user attribute.
 
- Added the method AppboyBinding.SetAdTrackingEnabled(bool adTrackingEnabled, string googleAdvertisingId) to set the adTrackingEnabled flag on iOS and both the adTrackingEnabled flag and the Google Advertising ID on Android.
 
- Added support to modify the allow list for Braze tracking properties via the following C# properties and methods:

- TrackingProperty class
 
- TrackingPropertyAllowList class
 
- AppboyBinding.UpdateTrackingPropertyAllowList(TrackingPropertyAllowList) to modify the allow list for Braze tracking properties.
 
- For details, refer to the Braze iOS Privacy Manifest documentation.

- Added the InAppMessage.IsTestSend property to indicate whether an in-app message was sent as a test send.
 
- Added the method AppboyBinding.HideCurrentInAppMessage() to hide the visible in-app message, if applicable.

## 6.0.0

##### Breaking

- Updated the native iOS bridge from Braze Swift SDK 7.7.0 to 9.0.0.
 
- Updated the native Android bridge from Braze Android SDK 29.0.1 to 30.3.0.

##### Added

- Added iOS In App Message Manager Initial Display Operation configuration setting.

- This setting allows you to configure the initial display operation for in-app messages on iOS. For instance, set it to Display Later to delay the initial display of in-app messages until after your game has finished loading, and use the AppboyBinding.DisplayNextInAppMessage() method to display it when ready.

- Added the Entitlements File Path configuration setting.

- This setting allows you to specify the path to an entitlements file to be used / modified by Braze in the Xcode project.
 
- If left blank, the default entitlements file will be used / created.

## 5.2.1

##### Fixed

- Fixed an issue with calling LogInAppMessageClicked(), LogInAppMessageImpression(), LogInAppMessageButtonClicked, and LogContentCardDismissed(card) on Android.

## 5.2.0

##### Added

- Updated the native iOS bridge from Braze Swift SDK 7.4.0 to 7.7.0.
 
- Updated the version of SDWebImage from 5.15.5 to 5.19.0 when automatically importing via “Braze Configuration”.

- This version of SDWebImage contains a Privacy Manifest file. See Apple’s documentation for more information.

## 5.1.0

##### Added

- Added support for custom user attributes to be nested objects.

- AppboyBinding.SetCustomUserAttribute(string, Dictionary<string, object>);
 
- AppboyBinding.SetCustomUserAttribute(string, List<Dictionary<string, object>>);
 
- You can specify that the Dictionary be merged with the existing value.

- AppboyBinding.SetCustomUserAttribute(string, Dictionary<string, object>, bool merge);

- See https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/ for more information.

- Added AppboyBinding.LogFeatureFlagImpression(string id) to log a Feature Flag impression.

## 5.0.0

#### Breaking

- Updated the native iOS bridge from Braze Swift SDK 6.1.0 to 7.4.0.

- The iOS repository link now points to the prebuilt dynamic XCFrameworks from this repo: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic.

- Updated the native Android bridge from Braze Android SDK 27.0.1 to 29.0.1.
 
- AppboyBinding.GetFeatureFlag(string id) will now return null if the Feature Flag does not exist.
 
- FEATURE_FLAGS_UPDATED will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.

##### Fixed

- Fixed an issue introduced in 4.0.0 which prevented compilation on Xcode 14.3+.

- The additional -fcxx-modules flag under “Other C++ Flags” has been removed from the build process.
 
- The dependencies BrazeKit and BrazeUI now get directly linked to the main app’s target, instead of being transitively linked via UnityFramework.

- Changed the iOS plugin to automatically update up to the next minor version, instead of up to the next major version.

## 4.3.0

Starting with this release, this SDK will use Semantic Versioning.

##### Added

- Updated the Android plugin to use Braze Android SDK 27.0.1.

## 4.2.0

#### Breaking

- Updated the Android plugin to use Braze Android SDK 26.2.0.

##### Fixed

- Fixed an issue on Android where In-App Message events would not properly get forwarded to the Unity layer.

## 4.1.1

##### Fixed

- Fixed the Braze iOS Push settings not being applied in the sample app code.

## 4.1.0

##### Added

- Added support for Feature Flags.

- AppboyBinding.GetFeatureFlag(string id) - Get a single Feature Flag.
 
- AppboyBinding.GetAllFeatureFlags() - Get all Feature Flags.
 
- AppboyBinding.RefreshFeatureFlags() - Request a refresh of Feature Flags.

- Adds the ability to subscribe to Feature Flag updates.

- Set the values for Game Object Name and Callback Method Name under “Braze Configuration” > “Feature Flags” to the corresponding values in your application.

- On FeatureFlag object, adds these APIs to get specific properties:

- featureFlag.getStringProperty(string id)
 
- featureFlag.getIntegerProperty(string id)
 
- featureFlag.getDoubleProperty(string id)
 
- featureFlag.getBooleanProperty(string id)

- Updated the iOS plugin to use the Braze Swift SDK 6.1.0.

## 4.0.0

#### Breaking

- Updated the Android plugin to use Braze Android SDK 25.0.0

- Update com.appboy.unity.AppboyUnityPlayerActivity references to com.braze.unity.BrazeUnityPlayerActivity.

- Updates the native iOS bridge to use the new Swift SDK version 6.0.0.

- Replace any instances of #import <Appboy_iOS_SDK/AppboyKit.h> in your iOS native code with:

```

1
2

```
 | 
```
@import BrazeKit;
@import BrazeUI; // Only needed if you use the UI in the file

```
 | 

- Replace the prefix ABK with BRZ for any of the constants found in AppboyUnityManager.h.
 
- Update your AppDelegate file with the code snippet below. Reference our sample code here.

```

1
2

```
 | 
```
BRZConfiguration *config = [[BRZConfiguration alloc] init];
Braze *braze = [AppboyUnityManager initBraze:config];

```
 | 

- This migration requires re-identifying users. To do so, you must call the changeUser method on the Braze instance for non-anonymous users. You can read more about it here.
 
- Reference this Migration Guide and this documentation for additional context around specific migration / integration steps.

- Requires Unity version 2020.3.42 or newer.
 
- The following changes have been made to AppboyUnityManager.h:

- Renames addInAppMessageListenerWithObjectNameAndSetDelegate:callbackMethodName: to addInAppMessageListenerWithObjectName:callbackMethodName:.
 
- Renames ABKUnityMessageType to BRZUnityMessageType.
 
- Removes parsePlist since it is implemented as a part of initBraze:.

- Removes setFacebookData and setTwitterData from AppboyBinding.cs.
 
- Removes the release asset Appboy-nodeps.unitypackage in favor of using the “Braze Configuration” option mentioned below.

##### Added

- Adds a configuration option under “Braze Configuration” which allows you to toggle between importing SDWebImage into your iOS application.

- If checked, the build process will automatically add SDWebImage version 5.15.5 to your project. If unchecked, it will be omitted.

## 3.11.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 23.3.0.
 
- Streamlined the integration required for handling push notifications on Android.

- References to AppboyUnityPushBroadcastReceiver must be removed from your AndroidManifest.xml file.
 
- Removed binding.FlushAndroidPendingPushIntents().

## 3.10.0

##### Fixed

- Removed AppboyBinding.LogContentCardsDisplayed().

## 3.9.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 23.1.0.
 
- Added the ability to request push notification permissions on Android 13+ devices via Appboy.AppboyBinding.PromptUserForPushPermissions(false).

- Either true or false result in the push prompt being shown, on Android. The parameter is unused.

##### Fixed

- Fixed an issue where AppboyBinding.logPurchase() calls could fail on Android based on the device locale.

## 3.8.1

##### Added

- Added Assembly Definitions for the SDK.

- See the Unity Asm Def docs for more information.
 
- Special thanks to @starikcetin!

## 3.8.0

##### Breaking

- Removed AppboyBinding.SetUserAvatarImageURL() from the binding.
 
- Utilities/MiniJson.cs now uses InvariantCulture during serialization.
 
- Updated the Android plugin to use Braze Android SDK 21.0.0

- This SDK version relies on implementation "androidx.recyclerview:recyclerview:1.2.1 or higher.

##### Added

- Added AppboyBinding.SetUserLastKnownLocation() to manually set the last known location for the user.
 
- Added SDK Authentication Support.

- Added AppboyBinding.SetSdkAuthenticationSignature(sdkAuthSignature) to set the signature only.
 
- Added AppboyBinding.ChangeUser(userId, sdkAuthSignature = null) to optionally set the SDK Authentication signature when changing users.
 
- Added SDK Authentication under “Braze Configuration”. There are separate configurations for iOS and Android. If you want to configure at runtime, use:

- AppboyBinding.IOSSdkAuthenticationFailureGameObjectName, AppboyBinding.IOSSdkAuthenticationEnabled, and AppboyBinding.IOSSdkAuthenticationFailureCallbackMethodName for iOS.
 
- AppboyBinding.AndroidSdkAuthenticationEnabled, AppboyBinding.AndroidSdkAuthenticationFailureGameObjectName, and AppboyBinding.AndroidSdkAuthenticationFailureCallbackMethodName for Android.

##### Changed

- Updated the iOS plugin to use Braze iOS SDK 4.4.3.

## 3.7.1

##### Changed

- Updated the Android plugin to use Braze Android SDK 18.0.1.

## 3.7.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 18.0.0.

- This SDK version requires a dependency on Kotlin coroutines. This can be added to your mainTemplate.gradle file via implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2"

##### Fixed

- Fixed an issue where AppboyUnityPlayerActivity could not be extended on Android.

## 3.6.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 16.0.0.

- This SDK version requires a dependency on Kotlin. This can be added to your mainTemplate.gradle file via implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"
 
- This SDK version has removed a dependency on the appcompat library.

##### Added

- Added AppboyBinding.AddToSubscriptionGroup() and AppboyBinding.RemoveFromSubscriptionGroup() to the binding.
 
- Added the DisplayNextInAppMessage() method, available on both iOS and Android.
 
- Added the ability to receive in-app messages UI events via AppboyBinding.inAppMessageListener. See BrazeInAppMessageListener for more information.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 4.3.3.
 
- Removed the iOS specific method DisplayNextInAppMessage(bool withDelegate).

## 3.5.1

##### Fixed

- Fixed an issue where simulator architectures were included in the iOS framework.

## 3.5.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 15.0.0.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 4.3.2.

## 3.4.0

##### Added

- Added the ability to change the display flow of In-App Messages directly from Unity code via AppboyBinding.SetInAppMessageDisplayAction().

- See the BrazeUnityInAppMessageDisplayActionType enum.

- Added the ability to open the default Content Cards UI via DisplayContentCards() on the binding.

- For Android, this requires the following dependencies:

```

1
2

```
 | 
```
implementation "androidx.swiperefreshlayout:swiperefreshlayout:+"
implementation "androidx.recyclerview:recyclerview:+"

```
 | 

## 3.3.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 14.0.0.

##### Added

- Added the ability to delay sending Android push notification data to the Unity layer until the native libraries have finished loading and any AppboyBinding method has been called.

- Configured under “Braze Configuration -> Automate Unity Android Integration -> Push Configuration -> Delay Sending Push Notification Intents”.
 
- Pending Android push notification intents are flushed automatically after the first call to any method on the Android binding is made.
 
- To optionally have finer control over when these push notification intents are flushed, call the following from Unity:

```

1
2
3
4

```
 | 
```
#if UNITY_ANDROID
BrazeAndroidPlatform binding = (BrazeAndroidPlatform) Appboy.AppboyBinding.mBinding;
binding.FlushAndroidPendingPushIntents();
#endif

```
 | 

## 3.2.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 14.0.0.1.

##### Fixed

- Fixed an issue introduced in 3.1.0 on Android where push opens could fail to launch the application on certain devices.
 
- Fixed an issue introduced in 3.0.0 in the iOS binding where enableSDK() and disableSDK() had swapped behaviors.

## 3.1.0

Important: This release has known issues with push notifications on Android. This is fixed in version 3.2.0.

##### Changed

- Updated the Android plugin to use Braze Android SDK 13.1.2.

## 3.0.0

##### Important

- This release contains several minor changes to our iOS push code. Most integrations will be unaffected, however, we recommend additional testing.

##### Breaking

- Updated the Android plugin to use Braze Android SDK 13.0.0.
 
- If automatic iOS push integration is enabled, Braze will now automatically add the Xcode Push Capability in OnPostprocessBuild().

- To disable this, check “Disable Automatic Push Capability” in the Braze configuration editor.

- In AppboyUnityManager.mm:

- registerForRemoteNotifications: has been replaced with registerForRemoteNotificationsWithProvisional:(BOOL)provisional. If using this method, note that the new method calls Apple’s APIs directly and does not respect Braze configuration’s settings for automatic push integration and registration.
 
- registerApplication:didReceiveRemoteNotification:fetchCompletionHandler: and registerPushToken have also been updated to no longer internally read Braze config.
 
- Several obsolete methods were removed, including methods where the manager trivially wrapped the native Appboy instance.
 
- Most integrations will not be affected by these changes.

##### Added

- Added the option to disable iOS provisional push authorization when automatic iOS push integration is enabled.

- To use, check “Disable Provisional Authorization” in the Braze configuration editor.
 
- When provisional push authorization is disabled, users will see the native push prompt dialog at app startup.

- Added AppboyBinding.ConfigureListener() as an alternative method for configuring GameObject listeners for push, in-app messages, Content Cards, and News Feed. Use the new BrazeUnityMessageType enum to specify the desired message type.

- On iOS, to receive push opened and received callbacks, Integrate Push With Braze must be enabled.

- Added AppboyBinding.PromptUserForPushPermissions(bool provisional) to request authorization and register for push notifications on iOS.

- Set provisional to true to request provisional authorization, or false to show the push prompt directly.
 
- If you would like to read the user response, pass an instance of PushPromptResponseReceived into the method.
 
- We recommend using this method with the following settings:

- Integrate Push With Braze enabled.
 
- Disable Automatic Push Registration enabled.

- Added AppboyBinding.SetPushTokenReceivedFromSystemDelegate() to receive push tokens Braze receives from the OS (iOS only).

##### Fixed

- Braze push delegates are no longer called automatically in fully manual integrations.

- Automatic push integration must be enabled for Braze push delegates to function.

## 2.8.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 12.0.0.
 
- Updated the native iOS bridge to Braze iOS SDK 3.31.2.

##### Added

- Added AppboyBinding.AddAlias() to the binding.

## 2.7.1

##### Fixed

- Fixed an issue where the return type for the Android implementation of setIsDismissed in AppboyBinding was incorrectly set to bool.
 
- Removed a deprecated usage of PBXProject.GetUnityTargetName().

## 2.7.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.29.1.
 
- Updated the Android plugin to use Braze Android SDK 11.0.0.

##### Fixed

- Fixed a metadata issue for Android artifacts.

## 2.6.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 10.0.0.

- Note that this SDK release internally uses AndroidX depdendences. See the linked SDK changelog entry for more information.
 
- All “jetified” packages are removed since the android artifacts are now fully on AndroidX.

- Removed PushNotification.cs#CollapseKey.

##### Changed

- Added PushNotification.cs#RawJsonString, PushNotification.cs#AndroidPushReceivedTimestamp.

##### Added

- Added Braze configuration option for Android to toggle automatically displaying In-App Messages.

##### Fixed

- Fixed push notification parsing for Android in PushNotification.cs.
 
- Fixed use of outdated UNITY_IPHONE directive in Card.cs.

## 2.5.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.27.0. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.

## 2.4.0

##### Changed

- Updated the Android plugin to use Braze Android SDK 8.1.0.
 
- Updated the native iOS bridge to Braze iOS SDK 3.26.1.

##### Fixed

- Fixed return type of AppboyBinding.RegisterAppboyPushMessages() for iOS to be void.
 
- Fixed the automatic config for Android push icons to correctly used drawable instead of string.

## 2.3.0

##### Changed

- Updated the Android plugin to use Braze Android SDK 8.0.1.
 
- Updated the native iOS bridge to Braze iOS SDK 3.25.0.

##### Added

- Added functionality to apps using the UserNotification framework to forward via UnitySendMessage push notification opens to game object methods on iOS.

## 2.2.2

##### Added

- Added a method for manually providing a push registration token via AppboyBinding.RegisterAppboyPushMessages() for iOS.

- Note that the Android implementation accepts string.
 
- The iOS implementation accepts byte[].

##### Fixed

- Fixed an issue which caused the extras dictionary to not be populated in JSON push payloads sent by the SDK to Unity listeners.

## 2.2.1

##### Added

- Added an implementation for AppboyBinding.GetInstallTrackingId() for iOS.

##### Changed

- Updated the Android plugin to use Braze Android SDK 7.0.0.

## 2.1.0

##### ⚠ Breaking

- Removes the unused CrossPromotionSmall.cs News Feed model.

##### Added

- Added the ability to automatically integrate Unity builds on Android in the ‘Braze Configuration’ window. Using this option obviates the need for a manually created appboy.xml file to configure Android apps.

- If enabled, an autogenerated config file will be generated at /unity-android-resources/res/values/appboy-generated.xml in your temp gradle out directory. If disabled, this auto-generated file will be deleted.
 
- If already using an appboy.xml file, the values from that configuration should be transferred in order to prevent build resource XML conflicts.

- Added AppboyBinding.LogContentCardDismissed() to log a Content Card dismissal.
 
- Added Other, Unknown, Not Applicable, and Prefer not to Say options for user gender.
 
- Added the ability to set the endpoint for iOS via the automatic config window Braze Configuration.
 
- Added support for UserNotifications Framework on iOS for push.

##### Changed

- Updated the Android plugin to use Braze Android SDK 6.0.0.
 
- Removed root level Libraries folder. Now, iOS frameworks exclusively exist under Assets/Plugins/iOS/.

## 2.0.0

##### ⚠ Breaking

- The structure of the Android plugin (i.e. found under Assets/Plugins/Android/) has been changed to only include AAR artifacts. All other folders have been removed.

- Additionally, depending on the .unitypackage chosen, you can import jetified Braze AAR artifacts. These artifacts were transformed using the jetifier tool to be compatible with androidX support libraries instead of the v4 support libraries. This is particularly relevant if you wish to update your unity firebase messaging dependencies to the latest versions, which use and require androidX support libraries. Please see our documentation for more information.

##### Added

- Added AppboyBinding.RequestImmediateDataFlush() to immediately request a data flush.
 
- Added AppboyBinding.RequestGeofences(latitude, longitude) to manually request Braze Geofences.
 
- Adds an option to disable automatic geofence requests on session start. Note that this is required in order to manually request geofences.

- iOS - You can do this in the plist by adding the Appboy dictionary to your Info.plist file. Inside the Appboy dictionary, add the DisableAutomaticGeofenceRequests boolean subentry and set the value to YES.
 
- Android - You can do this by configuring the boolean value for com_appboy_automatic_geofence_requests_enabled to false in your appboy.xml.

##### Changed

- Updated the Android plugin to use Braze Android SDK 5.0.0.
 
- Updated the native iOS bridge to Braze iOS SDK 3.21.3.

## 1.22.0

##### Added

- Added the ability to receive Content Cards data within a Unity Game Object or method in C#.

- On Android, set com_appboy_content_cards_updated_listener_game_object_name and com_appboy_content_cards_updated_listener_callback_method_name in your appboy.xml to set your Game Object and Callback Method for receiving Content Cards updates.
 
- On iOS, set ContentCardsCallbackMethodName and ContentCardsGameObjectName inside of a dictionary named Unity set inside a dictionary named Appboy within your Info.plist. Alternatively, use the configuration UI under the Braze menu added when integrating the Braze Unity package.
 
- Our Callback example class contains an example of parsing the received Content Cards json as well as using our provided convenience model class, ContentCard.cs to wrap the data and log analytics. Currently, ContentCard.cs supports logging clicks and impressions.

## 1.21.2

Important: This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the Braze iOS SDK Changelog for more information.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.2.

## 1.21.1

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.21.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.21.2 or above if you make use of HTML in-app messages.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.1.

## 1.21.0

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.21.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.21.2 or above if you make use of HTML in-app messages.

##### Breaking

- Updated the iOS plugin to use Braze iOS SDK 3.20.0.
 
- Important: Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In application:didRegisterForRemoteNotificationsWithDeviceToken:, replace

```

1
2

```
 | 
```
[[Appboy sharedInstance] registerPushToken:
 [NSString stringWithFormat:@"%@", deviceToken]];

```
 | 
 
with

```

1

```
 | 
```
[[Appboy sharedInstance] registerDeviceToken:deviceToken]];

```
 | 

- Updated the Android plugin to use Braze Android SDK 3.7.0.
 
- Note: This Braze Unity SDK release updates to a Braze Android SDK dependency which no longer enables automatic Braze location collection by default. Please consult the changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.
 
- Removes the Feedback feature and all associated methods, classes, and interfaces.

## 1.20.0

##### Breaking

- Updated the iOS plugin to use Braze iOS SDK 3.18.0.
 
- Note: This Braze Unity SDK release updates to a Braze iOS SDK dependency which no longer enables automatic Braze location collection by default. Please consult the changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.

##### Added

- Added RequestLocationInitialization to the Appboy interface for requesting Braze geofences and a single location update.

## 1.19.0

##### Breaking

- Updated the iOS plugin to use Braze iOS SDK 3.16.0.

## 1.18.0

##### Breaking

- Updated the iOS plugin to use Braze iOS SDK 3.14.0.

## 1.17.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 3.2.1.

- Added AppboyFirebaseMessagingService to directly use the Firebase messaging event com.google.firebase.MESSAGING_EVENT. This is now the recommended way to integrate Firebase push with Braze. The AppboyFcmReceiver should be removed from your AndroidManifest and replaced with the following:

```

1
2
3
4
5

```
 | 
```
<service android:name="com.appboy.AppboyFirebaseMessagingService">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT" />
 </intent-filter>
</service>

```
 | 

- Also note that any c2dm related permissions should be removed from your manifest as Braze does not require any extra permissions for AppboyFirebaseMessagingService to work correctly.

## 1.16.0

##### Breaking

- Updated the iOS plugin to use Braze iOS SDK 3.11.0.
 
- Updated the Android plugin to use Braze Android SDK 3.1.0.

##### Fixed

- Fixed an issue where the binding would cache the Appboy singleton instance.
 
- Fixed Card.cs to always return CardCategory.NO_CATEGORY in all cases where no valid categories are found.

- See https://github.com/Appboy/appboy-unity-sdk/pull/43. Thanks @Sencerd!

##### Changed

- Updated the Appboy configuration editor to use Braze branding.
 
- By default, native in-app messages on Android no longer show the status bar.

## 1.15.0

##### Breaking

- Updated the Android plugin to use Braze Android SDK 2.7.0.

- Important: Note that in Braze Android SDK 2.7.0, AppboyGcmReceiver was renamed to AppboyFcmReceiver. This receiver is intended to be used for Firebase integrations. Please update the AppboyGcmReceiver declaration in your AndroidManifest.xml to reference AppboyFcmReceiver and remove the com.google.android.c2dm.intent.REGISTRATION intent filter action.

##### Added

- Added SetAttributionData to the Appboy interface.

## 1.14.0

##### Breaking

- Updated the iOS plugin to use Braze iOS SDK 3.7.1.

- Updated the iOS plugin to use the Braze iOS SDK framework instead of local files.
 
- As a result, imports using local file syntax (e.g. "AppboyKit.h") must change to framework (e.g.<Appboy_iOS_SDK/AppboyKit.h>) syntax.

- Updates the Android plugin to use Braze Android SDK 2.6.0.
 
- Removes Android Support Library artifacts from the Braze Unity Plugin. This is to avoid duplicating the Android Support Library artifacts that are automatically included as part of the Firebase Unity SDK, our recommended push integration. Integrators not using Firebase or importing Android Support Library artifacts through another SDK must include the Android Support Library manually (v4 only).

##### Fixed

- Fixed an issue that required manual import of non-xib Braze iOS SDK resources into Unity-generated Xcode projects.

##### Added

- Added GetInstallTrackingId to the Appboy interface. This method is currently only implemented on Android and is a no-op on iOS.
 
- Updated the Unity Samples sample app to use FCM instead of GCM.

##### Changed

- In-app message analytics events on the Appboy interface no longer require using an Appboy Unity player subclass.

- See https://github.com/Appboy/appboy-unity-sdk/pull/38/files. Thanks @MartinGonzalez!

##### Removed

- Removes showStreamView: from the AppboyUnityManager.h interface.

## 1.13.0

##### Breaking

- Updates the iOS plugin to use Braze iOS SDK 3.4.0.
 
- Updates the Android plugin to use Braze Android SDK 2.3.0.
 
- Removes Windows support.
 
- Removes LogSlideupImpression and LogSlideupClicked from the Appboy interface.

##### Added

- PostBuild.cs now adds SDWebImage and FLAnimatedImage to XCode embedded binaries automatically.

- See https://github.com/Appboy/appboy-unity-sdk/pull/35. Thanks @nlattessi!

- PostBuild.cs may now run in Unity environments without Unity iOS Build Support.

- See https://github.com/Appboy/appboy-unity-sdk/pull/36. Thanks @Sencerd!

- Added support for wiping all customer data created by the Braze SDK via Appboy.AppboyBinding.wipeData().

- Note that on iOS, wipeData() will disable the SDK for the remainder of the app run. For more information, see our iOS SDK’s documentation for disableSDK.

- Added Appboy.AppboyBinding.disableSDK() to disable the Braze SDK immediately.
 
- Added Appboy.AppboyBinding.enableSDK() to re-enable the SDK after a call to Appboy.AppboyBinding.disableSDK().

- Note that on iOS, enableSDK() will not enable the SDK immediately. For more information, see our iOS SDK’s documentation for requestEnableSDKOnNextAppRun.

## 1.12.0

##### Breaking

- Updates the iOS plugin to use Braze iOS SDK 3.3.1.
 
- Updates the Android plugin to use Braze Android SDK 2.2.2.
 
- Removes methods RequestInAppMessage and RequestSlideup as they are removed in the Braze native SDKs.

## 1.11.0

##### Breaking

- Updates the iOS plugin to use Braze iOS SDK 2.29.0, which drops support for iOS 7.
 
- Updates the Android plugin to use Braze Android SDK 2.0.0.
 
- Removes methods SetUserIsSubscribedToEmails and SetUserBio as they are removed in the Braze native SDKs.

## 1.10.0

##### Breaking

- Updates the Android plugin to use Braze Android SDK 1.18.0.
 
- Updates the iOS plugin to use Braze iOS SDK 2.25.0.

##### Added

- Adds a new method DisplayNextInAppMessage(bool withDelegate) in iOS plugin to display next in-app message from the in-app message stack, if there is one.

- When the withDelegate is false, the in-app message will be displayed in Braze’s default UI. Otherwise, it will follow the normal in-app message displaying path by going through the - (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp in AppboyUnityManager.m.

- Updates the SDK to be compatible with Unity 5.5+.

## 1.9.0

##### Breaking

- Updates the SDK to require XCode 8.
 
- Updates the iOS plugin to use Braze iOS SDK 2.24.0, which supports iOS 10 and has the new in-app message V2 feature. The new in-app message V2 feature includes new in-app message UI change, event property trigger and templated in-app message.
 
- Updates the Android plugin to use Braze Android SDK 1.15.0 with the new triggered in-app message feature.

## 1.8.2

##### Added

- Updates the SDK to be compatible with Unity 5.4+. In 5.4.0 Unity stopped implementing push delegates in UnityAppController in certain conditions, causing a crash when the Braze SDK tried to call them.

## 1.8.1

##### Fixed

- Updates SDK to modify delegate usage to fix an issue with push-click handling introduced in iOS 10 - see https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md for details.

## 1.8.0

##### Breaking

- Updates the iOS plugin to use Braze iOS SDK 2.21.0, which drops support for iOS 6.
 
- Updates the Android plugin to use Braze Android SDK 1.13.5.
 
- Drops support for Windows Phone 8.

##### Added

- Adds support for passing triggered in-app messages to Unity.
 
- Bundles the Android and iOS plugins, along with Braze’s native Unity functionality, as a Unity package.
 
- Adds a native Unity solution for automating the iOS SDK integration.
 
- Adds object handling for custom event and purchase properties.
 
- Exposes the extras on the News Feed Card model in Unity.
 
- Updates the Unity sample project to Unity v.5.3.5.

## 1.7.0

##### Breaking

- Updates the Android plugin to use Braze Android SDK 1.13.2.
 
- Updates the iOS plugin to use Braze iOS SDK 2.19.1.

##### Added

- Adds binding methods for setting user’s Facebook and Twitter data (Android/iOS).
 
- Adds binding method to set the GCM registrationId (Android).
 
- Adds overloads to the binding methods for logCustomEvent and logPurchase that include properties (Android/iOS).

## 1.6.0

##### Breaking

- Updates the Android plugin to use Braze Android SDK 1.11.0.
 
- Updates the iOS plugin to use Braze iOS SDK 2.17.0.

## 1.5.0

##### Breaking

- Removes Unity 4 support. Unity 5 or higher is required to use this and future versions of the Braze Unity SDK. Unity 4 users may integrate Braze Unity SDK release 1.4.0, which includes analytics and push functionality but does not include native in-app messages on Android; however, upgrading to Unity 5 and using the latest Braze Unity SDK is recommended.
 
- Removes Froyo support, which was dropped in Unity 4.3. See https://unity3d.com/unity/whats-new/unity-4.3.
 
- Updates the iOS plugin to use Braze iOS SDK 2.12.1.
 
- Updates the Android plugin to use Braze Android SDK 1.8.0.

##### Added

- Adds native Braze ui capability to Android, including in-app messages, the News Feed, and Braze’s webview. Note: As a result of this change, in-app messages will display automatically with native Braze layouts. To disable this functionality, set com_appboy_inapp_show_inapp_messages_automatically to false in your Unity project’s appboy.xml file.

## 1.4.0

##### Breaking

- Updates the iOS plugin to use Braze iOS SDK 2.11.2.
 
- Updates the Android plugin to use Braze Android SDK 1.7.2.

##### Added

- Adds a sample Unity application that uses the Braze plugin.
 
- Adds new in-app message models for the Modal and Full screen types added in Android 1.7 and iOS 2.11.

## 1.3.1

##### Breaking

- Updates the Android plugin to use Braze Android SDK 1.6.1.

## 1.3.0

##### Breaking

- Updates the Android plugin to use Braze Android SDK 1.6.0.
 
- Updates the iOS plugin to use Braze iOS SDK 2.9.3.

##### Added

- Adds plugins for Windows Phone 8 and Windows Universal apps.

##### Fixed

- Fixes the corrupted support-v4 jar in the Android plugin.

## 1.2.2

##### Breaking

- Updates the Android plugin to use Braze Android SDK 1.5.2.

##### Added

- Adds logFeedDisplayed, logFeedbackDisplayed, SetUserAvatarImageURL, IncrementCustomUserAttribute; updates email and push notification subscription types to current options supported in the Android and iOS SDKs (OPTED_IN, SUBSCRIBED, or UNSUBSCRIBED).

## 1.2.1

##### Breaking

- Updates the plugin libraries to Braze Android SDK 1.5.1 and Braze iOS SDK 2.9.1 (without Facebook iOS SDK Support).

##### Added

- Adds quantity parameter as an option when logging purchase. The quantity should be an unsigned interger greater than 0 and no larger than 100.
 
- New Custom Attribute Data Type (Array): Braze now supports custom attributes which contain an array of string elements. In addition, we also provide methods for adding or removing an string element from an array type custom attribute.

## 1.2

##### Breaking

- Updates the plugin libraries to Braze Android SDK 1.4.3 and Braze iOS SDK 2.8 (without Facebook iOS SDK Support).

##### Added

- Adds SlideFrom, ClickAction, DismissType and Uri to Slideup; added logging slideup impressions and clicks.
 
- Exposes the card models from Braze to Unity; adds methods for requesting feed from Braze server or cache; adds logging impressions and clicks.

##### Changed

- In Android SDK, changes the device identifier from the device persistent ANDROID_ID to a non device persistent identifier for compliance with the new Google Play Terms of Service.

## 1.1

##### Breaking

- Updates the plugin libraries to Braze Android SDK 1.2.1 and Braze iOS SDK 2.3.1 (without Facebook iOS SDK Support).

##### Added

- Adds Prime31 plugin compatibility.

## 1.0

##### Added

- Initial release

tip

You can also find a copy of the .NET MAUI Braze SDK changelog on GitHub.

## 10.0.0

##### Breaking

- Updated the Android binding from Braze Android SDK 41.0.0 to 43.1.1.

- Xamarin.KotlinX.Coroutines.Android has been updated from 1.9.0.3 to 1.11.0.1.
 
- Xamarin.Kotlin.StdLib has been updated from 2.3.0.1 to 2.4.0.1. If your project explicitly pins this package to an older version, you will need to update it to avoid restore errors.

- Updated the iOS binding from Braze Swift SDK 14.0.1 to 18.2.0.

- Braze initialization and ChangeUser no longer block the calling thread. Prefer the asynchronous identifier getters (GetIdWithCompletion, GetDeviceIdWithCompletion) on the main thread.
 
- All public symbols in BrazeKitCompat and BrazeUICompat are deprecated in the native Swift SDK and will be removed in a future major release. Use BrazeKit and BrazeUI instead.

##### Fixed

- Fixed System.InvalidCastException when reading Card.Extras on Android.

## 9.0.0

##### Breaking

- Updated the Android binding from Braze Android SDK 37.0.0 to 41.0.0.
 
- Updated the iOS binding from Braze Swift SDK 13.3.0 to 14.0.1.
 
- Added new transitive NuGet dependencies required by the Braze Android SDK:

- Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
 
- Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
 
- Xamarin.Kotlin.StdLib has been updated from 2.0.21.3 to 2.3.0.1. If your project explicitly pins this package to an older version, you will need to update it to avoid restore errors.

- Removed the News Feed feature.

- This feature was removed from the native Android SDK in version 38.0.0.
 
- This feature was removed from the native Swift SDK in version 14.0.0.

- The BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData enum case has been renamed to BRZInAppMessageDismissalReason.WipeData.

##### Added

- Added BrazePlatform.BrazeAndroidLocationBinding, which introduces support for location services and geofences on Android.

- This package is available here on Nuget.

## 8.0.0

##### Breaking

- Updated the iOS binding from Braze Swift SDK 12.1.0 to 13.3.0.

- This includes Xcode 26 support.

## 7.0.0

##### Breaking

- Added support for .NET 9.0 for the iOS and Android bindings.

- This removes support for .NET 8.0.
 
- This requires a minimum version of iOS 12.2.

- Updated the Android binding from Braze Android 32.0.0 to 37.0.0.
 
- Updated the iOS binding from Braze Swift SDK 10.0.0 to 12.1.0.

NOTE: This release contains APIs for the Banners feature but is not currently fully supported by this SDK. If you wish to use Banners in your .NET MAUI app, please contact your Customer Support Manager before integrating into your application.

## 6.0.0

##### Breaking

- Added support for .NET 8.0 for the iOS and Android bindings as .NET 7.0 has reached end of life support.

- This removes support for .NET 7.0.

- Updated the Android binding from Braze Android 30.4.0 to 32.0.0.
 
- Updated the iOS binding from Braze Swift SDK 9.0.0 to 10.0.0.

- When subscribing to push notification events, the subscription will be triggered on iOS for both “Push Received” and “Push Opened”, instead of only for “Push Opened” events.

##### Fixed

- Removed the files under the Modules directories in the XCFrameworks to reduce the final size of the distributed application.

## 5.0.0

##### Breaking

- Updated the iOS binding from Braze Swift SDK 8.4.0 to 9.0.0.

## 4.0.3

##### Added

- Updated the Android binding from Braze Android 30.1.0 to 30.4.0.
 
- Updated the iOS binding from Braze Swift SDK 8.0.1 to 8.4.0.

## 4.0.2

##### Added

- Updated the Android binding from Braze Android SDK 29.0.1 to 30.1.0.
 
- Updated the iOS binding from Braze Swift SDK 7.6.0 to 8.0.1.

## 4.0.1

##### Fixed

- Corrected the incorrect dependency versions in the nuspecs of recent iOS libraries.

## 4.0.0

##### Breaking

- This version updates the iOS binding to use the Braze Swift SDK. Most iOS public APIs have changed, please refer to our migration guide (Swift) for guidance about replacement to use. We provide compatibility bindings to keep making use of the old public APIs.

- The iOS binding is now composed of multiple modules:

- BrazeKit: Main SDK library providing support for analytics and push notifications (nuget: Braze.iOS.BrazeKit).
 
- BrazeUI: Braze-provided user interface library for In-App Messages and Content Cards (nuget: Braze.iOS.BrazeUI).
 
- BrazeLocation: Location library providing support for location analytics and geofence monitoring (nuget: Braze.iOS.BrazeLocation).
 
- BrazeKitCompat: Compatibility library with support for pre-4.0.0 APIs (nuget: Braze.iOS.BrazeKitCompat).
 
- BrazeUICompat: Compatibility library with support for pre-4.0.0 UI APIs (nuget: Braze.iOS.BrazeUICompat).

- This migration requires re-identifying users. To do so, you must call the changeUser method on the Braze instance for non-anonymous users. You can read more about it here.
 
- Refer to the BrazeiOSMauiSampleApp for the new integration, and to BrazeiOSMauiCompatSampleApp for usage of the compatibility modules.

- Updated the iOS binding to the Braze Swift SDK 7.6.0
 
- The iOS binding requires using .NET 7 for compatibility with Xcode 15.

## 3.0.0

##### Breaking

- The NuGet package has been renamed from AppboyPlatformXamariniOSBinding to BrazePlatform.BrazeiOSBinding.

- To use the updated package, replace any instances of using AppboyPlatformXamariniOSBinding; with:

```

1

```
 | 
```
using Braze;

```
 | 

- This version requires using .NET 6+ and removes support for projects using the Xamarin framework. See Microsoft’s policy around the end of support for Xamarin.
 
- Updated the Android binding from Braze Android SDK 26.3.2 to 29.0.1.

##### Fixed

- Fixed an issue where some Android set methods were being hidden by the Xamarin framework.

##### Added

- Added support for .NET 6 (or newer) and support for projects using .NET MAUI.

- For a reference iOS implementation, see BrazeiOSMauiSampleApp.sln.

- Updated the iOS binding from Braze iOS SDK 4.4.1 to 4.6.0.

- The underlying iOS assets have been updated to use XCFrameworks:

- Appboy_iOS_SDK.framework -> Appboy_iOS_SDK.xcframework
 
- SDWebImage.framework -> SDWebImage.xcframework

## 2.0.1

##### Fixed

- Updated the Android binding to use Braze Android SDK 26.3.2.

## 2.0.0

Starting with this release, this SDK will use Semantic Versioning.

##### Breaking

- Updated the Android binding to use Braze Android SDK 26.3.0.

## 1.27.0

##### Added

- Added BrazePlatform.BrazeAndroidBinding which introduces .NET 6+ framework support for MAUI.

- This package is available here on Nuget.

- Updated the Android binding to use Braze Android SDK 24.2.0.

## 1.26.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 23.3.0.

## 1.25.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 21.0.0.

## 1.24.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 19.0.0.

## 1.23.0

##### Breaking

- Updated the iOS binding to use Braze iOS SDK 4.4.1.

- Added AddToSubscriptionGroupWithGroupId and RemoveFromSubscriptionGroupWithGroupId to ABKUser.

- Updated the Android binding to use Braze Android SDK 18.0.1.

- This introduces a hard dependency on Xamarin.Kotlin.StdLib in your package references.
 
- This introduces a hard dependency on Xamarin.KotlinX.Coroutines.Android in your package references.

## 1.21.1

##### Changed

- Updated the iOS binding to use Braze iOS SDK 4.3.2.

## 1.21.0

##### Breaking

- Updated the iOS binding to use Braze iOS SDK 4.3.1.

- This includes several breaking changes in the binding, and integrators should test before releasing. Please read the Braze iOS SDK changelog for details.

## 1.20.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 15.0.0.

## 1.19.0

##### Changed

- Updated the Android binding to use Braze Android SDK 13.1.2.

## 1.18.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 13.0.0.
 
- Updated the iOS binding to use Braze iOS SDK 3.33.1.

## 1.17.0

##### Breaking

- Updated the iOS binding to use Braze iOS SDK 3.29.1.
 
- Updated the Android binding to use Braze Android SDK 11.0.0.

## 1.16.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 10.0.0.

## 1.15.0

##### Breaking

- The native iOS bridge uses Braze iOS SDK 3.27.0. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.
 
- ABKIDFADelegate.IsAdvertisingTrackingEnabled has been renamed to ABKIDFADelegate.IsAdvertisingTrackingEnabledOrATTAuthorized.
 
- The class ABKIdentifierForAdvertisingProvider has been removed.

## 1.14.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.26.1.

## 1.13.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 8.1.0.

## 1.12.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 8.0.1.
 
- Updated the native iOS bridge to Braze iOS SDK 3.24.2.

- Flipped ABKLocationManager.DisableLocationTracking to ABKLocationManager.EnableLocationTracking.
 
- Replaced ABKInAppMessageWindowController.supportedOrientationMasks with ABKInAppMessageWindowController.supportedOrientationMask.

## 1.11.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 6.0.0.
 
- Changed the Android binding to target Android 10.

## 1.10.2

Important: This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the Braze iOS SDK Changelog for more information.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.2.

## 1.10.1

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.10.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.10.2 or above if you make use of HTML in-app messages.

##### Changed

- Updated the native iOS bridge to Braze iOS SDK 3.20.1.

## 1.10.0

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.10.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.10.2 or above if you make use of HTML in-app messages.

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.20.0.
 
- Important: Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In application.RegisteredForRemoteNotifications:, replace

```

1

```
 | 
```
Appboy.SharedInstance?.RegisterPushToken(deviceToken.ToString());

```
 | 
 
with

```

1

```
 | 
```
Appboy.SharedInstance?.RegisterDeviceToken(deviceToken);

```
 | 

## 1.9.0

Important: This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.10.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.10.2 or above if you make use of HTML in-app messages.

##### Breaking

- Updated the Android binding to use Braze Android SDK 3.7.0.
 
- Updated the native iOS bridge to Braze iOS SDK 3.19.0.
 
- Note: This Braze Xamarin SDK release updates to Braze Android SDK and Braze iOS SDK dependencies which no longer enable automatic Braze location collection by default. Please consult their respective changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.
 
- Removes the Feedback feature as well as all associated methods, classes, and interfaces.

## 1.8.0

##### Changed

- Updated the Android binding to use Braze Android SDK 3.3.0.

##### Added

- Added C# bindings for Braze Android SDK classes with Firebase Cloud Messaging dependencies.

## 1.7.0

##### Breaking

- Updated the Android binding to use Braze Android SDK 3.2.1.

- Added AppboyFirebaseMessagingService to directly use the Firebase messaging event com.google.firebase.MESSAGING_EVENT. This is now the recommended way to integrate Firebase push with Braze. The AppboyFcmReceiver should be removed from your AndroidManifest and replaced with the following:

```

1
2
3
4
5

```
 | 
```
<service android:name="com.appboy.AppboyFirebaseMessagingService">
<intent-filter>
<action android:name="com.google.firebase.MESSAGING_EVENT" />
</intent-filter>
</service>

```
 | 

- Also note that any c2dm related permissions should be removed from your manifest as Braze does not require any extra permissions for AppboyFirebaseMessagingService to work correctly.

- Updated the native iOS bridge to Braze iOS SDK 3.14.0.

- Drops support for iOS 8.
 
- Removes Cross-Promotion cards from the News Feed.

## 1.6.0

##### Breaking

- Updated the native iOS bridge to Braze iOS SDK 3.11.0.
 
- Updated the Android binding to use Braze Android SDK 3.0.1.

## 1.5.2

##### Breaking

- Updated the Android binding to use Braze SDK version 2.5.0.

##### Fixed

- Fixed an issue that caused C# bindings to not be generated for certain classes in the Braze UI library.

##### Changed

- Updated the Android sample app to use Firebase Cloud Messaging (FCM).

## 1.5.1

##### Changed

- Updated the iOS binding to use Braze SDK version Braze iOS SDK 3.3.4.

- Added DisableSDK() and RequestEnableSDKOnNextAppRun() to the Appboy interface to disable and re-enable the Braze SDK.
 
- Added WipeDataAndDisableForAppRun() on the Appboy interface to support wiping all customer data created by the Braze SDK.
 
- Note that methods that disable the SDK will cause Appboy.SharedInstance to return null. If you have code that uses Appboy.SharedInstance, do not use DisableSDK() or WipeDataAndDisableForAppRun() until your code can safely execute even if Appboy.SharedInstance is null.

- Updated the Android binding to use Braze SDK version 2.2.5.

- Added DisableSdk() and EnableSdk() to the Appboy interface to disable and re-enable the Braze SDK.
 
- Added WipeData() on the Appboy interface to support wiping all customer data created by the Braze SDK.

## 1.5

##### Breaking

- Updated the iOS binding to use Braze SDK version Braze iOS SDK 3.3.0.
 
- Updated the Android binding to use Braze SDK version 2.2.1.
 
- Removed the need to include Appboy.bundle manually in iOS integrations. Integrators should remove existing Appboy.bundle files from their iOS integrations.

##### Added

- Added the ability to report to Braze that the app is running Xamarin to iOS integrations. We strongly recommend reporting this value to allow Braze to calculate accurate usage around different SDK platforms. To enable reporting, add Appboy.SharedInstance.SdkFlavor = ABKSDKFlavor.Xamarin; to your AppDelegate.cs after calling Appboy.StartWithApiKey().
 
- Braze Xamarin Bindings are now available on Nuget. Check out our iOS Binding and Android Binding. Note that Braze Xamarin SDK version 1.5.0 is the last version to receive a Xamarin component store release. Future releases will be released to Nuget and the open source repo only.

## 1.4

##### Breaking

- Updated the iOS binding to use Braze SDK version Braze iOS SDK 2.29.0.
 
- Updated the Android binding to use Braze SDK version 2.0.0.

## 1.3

##### Breaking

- Updated the iOS binding to use Braze SDK version Braze iOS SDK 2.24.2.
 
- Updated the Android binding to use Braze SDK version 1.15.3.
 
- Update Required — Updated iOS push handling in the AppboyProject sample project to be compatible with iOS 10. For more information, refer to the CHANGELOG for Braze iOS SDK v2.24.0.

##### Changed

- Updated the AppboyProject sample project to integrate session handling and in-app message manager registration using an AppboyLifecycleCallbackListener, as introduced in Braze Android SDK v1.15.0.

##### Removed

- Removed AppboyBroadcastReceiver.cs from the AppboyProject sample project, as Braze Android SDK v1.15.0 removes the need for a custom AppboyBroadcastReceiver for Braze push notifications.

## 1.2

##### Breaking

- Updated the iOS binding to use Braze SDK version Braze iOS SDK 2.17.1.
 
- Updated the Android binding to use Braze SDK version 1.11.0.

## 1.1

##### Breaking

- Updated the iOS binding to use Braze SDK version Braze iOS SDK 2.12.0.
 
- Updated the Android binding to use Braze SDK version 1.8.0.

##### Added

- Added a Xamarin Forms sample application with News Feed integrations.
 
- Added AppboyXamarinFormsFeedFragment that inherits from Android.App.Fragment to be compatible with Xamarin Forms.

## 1.0

##### Added

- Added support for all standard API and UI functionality in the Android SDK and iOS SDKs.
 
- iOS functionality not included in this release: IDFA collection, custom Slideup viewControllers, social data collection.
 
- Please contact Braze Technical Support for assistance for more information about these features and the timeline for their inclusion.

- 

New Stuff!
