---
url: https://www.braze.com/docs/user_guide/audience/your_audience
slug: docs__user_guide__audience__your_audience
title: "Your Braze audience"
description: "Learn how Braze defines and manages your users, identifies users, and leverages user data to power segmentation, personalization, and messaging across channels."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Your Braze audience

Learn how Braze defines and manages your users, identifies users, and leverages user data to power segmentation, personalization, and messaging across channels.

In Braze, a user (and their user profile) represents an individual person you can message and analyze.

## User profiles

A user profile acts as a single source of truth for everything Braze knows about that person, including:

- Identifiers (such as user IDs or external IDs)
 
- Devices and messaging channels
 
- Behavioral data and events
 
- Attributes and preferences
 
- Message engagement history

A single user profile can be associated with multiple devices and channels, allowing you to understand and message someone holistically across platforms.

## Anonymous users and identified users

Users in Braze generally fall into one of two states.

### Anonymous users

An anonymous user is someone who has interacted with your app or website but has not yet been assigned an identifier from your system (such as an external_id).

- Anonymous users are automatically created when the Braze SDK initializes
 
- You can still track events, attributes, and message engagement
 
- These users can receive messages, depending on channel and opt-in status

### Identified users

An identified user is one that has been associated with an external_id you provide (for example, a customer ID or account ID).

Identifying a user allows you to:

- Merge activity across devices and sessions
 
- Send messages consistently across channels
 
- Segment and personalize using long-term user data
 
- Manage profiles through APIs and integrations

When an anonymous user is later identified, Braze merges eligible data into the identified profile according to this merge behavior. For example, push tokens and messaging history carry over, and many fields from the anonymous profile merge only when they are not already set on the identified profile; when values conflict, the identified profile is kept.

## Message users through channels

A channel is a specific way Braze can deliver a message to a user. Common channels include:

- Push (web or mobile)
 
- Email
 
- SMS, MMS, and RCS
 
- WhatsApp
 
- In-app messages
 
- Content Cards
 
- Banners
 
- LINE
 
- Webhooks

A single user profile can have multiple channels attached, such as both an email address and a mobile device. Braze uses this model to coordinate messaging across channels while maintaining a unified view of the user.

Each channel has its own delivery rules, opt-in requirements, and metadata, but all are associated with the same user profile.

## Ways users enter Braze

Users are created in Braze whenever someone interacts with your brand through a supported integration or channel. How they are added depends on how you implemented Braze.

- mobile apps
 
- web
 
- email and sms
 
- apis and integrations

- When a user opens your app for the first time, the Braze SDK creates a user profile.
 
- Devices and push tokens are automatically registered.
 
- Events and attributes can be logged immediately.

- Users are created when the Web SDK initializes.
 
- Web push subscriptions register a browser as a messaging channel.

- Users can be created when you upload data, call APIs, or collect opt-ins.
 
- Email addresses and phone numbers are stored as channel identifiers.
 
- Opt-in status is tracked per channel and per region.

- You can create or update users directly through REST APIs or importing a CSV.
 
- External tools (such as CDPs, CRMs, or data warehouses) can sync users into Braze automatically.

## Audience data sources

User data in Braze typically comes from a combination of sources.

- automatic collection
 
- user behavior
 
- your systems

Braze SDKs automatically collect contextual data such as:

- Device type and OS
 
- Language and timezone
 
- App version and session activity

When users interact with your app or messages, Braze records:

- Custom events (for example, purchases or feature usage)
 
- Message opens, clicks, and conversions
 
- Session activity and engagement trends

You can send data from your own tools into Braze using:

- REST APIs
 
- CSV uploads
 
- Scheduled data syncs

This often includes identifiers, account data, or historical context.

### User-provided input

Users may provide data directly through:

- Preference centers
 
- Forms or surveys (SDKs or integrations)
 
- In-app experiences

### Integrations

Braze integrates with platforms like Segment, data warehouses, and analytics tech partners through integrations, allowing user data to flow automatically into user profiles.

## Manage user data

You can add, update, or remove user data in several ways:

- Dashboard tools for manual edits or CSV uploads
 
- APIs for real-time or programmatic updates
 
- SDKs for capturing behavior directly in your app or site
 
- Integrations for ongoing synchronization

Data can be removed by:

- Clearing attribute values
 
- Removing tags
 
- Updating subscription states
 
- Resetting users on logout (for anonymous use cases)

## Audience data features

Once user data is in Braze, it powers nearly every engagement capability. The more complete and accurate your user data is, the more effectively you can use the following features.

 Feature | 
 Description | 

 Segmentation | 
 Create audiences based on: 
- Attributes and custom fields 
- Events and behaviors 
- Message engagement 
- Device and channel properties 
Segments can be reused across campaigns and Canvases. | 

 Personalization | 
 Use user data to tailor content, such as: 
- Names and preferences in message copy 
- Dynamic recommendations 
- Location- or language-specific content | 

 Automation and orchestration | 
 Trigger messages and journeys based on: 
- User actions 
- Attribute changes 
- Time-based conditions | 

 Cross-channel coordination | 
 Reach users on the most appropriate channel while respecting: 
- Opt-in status 
- Frequency caps 
- Channel preferences | 

 Analytics and insights | 
 Understand how different audiences behave by analyzing: 
- Engagement rates 
- Conversion paths 
- Segment performance over time | 

- 

New Stuff!
