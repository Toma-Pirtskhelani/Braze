---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage
slug: docs__user_guide__messaging__design_and_edit__personalize__sources__promotion_codes__manage
title: "Use promotion codes"
description: "Learn how to use promotion codes and view usage for your campaigns and Canvases."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Use promotion codes

Learn how to use promotion codes and view usage for your campaigns and Canvases.

## Prerequisites

Before you can use promotion codes, you’ll need to create a promotion code list.

## Using promotion codes

To send a promotion code in a message, select Copy Snippet next to the promotion code list you previously created.

Paste the code snippets into one of your messages in Braze, then use Liquid to insert one of the unique promotion codes from your list. That code is marked as sent, ensuring no other message sends the same code.

### Across Canvas steps

When a code snippet is used in a campaign or Canvas with multichannel messages, each user receives a unique code. In a Canvas with multiple steps that reference promotion codes, a user gets a new code for every step they enter.

To assign one promotion code in a Canvas and reuse it across steps:

- Assign the promotion code as a custom attribute in the first step (User Update).
 
- Use Liquid in later steps to reference that custom attribute instead of generating a new code.

When a user qualifies for a code across multiple channels, they receive the same code in each channel. For example, if they get messages by email and push, the same code is sent to both. Reporting also reflects a single code.

note

If no promotion codes are available, test or live messages that rely on codes do not send.

### In-app message campaigns

After creating an in-app message campaign, you can insert a promotion code list snippet into your in-app message message body. Promotion codes in in-app messages are deducted and used only when a user triggers the display of the in-app message.

### Test messages

Test sends and seed group email sends use up promotion codes unless requested otherwise. Contact your Braze account manager to update this feature behavior so promotion codes aren’t used during test sends and seed group email sends.

### With message extras for Currents

You can combine message_extras with promotion codes to send promotion code information to Currents. Use the capture tag to store the promotion code in a variable, then reference that variable in message_extras:

```

1
2
3
4
5

```
 | 
```
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}

```
 | 

## Saving promotion codes to user profiles

To reference the same promotion code in subsequent messages, the code must be saved to the user profile as a custom attribute. This can be done through a User Update step that assigns the discount code to a custom attribute, like “Promo Code”, directly before a Message step.

First, select the following for each field in the User Update step:

- Attribute Name: Promo Code
 
- Action: Update
 
- Key Value: The promotion code’s Liquid code snippet, such as {% promotion('spring25') %}

Second, add the custom attribute (in this example, {{custom_attribute.${Promo Code}}}) to a message. The discount code is templated in.

## Viewing promotion code usage

You can find the remaining code count in the Remaining column of the promotion code list on the Promotion Codes page.

This code count can also be found when revisiting a pre-existing promotion code list page. You can also export unused codes as a CSV file.

## Multichannel and single-channel sends

For multichannel and single-send campaigns and Canvases, all promotion codes referenced in a message’s Liquid are deducted to be used before the message is sent to make sure the following occurs:

- The same promotion codes are used across channels in a multichannel message.
 
- Extra promotion codes are not used if a message fails or aborts.

If a user has two promotion code lists referenced in one message that is split by a Liquid conditional logic tag, all promotion codes are still deducted, regardless of which conditional flow the user follows.

If a user enters a new Canvas step or re-enters a Canvas, and the promotion code Liquid snippet is applied again for a message to that user, a new promotion code is used.

### Example

In the following example, both promotion code lists vip-deal and regular-deal are deducted. Here’s the Liquid:

```

1
2
3
4
5

```
 | 
```
{% if user.is_vip %}
 {% promotion('vip-deal') %}
{% else %}
 {% promotion('regular-deal') %}
{% endif %} 

```
 | 

Braze recommends uploading more promotion codes than what you estimate using. If a promotion code list expires or runs out of promotion codes, the subsequent messages are aborted.

tip

Here’s an analogy for how promotion codes are used up in Braze. 

Imagine that sending your message is like sending a letter at the post office. You give the letter to a clerk, and they see that your letter should include a coupon. The clerk pulls the first coupon from the stack and adds it to the envelope. The clerk sends the letter, but for some reason, the letter gets lost in the mail (and the coupon is also now lost). 

In this scenario, Braze is the postal clerk, and your promotion code is the coupon. We cannot retrieve it after it has been pulled from the stack of promotion codes, regardless of the webhook result.

- 

New Stuff!
