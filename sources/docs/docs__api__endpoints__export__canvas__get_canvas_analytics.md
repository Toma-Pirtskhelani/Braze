---
url: https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics
slug: docs__api__endpoints__export__canvas__get_canvas_analytics
title: "Export Canvas data series analytics"
description: "This article outlines details about the Export Canvas data series analytics Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export Canvas data series analytics

get

/canvas/data_series

Use this endpoint to export time series data for a Canvas.

note

Counts from this endpoint do not always match dashboard Canvas analytics or aggregates you build from Currents one-for-one. Dashboard metrics and API time series use different aggregation windows and definitions than raw Currents events. For common reconciliation notes, see Currents FAQ.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the canvas.data_series permission.

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
 Date on which the data export should end. Defaults to time of the request. | 

 starting_at | 
 Optional* | 
 Datetime 
(ISO-8601 string) | 
 Date on which the data export should begin. 

* Either length or starting_at is required. | 

 length | 
 Optional* | 
 String | 
 Maximum number of days before ending_at to include in the returned series. Must be between 1 and 14 (inclusive). 

* Either length or starting_at is required. | 

 include_variant_breakdown | 
 Optional | 
 Boolean | 
 Whether or not to include variant statistics (defaults to false). | 

 include_step_breakdown | 
 Optional | 
 Boolean | 
 Whether or not to include step statistics (defaults to false). | 

 include_deleted_step_data | 
 Optional | 
 Boolean | 
 Whether or not to include step statistics for deleted steps (defaults to false). | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
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
 "stats": [
 {
 "time": (string) the date as ISO 8601 date,
 "total_stats": {
 "revenue": (float) the number of dollars of revenue (USD),
 "conversions": (int) the number of conversions,
 "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
 "entries": (int) the number of entries
 },
 "variant_stats": (optional) {
 "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
 "name": (string) the name of variant,
 "revenue": (float) the number of dollars of revenue (USD),
 "conversions": (int) the number of conversions,
 "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
 "entries": (int) the number of entries
 },
 ... (more variants)
 },
 "step_stats": (optional) {
 "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
 "name": (string) the name of step,
 "revenue": (float) the number of dollars of revenue (USD),
 "conversions": (int) the number of conversions,
 "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
 "messages": {
 "email": [
 {
 "sent": (int) the number of sends,
 "opens": (int) the number of opens,
 "unique_opens": (int) the number of unique opens,
 "clicks": (int) the number of clicks
 ... (more stats)
 }
 ],
 "sms" : [
 {
 "sent": (int) the number of sends,
 "sent_to_carrier" : (int) the number of messages sent to the carrier,
 "delivered": (int)the number of delivered messages,
 "rejected": (int) the number of rejected messages,
 "delivery_failed": (int) the number of failed deliveries,
 "clicks": (int) the number of clicks on shortened links,
 "opt_out" : (int) the number of opt outs,
 "help" : (int) the number of help messages received
 }
 ],
 ... (more channels)
 }
 },
 ... (more steps)
 }
 },
 ... (more stats by time)
 ]
 },
 "message": (string) returns 'success' when the request completes without errors
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
