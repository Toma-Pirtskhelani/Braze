---
url: https://www.braze.com/docs/api/endpoints/export/purchases/get_number_of_purchases
slug: docs__api__endpoints__export__purchases__get_number_of_purchases
title: "Export number of purchases"
description: "This article outlines details about the Export number of purchases Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export number of purchases

get

/purchases/quantity_series

Use this endpoint to return the total number of purchases in your app over a time range.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the purchases.quantity_series permission.

## Rate limit

We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the /custom_attributes, /events, and /events/list endpoints, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 ending_at | 
 Optional | 
 Datetime (ISO-8601 string) | 
 Date on which the data export should end. Defaults to time of the request. | 

 length | 
 Required | 
 Integer | 
 Maximum number of days before ending_at to include in the returned series. Must be between 1 and 100 (inclusive). | 

 unit | 
 Optional | 
 String | 
 Unit of time between data points. Can be day or hour, defaults to day. | 

 app_id | 
 Optional | 
 String | 
 App API identifier retrieved from the API Keys page. If excluded, results for all apps in a workspace will be returned. | 

 product | 
 Optional | 
 String | 
 Name of product to filter response by. If excluded, results for all apps will be returned. | 

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
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
 "purchase_quantity" : (int) the number of items purchased in the time period
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
