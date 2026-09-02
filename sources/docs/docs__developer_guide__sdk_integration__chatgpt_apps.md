---
url: https://www.braze.com/docs/developer_guide/sdk_integration/chatgpt_apps
slug: docs__developer_guide__sdk_integration__chatgpt_apps
title: "Integrate Braze with ChatGPT apps"
description: "Learn how to integrate Braze with ChatGPT Apps to enable analytics and event logging within AI-powered applications."
section: developer_guide/sdk_integration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Integrate Braze with ChatGPT apps

This guide covers how to integrate Braze with ChatGPT apps to enable analytics and event logging within AI-powered applications.

## Overview

ChatGPT apps provide a powerful platform for building AI conversational applications. By integrating Braze with your ChatGPT app, you can continue to maintain first-party data control in the age of AI, including how to:

- Track user engagement and behavior within your ChatGPT app (such as identifying which questions or chat features your customers use)
 
- Segment and retarget Braze campaigns based on AI interaction patterns (such as emailing users who have used the chat more than three times per week)

### Key benefits

- Own your customer journey: While users interact with your brand through ChatGPT, you maintain visibility into their behavior, preferences, and engagement patterns. This data flows directly onto Braze user profiles, not just the AI platform’s analytics.
 
- Cross-platform retargeting: Track user interactions in your ChatGPT app and retarget them across your owned channels (email, SMS, push notifications, in-app messaging) with personalized campaigns based on their AI usage patterns.
 
- Return 1:1 promotional content to ChatGPT conversations: Deliver Braze in-app messages, Content Cards, and more directly within your ChatGPT experience using the custom conversational UI components your team has built for your app.
 
- Revenue attribution: Track purchases and conversions that originate from ChatGPT app interactions.

## Prerequisites

Before integrating Braze with your ChatGPT app, you must have the following:

- A new web app and API key in your Braze workspace
 
- A ChatGPT app created in the OpenAI platform (OpenAI sample app)

# ChatGPT app integration

## Setup

### Step 1: Get the Braze integration file

Copy the braze.js file from our ChatGPT apps integration repository to your project. This file contains all the necessary Braze SDK configuration and helper functions.

### Step 2: Install dependencies

Install our Web SDK for Braze’s most up-to-date set of features:

For client-side integration:

```

1

```
 | 
```
npm install @braze/web-sdk

```
 | 

## Implementation

There are two ways to integrate Braze with your ChatGPT app depending on your use case:

### Client-side integration (custom widgets)

tip

Recommended Approach: This method enables rich messaging experiences and real-time user interaction tracking within your ChatGPT app widgets.

For displaying Braze messaging and tracking user interactions within your custom ChatGPT app widgets, use the Web SDK integration. A full messaging example can be found in our sample repository here.

#### Configure widget metadata

Add the following metadata to your MCP server file to allow Braze domains, ensuring to update the CDN domain based on your region:

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

```
 | 
```
"openai/widgetCSP": {
 connect_domains: ["https://YOUR-SDK-ENDPOINT"],
 resource_domains: [
 "https://appboy-images.com",
 "https://braze-images.com",
 "https://cdn.braze.eu",
 "https://use.fontawesome.com"
 ],
}

```
 | 

Replace YOUR-SDK-ENDPOINT with your actual Braze SDK endpoint.

#### Set up the useBraze hook

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
23
24

```
 | 
```
import { useBraze } from "./utils/braze";

function YourWidget() {
 const braze = useBraze({
 apiKey: "your-braze-api-key",
 baseUrl: "your-braze-endpoint.braze.com",
 });

 useEffect(() => {
 if (!braze.isInitialized) {
 return;
 }

 // Set user identity
 braze.changeUser("user-id-123");
 
 // Log widget interactions
 braze.logCustomEvent("viewed_pizzaz_list");
 }, [braze.isInitialized]);

 return (
 // Your widget JSX
 );
}

```
 | 

#### Display Braze Content Cards

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

```
 | 
```
const [cards, setCards] = useState([]);

useEffect(() => {
 // Get cached content cards
 setCards(braze.getCachedContentCards()?.cards ?? []);

 // Subscribe to content card updates
 braze.subscribeToContentCardsUpdates((contentCards) => {
 setCards(contentCards.cards);
 });

 // Open session
 braze.openSession();

 return () => {
 braze.removeAllSubscriptions();
 }
}, []);

```
 | 

#### Track widget events

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

```
 | 
```
// Track user interactions within your widget
const handleButtonClick = () => {
 braze.logCustomEvent("widget_button_clicked", {
 button_type: "save_list",
 widget_name: "pizza_list"
 });
};

const handleItemInteraction = (itemId) => {
 braze.logCustomEvent("item_interacted", {
 item_id: itemId,
 interaction_type: "view_details"
 });
};

```
 | 

### Server-side integration (MCP server)

If you also need a server-side integration for messaging functionality on your MCP server, contact [email protected]. For tracking events and purchases from your MCP server, use our REST API.

- 

New Stuff!
