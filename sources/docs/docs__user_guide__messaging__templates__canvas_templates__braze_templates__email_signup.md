---
url: https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/email_signup
slug: docs__user_guide__messaging__templates__canvas_templates__braze_templates__email_signup
title: "Email sign-up with double opt-in"
description: "This article describes how to use a Braze Canvas template to expand your reach with verified email sign-ups."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Email sign-up with double opt-in

Use the email sign-up with double opt-in template to expand your reach with verified email sign-ups. Target new users to capture their email, confirm their subscription, and receive a promotion code, all in one seamless journey.

This article will walk you through a use case for the Email sign-up with double opt-in template, which is designed for the consideration stage of the user lifecycle. When you’re finished, you’ll have created a Canvas that sends emails and in-app messages to users when they start a session or when they haven’t completed their onboarding.

## Prerequisites

To successfully use this template, you need the following:

- A multi-page in-app message with one page to capture your users’ emails and another to communicate a success message.
 
- A confirmation email for users to verify their email address.
 
- A welcome email with an exclusive promotion code for users who double opt-in.

## Tailoring the template to your needs

Let’s say you’re working for Steppington, a health app known for its features such as calorie tracking, digital exercise classes, and flash-mob marathons. Before creating the Canvas, you set up multi-page in-app and in-browser messages that include a series of engaging questions to determine the experience and impression of a user’s first ride with the app.

To access the template, when creating a new Canvas, select Use a Canvas template > Braze templates. Then, next to Email sign-up with double opt-in, select Apply Template. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details

Adjust the Canvas details to reflect your goal.

- Select Edit next to the template name.

- Update the Canvas name to specify that the Canvas is for targeting new users when they first use the app.
 
- Update the description to explain that this Canvas contains personalized messaging for users to double-opt in.
 
- Add the tag Email so that we can filter for it on the Canvas home page.

### Step 2: Assign conversion events

Next, assign our conversion events. Conversion events are a type of metric that you can use to measure the success of the Canvas. For Conversion event type, select Performs Custom Event. Then, select email_opt_in for the Custom event name.

Keep the template’s conversion deadline of three days because you want to target your most recent users.

### Step 3: Tailor the entry schedule

Keep the entry schedule as Action-Based so that users enter your Canvas when they start a session in the app. This way, you can begin to build your relationship with timely engagement.

Also, consider keeping the Action Based Options as is so that users enter the Canvas only when they start a session.

For the Entry Window, update the Started Time (Required) to our desired date and time.

### Step 4: Select the target audience

Define your target audience as Steppington users who don’t have an email address in their user profile by keeping the template’s default segmentation filter Email Available is false.

### Step 5: Select your send settings

Keep the default subscription settings, so you send only to users who have subscribed or opted in to receiving messages or notifications, and skip the other settings (frequency capping, quiet hours, and seed groups).

### Step 6: Customize your Canvas

Next, build the Canvas by customizing the channels and content that you want to send to users. Because you’re focusing on verifying email sign-ups, you don’t need to add or remove any of the template’s Canvas steps and channels.

- Select the first Message step named Email Sign-up. This is where you update the template to use our multi-page in-app (and in-browser) message.

- Page 1 captures the emails.
 
- Page 2 displays a confirmation message.

- From here, keep the Subscribed Action Path step as is. This step splits our users into two groups in a one-day window:

- Users who have subscribed to Steppington with their email
 
- Users who haven’t subscribed to Steppington with their email

- Next, replace the email body with our branded confirmation email for the Verify Email Message step. This will send an email to our subscribed users and prompt them to confirm their email address and opt in to our messaging.
 
- Keep the Confirm Subscription Action Path step as is. This step further splits our users into those who have confirmed their email and those who have not, with a one-week window.
 
- Lastly, update the Welcome + Discount Message step with our confirmation email that includes an exclusive promotion code.

note

The Verify Email Message step is triggered on the user’s second session. This is because the first session start event would trigger the Canvas, but a second session start after the user has reached the first Email Sign-up Message step is required for the user to be eligible to trigger the second in-app message.

### Step 7: Test and launch your Canvas

After testing and reviewing your Canvas to make sure it works as expected, launch it by selecting Launch Canvas.

tip

Check out our Pre and post-launch checklist for things to consider before and after you launch a Canvas.

- 

New Stuff!
