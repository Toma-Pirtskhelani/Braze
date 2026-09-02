---
url: https://www.braze.com/docs/user_guide/messaging/templates/in_app_message_templates/phone_number_capture
slug: docs__user_guide__messaging__templates__in_app_message_templates__phone_number_capture
title: "SMS, RCS, and WhatsApp sign-up form"
description: "This page covers how to create an SMS, RCS, and WhatsApp sign-up form with the in-app message drag-and-drop editor."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# SMS, RCS, and WhatsApp sign-up form

The SMS, RCS, and WhatsApp sign-up forms are templates available in the drag-and-drop editor for in-app messages. Use these templates to collect users’ phone numbers and grow your SMS, MMS, RCS, and WhatsApp subscription groups.

## Prerequisites

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. For more information, see Creating an in-app message with drag-and-drop: Prerequisites.

   Swift: 5.0.0+     Web: 2.5.0+     Android: 8.0.0+  

### SDK versions for text links

To include text links that do not dismiss the message, the following minimum SDK versions are required:

   Swift: 6.2.0+     Android: 26.0.0+  

warning

If you include a link in your in-app message that redirects to a URL and the user isn’t on the minimum SDK versions specified, clicking on the link will close the message, and the user won’t be able to return to the message to submit the form.

## Creating a phone number sign-up form

### Step 1: Choose your template

When creating a drag-and-drop in-app message, select SMS sign-up (this accommodates for RCS sign-up) or WhatsApp sign-up for your template, then select Build message. These templates are supported for both mobile apps and web browsers.

### Step 2: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

### Step 3: Customize your phone number input component

To get started building your sign-up form, select the phone number input component in the editor.

From the side menu, specify which subscription group this template will collect phone numbers for. To adhere to compliance best practices, you can only collect consent to one subscription group per phone number sign-up form. However, if desired, you can use multiple forms to collect consent for other subscription groups.

By default, we collect numbers globally, however you can limit the number of countries to collect numbers from. This is helpful if you intend to only message users who have phone numbers in specific countries, and can assist with list cleanliness. To do so, turn off Collect numbers from all countries and use the dropdown to select specific countries. Your users will only be able to select countries that you have explicitly added.

#### Invalid phone numbers

If your users input a phone number that includes any unaccepted special characters, they will see a generic error indicator that is not customizable and will not be able to submit the form. You can view the error behavior in the Preview & Test tab and on your test device. Refer to this article to learn how Braze formats phone numbers.

### Step 4: Add disclaimer language (for SMS and RCS sign-up forms)

For SMS and RCS sign-up forms, it’s important to clearly communicate the type of SMS or RCS you will be sending. Make sure your list growth is compliant by including the following information in your form:

- Description of the types of SMS and RCS messages your customers can expect (cart reminders, promotions and deals, appointment reminders, etc.). You don’t need to list every use case, but you should provide a description of the types of messages your brand will send.
 
- Note that consent is not a condition of any purchase (if applicable).
 
- Message frequency and reminder that message and data rates apply. If you don’t know the exact message frequency, you can say that frequency may vary.
 
- Links to your Terms & Conditions and SMS and RCS Privacy Policy.
 
- Reminder of help and opt-out keywords (HELP for help; STOP to cancel).

We have provided a placeholder disclaimer in the template solely as an example—it does not constitute legal advice and should not be relied upon for compliance purposes. It’s important to work with your legal team to develop language that is tailored to your specific brand.

note

This documentation is not intended to provide, nor may it be relied fully upon, as providing legal advise.

For more information about SMS and RCS compliance, see Laws and regulations for SMS, MMS, and RCS.

### Step 5: Style your message

Customize the look and feel of your message using the drag-and-drop in-app message components.

## Analyzing the results

After your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, you can create a segment of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

- 

New Stuff!
