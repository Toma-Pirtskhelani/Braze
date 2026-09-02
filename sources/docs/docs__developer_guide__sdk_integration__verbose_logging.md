---
url: https://www.braze.com/docs/developer_guide/sdk_integration/verbose_logging
slug: docs__developer_guide__sdk_integration__verbose_logging
title: "Verbose logging"
description: "Learn how to enable verbose logging for the Braze SDK, collect logs for troubleshooting, and share them with Braze Support."
section: developer_guide/sdk_integration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Verbose logging

Verbose logging outputs detailed, low-level information from the Braze SDK, giving you visibility into how the SDK initializes, communicates with servers, and processes messaging channels like push, in-app messages, and Content Cards.

When something isn’t working as expected—such as a push notification not arriving, an in-app message not displaying, or user data not syncing—verbose logs help you identify the root cause. Instead of guessing, you can see exactly what the SDK is doing at each step.

tip

If you want to debug without enabling verbose logging manually, you can use the SDK Debugger to create debugging sessions directly in the Braze dashboard.

## When to use verbose logging

Turn on verbose logging when you need to:

- Verify SDK initialization: Confirm the SDK starts correctly with the right API key and endpoint.
 
- Troubleshoot message delivery: Check whether push tokens are registered, in-app messages are triggered, or Content Cards are synced.
 
- Debug deep links: Verify the SDK receives and opens deep links from push, in-app messages, or Content Cards.
 
- Validate session tracking: Confirm sessions start and end as expected.
 
- Diagnose connectivity issues: Inspect the network requests and responses between the SDK and Braze servers.

## Enabling verbose logging

important

Verbose logs are intended for development and testing environments only. Disable verbose logging before releasing your app to production to prevent sensitive information from being exposed.

- android
 
- swift
 
- web
 
- unity
 
- react native

Enable verbose logging before any other SDK calls in your Application.onCreate() method to capture the most complete output.

In code:

- java
 
- kotlin

```

1

```
 | 
```
BrazeLogger.setLogLevel(Log.VERBOSE);

```
 | 

```

1

```
 | 
```
BrazeLogger.logLevel = Log.VERBOSE

```
 | 

In braze.xml:

```

1

```
 | 
```
<integer name="com_braze_logger_initial_log_level">2</integer>

```
 | 

To verify that verbose logging is enabled, search for V/Braze in your Logcat output. For example:

```

1

```
 | 
```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started

```
 | 

For full details, see Android SDK logging.

Set the log level to .debug on your Braze.Configuration object during initialization.

- swift
 
- objective-c

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
let configuration = Braze.Configuration(
 apiKey: "<BRAZE_API_KEY>",
 endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)

```
 | 

```

1
2
3
4

```
 | 
```
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
 endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];

```
 | 

The .debug level is the most verbose and is recommended for troubleshooting. For full details, see Swift SDK logging.

Add ?brazeLogging=true as a URL parameter, or enable logging during SDK initialization:

```

1
2
3
4

```
 | 
```
braze.initialize('YOUR-API-KEY', {
 baseUrl: 'YOUR-SDK-ENDPOINT',
 enableLogging: true
});

```
 | 

You can also toggle logging after initialization:

```

1

```
 | 
```
braze.toggleLogging();

```
 | 

Logs appear in the Console tab of your browser’s developer tools. For full details, see Web SDK logging.

- Open the Braze Configuration Settings by navigating to Braze > Braze Configuration.
 
- Select the Show Braze Android Settings dropdown.
 
- In the SDK Log Level field, enter 0.

Set the log level during SDK configuration:

```

1
2

```
 | 
```
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;

```
 | 

## Collecting logs

After you enable verbose logging, reproduce the issue you’re troubleshooting, then collect the logs from your platform’s console or debugging tool.

- android
 
- ios
 
- web

Use Logcat in Android Studio to capture logs:

- Connect your device or start an emulator.
 
- In Android Studio, open Logcat from the bottom panel.
 
- Filter by V/Braze or D/Braze to isolate Braze SDK output.
 
- Reproduce the issue.
 
- Copy the relevant logs and save them to a text file.

Use the Console app on macOS to capture logs:

- Install the app on your device with verbose logging enabled.
 
- Connect your device to your Mac.
 
- Open the Console app and select your device from the Devices sidebar.
 
- Filter logs by Braze or BrazeKit in the search bar.
 
- Reproduce the issue.
 
- Copy the relevant logs and save them to a text file.

Use your browser’s developer tools:

- Open your browser’s developer tools (usually F12 or Cmd+Option+I).
 
- Go to the Console tab.
 
- Reproduce the issue.
 
- Copy the console output and save it to a text file.

tip

When collecting logs for Braze Support, start logging before launching your app and continue until well after the issue occurs. This helps capture the full sequence of events.

## Reading verbose logs

Verbose logs follow a consistent structure that helps you trace what the SDK is doing. To learn how to interpret log output for specific channels, including what key entries to look for and common troubleshooting patterns, see Reading verbose logs.

## Sharing logs with Braze Support

When you contact Braze Support with an SDK issue, include the following:

- Verbose log file: A complete log capture from before app launch through the issue occurrence.
 
- Steps to reproduce: A clear description of the actions that trigger the issue.
 
- Expected vs. actual behavior: What you expected to happen and what happened instead.
 
- SDK version: The version of the Braze SDK you’re using.
 
- Platform and OS version: For example, iOS 18.0, Android 14, or Chrome 120.

- 

New Stuff!
