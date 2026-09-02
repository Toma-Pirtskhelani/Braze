---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs
slug: docs__user_guide__channels__whatsapp__message_processing__opt_ins_and_opt_outs
title: "Opt-in and opt-out"
description: "This reference article covers different WhatsApp opt-in and opt-out methods."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Opt-in and opt-out

Handling WhatsApp opt-ins and opt-outs is crucial as WhatsApp monitors your phone number quality rating, and low ratings may result in your message limits being reduced. 

One way to build a high-quality rating is to prevent users from blocking or reporting your business. This can be done by providing high-quality messaging (such as value to your users), controlling message frequency, and allowing customers to opt-out of receiving future communications. 

For a cross-channel overview of WhatsApp subscription status, see Subscription status. This page covers how to set up opt-ins and opt-outs, and the differences between the “regex” and “is” modifiers.

Opt-ins can come from external sources or from Braze methods, such as SMS or in-app and in-browser messages. Opt-outs can be dealt with using keywords set in Braze and WhatsApp marketing buttons. Reference the following methods for guidance on setting up opt-ins and opt-outs.

## Opt-in methods

- External to Braze opt-in methods

- Externally built opt-in list
 
- Outbound message in customer support WhatsApp channel
 
- Inbound WhatsApp message

- Braze-powered opt-in methods

### Opt-out methods

- General opt-out keywords
 
- Marketing opt-out selection

## Set up opt-ins for your Braze WhatsApp channel

For WhatsApp opt-ins, you must comply with WhatsApp’s requirements. You will also need to provide Braze with the following information:

- An external_id, a phone number, and an updated subscription status for every user. This can be done by using the SDK or through the /users/track endpoint to update the phone number and subscription status.

An inbound WhatsApp message doesn’t automatically subscribe a user to your WhatsApp subscription group. You must explicitly update the subscription status with a User Update step, webhook, or API call.

Meta requires opt-in copy to:

- Clearly state that the person is opting in to receive messages from your business
 
- Include your business name (not generic language such as “we’ll message you”)
 
- Comply with applicable local laws

Meta allows general messaging consent that meets these requirements instead of requiring WhatsApp-specific consent. However, Braze recommends collecting channel-specific WhatsApp consent so users know where to expect your messages.

note

Braze released an improvement to the /users/track endpoint that allows updates to the subscription status that you can learn about in Subscription groups. However, if you have already created opt-in protocols using the /v2/subscription/status/set endpoint, you may continue to do so there.

### Manage consent for different use cases

WhatsApp subscription status applies to the subscription group associated with a sending phone number. It doesn’t distinguish between marketing, utility, or other use cases that share the same number. For example, unsubscribing a user from the subscription group prevents you from targeting that user with messages from the number, regardless of the message category.

To manage consent separately by use case, choose one of these approaches:

- Use separate WhatsApp phone numbers and subscription groups for each use case.
 
- Use one phone number, store use-case consent in custom attributes, and exclude users who haven’t consented from the relevant campaign or Canvas audience.

Custom attributes don’t replace the WhatsApp subscription group. Users must still be subscribed to the phone number’s subscription group to receive messages through Braze.

### External to Braze opt-in methods

Your app or website (account registration, checkout page, account settings, credit card terminal) to Braze.

Wherever you already have marketing consent for email or texting, include an additional section for WhatsApp. After a user opts-in, they need an external_id, a phone number, and updated subscription status. To do this, depending on how your install of Braze is set up, either leverage the /subscription/status/set endpoint or use the SDK.

#### Externally built opt-in list

If you have used WhatsApp previously, you may have already built a user list with opt-ins per the WhatsApp requirements. In this case, upload a CSV or use the API with the following information into Braze.

#### Outbound message in customer support WhatsApp channel

In your customer support channel, follow up on resolved issues with an automatic message asking if they want to opt-in to marketing messaging. The functionality here depends on the feature availability in your customer support tool of choice and where you keep user information.

- Provide a message link from your WhatsApp Business phone number.
 
- Provide quick reply actions where the customer replies “Yes” to indicate opt-in
 
- Set up custom keyword trigger.
 
- For either of those ideas, you will probably need to finish the path with the following:

- Call the /users/track endpoint to either update or create a user
 
- Leverage the /subscription/status/set endpoint or use the SDK

#### Inbound WhatsApp message

Have customers send an inbound message to the WhatsApp number.

This can be set up as a Canvas or a campaign, depending on whether you’d like the user to receive a confirmation message on the new channel.

- Create a campaign with the action-based delivery trigger of an inbound message.
 
- Create a webhook campaign. For an example webhook, see Subscription groups.

tip

Note that you can build a URL or QR code to join a WhatsApp channel from within the WhatsApp manager under Phone Number > Message Links.

### Braze-powered opt-in methods

#### SMS message

In Canvas, set up a campaign that asks customers if they want to opt-in to receiving WhatsApp messages by using one of the following methods:

- Customer segment: subscribed marketing group outside of the US
 
- Custom keyword trigger setup

Learn about updating the subscription status of user profiles by viewing Subscription groups.

#### In-app or in-browser message

Create an in-app message or in-browser pop-up prompting customers to opt-in to WhatsApp usage.

Use HTML in-app message with JavaScript “bridge” to interface with Braze SDK. Make sure to use the WhatsApp subscription group ID.

#### Phone number capture form

Use the phone number capture form template in the drag-and-drop editor for in-app messages to collect user phone numbers and grow your WhatsApp subscription groups.

## Set up opt-outs for your Braze WhatsApp channel

### WhatsApp “Offers and Announcements” toggle

WhatsApp provides an “Offers and Announcements” toggle in the app settings that allows users to opt out of marketing messages. This toggle operates independently from Braze subscription groups:

- Braze subscription groups are managed through your Braze integration (API, preference center, or SDK) and control which users you target for messaging.
 
- WhatsApp’s native toggle is controlled by Meta and enforced at the platform level, outside of Braze.

These two layers don’t sync automatically by design. When a user turns off the “Offers and Announcements” toggle in WhatsApp, Meta blocks marketing message delivery at the platform level, even if the user’s Braze subscription status shows as “Subscribed”. The user’s preference is respected at the point of delivery.

note

Because Braze doesn’t receive an opt-out signal until a send attempt is made and Meta returns an error, subscription counts in Braze may not reflect users who have opted out through the WhatsApp toggle until a message is attempted. This means reach estimates may be slightly overstated until that feedback loop occurs.

### General opt-out keywords

You can set up a campaign or Canvas that allows users who message in particular words to opt-out of future messaging. Canvases can be especially beneficial as they allow you to include a follow-up message that confirms the successful opt-out.

#### Step 1: Create a Canvas with a trigger of “Inbound WhatsApp Message”

When selecting keyword triggers, include words like “Stop” or “No Message”. If you choose this method, ensure your customers know your opt-out words. For example, after receiving the initial opt-in, include a follow-up response like “To opt-out of these messages, message “Stop” at any time.”

#### Step 2: Update the user’s profile

Update the user’s profile by using one of the methods described in Subscription groups.

### Marketing opt-out selection

Within the WhatsApp message template creator, you can include the “marketing opt-out” option. Any time you include this, ensure the template is used in a Canvas with a subsequent step for a subscription group change.

- Create a message template with the “marketing opt-out” quick reply.

- Create a Canvas that uses this message template.

- Follow the steps in the preceding example but with the trigger text “STOP PROMOTIONS”.

- Update the user’s subscription status by using one of the methods described in Subscription groups.

## Set up opt-in and opt-out workflows

You can configure “START” and “STOP” keyword response workflows for WhatsApp with these two methods:

- User Update step
 
- Webhook campaign to trigger a second WhatsApp campaign

### User Update step

The User Update step can add the user’s phone number to the WhatsApp subscription group when the user sends a keyword to the subscription group’s phone number.

The User Update step avoids race conditions because the user won’t progress to the next step in the Canvas before their phone number is added to the subscription group. It also has fewer steps to set up than the other methods, so Braze generally recommends this method.

- Create a Canvas with the action-based step Send a WhatsApp Inbound Message. Select Where the message body and enter “START” for Is.

important

For “STOP” messages, invert the message step confirming the opt-out and the User Update step. If you don’t, the user will be opted out of the subscription group first, and then will not be eligible to receive the confirmation message.

- In the Canvas, create a Set Up User Update step and for Action select Advanced JSON Editor. 

- Populate the User Update object with the following JSON payload, replacing XXXXXXXXXXX with your subscription group ID:

```

1
2
3
4
5
6
7
8
9
10
11
12

```
 | 
```
{
 "attributes": [
 {
 "subscription_groups": [
 {
 "subscription_group_id": "XXXXXXXXXXX",
 "subscription_state": "subscribed"
 }
 ]
 }
 ]
}

```
 | 

- Add a subsequent WhatsApp message step. 

#### Considerations

The update might complete at variable speeds because Braze batches the User Update step requests. For time-sensitive opt-in flows where the confirmation must send immediately after the subscription update, use the webhook method instead of a User Update step.

### Webhook campaign to trigger a second WhatsApp campaign

A Webhook campaign can trigger entry into a second campaign after adding the user’s phone number to the WhatsApp subscription group when the user sends a keyword to the subscription group’s phone number.

important

You do not need to use this method for STOP messages. The confirmation message will be sent before the user is removed from the subscription group, so you can use one of the other two steps.

- Create a campaign or Canvas with an action-based step Send a WhatsApp Inbound Message. Select Where the message body and enter “START” for Is.

- In the campaign or Canvas, create a Webhook Message step, and change the Request Body to Raw Text.

- Enter the customer’s endpoint URL in the Webhook URL, followed by the endpoint link campaigns/trigger/send. For example, https://dashboard-02.braze.eu/campaigns/trigger/send.

- In the raw text, enter the following JSON payload and replace XXXXXXXXXXX with your subscription group ID. You will need to replace the campaign_id after creating your second campaign.

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

```
 | 
```
{
 "campaign_id": "XXXXXXXXXXX",
 "recipients": [
 {
 "external_user_id": "{{${user_id}}}",
 "attributes": {
 "subscription_groups": [
 {
 "subscription_group_id": "XXXXXXXXXXX",
 "subscription_state": "subscribed"
 }
 ]
 }
 }
 ]
}

```
 | 

- Create a WhatsApp campaign (your second campaign) and set the trigger to API. Make sure you copy this campaign_id into the JSON payload of your first campaign.

#### Considerations

- Attribute updates from within the Canvas API trigger JSON payload is not yet supported, so you can only trigger a WhatsApp campaign for the WhatsApp response message (as in step 2).
 
- A WhatsApp template must be approved to send it as a response message. This is because a quick response requires the inbound message trigger to be inside the same campaign or Canvas. If you use a User Update step, you can send a quick response message without Meta approval.

## Understanding the difference between “regex” and “is” modifiers

In this table, STOP is used as an example trigger word to demonstrate how the modifiers work.

 Modifier | 
 Trigger word | 
 Action | 

 Is | 
 STOP | 
 Catches any whole word use of “stop” regardless of case. For example, this catches “stop” but not “please stop”. | 

 Matches regex | 
 STOP | 
 Catches any use of “STOP” in that exact case. For example, this catches “STOP” and “PLEASE STOP” but not “stop”. | 

 Matches regex | 
 (?i)STOP(?-i) | 
 Catches any use of “STOP” in any case. For example, this catches “stop”, “please stop”, and “never stop sending me messages”. | 

- 

New Stuff!
