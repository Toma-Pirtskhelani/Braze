---
url: https://www.braze.com/docs/api/endpoints/preference_center/post_create_preference_center
slug: docs__api__endpoints__preference_center__post_create_preference_center
title: "Create preference center"
description: "This article outlines details about the Create a preference center Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create preference center

post

/preference_center/v1

Use this endpoint to create a preference center to allow users to manage their notification preferences for your email campaigns. Refer to Create a preference center with API for steps on how to build an API-generated preference center.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the preference_center.update permission.

## Rate limit

This endpoint has a rate limit of 10 requests per minute, per workspace, as documented in API rate limits.

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

```
 | 
```
{
 "name": "string",
 "preference_center_title": "string",
 "preference_center_page_html": "string",
 "confirmation_page_html": "string",
 "state": (optional) Choose `active` or `draft`. Defaults to `active` if not specified,
 "options": {
 "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag,
 "links-tags": [
 {
 "rel": "string", (required) One of the following "icon", "shortcut icon", or "apple-touch-icon",
 "type": "string", (optional) Valid values include "image/png", "image/svg", "image/gif", "image/x-icon", "image/svg+xml", "mask-icon",
 "sizes": "string", (optional),
 "color": "string", (optional) Use when type="mask-icon",
 "href": "string", (required)
 }
 ]
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 name | 
 Required | 
 String | 
 The name of the preference center that meets the following requirements: 
- Only contains letters, numbers, hyphens, and underscores 
- Does not have spaces | 

 preference_center_title | 
 Optional | 
 String | 
 The title for the preference center and confirmation pages. If a title is not specified, the title of the pages will default to “Preference Center”. | 

 preference_center_page_html | 
 Required | 
 String | 
 The HTML for the preference center page. | 

 confirmation_page_html | 
 Required | 
 String | 
 The HTML for the confirmation page. | 

 state | 
 Optional | 
 String | 
 Choose active or draft. Defaults to active if not specified. | 

 options | 
 Optional | 
 Object | 
 Attributes: 
meta-viewport-content: When present, a viewport meta tag will be added to the page with content= <value of attribute>.

 link-tags: Set a favicon for the page. When set, a <link> tag with a rel attribute is added to the page. | 

note

The preference center name can’t be edited after it’s created.

### Liquid tags

Refer to the following Liquid tags that can be included in your HTML to generate a user’s subscription state on the preference center page.

#### User subscription state

 Liquid | 
 Description | 

 {{subscribed_state.${email_global}}} | 
 Get the global email subscribed state for the user (such as “opted_in”, “subscribed”, or “unsubscribed”. | 

 {{subscribed_state.${<subscription_group_id>}}} | 
 Get the subscribed state of the specified subscription group for the user (such as “subscribed” or “unsubscribed”). | 

#### Form inputs and action

 Liquid | 
 Description | 

 {% form_field_name :email_global_state %} | 
 Indicates that a specific form input element corresponds to the user’s global email subscribed state. The user’s selection state should be “opted_in”, “subscribed”, or “unsubscribed” when the form is submitted with selection data for the global email subscribed state. If it’s a checkbox, the user will either be “opted_in” or “unsubscribed”. For a hidden input, the “subscribed” state will also be valid. | 

 {% form_field_name :subscription_group <subscription_group_id> %} | 
 Indicates that a specific form input element corresponds to a given subscription group. The user’s selection state should be either “subscribed” or “unsubscribed” when the form is submitted with selection data for a specific subscription group. | 

 {{preference_center_submit_url}} | 
 Generates URL for form submission. | 

## Example responses

### Create preference center

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
{
 "preference_center_api_id": "preference_center_api_id_example",
 "liquid_tag": "{{preference_center.${MyPreferenceCenter2022-09-22}}}",
 "created_at": "2022-09-22T18:28:07+00:00",
 "message": "success"
}

```
 | 

### HTML with form inputs

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
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161

```
 | 
```
<!doctype html>
<html lang="en">
 <head>
 <meta name="robots" content="noindex" />
 <title>Email Preferences</title>
 <script type="text/javascript">
 window.onload = () => {
 const globalUnsubscribed = '{{subscribed_state.${email_global}}}' == "unsubscribed";
 const globalSubscribedValue = '{{subscribed_state.${email_global}}}' == "opted_in" ? "opted_in" : "subscribed";
 const idStates = [
 // input format: [API_ID, '{{subscribed_state.${API_ID}}}' == "subscribed"][]
 ['3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec', '{{subscribed_state.${3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec}}}' == 'subscribed'],['7d89bdc3-4aa1-4592-8b8a-4c8b7161c875', '{{subscribed_state.${7d89bdc3-4aa1-4592-8b8a-4c8b7161c875}}}' == 'subscribed'],['5444d32e-2815-4258-964c-b9690d4ccb94', '{{subscribed_state.${5444d32e-2815-4258-964c-b9690d4ccb94}}}' == 'subscribed']
 ];

 const setState = (id, subscribed) => {
 document.querySelector(`#checkbox-${id}`).checked = subscribed;
 document.querySelector(`#value-${id}`).value = subscribed ? "subscribed" : "unsubscribed";
 };
 const setGlobal = (unsubscribed) => {
 document.querySelector(`#checkbox-global`).checked = unsubscribed;
 document.querySelector(`#value-global`).value = unsubscribed ? "unsubscribed" : globalSubscribedValue;
 idStates.forEach(([id]) => {
 document.querySelector(`#checkbox-${id}`).disabled = unsubscribed;
 });
 };

 idStates.forEach(([id, state]) => {
 setState(id, state);
 document.querySelector(`#checkbox-${id}`).onchange = ((e) => {
 setState(id, e.target.checked);
 });
 });
 setGlobal(globalUnsubscribed);
 document.querySelector(`#checkbox-global`).onchange = ((e) => {
 setGlobal(e.target.checked);
 });
 };
 </script>
 <style>
 body {
 background: #fff;
 margin: 0;
 }
 @media (max-width: 600px) {
 .main-container {
 margin-top: 0;
 width: 100%;
 }
 .main-container .content .email-input {
 width: 100%;
 }
 }
 </style>
 </head>
 <body class="vsc-initialized" style="margin: 0" bgcolor="#fff">
 <div
 class="main-container"
 style="
 background-color: #fff;
 color: #333335;
 font-family:
 Aribau Grotesk Regular,
 helvetica,
 arial,
 sans-serif;
 margin-left: auto;
 margin-right: auto;
 margin-top: 30px;
 width: 600px;
 padding: 15px 0 5px;
 "
 >
 <div class="content" style="margin-left: 20px; margin-right: 20px">

 <div>
 <h1
 style="color: #3accdd; font-size: 27px; font-weight: 400; margin-bottom: 40px; margin-top: 0"
 align="center"
 >
 Manage Email Preferences
 </h1>
 <p class="intro-text" style="font-size: 14px; margin-bottom: 20px" align="center">
 Select the emails that you want to receive.
 </p>
 </div>

 <form action="{{ preference_center_submit_url }}" method="post" accept-charset="UTF-8">
 <div>
 <h3 style="font-size: 15px; margin-bottom: 15px; margin-left: 5px; margin-top: 40px">
 Email Address: <span class="displayed-email" style="font-weight: 400">{{${email_address}}}</span>
 </h3>
 </div>
 <div class="subscription-groups-holder" style="margin-bottom: 20px"><div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
 <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
 <input type="checkbox" id="checkbox-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" class="sub_group" style="margin-right: 4px;">
 <input type="hidden" name="{% form_field_name :subscription_group 3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec %}" id="value-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" />
 Sub Group 1
 </label>
 <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">

 </p>
</div>
<div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
 <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
 <input type="checkbox" id="checkbox-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" class="sub_group" style="margin-right: 4px;">
 <input type="hidden" name="{% form_field_name :subscription_group 7d89bdc3-4aa1-4592-8b8a-4c8b7161c875 %}" id="value-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" />
 Sub Group 2
 </label>
 <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">

 </p>
</div>
<div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
 <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
 <input type="checkbox" id="checkbox-5444d32e-2815-4258-964c-b9690d4ccb94" class="sub_group" style="margin-right: 4px;">
 <input type="hidden" name="{% form_field_name :subscription_group 5444d32e-2815-4258-964c-b9690d4ccb94 %}" id="value-5444d32e-2815-4258-964c-b9690d4ccb94" />
 Sub Group 3
 </label>
 <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">

 </p>
</div>
</div>

 <div class="unsub-all" style="cursor: pointer; font-size: 13px; margin-bottom: 20px" align="center">
 <label>
 <input type="checkbox" id="checkbox-global" />
 <input
 type="hidden"
 id="value-global"
 name="{% form_field_name :email_global_state %}"
 />
 <i> Unsubscribe from all of the above types of emails </i>
 </label>
 </div>

 <div>
 <input
 class="save"
 type="submit"
 value="Save"
 style="
 background-color: rgb(71, 204, 163);
 color: #fff;
 cursor: pointer;
 display: block;
 font-size: 16px;
 text-align: center;
 text-decoration: none;
 width: 200px;
 margin: 0 auto 20px;
 padding: 12px;
 border-style: none;
 "
 />
 </div>
 </form>
 </div>
 </div>
 </body>
</html>

```
 | 

- 

New Stuff!
