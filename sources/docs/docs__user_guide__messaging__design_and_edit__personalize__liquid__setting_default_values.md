---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values
slug: docs__user_guide__messaging__design_and_edit__personalize__liquid__setting_default_values
title: "Set default values"
description: "This reference article cover how to set default fallback values for any personalization attribute that you use in your messages."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Set default values

Default fallback values can be set for any personalization attribute that you use in your messages. This article covers how default values work, how to set them up, and how to use them in your messages.

## How they work

Default values can be added by specifying a Liquid Filter (use | to distinguish the filter inline, as shown) with the name “default.”

```

1

```
 | 
```
| default: 'Insert Your Desired Default Here'

```
 | 

If a default value isn’t provided and the field is missing or not set on the user, the field will be blank in the message.

The following example shows the correct syntax for adding a default value. In this case, the words “Valued User” will replace the attribute {{ ${first_name} }} if a user’s first_name field is empty or unavailable.

```

1

```
 | 
```
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!

```
 | 

To a user named Janet Doe, the message would appear to the user as either:

```

1

```
 | 
```
Hi Janet, thanks for using the App!

```
 | 

Or…

```

1

```
 | 
```
Hi Valued User, thanks for using the App!

```
 | 

important

The default value will show for empty values, but not for blank values. An empty value doesn’t contain anything, while a blank value contains whitespace characters (such as spaces) and no other characters. For example, an empty string could look like "" and a blank string could look like " ".

## Setting default values for different data types

The example earlier in this section shows how to set a default for a string. You can set default values for any Liquid data type that has the value of empty, nil (undefined), or false, which includes strings, booleans, arrays, objects, and numbers.

### Use case: Booleans

Let’s say you have a boolean custom attribute called premium_user and you want to send a personalized message based on the user’s premium status. Some users don’t have a premium status set up, so you’ll need to set up a default value to capture those users.

- You’ll assign a variable called is_premium_user to the premium_user attribute with a default value of false. This means that if premium_user is nil, the value of is_premium_user will default to false.

```

1

```
 | 
```
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}

```
 | 

- Then, use conditional logic to specify the message to send if is_premium_user is true. In other words, what to send if premium_user is true. You’ll also assign a default value to the user’s first name, in case we don’t have the user’s name.

```

1
2

```
 | 
```
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!

```
 | 

- Finally, specify what message to send if is_premium_user is false (which means premium_user is false or nil). Then you’ll close the conditional logic.

```

1
2
3

```
 | 
```
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}

```
 | 

Full Liquid code

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
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}

```
 | 

### Use case: Numbers

Let’s say you have a numeric custom attribute called reward_points and you want to send a message with the user’s reward points. Some users don’t have reward points set up, so you’ll need to set up a default value to account for those users.

- Begin the message by addressing the user’s first name or a default value of Valued User, in case you don’t have their name.

```

1

```
 | 
```
Hi {{${first_name} | default: 'valued user'}},

```
 | 

- End the message with how many reward points the user has by using the custom attribute called reward_points and using the default value of 0. All users whose reward_points have a nil value will have 0 reward points in the message.

```

1

```
 | 
```
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.

```
 | 

### Use case: Objects

Let’s say you have a nested custom attribute object called location that contains the properties city and state. If any of these properties aren’t set, you want to encourage the user to provide them.

- Address the user by their first name and include a default value, in case you don’t have their name.

```

1

```
 | 
```
Hi {{${first_name} | default: 'valued user'}},

```
 | 

- Write a message that says you’d like to confirm the user’s location.

```

1

```
 | 
```
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

```
 | 

- Insert the user’s location into the message and assign default values for when the address property isn’t set.

```

1
2
3

```
 | 
```
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}

```
 | 

Full Liquid code

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
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}

```
 | 

### Use case: Arrays

Let’s say you have an array custom attribute called upcoming_trips that contains trips with the properties destination and departure_date. You want to send users personalized messages based on whether they have trips scheduled.

- Write conditional logic to specify that a message shouldn’t send if upcoming_trips is empty.

```

1
2

```
 | 
```
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}

```
 | 

- Specify what message to send if upcoming_trips has content:

2a. Address the user and include a default value, in case you don’t have their name. 
2b. Use a for tag to specify that you’ll pull properties (or information) for each trip that is contained in upcoming_trips. 
2c. List the properties in the message and include a default value for if the departure_date isn’t set. (Let’s say a destination is required for a trip to be created, so you don’t need to set a default value for that.)
2d. Close the for tag, then close the conditional logic.

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
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
 Here are your upcoming trips:
 <ul>
 {% for trip in {{custom_attribute.${upcoming_trips}}} %}
 <li>
 Destination: {{trip.destination}}
 Departure Date: {{trip.departure_date | default: 'Date not set'}}
 </li>
 {% endfor %}
 </ul>
{% endif %}

```
 | 

Full Liquid code

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

```
 | 
```
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
 Here are your upcoming trips:
 <ul>
 {% for trip in {{custom_attribute.${upcoming_trips}}} %}
 <li>
 Destination: {{trip.destination}}
 Departure Date: {{trip.departure_date | default: 'Date not set'}}
 </li>
 {% endfor %}
 </ul>
{% endif %}

```
 | 

- 

New Stuff!
