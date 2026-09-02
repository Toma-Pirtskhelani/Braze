---
url: https://www.braze.com/docs/developer_guide/network
slug: docs__developer_guide__network
title: "Network settings"
description: "Learn how to configure network settings for the Braze SDK."
section: developer_guide/network
fetched: 2026-09-02
evidence: company-own (technical)
---
# Network settings

Learn how to configure network settings for the Braze SDK.

- android
 
- swift

## Network offline mode

Network offline mode is an optional feature that pauses or resumes outbound network requests from the Braze SDK at any point during runtime. Events are not lost during the offline state. This reference article covers how to integrate this mode.

To enable network offline mode in the Braze SDK, see the following example:

- java
 
- kotlin

```

1

```
 | 
```
Braze.setOutboundNetworkRequestsOffline(true);

```
 | 

```

1

```
 | 
```
Braze.setOutboundNetworkRequestsOffline(true)

```
 | 

## Network traffic control

### Requesting processing policies

Braze allows the user the option to control network traffic using the following protocols:

- automatic
 
- manual

By default, the RequestPolicy enum value is set to automatic. When set, immediate server requests are performed when user-facing data is required for Braze features, such as in-app messages.

The Braze SDK will automatically handle all server communication, including:

- Flushing custom events and attributes data to Braze servers
 
- Updating Content Cards and geofences
 
- Requesting new in-app messages

To minimize server load, Braze performs periodic flushes of new user data every few seconds.

When the RequestPolicy enum value is manual, it performs the same as automatic request processing, except:

- Custom attributes and custom event data are not automatically flushed to the server throughout the user session.
 
- Braze will still perform automatic network requests for internal features, such as requesting in-app messages, Liquid templating in in-app messages, geofences, and location tracking. For more details, see the Braze.Configuration.Api.RequestPolicy.manual documentation. When these internal requests are made, Braze may flush locally stored custom attributes and custom event data to the Braze server, depending on the request type.

### Manually flushing user data

Data can be manually flushed to Braze servers at any time using the following method:

- swift
 
- objective-c

```

1

```
 | 
```
AppDelegate.braze?.requestImmediateDataFlush()

```
 | 

```

1

```
 | 
```
[AppDelegate.braze requestImmediateDataFlush];

```
 | 

### Setting the request processing policy

These policies can be set at app startup time when you initialize the Braze configuration. In the configuration object, set the Braze.Configuration.Api.RequestPolicy) as shown in the following code snippet:

- swift
 
- objective-c

```

1

```
 | 
```
configuration.api.requestPolicy = .automatic

```
 | 

```

1

```
 | 
```
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;

```
 | 

- 

New Stuff!
