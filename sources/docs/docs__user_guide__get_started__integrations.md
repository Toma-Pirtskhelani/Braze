---
url: https://www.braze.com/docs/user_guide/get_started/integrations
slug: docs__user_guide__get_started__integrations
title: "Integration"
description: "This reference article briefly covers the integration steps required from your engineers or developers."
section: user_guide/get_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# Integration

Integrating with Braze is a worthwhile process. But you’re smart. You’re here. Clearly, you already know that. But what you probably don’t know is that you and your developers are about to go on a journey together that requires technical expertise, strategic planning, and consistent communication that will help you coordinate between the two.

note

Note that the contents of this article don’t apply to email. Check that out in the Email setup section.

## The technical side of the integration process

You may find yourself thinking, “My developers are magical! They can do anything, so I usually just leave them to it!” And they probably are and probably can! But there’s no reason why you shouldn’t know what they’re doing behind the scenes. In fact, it would help the entire process if you knew when to jump in with information and what to look for when they say, “Can you send me the API key and API endpoint?”

So, what are they doing when they integrate Braze with your app or site? Glad you asked!

### Step 1: They implement the Braze SDK

The Braze SDK (Software Development Kit) is how we send and get information to and from your app or site. Your engineers are, essentially, tying our apps together. To do this, they need a few pieces of key information:

- Your API keys
 
- Your SDK endpoint

- Braze no longer gives out custom endpoints so use the predefined SDK endpoints. If you have been given a pre-existing custom endpoint, Here, you can find the setup steps involved for Android, iOS, and Web integration.

You can either give this information to them directly, or you can give them access to Braze by creating an account for them.

warning

Ensure that you and your developers don’t unknowingly or unintentionally change the company’s credentials in Braze, as this could cause issues during the implementation process or lock one or more of you out of your accounts.

### Step 2: They implement your desired messaging channels

Braze has many options for getting in touch with your users, and each requires its own setup or tweaking to work the way you want. This is where communication with your engineers becomes critical.

Be sure to tell your developers which channels you want to use to ensure that implementation is done efficiently and in proper order.

 Channel | 
 Details | 

 In-app messages | 
 Requires SDK implementation as well as these channel-specific steps. | 

 Push | 
 Requires SDK implementation to provide proper handling around messaging credentials and push tokens. | 

 Email | 
 This is an entirely different process. Check out the Email Setup section for more details on integration. | 

 Content Cards | 
 To get started with Content Cards, contact your Braze customer success manager. | 

 SMS & MMS | 
 Check out the SMS Setup section for more details on integration. | 

 Webhooks | 
 Requires SDK implementation as well as channel-specific steps. | 

tip

You can use Braze to create accessible messaging campaigns across each channel. Work with your developers to ensure that you meet accessibility standards in your implementation.

### Step 3: They set up your data

Braze isn’t a one-trick pony. This isn’t about just sending emails or sending push. This is about creating personalized customer journeys that are unique for every user and customer. The customer journeys are based on their actions within your app or site, and you get to define what those are! Your developers’ next task is to ensure that actions taken within your app or site are picked up by Braze.

So, what do you need to do to get them this information?

- Work with your marketing team to define campaigns, goals, attributes, and events you need to track. Define those use cases and share them with your teams.
 
- Define your custom data requirements (custom attributes, custom events, etc.).
 
- From there, discuss how that data should be tracked (triggered through the SDK, etc.).
 
- Define how many workspaces you need. Your engineers will need to know how to test and configure these workspaces.

Once you discover all of this information, share it with your engineer. They’ll take that information and implement your custom data. You might even need to import some users. You should also be aware of event naming conventions.

### Step 4: They customize based on what you want

If you want things like API-triggered launching and Connected Content, discuss that with both your Braze contact and your developers to ensure that you’ll be able to get data that lives outside of your app and Braze into your messages.

### Step 5: You both perform QA on your implementation

Work together with your engineer to make sure everything is working. Send test messages, use our test apps for Android and test apps for iOS, check every box before you start sending!

We even have specific instructions for testing your Android or FireOS integration and testing push for iOS.

## After implementation

Keep in mind that the implementation finish line isn’t also the green light to send a million messages at once. Sending a million push might break your app if every customer clicks the same link simultaneously. We recommend discussing what your capacity of your internal setup is for handling requests from Braze before clicking that Send button. Then, you can set your rate limiting based on that.

After you’re comfortable using Braze, consider becoming a Braze Firebrand! With Braze Firebrands, our customer engagement community, we’re building a community of movers and shakers using Braze to modernize their customer experience and marketing. Interested in learning more? Join now.

- 

New Stuff!
