---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/best_practices
slug: docs__user_guide__channels__whatsapp__best_practices
title: "WhatsApp best practices"
description: "This article outlines suggested best practices when using the WhatsApp messaging channel, including how to maintain a high phone quality rating and avoid a high..."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# WhatsApp best practices

Before sending your WhatsApp messages, refer to these suggested best practices to maintain a high phone quality rating, avoid blocks and reports, and opt-in and out-out users.

## Maintain a high phone quality rating

WhatsApp bases its phone quality rating on actions taken by users who receive your messages, such as blocking or reporting your business. It’s important to maintain a high quality rating because if it’s low and doesn’t improve over a certain time, your messaging limit may decrease.

The first time you message a user in WhatsApp, these options are displayed within the message thread.

note

For metrics about your blocks and reports, make sure the Insights tab is turned on in your WhatsApp Manager.

To avoid high instances of blocks and reports, Braze suggests the following best practices to maintain a high phone quality rating and stable messaging limits.

### Follow WhatsApp opt-in requirements and guidelines

Make sure all users have actively consented to receive WhatsApp messages before you start communicating with them on WhatsApp. When asking users to opt-in, users should be told that they are specifically agreeing to receive messages from your business over WhatsApp.

note

For information about opt-in requirements and helpful tips, see Get Opt-in for WhatsApp.

### Follow messaging best practices

- Make your channel name reflect your brand so users recognize that the message is from you, not spam.
 
- Send a confirmation message to users after you collect their opt-in consent.
 
- Send messages during appropriate times.

### Give customers the option to opt-out

Opt-outs don’t impact your phone quality rating, so it’s better for a user to opt-out of receiving WhatsApp communications versus blocking or reporting you.

A suggested best practice is to provide instructions about how to out-out in the footer of the first message you send users. For example, you could state that users can unsubscribe from your WhatsApp channel by responding with your opt-out trigger word. You could also regularly include the opt-out footer in future campaigns. To learn how to set this up, see Opt-in and opt-out.

### Minimize response latency for two-way flows

For interactive Canvas flows that reply with response messages:

- Place the response message step immediately after the inbound trigger or Action Path evaluation.
 
- Use webhooks instead of User Update steps when subscription changes are not required before the reply.
 
- Avoid long delays or multi-day waits between inbound messages and response sends; the WhatsApp customer service window is 24 hours per inbound message.

- 

New Stuff!
