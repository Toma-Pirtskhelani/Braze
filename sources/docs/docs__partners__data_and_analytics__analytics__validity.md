---
url: https://www.braze.com/docs/partners/data_and_analytics/analytics/validity
slug: docs__partners__data_and_analytics__analytics__validity
title: "Validity"
description: "This reference article outlines the partnership between Braze and Validity, an email deliverability platform that syncs Everest seed lists to Braze and automates inbox placement..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Validity

Validity Everest is an email deliverability platform that helps you measure inbox placement and protect your sending reputation. The Braze and Validity integration syncs your Everest seed list to Braze, automatically seeds qualifying campaigns and Canvases, and pulls engagement metrics back into Validity Inbox so you can compare seed-based placement with real subscriber engagement.

This integration is maintained by Validity.

## About the integration

Validity creates and maintains email seed list users in Braze so seed addresses stay active and unsuppressed. When a campaign or Canvas is ready to be seeded, Validity sends a copy to that seed list and surfaces engagement metrics—delivered, bounces, opens, clicks, and unsubscribes—in Validity Inbox alongside inbox placement data.

## Use cases

### Auto-seeding

With Validity auto-seeding, Validity detects when a Braze campaign or Canvas reaches a qualifying send volume and sends a copy of that campaign’s content to your Validity seed list. Seed sends target users where the validity_seed custom attribute is set to true.

## Prerequisites

Before you start, you need the following:

 Requirement | 
 Description | 

 A Validity account | 
 A Validity account is required to take advantage of this partnership. | 

 A Braze REST API key | 
 A Braze REST API key with the following permissions: users.track, users.delete, email.bounce.remove, email.spam.remove, campaigns.list, campaigns.details, campaigns.data_series, canvas.list, canvas.details, canvas.data_series, content_blocks.list, content_blocks.info, and messages.send. 

 Create this key in the Braze dashboard from Settings > APIs and Identifiers. | 

 A Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. For example, rest.iad-01.braze.com. | 

 A Braze app identifier | 
 The Braze app identifier that seed sends should be attributed to. Find it under Settings > APIs and Identifiers > App Identifiers. | 

## Integrating Validity

### Step 1: Share Braze credentials with Validity

Validity requires three credentials from Settings > APIs and Identifiers in your Braze dashboard:

- Your REST API key (with the permissions listed in Prerequisites)
 
- Your REST endpoint
 
- Your app identifier

Share these credentials with your Validity representative, who completes the integration setup for you. Validity validates the credentials with a live test call to Braze before enabling the integration. If you’re unsure who your Validity contact is, email [email protected].

After the integration is enabled, Validity syncs your Everest seed list to Braze on a recurring cycle (every 10 minutes). Validity creates, updates, and removes seed users in Braze to keep them aligned with your current seed list in Everest.

### Step 2: Optionally create a Braze segment for Validity seed users

Creating a segment is optional. Auto-seeding sends test emails using a Connected Audience object filtered on the validity_seed custom attribute whenever a qualifying send is detected. You don’t need to build a segment or attach it to your campaigns.

If you want a way to view this audience inside Braze for reference, create a segment under Audience > Segments with the filter validity_seed is true.

Validity creates users through the /users/track endpoint using the following schema:

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

```
 | 
```
curl -X POST "https://YOUR_API_ENDPOINT/users/track" \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer YOUR_BRAZE_API_KEY" \
 -d '{
 "attributes": [
 {
 "email": "[email protected]",
 "validity_seed": true
 },
 {
 "email": "[email protected]",
 "validity_seed": true
 }
 ],
 "events": [
 {
 "email": "[email protected]",
 "name": "validity_seed_event",
 "time": "2026-07-02T18:00:00.000Z"
 }
 ]
 }'

```
 | 

These users always include the custom attribute validity_seed with the boolean value true. Validity also sends a validity_seed_event custom event for each seed user so they register as active users in your Braze account.

## Considerations

### How seed sends work

Validity pulls the campaign body, subject, and from address through the campaign and Canvas details endpoints, then delivers a copy of that content to the seed list through the Braze /messages/send endpoint. Your Braze dashboard continues to show only the original campaign.

### Auto-seeding threshold

Validity detects when a campaign or Canvas crosses your configured send volume threshold (10,000 sends by default) and sends the seed test at that point. You don’t need to add the seed audience to your campaigns or Canvases.

A seed test sends your email campaign to the addresses on the seed list, gathers placement data, and helps you identify issues before or alongside sends to your audience. Inbox placement metrics show whether your campaign lands in the inbox, the spam folder, or goes missing. Use these metrics to confirm inbox placement and catch deliverability issues.

Seed tests can also help you diagnose why emails hit the spam folder or go missing. Checking header data, authentication (SPF, DKIM, and DMARC), link validation, and design rendering can show what steps to take to improve your inbox placement rate.

### Seed list health

Validity monitors seed list users and may update or remove them if they begin to lose effectiveness—for example, if email service providers (ESPs) start to flag seed list audience members as spam. These permissions allow Validity to monitor seed list health and update the list accordingly.

### How dynamic content is handled

Braze emails often use Liquid personalization tied to a real recipient’s profile. Because seed addresses don’t have that profile data, Validity runs each email through a sanitizer before seeding it. The sanitizer resolves Content Blocks, evaluates basic Liquid logic, and replaces anything it can’t resolve (such as a first name) with a visible [REDACTED] placeholder. Sections built entirely from live Connected Content APIs render blank in the seed.

You can turn the sanitizer on or off. When it’s turned off, Braze resolves Liquid personalization for seed sends the same way it would for a real recipient.

### Inbox Aggregate

Enabling auto-seeding also enables Inbox Aggregate. This feature pulls engagement metrics—sent, delivered, bounces, opens, clicks, and unsubscribes—from your real Braze sends (separately from seed sends) and surfaces them in Validity Inbox alongside your inbox placement data. The two features run on independent schedules and don’t need to be managed separately.

- 

New Stuff!
