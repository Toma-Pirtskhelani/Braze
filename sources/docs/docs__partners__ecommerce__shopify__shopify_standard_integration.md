---
url: https://www.braze.com/docs/partners/ecommerce/shopify/shopify_standard_integration
slug: docs__partners__ecommerce__shopify__shopify_standard_integration
title: "Shopify standard integration setup"
description: "This reference article outlines how to set up the standard Shopify integration."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Shopify standard integration setup

This page walks you through how to integrate Braze with Shopify using our standard integration for users with a Shopify online store. If you use a Shopify headless site or are looking to implement more tailored solutions, refer to Shopify custom integration setup.

## Step 1: Connect your Shopify store

- In Braze, go to Partner Integrations > Technology Partners and then search for “Shopify”.
 
- On the Shopify partner page, select Begin setup to start the integration process.

- In the Shopify app store, install the Braze application.

note

If your Shopify account is associated with more than one store, you can change the store you’re logged into by selecting the store icon in the header and selecting Switch stores.

- After installing the Braze app, you’ll be redirected to Braze to confirm the workspace you want to connect to Shopify. A Shopify store can connect to only one workspace. If you need to switch, select the correct workspace.

- Select Begin setup.

## Step 2: Enable Braze Web SDKs

For Shopify online stores, you can select the standard setup to automatically implement the Braze Web SDK and JavaScript SDK.

After you select the standard setup onboarding path, you’ll need to choose when Braze should initialize and load the SDKs from one of the following options:

- Upon site visit, such as session start

- Tracks both identified and anonymous users

- Upon account signup, such as account login

- Track only identified users
 
- Starts tracking data when site visitors sign up or log into their accounts

note

New customers are provisioned on the latest Braze Web SDK and JavaScript SDK versions during setup. Existing customers can view their current SDK version in integration settings, get notified when a newer version is available, and self-serve upgrades from integration settings.

## Step 3: Configure your Shopify data

### Standard data setup

important

For this integration, the user alias must use the following format so that Braze can match webhooks to the correct user profile:

- alias_label: shopify_cart_${cartToken}
 
- alias_name: shopify_cart_token

Now you’ll select the Shopify data you want to track.

The following events will be enabled by default in the standard integration.

 Braze recommended events | 
 Shopify custom events | 
 Shopify custom attributes | 

- Product viewed
- Cart updated
- Checkout started
- Order placed | 
 
- shopify_account_login
- shopify_paid_order
- shopify_order_canceled
- shopify_order_refunded
- shopify_order_fulfilled
- shopify_order_partially_fulfilled | 
 
- shopify_tags
- shopify_total_spent
- shopify_order_count
- shopify_last_order_id
- shopify_last_order_name
- shopify_zipcode
- shopify_province | 

For more information on the data tracked through the integration, refer to Shopify Data Features.

important

The Shopify integration supports Shopify customer create and customer update webhooks, which are located in your data configuration settings. When a user profile is created or updated in Shopify, a corresponding user profile in Braze will be created or updated. 

These actions don’t trigger custom events in Braze and are solely used to sync Shopify user data with Braze. The data synced includes custom attributes, standard attributes, and, if enabled within your configuration, subscription group states.

### Historical backfill setup

In the Track Shopify data step, select the checkbox to include the initial historical data load as part of your integration.

For what is imported, revenue reporting behavior, setup screenshots, and guidance if you already use Braze with active campaigns or Canvases, see Historical backfill.

### (Advanced) Custom data tracking setup

With the Braze SDKs, you can track custom events or custom attributes that go beyond standard events for this integration. Custom events capture unique interactions in your store, such as:

 (Advanced) Custom data tracking setup

 Custom events | 
 Custom attributes | 

- Using a custom discount code
 
- Interacting with a personalized product recommendation
 
- Adding a gift message to their order
 
 | 

- Favorite brands or products
 
- Preferred shopping categories
 
- Membership or loyalty status
 
 | 

Tracking custom data provides deeper insights into user behavior and supports additional personalization. To implement custom events, you need to edit your storefront’s theme code in the theme.liquid file. You may need help from your developers.

For example, the following JavaScript snippet tracks if the current user subscribes to a newsletter, and logs that as a custom event on their profile in Braze:

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
braze.logCustomEvent(
 “subscribed_to_newsletter”,
 {
 newsletterName: ‘News and Offers’,
 customerEmail: ‘customer_1@example.com’,
 sendOffers: true
 }
);

```
 | 

The SDK must be initialized (listening for activity) on a user’s device to log events or custom attributes. To learn more about logging custom data, refer to User object and logCustomEvent object.

## Step 4: Configure how you manage users

Select your external_id type from the dropdown.

important

Using an email address or a hashed email address as your Braze external ID can simplify identity management across your data sources. However, it’s important to consider the potential risks to user privacy and data security.

- Guessable Information: Email addresses are easily guessable, making them vulnerable to attacks.
 
- Risk of Exploitation: If a malicious user alters their web browser to send someone else’s email address as their external ID, they could potentially access sensitive messages or account information.

By default, Braze automatically converts emails from Shopify to lowercase before using them as the external ID. If you’re using email or hashed email as your external ID, confirm that your email addresses are also converted to lowercase before you assign them as your external ID or before hashing them from other data sources. This helps prevent discrepancies in external IDs and avoid creating duplicate user profiles in Braze.

note

The next steps depend on your external ID selection:

- If you selected a custom external ID type: Complete steps 4.1—4.3 to set up your custom external ID configuration.
 
- If you selected Shopify customer ID, email, or hashed email: Skip steps 4.1—4.3 and continue directly to step 4.4.

### Step 4.1: Create the braze.external_id metafield

- In your Shopify admin panel, go to Settings > Metafields and metaobjects.
 
- Select Customers > Add definition.
 
- For Name, enter braze.external_id.
 
- Select the auto-generated namespace and key (custom.braze_external_id) to edit it and change it to braze.external_id.
 
- For Type, select ID Type.

After the metafield is created, populate it for your customers. We recommend the following approaches:

- Listen to customer creation webhooks: Set up a webhook to listen for customer/create events. This allows you to write the metafield when a new customer is created.
 
- Backfill existing customers: Use the Admin API or Customer API to backfill the metafield for previously created customers.

#### Potential race condition

The Shopify customers/create webhook may fire before the braze.external_id metafield is written to the user profile. When this happens:

- If the metafield is missing, Braze calls the configured endpoint (Step 4.2) to fetch the external ID.
 
- If that call also fails or times out, Braze creates a temporary user profile with the Shopify customer ID as the external ID.
 
- On any subsequent event where the metafield is present (such as customers/update or orders/create for an ecommerce.order_placed event), Braze automatically detects the mismatch and merges the temporary profile with the correct external ID.

This means temporary duplicate profiles are possible but self-correct automatically. You do not need to take manual action to merge these profiles.

### Step 4.2: Create an endpoint to retrieve your external ID

You must create a public endpoint that Braze can call to retrieve the external ID. This allows Braze to fetch the ID in scenarios where Shopify cannot provide the braze.external_id metafield directly.

#### Endpoint specifications

Method: GET

Braze sends the following parameters to your endpoint:

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 shopify_customer_id | 
 Yes | 
 String | 
 The Shopify customer ID. | 

 shopify_storefront | 
 Yes | 
 String | 
 The storefront name for the request. Ex: <storefront_name>.myshopify.com | 

 email_address | 
 No | 
 String | 
 The email address of the logged-in user. 

This field may be missing in certain webhook scenarios. Your endpoint logic should account for null values here (for example, fetch the email using the shopify_customer_id if your internal logic requires it). | 

#### Example endpoint

```

1

```
 | 
```
GET https://mystore.com/custom_id?shopify_customer_id=1234&[email protected]&shopify_storefront=dev-store.myshopify.com

```
 | 

#### Expected response

Braze expects a 200 status code returning the external ID JSON:

```

1
2
3

```
 | 
```
{
 "external_id": "my_external_id"
}

```
 | 

#### Validation

It is critical to validate that the shopify_customer_id and email_address (if present) match the customer values in Shopify. You can use the Shopify Admin API or Customer API to validate these parameters and retrieve the correct braze.external_id metafield.

#### Failure behavior and merging

Any status code other than 200 is considered a failure.

- Merge implications: If the endpoint fails (returns non-200 or times out), Braze cannot retrieve the external ID. Consequently, the merge between the Shopify user and the Braze user profile does not happen at that time.
 
- Retry logic: Braze may attempt standard immediate network retries, but if the failure persists, the merge is deferred until the next qualifying event (for example, the next time the user updates their profile or completes a checkout).
 
- Supportability: To support timely user merging, ensure your endpoint is highly available and handles the optional email_address field gracefully.

### Step 4.3: Input your external ID

Repeat Step 4, and enter your endpoint URL after selecting custom external ID as your Braze external ID type.

#### Considerations

- If your external ID isn’t generated when Braze sends a request to your endpoint, the integration will default to using the Shopify customer ID when the changeUser function is called. This step is crucial for merging the anonymous user profile with the identified user profile. As a result, there may be a temporary period during which different types of external IDs exist within your workspace.
 
- When the external ID is available in the braze.external_id metafield, the integration will prioritize and assign this external ID.

- If the Shopify customer ID was previously set as the Braze external ID, it will be replaced with the braze.external_id metafield value.

### Step 4.4: Collect your email or SMS opt-ins from Shopify (optional)

You have the option to collect your email or SMS marketing opt-ins from Shopify.

If you use the email or SMS channels, you can sync your email and SMS marketing opt-in states into Braze. If you sync email marketing opt-ins from Shopify, Braze will automatically create an email subscription group for all users associated with that specific store. You need to create a unique name for this subscription group.

note

As mentioned in Shopify overview, if you want to use a third-party capture form, your developers need to integrate Braze SDK code. This will let you capture the email address and global email subscription status from form submissions. Specifically, you need to implement and test these methods to your theme.liquid file:

- setEmail: Sets the email address on the user profile
 
- setEmailNotificationSubscriptionType: Updates the global email subscription status

## Step 5: Sync products (optional)

You can sync all products from your Shopify store to a Braze catalog for deeper messaging personalization. Automatic updates occur in near real-time so your catalog reflects up-to-date product details. To learn more, check out Shopify product sync.

## Step 6: Activate Channels (optional)

You can enable in-app messages without using a developer by configuring them in your setup.

note

Braze collects visitor information, such as email addresses and phone numbers, through in-browser messages. This information is sent to Shopify. This data enables merchants to recognize visitors to their store and create a more personalized shopping experience. For more details, refer to Visitor API.

### Supporting additional SDK channels

The Braze SDKs enable various messaging channels, including Content Cards.

#### Content Cards and Feature Flags

To add content cards or feature flags, you will need to collaborate with your developers to insert the necessary SDK code directly into your theme.liquid file. For detailed instructions, refer to Integrating the Braze SDK.

#### Web push notifications

Web push currently is not supported for the Shopify integration. If you’re interested in web push for the Shopify integration, submit product feedback.

## Step 7: Finish setup

- After you configure your setup, select Finish Setup.
 
- Enable the Braze app embed within your Shopify theme settings. Select Open Shopify to be redirected to your Shopify account to enable the app embed within your store’s theme settings.

- After you enable the app embed, your setup is complete!
Confirm you can view your integration settings, the status of initial data sync, and your active Shopify events. 

- 

New Stuff!
