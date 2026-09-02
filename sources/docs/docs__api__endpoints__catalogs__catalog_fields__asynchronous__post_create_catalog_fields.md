---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields
slug: docs__api__endpoints__catalogs__catalog_fields__asynchronous__post_create_catalog_fields
title: "Create catalog fields"
description: "This article outlines details about the Create catalog fields Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create catalog fields

post

/catalogs/{catalog_name}/fields

Use this endpoint to create multiple fields in your catalog.

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.create_fields permission.

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

 fields | 
 Required | 
 Array | 
 An array that contains field objects. The fields objects should contain the name and type of the new fields. | 

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
27

```
 | 
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "fields": [
 {
 "name": "Name",
 "type": "string"
 },
 {
 "name": "Ratings",
 "type": "number"
 },
 {
 "name": "Loyalty_Program",
 "type": "boolean"
 },
 {
 "name": "Created_At",
 "type": "time"
 },
 {
 "name": "Location",
 "type": "geo"
 }
 ]
}'

```
 | 

note

You must provide geolocation field values as a [longitude, latitude] array—for example, [-73.988103, 40.779109]. Latitude must be between -90 and 90; longitude must be between -180 and 180.

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

 arbitrary-error | 
 An arbitrary error occurred. Please try again or contact Support. | 

 catalog-not-found | 
 Check that the catalog name is valid. | 

 company-size-limit-already-reached | 
 The catalog storage size limit is reached. | 

 request-includes-too-many-fields | 
 Each request can support up to 50 new fields. | 

 catalog-exceeds-fields-limit | 
 Catalog cannot have more than 500 fields. | 

- 

New Stuff!
