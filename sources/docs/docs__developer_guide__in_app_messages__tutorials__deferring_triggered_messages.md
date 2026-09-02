---
url: https://www.braze.com/docs/developer_guide/in_app_messages/tutorials/deferring_triggered_messages
slug: docs__developer_guide__in_app_messages__tutorials__deferring_triggered_messages
title: "Tutorial: Deferring and restoring triggered messages"
description: ""
section: developer_guide/in_app_messages
fetched: 2026-09-02
evidence: company-own (technical)
---
# Tutorial: Deferring and restoring triggered messages

Follow along with the sample code in this tutorial to defer and restore triggered in-app messages using the Braze SDK.

- web
 
- android
 
- swift

## Prerequisites

Before you can use this feature, you’ll need to integrate the Web Braze SDK. However, no additional setup is required.

## Deferring and restoring triggered messages for Web

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Remove calls to automaticallyShowInAppMessages()

Remove any calls to automaticallyShowInAppMessages() , as they’ll override any custom logic you implement later.

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 3. Subscribe to the in-app message callback handler

Register a callback with subscribeToInAppMessage(callback) to receive a message any time an in-app message is triggered.

#### 4. Defer the message instance

To defer the message, call deferInAppMessage(message). Braze will serialize and save this message so you can display it on a future page load.

#### 5. Retrieve a previously deferred message

To retrieve any previously-deferred messages, call getDeferredInAppMessage().

#### 6. Display the deferred message

After retrieving a deferred message, display it by passing it to showInAppMessage(message).

#### 7. Display a message immediately

To show a message instead of deferring it, call showInAppMessage(message) directly in your subscribeToInAppMessage callback.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK. You’ll also need to enable in-app messages for Android.

## Deferring and restoring triggered messages for Android

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Create a singleton Application instance

Use a companion object to expose your Application class as a singleton so it can be accessed later in your code.

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 3. Register activity lifecycle callbacks

Register Braze’s default listener to handle the in-app message lifecycle.

#### 4. Set up an in-app message listener

Use BrazeInAppMessageManager to set a custom listener that intercepts messages before they’re displayed.

#### 5. Create conditional logic

Use the showMessage flag to control timing—return DISPLAY_NOW to display the message now or DISPLAY_LATER to defer it.

#### 6. Create a method for displaying deferred messages

Use showDeferredMessage to trigger the next in-app message. When showMessage is true, the listener will return DISPLAY_NOW.

#### 7. Trigger the method from your UI

To display the previously-deferred message, call showDeferredMessage(true) from your UI, such as a button or tap.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

```

```

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK. You’ll also need to enable in-app messages for Swift.

## Deferring and restoring triggered messages for Swift

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Implement the BrazeInAppMessageUIDelegate

In your AppDelegate class, implement the BrazeInAppMessageUIDelegate so you can override its inAppMessage method later.

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 3. Set up your Braze UI and delegate

BrazeInAppMessageUI() renders in-app messages by default. By assigning self as its delegate, you can intercept and handle messages before they’re displayed. Be sure to save the instance, as you’ll need it later to restore deferred messages.

#### 4. Override DisplayChoice with conditional logic

Override inAppMessage(_:displayChoiceForMessage:) to determine when a message should be displayed. Return .now to show it immediately, or .reenqueue to defer it for later.

#### 5. Create a method to show deferred messages

Create a method that calls showDeferredMessage(true) to display the next deferred message in the stack. When called, showMessage is set to true, making the delegate return .now.

#### 5. Trigger the method from your UI

To display the previously-deferred message, call showDeferredMessage(true) from your UI, such as a button or tap.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

```

```

```

```

- 

New Stuff!
