---
url: https://www.braze.com/docs/partners/ecommerce/shopify/shopify_custom_integration
slug: docs__partners__ecommerce__shopify__shopify_custom_integration
title: "Shopify custom integration setup"
description: "This reference article covers how to connect with a Shopify Hydrogen store or any headless Shopify store by using a custom storefront."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Shopify custom integration setup

This page walks you through how to integrate Braze with a Shopify Hydrogen store or any headless Shopify store by using a custom storefront.

This guide uses Shopify’s Hydrogen framework as an example. However, you can follow a similar approach if your brand uses Shopify for the backend of your store with a “headless” front-end setup.

To integrate your Shopify headless store with Braze, you need to complete these two goals:

- Initialize and load the Braze Web SDK to enable onsite tracking

 Manually add code into your Shopify website to enable Braze onsite tracking. By implementing the Braze SDK on your Shopify headless store, you can track onsite activities, including sessions, anonymous user behavior, pre-checkout shopper actions, and any custom events or custom attributes you choose to include with your development team. You can also add any channels supported by the SDKs, such as in-app messages or Content Cards.

- Install the Braze Shopify integration

 After you connect your Shopify store to Braze, you’ll gain access to customer, checkout, order, and product data through Shopify webhooks.

important

Before starting your integration, confirm you have correctly set up the checkout subdomain for your Shopify storefront. For more information, refer to Migrate from the online store to Hydrogen.

 If this setup isn’t done correctly, Braze can’t process Shopify checkout webhooks. It also won’t be possible to test the integration in a local development environment, because that relies on a shared domain between your storefront and the checkout page.

To complete these goals, follow these steps:

## Initialize and load the Braze Web SDK

### Step 1: Select a website app and copy SDK credentials

Before you add code to your Hydrogen storefront, connect your Shopify store and start custom setup onboarding. If you haven’t connected your store yet, complete Connect your Shopify store, then continue with Enable Braze SDKs and select Custom setup.

In the custom setup flow, Braze prompts you to select the website app for your headless storefront:

- Select an existing website app or create a new one. You can name the app anything except Shopify, which Braze reserves for the standard Shopify integration path.
 
- Braze displays the selected app’s API key and base URL (your SDK endpoint) in the onboarding step. Select Copy for each value—you don’t need to open Settings > App Settings.
 
- Use the copied API key as BRAZE_API_KEY and the SDK endpoint as BRAZE_API_URL in your Shopify environment variables (Step 2).

After you connect the store, you can rename the selected website app in Settings > App Settings. You can’t delete the app while it’s connected to your Shopify integration.

warning

Use the API key for the website app you selected during onboarding. If your Hydrogen environment uses a different API key than the one connected to your Shopify integration, Braze may create duplicate users and SDK methods may not work as expected.

### Step 2: Add subdomain and environmental variables

- Set up your Shopify subdomain to redirect traffic from your online store to Hydrogen.
 
- Add a callback URI for login. (The URI will automatically be added when the domain is added.)
 
- Set up your Shopify environment variables:

- Create two environment variables using the API key and SDK endpoint you copied during custom setup onboarding in Step 1.

- BRAZE_API_KEY
 
- BRAZE_API_URL

### Step 3: Enable onsite tracking

The first step is to initialize the Braze Web SDK. We recommend doing that by installing our NPM package:

```

1
2
3

```
 | 
```
npm install --save @braze/web-sdk@6.8.0
# or, using yarn:
# yarn add @braze/web-sdk

```
 | 

important

The minimum supported Braze Web SDK version is 5.4.0. For Shopify custom integrations (including headless storefronts), you receive notifications when new SDK versions are available, but you manage upgrades on your side by updating both your storefront code and the SDK version in integration settings.

Then, include this setting as a top-level key in your vite.config.js file:

```

1
2
3

```
 | 
```
optimizeDeps: {
 exclude: ['@braze/web-sdk']
}

```
 | 

After installing the NPM package, you must initialize the SDK within a useEffect hook inside the Layout component. Depending on your Hydrogen version, this component may be located in either the root.jsx or layout.jsx file:

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

```
 | 
```
// Add these imports
import * as braze from "@braze/web-sdk";
import { useEffect } from 'react';

export function Layout({children}) {
 const nonce = useNonce();
 // @type {RootLoader} 
 const data = useRouteLoaderData('root');
 
 // Add useEffect call to initialize Braze SDK
 useEffect(() => {
 if(!braze.isInitialized()) {
 braze.initialize(data.brazeApiKey, {
 baseUrl: data.brazeApiUrl,
 });
 braze.openSession() 
 }
 }, [data]) 

 return (...);
}

```
 | 

The values data.brazeApiKey and data.brazeApiUrl need to be included in the component loader using the environment variables created in Step 2:

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

```
 | 
```
export async function loader(args) {
 // Start fetching non-critical data without blocking time to first byte
 const deferredData = loadDeferredData(args);

 // Await the critical data required to render initial state of the page
 const criticalData = await loadCriticalData(args);

 const {storefront, env} = args.context;

 return {
 ...deferredData,
 ...criticalData,
 publicStoreDomain: env.PUBLIC_STORE_DOMAIN,
 // Add the two properties below to the returned value
 brazeApiKey: env.BRAZE_API_KEY,
 brazeApiUrl: env.BRAZE_API_URL,
 shop: getShopAnalytics({
 storefront,
 publicStorefrontId: env.PUBLIC_STOREFRONT_ID,
 }),
 consent: {
 checkoutDomain: env.PUBLIC_CHECKOUT_DOMAIN,
 storefrontAccessToken: env.PUBLIC_STOREFRONT_API_TOKEN,
 withPrivacyBanner: false,
 // Localize the privacy banner
 country: args.context.storefront.i18n.country,
 language: args.context.storefront.i18n.language,
 },
 };
}

```
 | 

note

Content security policies (usually located in the entry.server.jsx Hydrogen file) can impact the functionality of Braze scripts both in local and production environments. We suggest testing through preview builds sent to Shopify through Oxygen or custom deployments. If you encounter issues, you’ll need to configure your CSP to allow our JavaScript to function.

### Step 4: Add a Shopify Account Login event

Track when a shopper signs into their account and syncs their user information to Braze. This includes calling our changeUser method to identify customers with a Braze external ID.

note

We currently don’t have guidance to support a custom Braze external ID. If you require this for your integration now, contact your customer success manager.

Before you start, make sure you’ve set up the callback URIs for the customer login to work within Hydrogen. For more information, refer to Using the Customer Account API with Hydrogen.

- After setting up the callback URIs, define a function for calling the Braze SDK. Create a new file (such as Tracking.jsx) and import it from your components:

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

```
 | 
```
import * as braze from "@braze/web-sdk";

export function trackCustomerLogin(customerData, storefrontUrl) {
 const customerId = customerData.id.substring(customerData.id.lastIndexOf('/') + 1)
 const customerSessionKey = `ab.shopify.shopify_customer_${customerId}`;
 const alreadySetCustomerInfo = sessionStorage.getItem(customerSessionKey);
 
 if(!alreadySetCustomerInfo) {
 const user = braze.getUser()

 // To use Shopify customer ID as Braze External ID, use:
 // braze.changeUser(customerId)

 // To use Shopify customer email as Braze External ID, use:
 // braze.changeUser(customerData.emailAddress?.emailAddress)
 // To use hashing for email addresses, apply hashing before calling changeUser

 // To use your own custom ID as the Braze External ID, pass that value to the changeUser call.

 user.setFirstName(customerData.firstName);
 user.setLastName(customerData.lastName);
 if(customerData.emailAddress.emailAddress) {
 user.setEmail(customerData.emailAddress?.emailAddress);
 }

 if(customerData.phoneNumber?.phoneNumber) {
 user.setPhoneNumber(customerData.phoneNumber?.phoneNumber);
 }
 braze.logCustomEvent(
 "shopify_account_login",
 { source: storefrontUrl }
 )
 sessionStorage.setItem(customerSessionKey, customerId);
 }
}

```
 | 

- In the same useEffect hook that initializes the Braze SDK, add the call to this function:

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

```
 | 
```
import { trackCustomerLogin } from './Tracking';

export function Layout({children}) {
 const nonce = useNonce();
 // @type {RootLoader}
 const data = useRouteLoaderData('root');

 useEffect(() => {
 if(!braze.isInitialized()) {
 braze.initialize(data.brazeApiKey, {
 baseUrl: data.brazeApiUrl,
 enableLogging: true,
 });
 braze.openSession() 
 }

 // Add call to trackCustomerLogin function
 data.isLoggedIn.then((isLoggedIn) => {
 if(isLoggedIn) {
 trackCustomerLogin(data.customerData, data.publicStoreDomain)
 }
 })

 }, [data])

```
 | 

- Fetch the customer email address and phone number in your Customer API GraphQL query, located in the file app/graphql/customer-account/CustomerDetailsQuery.js:

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

```
 | 
```
export const CUSTOMER_FRAGMENT = `#graphql
 fragment Customer on Customer {
 id
 firstName
 lastName
 emailAddress {
 emailAddress
 }
 phoneNumber {
 phoneNumber
 }
 defaultAddress {
 ...Address
 }
 addresses(first: 6) {
 nodes {
 ...Address
 }
 }
 }
 fragment Address on CustomerAddress {
 id
 formatted
 firstName
 lastName
 company
 address1
 address2
 territoryCode
 zoneCode
 city
 zip
 phoneNumber
 }
`;

```
 | 

- Finally, load the customer data in your loader function:

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
42
43
44
45
46

```
 | 
```
// Add import for GraphQL Query 
import { CUSTOMER_DETAILS_QUERY } from './graphql/customer-account/CustomerDetailsQuery';

export async function loader(args) {
 // Start fetching non-critical data without blocking time to first byte
 const deferredData = loadDeferredData(args);

 // Await the critical data required to render initial state of the page
 const criticalData = await loadCriticalData(args);

 const {storefront, env} = args.context;

 // Add GraphQL call to Customer API
 const isLoggedIn = await deferredData.isLoggedIn;
 let customerData;
 if (isLoggedIn) {
 const { data, errors } = await args.context.customerAccount.query(
 CUSTOMER_DETAILS_QUERY,
 );
 customerData = data.customer
 } else {
 customerData = {}
 }

 return {
 ...deferredData,
 ...criticalData,
 publicStoreDomain: env.PUBLIC_STORE_DOMAIN,
 brazeApiKey: env.BRAZE_API_KEY,
 brazeApiUrl: env.BRAZE_API_URL,
 // Add the property below to the returned value 
 customerData: customerData,
 shop: getShopAnalytics({
 storefront,
 publicStorefrontId: env.PUBLIC_STOREFRONT_ID,
 }),
 consent: {
 checkoutDomain: env.PUBLIC_CHECKOUT_DOMAIN,
 storefrontAccessToken: env.PUBLIC_STOREFRONT_API_TOKEN,
 withPrivacyBanner: false,
 // Localize the privacy banner
 country: args.context.storefront.i18n.country,
 language: args.context.storefront.i18n.language,
 },
 };
}

```
 | 

### Step 5: Add tracking for Product Viewed and Cart Updated events

#### Product Viewed events

- Add this function to your Tracking.jsx file:

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

```
 | 
```
export function trackProductViewed(product, storefrontUrl) {
 const eventData = {
 product_id: product.id.substring(product.id.lastIndexOf('/') + 1),
 product_name: product.title,
 variant_id: product.selectedOrFirstAvailableVariant.id.substring(product.selectedOrFirstAvailableVariant.id.lastIndexOf('/') + 1),
 image_url: product.selectedOrFirstAvailableVariant.image?.url,
 product_url: `${storefrontUrl}/products/${product.handle}`,
 price: product.selectedOrFirstAvailableVariant.price.amount,
 currency: product.selectedOrFirstAvailableVariant.price.currencyCode,
 source: storefrontUrl,
 type: ["price_drop", "back_in_stock"],
 metadata: {
 sku: product.selectedOrFirstAvailableVariant.sku
 }

 }
 braze.logCustomEvent(
 "ecommerce.product_viewed",
 eventData 
 )
}

```
 | 

- To call the prior function whenever a user visits a product page, add a useEffect hook to the Product component within the file app/routes/products.$handle.jsx:

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

```
 | 
```
import { trackProductViewed } from '~/tracking';
import { useEffect } from 'react';

export default function Product() {
 // @type {LoaderReturnData} 
 // retrieve storefrontUrl to be passed into trackProductViewed 
 const {product, storefrontUrl} = useLoaderData();
 
 // Add useEffect hook for tracking product_viewed event 
 useEffect(() => {
 trackProductViewed(product, storefrontUrl)
 }, [])

 return (...)
}

```
 | 

- Add the value for “storefrontUrl” (because it’s not in the component loader by default):

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

```
 | 
```
async function loadCriticalData({context, params, request}) {
 const {handle} = params;
 const {storefront} = context;

 if (!handle) {
 throw new Error('Expected product handle to be defined');
 }

 const [{product}] = await Promise.alll([
 storefront.query(PRODUCT_QUERY, {
 variables: {handle, selectedOptions: getSelectedProductOptions(request)},
 }),
 // Add other queries here, so that they are loaded in parallel
 ]);

 if (!product?.id) {
 throw new Response(null, {status: 404});
 }

 return {
 product,
 // Add this property to the returned value
 storefrontUrl: context.env.PUBLIC_STORE_DOMAIN,
 };
}

```
 | 

#### Cart Updated events

important

For this integration, the user alias must use the following format so that Braze can match webhooks to the correct user profile:

- alias_label: shopify_cart_${cartToken}
 
- alias_name: shopify_cart_token

- Define functions for tracking the cart_updated event and setting the cart token:

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
export function trackCartUpdated(cart, storefrontUrl) {
 const eventData = {
 cart_id: cart.id,
 total_value: cart.cost.totalAmount.amount,
 currency: cart.cost.totalAmount.currencyCode,

 products: cart.lines.nodes.map((line) => {
 return {
 product_id: line.merchandise.product.id.toString(),
 product_name: line.merchandise.product.title,
 variant_id: line.merchandise.id.toString(),
 image_url: line.merchandise.image.url,
 product_url: `${storefrontUrl}/products/${line.merchandise.product.handle}`,
 quantity: Number(line.quantity),
 price: Number(line.cost.totalAmount.amount / Number(line.quantity))
 }
 }),
 source: storefrontUrl,
 metadata: {},
 };
 
 braze.logCustomEvent(
 "ecommerce.cart_updated",
 eventData 
 )
}

export function setCartToken(cart) {
 const cartId = cart.id.substring(cart.id.lastIndexOf('/') + 1) 
 const cartToken = cartId.substring(0, cartId.indexOf("?key="));
 if (cartToken) {
 const cartSessionKey = `ab.shopify.shopify_cart_${cartToken}`;
 const alreadySetCartToken = sessionStorage.getItem(cartSessionKey);

 if (!alreadySetCartToken) {
 braze.getUser().addAlias("shopify_cart_token", `shopify_cart_${cartToken}`)
 braze.requestImmediateDataFlush();
 sessionStorage.setItem(cartSessionKey, cartToken);
 }
 }
}

```
 | 

- Return the cart object from the fetcher action so Braze can access its properties by going to your app/routes/cart.jsx file an adding the following to the action
function:

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

```
 | 
```
export async function action({request, context}) {
 const {cart} = context;

 ...

 switch (action) {
 case CartForm.ACTIONS.LinesAdd:
 result = await cart.addLines(inputs.lines);
 break;
 ... 
 }

 const cartId = result?.cart?.id;
 const headers = cartId ? cart.setCartId(result.cart.id) : new Headers();
 const {cart: cartResult, errors, warnings} = result;

 const redirectTo = formData.get('redirectTo') ?? null;
 if (typeof redirectTo === 'string') {
 status = 303;
 headers.set('Location', redirectTo);
 }
 
 return data(
 {
 cart: cartResult,
 // Add these two properties to the returned value 
 updatedCart: await cart.get(),
 storefrontUrl: context.env.PUBLIC_STORE_DOMAIN,
 errors,
 warnings,
 analytics: {
 cartId,
 },
 },
 {status, headers},
 );
}

```
 | 

For more information on Remix fetchers, refer to useFetcher.

- Hydrogen stores usually define a CartForm component that manages the cart object state, which gets used when adding, removing, and changing quantity of items in a cart. Add another useEffect hook in the AddToCartButton component that will call the trackCartUpdated function whenever the form fetcher state changes (whenever the user cart is updated):

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
42
43
44
45
46

```
 | 
```
// Add imports 
import { trackCartUpdated, setCartToken } from '~/tracking';
import { useEffect } from 'react';
import { useFetcher } from '@remix-run/react';

export function AddToCartButton({
 analytics,
 children,
 disabled,
 lines,
 onClick,
}) {
 
 // Define a new Fetcher to be used for tracking cart updates 
 const fetcher = useFetcher({ key: "cart-fetcher" });
 
 // Add useEffect hook for tracking cart_updated event and setting cart token alias
 useEffect(() => {
 if(fetcher.state === "idle" && fetcher.data) {
 trackCartUpdated(fetcher.data.updatedCart, fetcher.data.storefrontUrl)
 setCartToken(fetcher.data.updatedCart);
 }
 }, [fetcher.state, fetcher.data])

 // Add the fetcherKey prop to the CartForm component
 return (
 <CartForm route="/cart" inputs= fetcherKey="cart-fetcher" action={CartForm.ACTIONS.LinesAdd}>
 {(fetcher) => (
 <>
 <input
 name="analytics"
 type="hidden"
 value={JSON.stringify(analytics)}
 />
 <button
 type="submit"
 onClick={onClick}
 disabled={disabled ?? fetcher.state !== 'idle'}
 >
 {children}
 </button>
 </>
 )}
 </CartForm>
 );
}

```
 | 

- Use the same fetcherKey for the actions responsible for updating an existing product from your cart. Add the following to the CartLineRemoveButton and CartLineUpdateButton components (located by default in the file app/components/CartLineItem.jsx):

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

```
 | 
```
function CartLineRemoveButton({lineIds, disabled}) {
 // Add the fetcherKey prop to the CartForm component
 return (
 <CartForm
 fetcherKey="cart-fetcher"
 route="/cart"
 action={CartForm.ACTIONS.LinesRemove}
 inputs=
 >
 <button disabled={disabled} type="submit">
 Remove
 </button>
 </CartForm>
 );
}

function CartLineUpdateButton({children, lines}) {
 // Add the fetcherKey prop to the CartForm component
 return (
 <CartForm
 route="/cart"
 fetcherKey="cart-fetcher"
 action={CartForm.ACTIONS.LinesUpdate}
 inputs=
 >
 {children}
 </CartForm>
 );
}

```
 | 

## Install the Braze Shopify integration

### Step 1: Connect your Shopify store

Go to the Shopify partner page to start your setup. First, select Begin Setup to install the Braze application from the Shopify App Store. Follow the guided steps to complete the installation process.

### Step 2: Enable Braze SDKs

For Shopify Hydrogen or headless stores, select the Custom setup option.

Custom setup includes a website app picker. Select or create the app that powers your storefront, then copy the API key and SDK endpoint shown in the onboarding step. For details, see Step 1: Select a website app and copy SDK credentials.

Before continuing with the onboarding process, confirm that you’ve added the Braze SDK to your Shopify website using those credentials.

### Step 3: Track Shopify data

Enhance your integration by adding more Shopify events and attributes, which will be powered by Shopify webhooks. For detailed information on the data tracked through this integration, refer to Shopify Data Features.

### Step 4: Historical backfill (optional)

Through the custom setup, you can optionally include the same historical Shopify data load as the standard integration: order events from the past 90 days and user profiles from the past year, each counted back from the date you complete your integration. To include this initial data load, select the checkbox for the initial data load option.

If you prefer to perform the backfill later, you can complete the initial setup now and return to this step at a later time.

For the full list of data in the initial load, revenue reporting behavior, and monitoring the sync, see Historical backfill.

### Step 5: Custom data tracking setup (advanced)

With the Braze SDKs, you can track custom events or custom attributes that go beyond supported data for this integration. Custom events capture unique interactions in your store, such as:

 Step 5: Custom data tracking setup (advanced)

 Custom events | 
 Custom attributes | 

- Using a custom discount code
 
- Interacting with a personalized product recommendation
 
 | 

- Favorite brands or products
 
- Preferred shopping categories
 
- Membership or loyalty status
 
 | 

The SDK must be initialized (listening for activity) on a user’s device to log events or custom attributes. To learn more about logging custom data, refer to User object and logCustomEvent.

### Step 6: Configure how you manage users (optional)

Select your external_id type from the dropdown.

important

Using an email address or a hashed email address as your Braze external ID can help simplify identity management across your data sources. However, it’s important to consider the potential risks to user privacy and data security.

- Guessable Information: Email addresses are easily guessable, making them vulnerable to attacks.
 
- Risk of Exploitation: If a malicious user alters their web browser to send someone else’s email address as their external ID, they could potentially access sensitive messages or account information.

By default, Braze automatically converts emails from Shopify to lowercase before using them as the external ID. If you’re using email or hashed email as your external ID, confirm that your email addresses are also converted to lowercase before you assign them as your external ID or before hashing them from other data sources. This helps prevent discrepancies in external IDs and avoid creating duplicate user profiles in Braze.

note

The next steps depend on your external ID selection:

- If you selected a custom external ID type: Complete steps 6.1—6.3 to set up your custom external ID configuration.
 
- If you selected Shopify customer ID, email, or hashed email: Skip steps 6.1—6.3 and continue directly to step 6.4.

#### Step 6.1: Create the braze.external_id metafield

- In your Shopify admin panel, go to Settings > Metafields.
 
- Select Customers > Add definition.
 
- For Namespace and key, enter braze.external_id.
 
- For Type, select ID Type.

After the metafield is created, populate it for your customers. We recommend the following approaches:

- Listen to customer creation webhooks: Set up a webhook to listen for customer/create events. This allows you to write the metafield when a new customer is created.
 
- Backfill existing customers: Use the Admin API or Customer API to backfill the metafield for previously created customers.

#### Step 6.2: Create an endpoint to retrieve your external ID

You must create a public endpoint that Braze can call to retrieve the external ID. This allows Braze to fetch the ID in scenarios where Shopify cannot provide the braze.external_id metafield directly.

##### Endpoint specifications

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

##### Example endpoint

```

1

```
 | 
```
GET https://mystore.com/custom_id?shopify_customer_id=1234&[email protected]&shopify_storefront=dev-store.myshopify.com

```
 | 

##### Expected response

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

##### Validation

It is critical to validate that the shopify_customer_id and email_address (if present) match the customer values in Shopify. You can use the Shopify Admin API or Customer API to validate these parameters and retrieve the correct braze.external_id metafield.

##### Failure behavior and merging

Any status code other than 200 is considered a failure.

- Merge implications: If the endpoint fails (returns non-200 or times out), Braze cannot retrieve the external ID. Consequently, the merge between the Shopify user and the Braze user profile does not happen at that time.
 
- Retry logic: Braze may attempt standard immediate network retries, but if the failure persists, the merge is deferred until the next qualifying event (for example, the next time the user updates their profile or completes a checkout).
 
- Supportability: To support timely user merging, ensure your endpoint is highly available and handles the optional email_address field gracefully.

#### Step 6.3: Input your external ID

Repeat Step 6, and enter your endpoint URL after selecting custom external ID as your Braze external ID type.

##### Considerations

- If your external ID isn’t generated when Braze sends a request to your endpoint, the integration will default to using the Shopify customer ID when the changeUser function is called. This step is crucial for merging the anonymous user profile with the identified user profile. As a result, there may be a temporary period during which different types of external IDs exist within your workspace.
 
- When the external ID is available in the braze.external_id metafield, the integration will prioritize and assign this external ID.

- If the Shopify customer ID was previously set as the Braze external ID, it will be replaced with the braze.external_id metafield value.

#### Step 6.4: Collect your email or SMS opt-ins from Shopify (optional)

You have the option to collect your email or SMS marketing opt-ins from Shopify.

If you use the email or SMS channels, you can sync your email and SMS marketing opt-in states into Braze. If you sync email marketing opt-ins from Shopify, Braze will automatically create an email subscription group for all users associated with that specific store. You need to create a unique name for this subscription group.

note

As mentioned in Shopify overview, if you want to use a third-party capture form, your developers need to integrate Braze SDK code. This will let you capture the email address and global email subscription status from form submissions. Specifically, you need to implement and test these methods to your theme.liquid file:

- setEmail: Sets the email address on the user profile
 
- setEmailNotificationSubscriptionType: Updates the global email subscription status

### Step 7: Sync products (optional)

You can sync all products from your Shopify store to a Braze catalog for deeper messaging personalization. Automatic updates occur in near real-time so your catalog always reflects the latest product details. To learn more, check out Shopify product sync.

### Step 8: Activate channels

To activate in-app messages, Content Cards, and Feature Flags using the Shopify direct integration, add each channel to your SDK. Follow the documentation links provided for each channel:

- In-app messages: For enabling in-app messages for lead capture form use cases, refer to In-app messages.
 
- Content Cards: For enabling Content Cards for inbox or website banner use cases, refer to Content Cards.
 
- Feature flags: For enabling Feature Flags for site experimentation use cases, refer to Feature flags.

### Step 9: Finish setup

After you’ve gone through all the steps, select Finish Setup to return to the partner page. Then, enable the Braze app embed in your Shopify admin page as indicated by the banner that displays.

#### Example code

shopify-hydrogen-example is an example Hydrogen app that contains all the code covered in the prior steps.

- 

New Stuff!
