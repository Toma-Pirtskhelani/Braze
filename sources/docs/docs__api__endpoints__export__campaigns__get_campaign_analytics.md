---
url: https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics
slug: docs__api__endpoints__export__campaigns__get_campaign_analytics
title: "Export campaign analytics"
description: "This article outlines details about the Export campaign analytics Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export campaign analytics

get

/campaigns/data_series

Use this endpoint to retrieve a daily series of various stats for a campaign over time.

Data returned includes how many messages were sent, opened, clicked, or converted by messaging channel.

note

Counts from this endpoint do not always match dashboard engagement analytics or aggregates you build from Currents one-for-one. Dashboard metrics and API time series use different aggregation windows and definitions than raw Currents events. For common reconciliation notes, see Currents FAQ.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the campaigns.data_series permission.

## Rate limit

This endpoint has a rate limit of 50,000 requests per minute.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 campaign_id | 
 Required | 
 String | 
 See campaign API identifier.

 The campaign_id for API campaigns can be found on the API Keys page and the Campaign Details page within your dashboard, or you can use the List campaigns endpoint. | 

 length | 
 Required | 
 Integer | 
 Maximum number of days before ending_at to include in the returned series. Must be between 1 and 100 (inclusive). | 

 ending_at | 
 Optional | 
 Datetime 
(ISO-8601 string) | 
 Date on which the data series should end. Defaults to time of the request. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Responses

### Multichannel response

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

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "data" : [
 {
 "time": (string) the date as ISO 8601 date,
 "conversions_by_send_time": (optional, int),
 "conversions1_by_send_time": (optional, int),
 "conversions2_by_send_time": (optional, int),
 "conversions3_by_send_time": (optional, int),
 "conversions": (optional, int),
 "conversions1": (optional, int),
 "conversions2": (optional, int),
 "conversions3": (optional, int),
 "unique_recipients": (int),
 "revenue": (optional, float)
 "messages" : {
 "ios_push" : [
 {
 "variation_api_id": (string) the variation API identifier,
 "sent" : (int) the number of sends,
 "direct_opens" : (int) the number of direct opens,
 "total_opens" : (int)the number of total opens,
 "bounces" : (int) the number of bounces,
 "body_clicks" : (int) the number of body clicks
 }
 ],
 "android_push" : [
 {
 "variation_api_id": (string) the variation API identifier,
 "sent" : (int) the number of sends,
 "direct_opens" : (int) the number of direct opens,
 "total_opens" : (int)the number of total opens,
 "bounces" : (int) the number of bounces,
 "body_clicks" : (int) the number of body clicks
 }
 ],
 "webhook": [
 {
 "variation_api_id": (string) the variation API identifier,
 "sent": (int) the number of sends,
 "errors": (int) the number of errors
 }
 ],
 "email" : [
 {
 "variation_api_id": (string) the variation API identifier,
 "sent": (int) the number of sends,
 "opens": (int) the number of opens,
 "unique_opens": (int) the number of unique opens,
 "clicks": (int) the number of clicks,
 "unique_clicks": (int) the number of unique clicks,
 "unsubscribes": (int) the number of unsubscribes,
 "bounces": (int) the number of bounces,
 "delivered": (int) the number of messages delivered,
 "reported_spam": (int) the number of messages reported as spam
 }
 ],
 "sms" : [
 {
 "variation_api_id": (string) the variation API identifier,
 "sent": (int) the number of sends,
 "sent_to_carrier" : (int) the number of messages sent to the carrier,
 "delivered": (int) the number of delivered messages,
 "rejected": (int) the number of rejected messages,
 "delivery_failed": (int) the number of failed deliveries,
 "clicks": (int) the number of clicks on shortened links,
 "opt_out" : (int) the number of opt outs,
 "help" : (int) the number of help messages received
 }
 ],
 "whats_app": [
 {
 "variation_api_id": (string) the variation API identifier,
 "sent": (int) the number of sends,
 "delivered": (int) the number of delivered messages,
 "failed": (int) the number of failed deliveries,
 "read": (int) the number of opened messages
 },
 ],
 "content_cards" : [
 {
 "variation_api_id": (string) the variation API identifier,
 "sent": (int) the number of sends,
 "total_clicks": (int) the number of total clicks,
 "total_dismissals": (int) the number of total dismissals,
 "total_impressions": (int) the number of total impressions,
 "unique_clicks": (int) the number of unique clicks,
 "unique_dismissals": (int) the number of unique dismissals,
 "unique_impressions": (int) the number of unique impressions
 }
 ],
 ...
 }
 }
 ],
}

```
 | 

### Multivariate response

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

```
 | 
```
{
 "data" : [
 {
 "time" : (string) the date as ISO 8601 date,
 "conversions" : (int) the number of conversions,
 "revenue": (float) the number of dollars of revenue (USD),
 "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
 "messages" : {
 "trigger_in_app_message": [{
 "variation_name": (optional, string) the variation name,
 "impressions": (int) the number of impressions,
 "clicks": (int) the number of clicks,
 "first_button_clicks": (int) the number of first button clicks,
 "second_button_clicks": (int) the number of second button clicks,
 "revenue": (float) the number of dollars of revenue (USD),
 "unique_recipients": (int) the number of unique recipients,
 "conversions": (int) the number of conversions,
 "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
 "conversions1": (optional, int) the number of conversions for the second conversion event,
 "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
 "conversions2": (optional, int) the number of conversions for the third conversion event,
 "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
 "conversions3": (optional, int) the number of conversions for the fourth conversion event,
 "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
 }, {
 "variation_name": (optional, string) the variation name,
 "impressions": (int) the number of impressions,
 "clicks": (int) the number of clicks,
 "first_button_clicks": (int) the number of first button clicks,
 "second_button_clicks": (int) the number of second button clicks,
 "revenue": (float) the number of dollars of revenue (USD),
 "unique_recipients": (int) the number of unique recipients,
 "conversions": (int) the number of conversions,
 "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
 "conversions1": (optional, int) the number of conversions for the second conversion event,
 "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
 "conversions2": (optional, int) the number of conversions for the third conversion event,
 "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
 "conversions3": (optional, int) the number of conversions for the fourth conversion event,
 "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
 }, {
 "variation_name": (optional, string) the variation name,
 "revenue": (float) the number of dollars of revenue (USD),
 "unique_recipients": (int) the number of unique recipients,
 "conversions": (int) the number of conversions,
 "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
 "conversions1": (optional, int) the number of conversions for the second conversion event,
 "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
 "conversions2": (optional, int) the number of conversions for the third conversion event,
 "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
 "conversions3": (optional, int) the number of conversions for the fourth conversion event,
 "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
 "enrolled": (optional, int) the number of enrolled users
 }]
 },
 "conversions_by_send_time": (optional, int),
 "conversions1_by_send_time": (optional, int),
 "conversions2_by_send_time": (optional, int),
 "conversions3_by_send_time": (optional, int),
 "conversions": (optional, int),
 "conversions1": (optional, int),
 "conversions2": (optional, int),
 "conversions3": (optional, int),
 "unique_recipients": (int),
 "revenue": (optional, float)
 }],
 ...
}

```
 | 

The possible message types are: email, trigger_in_app_message, webhook, android_push, ios_push, kindle_push, and web_push. All push message types will have the same statistics shown for android_push.

tip

For help with CSV and API exports, visit Export troubleshooting.

## Troubleshooting

### Viewing delivery failures for API-triggered campaigns

The /campaigns/data_series endpoint returns aggregated daily stats (for example, delivery_failed for SMS or errors for webhooks). It does not return per-recipient failure reasons.

For per-message send failures, bounces, and aborts from API-triggered or API campaigns, use the Message Activity Log in the dashboard. For custom reports on send and delivery events, use Query Builder with query templates or custom SQL. You can also stream failure events through Currents or Snowflake Data Sharing if your workspace has those products enabled.

- 

New Stuff!
