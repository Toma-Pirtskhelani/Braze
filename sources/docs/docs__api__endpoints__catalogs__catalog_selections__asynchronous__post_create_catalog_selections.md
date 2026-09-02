---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections
slug: docs__api__endpoints__catalogs__catalog_selections__asynchronous__post_create_catalog_selections
title: "Create catalog selection"
description: "This article outlines details about the Create catalog selection Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create catalog selection

post

/catalogs/{catalog_name}/selections

Use this endpoint to create a selection in your catalog.

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.create_selection permission.

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all asynchronous catalog fields and selections endpoints, as documented in API rate limits.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 catalog_name | 
 Required | 
 String | 
 Name of the catalog. | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 selection | 
 Required | 
 Object | 
 An object that contains selection criteria. See catalog selection object for a full breakdown of the object and its fields. | 

### Selection object parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 name | 
 Required | 
 String | 
 The name of the catalog selection. | 

 description | 
 Optional | 
 String | 
 A description of the catalog selection. | 

 external_id | 
 Optional | 
 String | 
 A unique identifier for the selection. | 

 source | 
 Optional | 
 String | 
 The source of the catalog data. For Shopify catalogs, set this to "Shopify". Accepted values are "Shopify" and "Braze". | 

 filters | 
 Required | 
 Array | 
 An array of filter objects to apply to the catalog items. You can specify up to ten filters per request. If an empty array of filters is provided, all items from the catalog are included. | 

 results_limit | 
 Required | 
 Integer | 
 The maximum number of results to return. Must be a number between 1 and 50. | 

 sort_field | 
 Optional | 
 String | 
 The field to sort results by. This must be paired with sort_order. If both sort_field and sort_order are not present, the results are randomized. | 

 sort_order | 
 Optional | 
 String | 
 The order to sort results. Accepted values are "asc" (ascending) or "desc" (descending). This must be paired with sort_field. If both sort_field and sort_order are not present, the results are randomized. | 

note

The sort_field and sort_order parameters must be used together. If you provide one without the other, or if you omit both parameters, the selection results are returned in a randomized order.

## Example Request

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

```
 | 
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "selection": {
 "name": "favorite-restaurants",
 "description": "Favorite restaurants in NYC",
 "external_id": "favorite-nyc-restaurants",
 "source": "Braze",
 "filters": [
 {
 "field": "City",
 "operator": "equals",
 "value": "NYC"
 },
 {
 "field": "Rating",
 "operator": "greater than",
 "value": 7
 }
 ],
 "results_limit": 10,
 "sort_field": "Rating",
 "sort_order": "desc"
 }
}'

```
 | 

### Filter operators

 Field type | 
 Supported operators | 

 string | 
 equals, does not equal | 

 number | 
 equals, does not equal, greater than, less than | 

 boolean | 
 is | 

 time | 
 before, after | 

 array | 
 includes value, does not include value | 

 geo | 
 geo within, geo outside | 

note

The API supports a maximum of ten filters per selection request. Filters are applied in the order they appear in the array.

note

When you apply a geo filter, the system automatically sorts results by distance with the nearest item first, regardless of the sort_field and sort_order parameters.

## Response

There are three status code responses for this endpoint: 202, 400, and 404.

### Example success response

The status code 202 could return the following response body.

```

1
2
3

```
 | 
```
{
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
 "id": "catalog-not-found",
 "message": "Could not find catalog",
 "parameters": [
 "catalog_name"
 ],
 "parameter_values": [
 "restaurants"
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

 company-size-limit-already-reached | 
 The catalog storage size limit is reached. | 

 selection-limit-reached | 
 The catalog selections limit is reached. | 

 invalid-selection | 
 Check that the selection is valid. | 

 too-many-filters | 
 Check if the selection has too many filters. | 

 selection-name-already-exists | 
 Check if the selection name already exists in the catalog. | 

 selection-has-invalid-filter | 
 Check if the selection filter is valid. | 

 selection-invalid-results-limit | 
 Check if the selection results limit is valid. | 

 invalid-sorting | 
 Check if the selection sorting is valid. | 

 invalid-sort-field | 
 Check if the selection sort field is valid. | 

 invalid-sort-order | 
 Check if the selection sort order is valid. | 

 selection-contains-too-many-arrays | 
 Check if the selection contains more than one field with array type. Only one is supported. | 

- 

New Stuff!
