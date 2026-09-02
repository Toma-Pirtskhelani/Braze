---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers
slug: docs__user_guide__channels__whatsapp__whatsapp_setup__user_phone_numbers
title: "User phone numbers"
description: "This reference article covers WhatsApp phone number formatting, how to importing phone numbers, as well as how to add users to WhatsApp subscription groups."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# User phone numbers

This article will discuss different topics around your users’ or customers’ phone numbers.

Phone numbers are shown in the user profile in local formats, but will not be in the format you use to import the number ((724) 123 4567).

## Importing phone numbers

You can import phone numbers by uploading a CSV or via API to create a user.

### Formatting

It is important to import non-U.S. numbers in E.164 format, including the “+” and country code. Any phone numbers not provided in this format will be interpreted as a US number.

If a phone number is coerced into E.164 format but does not pass validation, Braze will not be able to send WhatsApp messages to this number. Any users with phone numbers that are not formattable will automatically exit from a Canvas step that includes WhatsApp

All U.S. numbers must be valid, 10-digit phone numbers with a valid area code. They can be input without the + and country code, as Braze will assume and map all valid, 10-digit phone numbers as U.S. numbers.

All international numbers should start with a +, followed by their country code and then the phone number. (e.g +442071838750)

However, to ensure accuracy in the event that you are sending to multiple regions with different country or area codes, it is recommended to use the E.164 format, even for U.S.-based phone numbers.

You can see the differences between local number formatting as well as universal, E.164 formatting in the following table:

 Country | 
 Local | 
 Country Code | 
 E.164 | 

 USA | 
 4155552671 | 
 1 | 
 +14155552671 | 

 UK | 
 02071838750 | 
 44 | 
 +442071838750 | 

 Brazil | 
 1155256325 | 
 55 | 
 +551155256325 | 

### Adding users to WhatsApp a subscription group

For a customer to receive an WhatsApp message, they must have a valid phone number and be opted-in to a subscription group. For more information, refer to WhatsApp subscription groups.

### Multiple users with the same phone number

If multiple users have the same phone number within a segment of a single campaign or Canvas step, Braze will deduplicate the sending and send only one message to that one phone number.

- 

New Stuff!
