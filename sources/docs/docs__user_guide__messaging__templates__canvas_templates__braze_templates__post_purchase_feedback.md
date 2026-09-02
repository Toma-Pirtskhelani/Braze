---
url: https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/post_purchase_feedback
slug: docs__user_guide__messaging__templates__canvas_templates__braze_templates__post_purchase_feedback
title: "Post-purchase feedback"
description: "This article describes how to use a Braze Canvas template to orchestrate personalized experiences that allow you to respond to feedback and build a relationship..."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Post-purchase feedback

Use the post-purchase feedback template to gain critical insight into how your customers interact with your brand and ensure they continue to have positive experiences. By leveraging personalized communication and a structured set of messages, you can continue to build and foster your customer relationships.

This article will walk you through a use case for the Post-Purchase Feedback template, which is designed for the conversion step of the user lifecycle. When you’re finished, you’ll have created a Canvas that encourages users to provide feedback for your app.

## Prerequisites

To successfully use this template, you’ll need the following:

- A custom attribute to reference for feedback survey results.
 
- A configured Braze Audience Sync with the partners and audiences you use.

## Tailoring the template to your needs

Let’s say we’re working for Decorumsoft, a mobile video game developer. We’ll use the post-purchase feedback template to gauge feedback for our latest video game launch, Proxy War 3: War of Thirst. Using this feedback, we’ll inform our development plans for the expansion pack, Liquid Mirage.

Before creating the Canvas, we set up the Braze Audience Sync to Google integration so that we can add user data from Braze to Google Audiences to send advertisements based on behavioral triggers, segmentation, and more.

To access the post-purchase feedback template, when creating a new Canvas, select Use a Canvas template > Braze templates. Then, next to Post-Purchase Feedback, select Apply Template. Now, we can go through the template to fit it for our needs.

### Step 1: Set up Canvas details

Let’s adjust the Canvas details to reflect our goal.

- Select Edit next to the template name.

- Update the Canvas name to specify that the Canvas is for targeting recent users.
 
- Update the description to specify that the Canvas is for encouraging users to submit feedback.
 
- Add the tag Feedback to filter for it on the Canvas home page.

### Step 2: Assign conversion events

Next, let’s assign our conversion events. Update the Primary Conversion Event - A to Make a specific purchase and select Proxy War.

We’ll keep the template’s conversion deadline of three days because we want to target our most recent users.

### Step 3: Set an entry schedule

- Keep the entry schedule type as Action-Based.
 
- Set the Start Time for the entry window to the date the game launches.

### Step 4: Determine who enters the Canvas

Our target audience for feedback is users who have recently purchased Proxy War 3.

- Select our target segment, “Purchased Proxy War 3”, which consists of users who’ve purchased the game.
 
- Select a filter to include users who have purchased “Proxy War 3” more than “0” times.

- Update the entry controls to not allow users to re-enter the Canvas after the Canvas’s maximum duration.

### Step 5: Select your send settings

We’ll keep the default subscription settings, so we only send to users who have subscribed or opted into receiving messages or notifications.

Because we want to be mindful with our sending, we’ll select Enable Quiet Hours to avoid requesting feedback between 11 pm and 10 am in our users’ time zone and only send at the next available time.

For our example, we’ll skip the other settings (frequency capping and seed groups).

### Step 6: Customize your Canvas

Next, we’ll build our Canvas by customizing the messaging channels and the content that will send to users. Because we’re only seeking feedback using email, in-app message, and webhook channels, we’ll go through the template and remove the SMS variants from the Message steps.

We’ll begin our customization by going through each messaging component to update the content. Our custom attribute to reference is Experience Feedback.

- In the Canvas builder, select the first Message step in the user journey.
 
- Select the Email variant.
 
- Fill out the Sending info with a subject that encourages user feedback.
 
- Select Edit message to replace the template’s email message with our feedback survey message. This includes replacing the links for each call-to-action to capture which option is selected, which will be referenced in the Action Path step of our user journey.

tip

You can use Canvas entry properties to customize the messages in your Canvas based on which product you’re referring to.

#### Set up feedback survey

Next, we’ll need to fill out the details for the In-App Message variant. This is where we need to specify our Experience Feedback custom attribute that indicates the sentiment of our user feedback. (We’ll also reference this in the subsequent Action Path step.)

- In the same first Message step, select the In-App Messages variant. We’ll keep the message controls as is.
 
- For the header and body, we’ll use language to encourage users to be honest about their experience with Proxy War 3.
 
- Because we want their survey responses to be logged with their profiles, we’ll keep the survey as Single-choice selection and Log attributes upon submission.
 
- For each of the three survey choices, select Experience Feedback as our custom attribute.
 
- We’ll keep the attribute values on the user profile as is since these values align with our custom attribute.

#### Build out the Action Path

Using our custom attribute Experience Feedback and the attribute values from the previous section, we’ll update the template’s Action Path to match our attribute and values.

### Set up ad retargeting

We’ll make sure our Google Audience sync is set up in our Ad Retargeting step. This will include selecting our ad account, an existing audience, and the option to add users to the audience.

### Set up webhook support cases

Next, let’s set up the webhook to trigger potential support cases. This can be especially insightful in combination with analyzing our user feedback.

For Message step named Support Case Creation, we’ll update the template to compose a webhook for users who are unsatisfied with their purchase and want a refund.

### Step 6: Test and launch the Canvas

After testing and reviewing our Canvas to make sure it works as expected, select Launch Canvas to launch the Canvas. Now, we can mindfully target users with a personalized user journey to encourage them to respond to our feedback survey based on their recent purchase of Proxy War 3!

tip

Check out our Pre and post-launch checklist for things to consider before and after you launch a Canvas.

- 

New Stuff!
