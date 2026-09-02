---
url: https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/custom_html
slug: docs__user_guide__channels__in_app_messages__message_types__custom_html
title: "Custom HTML in-app messages"
description: "This article provides an overview of custom code in-app messages, including JavaScript methods, button tracking, and using the interactive HTML preview in Braze."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Custom HTML in-app messages

While our standard in-app messages can be customized in a variety of ways, you can gain even greater control over the look and feel of your campaigns using messages designed and built using HTML, CSS, and JavaScript. With some simple composition, you can unlock custom functionality and branding to match any of your needs.

This message type is available in the traditional editor.

## How it works

HTML in-app messages allow for greater control over the look and feel of a message, including the following:

- Custom fonts and styles
 
- Videos
 
- Multiple images
 
- On-click behaviors
 
- Interactive components
 
- Custom animations

Custom HTML messages can use the JavaScript Bridge methods to log events, set custom attributes, close the message, and more! Check out our GitHub repository that contains detailed instructions on how to use and customize HTML in-app messages for your needs, and for a set of HTML5 in-app messages templates to help you get started.

note

To enable HTML in-app messages through the Web SDK, you must supply the allowUserSuppliedJavascript initialization option to Braze: for example, braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true}). This is for security reasons since HTML in-app messages can execute JavaScript, so we require a site maintainer to enable them.

### Rendering environments

Custom HTML in-app messages render directly in the browser on web, but inside a platform WebView on iOS and Android. Because each environment uses a different rendering engine, the same HTML and CSS may display with slight visual differences across platforms, particularly for column layouts, fonts, and spacing.

To minimize cross-platform differences:

- Use explicit CSS values rather than relying on browser defaults
 
- Include a viewport meta tag (for example, <meta name="viewport" content="width=device-width, initial-scale=1">)
 
- Test on actual devices with test sends

## Character encoding

When building custom HTML in-app messages with special characters—such as Cyrillic script, accented characters, or other non-ASCII text—include UTF-8 encoding in your HTML to ensure proper display. Without UTF-8 encoding, these characters may appear broken or missing when rendered in the webview.

To enable UTF-8 encoding, add the following meta tag inside your HTML <head> section:

```

1

```
 | 
```
<meta charset="UTF-8">

```
 | 

This forces UTF-8 encoding, which is the expected character set for webviews that display in-app messages.

## JavaScript bridge

Custom HTML in-app messages and Banners support a JavaScript “bridge” to interface with the Braze SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. These methods exist with the global brazeBridge or appboyBridge variable.

important

Braze recommends that you use the global brazeBridge variable. The global appboyBridge variable is deprecated but will continue to function for existing users. If you are using appboyBridge, we suggest you migrate to brazeBridge. 

 appboyBridge was deprecated in the following SDK versions:

- Web: 3.3.0+
 
- Android: 14.0.0+
 
- iOS: 4.2.0+

For example, to log a custom attribute and custom event, then close the message, you could use the following JavaScript within your custom HTML:

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

```
 | 
```
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
 // Event handler when the button is clicked
 document.querySelector("#button").onclick = function(){
 // Track Button 1 clicks for analytics
 // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
 brazeBridge.logClick("0");
 // Set the user's custom attribute
 brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
 // Track a custom event
 brazeBridge.logCustomEvent("completed survey");
 // Send the enqueued data to Braze
 brazeBridge.requestImmediateDataFlush();
 // Close the message
 brazeBridge.closeMessage();
 };
}, false);
</script>

```
 | 

### JavaScript Bridge methods

The following JavaScript methods are supported within custom HTML for in-app messages and Banners:

 Method Name | 
 Description | 

 brazeBridge.closeMessage() | 
 Close the current message. Behavior differs by channel: 

 In-app messages: closes the UI only. No dismissal is logged and no server-side suppression occurs. 

 Banners: equivalent to calling logBannerDismissal. This logs a Banner dismissal, removes the Banner from the UI, and suppresses the Banner for the user. Also re-triggers any active subscribeToBannersUpdates subscribers. Do not call this method if the message is already in the process of closing or will automatically close due to processing a deep-link. | 

 window.addEventListener("ab.BridgeReady", function(){...}, false) | 
 Callback method for when the brazeBridge has finished loading. All JavaScript code should be ran within this callback function. | 

 brazeBridge.requestImmediateDataFlush() | 
 Flush queued data to the Braze servers. JS Docs | 

 brazeBridge.logClick(button_id_string) | 
 Log a button click for a given button ID. When button_id_string is left blank, a body-click will be logged instead. The button_id_string can be passed out as the button_id in in-app message click events via Currents. 

This method was introduced in Android SDK v8.0.0, Web SDK v2.5.0, and iOS SDK v3.23.0

The button_id_string only accepts alphanumeric characters, spaces, dashes, and underscores. Adding a character with an accent (for example, ö,â,ê) breaks the button click tracking, resulting in the button string not appearing in the campaign analytics section and clicks not being accounted for. | 

 brazeBridge.logCustomEvent(eventName,eventProperties) | 
 Log a custom event. JS Docs | 

 brazeBridge.logPurchase(productId, price, currencyCode, quantity, purchaseProperties) | 
 Log a purchase. JS Docs | 

 brazeBridge.getUser().addAlias(alias, label) | 
 Adds an alias to a user. Introduced in Web SDK v2.7.0, Android v8.1.0, and iOS SDK v3.26.0 JS Docs | 

 brazeBridge.getUser().addToCustomAttributeArray(key, value) | 
 Adds to a custom attribute array. JS Docs | 

 brazeBridge.getUser().addToSubscriptionGroup(subscriptionGroupId) | 
 Adds a user to an email or SMS subscription group. JS Docs.

This method was introduced in Android SDK v15.0.0, Web SDK v3.4.0, and iOS SDK v4.3.3. | 

 brazeBridge.getUser().removeFromSubscriptionGroup(subscriptionGroupId) | 
 Removes a user from an email or SMS subscription group. JS Docs.

This method was introduced in Android SDK v15.0.0, Web SDK v3.4.0, and iOS SDK v4.3.3. | 

 brazeBridge.getUser().setFirstName(firstName) | 
 Set a user’s first name. JS Docs | 

 brazeBridge.getUser().setLastName(lastName) | 
 Set a user’s last name. JS Docs | 

 brazeBridge.getUser().setEmail(email) | 
 Set a user’s email address. JS Docs | 

 brazeBridge.getUser().setGender(gender) | 
 Set a user’s gender. JS Docs | 

 brazeBridge.getUser().setDateOfBirth(year, month, day) | 
 Set a user’s date of birth. JS Docs | 

 brazeBridge.getUser().setCountry(country) | 
 Set a user’s country. JS Docs | 

 brazeBridge.getUser().setHomeCity(city) | 
 Set a user’s city. JS Docs | 

 brazeBridge.getUser().setEmailNotificationSubscriptionType(notificationSubscriptionType) | 
 Set email notification subscription status. JS Docs | 

 brazeBridge.getUser().setPushNotificationSubscriptionType(notificationSubscriptionType) | 
 Set push notification subscription status. JS Docs | 

 brazeBridge.getUser().setPhoneNumber(phoneNumber) | 
 Set a user’s phone number. JS Docs | 

 brazeBridge.getUser().setCustomUserAttribute(key, value, merge) | 
 Set a custom user attribute. JS Docs | 

 brazeBridge.getUser().removeFromCustomAttributeArray(key, value) | 
 Remove a custom user attribute. JS Docs | 

 brazeBridge.getUser().incrementCustomUserAttribute(key, incrementValue) | 
 Increment a custom user attribute. JS Docs | 

 brazeBridge.getUser().setLanguage(language) | 
 Set a user’s language. Introduced in Android SDK v5.0.0 and Web SDK v2.6.0. JS Docs | 

 brazeBridge.getUser().setCustomLocationAttribute(key, latitude, longitude) | 
 Set a custom location attribute. Introduced in Android SDK v5.0.0. JS Docs | 

 brazeBridge.web.registerAppboyPushMessages(successCallback, deniedCallback) | 
 Register for web push (web only). This method is a no-op when called in a non-web environment. JS Docs | 

 brazeBridge.requestPushPermission(successCallback, deniedCallback) | 
 Register for push across Web, iOS, and Android. Note: the method’s callbacks are only supported on web. This method was introduced as of Web SDK v4.0.0, Android SDK v21.0.0, and Swift SDK v5.4.0. JS Docs | 

 brazeBridge.changeUser(id, sdkAuthSignature?) | 
 Identify user with a unique ID. JS Docs

This method was introduced in Web SDK v4.3.0. | 

### Button click tracking

Use the brazeBridge.logClick(button_id) method to track clicks in your custom HTML.

For in-app messages, you can programmatically track “Button 1”, “Button 2”, and “Body Clicks” using brazeBridge.logClick('0'), brazeBridge.logClick('1'), or brazeBridge.logClick(), respectively.

 Clicks | 
 Method | 
 Supported | 

 Body click | 
 brazeBridge.logClick() | 
 In-app messages and Banners | 

 Button 1 | 
 brazeBridge.logClick('0') | 
 In-app messages only | 

 Button 2 | 
 brazeBridge.logClick('1') | 
 In-app messages only | 

 Custom button tracking | 
 brazeBridge.logClick('your custom name here') | 
 In-app messages and Banners | 

For in-app messages, you can track multiple button click events per impression. For example, to close a message and log a Button 2 click:

```

1

```
 | 
```
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>

```
 | 

You can also track new custom button names—up to 100 unique names per campaign. For example, brazeBridge.logClick('blue button') or brazeBridge.logClick('viewed carousel page 3').

tip

When using JavaScript methods inside an onclick attribute, wrap string values in single quotes to avoid conflicts with the double-quoted HTML attribute.

#### Limitations (in-app messages only)

- You can have up to 100 unique button IDs per campaign.
 
- Button IDs can have up to 255 characters each.
 
- Button IDs can only include letters, numbers, spaces, dashes, and underscores.

## Link-based actions

In addition to custom JavaScript, Braze SDKs can also send analytics data with these convenient URL shortcuts. Note that these query parameters and URL schemes are all case sensitive.

### Button click tracking (deprecated)

warning

The use of abButtonID is not supported in HTML with Preview message types. For more information, see our upgrade guide.

To log button clicks for in-app message analytics, you can add abButtonId as a query parameter to any deep link, redirect URL, or anchor element <a>. Use ?abButtonId=0 to log a “Button 1” click, and ?abButtonId=1 to log a “Button 2” click.

As with other URL parameters, the first parameter should begin with a question mark ?, while subsequent parameters should be separated by an ampersand &.

#### Example URLs

- https://example.com/?abButtonId=0 - Button 1 click
 
- https://example.com/?abButtonId=1 - Button 2 click
 
- https://example.com/?utm_source=braze&abButtonId=0 - Button 1 click with other existing URL parameters
 
- myApp://deep-link?page=home&abButtonId=1 - Mobile deeplink with Button 2 click
 
- <a href="https://example.com/?abButtonId=1"> - Anchor element <a> with Button 2 click

note

In-app messages support only Button 1 and Button 2 clicks. URLs that do not specify one of these two button IDs will be logged as generic “body clicks”.

### Open link in new window (mobile only)

To open links outside your app in a new window, set ?abExternalOpen=true. The message will be dismissed before opening the link.

For deep linking, Braze will open your URL regardless of the value of abExternalOpen.

### Open as deeplink (mobile only)

To have Braze handle your HTTP or HTTPS link as a deep link, set ?abDeepLink=true.

When this query string parameter is absent or set to false, Braze will try to open the web link in an internal web browser inside the host app.

### Close in-app message

To close an in-app message, you can use the brazeBridge.closeMessage() javascript method.

For example, <a onclick="brazeBridge.closeMessage()" href="#">Close</a> will close the in-app message.

## HTML upload with preview

When crafting custom HTML in-app messages, you can preview your interactive content directly in Braze.

The message preview panel of the editor shows a realistic preview that renders the JavaScript included in your message. You can preview and interact with your custom messages from the preview panel by clicking through pagination, submitting forms or surveys, watching JavaScript animations, and more!

tip

Any brazeBridge JavaScript methods you use in your HTML won’t update user profiles while previewing in the dashboard.

### Creating a campaign

#### Asset files

When creating custom code in-app messages with HTML upload, you can upload campaign assets to the media library to reference in your message.

The following file types are supported for upload:

 File Type | 
 File Extension | 

 Font Files | 
 .ttf, .woff, .otf, .woff2 | 

 SVG Images | 
 .svg | 

 JavaScript Files | 
 .js | 

 CSS Files | 
 .css | 

Braze recommends uploading assets to the media library for two reasons:

- Assets added to a campaign via the media library allow your messages to be displayed even while the user is offline or has a poor internet connection.
 
- Assets uploaded to Braze can be reused across campaigns.

##### Adding asset files

You can add new or existing assets to your campaign.

To add new assets to your campaign, use the drag-and-drop section to upload a file. Assets added in this section will also be automatically added to the media library. To add assets that you’ve already uploaded to the media library, select Add from Media Library.

After your assets are added, they will appear in the Assets for this campaign section.

If an asset’s filename matches that of a local HTML asset, it is replaced automatically (for example, cat.png is uploaded and <img src="cat.png" /> exists).

Otherwise, hover over an asset from the list and select Copy to copy the file’s URL to your clipboard. Then paste the copied asset URL into your HTML as you normally would when referencing a remote asset.

### HTML editor

Changes you make in the HTML automatically render in the preview panel as you type. Any brazeBridge JavaScript methods you use in your HTML won’t update user profiles while previewing in the dashboard.

tip

You can select Search within the HTML editor to search within your code!

### Button tracking

You can track performance within your custom code in-app message using the brazeBridge.logClick(button_id) JavaScript method. This allows you to programmatically track “Button 1”, “Button 2”, and “Body Clicks” using brazeBridge.logClick('0'), brazeBridge.logClick('1'), or brazeBridge.logClick(), respectively.

 Clicks | 
 Method | 

 Button 1 | 
 brazeBridge.logClick('0') | 

 Button 2 | 
 brazeBridge.logClick('1') | 

 Body click | 
 brazeBridge.logClick() | 

 Custom button tracking | 
 brazeBridge.logClick('your custom name here') | 

note

This method of button tracking replaces the prior automatic click tracking methods (such as ?abButtonId=0), which have been removed.

Use brazeBridge.logClick(button_id) for HTML with preview messages when you need more than two tracked buttons. Button 1 and Button 2 map to '0' and '1'; additional buttons use custom IDs (up to 100 unique IDs per campaign). For character restrictions on button IDs, see Button tracking.

### Troubleshoot custom HTML links and close behavior

#### Button clicks do not open the link

If a button in your custom HTML in-app message does not load when clicked, verify that the link uses a valid URL or supported deep link scheme. Malformed URLs or unsupported custom schemes can prevent the click action from completing.

#### Body clicks when closing the message

Calling brazeBridge.closeMessage() closes the message but does not log analytics on its own. To log a body click when the user closes the message, call brazeBridge.logClick() before brazeBridge.closeMessage() so click logging stays consistent across platforms.

#### Custom HTML not rendering on Android (Windows zip files)

If your custom HTML in-app message renders in preview but fails to display on Android devices, check how your HTML and asset files were packaged. Some Windows zip utilities add directory entries (folder paths) inside the archive instead of placing files at the root level.

Android may fail to load assets referenced with relative paths when the zip includes nested directory entries. To fix this:

- Extract your HTML, CSS, JavaScript, and image files to a single folder.
 
- Select all files (not the parent folder) when creating the zip archive.
 
- Confirm paths in your HTML reference files at the zip root (for example, style.css, not assets/style.css), or adjust paths to match the flattened structure.
 
- Re-upload the zip and send a test message to an Android device.

Alternatively, upload assets through the media library instead of bundling them in a zip file.

### Backward incompatible changes

- The braze://close deeplink, which was previously supported on mobile apps, has been removed in favor of the JavaScript brazeBridge.closeMessage(). This allows for cross-platform HTML messages, since the web does not support deeplinks.
 
- 
 
Automatic click tracking, which used ?abButtonId=0 for button IDs, and “body click” tracking on close buttons have been removed. The following code examples show how to change your HTML to use our new click tracking JavaScript methods:

 Before | 
 After | 

 <a href="braze://close">Close Button</a> | 
 <a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">Close Button</a> | 

 <a href="braze://close?abButtonId=0">Close Button</a> | 
 <a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">Close Button</a> | 

 <a href="app://deeplink?abButtonId=0">Track button 1</a> | 
 <a href="app://deeplink" onclick="brazeBridge.logClick('0')">Track button 1</a> | 

 <script>
location.href = "braze://close?abButtonId=1"
</script> | 
 <script>
window.addEventListener("ab.BridgeReady", function(){
  brazeBridge.logClick("1");
  brazeBridge.closeMessage();
});
</script> | 

- 

New Stuff!
