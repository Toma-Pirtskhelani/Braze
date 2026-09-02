---
url: https://www.braze.com/docs/user_guide/messaging/ab_testing/create_tests
slug: docs__user_guide__messaging__ab_testing__create_tests
title: "Create multivariate and A/B tests"
description: "This article explains how to create multivariate and A/B tests with Braze."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create multivariate and A/B tests

You can create a multivariate or A/B test for any campaign that targets a single channel. For example, if you want to use multivariate or A/B testing for a push campaign, you can target iOS and Android devices in the same campaign.

## Step 1: Create your campaign

- Go to Messaging > Campaigns.
 
- Select Create campaign and a channel for the campaign from the section that allows multivariate and A/B testing. For detailed documentation on each messaging channel, refer to Create a campaign.

## Step 2: Compose your variants

You can create up to eight variants of your message, differentiating between titles, content, images, and more. The number of differences between the messages determines whether this is a multivariate or A/B test. An A/B test examines the effect of changing one variable, whereas a multivariate test examines two or more.

For some ideas on how to get started differentiating your variants, refer to Tips for different channels.

## Step 3: Schedule your campaign

Scheduling your multivariate campaign works the same as scheduling any other Braze campaign. All standard delivery types are available.

After a multivariate test begins, you can’t make changes to the campaign. If you change the parameters, such as the subject line or HTML body, Braze considers the experiment compromised and immediately disables the experiment.

To automatically optimize your variants, see Optimizing A/B tests with BrazeAI. Single-send and multi-send campaigns use different optimization methods and requirements.

## Step 4: Choose a segment and distribute your users across variants

Select segments to target, then distribute the members across your selected variants and the optional control group. For best practices around choosing a segment to test with, see Choosing a segment.

For supported campaigns, turn on Optimize with BrazeAI™ to automatically optimize your variant distribution. For a single-send campaign, Braze reserves part of the audience for an optimized second send. For a multi-send campaign, BrazeAI™ adjusts the distribution over time.

### Control group

You can reserve a percentage of your target audience for a randomized control group. Users in the control group don’t receive the test, but Braze monitors their conversion rate for the duration of the campaign.

When viewing your results, you can compare the conversion rates of your variants against a baseline conversion rate provided by your control group. This lets you compare both the effects of your variants and the effects of your variants against the conversion rate that would result if you didn’t send a message at all.

important

Using a control group when determining a winner by Opens or Clicks is not recommended. Because the control group won’t receive the message, those users cannot perform any opens or clicks. Therefore, that group’s conversion rate is 0% by definition and does not constitute a meaningful comparison to the variants.

#### Control groups and A/B testing

When using rate limiting with an A/B test, the rate limit isn’t applied to the control group in the same way as the test group, which is a potential source of time bias. Use appropriate conversion windows to avoid this bias.

#### Control groups with Optimize with BrazeAI™

For a multi-send campaign with Optimize with BrazeAI™, the initial control-group size depends on the number of variants. If each variant receives more than 20% of users, the control group starts at 20%, and the variants split the remaining 80% evenly. With more variants, the control group starts smaller. As BrazeAI™ analyzes performance, the control group may grow or shrink.

## Step 5: Designate a conversion event (optional)

Setting a conversion event for a campaign allows you to see how many recipients of that campaign performed a particular action after receiving it.

This only affects the test if you chose Primary Conversion Rate in the previous steps. For more information, refer to Conversion events.

## Step 6: Review and launch

On the confirmation page, review the details of your multivariate campaign and launch the test! Next, learn how to understand your test results.

## Things to know

If your experiment has already started sending and you edit the message, the experiment becomes invalidated, and any experiment results are removed.

- To prevent any interference with the expected experiment behavior, we recommend avoiding message edits within an hour of the experiment campaign launch.
 
- If your experiment is completed and you edit the message post-send, the experiment results remain available in your dashboard analytics. However, if you relaunch the campaign, the experiment results are removed.

### Tips for different channels

Depending on which channel you select, you can test different components of your message. For example, you can try to compose variants with an idea of what you want to test and what you hope to prove. What levers do you have to pull, and what are the desired effects? While there are millions of possibilities that you can investigate using a multivariate and A/B test, we have some suggestions to get you started:

 Channel | 
 Aspects of message you can change | 
 Results to look for | 

 Push | 
 Copy 
 Image and Emoji Usage 
 Deep Links 
 Presentation of numbers (for example, “triple” versus “increase by 200%”) 
 Presentation of time (for example, “ends at midnight” versus “ends in 6 hours”) | 
 Opens 
 Conversion Rate | 

 Email | 
 Subject 
 Display Name 
 Salutation 
 Body Copy 
 Image and Emoji Usage 
 Presentation of numbers (for example, “triple” versus “increase by 200%”) 
 Presentation of time (for example, “ends at midnight” versus “ends in 6 hours”) | 
 Opens 
 Conversion Rate | 

 In-app message | 
 Aspects listed for “push” 
 In-app message image specifications | 
 Click 
 Conversion Rate | 

tip

When running A/B tests, don’t forget to generate funnel reports that let you understand how each variant impacted your conversion funnel, especially if “conversion” for your business involves taking multiple steps or actions.

In addition, the ideal length of your test may also vary depending on the channel. Keep in mind the average amount of time most users may need to engage with each channel.

For instance, if you’re testing a push, you may achieve significant results faster than when testing email, since users see pushes immediately, but it may be days before they see or open an email. If you’re testing in-app messages, keep in mind that users must open the app to see the campaign, so you should wait longer to collect results from both your most active app openers as well as your more typical users.

If you’re unsure how long your test should run, Optimize with BrazeAI™ can automatically configure and run the optimization.

### Choosing a segment

Since different segments of your users may respond differently to messaging, the success of a particular message says something about both the message itself and its target segment. Therefore, try to design a test with your target segment in mind.

For instance, while active users may have equal response rates to “This deal expires tomorrow!” and “This deal expires in 24 hours!”, users who haven’t opened the app for a week may be more responsive toward the latter wording since it creates a greater sense of urgency.

Additionally, when choosing which segment to run your test on, be sure to consider whether the size of that segment is large enough for your test. In general, multivariate and A/B tests with more variants require a larger test group to achieve statistically significant results. This is because more variants result in fewer users seeing each individual variant.

tip

As a guide, you likely need around 15,000 users per variant (including the control) to achieve 95% confidence in your test results. However, the exact number of users you need could be higher or lower than that, depending on your particular case. For more exact guidance on variant sample sizes, consider referring to a sample size calculator.

### Bias and randomization

A common question with control and test group assignments is whether they can introduce bias to your testing. Others sometimes wonder how we know if these assignments are truly random.

Users are assigned to message variants, Canvas variants, or their respective control groups by concatenating their (randomly generated) user ID with the (randomly generated) campaign or Canvas ID, taking the modulus of that value with 100, and then ordering users into slices that correspond to the percentage assignments for variants and optional control chosen in the dashboard. So, there’s no practical way that users’ behaviors before creating a particular campaign or Canvas could vary systematically between variants and control. It is also not practical to be any more random (or more accurately, pseudo-random) than this implementation.

#### Mistakes to avoid

There are some common mistakes to avoid creating the appearance of differences based on the messaging channel if audiences are not filtered correctly.

For example, if you send a push message to a wide audience with a control, the test group sends messages only to users with a push token. However, the control group includes both users who do have a push token and users who don’t. In this case, your initial audience for the campaign or Canvas must filter for having a push token (Foreground Push Enabled is true). The same must be done for eligibility to receive messages on other channels: opted in, has a push token, or subscribed.

Note that if a control variant doesn’t consist of any Canvas steps, exit criteria events aren’t logged for users in the control variant.

note

If you manually use random bucket numbers for control groups, check out things to watch for in your control groups.

- 

New Stuff!
