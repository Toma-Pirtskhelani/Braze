---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item
slug: docs__api__endpoints__catalogs__catalog_items__synchronous__post_create_catalog_item
title: "Create catalog item"
description: "This article outlines details about the Create catalog item Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create catalog item

post

/catalogs/{catalog_name}/items/{item_id}

Use this endpoint to create an item in your catalog.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.create_item permission.

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

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 items | 
 Required | 
 Array | 
 An array that contains item objects. The item objects should contain all of the fields in the catalog except for the id field. Only one item object is allowed per request. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
 {
 "Name": "Restaurant1",
 "City": "New York",
 "Cuisine": "American",
 "Rating": 5,
 "Loyalty_Program": true,
 "Location": [-73.988103, 40.779109],
 "Preferences": {
 "favorite_brand": "Nike",
 "shirt_size": "L"
 },
 "Top_Dishes": [
 "Hamburger",
 "Deluxe Cheeseburger"
 ],
 "Created_At": "2022-11-01T09:03:19.967+00:00"
 }
 ]
}'

```
 | 

note

The Location field uses the geo data type, which expects an array formatted as [longitude, latitude].

## Response

There are three status code responses for this endpoint: 201, 400, and 404.

### Example success response

The status code 201 could return the following response body.

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

 arbitrary-error | 
 An arbitrary error occurred. Please try again or contact Support. | 

 catalog-not-found | 
 Check that the catalog name is valid. | 

 filtered-set-field-too-long | 
 The field value is being used in a filtered set that exceeds the character limit for an item. | 

 id-in-body | 
 Remove any item IDs in the request body. | 

 ids-too-large | 
 Character limit for each item ID is 250 characters. | 

 invalid-ids | 
 Supported characters for item ID names are letters, numbers, hyphens, and underscores. | 

 invalid-fields | 
 Confirm that all fields you are sending in the API request already exist in the catalog. This is not related to the ID field mentioned in the error. | 

 invalid-keys-in-value-object | 
 Item object keys can’t include . or $. | 

 item-already-exists | 
 The item already exists in the catalog. | 

 item-array-invalid | 
 items must be an array of objects. | 

 items-too-large | 
 Character limit for each item is 5,000 characters. | 

 request-includes-too-many-items | 
 You can only create one catalog item per request. | 

 too-deep-nesting-in-value-object | 
 Item objects can’t have more than 50 levels of nesting. | 

 unable-to-coerce-value | 
 Item types can’t be converted. | 

- 

New Stuff!
