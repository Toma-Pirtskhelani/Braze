---
url: https://www.braze.com/docs/user_guide/messaging/templates/in_app_message_templates/email_discount
slug: docs__user_guide__messaging__templates__in_app_message_templates__email_discount
title: "Email sign-up with discount"
description: "This reference page covers how to use the in-app message drag-and-drop editor to build an email sign-up form that offers a discount for new subscribers...."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Email sign-up with discount

Use the in-app message drag-and-drop editor to build an email sign-up form that offers a discount for new subscribers.

## Prerequisites

### Minimum SDK versions

Messages created using the drag-and-drop editor can only be sent to users on the following minimum SDK versions. For more information, see Creating an in-app message with drag-and-drop: Prerequisites.

   Swift: 5.0.0+     Web: 2.5.0+     Android: 8.0.0+  

### SDK versions for text links

To include text links that do not dismiss the message, the following minimum SDK versions are required:

   Swift: 6.2.0+     Android: 26.0.0+  

warning

If you include a link in your in-app message that redirects to a URL and the user isn’t on the minimum SDK versions specified, clicking on the link will close the message, and the user won’t be able to return to the message to submit the form.

## Creating an email sign-up form with a discount

### Step 1: Choose your template

When creating a drag-and-drop in-app message, select Email sign-up with welcome discount for your template, then select Build message. This template is supported for both mobile apps and web browsers.

### Step 2: Set up your message styles

Before you start customizing your template, you can set message-level styles for the entire message using the side menu. For example, you may want to customize the font of all the text or the color of all the links included in your message. You can also make the message a modal or fullscreen display type.

### Step 3: Customize your email sign-up component

To get started building your email sign-up form, select the email capture element in the editor. By default, collected email addresses will have the global subscription group Subscribed. To opt in users to specific subscription groups, refer to Updating email subscription states.

You can customize the placeholder text and label text of the email capture element.

#### Email validation

If the user enters an email address that includes any unaccepted special characters, they will see a generic error indicator and won’t be able to submit the form. This error message isn’t customizable. You can view the error behavior in the Preview & Test tab and on your test device. Learn more about how Braze formats email addresses in Email validation.

### Step 4: Add disclaimer language (optional)

We recommend including opt-in language and links to your brand’s privacy policy and terms and conditions in your message. Be sure to work with your legal team to develop language that is tailored to your specific brand.

note

Deliverability best practices often exceed legal requirements, and our recommendation is to always obtain explicit consent to send emails and allow users to easily decline.

### Step 5: Style your message

Customize the look and feel of your sign-up form and discount using the drag-and-drop in-app message components.

## Analyzing the results

After your campaign has launched, you can analyze results in real time to see how many users have engaged with your campaign. To see how many users have opted in to the subscription group, you can create a segment of users who subscribed to the subscription group by filtering for users who have received the in-app message and submitted the form.

## Best practices

### Double opt-in verification

To make sure that anyone who signed up for your list meant to sign up for your list and provided the correct email address, we recommend getting a second confirmation from anyone who signed up through your email sign-up form by sending a double opt-in flow.

One of the ways you can set this up is through Canvas:

- Build a Canvas that is action-based and set it up to trigger when a user adds an email address to Braze. Make sure that you allow for targeting users who are new to the platform (for example, by using a segment with no filters in the Canvas).
 
- Create an email message step with a CTA that has a hyperlink to the {{${set_user_to_opted_in_url}}} Liquid tag. This will change the user’s email subscription state to opted_in when they click the button.
 
- Add an Action Paths step.
 
- For the first path, trigger an email when a user changes their email subscription status to opted_in. This email should inform users that their email has been confirmed.
 
- Set up the other path to exit the Canvas after the window expires.

- 

New Stuff!
