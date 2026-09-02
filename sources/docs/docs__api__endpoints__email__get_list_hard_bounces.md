---
url: https://www.braze.com/docs/api/endpoints/email/get_list_hard_bounces
slug: docs__api__endpoints__email__get_list_hard_bounces
title: "Query hard bounced emails"
description: "This article outlines the details about the Query or list hard bounced email addresses Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Query hard bounced emails

get

/email/hard_bounces

Use this endpoint to pull a list of email addresses that have “hard bounced” your email messages within a certain time frame.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the email.hard_bounces permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 start_date | 
 Optional* | 
 String in YYYY-MM-DD format | 
 *One of start_date or email is required. This is the start date of the range to retrieve hard bounces and must be earlier than end_date. This is treated as midnight in UTC time by the API. | 

 end_date | 
 Required | 
 String in YYYY-MM-DD format | 
 End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. | 

 limit | 
 Optional | 
 Integer | 
 Optional field to limit the number of results returned. Defaults to 100, maximum is 500. | 

 offset | 
 Optional | 
 Integer | 
 Optional beginning point in the list to retrieve from. | 

 email | 
 Optional* | 
 String | 
 *One of start_date or email is required. If provided, we’ll return whether or not the user has hard bounced. Check that the email strings are formatted properly. | 

important

You must provide an end_date, and either an email or a start_date. If you provide all three, start_date, end_date, and an email, we prioritize the emails given and disregard the date range.

If your date range has more than the limit number of hard bounces, you will need to make multiple API calls, each time increasing the offset until a call returns either fewer than limit or zero results. Including offset and limit parameters with email can return an empty response.

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'

```
 | 

## Response

Entries are listed in descending order.

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

```
 | 
```
{
 "emails": [
 {
 "email": (string) an email that has hard bounced,
 "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
 },
 {
 "email": (string) an email that has hard bounced,
 "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
 },
 {
 "email": (string) an email that has hard bounced,
 "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
 }
 ],
 "message": "success"
}

```
 | 

- 

New Stuff!
