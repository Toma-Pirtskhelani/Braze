---
url: https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes
slug: docs__developer_guide__analytics__setting_user_attributes
title: "Set user attributes"
description: "Learn how to set user attributes through the Braze SDK."
section: developer_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Set user attributes

Learn how to set user attributes through the Braze SDK.

note

For wrapper SDKs not listed, use the relevant native Android or Swift method instead.

- web
 
- android
 
- swift
 
- flutter
 
- roku
 
- unity
 
- react native

## Prerequisites

Before you can use this feature, you’ll need to integrate the Web Braze SDK.

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes within the User class:

- First Name
 
- Last Name
 
- Language
 
- Country
 
- Date of Birth
 
- Email
 
- Gender
 
- Home City
 
- Phone Number

### Setting default attributes

- using methods
 
- google tag manager

To set a default attribute for a user, call the getUser() method on your Braze instance to get a reference to the current user of your app. Then you can call methods to set a user attribute.

- first name
 
- gender
 
- date of birth

```

1

```
 | 
```
braze.getUser().setFirstName("SomeFirstName");

```
 | 

```

1

```
 | 
```
braze.getUser().setGender(braze.User.Genders.FEMALE);

```
 | 

```

1

```
 | 
```
braze.getUser().setDateOfBirth(2000, 12, 25);

```
 | 

Using Google Tag Manager, standard user attributes (such as a user’s first name), should be logged in the same manner as custom user attributes. Ensure the values you’re passing in for standard attributes match the expected format specified in the User class documentation.

For example, the gender attribute can accept any of the following as values: "m" | "f" | "o" | "u" | "n" | "p". Therefore to set a user’s gender as female, create a Custom HTML tag with the following content:

```

1
2
3

```
 | 
```
<script>
window.braze.getUser().setGender("f")
</script>

```
 | 

### Unsetting default attributes

You can remove or unset a user attribute through your app code, a REST API request, or a User Update Canvas step. For array and boolean attributes, use null. For other data types, use an empty string ("").

To unset a default user attribute with the Web SDK, pass null to the related method. For example:

- first name
 
- gender
 
- date of birth

```

1

```
 | 
```
braze.getUser().setFirstName(null);

```
 | 

```

1

```
 | 
```
braze.getUser().setGender(null);

```
 | 

```

1

```
 | 
```
braze.getUser().setDateOfBirth(null, null, null);

```
 | 

## Custom user attributes

### Setting custom attributes

- using methods
 
- google tag manager

In addition to the default user attribute methods, you can also set custom attributes for your users. Full method specifications, see our JSDocs.

- string
 
- integer
 
- date
 
- array

To set a custom attribute with a string value:

```

1
2
3
4

```
 | 
```
braze.getUser().setCustomUserAttribute(
 YOUR_ATTRIBUTE_KEY_STRING,
 YOUR_STRING_VALUE
);

```
 | 

To set a custom attribute with a integer value:

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

```
 | 
```
braze.getUser().setCustomUserAttribute(
 YOUR_ATTRIBUTE_KEY_STRING,
 YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
 YOUR_ATTRIBUTE_KEY_STRING,
 THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);

```
 | 

To set a custom attribute with a date value:

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

```
 | 
```
braze.getUser().setCustomUserAttribute(
 YOUR_ATTRIBUTE_KEY_STRING,
 YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
 YOUR_ATTRIBUTE_KEY_STRING,
 new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
 YOUR_ATTRIBUTE_KEY_STRING,
 new Date(secondsFromEpoch * 1000)
);

```
 | 

The default and maximum number of elements in an array is 500. You can update the maximum number of arrays in the Braze dashboard, under Data Settings > Custom Attributes. Arrays exceeding the maximum number of elements are truncated to contain the maximum number of elements.

To set a custom attribute with an array value:

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
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");

```
 | 

important

Dates passed to Braze with this method must be JavaScript Date objects.

important

Custom attribute keys and values can only have a maximum of 255 characters. For more information about valid custom attribute values, refer to the reference documentation.

Custom user attributes are not available due to a limitation in Google Tag Manager’s scripting language. To log custom attributes, create a Custom HTML tag with the following content:

```

1
2
3
4
5

```
 | 
```
<script>
 // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
 // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>

```
 | 

important

The GTM template does not support nested properties on events or purchases. You can use the preceding HTML to log any events or purchases that require nested properties.

### Unsetting custom attributes

To unset a custom attribute, pass null to the related method.

```

1

```
 | 
```
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);

```
 | 

### Nesting custom attributes

You can also nest properties within custom attributes. In the following example, a favorite_book object with nested properties is set as a custom attribute on the user profile. For more details, refer to Nested Custom Attributes.

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
import * as braze from "@braze/web-sdk";

const favoriteBook = {
 title: "The Hobbit",
 author: "J.R.R. Tolkien",
 publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);

```
 | 

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to User Data Endpoints.

## Setting user subscriptions

To set up a subscription for your users (either email or push), call the functions setEmailNotificationSubscriptionType() or setPushNotificationSubscriptionType(), respectively. Both functions take the enum type braze.User.NotificationSubscriptionTypes as arguments. This type has three different states:

 Subscription Status | 
 Definition | 

 braze.User.NotificationSubscriptionTypes.OPTED_IN | 
 Subscribed, and explicitly opted in | 

 braze.User.NotificationSubscriptionTypes.SUBSCRIBED | 
 Subscribed, but not explicitly opted in | 

 braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED | 
 Unsubscribed and/or explicitly opted out | 

When a user is registered for push, the browser forces them to choose to allow or block notifications, and if they choose to allow push, they are set OPTED_IN by default.

Visit Managing user subscriptions for more information on implementing subscriptions and explicit opt-ins.

### Unsubscribing a user from email

```

1

```
 | 
```
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);

```
 | 

### Unsubscribing a user from push

```

1

```
 | 
```
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK.

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes within the BrazeUser class. For method specifications, refer to our KDoc.

- First name
 
- Last name
 
- Country
 
- Language
 
- Date of birth
 
- Email
 
- Gender
 
- Home city
 
- Phone number

note

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Setting default attributes

To set a default attribute for a user, call the getCurrentUser() method on your Braze instance to get a reference to the current user of your app. Then you can call methods to set a user attribute.

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setFirstName("first_name");
 }
}

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setFirstName("first_name")
}

```
 | 

### Unsetting default attributes

To unset a user attribute, pass null to the relevant method.

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setFirstName(null);
 }
}

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setFirstName(null)
}

```
 | 

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute’s segmentation option, see User data collection.

### Setting custom attributes

- string
 
- integers
 
- floating-points
 
- boolean
 
- date
 
- array

To set a custom attribute with a string value:

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value");
 }
}

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
}

```
 | 

To set a custom attribute with an int value:

- java
 
- kotlin

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
 
 // Integer attributes may also be incremented using code like the following:
 brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
 }
}

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
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)

 // Integer attributes may also be incremented using code like the following:
 brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
}

```
 | 

To set a custom attribute with a long integer value:

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
 }
});

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
}

```
 | 

To set a custom attribute with a float value:

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
 }
});

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
}

```
 | 

To set a custom attribute with a double value:

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
 }
});

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
}

```
 | 

To set a custom attribute with a boolean value:

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
 }
});

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
}

```
 | 

- java
 
- kotlin

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

```
 | 
```
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
 // This method will assign the current time to a custom attribute at the time the method is called:
 brazeUser.setCustomUserAttributeToNow("your_attribute_key");
 // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
 brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
 }
});

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

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
 // This method will assign the current time to a custom attribute at the time the method is called:
 brazeUser.setCustomUserAttributeToNow("your_attribute_key")
 // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
 brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
}

```
 | 

warning

Dates passed to Braze with this method must either be in the ISO 8601 format (e.g 2013-07-16T19:20:30+01:00) or in the yyyy-MM-dd'T'HH:mm:ss:SSSZ format (e.g 2016-12-14T13:32:31.601-0800).

The default and maximum number of elements in an array is 500. You can update the maximum number of arrays in the Braze dashboard, under Data Settings > Custom Attributes. Arrays exceeding the maximum number of elements are truncated to contain the maximum number of elements. For more information on custom attribute arrays and their behavior, see Arrays.

- java
 
- kotlin

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 // Setting a custom attribute with an array value
 brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray);
 // Adding to a custom attribute with an array value
 brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add");
 // Removing a value from an array type custom attribute
 brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
 }
});

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

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 // Setting a custom attribute with an array value
 brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray)
 // Adding to a custom attribute with an array value
 brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add")
 // Removing a value from an array type custom attribute
 brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
}

```
 | 

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the unsetCustomUserAttribute method.

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.unsetCustomUserAttribute("your_attribute_key");
 }
});

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.unsetCustomUserAttribute("your_attribute_key")
}

```
 | 

### Nesting custom attributes

You can also nest properties within custom attributes. In the following example, a favorite_book object with nested properties is set as a custom attribute on the user profile. For more details, refer to Nested Custom Attributes.

- java
 
- kotlin

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

```
 | 
```
JSONObject favoriteBook = new JSONObject();
try {
 favoriteBook.put("title", "The Hobbit");
 favoriteBook.put("author", "J.R.R. Tolkien");
 favoriteBook.put("publishing_date", "1937");
} catch (JSONException e) {
 e.printStackTrace();
}

braze.getCurrentUser(user -> {
 user.setCustomUserAttribute("favorite_book", favoriteBook);
 return null;
});

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

```
 | 
```
val favoriteBook = JSONObject()
 .put("title", "The Hobbit")
 .put("author", "J.R.R. Tolkien")
 .put("publishing_date", "1937")

braze.getCurrentUser { user ->
 user.setCustomUserAttribute("favorite_book", favoriteBook)
}

```
 | 

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to User Data Endpoints.

## Setting user subscriptions

To set up a subscription for your users (either email or push), call the functions setEmailNotificationSubscriptionType() or setPushNotificationSubscriptionType(), respectively. Both of these functions take the enum type NotificationSubscriptionType as arguments. This type has three different states:

 Subscription status | 
 Definition | 

 OPTED_IN | 
 Subscribed, and explicitly opted in | 

 SUBSCRIBED | 
 Subscribed, but not explicitly opted in | 

 UNSUBSCRIBED | 
 Unsubscribed and/or explicitly opted out | 

important

No explicit opt-in is required by Android to send users push notifications. When a user is registered for push, they are set to SUBSCRIBED rather than OPTED_IN by default. Refer to managing user subscriptions for more information on implementing subscriptions and explicit opt-ins.

### Setting email subscriptions

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
 }
});

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
}

```
 | 

### Setting push notification subscription

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
 }
});

```
 | 

```

1
2
3

```
 | 
```
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
}

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK.

## Default user attributes

### Supported attributes

The following attributes should be set on the Braze.User object:

- firstName
 
- lastName
 
- email
 
- dateOfBirth
 
- country
 
- language
 
- homeCity
 
- phone
 
- gender

### Setting default attributes

To set a default user attribute, set the appropriate field on the shared Braze.User object. The following is an example of setting the first name attribute:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.set(firstName: "Alex")

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setFirstName:@"Alex"];

```
 | 

### Unsetting default attributes

To unset a default user attribute, pass nil to the relevant method.

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.set(firstName: nil)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setFirstName:nil];

```
 | 

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute’s segmentation option, see User data collection.

important

Custom attribute values have a maximum length of 255 characters; longer values will be truncated. For more information, refer to Braze.User.

### Setting custom attributes

- string
 
- integer
 
- floating-points
 
- boolean
 
- date
 
- array

To set a custom attribute with a string value:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];

```
 | 

To set a custom attribute with an integer value:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];

```
 | 

Braze treats float and double values the same within our database. To set a custom attribute with a double value:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];

```
 | 

To set a custom attribute with a boolean value:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];

```
 | 

To set a custom attribute with a date value:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];

```
 | 

The default and maximum number of elements in an array is 500. You can update the maximum number of arrays in the Braze dashboard, under Data Settings > Custom Attributes. Arrays exceeding the maximum number of elements are truncated to contain the maximum number of elements.

To set a custom attribute with an array value:

- swift
 
- objective-c

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
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1", "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")

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

```
 | 
```
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1", @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];

```
 | 

### Incrementing or decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any integer or long value:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];

```
 | 

### Unsetting custom attributes

- swift
 
- objective-c

To unset a custom attribute, pass the relevant attribute key to the unsetCustomAttribute method.

```

1

```
 | 
```
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")

```
 | 

To unset a custom attribute, pass the relevant attribute key to the unsetCustomAttributeWithKey method.

```

1

```
 | 
```
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];

```
 | 

### Nesting custom attributes

You can also nest properties within custom attributes. In the following example, a favorite_book object with nested properties is set as a custom attribute on the user profile. For more details, refer to Nested Custom Attributes.

- swift
 
- objective-c

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
let favoriteBook: [String: Any?] = [
 "title": "The Hobbit",
 "author": "J.R.R. Tolkien",
 "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)

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

```
 | 
```
NSDictionary *favoriteBook = @{
 @"title": @"The Hobbit",
 @"author": @"J.R.R. Tolkien",
 @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];

```
 | 

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to User Data Endpoints.

## Setting user subscriptions

To set up a subscription for your users (either email or push), call the functions set(emailSubscriptionState:) or set(pushNotificationSubscriptionState:), respectively. Both of these functions take the enum type Braze.User.SubscriptionState as arguments. This type has three different states:

 Subscription Status | 
 Definition | 

 optedIn | 
 Subscribed, and explicitly opted in | 

 subscribed | 
 Subscribed, but not explicitly opted in | 

 unsubscribed | 
 Unsubscribed and/or explicitly opted out | 

Users who grant permission for an app to send them push notifications default to the status of optedIn as iOS requires an explicit opt-in.

Users will be set to subscribed automatically upon receipt of a valid email address; however, we suggest that you establish an explicit opt-in process and set this value to optedIn upon receipt of explicit consent from your user. Refer to Managing user subscriptions for more details.

### Setting email subscriptions

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]

```
 | 

### Setting push notification subscriptions

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)

```
 | 

```

1

```
 | 
```
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]

```
 | 

Refer to Managing user subscriptions for more details.

## Prerequisites

Before you can use this feature, you’ll need to integrate the Flutter Braze SDK.

## Default user attributes

### Supported attributes

The following attributes are supported:

- First Name
 
- Last Name
 
- Gender
 
- Date of Birth
 
- Home City
 
- Country
 
- Phone Number
 
- Language
 
- Email

important

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Setting default attributes

To set user attributes automatically collected by Braze, you can use the setter methods included with the SDK.

```

1

```
 | 
```
braze.setFirstName('Name');

```
 | 

## Custom user attributes

### Setting custom attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using a number of different data types:

- string
 
- integer
 
- double
 
- boolean
 
- date
 
- array

To set a custom attribute with a string value:

```

1

```
 | 
```
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");

```
 | 

To set a custom attribute with an integer value:

```

1
2
3
4

```
 | 
```
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);

```
 | 

To set a custom attribute with a double value:

```

1

```
 | 
```
braze.setDoubleCustomUserAttribute("custom double attribute key", double);

```
 | 

To set a custom attribute with a boolean value:

```

1

```
 | 
```
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);

```
 | 

To set a custom attribute with a date value:

```

1

```
 | 
```
braze.setDateCustomUserAttribute("custom date attribute key", date);

```
 | 

To set a custom attribute with an array value:

```

1
2
3
4

```
 | 
```
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");

```
 | 

important

Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the unsetCustomUserAttribute method.

```

1

```
 | 
```
braze.unsetCustomUserAttribute('attribute_key');

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Roku Braze SDK.

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes using the m.Braze object.

- FirstName
 
- LastName
 
- Email
 
- Gender
 
- DateOfBirth
 
- Country
 
- Language
 
- HomeCity
 
- PhoneNumber

### Setting default attributes

To set a default attribute, call the relevant method on the m.Braze object.

- first name
 
- last name
 
- email
 
- gender
 
- birth date
 
- country
 
- language
 
- home city
 
- phone number

```

1

```
 | 
```
m.Braze.setFirstName("Alex")

```
 | 

```

1

```
 | 
```
m.Braze.setLastName("Smith")

```
 | 

```

1

```
 | 
```
m.Braze.setEmail("[email protected]")

```
 | 

```

1

```
 | 
```
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"

```
 | 

```

1

```
 | 
```
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day

```
 | 

```

1

```
 | 
```
m.Braze.setCountry("United States")

```
 | 

```

1

```
 | 
```
m.Braze.setLanguage("en")

```
 | 

```

1

```
 | 
```
m.Braze.setHomeCity("New York")

```
 | 

```

1

```
 | 
```
m.Braze.setPhoneNumber("+1234567890")

```
 | 

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types.

### Settings custom attributes

- string
 
- integer
 
- floating-points
 
- boolean
 
- date
 
- array

To set a custom attribute a string value:

```

1

```
 | 
```
m.Braze.setCustomAttribute("stringAttribute", "stringValue")

```
 | 

To set a custom attribute with an integer value:

```

1

```
 | 
```
m.Braze.setCustomAttribute("intAttribute", 5)

```
 | 

Braze treats float and double values exactly the same. To set a custom attribute with either value:

```

1

```
 | 
```
m.Braze.setCustomAttribute("floatAttribute", 3.5)

```
 | 

To set a custom attribute with a boolean value:

```

1

```
 | 
```
m.Braze.setCustomAttribute("boolAttribute", true)

```
 | 

To set a custom attribute with a date value:

```

1
2
3

```
 | 
```
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)

```
 | 

To set a custom attribute with an array value:

```

1
2
3
4
5

```
 | 
```
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)

```
 | 

important

Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

### Incrementing and decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer value.

```

1

```
 | 
```
m.Braze.incrementCustomUserAttribute("intAttribute", 3)

```
 | 

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the unsetCustomAttribute method.

```

1

```
 | 
```
m.Braze.unsetCustomAttribute("attributeName")

```
 | 

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to User Data Endpoints.

## Setting email subscriptions

You can set the following email subscription statuses for your users programmatically through the SDK.

 Subscription Status | 
 Definition | 

 OptedIn | 
 Subscribed, and explicitly opted in | 

 Subscribed | 
 Subscribed, but not explicitly opted in | 

 UnSubscribed | 
 Unsubscribed and/or explicitly opted out | 

note

These types fall under BrazeConstants().SUBSCRIPTION_STATES.

The method for setting email subscription status is setEmailSubscriptionState(). Users will be set to Subscribed automatically upon receipt of a valid email address, however, we suggest that you establish an explicit opt-in process and set this value to OptedIn upon receipt of explicit consent from your user. For more details, visit Managing user subscriptions.

```

1

```
 | 
```
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Unity Braze SDK.

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes using the BrazeBinding object. For more information, see Braze Unity declaration file.

- First name
 
- Last name
 
- User email
 
- Gender
 
- Birth date
 
- User country
 
- User home city
 
- User email subscription
 
- User push subscription
 
- User phone number

### Setting default attributes

To set a default attribute, call the relevant method on the BrazeBinding object.

- first name
 
- last name
 
- email
 
- gender
 
- birth date
 
- country
 
- home city
 
- email subscription
 
- push subscription
 
- phone number

```

1

```
 | 
```
BrazeBinding.SetUserFirstName("first name");

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserLastName("last name");

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserEmail("[email protected]");

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserGender(Appboy.Models.Gender);

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserCountry("country name");

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserHomeCity("city name");

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);

```
 | 

```

1

```
 | 
```
BrazeBinding.SetUserPhoneNumber("phone number");

```
 | 

### Unsetting default attributes

To unset a default user attribute, pass null to the relevant method.

```

1

```
 | 
```
BrazeBinding.SetUserFirstName(null);

```
 | 

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute’s segmentation option, see User data collection.

### Setting custom attributes

To set a custom attribute, use the corresponding method for the attribute type:

- string
 
- integer
 
- float
 
- double
 
- boolean
 
- date
 
- array
 
- nested objects

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");

```
 | 

```

1
2
3
4

```
 | 
```
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))

```
 | 

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttribute("custom float attribute key", 'float value');

```
 | 

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');

```
 | 

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');

```
 | 

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");

```
 | 

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');

```
 | 

note

Dates passed to Braze must either be in the ISO 8601 format (such as 2013-07-16T19:20:30+01:00) or in the yyyy-MM-dd'T'HH:mm:ss:SSSZ format (such as2016-12-14T13:32:31.601-0800).

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
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")

```
 | 

You can set custom attributes containing nested objects (available in Unity SDK 5.1.0 and later). For more information, see Nested custom attributes.
The following examples show how to set a nested object attribute, merge updates into an existing object, and set an array of nested objects.

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>));

```
 | 

To update an existing nested object, use the merge parameter:

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>), merge(bool));

```
 | 

You can also set an array of nested objects:

```

1

```
 | 
```
AppboyBinding.SetCustomUserAttribute("custom object array attribute key", list(List<Dictionary<string, object>>));

```
 | 

important

Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the UnsetCustomUserAttribute method.

```

1

```
 | 
```
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");

```
 | 

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to User Data Endpoints.

## Setting user subscriptions

To set up an email or push subscription for your users, call one of the following functions.

```

1
2
3
4
5

```
 | 
```
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`

```
 | 

Both functions take Appboy.Models.AppboyNotificationSubscriptionType as arguments, which has three different states:

 Subscription Status | 
 Definition | 

 OPTED_IN | 
 Subscribed, and explicitly opted in | 

 SUBSCRIBED | 
 Subscribed, but not explicitly opted in | 

 UNSUBSCRIBED | 
 Unsubscribed and/or explicitly opted out | 

note

No explicit opt-in is required by Windows to send users push notifications. When a user is registered for push, they are set to SUBSCRIBED rather than OPTED_IN by default. To learn more, check out our documentation on implementing subscriptions and explicit opt-ins.

 Subscription Type | 
 Description | 

 EmailNotificationSubscriptionType | 
 Users will be set to SUBSCRIBED automatically upon receipt of a valid email address. However, we suggest that you establish an explicit opt-in process and set this value to OPTED_IN upon receipt of explicit consent from your user. Visit our Changing User Subscriptions doc for more details. | 

 PushNotificationSubscriptionType | 
 Users will be set to SUBSCRIBED automatically upon valid push registration. However, we suggest that you establish an explicit opt-in process and set this value to OPTED_IN upon receipt of explicit consent from your user. Visit our Changing User Subscriptions doc for more details. | 

note

These types fall under Appboy.Models.AppboyNotificationSubscriptionType.

### Setting email subscriptions

```

1

```
 | 
```
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);

```
 | 

### Setting push notification subscriptions

```

1

```
 | 
```
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the React Native Braze SDK.

## Logging custom attributes

Braze provides methods for assigning attributes to users. You’ll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To set user attributes automatically collected by Braze, you can use setter methods that come with the SDK.

```

1

```
 | 
```
Braze.setFirstName("Name");

```
 | 

The following attributes are supported:

- First Name
 
- Last Name
 
- Gender
 
- Date of Birth
 
- Home City
 
- Country
 
- Phone Number
 
- Language
 
- Email

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Custom user attributes

In addition to our predefined user attribute methods, Braze also provides custom attributes to track data from your applications.

```

1
2
3

```
 | 
```
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
 // optional onResult callback
});

```
 | 

#### Unsetting custom attributes

```

1
2
3

```
 | 
```
Braze.unsetCustomUserAttribute("attribute_key", function(){
 // optional onResult callback
});

```
 | 

#### Custom Attribute Arrays

```

1
2
3
4
5
6
7
8

```
 | 
```

// Adds a string to a custom attribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.

Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);

```
 | 

- 

New Stuff!
