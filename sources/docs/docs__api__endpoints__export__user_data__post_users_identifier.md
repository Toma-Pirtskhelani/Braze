---
url: https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier
slug: docs__api__endpoints__export__user_data__post_users_identifier
title: "Export user profile by identifier"
description: "This article outlines details about the Export users by identifier Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export user profile by identifier

post

/users/export/ids

Use this endpoint to export data from any user profile by specifying a user identifier.

Up to 50 external_ids or user_aliases can be included in a single request. Should you want to specify device_id, email_address, or phone, only one of these identifiers can be included per request.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the users.export.ids permission.

## Rate limit

If you onboarded with Braze on or after August 22, 2024, this endpoint has a rate limit of 250 requests per minute, as documented in API rate limits.

You can also increase this endpoint’s rate limit to 40 requests per second by meeting the following requirements:

- Your workspace has the default rate limit (250 requests per minute) enabled. Contact your Braze account manager for further assistance with removing any pre-existing rate limit you may have.
 
- Your request includes the fields_to_export parameter to list out all the fields you want to receive.

important

If you include canvases_received or campaigns_received in the fields_to_export parameter, your request will be ineligible for the faster rate limit. We recommend only including these in your request if you have a specific use case for them.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY

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

```
 | 
```
{
 "external_ids": (optional, array of strings) External identifiers for users you wish to export,
 "user_aliases": (optional, array of user alias objects) user aliases for users to export,
 "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
 "braze_id": (optional, string) Braze identifier for a particular user,
 "email_address": (optional, string) Email address of user,
 "phone": (optional, string) Phone number of user,
 "fields_to_export": (optional, array of strings) Name of user data fields to export
}

```
 | 

note

For customers who have onboarded with Braze on or after August 22, 2024, the request parameter fields_to_export is required.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 external_ids | 
 Optional | 
 Array of strings | 
 External identifiers for users you wish export. | 

 user_aliases | 
 Optional | 
 Array of user alias object | 
 User aliases for users to export. | 

 device_id | 
 Optional | 
 String | 
 Device identifier, as returned by various SDK methods such as getDeviceId. | 

 braze_id | 
 Optional | 
 String | 
 Braze identifier for a particular user. | 

 email_address | 
 Optional | 
 String | 
 Email address of user. | 

 phone | 
 Optional | 
 String in E.164 format | 
 Phone number of user. | 

 fields_to_export | 
 Optional* | 
 Array of strings | 
 Name of user data fields to export.

*This field is required to use the faster rate limit of 40 requests per second. If omitted, the default rate limit of 250 requests per min will be used instead. | 

*Required for customers who have onboarded with Braze on or after August 22, 2024.

## Example request

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "external_ids": ["user_identifier1", "user_identifier2"],
 "user_aliases": [
 {
 "alias_name": "example_alias",
 "alias_label": "example_label"
 }
 ],
 "device_id": "1234567",
 "braze_id": "braze_identifier",
 "email_address": "[email protected]",
 "phone": "11112223333",
 "fields_to_export": ["first_name", "email", "purchases"]
}'

```
 | 

## Fields to export

The following is a list of valid fields_to_export. Using fields_to_export to minimize the data returned can improve response time of this API endpoint:

 Field to export | 
 Data type | 
 Description | 

 apps | 
 Array | 
 Apps this user has logged sessions for, which includes the fields:

- name: app name
- platform: app platform, such as iOS, Android, or Web
- version: app version number or name 
- sessions: total number of sessions for this app
- first_used: date of first session
- last_used: date of last session

All fields are strings. | 

 attributed_campaign | 
 String | 
 Data from attribution integrations, if set up. Identifier for a particular ad campaign. | 

 attributed_source | 
 String | 
 Data from attribution integrations, if set up. Identifier for the platform the ad was on. | 

 attributed_adgroup | 
 String | 
 Data from attribution integrations, if set up. Identifier for an optional sub-grouping below campaign. | 

 attributed_ad | 
 String | 
 Data from attribution integrations, if set up. Identifier for an optional sub-grouping below campaign and ad group. | 

 push_subscribe | 
 String | 
 User’s push subscription status. | 

 email_subscribe | 
 String | 
 User’s email subscription status. | 

 braze_id | 
 String | 
 Device-specific unique user identifier set by Braze for this user. | 

 country | 
 String | 
 User’s country using ISO 3166-1 alpha-2 standard. | 

 created_at | 
 String | 
 Date and time for when the user profile was created, in ISO 8601 format. | 

 custom_attributes | 
 Object | 
 Custom attribute key-value pairs for this user. | 

 custom_events | 
 Array | 
 Custom events attributed to this user in the last 90 days. | 

 devices | 
 Array | 
 Information about the user’s device, which could include the following depending on platform:

- model: Device’s model name
- os: Device’s operating system
- carrier: Device’s service carrier, if available
- idfv: (iOS) Braze device identifier, the Apple Identifier for Vendor, if exists
- idfa: (iOS) Identifier for Advertising, if exists
- device_id: (Android) Braze device identifier
- google_ad_id: (Android) Google Play Advertising Identifier, if exists
- roku_ad_id: (Roku) Roku Advertising Identifier
- ad_tracking_enabled: If ad tracking is enabled on the device, can be true or false | 

 dob | 
 String | 
 User’s date of birth in the format YYYY-MM-DD. | 

 email | 
 String | 
 User’s email address. | 

 external_id | 
 String | 
 Unique user identifier for identified users. | 

 first_name | 
 String | 
 User’s first name. | 

 gender | 
 String | 
 User’s gender. Possible values are:

- M: male
- F: female
- O: other
- N: not applicable
- P: prefer not to say
- nil: unknown | 

 home_city | 
 String | 
 User’s home city. | 

 language | 
 String | 
 User’s language in ISO-639-1 standard. | 

 last_coordinates | 
 Array of floats | 
 User’s most recent device location, formatted as [longitude, latitude]. | 

 last_name | 
 String | 
 User’s last name. | 

 phone | 
 String | 
 User’s telephone number in E.164 format. | 

 purchases | 
 Array | 
 Purchases this user has made in the last 90 days. | 

 push_tokens | 
 Array | 
 Unique anonymous identifier that specifies where to send an app’s notifications. | 

 random_bucket | 
 Integer | 
 User’s random bucket number, used to create uniformly distributed segments of random users. | 

 time_zone | 
 String | 
 User’s time zone in the same format as the IANA Time Zone Database. | 

 total_revenue | 
 Float | 
 Total revenue attributed to this user. Total revenue is calculated based on purchases the user made during conversion windows for the campaigns and Canvases they received. | 

 uninstalled_at | 
 Timestamp | 
 Date and time the user uninstalls the app. Omitted if the app has not been uninstalled. | 

 user_aliases | 
 Object | 
 User aliases object containing the alias_name and alias_label, if exists. | 

Be aware that the /users/export/ids endpoint will pull together the entire user profile for this user, including data such as all campaigns and Canvases received, all custom events performed, all purchases made, and all custom attributes. As a result, this endpoint is slower than other REST API endpoints.

Depending on the data requested, this API endpoint may not be sufficient to meet your needs due to the 250 requests per minute rate limit. If you anticipate using this endpoint regularly to export users, instead consider exporting users by segment, which is asynchronous and more optimized for larger data pulls.

## Response

```

1
2
3
4
5

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
 "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}

```
 | 

For an example of the data that is accessible through this endpoint see the following example.

### Example user export file output

User export object (we will include the least data possible - if a field is missing from the object it should be assumed to be null or empty):

- all fields
 
- sample output

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
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137

```
 | 
```
{
 "created_at": (string),
 "external_id" : (string),
 "user_aliases" : [
 {
 "alias_name" : (string),
 "alias_label" : (string)
 }
 ],
 "braze_id": (string),
 "first_name" : (string),
 "last_name" : (string),
 "email" : (string),
 "dob" : (string) date for the user's date of birth,
 "home_city" : (string),
 "country" : (string) ISO-3166-1 alpha-2 standard,
 "phone" : (string),
 "language" : (string) ISO-639-1 standard,
 "time_zone" : (string),
 "last_coordinates" : (array of float) [lon, lat],
 "gender" : (string) "M" | "F",
 "total_revenue" : (float),
 "attributed_campaign" : (string),
 "attributed_source" : (string),
 "attributed_adgroup" : (string),
 "attributed_ad" : (string),
 "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
 "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
 "custom_attributes" : (object) custom attribute key-value pairs,
 "custom_events" : [
 {
 "name" : (string),
 "first" : (string) date,
 "last" : (string) date,
 "count" : (int)
 },
 ...
 ],
 "purchases" : [
 {
 "name" : (string),
 "first" : (string) date,
 "last" : (string) date,
 "count" : (int)
 },
 ...
 ],
 "devices" : [
 {
 "model" : (string),
 "os" : (string),
 "carrier" : (string),
 "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
 "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
 "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
 "roku_ad_id" : (string) only included for Roku devices,
 "ad_tracking_enabled" : (boolean)
 },
 ...
 ],
 "push_tokens" : [
 {
 "app" : (string) app name,
 "platform" : (string),
 "token" : (string),
 "device_id": (string),
 "notifications_enabled": (boolean) whether foreground push notifications are enabled for this token. `true` means foreground push is enabled for the token, and `false` means foreground push is disabled (for example, background-only). This is device-level and doesn't indicate the user's global push subscription status,
 "provisionally_opted_in": (boolean) included for iOS and Android tokens only. Indicates whether the token is in a provisional push authorization state. `true` means the token is provisionally opted in (notifications are delivered quietly), `false` means the token isn't provisional (the user has explicitly authorized or denied push), and `null` means provisional status isn't set. Provisional authorization applies to iOS; Android tokens report `null`
 },
 ...
 ],
 "apps" : [
 {
 "name" : (string),
 "platform" : (string),
 "version" : (string),
 "sessions" : (integer),
 "first_used" : (string) date,
 "last_used" : (string) date
 },
 ...
 ],
 "campaigns_received" : [
 {
 "name" : (string),
 "last_received" : (string) date,
 "engaged" :
 {
 "opened_email" : (boolean),
 "opened_push" : (boolean),
 "clicked_email" : (boolean),
 "clicked_triggered_in_app_message" : (boolean)
 },
 "converted" : (boolean),
 "api_campaign_id" : (string),
 "variation_name" : (optional, string) exists only if it is a multivariate campaign,
 "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
 "in_control" : (optional, boolean) exists only if it is a multivariate campaign
 },
 ...
 ],
 "canvases_received": [
 {
 "name": (string),
 "api_canvas_id": (string),
 "last_received_message": (string) date,
 "last_entered": (string) date,
 "variation_name": (string),
 "in_control": (boolean),
 "last_exited": (string) date,
 "steps_received": [
 {
 "name": (string),
 "api_canvas_step_id": (string),
 "last_received": (string) date
 },
 {
 "name": (string),
 "api_canvas_step_id": (string),
 "last_received": (string) date
 },
 {
 "name": (string),
 "api_canvas_step_id": (string),
 "last_received": (string) date
 }
 ]
 },
 ...
 ],
 "cards_clicked" : [
 {
 "name" : (string)
 },
 ...
 ]
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
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134

```
 | 
```
{
 "created_at" : "2020-07-10 15:00:00.000 UTC",
 "external_id" : "A8i3mkd99",
 "user_aliases" : [
 {
 "alias_name" : "user_123",
 "alias_label" : "amplitude_id"
 }
 ],
 "braze_id": "5fbd99bac125ca40511f2cb1",
 "random_bucket" : 2365,
 "first_name" : "Alex",
 "last_name" : "Smith",
 "email" : "[email protected]",
 "dob" : "1980-12-21",
 "home_city" : "Chicago",
 "country" : "US",
 "phone" : "+15555550123",
 "language" : "en",
 "time_zone" : "Eastern Time (US & Canada)",
 "last_coordinates" : [41.84157636433568, -87.83520818508256],
 "gender" : "F",
 "total_revenue" : 65,
 "attributed_campaign" : "braze_test_campaign_072219",
 "attributed_source" : "braze_test_source_072219",
 "attributed_adgroup" : "braze_test_adgroup_072219",
 "attributed_ad" : "braze_test_ad_072219",
 "push_subscribe" : "opted_in",
 "push_opted_in_at": "2020-01-26T22:45:53.953Z",
 "email_subscribe" : "subscribed",
 "custom_attributes":
 {
 "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
 "loyaltyPoints": "321",
 "loyaltyPointsNumber": 107
 },
 "custom_events": [
 {
 "name": "Loyalty Acknowledgement",
 "first": "2021-06-28T17:02:43.032Z",
 "last": "2021-06-28T17:02:43.032Z",
 "count": 1
 },
 ...
 ],
 "purchases": [
 {
 "name": "item_40834",
 "first": "2021-09-05T03:45:50.540Z",
 "last": "2022-06-03T17:30:41.201Z",
 "count": 10
 },
 ...
 ],
 "devices": [
 {
 "model": "Pixel XL",
 "os": "Android (Q)",
 "carrier": null,
 "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
 "ad_tracking_enabled": true
 },
 ...
 ],
 "push_tokens": [
 {
 "app": "MovieCanon",
 "platform": "Android",
 "token": "12345abcd",
 "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
 "notifications_enabled": true,
 "provisionally_opted_in": null
 },
 ...
 ],
 "apps": [
 {
 "name": "MovieCannon",
 "platform": "Android",
 "version": "3.29.0",
 "sessions": 1129,
 "first_used": "2020-02-02T19:56:19.142Z",
 "last_used": "2021-11-11T00:25:19.201Z"
 },
 ...
 ],
 "campaigns_received": [
 {
 "name": "Email Unsubscribe",
 "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
 "last_received": "2022-06-02T03:07:38.105Z",
 "engaged":
 {
 "opened_email": true
 },
 "converted": true,
 "multiple_converted":
 {
 "Primary Conversion Event - A": true
 },
 "in_control": false,
 "variation_name": "Variant 1",
 "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
 },
 ...
 ],
 "canvases_received": [
 {
 "name": "Non Global Holdout Group 4/21/21",
 "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
 "last_received_message": "2021-07-07T20:46:24.136Z",
 "last_entered": "2021-07-07T20:45:24.000+00:00",
 "variation_name": "Variant 1",
 "in_control": false,
 "last_entered_control_at": null,
 "last_exited": "2021-07-07T20:46:24.136Z",
 "steps_received": [
 {
 "name": "Step",
 "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
 "last_received": "2021-07-07T20:46:24.136Z"
 },
 ...
 ]
 }
 ...
 ],
 "cards_clicked" : [
 {
 "name" : "Loyalty Promo"
 },
 ...
 ]
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
