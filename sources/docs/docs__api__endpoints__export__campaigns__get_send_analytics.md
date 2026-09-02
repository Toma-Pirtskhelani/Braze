---
url: https://www.braze.com/docs/api/endpoints/export/campaigns/get_send_analytics
slug: docs__api__endpoints__export__campaigns__get_send_analytics
title: "Export send analytics"
description: "This article outlines details about the Export send analytics Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export send analytics

get

/sends/data_series

Use this endpoint to retrieve a daily series of various stats for a tracked send_id for API campaigns.

Braze stores send analytics for 14 days after the send. Campaign conversions will be attributed toward the most recent send_id that a given user has received from the campaign.

note

Send-level data_series counts do not always match dashboard engagement analytics or aggregates you build from Currents one-for-one. Dashboard metrics and API time series use different aggregation windows and definitions than raw Currents events. For common reconciliation notes, see Currents FAQ.

See me in Postman

## Prerequisites

This endpoint is for API campaigns only. To use this endpoint, you’ll need an API key with the sends.data_series permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 campaign_id | 
 Required | 
 String | 
 See campaign API identifier. | 

 send_id | 
 Required | 
 String | 
 See Send API identifier. | 

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
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

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
 "data" : [
 {
 "time": (string) the date as ISO 8601 date,
 "messages": {
 "ios_push" : [
 {
 "variation_name": (string) variation name,
 "sent": (int) the number of sends,
 "delivered": (int) the number of messages successfully delivered,
 "undelivered": (int) the number of undelivered,
 "delivery_failed": (int) the number of rejected,
 "direct_opens": (int) the number of direct opens,
 "total_opens": (int) the number of total opens,
 "bounces": (int) the number of bounces,
 "body_clicks": (int) the number of body clicks,
 "revenue": (float) the number of dollars of revenue (USD),
 "unique_recipients": (int) the number of unique recipients at the campaign-level,
 "conversions": (int) the number of conversions,
 "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
 "conversions1": (optional, int) the number of conversions for the second conversion event,
 "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
 "conversions2": (optional, int) the number of conversions for the third conversion event,
 "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
 "conversions3": (optional, int) the number of conversions for the fourth conversion event,
 "conversions3_by_send_time": (optional, int) the number of conversions for the fourth, conversion event attributed to the date the campaign was sent
 }
 ]
 },
 "conversions_by_send_time": (optional, int),
 "conversions1_by_send_time": (optional, int),
 "conversions2_by_send_time": (optional, int),
 "conversions3_by_send_time": (optional, int),
 "conversions": (int),
 "conversions1": (optional, int),
 "conversions2": (optional, int),
 "conversions3": (optional, int),
 "unique_recipients": (int),
 "revenue": (optional, float)
 }
 ],
 "message": (string) returns 'success' when the request completes without errors
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
