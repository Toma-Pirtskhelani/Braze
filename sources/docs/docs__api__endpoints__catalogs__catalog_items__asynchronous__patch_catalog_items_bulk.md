---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk
slug: docs__api__endpoints__catalogs__catalog_items__asynchronous__patch_catalog_items_bulk
title: "Edit multiple catalog items"
description: "This article outlines details about the Edit multiple catalog items Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Edit multiple catalog items

patch

/catalogs/{catalog_name}/items

Use this endpoint to edit multiple existing items in your catalog.

Each request can support up to 50 items. This endpoint is asynchronous.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.update_items permission.

## Rate limit

This endpoint has a shared rate limit of 16,000 requests per minute between all asynchronous catalog item endpoints, as documented in API rate limits.

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

 items | 
 Required | 
 Array | 
 An array that contains item objects. The item objects should contain fields that exist in the catalog. Up to 50 item objects are allowed per request. | 

## Example request

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

```
 | 
```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
 {
 "id": "restaurant1",
 "Name": "Restaurant",
 "Loyalty_Program": false,
 "Location": [-73.988103, 40.779109],
 "Preferences": {
 "favorite_brand": "Nike",
 "shirt_size": "L"
 },
 "Top_Dishes": {
 "$add": [
 "Biscuits",
 "Coleslaw"
 ],
 "$remove": [
 "French Fries"
 ]
 },
 "Open_Time": "2021-09-03T09:03:19.967+00:00"
 },
 {
 "id": "restaurant3",
 "City": "San Francisco",
 "Rating": 2,
 "Top_Dishes": [
 "Buffalo Wings",
 "Philly Cheesesteak"
 ]
 }
 ]
}'

```
 | 

note

- The Location field uses the geo data type, which expects an array formatted as [longitude, latitude].
 
- The $add and $remove operators are only applicable to array type fields, and are only supported by PATCH endpoints.

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
 "id": "invalid-fields",
 "message": "Some of the fields given do not exist in the catalog",
 "parameters": [
 "id"
 ],
 "parameter_values": [
 "restaurant1"
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

 ids-too-large | 
 Item IDs can’t be more than 250 characters. | 

 ids-not-strings | 
 Item IDs must be of type string. | 

 ids-not-unique | 
 Item IDs must be unique in the request. | 

 invalid-ids | 
 Item IDs can only include letters, numbers, hyphens, and underscores. | 

 invalid-fields | 
 Confirm that all fields you are sending in the API request already exist in the catalog. This is not related to the ID field mentioned in the error. | 

 invalid-keys-in-value-object | 
 Item object keys can’t include . or $. | 

 items-missing-ids | 
 Some items don’t have item IDs. Check that each item has an item ID. | 

 item-array-invalid | 
 items must be an array of objects. | 

 items-too-large | 
 Item values can’t exceed 5,000 characters. | 

 request-includes-too-many-items | 
 Your request has too many items. The item limit per request is 50. | 

 too-deep-nesting-in-value-object | 
 Item objects can’t have more than 50 levels of nesting. | 

 unable-to-coerce-value | 
 Item types can’t be converted. | 

- 

New Stuff!
