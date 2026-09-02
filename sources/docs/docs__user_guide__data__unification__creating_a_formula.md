---
url: https://www.braze.com/docs/user_guide/data/unification/creating_a_formula
slug: docs__user_guide__data__unification__creating_a_formula
title: "Create a formula"
description: "This reference article covers creating and managing formulas, which help you easily understand complex relationships that exist in your data."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create a formula

When viewing analytics in Braze, you can combine multiple data points to get valuable insights into your user data. These are referred to as formulas. Use formulas to normalize your time series data based on your total number of monthly active users (MAU) and daily active users (DAU).

Formulas help you understand complex relationships that exist in your data. For example, you can compare how many custom events were completed by daily active users that qualify for a particular segment versus the general population (or against another segment).

## Use cases

Formulas, especially when combined with custom events, can help you understand user behaviors within your app. Formulas can also lend deeper insight into segment purchasing patterns, even if your company uses paid media in conjunction with Braze, such as Google Ads or TV.

The following are some examples of the kinds of behavior patterns that can be detected using formulas:

- Ride-sharing apps: If you have a custom event for when the user cancels a ride, you can configure a function for Canceled Rides / DAU to find if certain user segments tend to cancel more rides than others.
 
- eCommerce apps: By configuring a function for purchases of a certain product ID / MAU, you can compare the popularity of a recently promoted product between segments, even if all the promotions couldn’t be tracked using Braze.
 
- Media apps using ads: If the users’ experience is interrupted by ads between video or audio clips, recording mid-ad exits as a custom event and calculating the ratio of mid-ad exits / DAU can help find the best segments to target with a campaign for ad-free premium subscriptions.

## Creating formulas

Formulas can be accessed on the Home, Revenue Report, and Custom events report pages in the dashboard. On Home and Revenue Report, open the Performance Over Time chart, set Statistics For to KPI Formulas, and select at least one formula. On the Custom Events Report page, open Filters, select one or more KPI formula options, and select Apply.

To create a new formula:

- Go to the appropriate dashboard (Home, Revenue Report, or Custom Events Report).
 
- Select Manage KPI Formulas.
 
- Enter a name for your formula.
 
- Select the relevant numerators and denominators.
 
- Select Save.

## Available numerators and denominators

### Overview dashboard

 Numerators | 
 Denominators | 

 DAU | 
 MAU | 

 Sessions | 
 DAU | 

   | 
 Segment size | 

### Revenue dashboard

 Numerators | 
 Denominators | 

 Purchases (all) | 
 DAU | 

 Select purchases (such as a gift card or product ID) | 
 MAU | 

### Custom event dashboard

 Numerators | 
 Denominators | 

 Custom event count | 
 MAU | 

   | 
 DAU | 

   | 
 Segment size (only segments that have analytics tracking enabled can be used) | 

- 

New Stuff!
