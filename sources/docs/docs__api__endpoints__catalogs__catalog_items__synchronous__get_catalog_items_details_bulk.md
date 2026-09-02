---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk
slug: docs__api__endpoints__catalogs__catalog_items__synchronous__get_catalog_items_details_bulk
title: "List multiple catalog item details"
description: "This article outlines details about the List multiple catalog item details Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List multiple catalog item details

get

/catalogs/{catalog_name}/items

Use this endpoint to return multiple catalog items and their content.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.get_items permission.

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

## Query parameters

Note that each call to this endpoint will return 50 items. For a catalog with more than 50 items, use the Link header to retrieve the data on the next page as shown in the following example response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 cursor | 
 Optional | 
 String | 
 Determines the pagination of the catalog items. | 

## Request parameters

There is no request body for this endpoint.

## Example requests

### Without cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

### With cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

There are three status code responses for this endpoint: 200, 400, and 404.

### Example success response

The status code 200 could return the following response header and body.

note

The Link header won’t exist if the catalog has less than or equal to 50 items. For calls without a cursor, prev will not show. When looking at the last page of items, next will not show.

```

1

```
 | 
```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"

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

```
 | 
```
{
 "items": [
 {
 "id": "restaurant1",
 "Name": "Restaurant1",
 "City": "New York",
 "Cuisine": "American",
 "Rating": 5,
 "Loyalty_Program": true,
 "Open_Time": "2022-11-02T09:03:19.967Z"
 },
 {
 "id": "restaurant2",
 "Name": "Restaurant2",
 "City": "New York",
 "Cuisine": "American",
 "Rating": 10,
 "Loyalty_Program": true,
 "Open_Time": "2022-11-02T09:03:19.967Z"
 },
 {
 "id": "restaurant3",
 "Name": "Restaurant3",
 "City": "New York",
 "Cuisine": "American",
 "Rating": 5,
 "Loyalty_Program": false,
 "Open_Time": "2022-11-02T09:03:19.967Z"
 }
 ],
 "message": "success"
}

```
 | 

### Example error response

The status code 400 could return the following response body. Refer to Troubleshooting for more information about errors you may encounter.

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
 "id": "invalid-cursor",
 "message": "'cursor' is not valid",
 "parameters": [
 "cursor"
 ],
 "parameter_values": [
 "bad-cursor"
 ]
 }
 ],
 "message": "Invalid Request"
}

```
 | 

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

 Error | 
 Troubleshooting | 

 catalog-not-found | 
 Check that the catalog name is valid. | 

 invalid-cursor | 
 Check that your cursor is valid. | 

- 

New Stuff!
