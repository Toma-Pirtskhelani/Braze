---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/handling_unknown_phone_numbers
slug: docs__user_guide__channels__whatsapp__message_processing__handling_unknown_phone_numbers
title: "Handle unknown phone numbers"
description: "This reference article covers how Braze will go about handling unknown phone numbers for WhatsApp users."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Handle unknown phone numbers

You may find that after you get WhatsApp up and running with Braze, you receive messages from unknown users. The following steps describe how an unidentified user and number get processed.

## Opt-in/out and custom keyword workflow for unknown numbers

Braze will first attempt to find a user with a matching number. If none is found, Braze automatically addresses an unknown number in one of two ways:

- If a trigger word with an opt-in Canvas is set up:

- Braze creates an anonymous profile
 
- We assign a user alias to the profile with the following details:

- An alias_name with the value being the user’s provided phone number
 
- An alias_label with the value phone

- Our system sets the phone attribute
 
- The user is subscribed to the corresponding subscription group based on the logic that is set up within the Canvas

- If no opt-in Canvas is set up:

- Braze creates an anonymous profile
 
- We assign a user alias to the profile with the following details:

- An alias_name with the value being the user’s provided phone number
 
- An alias_label with the value phone

- Our system sets the phone attribute
 
- The user’s subscription status will default to unsubscribed for all WhatsApp subscription groups

- 

New Stuff!
