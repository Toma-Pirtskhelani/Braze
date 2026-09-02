---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers
slug: docs__user_guide__channels__sms_mms_and_rcs__message_setup__user_phone_numbers
title: "User phone numbers"
description: "This reference article covers SMS phone number formatting, how to importing phone numbers, as well as how to add users to SMS subscription groups."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# User phone numbers

This article will discuss different topics around your users’ or customers’ phone numbers. If you’re looking for information about your own numbers, go to our article on sending phone numbers.

## Recommended format

We recommend importing phone numbers in E.164 format to ensure accuracy in the event that you are sending to multiple regions with different country or area codes—even for U.S.-based phone numbers.

- U.S. numbers: All U.S. numbers must be valid, 10-digit phone numbers with a valid area code. If any 10-digit phone number is missing a + and country code, Braze maps it as U.S. numbers. Puerto Rican phone numbers still require a + and country code even though they use 10-digit formatting with U.S.-style area codes.
 
- International numbers: All international numbers should start with a +, followed by their country code and then the phone number. For example, +442071838750.

Here’s a few examples showing the differences between local and E.164 formatting:

 Country | 
 Local | 
 Country Code | 
 E.164 | 

 USA | 
 4155552671 | 
 1 | 
 +14155552671 | 

 UK | 
 2071838750 | 
 44 | 
 +442071838750 | 

 Brazil | 
 1155256325 | 
 55 | 
 +551155256325 | 

## Import phone numbers

When importing phone numbers, it’s important that you follow the recommended format. To import phone numbers, use one of the following methods:

- Uploading a CSV to Braze
 
- Using the /users/track endpoint

important

User phone numbers appear in Braze as a string of digits. If you import a number that contains non-digits (such as ,, -, or () other than the leading +, the non-digits are removed when rendered in Braze. For example, importing +1 (724) 123-4567 appears as +17241234567.

## Phone number validation

Braze uses Google’s libphonenumber library to validate phone numbers. When new mobile number prefixes are introduced, support is added as the upstream library is updated. Braze does not maintain a separate list of valid prefixes.

### Handling invalid phone numbers

When a phone number is deemed invalid, Braze marks the user’s phone number as invalid and does not attempt to send further communications to that phone number. An invalid phone number is marked in the Engagement Tab of a user profile.

A phone number is considered invalid for the following reasons:

- Provider Error: a permanent error was received from the SMS and RCS provider. This indicates that the phone number supplied is incorrectly formatted or permanently unable to receive SMS or RCS messages.
 
- Deactivated: the phone number has been deactivated due to a mobile subscriber terminating their service and releasing their number from their carrier (and may eventually be recycled and assigned to a new user). A deactivated phone number can be marked invalid even if you have not sent any SMS or RCS messages to that phone number.

These invalid phone numbers can be managed using SMS and RCS endpoints.

note

If multiple user profiles have the same phone number and that phone number is marked invalid, then all existing User Profiles with that number will display as invalid. Newly created user profiles will never initially be marked as invalid.

You can also include or exclude any users with invalid phone numbers when creating a segment.

## Exclude rejected SMS sends from segmentation

important

SMS rejections may count toward your SMS allotment depending on your Braze contract and SMS provider. For billing outcomes, see Reporting.

To exclude users with rejected SMS sends from your segments, use SQL Segment Extensions, do the following:

- Go to Audience > Segment Extensions.
 
- Select Create New Extension > Full refresh or Incremental refresh.
 
- Write a SQL query that identifies users with SMS rejections. For example, you can query the USERS_MESSAGES_SMS_REJECTION_SHARED event to find users who have received SMS rejections.
 
- Save your Segment Extension.
 
- When creating your SMS segment, add a filter to exclude users in this Segment Extension.

## Add users to SMS and RCS subscription groups

For a user to receive an SMS or RCS message, they must have a valid phone number and be opted-in to a subscription group. Subscription groups are tied to the SMS or RCS program you are running (make sure you follow the legal requirements for SMS, MMS, and RCS and have recorded consent for each customer). For more information, refer to SMS and RCS subscription groups.

## Third-party sourcing and verification

Braze relies on third-party tools to source invalid numbers. Braze is not responsible for any outages or misinformation of these services. Thus, this tool should not be relied upon as your sole method of compliance for verifying invalid numbers.

## Phone number capture

To capture phone numbers through in-app messages, refer to SMS, RCS, and WhatsApp sign-up form.

- 

New Stuff!
