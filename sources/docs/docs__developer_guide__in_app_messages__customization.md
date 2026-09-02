---
url: https://www.braze.com/docs/developer_guide/in_app_messages/customization
slug: docs__developer_guide__in_app_messages__customization
title: "Customize in-app messages"
description: "Learn how to set up in-app messages for the Braze SDK."
section: developer_guide/in_app_messages
fetched: 2026-09-02
evidence: company-own (technical)
---
# Customize in-app messages

Learn how to customize in-app messages for the Braze SDK. For advanced styling techniques, check out our tutorial for customizing message styling using key-value pairs.

- web
 
- android
 
- swift
 
- react native
 
- unity

## Prerequisites

Before you can use this feature, you’ll need to integrate the Web Braze SDK.

## Custom styles

Braze UI elements come with a default look and feel that create a neutral in-app message experience and aim for consistency with other Braze mobile platforms. The default Braze styles are defined in CSS within the Braze SDK.

### Setting a default style

By overriding selected styles in your application, you can customize our standard in-app message types with your own background images, font families, styles, sizes, animations, and more.

For instance, the following is an example override that will cause an in-app message’s headers to appear italicized:

```

1
2
3

```
 | 
```
 body .ab-in-app-message .ab-message-header {
 font-style: italic;
 }

```
 | 

See the JSDocs for more information.

### Customizing the z-index

By default, in-app messages are displayed using z-index: 9001. This is configurable using the inAppMessageZIndex initialization option in the scenario that your website styles elements with higher values than that.

```

1
2
3
4

```
 | 
```
braze.initialize("YOUR-API-KEY", {
 baseUrl: "YOUR-API-ENDPOINT",
 inAppMessageZIndex: 12000
});

```
 | 

important

This feature is only available for Web Braze SDK v3.3.0 and later.

## Customizing message dismissals

By default, when an in-app message is showing, pressing the escape button or a click on the grayed-out background of the page will dismiss the message. Configure the requireExplicitInAppMessageDismissal initialization option to true to prevent this behavior and require an explicit button click to dismiss messages.

```

1
2
3
4
5

```
 | 
```
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
 baseUrl: "YOUR-API-ENDPOINT",
 requireExplicitInAppMessageDismissal: true
});

```
 | 

## Customizing display timing

To override the default display timing, remove calls to braze.automaticallyShowInAppMessages() and handle messages in braze.subscribeToInAppMessage(). Register your callback before braze.openSession(), so you can intercept session-start messages and decide whether to display or defer each message.

By default, Braze displays in-app messages when they are triggered and eligible to display. If you need different behavior for your app experience, use a custom callback to defer or display messages based on your own logic.

The following example shows how to subscribe to triggered in-app messages, defer selected messages, and display deferred messages later:

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
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
 baseUrl: "YOUR-API-ENDPOINT"
});

braze.subscribeToInAppMessage(function (message) {
 // Control-group messages should always be "shown" to log analytics.
 if (message.isControl || message instanceof braze.ControlMessage) {
 braze.showInAppMessage(message);
 return;
 }

 const shouldDefer = true; // Replace with your own display logic

 if (shouldDefer) {
 braze.deferInAppMessage(message);
 return;
 }

 braze.showInAppMessage(message);
});

braze.openSession();

// Later, when your app is ready to display a deferred message:
const deferredMessage = braze.getDeferredInAppMessage();
if (deferredMessage) {
 braze.showInAppMessage(deferredMessage);
}

```
 | 

For related delivery customization guidance, see:

- Web deferInAppMessage reference
 
- Web subscribeToInAppMessage reference

## Opening links in a new tab

To set your in-app message links to open in a new tab, set the openInAppMessagesInNewTab option to true to force all links from in-app message clicks open in a new tab or window.

```

1

```
 | 
```
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Android Braze SDK. You’ll also need to set up in-app messages.

## Setting custom manager listeners

- global listener
 
- html listener

While the BrazeInAppMessageManager listener can automatically handle the display and lifecycle of in-app messages, you’ll need to implement a custom manager listener if you’d like to fully customize your messages.

The Braze SDK has a default DefaultHtmlInAppMessageActionListener class that is used if no custom listener is defined and takes appropriate action automatically. If you require more control over how a user interacts with different buttons inside a custom HTML in-app message, implement a custom IHtmlInAppMessageActionListener class.

This listener applies to both messages built with custom HTML and messages created using the Drag-and-Drop (DnD) editor. It does not apply to traditional IAMs. Traditional IAMs are Braze’s built-in, SDK-rendered message types (for example, slideup, modal, and full) created in the original in-app message composer using predefined layouts. Unlike custom HTML and DnD IAMs, they do not run through the HTML action listener flow.

If you set a custom IHtmlInAppMessageActionListener, its logic will override the default click behavior for all DnD messages. Please ensure your marketing team is aware of this, as it may affect their campaigns in unexpected ways.

### Step 1: Implement the custom manager listener

- global listener
 
- html listener

#### Step 1.1: Implement IInAppMessageManagerListener

Create a class that implements IInAppMessageManagerListener.

The callbacks in your IInAppMessageManagerListener will also be called at various points in the in-app message lifecycle. For example, if you set a custom manager listener when an in-app message is received from Braze, the beforeInAppMessageDisplayed() method will be called. If your implementation of this method returns InAppMessageOperation.DISCARD, that signals to Braze that the in-app message will be handled by the host app and should not be displayed by Braze. If InAppMessageOperation.DISPLAY_NOW is returned, Braze will attempt to display the in-app message. This method should be used if you choose to display the in-app message in a customized manner.

IInAppMessageManagerListener also includes delegate methods for message clicks and buttons, which can be used in cases like intercepting a message when a button or message is clicked for further processing.

#### Step 1.2: Hook into IAM view lifecycle methods (optional)

The IInAppMessageManagerListener interface has in-app message view methods called at distinct points in the in-app message view lifecycle. These methods are called in the following order:

- beforeInAppMessageViewOpened: Called just before the in-app message is added to the activity’s view. The in-app message is not yet visible to the user at this time.
 
- afterInAppMessageViewOpened: Called just after the in-app message is added to the activity’s view. The in-app message is now visible to the user at this time.
 
- beforeInAppMessageViewClosed: Called just before the in-app message is removed from the activity’s view. The in-app message is still visible to the user at this time.
 
- afterInAppMessageViewClosed: Called just after the in-app message is removed from the activity’s view. The in-app message is no longer visible to the user at this time.

Note that the time between afterInAppMessageViewOpened and beforeInAppMessageViewClosed is when the in-app message view is on screen, visible to the user.

note

Implementation of these methods is not required. They’re only provided to track and inform the in-app message view lifecycle. You can leave these method implementations empty.

Create a class that implements IHtmlInAppMessageActionListener.

The callbacks in your IHtmlInAppMessageActionListener will be called whenever the user initiates any of the following actions inside the HTML in-app message:

- Clicks on the close button
 
- Fires a custom event
 
- Clicks on a URL inside HTML in-app message

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

```
 | 
```
public class CustomHtmlInAppMessageActionListener implements IHtmlInAppMessageActionListener {
 private final Context mContext;

 public CustomHtmlInAppMessageActionListener(Context context) {
 mContext = context;
 }

 @Override
 public void onCloseClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
 Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show();
 BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
 }

 @Override
 public boolean onCustomEventFired(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
 Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show();
 return true;
 }

 @Override
 public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
 Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
 BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
 return true;
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

```
 | 
```
class CustomHtmlInAppMessageActionListener(private val mContext: Context) : IHtmlInAppMessageActionListener {

 override fun onCloseClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle) {
 Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show()
 BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
 }

 override fun onCustomEventFired(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
 Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show()
 return true
 }

 override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
 Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
 BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
 return true
 }
}

```
 | 

### Step 2: Instruct Braze to use the custom manager listener

- global listener
 
- html listener

After you create IInAppMessageManagerListener, call BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener() to instruct BrazeInAppMessageManager
to use your custom IInAppMessageManagerListener instead of the default listener. Do this in your Application.onCreate() before any other calls to Braze, so the custom listener is set before any in-app messages are displayed.

#### Altering in-app messages before display

When a new in-app message is received, and there is already an in-app message being displayed, the new message will be put onto the top of the stack and can be displayed at a later time.

However, if there is no in-app message being displayed, the following delegate method in IInAppMessageManagerListener will be called:

- java
 
- kotlin

```

1
2
3
4

```
 | 
```
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
 return InAppMessageOperation.DISPLAY_NOW;
}

```
 | 

```

1
2
3

```
 | 
```
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
 return InAppMessageOperation.DISPLAY_NOW
}

```
 | 

The InAppMessageOperation() return value can control when the message should be displayed. The suggested usage of this method would be to delay messages in certain parts of the app by returning DISPLAY_LATER when in-app messages would be distracting to the user’s app experience.

 InAppMessageOperation return value | 
 Behavior | 

 DISPLAY_NOW | 
 The message will be displayed | 

 DISPLAY_LATER | 
 The message will be returned to the stack and displayed at the next available opportunity | 

 DISCARD | 
 The message will be discarded | 

 null | 
 The message will be ignored. This method should NOT return null | 

See InAppMessageOperation for more details.

tip

If you choose to DISCARD the in-app message and replace it with your in-app message view, you will need to log in-app message clicks and impressions manually.

On Android, this is done by calling logClick and logImpression on in-app messages and logButtonClick on immersive in-app messages.

tip

Once an in-app message has been placed on the stack, you can request for it to be retrieved and displayed at any time by calling BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage(). This method requests Braze to display the next available in-app message from the stack.

After your IHtmlInAppMessageActionListener is created, call BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener() to instruct BrazeInAppMessageManager to use your custom IHtmlInAppMessageActionListener instead of the default action listener.

We recommend setting your IHtmlInAppMessageActionListener in your Application.onCreate() before any other calls to Braze. This will set the custom action listener before any in-app message is displayed:

- java
 
- kotlin

```

1

```
 | 
```
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));

```
 | 

```

1

```
 | 
```
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))

```
 | 

## Setting custom factories

You can override a number of defaults through custom factory objects. These can be registered with the Braze SDK as needed to achieve the desired results. However, if you decide to override a factory, you’ll likely need to explicitly defer to the default or reimplement the functionality provided by the Braze default. The following code snippet illustrates how to supply custom implementations of the IInAppMessageViewFactory and the IInAppMessageViewWrapperFactory interfaces.

- kotlin
 
- java

In-app message types

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
class BrazeDemoApplication : Application(){
 override fun onCreate() {
 super.onCreate()
 registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(true, true))
 BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
 BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
 }
}

```
 | 

In-app message types

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
public class BrazeDemoApplication extends Application {
 @Override
 public void onCreate{
 super.onCreate();
 registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(true, true));
 BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
 BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(new CustomInAppMessageViewFactory());
 }
}

```
 | 

- view
 
- view wrapper
 
- animation

Braze in-app message types are versatile enough to cover most custom use cases. However, if you want to fully define the visual appearance of your in-app messages instead of using a default type, Braze makes this possible by setting a custom view factory.

The BrazeInAppMessageManager automatically handles placing the in-app message model into the existing activity view hierarchy by default using DefaultInAppMessageViewWrapper. If you need to customize how in-app messages are placed into the view hierarchy, you should use a custom IInAppMessageViewWrapperFactory.

In-app messages have preset animation behavior. Slideup messages slide into the screen; full and modal messages fade in and out. If you want to define custom animation behaviors for your in-app messages, Braze makes this possible by setting up a custom animation factory.

### Step 1: Implement the factory

- view
 
- view wrapper
 
- animation

Create a class that implements IInAppMessageViewFactory:

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

```
 | 
```
public class CustomInAppMessageViewFactory implements IInAppMessageViewFactory {
 @Override
 public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
 // Uses a custom view for slideups, modals, and full in-app messages.
 // HTML in-app messages and any other types will use the Braze default in-app message view factories
 switch (inAppMessage.getMessageType()) {
 case SLIDEUP:
 case MODAL:
 case FULL:
 // Use a custom view of your choosing
 return createMyCustomInAppMessageView();
 default:
 // Use the default in-app message factories
 final IInAppMessageViewFactory defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage);
 return defaultInAppMessageViewFactory.createInAppMessageView(activity, inAppMessage);
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

```
 | 
```
class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
 override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
 // Uses a custom view for slideups, modals, and full in-app messages.
 // HTML in-app messages and any other types will use the Braze default in-app message view factories
 when (inAppMessage.messageType) {
 MessageType.SLIDEUP, MessageType.MODAL, MessageType.FULL ->
 // Use a custom view of your choosing
 return createMyCustomInAppMessageView()
 else -> {
 // Use the default in-app message factories
 val defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage)
 return defaultInAppMessageViewFactory!!.createInAppMessageView(activity, inAppMessage)
 }
 }
 }
}

```
 | 

Create a class that implements IInAppMessageViewWrapperFactory and returns an IInAppMessageViewWrapper.

This factory is called immediately after the in-app message view is created. The easiest way to implement a custom IInAppMessageViewWrapper is just to extend the default DefaultInAppMessageViewWrapper:

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

```
 | 
```
public class CustomInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {
 public CustomInAppMessageViewWrapper(View inAppMessageView,
 IInAppMessage inAppMessage,
 IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
 BrazeConfigurationProvider brazeConfigurationProvider,
 Animation openingAnimation,
 Animation closingAnimation, View clickableInAppMessageView) {
 super(inAppMessageView,
 inAppMessage,
 inAppMessageViewLifecycleListener,
 brazeConfigurationProvider,
 openingAnimation,
 closingAnimation,
 clickableInAppMessageView);
 }

 @Override
 public void open(@NonNull Activity activity) {
 super.open(activity);
 Toast.makeText(activity.getApplicationContext(), "Opened in-app message", Toast.LENGTH_SHORT).show();
 }

 @Override
 public void close() {
 super.close();
 Toast.makeText(mInAppMessageView.getContext().getApplicationContext(), "Closed in-app message", Toast.LENGTH_SHORT).show();
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

```
 | 
```
class CustomInAppMessageViewWrapper(inAppMessageView: View,
 inAppMessage: IInAppMessage,
 inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener,
 brazeConfigurationProvider: BrazeConfigurationProvider,
 openingAnimation: Animation,
 closingAnimation: Animation, clickableInAppMessageView: View) : 
 DefaultInAppMessageViewWrapper(inAppMessageView, 
 inAppMessage, 
 inAppMessageViewLifecycleListener, 
 brazeConfigurationProvider, 
 openingAnimation, 
 closingAnimation, 
 clickableInAppMessageView) {

 override fun open(activity: Activity) {
 super.open(activity)
 Toast.makeText(activity.applicationContext, "Opened in-app message", Toast.LENGTH_SHORT).show()
 }

 override fun close() {
 super.close()
 Toast.makeText(mInAppMessageView.context.applicationContext, "Closed in-app message", Toast.LENGTH_SHORT).show()
 }
}

```
 | 

Create a class that implements IInAppMessageAnimationFactory:

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

```
 | 
```
public class CustomInAppMessageAnimationFactory implements IInAppMessageAnimationFactory {

 @Override
 public Animation getOpeningAnimation(IInAppMessage inAppMessage) {
 Animation animation = new AlphaAnimation(0, 1);
 animation.setInterpolator(new AccelerateInterpolator());
 animation.setDuration(2000L);
 return animation;
 }

 @Override
 public Animation getClosingAnimation(IInAppMessage inAppMessage) {
 Animation animation = new AlphaAnimation(1, 0);
 animation.setInterpolator(new DecelerateInterpolator());
 animation.setDuration(2000L);
 return animation;
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

```
 | 
```
class CustomInAppMessageAnimationFactory : IInAppMessageAnimationFactory {
 override fun getOpeningAnimation(inAppMessage: IInAppMessage): Animation {
 val animation: Animation = AlphaAnimation(0, 1)
 animation.interpolator = AccelerateInterpolator()
 animation.duration = 2000L
 return animation
 }

 override fun getClosingAnimation(inAppMessage: IInAppMessage): Animation {
 val animation: Animation = AlphaAnimation(1, 0)
 animation.interpolator = DecelerateInterpolator()
 animation.duration = 2000L
 return animation
 }
}

```
 | 

### Step 2: Instruct Braze to use the factory

- view
 
- view wrapper
 
- animation

After your IInAppMessageViewFactory is created, call BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory() to instruct BrazeInAppMessageManager
to use your custom IInAppMessageViewFactory instead of the default view factory.

tip

We recommend setting your IInAppMessageViewFactory in your Application.onCreate() before any other calls to Braze. This will set the custom view factory before any in-app message is displayed.

#### How it works

The slideup in-app message view implements IInAppMessageView. The full and modal type message views implement IInAppMessageImmersiveView. Implementing one of these classes allows Braze to add click listeners to your custom view where appropriate. All Braze view classes extend Android’s View class.

Implementing IInAppMessageView allows you to define a certain portion of your custom view as clickable. Implementing IInAppMessageImmersiveView allows you to define message button views and a close button view.

After your IInAppMessageViewWrapper is created, call BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory() to instruct BrazeInAppMessageManager to use your custom IInAppMessageViewWrapperFactory instead of the default view wrapper factory.

We recommend setting your IInAppMessageViewWrapperFactory in your Application.onCreate() before any other calls to Braze. This will set the custom view wrapper factory before any in-app message is displayed:

- java
 
- kotlin

```

1

```
 | 
```
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());

```
 | 

```

1

```
 | 
```
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())

```
 | 

Once your IInAppMessageAnimationFactory is created, call BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory() to instruct BrazeInAppMessageManager
to use your custom IInAppMessageAnimationFactory instead of the default animation factory.

We recommend setting your IInAppMessageAnimationFactory in your Application.onCreate() before any other calls to Braze. This will set the custom animation factory before any in-app message is displayed.

## Custom styles

Braze UI elements come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. This reference article covers custom in-app messaging styling for your Android or FireOS application.

### Setting a default style

You can see default styles in the Braze SDK’s styles.xml file:

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

```
 | 
```
 <style name="Braze"/>
 <style name="Braze.InAppMessage"/>
 <style name="Braze.InAppMessage.Header">
 <item name="android:layout_height">wrap_content</item>
 <item name="android:layout_width">match_parent</item>
 <item name="android:padding">0.0dp</item>
 <item name="android:background">@android:color/transparent</item>
 <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
 <item name="android:textSize">20.0sp</item>
 <item name="android:lineSpacingMultiplier">1.3</item>
 <item name="android:gravity">center</item>
 <item name="android:textStyle">bold</item>
 <item name="android:layout_centerHorizontal">true</item>
 </style>

```
 | 

If you would prefer, you can override these styles to create a look and feel that better suits your app.

To override a style, copy it in its entirety to the styles.xml file in your project and make modifications. The whole style must be copied over to your local styles.xml file for all attributes to be correctly set. Note that these custom styles are for changes to individual UI elements, not wholesale changes to layouts. Layout-level changes need to be handled with custom views.

note

You can customize some colors directly in your Braze campaign without modifying the XML. Keep in mind, colors set in the Braze dashboard will override colors you set anywhere else.

### Customizing the font

You can set a custom font by locating the typeface in the res/font directory. To use it, override the style for message text, headers, and button text and use the fontFamily attribute to instruct Braze to use your custom font family.

For example, to update the font on your in-app message button text, override the Braze.InAppMessage.Button style and reference your custom font family. The attribute value should point to a font family in your res/font directory.

Here is a truncated example with a custom font family, my_custom_font_family, referenced on the last line:

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
 <style name="Braze.InAppMessage.Button">
 <item name="android:layout_height">wrap_content</item>
 ...
 <item name="android:paddingBottom">15.0dp</item>
 <item name="android:fontFamily">@font/my_custom_font_family</item>
 <item name="fontFamily">@font/my_custom_font_family</item>
 </style>

```
 | 

Aside from the Braze.InAppMessage.Button style for button text, the style for message text is Braze.InAppMessage.Message and the style for message headers is Braze.InAppMessage.Header. If you want to use your custom font family across all possible in-app message text, you can set your font family on the Braze.InAppMessage style, which is the parent style for all in-app messages.

important

As with other custom styles, the entire style must be copied over to your local styles.xml file for all attributes to be correctly set.

## Message dismissals

### Swiping to dismiss slideup messages

By default, slideup in-app messages can be dismissed with a swipe gesture. The direction of the swipe depends on the slideup position:

- Left or right swipe: Dismisses the slideup regardless of its position.
 
- Slideup from the bottom: Swiping from top to bottom dismisses the message. Swiping from bottom to top does not dismiss it.
 
- Slideup from the top: Swiping from bottom to top dismisses the message. Swiping from top to bottom does not dismiss it.

This swipe behavior is built into the default DefaultInAppMessageViewWrapper and applies only to slideup in-app messages. Modal and full in-app messages don’t support swipe-to-dismiss. To customize this behavior, you can implement a custom view wrapper factory.

note

Tapping outside of a slideup message does not dismiss it by default. This behavior differs from modal messages, which can be configured for outside tap dismissal. For slideups, use the swipe gesture or the close button to dismiss the message.

### Disabling back button dismissals

By default, the hardware back button dismisses Braze in-app messages. This behavior can be disabled on a per-message basis via BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView().

In the following example, disable_back_button is a custom key-value pair set on the in-app message that signifies whether the message should allow for the back button to dismiss the message:

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

```
 | 
```
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
 @Override
 public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
 super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
 final Map<String, String> extras = inAppMessage.getExtras();
 if (extras != null && extras.containsKey("disable_back_button")) {
 BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
 }
 }

 @Override
 public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
 super.afterInAppMessageViewClosed(inAppMessage);
 BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
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

```
 | 
```
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
 override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
 super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
 val extras = inAppMessage.extras
 if (extras != null && extras.containsKey("disable_back_button")) {
 BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
 }
 }

 override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
 super.afterInAppMessageViewClosed(inAppMessage)
 BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
 }
})

```
 | 

note

Note that if this functionality is disabled, the host activity’s hardware back button default behavior will be used instead. This may lead to the back button closing the application instead of the displayed in-app message.

### Enabling outside tap dismissals

By default, dismissing the modal using an outside tap is set to false. Setting this value to true will result in the modal in-app message being dismissed when the user taps outside of the in-app message. This behavior can be toggled on by calling:

```

1

```
 | 
```
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)

```
 | 

## Customizing the orientation

To set a fixed orientation for an in-app message, first set a custom in-app message manager listener. Then, update the orientation on the IInAppMessage object in the beforeInAppMessageDisplayed() delegate method:

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
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
 // Set the orientation to portrait
 inAppMessage.setOrientation(Orientation.PORTRAIT);
 return InAppMessageOperation.DISPLAY_NOW;
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
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
 // Set the orientation to portrait
 inAppMessage.orientation = Orientation.PORTRAIT
 return InAppMessageOperation.DISPLAY_NOW
}

```
 | 

For tablet devices, in-app messages will appear in the user’s preferred orientation style regardless of actual screen orientation.

## Disabling dark theme

By default, IInAppMessageManagerListener’s beforeInAppMessageDisplayed() checks the system settings and conditionally enables dark theme styling on the message with the following code:

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

```
 | 
```
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
 if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().getApplicationContext())) {
 ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
 }
 return InAppMessageOperation.DISPLAY_NOW;
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
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
 if (inAppMessage is IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().applicationContext!!)) {
 (inAppMessage as IInAppMessageThemeable).enableDarkTheme()
 }
 return InAppMessageOperation.DISPLAY_NOW
}

```
 | 

To change this, you can call enableDarkTheme at any step in the pre-display process to implement your own conditional logic.

## Customizing the Google Play review prompt

Due to the limitations and restrictions set by Google, custom Google Play review prompts are not currently supported by Braze. While some users have been able to integrate these prompts successfully, others have shown low success rates due to Google Play quotas. Integrate at your own risk. Refer to documentation on Google Play in-app review prompts.

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK.

## Setting up the UI delegate (required)

To customize the presentation of in-app messages and react to various lifecycle events, you’ll need to set up BrazeInAppMessageUIDelegate. This is a delegate protocol used for receiving and processing triggered in-app message payloads, receiving display lifecycle events, and controlling display timing. To use BrazeInAppMessageUIDelegate, you must:

- Use the default BrazeInAppMessageUI implementation as your inAppMessagePresenter.
 
- Include the BrazeUI library in your project.

### Step 1: Implement the BrazeInAppMessageUIDelegate protocol

First, implement the BrazeInAppMessageUIDelegate protocol and any corresponding methods you wish. In the following example, this protocol is implemented in the application’s AppDelegate class.

- swift
 
- objective-c

```

1
2
3

```
 | 
```
extension AppDelegate: BrazeInAppMessageUIDelegate {
 // Implement your protocol methods here.
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
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
 // Implement your protocol methods here.
@end

```
 | 

### Step 2: Assign the delegate object

Assign the delegate object on the BrazeInAppMessageUI instance before assigning this in-app message UI as your inAppMessagePresenter.

- swift
 
- objective-c

```

1
2
3

```
 | 
```
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI

```
 | 

```

1
2
3

```
 | 
```
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;

```
 | 

important

Not all delegate methods are available in Objective-C due to the incompatibility of their parameters with the language runtime.

tip

For a step-by-step implementation of the in-app message UI delegate, refer to this tutorial.

## On-click behavior

Each Braze.InAppMessage object contains a corresponding ClickAction, which defines the behavior upon clicking.

### Click action types

The clickAction property on your Braze.InAppMessage defaults to .none but can be set to one of the following values:

 ClickAction | 
 On-Click Behavior | 

 .url(URL, useWebView: Bool) | 
 Opens the given URL in an external browser. If useWebView is set to true, it will open in a web view. | 

 .none | 
 The message will be dismissed when clicked. | 

important

For in-app messages containing buttons, the message clickAction will also be included in the final payload if the click action is added prior to adding the button text.

### Customizing on-click behavior

To customize this behavior, you may modify the clickAction property by referring to the following sample:

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
func inAppMessage(
 _ ui: BrazeInAppMessageUI, 
 prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
 if let newUrl = URL(string: "{your-url}") {
 context.message.clickAction = .url(newUrl, useWebView: true)
 }
}

```
 | 

The inAppMessage(_:prepareWith:) method is not available in Objective-C.

### Handling the custom behavior

The following BrazeInAppMessageUIDelegate delegate method is called when a user clicks an in-app message. This callback is triggered for user-initiated clicks on in-app message buttons and HTML in-app message buttons (links), and a button ID is provided as an optional parameter for these interactions. This callback is not invoked for programmatic clicks triggered through brazeBridge.logClick().

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

```
 | 
```
func inAppMessage(
 _ ui: BrazeInAppMessageUI,
 shouldProcess clickAction: Braze.InAppMessage.ClickAction,
 buttonId: String?,
 message: Braze.InAppMessage,
 view: InAppMessageView
) -> Bool

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
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
 shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
 url:(NSURL *)uri
 buttonId:(NSString *)buttonId
 message:(BRZInAppMessageRaw *)message
 view:(UIView *)view;

```
 | 

This method returns a boolean value to indicate if Braze should continue to execute the click action.

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

```
 | 
```
func inAppMessage(
 _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
 buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
 guard let buttonId,
 let idInt = Int(buttonId)
 else { return true }
 var button: BrazeKit.Braze.InAppMessage.Button? = nil

 switch message {
 case .modal(let modal):
 button = modal.buttons[idInt]

 case .modalImage(let modalImage):
 button = modalImage.buttons[idInt]

 case .full(let full):
 button = full.buttons[idInt]

 case .fullImage(let fullImage):
 button = fullImage.buttons[idInt]

 default:
 break
 }
 
 print(button?.id)
 print(button?.text)
 print(button?.clickAction)

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
9
10
11
12
13
14
15
16

```
 | 
```
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
 shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
 url:(NSURL *)uri
 buttonId:(NSString *)buttonId
 message:(BRZInAppMessageRaw *)message
 view:(UIView *)view {
 NSInteger buttonInt = [buttonId integerValue];

 if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
 BRZInAppMessageRawButton *button = message.buttons[buttonInt];
 NSLog(@"%ld", (long)button.identifier);
 NSLog(@"%@", button.text);
 NSLog(@"%ld", (long)button.clickAction);
 }
 return YES;
}

```
 | 

## Swiping to dismiss slideup messages

By default, slideup in-app messages can be dismissed with a swipe gesture. The direction of the swipe depends on the slideup position:

- Left or right swipe: Dismisses the slideup regardless of its position.
 
- Slideup from the bottom: Swiping from top to bottom dismisses the message. Swiping from bottom to top does not dismiss it.
 
- Slideup from the top: Swiping from bottom to top dismisses the message. Swiping from top to bottom does not dismiss it.

This swipe behavior is built into the default BrazeInAppMessageUI SlideupView and applies only to slideup in-app messages. Modal and full in-app messages don’t support swipe-to-dismiss. To further customize the slideup view, including swipe behavior, you can modify the SlideupView.Attributes or provide a custom view through subclassing.

note

Tapping outside of a slideup message does not dismiss it. For modal or full in-app messages, you can enable outside tap dismissals using the dismissOnBackgroundTap attribute described in the following section.

## Customizing modal dismissals

To enable outside tap dismissals, you can modify the dismissOnBackgroundTap property on the Attributes struct of the in-app message type you wish to customize.

For example, if you wish to enable this feature for modal image in-app messages, you can configure the following:

- swift
 
- objective-c

```

1

```
 | 
```
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true

```
 | 

Customization through Attributes is not available in Objective-C.

The default value is false. This determines if the modal in-app message will be dismissed when the user taps outside of the in-app message.

 DismissModalOnOutsideTap | 
 Description | 

 true | 
 Modal in-app messages will be dismissed on outside tap. | 

 false | 
 Default, modal in-app messages will not be dismissed on outside tap. | 

For more details on in-app message customization, refer to this article.

## Customizing message orientation

You can customize the orientation of your in-app messages. You can set a new default orientation for all messages or set a custom orientation for a single message.

- all messages
 
- single message

To choose a default orientation for all in-app messages, use the inAppMessage(_:prepareWith:) method to set the preferredOrientation property on the PresentationContext.

For example, to set portrait as the default orientation:

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
func inAppMessage(
 _ ui: BrazeInAppMessageUI,
 prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
 context.preferredOrientation = .portrait
}

```
 | 

```

1
2
3
4

```
 | 
```
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
 prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
 context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}

```
 | 

To set the orientation for a single message, modify the orientation property of Braze.InAppMessage:

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
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape

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
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;

```
 | 

After the in-app message is displayed, any device orientation changes while the message is still being displayed will cause the message to rotate with the device (provided it’s supported by the message’s orientation configuration).

The device orientation must also be supported by the in-app message’s orientation property for the message to display. Additionally, the preferredOrientation setting will only be respected if it is included in your application’s supported interface orientations under the Deployment Info section of your target’s settings in Xcode.

note

The orientation is applied only for the presentation of the message. After the device changes orientation, the message view adopts one of the orientations it supports. On smaller devices (iPhones, iPod Touch), setting a landscape orientation for a modal or full in-app message may lead to truncated content.

## Customizing display timing

You can control if an available in-app message will display during certain points of your user experience. If there are situations where you would not want the in-app message to appear, such as during a fullscreen game or on a loading screen, you can delay or discard pending in-app message messages. To control the timing of in-app message, use the inAppMessage(_:displayChoiceForMessage:) delegate method to set the BrazeInAppMessageUI.DisplayChoice property.

- swift
 
- objective-c

```

1
2
3
4

```
 | 
```
func inAppMessage(
 _ ui: BrazeInAppMessageUI,
 displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice

```
 | 

```

1

```
 | 
```
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message

```
 | 

Configure BrazeInAppMessageUI.DisplayChoice to return one of the following values:

 Display Choice | 
 Behavior | 

 .now | 
 The message will be displayed immediately. This is the default value. | 

 .reenqueue | 
 The message will be not be displayed and will be placed back on the top of the stack. | 

 .later | 
 The message will be not be displayed and will be placed back on the top of the stack. (Deprecated, please use .reenqueue) | 

 .discard | 
 The message will be discarded and will not be displayed. | 

tip

For a sample of InAppMessageUI, check out our Swift Braze SDK repository and Objective-C.

## Hiding the status bar

For Full, FullImage and HTML in-app messages, the SDK will hide the status bar by default. For other types of in-app messages, the status bar is left untouched. To configure this behavior, use the inAppMessage(_:prepareWith:) delegate method to set the statusBarHideBehavior property on the PresentationContext. This field takes one of the following values:

 Status Bar Hide Behavior | 
 Description | 

 .auto | 
 The message view decides the status bar hidden state. | 

 .hidden | 
 Always hide the status bar. | 

 .visible | 
 Always display the status bar. | 

## Disabling dark mode

To prevent in-app messages from adopting dark mode styling when the user device has dark mode enabled, implement the inAppMessage(_:prepareWith:) delegate method method. The PresentationContext passed to the method contains a reference to the InAppMessage object to be presented. Each InAppMessage has a themes property containing a dark and light mode theme. If you set the themes.dark property to nil, Braze will automatically present the in-app message using its light theme.

In-app message types with buttons have an additional themes object on their buttons property. To prevent buttons from adopting dark mode styling, you can use map(_:) to create a new array of buttons with a light theme and no dark theme.

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
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54

```
 | 
```
func inAppMessage(
 _ ui: BrazeInAppMessageUI,
 prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
 switch context.message {
 case .slideup:
 guard var slideup = context.message.slideup else { return }
 slideup.themes.dark = nil
 context.message.slideup = slideup
 
 case .modal:
 guard var modal = context.message.modal else { return }
 modal.themes.dark = nil
 modal.buttons = modal.buttons.map {
 var newButton = $0
 newButton.themes = .init(themes: ["light": $0.themes.light])
 return newButton
 }
 context.message.modal = modal
 
 case .modalImage:
 guard var modalImage = context.message.modalImage else { return }
 modalImage.themes.dark = nil
 modalImage.buttons = modalImage.buttons.map {
 var newButton = $0
 newButton.themes = .init(themes: ["light": $0.themes.light])
 return newButton
 }
 context.message.modalImage = modalImage
 
 case .full:
 guard var full = context.message.full else { return }
 full.themes.dark = nil
 full.buttons = full.buttons.map {
 var newButton = $0
 newButton.themes = .init(themes: ["light": $0.themes.light])
 return newButton
 }
 context.message.full = full
 
 case .fullImage:
 guard var fullImage = context.message.fullImage else { return }
 fullImage.themes.dark = nil
 fullImage.buttons = fullImage.buttons.map {
 var newButton = $0
 newButton.themes = .init(themes: ["light": $0.themes.light])
 return newButton
 }
 context.message.fullImage = fullImage
 
 default:
 break
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
31
32

```
 | 
```
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
 prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
 switch (context.message.type) {
 case BRZInAppMessageRawTypeSlideup: {
 NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
 [updatedThemes removeObjectForKey:@"dark"];
 context.message.themes = updatedThemes;
 break;
 }
 case BRZInAppMessageRawTypeModal:
 case BRZInAppMessageRawTypeFull:
 {
 NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
 [updatedThemes removeObjectForKey:@"dark"];
 context.message.themes = updatedThemes;

 NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
 for (BRZInAppMessageRawButton *button in context.message.buttons) {
 BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
 BRZInAppMessageRawButton *newButton = [button mutableCopy];
 newButton.textColor = lightTheme.textColor;
 newButton.backgroundColor = lightTheme.backgroundColor;
 newButton.borderColor = lightTheme.borderColor;
 [updatedButtons addObject:newButton];
 }
 context.message.buttons = updatedButtons;
 break;
 }
 default:
 break;
 }
}

```
 | 

## Customizing the app store review prompt

You can use in-app messages in a campaign to ask users for an App Store review.

note

Because this example prompt overrides default behavior of Braze, we cannot automatically track impressions if it is implemented. You must log your own analytics.

### Step 1: Set the in-app message delegate

First, set the BrazeInAppMessageUIDelegate in your app.

### Step 2: Disable the default App Store review message

Next, implement the inAppMessage(_:displayChoiceForMessage:) delegate method to disable the default App Store review message.

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
9

```
 | 
```
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
 if message.extras["AppStore Review"] != nil,
 let messageUrl = message.clickAction.url {
 UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
 return .discard
 } else {
 return .now
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

```
 | 
```
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
 displayChoiceForMessage:(BRZInAppMessageRaw *)message {
 if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
 [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
 return BRZInAppMessageUIDisplayChoiceDiscard;
 } else {
 return BRZInAppMessageUIDisplayChoiceNow;
 }
}

```
 | 

### Step 3: Create a deep link

In your scene:openURLContexts: handler, add the following code to process the {YOUR-APP-SCHEME}:app-store-review deep link. Note that you will need to import StoreKit to use SKStoreReviewController:

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
9

```
 | 
```
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
 guard let url = URLContexts.first?.url else { return }
 let urlString = url.absoluteString.removingPercentEncoding
 if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
 SKStoreReviewController.requestReview()
 return;
 }
 // Other deep link handling code…
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

```
 | 
```
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
 NSURL *url = URLContexts.allObjects.firstObject.URL;
 NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
 if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
 [SKStoreReviewController requestReview];
 return;
 }
 // Other deep link handling code…
}

```
 | 

### Step 4: Set custom on-click behavior

Next, create an in-app messaging campaign with the following:

- The key-value pair "AppStore Review" : "true"
 
- The on-click behavior set to “Deep Link Into App”, using the deep link {YOUR-APP-SCHEME}:app-store-review.

tip

Apple limits App Store review prompts to a maximum of three times per year for each user, so your campaign should be rate-limited to three times per year per user.

Users may turn off App Store review prompts. As a result, your custom review prompt should not promise that a native App Store review prompt will appear or directly ask for a review.

## Prerequisites

Before you can use this feature, you’ll need to integrate the React Native Braze SDK.

## Methods for logging

You can use these methods by passing your BrazeInAppMessage instance to log analytics and perform actions:

 Method | 
 Description | 

 logInAppMessageClicked(inAppMessage) | 
 Logs a click for the provided in-app message data. | 

 logInAppMessageImpression(inAppMessage) | 
 Logs an impression for the provided in-app message data. | 

 logInAppMessageButtonClicked(inAppMessage, buttonId) | 
 Logs a button click for the provided in-app message data and button ID. | 

 hideCurrentInAppMessage() | 
 Dismisses the currently displayed in-app message. | 

 performInAppMessageAction(inAppMessage) | 
 Performs the action for an in-app message. | 

 performInAppMessageButtonAction(inAppMessage, buttonId) | 
 Performs the action for an in-app message button. | 

## Handling message data

In most cases, you can use the Braze.addListener method to register event listeners to handle data coming from in-app messages.

Additionally, you can access the in-app message data in the JavaScript layer by calling the Braze.subscribeToInAppMessage method to have the SDKs publish an inAppMessageReceived event when an in-app message is triggered. Pass a callback to this method to execute your own code when the in-app message is triggered and received by the listener.

To customize how message data is handled, refer to the following implementation examples:

- basic
 
- advanced

To enhance the default behavior, or if you don’t have access to customize the native iOS or Android code, we recommend that you disable the default UI while still receiving in-app message events from Braze. To disable the default UI, pass false to the Braze.subscribeToInAppMessage method and use the in-app message data to construct your own message in JavaScript. Note that you will need to manually log analytics on your messages if you choose to disable the default UI.

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
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
 console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
 console.log(event.inAppMessage);
 // Use `event.inAppMessage` to construct your own custom message UI.
});

```
 | 

To include more advanced logic to determine whether or not to show an in-app message using the built-in UI, implement in-app messages through the native layer.

warning

Since this is an advanced customization option, note that overriding the default Braze implementation will also nullify the logic to emit in-app message events to your JavaScript listeners. If you wish to still use Braze.subscribeToInAppMessage or Braze.addListener as described in Accessing in-app message data, you will need to handle publishing the events yourself.

- android
 
- ios

Implement the IInAppMessageManagerListener as described in our Android article on Custom Manager Listener. In your beforeInAppMessageDisplayed implementation, you can access the inAppMessage data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

For more on these values, see our Android documentation.

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

```
 | 
```
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
 WritableMap parameters = new WritableNativeMap();
 parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
 getReactNativeHost()
 .getReactInstanceManager()
 .getCurrentReactContext()
 .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
 .emit("inAppMessageReceived", parameters);
 // Note: return InAppMessageOperation.DISCARD if you would like
 // to prevent the Braze SDK from displaying the message natively.
 return InAppMessageOperation.DISPLAY_NOW;
}

```
 | 

### Overriding the default UI delegate

By default, BrazeInAppMessageUI is created and assigned when you initialize the braze instance. BrazeInAppMessageUI is an implementation of the BrazeInAppMessagePresenter protocol and comes with a delegate property that can be used to customize the handling of in-app messages that have been received.

- 
 
Implement the BrazeInAppMessageUIDelegate delegate as described in our iOS in-app message UI tutorial.

- 
 
In the inAppMessage(_:displayChoiceForMessage:) delegate method, you can access the inAppMessage data, send it to the JavaScript layer, and decide to show or not show the native message based on the return value.

For more details on these values, see our iOS documentation.

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

```
 | 
```
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
 displayChoiceForMessage:(BRZInAppMessageRaw *)message {
 // Convert the message to a JavaScript representation.
 NSData *inAppMessageData = [message json];
 NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
 NSDictionary *arguments = @{
 @"inAppMessage" : inAppMessageString
 };

 // Send to JavaScript.
 [self sendEventWithName:@"inAppMessageReceived" body:arguments];

 // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
 // to prevent the Braze SDK from displaying the message natively.
 return BRZInAppMessageUIDisplayChoiceNow;
}

```
 | 

To use this delegate, assign it to brazeInAppMessagePresenter.delegate after initializing the braze instance.

note

BrazeUI can only be imported in Objective-C or Swift. If you are using Objective-C++, you will need to handle this in a separate file.

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
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
 BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
 Braze *braze = [BrazeReactBridge initBraze:configuration];
 ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
 AppDelegate.braze = braze;
}

```
 | 

### Overriding the default native UI

If you wish to fully customize the presentation of your in-app messages at the native iOS layer, conform to the BrazeInAppMessagePresenter protocol and assign your custom presenter following this sample:

```

1
2
3
4

```
 | 
```
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;

```
 | 

## Customizing the display behavior

You can change the display behavior of in-app messages at runtime via the following:

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
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);

```
 | 

## Setting a custom listener

If you require more control over how a user interacts with in-app messages, use a BrazeInAppMessageListener and assign it to Appboy.AppboyBinding.inAppMessageListener. For any delegates you don’t want to use, you can simply leave them as null.

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

```
 | 
```
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
 BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed,
 OnInAppMessageButtonClicked = OnInAppMessageButtonClicked,
 OnInAppMessageClicked = OnInAppMessageClicked,
 OnInAppMessageHTMLClicked = OnInAppMessageHTMLClicked,
 OnInAppMessageDismissed = OnInAppMessageDismissed,
};
Appboy.AppboyBinding.inAppMessageListener = listener;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
 // Executed before an in-app message is displayed.
}

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
 // Executed whenever an in-app message button is clicked.
}

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
 // Executed whenever an in-app message is clicked.
}

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
 // Executed whenever an HTML in-app message is clicked.
}

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
 // Executed whenever an in-app message is dismissed without a click.
}

```
 | 

- 

New Stuff!
