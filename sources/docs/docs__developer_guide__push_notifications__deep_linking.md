---
url: https://www.braze.com/docs/developer_guide/push_notifications/deep_linking
slug: docs__developer_guide__push_notifications__deep_linking
title: "Deep linking in push notifications"
description: "Deep linking in push notifications Learn how to set up silent push notifications for the Braze SDK. android swift flutter cordova Prerequisites Before you can..."
section: developer_guide/push_notifications
fetched: 2026-09-02
evidence: company-own (technical)
---
# Deep linking in push notifications

Learn how to set up silent push notifications for the Braze SDK.

- android
 
- swift
 
- flutter
 
- cordova

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK.

## Creating a universal delegate

The Android SDK provides the ability to set a single delegate object to custom handle all deep links opened by Braze across Content Cards, in-app messages, and push notifications.

Your delegate object should implement the IBrazeDeeplinkHandler interface and be set using BrazeDeeplinkHandler.setBrazeDeeplinkHandler(). In most cases, the delegate should be set in your app’s Application.onCreate().

The following is an example of overriding the default UriAction behavior with custom intent flags and custom behavior for YouTube URLs:

- java
 
- kotlin

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
25
26
27
28
29
30
31
32
33

```
 | 
```
public class CustomDeeplinkHandler implements IBrazeDeeplinkHandler {
 private static final String TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler.class);

 @Override
 public void gotoUri(Context context, UriAction uriAction) {
 String uri = uriAction.getUri().toString();
 // Open YouTube URLs in the YouTube app and not our app
 if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
 uriAction.setUseWebView(false);
 }

 CustomUriAction customUriAction = new CustomUriAction(uriAction);
 customUriAction.execute(context);
 }

 public static class CustomUriAction extends UriAction {

 public CustomUriAction(@NonNull UriAction uriAction) {
 super(uriAction);
 }

 @Override
 protected void openUriWithActionView(Context context, Uri uri, Bundle extras) {
 Intent intent = getActionViewIntent(context, uri, extras);
 intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
 if (intent.resolveActivity(context.getPackageManager()) != null) {
 context.startActivity(intent);
 } else {
 BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link " + uri + ".");
 }
 }
 }
}

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
25
26
27
28
29
30

```
 | 
```
class CustomDeeplinkHandler : IBrazeDeeplinkHandler {

 override fun gotoUri(context: Context, uriAction: UriAction) {
 val uri = uriAction.uri.toString()
 // Open YouTube URLs in the YouTube app and not our app
 if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
 uriAction.useWebView = false
 }

 val customUriAction = CustomUriAction(uriAction)
 customUriAction.execute(context)
 }

 class CustomUriAction(uriAction: UriAction) : UriAction(uriAction) {

 override fun openUriWithActionView(context: Context, uri: Uri, extras: Bundle) {
 val intent = getActionViewIntent(context, uri, extras)
 intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_SINGLE_TOP
 if (intent.resolveActivity(context.packageManager) != null) {
 context.startActivity(intent)
 } else {
 BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link $uri.")
 }
 }
 }

 companion object {
 private val TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler::class.java)
 }
}

```
 | 

## Deep linking to app settings

To allow deep links to directly open your app’s settings, you’ll need a custom BrazeDeeplinkHandler. In the following example, the presence of a custom key-value pair called open_notification_page will make the deep link open the app’s settings page:

- java
 
- kotlin

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

```
 | 
```
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(new IBrazeDeeplinkHandler() {
 @Override
 public void gotoUri(Context context, UriAction uriAction) {
 final Bundle extras = uriAction.getExtras();
 if (extras.containsKey("open_notification_page")) {
 Intent intent = new Intent();
 intent.setAction("android.settings.APP_NOTIFICATION_SETTINGS");
 intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);

 //for Android 5-7
 intent.putExtra("app_package", context.getPackageName());
 intent.putExtra("app_uid", context.getApplicationInfo().uid);

 // for Android 8 and later
 intent.putExtra("android.provider.extra.APP_PACKAGE", context.getPackageName());
 context.startActivity(intent);
 }
 }
});

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
13
14
15
16
17
18

```
 | 
```
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(object : IBrazeDeeplinkHandler {
 override fun gotoUri(context: Context, uriAction: UriAction) {
 val extras = uriAction.extras
 if (extras.containsKey("open_notification_page")) {
 val intent = Intent()
 intent.action = "android.settings.APP_NOTIFICATION_SETTINGS"
 intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK

 //for Android 5-7
 intent.putExtra("app_package", context.packageName)
 intent.putExtra("app_uid", context.applicationInfo.uid)

 // for Android 8 and later
 intent.putExtra("android.provider.extra.APP_PACKAGE", context.packageName)
 context.startActivity(intent)
 }
 }
})

```
 | 

## Customizing WebView activity

When Braze opens website deeplinks inside the app, the deeplinks are handled by BrazeWebViewActivity.

note

For custom HTML in-app messages, links configured with target="_blank" open in the device’s default web browser and are not handled by BrazeWebViewActivity.

To change this:

- Create a new Activity that handles the target URL from Intent.getExtras() with the key com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA. For an example, see BrazeWebViewActivity.kt.
 
- Add that activity to AndroidManifest.xml and set exported to false.

```

1
2
3

```
 | 
```
 <activity
 android:name=".MyCustomWebViewActivity"
 android:exported="false" />

```
 | 

- Set your custom Activity in a BrazeConfig builder object. Build the builder and pass it to Braze.configure() in your Application.onCreate().

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
BrazeConfig brazeConfig = new BrazeConfig.Builder()
 .setCustomWebViewActivityClass(MyCustomWebViewActivity::class)
 ...
 .build();
Braze.configure(this, brazeConfig);

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
val brazeConfig = BrazeConfig.Builder()
 .setCustomWebViewActivityClass(MyCustomWebViewActivity::class.java)
 ...
 .build()
Braze.configure(this, brazeConfig)

```
 | 

## Troubleshooting

If deep links from push notifications aren’t working on Android, try the following steps:

- Test the deep link outside of Braze. Open the deep link URL from another app, such as email or a browser. If it doesn’t open your app, the deep link may not be configured correctly in your AndroidManifest.xml. For more information, see Android’s Create Deep Links documentation.
 
- Check that automatic deep link handling is enabled. Verify that com_braze_handle_push_deep_links_automatically is set to true in braze.xml, or set this option through runtime configuration. Without this setting, Braze doesn’t automatically open your app and deep link destination when someone taps a push notification.
 
- Verify your deep link handler delegate. If you set a custom IBrazeDeeplinkHandler, confirm that your gotoUri implementation handles the URI and doesn’t drop it.
 
- Test across channels. If the same deep link works in an in-app message but not from push, the issue is likely in your push deep link handling, not in the deep link itself.

## Using Jetpack Compose

To handle deeplinks when using Jetpack Compose with NavHost:

- Ensure that the activity handling your deeplink is registered in the Android Manifest.

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
 <activity
 ...
 <intent-filter>
 <action android:name="android.intent.action.VIEW" />
 <category android:name="android.intent.category.BROWSABLE" />
 <category android:name="android.intent.category.DEFAULT" />
 <data
 android:host="articles"
 android:scheme="myapp" />
 </intent-filter>
 </activity>

```
 | 

- In NavHost, specify which deeplinks you want it to handle.

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

```
 | 
```
 composableWithCompositionLocal(
 route = "YOUR_ROUTE_HERE",
 deepLinks = listOf(navDeepLink {
 uriPattern = "myapp://articles/{${MainDestinations.ARTICLE_ID_KEY}}"
 }),
 arguments = listOf(
 navArgument(MainDestinations.ARTICLE_ID_KEY) {
 type = NavType.LongType
 }
 ),
 ) { backStackEntry ->
 val arguments = requireNotNull(backStackEntry.arguments)
 val articleId = arguments.getLong(MainDestinations.ARTICLE_ID_KEY)
 ArticleDetail(
 articleId
 )
 }

```
 | 

- Depending on your app architecture, you may need to handle the new intent that’s sent to your current activity as well.

```

1
2
3
4
5
6
7

```
 | 
```
 DisposableEffect(Unit) {
 val listener = Consumer<Intent> {
 navHostController.handleDeepLink(it)
 }
 addOnNewIntentListener(listener)
 onDispose { removeOnNewIntentListener(listener) }
 }

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK.

tip

For help choosing between custom scheme deep links, universal links, and “Open Web URL Inside App,” see iOS deep linking guide. For troubleshooting, see Deep linking troubleshooting.

## Handling deep links

### Step 1: Register a scheme

To handle deep linking, a custom scheme must be stated in your Info.plist file. The navigation structure is defined by an array of dictionaries. Each of those dictionaries contains an array of strings.

Use Xcode to edit your Info.plist file:

- Add a new key, URL types. Xcode will automatically make this an array containing a dictionary called Item 0.
 
- Within Item 0, add a key URL identifier. Set the value to your custom scheme.
 
- Within Item 0, add a key URL Schemes. This will automatically be an array containing a Item 0 string.
 
- Set URL Schemes » Item 0 to your custom scheme.

Alternatively, if you wish to edit your Info.plist file directly, you can follow this spec:

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
<key>CFBundleURLTypes</key>
<array>
 <dict>
 <key>CFBundleURLName</key>
 <string>YOUR.SCHEME</string>
 <key>CFBundleURLSchemes</key>
 <array>
 <string>YOUR.SCHEME</string>
 </array>
 </dict>
</array>

```
 | 

### Step 2: Add a scheme allowlist

You must declare the URL schemes you wish to pass to canOpenURL(_:) by adding the LSApplicationQueriesSchemes key to your app’s Info.plist file. Attempting to call schemes outside this allowlist will cause the system to record an error in the device’s logs, and the deep link will not open. An example of this error will look like this:

```

1

```
 | 
```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"

```
 | 

For example, if an in-app message should open the Facebook app when tapped, the app has to have the Facebook custom scheme (fb) in your allowlist. Otherwise, the system will reject the deep link. Deep links that direct to a page or view inside your own app still require that your app’s custom scheme be listed in your app’s Info.plist.

Your example allowlist might look something like:

```

1
2
3
4
5
6

```
 | 
```
<key>LSApplicationQueriesSchemes</key>
<array>
 <string>myapp</string>
 <string>fb</string>
 <string>twitter</string>
</array>

```
 | 

For more information, refer to Apple’s documentation on the LSApplicationQueriesSchemes key.

### Step 3: Implement a handler

Apps built with Xcode 27 and later are required to adopt the UIScene life cycle, so iOS delivers custom scheme URLs to your SceneDelegate through scene:openURLContexts: rather than to your AppDelegate. The important argument is the NSURL object.

- swift
 
- objective-c

```

1
2
3
4
5
6

```
 | 
```
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
 guard let url = URLContexts.first?.url else { return }
 let path = url.path
 let query = url.query
 // Insert your code here to take some action based upon the path and query.
}

```
 | 

```

1
2
3
4
5
6

```
 | 
```
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
 NSURL *url = URLContexts.allObjects.firstObject.URL;
 NSString *path = [url path];
 NSString *query = [url query];
 // Insert your code here to take some action based upon the path and query.
}

```
 | 

note

If your app has not yet adopted the UIScene life cycle, iOS instead calls application:openURL:options: on your AppDelegate:

```

1
2
3
4
5
6

```
 | 
```
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
 let path = url.path
 let query = url.query
 // Insert your code here to take some action based upon the path and query.
 return true
}

```
 | 

## App Transport Security (ATS)

As defined by Apple, “App Transport Security is a feature that improves the security of connections between an app and web services. The feature consists of default connection requirements that conform to best practices for secure connections. Apps can override this default behavior and turn off transport security.”

ATS is applied by default. It requires that all connections use HTTPS and are encrypted using TLS 1.2 with forward secrecy. Refer to Requirements for Connecting Using ATS for more information. All images served by Braze to end devices are handled by a content delivery network (“CDN”) that supports TLS 1.2 and is compatible with ATS.

Unless they are specified as exceptions in your application’s Info.plist, connections that do not follow these requirements will fail with errors that are similar to the following.

Example Error 1:

```

1
2

```
 | 
```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."

```
 | 

Example Error 2:

```

1

```
 | 
```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)

```
 | 

ATS compliance is enforced for links opened within the mobile app (our default handling of clicked links) and does not apply to sites opened externally through a web browser.

### Working with ATS

You can handle ATS in either of the following ways, but we recommend complying with ATS requirements.

- comply
 
- partially disable
 
- fully disable

Your Braze integration can satisfy ATS requirements by ensuring that any existing links you drive users to (for example, though in-app message and push campaigns) satisfy ATS requirements. While there are ways to bypass ATS restrictions, our recommendation is to ensure that all linked URLs are ATS-compliant. Given Apple’s increasing emphasis on application security, the following approaches to allowing ATS exceptions are not guaranteed to be supported by Apple.

You can allow a subset of links with certain domains or schemes to be treated as exceptions to the ATS rules. Your Braze integration will satisfy ATS requirements if every link you use in a Braze messaging channel is either ATS compliant or handled by an exception.

To add a domain as an exception of the ATS, add following to your app’s Info.plist file:

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

```
 | 
```
<key>NSAppTransportSecurity</key>
<dict>
 <key>NSAllowsArbitraryLoads</key>
 <true/>
 <key>NSExceptionDomains</key>
 <dict>
 <key>example.com</key>
 <dict>
 <key>NSExceptionAllowsInsecureHTTPLoads</key>
 <false/>
 <key>NSIncludesSubdomains</key>
 <true/>
 </dict>
 </dict>
</dict>

```
 | 

Refer to Apple’s article on app transport security keys for more information.

You can turn off ATS entirely. Note that this is not recommended practice, due to both lost security protections and future iOS compatibility. To disable ATS, insert the following in your app’s Info.plist file:

```

1
2
3
4
5

```
 | 
```
<key>NSAppTransportSecurity</key>
<dict>
 <key>NSAllowsArbitraryLoads</key>
 <true/>
</dict>

```
 | 

## Decoding URLs

The SDK percent-encodes links to create valid URLs. All link characters that are not allowed in a properly formed URL, such as Unicode characters, will be percent escaped.

To decode an encoded link, use the String property removingPercentEncoding. You must also return true in the BrazeDelegate.braze(_:shouldOpenURL:). A call to action is required to trigger the handling of the URL by your app. For example, in your scene:openURLContexts: handler from Step 3:

- swift
 
- objective-c

```

1
2
3
4
5

```
 | 
```
 func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
 guard let url = URLContexts.first?.url else { return }
 let urlString = url.absoluteString.removingPercentEncoding
 // Handle urlString
 }

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
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
 NSURL *url = URLContexts.allObjects.firstObject.URL;
 NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
 // Handle urlString
}

```
 | 

## Deep linking to app settings

You can take advantage of UIApplicationOpenSettingsURLString to deep link users to your app’s settings from Braze push notifications and in-app messages.

To take users from your app into the iOS settings:

- First, make sure your application is set up for either scheme-based deep links or universal links.
 
- Decide on a URI for deep linking to the Settings page (for example, myapp://settings or https://www.braze.com/settings).
 
- If you are using custom scheme-based deep links, add the following code to your scene:openURLContexts: handler:

- swift
 
- objective-c

```

1
2
3
4
5
6

```
 | 
```
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
 guard let path = URLContexts.first?.url.path else { return }
 if (path == "settings") {
 UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
 }
}

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

```
 | 
```
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
 NSString *path = [URLContexts.allObjects.firstObject.URL path];
 if ([path isEqualToString:@"settings"]) {
 NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
 [[UIApplication sharedApplication] openURL:settingsURL];
 }
}

```
 | 

## Customization options

### Default WebView customization

The Braze.WebViewController class displays web URLs opened by the SDK, typically when “Open Web URL Inside App” is selected for a web deep link.

You can customize the Braze.WebViewController through the BrazeDelegate.braze(_:willPresentModalWithContext:) delegate method.

### Linking handling customization

The BrazeDelegate protocol can be used to customize the handling of URLs such as deep links, web URLs, and universal links. To set the delegate during Braze initialization, set a delegate object on the Braze instance. Braze will then call your delegate’s implementation of shouldOpenURL before handling any URIs.

When a push notification or in-app message uses Open web URL inside mobile app, Braze passes context.useWebView == true on Braze.URLContext. When the message opens the URL in the system browser instead, useWebView is false. Inspect context.useWebView in braze(_:shouldOpenURL:) to branch your custom handling—for example, to open an in-app WebViewController only when the campaign requested in-app display.

#### Universal links

Braze supports universal links in push notifications, in-app messages, and Content Cards. To enable universal link support, configuration.forwardUniversalLinks must be set to true.

When enabled, Braze will forward universal links to your SceneDelegate through the scene:continue: method for apps that have adopted the UIScene life cycle (required for apps built with Xcode 27 and later), or to your AppDelegate through application:continueUserActivity:restorationHandler: otherwise.

Your application also needs to be set up to handle universal links. Refer to Apple’s documentation to ensure your application is configured correctly for universal links.

warning

Universal link forwarding requires access to the application entitlements. When running the application in a simulator, these entitlements are not directly available and universal links are not forwarded to the system handlers.
To add support to simulator builds, you can add the application .entitlements file to the Copy Bundle Resources build phase. See forwardUniversalLinks documentation for more details.

note

The SDK does not query your domains’ apple-app-site-association file. It performs the differentiation between universal links and regular URLs by looking at the domain name only. As a result, the SDK does not respect any exclusion rule defined in the apple-app-site-association per Supporting associated domains.

## Examples

### BrazeDelegate

Here’s an example using BrazeDelegate. For more information, see Braze Swift SDK reference.

- swift
 
- objective-c

```

1
2
3
4
5
6
7
8

```
 | 
```
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
 if context.url.host == "MY-DOMAIN.com" {
 // Custom handle link here
 return false
 }
 // Let Braze handle links otherwise
 return true
}

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

```
 | 
```
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
 if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
 // Custom handle link here
 return NO;
 }
 // Let Braze handle links otherwise
 return YES;
}

```
 | 

## Prerequisites

- ios
 
- android

Before you can implement deep linking into your Flutter iOS app, configure your URL schemes in your Info.plist file. For details, refer to Deep linking for iOS.

For Flutter Android, no additional native setup is required if you’re handling deep links on the Dart layer. The minimal implementation shown in this article is sufficient for most Flutter apps.

warning

Braze’s native com_braze_handle_push_deep_links_automatically flag defaults to false on Android. Without setting it to true in your braze.xml, your app isn’t automatically brought to the foreground or routed to the deep link destination when a user taps a push notification, even though a push_opened event still reaches your Dart listener. For more information, see Add deep links (Android).

If you need advanced native-layer link handling (such as custom IBrazeDeeplinkHandler implementations), refer to Deep linking for Android.

## Implementing deep linking

### Step 1: Set up Flutter’s built-in handling

- ios
 
- android

- In your Xcode project, open your Info.plist file.
 
- Add a new key-value pair.
 
- Set the key to FlutterDeepLinkingEnabled.
 
- Set the type to Boolean.
 
- Set the value to YES.

- In your Android Studio project, open your AndroidManifest.xml file.
 
- Locate .MainActivity in your activity tags.
 
- Within the activity tag, add the following meta-data tag:

```

1

```
 | 
```
 <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />

```
 | 

### Step 2: Forward data to the Dart layer (optional)

You can use native, first-party, or third-party link handling for complex use cases, such as sending a user to a specific location in your app, or calling a specific function.

#### Example: Deep linking to an alert dialog

note

While the following example does not rely on additional packages, you can use a similar approach to implement native, first-party, or third-party packages, such as go_router. Additional Dart code may be required.

First, a method channel is used in the native layer to forward the deep link’s URL string data to the Dart layer.

- ios
 
- android

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
25

```
 | 
```
extension AppDelegate {
 
 // Delegate method for handling custom scheme links.
 override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
 forwardURL(url)
 return true
 }
 
 // Delegate method for handling universal links.
 override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
 guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
 let url = userActivity.webpageURL else {
 return false
 }
 forwardURL(url)
 return true
 }

 private func forwardURL(_ url: URL) {
 guard let controller: FlutterViewController = window?.rootViewController as? FlutterViewController else { return }
 let deepLinkChannel = FlutterMethodChannel(name: "deepLinkChannel", binaryMessenger: controller.binaryMessenger)
 deepLinkChannel.invokeMethod("receiveDeepLink", arguments: url.absoluteString)
 }

}

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
class MainActivity : FlutterActivity() {

 override fun onCreate(savedInstanceState: Bundle?) {
 super.onCreate(savedInstanceState)
 handleDeepLink(intent)
 }

 override fun onNewIntent(intent: Intent) {
 super.onNewIntent(intent)
 handleDeepLink(intent)
 }

 private fun handleDeepLink(intent: Intent) {
 val binaryMessenger = flutterEngine?.dartExecutor?.binaryMessenger
 if (intent?.action == Intent.ACTION_VIEW && binaryMessenger != null) {
 MethodChannel(binaryMessenger, "deepLinkChannel")
 .invokeMethod("receivedDeepLink", intent?.data.toString())
 }
 }

}

```
 | 

Next, a callback function is used in the Dart layer to display an alert dialogue using the URL string data sent previously.

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

```
 | 
```
MethodChannel('deepLinkChannel').setMethodCallHandler((call) async {
 deepLinkAlert(call.arguments, context);
});

void deepLinkAlert(String link, BuildContext context) {
 showDialog(
 context: context,
 builder: (BuildContext context) {
 return AlertDialog(
 title: Text("Deep Link Alert"),
 content: Text("Opened with deep link: $link"),
 actions: <Widget>[
 TextButton(
 child: Text("Close"),
 onPressed: () {
 Navigator.of(context).pop();
 },
 ),
 ],
 );
 },
 );
}

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Cordova Braze SDK.

## Enabling push deep linking

By default, the Braze Cordova SDK doesn’t automatically handle push deep linking from notifications. To enable push deep linking, add the following preferences to the platform element in your project’s config.xml file.

- ios
 
- android

```

1
2
3

```
 | 
```
<platform name="ios">
 <preference name="com.braze.ios_forward_universal_links" value="YES" />
</platform>

```
 | 

```

1
2
3

```
 | 
```
<platform name="android">
 <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
</platform>

```
 | 

To customize back stack behavior when deep links are followed, you can also add these optional preferences:

```

1
2
3
4
5

```
 | 
```
<platform name="android">
 <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
 <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
 <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>

```
 | 

For a full list of available push configuration options, see Optional configurations.

- 

New Stuff!
