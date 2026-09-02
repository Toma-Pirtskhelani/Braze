---
url: https://www.braze.com/docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
slug: docs__user_guide__channels__email__email_setup__open_pixel_and_click_tracking
title: "Email open pixel and click tracking"
description: "This reference article covers how to implement open pixel and click tracking."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Email open pixel and click tracking

Open pixel tracking and click tracking can be turned on or off for each user profile. This flexibility helps you follow regional privacy laws, where an individual user profile might indicate they no longer want to be tracked.

## Turning on open pixel or click tracking

When either importing or updating a user profile through API, CSV, or Cloud Data Ingestion (CDI), two fields are available for you to modify:

- email_open_tracking_disabled: Accepts true or false. Set to false to add the open tracking pixel to all future emails sent to this user.
 
- email_click_tracking_disabled: Accepts true or false. Set to false to add click tracking to all links within a future email, sent to this user.

For reference, this information is reflected on the user profile in the email Contact Settings, located in the Engagement tab.

## Click tracking link requirements

Braze click tracking only rewrites links that use http:// or https:// URLs. Links that use other schemes, such as mailto: or tel:, are not click-tracked.

To track clicks on phone numbers or email addresses, use an https:// redirect URL that forwards to the tel: or mailto: destination instead.

### Click tracking URL patterns

When your email service provider (ESP) rewrites a link for click tracking, the resulting URL uses your click tracking domain and an ESP-specific path prefix. For the patterns each ESP generates, which you need for firewall rules and security allowlists, refer to Click and open tracking URL patterns.

- 

New Stuff!
