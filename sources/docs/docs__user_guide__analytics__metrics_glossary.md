---
url: https://www.braze.com/docs/user_guide/analytics/metrics_glossary
slug: docs__user_guide__analytics__metrics_glossary
title: "Metrics Glossary"
description: "This glossary defines terms you'll find in your reports in your Braze account."
section: user_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Metrics Glossary

These are terms you'll find in your reports in your Braze account. Search for the metrics you need or filter by channel. This glossary does not necessarily include metrics you might see in Currents or other downloaded reports outside of your Braze account.

 Search glossary
 
 Results update automatically as you type.
 
 Filter by channel

## AMP Clicks

AMP Clicks is the total number of clicks in your AMP HTML email, cumulative of the HTML, plaintext, and AMP HTML versions of the email.

## AMP Opens

AMP Opens is the total count for opens in your AMP HTML email and AMP HTML versions of the email.

## Audience

Audience is the percentage of users who received a particular message. This number is received from Braze.

Calculation: (Number of Recipients in Variant) / (Unique Recipients)

## Bounces

Bounces is the total number of messages that were unsuccessfully delivered to the intended recipients.

This could occur because there isn’t a valid push token, the user unsubscribed after the campaign was launched, or the email address is inaccurate or deactivated.

 Channel | 
 Additional information | 

 Email | 
 An email bounce for customers using SendGrid consists of hard bounces, spam (spam_report_drops), and emails sent to invalid addresses (invalid_emails).

For email, Bounce % or Bounce Rate is the percentage of messages that were unsuccessfully sent or designated as “returned” or “not received” from send services used or not received by the intended emailable users. | 

 Push | 
 These users have been automatically unsubscribed from all future push notifications. | 

 Calculation:

- Bounces: Count
 
- Bounce % or Bounce Rate %: (Bounces) / (Sends)

## Body Click

Push Story Notifications record a Body Click when the notification is clicked. It will not be recorded when a message is expanded, or for action button clicks.

Calculation: (Body Clicks) / (Impressions)

## Body Clicks

Body Clicks occur when a user clicks on a message that doesn’t have buttons (Button 1, Button 2) and was created with the traditional editor, and when a message created with the HTML editor or drag-and-drop editor uses brazeBridge.logClick() with no arguments.

Calculation: (Body Clicks) / (Impressions)

## Button 1 Clicks

Button 1 Clicks is the total number of clicks on Button 1 of the message.

Reporting for Button 1 Clicks only works when you specify the Identifier for Reporting as “0” in the in-app message.

Calculation: (Button 1 Clicks) / (Impressions)

## Button 2 Clicks

Button 2 Clicks is the total number of clicks on Button 2 of the message.

Reporting for Button 2 Clicks only works when you specify the Identifier for Reporting as “1” in the in-app message.

Calculation: (Button 2 Clicks) / (Impressions)

## Campaign analytics

The performance of the message across various channels. The metrics shown depend on the selected messaging channel, and whether the Feature Flag experiment is a multivariate test.

## Choices Submitted

Choices Submitted is the total number of choices selected when the user clicks the submit button on the survey question page of a simple survey.

## Click-to-Open Rate

Click-to-Open Rate is the percentage of opened emails that have been clicked by a single user or machine at least once, and is only available in the Report Builder.

Calculation: (Unique Clicks) / (Unique Opens) (for Email)

## RCS Confirmed Deliveries or SMS Confirmed Deliveries

Confirmed Deliveries are when the carrier has confirmed the message was delivered to the target phone number.

As a Braze customer, deliveries are charged toward your SMS allotment.

 Calculation:

- Confirmed Deliveries: Count
 
- Confirmed Delivery Rate: (Confirmed Deliveries) / (Sends)

## Confidence

Confidence is the percentage of confidence that a certain variant of a message is outperforming the control group.

## Confirmation Page Button

Confirmation Page Button is the total clicks on the call to action button on the confirmation page of a simple survey.

## Confirmation Page Dismissals

Confirmation Page Dismissals is the total clicks on the close (x) button on the confirmation page of a simple survey.

## Conversions (B, C, D)

Conversions (B, C, D) are additional conversion events added after the primary conversion event. This is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign.

This defined event is determined by you when building the campaign.

 Channel | 
 Additional information | 

 Email, Push, Webhooks | 
 Conversions are tracked after the initial send. | 

 Content Cards | 
 Conversions are counted when the user views a Content Card for the first time. | 

 In-app messages | 
 A conversion is counted if the user has received and viewed the in-app message campaign, and subsequently performs the specific conversion event within the defined conversion window, regardless of whether they clicked on the message or not.

Conversions are attributed to the most recently received message. If re-eligibility is enabled, the conversion will be assigned to the latest in-app message received, provided that it occurs within the defined conversion window. However, if the in-app message has already been assigned a conversion, then the new conversion cannot be logged for that specific message. This means that each in-app message delivery is associated with only one conversion. | 

## Total Conversions

Total Conversions is the total number of times a user completes a specific conversion event after viewing an in-app message campaign.

When a user views an in-app message campaign only once, only one conversion is counted, even if they perform the conversion event multiple times later on. However, if re-eligibility is turned on and the user sees the in-app message campaign multiple times, Total Conversions can increase once for each time the user logs an impression for a new instance of the in-app message campaign.

For example, if a user triggers an in-app message twice and converts after each in-app message impression (resulting in two conversions), then Total Conversions will increase by two. However, if there was only one in-app message impression followed by two conversion events, only one conversion will be logged, and Total Conversions will increase by one.

## Close Message

Close Message is the total number of clicks on the close button of the message. This only exists for in-app messages created in the drag-and-drop editor, not the traditional editor.

## Conversion Rate

Conversion Rate is the percentage of times a defined event occurred compared to all recipients of a message. This defined event is determined when you build the campaign.

 Channel | 
 Additional information | 

 In-app messages | 
 The metric of total daily Unique Impressions is used to calculate the Conversion Rate for in-app messages.

Unique Impressions for in-app messages can only be counted once per calendar day in your workspace’s time zone. The number of times a user completes a desired action (a “conversion”) can increase within that same calendar day. While conversions can happen more than once per day, Unique Impressions cannot. Therefore, if a user completes a conversion multiple times within a day, the Conversion Rate can increase accordingly, but Unique Impressions are only counted once for that calendar day. For more details, refer to In-app message reporting. | 

 Calculation:

- In-App Messages: (Primary Conversions) / (Unique Impressions)
 
- Other Channels: (Primary Conversions) / (Unique Recipients)

## Conversion Window

Conversion Window is the number of days after receiving the message during which user actions are tracked and attributed to a conversion event. Conversions that occur after this window are not attributed to the conversion event.

## Deliveries

Deliveries is the total number (or percentage) of message requests that are accepted by the receiving server. This doesn’t mean the message was delivered to a device, only that the message was accepted by the server.

 Channel | 
 Additional information | 

 Email | 
 Refers to the total number of messages (Sends) successfully sent to and received by emailable parties. | 

 Calculation:

- Deliveries: Count
 
- Deliveries %: (Sends - Bounces) / (Sends)

## RCS Delivery Failures or SMS Delivery Failures

Delivery Failures are when the SMS couldn’t be sent because of queues overflowing (sending SMS at a rate higher than your long or short codes can handle).

Contact Braze Support for assistance in understanding the reasons for delivery failures.

Calculation: (Sends) - (Sends to Carrier)

## Delivery Failures

Delivery Failures are when the RCS couldn’t be sent because of queues overflowing (sending RCS at a rate higher than your RCS-verified sender can handle).

Contact Braze Support for assistance in understanding the reasons for delivery failures.

Calculation: (Sends) - (Sends to Carrier)

## Failed Delivery Rate

The Failed Delivery Rate is the percentage of sends that failed because the message could not be sent. This can happen for various reasons, including queue overflows, account suspensions, and media errors in the case of MMS.

Contact Braze Support for assistance in understanding the reasons for delivery failures.

Calculation: (Delivery Failures) / (Sends)

## Direct Opens

Direct Opens is the total number (or percentage) of users who opened your app or website by directly pressing the notification.

Calculation: (Direct Opens) / (Deliveries)

## Emailable

Emailable is the total number of users who have an email address on record and have explicitly opted in or subscribed.

Calculation: Count

## Errors

Errors is the number of errors returned by webhook events (incremented during the sending process).

Errors are included in the Sends count but are not included in the Unique Recipients count.

## Estimated Real Opens

Estimated Real Opens is an estimate of how many unique opens there would be if machine opens did not exist, and is the result of a proprietary Braze statistical model.

## Failures

Failures are when the WhatsApp message couldn’t send because the internet service provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure.

Failures are included in the Sends count but not in the Deliveries count.</td>

Calculation (Failure Rate): (Failures) / (Sends)

## Feature flag experiment performance

Performance metrics for the message in a Feature Flag experiment. The specific metrics shown will vary depending on the messaging channel, and whether or not the experiment was a multivariate test.

## Hard Bounce

A Hard Bounce is when an email fails to deliver to the recipient due to a permanent delivery error. A hard bounce might occur because the domain name doesn’t exist or because the recipient is unknown.

When this occurs, Braze marks the email address as invalid but does not update the user’s subscription status. If an email receives a hard bounce, Braze stops any future requests to this email address.

## Help

Help is when a user replied to your message with a HELP keyword and was dispatched a HELP auto-response.

A user reply is measured anytime a user sends an inbound message within four hours of receiving your message.

## Influenced Opens

Influenced Opens is the total number (or percentage) of users who opened the app after the push notification was sent, without directly opening the push.

Calculation: (Influenced Opens) / (Deliveries)

## Lifetime Revenue

Lifetime Revenue is the total PurchaseEvents price value (in USD) received since inception.

## Lifetime Value Per User

Lifetime Value Per User is the Lifetime revenue divided by your total Users (located on your home page).

## Average Daily Revenue

Average Daily Revenue is the average of the sum of the campaign and Canvas revenue for a given day.

## Daily Purchases

Daily Purchases is the average of the total unique PurchaseEvents over the time period.

## Daily Revenue Per User

Daily Revenue Per User is the average daily revenue per daily active user.

## Machine Opens

Machine Opens includes both non-human and human opens that indicate an open by an Apple Mail Privacy Protection (MPP)-enabled user. This means that a user can log multiple Machine Opens. Machine Opens are not automatically generated if the device isn’t connected to Wi-Fi, so a user can potentially open an email in the Apple Mail app before Apple pre-fetches images, which still results in a Machine Opens.

For MPP-enabled users:

- 1+ Machine Open: Apple pre-fetched the message or the user proactively opened an email on an iOS device
 
- 2+ Machine Opens: Braze does not have visibility into human versus non-human opens, so this may be made up of multiple human opens (across one Apple device or multiple) or a combination of human opens and 1 open associated with Apple pre-fetching the message

This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost. For Amazon SES, analytics will show up as Opens. However, bot filtering for clicks will be supported.

## Opens

Opens are instances including both Direct Opens and Influenced Opens in which the Braze SDK has determined, using a proprietary algorithm, that a push notification has caused a user to open the app.

## Opt-Out

Opt-Out is when a user replied to your message with an opt-out keyword and was unsubscribed from your SMS or RCS program.

A user reply is measured anytime a user sends an inbound message within four hours of receiving your message.

## Other Opens

Other Opens includes human opens that are not impacted by MPP (such as a user opening an email in the Gmail app or on Gmail desktop, which subsequently fires a tracking pixel and logs a regular open). Other Opens are typically human opens, but there could also be scenarios where a machine opens the mail (a bot or an inbox service provider like Gmail or Yahoo). It is also possible for a user to open an email on a non-iOS device and log the Other Open before a Machine Open is logged.

Because Machine Opens can be user-driven, the relationship between Machine Opens and Other Opens is not human versus non-human, but rather, MPP-impacted versus not MPP-impacted. While Other Opens can still be relied on to measure some portion of human opens, it’s not currently possible to determine the percentage of Machine Opens that are human-driven, so determining a precise “true” open rate is not currently possible.

For MPP-enabled users:

- +1 Other Open(s): The user proactively opened an email on a non-iOS device
 
- +1 Machine Open(s) and +1 Other Opens: Apple pre-fetched the message or the user proactively opened an email on an iOS device and proactively opened an email on a non-iOS device

For non-MPP-enabled users:

- +1 Other Open(s): The user proactively opened an email on any device

Note that a user can also open an email (such as the open counts toward Other Opens) before a Machine Opens count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward Other Opens and only once toward Unique Opens.

## Pending Retry

Pending Retry is the number of requests that were temporarily rejected, by the receiving server, but still attempted for re-delivery by the email service provider (ESP). The ESP will retry delivery until a timeout period is reached (typically after 72 hours).

## Primary Conversions (A) or Primary Conversion Event

Primary Conversions (A) or Primary Conversion Event is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by you when building the campaign.

 Channel | 
 Additional information | 

 Email, Push, Webhooks | 
 After the initial send. | 

 Content Cards, In-app messages | 
 When the user views the Content Card or message for the first time. | 

 Calculation:

- Primary Conversions (A) or Primary Conversion Event: Count
 
- Primary Conversions (A) % or Primary Conversion Event Rate: (Primary Conversions) / (Unique Recipients)

## Reads

Reads is when the user reads the message. The user’s read receipts must be “On” for Braze to track reads.

## Read Rate

Read Rate is the percentage of sends that resulted in a read. This is only given for users who have read receipts turned on.

Calculation: (Reads with read receipts) / (Sends)

## Received

Received is defined differently per channel, and can be when users view the message, users perform a defined trigger action, or the message is sent to the message provider.

 Channel | 
 Additional information | 

 Content Cards | 
 Received when users view the card in the app. | 

 Push | 
 Received when messages are sent from the Braze server to the push provider. | 

 Email | 
 Received when messages are sent from the Braze server to the email service provider. | 

 SMS/MMS | 
 “Delivered” after the SMS provider receives confirmation from the upstream carrier and destination device. | 

 In-app message | 
 Received at the time of display based on the trigger action defined. | 

 WhatsApp | 
 Received at the time of display based on the trigger action defined. | 

## RCS Rejections or SMS Rejections

Rejections are when the SMS or RCS has been rejected by the carrier. This can happen for several reasons, including carrier content filtering, availability of the destination device, the phone number is no longer in service, and similar.

As a Braze customer, rejections are charged toward your SMS allotment.

 Calculation:

- Rejections: Count
 
- Rejection Rate: (Rejections) / (Sends)

## Revenue

Revenue is the total revenue in dollars from campaign recipients within the set primary conversion window.

## Sent

Sent is every time a campaign or Canvas step has been launched or triggered, and an SMS or RCS has been sent from Braze. It’s possible that the SMS or RCS didn’t reach a user’s device due to errors.

Calculation: Count

## Sends

Sends is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent.

This metric is provided by Braze. Note that upon launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting.

tip

For Content Cards, this metric is calculated differently depending on what you selected for Card creation:

- At launch or step entry: The number of cards created and available to be seen. This doesn’t count whether the users viewed the card.
 
- At first impression: The number of cards displayed to users.

Calculation: Count

## Messages Sent

Messages Sent is the total number of messages sent in a campaign. After launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting. This doesn’t mean the message was received or delivered to a device, only that the message was sent.

This metric is provided by Braze. Note that upon launching a scheduled campaign, this metric will include all messages sent, regardless of whether they have been sent out yet due to rate limiting.

tip

For Content Cards, this metric is calculated differently depending on what you selected for Card creation:

- At launch or step entry: The number of cards created and available to be seen. This doesn’t count whether the users viewed the card.
 
- At first impression: The number of cards displayed to users.

Calculation: Count

## Sends to Carrier

Sends to Carrier is deprecated, but will continue to be supported for users that already have it. It’s the sum of Confirmed Deliveries, Rejections, and Sends where delivery or rejection wasn’t confirmed by the carrier. This includes instances where carriers don’t provide delivery or rejected confirmation, as some carriers don’t provide this confirmation or can’t do so at the time of send.

 Calculation:

- Sends to Carrier: Count
 
- Sends to Carrier Rate: (Sends to Carrier) / (Sends)

## Soft Bounce

A Soft Bounce is when an email fails to deliver to the recipient due to a temporary delivery error, even though the recipient’s email address is valid. A soft bounce might occur because the recipient’s inbox is full, the server was down, or the message was too large for the recipient’s inbox.

If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver.

Note that Soft Bounces differ from Deferrals. If no email is successfully delivered during this retry period, Braze sends one soft bounce event per attempted campaign send. Before February 25, 2025, these retries were counted as multiple soft bounces for one campaign send.

While soft bounces aren’t tracked in your campaign analytics, you can monitor the soft bounces in the Message Activity Log. You can also exclude these users from your sending or look back at the amount of soft bounces from the last 30 days with the Soft Bounced segment filter. In the Message Activity Log, you can also see the reason for the soft bounces and understand possible discrepancies between the “sends” and “deliveries” for your email campaigns.

## Spam

Spam is the total number of emails delivered that were marked as “spam” by the recipient. While Braze doesn’t change the subscription state of these users, these users will be automatically excluded in future emails, unless you’re sending a transactional email, which is configured to “send to all users including unsubscribe”.

note

Spam complaints are handled directly by email service providers and then relayed to Braze through a feedback loop. Most feedback loops only report a portion of the actual complaints, so the Spam metric often represents a fraction of the actual total. Only email service providers can view the true volume of spam complaints, which means Spam should be viewed as an indicative, not exhaustive, metric.

 Calculation:

- Spam: Count
 
- Spam % or Spam Rate %: (Marked as Spam) / (Sends)

## Survey Page Dismissals

Survey Page Dismissals is the total clicks on the close (x) button on the survey question page of a simple survey.

## Survey Submissions

Survey Submissions is the total clicks on the submit button of a simple survey.

## Total Clicks

Total Clicks is the number (or percentage) of unique recipients who clicked on a link in the delivered message.

 Channel | 
 Additional information | 

 LINE | 
 Tracked after a minimum threshold of 20 messages per day has been reached. AMP emails include clicks recorded in both HTML and plaintext versions. This number may be artificially inflated by anti-spam tools. | 

 Banners | 
 The total number (and percentage) of users who clicked within the delivered message, regardless of whether the same user clicks multiple times. | 

 Calculation:

- Email: (Total Clicks) / (Deliveries)
 
- Content Cards: (Total Clicks) / (Total Impressions)
 
- SMS: (Click Opens) / (Deliveries)

## Total Dismissals

Total Dismissals is the number of times users dismissed a message from a campaign. For Content Cards, this counts each card dismissal. For Banners, this counts each time a user dismissed the Banner when dismissal behavior is enabled.

For Content Cards, if a user receives two different cards from the same campaign and dismisses both, this count increases by two. Re-eligibility allows you to increment Total Dismissals once every time a user receives a card; each card is a different message. For Banners, this counts each dismissal when dismissal behavior is enabled.

 Calculation:

- Total Dismissals: Count
 
- Total Dismissal Rate: Total Dismissals / Total Impressions

## Total Impressions

Total Impressions is the number of times a message is viewed. Braze logs an impression only when the message becomes visible to the user on their screen. For example, if a message is placed at the bottom of a page, the impression is not logged until the user scrolls down and the message comes into view. If a user is shown the same message twice, it will count as two impressions.

This number is a sum of the number of impression events that Braze receives from the SDKs.

 Channel | 
 Additional information | 

 Content Cards | 
 The total count of impressions logged for a given Content Card. This can increment multiple times for the same user. | 

 In-app messages | 
 If there are multiple devices and re-eligibility is off, the user should only see the in-app message once. Even if the user uses multiple devices, they will only see it on the first device that is targeted. This assumes that the profile has consolidated devices and a user has one user ID that they are logged into across devices. If re-eligibility is on, an impression is logged for every time that user sees the in-app message. For more details, refer to In-app message reporting. | 

Calculation: Count

## Total Opens

Total Opens is the total number of messages that were opened.

 Channel | 
 Additional information | 

 LINE | 
 Tracked after a minimum threshold of 20 messages per day has been reached. | 

 AMP emails | 
 The total opens for the HTML and plaintext versions. | 

 Calculation:

- Email Total Opens: Count
 
- Email Total Open Rate: (Opens) / (Deliveries)
 
- Web push Total Opens: Direct Opens count
 
- Web push Total Open Rate: (Total Opens) / (Deliveries)
 
- iOS, Android, and Kindle push Total Opens: (Direct Opens) + (Influenced Opens)
 
- iOS, Android, and Kindle push Total Open Rate: (Total Opens) / (Deliveries)

## Total Revenue

Total Revenue is the total revenue in dollars from campaign recipients within the set primary conversion window.

This metric is only available on Campaign Comparison Reports through the Report Builder.

## Unique Clicks

Unique Clicks is the distinct number of recipients who have clicked a link within a message at least once and is measured by dispatch_id.

This includes clicks on Braze-provided unsubscribe links.

 Channel | 
 Additional information | 

 Email | 
 Tracked over a seven-day period. | 

 LINE | 
 Tracked after a minimum threshold of 20 messages per day has been reached. | 

 Calculation:

- Unique Clicks: Count
 
- Content Cards Unique Clicks % or Unique Clicks Rate: (Unique Clicks) / (Unique Impressions)
 
- Email Unique Clicks % or Unique Clicks Rate: (Unique Clicks) / (Deliveries)

## Unique Dismissals

Unique Dismissals is the number of unique recipients who dismissed a Content Card from a campaign. A user dismissing a Content Card from a campaign multiple times represents one unique dismissal.

Calculation: (Unique Dismissals) / (Unique Impressions)

## Unique Daily Impressions

Unique Daily Impressions is the number of unique users who viewed the message on a given day. This count resets each calendar day, so a user who views the same message on two different days is counted twice. This metric aligns with the billing metric of the same name.

This number is received from Braze and is based on the user_id. Unique daily impressions are counted at the campaign or Canvas step level.

Calculation: Count

## Unique Impressions

Unique Impressions is the total number of users who have viewed a message from a given campaign. An impression is logged only when the message becomes visible on a user’s screen.

 Channel | 
 Additional information | 

 In-app messages | 
 Unique impressions can be incremented again on a new calendar day in your workspace’s time zone if re-eligibility is on and a user performs the trigger action. If re-eligibility is on, Unique Impressions = Unique Recipients. For more details, refer to In-app message reporting. | 

 Content Cards | 
 The count should not increment the second time a user views a card. | 

Calculation: Count

## Unique Opens

Unique Opens is the total number (or percentage) of delivered messages that have been opened by a single user at least once and are tracked over a seven-day period.

When evaluating a specific time period, Unique Opens may appear higher than Sends for that same period. This can occur because users may still log open events for messages that were sent outside of that time period. For the entire campaign duration, Unique Opens is always lower than the total Sends.

 Channel | 
 Additional information | 

 Email | 
 Tracked over a 7 day period. | 

 LINE | 
 Tracked after a minimum threshold of 20 messages per day has been reached. | 

 Calculation:

- Unique Opens: Count
 
- Unique Opens % or Unique Open Rate: (Unique Opens) / (Deliveries)

## Unique Recipients

Unique Recipients is the number of unique daily recipients, or users who received a new message in a day. For this count to increment for a user more than once, the user must receive a new message on a different day.

Because a viewer can be a unique recipient every day, you should expect this to be higher than Unique Impressions. This number is received from Braze and is based on the user_id. Unique recipients are counted at the campaign or Canvas step level, not the send identifier level.

Users who bounce still count toward Unique Recipients when Braze counts them as a recipient for that send day. Unique Recipients is based on users Braze targeted for the message that day, not only successful deliveries.

Calculation: Count

## Unsubscribers or Unsub

Unsubscribers or Unsub is the number of messages resulting in an unsubscription. Unsubscriptions occur when Braze processes an unsubscribe from the Braze unsubscribe URL in the message body or from the list-unsubscribe header when that path is handled by Braze.

 Calculation:

- Unsubscribers or Unsub: Count
 
- Unsubscribers % or Unsub Rate: (Unsubscribes) / (Deliveries)

## Unsubscribes

Unsubscribes is the number of recipients whose subscription state changed to unsubscribed from a Braze-handled unsubscribe path, including the Braze unsubscribe URL in the message body and list-unsubscribe when Braze processes the request.

Calculation: (Unsubscribes) / (Deliveries)

## Variation

Variation is the number of variations of a campaign, differing as defined by the creator.

Calculation: Count

- 

New Stuff!
