---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details
slug: docs__api__endpoints__catalogs__catalog_items__synchronous__get_catalog_item_details
title: "List catalog item details"
description: "This article outlines details about the List catalog item details Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List catalog item details

get

/catalogs/{catalog_name}/items/{item_id}

Use this endpoint to return a catalog item and its content.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.get_item permission.

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog item endpoints, as documented in API rate limits.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 catalog_name | 
 Required | 
 String | 
 Name of the catalog. | 

 item_id | 
 Required | 
 String | 
 The ID of the catalog item. | 

## Request parameters

There is no request body for this endpoint.

## Example request

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

There are two status code responses for this endpoint: 200 and 404.

### Example success response

The status code 200 could return the following response body.

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

```
 | 
```
{
 "items": [
 {
 "id": "restaurant3",
 "Name": "Restaurant1",
 "City": "New York",
 "Cuisine": "American",
 "Rating": 5,
 "Loyalty_Program": true,
 "Open_Time": "2022-11-01T09:03:19.967Z"
 }
 ],
 "message": "success"
}

```
 | 

### Example error response

The status code 404 could return the following response. Refer to Troubleshooting for more information about errors you may encounter.

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

```
 | 
```
{
 "errors": [
 {
 "id": "item-not-found",
 "message": "Could not find item",
 "parameters": [
 "item_id"
 ],
 "parameter_values": [
 "restaurant34"
 ]
 }
 ],
 "message": "Invalid Request"
}

```
 | 

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps, if applicable.

 Error | 
 Troubleshooting | 

 catalog-not-found | 
 Check that the catalog name is valid. | 

 item-not-found | 
 Check that the item is in the catalog. | 

- 

New Stuff!
