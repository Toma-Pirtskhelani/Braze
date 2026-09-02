---
url: https://www.braze.com/docs/releases/2025/12_9_25
slug: docs__releases__2025__12_9_25
title: "December 9, 2025 release"
description: "This article contains release notes for December 9, 2025."
section: releases/2025
fetched: 2026-09-02
evidence: company-own (technical)
---
# December 9, 2025 release

## Data & Reporting

### Adding Google Tag Manager to a landing page

To add Google Tag Manager to your landing pages, add a Custom Code block to your landing page in the drag-and-drop editor, then insert the Tag Manager code into the block.

## Orchestration

### SMS Liquid use case

The Respond with different messages based on inbound SMS keyword use case incorporates dynamic SMS keyword processing to respond to specific inbound messages with different message copy. For example, you can send different responses when someone texts “START” versus “JOIN”.

### Allowlisting for Connected Content

You can allowlist specific URLs to be used for Connected Content. To access this feature, contact your customer success manager.

## Channels & Touchpoints

### SMS character encoding

Our SMS segment calculator now has character encoding! Select Display Character Encoding to identify which characters are encoded as GSM-7 or UCS-2.

### WhatsApp messages with optimization

Because MM API for WhatsApp doesn’t offer 100% deliverability, it’s important to understand how to retarget users who may not have received your message on other channels.

To retarget users, we recommend building a segment of users who didn’t receive a specific message. To do this, filter by the error code 131049, which indicates that a marketing template message was not sent due to WhatsApp’s per-user marketing template limit enforcement. You can do this by using Braze Currents or SQL Segment Extensions.

## Partnerships

### OtherLevels - Dynamic content

OtherLevels is an experience platform that uses generative AI to transform how sports brands, publishers, and operators connect with their customers by transforming traditional content into on-brand personalized video and rich media experiences at scale.

## SDK

### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Web SDK 6.3.1

- 

New Stuff!
