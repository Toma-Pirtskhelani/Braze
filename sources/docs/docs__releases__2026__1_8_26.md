---
url: https://www.braze.com/docs/releases/2026/1_8_26
slug: docs__releases__2026__1_8_26
title: "January 8, 2026 release"
description: "This article contains release notes for 1/8/2026."
section: releases/2026
fetched: 2026-09-02
evidence: company-own (technical)
---
# January 8, 2026 release

## Data & Reporting

### Updates to Currents events

 General availability

The following changes were made to Currents in Version 4:

- Field changes to event type users.behaviors.pushnotification.TokenStateChange:

- Added new string field push_token: Push token of the event

- Field changes to event type users.messages.pushnotification.Bounce:

- Added new string field push_token: Push token of the event

- Field changes to event type users.messages.pushnotification.Send:

- Added new string field push_token: Push token of the event

- Field changes to event type users.messages.rcs.Click:

- Added new string field canvas_variation_name: Name of the Canvas variation this user received
 
- Field user_phone_number is now optional.

- Field changes to event type users.messages.rcs.InboundReceive:

- Field user_id is now optional.

- Field changes to event type users.messages.rcs.Rejection:

- Added new string field canvas_step_message_variation_id: API ID of the Canvas step message variation this user received

Refer to the Currents changelog for the event changes for each release.

### Export sync logs by all rows

 Early access

In the Cloud Data Ingestion Sync Log dashboard, you can choose to export the row-level logs for a sync run by:

- Rows with errors: Downloads a file containing only the rows that had an Error status.
 
- All rows: Downloads a file containing every row processed in the run.

## Channels & Touchpoints

### Bring Your Own (BYO) WhatsApp connector

The Bring Your Own (BYO) WhatsApp connector offers a partnership between Braze and Infobip, in which you give Braze access to your Infobip WhatsApp Business Manager (WABA). This allows you to manage and pay for messaging costs directly with Infobip while using Braze for segmentation, personalization, and campaign orchestration.

### Banners in Canvas

 Early access

You can select Banners as a messaging channel in a Message step for Canvas. You can use the drag-and-drop editor to create personalized inline messages, providing non-intrusive, contextually relevant experiences that update automatically at the start of each user session.

### Dynamic BCC

 General availability

With dynamic BCC, you can use Liquid in your BCC address. Note that this feature is only available in Email Preferences and can’t be set on the campaign itself. Only one BCC address per email recipient is allowed.

### Channel-based rate limits

As an alternative to a rate limit that gets shared across an entire multi-channel campaign or Canvas, you can select a specific rate limit per channel. In this case, the rate limit will apply to each of your selected channels. For example, you can set your campaign or Canvas to send a maximum of 5,000 webhooks and 2,500 SMS messages per minute across the campaign or Canvas. For more details, see Rate limiting and frequency capping.

## Partnerships

### LILT - Localization

LILT is the complete AI solution for enterprise translation and content creation. LILT enables global organizations to scale and optimize their content, product, communications, and support operations, with AI agents and fully automated workflows.

## SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Android 40.1.1
 
- Android SDK 40.1.0
 
- Swift SDK 14.0.0

- Removes News Feed.

- This fully removes all UI elements, data models, and actions associated with News Feed.

- Web SDK 6.4.0

- 

New Stuff!
