---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog
slug: docs__api__endpoints__catalogs__catalog_management__synchronous__delete_catalog
title: "Delete catalog"
description: "This article outlines details about the Delete catalog Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete catalog

delete

/catalogs/{catalog_name}

Use this endpoint to delete a catalog.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.delete permission.

## Rate limit

This endpoint has a shared rate limit of 50 requests per minute between all synchronous catalog endpoints, as documented in API rate limits.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 catalog_name | 
 Required | 
 String | 
 Name of the catalog. | 

## Example request

```

1
2
3

```
 | 
```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \

```
 | 

## Response

There are two status code responses for this endpoint: 200 and 404.

### Example success response

The status code 200 could return the following response body:

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

- 

New Stuff!
