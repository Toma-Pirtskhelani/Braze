---
url: https://www.braze.com/docs/api/endpoints/export/purchases/get_list_product_id
slug: docs__api__endpoints__export__purchases__get_list_product_id
title: "Export product IDs"
description: "This article outlines details about the Export product IDs Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export product IDs

get

/purchases/product_list

Use this endpoint to return a paginated lists of product IDs.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the purchases.product_list permission.

## Rate limit

We apply a shared rate limit of 1,000 requests per hour to this endpoint. This rate limit is shared with the /custom_attributes, /events, and /events/list endpoints, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 page | 
 Optional | 
 String | 
 The page of your product list that you want to view. | 

## Example request

```

1

```
 | 
```
https://rest.iad-01.braze.com/purchases/product_list?page=1

```
 | 

## Response

```

1
2
3
4
5
6

```
 | 
```
{
 "products": [
 "product_name" (string), the name of the product
 ],
 "message": (string) returns 'success' when the request completes without errors
}

```
 | 

tip

For help with CSV and API exports, visit Export troubleshooting.

- 

New Stuff!
