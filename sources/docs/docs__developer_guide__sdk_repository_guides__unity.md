---
url: https://www.braze.com/docs/developer_guide/sdk_repository_guides/unity
slug: docs__developer_guide__sdk_repository_guides__unity
title: "Unity SDK repository guide"
description: "Braze Unity SDK README reference mirrored from GitHub."
section: developer_guide/sdk_repository_guides
fetched: 2026-09-02
evidence: company-own (technical)
---
# Unity SDK repository guide

## About the Braze Unity SDK

The Braze Unity SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- Braze User Guide
 
- Braze Developer Guide

## Plugin setup

Before you can start using Braze in Unity scripts, you’ll need to import the plugin files to your Unity project.

Recommended: The Android and iOS plugins are bundled as a Unity package available for download from the SDK release page.

Manual Plugin Setup: Alternatively, you can copy the plugins into your Unity project:

- First, clone this repo.
 
- If you’re not using any other plugins, all you have to do is copy the Plugins directory from this repo into the Assets folder of your Unity project.
 
- If you already have a /<your-project>/Assets/Plugins directory (probably because you’re using another plugin already), copy Plugins/Appboy/AppboyBinding.cs into /<your-project>/Assets/Plugins. Then copy the contents of Plugins/iOS and Plugins/Android from this repo into /<your-project>/Assets/Plugins/iOS and /<your-project>/Assets/Plugins/Android respectively.

## Integration Setup

To integrate Braze into your Unity application, complete the instructions in Integrating the Braze Unity SDK.

## Contact

For questions, contact Braze Technical Support for assistance.

For repository details and sample projects, see https://github.com/braze-inc/braze-unity-sdk.

- 

New Stuff!
