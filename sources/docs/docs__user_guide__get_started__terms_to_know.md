---
url: https://www.braze.com/docs/user_guide/get_started/terms_to_know
slug: docs__user_guide__get_started__terms_to_know
title: "Terms to Know"
description: "This glossary covers important terms to know as you go through the Braze onboarding process."
section: user_guide/get_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# Terms to Know 

 These terms should help you as you begin your journey to better customer and user bonds with Braze. Give this a read before you begin your onboarding. 

 Search glossary
 Results update automatically as you type.

API campaigns 
API campaigns use the Braze dashboard to generate a campaign_id (and variation IDs) while you supply copy, audience, schedule, and assets through the messaging APIs. They differ from API-triggered campaigns, where you trigger a fully configured campaign from the dashboard via API.

Active user 
For campaign targeting, Braze defines an active user for a given period as anyone who has a session in that period (users updated via the API also count for that period). For user archival and reachability statistics, Braze uses a broader definition that also includes profile updates, messages sent to the user, and interactions with messages.

Alloys 
Alloys are our Technology Partners.

Anonymous users 
When a user profile is recognized via the SDK, an anonymous user profile is created with the associated Braze user ID.

App instance 
App instances refer to the different sites and apps that are collected in a workspace.

Application program interface (API) 
The Braze API provides a web service where you can record actions taken by your users directly via HTTP, rather than through the mobile SDKs. This allows you to, for example, pass user data to Braze that is not tracked within your app or website.

Braze (the product) 
Sometimes referred to as the dashboard, this product controls all of the data and interactions at the heart of the Braze platform. Braze customers use it to manage notifications, set up targeted messaging campaigns, and view analytics. Developers use it to manage settings for integrating apps, such as API keys and push notification credentials.

Campaign 
Campaigns are customizable messaging methods to deliver personalized response to your customers. You can build campaigns using different messaging channels to send your unique messages.

Canvas 
Canvas is a single unified interface where marketers can set up campaigns with multiple messages and steps to form a cohesive journey. Canvas allows you to compare and optimize those experiences using comprehensive analytics for the full user experience.

Connected Content 
Connected Content expands on marketing personalization to boost customer engagement and conversions. You can insert any information accessible using API directly into messages you send to users. Connected Content allows for pulling content either directly from your web server or publicly accessible APIs.

Content Cards 
Content Cards allow you to send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. Content Cards can be sent to iOS, Android, and web users.

Conversion event 
A conversion event is a success metric that records whether a recipient performed a high-value action within a conversion window after receiving your message (or after entering a Canvas or control group, depending on channel and setup). Use conversion events to measure campaign and Canvas performance beyond sends alone.

Currents 
Currents, our data streaming export, is included in certain Braze packages. Braze Currents allows you to integrate through Data Storage using flat files or to our Behavioral Analytics and Customer Data partners using batched JSON payloads to a designated endpoint.

Custom attributes 
Custom attributes are a collection of your users' unique traits. They are best for storing attributes about your users, or information about low-value actions within your application. You can assign custom attributes to users within the dashboard. You can filter and segment your users according to these attributes for both Swift and Android campaigns.

Custom events 
Custom events are actions taken by your users; they're best suited for tracking high-value user interactions with your application.

Data point 
A data point is counted when a custom attribute is set or updated (even if you're updating it with the same value), a custom event or purchase event is logged, any standard data (for example, email, first_name, last_name, country, or home_city) is logged, when a session starts, and when a session ends.

Deep linking 
Deep links are used to direct customers to their next action or engagement. Using deep links, you can connect a message with a targeted piece of content within a website or mobile app.

Dormant users 
A user is considered dormant when they have had no qualifying activity in the last twelve months—they have not used any app or website in the workspace, have not received any messages from the workspace, and have not been updated in more than twelve months. By default Braze uses a twelve-month window for dormant archival; your company settings can override the number of days.

Endpoint 
An end of a communication channel also known as an API endpoint is used within the Braze messaging API for sending and scheduling messages.

Exception event 
In Canvas, exception events are specific actions that remove a user from the journey when they occur (for example, placing an order). They keep follow-up messages relevant after the user completes your goal. See Exit criteria for how exits are evaluated and timed.

External ID 
The external_id is the primary user identifier on a Braze user profile. It ties the same person across channels and devices when you assign IDs from your own systems. Anonymous profiles may not have an external_id until you identify the user. For more information, see Users and segments and User IDs.

Frequency capping 
Frequency capping allows you to manage communication without overwhelming your audience. It's an automated limit on messages to prevent users from receiving too many communications in a short period of time.

HIPAA 
HIPAA is an acronym for Health Insurance Portability and Accountability Act. Braze is HIPAA compliant. HIPAA requirements involve administrative, physical, and technical security.

IP warming 
IP warming is the practice of gradually increasing the amount of mail sent out from a dedicated IP. This helps establish a reputation with Internet Service Providers, minimizing the probability of your messages getting flagged.

In-app message 
In-app messages are mobile messages that appear within your application. They help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app.

Inactive users 
A user is considered inactive when they are unreachable on major messaging channels (for example, email, SMS, push, WhatsApp, and LINE per your configuration), have not used any app or website in the workspace in more than six months, have not received any messages from the workspace in more than six months, and have not been updated in more than six months. Inactive users are candidates for archival along with dormant users. By default Braze uses a six-month window for inactive archival; your company settings can override the number of days.

Key-value pairs 
Key-value pairs are linked data items where the key is a unique identifier and the value is the content. They can be used to send extra data payloads to user devices.

Liquid 
Liquid is a commonly-used, customer-facing template language created by Shopify and written in Ruby. Liquid is used to load and pull dynamic content. Liquid allows you to use objects, tags, and filters to add personal customization.

Messaging channel 
Messaging channels are ways you can virtually communicate with your customers–through push notifications on their phone or web browser, email, in-app messages, and so much more!

Monthly active user (MAU) 
These are users who have a session within the last 30 days.

Multichannel messaging 
Messaging a user across various mediums, such as a combination of email, web push, and mobile push notifications. Messaging channels are best used in concert and with regularity to re-engage lost users, retain active users, and energize your brand ambassadors.

Multivariate testing 
A/B testing compares a smaller set of message versions; multivariate testing compares multiple variables at once to see which combination performs best. You can configure both from the dashboard for supported campaign types.

New user 
Braze considers a new user as anyone who has newly installed your app. Alternatively, a new user can also be defined as a user with a user ID that has not been previously identified within Braze.

Personalization 
Using technology to take into account the individual preferences and tendencies of each user when communicating with them. Personalized messaging helps build valuable customer experiences by tailoring to their preferences.

Push message 
A push message, or push notification, is a notification that appears from a mobile application. Push notifications often appear as pop-up dialogs and banners for both iOS and Android.

Push time to live (TTL) 
Also known as Push TTL, time to live refers to the period that campaigns will continue to attempt to be delivered to an offline user.

Push token 
A push token is a unique key, created and assigned by Apple or Google to create a connection between an app and an iOS, Android, or web device. Push token migration is the importing of those already-generated keys into Braze.

Race condition 
A race condition is a software engineering concept that describes some undesirable situation that occurs when a system tries to perform several operations simultaneously, but because of the nature of the system, the operations must be done in the correct sequence to be done correctly. 

In the Braze platform, segmenting a triggered campaign on user data recorded at the time of the event may cause a race condition. This happens when a change in the user attribute on which the campaign is segmented hasn't yet been processed for the user at the time segment membership is determined and the campaign is sent and can lead to the user not receiving the campaign.

Rate limiting 
Rate limiting controls how quickly messages leave Braze (for example, delivery speed per minute or user-centric limits using segment filters). It works alongside frequency capping on the same page, which limits how many messages a user receives in a time window.

Segmentation 
Dashboard segmentation allows you to create groups or extensions of users based on powerful filters of their in-app behavior, demographic data, and more.

Software development kit (SDK) 
SDKs are integrated into your mobile apps, websites, and connected experiences and provide marketing, messaging, and analytics tools. Braze publishes SDK integration guides for platforms such as Swift and Android; for Web and other platforms, follow the integration paths linked from the SDK overview.

Subscription groups 
Subscription groups layer on top of global subscription states so you can offer granular opt-in choices (for example, newsletters versus promotions). Similar patterns exist for channels such as SMS and WhatsApp; always target a subscription group where your channel requires it.

Sunsetting 
Sunsetting refers to the process of identifying disengaged users and ceasing active messaging to these users without them having to take any action. Creating sunset policies for your email and push messages can help curb impacts to your open rates.

Tag 
Tags are a tool that help you categorize, organize, and sort your engagement across one or multiple campaigns.

Team 
Braze admins can divide a subset of dashboard users into Teams with varying user roles and permissions. This allows Braze admins to limit access to certain features by group membership.

User alias 
User aliases are alternative identifiers you can assign to anonymous profiles before an external_id exists, so you can reference the same person across devices or channels until they log in.

User archival 
User archival refers to users that have been archived. At Braze, this includes both inactive and dormant users. Archival evaluates the inactive and dormant rules in Braze services (see User archival for scheduling, workspace eligibility such as user-count thresholds, and how to customize windows with company settings or Canvas).

User profile 
A user profile is the central record for each person in Braze, including identifiers, attributes, events, purchases, devices, engagement history, and message history. Profiles power segmentation, personalization, and compliance workflows across channels.

Webhook 
Webhooks allow you to trigger non-app actions such as SMS text message delivery. You can use webhooks to provide other systems and applications with real-time information. The flexibility of this feature allows you to send information to any endpoint.

Workspace 
A workspace is the container where Braze stores data and where your team builds campaigns, Canvases, and segments. Each workspace holds one or more app instances (the individual apps and sites that send data into that workspace).

- 

New Stuff!
