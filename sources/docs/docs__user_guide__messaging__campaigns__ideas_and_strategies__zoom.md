---
url: https://www.braze.com/docs/user_guide/messaging/campaigns/ideas_and_strategies/zoom
slug: docs__user_guide__messaging__campaigns__ideas_and_strategies__zoom
title: "Automate Zoom registration"
description: "This article describes how to automate Zoom attendee registration in your email, push, and in-app message campaigns."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Automate Zoom registration

Webinars have become common for Braze customers to host over the past few years. When hosting a Zoom webinar, users must enter their information on a Zoom landing page to sign up.

A recommended user flow is outlined as follows:

- Schedule a webinar in Zoom and generate a webinarId.
 
- Use Braze to promote Zoom webinars via email, push, and in-app message channels.
 
- Include a call-to-action button in these communications that automatically adds users to the webinar.

This can be accomplished by using the Zoom APIs to automatically add a user to a webinar through a button click within an email, push, or in-app message. Use the following endpoint, replacing the webinar ID in the API request.

POST: /meetings/{webinarId}/registrants

For more information, refer to the Zoom Add webinar registrant endpoint.

- email
 
- push
 
- in-app message

Create an email campaign with a call-to-action button within the message body. When a user clicks the button, redirect them to the webinar landing page (with appropriate parameters included in the redirect link).

Using the parameters in the URL to pass user data, build an API call to fire when the page loads to add the user to the webinar.

Users are now registered for the webinar with the details that already exist on their Braze profile.

- 
 
Create a push campaign

Set on-click behavior for the button to link out to the webinar landing page.

A simple example of a landing page for users who sign up via button click from a push. Let the user know what they have signed up for and confirm their registration:

- 
 
Create a webhook campaign triggered by the in-app message or button click.

 Using existing user data on their Braze profile, sign up the user for the webinar.

Example webhook call to Zoom endpoint.

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
 POST https://api.zoom.com/meetings/{webinarId}/registrants

 {
 "email": "{{${email_addresses}}}",
 "first_name": "{{${first_name}}}",
 "last_name": "{{${last_name}}}",
 "city": "{{${city}}}",
 "country": "{{${country}}}",
 "phone": "{{${phone_number}}}"
 }

```
 | 

- 
 
Users are now registered for the webinar with the details that already exist on their Braze profile.

- 
 
Create an in-app message campaign

Set on-click behavior for the button to link out to the webinar landing page

A simple example of a landing page for users who sign up via button click from an in-app message. Let the user know what they have signed up for and confirm their registration:

- 
 
Create a webhook campaign triggered by the in-app message or button click.

 Using existing user data on their Braze profile, sign up the user for the webinar.

Example webhook call to Zoom endpoint.

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
 POST https://api.zoom.com/meetings/{webinarId}/registrants

 {
 "email": "{{${email_addresses}}}",
 "first_name": "{{${first_name}}}",
 "last_name": "{{${last_name}}}",
 "city": "{{${city}}}",
 "country": "{{${country}}}",
 "phone": "{{${phone_number}}}"
 }

```
 | 

- 
 
Users are now registered for the webinar with the details that already exist on their Braze profile.

- 

New Stuff!
