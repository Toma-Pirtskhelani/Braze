---
url: https://www.braze.com/docs/user_guide/channels/banners
slug: docs__user_guide__channels__banners
title: "Banners"
description: "This landing page is home to the Braze Banners channel. Here, you can find articles on creating Banners, reporting, testing, and more."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Banners

With Banners, you can create personalized messaging for your users, all while extending the reach of your other channels, such as email or push notifications. You can embed Banners directly in your app or website, which lets you engage with users through an experience that feels natural.

## Prerequisites

Banners availability depends on your Braze package. Contact your account manager or customer success manager to get started.

Before you start, make sure you have Banner placements created in your app or website.

## Why use Banners?

Banners allow marketing and product teams to personalize app or website content dynamically, reflecting real-time user eligibility and behavior. They persistently display messages inline, providing non-intrusive, contextually relevant experiences that can be refreshed at the start of a session or mid-session when your app or website explicitly requests it.

After Banners are integrated into an app or website, marketers can design and launch Banners using a drag-and-drop editor or a full HTML editor, eliminating the need for ongoing developer assistance, reducing complexity, and improving efficiency.

 Use case | 
 Explanation | 

 Announcements | 
 Keep announcements like upcoming events or policy changes at the forefront of your app experience. | 

 Personalizing offers | 
 Show personalized promotions and incentives based on each user’s browsing history, cart content, subscription tier, and loyalty status. | 

 Targeting new user engagement | 
 Guide new users through onboarding flows and account setup. | 

 Sales and promotions | 
 Highlight featured content, trending products, and ongoing brand campaigns persistently and directly on your homepage without disrupting the user experience. | 

## Features

Features for Banners include:

- Easy content building: Create and preview your Banner using a visual, drag-and-drop editor with support for images, text, buttons, email capture forms, custom code, and more. Teams that prefer to manage their own markup can use the HTML editor instead for full control over the Banner’s HTML and styles, or ask BrazeAI Operator™ to generate HTML from a description.
 
- Flexible placements: Define multiple locations within your application or website where Banners can appear, enabling precise targeting to specific contexts or user experiences.
 
- Dynamic personalization: Banners recalculate personalization (Liquid logic) and segmentation every time the banner is refreshed. If a user updates their profile or a custom attribute changes, the next Banner refresh will reflect those changes.
 
- Native prioritization: Set the display priority for when multiple Banners target the same placement, ensuring the right message reaches users at the right time.
 
- Custom Code editor block: Use the Custom Code editor block to add custom HTML for advanced customization or seamless integration with your existing web styles.

## About Banners

### Placement IDs

Banner placements are specific locations in your app or website you create with the Braze SDK that designate where Banners can appear.

Common locations include the top of your homepage, product detail pages, and checkout flows. After placements are created, Banners can be assigned in your Banner campaign.

There is no fixed limit on the number of placements you can create per workspace, and you can create as many placement IDs as your experience requires. Each placement must be unique within a workspace. A single placement ID can be referenced by up to 25 active messages at the same time.

important

Avoid modifying placement IDs after launching a Banner campaign.

### Banner priority

When multiple Banner messages reference the same placement ID, Banners are displayed in order of priority: high, medium, or low. By default, Banners are set to medium, but you can manually set the priority when you create or edit your Banner campaign.

If multiple Banners are set to the same priority, the newest Banner that the user is eligible for is displayed first.

### Placement requests

When you create placements in your app or website, your app sends a request to Braze to fetch Banner messages for each placement.

- You can request up to 10 placements per refresh request.
 
- For each placement, Braze returns the highest-priority Banner the user is eligible to receive.
 
- If more than 10 placements are requested in a refresh, only the first 10 are returned; the rest are dropped.

For example, an app might request three placements in a refresh request: homepage_promo, cart_abandonment, and seasonal_offer. Each request returns the most relevant Banner for that placement.

#### Rate limiting for refresh requests

If you’re on older SDK versions (before Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0, and Flutter 15.0.0), only one refresh request is permitted per user session.

If you’re on newer minimum SDK versions (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+, and Flutter 15.0.0+), refresh requests are controlled by a token bucket algorithm to prevent excessive polling:

- Each user session begins with five refresh tokens.
 
- Tokens refill at a rate of one token every 180 seconds (3 minutes).

Each explicit call to requestBannersRefresh consumes one token. The automatic refresh that occurs at the start of a new session or when changeUser is called does not consume a token, as this refresh is a publishing of the last cached Banner for that user. If you attempt a refresh when no tokens are available, the SDK doesn’t make the request and logs an error until a token refills. This is important for mid-session and event-triggered updates. To implement dynamic updates (for example, after a user completes an action on the same page), call the refresh method after the custom event is logged, but note the necessary delay for Braze to ingest and process the event before the user qualifies for a different Banner campaign.

### Message delivery

Banner messages are delivered to your app or website as HTML content, typically rendered inside an iframe. This ensures that your Banners render consistently across devices, and helps you keep their styles and scripts separate from the rest of your code.

Iframes allow for dynamic and personalized content updates that don’t require changes to your codebase. Each iframe retrieves and displays the HTML for each user session using campaign targeting and personalization logic.

important

Content Cards, in-app messages, Banners, and feature flags rely on device connectivity to sync with Braze servers. Because network conditions can vary, there is a chance that content or updates may not sync, display, or be cleared immediately (for example, if a user is offline). We recommend avoiding these channels for critical, time-sensitive updates.

### Dimensions and sizing

Here’s what you need to know about Banner dimensions and sizing:

- While the composer allows you to preview Banners in different dimensions, that information isn’t saved or sent to the SDK.
 
- The HTML takes up the full width of the container it’s rendered in.
 
- We recommend making a fixed dimension element and testing those dimensions in composer.

### Connected Content

important

Connected Content for Banners is currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.

You can use Connected Content to pull real-time data from external APIs into your Banner. Because Banners render inline during a session refresh, Connected Content has specific limitations in this channel:

- GET requests only: Banners render only GET Connected Content requests. POST requests aren’t supported.
 
- Shared rendering budget: All placements returned in a single refresh request (up to 10) share one rendering budget of approximately two seconds. Each Connected Content call counts against this shared budget, so a placement with slow or numerous calls can use time that other placements need.
 
- No retries: If a Connected Content call fails, times out, or the rendering budget is exceeded, the Connected Content result for that placement is treated as null. Unlike other channels, Banners don’t retry the request or delay delivery.

## Limitations

Each workspace can support up to 200 active Banner campaigns. If this limit is reached, you’ll need to archive or deactivate an existing campaign before creating a new one.

Additionally, Banner messages do not support the following features:

- API-triggered and action-based campaigns
 
- Connected Content (in early access)
 
- Promotional codes
 
- catalog_items using the :rerender tag

## Next steps

- Create Banner placements in your app or website
 
- Create a Banner campaign in Braze
 
- Tutorial: Displaying a Banner by Placement ID

tip

Want to help prioritize what’s next? Contact [email protected].

- 

New Stuff!
