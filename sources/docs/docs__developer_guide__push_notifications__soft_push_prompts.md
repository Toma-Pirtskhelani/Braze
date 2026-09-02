---
url: https://www.braze.com/docs/developer_guide/push_notifications/soft_push_prompts
slug: docs__developer_guide__push_notifications__soft_push_prompts
title: "Soft push prompts for Web"
description: "Learn how to set up soft push prompts for the Braze Web SDK before the native browser notification permission prompt."
section: developer_guide/push_notifications
fetched: 2026-09-02
evidence: company-own (technical)
---
# Soft push prompts for Web

Soft push prompts are custom messages you show before the browser’s native notification permission prompt. They explain why users should enable push notifications and can improve opt-in rates compared with displaying the system prompt on first visit. This guide covers how to implement soft push prompts with the Braze Web SDK, including when to trigger the prompt, how to customize the message content, and best practices for timing the request after users understand the value of push.

- web

## Prerequisites

Before you can use this feature, you’ll need to integrate the Web Braze SDK. You’ll also need to set up push notifications.

If you’re integrating Braze through mParticle’s embedded kit on the web, see Step 3 in mParticle’s Braze Web event integration for instructions to implement soft push prompts.

## About soft push prompts

It’s often a good idea for sites to implement a “soft” push prompt where you “prime” the user and make your case for sending them push notifications before requesting push permission. This is useful because the browser throttles how often you may prompt the user directly, and if the user denies permission you can never ask them again.

Alternatively, if you would like to include special custom handling, instead of calling requestPushPermission() directly as described in the standard Web push integration, use our triggered in-app messages.

tip

This can be done without SDK customization using our new no code push primer.

## Setting up soft push prompts

note

This guide uses code samples from the Braze Web SDK 4.0.0+. To upgrade to the latest Web SDK version, see SDK Upgrade Guide.

### Step 1: Create a push primer campaign

First, you must create a “Prime for Push” in-app messaging campaign in the Braze dashboard:

- Create a Modal in-app message with the text and styling you want.
 
- Next, set the on-click behavior to Close Message. This behavior will be customized later.
 
- Add a key-value pair to the message where the key is msg-id, and the value is push-primer.
 
- Assign a custom event trigger action (such as “prime-for-push”) to the message. You can create the custom event manually from the dashboard if needed.

### Step 2: Remove calls

In your Braze SDK integration, find and remove any calls to automaticallyShowInAppMessages() from within your loading snippet.

### Step 3: Update integration

Finally, replace the removed call with the following snippet. Call subscribeToInAppMessage() before calling openSession(). This ensures your in-app message listener is registered in time to receive the push primer message.

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
28
29
30
31
32
33
34
35
36
37
38
39
40
41

```
 | 
```
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
 // check if message is not a control variant
 if (inAppMessage instanceof braze.inAppMessage) {
 // access the key-value pairs, defined as `extras`
 const keyValuePairs = inAppMessage.extras || {};
 // check the value of our key `msg-id` defined in the Braze dashboard
 if (keyValuePairs["msg-id"] === "push-primer") {
 // We don't want to display the soft push prompt to users on browsers
 // that don't support push, or if the user has already granted/blocked permission
 if (
 braze.isPushSupported() === false ||
 braze.isPushPermissionGranted() ||
 braze.isPushBlocked()
 ) {
 // do not call `showInAppMessage`
 return;
 }

 // user is eligible to receive the native prompt
 // register a click handler on one of the two buttons
 if (inAppMessage.buttons[0]) {
 // Prompt the user when the first button is clicked
 inAppMessage.buttons[0].subscribeToClickedEvent(function() {
 braze.requestPushPermission(
 function() {
 // success!
 },
 function() {
 // user declined
 }
 );
 });
 }
 }
 }

 // show the in-app message now
 braze.showInAppMessage(inAppMessage);
});

```
 | 

When you wish to display the soft push prompt to the user, call braze.logCustomEvent - with whatever event name triggers this in-app message.

## Frequently asked questions

### What is a soft push prompt?

A soft push prompt is a custom in-app or on-site message you show before the browser’s native notification permission dialog. It explains the value of push so users are more likely to accept when the system prompt appears.

### When should I show a soft push prompt?

Show a soft push prompt after users understand your product value—for example, after onboarding or a meaningful in-app action—not on first page load. Refer to the Web SDK steps in this guide for implementation details.

- 

New Stuff!
