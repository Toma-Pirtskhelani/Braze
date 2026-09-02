---
url: https://www.braze.com/docs/user_guide/channels/banners/custom_code
slug: docs__user_guide__channels__banners__custom_code
title: "Custom code and JavaScript bridge for Banners"
description: "Learn how to use custom HTML in Banners and the JavaScript bridge to log clicks and trigger Braze actions."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Custom code and JavaScript bridge for Banners

When you use the Custom Code editor block in the Banner builder, or when you build a Banner with the HTML editor, you must call brazeBridge.logClick() from within your custom HTML to log clicks. Banners use the same JavaScript bridge as HTML in-app messages, so the same methods and patterns apply.

If you use custom HTML in your Banner design—whether through a Custom Code block in the builder or the full HTML editor—the Braze SDK cannot automatically attach click listeners to elements inside your custom code. You must explicitly call brazeBridge.logClick() for any clickable elements (links, buttons, and similar) that you want to track in campaign analytics.

For example, to log a click when a user taps a button in your custom HTML:

```

1
2
3

```
 | 
```
<button onclick="brazeBridge.logClick()">
 Click me
</button>

```
 | 

For the full JavaScript bridge reference, including all available methods and click tracking options, see JavaScript bridge.

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

- 

New Stuff!
