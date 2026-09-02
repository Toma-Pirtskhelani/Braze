---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins
slug: docs__user_guide__channels__sms_mms_and_rcs__compliance_and_delivery__collecting_user_opt_ins
title: "Collect user opt-ins"
description: "This reference article covers three best practices for collecting user opt-ins."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Collect user opt-ins

The following article lists some common SMS opt-in methods.

## Option 1: Ask users to text your short or long code

Ask users to text “START”, “UNSTOP”, “YES”, or a custom opt-in keyword to your number to automatically add them to your subscription group. On your website, mobile app, or even advertising, you can request users do this to opt-in, and you can offer an incentive if it’s helpful.

## Option 2: Users opt-in via in-app message

To allow users to opt into SMS from an in-app message, use the phone number capture form provided by Braze to create a branded form that allows you to collect phone numbers and grow your SMS list.

Braze recommends that you also use the SMS double opt-in feature. This feature automatically works with the in-app message phone number capture form, prompting users to confirm their intent after submitting their phone number via the form.

## Option 3: Sign-up flow

When a new user signs up or registers on the website or app, ask for their phone number and email. Include a checkbox to receive promotional emails and SMS.

After the user signs up, do the following:

- Use the /subscription/status/set endpoint to create the user and save their attributes.

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
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "subscription_group_id": "xyz-abcd-1234567",
 "subscription_state": "subscribed",
 "external_id": "external_identifier",
 "phone": "+12223334444",
 "use_double_opt_in_logic": true
}
'

```
 | 

- Use the /users/track endpoint to subscribe the user to SMS.

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "attributes": [
 {
 "external_id": "external_identifier",
 "phone": "+12223334444",
 "subscription_groups": [
 {
 "subscription_group_id": "xyz-abcd-1234567",
 "subscription_state": "subscribed",
 "use_double_opt_in_logic": true
 }
 ]
 }
 ]
}'

```
 | 

note

To enter users into the SMS double opt-in workflow when subscribing through the REST API, set use_double_opt_in_logic to true in your request. This parameter is supported by /subscription/status/set, /v2/subscription/status/set, and /users/track. A user profile must exist for the subscription state to be updated. If no user profile is associated with the provided phone number, the subscription state isn’t updated.

Subscription updates through the REST API don’t automatically trigger welcome messages. To send a welcome message, create an action-based campaign with the Update Subscription Group Status trigger and set the update source to REST API.

- 

New Stuff!
