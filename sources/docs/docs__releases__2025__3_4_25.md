---
url: https://www.braze.com/docs/releases/2025/3_4_25
slug: docs__releases__2025__3_4_25
title: "March 4, 2025 release"
description: "This article contains release notes for March 4, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# March 4, 2025 release

## Developer Guide detangle

Identical content that’s shared across multiple SDKs are starting to be merged together using the docs site’s new SDK tabbing feature. This month SDK integration, SDK initialization, and Content Cards were combined. Stay tuned for more updates in the coming months.

## Data flexibility

### Braze IDs for user profiles

A user profile now includes a Braze ID. You can use this when searching for user profiles.

### Deferrals

Braze has updated our definition for what is a soft bounce and is sending a new event called deferrals, which is when an email was not immediately delivered, but Braze will retry the email for up to 72 hours after this temporary delivery failure to maximize the chances of successful delivery before attempts for that specific campaign are stopped.

### Snowflake entity relationships

We’ve mapped the raw table schemas for Snowflake and Braze entity relationships to a new user-friendly docs page. It includes a breakdown of the USER_MESSAGES tables belonging to each channel, as well as descriptions for each table’s primary, foreign, and native keys.

### Identity management for external IDs

Using an email address or a hashed email address as your Braze external ID can simplify identity management across your data sources; however, it’s important to consider the potential risks to user privacy and data security.

## Unlocking creativity

### Liquid tutorials

Added three Liquid tutorials about how to use operators in the following scenarios.

 Liquid tutorials

 Choosing a message with an integer custom attribute. | 
 | 

 Choosing a message with a string custom attribute. | 
 | 

 Aborting a message based on location. | 
 | 

### Context steps for Canvas

 Early access

Use Context steps to create or update a set of variables that represent the context of a user (or insights into that user’s behavior) as they move through a Canvas.

### Personalized delay

 Early access

You can set up a personalized delay for your users by selecting the Personalize delay toggle in your Delay step. You can use this with a Context step to select a context variable to delay by.

When setting up a Delay step in your Canvas user journey, you can now create a delay up to 2 years.

### Reverting automatic synchronization

When composing an email message, you can revert to automatic synchronization in the Plaintext tab by selecting the Regenerate from HTML icon, which only appears if the plaintext isn’t synchronizing.

## Robust channels

### Android Live Updates

Although Live Updates won’t be officially available until 
Android 16, our Live Updates for Android page shows you how to emulate their behavior, so you can display interactive lock-screen notifications similar to Live Activities for the Swift Braze SDK. Unlike official Live Updates, this functionality can be implemented for older Android versions.

### Copying campaigns with feature flags across workspaces

You can now copy campaigns with feature flags across workspaces. To do so, make sure the destination workspace has a feature flag experiment configured with an ID that matches the feature flag referenced in the original campaign.

### New WhatsApp message types supported

WhatsApp messages now support video, audio, and document outbound messages. Contact your Braze account manager if you’re interested in participating in the early access.

### Right-to-left messages

Creating right-to-left messages covers best practices for crafting messages in languages that read right-to-left so that your messages display accurately as much as possible.

## AI and ML automation

### Item recommendations

Using item recommendations in messaging covers the product_recommendation Liquid object and includes a tutorial to help you put that knowledge into practice.

## New Braze partnerships

### Email Love - Channel Extensions

The Braze and Email Love partnership leverages Email Love’s Export to Braze feature and the Braze API to upload your email templates to Braze seamlessly.

### VWO - A/B Testing

The Braze and VWO integration allows you to leverage VWO experiment data to create targeted segments and deliver personalized campaigns.

## SDK updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- React Native

- Bumps React Native minimum requirement version to 0.71.0. For more information, refer to Releases Support Policy in the React Working Group.
 
- Bumps the minimum required iOS version to 12.0.
 
- Updates the native iOS version bindings from Braze Swift SDK 7.5.0 to 8.1.0.
 
- Updates the native Android version bindings from Braze Android SDK 29.0.1 to 30.1.1.

- 

New Stuff!
