---
url: https://www.braze.com/docs/developer_guide/in_app_messages/html_messages
slug: docs__developer_guide__in_app_messages__html_messages
title: "HTML in-app messages"
description: "Learn how to add the Braze JavaScript interface to your app."
section: developer_guide/in_app_messages
fetched: 2026-09-02
evidence: company-own (technical)
---
# HTML in-app messages

Learn how to add the Braze JavaScript interface to your app, so you can use the Braze API to create HTML in-app messages in your custom WebViews.

- android
 
- swift

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK.

## About HTML messages

With the Braze JavaScript interface, you can leverage Braze inside the custom WebViews within your app. The InAppMessageJavascriptInterface is responsible for:

- Injecting the Braze JavaScript bridge into your WebView, as outlined in User Guide: HTML in-app messages.
 
- Passing the bridge methods received from your WebView to the Braze Android SDK.

## Adding the interface to a WebView

Using Braze functionality from a WebView in your app can be done by adding the Braze JavaScript interface to your WebView. After the interface has been added, the same API available for User Guide: HTML in-app messages will be available within your custom WebView.

- java
 
- kotlin

```

1
2
3
4
5

```
 | 
```
String javascriptString = BrazeFileUtils.getAssetFileStringContents(context.getAssets(), "braze-html-bridge.js");
myWebView.loadUrl("javascript:" + javascriptString);

final InAppMessageJavascriptInterface javascriptInterface = new InAppMessageJavascriptInterface(context, inAppMessage);
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge");

```
 | 

```

1
2
3
4
5

```
 | 
```
val javascriptString = context.assets.getAssetFileStringContents("braze-html-bridge.js")
myWebView.loadUrl("javascript:" + javascriptString!!)

val javascriptInterface = InAppMessageJavascriptInterface(context, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge")

```
 | 

## Embedding YouTube content

YouTube and other HTML5 content can play in HTML in-app messages. This requires hardware acceleration to be enabled in the activity where the in-app message is being displayed; see the Android developer guide for more details. Hardware acceleration is only available on Android API versions 11 and later.

The following is an example of an embedded YouTube video in an HTML snippet:

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
<body>
 <div class="box">
 <div class="relativeTopRight">
 <a href="appboy://close">X</a>
 </div>
 <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI" title="YouTube video player">
 </iframe>
 </div>
</body>

```
 | 

## Using deep links

When using deep links or external links in Android HTML in-app messages, do not call brazeBridge.closeMessage() in your JavaScript. The SDK’s internal logic automatically closes the in-app message when it redirects to a link. Calling brazeBridge.closeMessage() interferes with this process and may cause the message to become unresponsive when users return to your app.

The following is an example of a deep link in a code snippet:

```

1
2
3
4
5

```
 | 
```
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK.

## About HTML messages

With the Braze JavaScript interface, you can leverage Braze inside the custom WebViews within your app. The interface’s ScriptMessageHandler is responsible for:

- Injecting the Braze JavaScript bridge into your WebView, as outlined in User Guide: HTML in-app messages.
 
- Passing the bridge methods received from your WebView to the Braze Swift SDK.

## Adding the interface to a WebView

First, add the ScriptMessageHandler from WebViewBridge to your app.

```

1
2
3
4

```
 | 
```
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
 channel: .inAppMessage,
 braze: braze
)

```
 | 

Add the initialized scriptMessageHandler to a WkWebView’s userContentController.

```

1
2
3
4

```
 | 
```
configuration.userContentController.add(
 scriptMessageHandler,
 name: Braze.WebViewBridge.ScriptMessageHandler.name
)

```
 | 

Then create the WebView using your configuration.

```

1

```
 | 
```
let webView = WKWebView(frame: .zero, configuration: configuration)

```
 | 

When you’re finished, your code should be similar to the following:

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
// Create the script message handler using your initialized Braze instance.
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
 channel: .inAppMessage,
 braze: braze
)

// Create a web view configuration and setup the script message handler.
let configuration = WKWebViewConfiguration()
configuration.userContentController.addUserScript(
 Braze.WebViewBridge.ScriptMessageHandler.script
)
configuration.userContentController.add(
 scriptMessageHandler,
 name: Braze.WebViewBridge.ScriptMessageHandler.name
)

// Create the webview using the configuration
let webView = WKWebView(frame: .zero, configuration: configuration)

```
 | 

## Example: Logging a custom event

In the following example, BrazeBridge logs a custom event from existing web content to the Braze Swift SDK.

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

```
 | 
```
<!DOCTYPE html>
<html lang="en">
 <head>
 <meta charset="UTF-8" />
 <meta name="viewport" content="width=device-width, initial-scale=1.0" />
 <title>Logging data via BrazeBridge Example</title>
 <script>
 function logData(data) {
 window.brazeBridge.logCustomEvent(data);
 }
 </script>
 </head>

 <body>
 <input
 type="button"
 value="Click to log a custom Event 'completed_level'"
 onclick="logData('completed_level')"
 />
 </body>
</html>

```
 | 

- 

New Stuff!
