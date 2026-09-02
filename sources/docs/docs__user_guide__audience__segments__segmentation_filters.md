---
url: https://www.braze.com/docs/user_guide/audience/segments/segmentation_filters
slug: docs__user_guide__audience__segments__segmentation_filters
title: "Segmentation Filters"
description: "This glossary lists available filters to segment and target your users."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Segmentation Filters 

 The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.

To learn about the different custom attribute data types you can use to segment users, view Custom attribute data types. 

 Search glossary
 Results update automatically as you type.
 
Select a category to narrow the glossary:

 ‍
 Segment or CSV membership

 ‍
 Custom attribute

 ‍
 Custom events

 ‍
 Sessions

 ‍
 Retargeting

 ‍
 Channel subscription behavior

 ‍
 Purchase behavior

 ‍
 eCommerce

 ‍
 Demographic attributes

 ‍
 App

 ‍
 Uninstall

 ‍
 Devices

 ‍
 Location

 ‍
 Cohort membership

 ‍
 Install attribution

 ‍
 Intelligence and predictive

 ‍
 Social activity

 ‍
 Other Filters

 ‍
 Advertising use cases

 ‍
 User Attributes

Ad Tracking Enabled 
Allows you to filter based on whether your users have opted-in to ad tracking. Ad tracking relates to the IDFA or "identifier for advertisers" assigned to all iOS devices by Apple, which can be set by SDKs. This identifier allows advertisers to track users and serve them targeted ads.

Filter Category: Advertising use cases

Age 
Segments your users by their age, as they indicated from within your app.

Filter Category: Demographic attributes

Amplitude Cohorts 
Clients who use Amplitude can supplement their segments by choosing and importing their cohorts in Amplitude.

Filter Category: Cohort membership

Average order value (last 730 days) 
Segments your users by the average (mean) value of a user's orders over the last 2 years, based on the eCommerce recommended event for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Background or Foreground Push Enabled 
Segments by whether users have a push token and haven't unsubscribed. Users who are background or foreground push enabled for any of your apps.

Filter Category: Channel subscription behavior

Birthday 
Segments your users by their birthday, as they indicated from within your app. 
 Users with a birthday on the 29th of February are included in segments including March 1.

To target December or January birthdays, only insert filter logic within the 12-month span of the year you're targeting. In other words, do not insert logic that looks back to the previous calendar year's December or forward to the next year's January. For example, to target December birthdays, you can filter for "on December 31", "before December 31", or "after November 30".

Filter Category: Demographic attributes

Braze Segment Extensions 
After creating a Segment Extension in the Braze dashboard, you can choose to include/exclude those extensions in your segment.

Filter Category: Segment or CSV membership

Census Cohorts 
Clients who use Census can supplement their segments by choosing and importing their cohorts in Census.

Filter Category: Cohort membership

Churn Risk Category 
Segments your users by churn risk category according to a specific prediction.

Filter Category: Intelligence and predictive

Churn Risk Score 
Segments your users by churn risk score according to a specific prediction.

Filter Category: Intelligence and predictive

City 
Segments your users by their last indicated city location.

Filter Category: Demographic attributes

Clicked Alias in Any Campaign or Canvas Step 
Filter your users by whether they clicked a specific alias in any campaign or Canvas. This only applies to email messages. 

 If multiple users share the same email address:
- When the email is opened or clicked, all other users with that same email address also have their profiles updated. 
- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.

Filter Category: Retargeting

Clicked Alias in Campaign 
Filter your users by whether they clicked a specific alias in a specific campaign. This only applies to email messages. 

 If multiple users share the same email address:
- When the email is opened or clicked, all other users with that same email address also have their profiles updated. 
- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.

Filter Category: Retargeting

Clicked Alias in Canvas Step 
Filter your users by whether they clicked a specific alias in a specific Canvas. This only applies to email messages. 

 If multiple users share the same email address:
- When the email is opened or clicked, all other users with that same email address also have their profiles updated. 
- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.

Filter Category: Retargeting

Clicked card 
Segments your users by whether they have clicked a specific Content Card. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".

Filter Category: Retargeting

Clicked/Opened Campaign 
Filter by interaction with a specific campaign. For in-app messages, clicked in-app messages include body and button clicks. It does not count dismiss actions or closing the message with the X.

For emails, the open event includes both machine opens and non-machine opens. This filter also includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)". Clicks on unsubscribe links and preference centers don't count toward this filter. If multiple users share the same email address:
- When the email is opened or clicked, all other users with that same email address also have their profiles updated. 
- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.

For SMS and RCS, an interaction is defined as:
- The user last sent a reply SMS or RCS matching a given keyword category. This is attributed to the most recent campaign received by all users with this phone number. The campaign must have been received in the last four hours.
- The user last selected any shortened link in an SMS or RCS message that has user click tracking turned on, from a given campaign.

Filter Category: Retargeting

Clicked/Opened Campaign or Canvas With Tag 
Filter by interaction with a specific campaign that has a specific tag. For in-app messages, clicked in-app messages include body and button clicks. It does not count dismiss actions or closing the message with the X.

For emails, the open event includes both machine opens and non-machine opens. This filter also includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)". If multiple users share the same email address:
- When the email is opened or clicked, all other users with that same email address also have their profiles updated. 
- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.

For SMS and RCS, an interaction is defined as:
- The user last sent a reply SMS or RCS matching a given keyword category. This is attributed to the most recent campaign received by all users with this phone number. The campaign must have been received in the last four hours.
- When the user last selected any shortened link in an SMS or RCS message that has user click tracking turned on, from a given campaign or Canvas step with tag.

Filter Category: Retargeting

Clicked/Opened Step 
Filter by interaction with a specific Canvas component. For in-app messages, clicked in-app messages also count body and button clicks. It does not count dismiss actions or closing the message with the X.

For emails, the open event includes both machine opens and non-machine opens. This filter also includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)".

For SMS and RCS, an interaction is defined as:
- The user last sent a reply SMS or RCS matching a given keyword category. This is attributed to the most recent campaign received by all users with this phone number. The campaign must have been received in the last four hours. 
- The user last selected any shortened link in an SMS or RCS message that has user click tracking turned on, from a given Canvas step.

Filter Category: Retargeting

Connected Facebook 
Segments your users by whether they connected your app to Facebook.

Filter Category: Social activity

Connected Twitter 
Segments your users by whether they connected your app to X (formerly Twitter).

Filter Category: Social activity

Converted From Campaign 
Segments your users by whether they have converted on a specific campaign. This filter doesn't include users that are in the control group.

Filter Category: Retargeting

Converted From Canvas 
Segments your users by whether they have converted on a specific Canvas. This filter doesn't include users that are in the control group.

Filter Category: Retargeting

Country 
Segments your users by their last indicated country location.

Filter Category: Demographic attributes

Created At 
Segments users by when their user profile was created. If a user was added by CSV or API, then this filter reflects the date they were added. If the user isn't added by CSV or API and has their first session tracked by the SDK, then this filter reflects the date of that first session. Maximum lookback period is 100 years.

Filter Category: Other Filters

Created From 
Segments users by where their user profile was created.

The following values are supported:
- SDK (sdk): User profile created through the Braze SDK.
- REST API (rest): User profile created through the Braze REST API.
- Push Token Import (pti): User profile created through push token import.
- CSV (csv): User profile created through CSV import.
- Demo (demo): User profile created through demo data.
- SMS (sms): User profile created through SMS.
- Shopify (shopify): User profile created through Shopify.
- WhatsApp (whats_app): User profile created through WhatsApp.
- Provider Event (provider_event): User profile created through a provider event.
- Provider Sync (provider_sync): User profile created through a provider sync.
- Landing Page (landing_page): User profile created through a landing page.

Filter Category: Other Filters

Custom Attributes 
Determines whether or not a user matches a custom recorded attribute value. Maximum lookback period is 100 years for date and time interval comparisons.

Time zone:
Company's Time Zone

Filter Category: Custom attribute

Custom Event 
Determines whether or not a user has performed a specially recorded event.

 Example:
Activity completed with property activity_name.

Time zone:
UTC - Calendar Day = 1 calendar day looks at 24-48 hours of user history

Filter Category: Custom events

Customer lifetime value (last 730 days) 
Segments your users by the total revenue a user is expected to generate over their purchasing history with your brand. The calculation considers the last 730 days and takes the Average Order Value (AOV), multiplies it by the total number of orders placed, and then factors in the user's active purchasing duration (the time span between their first and their most recent order). This filter uses data tracked in eCommerce recommended events (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Day of Recurring Event 
This filter looks at the month and day of custom attribute with the data type of "date", but does not look at the year. This filter is useful for annual events.

Time zone:
This filter adjusts for whatever time zones the user is in, so long as the message sends using the local time scheduling option; otherwise, this filter uses your company time zone.

Filter Category: Custom attribute

Device Carrier 
Segments your users by their device carrier.

Filter Category: Devices

Device Count 
Segments your users by how many devices they have used your app on.

Filter Category: Devices

Device Google Ad ID 
Segments your users by the Google ad ID.

Filter Category: Advertising use cases

Device IDFA 
Allows you to designate your campaign recipients by IDFA for testing.

Filter Category: Advertising use cases

Device IDFV 
Allows you to designate your campaign recipients by IDFV for testing.

Filter Category: Advertising use cases

Device Model 
Segments your users by their mobile phone's model version.

Filter Category: Devices

Device OS 
Segments your users that have one or more devices with the specified operating system. To segment users by a range of operating systems, use the Device OS Version Number filter.

Filter Category: Devices

Device OS Version Number 
Segments your users that have one or more devices with an operating system version that is within a specified range. For example, you can target users who have an iOS operating system version that is greater than or equal to 26.0.

Filter Category: Devices

Device Roku Ad ID 
Segments your users by the Roku ad ID.

Filter Category: Advertising use cases

Device Windows Ad ID 
Segments your users by the Windows ad ID.

Filter Category: Advertising use cases

Email Address 
Allows you to designate your campaign recipients by individual email addresses for testing. This can also be used to send transactional emails to all your users (including unsubscribed) using the "Email Address is not Blank" specifier within the filter, so that you can maximize delivery of emails regardless of opt-in status. 

This filter only checks if user profiles have an email address, whereas the Email Available filter checks for additional criteria.

Filter Category: Other Filters

Email Available 
Segments your users by whether they have a valid email address and whether they are subscribed or opted in to email. This filter checks for three criteria: if the user is unsubscribed from emails, if Braze has received a hard bounce, and if the email was marked as spam. If any of these criteria are met, or if an email doesn't exist for a user, the user is not included.

Users whose Email Available is false are excluded from the campaign audience and do not receive the email—even if your send settings are configured to send to all users (including unsubscribed users).

For emails where opt-in status matters, use Email Available instead of Email Address. The additional criteria help you target users who are eligible to receive email.

Filter Category: Channel subscription behavior

Email Opt In Date 
Segments your users by the date on which they opted into email. Maximum lookback period is 100 years.

Filter Category: Channel subscription behavior

Email Subscription Status 
Segments your users by their subscription status for email.

Filter Category: Channel subscription behavior

Email Unsubscribed Date 
Segments your users by the date on which they unsubscribed from future emails. Maximum lookback period is 100 years.

Filter Category: Channel subscription behavior

Entered Canvas Variation 
Segments your users by whether they have entered a variation path of a specific Canvas. This filter evaluates all users.

For example, if you filter for users who have not entered a Canvas variation control group, you receive all users who are not in the control group regardless if they entered the Canvas.

Filter Category: Retargeting

Event Likelihood Category 
Segments your users by likelihood of performing an event according to a specific prediction.

Filter Category: Intelligence and predictive

Event Likelihood Score 
Segments your users by likelihood of performing an event according to a specific prediction.

Filter Category: Intelligence and predictive

External User ID 
Allows you to designate your campaign recipients by individual user IDs for testing.

Filter Category: Other Filters

Feature Flags 
The segment of your users that have a particular feature flag currently enabled.

Filter Category: Retargeting

First Did Custom Event 
Determines the earliest time that a user has performed a specially recorded event. Maximum lookback period is 100 years. (24-hour period) 

Example:
 First Abandoned Cart Less than 1 day ago

Time zone:
Company's Time Zone

Filter Category: Custom events

First Made Purchase 
Segments your users by the earliest time that a user made a purchase in your app. Maximum lookback period is 100 years.

Filter Category: Purchase behavior

First Name 
Segments your users by their first name, as they indicated from within your app.

Filter Category: Demographic attributes

First Purchase For App 
Segments your users by the earliest time that a user made a purchase from your app. Maximum lookback period is 100 years.

Filter Category: Purchase behavior

First Used App 
Segments your users by the earliest recorded time that they opened your app. This captures the first session they have using a version of your app with the Braze SDK integrated. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Sessions

First Used Specific App 
Segments your users by the earliest recorded time that they opened any of your apps within your workspace. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Sessions

Foreground Push Enabled 
Segments your users who have provisional push authorization or are enabled for foreground push. Specifically, this count includes:
1. iOS users who are provisionally authorized for push. 
2. Users who are foreground push enabled and whose push subscription status is not unsubscribed, for any of your apps. For these users, this count includes only foreground push.

Foreground Push Enabled does not include users who have unsubscribed. 

After segmenting with this filter, you can see a breakdown of who is in that segment for Android, iOS, and web in the bottom panel, called Reachable Users.

Filter Category: Channel subscription behavior

Foreground Push Enabled for App 
Segments by whether users have push enabled for your app on their device. Users who are foreground push enabled for an app. This does not take push subscription status into account. This count includes users who have provisionally authorized foreground and background push tokens.

Filter Category: Channel subscription behavior

Gender 
Segments your users by gender, as they indicated from within your app.

Filter Category: Demographic attributes

Hard Bounced 
Segment your users by whether their email address has hard bounced (such as the email address is invalid). To export users with invalid emails, call the /email/hard_bounces endpoint or build a segment with filters such as email address is not blank, email is not available, and email subscription status is not unsubscribed.

Filter Category: Retargeting

Has App 
Segments by whether a user has ever installed your app. This includes users who currently have your app installed and those that have uninstalled in the past. This generally requires users to open the app (start a session) to be included in this filter. However, there are some exceptions, such as if a user was imported into Braze and manually associated with your app.

Filter Category: App

Has Marked You As Spam 
Segments your users by whether they have marked your messages as spam.

Filter Category: Retargeting

Has Never Received a Message from Campaign or Canvas Step 
Segments your users by whether they have received any campaign or Canvas component.

Filter Category: Retargeting

Heap Cohorts 
Clients who use Heap can supplement their segments by choosing and importing their cohorts in Heap.

Filter Category: Cohort membership

Hightouch Cohorts 
Clients who use Hightouch can supplement their segments by choosing and importing their cohorts in Hightouch.

Filter Category: Cohort membership

In Campaign Control Group 
Segments your users by whether they were in the control group for a specific multivariate campaign.

Filter Category: Retargeting

In Canvas Control Group 
Segments your users by whether they were in the control group for a specific Canvas. This filter only evaluates users who have entered the Canvas, so users who never entered are excluded from results entirely.

For example, if you filter for users who are not in the control group for a Canvas, you receive only users who entered the Canvas and were assigned to a non-control variant—users who never entered the Canvas are not included. To include all users regardless of Canvas entry, use the Entered Canvas Variation filter instead.

Filter Category: Retargeting

Install Attribution Ad 
Segments your users by the ad that their install was attributed to.

Filter Category: User Attributes

Install Attribution Adgroup 
Segments your users by the ad group that their install was attributed to.

Filter Category: Install attribution

Install Attribution Campaign 
Segments your users by the ad campaign that their install was attributed to.

Filter Category: Install attribution

Install Attribution Source 
Segments your users by the source that their install was attributed to.

Filter Category: Install attribution

Intelligent Channel 
Segment your users by their most active channel in the last three months.

Filter Category: Intelligence and predictive

Invalid Phone Number 
Segments your users by whether their phone number is invalid.

Filter Category: Retargeting

Kubit Cohorts 
Clients who use Kubit can supplement their segments by choosing and importing their cohorts in Kubit.

Filter Category: Cohort membership

Language 
Segments your users by their preferred language.

Filter Category: Demographic attributes

Last Did Custom Event 
Determines the latest time that a user has performed a specially recorded event. This filter supports decimals, such as 0.25 hours. Maximum lookback period is 100 years. (24-hour period) 

Example:
 Last Abandoned Cart Less than 1 day ago

Time zone:
Company's Time Zone

Filter Category: Custom events

Last Engaged With Message 
Segments your users by the last time they have clicked or opened one of your messaging channels (Banners, Content Card, email, in-app, SMS, RCS, push, WhatsApp).

For Content Cards, Banners, and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.

 For push and webhooks, this is when the message is sent to the user.

 For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device.

 For email messaging, the open event includes both machine opens and non-machine opens. Maximum lookback period is 100 years. (24-hour period)

For emails, the targeted user profile matches this filter when an email request is sent to the email service provider (regardless if it actually gets delivered). This also includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)".

 For SMS and RCS, this is when the user last selected any shortened link in a message that has user click tracking turned on.

 When a message is delivered, opened, or clicked, Braze updates data for all profiles that share the same channel identifier (for example, email or phone number), so users who share an identifier with someone who received the message can match this filter even if their profile was not directly sent the campaign.

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last Enrolled in Any Control Group 
Segments your users by the last time that they fell into the control group in a campaign. Maximum lookback period is 100 years. 

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last In App Message Impression 
Segments your users by the last time they viewed an in-app message. Maximum lookback period is 100 years.

Filter Category: Retargeting

Last Made Purchase 
Filter users by the last time they made a purchase. Maximum lookback period is 100 years.

Filter Category: Purchase behavior

Last Name 
Segments your users by their last name, as they indicated from within your app.

Filter Category: Demographic attributes

Last Purchased Product 
Filter users by when they last purchased a specific product. Maximum lookback period is 100 years.

Filter Category: Purchase behavior

Last Received Any Message 
Segments your users by determining the last message that was received. Maximum lookback period is 100 years. (24-hour period)

For Content Cards, Banners, and in-app messages, this is when a user last logged an impression, not when the card or in-app message was last sent.

For push and webhooks, this is when any message was sent to the user.

 For WhatsApp, this is when the last message API request was sent to WhatsApp, not when the message was delivered to the user's device.

 For emails, the targeted user profile matches this filter when an email request is sent to the email service provider (regardless if it actually gets delivered).

 For SMS and RCS, users are considered to have "received" a message at send time. Even if the message fails to reach the user's device, the user still matches this filter.

 When a message is delivered, opened, or clicked, Braze updates data for all profiles that share the same channel identifier (for example, email or phone number), so users who share an identifier with someone who received the message can match this filter even if their profile was not directly sent the campaign.

Example:
Last Received Message Less than 1 Day ago = less than 24 hours ago

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last Received Email 
Segments your users by the last time that they have received one of your email messages. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last Received Message from Campaign or Canvas With Tag 
Segments your users by when they received a specific campaign or Canvas with a specific tag. This filter doesn't consider when users received other campaigns or Canvases. Maximum lookback period is 100 years. (24-hour period)

Filter Category: Retargeting

Last Received Message from Specific Campaign 
Segments your users by whether they have received a specific campaign. Maximum lookback period is 100 years.

 Because data is updated for all profiles that share the same channel identifier (for example, email or phone) when a delivery, open, or click occurs, a user who shares an identifier with someone who received a message may not match this filter even if they were never explicitly sent the message.

 This filter doesn't consider when users received other campaigns.

Filter Category: Retargeting

Last Received Message from Specific Canvas Step 
Segments your users by when they received a specific Canvas component. Maximum lookback period is 100 years.

 Because data is updated for all profiles that share the same channel identifier (for example, email or phone) when a delivery, open, or click occurs, a user who shares an identifier with someone who received a message may not match this filter even if they were never explicitly sent the message. Use "Entered Canvas Variation" to isolate user profiles from duplicates.

 This filter doesn't consider when users received other Canvas components.

Filter Category: Retargeting

Last Received Push 
Segments your users by the last time that they received one of your push notifications. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last Received SMS 
Segments your users by the time that the last SMS, MMS, or RCS message was delivered to the SMS or RCS provider. This doesn't guarantee that the message was delivered to the user's device. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last Received Webhook 
Segments your users by the last time that Braze sent a webhook for that user. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last Received WhatsApp 
Segments your users by the last time that they received a WhatsApp message. This is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Retargeting

Last Sent Specific SMS Inbound Keyword Category 
Segments your users by when they last sent an SMS, MMS, or RCS to a specific subscription group within a specific keyword category. Maximum lookback period is 100 years.

Filter Category: Retargeting

Last Used App 
Segments your users by the most recent time that they have opened your app. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Sessions

Last Used Specific App 
Segments your users by the most recent time that they have opened a specific, designated app. Maximum lookback period is 100 years. (24-hour period)

Time zone:
Company's Time Zone

Filter Category: Sessions

Last order placed (last 730 days) 
Segments your users by when they last placed an order, which is based on the eCommerce recommended event for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day, and the maximum lookback window is the last 2 years.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Live Activities Push to Start Registered for App 
Segments your users by whether they are registered to start a Live Activity through iOS push notifications for a specific app.

Filter Category: Devices

Location Available 
Segments your users by whether they have reported their locations. In order to use this filter, your app needs to have location tracking integrated.

Filter Category: Location

Median Session Duration 
Segments your users by the median length of their sessions in your app.

Filter Category: Sessions

Message Open Likelihood 
Filters your users based on their likelihood to open a message on a specified channel on a scale of 0-100%. Users without sufficient data to measure a likelihood for a channel can be selected using "is blank."

For email, machine opens are excluded from the likelihood calculation.

Filter Category: Intelligence and predictive

Mixpanel Cohorts 
Clients who use Mixpanel can supplement their segments by choosing and importing their cohorts in Mixpanel.

Filter Category: Cohort membership

Money Spent 
Segments your users by the amount of money that they have spent in your app.

Filter Category: Purchase behavior

Most Recent App Version Name 
Segments by the recent name of the user's app.

When using "less than" or "less than or equal to", if the main app version doesn't exist, this filter returns `true` because the user is older than the app version. This means that if the user’s last main app version doesn't exist, they automatically match the filter.

Filter Category: App

Most Recent App Version Number 
Segments by the most recent app version number of the user's app. The version number inside the parentheses is used for filtering, while the number preceding it is for reference—for example, in "3.7.0(134.0.0.0)", "134.0.0.0" is the filtered version number.

When using “less than” or “less than or equal to”, if the main app version doesn't exist, this filter returns `true` because the user is older than the app version. This means that if the user’s last main app version doesn't exist, they automatically match the filter.

It may take time for the current app versions to populate. The app version on the user profile updates when the information is captured by the SDK, which relies on when users open their apps. If the user doesn't open the app, the current version won't be updated. These filters also won't apply retroactively. It's good to use "greater than" or "equal" to current and future versions, but using past version filters may cause unexpected behaviors.

Filter Category: App

Most Recent Device Locale 
Segments your users by the locale information from the most recently used device.

Filter Category: Devices

Most Recent Location 
Segments your users by the last recorded location at which they have used your app.

Filter Category: Location

Most Recent Watch Model 
Segments your users by their most recent smartwatch model.

Filter Category: Devices

Nested Custom Attributes 
Attributes that are the properties of custom attributes.

When filtering a nested time custom attribute, you can choose to filter based on "Day of Year" or "Time". "Day of Year" checks only the month and day for comparison. "Time" compares the full timestamp, including the year. Maximum lookback period is 100 years for time interval comparisons. The same logic applies when filtering on context variables in Canvas Audience Paths; see Day of Year and Time filters for date context variables for details.

Filter Category: Custom attribute

Number of Facebook Friends Using App 
Segments your users by how many Facebook friends they have who use the same app.

Filter Category: Social activity

Number of Twitter Followers 
Segments your users by how many X (formerly Twitter) followers they have.

Filter Category: Social activity

Phone Number 
Segments your users by the E.164 formatted phone number field.

 When a phone number is sent to Braze, Braze tries to coerce it into the e.164 format that is used to send across SMS, RCS, and WhatsApp channels. The coercion process can fail if the number isn't formatted properly, which results in the user profile having an unformatted phone number but not a sending phone number. This segment filter returns users by their e.164 formatted phone number (when available).

Use cases:
 - Use this filter to understand the most accurate target audience size when sending SMS, RCS, or WhatsApp messages. 
- Use regular expressions (regex) with this filter to segment by phone numbers with a specific country code. 
- Use this filter to segment users by phone numbers that failed the e.164 coercion process.

Filter Category: Other Filters

Provisionally Authorized on iOS 
Allows you to find users who are provisionally authorized on iOS 12 for a given app.

Filter Category: Devices

Purchased Product 
Segments your users by products purchased in your app.

Filter Category: Purchase behavior

Push Opt In Date 
Segments your users by the date on which they opted into push. Maximum lookback period is 100 years.

Filter Category: Channel subscription behavior

Push Subscription Status 
Segments your users by their subscription status for push.

Filter Category: Channel subscription behavior

Push Unsubscribed Date 
Segments your users by the date on which they unsubscribed from future push notifications. Maximum lookback period is 100 years.

Filter Category: Channel subscription behavior

Random Bucket # 
Segments your users by a randomly assigned number (0 to 9999 inclusive). It can enable the creation of uniformly distributed segments of truly random users for A/B and multivariate testing.

Filter Category: Other Filters

Received Campaign Variant 
Segments your users by which variant of a multivariate campaign they have received.

This filter applies to multivariate and multivariate quick push campaigns. API campaigns, standard multichannel campaigns, and feature flag experiment campaigns do not appear in the campaign selector. Webhook-only campaigns do not appear in the campaign selector.

For Content Cards, Banners, and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.

 For push and webhooks, this is when the message is sent to the user.

 For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device.

 For emails, the targeted user profile matches this filter when an email request is sent to the email service provider (regardless if it actually gets delivered).

 For SMS and RCS, users are considered to have "received" a message at send time. Even if the message fails to reach the user's device, the user still matches this filter.

 When a message is delivered, opened, or clicked, Braze updates data for all profiles that share the same channel identifier (for example, email or phone number), so users who share an identifier with someone who received the message can match this filter even if their profile was not directly sent the campaign.

Filter Category: Retargeting

Received Message from Campaign 
Segments your users by whether they have received a specific campaign. 

For Content Cards, Banners, and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.

 For push and webhooks, this is when the message is sent to the user.

 For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device.

 For emails, the targeted user profile matches this filter when an email request is sent to the email service provider (regardless if it actually gets delivered).

 For SMS and RCS, users are considered to have "received" a message at send time. Even if the message fails to reach the user's device, the user still matches this filter.

 When a message is delivered, opened, or clicked, Braze updates data for all profiles that share the same channel identifier (for example, email or phone number), so users who share an identifier with someone who received the message can match this filter even if their profile was not directly sent the campaign.

Filter Category: Retargeting

Received Message from Campaign or Canvas with Tag 
Segments your users by whether they have received a specific campaign or Canvas with a specific tag.

Braze evaluates only the last 200 sent campaigns and Canvases that use the selected tag when this filter runs.

 For Content Cards, Banners (Campaigns only), and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.

 For push and webhooks, this is when the message is sent to the user.

 For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device.

 For emails, the targeted user profile matches this filter when an email request is sent to the email service provider (regardless if it actually gets delivered).

 For SMS and RCS, users are considered to have "received" a message at send time. Even if the message fails to reach the user's device, the user still matches this filter.

 When a message is delivered, opened, or clicked, Braze updates data for all profiles that share the same channel identifier (for example, email or phone number), so users who share an identifier with someone who received the message can match this filter even if their profile was not directly sent the campaign.

Filter Category: Retargeting

Received Message from Canvas Step 
Segments your users by whether they have received a specific Canvas component.

For Content Cards and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.

 For push and webhooks, this is when the message is sent to the user.

 For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device.

 For emails, the targeted user profile matches this filter when an email request is sent to the email service provider (regardless if it actually gets delivered).

 For SMS and RCS, users are considered to have "received" a message at send time. Even if the message fails to reach the user's device, the user still matches this filter.

 When a message is delivered, opened, or clicked, Braze updates data for all profiles that share the same channel identifier (for example, email or phone number), so users who share an identifier with someone who received the message can match this filter even if their profile was not directly sent the campaign.

Filter Category: Retargeting

Segment Cohorts 
Clients who use Segment can supplement their segments by choosing and importing their cohorts in Segment.

Filter Category: Cohort membership

Segment Membership 
Allows you to filter based on segment membership anywhere that filters are used (such as segments, campaigns, and others) and target multiple different segments within one campaign. 

To capture segment membership at a specific point in time, export users from the segment in the dashboard or call the /users/export/segment endpoint before you send a campaign or Canvas. Braze does not store per-user segmentation history, so you cannot retroactively check whether a user was in a segment at a past time. For more information, see Export segment data to CSV.

Note that segments already using this filter cannot be further included or nested into other segments because this may create a cycle where Segment A includes Segment B, which then tries to include Segment A again. If that happened, the segment would keep referencing itself, making it impossible to calculate who actually belongs in it. Also, nesting segments like this adds complexity and can slow things down. Instead, recreate the segment you're trying to include using the same filters.

If a segment does not appear in the **Segment Membership** filter dropdown, recreate it with the same filters and select the new segment, or confirm it does not already depend on this audience in a way that would create a cycle.

Filter Category: Segment or CSV membership

Session Count 
Segments your users by the number of sessions they have had in any of your apps within your workspace.

Filter Category: Sessions

Session Count For App 
Segments your users by the number of sessions they have had in a specific, designated app.

Filter Category: Sessions

Soft Bounced 
Segment your users by whether they soft bounced X times in Y days. Segment filters can only look back 30 days, but you can look back further with Segment Extensions.

This filter operates differently than a soft bounce event in Currents. The Soft Bounced segment filter counts a soft bounce if there was no successful delivery during the 72 hour retry period. In Currents, every unsuccessful retry is sent as a soft bounce event.

Filter Category: Retargeting

Subscription Group 
Segments your users by their subscription group for email, SMS, MMS, RCS, or WhatsApp. Archived Groups do not appear and cannot be used.

Filter Category: Channel subscription behavior

Tinyclues Cohorts 
Clients who use Tinyclues can supplement their segments by choosing and importing their cohorts in Tinyclues.

Filter Category: Cohort membership

Total Number of Purchases 
Segments your users by how many purchases they have made in your app.

Filter Category: Purchase behavior

Total canceled orders count (last 730 days) 
Segments your users by the total count of orders a user canceled within the last 2 years, based on the eCommerce recommended event for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Total orders count 
Segments your users by the total count of a user's orders across their lifetime, based on the eCommerce recommended event for order placed (workspaces not tracking eCommerce events do not have data for this filter). This count excludes canceled orders, which must be tracked using the eCommerce recommended event for order canceled. Users are evaluated for this filter in real time.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Total orders count (last 730 days) 
Segments your users by the total count of a user's orders within the last 2 years, based on the eCommerce recommended event for order placed (workspaces not tracking eCommerce events do not have data for this filter). This count excludes canceled orders, which must be tracked using the eCommerce recommended event for order canceled. Users are evaluated for this filter once per day.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Total refund value 
Segments your users by the total value of refunds granted to a user across their lifetime, based on the eCommerce recommended event for order refunded (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter in real time.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Total refund value (last 730 days) 
Segments your users by the value of refunds granted to a user over the last 2 years, based on the eCommerce recommended event for order refunded (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Total revenue 
Segments your users by the total revenue generated from a user's orders across the user's lifetime, calculated based on subtracting the revenue associated with the eCommerce recommended event for order refunded from the revenue associated with the eCommerce event for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter in real time.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Total revenue (last 730 days) 
Segments your users by the total revenue generated from a user's orders over the last 2 years, calculated based on subtracting the revenue associated with the eCommerce recommended event for order refunded from the revenue associated with the eCommerce event for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.

This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.

Filter Category: eCommerce

Unformatted Phone Number 
Segments your users by their unformatted phone number. Does not include parenthesis, dashes, or other symbols.

Filter Category: Demographic attributes

Uninstalled 
Segments your users by whether they are currently marked as uninstalled on the backend. Users who uninstalled and later reinstalled the app are not included. This filter reflects the current uninstall state, not a historical log of every uninstall event. Maximum lookback period is 100 years.

Filter Category: Uninstall

Updated/Imported from CSV 
Segments your users based on whether they were a part of a CSV upload or not. Braze retains only the most recent 100 CSV imports per user profile for segmentation purposes. If a user appears in more than 100 CSV imports that were selected for retargeting, only the 100 most recent are available for this filter. Older imports no longer match that user.

Filter Category: Segment or CSV membership

Web Browser 
Segments your users by the web browser they use to access your website. This filter matches against any browser in the user's device history, not only the most recently used browser.

Filter Category: Devices

X Custom Event In Y Days 
Determines whether or not a user has performed a specially recorded event between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day looks at 24-48 hours of user history)
 Learn more about X-in-Y behavior here. 

Example:
Abandoned Cart exactly 0 times in the last 1 calendar day

Time zone:
UTC - To account for all time zones, 1 calendar day looks at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, looks at 48-72 hours of user history, and so on.

Filter Category: Custom events

X Custom Event Property In Y Days 
Determines whether or not a user has performed a specially recorded event in relation to a specific property between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day looks at 24-48 hours of user history)
Learn more about X-in-Y behavior here. 

Example:
 Added to Favorites w/ property "event_name" exactly 0 times in the last 1 calendar day

Time zone:
UTC - To account for all time zones, 1 calendar day looks at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, looks at 48-72 hours of user history, and so on.

Filter Category: Custom events

X Money Spent in Y Days 
Segments your users by the amount of money that they have spent in your app in the last specified number of calendar days between 1 and 30. This amount includes only the sum of the last 50 purchases. 
 Learn more about X-in-Y behavior here.

Filter Category: Purchase behavior

X Product Purchased In Y Days 
Filter users by times a specific product was purchased.

Filter Category: Purchase behavior

X Purchase Property In Y Days 
Segments your users by the number of times a purchase was made in relation to a certain purchase property in the last specified number of calendar days between 1 and 30. 
 Learn more about X-in-Y behavior here.

Filter Category: Purchase behavior

X Purchases in Last Y Days 
Segments your users by the number of times (between 0 and 50) they have made a purchase in the last specified number of calendar days between 1 and 30. 
 Learn more about X-in-Y behavior here.

Filter Category: Purchase behavior

X Sessions In Last Y Days 
Segments your users by the number of sessions (between 0 and 50) they have had in your app in the last specified number of calendar days between 1 and 30. 
 Learn more about X-in-Y behavior here.

Filter Category: Sessions

- 

New Stuff!
