---
url: https://www.braze.com/docs/developer_guide/sdk_integration/debugging
slug: docs__developer_guide__sdk_integration__debugging
title: "Debugging the Braze SDK"
description: "Learn how to use the Braze SDK debugger, so you can troubleshoot issues for your SDK-powered channels, without enabling verbose logging in your."
section: developer_guide/sdk_integration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Debugging the Braze SDK

Learn how to use the Braze SDK’s built-in debugger, so you can troubleshoot issues for your SDK-powered channels, without needing to enable verbose logging in your app.

tip

For deeper investigation, you can also enable verbose logging to capture detailed SDK output and learn how to read verbose logs for specific channels.

## Prerequisites

To use the Braze SDK debugger, you’ll need the “View PII” and “View User Profiles (PII Redacted)” permissions. To download your debugging session logs, you’ll also need the “Export User Data” permission. Additionally, your Braze SDK needs to meet or point to the following minimum versions:

   Swift: 10.2.0+     Android: 32.1.0+  

To collect debugger logs when Braze.configuration.logger.level is .disabled, use Swift SDK 11.9.0 or later. For more information, see Swift changelogs.

## Debugging the Braze SDK

tip

To enable debugging for the Braze Web SDK, you can use a URL parameter.

### Step 1: Close your app

Before you start your debugging session, close the app that’s currently experiencing issues. You can relaunch the app at the start of your session.

### Step 2: Create a debugging session

In Braze, go to Settings, then under Setup and Testing, select SDK Debugger.

Select Create debugging session.

### Step 3: Select a user

Search for a user using their email address, external_id, user alias, or push token. When you’re ready to start your session, select Select User.

### Step 4: Relaunch the app

First, launch the app and confirm that your device is paired. If the pairing is successful, relaunch your app—this will ensure that app’s initialization logs are fully captured.

### Step 5: Complete the reproduction steps

After relaunching your app, follow the steps to reproduce the error.

tip

When you’re reproducing the error, be sure to follow the reproduction steps as closely as possible, so you can create quality logs.

### Step 6: End your session

When you’re finished with your reproduction steps, select End Session > Close.

note

It may take a few minutes to generate your logs depending on your session length and network connectivity.

### Step 7: Share or export your session (optional)

After your session, you can export your session logs as a CSV file. Additionally, others can use your Session ID to search for your debug session, so you don’t need to send them your logs directly.

- 

New Stuff!
