---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling
slug: docs__user_guide__channels__sms_mms_and_rcs__message_features_and_optimization__keyword_processing__keyword_handling
title: "Custom keyword handling"
description: "This reference article covers how Braze deals with two-way SMS, MMS, and RCS messaging and auto-responses. This includes explanations on how keyword triggering works as..."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Custom keyword handling

This reference article covers how Braze deals with two-way SMS, MMS, and RCS messaging and auto-responses. This includes explanations on how keyword triggering works as well as custom keyword categories and multi-language support.

## Two-way messaging (custom keyword responses)

Two-way messaging allows you to send messages and process the responses to those messages. It requires end-users to send a keyword to Braze, to which that user will receive an automatic reply. Applied correctly, two-way messaging can be a simple, immediate, and dynamic solution to customer marketing, saving time and resources along the way.

## Managing keywords and auto responses

SMS, MMS, and RCS with Braze gives you the option to create keyword triggers, custom responses, define keyword sets for multiple languages, and establish custom keyword categories.

note

Braze uses your full set of opt-out keywords (default keywords and custom keywords) for exact opt-out handling and fuzzy opt-out.

- add keyword triggers
 
- manage responses

### Add keyword triggers

In addition to the default opt-in and opt-out keywords, you may also define your own keywords to trigger Opt-In, Opt-Out, and Help responses.

To define your own keywords, do the following:

- In the Braze dashboard, go to Audience > Subscription Group Management and select an SMS/MMS/RCS subscription group.
 
- Under Global Keywords, select the pencil icon next to the keyword category you want to add a keyword to. 

- In the tab that opens, add a keyword you want to trigger this keyword category. Note that keywords are case insensitive, and universal keywords like START, YES, and UNSTOP cannot be changed. 

The following rules apply to keywords and keyword responses:

 Keywords | 
 Keyword responses | 

 - Valid UTF-8 encoded characters
- Maximum of 20 keywords per category total
- Maximum length of 34 characters
- Minimum length of 1 character 
- Cannot contain spaces
- Required to be case insensitive and unique across the subscription group | 
 - Cannot be blank
- Maximum length of 300 characters
- Valid UTF-8 characters | 

tip

Interested in seeing how these keywords can be used in your campaigns and Canvases to retarget and trigger messages? Visit User retargeting for more information.

### Manage responses

You can manage your own responses that are sent to users after they text in a keyword to a specific keyword category.

- In the Braze dashboard, go to Audience > Subscription Group Management and select an SMS/MMS/RCS subscription group. 

- Under Global Keywords, select a keyword category to edit a response for by selecting the pencil icon. 

- In the tab that opens, edit your response. Be mindful of our six rules to get compliance right as you create your response, and read the following rules that apply to keywords and keyword responses.

- To automatically shorten static URLs in your response, select the Link Shortening toggle. The character counter will update to show the expected length of the shortened URL. 

#### Considerations

 Keywords | 
 Keyword responses | 

 - Valid UTF-8 encoded characters
- Maximum of 20 keywords per category total
- Maximum length of 34 characters
- Minimum length of 1 character 
- Cannot contain spaces
- Required to be case insensitive and unique across the subscription group | 
 - Cannot be blank
- Maximum length of 300 characters
- Valid UTF-8 characters | 

tip

If an action-based Canvas is triggered by an inbound SMS, MMS, or RCS message, you can reference SMS, MMS, or RCS properties in the first message step of the Canvas.

## Multi-language support

When sending to certain countries, a sender may be required to support inbound keywords and outbound replies with a local language. To support this, Braze allows you to create a language-specific keyword setting. When created, language-specific keyword settings will apply to all sending numbers within the subscription group. 

### Creating language-specific keywords

Select Add a Language and select your target language or search for a language within the dropdown.

important

Non-English languages do not come with preset keywords and responses, so senders will need to work with their marketing and legal teams to add any required keywords to this set. Otherwise, Braze will not handle localized incoming messages for those languages.

If you need to delete a language, select the Delete Language button at the bottom of the page.

## Custom keyword categories

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), you can also create up to 25 of your own keyword categories. This allows you to identify arbitrary keywords and set up responses specific to your business. An example category might be “PROMO” or “DISCOUNT”, which might prompt a response about promos that are happening this month.

These custom keywords operate in an “always-on” capacity, meaning that any user subscribed to your message service can text keywords and receive a response at any point. In addition to this behavior, you also have the option to define specific keywords that can only be sent to at certain points of your user’s lifecycle.

### Creating a custom category

To create a custom keyword category, do the following:

- Edit the appropriate subscription group.
 
- Select Add custom keyword. 
 
- Provide a keyword category name and define which keywords a user can text in to receive the reply message.

After this keyword category is created, it will be available to filter and trigger against in your campaigns and Canvases.

Keywords created in custom keyword categories adhere to all of the rules and validations for the creation of new keywords.

### Lifecycle-specific keywords

If you have a use case where you would like to limit when a customer can send a specific keyword during their lifecycle (for example, during their first initial onboarding) to receive a response, you can use the trigger Sent inbound SMS to subscription group within keyword category OTHER in your campaign or Canvas and define keywords that your users can send in at a point in time.

This trigger supports filtering on the specific inbound message using is or is not comparisons of the message, as well as matches or does not match regex rules to validate the user’s input.

#### Canvas

#### Campaign

### Dealing with unknown keywords

We strongly recommend setting up an auto-response when subscribed users text something that doesn’t match any of your defined keywords (handled under the OTHER keyword category).

To send a default reply—for example, “Sorry! We didn’t recognize that keyword.”—do the following:

- Create an SMS campaign.
 
- For Target audience, choose All users (the trigger still limits who receives the message).
 
- For Schedule, choose Action-based delivery.
 
- Set the trigger to Send inbound SMS to the appropriate subscription group within keyword category OTHER.
 
- In the Messaging step, enter the response body you want users to receive.

For how Braze handles inbound messages from unknown phone numbers (before a profile exists), see Handle unknown phone numbers.

tip

Interested in seeing how these keywords and keyword categories can be used in your campaigns and Canvases to retarget and trigger messages? Visit User retargeting for more information.

- 

New Stuff!
