---
url: https://www.braze.com/docs/developer_guide/in_app_messages/tutorials/customizing_message_styling
slug: docs__developer_guide__in_app_messages__tutorials__customizing_message_styling
title: "Tutorial: Customizing message styling using key-value pairs"
description: ""
section: developer_guide/in_app_messages
fetched: 2026-09-02
evidence: company-own (technical)
---
# Tutorial: Customizing message styling using key-value pairs

Follow along with the sample code in this tutorial to customize your in-app message styling using key-value pairs in the Braze SDK.

- web
 
- android
 
- swift

## Prerequisites

Before you can use this feature, you’ll need to integrate the Web Braze SDK. However, no additional setup is required.

## Customizing message styling using key-value pairs for Web

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Remove calls to automaticallyShowInAppMessages()

Remove any calls to automaticallyShowInAppMessages() , as they’ll override any custom logic you implement later.

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 3. Subscribe to the in-app message callback handler

Register a callback with subscribeToInAppMessage(callback) to receive a message any time an in-app message is triggered.

#### 4. Access the message.extras property

Use message.extras to access customization types, styling attributes, or any other values defined in the dashboard. All values are returned as strings.

#### 5. Conditionally call showInAppMessage

To display the message, call showInAppMessage(message). Otherwise, use any custom properties as needed.

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

## Customizing message styling using key-value pairs for Android

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 2. Register activity lifecycle callbacks

Register Braze’s default listener to handle the in-app message lifecycle.

#### 3. Create your custom view factory class

Ensure your class conforms to IInAppMessageViewFactory so it can construct and return custom message views.

#### 4. Delegate to Braze’s default factory

Delegate to the default factory to retain Braze’s built-in styling before applying your own conditional changes.

#### 5. Access key-value pairs from inAppMessage.extras

Use inAppMessage.extras to access customization types, styling attributes, or any other values defined in the dashboard. Apply styling overrides before returning the view.

#### 6. Implement a custom IInAppMessageViewFactory

Implement IInAppMessageViewFactory in your custom class to construct and render in-app message views.

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

## Customizing message styling using key-value pairs for Swift

important

We’re piloting this new tutorial format. Tell us what you think — your feedback helps us improve future guides.

### 1. Implement BrazeInAppMessageUIDelegate

In your AppDelegate class, implement BrazeInAppMessageUIDelegate so you can override its inAppMessage method later.

#### 2. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

#### 3. Prepare messages before they’re displayed

Braze calls inAppMessage(_:prepareWith:) during message preparation. Use it to customize styling or apply logic based on key-value pairs.

#### 4. Access key-value pairs from message.extras

Use message.extras to access customization types, styling attributes, or any other values defined in the dashboard.

#### 5. Update the message’s styling attributes

Use inAppMessage(_:prepareWith:) to access the PresentationContext so you can modify styling attributes directly. Each in-app message type exposes different attributes.

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
