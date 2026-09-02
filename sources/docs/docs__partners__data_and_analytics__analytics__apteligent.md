---
url: https://www.braze.com/docs/partners/data_and_analytics/analytics/apteligent
slug: docs__partners__data_and_analytics__analytics__apteligent
title: "Apteligent"
description: "This reference article outlines the partnership between Braze and Apteligent, a mobile application that details crash reporting, allowing you to log critical data into your..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Apteligent

Apteligent is a mobile application performance platform providing tools and insights for developers and product managers.

This integration is maintained by Apteligent.

## About the integration

The Braze and Apteligent integration provides detailed iOS crash reporting, allowing you to log critical data into your existing Braze solution as well as segment, understand, and engage with users who have experienced application crashes.

## Prerequisites

 Requirement | 
 Description | 

 TestDrive account | 
 A TestDrive account is required to take advantage of this partnership. | 

warning

This integration is currently only supported on iOS.

## Integration

### Step 1: Register an observer

First, you must register an observer. Ensure that this is done before you initialize Apteligent.

```

1
2
3
4

```
 | 
```
[[NSNotificationCenter defaultCenter] addObserver:self
 selector:@selector(crashDidOccur:)
 name:@"CRCrashNotification"
 object:nil];

```
 | 

### Step 2: Log custom crash analytics

The Apteligent SDK will fire a notification when the user loads the application after a crash occurs. The notification will contain the crash name, reason, and date of occurrence.

Upon receiving the notification, log a custom crash event and update user attributes with Apteligent’s crash reporting analytics:

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
- (void)crashDidOccur:(NSNotification*)notification {
 NSDictionary *crashInfo = notification.userInfo;
 [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
 [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
 [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
 [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}

```
 | 

Once completed, you’ll be able to harness the power of Braze segmentation and engagement analytics using the crash information found in the Apteligent platform.

- 

New Stuff!
