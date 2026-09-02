---
url: https://www.braze.com/docs/api/objects_filters/recipient_object
slug: docs__api__objects_filters__recipient_object
title: "Recipients object"
description: "This reference article explains the different components of the Braze recipients object."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# Recipients object

The recipients object allows you to request or write information in our endpoints.

You must include one of external_user_id, user_alias, braze_id, or email in this object. Requests must specify only one.

The recipients object allows you to combine the user alias object, the trigger properties object, the Canvas entry properties object, and the user attributes object.

## Object body

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
[{
 "user_alias": (optional, User Alias Object) User alias of user to receive message,
 "external_user_id": (optional, string) see External user ID,
 "braze_id": (optional, string) see Braze ID,
 "email": (optional, string) email address of user to receive message,
 "prioritization": (optional, array) see Prioritization; required when using email,
 "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
 "context": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas context object,
 "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases; if set to `false`, an `attributes` object must also be included,
 "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]

```
 | 

When send_to_existing_only is true, Braze only sends the message to existing users. However, you cannot use this flag with user aliases.

When send_to_existing_only is false, you must include an attributes object on the same recipient. The flag does not replace attributes. Braze uses attributes for the pre-send profile create or update (for example adding email or phone fields for Email or SMS delivery, or updating subscription groups). Without that object, you do not get the intended combined behavior for net-new users on /campaigns/trigger/send or /canvas/trigger/send.

That profile must still meet the message’s audience and channel eligibility rules before Braze sends.

- Braze ID
 
- User aliases
 
- External user ID
 
- Prioritization
 
- User attributes object

## Recipient object deduping

When making an API call with the recipient object, if there exists a duplicated recipient targeting the same address (that is, email, push), Braze dedupes the user, meaning Braze removes identical users, leaving one.

For example, if you use the same external_user_id, then the user receives only one message. Consider making multiple API calls if you need a workaround for this behavior.

When the same external_user_id appears multiple times in the recipients array, Braze sends only one message and uses 
the trigger properties from the last occurrence in the array. This behavior is deterministic and based on array order.

In the following example, userid1 receives one message using "name": "Beth Test 2" because that entry appears last in the array.

```

1
2
3
4

```
 | 
```
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}

```
 | 

- 

New Stuff!
