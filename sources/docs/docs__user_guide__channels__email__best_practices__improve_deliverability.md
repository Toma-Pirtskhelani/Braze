---
url: https://www.braze.com/docs/user_guide/channels/email/best_practices/improve_deliverability
slug: docs__user_guide__channels__email__best_practices__improve_deliverability
title: "Improve email deliverability"
description: "This reference article explains why marketing email can reach the spam folder and how sending patterns, message content, and recipient behavior affect inbox placement."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Improve email deliverability

Mailbox providers (MBPs) consider your sending domain’s reputation when they accept or bounce a message. Sometimes a message is accepted but not placed in the inbox. It can be routed to the spam folder instead, where recipients are less likely to see it.

The following provides general guidance to reduce your chances of spam-folder placement and low engagement.

## Sending patterns

Sending patterns influence domain reputation. When they misalign with the following best practices, MBPs are more likely to bounce or filter mail.

- Collect high-quality subscriber data. Gather valid addresses, use voluntary opt-in with clear language, and consider confirmed opt-in or validation services so subscribers know what they’re signing up for. Design the sign up flow to be clear and resistant to fraudulent sign ups.
 
- Set and honor expectations about content and frequency. Avoid mailing products or cadences the subscriber didn’t agree to.
 
- Send mail subscribers want to open and interact with. Ask what value each send provides before you schedule it.
 
- Prioritize recipients who recently opted in or engaged (such as users who have logged opens, clicks, and website activity). Avoid repeatedly mailing inactive addresses.
 
- Separate transactional mail from marketing mail. Many Internet Service Providers (ISPs) treat transactional mail differently from marketing. Separate the two when it makes sense. For example, distinct sender email addresses can be enough separation in some cases.

important

Do not send legally required transactional emails to SMS gateways, as there’s a strong likelihood that those emails will not be delivered.

Although emails you send using a phone number and the provider’s gateway domain (known as an MM3) can result in the email being received as an SMS (text) message, some of our email providers do not support this behavior. For example, if you send an email to a T-Mobile phone number (such as “[email protected]”), your SMS message would be sent to whoever owns that phone number on the T-Mobile network.

Keep in mind that even though these emails may not be delivered to the SMS gateway, they will still count towards your email billing. To avoid sending emails to unsupported gateways, review the list of unsupported gateway domain names.

## Message content

Content filters help MBPs protect their users from phishing, malware, and unwanted mail. Your creativity may look benign, but still resemble patterns filters watch for.

- Review recent changes to the message. For example, changes to the HTML, image ratio, image hosts, and the inclusion of new templates may trigger MBP content filters.
 
- Freshen up templates and copy when engagement drops. Stale, repetitive sends give subscribers little reason to open.

## Recipient reports and behavior

Subscriber actions feed both reputation systems and future inbox decisions. High complaint volume can divert later messages to spam, which acts like a quarantine when the MBP or the subscriber isn’t confident in the mail’s quality.

- Write relevant subject lines and body content with clear calls to action. Deletes without opens, low engagement, and weak subject lines all signal disinterest before the body is read.
 
- Ask subscribers at the point of opt-in to add your sender address to their email contacts list. This improves your sender reputation and increases the chance that your mail reaches inboxes.

## Related resources

- Sunset policies
 
- IP warming
 
- Deliverability pitfalls and spam traps
 
- Know before you send
 
- Consent and address collection
 
- Email FAQ

- 

New Stuff!
