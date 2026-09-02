---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog
slug: docs__api__endpoints__catalogs__catalog_management__synchronous__post_create_catalog
title: "Create catalog"
description: "This article outlines details about the Create catalog Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create catalog

post

/catalogs

Use this endpoint to create a catalog.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.create permission.

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog endpoints, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 catalogs | 
 Required | 
 Array | 
 An array that contains catalog objects. Only one catalog object is allowed for this request. | 

### Catalog object parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 name | 
 Required | 
 String | 
 The name of the catalog that you want to create. | 

 description | 
 Required | 
 String | 
 The description of the catalog that you want to create. | 

 fields | 
 Required | 
 Array | 
 An array of objects where the object contains keys name and type. | 

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

```
 | 
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
 {
 "name": "restaurants",
 "description": "My Restaurants",
 "fields": [
 {
 "name": "id",
 "type": "string"
 },
 {
 "name": "Name",
 "type": "string"
 },
 {
 "name": "City",
 "type": "string"
 },
 {
 "name": "Cuisine",
 "type": "string"
 },
 {
 "name": "Rating",
 "type": "number"
 },
 {
 "name": "Loyalty_Program",
 "type": "boolean"
 },
 {
 "name": "Location",
 "type": "geo"
 },
 {
 "name": "Preferences",
 "type": "object"
 },
 {
 "name": "Top_Dishes",
 "type": "array"
 },
 {
 "name": "Created_At",
 "type": "time"
 }
 ]
 }
 ]
}'

```
 | 

note

The geo data type stores a geographic coordinate as an array formatted as [longitude, latitude]. For example, [-73.988103, 40.779109].

## Response

There are two status code responses for this endpoint: 201 and 400.

### Example success response

The status code 201 could return the following response body.

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

```
 | 
```
{
 "catalogs": [
 {
 "description": "My Restaurants",
 "fields": [
 {
 "name": "id",
 "type": "string"
 },
 {
 "name": "Name",
 "type": "string"
 },
 {
 "name": "City",
 "type": "string"
 },
 {
 "name": "Cuisine",
 "type": "string"
 },
 {
 "name": "Rating",
 "type": "number"
 },
 {
 "name": "Loyalty_Program",
 "type": "boolean"
 },
 {
 "name": "Location",
 "type": "geo"
 },
 {
 "name": "Preferences",
 "type": "object"
 },
 {
 "name": "Top_Dishes",
 "type": "array"
 },
 {
 "name": "Created_At",
 "type": "time"
 }
 ],
 "name": "restaurants",
 "num_items": 0,
 "updated_at": "2022-11-02T20:04:06.879+00:00"
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
 "id": "catalog-name-already-exists",
 "message": "A catalog with that name already exists",
 "parameters": [
 "name"
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

 catalog-array-invalid | 
 catalogs must be an array of objects. | 

 catalog-name-already-exists | 
 Catalog with that name already exists. | 

 catalog-name-too-large | 
 Character limit for a catalog name is 250. | 

 description-too-long | 
 Character limit for description is 250. | 

 field-names-not-unique | 
 The same field name is referenced twice. | 

 field-names-too-large | 
 Character limit for a field name is 250. | 

 id-not-first-column | 
 The id must be the first field in the array. Check that the type is a string. | 

 invalid-catalog-name | 
 Catalog name can only include letters, numbers, hyphens, and underscores. | 

 invalid-field-names | 
 Fields can only include letters, numbers, hyphens, and underscores. | 

 invalid-field-types | 
 Make sure the field types are valid. | 

 invalid-fields | 
 fields is not formatted correctly. | 

 too-many-catalog-atoms | 
 You can only create one catalog per request. | 

 too-many-fields | 
 Number of fields limit is 500. | 

- 

New Stuff!
