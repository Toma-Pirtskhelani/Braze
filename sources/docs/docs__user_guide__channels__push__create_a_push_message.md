---
url: https://www.braze.com/docs/user_guide/channels/push/create_a_push_message
slug: docs__user_guide__channels__push__create_a_push_message
title: "Create a push message"
description: "This tutorial page covers the different components involved in creating a Push Message, including configuration, sending, targeting, and more."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create a push message

Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven’t come into the app in a while. Successful push campaigns drive the user directly to content and demonstrate the value of your app. For examples of push notifications, see Braze customer case studies.

## Step 1: Choose where to build your message

tip

Not sure whether to use a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.

- campaign
 
- canvas

- Go to Messaging > Campaigns, then select Create campaign.
 
- For campaigns targeting multiple channels, select Multichannel. Otherwise, select Push notification.
 
- Name your campaign something clear and meaningful.
 
- Add Teams and Tags as needed.

tip

Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by particular tags.

- Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to Multivariate and A/B testing.

tip

If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose Copy from Variant from the Add Variant dropdown.

- Create your Canvas using the Canvas composer.
 
- After you’ve set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
 
- Choose a step schedule and specify a delay as needed.
 
- Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
 
- Choose your advancement behavior.
 
- Choose any other messaging channels which you would like to pair with your message.

## Step 2: Select push platforms

Next, choose which platform and mobile device combination should receive the push. Use this selection to limit the delivery of a push notification to a specific set of apps.

There are a few different ways to do this depending on your previous selections:

 Previous selection | 
 Options | 

 Push notification campaign | 
 Select one or more platforms and devices. If you choose to target multiple devices and platforms your editing experience is optimized for crafting one message for all selected platforms. See Multiple platform push to understand what’s different in this editing experience. | 

 Multichannel campaign | 
 Select Add Messaging Channel to add additional push platforms. Because platform selections are specific to each variant, you can try testing message engagement per platform. | 

 Canvas | 
 In your Message step, select + Add more to add additional push platforms. Similar to multichannel campaigns, platform selections are specific to each variant. | 

## Step 3: Select notification type (iOS and Android)

If you’re creating a multiple platform push campaign and you select Web and/or Kindle the notification type is automatically set to Standard push and cannot be changed.

Otherwise, for iOS and Android, select your notification type:

- Standard push
 
- Push stories (supported on Android + iOS)
 
- Inline image (Android only)

If you want to include images in your push campaign, refer to the following guides on creating a rich notification for iOS or Android.

## Step 4: Compose your push message

Now it’s time to write your push message! The Compose tab allows you to edit all aspects of your message’s content and behavior.

The content of the Compose tab varies based on your chosen notification type in the previous step, but may include any of the following options:

### Notification channel or group (iOS and Android)

For more information on platform-specific notification options, see iOS Notification Options or Android Notification Options.

### Language

Add copy in multiple languages using the Add Languages button. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. For our full list of available languages you can use, refer to Languages supported.

If you’re adding copy in a language that is written right-to-left, note that the final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to Creating right-to-left messages.

### Title and body

- ios
 
- android

Start typing in the message box and watch a preview appear in the preview box beside it. Push messages must be formatted in plain text.

Add a headline using the Title field. To make your push personalized and targeted, you can include Liquid.

Start typing in the message box and watch a preview appear in the preview box beside it. Push messages must be formatted in plain text.

To make your push personalized and targeted, you can include Liquid.

important

You cannot send an Android push message without a title—however, you can enter a single space instead. Keep in mind, if your message only contains a single space, it will be sent as a silent push notification. For more information, refer to Silent push notifications.

tip

Need help creating awesome copy? Try using the AI copywriting assistant. Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

### Image

Where supported, your app icon is automatically added as the image for your push notification. You also have the option to send rich notifications, which allow for more customization in your push notifications by adding additional content beyond copy.

For additional guidance on using images in your push notifications, refer to the following articles:

- Create rich notifications for iOS
 
- Create rich notifications for Android

important

If you are pulling in images with Connected Content or Liquid, ensure that your image URL begins with https://. Using http:// will crash your app.

### On-click behavior

Specify what happens when a user selects the body of a push notification with On-Click Behavior. For example, you can prompt customers to open your application, redirect customers to a specified Web URL, or even open a specific page of your application with a deep link.

Here, you can also set up button prompts within your push notification, such as:

- Accept/Decline
 
- Yes/No
 
- Confirm/Cancel
 
- More

### Sending options

If a user has your app installed on multiple devices, by default, your push message is sent to all devices with a valid push token assigned. If desired, you can select Most recently used device.

There is some nuance for this setting. If this option is selected, Braze will limit multiple sends from occurring except when a campaign targets multiple platforms, such as both iOS and Android. If the user has your app on both an iOS and an Android device, they’ll receive a push for both platforms. If a user’s most recently used device isn’t push enabled, the message will not send.

By default, Braze sends messages to every device a user owns that has a valid push token. For iOS, you can further refine your reach by choosing to send notifications only to iPad devices, or only to iPhone and iPod devices.

If desired, you can set the push destination to Most recently used device.

#### Most recently used device

“Most recently used” is a technical status, not a behavioral one. Because Braze defaults to all devices, switching to this setting significantly narrows your reach and relies entirely on the status of the single device with the newest token.

The most recently used device is determined by which device has the most recently updated push token, rather than which device had the most recent session.

- If a new device’s push token is added to a user profile through the API, that device is immediately considered the most recently used, even if the user hasn’t started a session on it yet.
 
- If a user’s most recently used device is not push enabled, the message will not send at all.

Multiple sends can still occur if a campaign targets different platforms, such as both iOS and Android. If a user has the app on both, they can receive a push for both platforms.

For iOS, you can further limit messaging by only sending push notifications to iPad devices, or only sending to iPhone and iPod devices.

## Step 5: Preview and test your message (optional)

Testing is arguably one of the most critical steps. After you finish composing your perfect push message, test it before sending it out. Select the Test tab to choose from options on how to test your push message. In Test Recipients, you can select a content test group or individual users. You can also use Preview message as user to get a sense of how your message may view on mobile for a random user, existing user, custom user, or multi-language user.

For more information, see Send test messages.

## Step 6: Build the remainder of your campaign or Canvas

- campaign
 
- canvas

Build the remainder of your campaign; see the following sections for further details on how to best use our tools to build push notifications.

### Choose delivery schedule or trigger

Push messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to Scheduling your campaign.

For action-based delivery, you can also set the campaign’s duration and Quiet hours.

This step is also where you can specify delivery controls, such as allowing users to become re-eligible to receive the campaign, or enabling frequency capping rules.

### Choose users to target

Next, you must target users by choosing segments or filters to narrow your audience. You automatically receive a preview of what that approximate segment population looks like. Detailed audience statistics for the channels targeted by your campaign are available in the footer. To see what percentage of your user base is being targeted and the Lifetime Value for this segment, select Show Additional Stats.

important

Your message will only be sent to users who already match the conditions you set in the Target Audience step. After that, they still need to meet the trigger you define in the Schedule Delivery step. Think of the target audience as a waiting room—only people already inside can move forward when the next action happens.

Why does my Total Reachable Users metric not match the sum of all channels?

When you view the Total Reachable Users for your filtered audience, you may notice that the sum of the individual columns is smaller than the Total Reachable Users. This gap is usually because there are a number of users who qualify for the segment or filters in the campaign, but are not reachable through push (for example, because they don’t have valid or active push tokens).

Keep in mind that exact segment membership is always calculated before the message is sent.

You can also choose to only send your campaign to users who have a specific subscription status, such as those who are subscribed and opted in to push.

Optionally, you can also limit delivery to a specified number of users within the segment, or allow users to receive the same message twice upon a recurrence of the campaign.

#### Multichannel campaigns with email and push

For multichannel campaigns targeting both email and push channels, you may want to limit your campaign so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in statuses:

- User A is subscribed to email and is push enabled. This user doesn’t receive the email but will receive the push.
 
- User B is opted-in to email but is not push enabled. This user will receive the email but doesn’t receive the push.
 
- User C is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, under Audience Summary, select to send this campaign to “opted-in users only”. This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default.

important

With this configuration, don’t include any filters in the Target Audiences step that limit the audience to a single channel (for example, Foreground Push Enabled = True or Email Subscription = Opted-In).

### Choose conversion events

Braze allows you to track how often users perform specific actions, conversion events, after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

If you haven’t done so already, complete the remaining sections of your Canvas component. For details about building the rest of your Canvas, including multivariate testing and Optimize with BrazeAI™, see Build your Canvas.

## Step 7: Review and deploy

After you’ve finished building the last of your campaign or Canvas, review its details. For campaigns, the final page gives you a summary of the campaign you designed. Confirm all the relevant details, make sure you’ve tested your message, then send it and watch the data roll in!

Next, see Push reporting to learn how you can access the results of your push campaign. For push notifications, you’ll be able to view statistics for the number of messages sent, delivered, bounced, opened, and directly opened.

### Troubleshooting

#### On-click behavior

If you’re using the default on-click behavior for your SDK version and selecting a push notification with a web URL opens in the app instead of in a web browser, check the following integration guides to determine push notification handling:

- Swift
 
- Android

important

You must assign your delegate object using center.delegate = self synchronously before your app finishes launching, preferably in application:didFinishLaunchingWithOptions:. Otherwise, this can cause your app to miss incoming push notifications. Refer to Apple’s UNUserNotificationCenterDelegate documentation to learn more.

- 

New Stuff!
