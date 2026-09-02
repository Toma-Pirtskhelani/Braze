---
url: https://www.braze.com/docs/api/endpoints/cdi/post_job_sync
slug: docs__api__endpoints__cdi__post_job_sync
title: "Trigger a sync"
description: "This article outlines details about the Trigger sync Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Trigger a sync

post

/cdi/integrations/{integration_id}/sync

Use this endpoint to trigger a sync for a given integration.

note

To use this endpoint, you must generate an API key with the cdi.integration_sync permission.

## Rate limit

This endpoint has a rate limit of 20 requests per minute.

## Path parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 integration_id | 
 Required | 
 String | 
 Integration ID. This is found in the URL when viewing an integration in the Braze dashboard. The URL format is https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]. | 

## Example request

```

1
2
3

```
 | 
```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'

```
 | 

## Response

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

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

 Error | 
 Troubleshooting | 

 400 Invalid integration ID | 
 Check that your integration_id is valid. | 

 404 Integration not found | 
 No integration exists for the given integration ID. Make sure that your integration ID is valid. | 

 429 Another job is in progress | 
 There is a sync currently running for this integration. Try again after the sync has completed. | 

For additional status codes and associated error messages, refer to Fatal errors & responses.

- 

New Stuff!
