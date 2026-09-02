---
url: https://www.braze.com/docs/api/endpoints/user_data/post_user_track_bulk
slug: docs__api__endpoints__user_data__post_user_track_bulk
title: "Create and update users (bulk)"
description: "This article outlines details about the bulk Track users endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create and update users (bulk)

post

/users/track/bulk

core endpoint

Use this endpoint to record custom events and purchases and update user profile attributes in bulk.

important

This endpoint is currently in limited beta. Although we’re not adding new customers to the beta right now, let your Braze account manager know if you think this feature could be useful for your Braze integration.

## When to use this endpoint

Like the /users/track endpoint, you can use this endpoint to update user profiles. This endpoint is better suited for bulk updates:

- Larger requests: Send up to 1,000 users per request, so you can make fewer requests for large backfills and syncs.
 
- Prioritization: During peak traffic conditions, requests to /users/track are prioritized over requests to /users/track/bulk.

Use this endpoint when you’re backfilling many user profiles during onboarding, or syncing large volumes of profiles as part of a daily sync.

note

The /users/track endpoint request object limits vary by pricing model and configuration. Use /users/track/bulk for bulk ingestion.

## Prerequisites

To use this endpoint, you must have an API key with the users.track.bulk permission.

If you’re making server-to-server calls behind a firewall, you may need to allowlist your Braze REST endpoint (for example, rest.iad-01.braze.com). For more information, see API endpoints.

## Rate limit

note

Each custom attribute sent in a request to /users/track/bulk consumes a data point. For more information, see Data points.

For most customers, this endpoint has a base speed limit of 50 requests per second.

Customers on newer contracts may instead have burst (per-second) and steady (per-hour) limits based on contracted monthly active users.

Each /users/track/bulk request has a payload limit of 2 MB and can include up to 1,000 objects total across attributes, events, and purchases, depending on your account’s bulk rate-limit policy.

Each object can update one user, so a single request can update up to your account’s request object limit of different users. Additionally, each request can contain a maximum of 100 objects per user profile across attributes, events, and purchases.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY

```
 | 

```

1
2
3
4
5

```
 | 
```
{
 "attributes": (optional, array of attributes object),
 "events": (optional, array of event object),
 "purchases": (optional, array of purchase object)
}

```
 | 

### Request parameters

important

For each request object, you must include one of external_id, user_alias, braze_id, email, or phone.

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 attributes | 
 Optional | 
 Array of attributes objects | 
 See user attributes object | 

 events | 
 Optional | 
 Array of event objects | 
 See events object | 

 purchases | 
 Optional | 
 Array of purchase objects | 
 See purchases object | 

## Example requests

### Bulk update user profiles in one request

Update up to your account’s request object limit of user profiles in one request.

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
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "attributes": [
 {
 "external_id": "user1",
 "string_attribute": "fruit",
 "boolean_attribute_1": true,
 "integer_attribute": 25,
 "array_attribute": [
 "banana",
 "apple"
 ]
 },
 {
 "external_id": "user2",
 "string_attribute": "vegetables",
 "boolean_attribute_1": false,
 "integer_attribute": 25,
 "array_attribute": [
 "broccoli",
 "asparagus"
 ]
 }
 ]
}'

```
 | 

### Send attributes and events in one request

Include attributes and events in the same request, up to your account’s total object limit.

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "attributes": [
 {
 "external_id": "user1",
 "string_attribute": "fruit",
 "boolean_attribute_1": true,
 "integer_attribute": 25,
 "array_attribute": [
 "banana",
 "apple"
 ]
 }
 ],
 "events": [
 {
 "external_id": "user2",
 "app_id": "your_app_identifier",
 "name": "rented_movie",
 "time": "2022-12-06T19:20:45+01:00",
 "properties": {
 "release": {
 "studio": "FilmStudio",
 "year": "2022"
 },
 "cast": [
 {
 "name": "Actor1"
 },
 {
 "name": "Actor2"
 }
 ]
 }
 }
 ]
}'

```
 | 

## Responses

### Successful message

Successful messages return the following response:

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
 "message": "success",
 "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
 "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
 "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}

```
 | 

### Successful message with non-fatal errors

If your request is successful but has non-fatal errors (for example, one invalid event object in a large batch), you receive the following response:

```

1
2
3
4
5
6
7
8

```
 | 
```
{
 "message": "success",
 "errors": [
 {
 <minor error message>
 }
 ]
}

```
 | 

### Message with fatal errors

If your request has a fatal error, you receive the following response:

```

1
2
3
4
5
6
7
8

```
 | 
```
{
 "message": <fatal error message>,
 "errors": [
 {
 <fatal error message>
 }
 ]
}

```
 | 

### Fatal error response codes

For status codes and associated error messages that Braze returns when your request has a fatal error, see Fatal errors & responses.

If you receive the error “provided external_id is blacklisted and disallowed”, your request may include a “dummy user.” For more information, see Spam blocking.

## Frequently asked questions

### Should I use this endpoint or /users/track?

Use both endpoints based on your use case:

- For large backfills and syncs, use /users/track/bulk.
 
- For real-time use cases, use /users/track.

### What identifiers can I use in /users/track/bulk?

For each request object, include one of external_id, braze_id, user_alias, email, or phone.

### Can I include attributes, events, and purchases in one request?

Yes. Include any mix of attributes, events, and purchases, up to your account’s combined request object limit.

- 

New Stuff!
