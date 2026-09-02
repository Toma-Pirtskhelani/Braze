---
url: https://www.braze.com/docs/developer_guide/platforms/web/browser_extensions
slug: docs__developer_guide__platforms__web__browser_extensions
title: "Browser extension"
description: "This article describes how to use the Braze Web SDK inside your Browser Extensions (Google Chrome, Firefox)."
section: developer_guide/platforms
fetched: 2026-09-02
evidence: company-own (technical)
---
# Browser extension

This article describes how to use the Braze Web SDK inside your Browser Extensions (Google Chrome, Firefox).

Integrate the Braze Web SDK within your browser extension to collect analytics and display rich messaging to users. This includes both Google Chrome Extensions and Firefox Add-Ons.

## What’s supported

In general, since extensions are HTML and JavaScript, you can use Braze for the following:

- Analytics: Capture custom events, attributes, and even identify repeat users within your extension. Use these profile traits to power cross-channel messaging.
 
- In-app messages: Trigger in-app messages when users take action within your extension, using our native or custom HTML messaging.
 
- Content Cards: Add a feed of native cards to your extension for onboarding or promotional content.
 
- Web Push: Send timely notifications even when your web page is not currently open.

## What’s not supported

- Using the Braze SDK from within a service worker is not supported. You can still use the Braze SDK in your extension’s popup or settings page. If you’re interested in service worker support in the Braze Web SDK, submit product feedback.

## Extension types

Braze can be included in the following areas of your extension:

 Area | 
 Details | 
 What’s supported | 

 Popup Page | 
 The Popup page is a dialog that can be shown to users when clicking on your extension’s icon in the browser toolbar. | 
 Analytics, in-app messages, and Content Cards | 

 Background Scripts | 
 Background Scripts (Manifest v2 only) allow your extension to inspect and interact with user navigation or modify webpages (for example, how ad blockers detect and change content on pages). | 
 Analytics, in-app messages, and Content Cards.

Background scripts aren’t visible to users, so for messaging, you would need to communicate with browser tabs or your popup page when displaying messages. | 

 Options Pages | 
 The Options Page lets your users toggle settings within your extension. It’s a standalone HTML page that opens a new tab. | 
 Analytics, in-app messages, and Content Cards | 

## Permissions

No additional permissions are required in your manifest.json when integrating the Braze SDK (braze.min.js) as a local file bundled with your extension.

However, if you use Google Tag Manager, or reference the Braze SDK from an external URL, or have set a strict Content Security Policy for your extension, you will need to adjust the content_security_policy setting in your manifest.json to allow remote script sources.

## Getting started

tip

Before you get started, make sure you’ve read through the Web SDK’s Initial SDK setup guide to learn more about our JavaScript integration in general. 

You may also want to bookmark the JavaScript SDK reference for full details on all of the different SDK methods and configuration options.

To integrate the Braze Web SDK, you’ll first need to download a copy of the latest JavaScript library. This can be done using NPM or directly downloading it from the Braze CDN.

Alternatively, if you prefer to use Google Tag Manager or use an externally hosted copy of the Braze SDK, keep in mind that loading external resources will require you to adjust your content_security_policy setting in your manifest.json.

Once downloaded, be sure to copy the braze.min.js file somewhere into your extension’s directory.

### Extension popups

To add Braze to an extension popup, reference the local JavaScript file in your popup.html, as you would in a regular website. If you’re using Google Tag Manager, you can add Braze using our Google Tag Manager templates instead.

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
<html>
 <title>popup.html</title>
 <!-- Add the Braze library -->
 <script src="/relative/path/to/braze.min.js"></script>
 <script>
 // Initialize Braze here
 </script>
</html>

```
 | 

### Background script (Manifest v2 only)

To use Braze within your extension’s background script, add the Braze library to your manifest.json in the background.scripts array. This will make the global braze variable available in your background script context.

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
{
 "manifest_version": 2,
 "background": {
 "scripts": [
 "relative/path/to/braze.min.js",
 "background.js"
 ]
 }
}

```
 | 

### Options page

If you use an options page (via the options or options_ui manifest properties), you can include Braze just as you would in the popup.html instructions.

## Initialization

Once the SDK is included, you can initialize the library as usual.

Since cookies are not supported in browser extensions, you can disable cookies by initializing with noCookies: true.

```

1
2
3
4
5

```
 | 
```
braze.initialize("YOUR-API-KEY-HERE", {
 baseUrl: "YOUR-API-ENDPOINT",
 enableLogging: true,
 noCookies: true
});

```
 | 

For more information on our supported initialization options, visit the Web SDK reference.

## Push

Extension popup dialogs don’t allow for push prompts (they don’t have the URL bar in the navigation). So to register and request push permission within an extension’s Popup dialog, you’ll have to make use of an alternate domain workaround, as described in Alternate push domain.

- 

New Stuff!
