---
url: https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics_summary
slug: docs__api__endpoints__export__canvas__get_canvas_analytics_summary
title: "Export Canvas data summary analytics"
description: "This article describes the Export Canvas data summary analytics Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export Canvas data summary analytics

get

/canvas/data_summary

Use this endpoint to export rollups of time series data for a Canvas, providing a concise summary of Canvas results.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the canvas.data_summary permission.

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
 See Canvas API identifier. | 

 ending_at | 
 Required | 
 Datetime 
(ISO-8601 string) | 
 End date for the data export. Defaults to the time of the request. | 

 starting_at | 
 Optional* | 
 Datetime 
(ISO-8601 string) | 
 Start date for the data export. 

* Either length or starting_at is required. | 

 length | 
 Optional* | 
 String | 
 Maximum number of days before ending_at included in the returned series. Must be between 1 and 14 (inclusive). 

* Either length or starting_at is required. | 

 include_variant_breakdown | 
 Optional | 
 Boolean | 
 Whether to include variant statistics (defaults to false). | 

 include_step_breakdown | 
 Optional | 
 Boolean | 
 Whether to include step statistics (defaults to false). | 

 include_deleted_step_data | 
 Optional | 
 Boolean | 
 Whether to include step statistics for deleted steps (defaults to false). | 

important

Canvas analytics are aggregated by day in your company’s configured time zone in Braze (the same time zone the dashboard uses). The API normalizes starting_at and ending_at to midnight in that time zone. Make sure your timestamps align with your company’s time zone so that your stats match the dashboard. For example, if your company time is UTC+2, then the timestamp should be 12 am UTC+2.

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

### Conversion event fields

The response includes one pair of conversion fields for each conversion event configured on the Canvas. The primary conversion event uses conversions and conversions_by_entry_time. Each additional event uses the same base name with a numeric suffix that starts at 1 for the second event and increases by one for each additional event.

 Conversion event order on the Canvas | 
 Conversions field | 
 By entry time field | 

 Primary | 
 conversions | 
 conversions_by_entry_time | 

 Second | 
 conversions1 | 
 conversions1_by_entry_time | 

 Third | 
 conversions2 | 
 conversions2_by_entry_time | 

 Fourth | 
 conversions3 | 
 conversions3_by_entry_time | 

Fifth and later events follow the same pattern (for example, conversions4 and conversions4_by_entry_time). These fields appear in total_stats and, when you request breakdowns, in variant_stats and step_stats using the same names.

note

In total_stats, variant_stats, and step_stats, conversions is the count for the primary conversion event of the Canvas. When you configure additional conversion events, the payload can also include conversions1, conversions2, and higher-indexed fields for the second, third, and further events. This is similar to the multivariate response for the ` /campaigns/data_series endpoint. Where present, fields ending in _by_entry_time` attribute those conversions by Canvas entry time.

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

```
 | 
```
{
 "data": {
 "name": (string) the Canvas name,
 "total_stats": {
 "revenue": (float) the number of dollars of revenue (USD),
 "entries": (int) the number of entries,
 "conversions": (int) the number of conversions for the primary conversion event,
 "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
 "conversions1": (optional, int) the number of conversions for the second conversion event,
 "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
 "conversions2": (optional, int) the number of conversions for the third conversion event,
 "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
 "conversions3": (optional, int) the number of conversions for the fourth conversion event,
 "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time
 },
 "variant_stats": (optional) {
 "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
 "name": (string) the name of the variant,
 "revenue": (float) the number of dollars of revenue (USD),
 "conversions": (int) the number of conversions for the primary conversion event,
 "conversions_by_entry_time": (optional, int) the number of conversions for the primary conversion event by entry time,
 "conversions1": (optional, int) the number of conversions for the second conversion event,
 "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
 "conversions2": (optional, int) the number of conversions for the third conversion event,
 "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
 "conversions3": (optional, int) the number of conversions for the fourth conversion event,
 "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
 "entries": (int) the number of entries
 },
 ... (more variants)
 },
 "step_stats": (optional) {
 "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
 "name": (string) the name of the step,
 "revenue": (float) the number of dollars of revenue (USD),
 "conversions": (int) the number of conversions for the primary conversion event,
 "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
 "conversions1": (optional, int) the number of conversions for the second conversion event,
 "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
 "conversions2": (optional, int) the number of conversions for the third conversion event,
 "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
 "conversions3": (optional, int) the number of conversions for the fourth conversion event,
 "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
 "messages": {
 "android_push": (name of channel) [
 {
 "sent": (int) the number of sends,
 "opens": (int) the number of opens,
 "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
 "bounces": (int) the number of bounces
 ... (more stats for channel)
 }
 ],
 ... (more channels)
 }
 },
 ... (more steps)
 }
 },
 "message": (string) returns 'success' when the request completes without errors
}

```
 | 

important

In the API response, the influenced_opens field represents the total number of opens (both direct and influenced opens combined). In the Braze dashboard, “influenced opens” refers only to influenced opens, excluding direct opens. This is due to a legacy naming convention in the API.

## Related articles

- Export troubleshooting

- 

New Stuff!
