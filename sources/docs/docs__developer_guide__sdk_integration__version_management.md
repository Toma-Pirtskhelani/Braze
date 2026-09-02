---
url: https://www.braze.com/docs/developer_guide/sdk_integration/version_management
slug: docs__developer_guide__sdk_integration__version_management
title: "About version management"
description: "Learn about version management for the Braze SDK."
section: developer_guide/sdk_integration
fetched: 2026-09-02
evidence: company-own (technical)
---
# About version management

Learn about version management for the Braze SDK, so your app can stay up to date with the latest features and quality improvements. Because older versions of the SDK may not receive the latest patch, bugfix, or support, we recommend always keeping it up to date as a part of your ongoing development lifecycle.

## Versioning recommendations

All Braze SDKs adhere to the Semantic Versioning Specification (SemVer), so given a version number MAJOR.MINOR.PATCH, we recommend the following:

 Version | 
 About this Version | 
 Recommendation | 

 PATCH | 
 Updates are always non-breaking, and include important bug fixes. They’ll always be safe. | 
 You should always try to update to the latest patch version of your current major and minor version immediately. | 

 MINOR | 
 Updates are always non-breaking, and include net new functionality. They’ll never require changes in your application code. | 
 While you don’t need to do this immediately, you should update to the latest minor version of your current major version as soon as possible. | 

 MAJOR | 
 Updates are breaking changes, and may require changes in your application code. | 
 Because this may require code changes, update to the latest major version in a timeframe that works best for your team. | 

note

Sometimes new Android or Apple OS updates require changes to the Braze SDK. To help keep your app compatible with newer phones, it’s important you keep your SDK up to date.

## Getting notified of new releases

To receive automatic notifications when a new SDK version is released, you can watch the GitHub repository for any Braze SDK:

- Go to the SDK’s GitHub repository (for example, braze-android-sdk, braze-swift-sdk, or braze-web-sdk).
 
- Click Watch at the top of the page.
 
- Click Custom, then select Releases, and click Apply.

You receive a GitHub notification (and an email, depending on your notification settings) each time a new release is published. For the full list of SDK repositories, see References, Repositories, and Sample Apps.

## About known issues

To ensure our changes won’t break your build pipelines, we will never alter or remove a release after it’s been published to a distribution system—even if that particular release has known issues.

In these cases, we’ll document the issue to the Braze SDK changelog, then release a new patch for the impacted major or minor versions as soon as possible.

- 

New Stuff!
