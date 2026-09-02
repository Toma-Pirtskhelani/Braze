---
url: https://www.braze.com/docs/developer_guide/in_app_messages/troubleshooting
slug: docs__developer_guide__in_app_messages__troubleshooting
title: "Troubleshoot in-app messages"
description: "Diagnose why in-app messages aren't delivered or displayed using a symptom index, standard investigation path, Canvas IAM callouts, and platform-specific SDK checks."
section: developer_guide/in_app_messages
fetched: 2026-09-02
evidence: company-own (technical)
---
# Troubleshoot in-app messages

Use this page to diagnose why in-app messages aren’t delivered or displayed on a device. For dashboard setup (priority, triggers, segments, and re-eligibility), see the In-App Message FAQ.

Before you debug, add yourself as a test user and review Sending test messages.

## Start here: Match your symptom

 Symptom | 
 Go to | 

 In-app message didn’t show for one user | 
 One user | 

 In-app message didn’t show on one platform (Android, iOS, or Web) | 
 One platform | 

 In-app message from a Canvas step didn’t show | 
 Canvas in-app messages | 

 In-app message showed late or after a delay | 
 Timing and delayed display | 

 Impressions or clicks look wrong | 
 Impressions and analytics | 

 triggers missing or empty in event user logs | 
 Delivery troubleshooting | 

 Triggers returned but nothing displays on the device | 
 Platform-specific display troubleshooting | 

 In-app message assets fail to load (iOS, NSURLError -1008) | 
 Asset loading (Swift tab) | 

 Links don’t display or device logs show a click-action parse error | 
 Invalid link setup | 

## Standard investigation path

Use this workflow for every incident. Start at step 1.

- Confirm a session start is logged for the test device. In-app messages are requested on session start.
 
- Open event user logs and find the SDK request for that session start. In Response Data:

- In the raw JSON, confirm respond_with includes "triggers": true.
 
- The Requested Responses row should include triggers.
 
- Trigger In-App Message rows list each in-app message returned for that request.
 
- If there’s no triggers key or no Trigger In-App Message rows, go to Troubleshoot messages not being requested.
 
- If triggers is present but empty ([]), go to Troubleshoot messages not being returned.
 
- If Trigger In-App Message rows are present but nothing displays, go to Platform-specific display troubleshooting.
 
- Each trigger payload includes a type: inapp (standard) or templated_iam (requires a template request before display). See Types of in-app messages.

- For dashboard-side eligibility (segment, re-eligibility, frequency caps, priority, control groups), see Delivery troubleshooting and the In-App Message FAQ.
 
- For device-side display issues (delegates, rate limits, orientation, session timeout), select your SDK tab under Platform-specific display troubleshooting.

## Canvas in-app messages

Symptom: A user entered a Canvas in-app message step but didn’t see the message when expected.

Three behaviors drive most Canvas and in-app message tickets:

- Next-session display: Canvas in-app messages are eligible on the next session start after the step is processed—not immediately mid-session. See When are in-app messages in Canvas sent? in the Canvas FAQ.
 
- Delivery validations at step entry: If Validate audience at message send is enabled on the Message step, segment membership and frequency caps are evaluated when the user enters the step, not at display time. See Delivery validations.
 
- Delay and session timeout: If a user enters a Delay step longer than your SDK session timeout, they may start a new session before the in-app message step. The message might not be fetched at the session start when you expect it to display.

For availability windows, expiration, and zero Sends on Canvas analytics, see In-app messages and delivery in the Canvas FAQ.

important

In-app messages in Canvas can only be triggered by events sent through the SDK, not the REST API.

## In-app message didn’t show for one user

Symptom: One user didn’t receive an expected in-app message; other users may be unaffected.

Check the following:

- Was the user in the segment at session start, when the SDK requests new in-app messages?
 
- Was the user eligible or re-eligible per campaign or Canvas targeting rules? See Re-eligibility for campaigns and Canvas.
 
- Did a frequency cap apply?
 
- Was the user in a campaign control group? Check whether the campaign is configured for A/B testing.
 
- Did a higher-priority in-app message display instead? See Can multiple in-app messages display in the same session? in the In-App Message FAQ.
 
- Was the device in the orientation specified by the campaign?
 
- Was the message suppressed by the default 30-second minimum interval between triggers? See Overriding the default rate limit.

Then follow the standard investigation path.

## In-app message didn’t show on one platform

Symptom: In-app messages don’t show on Android, iOS, or Web, but may work on other platforms.

 Likely cause | 
 What to check | 

 Wrong Send To target | 
 Confirm the campaign or Canvas step targets Mobile Apps or Web Browsers as appropriate. A Web-only campaign won’t send to Android devices. | 

 Custom UI or handler suppresses display | 
 Review delegates (mobile) or braze.subscribeToInAppMessage (Web). See Customization and your SDK tab for your platform. | 

 Integration never worked on this platform | 
 Confirm this platform and app version have shown in-app messages before. | 

 Trigger didn’t fire on the device | 
 The trigger must occur locally through the SDK. A REST API call can’t trigger an in-app message in the SDK. See Triggering messages. | 

 Empty triggers in event user logs | 
 Segment, re-eligibility, frequency cap, or control group. See Troubleshoot messages not being returned. | 

## In-app message didn’t show for all users

Symptom: No users or fewer users than expected received the in-app message.

Check the following:

- Is the trigger action configured correctly in the dashboard and in the app integration?
 
- Did a higher-priority in-app message intercept the campaign? See the In-App Message FAQ.
 
- Are you on a recent SDK version? Some in-app message types have minimum SDK requirements.
 
- Are sessions integrated correctly? Confirm session analytics work for this app.
 
- Is a customized UI library interfering with display? See Customization.

Then follow the standard investigation path.

## Timing and delayed display

Symptom: The in-app message appeared later than expected or not until a new session.

Common causes:

- Campaign session-start prefetch: In-app messages are cached at session start and display when the trigger fires. A trigger that occurs before the next session start won’t show until that session. See Triggering messages.
 
- Canvas next-session behavior: See Canvas in-app messages.
 
- Scheduled dashboard delay: Confirm whether a delay is configured on the campaign or step.
 
- Trigger sync race: If users log an event immediately after session start, triggers may not be synced yet. Consider triggering off session start and segmenting on the intended event so delivery happens on the next session after the event.
 
- Sequential in-app messages: If you’re deferring or restoring messages in a tour, see Deferring triggered in-app messages.
 
- Large assets or slow CDN: Optimize images and video for HTML in-app messages. On mobile, images may download before display on slow networks—select your SDK tab for platform notes.

note

If your in-app message is triggered by session start and you’ve set an extended session timeout, closing and re-opening the app within that window won’t refresh the session. For example, with a 300-second timeout, a session-start in-app message won’t display until the session actually refreshes. Adjust the session timeout or trigger type if this affects your test.

## Delivery troubleshooting

Most in-app message issues are delivery (the device didn’t receive triggers) or display (triggers arrived but didn’t show). Confirm delivery first, then check display.

### Troubleshooting delivery

The SDK requests in-app messages from Braze servers on session start. Confirm the SDK is requesting triggers and Braze is returning them.

#### Check if messages are requested and returned

- Add yourself as a test user.
 
- Set up an in-app message campaign targeted at your user.
 
- Start a new session in your application.
 
- In event user logs, find the SDK request for the session start event. In Response Data:

- In the raw JSON, confirm respond_with includes "triggers": true.
 
- The Requested Responses row lists top-level keys in the response. For in-app messages, expect triggers.
 
- Trigger In-App Message rows list each in-app message returned for that request.

Then triage:

- If there’s no triggers key or Trigger In-App Message rows, see Troubleshoot messages not being requested.
 
- If triggers are present but empty ([]), see Troubleshoot messages not being returned.
 
- If Trigger In-App Message rows are present but nothing displays on the device, see Platform-specific display troubleshooting.
 
- Each trigger payload includes a type: inapp (standard) or templated_iam (requires a template request before display). See Types of in-app messages.

- Confirm the correct in-app messages appear in the response data.

##### Troubleshoot messages not being requested

If in-app messages aren’t being requested, your app might not be tracking sessions correctly—in-app messages refresh on session start. Confirm the app is starting a session based on your session timeout semantics:

##### Troubleshoot messages not being returned

If in-app messages aren’t being returned, you’re likely hitting a targeting or eligibility issue:

- Your segment doesn’t contain your user.

- Check the user’s Engagement tab for the expected segment.

- Your user already received the message and wasn’t re-eligible.

- Check re-eligibility settings and the In-App Message FAQ.

- Your user hit the frequency cap.

- Check frequency cap settings.

- Your user fell into a control group.

- Create a segment with a Received campaign variant filter set to Control, or opt out of control groups during integration testing.

- A higher-priority in-app message took precedence. See the In-App Message FAQ.

For archived campaigns, trigger configuration, and Quiet Hours, see the In-App Message FAQ.

## Impressions and analytics

Symptom: Impression or click counts don’t match expectations.

- Impressions greater than Unique Impressions: Expected when users have multiple devices or when a scheduled delay causes the same user to qualify more than once. See Re-eligibility for campaigns and Canvas.
 
- Impressions lower than expected: Users may not have viewed the message (impressions log on display), multiple high-priority messages may intercept each other, or trigger sync races may apply. For Canvas in-app messages, see Canvas in-app messages. For full metric definitions, see In-app message reporting and the In-App Message FAQ.
 
- Impressions lower than before: Review segment and campaign changelogs. Confirm you didn’t reuse the same trigger event in a higher-priority campaign.

If you use a delegate or custom handler to display in-app messages manually, you must log impressions and clicks yourself. See your SDK tab under Platform-specific display troubleshooting for Swift and Android details, or Log in-app message data for Web.

## Invalid link setup

Symptom: Links don’t display in an in-app message, or device logs reference a click-action parse error (for example, an error mentioning an invalid platform message click action).

This typically indicates an invalid or malformed link in the in-app message setup.

Check the following:

- Temporarily change the on-click behavior to Close message. If the message displays correctly, the link URL is likely causing the issue.
 
- Review link configuration for your editor and message type:

- Custom HTML: Troubleshoot custom HTML links and close behavior
 
- Drag-and-drop: Links and deep links in the In-App Message FAQ and minimum SDK requirements for text links
 
- Messages with buttons: Customize in-app messages for your platform

## Platform-specific display troubleshooting

If Trigger In-App Message rows appear in event user logs but nothing displays on the device, select your SDK tab for display checks (delegates, rate limits, orientation, and custom handlers).

- web
 
- android
 
- swift

### Troubleshooting display

If your app is requesting and receiving in-app messages but they aren’t showing, device-side logic may be preventing display:

- 
 
Is the trigger event firing as expected? To test, configure the message to trigger on a different action (such as session start) and verify whether it displays.

- 
 
Triggered in-app messages are rate-limited based on the minimum time interval between triggers, which defaults to 30 seconds.

- 
 
Failed image downloads prevent in-app messages with images from displaying. Check device logs for download failures. Try removing the image temporarily to see if the message displays.

- 
 
If you use custom in-app message handling through braze.subscribeToInAppMessage, verify the callback isn’t suppressing display. See Customization.

### Troubleshooting display

If your app is requesting and receiving in-app messages but they aren’t showing, device-side logic may be preventing display:

- 
 
Is the trigger event firing as expected? To test, configure the message to trigger on a different action (such as session start) and verify whether it displays.

- 
 
Triggered in-app messages are rate-limited based on the minimum time interval between triggers, which defaults to 30 seconds.

- 
 
Failed image downloads prevent in-app messages with images from displaying. Check device logs for download failures. Try removing the image temporarily to see if the message displays.

- 
 
If you’ve set a delegate to customize in-app message handling, confirm it isn’t suppressing display. See Customization.

- 
 
If device orientation doesn’t match the in-app message setting, the message won’t display.

- 
 
Depending on network conditions, images may download before display. On slow connections or low-performance devices, allow extra time or optimize asset size.

### Impressions and clicks aren’t being logged

If you’ve set an in-app message delegate to manually handle message display or click actions, you must manually log clicks and impressions on the in-app message.

### Troubleshooting display

If your app is requesting and receiving in-app messages but they aren’t showing, device-side logic may be preventing display:

- 
 
Is the trigger event firing as expected? To test, configure the message to trigger on a different action (such as session start) and verify whether it displays.

- 
 
Triggered in-app messages are rate-limited based on the minimum time interval between triggers, which defaults to 30 seconds.

- 
 
Failed image downloads prevent in-app messages with images from displaying. Check device logs for download failures. Try removing the image temporarily to see if the message displays.

- 
 
If you’ve set a delegate to customize in-app message handling, confirm it isn’t suppressing display. See Customization.

- 
 
If device orientation doesn’t match the in-app message setting, the message won’t display.

- 
 
Depending on network conditions, images may download before display. On slow connections or low-performance devices, allow extra time or optimize asset size.

### Impressions and clicks aren’t being logged

If you’ve set an in-app message delegate to manually handle message display or click actions, you must manually log clicks and impressions on the in-app message.

### Troubleshooting asset loading (NSURLError code -1008)

When integrating Braze alongside third-party network logging libraries, developers can commonly run into an NSURLError with the domain code -1008. This error indicates that assets like images and fonts could not be retrieved or failed to cache. To work around such cases, you must register Braze CDN URLs to the list of domains that should be ignored by these libraries.

#### Domains

The full list of CDN domains is as follows:

- "appboy-images.com"
 
- "braze-images.com"
 
- "cdn.braze.eu"
 
- "cdn.braze.com"

#### Examples

The following libraries are known to conflict with Braze asset caching, along with example code to work around the issue. If your project uses a library that causes an unavailable resource error and is not listed here, consult the documentation of that library for similar usage APIs.

##### Netfox

- swift
 
- objective-c

```

1

```
 | 
```
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])

```
 | 

```

1

```
 | 
```
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];

```
 | 

##### NetGuard

- swift
 
- objective-c

```

1

```
 | 
```
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])

```
 | 

```

1
2
3

```
 | 
```
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;

```
 | 

##### XNLogger

- swift
 
- objective-c

```

1
2

```
 | 
```
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])

```
 | 

```

1
2

```
 | 
```
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];

```
 | 

##### Wormholy

- swift
 
- objective-c

```

1

```
 | 
```
Wormholy.ignoredHosts = ["cdn.braze.com"]

```
 | 

```

1

```
 | 
```
Wormholy.ignoredHosts = @[@"cdn.braze.com"];

```
 | 

- 

New Stuff!
