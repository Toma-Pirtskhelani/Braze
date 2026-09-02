---
url: https://www.braze.com/docs/user_guide/audience/segments/segment_insights
slug: docs__user_guide__audience__segments__segment_insights
title: "Segment Insights"
description: "This how-to article will walk you through how to use, interpret, and share Segment Insights."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Segment Insights

Learn how to how to use, interpret, and share Segment Insights.

Segment Insights shows you how one segment is performing compared to another across a set of pre-selected KPIs.

## Viewing Segment Insights

Go to the Segment Insights page of your dashboard, under Analytics, and to view up to 10 different segments compared against a baseline.

note

Statistics on the Segment Insights page are estimated by default. To calculate exact values, open a segment and select Calculate Exact Statistics. Estimates can be higher or lower than exact values, especially in large workspaces or for small segments.

The baseline segment can either be a specific segment you select, or a segment containing all of your users. You can compare the following statistics using Segment Insights:

 Measurement | 
 Description | 
 Formula | 

 Sessions per day | 
 Average number of segment users’ sessions per day | 
 (total # of sessions) / (# days since first session) | 

 Days since first session | 
 Average number of days between segment users’ first session and now | 
 today – date of first session | 

 Days since last session | 
 Average number of days between segment users’ last session and now | 
 today – date of last session | 

 Lifetime revenue in dollars | 
 Average lifetime revenue in dollars for segment users | 
 user lifetime spend | 

 Days since first purchase | 
 Average number of days between segment users’ first session and first purchase | 
 date of first purchase – date of first session | 

 Days since last purchase | 
 Average number of days between segment users’ last purchase and now | 
 today – date of last purchase | 

You can easily share specific comparisons with your teammates using the page’s unique URL, and you can also select the eye icon next to each segment to reveal more information about that segment. These comparisons will reset when you switch between workspaces.

## Segment Details page

Segment Insights have also been built right into the Segment Details view. When looking at a particular segment you’ve previously set up, you can find the same six statistics outlined within the dynamic, gray Segment Statistics box. From here, you can quickly launch the Segment Insights tool to compare this particular segment with any others you’ve previously set up, but note that this will overwrite any segments you’ve previously selected within the Segment Insights tool.

note

Segment Insights and the Segment Details page calculate size estimations separately using different user samples and sample sizes, so it’s expected that the numbers may not match.

## Use cases

### Comparing demographic usage and purchasing patterns

One of the best usages of Segment Insights is answering questions about the impact of user demographics on app usage and campaign effectiveness, such as:

- Are certain user demographics performing significantly better or worse than average?
 
- Should I rethink the localization of a particular campaign?
 
- Is a campaign engaging a certain demographic?
 
- What goals should I set for a campaign aimed at a certain demographic?

Segment Insights can help uncover differences between user demographics. The following example shows a comparison of an app’s user base by their language, illustrating how English speakers tend to have higher LTV and activity levels than speakers of other languages.

In this example, German speakers signed up longer ago on average, which might explain why they’re no longer as active. This could be due to a multitude of factor. For example if the app first launched in Europe but is now more popular in the US, where most people speak English or Spanish. For more robust findings, when analyzing KPIs across demographics, it’s sensible to test the findings from a general study of demographics (for example, if language impacts LTV in all users) by looking at a smaller, more similar population and seeing if the findings persist.

To improve conversions among speakers of languages other than English, a good first step would be to localize campaigns to the user’s device language and making sure that the copy of those messages is engaging users by using a multivariate campaign to test different versions of the foreign language copy.

### Understanding indicators of higher revenue

Getting users to convert to purchasers can be difficult, and trying to push new, inactive or disengaged users directly toward purchasing may lead the user to uninstall your app. Segment Insights can help you discover actions that lead users further down the purchase funnel without requiring them to purchase just yet, for example, subscribing to your newsletter, sharing on social media, or signing up for promotional messages. For example, you can chart out the impact on purchases different behaviors within an eCommerce app.

In this case, relatively few users are currently signed up for promotional messages and aren’t as active, but these users generate a higher lifetime revenue. To increase revenue, it may be a good idea to include an invitation to sign up for promotional messages in onboarding campaigns. To re-engage lapsed users, a good plan would be to send out a typical lapsed user campaign and target users who converted with a subsequent campaign to sign up for promotional messages.

- 

New Stuff!
