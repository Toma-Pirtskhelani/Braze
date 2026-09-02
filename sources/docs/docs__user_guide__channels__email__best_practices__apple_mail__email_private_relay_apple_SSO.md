---
url: https://www.braze.com/docs/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO
slug: docs__user_guide__channels__email__best_practices__apple_mail__email_private_relay_apple_SSO
title: "Send emails to Apple Private Relay"
description: "This article covers the process of sending emails to Apple Private Relay."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Send emails to Apple Private Relay

Apple’s single sign-on (SSO) feature allows its users to share their email addresses ([email protected]) or to hide their email addresses by masking what’s provided to brands ([email protected]) instead of their personal email address. Apple will then forward messages sent to the relay addresses to the user’s actual email address.

To send emails to Apple’s private email relay, register your sending domains with Apple. If you don’t configure your domains with Apple, emails sent to relay addresses will result in bounces.

If a user decides to disable the email forwarding to your app’s relay email, Braze will receive email bounce information as usual. These users can manage apps that use sign-in with Apple from their Apple ID settings page (see Apple’s documentation).

## Configure your email provider

- sendgrid
 
- sparkpost
 
- amazon ses

If you use SendGrid as an email provider, you can send emails to Apple without making DNS changes.

- Log into the Apple Developer Portal
 
- Go to the Certificates, Identifiers & Profiles page.
 
- Select Services > Sign in with Apple for Email Communication.
 
- In the Email Sources section, add the domains and subdomains.

- The address should be formatted as: bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN> (an example is: [email protected]).

If your desired “From” address is an abmail address, include that in your subdomain. For example, use abmail.docs.braze.com instead of docs.braze.com.

To set up Apple Private Relay for SparkPost, follow these steps:

- Sign in with Apple.
 
- Follow Apple’s documentation to register the email domains.
 
- Apple will automatically check the domains, show which ones are verified, and provide the option to reverify or delete the domains.

### When the sending domain is also the bounce domain

If a sending domain is also used as a bounce domain, you won’t be able to store any records and will need to follow these additional steps:

- If the domain has already been verified on SparkPost, you must create MX and TXT records:

 Instance | 
 MX record | 
 TXT record | 

 US | 
 smtp.sparkpostmail.com | 
 "v=spf1 redirect=_spf.sparkpostmail.com" | 

 EU | 
 smtp.eu.sparkpostmail.com | 
 "v=spf1 redirect=_spf.eu.sparkpostmail.com" | 

important

To avoid SPF failures, you must create the MX and TXT records and have them propagated in the DNS before deleting the CNAME record.

- Delete the CNAME record.
 
- Replace it with the MX and TXT records for proper routing.
 
- Create your A record to point to your CDN or file hosting.

To set up Apple Private Relay, you should ideally have a custom MAIL FROM domain set up.

- Sign in with Apple.
 
- Follow Apple’s documentation to register the email domains.

important

Confirm your DKIM/SPF matches what you register per the instructions linked.

- Apple will automatically check the domains, show which ones are verified, and provide the option to reverify or delete the domains.

If you have any further questions, open a support ticket.

- 

New Stuff!
