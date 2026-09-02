---
url: https://www.braze.com/docs/developer_guide/platforms/web/multi_domain_integration
slug: docs__developer_guide__platforms__web__multi_domain_integration
title: "Multi-domain integration"
description: "Learn how to implement the Braze Web SDK across multiple domains, including API key strategy, push setup, and session behavior."
section: developer_guide/platforms
fetched: 2026-09-02
evidence: company-own (technical)
---
# Multi-domain integration

Learn how to integrate the Braze Web SDK across multiple web domains.

When your implementation spans multiple domains, browser origin boundaries affect how the Braze Web SDK stores and reads user state.

## Choose an app and API key strategy

You can use one Web SDK API key across multiple domains, but in most cases, using separate API keys mapped to separate apps in the same workspace gives you better control.

 Strategy | 
 Recommended when | 
 Tradeoffs | 

 Separate apps (recommended) | 
 You want independent targeting, reporting, and campaign control per domain | 
 Requires managing two app integrations | 

 Single app | 
 You treat both domains as one property operationally | 
 Session triggers and domain-level reporting are harder to separate | 

With separate apps in one workspace, you can use app filters for cleaner segmentation and message targeting by domain.

## Configure push notifications on one domain

For separate root domains, web push registration is isolated per domain.

- Choose one domain as your push-notification domain.
 
- Do not register push on both root domains for the same user journey, because this can create conflicting prompt and subscription behavior.

## Identify users consistently across domains

By default, each root domain stores its own SDK state. To associate activity to the same Braze user profile across domains:

- Call changeUser() with the same external_id on each domain after login.
 
- Keep both apps in the same workspace if you’re using separate API keys.

For general user ID guidance, refer to Set user IDs through the Braze SDK.

## Plan event and trigger behavior by domain

How you model events and triggers depends on your app strategy:

- Single app across domains: Log domain-specific custom events so you can distinguish behavior by site in segmentation and triggering.
 
- Separate apps: Prefer app filters for domain-specific targeting and analytics.

## Understand session behavior across domains

By default, the Web SDK session timeout is 30 minutes of inactivity. For separate root domains using one app/API key:

- Each domain starts and ends sessions independently.
 
- A user moving between both domains can create overlapping sessions.
 
- Session start triggers may fire on both domains.

For base session lifecycle details, refer to Track sessions through the Braze SDK.

- 

New Stuff!
