---
url: https://www.braze.com/docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
slug: docs__user_guide__audience__subscription_preferences__preference_center__api_preference_center
title: "API email preference center"
description: "This article describes the API email preference center and how to customize it."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# API email preference center

Setting up a preference center provides a one-stop shop for your users to edit and manage their notification preferences for your email messaging. This article includes steps for building an API-generated preference center, but you can also build a preference center using the drag-and-drop editor.

tip

You can also manage subscriptions on a Braze landing page. Add a Manage Subscriptions block so consumers can review and update their existing subscriptions or opt in to new ones, all while you capture their engagement data on the same page. For more information, see Manage Subscriptions block.

In the Braze dashboard, go to Audience > Email Preference Centers.

This is where you can manage and view each subscription group. Each subscription group you create is added to this preference center list. You can create multiple preference centers.

important

The preference center is intended to be used within the Braze email channel. The preference center links are dynamic based on each user and cannot be hosted externally.

## Create a preference center with API

By using the Preference Center Braze endpoints, you can create a preference center, a website hosted by Braze, that can display your user’s subscription state and subscription group statuses. Using HTML and CSS, your developer team can build the preference center using HTML and CSS so that the styling of the page matches your brand guidelines.

Using Liquid enables you to retrieve the names of your subscription groups, and each user’s status. This way, Braze stores and retrieves this data when the page is loaded.

### Prerequisites

 Requirement | 
 Description | 

 Enabled preference center | 
 Your Braze dashboard has permissions to use the preference center feature. | 

 Valid workspace with an email, SMS, or WhatsApp subscription group | 
 A working workspace with valid users and an email, SMS, or WhatsApp subscription group. | 

 Valid user | 
 A user with an email address and an external ID. | 

 Generated API key with preference center permissions | 
 In the Braze dashboard, go to Settings > API Keys to confirm that you have access to an API key with preference center permissions. | 

### Step 1: Use the Create preference center endpoint

Let’s begin building a preference center using the Create preference center endpoint. To customize your preference center, you can include HTML that aligns with your branding in the preference_center_page_html field and confirmation_page_html field.

The Generate preference center URL endpoint allows you to grab the preference center URL for a specific user outside of an email that is sent through Braze.

note

Braze renders confirmation_page_html in an iframe that uses a data: URL. Browsers treat data: URLs as opaque origins. As a result, scripts in that iframe can’t load additional external resources, and navigating the parent window or communicating across frames from that page fails.

Instead, you can link to external content, such as a hosted survey URL, instead of embedding scripts. If you must embed a third-party tool and the vendor allows it, use an <iframe title="Description of the embedded content" src="https://example.com/..."> pointing to the tool’s hosted HTTPS URL.

### Step 2: Include in your email campaign

important

There are certain browsers, such as the Naver Android and iOS apps, that don’t support the Braze preference center. If you anticipate that some of your users use these browsers, consider providing alternative methods for them to manage their email preferences.

To place a link to the preference center in your emails, use the following Liquid tag in the desired place in your email, similar to the way you would insert unsubscribe URLs.

```

1

```
 | 
```
{{preference_center.${kitchenerie_preference_center_example}}}

```
 | 

You can also use a combination of HTML that includes Liquid. For example, you can paste the following as the URL in either the HTML editor or drag-and-drop editor. This shows the basic preference center layout that lists all of the email subscription groups automatically. If you use link aliasing, add a trailing question mark (?) after the Liquid tag so Braze can append tracking parameters.

```

1

```
 | 
```
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>

```
 | 

The preference center has a checkbox that allows your users to unsubscribe from all emails.

## Testing preference centers

Preference center links are generated for each user at send time and are tied to a live campaign or Canvas send. Test sends and editor previews do not support saving subscription changes. This is expected behavior.

### What you’ll see

- Test sends: Preference center Liquid tags may not resolve to a valid link. If the page loads, the Save Preferences button is disabled, and subscription changes are not saved.
 
- Drag-and-drop editor Preview tab: You can preview layout and styling, but you cannot test saving preferences from the editor.

### How to test end-to-end

To verify that preference center links and buttons work before a full launch:

- Create a campaign or Canvas email step that includes your preference center Liquid tag.
 
- Target only your test users or a small internal segment.
 
- Launch the message and open the email from a real inbox (not Send Test).
 
- Select the preference center link, update subscription groups, and select Save Preferences.
 
- Confirm the changes on the user’s profile in the Braze dashboard.

As an alternative for API-built preference centers, use the Generate preference center URL endpoint to retrieve a working URL for a specific user outside of a test send.

For other test-send limitations, see Send test messages.

### Preview, test send, and live send

 Method | 
 Preview layout | 
 Save subscription changes | 

 Drag-and-drop editor Preview tab | 
 Yes | 
 No | 

 Campaign or Canvas Send Test | 
 Partial (email arrives) | 
 No | 

 Live send to a test user or segment | 
 Yes | 
 Yes | 

 Generate preference center URL API | 
 Yes | 
 Yes | 

#### Edit a preference center

You can edit and update your preference center by using the Update preference center endpoint.

#### Identify preference centers and details

To identify your preference centers, use the View details for preference center endpoint to return related information such as the last updated timestamp, the preference center ID, and more.

## Customize a preference center

Braze manages the subscription state updates from the preference center, which keeps the preference center in sync. However, you can also create and host your own preference center using the subscription groups APIs with the following options.

### Option 1: Link with string query parameters

Use query string field-value pairs in the body of the URL to pass the user ID and email category to the page so users only need to confirm their choice to unsubscribe. This option is good for those who store a user identifier in a hashed format and do not already have a subscription center.

For this option, each email category requires its own specific unsubscribe link:

http://mycompany.com/query-string-form-fill?field_id=Alex&field_category=offers

tip

It is also possible to hash the user’s external ID at the point of send using a Liquid filter. This will convert the user_id to an MD5 hash value, for example:

```

1
2

```
 | 
```
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}

```
 | 

### Option 2: Authenticate with JSON web token

Use a JSON web token to authenticate users to a part of your web server (for example, account preferences) that is normally behind a layer of authentication such as username and password login.

This approach does not require query string value-pairs embedded in the URL as these can be passed in the JSON web token’s payload, for example:

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
 "user_id": "1234567890",
 "name": "Alex Smith",
 "category": "offers"
}

```
 | 

## Frequently asked questions

### Why doesn’t my preference center work in a test send?

Preference center links require a live send context. Test sends do not generate valid preference center URLs, and the Save Preferences button is disabled if the page loads. This is expected behavior. To test end-to-end, launch a campaign or Canvas step to a test user or small internal segment, or use the Generate preference center URL endpoint. For details, see Testing preference centers.

### I haven’t created a preference center. Why am I seeing “PreferenceCenterBrazeDefault” on my dashboard?

This is used to render the preference center when legacy Liquid ${preference_center_url} is used, meaning Canvas steps or templates that reference either ${preference_center_url} or preference_center.${PreferenceCenterBrazeDefault} won’t work. This also applies to previously sent messages that included the legacy Liquid or “PreferenceCenterBrazeDefault” as part of the message.

If you reference ${preference_center_url} in a new message again, a preference center named “PreferenceCenterBrazeDefault” will be created again.

### Do preference centers support multiple languages?

No. However, you can leverage Liquid when writing the HTML for custom opt-in and opt-out pages. If you’re using dynamic links to manage unsubscribes, this is a single link.

For example, if you’re tracking the unsubscribe rate for Spanish-speaking users, you would need to either use separate campaigns or leverage analytics around Currents (such as looking at when a user unsubscribes and checking the preferred language of that user).

As another example, for tracking unsubscribe rates for Spanish-speaking users, you could add a query parameter string like ?Spanish=true to the unsubscribe URL if the user’s language is Spanish and use a regular unsubscribe link otherwise:

```

1
2
3
4

```
 | 
```
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}

```
 | 

Then, through Currents, you could identify which users speak Spanish and how many click events there were for that unsubscribe link.

### Are both unsubscribe links and email preference centers required for sending?

No. If you see the message “Your Email Body does not include an unsubscribe link” when composing an email campaign, this warning is expected if your unsubscribe link is in a Content Block.

### How do I update the default browser icon?

By default, the icon next to the browser tab name (favicon) uses the Braze logo. To add a custom favicon, you set it via the links-tags attribute in your Create or Update Preference Center API call. Braze then injects the <link rel="icon" ...> tag into the hosted page for you.

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

```
 | 
```
{
 "name": "MyPreferenceCenter",
 "preference_center_title": "Email Preferences",
 "preference_center_page_html": "<!doctype html> ...",
 "confirmation_page_html": "<!doctype html> ...",
 "state": "active",
 "options": {
 "links-tags": [
 {
 "rel": "icon",
 "type": "image/png",
 "sizes": "32x32",
 "href": "https://yourcdn.com/path/to/favicon-32x32.png"
 },
 {
 "rel": "shortcut icon",
 "type": "image/x-icon",
 "href": "https://yourcdn.com/path/to/favicon.ico"
 },
 {
 "rel": "apple-touch-icon",
 "sizes": "180x180",
 "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
 }
 ]
 }
}

```
 | 

- 

New Stuff!
