---
url: https://www.braze.com/docs/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages
slug: docs__developer_guide__in_app_messages__tutorials__conditionally_displaying_messages
title: "Tutorial: Conditionally displaying in-app messages"
description: ""
section: developer_guide/in_app_messages
fetched: 2026-09-02
evidence: company-own (technical)
---
# Tutorial: Conditionally displaying in-app messages

Follow along with the sample code in this tutorial to conditionally display in-app messages using the Braze SDK.

- web
 
- android
 
- swift

## Prerequisites

Before you can use this feature, you’ll need to integrate the Web Braze SDK. However, no additional setup is required.

## Conditionally displaying in-app messages for Web

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Remove calls to automaticallyShowInAppMessages()

Remove any calls to automaticallyShowInAppMessages(), as they’ll override any custom logic you implement later.

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 3. Subscribe to in-app message updates

Register a callback with subscribeToInAppMessage(callback) to receive a message any time an in-app message is triggered.

#### 4. Create conditional logic

Create custom logic to control when messages are displayed. In this example, the logic checks if the URL contains "checkout" or if a #checkout element exists on the page.

#### 5. Display messages with showInAppMessage

To display the message, call showInAppMessage(message). If omitted, the message will be skipped.

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

## Conditionally displaying in-app messages for Android

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 2. Register activity lifecycle callbacks

Register Braze’s default listener to handle the in-app message lifecycle.

#### 3. Set up an in-app message listener

Use BrazeInAppMessageManager to set a custom listener that intercepts messages before they’re displayed.

#### 4. Create conditional logic

Use custom logic to control message display timing. In this example, the custom logic checks if the should_display_message extra is set to "true".

#### 5. Return or discard the message

Return an InAppMessageOperation with DISPLAY_NOW to display the message, or with DISCARD to suppress it.

Please rate this tutorial:

 ★
 ★
 ★
 ★
 ★

```

```

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK. You’ll also need to enable in-app messages for Swift.

## Conditionally displaying in-app messages for Swift

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Implement the BrazeInAppMessageUIDelegate

In your AppDelegate class, implement the BrazeInAppMessageUIDelegate so you can override its inAppMessage method later.

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 3. Set up your Braze UI and delegate

BrazeInAppMessageUI() renders in-app messages by default. By assigning self as its delegate, you can intercept and handle messages before they’re displayed.

#### 4. Override DisplayChoice with conditional logic

Override inAppMessage(_:displayChoiceForMessage:) to decide whether a message should be shown. Return .now to display the message or .discard to suppress it.

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

- 

New Stuff!
