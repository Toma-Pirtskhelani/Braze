---
url: https://www.braze.com/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups
slug: docs__api__endpoints__subscription_groups__get_list_user_subscription_groups
title: "List user’s subscription groups"
description: "This article outlines details about the List user's subscription groups Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List user’s subscription groups

get

/subscription/user/status

Use this endpoint to list and get the subscription groups with the history of a certain user.

If you want to see examples or test this endpoint for Email Subscription Groups:

See me in Postman

If you want to see examples or test this endpoint for SMS Subscription Groups:

See me in Postman

If you want to see examples or test this endpoint for WhatsApp Groups:

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the subscription.groups.get permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 external_id | 
 Required | 
 String | 
 The external_id of the user (must include at least one and at most 50 external_ids). | 

 email | 
 Required* | 
 String | 
 The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). | 

 phone | 
 Required* | 
 String in E.164 format | 
 The phone number of the user. Must include at least one phone number (with a maximum of 50). | 

 limit | 
 Optional | 
 Integer | 
 The limit on the maximum number of results returned. Default (and maximum) limit is 100. | 

 offset | 
 Optional | 
 Integer | 
 Number of templates to skip before returning the rest of the templates that fit the search criteria. | 

tip

If there are multiple users (multiple external_ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).

## Example request

- multiple users
 
- sms and whatsapp
 
- email

https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&[email protected]&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Example response

Only subscription groups that have had a subscription status update in a user’s history will be included in a successful response. This means that newly created subscription groups will not be listed.

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

```
 | 
```
{
 "users": [
 {
 "email": "[email protected]",
 "phone": "+11112223333",
 "external_id": "external_identifier",
 "subscription_groups": [
 {
 "id": "ec2fcc919fca",
 "name": "ActivationGroup",
 "channel": "email",
 "status": "Subscribed"
 },
 {
 "id": "7d7af9dd5556",
 "name": "ReactivationGroup",
 "channel": "email",
 "status": "Subscribed"
 },
 {
 "id": "a5e84fd16220",
 "name": "MarketingGroup",
 "channel": "sms",
 "status": "Unsubscribed"
 },
 {
 "id": "64d8cad9176c",
 "name": "TransactionalGroup",
 "channel": "sms",
 "status": "Unsubscribed"
 },
 {
 "id": "b2134cd63942",
 "name": "BankerMarketingGroup",
 "channel": "sms",
 "status": "Subscribed"
 }
 ]
 }
 ],
 "total_count": 1,
 "message": "success"
}

```
 | 

- 

New Stuff!
