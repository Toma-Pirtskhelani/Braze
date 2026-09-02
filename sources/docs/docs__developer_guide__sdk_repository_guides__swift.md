---
url: https://www.braze.com/docs/developer_guide/sdk_repository_guides/swift
slug: docs__developer_guide__sdk_repository_guides__swift
title: "Swift SDK repository guide"
description: "Braze Swift SDK README reference mirrored from GitHub."
section: developer_guide/sdk_repository_guides
fetched: 2026-09-02
evidence: company-own (technical)
---
# Swift SDK repository guide

## About the Braze Swift SDK

The Braze Swift SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- Braze User Guide
 
- Braze Developer Guide

## Quickstart

The following snippets show the minimum configuration required to add the Braze Swift SDK to your app.

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

```
 | 
```
// AppDelegate.swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
 // ...
 static var braze: Braze? = nil

 // ...
 func application(
 _ application: UIApplication, 
 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
 ) -> Bool {
 // ...
 let configuration = Braze.Configuration(
 apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
 endpoint: "YOUR-BRAZE-ENDPOINT"
 )
 let braze = Braze(configuration: configuration)

 AppDelegate.braze = braze
 // ...
 }
}

```
 | 

```

1

```
 | 
```
AppDelegate.braze?.changeUser(userId: "Jane Doe")

```
 | 

For more information about advanced integration options, see the Braze Developer Guide.

## Version support

The following table lists the minimum supported versions for tools used by the Braze Swift SDK.

 Tool | 
 Minimum supported version | 

 iOS | 
 12.0+ | 

 Mac Catalyst | 
 16.0+ | 

 tvOS | 
 12.0+ | 

 visionOS | 
 1.0+ | 

 Xcode | 
 26.0+ (17A324) | 

## Package Managers

- Swift Package Manager
 
- CocoaPods

## Libraries

The following table describes each library in the Braze Swift SDK.

   | 
 iOS | 
 tvOS | 
 macCatalyst | 
 visionOS | 

 BrazeKit
 Main SDK library providing support for analytics and push notifications. | 
 ✅ | 
 ✅1 | 
 ✅ | 
 ✅ | 

 BrazeUI
 Braze-provided user interface library for In-App Messages and Content Cards. | 
 ✅ | 
 n/a | 
 ✅ | 
 ✅ | 

 BrazeLocation
 Location library providing support for location analytics and geofence monitoring. | 
 ✅ | 
 ✅2 | 
 ✅ | 
 ✅2 | 

 BrazeNotificationService
 Notification service extension library providing support for rich push notifications. | 
 ✅ | 
 n/a | 
 ✅ | 
 ✅ | 

 BrazePushStory
 Notification content extension library providing support for Push Stories. | 
 ✅ | 
 n/a | 
 ✅ | 
 ✅ | 

1 Push notifications not supported on tvOS

2 Geofence monitoring not supported on tvOS and visionOS

## Examples

Explore our examples project, which showcases sample integrations for multiple features.

## Alternative Repositories

 Variant | 
 Repository | 
 GH Issues, SDK info | 

 → Sources and Static XCFrameworks | 
 braze-inc/braze-swift-sdk | 
 ✓ | 

 Static XCFrameworks | 
 braze-inc/braze-swift-sdk-prebuilt-static | 
 ✗ | 

 Dynamic XCFrameworks | 
 braze-inc/braze-swift-sdk-prebuilt-dynamic | 
 ✗ | 

 Mergeable XCFrameworks | 
 braze-inc/braze-swift-sdk-prebuilt-mergeable | 
 ✗ | 

## Contact

For questions, contact Braze Technical Support for assistance.

For repository details and sample projects, see https://github.com/braze-inc/braze-swift-sdk.

- 

New Stuff!
