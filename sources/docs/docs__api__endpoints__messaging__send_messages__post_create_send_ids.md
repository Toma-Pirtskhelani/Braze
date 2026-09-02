---
url: https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_create_send_ids
slug: docs__api__endpoints__messaging__send_messages__post_create_send_ids
title: "Create send IDs"
description: "This article outlines details about the Create send IDs Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create send IDs

post

/sends/id/create

Use this endpoint to create send IDs that can be used to send messages and track message performance programmatically, without campaign creation for each send.

Using the send identifier to track and send messages is useful if you are planning to programmatically generate and send content.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need to generate an API key with the sends.id.create permission.

## Rate limit

You can create up to 100 custom send identifiers per day using this endpoint for a given workspace. Each send_id and campaign_id combination that you create will count toward your daily limit. The response headers for any valid request include the current rate limit status. See API rate limits for details.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY

```
 | 

```

1
2
3
4

```
 | 
```
{
 "campaign_id": (required, string) see campaign identifier,
 "send_id": (optional, string) see send identifier
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 campaign_id | 
 Required | 
 String | 
 See campaign identifier. | 

 send_id | 
 Optional | 
 String | 
 See send identifier. | 

## Example request

```

1
2
3
4
5
6
7

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "campaign_id": "campaign_identifier",
 "send_id": "send_identifier"
}'

```
 | 

## Response

### Example success response

```

1
2
3
4

```
 | 
```
{
 "message": "success",
 "send_id" : (string) the send identifier
}

```
 | 

- 

New Stuff!
