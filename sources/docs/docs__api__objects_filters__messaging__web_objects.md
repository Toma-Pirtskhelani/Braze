---
url: https://www.braze.com/docs/api/objects_filters/messaging/web_objects
slug: docs__api__objects_filters__messaging__web_objects
title: "Web push object"
description: "This reference article lists and explains the different web objects used at Braze."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# Web push object

The web_push object allows you to define or request information related to web push and web push alert content via our messaging endpoints.

## Web push object

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
{
 "alert": (required, string) the notification message,
 "title": (required, string) the title that appears in the notification drawer,
 "extra": (optional, object) additional keys and values to be sent in the push,
 "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
 "custom_uri": (optional, string) a web URL,
 "image_url": (optional, string) URL for image to show,
 "large_image_url": (optional, string) URL for large image, supported on Chrome Windows/Android,
 "require_interaction": (optional, boolean) whether to require the user to dismiss the notification. for a list of supported platforms, see: "https://developer.mozilla.org/en-US/docs/Web/API/Notification/requireInteraction#browser_compatibility",
 "time_to_live": (optional, integer (seconds)),
 "send_to_most_recent_device_only" : (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used browser, rather than all eligibles browsers,
 "buttons" : (optional, array of Web push action button objects) push action buttons to display
}

```
 | 

The value for image_url should be a URL that links to where your image is hosted. Images need to be cropped to a 1:1 aspect ratio.

## Web push action button object

```

1
2
3
4
5

```
 | 
```
{
 "text": (required, string) the button's text,
 "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
 "uri": (optional, string) a web URL
}

```
 | 

- 

New Stuff!
