---
url: https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details
slug: docs__api__endpoints__export__canvas__get_canvas_details
title: "Export Canvas details"
description: "This article outlines details about the Export Canvas details Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export Canvas details

get

/canvas/details

Use this endpoint to export metadata about a Canvas, such as the name, time created, current status, and more.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the canvas.details permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 canvas_id | 
 Required | 
 String | 
 See Canvas API Identifier | 

 post_launch_draft_version | 
 Optional | 
 Boolean | 
 For Canvases that have a post-launch draft, setting this to true shows any draft changes available. Defaults to false. | 

 include_has_translatable_content | 
 Optional | 
 Boolean | 
 When set to true, the API response includes a has_translatable_content field for each message. Defaults to false. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/details?canvas_id={{canvas_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Responses

note

All Canvas steps have a next_paths field, which is an array of {name, next_step_id} data. For Message steps, the next_step_ids field will be present, but will not contain data for other Canvas steps.

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

```
 | 
```
{
 "created_at": (string) the date created as ISO 8601 date,
 "updated_at": (string) the date updated as ISO 8601 date,
 "name": (string) the Canvas name,
 "description": (string) the Canvas description,
 "archived": (boolean) whether this Canvas is archived,
 "draft": (boolean) whether this Canvas is a draft,
 "enabled": (boolean) whether this Canvas is active or not,
 "has_post_launch_draft": (boolean) whether this Canvas has a post-launch draft,
 "schedule_type": (string) the type of scheduling action,
 "first_entry": (string) the date of first entry as ISO 8601 date,
 "last_entry": (string) the date of last entry as ISO 8601 date,
 "channels": (array of strings) step channels used with Canvas,
 "variants": [
 {
 "name": (string) the name of variant,
 "id": (string) the API identifier of the variant,
 "first_step_ids": (array of strings) the API identifiers for first steps in variant,
 "first_step_id": (string) the API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)
 },
 ... (more variations)
 ],
 "tags": (array of strings) the tag names associated with the Canvas,
 "teams" : (array) the names of the Teams associated with the Canvas,
 "steps": [
 {
 "name": (string) the name of step,
 "type" (string) the type of Canvas component,
 "id": (string) the API identifier of the step,
 "next_step_ids": (array of strings) IDs for next steps that are full steps or Message steps,
 "next_paths": { (array of objects)
 // for Decision Splits, this property should evaluate to "Yes" or "No"
 // for Audience Path and Action Paths, this property should evaluate to the group name
 // for Experiment Paths, this property should evaluate to the path name
 // for other steps, this property should evaluate to "null"
 "name": (string) name the name of step,
 "next_step_id": (string) IDs for next steps that are full steps or Message steps,
 }
 "channels": (array of strings) the channels used in step,
 "messages": {
 "message_variation_id": (string) { // <=This is the actual id
 "channel": (string) the channel type of the message (for example, "email"),
 "has_translatable_content": (boolean) whether the message has translatable content (only present if `include_has_translatable_content` is true); `true` if locales are configured and the message contains at least one translation tag; `false` if no locales are configured or no translation tags detected; `null` if detection could not be completed,
 // channel-specific fields for this message, see Campaign Details endpoint API Response for example message responses
 }
 }
 },
 ... (more steps)
 ],
 "message": (string) returns 'success' when the request completes without errors
}

```
 | 

### Messages by channel

The following is an example response that includes Canvas messages sent through different channels (email, push, SMS, and in-app messages):

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

```
 | 
```
{
 "message": "success",
 "created_at": "2023-01-01T12:00:00Z",
 "updated_at": "2023-01-10T12:00:00Z",
 "name": "Multi-Channel Engagement",
 "description": "Complete profile reminder via multiple channels",
 "archived": false,
 "draft": false,
 "enabled": true,
 "has_post_launch_draft": true,
 "schedule_type": "date",
 "first_entry": "2023-01-01T12:00:00Z",
 "last_entry": "2023-01-10T12:00:00Z",
 "channels": ["email", "push", "sms", "in_app_message"],
 "variants": [
 {
 "name": "Variant 1",
 "id": "variant_1_id",
 "first_step_ids": ["step_1"]
 }
 ],
 "tags": ["engagement", "multi-channel"],
 "teams": ["Marketing Team"],
 "steps": [
 {
 "name": "Welcome Email",
 "type": "email",
 "id": "step_1",
 "next_step_ids": ["step_2"],
 "next_paths": [
 {
 "name": "Next Step",
 "next_step_id": "step_2"
 }
 ],
 "channels": ["email"],
 "messages": {
 "message_1": {
 "channel": "email",
 "subject": "Welcome to Kitchenerie!",
 "body": "<html><body>Welcome to the Kitchenerie family, !</body></html>",
 "created_at": "2023-01-01T12:00:00Z",
 "updated_at": "2023-01-01T12:00:00Z"
 }
 }
 },
 {
 "name": "Follow-Up Push Notification",
 "type": "push",
 "id": "step_2",
 "next_step_ids": ["step_3"],
 "next_paths": [
 {
 "name": "Next Step",
 "next_step_id": "step_3"
 }
 ],
 "channels": ["push"],
 "messages": {
 "message_2": {
 "channel": "push",
 "title": "Don't Forget to Complete Your Kitchenerie Profile",
 "body": "Complete your Kitchenerie profile for access to special offers and local events.",
 "created_at": "2023-01-02T12:00:00Z",
 "updated_at": "2023-01-02T12:00:00Z"
 }
 }
 },
 {
 "name": "Reminder SMS",
 "type": "sms",
 "id": "step_3",
 "next_step_ids": ["step_4"],
 "next_paths": [
 {
 "name": "Next Step",
 "next_step_id": "step_4"
 }
 ],
 "channels": ["sms"],
 "messages": {
 "message_3": {
 "channel": "sms",
 "body": "Hi , remember to complete Kitchenerie your profile!",
 "created_at": "2023-01-03T12:00:00Z",
 "updated_at": "2023-01-03T12:00:00Z"
 }
 }
 },
 {
 "name": "In-App Message",
 "type": "in_app_message",
 "id": "step_4",
 "next_step_ids": [],
 "next_paths": [],
 "channels": ["in_app_message"],
 "messages": {
 "message_4": {
 "channel": "in_app_message",
 "header": "Complete Your Kitchenerie Profile",
 "body": "Complete your Kitchenerie profile to unlock access to savings and local events!",
 "created_at": "2023-01-04T12:00:00Z",
 "updated_at": "2023-01-04T12:00:00Z"
 }
 }
 }
 ]
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
