---
url: https://www.braze.com/docs/developer_guide/push_notifications/sending_test_messages
slug: docs__developer_guide__push_notifications__sending_test_messages
title: "Sending test messages"
description: "Learn how to send a test message for the Braze SDK."
section: developer_guide/push_notifications
fetched: 2026-09-02
evidence: company-own (technical)
---
# Sending test messages

Before sending out a messaging campaign to your users, you may want to test it to make sure it looks right and operates in the intended manner. You can use the dashboard to create and send test messages with push notifications, in-app messages (IAM), or email.

## Sending a test message

### Step 1: Create a designated test segment 

After you set up a test segment, you can use it to test any of your Braze messaging channels. When set up correctly, this only needs to be done a single time.

To set up a test segment, go to Segments and create a new segment. Select Add Filter, then choose a one of the test filters.

With test filters, you can ensure that only users with a specific email address or external user ID are sent the test message.

Both email address and external user ID filters offer the following options:

 Operator | 
 Description | 

 equals | 
 This will look for an exact match of the email or user ID that you provide. Use this if you only want to send the test campaigns to devices associated with a single email or user ID. | 

 does not equal | 
 Use this if you want to exclude a particular email or user ID from test campaigns. | 

 matches | 
 This will find users that have email addresses or user IDs that match part of the search term you provide. You could use this to find only the users that have an @yourcompany.com address, allowing you to send messages to everyone on your team. | 

You can select multiple specific emails using the “matches” option and separating the email addresses with a | character. For example: “matches” “[email protected] | [email protected]”. You can also combine multiple operators together. For example, the test segment could include an email address filter that “matches” “@braze.com” and another filter that “does not equal” “[email protected]”.

After adding the testing filters to your test segment, you can verify it’s working by selecting Preview or by selecting Settings > CSV Export All User Data to export that segment’s user data to a CSV file.

note

Exporting the segment’s User Data to a CSV file is the most accurate verification method, as the preview will only show a sample of your users and may not include all users.

### Step 2: Send the message

You can send a message using the Braze dashboard or the command line.

- using the dashboard
 
- using the command line

- push or in-app message
 
- email message

To send test push notifications or in-app messages, you need to target your previously created test segment. Begin by creating your campaign and following the usual steps. When you reach the Target Audiences step, select your test segment from the dropdown menu.

Confirm your campaign and launch it to test your push notification and in-app messages.

note

Be sure to select Allow users to become re-eligible to receive campaign under the Schedule portion of the campaign composer if you intend to use a single campaign to send a test message to yourself more than once.

If you’re only testing email messages, you do not necessarily have to set up a test segment. In the first step of the campaign composer where you compose your campaign’s email message, click Send Test and enter the email address to which you wish to send a test email.

tip

You can also enable or disable TEST (or SEED) being appended on your test messages.

Alternatively, you can send a single notification using cURL and the Braze Messaging API. Note that these examples make a request using the US-01 instance. To find out yours, refer to API endpoints.

- android
 
- swift
 
- kindle

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

```
 | 
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
 "external_user_ids":["EXTERNAL_USER_ID"],
 "messages": {
 "android_push": {
 "title":"Test push title",
 "alert":"Test push",
 "extra":{
 "CUSTOM_KEY":"CUSTOM_VALUE"
 }
 }
 }
}' https://rest.iad-01.braze.com/messages/send

```
 | 

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

```
 | 
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
 "external_user_ids":["EXTERNAL_USER_ID"],
 "messages": {
 "apple_push": {
 "alert": "Test push",
 "extra": { 
 "CUSTOM_KEY" :"CUSTOM_VALUE"
 }
 }
 }
}' https://rest.iad-01.braze.com/messages/send

```
 | 

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

```
 | 
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
 "external_user_ids":["EXTERNAL_USER_ID"],
 "messages": {
 "kindle_push": {
 "title":"Test push title",
 "alert":"Test push",
 "extra":{
 "CUSTOM_KEY":"CUSTOM_VALUE"
 }
 }
 }
}' https://rest.iad-01.braze.com/messages/send

```
 | 

Replace the following:

 Placeholder | 
 Description | 

 BRAZE_API_KEY | 
 Your Braze API key used for authentication. In Braze, go to Settings > API Keys to locate your key. | 

 EXTERNAL_USER_ID | 
 The external user ID used to send your message to a specific user. In Braze, go to Audience > Search users, then search for a user. | 

 CUSTOM_KEY | 
 (Optional) A custom key for additional data. | 

 CUSTOM_VALUE | 
 (Optional) A custom value assigned to your custom key. | 

## Test limitations

There are a few situations where test messages don’t have complete feature parity with launching a campaign or Canvas to a real set of users. In these instances, to validate this behavior, you should launch the campaign or Canvas to a limited set of test users.

- Viewing the Braze preference center from Test Messages will cause the submit button to be grayed out.
 
- The list-unsubscribe header is not included in emails sent by the test message functionality.
 
- For in-app messages and Content Cards, the target user must have a push token for the target device.

- 

New Stuff!
