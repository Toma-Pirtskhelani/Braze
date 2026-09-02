---
url: https://www.braze.com/docs/partners/ecommerce/ordering_payments_subscription/revenuecat
slug: docs__partners__ecommerce__ordering_payments_subscription__revenuecat
title: "RevenueCat"
description: "The RevenueCat and Braze integration allows you to automatically sync your customer's purchase and subscription lifecycle events across platforms. This allows you to build campaigns..."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# RevenueCat

RevenueCat is the single source of truth for your subscription status across iOS, Android, and web. Whether you are building a new app or already have millions of subscribers, you can use RevenueCat to build cross-platform in-app purchases, manage your products and subscribers, and analyze your data - no server code required.

This integration is maintained by RevenueCat.

## About the integration

The RevenueCat and Braze integration allows you to automatically sync your customer’s purchase and subscription lifecycle events across platforms. This allows you to build campaigns that react to the subscription lifecycle stage of your customers, such as engaging with customers that opted out during their free trial or sending reminders to customers with billing issues.

## Prerequisites

At a minimum, you will need to enable the integration from the RevenueCat dashboard to connect RevenueCat to Braze. If you’re using the Braze SDK, you can use the RevenueCat and Braze SDKs together to enhance the integration by ensuring the same customer identifier is being used in both systems.

 Requirement | 
 Description | 

 RevenueCat account and app | 
 A RevenueCat account is required to take advantage of this partnership. You must also have a configured RevenueCat app. | 

 RevenueCat SDK | 
 In addition to the required Braze SDK, we recommend installing the RevenueCat SDK to provide user aliases to RevenueCat. | 

 Braze instance | 
 Your Braze instance can be obtained from your Braze onboarding manager or can be found on the API overview page.

RevenueCat requires the Braze instance to send server-side to the correct Braze REST endpoint. | 

 Braze REST API key | 
 A Braze REST API key with users.track permissions. 

 This can be created in the Braze dashboard from Settings > API Keys. | 

 Braze test REST API key (optional) | 
 A test API key can be used for test and production purchases if you’d like these requests sent to separate Braze instances. | 

## Use Cases

- Trigger an onboarding campaign highlighting your premium features when a customer starts a free trial.
 
- Send a reminder to update billing information when a “Billing Issue” event is received.
 
- Send a feedback survey after a customer cancels a free trial.

## Integration

### Step 1: Set Braze user identity

In the Braze SDK, you can set the Braze user ID to match the RevenueCat app user ID, ensuring events sent from the Braze and RevenueCat can be synced to the same user.

Configure the Braze SDK with the same app user ID as RevenueCat or use the Braze SDK .changeUser() method.

- swift
 
- objective-c
 
- java

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
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
 "$brazeAliasLabel" : "label"])

```
 | 

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

```
 | 
```
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
 @"$brazeAliasName": @"name",
 @"$brazeAliasLabel": @"label"
}];

```
 | 

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

```
 | 
```
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);

```
 | 

#### Send user alias object to Braze (optional)

If you want to send an alternative unique user identifier different from the RevenueCat app user ID, update users with the following data as RevenueCat subscriber attributes.

 Key | 
 Description | 

 $brazeAliasName | 
 The Braze alias_name in the user alias object | 

 $brazeAliasLabel | 
 The Braze alias_label in the user alias object | 

Both attributes are required for the user alias object to be sent alongside your event data. These properties can be set manually, like any other RevenueCat subscriber attribute. Example code snippets are shown in step one.

### Step 2: Send RevenueCat events to Braze

After you’ve set up the RevenueCat purchases SDK and Braze SDK to have the same user identity, you can turn on the integration and configure the event names from the RevenueCat dashboard.

- Navigate to your project in the RevenueCat dashboard and find the Integrations card in the navigation menu. Select + New.
 
- Next, select Braze from the available integration and add your Braze instance and Braze REST API key.
 
- Enter the event names that RevenueCat will send or choose the default event names. More details on available events can be found in step 3.
 
- Select whether you want RevenueCat to report proceeds (after app store cut) or revenue (gross sales).

### Step 3: Configure event names

Enter the event names that RevenueCat will send or select from the default event names by selecting Use Default Event Names. The events that RevenueCat supports sending are described in the following chart.

 Event | 
 Description | 

 Initial Purchase | 
 The first purchase of an auto-renewing subscription product that does not contain a free trial. | 

 Trial Started | 
 The start of an auto-renewing subscription product free trial. | 

 Trial Converted | 
 When an auto-renewing subscription product converts from a free trial to a normal paid period. | 

 Trial Canceled | 
 When a user turns off renewals for an auto-renewing subscription product during a free trial period. | 

 Renewal | 
 When an auto-renewing subscription product renews, or a user repurchases the auto-renewing subscription product after a lapse in their subscription. | 

 Cancellation | 
 When a user turns off renewals for an auto-renewing subscription product during the normal paid period. | 

 Non Subscription Purchase | 
 The purchase of any product that’s not an auto-renewing subscription. | 

 Expiration | 
 When a subscription expires. | 

 Billing Issue | 
 When there has been a problem trying to charge the user. | 

For events that include revenue, RevenueCat will automatically record this amount along with the event in Braze, such as trial conversions and renewals.

## Using this integration

After configuring Braze settings in RevenueCat, events will automatically begin flowing from RevenueCat to Braze without any other action on your part.

## Customization

### Add a sandbox API key for Testing

If you only provide one Braze REST API key to RevenueCat, only production events will be sent. If you also want to send sandbox testing events, create another Braze REST API key and add it to your Braze settings in RevenueCat.

- 

New Stuff!
