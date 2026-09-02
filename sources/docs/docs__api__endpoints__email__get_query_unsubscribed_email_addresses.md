---
url: https://www.braze.com/docs/api/endpoints/email/get_query_unsubscribed_email_addresses
slug: docs__api__endpoints__email__get_query_unsubscribed_email_addresses
title: "Query list of unsubscribed email addresses"
description: "This article outlines the details about the Retrieve list of or query email unsubscribes Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Query list of unsubscribed email addresses

get

/email/unsubscribes

Use this endpoint to return the latest emails that have unsubscribed during the time period from start_date to end_date. For a full subscription state history, use Currents to track this data.

You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the email.unsubscribe permission.

## Rate limit

We apply the default Braze rate limit of 250,000 requests per hour to this endpoint, as documented in API rate limits.

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 start_date | 
 Optional 
(see note) | 
 String in YYYY-MM-DD format | 
 Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. | 

 end_date | 
 Optional 
(see note) | 
 String in YYYY-MM-DD format | 
 End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. | 

 limit | 
 Optional | 
 Integer | 
 Optional field to limit the number of results returned. Defaults to 100, maximum is 500. | 

 offset | 
 Optional | 
 Integer | 
 Optional beginning point in the list to retrieve from. | 

 sort_direction | 
 Optional | 
 String | 
 Pass in the value asc to sort unsubscribes from oldest to newest. Pass in desc to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest. | 

 email | 
 Optional 
(see note) | 
 String | 
 If provided, we will return whether or not the user has unsubscribed. | 

note

You must provide an end_date, as well as either an email or a start_date.

If your date range has more than limit number of unsubscribes, you will need to make multiple API calls, each time increasing the offset until a call returns either fewer than limit or zero results.

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&[email protected]' \
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
 "email": (string) an email that has been unsubscribed,
 "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
 },
 {
 "email": (string) an email that has been unsubscribed,
 "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
 },
 {
 "email": (string) an email that has been unsubscribed,
 "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
 }
 ],
 "message": "success"
}

```
 | 

- 

New Stuff!
