---
url: https://www.braze.com/docs/partners/ecommerce/analytics_workflow/wunderkind
slug: docs__partners__ecommerce__analytics_workflow__wunderkind
title: "Wunderkind (Signals)"
description: "This reference article covers the Wunderkind Signals integration with Braze, including behavioral signals that trigger Canvas journeys, setup with the Canvas Entry API, the Canvas..."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Wunderkind (Signals)

Wunderkind is an eCommerce performance platform that uses proprietary Identity technology to recognize anonymous website visitors and resolve them to actionable email addresses. On average, Wunderkind scales identification from 3 to 5% of website traffic to 40 to 60%, enabling brands to trigger personalized, one-to-one messages at scale through their existing ESP.

This integration is maintained by Wunderkind. For support, visit support.wunderkind.co.

## About the integration

The Wunderkind Signals integration allows high-intent behavioral signals—such as cart abandonment, product abandonment, and price drops—to trigger real-time Canvas journeys in Braze. Wunderkind identifies anonymous users on your website, resolves their identity to a deliverable email address, and delivers a structured signal payload to Braze via the Canvas Entry API, initiating your pre-configured email flows automatically.

## Prerequisites

 Requirement | 
 Description | 

 Wunderkind account | 
 A Wunderkind account with Signals enabled is required. Contact your Wunderkind representative to confirm eligibility. | 

 Braze account | 
 A Braze account with Canvas access is required. The Wunderkind team must be granted a seat in your account. For full details, see Grant Wunderkind access to your Braze account. | 

 Braze REST API key | 
 You create a dedicated API key with specific permissions during setup (see Step 1). | 

 User identification | 
 Wunderkind typically resolves a consumer to Braze using user_alias with alias_label: "wknd_email_id" (often with the email as alias_name). Each /canvas/trigger/send recipient must include exactly one of external_user_id, user_alias, braze_id, or email (recipients object); if you use email, include prioritization. When you use user_alias, the profile must already exist in Braze before the trigger. Create or update users and aliases first with /users/track or /users/identify. For more information, see Limitations. | 

## How it works

When Wunderkind identifies a high-intent anonymous user and resolves their identity, it sends a signal payload to Braze using the /canvas/trigger/send endpoint, triggering the relevant Canvas journey for that user in real time.

For a full technical overview, see the Wunderkind Developer Portal.

## Integration

### Step 1: Create a Braze API key for Wunderkind

In your Braze dashboard:

- Go to Settings > API Keys and click Create New API Key.
 
- Give the key a descriptive name (for example, Wunderkind Signals).
 
- Grant the permissions listed in Grant Wunderkind access to your Braze account.
 
- Copy the API key to enter it in the Wunderkind platform in the next section.

note

For Wunderkind Signals, Braze REST API requests are authenticated with a REST API key, not with OAuth tokens. Create a dedicated API key in the dashboard and provide that key to Wunderkind.

### Step 2: Connect Braze to the Wunderkind platform

- Log into the Wunderkind platform and go to Integrations Hub.
 
- Select the Braze tile, then select Connect.
 
- Enter your Braze REST API key and select your cluster.
 
- Select Save.

### Step 3: Review new Braze assets

Upon activation, Wunderkind provisions new implementation assets in your Braze workspace based on the strategy aligned with your Wunderkind representative:

 Asset type | 
 Wunderkind creation method | 

 Content Blocks | 
 Automatic | 

 API-triggered Canvases | 
 Managed Service | 

 Tags, custom attributes, link templates | 
 Managed Service | 

### Step 4: Complete Canvas setup

For each Signals Canvas, build your email templates using Braze’s drag-and-drop editor or HTML.

- Wunderkind populates product and session data in each recipient’s context object on /canvas/trigger/send at send time.
 
- For in-depth instructions on how to use Liquid with that payload in your templates, see Complete Canvas setup in the Wunderkind Help Center.

### Step 5: Review Canvas eligibility

For each Signals Canvas, go to the Target Audience settings to review Wunderkind’s default entry audience and exit criteria.

- To ensure that you are not messaging your users too often, see User-centric rate limiting.
 
- Adjust settings to prevent users from continuing to receive Canvas messages after they make a purchase. For example, add the exception Make Purchase.
 
- Certain Signals Canvases are pre-configured with custom attribute filters for users to receive the highest-intent message possible.
 
- See Review Canvas eligibility in the Wunderkind Help Center for details on Canvas eligibility and priority.

### Step 6: Test and launch

Wunderkind conducts end-to-end QA before go-live:

- Confirm signals are delivering to the correct Canvas IDs without API errors.
 
- Verify context fields (product name, image, URL) are populating correctly in rendered email templates.
 
- See Test and launch Signals for Braze in the Wunderkind Help Center for instructions on previewing templates with mock Wunderkind products.

When QA passes, your Wunderkind implementation manager coordinates the production launch with your team.

## Canvas context payload

Wunderkind supports six signal types. Each delivers a distinct set of keys and values inside the context object for that recipient on /canvas/trigger/send (see Send Canvas messages using API-triggered delivery). The WkPurpose field identifies the signal type within that payload.

### Common fields (all Canvas types)

 Property | 
 Type | 
 Description | 

 Origin | 
 String | 
 Always "wunderkind" | 

 DataOnly | 
 String | 
 Always "Y" — indicates Wunderkind is acting as a data layer only; Braze executes the send | 

 UserType | 
 String | 
 "prospect" or "customer" | 

 WkChannel | 
 String | 
 Always "email" for this integration | 

 WkPurpose | 
 String | 
 Signal type identifier (see values per Canvas in this section) | 

 WKCouponCode | 
 String | 
 Coupon code, if applicable (empty string if not used) | 

 WKCouponPurpose | 
 String | 
 Description of coupon offer (empty string if not used) | 

 Items | 
 Array | 
 Array of product objects (see product fields in this section) | 

 WkOpen | 
 String | 
 Tracking pixel available for reporting purposes | 

### Product item fields

 Property | 
 Type | 
 Description | 

 WkCopy | 
 String | 
 Product name | 

 WkId | 
 String | 
 Product ID | 

 WkImageUrl | 
 String | 
 Product image URL | 

 WkUrl | 
 String | 
 Product detail page URL | 

 WkPrice | 
 String | 
 Original price (price drop Canvas only) | 

 WKSalePrice | 
 String | 
 Sale price (price drop Canvas only) | 

 WkQuantity | 
 String | 
 Units remaining (low stock Canvas only) | 

### Canvas-specific fields and WkPurpose values

 Canvas type | 
 WkPurpose value | 
 Additional fields | 

 Cart abandonment | 
 "cart abandonment" | 
 WkCartReplenUrl — URL to replenish the cart | 

 Product abandonment | 
 "product abandonment" | 
 — | 

 Category recap | 
 "category recap" | 
 WkCategoryUrl — URL to the browsed category | 

 Back in stock | 
 "back in stock" | 
 — | 

 Price drop | 
 "price drop" | 
 WkPrice, WKSalePrice on each item | 

 Low stock | 
 "low stock" | 
 WkQuantity on each item | 

### Example payloads

Each object in recipients must include exactly one of external_user_id, user_alias, braze_id, or email. For more information, see the Recipients object.

note

Each example uses one Braze recipient identifier. The first six use user_alias only; the last uses email with prioritization only. The example JSON omits the WkChannel key inside context so review tools do not confuse its value ("email") with Braze’s recipient email field. In production, include "WkChannel": "email" in context as documented in the Common fields (all Canvas types) table.

The following examples use user_alias with wknd_email_id, matching how Wunderkind resolves identities.

Cart abandonment example payload

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
{
 "canvas_id": "<your_canvas_id>",
 "recipients": [
 {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "wknd_email_id"
 },
 "context": {
 "Origin": "wunderkind",
 "DataOnly": "Y",
 "UserType": "prospect",
 "WkOpen": "https://example.com/cart",
 "WkPurpose": "cart abandonment",
 "WKCouponCode": "",
 "WKCouponPurpose": "",
 "WkCartReplenUrl": "https://example.com/cart/replenish",
 "Items": [
 {
 "WkCopy": "Product name",
 "WkId": "012345",
 "WkImageUrl": "https://example.com/image.jpg",
 "WkUrl": "https://example.com/product"
 }
 ]
 }
 }
 ]
}

```
 | 

Product abandonment example payload

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

```
 | 
```
{
 "canvas_id": "<your_canvas_id>",
 "recipients": [
 {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "wknd_email_id"
 },
 "context": {
 "Origin": "wunderkind",
 "DataOnly": "Y",
 "UserType": "prospect",
 "WkOpen": "https://example.com/product",
 "WkPurpose": "product abandonment",
 "WKCouponCode": "",
 "WKCouponPurpose": "",
 "Items": [
 {
 "WkCopy": "Product name",
 "WkId": "012345",
 "WkImageUrl": "https://example.com/image.jpg",
 "WkUrl": "https://example.com/product"
 }
 ]
 }
 }
 ]
}

```
 | 

Category recap example payload

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
{
 "canvas_id": "<your_canvas_id>",
 "recipients": [
 {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "wknd_email_id"
 },
 "context": {
 "Origin": "wunderkind",
 "DataOnly": "Y",
 "UserType": "prospect",
 "WkOpen": "https://example.com/category",
 "WkPurpose": "category recap",
 "WKCouponCode": "",
 "WKCouponPurpose": "",
 "WkCategoryUrl": "https://example.com/category",
 "Items": [
 {
 "WkCopy": "Product name",
 "WkId": "012345",
 "WkImageUrl": "https://example.com/image.jpg",
 "WkUrl": "https://example.com/product"
 }
 ]
 }
 }
 ]
}

```
 | 

Back in stock example payload

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

```
 | 
```
{
 "canvas_id": "<your_canvas_id>",
 "recipients": [
 {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "wknd_email_id"
 },
 "context": {
 "Origin": "wunderkind",
 "DataOnly": "Y",
 "UserType": "prospect",
 "WkOpen": "https://example.com/product",
 "WkPurpose": "back in stock",
 "WKCouponCode": "",
 "WKCouponPurpose": "",
 "Items": [
 {
 "WkCopy": "Product name",
 "WkId": "012345",
 "WkImageUrl": "https://example.com/image.jpg",
 "WkUrl": "https://example.com/product"
 }
 ]
 }
 }
 ]
}

```
 | 

Price drop example payload

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
{
 "canvas_id": "<your_canvas_id>",
 "recipients": [
 {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "wknd_email_id"
 },
 "context": {
 "Origin": "wunderkind",
 "DataOnly": "Y",
 "UserType": "prospect",
 "WkOpen": "https://example.com/product",
 "WkPurpose": "price drop",
 "WKCouponCode": "",
 "WKCouponPurpose": "",
 "Items": [
 {
 "WkCopy": "Product name",
 "WkId": "012345",
 "WkImageUrl": "https://example.com/image.jpg",
 "WkUrl": "https://example.com/product",
 "WkPrice": "49.99",
 "WKSalePrice": "39.99"
 }
 ]
 }
 }
 ]
}

```
 | 

Low stock example payload

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
{
 "canvas_id": "<your_canvas_id>",
 "recipients": [
 {
 "user_alias": {
 "alias_name": "[email protected]",
 "alias_label": "wknd_email_id"
 },
 "context": {
 "Origin": "wunderkind",
 "DataOnly": "Y",
 "UserType": "prospect",
 "WkOpen": "https://example.com/product",
 "WkPurpose": "low stock",
 "WKCouponCode": "",
 "WKCouponPurpose": "",
 "Items": [
 {
 "WkCopy": "Product name",
 "WkId": "012345",
 "WkImageUrl": "https://example.com/image.jpg",
 "WkUrl": "https://example.com/product",
 "WkQuantity": "1"
 }
 ]
 }
 }
 ]
}

```
 | 

Email identifier example (alternate)

If you trigger the Canvas with Braze’s email field instead of user_alias, the recipient must include only email and prioritization (see Send Canvas messages using API-triggered delivery). The context object matches the other examples.

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

```
 | 
```
{
 "canvas_id": "<your_canvas_id>",
 "recipients": [
 {
 "email": "[email protected]",
 "prioritization": ["unidentified", "most_recently_updated"],
 "context": {
 "Origin": "wunderkind",
 "DataOnly": "Y",
 "UserType": "prospect",
 "WkOpen": "https://example.com/product",
 "WkPurpose": "product abandonment",
 "WKCouponCode": "",
 "WKCouponPurpose": "",
 "Items": [
 {
 "WkCopy": "Product name",
 "WkId": "012345",
 "WkImageUrl": "https://example.com/image.jpg",
 "WkUrl": "https://example.com/product"
 }
 ]
 }
 }
 ]
}

```
 | 

### Example Liquid usage

When Wunderkind calls /canvas/trigger/send, the keys and values you pass in each recipient’s context object become Canvas entry data. In Message steps, reference them with the context Liquid namespace. An example is {{context.${WkPurpose}}} as described in Canvas context object and Message. No extra configuration is required beyond using the correct Liquid syntax.

Do not nest Braze output tags inside the for tag condition. Assign the Items array from context to a variable first, then loop, as described in Using Liquid. The assign line uses Braze’s Canvas entry form {{context.${Items}}} (see Supported personalization tags).

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
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
 <tr>
 <td>
 <a href="{{ item.WkUrl }}">
 <img src="{{ item.WkImageUrl }}" />
 <p>{{ item.WkCopy }}</p>
 </a>
 </td>
 </tr>
{% endfor %}

```
 | 

## Reporting

Wunderkind ingests performance data from Braze using Braze Currents, which streams raw events to Google Cloud Storage. Wunderkind then normalizes and aggregates these events against the originating signal for 1:1 attribution reporting.

The following metrics will be available soon in the Wunderkind reporting dashboard:

 Metric | 
 Source | 

 Delivered sends | 
 Braze Currents | 

 Email opens | 
 Braze Currents | 

 Clicks | 
 Braze Currents | 

 Conversions | 
 Braze Currents (event defined at setup) | 

 Unsubscribes | 
 Braze Currents | 

## Limitations

- No suppression/opt-out sync. Suppression must be managed natively in Braze. Note: For existing Wunderkind customers migrating to Braze Signals, Wunderkind works with your team to preserve your current setup.
 
- Email channel only. SMS is not currently supported through this integration.
 
- User profile must exist before the Canvas trigger. /canvas/trigger/send with a user_alias recipient resolves only existing Braze profiles that already have that alias. You cannot use send_to_existing_only with aliases, and the Canvas trigger does not create a net-new profile from the alias alone. The user must be created or updated and the wknd_email_id alias set first (for example, using /users/track or /users/identify). Wunderkind may wait briefly after that upsert so Braze can finish processing before firing the trigger.
 
- Email as the identifier. If the Canvas trigger identifies the recipient with email instead of user_alias, include prioritization on that recipient object, as required by Braze.

## Additional resources

- Wunderkind Help Center — Signals for Braze Overview
 
- Wunderkind Developer Portal — Integration Overview
 
- Send Canvas messages using API-triggered delivery
 
- Canvas context object
 
- Braze Currents

- 

New Stuff!
