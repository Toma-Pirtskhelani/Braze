---
url: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk
slug: docs__api__endpoints__catalogs__catalog_items__asynchronous__delete_catalog_items_bulk
title: "Delete multiple catalog items"
description: "This article outlines details about the Delete multiple catalog items Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Delete multiple catalog items

delete

/catalogs/{catalog_name}/items

Use this endpoint to delete multiple items in your catalog.

Each request can support up to 50 items. This endpoint is asynchronous.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the catalogs.delete_items permission.

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
 An array that contains item objects. The item objects should contain an id referencing the items Braze should delete. Up to 50 item objects are allowed per request. | 

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

```
 | 
```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
 {"id": "restaurant1"},
 {"id": "restaurant2"},
 {"id": "restaurant3"}
 ]
}'

```
 | 

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

```
 | 
```
{
 "errors": [
 {
 "id": "items-missing-ids",
 "message": "There are 1 item(s) that do not have ids",
 "parameters": [],
 "parameter_values": []
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

 ids-not-unique | 
 Check that the item IDs are unique in the request. | 

 ids-not-strings | 
 Item IDs must be of type string. | 

 items-missing-ids | 
 Some items don’t have item IDs. Check that each item has an item ID. | 

 invalid-ids | 
 Item IDs can only include letters, numbers, hyphens, and underscores. | 

 request-includes-too-many-items | 
 Your request has too many items. The item limit per request is 50. | 

- 

New Stuff!
