---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field
slug: docs__api__endpoints__catalogs__catalog_fields__asynchronous__delete_catalog_field
title: "Delete catalog field"
description: "This article outlines details about the Delete catalog field Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete catalog field

delete

/catalogs/{catalog_name}/fields/{field_name}

Use this endpoint to delete a catalog field.

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.delete_fields permission.

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

 field_name | 
 Required | 
 String | 
 Name of the catalog field. | 

## Example request

```

1
2
3

```
 | 
```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/fields/ratings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \

```
 | 

## Response

There are two status code responses for this endpoint: 202 and 404.

### Example success response

The status code 202 could return the following response body:

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

The status code 404 could return the following response body. Refer to Troubleshooting for more information about errors you may encounter.

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

 field-referenced-by-selection | 
 Check that the catalog field is currently in use by a selection. | 

 field-is-inventory | 
 Check that the catalog field is used as an inventory field. | 

 invalid-field-name | 
 Check that the catalog field name is valid. | 

- 

New Stuff!
