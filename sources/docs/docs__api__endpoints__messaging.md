---
url: https://www.braze.com/docs/api/endpoints/messaging
slug: docs__api__endpoints__messaging
title: "Messaging Endpoints"
description: "This landing page lists the Braze messaging endpoints."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Messaging Endpoints 

The Braze Messaging API provides you with two distinct options for sending messages to your users. You can provide the message contents and configuration in the API request with the /messages/send and /messages/schedule endpoints. Alternatively, you can manage the details of your message with an API-triggered campaign in the Braze dashboard and control when and to whom it is sent with the /campaigns/trigger/send and /campaigns/trigger/schedule endpoints. The following sections will detail the request specification for both methods. 
 
 Similarly to other campaigns, you can limit the number of times a particular user can receive a messaging API campaign by configuring re-eligibility settings in the Braze dashboard. Braze will not deliver API messages to users that haven’t become re-eligible for the campaign regardless of how many API requests are sent. 
 
 The Send Message endpoints allow you to send immediate messages to designated users. If you are targeting a segment, a record of your request will be stored in the Message Activity Log. Use the Schedule Message endpoints to send messages at a designated time, and modify or cancel messages that you have already scheduled.

## Schedule messages endpoints 

- 

 GET: List Upcoming Scheduled Campaigns and Canvases

- 

 POST: Delete Scheduled Messages

- 

 POST: Delete Scheduled API-Triggered Campaigns

- 

 POST: Delete Scheduled API-Triggered Canvases

- 

 POST: Schedule Messages

- 

 POST: Schedule API-Triggered Campaign Messages

- 

 POST: Schedule API-Triggered Canvas Messages

- 

 POST: Update Scheduled Messages

- 

 POST: Update Scheduled API-Triggered Campaign Messages

- 

 POST: Update Scheduled API-Triggered Canvas Messages

## Send messages endpoints

- 

 POST: Create Send IDs

- 

 POST: Send Messages Immediately

- 

 POST: Send API-Triggered Campaign Messages Immediately

- 

 POST: Send API-Triggered Canvas Messages Immediately

## Duplicate message endpoints 

- 

 POST: Duplicate Campaigns

- 

 POST: Duplicate Canvases

## Live Activity endpoints 

- 

 POST: Update Live Activity

- 

New Stuff!
