---
url: https://www.braze.com/docs/api/endpoints/sms/get_query_invalid_numbers
slug: docs__api__endpoints__sms__get_query_invalid_numbers
title: "Query invalid phone numbers"
description: "This article outlines details about Query invalid phone numbers Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Query invalid phone numbers

get

/sms/invalid_phone_numbers

Use this endpoint to pull a list of phone numbers that have been marked “invalid” within a certain time frame. See Invalid Phone Number Handling documentation for more information.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the sms.invalid_phone_numbers permission.

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
 Start date of the range to retrieve invalid phone numbers, must be earlier than end_date. This is treated as midnight in UTC time by the API. | 

 end_date | 
 Optional 
(see note) | 
 String in YYYY-MM-DD format | 
 End date of the range to retrieve invalid phone numbers. This is treated as midnight in UTC time by the API. | 

 limit | 
 Optional | 
 Integer | 
 Optional field to limit the number of results returned. Defaults to 100, maximum is 500. | 

 offset | 
 Optional | 
 Integer | 
 Optional beginning point in the list to retrieve from. | 

 phone_numbers | 
 Optional 
(see note) | 
 Array of Strings in e.164 format | 
 If provided, we will return the phone number if it has been found to be invalid. | 

 reason | 
 Optional 
(see note) | 
 String | 
 Available values are “provider_error” (provider error indicates phone cannot receive SMS) or “deactivated” (phone number has been deactivated). If omitted, all reasons are returned. | 

note

You must provide either a start_date and an end_date OR phone_numbers. If you provide all three, start_date, end_date, and phone_numbers, we prioritize the given phone numbers and disregard the date range.

If your date range has more than the limit number of invalid phone numbers, you will need to make multiple API calls with increasing the offset each time until a call returns either fewer than limit or zero results.

## Example request

```

1
2

```
 | 
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
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
18
19
20

```
 | 
```
{
 "sms": [
 {
 "phone": (string) phone number in e.164 format,
 "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
 "reason" : "provider_error"
 },
 {
 "phone": (string) phone number in e.164 format,
 "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
 "reason" : "deactivated"
 },
 {
 "phone": (string) phone number in e.164 format,
 "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
 "reason" : "provider_error"
 }
 ],
 "message": "success"
}

```
 | 

- 

New Stuff!
