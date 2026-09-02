---
url: https://www.braze.com/docs/api/endpoints/cdi/get_job_sync_status
slug: docs__api__endpoints__cdi__get_job_sync_status
title: "List job sync status"
description: "This article outlines details about the List job sync status Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# List job sync status

get

/cdi/integrations/{integration_id}/job_sync_status

Use this endpoint to return a list of past sync statuses for a given integration.

note

To use this endpoint, you’ll need to generate an API key with the cdi.integration_job_status permission.

## Rate limit

This endpoint has a rate limit of 100 requests per minute.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 integration_id | 
 Required | 
 String | 
 Integration ID. | 

## Query parameters

Each call to this endpoint will return 10 items. For an integration with more than 10 syncs, use the Link header to retrieve the data on the next page as shown in the following example response.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 cursor | 
 Optional | 
 String | 
 Determines the pagination of the sync status. | 

## Example request

### Without cursor

```

1
2
3

```
 | 
```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
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
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

### Example success response

The status code 200 could return the following response body.

note

The Link header won’t exist if there are less than or equal to 10 syncs in total. For calls without a cursor, prev will not show. When looking at the last page of items, next will not show.

```

1

```
 | 
```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"

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

```
 | 
```
{
 "results": [
 {
 "job_status": (string) status of the sync, see below for explanation of different statuses,
 "sync_start_time": (string) time the sync started in ISO 8601,
 "sync_finish_time": (string) time the sync finished in ISO 8601,
 "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
 "rows_synced": (integer) number of rows successfully synced to Braze,
 "rows_failed_with_errors": (integer) number of rows failed because of errors
 }
 ],
 "message": "success"
}

```
 | 

 job_status | 
 Explanation | 

 running | 
 The job is currently running. | 

 success | 
 All rows synced successfully. | 

 partial | 
 Some rows failed to sync due to errors. | 

 error | 
 No rows were synced. | 

 config_error | 
 There was an error in integration configuration. Check your integration setup. | 

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

 Error | 
 Troubleshooting | 

 400 Invalid cursor | 
 Check that your cursor is valid. | 

 400 Invalid integration ID | 
 Check that your integration_id is valid. | 

For additional status codes and associated error messages, please refer to Fatal errors & responses.

- 

New Stuff!
