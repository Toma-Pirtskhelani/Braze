---
url: https://www.braze.com/docs/user_guide/brazeai/item_recommendations/use_case
slug: docs__user_guide__brazeai__item_recommendations__use_case
title: "Use case: Drive content discovery after viewing"
description: "This example shows how a fictional brand uses Braze AI item recommendations to deliver personalized content and product suggestions across key customer moments."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Use case: Drive content discovery after viewing

This example shows how a fictional brand uses Braze AI item recommendations to deliver personalized content and product suggestions across key customer moments. Learn how recommendation logic can improve engagement, increase conversions, and reduce manual effort.

Let’s say Camila is a CRM manager at MovieCanon, a streaming platform featuring curated films and series.

Camila’s goal is to keep viewers engaged after they finish watching something. Historically, MovieCanon’s “You might also like” messages were based on broad genre matching and sent at arbitrary times—often hours or days after a session. Engagement was low, and her team knew they could do better.

Using AI Item Recommendations, Camila sets up a system to automatically recommend new titles based on each viewer’s watching history, delivered immediately after a user finishes a film or episode. It’s a smarter, more personal way to help users discover content they’ll actually want to watch next and keep them engaged with the platform.

This tutorial walks through how Camila:

- A personalized message triggered when a user finishes watching something
 
- Recommendations that are tailored to the viewer’s preferences—automatically pulled from MovieCanon’s catalog and inserted into the message

## Step 1: Create a churn prediction model

Camila starts by creating a recommendation that will surface relevant titles whenever a user finishes watching something. She wants it to be dynamic, so users receive different suggestions based on what they’ve watched recently.

- In the Braze dashboard, Camila navigates to AI Item Recommendations.
 
- She creates a new recommendation and names it “Post-viewing suggestions”.
 
- For the recommendation type she chooses AI Personalized, so each user sees tailored recommendations based on past behaviors.
 
- She selects Do not recommend items users have previously interacted with so users don’t get recommendations for something they’ve already watched.
 
- She selects the catalog containing MovieCanon’s current content library. Camila doesn’t add a catalog selection, since she wants all items in the catalog to be eligible items for recommendation.
 
- Camila links the recommendation to the Watched Content custom event, which tracks completed views, and sets the Property Name to the content’s title.
 
- She creates the recommendation.

## Step 2: Set up an in-app message

After the recommendation has finished training, Camila builds a messaging flow that reaches the user at the right moment: immediately after they finish a title. The message includes a list of three personalized suggestions pulled directly from the catalog.

- Camila creates an in-app message campaign using the drag-and-drop editor.
 
- She sets the trigger to her custom event: Watched Content.
 
- She designs a multi-page in-app message with title images, names, and a “Watch now” CTA.

- In the message body, Camila uses the Add Personalization modal to add variables like the recommended title’s name, description, and thumbnail using Liquid, which dynamically populates content from the catalog. She templates in a custom attribute for Last Watched Movie to let users know this recommendation is based on their watch history.

Show Liquid used in image

```

1

```
 | 
```
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}

```
 | 

```

1

```
 | 
```
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}

```
 | 

```

1

```
 | 
```
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}

```
 | 

- Camila then duplicates her page and increments the Liquid array ({{ items[0]}} to {{items[1]}}) in each variable to template in the next item in the recommendation list.

## Step 3: Measure and optimize

With the campaign live, Camila monitors open rates, CTRs, and follow-up viewing behavior. She compares performance against previous static recommendation campaigns and sees higher engagement—and more content sessions per user.

She also plans to A/B test:

- Timing (immediate versus 10 minutes post-watch)
 
- Content layout (carousel versus list)
 
- CTA variations (“Watch now” versus “Add to queue”)

By pairing event-driven messaging with AI Item Recommendations, Camila turns content discovery into an automatic, personalized experience. MovieCanon keeps users engaged without guesswork—delivering relevant content at just the right time to drive session depth and reduce churn.

- 

New Stuff!
