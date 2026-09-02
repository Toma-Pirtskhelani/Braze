---
url: https://www.braze.com/docs/api/endpoints/cdi/get_integration_list
slug: docs__api__endpoints__cdi__get_integration_list
title: "List integrations"
description: "This article outlines details about the List integrations Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List integrations

get

/cdi/integrations

Use this endpoint to return a list of existing integrations.

note

To use this endpoint, you’ll need to generate an API key with the cdi.integration_list permission.

## Rate limit

This endpoint has a rate limit of 50 requests per minute.

## Query parameters

Each call to this endpoint will return 10 items. For a list with more than 10 integrations, use the Link header to retrieve the data on the next page as shown in the example response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 cursor | 
 Optional | 
 String | 
 Determines the pagination of the integration list. | 

## Example request

### Without cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
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
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

### Example success response

The status code 200 could return the following response body.

note

The Link header won’t exist if there are less than or equal to 10 integrations in total. For calls without a cursor, prev will not show. When looking at the last page of items, next will not show.

```

1

```
 | 
```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"

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

```
 | 
```
{
 "results": [
 {
 "integration_id": (string) integration ID,
 "app_group_id": (string) app group ID,
 "integration_name": (string) integration name,
 "integration_type": (string) integration type,
 "integration_status": (string) integration status,
 "contact_emails": (string) contact email(s),
 "last_updated_at": (string) last timestamp that was synced in ISO 8601,
 "warehouse_type": (string) data warehouse type,
 "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
 "last_job_status": (string) status of the last sync run,
 "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601
 }
 ],
 "message": "success"
}

```
 | 

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

 Error | 
 Troubleshooting | 

 400 Invalid cursor | 
 Check that your cursor is valid. | 

For additional status codes and associated error messages, refer to Fatal errors & responses.

- 

New Stuff!
