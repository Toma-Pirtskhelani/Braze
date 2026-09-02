---
url: https://www.braze.com/docs/api/objects_filters/messaging/webhook_object
slug: docs__api__objects_filters__messaging__webhook_object
title: "Webhook object"
description: "This reference article outlines the Braze webhook object."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# Webhook object

The webhook object allows you to modify or create webhook messages via our messaging endpoints.

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
{
 "url": (required, string),
 "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
 "request_headers": (optional, Hash) key-value pairs to use as request headers,
 "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
 "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}

```
 | 

As a best practice, Braze recommends providing an explicit value for Content-Type in the request_headers field for consistent and predictable behavior, as senders and servers may change over time. If you don’t specify a value for the Content-Type header, the system infers a value from the request body.

- 

New Stuff!
