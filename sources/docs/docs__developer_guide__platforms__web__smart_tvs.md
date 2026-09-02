---
url: https://www.braze.com/docs/developer_guide/platforms/web/smart_tvs
slug: docs__developer_guide__platforms__web__smart_tvs
title: "Smart TV support"
description: "This article covers how to use the Braze Web SDK to integrate with Smart TVs (Samsung and LG)."
section: developer_guide/platforms
fetched: 2026-09-02
evidence: company-own (technical)
---
# Smart TV support

The Braze Web SDK lets you collect analytics and display rich in-app messages and Content Card messages to Smart TV users, including Samsung Tizen TVs and LG TVs (webOS). This article covers how to use the Braze Web SDK to integrate with Smart TVs.

tip

For a complete technical reference, check out our JavaScript Documentation or our sample apps to see the Web SDK running on a TV.

## Prerequisites

Before you can use this feature, you’ll need to integrate the Web Braze SDK.

## Configuring the Web Braze SDK

There are two changes required when integrating with Smart TVs:

- When downloading or importing the Web SDK, be sure to use the “core” bundle (available at https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js, where x.y is the desired version). We recommend using the CDN version of our Web SDK, since the NPM version is written in native ES modules whereas the CDN version is transpiled down to ES5. If you prefer to use the NPM version, ensure you are using a bundler such as webpack that will remove unused code and that the code is transpiled down to ES5.
 
- When initializing the Web SDK, you must set the disablePushTokenMaintenance and manageServiceWorkerExternally initialization options to true.

## Analytics

All of the same Web SDK methods for analytics can be used on Smart TVs. For a full walkthrough for tracking custom events, custom attributes, and more, see Analytics.

## In-app messages and Content Cards

The Braze Web SDK supports both in-app messages and Content Cards on Smart TVs. Note that you must use the “Core” Web SDK as rendering in-app messages and Content Cards is not supported using our standard UI display and should instead be customized by your app to fit into your TV App’s experience.

For more information on how your Smart TV App can receive and display in-app messages, see Triggering messages.

- 

New Stuff!
