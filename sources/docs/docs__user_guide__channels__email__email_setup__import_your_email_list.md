---
url: https://www.braze.com/docs/user_guide/channels/email/email_setup/import_your_email_list
slug: docs__user_guide__channels__email__email_setup__import_your_email_list
title: "Import your email list into Braze"
description: "This reference article covers best practices for importing your email list into Braze."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Import your email list into Braze

An important step in setting yourself as a successful email sender is ensuring that you have a high-quality email list. Proper email list management can improve your deliverability and give you more accurate and clean campaign results.

## Considerations before importing

important

Do not send legally required transactional emails to SMS gateways, as there’s a strong likelihood that those emails will not be delivered.

Although emails you send using a phone number and the provider’s gateway domain (known as an MM3) can result in the email being received as an SMS (text) message, some of our email providers do not support this behavior. For example, if you send an email to a T-Mobile phone number (such as “[email protected]”), your SMS message would be sent to whoever owns that phone number on the T-Mobile network.

Keep in mind that even though these emails may not be delivered to the SMS gateway, they will still count towards your email billing. To avoid sending emails to unsupported gateways, review the list of unsupported gateway domain names.

### Validate your email lists

Before importing your email list into Braze, validate that your list includes only genuine email addresses. A high bounce rate can damage your email sender reputation.

Email list cleaning services can do this for you by determining if the email address follows the correct syntax and has the physical properties of an email address, verifying the email domain, and connecting to the email server to authenticate if the email address exists there.

### Check if an email address is already associated with a user

Before creating a user through the API or SDK, call the /users/export/ids endpoint and specify the user’s email_address. If it returns a user profile, that Braze user is already associated with that email address.

We strongly recommend that you look for unique email addresses when new users are created, and avoid passing or importing users with the same email address. Otherwise, you may have unintended consequences that impact message sending, targeting, reporting, and other features.

For example, let’s say you have duplicate profiles, but certain custom attributes or events reside on only one profile. When you try to trigger campaigns or Canvases with multiple criteria, Braze can’t identify the user as eligible because there are two user profiles. Or, if a campaign targets an email address shared by two users, the Search Users page will show both user profiles as having received the campaign.

### Identify your engaged users

In order to identify your most engaged users, first remove deeply lapsed users. It’s a best practice to not email users who have not engaged with an email in over six months as this can damage your email sender reputation. When importing your email list, make sure to only include users who have opened an email from you within the last six months.

In the long term, you should also consider implementing a sunset policy.

### Avoid suppression lists

If you are transitioning off an existing email provider, make certain that you do not import users from a suppression list. Suppression lists feature email addresses that have either unsubscribed, marked your emails as spam, or hard bounced.

## Methods for importing

Once you have your email list prepared, there are several ways to import users into Braze, such as via the Braze REST API or CSV files. Read more at our dedicated User Import article.

- 

New Stuff!
