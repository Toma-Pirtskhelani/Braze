---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting
slug: docs__user_guide__channels__sms_mms_and_rcs__message_features_and_optimization__user_retargeting
title: "User retargeting"
description: "This reference article covers how users can retarget their messages by a user's SMS and RCS interactions."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# User retargeting

In addition to changing the user’s subscription state and sending auto-responses based on incoming keywords, Braze will also record interactions to the user profile for filtering and triggering messages.

These filters and triggers allow you to filter actions based on users who have been sent or have responded to SMS, MMS, and RCS campaigns, or further engage with users who have clicked shorted URLs.

tip

To read more about custom keywords and how to set up two-way messaging to take advantage of these retargeting options, visit our custom keyword article.

## Retargeting options

note

When building audiences with user retargeting, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the CUP. Marketers should implement the relevant filters for users’ eligibility within their Canvas and/or Campaign entry criteria.

### Filter users by SMS, MMS, and RCS

Users can be filtered by when they last received an SMS, MMS, or RCS or if they have received an SMS, MMS, or RCS from a specific campaign. Filters can be set in the Target Audiences step of the campaign builder.

note

When a message is received, opened, or clicked, Braze updates data for all profiles that share the same phone number as the profile that logged the interaction. Users who share a phone number with someone who received, opened, or clicked the message can match this filter even if they were not originally in the campaign or were not directly sent the message.

#### Filter by last received SMS/MMS/RCS

#### Filter by received messages from SMS/MMS/RCS campaign

Filters users who have received a message from a specific campaign. With this filter, you also have the option to filter off those that have not received messages from a campaign.

### Trigger messages as users receive SMS, MMS, or RCS

To trigger messages as users receive SMS, MMS, or RCS messages from a specific campaign, select Interact with Campaign as the trigger action for an action-based campaign. Next, select Receive SMS and the SMS, MMS, or RCS campaign you would like to use.

### Filter by advanced tracking links

Retarget users who have clicked campaigns with advanced tracking links.
Only campaigns that have advanced tracking enabled appear in the following dropdowns:

#### Retarget users who have clicked a specific SMS, MMS, or RCS Campaign

- Create a segment using the Clicked/Opened Campaign filter.
 
- Select clicked shortened sms link.
 
- Choose the desired campaign.

#### Retarget users who have clicked a specific Canvas Step

- Create a segment using the Clicked/Opened Step filter.
 
- Select clicked shortened sms link.
 
- Choose the desired Canvas and Canvas step.

## Keyword category-specific retargeting

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), you are also able to create up to 25 of your own keyword categories, allowing you to identify arbitrary keywords and responses. These categories can be used for filtering and retargeting. To read more about Global keyword categories and how to set them up, refer to Keyword processing.

### Filter by recency

Filter for the recency of a user responding to your SMS, MMS, or RCS program. This filter will evaluate the last date a user sent an inbound message that is within one of the keyword categories.

### Filter by campaign or Canvas attribution

Filter for users who have replied to a specific SMS, MMS, or RCS campaign or Canvas component, keyword category, or tag.

#### Filter by replied to a specific campaign with keyword category

#### Filter by replied to a campaign or Canvas with a specific tag

#### Filter by replied to a specific step

### Trigger messages by keyword

Messages can be triggered as users send messages inbound based on keyword categories (user sent any one of the keywords) or other keywords (user sent a keyword that does not fall into one of the existing categories). These triggers are set in the Delivery step of the campaign builder.

When evaluating if an inbound message meets a defined trigger event, the leading and trailing spaces are removed before evaluation begins.

tip

If an action-based Canvas is triggered by an inbound SMS or MMS message, you can reference supported SMS Liquid properties in any Canvas step until the next action path.

#### Trigger by inbound keyword category

#### Trigger by arbitrary keywords

Note when triggering a message on an “Other” keyword response, you have the opportunity to evaluate the keyword body on an exact text match. This match follows the same rules as noted: Only the exact, single-word message is processed (case insensitive). A keyword sent of Hello Braze! would not match the criteria shown in the following example.

#### Template keywords

When triggering a campaign or Canvas component on an inbound SMS or MMS, you can optionally template the text or media attachments that your user sent into the body of your campaign or Canvas with Liquid. This enables you to access the user’s response which you can then include in your reply, apply conditional logic to, or anything else you can do with Liquid.

```

1

```
 | 
```
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.

```
 | 

```

1
2
3
4
5
6
7

```
 | 
```
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}

```
 | 

- 

New Stuff!
