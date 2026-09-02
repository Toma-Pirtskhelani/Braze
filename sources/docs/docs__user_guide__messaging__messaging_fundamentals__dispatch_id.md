---
url: https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/dispatch_id
slug: docs__user_guide__messaging__messaging_fundamentals__dispatch_id
title: "Dispatch ID behavior"
description: "This reference article describes dispatch ID behavior for campaigns, Canvas, Liquid, and Currents."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Dispatch ID behavior

The dispatch_id is a unique ID for each message dispatch, or “transmission”, sent from Braze.

## Dispatch ID behavior in campaigns

Scheduled campaign messages get the same dispatch_id. Action-based or API-triggered campaign messages may get a unique dispatch_id per user, or the dispatch_id may be the same for multiple users when sent within close proximity or in the same API call. For example, two users in your scheduled campaign audience have the same dispatch_id each time the campaign is scheduled. However, two users in the audience of an API-triggered campaign may have different dispatch IDs if the campaigns were sent in separate API calls and not in close proximity to each other.

Multichannel campaigns have the same behavior for their delivery type.

warning

A dispatch_id is generated randomly for all Canvas steps because Braze treats Canvas steps as triggered events, even when they are “scheduled”. This may result in inconsistencies generating the IDs. Sometimes, a Canvas component has a unique dispatch_id per user per send, or it may have shared dispatch IDs across users per send.

## Template dispatch ID into messages with Liquid

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the dispatch_id. You can find the formatting for this under Canvas Attributes in the list of supported personalization tags.

This behaves like api_id: because the api_id isn’t available at campaign creation, Braze templates it in as a placeholder that previews as dispatch_id_for_unsent_campaign. The ID is generated before the message is sent and is included at send time.

warning

Liquid templating of dispatch_id_for_unsent_campaign does not work with in-app messages since in-app messages don’t have a dispatch_id.

## Dispatch ID Currents field for email

The dispatch_id field is available in Currents email events across all connector types. The dispatch_id is the unique ID generated for each transmission, or dispatch, sent from the Braze platform.

While all customers who are sent a scheduled message get the same dispatch_id, customers who receive either action-based or API-triggered messages get a unique dispatch_id per message. The dispatch_id field enables you to identify which instance of a recurring campaign is responsible for conversion, so you can see which types of campaigns drive results.

You can use dispatch_id as a personalization tag, in message engagement events, or when you use Segment, Mixpanel, or Amplitude for Currents.

- 

New Stuff!
