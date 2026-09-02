---
url: https://www.braze.com/docs/developer_guide/sdk_repository_guides/cordova
slug: docs__developer_guide__sdk_repository_guides__cordova
title: "Cordova SDK repository guide"
description: "Braze Cordova SDK README reference mirrored from GitHub."
section: developer_guide/sdk_repository_guides
fetched: 2026-09-02
evidence: company-own (technical)
---
# Cordova SDK repository guide

## About the Braze Cordova SDK

The Braze Cordova SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- Braze User Guide
 
- Braze Developer Guide

## Minimum version requirements

 Braze Plugin | 
 Cordova Android | 
 Cordova iOS | 

 10.0.0+ | 
 >= 13.0.0 | 
 >= 5.0.0 | 

 2.31.0+ | 
 >= 12.0.0 | 
 >= 5.0.0 | 

This SDK additionally inherits the requirements of its underlying Braze native SDKs. Be sure to also adhere to the linked Android and Swift SDK requirement lists:

- Android SDK requirements
 
- Swift SDK requirements

## Installing the SDK

warning

Only add the Braze Cordova SDK using the methods below. Do not attempt to install using other methods as it could lead to a security breach.

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
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch

```
 | 

## Running the sample application

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
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios

```
 | 

For repository details and sample projects, see https://github.com/braze-inc/braze-cordova-sdk.

- 

New Stuff!
