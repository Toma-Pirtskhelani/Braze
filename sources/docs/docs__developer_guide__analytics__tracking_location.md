---
url: https://www.braze.com/docs/developer_guide/analytics/tracking_location
slug: docs__developer_guide__analytics__tracking_location
title: "Track location"
description: "Learn how to track location through the Braze SDK."
section: developer_guide/analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Track location

Learn how to track location through the Braze SDK.

- web
 
- android
 
- swift
 
- react native

## Logging the current location

To get a user’s current location, use the geolocation API’s getCurrentPosition() method. This immediately prompts the user to allow or disallow tracking (unless they’ve already done so).

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

```
 | 
```
import * as braze from "@braze/web-sdk";
function success(position) {
 var coords = position.coords;
 braze.getUser().setLastKnownLocation(
 coords.latitude,
 coords.longitude,
 coords.accuracy,
 coords.altitude,
 coords.altitudeAccuracy
 );
}

navigator.geolocation.getCurrentPosition(success);

```
 | 

Now when data is sent to Braze, the SDK can automatically detect the user’s country using their IP address. For more information, see setLastKnownLocation().

## Continuously tracking the location

To continuously track a user’s location during a page load, use the geolocation API’s watchPosition() method. Calling this method immediately prompts the user to allow or disallow tracking (unless they’ve already done so).

If they opt-in, a success callback is invoked every time their location is updated.

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
function success(position) {
 var coords = position.coords;
 braze.getUser().setLastKnownLocation(
 coords.latitude,
 coords.longitude,
 coords.accuracy,
 coords.altitude,
 coords.altitudeAccuracy
 );
}

navigator.geolocation.watchPosition(success);

```
 | 

important

To learn how to disable continuous tracking, refer to the Mozilla developer docs.

## Logging the current location

Even if continuous tracking is disabled, you can manually log the user’s current location using the setLastKnownLocation() method.

- java
 
- kotlin

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
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
 @Override
 public void onSuccess(BrazeUser brazeUser) {
 brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
 }
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
Braze.getInstance(context).getCurrentUser { brazeUser ->
 brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}

```
 | 

## Continuously tracking the location

important

Starting with Android Marshmallow, you must prompt your users to explicitly opt-in to location tracking. Once they do, Braze can start tracking their location at the beginning of the next session. This is unlike earlier versions of Android, where only declaring location permissions in your AndroidManifest.xml was required.

To continuously track a user’s location, you’ll need to declare your app’s intent to collect location data by adding at least one of the following permissions to your AndroidManifest.xml file.

 Permission | 
 Description | 

 ACCESS_COARSE_LOCATION | 
 Uses the most battery-efficient, non-GPS provider (such as a home network). Typically, this is sufficient for most location-data needs. Under the runtime permissions model, granting location permission implicitly authorizes the collection of fine location data. | 

 ACCESS_FINE_LOCATION | 
 Includes GPS data for more precise location. Under the runtime permissions model, granting location permission also covers fine location access. | 

Your AndroidManifest.xml should be similar to the following:

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
<manifest ... >
 <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
 <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

 <application ... >
 ...
 </application>
</manifest>

```
 | 

## Disabling continuous tracking

You can disable continuous tracking at compile time or runtime.

- compile time
 
- runtime

To disable continuous location tracking at compile time, set com_braze_enable_location_collection to false in braze.xml:

```

1

```
 | 
```
<bool name="com_braze_enable_location_collection">false</bool>

```
 | 

To selectively disable continuous location tracking at runtime, use BrazeConfig:

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
BrazeConfig brazeConfig = new BrazeConfig.Builder()
 .setIsAutomaticLocationCollectionEnabled(false)
 .build();
Braze.configure(this, brazeConfig);

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
val brazeConfig = BrazeConfig.Builder()
 .setIsAutomaticLocationCollectionEnabled(false)
 .build()
Braze.configure(this, brazeConfig)

```
 | 

## Logging the current location

### Step 1: Configure your project

important

When using Braze location features, your application is responsible for requesting authorization for using location services. Be sure to review Apple Developer: Requesting authorization to user location services.

To enable location tracking, open your Xcode project and select your app. In the General tab, add the BrazeLocation module.

- swift
 
- objective-c

In your AppDelegate.swift file, import the BrazeLocation module at the top of the file. Add a BrazeLocationProvider instance to the Braze configuration, making sure all changes to the configuration are done prior to calling Braze(configuration:). See Braze.Configuration.Location for the available configurations.

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
import UIKit
import BrazeKit
import BrazeLocation

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

 static var braze: Braze? = nil

 func application(
 _ application: UIApplication,
 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
 ) -> Bool {
 // Setup Braze
 let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
 configuration.logger.level = .info
 configuration.location.brazeLocationProvider = BrazeLocationProvider()
 configuration.location.automaticLocationCollection = true
 configuration.location.geofencesEnabled = true
 configuration.location.automaticGeofenceRequests = true
 let braze = Braze(configuration: configuration)
 AppDelegate.braze = braze

 return true
 }

}

```
 | 

In your AppDelegate.m file, import the BrazeLocation module at the top of the file. Add a BrazeLocationProvider instance to the Braze configuration, making sure all changes to the configuration are done prior to calling Braze(configuration:). See BRZConfigurationLocation for the available configurations.

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

```
 | 
```
#import "AppDelegate.h"

@import BrazeKit;
@import BrazeLocation;

@implementation AppDelegate

#pragma mark - Lifecycle

- (BOOL)application:(UIApplication *)application
 didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
 // Setup Braze
 BRZConfiguration *configuration =
 [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
 endpoint:brazeEndpoint];
 configuration.logger.level = BRZLoggerLevelInfo;
 configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
 configuration.location.automaticLocationCollection = YES;
 configuration.location.geofencesEnabled = YES;
 configuration.location.automaticGeofenceRequests = YES;
 Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
 AppDelegate.braze = braze;

 [self.window makeKeyAndVisible];
 return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
 return _braze;
}

+ (void)setBraze:(Braze *)braze {
 _braze = braze;
}

@end

```
 | 

### Step 2: Log the user’s location

Next, log the user’s last-known location to Braze. The following examples assume you’ve assigned the Braze instance as a variable in your AppDelegate.

- swift
 
- objective-c

```

1
2

```
 | 
```
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
 longitude:longitude)

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
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
 longitude:longitude,
 altitude:altitude,
 horizontalAccuracy:horizontalAccuracy,
 verticalAccuracy:verticalAccuracy)

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
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
 longitude:longitude
 horizontalAccuracy:horizontalAccuracy];

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
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
 longitude:longitude
 horizontalAccuracy:horizontalAccuracy
 altitude:altitude
 verticalAccuracy:verticalAccuracy];

```
 | 

tip

For more information, see Braze.User.swift.

## Prerequisites

Before you can use this feature, you’ll need to integrate the React Native Braze SDK.

## Setting the last known location

To manually set the last known location for a user, use the setLastKnownLocation method. This is useful if you collect location data outside of the Braze SDK.

```

1

```
 | 
```
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);

```
 | 

- On Android, latitude and longitude are required. altitude, horizontalAccuracy, and verticalAccuracy are optional.
 
- On iOS, latitude, longitude, and horizontalAccuracy are required. altitude and verticalAccuracy are optional.

For cross-platform compatibility, provide latitude, longitude, and horizontalAccuracy at a minimum.

## Setting a custom location attribute

To set a custom location attribute on a user profile, use the setLocationCustomAttribute method.

```

1

```
 | 
```
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);

```
 | 

## Requesting location initialization (Android only)

Call requestLocationInitialization after a user grants location permissions to initialize Braze location features on Android. This method is not supported on iOS and is not required for iOS geofence or location features.

```

1

```
 | 
```
Braze.requestLocationInitialization();

```
 | 

## Geofences

Geofences are supported on both iOS and Android. By default, the Braze SDK can automatically request and monitor geofences when location is available. You can rely on this automatic configuration for most integrations.

### Manually requesting geofences

To manually request a geofence update for a specific GPS coordinate, use requestGeofences. This is available on both iOS and Android. If you use this method, disable automatic geofence requests in your native configuration so the SDK does not overwrite your manual requests.

```

1

```
 | 
```
Braze.requestGeofences(LATITUDE, LONGITUDE);

```
 | 

- 

New Stuff!
