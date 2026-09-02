---
url: https://www.braze.com/docs/user_guide/channels/content_cards/create_a_content_card/card_creation
slug: docs__user_guide__channels__content_cards__create_a_content_card__card_creation
title: "Card creation"
description: "This article describes the differences between Content Card creation at campaign launch or Canvas step entry versus at first impression."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Card creation

You can choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns and Canvas steps by specifying when the card is created.

## Prerequisites

To take advantage of this feature, you must upgrade to the following minimum SDK versions:

   iOS Objective-C: 4.5.0+     Swift: 5.2.0+     Web: 4.2.0+     Android: 23.0.0+  

On iOS, the Swift SDK supports this feature starting with version 5.2.0, and the legacy Objective-C SDK supports it starting with version 4.5.0. Swift SDK versions 5.0.0 through 5.1.x don’t support it.

After upgrading the SDK, your mobile users must upgrade their app. You can filter your campaign or Canvas audience to only target users on these minimum app versions.

## Overview

- campaign
 
- canvas

You can choose when Braze creates a card on the Delivery step when creating a new Content Card campaign with scheduled delivery.

The following options are available:

- At campaign launch: The previous default behavior for Content Cards. Braze calculates audience eligibility and personalization when the campaign launches, then creates the card and stores it until the user opens your app.
 
- At first impression (recommended): When the user next opens your app (starts a new session), Braze determines which Content Cards the user is eligible for, templates any personalization like Liquid or Connected Content, then creates the card. This option usually delivers better performance.

Regardless of your selected option, the Content Card expiration date countdown begins when the campaign launches.

You can choose when Braze creates a card on the Messaging Channels tab of a Content Card Message step.

The following options are available:

- At step entry: The previous default behavior for Content Cards. Braze calculates audience eligibility when the user enters the Canvas step, then creates the card and stores it until the user opens your app.
 
- At first impression (recommended): Braze calculates audience eligibility when the user enters the Canvas step. When the user next opens your app (starts a new session), Braze templates any personalization like Liquid or Connected Content, then creates the card. This option delivers better performance in card deliveries and more up-to-date personalization.

Regardless of your selected option, the Content Card expiration date countdown begins when the user enters the Canvas step.

tip

If you want anonymous users to see a Content Card in their very first session, use a campaign instead of a Canvas. This is because when an anonymous user enters a Canvas, their session has already started, so they won’t get the Content Card until they start a new session.

### Removal event

Select the option to remove Content Cards when users complete a purchase or perform a custom event. To use Perform Custom Event as the removal event, select context variables or custom attributes for comparisons when using property filters.

### Expiration

In the Expiration (Time in Feed) settings, you can select Personalize duration to set the expiration of the Content Card using context variables.

important

Content Cards have a maximum expiration of 30 days, even when using personalized duration with context variables. Any value set beyond 30 days is capped at 30 days. For more details, refer to Card expiration.

note

For both options, after a card is created, Braze does not recalculate audience eligibility or personalization.

### Differences between creating cards at launch or entry versus at first impression

This section describes the main differences between card creation at campaign launch or step entry versus at first impression.

 Differences between creating cards at launch or entry versus at first impression

 | 
 When campaign is launched / At Canvas step entry | 
 At first impression | 

 When to use this | 
 If you need content to be snapshot at a specific time (the launch time). | 
 
- If you need to display cards to new or anonymous users who may enter the segment after launch (campaigns only*).
- If you're using personalization and want the latest content to be available on the card. | 

 Audience | 
 Braze evaluates audience membership when the campaign sends.

New or anonymous users will not be evaluated for eligibility if they try to view the card after the campaign sends. For recurring campaigns, this will be at the next recurrence interval. | 
 Braze evaluates membership when the user next opens your app (starts a session, campaigns only*).

 This setting will have a wider audience reach because any new or anonymous users will always be evaluated for eligibility when they try to view the card. 

Additionally, rate limiting (limiting the number of people who will receive the card) is not applicable when set to at first impression. | 

 Personalization | 
 Braze evaluates Liquid, Connected Content, and Content Blocks at the time the campaign is launched or when a user enters the Canvas step. For recurring campaigns, this will be at the next recurrence interval. | 
 Braze evaluates Liquid, Connected Content, and Content Blocks at the time of first impression or after the next recurrence interval. | 

 Analytics | 
 Messages Sent refers to the number of cards Braze created and made available. This doesn't count whether users viewed the card. | 
 Messages Sent refers to the number of cards Braze sends to a user after a session start. In Canvas, if a user enters the step without starting a session, Braze doesn't send a card, so this metric may not align with the number of users entering a step.

While reachable users and impressions don't change, expect lower send volume (Messages Sent) when you create a card at first impression compared to campaign launch or Canvas step entry. | 

 Processing time | 
 Braze creates cards for every eligible user in the segment at launch time. For large audiences, select At First Impression so cards are available more quickly after launch. | 
 Braze creates a card the first time a user tries to view it, so it may take 1-2 seconds to display on the first impression. | 

* This scenario only applies to campaigns, as Canvas audience is evaluated at Canvas entry, not at the step level.

## Considerations

### Multichannel campaigns

Multichannel campaigns do not support at-first impression cards, so all Content Cards are sent at campaign launch.

### Use Canvas context properties

When personalizing Content Cards with Canvas context properties, use the ${...} syntax (for example, {{context.${property_name}}}). Dot notation without the syntax (for example, {{context.property_name}}) may not resolve correctly in Content Cards, even if it works in other channels like push and email.

### Change card creation after launch

Braze recommends not changing how cards are created after a campaign has launched. Due to the differences in how Messages Sent is calculated between the two card creation types, changing how cards are created after the campaign has launched can affect the accuracy of your send volume.

### Potential processing time

For large audiences, select the option to create cards at first impression so cards are available quickly after launch. Campaigns triggered on session start may also benefit from moving to create at first impression (available through scheduled delivery) to improve performance.

When cards are created at first impression, it may take a few seconds for the cards to process. The length of this processing time depends on various factors, such as the card size and the complexity of the message templating options. For example, the processing time for cards using Connected Content is at least as long as the Connected Content response time.

### Previous SDK versions

If a user’s app runs a previous SDK version, they still receive Content Cards you send. However, cards take longer to appear and may not show until the next Content Card sync.

- 

New Stuff!
