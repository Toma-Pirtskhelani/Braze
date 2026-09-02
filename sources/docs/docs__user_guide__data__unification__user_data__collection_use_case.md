---
url: https://www.braze.com/docs/user_guide/data/unification/user_data/collection_use_case
slug: docs__user_guide__data__unification__user_data__collection_use_case
title: "Collection use case"
description: "This reference article covers a user data collection use case on how a ride-sharing app might decide what user data to collect."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Collection use case

This article covers a user data collection use case on how a ride-sharing app might decide what user data to collect.

Let’s say a taxi or ride-sharing app, called StyleRyde, wants to decide what user data to collect. The following questions and brainstorming process are a great model for their marketing and development teams to follow. By the end of this exercise, both teams should have a solid understanding of what custom events and attributes make sense to collect to help meet their goal.

## Case question 1: What is the goal?

StyleRyde’s goal is straightforward in that they want users to hail taxi rides through their app.

## Case question 2: What are the steps to reach that goal after app installation?

- StyleRyde needs users to begin the registration process and fill out their personal information.
 
- StyleRyde needs users to complete and verify the registration process by inputting a code into the app they receive through SMS.
 
- StyleRyde needs users to attempt to hail a taxi.
 
- StyleRyde needs to be available when users hail a taxi.

These actions could then be tagged as the following custom events:

- Began Registration
 
- Completed Registration
 
- Successful Taxi Hails
 
- Unsuccessful Taxi Hails

After implementing the events, StyleRyde can run campaigns including the following:

- Message users who Began Registration, but haven’t Completed Registration within a certain time frame.
 
- Send congratulation messages to users who Completed Registration.
 
- Send apologies and promotional credit to users who had Unsuccessful Taxi Hails, that weren’t followed by a Successful Taxi Hail within a certain amount of time.
 
- Send promotions to power users with lots of Successful Taxi Hails to thank them for their loyalty.

## Case question 3: What other user information could we collect and use to inform our messaging?

- Whether users have any promotional credit?
 
- The average rating users give to their drivers?
 
- Unique promo codes for users?

These characteristics could then be tagged as the following custom attributes:

- Promotional Credit Balance (Decimal Type)
 
- Average Driver Rating (Integer Type)
 
- Unique Promo Code (String Type)

These attributes allow you to send campaigns to users such as:

- Reminding users who haven’t used the app in seven days and have promotional credit in their account to return to the app and use the credit.
 
- Using our message templates and personalization features to drag the unique promotion code attribute into messaging directed at users.

important

Braze blocks user profiles (“dummy users”) with more than 5,000,000 sessions, more than 20,000 distinct custom event names, or more than 20,000 distinct product names in purchases, because they are usually the result of misintegration. After a profile is blocked, Braze stops ingesting all inbound data for that profile, from both the SDKs and the REST API. If you find that this has happened to a legitimate user, contact your Braze account manager.

- 

New Stuff!
