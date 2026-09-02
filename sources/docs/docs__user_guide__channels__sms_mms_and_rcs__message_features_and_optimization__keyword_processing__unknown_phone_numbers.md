---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/unknown_phone_numbers
slug: docs__user_guide__channels__sms_mms_and_rcs__message_features_and_optimization__keyword_processing__unknown_phone_numbers
title: "Handle unknown phone numbers - new users"
description: "This reference article covers how Braze processes unknown phone numbers from new users."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Handle unknown phone numbers - new users

You may find that after you get SMS, MMS, and RCS up and running with Braze, you receive messages from unknown users. The following steps describe how an unidentified user and number get processed.

## Opt-in/out and custom keyword workflow for unknown numbers

Braze automatically addresses an unknown number in one of three ways:

- If an opt-in keyword is texted:

- Braze creates an anonymous profile
 
- Our system sets the phone attribute
 
- Subscribes the user to the corresponding subscription group based on what opt-in keyword was received by Braze.

- If an opt-out keyword is texted:

- Braze creates an anonymous profile
 
- Our system sets the phone attribute
 
- Unsubscribes the user from the corresponding subscription group based on what opt-out keyword was received by Braze.

- If any other custom keyword is texted:

- Braze ignores the text message and does nothing.

- 

New Stuff!
