---
url: https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_dau_date
slug: docs__api__endpoints__export__kpi__get_kpi_dau_date
title: "Export daily active users by date"
description: "This article outlines details about the Export daily active users Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export daily active users by date

get

/kpi/dau/data_series

Use this endpoint to retrieve a daily series of the total number of unique active users on each date.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the kpi.dau.data_series permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 length | 
 Required | 
 Integer | 
 Maximum number of days before ending_at to include in the returned series. Must be between 1 and 100 (inclusive). | 

 ending_at | 
 Optional | 
 Datetime 
(ISO-8601 string) | 
 Date on which the data series should end. Defaults to time of the request. | 

 app_id | 
 Optional | 
 String | 
 App API identifier retrieved from the API Keys page. If excluded, results for all apps in workspace will be returned. | 

## Example request

```

1
2

```
 | 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/dau/data_series?length=10&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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

```
 | 
```
{
 "message": (string) returns 'success' when the request completes without errors,
 "data" : [
 {
 "time" : (string) the date as ISO 8601 date,
 "dau" : (int) the number of daily active users
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
