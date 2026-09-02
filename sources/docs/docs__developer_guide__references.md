---
url: https://www.braze.com/docs/developer_guide/references
slug: docs__developer_guide__references
title: "References, repositories, and sample apps"
description: "This is a list of reference documentation, GitHub repositories, and sample apps belonging to each Braze SDK."
section: developer_guide/references
fetched: 2026-09-02
evidence: company-own (technical)
---
# References, repositories, and sample apps

This is a list of reference documentation, GitHub repositories, and sample apps belonging to each Braze SDK. An SDK’s reference documentation details its available classes, types, functions, and variables. While the GitHub repository provides insight into that SDK’s function and attribute declarations, code changes, and versioning. Each repository also includes fully-buildable sample applications you can use to test Braze features or implement alongside your own applications.

For mirrored repository README content in docs, see Repository guides.

## List of resources

note

Currently, some SDKs do not have dedicated reference documentation—but we’re actively working on it.

 Platform | 
 Reference | 
 Repository | 
 Sample app | 

 Android SDK | 
 Reference documentation | 
 GitHub repository | 
 Sample app | 

 Swift SDK | 
 Reference documentation | 
 GitHub repository | 
 Sample app | 

 Web SDK | 
 Reference documentation | 
 GitHub repository | 
 Sample app | 

 Javascript SDK | 
 Reference documentation | 
 GitHub repository | 
 N/A | 

 Cordova SDK | 
 Declaration file | 
 GitHub repository | 
 Sample app | 

 Flutter SDK | 
 Reference documentation | 
 GitHub repository | 
 Sample app | 

 React Native SDK | 
 Reference documentation | 
 GitHub repository | 
 Sample app | 

 Vega SDK | 
 Reference documentation | 
 GitHub repository | 
 N/A | 

 Roku SDK | 
 N/A | 
 GitHub repository | 
 Sample app | 

 Unity SDK | 
 Declaration file | 
 GitHub repository | 
 Sample app | 

 .NET MAUI SDK (formerly Xamarin) | 
 N/A | 
 GitHub repository | 
 Sample app | 

## Building a sample app

- android
 
- swift

### Building “Droidboy”

Our test application within the Android SDK GitHub repository is called Droidboy. Follow these instructions to build a fully functional copy of it alongside your project.

- Create a new workspace and note the Braze API identifier key.

- Copy your FCM sender ID and Braze API identifier key into the appropriate places within /droidboy/res/values/braze.xml (in between the tags for the strings named com_braze_push_fcm_sender_id and com_braze_api_key, respectively).

- Copy your FCM server key and server ID into your workspace settings under Manage Settings.

- To assemble the Droidboy APK, run ./gradlew assemble within the SDK directory. Use gradlew.bat on Windows.

- To automatically install the Droidboy APK on a test device, run ./gradlew installDebug within the SDK directory:

### Building “Hello Braze”

The Hello Braze test application shows a minimal use case of the Braze SDK and additionally shows how to easily integrate the Braze SDK into a Gradle project.

- Copy your API identifier key from the Manage Settings page into your braze.xml file in the res/values folder.

- To install the sample app to a device or emulator, run the following command within the SDK directory:

```

1

```
 | 
```
./gradlew installDebug

```
 | 
 
If you don’t have your ANDROID_HOME variable properly set or don’t have a local.properties folder with a valid sdk.dir folder, this plugin will also install the base SDK for you. See the plugin repository for more information.

For more information on the Android SDK build system, see the GitHub Repository README.

### Building Swift test apps

Follow these instructions to build and run our test applications.

- Create a new workspace and note the app identifier API key and endpoint.
 
- Based on your integration method (Swift Package Manager, CocoaPods, Manual), select the appropriate xcodeproj file to open.
 
- Place your API key and your endpoint within the appropriate field in the Credentials file.

note

While performing QA on your SDK integration, use the SDK Debugger to get troubleshoot issues without turning on verbose logging for your app.

- 

New Stuff!
