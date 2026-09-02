---
url: https://www.braze.com/docs/developer_guide/sdk_repository_guides/flutter
slug: docs__developer_guide__sdk_repository_guides__flutter
title: "Flutter SDK repository guide"
description: "Braze Flutter SDK README reference mirrored from GitHub."
section: developer_guide/sdk_repository_guides
fetched: 2026-09-02
evidence: company-own (technical)
---
# Flutter SDK repository guide

## About the Braze Flutter SDK

The Braze Flutter SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- Braze User Guide
 
- Braze Developer Guide

## Quickstart

The following snippets show the minimum configuration required to add the Braze Flutter SDK to your app.

```

1

```
 | 
```
flutter pub add braze_plugin

```
 | 

### Android

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
<!-- android/res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
 <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
 <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>

```
 | 

```

1
2
3

```
 | 
```
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

```
 | 

### iOS

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

```
 | 
```
// AppDelegate.swift
import BrazeKit
import braze_plugin

class AppDelegate: UIResponder, UIApplicationDelegate {
 static var braze: Braze? = nil

 func application(
 _ application: UIApplication,
 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
 ) -> Bool {
 // Setup Braze
 let configuration = Braze.Configuration(
 apiKey: "<BRAZE_API_KEY>",
 endpoint: "<BRAZE_ENDPOINT>"
 )
 // - Enable logging or customize configuration here
 configuration.logger.level = .info
 let braze = BrazePlugin.initBraze(configuration)
 AppDelegate.braze = braze

 return true
 }
}

```
 | 

### Dart

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
import 'package:braze_plugin/braze_plugin.dart';

// ...
_braze = new BrazePlugin();

// ...
_braze.changeUser("Jane Doe");

```
 | 

For more information about advanced integration options, see the Braze Developer Guide.

## Version support

The following table lists the minimum supported versions for tools used by the Braze Flutter SDK.

 Tool | 
 Minimum supported version | 

 Dart | 
 2.17.0+ | 

 Flutter (integration via CocoaPods) | 
 1.10.0+ | 

 Flutter (integration via CocoaPods or Swift Package Manager) | 
 3.24.0+ | 

 iOS Deployment Target | 
 12.0+ | 

This SDK also inherits requirements from the underlying Braze native SDKs. For more information, see braze-inc/braze-android-sdk and braze-inc/braze-swift-sdk.

## Sample App

The /example folder contains a sample app that illustrates how to integrate and use this package’s APIs.

## Contact

For questions, contact Braze Technical Support for assistance.

For repository details and sample projects, see https://github.com/braze-inc/braze-flutter-sdk.

- 

New Stuff!
