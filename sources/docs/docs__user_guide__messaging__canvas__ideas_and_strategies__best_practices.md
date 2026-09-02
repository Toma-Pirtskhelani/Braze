---
url: https://www.braze.com/docs/user_guide/messaging/canvas/ideas_and_strategies/best_practices
slug: docs__user_guide__messaging__canvas__ideas_and_strategies__best_practices
title: "Canvas best practices"
description: "This article provides some best practices for creating and customizing user journeys with Canvas and Canvas Flow."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Canvas best practices

This article provides some best practices for creating and customizing user journeys with Canvas and Canvas Flow.

## Identify your purpose

Dive into the what, who, and why!

- What are you trying to help the users accomplish?
 
- Who are the users you’re trying to reach?
 
- Why are you building this Canvas?

## Mix and match

Unlock new combinations of user journeys with Canvas components.

- Split your users with Decision Split and build different workflows.
 
- Space out your user journeys with a Delay step.
 
- Add standalone messages anywhere you want in your Canvas flow.

note

Canvas steps can move users only forward in the flow. You cannot configure a Canvas to link a step to a previous step, as this would send users backwards. This validation ensures users progress in a single direction through your Canvas.

## Create richer messages

Reel in your users with richer messages.

- Build in-app messages for onboarding Canvases to make the most out of your first impression.
 
- Introduce Content Cards in a Canvas journey for promotional offers and push notifications.

## Test your user journeys

Determine the impact of your Canvas messaging by incorporating control groups. This way, you can build an understanding of how your Canvas was received!

- Name each step of your Canvas to identify your user journey.
 
- Leverage the Experiment Paths component in your user journey to randomly assign users to different paths you create.
 
- Diversify your user journeys with Delay and Message steps to help uncover what path is most effective.
 
- Check Canvas analytics to see the performance of each component in your user journey.
 
- Edit your Canvas after the initial launch.

## Scheduling your Canvases

note

Canvas will prevent you from using scheduled send with a time that has already passed. However, it’s possible to launch a Canvas during the exact same minute that the campaign is scheduled (or in the seconds before). This can lead to the Canvas missing the scheduled entry time and users not entering the Canvas. We recommend sending Canvases immediately in the event that any campaigns are edited within minutes of the scheduled send time.

important

If you change audience, schedule, or delivery close to a scheduled entry or send window, some users may already be waiting on a step or were evaluated under earlier settings, so not everyone is guaranteed to pick up the change. To see how schedule changes, audience changes, Evaluate at enqueue time, and Message step delivery timing interact, read Change your Canvas after launch. When in doubt, stop the Canvas, duplicate it, and relaunch for a clean re-evaluation.

For Canvas steps, consider the following details when scheduling your Canvas:

- Schedule changes only apply to users who aren’t already waiting to receive the step.
 
- Audience changes by default apply to all users, unless you schedule changes to apply to users who aren’t waiting to receive the step.
 
- Editing a Canvas that is scheduled to deliver as soon as deployed and selecting Update essentially sends it.

### Post-launch edits

If you stop an active Canvas while an unsaved draft exists, stopping can discard that draft. Save, launch, or discard the draft before stopping if you need to keep in-progress edits.

#### Audience evaluation timing

Braze evaluates audiences at different points in the Canvas builder and in individual steps. For setup details, see:

- Set your target entry audience and Determine your Canvas entry schedule when you create a Canvas
 
- How target audience and entry criteria work together
 
- Edit delivery settings for Message steps
 
- How users are evaluated for Audience Paths steps

If you edit a live Canvas close to a scheduled entry or send window, users already enqueued for a Message step may not pick up your changes. For more information, see Edit Canvases after launch.

- 

New Stuff!
