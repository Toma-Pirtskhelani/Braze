---
url: https://www.braze.com/docs/user_guide/channels/in_app_messages/customize/video_in_custom_html
slug: docs__user_guide__channels__in_app_messages__customize__video_in_custom_html
title: "Video in custom HTML  in-app messages"
description: "This article describes how to embed videos into your HTML in-app messages."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Video in custom HTML in-app messages

This article applies to custom HTML messages in the traditional editor.

## Embed videos

To play a video in an HTML in-app message, include the following <video> element in your HTML, and replace the video names with your file’s name (or the remote asset’s URL). You can find other possible <video> options on MDN Web Docs.

```

1
2
3
4
5

```
 | 
```
<video class="video" autoplay muted playsinline controls>
 <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
 <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
 Your device does not support playing this video.
</video>

```
 | 

To use a local video asset, be sure to include this file when uploading assets to your campaign.

note

Video content is only available when the device has a reasonable network speed, unless the video is sourced from the device locally.

## Android considerations

To embed video and other HTML5 content in HTML in-app messages on Android, hardware acceleration is required to be enabled in the Activity where the in-app message is displayed. For more information, refer to the Android developer guide.

auto-play: Even with hardware acceleration enabled, Android WebViews may require a user gesture to start media playback. If you need auto-play, configure the WebView used to render HTML in-app messages to disable the user gesture requirement by setting WebSettings.setMediaPlaybackRequiresUserGesture(false). This requires SDK-level customization of how HTML in-app messages are displayed. For setup guidance, see Customize in-app messages for the Braze SDK.

## iOS considerations

To support iOS devices:

- You must include the playsinline attribute because full screen playback is not supported.
 
- auto-play is not guaranteed on iOS. iOS playback behavior depends on WKWebView and OS-level media policies, and may require a user gesture even when autoplay and muted are set. Test your HTML in-app message on your target iOS versions and devices.

If auto-play is required and your tests show it doesn’t work by default, you can customize the WKWebViewConfiguration used by HTML in-app messages to adjust the media playback user-action requirement, for example by setting the mediaTypesRequiringUserActionForPlayback property. This requires SDK-level customization. For Swift resources, see Customize in-app messages for the Braze SDK and Adding the Braze JavaScript interface to WebViews for Swift.

## Web considerations

Most modern browsers allow auto-play only under certain conditions (commonly when the video is muted). If you use autoplay in a web in-app message, include muted and test across your supported browsers and devices, as browser policies vary and may still require a user gesture in some cases.

To autoplay YouTube videos in a web in-app message, add the URL parameter &autoplay=1. For example, the following video will autoplay, be muted (&mute=1), and show no controls (&controls=0):

```

1

```
 | 
```
<iframe class="video" src="https://www.youtube.com/embed/VPIPAc4oQqw?autoplay=1&mute=1&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

```
 | 

## How YouTube videos display

- YouTube-embedded in-app messages can display directly inside the app or in a separate tab within the app, depending on the platform.
 
- In-app message text may not display when the YouTube embed is shown.

## Troubleshooting

If your in-app message doesn’t display your video:

- Confirm your URL is valid.
 
- Confirm you’re not missing the type="video/mp4" declaration (for non-YouTube video).
 
- Add any missing closing tags and fix typos.

- 

New Stuff!
