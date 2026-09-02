---
url: https://www.braze.com/docs/developer_guide/push_notifications/deep_linking_troubleshooting
slug: docs__developer_guide__push_notifications__deep_linking_troubleshooting
title: "Troubleshoot deep linking"
description: "Diagnose iOS deep linking issues using a symptom index, standard investigation path, and platform-specific checks."
section: developer_guide/push_notifications
fetched: 2026-09-02
evidence: company-own (technical)
---
# Troubleshoot deep linking

Use this page to diagnose common deep linking issues on iOS. For help choosing the right link type, see iOS deep linking guide. For implementation details, see Deep linking.

## Start here: Match your symptom

Find the behavior you’re seeing in the table, then follow that section’s steps. If you’re not sure which section applies, use the standard investigation path.

 Symptom | 
 Go to | 

 Custom scheme link opens app but wrong screen | 
 Custom scheme deep link doesn’t open the correct view | 

 Universal link opens Safari instead of app | 
 Universal link opens in Safari instead of the app | 

 Email link doesn’t open the app | 
 Deep link from email doesn’t open the app | 

 Every email link opens the app | 
 Every email link opens the app | 

 Works from push but not in-app message (or the other way around) | 
 Deep link works from push but not from in-app message | 

 “Open Web URL Inside App” shows blank WebView | 
 “Open Web URL Inside App” shows a blank or broken page | 

 Branch link doesn’t open the app or route correctly | 
 Troubleshooting Branch with Braze | 

 Deep link fails with no clear cause | 
 General debugging tips | 

## Standard investigation path

Use this workflow for every deep linking incident. Start at step 1.

- Test the link outside Braze. For custom schemes, run xcrun simctl openurl booted "<URL>" in Terminal (for example, xcrun simctl openurl booted "myapp://products/123"). For universal links, paste the URL into the Notes app on a physical device and tap it.
 
- Enable verbose logging and reproduce the issue. Look for Opening '<URL>': entries with channel, useWebView, and isUniversalLink.
 
- For universal links, validate your AASA file and Associated Domains entitlement.
 
- For email links, confirm the click-tracking domain hosts a valid AASA file.
 
- If you implement BrazeDelegate.braze(_:shouldOpenURL:), verify it handles links consistently across channels.
 
- If the issue persists, contact Braze Support with verbose logs and the link URL.

## Custom scheme deep link doesn’t open the correct view

Symptom: A custom scheme deep link (for example, myapp://products/123) opens your app but doesn’t navigate to the intended screen.

- Verify the scheme is registered. In Xcode, check that your scheme is listed under CFBundleURLTypes in Info.plist.
 
- Check your handler. Set a breakpoint in application(_:open:options:) to confirm it’s being called and inspect the url parameter.
 
- Test the link independently. Run the following command from Terminal to test the deep link outside of Braze:

```

1

```
 | 
```
xcrun simctl openurl booted "myapp://products/123"

```
 | 
 
If the link doesn’t work here, the issue is in your app’s URL handling—not in Braze.

- Check the URL format. Verify the URL in your campaign matches what your handler expects. Common mistakes include missing path components or incorrect casing.

## Universal link opens in Safari instead of the app

Symptom: A universal link (for example, https://myapp.com/products/123) opens in Safari instead of your app.

### Verify the Associated Domains entitlement

In Xcode, go to your app target > Signing & Capabilities and check that applinks:yourdomain.com is listed in Associated Domains.

### Validate the AASA file

Your Apple App Site Association (AASA) file must be hosted at one of these locations:

- https://yourdomain.com/.well-known/apple-app-site-association
 
- https://yourdomain.com/apple-app-site-association

Verify the following:

- The file is served over HTTPS with a valid certificate.
 
- The Content-Type is application/json.
 
- The file size is under 128 KB.
 
- The appID matches your Team ID and Bundle ID (for example, ABCDE12345.com.example.myapp).
 
- The paths or components array includes the URL patterns you expect.

You can validate your AASA using Apple’s search validation tool or by running:

```

1

```
 | 
```
swcutil dl -d yourdomain.com

```
 | 

### Check the AppDelegate

Verify that application(_:continue:restorationHandler:) is implemented in your AppDelegate and handles the NSUserActivity correctly:

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

```
 | 
```
func application(_ application: UIApplication,
 continue userActivity: NSUserActivity,
 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
 guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
 let url = userActivity.webpageURL else {
 return false
 }
 // Handle the URL
 return true
}

```
 | 

### Verify Braze SDK configuration

If you’re using universal links from Braze-delivered push notifications, in-app messages, or Content Cards, confirm that forwardUniversalLinks is enabled:

```

1
2

```
 | 
```
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true

```
 | 

note

Universal link forwarding requires access to the application entitlements. When running in a simulator, these entitlements aren’t directly available. To test in a simulator, add the .entitlements file to the Copy Bundle Resources build phase.

### Check for the long-press issue

If you long-press a universal link and select Open, iOS may “break” the universal link association for that domain. This is a known iOS behavior. To reset it, long-press the link again and select Open in [App Name].

## Deep link from email doesn’t open the app

Symptom: A link in an email doesn’t open your app through the universal link.

Email links go through your ESP’s click-tracking system, which wraps links in a tracking domain (for example, https://click.yourdomain.com/...). For universal links to work from email, you must configure the AASA file on your click-tracking domain—not just your primary domain.

### Verify click-tracking domain AASA

- Identify your click-tracking domain from your ESP settings (SendGrid, SparkPost, or Amazon SES).
 
- Host the AASA file at https://your-click-tracking-domain/.well-known/apple-app-site-association.
 
- Confirm the AASA file on the click-tracking domain includes the same appID and valid path patterns.

For ESP-specific setup instructions, see Universal links and App Links.

### Check the redirect chain

Some ESPs perform a redirect from the click-tracking URL to your final URL. Universal links only work if iOS recognizes the initial domain (the click-tracking domain) as associated with your app. If the redirect bypasses the AASA check, the link opens in Safari.

To test:

- Send yourself a test email.
 
- Long-press the link and inspect the URL — this is the click-tracking URL.
 
- Verify this domain has a valid AASA file.

## Every email link opens the app

Symptom: Every link in an email opens your app, including links you expect to open in a browser.

Your AASA file on the click-tracking domain uses paths that match every URL on that domain (for example * or /*). iOS then treats every click-tracked email link as a universal link.

Limit paths to the URLs that should open the app. For SendGrid, match /uni/ and add universal="true" only on those links.

For ESP-specific setup, including Android pathPrefix values, see Universal links and App Links.

## Deep link works from push but not from in-app message (or the other way around)

Symptom: The same deep link works from one Braze channel but not another.

### Check the BrazeDelegate

If you implement BrazeDelegate.braze(_:shouldOpenURL:), verify it handles links consistently across channels. The context parameter includes the source channel. Look for conditional logic that may accidentally filter links from specific channels.

### Enable verbose logging

Enable verbose logging and reproduce the issue. Look for the Opening log entry:

```

1
2
3
4

```
 | 
```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>

```
 | 

Compare the log output for the working channel vs. the non-working channel. Differences in useWebView or isUniversalLink indicate how the SDK is interpreting the link differently.

### Check for custom display delegates

If you use a custom in-app message display delegate or Content Card click handler, verify that it correctly passes link events to the Braze SDK for handling.

## “Open Web URL Inside App” shows a blank or broken page

Symptom: Selecting Open Web URL Inside App results in a blank or broken WebView.

- Verify the URL uses HTTPS. The SDK’s WebView requires ATS-compliant URLs. HTTP links fail silently.
 
- Check for Content Security Policy headers. If the target web page sets X-Frame-Options: DENY or a restrictive Content-Security-Policy, it blocks rendering in a WebView.
 
- Check for redirects to custom schemes. If the web page redirects to a custom scheme (for example, myapp://), the WebView can’t handle it.
 
- Test the URL in Safari. If the page doesn’t load in Safari on the device, it won’t load in the WebView either.

## Troubleshooting Branch with Braze

If you use Branch as your linking provider:

### Verify the BrazeDelegate routes to Branch

Your BrazeDelegate must intercept Branch links and pass them to the Branch SDK. Verify the following:

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
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
 if let host = context.url.host, host.contains("app.link") {
 // Route to Branch SDK
 Branch.getInstance.handleDeepLink(context.url)
 return false
 }
 // Let Braze handle other links
 return true
}

```
 | 

If shouldOpenURL returns true for Branch links, Braze handles them directly instead of routing to Branch.

### Check Branch link domain

Verify the Branch domain in your BrazeDelegate matches your actual Branch link domain. Branch uses several domain formats:

- yourapp.app.link (default)
 
- yourapp-alternate.app.link (alternate)
 
- Custom domains (if configured in Branch dashboard)

### Enable both SDKs’ logging

To diagnose where the link breaks in the chain:

- Enable Braze verbose logging. Look for Opening '<URL>': entries to verify the SDK received the link.
 
- Enable Branch test mode. Check the Branch dashboard for link click events.
 
- If Braze logs the link, but Branch doesn’t see a click, the BrazeDelegate routing logic is the likely issue.

### Check Branch dashboard configuration

In the Branch dashboard, verify:

- Your app’s Bundle ID and Team ID match your Xcode project.
 
- Your Associated Domains include the Branch link domain.
 
- Your Branch AASA file is valid (Branch hosts this automatically on app.link domains).

### Test Branch links independently

Test the Branch link outside of Braze to isolate the issue:

- Open the Branch link in Safari on your device. If it doesn’t open the app, the issue is in your Branch or AASA configuration — not Braze.
 
- Paste the Branch link into the Notes app and tap it. Universal links work more reliably from Notes than from Safari’s address bar.

## General debugging tips

### Use verbose logging

Enable verbose logging to see exactly how the SDK processes links. Key entries to look for:

 Log entry | 
 What it means | 

 Opening '<URL>': - channel: notification | 
 SDK is processing a link from a push notification | 

 Opening '<URL>': - channel: inAppMessage | 
 SDK is processing a link from an in-app message | 

 Opening '<URL>': - channel: contentCard | 
 SDK is processing a link from a Content Card | 

 useWebView: true | 
 SDK opens the URL in the in-app WebView | 

 isUniversalLink: true | 
 SDK identified the URL as a universal link | 

For more details on reading these logs, see Reading verbose logs.

### Test links in isolation

Before testing through Braze, verify that your deep link or universal link works on its own:

- Custom scheme: Run xcrun simctl openurl booted "myapp://path" in Terminal.
 
- Universal link: Paste the URL into the Notes app on a physical device and tap it. Don’t test from the Safari address bar, as iOS treats typed URLs differently from tapped links.
 
- Branch link: Open the Branch link from the Notes app on a device.

### Test on a physical device

Universal links have limited support in the iOS simulator. Always test on a physical device for accurate results. If you must test in a simulator, add the .entitlements file to the Copy Bundle Resources build phase.

- 

New Stuff!
