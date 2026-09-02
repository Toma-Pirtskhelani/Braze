---
url: https://www.braze.com/docs/developer_guide/analytics/logging_purchases
slug: docs__developer_guide__analytics__logging_purchases
title: "Log purchases"
description: "Learn how to log purchases through the Braze SDK."
section: developer_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Log purchases

Learn how to log in-app purchases through the Braze SDK, so you can determine your revenue over-time and across sources. This lets you segment users based on their lifetime value using custom events, custom attributes, and purchase events.

note

For wrapper SDKs not listed, use the relevant native Android or Swift method instead.

Any non-USD currency reported will display in Braze in USD based on the exchange rate on the date it was reported. For dashboard conversion, caching, and exchange rate refresh timing, see Currency conversion. To prevent conversion, log purchases with USD as the currency code.

## Logging purchases and revenue

To log purchases and revenue, call logPurchase() after a successful purchase in your app. If the product Identifier is empty, the purchase will not be logged to Braze.

- web
 
- android
 
- swift
 
- cordova
 
- flutter
 
- react native
 
- roku
 
- unity

For a standard Web SDK implementation, you can use the following method:

```

1

```
 | 
```
braze.logPurchase(product_id, price, "USD", quantity);

```
 | 

If you’d like to use Google Tag Manager instead, you can use the Purchase tag type to call the logPurchase method. Use this tag to track purchases to Braze, optionally including purchase properties. To do so:

- The Product ID and Price fields are required.
 
- Use the Add Row button to add purchase properties.

- java
 
- kotlin

```

1
2
3
4
5
6

```
 | 
```
Braze.getInstance(context).logPurchase(
 String productId,
 String currencyCode,
 BigDecimal price,
 int quantity
);

```
 | 

```

1
2
3
4
5
6

```
 | 
```
Braze.getInstance(context).logPurchase(
 productId: String,
 currencyCode: String,
 price: BigDecimal,
 quantity: Int
)

```
 | 

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)

```
 | 

```

1
2
3

```
 | 
```
[AppDelegate.braze logPurchase:"product_id"
 currency:@"USD"
 price:price];

```
 | 

```

1
2
3

```
 | 
```
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);

```
 | 

```

1

```
 | 
```
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);

```
 | 

```

1

```
 | 
```
Braze.logPurchase(productId, price, currencyCode, quantity, properties);

```
 | 

```

1

```
 | 
```
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)

```
 | 

```

1

```
 | 
```
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));

```
 | 

warning

productID can only have a maximum of 255 characters. Additionally, if the product identifier is empty, the purchase will not be logged to Braze.

### Adding properties

You can add metadata about purchases by passing a Dictionary populated with Int, Double, String, Bool, or Date values.

- web
 
- android
 
- swift
 
- cordova
 
- flutter
 
- react native
 
- roku
 
- unity

For a standard Web SDK implementation, you can use the following method:

```

1

```
 | 
```
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});

```
 | 

If your site logs purchases using the standard eCommerce event data layer item to Google Tag Manager, then you can use the E-commerce Purchase tag type. This action type will log a separate “purchase” in Braze for each item sent in the list of items.

You can also specify additional property names you want to include as purchase properties by specifying their keys in the Purchase properties list. Note that Braze will look within the individual item that is being logged for any purchase properties you add to the list.

For example, given the following eCommerce payload:

```

1
2
3
4
5
6
7

```
 | 
```
items: [{
 item_name: "5 L WIV ECO SAE 5W/30",
 item_id: "10801463",
 price: 24.65,
 item_brand: "EUROLUB",
 quantity: 1
}]

```
 | 

If you only want item_brand and item_name to be passed as purchase properties, then just add those two fields to the purchase properties table. If you don’t supply any properties, then no purchase properties will be sent in the logPurchase call to Braze.

- java
 
- kotlin

```

1
2
3

```
 | 
```
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);

```
 | 

```

1
2
3

```
 | 
```
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)

```
 | 

- swift
 
- objective-c

```

1
2

```
 | 
```
let purchaseProperties = ["key": "value"]
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price, properties: purchaseProperties)

```
 | 

```

1
2
3
4
5

```
 | 
```
NSDictionary *purchaseProperties = @{@"key": @"value"};
[AppDelegate.braze logPurchase:@"product_id"
 currency:@"USD"
 price:price
 properties:purchaseProperties];

```
 | 

```

1
2
3

```
 | 
```
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);

```
 | 

```

1

```
 | 
```
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});

```
 | 

```

1

```
 | 
```
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });

```
 | 

```

1

```
 | 
```
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})

```
 | 

```

1
2
3
4
5

```
 | 
```
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
 { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);

```
 | 

### Adding quantity

By default, quantity is set to 1. However, you can add a quantity to your purchases if customers make the same purchase multiple times in a single checkout. To add a quantity, pass an Int value to quantity.

### Using the REST API

You can also use our REST API to record purchases. For more information, refer to User Data Endpoints.

## Logging orders

If you want to log purchases at the order level instead of the product level, you can use order name or order category as the product_id. Refer to our purchase object specification to learn more.

## Reserved keys

The following keys are reserved and cannot be used as purchase properties:

- time
 
- product_id
 
- quantity
 
- event_name
 
- price
 
- currency

## Supported currencies

Braze supports the following currency symbols. Any other currency symbol you provide logs a warning and the purchase is not logged to Braze.

- AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN
 
- BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL
 
- BSD, BTC, BTN, BWP, BYR, BZD
 
- CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK
 
- DJF, DKK, DOP, DZD
 
- EEK, EGP, ERN, ETB, EUR
 
- FJD, FKP
 
- GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD
 
- HKD, HNL, HRK, HTG, HUF
 
- IDR, ILS, IMP, INR, IQD, IRR, ISK
 
- JEP, JMD, JOD, JPY
 
- KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT
 
- LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD
 
- MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MTL, MUR, MVR, MWK, MXN, MYR, MZN
 
- NAD, NGN, NIO, NOK, NPR, NZD
 
- OMR
 
- PAB, PEN, PGK, PHP, PKR, PLN, PYG
 
- QAR
 
- RON, RSD, RUB, RWF
 
- SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, STD, SVC, SYP, SZL
 
- THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS
 
- UAH, UGX, USD, UYU, UZS
 
- VEF, VND, VUV
 
- WST
 
- XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT
 
- YER
 
- ZAR, ZMK, ZMW, ZWL

- 

New Stuff!
