---
url: https://www.braze.com/docs/developer_guide/content_cards/embedding_gifs
slug: docs__developer_guide__content_cards__embedding_gifs
title: "Embed GIFs in Content Cards"
description: "Learn how to embed GIFs into Content Cards using the Braze SDK."
section: developer_guide/content_cards
fetched: 2026-09-02
evidence: company-own (technical)
---
# Embed GIFs in Content Cards

Learn how to embed GIFs into Content Cards using the Braze SDK.

note

For wrapper SDKs not listed, use the relevant native Android or Swift method instead. Keep in mind, the Android and Swift Braze SDKs don’t support animated GIFs natively, so you’ll implement Content Card GIFs using third-party tools instead.

- web
 
- android
 
- swift

GIF support is included by default in the Web SDK integration.

## About GIFs

Braze offers the ability to use a custom image library to display animated GIFs. Although the following example uses Glide, any image library that supports GIFs is compatible.

## Integrating a custom image library

### Step 1: Creating the image loader delegate

The Image Loader delegate must implement the following methods:

- getInAppMessageBitmapFromUrl()
 
- getPushBitmapFromUrl()
 
- renderUrlIntoCardView()
 
- renderUrlIntoInAppMessageView()
 
- setOffline()

The following integration example is taken from the Glide integration sample app included with the Braze Android SDK.

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
55
56
57
58
59
60
61
62
63
64
65
66

```
 | 
```
import com.braze.support.BrazeLogger;
import com.bumptech.glide.load.resource.gif.GifDrawable;
import android.graphics.drawable.Drawable;

public class GlideBrazeImageLoader implements IBrazeImageLoader {
 private static final String TAG = GlideBrazeImageLoader.class.getName();

 private RequestOptions mRequestOptions = new RequestOptions();

 @Override
 public void renderUrlIntoCardView(Context context, Card card, String imageUrl, ImageView imageView, BrazeViewBounds viewBounds) {
 renderUrlIntoView(context, imageUrl, imageView);
 }

 @Override
 public void renderUrlIntoInAppMessageView(Context context, IInAppMessage inAppMessage, String imageUrl, ImageView imageView, BrazeViewBounds viewBounds) {
 renderUrlIntoView(context, imageUrl, imageView);
 }

 @Override
 public Bitmap getPushBitmapFromUrl(Context context, Bundle extras, String imageUrl, BrazeViewBounds viewBounds) {
 return getBitmapFromUrl(context, imageUrl, viewBounds);
 }

 @Override
 public Bitmap getInAppMessageBitmapFromUrl(Context context, IInAppMessage inAppMessage, String imageUrl, BrazeViewBounds viewBounds) {
 return getBitmapFromUrl(context, imageUrl, viewBounds);
 }

 private void renderUrlIntoView(Context context, String imageUrl, ImageView imageView) {
 try {
 final Drawable drawable = Glide.with(context)
 .load(imageUrl)
 .apply(mRequestOptions)
 .submit()
 .get();

 imageView.post(() -> {
 imageView.setImageDrawable(drawable);
 if (drawable instanceof GifDrawable) {
 ((GifDrawable) drawable).start();
 }
 });
 } catch (Exception e) {
 BrazeLogger.e(TAG, "Failed to render URL into view: " + imageUrl, e);
 }
 }

 private Bitmap getBitmapFromUrl(Context context, String imageUrl, BrazeViewBounds viewBounds) {
 try {
 return Glide.with(context)
 .asBitmap()
 .apply(mRequestOptions)
 .load(imageUrl).submit().get();
 } catch (Exception e) {
 Log.e(TAG, "Failed to retrieve bitmap at url: " + imageUrl, e);
 }
 return null;
 }

 @Override
 public void setOffline(boolean isOffline) {
 // If the loader is offline, then we should only be retrieving from the cache
 mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline);
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
55
56
57
58
59
60
61
62
63

```
 | 
```
import com.braze.support.BrazeLogger
import com.bumptech.glide.load.resource.gif.GifDrawable

class GlideBrazeImageLoader : IBrazeImageLoader {
 companion object {
 private val TAG = GlideBrazeImageLoader::class.qualifiedName
 }

 private var mRequestOptions = RequestOptions()

 override fun renderUrlIntoCardView(context: Context, card: Card, imageUrl: String, imageView: ImageView, viewBounds: BrazeViewBounds) {
 renderUrlIntoView(context, imageUrl, imageView)
 }

 override fun renderUrlIntoInAppMessageView(context: Context, inAppMessage: IInAppMessage, imageUrl: String, imageView: ImageView, viewBounds: BrazeViewBounds) {
 renderUrlIntoView(context, imageUrl, imageView)
 }

 override fun getPushBitmapFromUrl(context: Context, extras: Bundle, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
 return getBitmapFromUrl(context, imageUrl, viewBounds)
 }

 override fun getInAppMessageBitmapFromUrl(context: Context, inAppMessage: IInAppMessage, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
 return getBitmapFromUrl(context, imageUrl, viewBounds)
 }

 private fun renderUrlIntoView(context: Context, imageUrl: String, imageView: ImageView) {
 try {
 val drawable = Glide.with(context)
 .load(imageUrl)
 .apply(mRequestOptions)
 .submit()
 .get()

 imageView.post {
 imageView.setImageDrawable(drawable)
 if (drawable is GifDrawable) {
 drawable.start()
 }
 }
 } catch (e: Exception) {
 BrazeLogger.e(TAG, "Failed to render URL into view: $imageUrl", e)
 }
 }

 private fun getBitmapFromUrl(context: Context, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
 try {
 return Glide.with(context)
 .asBitmap()
 .apply(mRequestOptions)
 .load(imageUrl).submit().get()
 } catch (e: Exception) {
 Log.e(TAG, "Failed to retrieve bitmap at url: $imageUrl", e)
 }

 return null
 }

 override fun setOffline(isOffline: Boolean) {
 // If the loader is offline, then we should only be retrieving from the cache
 mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline)
 }
}

```
 | 

### Fixing image loading for Android SDK 36.0.0 and later

In Android SDK 36.0.0 and later, displayInAppMessage() is a suspend function. This means renderUrlIntoInAppMessageView() runs on a background thread instead of the main thread.

If your custom image loader calls Glide.into(imageView) in renderUrlIntoInAppMessageView(), your app can fail with “You must call this method on the main thread.”

To avoid this:

- Load the image on the background thread with submit().get().
 
- Post the UI update to the main thread with imageView.post { ... }.
 
- If the loaded result is a GIF drawable, start the animation after setting it on the view.

This separates image loading from UI rendering, and keeps your custom image loader compatible with Android SDK 36.0.0 and later.

This guidance applies to Android custom image loaders. Web in-app messages support GIFs out of the box.

The following Kotlin sample uses placeholder values to show this pattern:

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
private const val TAG = "SampleGlideLoader"
private const val glideBrazeImageLoaderTag = "sample-loader"

private fun renderUrlIntoView(
 context: Context,
 imageUrl: String,
 imageView: ImageView
) {
 try {
 val drawable: Drawable = Glide.with(context)
 .load(imageUrl)
 .apply(mRequestOptions)
 .submit()
 .get()

 imageView.post {
 imageView.setImageDrawable(drawable)
 if (drawable is GifDrawable) {
 drawable.start()
 }
 }
 } catch (e: Exception) {
 Log.e(TAG, "$glideBrazeImageLoaderTag renderUrlIntoView failed: url=$imageUrl", e)
 }
}

```
 | 

### Step 2: Setting the image loader delegate

The Braze SDK will use any custom image loader set with IBrazeImageLoader. We recommend setting the custom image loader in a custom application subclass:

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
public class GlideIntegrationApplication extends Application {
 @Override
 public void onCreate() {
 super.onCreate();
 Braze.getInstance(context).setImageLoader(new GlideBrazeImageLoader());
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

```
 | 
```
class GlideIntegrationApplication : Application() {
 override fun onCreate() {
 super.onCreate()
 Braze.getInstance(context).imageLoader = GlideBrazeImageLoader()
 }
}

```
 | 

### Troubleshooting Glide image loads

If images stop loading after you set a custom IBrazeImageLoader (for example with Glide), check whether a global OkHttp interceptor adds authentication headers to every request.

The Glide sample on this page uses the same load path for Content Cards, in-app messages, and push. Braze-hosted images are CDN URLs and do not use your REST API authentication. Scope interceptors to your own API hosts, or exclude Braze image hosts. A Content Card image that fails after a Glide integration is a common symptom of this interceptor pattern.

## Custom Image Loading with Jetpack Compose

To override image loading with Jetpack Compose, you can pass in a value to imageComposable. This function will take a Card and render the image and the modifiers needed. Alternatively, you can use customCardComposer of ContentCardsList to render the entire card.

In the following example, Glide’s Compose library is used for the cards listed in the imageComposable function:

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
55
56
57

```
 | 
```
ContentCardsList(
 cardStyle = ContentCardStyling(
 imageComposable = { card ->
 when (card.cardType) {
 CardType.CAPTIONED_IMAGE -> {
 val captionedImageCard = card as CaptionedImageCard
 GlideImage(
 modifier = Modifier
 .fillMaxWidth()
 .wrapContentHeight()
 .run {
 if (captionedImageCard.aspectRatio > 0) {
 aspectRatio(captionedImageCard.aspectRatio)
 } else {
 this
 }
 },
 contentScale = ContentScale.Crop,
 model = captionedImageCard.url,
 loading = placeholder(R.drawable.pushpin),
 contentDescription = ""
 )
 }
 CardType.IMAGE -> {
 val imageOnlyCard = card as ImageOnlyCard
 GlideImage(
 modifier = Modifier
 .fillMaxWidth()
 .run {
 if (imageOnlyCard.aspectRatio > 0) {
 aspectRatio(imageOnlyCard.aspectRatio)
 } else {
 this
 }
 },
 contentScale = ContentScale.Crop,
 model = imageOnlyCard.url,
 loading = placeholder(R.drawable.pushpin),
 contentDescription = ""
 )
 }
 CardType.SHORT_NEWS -> {
 val shortNews = card as ShortNewsCard
 GlideImage(
 modifier = Modifier
 .width(100.dp)
 .height(100.dp),
 model = shortNews.url,
 loading = placeholder(R.drawable.pushpin),
 contentDescription = ""
 )
 }
 else -> Unit
 }
 }
 )
)

```
 | 

## Prerequisites

Before you can use this feature, you’ll need to integrate the Swift Braze SDK.

## Integrating a custom image library

### Step 1: Integrate SDWebImage

Integrate the SDWebImage repository into your Xcode project.

### Step 2: Create a new Swift file

In your Xcode project, create a new file named SDWebImageGIFViewProvider.swift and import the following:

```

1
2
3

```
 | 
```
import UIKit
import BrazeUI
import SDWebImage

```
 | 

### Step 3: Add GIFViewProvider

Next, add our sample SDWebImage GIFViewProvider. Your file should be similar to the following:

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
import UIKit
import BrazeUI
import SDWebImage

extension GIFViewProvider {

 /// A GIF view provider using [SDWebImage](https://github.com/SDWebImage/SDWebImage) as a
 /// rendering library.
 public static let sdWebImage = Self(
 view: { SDAnimatedImageView(image: image(for: $0)) },
 updateView: { ($0 as? SDAnimatedImageView)?.image = image(for: $1) }
 )

 private static func image(for url: URL?) -> UIImage? {
 guard let url else { return nil }
 return url.pathExtension == "gif"
 ? SDAnimatedImage(contentsOfFile: url.path)
 : UIImage(contentsOfFile: url.path)
 }

}

```
 | 

### Step 4: Modify your AppDelegate.swift

In your project’s AppDelegate.swift, add GIF support to your BrazeUI components using GIFViewProvider. Your file should be similar to the following:

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
import UIKit
import BrazeKit
import BrazeUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

 static var braze: Braze? = nil

 func application(
 _ application: UIApplication,
 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
 ) -> Bool {
 /* ... */

 GIFViewProvider.shared = .sdWebImage

 return true
 }
}

```
 | 

- 

New Stuff!
