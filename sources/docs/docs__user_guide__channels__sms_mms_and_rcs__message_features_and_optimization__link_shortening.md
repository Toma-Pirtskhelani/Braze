---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening
slug: docs__user_guide__channels__sms_mms_and_rcs__message_features_and_optimization__link_shortening
title: "Link shortening"
description: "This reference article covers how to turn on link shortening in your SMS messages and some frequently asked questions."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Link shortening

This page covers how to turn on link shortening in your SMS and RCS messages, test shortened links, use your custom domain in shortened links, and more.

important

Braze is gradually rolling out unified link shortening, which consolidates all SMS and RCS shortened links into a single personalized link format (for example, brz.ai/abcdefgh).

- legacy
 
- unified

Link shortening and click tracking allow you to automatically shorten URLs contained in SMS or RCS messages and collect click-through-rate analytics, providing additional engagement metrics to help understand how users are engaging with your campaigns.

Link shortening and click tracking can be turned on at the message variant-level in both campaigns and Canvases.

note

For RCS messages, link shortening and URL-level click tracking are supported for URLs in the message body, but not for URLs in suggested actions. Clicks on suggested action URLs are recorded as RCS click events, but the URL and SHORT_URL fields will be null in Currents and Snowflake.

The length of the URL is determined by the type of tracking that is turned on:

- Basic tracking enables campaign-level click tracking. Static URLs have a length of 20 characters, and personalized URLs have a length of 25 characters.
 
- Advanced tracking enables campaign-level and user-level click tracking, and enables use of segmentation and retargeting capabilities which rely on clicks. Clicks also generate an SMS click event sent through Currents. Static URLs with advanced tracking have a length of 27-28 characters, allowing you to create segments of users who have clicked on URLs. Personalized URLs have a length of 32-33 characters.

Links are shortened using our shared short domain (brz.ai) or your custom link shortening domain. An example URL may look something like this: https://brz.ai/8jshX (basic, static) or https://brz.ai/p/8jshX/2dj8d (advanced, personalized). Refer to Testing for more information.

Any static URLs that start with http:// or https:// are shortened. Static shortened URLs are valid for one year from the date they were created. Shortened URLs that contain Liquid personalization are valid for two months.

note

Braze shortened links always include the https:// protocol and can’t be configured to use a different protocol.

## Using link shortening

To use link shortening, make sure the link shortening toggle in the message composer is turned on. Then, choose to use either basic or advanced tracking.

Braze recognizes only URLs that start with http:// or https://. When a URL is recognized, the Preview section updates with a placeholder URL. Braze estimates the length of the URL after shortening, but a warning prompts you to select a test user and save the message as a draft for a more accurate estimate.

note

If you plan to use the BrazeAITM Intelligent Channel filter and want the SMS and RCS channels to be selectable, turn on link shortening with advanced tracking.

### Adding UTM parameters

While link shortening allows you to track your URLs automatically, you can also add UTM parameters to your URLs to track the performance of campaigns in third-party analytics tools, such as Google Analytics.

To add UTM parameters to your URL, do the following:

- Start with your base URL. This is the URL of the page you want to track (such as https://www.example.com).
 
- Add a question mark (?) after your base URL.
 
- Add each UTM parameter separated by an ampersand (&).

An example is https://www.example.com?utm_source=newsletter&utm_medium=sms.

## Liquid personalization in URLs

You can dynamically construct your URL directly within the Braze composer, allowing you to add dynamic UTM parameters to your URLs or send users unique links (such as directing users to their abandoned cart or to a specific product that is back in stock).

### Create a URL with supported Liquid personalization tags

URLs can be dynamically generated through the use of any supported Liquid personalization tags.

```

1

```
 | 
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}

```
 | 

Braze also supports the shortening of custom-defined Liquid variables, such as in the following examples:

### Create a URL using Liquid variables

```

1
2

```
 | 
```
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}

```
 | 

### Shorten URLs rendered by Liquid variables

Supported channels: KakaoTalk, LINE, SMS, RCS, WhatsApp

Braze shortens URLs that are rendered by Liquid, even those included in API-trigger properties. For example, if {{api_trigger_properties.${url_value}}} represents a valid URL, Braze shortens and tracks that URL before sending the message.

### Shorten URLs in /messages/send endpoint

Link shortening is also turned on for API-only messages through the /messages/send endpoint. To also turn on basic or advanced tracking, use the link_shortening_enabled or user_click_tracking_enabled request parameters.

 Parameter | 
 Required | 
 Data type | 
 Description | 

 link_shortening_enabled | 
 Optional | 
 Boolean | 
 Set link_shortening_enabled to true to turn on link shortening and campaign-level click tracking. To use tracking, a campaign_id and message_variation_id must be present. | 

 user_click_tracking_enabled | 
 Optional | 
 Boolean | 
 Set user_click_tracking_enabled to true to turn on link shortening, and campaign-level and user-level click tracking. You can use the tracked data to create segments of users who clicked URLs.

 To use this parameter, link_shortening_enabled must be true, and a campaign_id and message_variation_id must be present. | 

For a full list of request parameters, go to request parameters.

## Testing

Before launching your campaign or Canvas, it’s best practice to preview and test your message first. To do so, go to the Test tab to preview and send an SMS or RCS message to content test groups or an individual user.

This preview updates with relevant personalization and the shortened URL. The number of characters and billable segments also update to reflect the rendered personalization and the shortened URL.

Make sure to save the campaign or Canvas before sending a test message to receive a representation of the shortened URL that is dispatched in your message. If the campaign or Canvas isn’t saved before a test send, the test send includes a placeholder URL.

For Canvases to appear in the “Clicked shortened SMS link” filter, the Canvas step containing the short link must also be enabled with advanced tracking, which allows user-level click tracking. If the short link is configured with basic tracking, the option to filter SMS short link click events isn’t available. The same advanced tracking requirement applies when you configure Canvas entry or action paths that depend on clicked shortened SMS links.

important

If a draft is created within an active Canvas, a shortened URL won’t be generated. The actual shortened URL is generated when the Canvas draft is made active.

note

Liquid personalization and shortened URLs are templated in the Test tab after a user has been selected. Make sure a user is selected to receive an accurate character count.

## Click tracking

When link shortening is turned on, the SMS/MMS/RCS Performance table includes a column titled Total Clicks that shows a count of click events per variant and an associated click rate. Total Clicks excludes suspected bot clicks from dashboard counts. For more details on metrics, see Message performance and Bot click filtering.

The Historical Performance and SMS/MMS/RCS Performance tables also include an option for Total Clicks and show a daily time series of click events. Clicks are incremented on redirect (such as when a user visits a link), and may be incremented more than once per user.

## Retargeting users

For guidance on retargeting, visit Retargeting.

## Custom domains

Link shortening also allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image. For more information, refer to Self-serve custom domains.

## Frequently asked questions

### Are the links I receive when test sending real URLs?

If the campaign has been saved as a draft before test sending, yes. Otherwise, it is a placeholder link. Note that the exact URL sent in a launched campaign may differ from the one sent in a test send.

### Can I add UTM parameters to a URL before it is shortened?

Yes. Both static and dynamic parameters can be added.

### How long do shortened URLs remain valid?

Personalized URLs are valid for two months from the time of URL registration. For unified link shortening, which does not have a static or personalized distinction, all links are valid for nine weeks.

### Does the Braze SDK need to be installed in order to shorten links?

No. Link shortening works without any SDK integration.

### Do I know which individual users are clicking on a URL?

Yes. When Advanced Tracking is turned on, you can retarget users who have clicked URLs by leveraging the SMS retargeting filters or the SMS click events (users.messages.sms.ShortLinkClick) sent by Currents.

### Does link shortening work with deep links or universal links?

Link shortening doesn’t work with deep links. Alternatively, you can shorten universal links from third-party providers such as Branch or Appsflyer, but users may experience a brief redirect or “flickering” effect. This occurs because the shortened link routes through the web first before resolving to the universal link that supports app opening. Additionally, Braze is unable to troubleshoot issues that may arise when shortening universal links, such as breaking the attribution or causing unexpected redirects.

note

Test the user experience before implementing link shortening with universal links to confirm it meets your expectations.

### Are send_ids associated with SMS click events?

No. However, if you have advanced tracking enabled, you can generally attribute send_ids with click events by using Query Builder to query Currents data with this query:

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
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
 INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
 ON s.user_id = c.user_id 
 AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 

```
 | 

Link shortening allows you to automatically shorten URLs contained in SMS or RCS messages and collect click-through-rate analytics, providing additional engagement metrics to help understand how users are engaging with your campaigns.

Link shortening can be turned on at the message variant-level in both campaigns and Canvases. When link shortening is turned on, clicks will generate an SMS click event sent through Currents.

note

For RCS messages, link shortening and URL-level click tracking are supported for URLs in the message body, but not for URLs in suggested actions. Clicks on suggested action URLs are recorded as RCS click events, but the URL and SHORT_URL fields will be null in Currents and Snowflake.

Links are shortened using our shared short domain (brz.ai) or your custom link shortening domain, and are valid for 9 weeks from the date they were created. An example URL may look something like https://brz.ai/8jshX2dj.

## Using link shortening

To use link shortening, make sure the link shortening checkbox in the message composer is selected.

- sms composer
 
- rcs composer

Braze recognizes only URLs that start with http:// or https://. When a URL is recognized, the Preview section updates with a placeholder URL. Braze estimates the length of the message after shortening, but a warning prompts you to select a test user and save the message as a draft for a more accurate estimate.

### Adding UTM parameters

While link shortening allows you to track your URLs automatically, you can also add UTM parameters to your URLs to track the performance of campaigns in third-party analytics tools, such as Google Analytics.

To add UTM parameters to your URL, do the following:

- Start with your base URL. This is the URL of the page you want to track (such as https://www.example.com).
 
- Add a question mark (?) after your base URL.
 
- Add each UTM parameter separated by an ampersand (&).

An example is https://www.example.com?utm_source=newsletter&utm_medium=sms.

## Liquid personalization in URLs

For information on how to dynamically construct URLs directly within the Braze composer, allowing you to add dynamic UTM parameters to your URLs or send users unique links, see Use Liquid personalization in URLs.

## Testing

Before launching your campaign or Canvas, it’s best practice to preview and test your message first. To do so, go to the Test tab to preview and send an SMS or RCS message to content test groups or an individual user.

This preview updates with relevant personalization and the shortened URL. The number of characters and billable segments also update to reflect the rendered personalization and the shortened URL.

Make sure to save the campaign or Canvas before sending a test message to receive a representation of the shortened URL that is dispatched in your message. If the campaign or Canvas isn’t saved before a test send, the test send includes a placeholder URL.

important

If a draft is created within an active Canvas, a shortened URL won’t be generated. The actual shortened URL is generated when the Canvas draft is made active.

note

Liquid personalization and shortened URLs are templated in the Test tab after a user has been selected. Make sure a user is selected to receive an accurate character count.

## Click tracking

When link shortening is turned on, the SMS/MMS/RCS Performance table includes a column titled Total Clicks that shows a count of click events per variant and an associated click rate. For more details on metrics, see Message performance.

The Historical Performance and SMS/MMS/RCS Performance tables also include an option for Total Clicks and show a daily time series of click events. Clicks are incremented on redirect (such as when a user visits a link), and may be incremented more than once per user.

## Retargeting users

For guidance on retargeting, visit Retargeting.

## Custom domains

Link shortening also allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image. For more information, refer to Self-serve custom domains.

## Frequently asked questions

### Are the links I receive when test sending real URLs?

If the campaign has been saved as a draft before test sending, yes. Otherwise, it is a placeholder link. Note that the exact URL sent in a launched campaign may differ from the one sent in a test send.

### Can I add UTM parameters to a URL before it is shortened?

Yes. Both static and dynamic parameters can be added.

### How long do shortened URLs remain valid?

Personalized URLs are valid for two months from the time of URL registration. For unified link shortening, which does not have a static or personalized distinction, all links are valid for nine weeks.

### Does the Braze SDK need to be installed in order to shorten links?

No. Link shortening works without any SDK integration.

### Do I know which individual users are clicking on a URL?

Yes. You can retarget users who have clicked URLs by using the SMS retargeting filters or the SMS click events (users.messages.sms.ShortLinkClick) sent by Currents.

### Does link shortening work with deep links or universal links?

Link shortening doesn’t work with deep links. Alternatively, you can shorten universal links from third-party providers such as Branch or Appsflyer, but users may experience a brief redirect or “flickering” effect. This occurs because the shortened link routes through the web first before resolving to the universal link that supports app opening. Additionally, Braze is unable to troubleshoot issues that may arise when shortening universal links, such as breaking the attribution or causing unexpected redirects.

note

Test the user experience before implementing link shortening with universal links to confirm it meets your expectations.

### Are send_ids associated with SMS click events?

No. However, you can generally attribute send_ids with click events by using Query Builder to query Currents data with this query:

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
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
 INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
 ON s.user_id = c.user_id 
 AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 

```
 | 

- 

New Stuff!
